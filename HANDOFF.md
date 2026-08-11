# Handoff — state of play

Snapshot for whoever picks this up cold. Rewritten in place, never appended to.

**This layer gets the cold-start half of the handoff pattern and not the
write-during-work half.** Applying the pattern's own adoption test
(`patterns/handoff-record.md`): a quarterly review runs in one sitting and its
output *is* `meta/architect-log.md`, so there is no mid-work state to lose. A
child system running a weekly cycle or a multi-day ticket is a different case and
gets the full pattern. Do not add phase-boundary writes here — that would be the
layer taking on ceremony it does not need, which is a named failure mode in
`charter.md`.

---

## Current

```yaml
status: restated 2026-08-10 — two-clock design; no review run yet
last_review: 000 (founding entry, 2026-08-09)
next_review: 2026-11 or on flag — quarterly, never more often than
             the fastest child Architect
registry_changed: 2026-08-10 — two systems added, no review run
purpose_changed: 2026-08-10 — generative half made explicit, kill condition
             removed. Not a review. See below.
```

## What this layer is now

**Two jobs, two clocks.** This is the 2026-08-10 restatement and the most
important thing to absorb before doing anything here.

- **Generative, on demand.** New systems are grown from `spine.md`, read as a
  resource. No cadence, no ceremony, no procedure — deliberately. A scaffold
  script would freeze one model's understanding into the framework; a stated body
  of reasoning gets better every time the reader does.
- **Evolutionary, quarterly.** Proven divergence from the children is carried
  back into the spine. Slow because evidence accumulates slowly, and because a
  spine change reaches every system built afterwards.

**Divergence is cheap and local; convergence is expensive and deliberate.**

## What changed on 2026-08-10 (second entry that day)

Not a review. A restatement of purpose by the human, applied to the documents.

- **`spine.md` created** — the generative half, previously implicit in
  `patterns/`. Names what every system inherits, where systems are expected to
  differ, and that it is a resource rather than a procedure.
- **`charter.md` rewritten** — two jobs and two clocks; three named failure modes
  with tripwires; overhead ceiling now applies to the evolutionary clock only.
- **The kill condition is removed.** It was correct for a pure observer and wrong
  for the thing systems are grown from. What replaces it is a bar on action, not
  existence: the spine does not change until the children have earned it.
  Reasoning recorded in `charter.md` § On self-judgment and `meta/thesis.md`.
- **The founding convergence claim is withdrawn as stated.** Four systems built
  by one person in two days is one derivation repeated, not four independent
  ones. The `†` skepticism applied to the mPulse copies applies to the original
  four. The spine survives as a well-motivated hypothesis with no evidence yet —
  see `meta/thesis.md` § The origin observation.
- **`patterns/README.md` gained an explicit promotion gate** — `proven` now
  requires two or more *independent* adopters plus evidence of a changed outcome.
  **The existing `proven` statuses predate this bar and have not been re-audited
  against it.**
- **`meta/architect.md` gained § Steward the spine** and lost the instruction to
  propose deleting the repo.

## What exists

The portfolio is **seven repos**: six systems plus this layer, all on GitHub
under `agalin920`, all checked out under `~/dev/` as of 2026-08-10.

Two systems were added on 2026-08-10 — `mpulse-engage-team` and `mpulse-dpi-team`,
both **copied from zesty-eng-team, not grown from the spine**. That distinction is
load-bearing: see the `†` note on the adoption matrix. Registration is not a
review; nothing about them has been assessed.

**`personal-university` is PUBLIC. `meta-architecture` is now also PUBLIC.**
Every other repo in the portfolio is private. Whether either is deliberate is not
recorded anywhere.

## What happened on 2026-08-09

The layer was created, and three catalog patterns moved between systems the same
day. Full record in [`meta/architect-log.md`](meta/architect-log.md) review 000.

- **brand-system** gained the Critic (independent adversary), the untrusted-input
  boundary, and `CYCLE-STATE.md` (handoff record).
- **personal-university** cut the human half of predict-then-check, and moved its
  handoff from write-at-close to write-during.
- **This repo** cut `budget.md` before it was ever filled.

