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
status: goal rulings recorded 2026-08-14 — eight decisions by the human,
             see the final architect-log entry. Charter amended (roles/product,
             dispatch, company boundary). Deny list applied. Opens 7 and 9 closed
last_review: 001a (scoped, 2026-08-13). 000 was the founding entry
next_review: 001 — full portfolio, six systems. Undischarged. New agenda from
             the rulings: earned-autonomy change-classes, the two feedback
             instruments, the MET shadow-grants finding
registry_changed: 2026-08-14 — MDT ruled active/low-cadence by decision
purpose_changed: 2026-08-14 — engine is the product, delivery the constraint;
             hands-on Director permanently the gate; scoreboard + falsifier
             in meta/thesis.md. By the human, through a directed session
dispatched: 2026-08-14 — all seven approved items applied and on main in both
             child repos. Nothing pending dispatch
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
7. ~~**`charter.md` is still silent on dispatch**~~ **Closed 2026-08-14: the
   amendment is applied to `charter.md` as drafted, on the human's explicit
   instruction through a directed session.** Original item kept below for
   history: **both packets had been dispatched anyway** — on the human's explicit verbal instruction, 2026-08-13,
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
9. ~~**This repo has no permission guard of any kind.**~~ **Closed 2026-08-14:
   `.claude/settings.json` created with `Edit`/`Write` denies on `../**` and
   every child path (both verbs per path), plus best-effort `Bash(git -C ../*
   <verb>*)` lines — the Bash patterns are untested against the matcher and
   may be inert; the Edit denies are the load-bearing guard. Applied on the
   human's explicit instruction.** Original item kept for history:
   `.claude/settings.local.json` carries **no `deny` key** — `permissions`
   contains only `allow`, 21 entries, including **`Bash(git push *)`
   unrestricted.** Nothing prevents a Meta-Architect session writing to a child
   repo except the instruction not to; both dispatches denied writes in the
   moment, which is a judgment rather than a property. **mpulse-engage-team is
   still the only system in the portfolio where the boundary holds against an
   agent that decides otherwise.** Verified 2026-08-14 and deliberately not
   applied — see the ruling entry. Two gaps to carry into any fix: `Write(...)`
   deny lines are inert where `Edit(path)` is not, and `Bash(git commit:*)` does
   not cover the `git -C . commit` form.

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

**Updated 2026-08-14 after the goal rulings** (final architect-log entry —
read it first; it supersedes much of what follows). Still open, in order:
**MF-7 evolved** — the human ruled he *is* the external feedback; what remains
is instrumenting his miss rate (escape tracking + calibration sample), which is
review 001 packet material. **MDT's wake-up item** — DF-1's Jira/PHI fix,
standing in `systems.md`. **Review 001** — quarterly, undischarged, agenda now
includes the earned-autonomy classes and the MET shadow-grants finding.
**A birth** — no domain yet, none forced; the two-quarter falsifier clock in
`meta/thesis.md` started 2026-08-14.

The record below is the pre-ruling state, kept for history.

**Three things were due, and none of them is a review.**

1. ~~**Approve or decline the five accepted proposals.**~~ **Approved by the human
   on 2026-08-14. Still unapplied — this is now an execution item, not a decision
   one.** Verified the same day that none of the seven accepted items across both
   dispatches had landed: ZET `306a59d`, MET `17112a9`, and the only post-dispatch
   commits in either repo are each team's own self-found fixes from the advisory
   addendum, which are a disjoint set. **Pending, by repo:**
   - **ZET (2)** — MF-1 § Cuts with the two-state clause it made non-optional;
     MF-4 verify-blocks on the two targets it chose. Neither present: no Cuts
     heading and no `verify-block` anywhere in `.claude/`, `CLAUDE.md`, `docs/`.
   - **MET (5)** — MF-1b cap 1,300 → 1,100; MF-2b grade the previous cycle;
     MF-8 overhead ratio; AF-3 severity buckets; AF-6 context-per-ticket query.
     None present. **MF-1b is two edits, not one:** `architect.md:103` carries the
     number and `:106` carries the executable assertion that tests `<= 1300`.
     Changing one without the other makes `verify_docs.py` fail against MET's own
     accepted figure — which is the executable-claims convention working, and a
     trap for a session applying in a hurry.

   **Dispatched the same day on the human's instruction — the first application
   dispatch this layer has run, and the first authorised to write.** Outcome:
   - **MET — 1 of 5 applied.** `17112a9 → eb4280c`, three commits, not pushed.
     AF-3's tooling half landed and is fixture-verified. **MF-1b, MF-2b, MF-8 and
     AF-6 are blocked**: writes to `.claude/agents/architect.md` and
     `.claude/commands/retro.md` were refused by harness behaviour in
     non-interactive mode — **not by any deny rule; none exists at any settings
     level, and an explicit `Edit(.claude/**)` grant does not lift it either.**
     **Only an interactive session can apply these five.** MET corrected its own
     false "deliberate guard" claim at `b0517e5`. **AF-6's precondition is now
     answered** — transcripts do carry `message.usage` token counts, but subagent
     usage is absent (`isSidechain` false everywhere, so any figure is a *floor*,
     and MET delegates by default) and nothing keys a session to a ticket, so
     attribution is by timestamp and approximate. Write the instruction to that,
     numeric fields only, no transcript content.
   - **ZET — MF-4 applied**, `d8c9a49 → 354359d`, two commits, not pushed. Three
     `**Verify.**` blocks, all executed before commit — and running them caught a
     self-matching regex that would have shipped broken. **MF-1 is blocked**, same
     harness refusal on `.claude/agents/architect.md`. **Its accepted targets were
     recoverable only from a session transcript and are now written into
     `meta/architect-log.md`** — the decision existed in no reproducible form in
     either repo, which is the dispatch write-back defect recorded there.
   - **Useful by-product:** MET's read path is **1,056 against the accepted 1,100
     cap — 44 lines of headroom**, and `retro.md`/`architect.md` are off the read
     path, so all five accepts are mutually compatible. **AF-6 must not be written
     until someone checks whether the transcripts carry `usage` counts**, and it
     must be scoped to numeric fields only — those are HIPAA-platform session logs.
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
4. **Decide whether this repo gets a deny list.** Open 9, new on 2026-08-14 and
   verified rather than argued. **Not applied deliberately** — a permissions
   change is a change to how a Meta-Architect session is constrained, and making
   it from inside the session it constrains is the wrong hand on the switch. It
   is also your call whether denies here break your other sessions. **The
   suggested form:** deny `Edit` **and** `Write` on `../*/**` and on each child
   path by name, plus the write verbs under `Bash(git -C:*)`.

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
