# Turn adversary findings into machine checks

**Status:** `candidate` (side projects only; much of the evidence is
uncommitted).

**Lesson.** When the adversary finds the same kind of defect twice, turn it
into a machine check, so the next pass spends its attention on claims rather
than mechanics. Every known defeat of a guard becomes a regression test.

**Evidence**
- the-debrief converted 9 adversary findings into checks; its selftest grew
  18 → 42 → 52 cases: `the-debrief: docs/retro-input-001.md:130-146`.
- A systematic drafter defect, measured: the same check caught the same wrong
  reading 3 times: `the-debrief: docs/retro-input-001.md:148-153`.
- galind-team: a no-network guard test would have passed with the scanner
  deleted; the adversary defeated it four ways, and each defeat became a
  regression test:
  `galind-team: tickets/001-galind-email-surface.md:102-128` *(untracked)*.

**Where it failed / limits**
- **First versions leak:** two checks had to be rewritten after their first
  version let a defect through: `the-debrief: docs/retro-input-001.md:130-146`.
- **A check catches the shape it encodes:** a fused-citation defect recurred in
  a form the check did not cover:
  `the-debrief: slices/ADVERSARY-011-014.md:404` *(untracked)*.
- One lineage, two side projects, both now dormant.

**Origin.** the-debrief, 2026-08/10; galind-team, 2026-08.
