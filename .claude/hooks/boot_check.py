#!/usr/bin/env python3
"""
SessionStart hook: what a session must know before it does anything.

Prints a short block into the session's context, one line per item and only
when something is due:
  - whether the locks are intact (scoreboard/lock.sha256);
  - loop entries still owed: a `unit` or `begin` with no later `loop` for its ref;
  - another live session in this repo (log/.live/, written by session_live.py);
  - memory that is not committed (an uncommitted log is not a log);
  - the boot read path against its budget;
  - a deeper pass due, and why (units, a recurring correction class, a new
    escape, a measure worse than baseline);
  - self-changes due a verdict, and verdicts overdue past their cap;
  - the score snapshot (log/scores/) stale or broken, or more merged PRs than units;
  - instruction channels changed since log/env.sha256 (memory, settings, model);
  - what is waiting on Andres, aged from each item's first date;
  - playbook trials addressed to this system that it has not taken up.

Usage: as a SessionStart hook (payload on stdin), or by hand:
  python3 .claude/hooks/boot_check.py < /dev/null
  python3 .claude/hooks/boot_check.py --write-env [--model <id>]   # record instruction channels

Every item here exists because the thing it checks was once left to someone
remembering, and was forgotten. This file is locked.
"""

import datetime as dt
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

# --- per-system configuration ------------------------------------------------
SYSTEM = "meta-architecture"
BOOT_BUDGET = 1000                         # lines; the kernel's overhead ceiling
MEMORY = ["log/", "HANDOFF.md", "lessons/", "trials.md", "playbook.md", "meta/", "systems.md", "CHANGELOG.md"]
TRIALS = "trials.md"   # relative to repo root
STATE = "HANDOFF.md"
CHANGELOG = "CHANGELOG.md"
# Score snapshot lines read "  S2     now 2.1 (n=9)   baseline 2.82 (n=22)  <note>".
DIRECTIONS = {}                         # meta snapshots are not parsed for triggers
ESCAPES = None
DEEP_UNITS, RECUR_DAYS, SNAPSHOT_DAYS, LIVE_HOURS, CAP_DAYS = 10, 30, 7, 6, 30
# -----------------------------------------------------------------------------

