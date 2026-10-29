# Handoff record

**Status:** `proven`
**Invented in:** zesty-eng-team
**Adopted by:** personal-university (`NEXT-SESSION.md`)
**Missing from:** brand-system

## The pattern

**Anything written only at session close is a memory you will lose.**

A session can be interrupted, run out of context, or crash. So state is written
*as work happens*, not summarised at the end, into a file whose explicit job is
to let a cold session resume without redoing work.

Three parts:

1. **A per-unit-of-work file**, updated at every pipeline step — not at the end.
   One per ticket, per cycle item, per session.
2. **A current-state pointer**, rewritten in place, that says where things stand
   right now across all units.
3. **A resume instruction** in the boot ritual: read it and *continue from it,
   never restart from zero.*

## Why it works

It converts "I have to finish this in one sitting" into "I can stop anywhere."
That is the difference between a system that survives a real week and one that
only runs on good days — which is the same argument as
[cadence defence](cadence-defence.md), one level down.

**It is also what makes concurrency possible**, and that is the underrated half.
If each unit of work owns its own file, two sessions can run at once without
colliding. What they cannot both hold is the shared current-state header — so
per-unit files are the parallel part and the header is the serial part.

## Evidence

- `zesty-eng-team/CLAUDE.md` — the reference implementation. *"Update
  `tickets/<issue#>-<slug>.md` at every pipeline step — after intake, after
  investigation, after the plan, after implementation, after review. That file
  is the crash-recovery record: a fresh session must be able to read it and
  resume mid-ticket without redoing work."* Plus: *"The moment something lands
  — a branch pushed, a PR opened, CI going red — update the Current state
  header. It should never describe a world that no longer exists."*
- `personal-university/NEXT-SESSION.md` — *"Snapshot for whoever picks this up
  cold. Regenerated at the end of each session."* Weaker on one axis: it is
  written at session close rather than during, so an interrupted session loses
  its own state. Strong on another: it carries *why*, not just where — the
  standing rules that came out of the last session and what to avoid repeating.
- **brand-system has neither.** `pipeline.md` item states imply progress, but
  nothing records mid-cycle position and there is no current-state header. A
  cycle interrupted between the Writer and the gate leaves a draft on disk with
  no record of what was decided about it.

## Concurrency notes

For running two sessions at once on the same repo:

- **Per-unit files are safe to parallelise.** Disjoint paths, no conflict.
- **The current-state header is not.** One writer. Whoever finishes reconciles.
- **Monotonic ids collide.** `session_id`, `pipeline_id`, ticket numbers — two
  sessions will both claim the next one. Either allocate before forking, or use
  the external id where one exists (zesty-eng-team uses the GitHub issue number
  and sidesteps this entirely).
- **Filesystem isolation is a separate question.** zesty-eng-team's implementer
  uses a git worktree for a second concurrent ticket, and its docs are explicit
  that this costs a multi-minute `npm install` — *"parallelize tickets only when
  the throughput is worth that cost."* Worth copying that honesty: concurrency
  has a setup cost and the decision to pay it belongs in the docs.

## How it fails

- **Written at the end.** Then it is a summary, not a handoff, and the crash it
  was built for is exactly when it does not exist.
- **Describing a world that has moved.** Needs the reconcile-against-reality
  rule from [boot ritual](boot-ritual.md).
- **Growing into a second log.** It is a snapshot. If it accumulates history it
  has become [an append-only log](append-only-log.md) with a misleading name.
