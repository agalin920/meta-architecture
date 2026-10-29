#!/usr/bin/env python3
"""
Stop hook: a session does not end with the loop owed, memory uncommitted, or
the event log edited.

Steps scheduled for "the end" are the ones that get dropped; one side project
measured seven instances across four mechanisms. So the end is enforced here.
The stop is blocked once, with the reason, when:
  - a finished `unit` has no later `loop` entry (an open `begin` is left to the
    boot check: this hook fires at the end of every turn, mid-work included);
  - memory is uncommitted;
  - a line was removed from an append-only log (log/events-*, log/spawns-*,
    any other log/*.md), against the HEAD this session started from;
  - an event line this session added has an unknown type or no time.
The second attempt is let through (stop_hook_active) so a session can never be
trapped, and the boot check reports whatever is still owed. This file is locked.
"""

import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from boot_check import EVENT, owed_loops, read, uncommitted  # noqa: E402

KNOWN = {"begin", "unit", "loop", "correction", "escalation", "change", "reviewed", "verdict", "revert", "lesson",
         "decision", "trial", "agent", "env", "knowledge", "state", "finding", "review", "deep pass"}


def git(root, *args):
    try:
        return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=20).stdout
    except Exception:
        return ""


def session_base(root, sid):
    m = re.search(r"^head ([0-9a-f]{7,40})", read(os.path.join(root, "log", ".live", sid)) or "", re.M) if sid else None
    return m.group(1) if m else "HEAD"


def log_diff(root, base):
    """(removed, added) lines of the append-only logs, working tree against `base`."""
    out = git(root, "diff", "--no-color", "-U0", base, "--", "log/*.md", ":(exclude)log/pending/**",
              ":(exclude)log/scores/**")
    removed, added, f = [], [], ""
    for line in out.splitlines():
        if line.startswith("+++ "):
            f = line[6:] if line.startswith("+++ b/") else ""
        elif line.startswith("-") and not line.startswith("--- "):
            removed.append(line[1:])
        elif line.startswith("+") and f:
            added.append((f, line[1:]))
    for f in git(root, "ls-files", "--others", "--exclude-standard", "--", "log/*.md").splitlines():
        if f.startswith(("log/pending/", "log/scores/")):
            continue
        added += [(f, l) for l in (read(os.path.join(root, f)) or "").splitlines()]
    return removed, added


def malformed(added):
    bad = []
    for f, line in added:
        if not os.path.basename(f).startswith("events-") or not line.startswith("- "):
            continue
        m = EVENT.match(line)
        if not m:
            bad.append(f"unparseable: {line[:60]}")
        elif m.group(3).strip().lower() not in KNOWN:
            bad.append(f"unknown type '{m.group(3).strip()}': {line[:60]}")
        elif not m.group(2):
            bad.append(f"no time: {line[:60]}")
    return bad


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    if payload.get("stop_hook_active"):
        sys.exit(0)
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    problems = []
    owed = owed_loops(root, kinds=("unit",))
    if owed:
        problems.append("The loop is owed for: " + ", ".join(owed) +
                        ". Run docs/loop.md for each, then write its `loop` event.")
    base = session_base(root, str(payload.get("session_id") or ""))
    removed, added = log_diff(root, base)
    if removed:
        problems.append(f"{len(removed)} line(s) were removed from the log since {base[:9]}, and the log is "
                        f"append-only (first: {removed[0][:70]!r}). Restore them (`git -C {root} diff {base[:9]} -- log/` "
                        "shows them); to correct an event, append a new one.")
    bad = malformed(added)
    if bad:
        problems.append(f"{len(bad)} event line(s) written this session need fixing (`- YYYY-MM-DD HH:MM | <type> | "
                        "<ref> | <text>`, types in docs/loop.md § Events): " + "; ".join(bad[:4]))
    dirty = uncommitted(root)
    if dirty:
        problems.append(f"{len(dirty)} memory file(s) are uncommitted ({', '.join(dirty[:6])}). "
                        "Commit them with a `memory:` commit; an uncommitted log is not a log.")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
