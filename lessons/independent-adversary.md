# Independent adversary

**Status:** `founding` (ruling 1)

**Lesson.** Whoever produces does not grade. A separate role with no stake in
the work judges it before it reaches the human, can fail it, never produces,
and is itself scored against what is found later.

**Evidence**
- zesty-eng-team's cold review caught a second component sharing a crash's
  failure shape and materially changed the fix:
  `archive/patterns/independent-adversary.md:34-37`.
- the-debrief's adversary caught two fabricated citations; the drafter caught
  neither: `the-debrief: docs/decision-log.md:291-337`.
- engage's gate trace records its cold reviewer as the top catcher: 28 CAUGHT
  (9 blocker) across the worklogs that record gates
  (`mpulse-engage-team: tools/gates.py`, run at the pre-migration tag).
- Review 001: changed-outcome evidence exists; a second independent inventor
  does not: `archive/meta/architect-log.md:3243-3246`.

**Where it failed / limits**
- **Unscored, it is confidently wrong.** brand-system's first scored critic
  entry missed one failure and overcalled two on the same draft:
  `brand-system: progress/critic-log.md:15-29` (partly uncommitted).
- **Independent of the author is not independent of the context.** Four
  adversary passes missed a conflict with the system's own decision log:
  `galind-team: docs/decision-log.md:259-265` *(uncommitted)*.
- **Framing errors survive** because the reviewer receives the plan's frame:
  `mpulse-engage-team: .claude/agents/reviewer.md:39`.
- **It fails open.** With subagents unavailable, review silently became
  self-review and the PR merged:
  `mpulse-engage-team: docs/definition-of-done.md:141`; the same at
  mpulse-dpi-team, now a draft PR (`47d6ba2`).
- **It costs.** Four passes, five revisions, zero product commits:
  `galind-team: strategy/proposals/001-galind-email-v0.md:735-753` *(untracked)*.
- Applied to self-changes it is a separate candidate:
  [self-change-adversary](self-change-adversary.md).

**Origin.** personal-university (Examiner) and zesty-eng-team (reviewer),
2026-08; scored form from brand-system (Critic). Kernel 5.
