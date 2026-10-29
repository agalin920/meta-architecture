# Write state during the work, not at the end

**Status:** `candidate` (old `handoff-record`).

**Lesson.** Anything left to the end of a session gets dropped. Write state as
the work happens, one file per unit of work, so a cold session resumes instead
of restarting. Per-unit files can run in parallel; the shared current-state
header cannot.

**Evidence**
- personal-university: seven instances across four mechanisms of end-of-session
  steps dropped. The fix was position, not enforcement: once the audit moved to
  the front it ran 2 of 2, after 5 skips:
  `personal-university: meta/architect-log.md:952-966`;
  `agents/session-protocol.md:94-96`.
- zesty-eng-team: "push this repo" was raised at three session closes and
  actioned at none, leaving 99 commits on one machine only:
  `zesty-eng-team: .claude/hooks/unpushed-check.sh:5-9`.
- zesty-eng-team's per-ticket worklog, updated at every pipeline step, is its
  crash-recovery record: `archive/patterns/handoff-record.md:39-45`.

**Where it failed / limits**
- **Written but not committed** is still lost: two zesty-eng-team worklogs sat
  uncommitted (one untracked 12 days, one +381 lines):
  `zesty-eng-team: docs/team-log.md:34`.
- **Monotonic ids collide** under parallel sessions: engage issued decision
  ids twice and renumbered them:
  `mpulse-engage-team: docs/team-log.md:5833`.
- **No checkout isolation:** zesty-eng-team sessions share one product
  checkout, and a commit landed on another session's branch (recorded,
  deliberately not fixed).
- Written at the end, it is a summary, not a handoff:
  `archive/patterns/handoff-record.md:74-75`.

**Origin.** zesty-eng-team (ticket worklogs) and personal-university
(`NEXT-SESSION.md`), 2026-08.
