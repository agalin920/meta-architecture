# Grade the previous cycle's changes

**Status:** `candidate`. Carried to a second system, where it ran; a carried
trial now counts, but the 30-day hold has not been measured under the rule.

**Lesson.** Each improvement pass first grades the last pass's changes: fired
and worked, fired and failed, inert, or mis-sited. A change whose effect was
never checked was a guess. The kernel's rollback window now does this for
every self-change.

**Evidence**
- personal-university: 3 of 4 approved proposals did not produce their effect,
  and nobody noticed for six sessions:
  `personal-university: meta/architect-log.md:1160-1190`.
- zesty-eng-team grades every retro from 3 on
  (`zesty-eng-team: docs/decision-log.md:620`, `:763`, `:829`, `:885`): e.g.
  the Orient script "fired and failed", run in 5 of 13+ sessions (`:888`); the
  answer-first rule partly worked, median reply 224 → 168 words (`:890`).
- mpulse-engage-team (carried): retro 003 graded four of retro 002's changes
  "did nothing": `mpulse-engage-team: docs/team-log.md:5811-5813`.
- It graded this layer too: a carried mechanism was "correctly built, pointed
  at the wrong claims": `archive/meta/architect-log.md:2222-2227`.

**Where it failed / limits**
- **Only as frequent as the pass.** In engage's 69 days without a retro nothing
  was graded; the kernel ties the check to a window, not to a ritual.
- The grader is the party the retro is about: "treat your own agreement as
  the weakest signal": `zesty-eng-team: .claude/commands/retro.md:46`.
- The system half of the old `predict-then-check` lives here; the human half
  is retired: [predict-then-check](predict-then-check.md).

**Origin.** zesty-eng-team, 2026-08; independently personal-university;
carried to mpulse-engage-team (MF-2b).