## Open

1. **The `proven` statuses have not been audited against the new independence
   bar.** Eight patterns are marked `proven` on evidence from four systems that
   are now understood to be one derivation repeated. Some will survive; some are
   `provisional` and were never anything else. **Review 001's first job**, and it
   is a demotion exercise, not a validation one.
2. **No Architect has run anywhere in the portfolio.** Zero completed reviews
   across six systems, two of which shipped with an architect and a drift check
   they have never exercised. Every claim about whether propose-never-apply
   actually works is still untested. This is the baseline review 001 measures
   against.
3. **F1 — brand-system's README is stale.** It says Session Zero has not been run;
   the repo has 16 pipeline items and 5 logged decisions, and `positioning.md`
   records a reduced Session Zero on 2026-08-09. Proposed to that repo's
   Architect, **not yet applied.** Also proposed: a reconcile-against-reality step
   in the Orchestrator's Phase 1.
4. **mpulse-engage-team's D-001 accepts drift from a shared org toolkit it does
   not control**, and names its own `/retro` as the only mechanism that catches
   it. An un-run mechanism guarding a live liability. Worth checking at review 001
   whether that retro ever happens — not whether the drift is bad yet.
5. **A candidate pattern is waiting on evidence**, not on argument: *knowledge
   accumulation as a gate rather than a habit*, from mpulse-dpi-team. See
   `patterns/README.md` § Candidate. Do not promote it before review 001 has
   looked at whether it produced knowledge or filler.
6. **Review 000 failed its own falsifier check** — three of five findings were
   within reach of a local Architect. Entry 000 is founding, not a review. Note
   that this no longer carries a deletion consequence; it is now evidence about
   thesis claims III and IV specifically, and should be read that way.

## Decisions that constrain the next session

- **`budget.md` was cut on 2026-08-09**, unfilled. It asked the human to state and
  maintain weekly capacity; he declined. The free half survives — observed
  distribution from `git log`. **Do not reintroduce a stated budget, and do not
  infer capacity from commit counts.**
- **Both public repos are public on purpose.** Decided by the human on
  2026-08-10: `personal-university` and `meta-architecture` stay public. The
  exposure was named at the time of the decision and accepted — this repo lists
  five private systems by name, domain, and cadence, and `systems.md` goes
  further. **This is settled; do not re-open it as a check.** If the calculus
  changes it is a new decision, made the same way.
- **Do not reintroduce a kill condition.** Removed deliberately on 2026-08-10
  with reasoning recorded in two places. If a future review concludes the layer
  is decoration, that is a finding for the human, not a self-executing clause.
- **`spine.md` stays a resource.** Do not turn it into a scaffold command, a
  checklist, or an instantiation procedure. The reasoning — that a procedure pins
  the framework to the capabilities of whatever wrote it — is in `charter.md` and
  `meta/thesis.md` claim I.
- **This is the second mechanism cut for costing the human a recurring step**,
  after the student prediction in personal-university. Both cuts were correct on
  their merits. **The Meta-Architect is the only thing positioned to see a *run*
  of these** — one cut is discipline, a pattern of them is comfort drift with
  better prose. Watch it at review 001; do not raise it yet, at n=2.
- **Never edit a child repo.** Findings go to that system's Architect and the
  human carries them. F2 and F3 were applied this way and it worked. This applies
  to spine changes: a promoted pattern changes what *future* systems inherit and
  does not retrofit itself into existing ones.

## Next action

Nothing is due. The next scheduled event is review 001, quarterly — **and neither
the registry growing nor the purpose being restated is a reason to run it early.**
"We changed things, let's review" is exactly what the named failure mode looks
like from inside.

Two things are worth doing before review 001, and neither is a review:

- **Decide whether the two public repos are intentional**, and record the
  decision either way. It is a decision, not a check.
- **Grow the next new system from `spine.md` rather than by copying an existing
  repo.** This is the only way claim I ever gets evidence, and copying is the path
  of least resistance — as 2026-08-10 demonstrated twice.

If something feels structurally wrong across systems before then:

```bash
claude "Read meta/architect.md and run a review."
```
