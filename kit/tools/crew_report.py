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
                `reviewed` events, one per change-reviewer opinion (LAND, CONCERN, ESCALATE;
                REJECT only before 2026-10-29):
                    - 2026-10-30 15:00 | reviewed | C-004 | LAND · <notes>
                    - 2026-10-30 15:05 | reviewed | C-005 | CONCERN · <its point> · landed anyway because <why>
                `correction` events with a class (for --corrections):
                    - 2026-10-30 16:00 | correction | <ref> | <class-slug> · <what he caught, where we should have>
                Corrections are learning evidence, not a score: S3 counts Andres's
                follow-ups from the raw prompt log and GitHub, never these events.
and CHANGELOG.md: changes the reviewer LANDed that were later reverted for harm
count against it; changes it raised a CONCERN on that were later reverted for
harm count for it. A revert for "no effect" (the rule before 2026-10-29) is not harm.

Skills: every skill in .claude/skills/, and any loaded from elsewhere, with how
often the model loaded it (`skill` lines in spawns-*.md, from the same hook):
                    - 2026-10-30 14:05 | skill | 1a2b3c4d | run-tests

Commands: every command in .claude/commands/, with how often Andres typed it
(`command` lines in spawns-*.md, from the hook on UserPromptExpansion):
                    - 2026-10-30 14:00 | command | 1a2b3c4d | take-ticket
Kinds of work: `unit` events start with a kind (`<kind> · <outcome>`): a command's
name or a short slug. A kind seen on 3 distinct refs within 30 days with no
command or skill of that name is flagged as recurring freehand work.

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
import subprocess
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2})(?:[ T]\d{1,2}:\d{2})?\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s?(.*)$")
EFFECTS = ["changed", "confirmed", "unused", "wrong"]
DECISIONS = ["LAND", "CONCERN", "ESCALATE", "REJECT"]   # REJECT: only in events before 2026-10-29
# Built-in generic types: spawned for anything, so their count says nothing about a missing role.
GENERIC = {"general-purpose", "fork", "claude", "explore", "plan", "claude-code-guide", "statusline-setup"}
AD_HOC_MIN = 3
KIND_MIN, KIND_DAYS = 3, 30   # units of one kind within that many days, no command or skill: recurring freehand work
PRUNE_DAYS = 60               # defined and unused this long: the deeper pass cuts it or says why it stays
SINCE, UNTIL = dt.date(2000, 1, 1), dt.date(2999, 12, 31)
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def lines(pattern, since, until):
    for path in sorted(glob.glob(os.path.join(ROOT, "log", pattern))):
        for raw in open(path, encoding="utf-8", errors="replace"):
            m = LINE.match(raw.strip())
            if m:
                day = dt.date.fromisoformat(m.group(1))
                if since <= day <= until:
                    yield day, m.group(2).strip().lower(), m.group(3).strip(), m.group(4).strip()


def reviewer_record():
    """(C-NNN, reviewer's word, verdict, scored) for entries whose outcome bears on the reviewer.
    scored is "against" (it said LAND; reverted for harm), "for" (it said CONCERN; reverted for harm), or ""."""
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
        if not (rev and ver):
            continue
        word = next((d for d in DECISIONS if rev.group(1).upper().startswith(d)), "LAND" if "LAND" in rev.group(1) else "?")
        v = ver.group(1).lower()
        harm = v.startswith("reverted") and "no effect" not in v
        if harm or (word == "CONCERN" and v.startswith(("helped", "looks worse"))):
            scored = ("against" if word == "LAND" else "for" if word == "CONCERN" else "") if harm else ""
            out.append((cid, word, ver.group(1)[:90], scored))
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


