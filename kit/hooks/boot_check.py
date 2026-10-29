#!/usr/bin/env python3
"""
SessionStart hook: what a session must know before it does anything.

Prints a short block into the session's context:
  - whether the locks are intact (scoreboard/lock.sha256);
  - loop entries still owed for finished units of work;
  - memory that is not committed (an uncommitted log is not a log);
  - the boot read path against its budget;
  - self-changes whose verdict window has closed;
  - what is waiting on Andres;
  - DNA trials addressed to this system that it has not taken up.

Every item here exists because the thing it checks was once left to someone
remembering, and was forgotten. This file is locked.
"""

import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys

# --- per-system configuration ------------------------------------------------
SYSTEM = "SYSTEM-NAME"
BOOT_BUDGET = 1000                         # lines; the kernel's overhead ceiling
MEMORY = ["log/", "state.md", "knowledge/", "lessons.md", "CHANGELOG.md", "tickets/"]
DNA_TRIALS = "../../meta-architecture/dna/trials.md"   # relative to repo root
# -----------------------------------------------------------------------------

EVENT = re.compile(r"^- (\d{4}-\d{2}-\d{2})[^|]*\|\s*(\w[\w-]*)\s*\|\s*([^|]+?)\s*\|")
ENTRY = re.compile(r"^## (C-\d+)")
CLAIM = re.compile(r"<!--\s*claim:\s*(.+?);\s*landed:\s*(\d{4}-\d{2}-\d{2})")
VERDICT = re.compile(r"\*\*Verdict:\*\*\s*(\w[\w -]*)")


def sh(args, root):
    try:
        return subprocess.run(args, cwd=root, capture_output=True, text=True, timeout=20).stdout
    except Exception:
        return ""


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def locks(root):
    spec = read(os.path.join(root, "scoreboard/lock.sha256"))
    if spec is None:
        return "LOCK BROKEN: scoreboard/lock.sha256 is missing"
    bad = []
    n = 0
    for line in spec.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, path = line.split(None, 1)
        n += 1
        data = None
        try:
            with open(os.path.join(root, path.strip()), "rb") as f:
                data = f.read()
        except OSError:
            pass
        if data is None or hashlib.sha256(data).hexdigest() != digest:
            bad.append(path.strip())
    if bad:
        return ("LOCK BROKEN: " + ", ".join(bad) +
                " changed outside Andres's relock. Tell Andres before anything else.")
    return f"Locks intact ({n} files)."


def owed_loops(root):
    units, loops = {}, set()
    logdir = os.path.join(root, "log")
    for name in sorted(os.listdir(logdir)) if os.path.isdir(logdir) else []:
        if not name.startswith("events-"):
            continue
        for line in (read(os.path.join(logdir, name)) or "").splitlines():
            m = EVENT.match(line)
            if not m:
                continue
            kind, ref = m.group(2), m.group(3)
            if kind == "unit":
                units[ref] = m.group(1)
            elif kind == "loop":
                loops.add(ref)
    return [f"{ref} ({d})" for ref, d in units.items() if ref not in loops]


def uncommitted(root):
    out = sh(["git", "status", "--porcelain", "--"] + MEMORY, root)
    return [l[3:] for l in out.splitlines() if l.strip()]


def boot_lines(root):
    listing = read(os.path.join(root, ".claude/boot-path.txt")) or ""
    total, missing = 0, []
    for p in listing.splitlines():
        p = p.split("#")[0].strip()
        if not p:
            continue
        text = read(os.path.join(root, p))
        if text is None:
            missing.append(p)
        else:
            total += text.count("\n")
    return total, missing


def due_changes(root):
    text = read(os.path.join(root, "CHANGELOG.md")) or ""
    today = dt.date.today()
    due, cur = [], None
    for line in text.splitlines():
        m = ENTRY.match(line)
        if m:
            cur = {"id": m.group(1)}
            continue
        if line.startswith("## "):   # any other heading ends the entry
            cur = None
            continue
        if cur is None:
            continue
        c = CLAIM.search(line)
        if c:
            cur["landed"] = dt.date.fromisoformat(c.group(2))
        v = VERDICT.search(line)
        if v:
            cur["verdict"] = v.group(1).strip().lower()
            if cur["verdict"].startswith("open") and "landed" in cur and (today - cur["landed"]).days >= 14:
                due.append(cur["id"])
    return due


def waiting(root):
    text = read(os.path.join(root, "state.md")) or ""
    m = re.search(r"^## Waiting on Andres\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return 0
    return sum(1 for l in m.group(1).splitlines() if l.startswith(("- ", "* ")))


def trials(root):
    text = read(os.path.normpath(os.path.join(root, DNA_TRIALS)))
    if not text:
        return []
    taken = read(os.path.join(root, "CHANGELOG.md")) or ""
    out = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        tid = block.split()[0]
        if re.search(rf"^- \*\*To:\*\*.*\b{re.escape(SYSTEM)}\b", block, re.M) and \
           re.search(r"^- \*\*Status:\*\*\s*open", block, re.M) and tid not in taken:
            out.append(tid)
    return out


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    lines = [f"## Boot check — {SYSTEM} — {dt.date.today()}", locks(root)]

    owed = owed_loops(root)
    if owed:
        lines.append("Loop entries owed (run docs/loop.md for each before new work): " + ", ".join(owed))
    dirty = uncommitted(root)
    if dirty:
        lines.append(f"Uncommitted memory ({len(dirty)}): " + ", ".join(dirty[:8]) +
                     (" …" if len(dirty) > 8 else "") + " — commit it.")
    total, missing = boot_lines(root)
    over = " OVER BUDGET — compacting is owed." if total > BOOT_BUDGET else ""
    lines.append(f"Boot read path: {total}/{BOOT_BUDGET} lines.{over}" +
                 (f" Missing: {', '.join(missing)}" if missing else ""))
    due = due_changes(root)
    if due:
        lines.append("Self-changes due a verdict (run `python3 scoreboard/verdicts.py`): " + ", ".join(due))
    w = waiting(root)
    if w:
        lines.append(f"Waiting on Andres: {w} item(s) in current state. Mention them when he arrives.")
    t = trials(root)
    if t:
        lines.append("DNA trials addressed here, not yet taken up: " + ", ".join(t) +
                     " (see " + DNA_TRIALS + ").")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
