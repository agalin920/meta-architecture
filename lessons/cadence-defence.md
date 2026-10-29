# Cadence defence

**Status:** `retired` (rulings 2 and 4). Never measured anywhere.

**Lesson.** A role whose first job each cycle is defending a human-facing
schedule, halting on two misses and cutting the cadence rather than trying
harder. It assumed a miss is a failure to fix.

**Evidence**
- No datapoint: brand-system, its origin, stopped on 2026-08-16 and its
  Architect never ran: `archive/meta/architect-log.md:3302`;
  `brand-system: README.md:178` (the rule itself, asserted).
- personal-university's form, "due reviews outrank new material", is recorded
  and never measured: `archive/patterns/cadence-defence.md:35-37`.
- Misses fell on every system without an outside forcing function, and no
  local defence could see that: `archive/meta/architect-log.md:3307-3316`.

**Why retired**
- Ruling 2: a quiet side project is paused, not failed; the layer stops
  treating inactivity as something to fix (`REDESIGN.md:97-103`).
- Ruling 4: rituals are optional; the loop runs per unit of work, not per
  calendar slot (`REDESIGN.md:106-108`).

**Where it failed / limits**
- The half worth keeping is an observation, not a status: a schedule the human
  reliably fails corrodes a system faster than a slower one he meets
  (`archive/patterns/cadence-defence.md:23-25`). See
  [recurring-human-step](recurring-human-step.md).

**Origin.** brand-system (the Orchestrator), 2026-08.
