# Cadence defence

**Status:** `provisional`
**Invented in:** brand-system (the Orchestrator)
**Partial in:** personal-university (due-reviews-outrank-new-material)
**Missing from:** zesty-eng-team (correctly — its cadence is externally driven)

## The pattern

A named role whose **primary job**, above quality and above strategy, is
defending the schedule. It opens every cycle with a cadence statement before it
reasons about anything else, and it can halt production on consecutive misses.

The correction on repeated misses is **reduce the cadence** — never try harder.

## Why it works

Consistency beats brilliance for anything compounding over years, and a schedule
degrades silently: no single missed week looks like failure. Making the cadence
statement the *first* output every cycle means the miss cannot be discovered
late.

The under-commit rule is the counterintuitive half and it is right:
*"a schedule the operator reliably fails against corrodes the system faster than
a slower one they meet, and under-committing is the correct correction."*

## Evidence

- `brand-system/agents/cycle-protocol.md` — Phase 1 opens with the cadence
  statement: days since last publish, state of this week's piece, consecutive
  misses. *"If the cadence has been missed twice, stop here."*
- `brand-system/agents/architect.md` — and the refinement that makes it usable:
  if cadence is being met but **scoping** is the strain, say that instead — the
  fix is smaller pieces, not a slower clock.
- `personal-university/agents/session-protocol.md` — *"Due reviews outrank new
  material, always."* Defends retention rather than frequency; the same shape
  applied to a different scarce thing.

## The limit — and why this repo exists

**Every implementation of this pattern is blind to the other systems.**

An Orchestrator correctly defending a weekly cycle cannot see that the same
human owes a school ten sessions and a team a ticket queue. It will read a miss
as a local cadence problem and propose a local slowdown. So will every other
Architect. All of them will be locally right and collectively wrong.

That failure is not fixable inside any of these systems, and it is claim II of
`meta/thesis.md`. See `budget.md`.

## How it fails

- **Defending a cadence nobody chose.** Weekly should be a decision, not a
  default that hardened.
- **Halting production and calling it discipline.** The halt exists to force a
  cadence decision, not to become the steady state.
