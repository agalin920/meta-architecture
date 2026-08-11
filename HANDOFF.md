# Handoff — state of play

Snapshot for whoever picks this up cold. Rewritten in place, never appended to.

**This layer gets the cold-start half of the handoff pattern and not the
write-during-work half.** Applying the pattern's own adoption test
(`patterns/handoff-record.md`): a quarterly review runs in one sitting and its
output *is* `meta/architect-log.md`, so there is no mid-work state to lose. A
child system running a weekly cycle or a multi-day ticket is a different case
and gets the full pattern. Do not add phase-boundary writes here — that would be
the layer taking on ceremony it does not need, which is the failure mode in
`charter.md`.

---

## Current

```yaml
status: established, no review run yet
last_review: 000 (founding entry, 2026-08-09)
next_review: 2026-11 or on flag — quarterly, never more often than
             the fastest child Architect
registry_changed: 2026-08-10 — two systems added, no review run
```

## What exists

The portfolio is **seven repos**: six systems plus this layer, all on GitHub
under `agalin920`.

Two systems were added on 2026-08-10 — `mpulse-engage-team` and
`mpulse-dpi-team`, both **derived from zesty-eng-team, not independently
arrived at**. That distinction is load-bearing: see the `†` note on the adoption
matrix. Registration is not a review; nothing about them has been assessed.

The deliverable is [`patterns/`](patterns/) — 15 patterns with origin repo,
adoption matrix, evidence, and failure modes. Start there; the matrix in
[`patterns/README.md`](patterns/README.md) is the whole thing in one table.

**Two things about that "all private, all clean and pushed" line, which used to
be here and was wrong by 2026-08-10:**

- **`personal-university` is PUBLIC.** Every other repo in the portfolio is
  private. Whether that is deliberate is not recorded anywhere. It is a
  five-second check and nobody had made it — which is the exact shape of finding
  this layer exists for.
- **All seven are now checked out** under `~/dev/` as of 2026-08-10.
  `personal-university`, `brand-system`, and `media-log` were cloned that day;
  they had been on GitHub but not locally, which would have blocked review 001
  outright. Nothing about them has been read since cloning.

## What happened on 2026-08-09

The layer was created, and three catalog patterns moved between systems the
same day. Full record in [`meta/architect-log.md`](meta/architect-log.md)
review 000.

- **brand-system** gained the Critic (independent adversary), the
  untrusted-input boundary, and `CYCLE-STATE.md` (handoff record).
- **personal-university** cut the human half of predict-then-check, and moved
  its handoff from write-at-close to write-during.
- **This repo** cut `budget.md` before it was ever filled — see below.

## What happened on 2026-08-10

Two systems added to the registry. **No review ran** — this was registration,
which is bookkeeping, not assessment.

- **mpulse-engage-team** and **mpulse-dpi-team** created, both adapted from
  zesty-eng-team for the two engineering teams the human manages at mPulse. Full
  entries in [`systems.md`](systems.md).
- The adoption matrix gained two columns, **marked `†` and explicitly excluded
  from the convergence claim.** Copies are not evidence. The reason to keep them
  in the table at all is to see where a copy dropped something — and one already
  has: both lost the `unmeasured` category that made zesty-eng-team's honest
  metric honest.
- One candidate pattern recorded and deliberately kept out of the catalog:
  *knowledge accumulation as a gate rather than a habit*.
- Two stale claims in this file corrected — the portfolio is not "five repos"
  and is not "all private".

## Open

1. **F1 — brand-system's README is stale.** It says Session Zero has not been
   run; the repo has 16 pipeline items and 5 logged decisions, and
   `positioning.md` records a reduced Session Zero on 2026-08-09. Proposed to
   that repo's Architect, **not yet applied.** Also proposed: a
   reconcile-against-reality step in the Orchestrator's Phase 1.
2. **No Architect has run anywhere in the portfolio.** Zero completed reviews
   across **six** systems now, two of which shipped with an architect and a
   drift check they have never exercised. Every claim about whether
   propose-never-apply actually works is still untested, and adding systems
   widened the untested surface without adding evidence. This is the baseline
   review 001 measures against.
3. **Review 000 failed its own falsifier check** — three of five findings were
   within reach of a local Architect. Entry 000 is founding, not a review, so
   the two-review clock has not started. **It starts at review 001.**
4. **`personal-university` is public and nothing records whether that is
   deliberate.** See above. Resolve it by deciding, not by checking again.
5. ~~**Three of seven repos are not checked out.**~~ **Resolved 2026-08-10** —
   all seven are now under `~/dev/`. **Review 001 is no longer blocked.** Note
   that removing the blocker is not a reason to run it early; see § Next action.
6. **mpulse-engage-team's D-001 accepts drift from a shared org toolkit it does
   not control, and names its own `/retro` as the only mechanism that catches
   it.** An un-run mechanism guarding a live liability. Worth checking at review
   001 whether that retro ever happens — not whether the drift is bad yet.
7. **A candidate pattern is waiting on evidence**, not on argument:
   *knowledge accumulation as a gate rather than a habit*, from
   mpulse-dpi-team. See `patterns/README.md` § Candidate. Do not promote it into
   the catalog before review 001 has looked at whether it produced knowledge or
   filler.

## Decisions that constrain the next session

- **`budget.md` was cut on 2026-08-09**, unfilled. It asked the human to state
  and maintain weekly capacity; he declined. The free half survives — observed
  distribution from `git log` across the four repos — and that is enough for the
  finding claim II is really about: *where the misses cluster*. **Do not
  reintroduce a stated budget, and do not infer capacity from commit counts.**
  See `meta/thesis.md` §II and `meta/architect.md`.
- **This is the second mechanism cut for costing the human a recurring step**,
  after the student prediction in personal-university. Both cuts were correct on
  their merits and the reasoning is recorded in each. **The Meta-Architect is
  the only thing positioned to see a *run* of these** — one cut is discipline, a
  pattern of them is comfort drift with better prose. personal-university's
  architect log flags the same check locally. Watch it at review 001; do not
  raise it yet, at n=2.
- **Never edit a child repo.** Findings go to that system's Architect and the
  human carries them. F2 and F3 were applied this way and it worked.

## Next action

Nothing is due. The next scheduled event is review 001, quarterly — **and the
registry growing from four systems to six is not a reason to run it early.**
`charter.md`'s failure mode is building the system being more fun than using it,
and "we added things, let's review" is exactly what that looks like from inside.

One thing is worth doing before review 001, and it is not a review:

- Decide whether `personal-university` being public is intentional, and record
  the decision either way. It is a decision, not a check.

Cloning the three missing repos was the other, and it is done — **which means
the only thing now standing between here and a review is the calendar.** That
is the point at which the temptation in `charter.md` is strongest.

If something feels structurally wrong across systems before then:

```bash
claude "Read meta/architect.md and run a review."
```
