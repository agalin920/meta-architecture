# Human gate on the irreversible action

**Status:** `founding` (ruling 1)

**Lesson.** Put an absolute human gate, with no exception clause, on the
actions that cannot be taken back, and only there. The hard stop at the end is
what makes autonomy upstream of it safe.

**Evidence**
- zesty-eng-team removed mid-flight checkpoints because the merge gate exists:
  `archive/patterns/human-gate.md:21-25`.
- When the gate was skipped it showed: the-debrief's human merged slices before
  the adversary saw them, and that later pass found unsupported central claims
  in 4 of 11 entries: `the-debrief: docs/project-log.md:89-92` *(uncommitted)*.
- Review 001: one derivation, kept by ruling 1:
  `archive/meta/architect-log.md:3229`.

**Where it failed / limits**
- **Gating too much.** Every reversible self-change waited for Andres, and he
  became the bottleneck on evolution (`REDESIGN.md:47-49`). Retired as
  [human-approves-self-changes](human-approves-self-changes.md).
- **The human routes around it.** the-debrief's owner told the agent three
  times to bypass the gate; it complied on the third. "A denial that yields to
  insistence is a speed bump": `the-debrief: docs/decision-log.md:375-412`.
- **Prose gates leak.** `Write(...)` deny lines were inert, only `Edit(...)`
  bound, and Bash denies are prefix matches:
  `archive/meta/architect-log.md:989-994`. Locks must be tested by an edit
  attempt (`REDESIGN.md:194-197`).
- **A "never" broken in practice:** engage built changes to a shared company
  toolkit in a scratch worktree despite a never-edit rule; the fix was held
  for the human: `mpulse-engage-team: docs/team-log.md:5850`.
- It covers irreversibility, not volume: a gate asked to approve more than it
  can read approves it anyway: `archive/meta/architect-log.md:2722-2755`.

**Origin.** Convergent founding: zesty-eng-team (never merge), brand-system
(nothing publishes), personal-university, media-log. Kernel: the gates.
