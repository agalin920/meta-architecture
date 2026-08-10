# Falsifiable thesis

**Status:** `provisional` — one implementation, no completed review cycle yet
**Invented in:** personal-university
**Missing from:** zesty-eng-team, brand-system

## The pattern

A document, separate from the charter, stating **why the system is shaped the
way it is** — and naming the conditions that would prove the shape wrong.

The charter says what the human is owed. The thesis says what the machine
believes, and it is the thing to argue with when the shape looks wrong.

Critically: **every non-obvious piece of the architecture traces back to it.**
An agent, file, or ritual that serves nothing in the thesis gets cut.

## Why it works

Without it, an Architect can find drift but can never conclude *this whole
mechanism is decoration, kill it.* It can only tune. That is why every system
here has to default "should we add an agent?" to **no** — with no kill path,
additions are permanent, so the only defence is never adding.

A thesis with falsifiers inverts that. personal-university can afford the
Synthesist and the Examiner precisely because it wrote down what would prove
each one worthless.

## Evidence

- `personal-university/meta/thesis.md` — five capacities, three structural
  commitments, a list of agents *considered and rejected with reasons*, and four
  falsifiers. *"A thesis with no falsifier is a mood."*
- **It works.** On 2026-08-09 the student's prediction step was cut. Because the
  thesis existed, the cut could be scored honestly: capacity 3 is now marked
  *not currently trained*, §III marked half true, and the discharged falsifier
  replaced with a school-side one. Without a thesis that would have been a tidy
  simplification with no visible cost.
- **The gap:** zesty-eng-team's `docs/decision-log.md` records rationale per
  decision, which is close and genuinely useful — but it is a history of choices,
  not a claim that can be wrong. brand-system's risk table names failure modes,
  which is not the same as naming conditions that would falsify the design.

## Adoption notes

Cheaper than it sounds. A thesis is one page: what this system believes produces
the outcome, which parts of the architecture serve which belief, and three or
four conditions that would prove it wrong.

For zesty-eng-team the claim is roughly already written across the decision log
— *a pre-PR adversarial gate plus accumulated private knowledge beats a faster
loop with human review at the end* — and its falsifier is nearly stated in the
metric: if blockers-per-PR doesn't fall, the gate is not doing the work.

## How it fails

- **Written and never checked.** An unchecked falsifier is the same as none;
  personal-university's Architect is therefore told to check all four every
  review.
- **Falsifiers too weak to ever fire.** If no realistic outcome trips them, they
  are decoration with the shape of rigour.
