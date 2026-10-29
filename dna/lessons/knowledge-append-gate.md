# Mandatory knowledge append at every unit of work

**Status:** `retired` (2026-10-28, replaced by maintain).

**Lesson.** A gate that makes every ticket append what it taught grows the
knowledge file but does not keep it true. Appended facts go stale as the code
moves on; the gate had no step that corrected them.

**Evidence**
- mpulse-dpi-team made it gate 9 of its definition of done (D-003) and named
  its own predicted risk, filler: `mpulse-dpi-team: docs/decision-log.md:47`.
- The old catalog held it as a candidate with zero evidence:
  `archive/patterns/README.md:290-304`.
- Graded at the first retro: filler was under 1% (9 lines), **8 facts had gone
  stale**, so the gate was rewritten from append to maintain:
  `archive/meta/architect-log.md:3399-3404`; `444b364`.

**Why retired**
- It measured the wrong thing. Growth said nothing about truth.

**Where it failed / limits**
- The idea behind it holds: knowledge as a gate rather than a habit, because
  habits lose to the task in front of you. The gate survives, rewritten; see
  [maintain-knowledge](maintain-knowledge.md).

**Origin.** mpulse-dpi-team, 2026-08-10.
