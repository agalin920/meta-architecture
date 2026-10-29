#!/usr/bin/env python3
"""
Verdicts: read every self-change whose window has closed, as evidence.

Each self-change in CHANGELOG.md carries a machine line:
    <!-- claim: S2 down; landed: 2026-10-29; commit: abc1234 -->
    <!-- claim: maintenance none; landed: 2026-10-29; commit: abc1234; files: tools/x.sh,docs/y.md -->
and a human line:
    - **Verdict:** open

A change's window closes at the later of 14 days or 5 merged team PRs after it
landed, and never later than 30 days. Then the named score over the window is
compared with the same-length window before the change, and `n` is printed for
both. Changes are kept by default (Andres, 2026-10-29): at a few merged PRs a
week, a change that does nothing reads "helped" or "worse" about 40% of the
time each, so these numbers are evidence the system reads, never an automatic
rollback.

    insufficient data  either window has n < 5      -> keep open; the window extends,
                                                        up to a 60-day hard cap, then
                                                        it is kept as "unproven"
    helped     moved >= 10% in the claimed direction -> keep; playbook candidate
    no effect  moved less than 10% either way        -> keep as "unproven"; lesson "no
                                                        measured effect" (retryable)
    looks worse moved >= 10% the other way           -> uncertain at this n; nothing
                                                        happens automatically. The system
                                                        decides on its own judgement and
                                                        records a `decision` event saying why

A change is undone only for clear harm: an escape (S1) traced to it, Andres
saying it made things worse, or the system's own judgement (docs/loop.md).

S1 and S4 are guardrails and cannot be claimed. S1 (escapes) only counts PRs
merged 30+ days ago, so no 14-30 day window can see it move; the escape
tripwire in docs/loop.md watches it. S4 (escalations) is the gaming path: the
easy way to look better is to ask Andres less. For every judged change both are
printed over the same windows, beside the claimed measure, as counter-metrics.

Lack of data is never "no effect". Other changes claiming the same measure in an
overlapping window are listed: the credit (or blame) is shared. Kept changes
over 60 days old are listed once for a re-read on the longer window.

Maintenance changes claim `maintenance none` and are never judged on score.
They list the files they touched; a behaviour file among them (CLAUDE.md,
docs/, .claude/commands, .claude/agents) gets a note for the reviewer.
This script only reports; the loop weighs the verdict and records it. It is
locked: a system cannot soften its own ruler.

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
GUARDRAILS = {   # never claimable; printed beside every judged claim
    "S1": "no 14-30 day window can see it move (it counts PRs merged 30+ days ago)",
    "S4": "claiming fewer escalations is the gaming path: the easy way to look better is to ask Andres less",
}
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


def windows(ch, start, end):
    """Every measure before and after the change: the claim and its guardrails come from the same windows."""
    return score.compute(start, ch["landed"]), score.compute(ch["landed"], end)


def measure_at(ch, start, end):
    before, after = windows(ch, start, end)
    return before.get(ch["measure"], {}), after.get(ch["measure"], {})


def guardrails(ch, ctx):
    """S1 and S4 over the same windows as the claim: counter-metrics, read beside it."""
    start, end, before_all, after_all = ctx
    out = []
    for g in GUARDRAILS:
        if g not in before_all and g not in after_all:
            out.append(f"{g} not measured here")
            continue
        b, a = before_all.get(g) or {}, after_all.get(g) or {}
        bv, av = b.get("value"), a.get("value")
        s = f"{g} {bv} (n={b.get('n') or 0}) -> {av} (n={a.get('n') or 0})"
        if bv is None or av is None:
            s += " (no reading yet: S1 lags 30 days)" if g == "S1" else " (no reading)"
        else:
            moved, rel = compare(g, "down", bv, av)
            pct = "from 0" if rel == float("inf") else f"{rel:+.0%}"
            s += {"worse": f", {pct}: MOVED THE WRONG WAY, weigh it", "helped": f", {pct}",
                  "no effect": " (within 10%)"}[moved]
        out.append(s)
    return f"    guardrails over the same windows ({start}..{ch['landed']}..{end}): " + "; ".join(out)


def judge(ch, end, today):
    """(verdict, why, ctx). Extends the window when either side has n < MIN_N."""
    floor = getattr(score, "INSTRUMENT_SINCE", {}).get(ch["measure"])
    hard = ch["landed"] + dt.timedelta(days=HARD_CAP)
    while True:
        span = end - ch["landed"]
        start = ch["landed"] - span
        # A measure whose instrument changed is only compared against data from the same instrument.
        if floor and start < floor:
            start = floor
            if (ch["landed"] - start).days < 7:
                return "too early", f"fewer than 7 days of {ch['measure']} before the change on the current instrument", None
        before_all, after_all = windows(ch, start, end)
        before, after = before_all.get(ch["measure"], {}), after_all.get(ch["measure"], {})
        b, a = before.get("value"), after.get("value")
        nb, na = before.get("n") or 0, after.get("n") or 0
        nums = f"{ch['measure']} {b} (n={nb}) -> {a} (n={na}), window {start}..{ch['landed']}..{end}"
        if (nb < MIN_N or na < MIN_N or a is None or b is None) and end < min(today, hard):
            end = min(today, hard)      # extend, then look again
            continue
        ctx = (start, end, before_all, after_all)
        if nb < MIN_N or na < MIN_N or a is None or b is None:
            if end < hard:
                return "insufficient data", f"{nums}; n < {MIN_N} on a side. Leave it open and set its Verdict to " \
                                            f"`open (extended to {hard}: insufficient data)`", ctx
            blind = " The measure may not see this change: consider a scoreboard proposal (docs/loop.md)." \
                if a is None or b is None else ""
            return "unproven", f"{nums}; still n < {MIN_N} on a side at the {HARD_CAP}-day cap. Keep it and set " \
                               f"its Verdict to `unproven: insufficient data (<numbers>)`.{blind}", ctx
        verdict, rel = compare(ch["measure"], ch["direction"], b, a)
        pct = "n/a" if rel == float("inf") else f"{rel:+.0%}"
        return verdict, f"{nums}; change {pct}, claimed {ch['direction']}, threshold {MIN_REL:.0%}", ctx


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
    flag = ("now LOOKS WORSE on the longer window: evidence for your own judgement; whatever you decide, "
            "write a `decision` event saying why") if verdict == "worse" else f"now reads {verdict}"
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
            if v.startswith(("helped", "kept", "unproven", "looks worse")) and ch.get("direction") in ("up", "down") \
                    and "re-read" not in v \
                    and (today - ch["landed"]).days > REREAD_DAYS:
                due += 1
                print(reread(ch, today))
            elif args.all:
                print(f"{ch['id']}: {ch.get('verdict', '?')}")
            continue
        if "measure" not in ch:
            print(f"{ch['id']}: OPEN but has no claim line; fix the entry")
            continue
        if ch["measure"] in GUARDRAILS:
            print(f"{ch['id']}: claims {ch['measure']}, a guardrail that cannot be claimed: {GUARDRAILS[ch['measure']]}. "
                  "Re-claim a leading measure")
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
        verdict, why, ctx = judge(ch, end, today)
        shared = overlaps(ch, every)
        share = f" Credit is shared with {', '.join(shared)} (same measure, overlapping window)." if shared else ""
        if verdict == "too early":
            print(f"{ch['id']}: TOO EARLY — {why} — leave it open and re-judge later")
            continue
        if verdict == "insufficient data":
            print(f"{ch['id']}: INSUFFICIENT DATA — {why}.{share}")
        elif verdict == "unproven":
            print(f"{ch['id']}: UNPROVEN (insufficient data at the cap) — {why}{share}")
        elif verdict == "helped":
            print(f"{ch['id']}: HELPED — {why} — keep; add to lessons.md as a playbook candidate.{share}")
        elif verdict == "worse":
            print(f"{ch['id']}: LOOKS WORSE (uncertain at this n) — {why} — nothing happens automatically. "
                  f"Weigh it with the guardrails below and decide, on your own judgement, whether it stays; "
                  f"write a `decision` event (ref {ch['id']}) with your reasoning, then set its Verdict "
                  f"(docs/loop.md § Applying a verdict). Its commit: {commit_of(ch)}.{share}")
        else:
            print(f"{ch['id']}: NO EFFECT — {why} — keep it as unproven: set its Verdict to "
                  f"`unproven: no effect (<numbers>)` and record the lesson with status \"no measured effect\" "
                  f"(retryable, not retired).{share}")
        print(guardrails(ch, ctx))
    if not due and not args.all:
        print("No self-change is due a verdict.")


if __name__ == "__main__":
    main()