EVENT = re.compile(r"^- (\d{4}-\d{2}-\d{2})(?:[ T](\d{1,2}:\d{2}))?\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s?(.*)$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
ENTRY = re.compile(r"^## (C-\d+)")
CLAIM = re.compile(r"<!--\s*claim:\s*(.+?);\s*landed:\s*(\d{4}-\d{2}-\d{2})")
EXTENDED = re.compile(r"extended to (\d{4}-\d{2}-\d{2})")
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
    listed = [l.split(None, 1)[1].strip() for l in spec.splitlines()
              if l.strip() and not l.startswith("#")] + ["scoreboard/lock.sha256"]
    dirty = [l[3:] for l in sh(["git", "status", "--porcelain", "--"] + listed, root).splitlines() if l.strip()]
    if dirty:
        return ("LOCKED FILES CHANGED, NOT COMMITTED: " + ", ".join(dirty) +
                ". Hashes match, but only a relock should touch these. Ask Andres whose edit it is.")
    return f"Locks intact ({n} files)."


def events(root):
    """Every event line in log order (files by name, lines as appended)."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "log", "events-*.md"))):
        for line in (read(path) or "").splitlines():
            m = EVENT.match(line)
            if m:
                out.append({"date": dt.date.fromisoformat(m.group(1)), "time": m.group(2),
                            "type": m.group(3).strip().lower(), "ref": m.group(4).strip(), "text": m.group(5)})
    return out


def correction_class(e):
    head = e["text"].split("·", 1)[0].strip()
    return head if "·" in e["text"] and SLUG.match(head) else None


def owed_loops(root, kinds=("unit", "begin")):
    """A unit (or begin) is owed until a LATER loop event with the same ref."""
    owed = {}
    for e in events(root):
        if e["type"] in kinds:
            if e["type"] == "unit" or owed.get(e["ref"], ("begin",))[0] == "begin":
                owed[e["ref"]] = (e["type"], e["date"])
        elif e["type"] == "loop":
            owed.pop(e["ref"], None)
    return [f"{ref} ({d}{', begun, no unit yet' if k == 'begin' else ''})" for ref, (k, d) in owed.items()]


def live_sessions(root, sid):
    """Other sessions whose log/.live marker is under LIVE_HOURS old."""
    out = []
    d = os.path.join(root, "log", ".live")
    for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if name == sid or name.startswith("."):
            continue
        m = re.search(r"started (\S+)", read(os.path.join(d, name)) or "")
        try:
            started = dt.datetime.fromisoformat(m.group(1))
        except Exception:
            continue
        if dt.timedelta(0) <= dt.datetime.now() - started < dt.timedelta(hours=LIVE_HOURS):
            out.append(started)
    return sorted(out)


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


def changelog(root):
    text = read(os.path.join(root, CHANGELOG)) or ""
    out, cur = [], None
    for line in text.splitlines():
        m = ENTRY.match(line)
        if m:
            cur = {"id": m.group(1)}
            out.append(cur)
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
            cur["verdict"] = line.split("**Verdict:**", 1)[1].strip()
    return out


def due_changes(root, today=None):
    """(due, overdue): open changes 14+ days old, and open changes past their cap."""
    today = today or dt.date.today()
    due, overdue = [], []
    for ch in changelog(root):
        v = ch.get("verdict", "").lower()
        if not v.startswith("open") or "landed" not in ch:
            continue
        ext = EXTENDED.search(v)
        cap = dt.date.fromisoformat(ext.group(1)) if ext else ch["landed"] + dt.timedelta(days=CAP_DAYS)
        if today > cap:
            overdue.append(f"{ch['id']} (cap {cap})")
        elif (today - ch["landed"]).days >= 14:
            due.append(ch["id"])
    return due, overdue


def snapshots(root):
    """[(date, text)] of log/scores/YYYY-MM-DD.txt, oldest first."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "log", "scores", "*.txt"))):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
        if m:
            out.append((dt.date.fromisoformat(m.group(1)), read(path) or ""))
    return out


def measures(text):
    """{measure: (now, baseline)} from a score.py --summary snapshot; values may be None."""
    out = {}
    for m in re.finditer(r"^\s*(\w+)\s+now\s+(\S+)\s+\(n=[^)]*\)\s+baseline\s+(\S+)", text, re.M):
        def num(x):
            try:
                return float(x)
            except ValueError:
                return None
        out[m.group(1)] = (num(m.group(2)), num(m.group(3)))
    return out


def escape_count(text):
    line = next((l for l in text.splitlines() if re.match(rf"^\s*{ESCAPES}\s+now\b", l)), "")
    m = re.search(r"(\d+)\s+escape", line)
    if m:
        return int(m.group(1))
    now = measures(line).get(ESCAPES, (None, None))[0]
    return 1 if now else 0


def deep_pass_due(evs, snaps):
    """Reasons a deeper pass is due since the last `deep pass` event."""
    idx, last = -1, None
    for i, e in enumerate(evs):
        if e["type"] == "deep pass" or e["ref"].lower() == "deep pass":
            idx, last = i, e["date"]
    since = evs[idx + 1:]
    why = []
    units = sum(1 for e in since if e["type"] == "unit")
    if units >= DEEP_UNITS:
        why.append(f"{units} units since the last deep pass")
    corr = [(i, e) for i, e in enumerate(evs) if e["type"] == "correction" and correction_class(e)]
    rec = {}
    for i, e in corr:
        if i <= idx:
            continue
        c = correction_class(e)
        if any(correction_class(o) == c and j < i and 0 <= (e["date"] - o["date"]).days <= RECUR_DAYS for j, o in corr):
            rec[c] = e["date"]
    for c, d in rec.items():
        why.append(f"correction class '{c}' recurred within {RECUR_DAYS} days ({d})")
    if snaps and (last is None or snaps[-1][0] > last):
        day, text = snaps[-1]
        seen = [t for d, t in snaps if last and d <= last]
        before = escape_count(seen[-1]) if seen else 0
        if escape_count(text) > before:
            why.append(f"new escape in the {day} score snapshot ({escape_count(text)}, was {before})")
        worse = [f"{k} {now} vs {base}" for k, (now, base) in measures(text).items()
                 if DIRECTIONS.get(k) and now is not None and base is not None
                 and (now > base if DIRECTIONS[k] == "down" else now < base)]
        if worse:
            why.append(f"worse than baseline in the {day} snapshot: {', '.join(worse)}")
    return why, last


def snapshot_issues(evs, snaps, today):
    if not snaps:
        return [f"No score snapshot yet: save one with `python3 scoreboard/score.py --summary > log/scores/{today}.txt`."]
    out = []
    day, text = snaps[-1]
    if (today - day).days > SNAPSHOT_DAYS:
        out.append(f"Score snapshot is {(today - day).days} days old ({day}): save a new one with "
                   f"`python3 scoreboard/score.py --summary > log/scores/{today}.txt`.")
    bad = sorted({w.lower() for w in re.findall(r"no data|error|traceback", text, re.I)})
    if bad:
        out.append(f"Score snapshot {day} shows {', '.join(repr(b) for b in bad)}: an instrument may be broken; "
                   "check score.py before trusting any verdict.")
    w = re.search(r"\((\d{4}-\d{2}-\d{2})\.\.(\d{4}-\d{2}-\d{2})\)", text)
    m = re.search(r"(\d+)\s+team\s+PRs?\s+merged", text)
    if w and m:
        a, b = dt.date.fromisoformat(w.group(1)), dt.date.fromisoformat(w.group(2))
        units = sum(1 for e in evs if e["type"] == "unit" and a <= e["date"] <= b)
        if int(m.group(1)) > units:
            out.append(f"Snapshot {day}: {m.group(1)} merged team PRs in {a}..{b} but {units} `unit` events: "
                       "units may be going unlogged.")
    return out


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def channels(root, model=None):
    """{name: sha256} of every channel that can change how a session behaves outside this repo."""
    home = os.path.expanduser("~")
    out = {}
    keys = {re.sub(r"[^A-Za-z0-9]", "-", p) for p in (root, os.path.realpath(root))}
    for key in sorted(keys):
        for f in sorted(glob.glob(os.path.join(home, ".claude", "projects", key, "memory", "*"))):
            if os.path.isfile(f):
                out[f"memory/{os.path.basename(f)}"] = _sha(open(f, "rb").read())
    for name, path in ((".claude/settings.local.json", os.path.join(root, ".claude", "settings.local.json")),
                       ("~/.claude/settings.json", os.path.join(home, ".claude", "settings.json")),
                       ("~/.claude/CLAUDE.md", os.path.join(home, ".claude", "CLAUDE.md"))):
        if os.path.isfile(path):
            out[name] = _sha(open(path, "rb").read())
    if model:
        out[f"model:{model}"] = _sha(model.encode())
    return out


def recorded_channels(root):
    text = read(os.path.join(root, "log", "env.sha256"))
    if text is None:
        return None
    return dict(reversed(l.split(None, 1)) for l in text.splitlines() if l.strip() and not l.startswith("#"))


def channel_changes(root, model):
    old = recorded_channels(root)
    if old is None:
        return None
    new = channels(root, model)
    if not model:      # no model in this payload: do not report it as removed
        new.update({k: v for k, v in old.items() if k.startswith("model:")})
    changed = sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k) and not k.startswith("model:"))
    was = [k[6:] for k in old if k.startswith("model:")]
    now = [k[6:] for k in new if k.startswith("model:")]
    if sorted(was) != sorted(now):
        changed.append(f"model {', '.join(was) or '(none)'} -> {', '.join(now) or '(none)'}")
    return changed


