# Honest metric

**Status:** `candidate`. Measured in two systems, and was the old catalog's one
promotion under the independence bar (2026-08-18). Not `proven` under the new
rule: no trial has run the 10-unit, 30-day hold.

**Lesson.** Report few metrics, each with its previous figure, its exact
denominator, and a named `unmeasured` bucket. Silence, a green run that posted
nothing and a skipped check are never "clean". When a figure is uncertain,
report a floor, or both cuts, with the reason.

**Evidence**
- zesty-eng-team retro 5: the metric script returned 0.00 silently on n=1; the
  discipline corrected it to **2.00 per PR, as a floor, n=2**, and the
  published trend flipped from flat to rising:
  `zesty-eng-team: docs/decision-log.md:596-602`.
- mpulse-engage-team retro 002 reported both cuts of its headline (1/4 and 5/5)
  and its context cost as a floor (≥1,356,714 output tokens) with the reason:
  `archive/patterns/honest-metric.md:144-161`.
- Coverage beside the count: engage's retro 003 figure (0.48) moved with
  reviewer coverage, not quality; 16 of 80 PRs had no outside reviewer:
  `mpulse-engage-team: docs/team-log.md:5817-5821`.

**Where it failed / limits**
- **The instruction alone failed** in the system that invented it: three
  retros, three wrong figures. Counting moved to a script; see
  [scripts-count](scripts-count.md).
- **Copies lose it.** Both mPulse teams inherited the metric and lost the
  `unmeasured` category: `archive/patterns/README.md:142-145`.
- **Definitions keep changing**, so figures are not comparable across retros:
  zesty-eng-team's changed at six of eight
  (`zesty-eng-team: docs/decision-log.md:800`, among others).
- A placeholder and a checked-clean entry look the same unless the format
  forbids it: `zesty-eng-team: tickets/README.md:46`.
- Escape rate, the measure both teams want, still has no feed from defects
  found after release: `archive/patterns/honest-metric.md:171-175`.

**Origin.** zesty-eng-team, 2026-08; re-derived at mpulse-engage-team
2026-08-13. Kernel 4: the scoreboard names what is not measured.