def skills():
    """Each skill in .claude/skills/, and each skill loaded from elsewhere (user or plugin),
    with how often the model loaded it. A slash command typed by Andres is not a load."""
    sdir = os.path.join(ROOT, ".claude", "skills")
    defined = sorted(d for d in os.listdir(sdir) if os.path.isfile(os.path.join(sdir, d, "SKILL.md"))) \
        if os.path.isdir(sdir) else []
    loads = defaultdict(lambda: {"n": 0, "sessions": set(), "last": None})
    for d, kind, sid, rest in lines("spawns-*.md", SINCE, UNTIL):
        if kind != "skill":
            continue
        s = loads[rest.split("|", 1)[0].strip() or "?"]
        s["n"] += 1
        s["sessions"].add(sid)
        s["last"] = max(s["last"] or d, d)
    print()
    print(f"{'skill':<40}{'loaded':>8}{'sessions':>10}  last")
    for name in sorted(set(defined) | set(loads), key=lambda x: (x not in defined, x.lower())):
        s = loads.get(name)
        tag = "" if name in defined else "  (user or plugin)"
        if not s:
            print(f"{name:<40}{0:>8}{0:>10}  never loaded in this window")
            continue
        print(f"{name:<40}{s['n']:>8}{len(s['sessions']):>10}  {s['last']}{tag}")
    if not defined and not loads:
        print("No skills defined in .claude/skills/ and none loaded in this window.")
    elif not loads:
        print("No skill lines in this window (written by .claude/hooks/spawn_log.py, matcher Skill).")
    return set(defined) | set(loads)


def commands():
    """Each command in .claude/commands/, and each typed command or skill defined elsewhere, with
    how often Andres typed it (`command` lines in spawns-*.md, from the UserPromptExpansion hook)."""
    cdir = os.path.join(ROOT, ".claude", "commands")
    defined = sorted(f[:-3] for f in os.listdir(cdir) if f.endswith(".md")) if os.path.isdir(cdir) else []
    typed = defaultdict(lambda: {"n": 0, "last": None})
    for d, kind, sid, rest in lines("spawns-*.md", SINCE, UNTIL):
        if kind == "command":
            t = typed[rest.split("|", 1)[0].strip().lstrip("/") or "?"]
            t["n"] += 1
            t["last"] = max(t["last"] or d, d)
    print()
    print(f"{'command':<40}{'typed':>8}  last")
    for name in sorted(set(defined) | set(typed), key=lambda x: (x not in defined, x.lower())):
        t = typed.get(name)
        tag = "" if name in defined else "  (skill, plugin or built-in)"
        print(f"{name:<40}{t['n']:>8}  {t['last']}{tag}" if t else f"{name:<40}{0:>8}  never typed in this window")
    if not typed:
        print("No command lines in this window (written by .claude/hooks/spawn_log.py on UserPromptExpansion).")
    return set(defined) | set(typed)