def write_env(root, model):
    old = recorded_channels(root) or {}
    if not model:
        model = next((k[6:] for k in old if k.startswith("model:")), None)
    new = channels(root, model)
    os.makedirs(os.path.join(root, "log"), exist_ok=True)
    with open(os.path.join(root, "log", "env.sha256"), "w", encoding="utf-8") as f:
        f.write(f"# Instruction channels outside this repo, hashed {dt.date.today()} by boot_check.py --write-env.\n")
        f.write("# When one changes, the boot check says so; write an `env` event, then re-run --write-env.\n")
        for k, v in sorted(new.items()):
            f.write(f"{v}  {k}\n")
    print(f"log/env.sha256: {len(new)} channels recorded. Commit it with the `env` event.")


def model_of(payload):
    m = payload.get("model")
    if isinstance(m, dict):
        m = m.get("id") or m.get("display_name")
    return str(m) if m else None


WAIT = re.compile(r"^## Waiting on Andres(?::\s*(system|work))?\s*\n(.*?)(?=^## |\Z)", re.S | re.M)
FULL_DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def waiting(root):
    """Items waiting on Andres, split by kind.

    system: proposals, escalated self-changes, broken locks; what the design is about.
    work:   merges, approvals, product or security calls; the outside-world gates.
    An old unsplit "## Waiting on Andres" section counts as work.
    """
    text = read(os.path.join(root, STATE)) or ""
    out = {"system": [], "work": []}
    for m in WAIT.finditer(text):
        out[m.group(1) or "work"] += [l for l in m.group(2).splitlines() if l.startswith(("- ", "* "))]
    return out


def freshness(items, today, days=14):
    """Work items aged from their FIRST date (not the latest re-check), with re-check counts."""
    stale, undated = [], 0
    for item in items:
        dates = FULL_DATE.findall(item)
        if not dates:
            undated += 1
            continue
        first = dt.date.fromisoformat(dates[0])
        if (today - first).days > days:
            stale.append((first, len(re.findall(r"re-?checked", item, re.I))))
    return sorted(stale), undated


