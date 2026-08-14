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
status: review 001a run 2026-08-13 — scoped to the two engineering teams
last_review: 001a (scoped, 2026-08-13). 000 was the founding entry
next_review: 001 — full portfolio, six systems. Undischarged; 001a did not
             cover it and its first job is unchanged
registry_changed: 2026-08-10 — two systems added
purpose_changed: 2026-08-10 — generative half made explicit, kill condition
             removed. Not a review. See below.
dispatched: 2026-08-13 — both packets, MET then ZET. Child repos verified
             unchanged. 5 accepted, 5 rejected. Nothing applied anywhere;
             the approvals are the human's. See Open 7.
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
2. ~~**No Architect has run anywhere in the portfolio.**~~ **Closed at review
   001a, 2026-08-13.** Four Architect reviews have run: zesty-eng-team ×3
   (08-08, 08-09, 08-13) and mpulse-engage-team ×1 (retro 001, 08-13).
   Propose-never-apply is no longer untested — ZET's Architect graded its own
   prior cycle proposal by proposal and **falsified its own P8**
   (`docs/decision-log.md:487`), which is the first direct evidence in the
   portfolio that the loop does anything. **The remaining four systems' Architects
   are still unmeasured** and that is review 001's, not this item's.
3. **F1 — brand-system's README is stale.** It says Session Zero has not been run;
   the repo has 16 pipeline items and 5 logged decisions, and `positioning.md`
   records a reduced Session Zero on 2026-08-09. Proposed to that repo's
   Architect, **not yet applied.** Also proposed: a reconcile-against-reality step
   in the Orchestrator's Phase 1.
4. ~~**mpulse-engage-team's D-001 ... an un-run mechanism guarding a live
   liability.**~~ **Closed at review 001a, 2026-08-13. It ran, and it found real
   drift.** `047dd6b` — +38/−2 across `definition-of-done.md`, `platform.md` and
   `repo-map.md`, recorded as D-018 (PR title convention) and D-019 (release PRs
   out of the metric denominator). The mechanism is no longer hypothetical and
   the liability is no longer unguarded. **What replaces this item:** the drift
   check has run once and the toolkit keeps moving, so the open question is
   whether it runs *again* — a check that fires once is not a mechanism yet.
5. **A candidate pattern is waiting on evidence**, not on argument: *knowledge
   accumulation as a gate rather than a habit*, from mpulse-dpi-team. See
   `patterns/README.md` § Candidate. Do not promote it before review 001 has
   looked at whether it produced knowledge or filler.
6. **Review 000 failed its own falsifier check** — three of five findings were
   within reach of a local Architect. Entry 000 is founding, not a review. Note
   that this no longer carries a deletion consequence; it is now evidence about
   thesis claims III and IV specifically, and should be read that way.
   **Review 001a came in at five of eight cross-system** — better, and the three
   local ones are the three child inventions this layer *carried* rather than
   found. Carrying is a service, not an insight. Read it that way too.
7. **`charter.md` is still silent on dispatch, and both packets have now been
   dispatched anyway** — on the human's explicit verbal instruction, 2026-08-13,
   MET first per rule 5. **Both child repos verified unchanged afterwards**
   (`889bf4f`, `6d43727`, clean trees); writes were denied at the tool layer, not
   merely asked against. Outcomes are in `meta/architect-log.md` § dispatch record.
   **The amendment is still unwritten and still his alone.** Verbal authorisation
   covered one instance; it did not move the boundary, and the next session will
   read a charter that bans editing children and says nothing about this. Wording
   is at the bottom of `meta/dispatch.md`. **If the answer is no, say so** and
   `meta/dispatch.md` becomes a `retired` entry with its reasoning — which is
   worth as much as a kept one, and the mechanism worked on its first outing.
8. **Claim IV is the thesis claim most likely to fail, and the evidence is
   against it.** ZET's Architect graded its own prior cycle, falsified its own
   P8, and corrected two false statements it had itself committed — an accurate,
   self-critical self-audit, which is exactly claim IV's falsifying condition.
   One instance is not "review after review", so it stands. **A second at ZET
   retro #4 means the audit-the-Architects job should be cut to a spot check**,
   as `meta/thesis.md` itself says. Do not read past this at review 002.

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

**Three things are due, and none of them is a review.**

1. **Approve or decline the five accepted proposals**, which is where both
   dispatches ended and where they were designed to end. **Nothing is applied in
   either child repo.** ZET has two diffs it says it would rather write than
   paste — § Cuts with the two-state clause, and two verify-blocks on targets it
   chose. MET has four, all landing in `retro.md`, off its capped read path:
   **net zero lines added to the per-ticket read path, cap tightened by 200.**
2. **Amend `charter.md` on dispatch, or decide not to.** Open 7. It ran once
   without the amendment, on verbal instruction. That does not carry forward.
3. **Decide on MF-7**, the one finding no Architect anywhere can act on. Both
   teams are graded only by bots — MET's window drew no human review at all, and
   ZET's three graders run under one account with two overwriting their own
   comments. **And it is worse than 001a recorded** — MET found its own comment
   marker missed once, on the repo with the weakest external coverage, which puts
   a phantom external review into the only number that measures this. Buying
   external feedback is a decision only the human can make. (Coverage specifics
   are held back from this public repo — see the publication note in
   `meta/architect-log.md`.)

**Then nothing until review 001**, which is quarterly and undischarged. **001a
did not discharge it** — it read two of six systems, and its own distribution
table has four blank rows. **Two scoped reviews in a row on the same two repos
would be this layer following attention instead of auditing it**, which is the
inverse of its job and would look like productivity the whole way down.

Still true, and still not reasons to run 001 early: the registry growing, the
purpose being restated, or a good idea arriving from a live project. *"We changed
things, let's review"* is exactly what the named failure mode looks like from
inside. **Review 001a cleared that bar on a data condition — F4's baseline became
false — and not on interest.** The next flag needs its own data condition.

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
