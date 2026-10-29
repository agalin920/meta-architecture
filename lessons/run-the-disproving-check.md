# Run the check that could disprove it

**Status:** `candidate` (measured at this layer).

**Lesson.** A finding or claim is worth what the command that could disprove it
returned, run in the repo the claim is about. Before acting, name the one
direct observation that would prove it wrong, and make it.

**Evidence**
- This layer's dispatches: findings with an executed check were accepted 5 of
  10, without one 2 of 8; 10 of 11 rejections shared one failure (no check, or
  a check run somewhere else): `archive/meta/architect-log.md:1181-1188`,
  `:1352-1368`. It became a bar for every finding sent to a child.
- Structural arguments lost; the survivor was grounded in a measured present
  defect: `archive/meta/architect-log.md:1995-2000`.
- mpulse-engage-team: two errors in the architect's own report survived a
  well-argued report and died to checking:
  `mpulse-engage-team: docs/team-log.md:818-826`.
- mpulse-dpi-team: indirect artifacts trusted over a cheap direct read, "three
  instances in one ticket is a pattern":
  `mpulse-dpi-team: docs/team-log.md:435-436`.

**Where it failed / limits**
- **Substitute probes** (stubs, unauthenticated calls) get reported as the
  system's behaviour: zesty-eng-team's recurring inference failure.
- **Absence proven from one place** (searching an output, not the code that
  builds it) at mpulse-engage-team.
- A check that confirms is worth less than one that could kill:
  `archive/meta/architect-log.md:1471-1475`.

**Origin.** This layer, 2026-08-14 (SQ-2); the same rule in all three core
systems' own words.
