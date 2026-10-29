# Boot ritual

**Status:** `founding` (ruling 1)

**Lesson.** Before deciding anything, a session reads a named, ordered, short
list of files and ends with one check against outside reality. What the boot
reads is what the system knows; the order itself carries priority.

**Evidence**
- zesty-eng-team's Orient ends in `git fetch && git status`, with the rule
  "if Current state disagrees with GitHub, GitHub is right":
  `archive/patterns/boot-ritual.md:36-40`.
- Position decides whether a step runs: personal-university's transfer audit
  was skipped 5 times at the end of a session and ran 2 of 2 once moved to the
  front: `personal-university: meta/architect-log.md:952-966`.
- Review 001: one derivation, kept by ruling 1:
  `archive/meta/architect-log.md:3226`.

**Where it failed / limits**
- **It loads a stale world faithfully.** zesty-eng-team's hand-kept Current
  state had 9 of 16 PR entries wrong at retro 7 and 6 of 11 at retro 8:
  `zesty-eng-team: docs/decision-log.md:816`, `:888`. See
  [reconcile-state-by-script](reconcile-state-by-script.md).
- **Rollups mislead.** personal-university answered a question about history
  from its own summary file and was wrong in both directions; claims about what
  happened are read from the log first:
  `personal-university: meta/architect-log.md:994-1013`.
- **Boot files go stale across a commit.** the-debrief stated its read path as
  571 lines while it was 693; rule: every number carries the command that
  produced it: `the-debrief: HANDOFF.md:15-25` *(uncommitted)*.
- **It grows.** Every incident adds a file and nothing removes one: engage's
  read path went 1,082 → 1,477 in 69 days. See
  [overhead-ceiling](overhead-ceiling.md).

**Origin.** Convergent: personal-university, zesty-eng-team, brand-system,
2026-08. Expressed now as the boot path and boot check (`../../dna.md`).
