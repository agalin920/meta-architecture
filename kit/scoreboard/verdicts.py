#!/usr/bin/env python3
"""
Rollback: judge every self-change whose window has closed.

Each self-change in CHANGELOG.md carries a machine line:
    <!-- claim: S2 down; landed: 2026-10-29; commit: abc1234 -->
and a human line:
    - **Verdict:** open

A change's window closes at the later of 14 days or 5 merged team PRs after it
landed, and never later than 30 days. Then the named score over the window is
compared with the same-length window before the change:

    helped     moved in the claimed direction        -> keep; playbook candidate
    worse      moved the other way                   -> revert
    no effect  did not move, or there is no data     -> revert

Maintenance changes claim `maintenance none` and are never judged on score.
S1 (escapes) cannot be a claim: it only counts PRs merged 30+ days ago, so no
14-30 day window can ever see it move. Claim a leading measure; S1 is watched
by the escape tripwire in docs/loop.md instead.
This script only reports; the loop applies the verdict (git revert of the one
commit, confirmed by the change-reviewer) and records it. It is locked: a
system cannot soften its own rollback.

Usage: python3 scoreboard/verdicts.py [--all]
"""

import argparse
import datetime as dt
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score  # noqa: E402  (per-system: compute(since, until) and merged_prs(since, until))

MIN_DAYS, MIN_PRS, MAX_DAYS = 14, 5, 30
ENTRY = re.compile(r"^## (C-\d+)\s*·?\s*(.*)$")
CLAIM = re.compile(r"<!--\s*claim:\s*(\S+)\s+(up|down|none)\s*;\s*landed:\s*(\d{4}-\d{2}-\d{2})(?:\s*;\s*commit:\s*([0-9a-f]+))?")
VERDICT = re.compile(r"\*\*Verdict:\*\*\s*(.+)$")


def changes(path):
    out, cur = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = ENTRY.match(line)
            if m:
                cur = {"id": m.group(1), "title": m.group(2).strip()}
                out.append(cur)
                continue
            if line.startswith("## "):   # any other heading ends the entry
                cur = None
                continue
            if cur is None:
                continue
            c = CLAIM.search(line)
            if c:
                cur.update(measure=c.group(1), direction=c.group(2),
                           landed=dt.date.fromisoformat(c.group(3)), commit=c.group(4))
            v = VERDICT.search(line)
            if v:
                cur["verdict"] = v.group(1).strip()
    return out


def commit_of(ch):
    """The entry's commit, or the `evolve(C-NNN)` commit found by its subject."""
    if ch.get("commit"):
        return ch["commit"]
    out = subprocess.run(["git", "log", "--format=%h", "--grep", f"^evolve({ch['id']})"],
                         capture_output=True, text=True).stdout.split()
    return out[0] if out else "<commit not found>"


def window_end(ch, today):
    floor = ch["landed"] + dt.timedelta(days=MIN_DAYS)
    cap = ch["landed"] + dt.timedelta(days=MAX_DAYS)
    if today < floor:
        return None
    if score.merged_prs(ch["landed"], today) >= MIN_PRS or today >= cap:
        return min(today, cap)
    return None


def judge(ch, end):
    span = end - ch["landed"]
    start = ch["landed"] - span
    # A measure whose instrument changed (e.g. S3/S4 from 2026-10-29) is only
    # compared against data from the same instrument.
    floor = getattr(score, "INSTRUMENT_SINCE", {}).get(ch["measure"])
    if floor and start < floor:
        start = floor
        if (ch["landed"] - start).days < 7:
            return "too early", f"fewer than 7 days of {ch['measure']} before the change on the current instrument"
    before = score.compute(start, ch["landed"]).get(ch["measure"], {})
    after = score.compute(ch["landed"], end).get(ch["measure"], {})
    b, a = before.get("value"), after.get("value")
    if a is None or b is None:
        return "no effect", f"no data (before={b}, after={a})"
    if a == b:
        return "no effect", f"{ch['measure']} {b} -> {a}"
    better = a < b if ch["direction"] == "down" else a > b
    return ("helped" if better else "worse"), f"{ch['measure']} {b} -> {a} (claimed {ch['direction']})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="list every change, not only due ones")
    args = ap.parse_args()
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    today = dt.date.today()
    due = 0
    for ch in changes(os.path.join(root, "CHANGELOG.md")):
        if not str(ch.get("verdict", "")).lower().startswith("open"):
            if args.all:
                print(f"{ch['id']}: {ch.get('verdict', '?')}")
            continue
        if "measure" not in ch:
            print(f"{ch['id']}: OPEN but has no claim line; fix the entry")
            continue
        if ch["measure"] == "S1":
            print(f"{ch['id']}: claims S1, which no window can judge; re-claim a leading measure")
            continue
        if ch["direction"] == "none":
            print(f"{ch['id']}: maintenance; close it as 'kept (maintenance)'")
            continue
        end = window_end(ch, today)
        if end is None:
            if args.all:
                print(f"{ch['id']}: window still open (landed {ch['landed']})")
            continue
        due += 1
        verdict, why = judge(ch, end)
        if verdict == "too early":
            print(f"{ch['id']}: TOO EARLY — {why} — leave it open and re-judge later")
            continue
        action = "keep; add to lessons.md as a playbook candidate" if verdict == "helped" \
            else f"revert: git revert {commit_of(ch)}  (confirm with change-reviewer first)"
        print(f"{ch['id']}: {verdict.upper()} — {why} — window {ch['landed']}..{end} — {action}")
    if not due and not args.all:
        print("No self-change is due a verdict.")


if __name__ == "__main__":
    main()
