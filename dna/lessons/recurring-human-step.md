# Any mechanism that needs a recurring human step

**Status:** `retired` as a design choice (n=3 cuts, plus the retro itself).

**Lesson.** Every mechanism in the portfolio that needed Andres to do something
every cycle was eventually cut or stopped. Each cut was right on its merits;
the run is the lesson. Capture the human's signal from what he already does.

**Evidence**
- **`budget.md`**, cut 2026-08-09 unfilled: it asked him to state and keep
  weekly capacity for a benefit he did not want:
  `archive/meta/architect-log.md:181-183`.
- **The student prediction**, cut 2026-08-09: see
  [predict-then-check](predict-then-check.md).
- **Ambient input**, cut 2026-08-20: "he does not plan to mention what he
  consumes, so the mechanism will never fire" (`02b2aa7`):
  `archive/meta/architect-log.md:3406-3413`.
- **The retro itself:** human-invoked everywhere, it ran on his attention
  clock: `archive/meta/architect-log.md:3351-3353`.
- Side projects agree: resale-desk's decline re-checks lapsed and its F1 lit,
  as its own founding note predicted:
  `resale-desk: docs/decision-log.md:193-214`.

**Where it failed / limits**
- **Not the gate.** Approving irreversible actions is not a recurring
  bookkeeping step; [human-gate](human-gate.md) stays founding.
- A run of such cuts is comfort drift unless the signal is replaced:
  `archive/meta/architect-log.md:200-206`. The kernel replaces it with
  automatic capture of his corrections (phase-1 §4.3).
- A rule that cannot fire is worse than no rule: retire the rule, not just its
  log (`02b2aa7`).

**Origin.** Seen first at this layer and personal-university, 2026-08-09;
raised at review 001. Basis of ruling 4 and `REDESIGN.md:42-46`.
