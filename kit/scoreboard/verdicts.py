#!/usr/bin/env python3
"""
Rollback: judge every self-change whose window has closed.

Each self-change in CHANGELOG.md carries a machine line:
    <!-- claim: S2 down; landed: 2026-10-29; commit: abc1234 -->
    <!-- claim: maintenance none; landed: 2026-10-29; commit: abc1234; files: tools/x.sh,docs/y.md -->
and a human line:
    - **Verdict:** open

A change's window closes at the later of 14 days or 5 merged team PRs after it
landed, and never later than 30 days. Then the named score over the window is
compared with the same-length window before the change, and `n` is printed for
both:

    insufficient data  either window has n < 5      -> keep open; the window extends,
                                                        up to a 60-day hard cap, then
                                                        it is judged on what there is
    helped     moved >= 10% in the claimed direction -> keep; playbook candidate
    worse      moved >= 10% the other way            -> revert; lesson `retired`
    no effect  moved less than 10% either way        -> revert; lesson "no measured
                                                        effect" (retryable, not retired)

Lack of data is never "no effect". Other changes claiming the same measure in an
overlapping window are listed: the credit (or blame) is shared. Kept changes
over 60 days old are listed once for a re-read on the longer window, flagged if
the measure has turned worse since.

Maintenance changes claim `maintenance none` and are never judged on score.
They list the files they touched; a behaviour file among them (CLAUDE.md,
docs/, .claude/commands, .claude/agents) gets a note for the reviewer.
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
import score  # noqa: E402  (per-system: compute(since, until) -> {measure: {value, n}}, merged_prs(since, until))

MIN_DAYS, MIN_PRS, MAX_DAYS, HARD_CAP, MIN_N, MIN_REL, REREAD_DAYS = 14, 5, 30, 60, 5, 0.10, 60
BEHAVIOUR = ("CLAUDE.md", "docs/", ".claude/commands", ".claude/agents")
ENTRY = re.compile(r"^## (C-\d+)\s*·?\s*(.*)$")
CLAIM = re.compile(r"<!--\s*claim:\s*(\S+)\s+(up|down|none)\s*;\s*landed:\s*(\d{4}-\d{2}-\d{2})(.*?)-->")
VERDICT = re.compile(r"\*\*Verdict:\*\*\s*(.+)$")
EXTENDED = re.compile(r"extended to (\d{4}-\d{2}-\d{2})")


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
                rest = c.group(4)
                commit = re.search(r"commit:\s*([0-9a-f]+)", rest)
                files = re.search(r"files:\s*([^;]+)", rest)
                cur.update(measure=c.group(1), direction=c.group(2), landed=dt.date.fromisoformat(c.group(3)),
                           commit=commit.group(1) if commit else None,
                           files=[x.strip() for x in files.group(1).split(",") if x.strip()] if files else None)
            v = VERDICT.search(line)
            if v:
                cur["verdict"] = v.group(1).strip()
            if re.match(r"^- \*\*Reviewer:\*\*", line):
                cur["reviewer"] = line.split("**Reviewer:**", 1)[1].strip()
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


def compare(measure, direction, b, a):
    """helped / worse / no effect on a relative change of at least MIN_REL."""
    if a == b:
        return "no effect", 0.0
    if b == 0:
        rel = float("inf")
    else:
        rel = (a - b) / abs(b)
    toward = -rel if direction == "down" else rel
    if toward >= MIN_REL:
        return "helped", rel
    if toward <= -MIN_REL:
        return "worse", rel
    return "no effect", rel


def measure_at(ch, start, end):
    before = score.compute(start, ch["landed"]).get(ch["measure"], {})
    after = score.compute(ch["landed"], end).get(ch["measure"], {})
    return before, after


def judge(ch, end, today):
    """(verdict, why). Extends the window when either side has n < MIN_N."""
    floor = getattr(score, "INSTRUMENT_SINCE", {}).get(ch["measure"])
    hard = ch["landed"] + dt.timedelta(days=HARD_CAP)
    while True:
        span = end - ch["landed"]
        start = ch["landed"] - span
        # A measure whose instrument changed is only compared against data from the same instrument.
        if floor and start < floor:
            start = floor
            if (ch["landed"] - start).days < 7:
                return "too early", f"fewer than 7 days of {ch['measure']} before the change on the current instrument"
        before, after = measure_at(ch, start, end)
        b, a = before.get("value"), after.get("value")
        nb, na = before.get("n") or 0, after.get("n") or 0
        nums = f"{ch['measure']} {b} (n={nb}) -> {a} (n={na}), window {start}..{ch['landed']}..{end}"
        if (nb < MIN_N or na < MIN_N or a is None or b is None) and end < min(today, hard):
            end = min(today, hard)      # extend, then look again
            continue
        if nb < MIN_N or na < MIN_N or a is None or b is None:
            if end < hard:
                return "insufficient data", f"{nums}; n < {MIN_N} on a side. Leave it open and set its Verdict to " \
                                            f"`open (extended to {hard}: insufficient data)`"
            if a is None or b is None:
                return "insufficient data", f"{nums}; still no data at the {HARD_CAP}-day cap. The measure cannot see " \
                                            "this change: record `unjudged: insufficient data` and consider a " \
                                            "scoreboard proposal (docs/loop.md)"
            nums += f" (judged at the {HARD_CAP}-day cap on n < {MIN_N})"
        verdict, rel = compare(ch["measure"], ch["direction"], b, a)
        pct = "n/a" if rel == float("inf") else f"{rel:+.0%}"
        return verdict, f"{nums}; change {pct}, claimed {ch['direction']}, threshold {MIN_REL:.0%}"


def window_of(ch):
    ext = EXTENDED.search(ch.get("verdict", ""))
    end = dt.date.fromisoformat(ext.group(1)) if ext else ch["landed"] + dt.timedelta(days=MAX_DAYS)
    return ch["landed"], end


def overlaps(ch, every):
    a0, a1 = window_of(ch)
    out = []
    for o in every:
        if o is ch or o.get("measure") != ch.get("measure") or "landed" not in o:
            continue
        b0, b1 = window_of(o)
        if a0 <= b1 and b0 <= a1:
            out.append(f"{o['id']} ({o.get('verdict', '?').split(':')[0][:20]})")
    return out


def maintenance(ch):
    files = ch.get("files")
    if not files:
        return f"{ch['id']}: maintenance, but its claim lists no `files:`; add them, then close it as 'kept (maintenance)'"
    beh = [f for f in files if f == "CLAUDE.md" or f.startswith(BEHAVIOUR)]
    msg = f"{ch['id']}: maintenance ({len(files)} file(s)); close it as 'kept (maintenance)'"
    if beh:
        msg += f". NOTE: it touched behaviour files ({', '.join(beh)}): the reviewer checks that no behaviour changed"
    return msg


def reread(ch, today):
    span = today - ch["landed"]
    before, after = measure_at(ch, ch["landed"] - span, today)
    b, a = before.get("value"), after.get("value")
    nums = f"{ch['measure']} {b} (n={before.get('n')}) -> {a} (n={after.get('n')}) over {span.days} days each side"
    if a is None or b is None:
        return f"{ch['id']}: RE-READ (kept {span.days} days) — no data on the longer window ({nums})"
    verdict, rel = compare(ch["measure"], ch["direction"], b, a)
    flag = "TURNED WORSE since it was kept — take it to the change-reviewer" if verdict == "worse" else f"now reads {verdict}"
    return (f"{ch['id']}: RE-READ (kept {span.days} days) — {nums}: {flag}. "
            f"Append `re-read {today}: <result>` to its Verdict so it is listed once.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="list every change, not only due ones")
    args = ap.parse_args()
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    today = dt.date.today()
    every = changes(os.path.join(root, "CHANGELOG.md"))
    due = 0
    for ch in every:
        verdict_line = str(ch.get("verdict", ""))
        v = verdict_line.lower()
        if not v.startswith("open"):
            if v.startswith(("helped", "kept")) and ch.get("direction") in ("up", "down") and "re-read" not in v \
                    and (today - ch["landed"]).days > REREAD_DAYS:
                due += 1
                print(reread(ch, today))
            elif args.all:
                print(f"{ch['id']}: {ch.get('verdict', '?')}")
            continue
        if "measure" not in ch:
            print(f"{ch['id']}: OPEN but has no claim line; fix the entry")
            continue
        if ch["measure"] == "S1":
            print(f"{ch['id']}: claims S1, which no window can judge; re-claim a leading measure")
            continue
        if ch["direction"] == "none":
            print(maintenance(ch))
            continue
        end = window_end(ch, today)
        if end is None:
            if args.all:
                print(f"{ch['id']}: window still open (landed {ch['landed']})")
            continue
        ext = EXTENDED.search(verdict_line)
        if ext and today < dt.date.fromisoformat(ext.group(1)):
            end = today
        due += 1
        verdict, why = judge(ch, end, today)
        shared = overlaps(ch, every)
        share = f" Credit is shared with {', '.join(shared)} (same measure, overlapping window)." if shared else ""
        if verdict == "too early":
            print(f"{ch['id']}: TOO EARLY — {why} — leave it open and re-judge later")
            continue
        if verdict == "insufficient data":
            print(f"{ch['id']}: INSUFFICIENT DATA — {why}.{share}")
            continue
        if verdict == "helped":
            action = "keep; add to lessons.md as a playbook candidate"
        elif verdict == "worse":
            action = (f"revert: git revert {commit_of(ch)} (confirm with change-reviewer first); "
                      "lesson status `retired`, with the reason")
        else:
            action = (f"revert: git revert {commit_of(ch)} (confirm with change-reviewer first); "
                      "lesson status \"no measured effect\": retryable, not retired")
        print(f"{ch['id']}: {verdict.upper()} — {why} — {action}.{share}")
    if not due and not args.all:
        print("No self-change is due a verdict.")


if __name__ == "__main__":
    main()