def kinds(capabilities):
    """Kinds of work, from `unit` events (`<kind> · <outcome>`). A kind seen on KIND_MIN distinct refs
    (pieces of work, not revisions of one) within KIND_DAYS days, with no command or skill of that
    name, is work the system keeps doing freehand."""
    by = defaultdict(dict)   # kind -> {ref: first date}
    units = defaultdict(int)
    unkinded = 0
    for d, kind, ref, text in lines("events-*.md", SINCE, UNTIL):
        if kind != "unit":
            continue
        head = text.split("·", 1)[0].strip()
        if "·" in text and SLUG.match(head):
            by[head][ref] = min(by[head].get(ref, d), d)
            units[head] += 1
        else:
            unkinded += 1
    print()
    print(f"Kinds of work: {sum(units.values())} unit(s) with a kind, {unkinded} without")
    print(f"  {'kind':<36}{'pieces':>7}{'units':>7}  last")
    for k, refs in sorted(by.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        backed = k in capabilities
        print(f"  {k:<36}{len(refs):>7}{units[k]:>7}  {max(refs.values())}{'' if backed else '  (no command or skill)'}")
    for k, refs in sorted(by.items()):
        ds = sorted(refs.values())
        recur = any((ds[i + KIND_MIN - 1] - ds[i]).days <= KIND_DAYS for i in range(len(ds) - KIND_MIN + 1))
        if k not in capabilities and recur:
            print(f"{k}: {KIND_MIN}+ pieces of work within {KIND_DAYS} days with no command or skill behind it: "
                  "recurring work; consider one.")


def prune(today=None):
    """Agents, skills and commands defined here more than PRUNE_DAYS ago and not used in the last
    PRUNE_DAYS: spawned or logged (agents), loaded (skills), typed (commands). Reads all of the log,
    whatever the window. The change-reviewer is locked and never listed."""
    today = today or dt.date.today()
    last, logged_since = {}, {}   # logged_since: the first day each kind of use was logged at all
    for d, kind, sid, rest in lines("spawns-*.md", dt.date(2000, 1, 1), today):
        name = rest.split("|", 1)[0].strip().lstrip("/")
        key = {"spawn": "agent", "skill": "skill", "command": "command"}.get(kind)
        if key:
            last[(key, name)] = max(last.get((key, name), d), d)
            logged_since[key] = min(logged_since.get(key, d), d)
    for d, kind, ref, text in lines("events-*.md", dt.date(2000, 1, 1), today):
        if kind == "agent":
            name = text.split("·", 1)[0].strip()
            last[("agent", name)] = max(last.get(("agent", name), d), d)
    found = [("agent", f[:-3], f".claude/agents/{f}") for f in sorted(os.listdir(os.path.join(ROOT, ".claude", "agents")))
             if f.endswith(".md") and f != "change-reviewer.md"] if os.path.isdir(os.path.join(ROOT, ".claude", "agents")) else []
    sdir = os.path.join(ROOT, ".claude", "skills")
    found += [("skill", d, f".claude/skills/{d}/SKILL.md") for d in sorted(os.listdir(sdir))
              if os.path.isfile(os.path.join(sdir, d, "SKILL.md"))] if os.path.isdir(sdir) else []
    cdir = os.path.join(ROOT, ".claude", "commands")
    found += [("command", f[:-3], f".claude/commands/{f}") for f in sorted(os.listdir(cdir))
              if f.endswith(".md")] if os.path.isdir(cdir) else []
    out = []
    for key, name, path in found:
        added = subprocess.run(["git", "-C", ROOT, "log", "--diff-filter=A", "--follow", "--format=%cs", "--", path],
                               capture_output=True, text=True).stdout.split()
        born = dt.date.fromisoformat(added[-1]) if added else today
        if key not in logged_since:
            continue                  # this kind of use was never logged here: no evidence either way
        born = max(born, logged_since[key])   # use before logging began is unknown, not absent
        # /x is one capability whether Andres types it or the model loads it: take the later use.
        uses = [last.get((k, name)) for k in ((key,) if key == "agent" else ("skill", "command"))]
        used = max((u for u in uses if u), default=None)
        if (today - born).days > PRUNE_DAYS and (not used or (today - used).days > PRUNE_DAYS):
            out.append(f"  {key} {name}: tracked since {born}, last used {used or 'never'}")
    print()
    if out:
        print(f"Prune candidates (defined and unused for {PRUNE_DAYS}+ days): cut each, or record why it stays "
              f"(docs/loop.md § Agents, skills and commands)")
        print("\n".join(out))
    else:
        print(f"Prune candidates: none (nothing defined and unused for {PRUNE_DAYS}+ days).")


def main():
    global SINCE, UNTIL
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2000-01-01")
    ap.add_argument("--until", default="2999-12-31")
    ap.add_argument("--corrections", action="store_true", help="correction classes and their recurrence")
    a = ap.parse_args()
    since, until = dt.date.fromisoformat(a.since), dt.date.fromisoformat(a.until)
    SINCE, UNTIL = since, until
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

    caps = skills() | commands()   # defined here, or loaded or typed from a user or plugin skill
    kinds(caps)
    print()
    total = sum(reviewed.values())
    print(f"change-reviewer: {total} decision(s) logged as `reviewed` events: " +
          ", ".join(f"{k} {reviewed[k]}" for k in DECISIONS + ["?"] if reviewed.get(k)) if total else
          "change-reviewer: no `reviewed` events in this window.")
    for cid, word, verdict, scored in reviewer_record():
        note = {"against": "  (counts against it)", "for": "  (its concern proved right: counts for it)"}.get(scored, "")
        print(f"  {cid}: it said {word}; later {verdict}{note}")
    concerns = [row for row in reviewed_rows if row[2].upper().startswith(("CONCERN", "REJECT"))]
    for d, ref, text in concerns[-5:]:
        print(f"  {ref} on {d}: {text}")
    prune()


if __name__ == "__main__":
    main()
