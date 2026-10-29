---
description: Tell Andres, in two minutes, how this system has evolved and whether each change helped.
---

Andres asked "what has changed?". Answer in plain language, short enough to read in two minutes.

1. Run `python3 .claude/hooks/boot_check.py < /dev/null` and `python3 scoreboard/score.py --summary`. If either reports **LOCK BROKEN**, lead with that and stop there.
2. Read `CHANGELOG.md` entries since the date under "Last asked" in `state.md` (or the last 30 days if none).
3. Write, in this order and nothing else:
   - **Waiting on you** — first the system list (`## Waiting on Andres: system` in `state.md`): for each open proposal in `log/pending/S-*.md`, its one-sentence change, the evidence in one line, and how to approve it (`scoreboard/apply S-NNN` in his terminal) or decline it (tell any session why); for each escalated self-change, what it is and what you need. Then the work list (`## Waiting on Andres: work`), one line each, oldest first, with its date. If both are empty, say so in one line.
   - **What changed** — one line per change: what, why (the event that prompted it), and its verdict so far: helped (with the numbers), unproven (no effect or insufficient data; kept), looks worse (kept or reverted, with the `decision` event's reason), reverted for harm (and the harm), or still open (due when).
   - **Looks worse** — information, not a request: each change whose verdict read *looks worse* since "Last asked", with its numbers, the S1 and S4 guardrails beside it, and what the system decided and why. Say "none" in one line if there were none.
   - **The scores** — each measure now against the 2026-10-28 baseline, one line, with what is not measured named where it matters. S3 counts Andres's follow-ups (raw prompt log and GitHub) from 2026-10-29, not `correction` events: say so when comparing it with the baseline.
   - **Due** — one line each, only if the boot check said so: a deeper pass due (and why); verdicts overdue past their cap.
   - **The crew** — one line from `python3 tools/crew_report.py`: who was spawned, what changed outcomes, any repeated ad hoc role.
   - **The reviewer's record** — its `reviewed` opinions (LAND, CONCERN, ESCALATE), CONCERNs the system landed anyway and why, changes it LANDed that were later reverted for harm, and CONCERNs that proved right.
   - **Lessons sent to the playbook** — candidates marked since last time, if any.
4. Update "Last asked" in `state.md` to today and commit it as `memory: what-changed`.

No process narrative, no tool-by-tool account. Name numbers and commits. Say what you did not verify.
