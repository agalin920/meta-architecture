# Named failure modes with tripwires

**Status:** `founding` (ruling 1)

**Lesson.** Write down the system's likely silent failures up front, each with
an observable tripwire: a specific thing you could check that says it is
happening. A named risk with no observable is a mood.

**Evidence**
- The sharpest tripwires are computable: personal-university's "a rising
  `trivial` rate with flat mastery"; brand-system's voice convergence is
  tripped when its own voice check says "looks fine":
  `archive/patterns/named-failure-modes.md:31-40`.
- Tripwires do fire: engage's preflight reported the same three failures on
  every ticket from 08-20: `mpulse-engage-team: docs/team-log.md:5805-5808`;
  galind-team's F1 ledger and resale-desk's F1 were lit at review 001:
  `archive/meta/architect-log.md:3341-3343`.
- Review 001: one derivation, kept by ruling 1:
  `archive/meta/architect-log.md:3230`.

**Where it failed / limits**
- **A tripwire that fires into nothing.** In all three cases above the remedy
  waited for a retro nobody ran (engage: 69 days). A tripwire's remedy must run
  in the loop, not wait for a ritual: `archive/meta/architect-log.md:3277-3283`.
- **Predictions are guesses until the system runs.** mpulse-dpi-team predicted
  filler as its knowledge failure; the real one was staleness. See
  [maintain-knowledge](maintain-knowledge.md).
- A named failure backed by a real failure is a different object from a
  predicted one: `archive/meta/architect-log.md:2478-2479`.
- Tables are rarely revised: retire the ones that never fired, add the ones
  that bit: `archive/patterns/named-failure-modes.md:47-50`.

**Origin.** brand-system (risk table) and personal-university (anti-rigor
tripwire), 2026-08. In the kernel through the scoreboard and the loop.
