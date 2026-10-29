#!/usr/bin/env python3
"""
The crew's record: who was spawned, for what, whether it mattered, and how the
change-reviewer's decisions held up.

Reads, from log/:
  spawns-*.md   one line per subagent spawn, written by .claude/hooks/spawn_log.py
                    - 2026-10-30 14:02 | spawn | 1a2b3c4d | reviewer | Review PR 4443
  events-*.md   `agent` events, written by the session in the loop:
                    - 2026-10-30 14:30 | agent | <unit ref> | <name> · changed|confirmed|unused|wrong · <line>
                    changed    its output changed the outcome (caught a blocker, found the cause)
                    confirmed  it confirmed what the session already believed
                    unused     its output was not used
                    wrong      its output was wrong and had to be corrected
                `reviewed` events, one per change-reviewer decision:
                    - 2026-10-30 15:00 | reviewed | C-004 | LAND · <one line>
                `correction` events with a class (for --corrections):
                    - 2026-10-30 16:00 | correction | <ref> | <class-slug> · <what he caught, where we should have>
and CHANGELOG.md: entries whose Reviewer line said LAND and whose Verdict says
reverted count against the reviewer.

Every agent defined in .claude/agents/ is listed, including the ones never
spawned. Undefined subagent types or names seen at least 3 times are listed as
"repeated ad hoc role; consider defining it". This is evidence for the evolver's
standing question, "would we define this one today, given its record?". It
reports; it never recommends a change.

Usage: python3 tools/crew_report.py [--since YYYY-MM-DD] [--until YYYY-MM-DD] [--corrections]
"""

import argparse
import datetime as dt
import glob
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2})(?:[ T]\d{1,2}:\d{2})?\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s?(.*)$")
EFFECTS = ["changed", "confirmed", "unused", "wrong"]
DECISIONS = ["LAND", "ESCALATE", "REJECT"]
# Built-in generic types: spawned for anything, so their count says nothing about a missing role.
GENERIC = {"general-purpose", "fork", "claude", "explore", "plan", "claude-code-guide", "statusline-setup"}
AD_HOC_MIN = 3
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def lines(pattern, since, until):
    for path in sorted(glob.glob(os.path.join(ROOT, "log", pattern))):
        for raw in open(path, encoding="utf-8", errors="replace"):
            m = LINE.match(raw.strip())
            if m:
                day = dt.date.fromisoformat(m.group(1))
                if since <= day <= until:
                    yield day, m.group(2).strip().lower(), m.group(3).strip(), m.group(4).strip()


def changelog_reverts():
    """C-NNN entries the reviewer landed that were later reverted, with the verdict text."""
    text = ""
    try:
        text = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
    except OSError:
        pass
    out = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        cid = block.split()[0]
        if not cid.startswith("C-"):
            continue
        rev = re.search(r"^- \*\*Reviewer:\*\*\s*(.*)$", block, re.M)
        ver = re.search(r"^- \*\*Verdict:\*\*\s*(.*)$", block, re.M)
        if rev and ver and "LAND" in rev.group(1) and ver.group(1).lower().startswith("reverted"):
            out.append((cid, ver.group(1)[:90]))
    return out


