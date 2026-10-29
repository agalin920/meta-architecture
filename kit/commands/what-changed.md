---
description: Tell Andres, in two minutes, how this system has evolved and whether each change helped.
---

Andres asked "what has changed?". Answer in plain language, short enough to read in two minutes.

1. Run `python3 .claude/hooks/boot_check.py < /dev/null` and `python3 scoreboard/score.py --summary`. If either reports **LOCK BROKEN**, lead with that and stop there.
2. Read `CHANGELOG.md` entries since the date under "Last asked" in `state.md` (or the last 30 days if none).
3. Write, in this order and nothing else:
   - **Waiting on you** — escalations in `state.md`, one line each, with what you need from him. If none, say so in one line.
   - **What changed** — one line per change: what, why (the event that prompted it), and its verdict so far: helped (with the numbers), reverted (and why), or still open (due when).
   - **The scores** — each measure now against the 2026-10-28 baseline, one line, with what is not measured named where it matters.
   - **The reviewer's record** — changes it landed that were later reverted as worse, if any.
   - **Lessons sent to the playbook** — candidates marked since last time, if any.
4. Update "Last asked" in `state.md` to today and commit it as `memory: what-changed`.

No process narrative, no tool-by-tool account. Name numbers and commits. Say what you did not verify.
