# Predict-then-check

**Status:** `provisional` — **half of it was cut on first contact with the human**
**Invented in:** personal-university
**Considered and rejected for:** zesty-eng-team, brand-system (2026-08-09)

## The pattern

Before acting, the system records what it expects to happen. Afterwards, the
prediction is scored against reality. The accumulated error is audited **before
anything else**, because every other finding is downstream of whether the system
understands what it is doing.

Two halves, and they are not equal:

- **System-side** — the system predicts its own output. Costs the human nothing.
- **Human-side** — the human predicts too, training calibration as a skill.
  Costs one number per session.

## Why the system-side half works

Outcome metrics tell you whether you are improving. Prediction error tells you
whether you are **right about yourself** — which is a different and harder
question, and the one that detects drift in either direction. Persistent
over-prediction means placement is too aggressive; under-prediction means the
system has gone soft.

## Why the human-side half was cut

**Recorded because this is the most useful entry in the catalog: a pattern that
looked elegant and did not survive.**

`personal-university/meta/calibration.md`, 2026-08-09. The ask failed on first
use at session 0005 — *"I have no clue what you are asking me"* — because
predicting your own score against a rubric you have never been graded on is
guessing at a scale, not at yourself. A better-worded replacement was drafted
and **never ran**: the student cut the mechanism first, on the grounds that it
was overly complicated for the gain.

Three reasons that was accepted rather than argued down:

1. **Friction against the real failure mode.** The charter caps admin at ~10%
   and names time as scarce. The likeliest way that system dies is the human
   stopping, not any of the architectural risks.
2. **The signal was already collected, more cheaply.** `friction_type` reports
   *"beneath me"* vs *"this is hard"* directly, in one word already being
   written. Prediction error reached the same question by inference.
3. **A field no decision reads gets deleted.** See [overhead
   ceiling](overhead-ceiling.md).

**What it cost, recorded honestly:** thesis capacity 3 lost its only direct
training mechanism, and `meta/thesis.md` now reads *not currently trained*.

## The generalisable lesson

**Split any pattern by who pays for it.** The system-side half is nearly free
and survives; the human-side half costs a step every cycle and did not. A
pattern is not one thing to adopt or reject — it usually has a cheap half and an
expensive half, and they should be evaluated separately.

**Do not port the human-side half** to zesty-eng-team or brand-system. It was
considered on 2026-08-09 and rejected on the same reasoning: both already have
retrospective signals (Director findings per ticket; traction plus the
decision-log `energy` field) covering the same question without a new human step.

**Reintroduction bar:** a mechanism that costs the human nothing at the point of
use. A rewording does not qualify — the friction was the objection, not the
phrasing.

## Open question for the first review

`brand-system` has an Analyst that measures and a Critic that judges, both
system-side and both free. An Analyst prediction of resonance before publish
would cost the human nothing and would tell the Scout and Writer whether they
understand the audience. **Not adopted** — flagged here because the cheap half
of this pattern has not actually been ruled out anywhere, only the expensive one.