def proposals(root):
    """Open charter/scoreboard proposals (log/pending/S-NNN.md) for Andres."""
    d = os.path.join(root, "log", "pending")
    out, kinds = [], {}
    for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not re.match(r"S-\d+\.md$", name):
            continue
        text = read(os.path.join(d, name)) or ""
        if not re.search(r"^- \*\*Status:\*\*\s*open", text, re.M):
            continue
        kind = (re.search(r"^- \*\*Kind:\*\*\s*(\w+)", text, re.M) or [None, "?"])[1]
        kinds[kind] = kinds.get(kind, 0) + 1
        title = re.sub(r"^S-\d+\s*·\s*", "", text.splitlines()[0].lstrip("# ").strip()) if text else name
        out.append(f"{name[:-3]} ({kind}): {title}")
    over = [k for k, n in kinds.items() if n > 1]
    return out, over


def trials(root):
    text = read(os.path.normpath(os.path.join(root, TRIALS)))
    if not text:
        return []
    taken = read(os.path.join(root, CHANGELOG)) or ""
    out = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        tid = block.split()[0]
        if re.search(rf"^- \*\*To:\*\*.*\b{re.escape(SYSTEM)}\b", block, re.M) and \
           re.search(r"^- \*\*Status:\*\*\s*open", block, re.M) and tid not in taken:
            out.append(tid)
    return out


def main():
    if "--write-env" in sys.argv:
        root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
        model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv[:-1] else None
        return write_env(root, model)
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    today = dt.date.today()
    evs = events(root)
    lines = [f"## Boot check — {SYSTEM} — {today}", locks(root)]

    owed = owed_loops(root)
    if owed:
        lines.append("Loop entries owed (run docs/loop.md for each before new work): " + ", ".join(owed))
    live = live_sessions(root, str(payload.get("session_id") or ""))
    if live:
        lines.append(f"Another session is active in this repo since {', '.join(f'{t:%H:%M}' for t in live)}; "
                     "re-read state files right before writing them.")
    dirty = uncommitted(root)
    if dirty:
        lines.append(f"Uncommitted memory ({len(dirty)}): " + ", ".join(dirty[:8]) +
                     (" …" if len(dirty) > 8 else "") + " — commit it.")
    total, missing = boot_lines(root)
    over = " OVER BUDGET — compacting is owed." if total > BOOT_BUDGET else ""
    lines.append(f"Boot read path: {total}/{BOOT_BUDGET} lines.{over}" +
                 (f" Missing: {', '.join(missing)}" if missing else ""))
    snaps = snapshots(root)
    why, last = deep_pass_due(evs, snaps)
    if why:
        lines.append(f"Deeper pass due (last: {last or 'never'}): " + "; ".join(why) + ". Run /evolve.")
    due, overdue = due_changes(root, today)
    if due:
        lines.append("Self-changes due a verdict (run `python3 scoreboard/verdicts.py`): " + ", ".join(due))
    if overdue:
        lines.append("Verdicts OVERDUE, past their cap (judge them now with `python3 scoreboard/verdicts.py`): " +
                     ", ".join(overdue))
    lines += snapshot_issues(evs, snaps, today)
    model = model_of(payload)
    changed = channel_changes(root, model)
    if changed is None:
        lines.append("Instruction channels not recorded: run `python3 .claude/hooks/boot_check.py --write-env" +
                     (f" --model {model}" if model else "") + "` and commit log/env.sha256.")
    elif changed:
        lines.append("Instruction channels changed: " + ", ".join(changed[:6]) + (" …" if len(changed) > 6 else "") +
                     ". Write an `env` event saying what changed, then run `python3 .claude/hooks/boot_check.py "
                     "--write-env" + (f" --model {model}" if model else "") + "` and commit log/env.sha256.")
    w = waiting(root)
    if w["system"]:
        lines.append(f"Waiting on Andres, system: {len(w['system'])}. Lead with these when he arrives.")
    if w["work"]:
        stale, undated = freshness(w["work"], today)
        msg = f"Waiting on Andres, work: {len(w['work'])}"
        if stale:
            msg += (f"; {len(stale)} older than 14 days from first raised (" +
                    ", ".join(f"{d}, re-checked {n}x" for d, n in stale[:5]) + (" …" if len(stale) > 5 else "") +
                    "), re-check them (docs/loop.md § Keeping work items fresh)")
        if undated:
            msg += f"; {undated} undated, date them"
        lines.append(msg + ".")
    props, over = proposals(root)
    if props:
        lines.append("Proposals for Andres (he approves with `scoreboard/apply S-NNN` in his terminal): " + "; ".join(props))
    if over:
        lines.append("More than one open proposal for: " + ", ".join(over) + ". Keep one per kind; withdraw the weaker.")
    t = trials(root)
    if t:
        lines.append("Playbook trials addressed here, not yet taken up: " + ", ".join(t) +
                     " (see " + TRIALS + ").")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