def corrections(since, until):
    rows = [(d, ref, text) for d, kind, ref, text in lines("events-*.md", since, until) if kind == "correction"]
    by = defaultdict(list)
    unclassed = 0
    for d, ref, text in rows:
        head = text.split("·", 1)[0].strip()
        if "·" in text and SLUG.match(head):
            by[head].append((d, ref))
        else:
            unclassed += 1
    print(f"Correction classes {since} .. {until}  ({len(rows)} correction events, {unclassed} without a class)")
    for c, items in sorted(by.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        dates = sorted(d for d, _ in items)
        recur = any((b - a).days <= 30 for a, b in zip(dates, dates[1:]))
        print(f"  {c:<32}{len(items):>3}  {', '.join(str(d) for d in dates[-4:])}"
              f"{'  RECURRED within 30 days' if recur else ''}")
    if not rows:
        print("  No `correction` events in this window.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2000-01-01")
    ap.add_argument("--until", default="2999-12-31")
    ap.add_argument("--corrections", action="store_true", help="correction classes and their recurrence")
    a = ap.parse_args()
    since, until = dt.date.fromisoformat(a.since), dt.date.fromisoformat(a.until)
    if a.corrections:
        return corrections(since, until)

    spawns = defaultdict(lambda: {"n": 0, "sessions": set(), "last": None})
    for d, kind, sid, rest in lines("spawns-*.md", since, until):
        if kind != "spawn":
            continue
        typ = rest.split("|", 1)[0].strip() or "?"
        s = spawns[typ]
        s["n"] += 1
        s["sessions"].add(sid)
        s["last"] = max(s["last"] or d, d)

    rec = defaultdict(lambda: {e: 0 for e in EFFECTS} | {"logged": 0, "last": None, "units": set()})
    reviewed = defaultdict(int)
    reviewed_rows = []
    for d, kind, ref, text in lines("events-*.md", since, until):
        if kind == "agent":
            parts = [p.strip() for p in text.split("·")]
            r = rec[parts[0] or "?"]
            r["logged"] += 1
            r["units"].add(ref)
            effect = parts[1].lower() if len(parts) > 1 else ""
            if effect in EFFECTS:
                r[effect] += 1
            r["last"] = max(r["last"] or d, d)
        elif kind == "reviewed":
            dec = text.split("·", 1)[0].strip().upper()
            reviewed[dec if dec in DECISIONS else "?"] += 1
            reviewed_rows.append((d, ref, text[:80]))

    adir = os.path.join(ROOT, ".claude", "agents")
    defined = sorted(f[:-3] for f in os.listdir(adir) if f.endswith(".md")) if os.path.isdir(adir) else []

    print(f"Crew record {a.since} .. {a.until}")
    print(f"{'agent':<26}{'spawned':>8}{'logged':>8}{'units':>7}{'changed':>9}{'confirmed':>11}{'unused':>8}"
          f"{'wrong':>7}  last")
    for agent in sorted(set(defined) | set(rec) | set(spawns), key=lambda x: (x not in defined, x.lower())):
        s, r = spawns.get(agent), rec.get(agent)
        tag = "" if agent in defined else "  (ad hoc)" if agent.lower() not in GENERIC else "  (built-in)"
        if not s and not r:
            print(f"{agent:<26}{0:>8}{0:>8}{0:>7}{0:>9}{0:>11}{0:>8}{0:>7}  never spawned in this window")
            continue
        r = r or {e: 0 for e in EFFECTS} | {"logged": 0, "last": None, "units": set()}
        last = max(x for x in ((s or {}).get("last"), r["last"]) if x)
        print(f"{agent:<26}{(s or {}).get('n', 0):>8}{r['logged']:>8}{len(r['units']):>7}{r['changed']:>9}"
              f"{r['confirmed']:>11}{r['unused']:>8}{r['wrong']:>7}  {last}{tag}")
    if not spawns:
        print("No spawn lines in this window (log/spawns-*.md is written by .claude/hooks/spawn_log.py).")
    if not rec:
        print("No `agent` events in this window. The record starts once units log them (docs/loop.md).")
    unlogged = sum(s["n"] for k, s in spawns.items()) - sum(r["logged"] for r in rec.values())
    if spawns and unlogged > 0:
        print(f"{unlogged} spawn(s) have no `agent` event: their effect is unrecorded.")

    counts = defaultdict(int)
    for k, s in spawns.items():
        counts[k] += s["n"]
    for k, r in rec.items():
        counts[k] = max(counts[k], r["logged"])
    for k, n in sorted(counts.items()):
        if k not in defined and k.lower() not in GENERIC and n >= AD_HOC_MIN:
            print(f"{k}: spawned {n} times, not defined in .claude/agents/: repeated ad hoc role; consider defining it.")

    print()
    total = sum(reviewed.values())
    print(f"change-reviewer: {total} decision(s) logged as `reviewed` events: " +
          ", ".join(f"{k} {reviewed[k]}" for k in DECISIONS + ["?"] if reviewed.get(k)) if total else
          "change-reviewer: no `reviewed` events in this window.")
    for cid, verdict in changelog_reverts():
        worse = "worse" in verdict.lower()
        print(f"  {cid}: it said LAND; later {verdict}{'  (counts against it)' if worse else ''}")
    rejects = [row for row in reviewed_rows if row[2].upper().startswith("REJECT")]
    for d, ref, text in rejects[-5:]:
        print(f"  rejected {ref} on {d}: {text}")


if __name__ == "__main__":
    main()
