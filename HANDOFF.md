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
status: BOTH CLOCKS TURNED for the first time, 2026-08-18/19.
             Evolutionary: honest-metric promoted to `proven` — the portfolio's
             first promotion. Generative: zesty-webengine-team GROWN FROM THE
             SPINE — the portfolio's first birth. Neither claim is tested by
             either event; read the caveats before repeating the headline
last_review: 001a (scoped, 2026-08-13). 000 was founding. The 08-14 rulings, the
             08-15 AR proposals and the 08-18 scoped read are entries, not reviews
next_review: 001 — full portfolio, now SEVEN systems. STILL UNDISCHARGED, and now
             overdue in a way that has a name: see the cadence warning below
promotions:  1 (honest-metric, 2026-08-18). Births: 1 (zesty-webengine-team,
             2026-08-19, zero tickets run). Transfer yield: 4 of 7
registry:    systems.md refreshed 2026-08-18 with MEASURED commit counts and a
             distribution table. MDT's standing wake-up item is DISCHARGED
dispatched:  nothing since 2026-08-15. All seven 08-14 items and AR-3 have landed
             in the children and are verified there
```

## Read this before you do anything: the cadence warning has fired

**This layer has now read the same two repos three times running** — 001a
(08-13), the goal rulings and AR proposals (08-14/08-15), and the scoped read
(08-18). The previous version of this file warned against *two*:

> *"Two scoped reviews in a row on the same two repos would be this layer
> following attention instead of auditing it, which is the inverse of its job and
> would look like productivity the whole way down."*

**It made three, and each one produced real findings**, which is exactly why it
is hard to stop. Measured distribution since 2026-08-14: **84 of 100 commits are
in zesty-eng-team and mpulse-engage-team.** Four of six systems were unexamined
for the third consecutive time. personal-university (1 commit) and brand-system
(3) have not been opened by this layer since 2026-08-13.

**The next thing this layer does should be review 001, or nothing.** A fourth
scoped read of the engineering teams is the failure mode, not the work — however
good the findings are, and they will be good, because those two repos generate
findings faster than this layer reads them.

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

The portfolio is **eight repos**: seven systems plus this layer, all under
`agalin920`, all checked out under `~/dev/`. **`zesty-webengine-team` was added
2026-08-19 — the first system grown from `spine.md` rather than copied.**

Two systems were added on 2026-08-10 — `mpulse-engage-team` and `mpulse-dpi-team`,
both **copied from zesty-eng-team, not grown from the spine**. That distinction is
load-bearing: see the `†` note on the adoption matrix. *(Was: "nothing about
them has been assessed." **Superseded** — both were assessed at 001a, both have
since run their own retros, and MET now holds patterns its parent lacks.)*

**`personal-university` is PUBLIC. `meta-architecture` is now also PUBLIC.**
Every other repo in the portfolio is private. **Both are public on purpose**,
decided by the human on 2026-08-10 with the exposure named and accepted. *(Was:
"whether either is deliberate is not recorded anywhere." **Superseded** — it is
recorded, in § Decisions below, and re-opening it as a check is explicitly out
of bounds.)*

## What happened on 2026-08-09

The layer was created, and three catalog patterns moved between systems the same
day. Full record in [`meta/architect-log.md`](meta/architect-log.md) review 000.

- **brand-system** gained the Critic (independent adversary), the untrusted-input
  boundary, and `CYCLE-STATE.md` (handoff record).
- **personal-university** cut the human half of predict-then-check, and moved its
  handoff from write-at-close to write-during.
- **This repo** cut `budget.md` before it was ever filled.

## Open

Renumbered and re-verified 2026-08-18. Closed items are struck rather than
deleted — a closed item with its evidence is worth as much as an open one.

1. **The `proven` statuses have not been audited against the independence bar.**
   Eight patterns are `proven` on evidence from four systems now understood to be
   one derivation repeated. **Review 001's first job, and it is a demotion
   exercise.** Unchanged since 2026-08-10 and now the oldest open item here.
   **Newly urgent:** the bar itself gained a third case on 2026-08-18
   (`carried`), so the re-audit has one more question to ask of every row —
   *did this adopter arrive at it, inherit it, or get it dispatched from here?*
2. **F1 — brand-system's README is stale.** Says Session Zero has not been run;
   the repo has 16 pipeline items, 5 logged decisions, and a reduced Session Zero
   recorded in `positioning.md` on 2026-08-09. Proposed to that repo's Architect,
   **still not applied, and this layer has not opened brand-system since
   2026-08-13.** Do not re-verify it from here as a substitute for review 001.
3. **The two feedback instruments remain unbuilt.** The human ruled on 2026-08-14
   that he *is* the external feedback; what is unresolved is instrumenting his
   miss rate — escape tracking (defects traced to the originating PR) and a
   calibration sample (one PR per quarter reviewed by a second human).
   **Partial movement:** MET reported a bucketed escape rate at retro 002 (14
   caught: 7 blocker, 7 suggestion), **but it still has no feed from defects
   surfacing after release**, which is the half that measures the human. Review
   001 packet material.
4. **The `carried` gate case is written but nothing has been re-audited against
   it.** Added 2026-08-18 to `patterns/README.md` § The third case, because
   `executable-claims` had quietly acquired a second adopter that was this
   layer's own dispatched proposal. **Checked: it changes nothing retroactively**
   — `honest-metric`'s promotion rests on invention plus documentary
   re-derivation, neither a carry. Every other row is untested against it, which
   is item 1.
5. **mpulse-dpi-team has run zero retros, ever**
   (`git log --all --oneline | grep -ci retro` → `0`, checked 2026-08-18). Its
   Architect is the only one in the portfolio that has never executed, and the
   knowledge-gate candidate in `patterns/README.md` **cannot be graded because
   the grading step does not exist.** This is *not* a cadence miss — the human
   ruled the quiet deliberate on 2026-08-14 — but "low cadence" and "the
   improvement loop has never run" are different facts and only the first was
   ruled on.
6. **`single-source-claims` is at `provisional` on day-one evidence and has a
   retirement test that has not returned.** If neither instrument catches a
   drifted or struck-but-surviving claim by the end of the next full cycle at ZET
   and MET, it is prose that made everyone feel careful. MET's shasum assertion
   is the cheaper one to grade: it either fires or it does not.
7. **Review 000 failed its own falsifier check** — three of five findings were
   within reach of a local Architect. 001a came in at five of eight. **The
   2026-08-18 scoped read came in at two of six**, and the two that were
   genuinely unavailable locally are both about this layer's own machinery
   (the gate hole, the two-timezone date slip). **The trend on claim III is
   down, and it should be read as evidence about claim III rather than smoothed
   over.**
8. **Claim IV has taken six consecutive hits and the thesis says to act on two.**
   `meta/thesis.md`: *"the Architects' self-audits turn out to be accurate and
   self-critical when checked... Then the audit is redundant and should be cut to
   a spot check."* Six. **Review 001 should cut § 3 Audit the Architects to a
   spot check** and stop reporting the hit as news. This is the clearest
   act-on-your-own-falsifier item in the file.
9. ~~**This repo has no permission guard.**~~ **Closed 2026-08-14**,
   `.claude/settings.json` with `Edit`/`Write` denies on `../**` and every child
   path. **Held as a property since**: the 2026-08-15 AR dispatch was the first
   run where the boundary held at the settings layer rather than by judgment.
   Two known limits, both now confirmed by the harness rather than inferred:
   `Write(...)` deny lines are inert and only `Edit(path)` binds, and
   `Bash(git commit:*)` does not cover the `git -C . commit` form.
10. ~~**Seven approved items pending application.**~~ **Closed 2026-08-18 — all
    seven landed, plus AR-3, verified in the target repos.** This file previously
    asserted both that they were applied (header) and that they were pending
    (Next action). The header was right. Item-by-item table with locations and
    effects is in the final `meta/architect-log.md` entry, § 5.
11. ~~**mpulse-dpi-team's standing wake-up item.**~~ **Closed 2026-08-18 —
    discharged at `7888bb3` on 2026-08-14**, four days before this layer looked.
    All four command files route through `jira.py`; the false PHI-sanitization
    claim at `take-ticket.md:10` is gone and `:17` now states the truth.
    **MDT is eligible for proposals again.**
12. ~~**`charter.md` silent on dispatch.**~~ **Closed 2026-08-14**, amendment
    applied on the human's explicit instruction.

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

**Review 001. Or nothing.**

**Unchanged by the birth, and the birth is the reason to say so explicitly.**
Growing `zesty-webengine-team` was the generative clock, which has no cadence and
blocks nothing. It does not discharge review 001, it does not reset the cadence
warning, and *"we just built something, let's review"* is the named failure mode
wearing a new coat. What it does do is **add a seventh system to review 001's
scope** and put two new spine questions on its agenda (see below).

The reason is in the cadence warning at the top of this file: three consecutive reads of the same two repos, 84 of 100
commits in those two repos, four systems unexamined three times running. **A
fourth scoped read of the engineering teams would be the named failure mode
executing itself, and it would produce good findings while doing it.**

When 001 runs, it has an agenda it did not have before, in rough priority:

1. **The `proven` re-audit** (open 1), now with the `carried` question added to
   every row.
2. **Cut § 3 Audit the Architects to a spot check** (open 8). Six consecutive
   hits against a thesis that says act on two. This is the layer applying its own
   falsifier to itself, which it has not yet done once.
3. **The four unexamined systems** — personal-university, brand-system,
   media-log, and mpulse-dpi-team's never-run Architect (open 5). Their
   Architects are the four still unmeasured. **Where you cannot tell a miss from
   a deliberate deprioritisation, ask the human. Do not assume the first.**
4. **The feedback instruments** (open 3) and **brand-system's stale README**
   (open 2).
5. **`single-source-claims`' retirement test** (open 6), if a cycle has run at
   either origin system by then.
6. **The two spine questions the birth raised**, neither dispatchable, both
   labelled as questions rather than proposals:
   - **`charter-as-constitution` has no account of a charter whose owner is not
     the repo's owner.** At founding, `zesty-webengine-team` lives under one
     account and is charted for a different person. Does handover close this, or
     does the pattern need amending?
   - **Every system's human gate until now designed the system it gates.** This
     one's did not, and is doing the engineering as well. The spine assumes a
     level of correction it has no way to check.
7. **Draft a sharper falsifier for the engine, before the new child delivers
   anything.** The current one fires on zero births and zero promotions; quarter
   one now has one of each and **neither claim has been tested.** Writing the bar
   after results are in hand is choosing the target after the shot.

**The birth happened on 2026-08-19 and it was grown, not copied.**
`zesty-webengine-team`, targeting `zesty-io/webengine`, for a colleague who is
its Maintainer. It is the first time the generative clock has ever turned.

**Do not repeat that as a result.** It has run zero tickets and zero retros.
Claim I says a spine-grown system reaches competence *faster than a cold start*,
and competence is delivered tickets. The count moved; the claim did not. The full
entry in `meta/architect-log.md` names what would count against claim I — chiefly
**a large first-retro § Cuts, which would be evidence the spine over-specifies.**

**If another domain appears, grow it the same way.** Copying is the path of least
resistance and 2026-08-10 demonstrated that twice.

```bash
claude "Read meta/architect.md and run review 001. Full portfolio, seven systems."
```
