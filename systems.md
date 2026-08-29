# Systems Registry

Every system in the portfolio, what it is, and whether it is alive.

Maintained by the Meta-Architect. **Status is a decision, not an observation** —
a system with no activity is `dormant` only if someone decided that. Otherwise
it is `unreviewed`, and deciding is the Meta-Architect's job.

_Last reconciled: 2026-08-13 — **partially, and unevenly.** Review 001a re-read
`zesty-eng-team` and `mpulse-engage-team` against their repos and corrected both
entries. **The other four entries were not read and still carry 2026-08-09/10
claims.** A full reconcile is review 001's job. The distinction matters more than
it did before: this file now mixes numbers verified on three different days, and
the two freshest entries sit next to four that are four days stale._

## Status vocabulary

| Status | Means |
|---|---|
| `active` | Running its loop, meeting or missing its cadence, being watched |
| `dormant` | Deliberately parked. Someone decided. Has a revisit date |
| `dead` | Retired. Kept for its history; nothing is expected of it |
| `unreviewed` | No activity and no decision. **Not a resting state** — resolve it |
| `dataset` | Not an agentic system. Has a spec and a human gate, nothing more |

---

## personal-university

| | |
|---|---|
| **Domain** | Broad classical education for one student |
| **Status** | `active` |
| **Loop** | `agents/session-protocol.md` — plan → predict → teach → grade → log → commit, one turn |
| **Cadence** | Per session, student-driven |
| **Architect** | `agents/architect.md`, every 10 sessions |
| **Metric** | Mastery vs later review performance; school calibration error; `hard` vs `trivial` friction ratio |
| **Theory** | `meta/thesis.md` — five capacities, four named falsifiers |
| **Handoff** | `NEXT-SESSION.md`, regenerated each session |
| **First commit** | 2026-08-08 · **31 commits** as of 2026-08-18 · 5 sessions run at last count · **not opened by this layer since 2026-08-13** |

The most architecturally complete system in the portfolio and the source of most
of the catalog. The only one with a falsifiable theory of what it produces.

**Open:** thesis capacity 3 (calibration) lost its training mechanism on
2026-08-09 when the student's prediction was cut. Recorded as an open gap, not
resolved.

---

## zesty-eng-team

| | |
|---|---|
| **Domain** | Engineering delivery on `zesty-io/manager-ui` |
| **Status** | `active` |
| **Loop** | Slash commands — `/take-ticket`, `/review-pr`, `/triage`, `/standup`, `/retro` |
| **Cadence** | Per ticket, Director-driven |
| **Architect** | `.claude/agents/architect.md`, at `/retro` |
| **Metric** | CI-reviewer blockers per PR; Director findings per ticket — both with a named `unmeasured` category |
| **Theory** | None. `docs/decision-log.md` records rationale per decision, which is not the same thing |
| **Handoff** | `tickets/<issue#>-<slug>.md` written at every pipeline step + `docs/team-log.md` current-state header |
| **First commit** | 2026-08-08 · **196 commits** as of 2026-08-18 · real PRs shipped · **5 retros run** (08-08, 08-09, 08-13, 08-14, 08-18) |

By far the most operationally exercised system, and the only one that has
survived contact with an external world that pushes back. Source of the honest
metric, the handoff record, and the untrusted-input boundary.

**The only Architect in the portfolio with a track record** (review 001a). It has
graded its own prior cycle proposal by proposal, **falsified one of its own
proposals** (P8, four further instances after it landed, replaced by `1646f8b` at
a narrower scope), and corrected two false statements it had itself committed
hours earlier. That is the first direct evidence anywhere that the
propose-never-apply loop does anything — and it is also evidence *against* thesis
claim IV, which says nobody scores the scorers. Recorded as such.

**Its improvement loop gained an adversary on 2026-08-13** (`ac65e24`): `/retro`
step 2 dispatches a second `architect` against pass 1's report. On its first run
it found that the prescribed evidence command could not see the auto-reviewer's
findings at all — **three retros had scored that gate 0.00 against a true 0.83
on n=6.** Six of retro #3's 13 applied changes came from pass 2. Its retirement
test is retro #4 and has not returned.

**Its retirement test has now returned twice, and it survives.** At retro #4 and
again at retro #5 the second pass produced material findings — at #5 it corrected
the headline metric 1.50 → 2.00, found a counting defect running the opposite
way, and **caught pass 1 proposing to delete a standing blocker that is true.**
The test *"nothing material two retros running"* is, in that team's own words,
*"nowhere near met."* It remains a **one-adopter** mechanism: mpulse-engage-team
has declined it twice, both times on its own evidence.

**Closed 2026-08-18:** ~~zero applied rules retired~~, across 138 commits and three retros
(+155/−47 on instruction files, every deletion a replacement or renumbering).
And **no overhead tripwire** — `overhead-ceiling` is `proven` and this system is
❌. Both were carried in `proposals/2026-08-13-zesty-eng-team.md`, **dispatched
2026-08-13.** Its Architect **accepted the § Cuts section** (with a required
two-state clause of its own) and **rejected the ceiling**, on the grounds that the
line count this layer proposed capping is not a read path: a ticket session there
reads **1,474 lines**, not 777, and the growth is in `team-log.md` (93→547) and
`knowledge/` — files the proposed cap excluded. **The rejection is correct and the
gap it names is its own:** `CLAUDE.md:90` tells the architect to condense
`team-log.md` at a retro, has no number, and has never fired.

**Distinguishing fork:** the only system using context-isolated subagents rather
than roles adopted in sequence. Correct for its domain — real filesystem
isolation and a reviewer that genuinely did not write the diff. Do not propose
converging this.

---

## mpulse-engage-team

| | |
|---|---|
| **Domain** | Engineering delivery on the mPulse Engage platform — ~30 repos, Jira project `PDEV` |
| **Status** | `active` |
| **Loop** | Slash commands — `/take-ticket`, `/review-pr`, `/address-feedback`, `/triage`, `/standup`, `/retro` |
| **Cadence** | Per ticket, Manager-driven |
| **Architect** | `.claude/agents/architect.md`, at `/retro` |
| **Metric** | External-reviewer blockers per PR (humans, Optibot, Copilot); routing errors; escape rate, bucketed. **Both denominator cuts reported when they disagree**, and context cost stated as a floor |
| **Theory** | None. `docs/decision-log.md` records rationale per decision, which is not the same thing |
| **Handoff** | `tickets/PDEV-####-<slug>.md` written at every pipeline step + `docs/team-log.md` current-state header |
| **First commit** | 2026-08-10 · **103 commits** as of 2026-08-18 · **7 PRs + 5 more in the 08-15→08-17 window, 2 retros** (001 on 08-13, 002 on 08-18) |

**Derived, not independently arrived at.** Structure adapted directly from
zesty-eng-team on 2026-08-10. See the note in `patterns/README.md` — its column
in the adoption matrix is **not** convergence evidence.

Three genuine divergences from its source, each forced by the domain:

- **Routing is a first-class pipeline step and a gate.** zesty-eng-team targets
  one repo. This targets ~30, and the expensive failure is building the right
  thing in the wrong service.
- **PHI boundary.** HIPAA platform, permanent git history. No equivalent exists
  in any other system in the portfolio.
- **Human engineers share the target repos and the ticket tracker.** No other
  system in the portfolio operates in a space where a collision costs a
  colleague their afternoon. It is why its operating rules are stricter than a
  solo-agent team's would be.

**The first copy in the portfolio to invent rather than drop** (review 001a).
Everything the catalog predicted about copies is about what they *lose*. This one
built four tools on 2026-08-13 and now holds two patterns its parent lacks:

- **`tools/verify_docs.py`** (244 lines) — docs embed the command that
  established a claim as an HTML comment, and **the claim is re-run rather than
  reread.** Six assertions pinned, re-run 6/6 passing at review 001a. It answers
  a real failure: *one measured fact, four files, three values, three days*
  (`3cfe318`).
- **`tools/gates.py`** (157 lines) — every gate emits `PASS/CAUGHT/SKIP/BLOCKED`
  into the ticket worklog, and `CAUGHT` is the only evidence a gate is
  load-bearing. Its own diagnosis is the best sentence in either engineering
  repo: *"the system could observe its own outputs but not its own mechanism."*
- **A 1,300-line budget on the per-ticket read path**, machine-asserted. **The
  only overhead tripwire in either engineering team.**

**It also independently re-derived the metric fix it did not inherit.** It took
ZET's blockers-per-PR *with the flaw* — both mPulse copies dropped the
`unmeasured` category — then diagnosed the fault itself (*"a denominator the team
does not control... gameable in the wrong direction"*) and built a **different**
remedy: coverage reported beside every count, D-019 excluding the release PR from
the denominator by name, and a move toward **escape rate**. Review 001a ruled
that this counts as independent evidence; see `patterns/README.md` § The
independence bar and copies that re-derive.

**And it independently invented the carry-packet.** `/retro` § 7: *"Do not edit
the other team's repo. Report it and let him carry it across."* That is
`meta/dispatch.md`'s rule, arrived at one level down by a system that has never
read this repo.

**Open:** **zero applied rules retired** (+209/−21 on instruction files in three
days, every deletion a replacement). **Neither tool has produced data yet** —
`gates.py` reports 12 of 12 declared gates unrecorded, and the read-path cap is
1,300 against a current 1,056, so it has never bound. The instruments exist and
the evidence does not. And **no step that grades the previous cycle's proposals**,
which is the thing its sibling does that produced all the portfolio's best
evidence. All carried in `proposals/2026-08-13-mpulse-engage-team.md`,
**dispatched 2026-08-13.** Its Architect **accepted the prior-cycle grading step,
the lower read-path cap (1,100), and the overhead ratio line** — and **rejected
mandatory subtraction and the second adversarial pass**, both on evidence this
layer had not gathered. **Both rejections were right.** See the correction to the
first below.

**Correction to review 001a, from that rejection:** this layer claimed the
subtraction question was going unasked here. **It is not.**
`.claude/agents/architect.md:124` mandates a **§ Cuts** section — *"do not skip
this section — if nothing should be cut, say so and say why you believe it"* — and
retro 001 produced one, proposed C3, and **the judging step rejected it with a
recorded reason** (`docs/team-log.md:420`). Zero rules retired is still true; *the
question never being asked* is not. Asked-and-answered is a different failure mode
with a different remedy.

**The never-edit-a-sibling rule is enforced here at the permission layer, not in
prose.** `.claude/settings.json` denies `Edit`/`Write` on
`../mpulse-dpi-team/**`, `../dpi/**`, and `../agentic-development-tools/**` — the
sibling team, the product repos, and the shared org toolkit it does not control —
alongside push denials on six service repos. **That is `human-gate` implemented as
a harness constraint rather than an instruction**, and it is the strongest form of
the pattern anywhere in the portfolio: it does not depend on the agent complying.
(Noted in passing: the `Write(...)` deny lines are inert — the harness matches only
`Edit(path)` for file writes — but every path here carries both, so the guard
holds.)

**Resolved:** D-001's drift check — registered at review 000 as *"an un-run
mechanism guarding a live liability"* — **ran on 2026-08-13 and found real
drift** (`047dd6b`, D-018 and D-019). The open question is now whether it runs
*again*; a check that fires once is not yet a mechanism.

---

## mpulse-dpi-team

| | |
|---|---|
| **Domain** | Engineering delivery on DPI — 4 repos under `dpi/`, Jira project `PDEV` |
| **Status** | `active` — **low-cadence, by decision** (human, 2026-08-14): runs when DPI work arrives; quiet windows are not misses |
| **Loop** | Slash commands — same six as its sibling |
| **Cadence** | Per ticket, Manager-driven |
| **Architect** | `.claude/agents/architect.md`, at `/retro` |
| **Metric** | External-reviewer blockers per PR; **did `knowledge/dpi.md` grow, and is any of it filler or wrong** |
| **Theory** | None |
| **Handoff** | `tickets/PDEV-####-<slug>.md` + `docs/team-log.md` current-state header |
| **First commit** | 2026-08-10 · **14 commits** as of 2026-08-18 · onboarding kit + local-setup work · **0 retros, ever** |

**Derived from zesty-eng-team**, same as its sibling, same caveat.

**Ruled 2026-08-14 by the human: the quiet is deliberate.** DPI gets little
work by the shape of his job, not by neglect — the exact ambiguity
`meta/architect.md` § 1 says this layer cannot resolve alone, now resolved.
Do not read low commit counts here as a cadence miss.

**The standing wake-up item is DISCHARGED, verified 2026-08-18.** It read: *the
first session that opens this repo fixes the four command files still routing
Jira through the dead MCP — `take-ticket.md:10` carries a false PHI-sanitization
claim (DF-1) — before any `/take-ticket` runs.* It was fixed at `7888bb3`
(2026-08-14), before this layer next looked.

> **Check, executed 2026-08-18 in `../mpulsemobile/mpulse-dpi-team`:**
> `grep -rn -i "mcp|sanitiz|jira" .claude/commands/*.md` → `take-ticket.md:10`,
> `review-pr.md:19`, `triage.md:10` and `standup.md:12` **all** route through
> `python3 tools/jira.py` and each says *"not the `jira` MCP server"*. The false
> claim at `take-ticket.md:10` is gone and `:17` now carries the true one:
> **"Nothing sanitizes this output."**

**So MDT is eligible for proposals again**, for the first time since the
2026-08-14 low-cadence ruling. Its wake-up item no longer precedes anything.

**Two things about it are worth a review's attention, and neither is a cadence
miss.** First: **it has run zero retros in its entire history**
(`git log --all --oneline | grep -ci retro` → `0`, checked 2026-08-18), so its
Architect is the only one in the portfolio that has never executed and its
knowledge-gate candidate in `patterns/README.md` **cannot be graded** — the
grading step does not exist. Second: it states the PHI-sanitizer fact in **four
places** (`operating-rules.md:13`, `team-log.md:116`, `CLAUDE.md:53`,
`take-ticket.md:17`), with three further command files pointing at
`operating-rules.md § PHI`. The copies agree today, checked. It is a
safety-critical claim on a HIPAA platform held in four copies in the one repo
with no retro to catch drift — the exposure both sibling teams got burned by on
2026-08-18. See `patterns/single-source-claims.md`.

**The one thing here that is genuinely new to the portfolio:** documenting the
product is a *gate*, not a byproduct (`docs/decision-log.md` D-003). DPI has no
`CLAUDE.md` in any repo, no coverage in the org's shared tooling, and READMEs
that are actively wrong — `dp-auth`'s claims Django 1.11 on Python 3.5 against a
Pipfile pinning 4.2.11 on 3.12. So `knowledge/dpi.md` is a charter-level
deliverable and gate 9 of its definition of done.

D-003 also names the failure mode it creates, which is the part worth watching:
**a mandatory entry every ticket invites filler** — restating what the diff
already shows so the box gets ticked, which is worse than absence because it
dilutes the file. Its architect is instructed to check for filler as hard as for
absence, and to spot-check the facts against code.

**This is a candidate pattern.** *Knowledge accumulation as a gate rather than a
habit* is not in the catalog. It has one adopter, zero evidence, and an
identified failure mode — `provisional` at best, and it should not enter
`patterns/` until review 001 has seen whether it produces knowledge or filler.

---

## brand-system

| | |
|---|---|
| **Domain** | Public presence for galind.io — writing, projects, engagement |
| **Status** | `active` |
| **Loop** | `agents/cycle-protocol.md` — orchestrate → execute → critique → gate → log → distribute → measure |
| **Cadence** | Weekly |
| **Architect** | `agents/architect.md`, every 4 weeks |
| **Metric** | Receipts ratio; resonance over reach; human-originated items per window; Critic anyone-else count |
| **Theory** | None. A risk table with tripwires, which is failure modes rather than falsifiers |
| **Handoff** | **None.** `pipeline.md` item states imply progress but nothing records mid-cycle position |
| **First commit** | 2026-08-09 · **10 commits** as of 2026-08-18 · Session Zero run reduced; 16 pipeline items, 5 decisions logged · **not opened by this layer since 2026-08-13** |

Youngest system. One day old at first registry entry — **do not read low commit
count as stalling yet.**

**Changed 2026-08-09:** gained the Critic (independent adversary) and the
untrusted-input boundary, both adopted from the catalog.

**Open:** no handoff record — see `patterns/handoff-record.md`. And `README.md`
says Session Zero has not been run while the repo shows it partially has; see
the first Meta-Architect log entry.

---

## media-log

| | |
|---|---|
| **Domain** | Personal media-consumption database |
| **Status** | `dataset` — not an agentic system |
| **Loop** | None. `CLAUDE.md` is an ingestion spec |
| **Cadence** | None. Ad hoc |
| **Architect** | None, correctly |
| **Metric** | None needed |
| **Handoff** | The CSV is the state |
| **First commit** | 2026-08-08 · **18 commits**, unchanged since 2026-08-09 — correct for a dataset |

**Registered so it stops reading as a gap.** It is a dataset with a spec and a
human gate on spec changes — the spine's degenerate case, and evidence the
pattern reproduces at every scale. It correctly has no Architect and should not
acquire one.

The Meta-Architect checks one thing here and nothing else: **is the controlled
vocabulary drifting?** Variant spellings, single-use `type` values, a `status`
enum nobody uses. That is a ten-minute read, not a review.

---

## meta-architecture

| | |
|---|---|
| **Domain** | The portfolio itself — patterns, distribution, the Architects |
| **Status** | `active` |
| **Loop** | None, deliberately. A review is not a loop |
| **Cadence** | Quarterly, never more often than the fastest child Architect |
| **Architect** | `meta/architect.md` — it reviews itself, which is the known weak point |
| **Metric** | Superseded 2026-08-14 by the engine's scoreboard (`meta/thesis.md`): **births 0, promotions 1, transfer yield 4 of 7.** The old auditor's metric — findings a local Architect could not have made — was 2 of 5 at review 000 and 5 of 8 at 001a |
| **Theory** | `meta/thesis.md` — three claims, four falsifiers |
| **Handoff** | `HANDOFF.md`, cold-start only — see the note in that file |
| **First commit** | 2026-08-09 · **17 commits** · **one scoped review (001a, 08-13)**; review 001 undischarged. Three scoped reads of the same two children (08-13, 08-14, 08-18) — see the cadence note in `meta/architect-log.md` |

**Listed in its own registry on purpose.** A layer exempt from its own catalog
is precisely the thing it would flag in a child, and the entry it is missing is
the honest one: **nothing audits this layer.** It audits the four Architects
below it and there is no fifth level, correctly — the kill condition in
`charter.md` is the substitute, and it is deliberately mechanical so the
judgement does not depend on the thing being judged.

Its own gaps, by the catalog's matrix: no independent adversary, no honest
metric with an `unmeasured` category, no named failure-mode table. **All three
are probably correct absences** for something that runs four times a year and
produces only findings — but they are absences, and review 001 should say so
rather than leaving the layer unassessed.

---

## zesty-webengine-team

| | |
|---|---|
| **Domain** | Engineering delivery on `zesty-io/webengine` — one repo, PHP, GitHub issues |
| **Status** | `active` — **founded 2026-08-19, nothing exercised yet** |
| **Loop** | Slash commands — `/take-ticket`, `/review-pr`, `/standup`, `/retro` |
| **Cadence** | Per ticket, Maintainer-driven |
| **Architect** | `.claude/agents/architect.md`, at `/retro`. **Never run** |
| **Metric** | Blockers per PR from reviewers the team does not control; Maintainer findings per ticket. Five named `unmeasured` categories from day one |
| **Theory** | None, correctly. A system that does work does not need a thesis |
| **Handoff** | `tickets/<issue#>-<slug>.md` written at every step + `docs/team-log.md` current-state header |
| **First commit** | 2026-08-19 · 1 commit · **0 tickets, 0 retros** |

**THE PORTFOLIO'S FIRST BIRTH. Grown from `spine.md`, not copied.** Every prior
system is either one of the founding four or a derived copy, which is why claim I
of `meta/thesis.md` has had zero evidence since the layer was created.

**The `†` discount does not apply and neither does the `carried` case.** This
system was derived from the spine's reasoning by a session that read it as a
resource. **What it is not yet is evidence for claim I** — that requires reaching
competence, and it has run zero tickets.

**Three things it did that its would-be parent does not**, each traceable to
deriving from reasoning rather than copying a file:

- **`unmeasured` categories tuned to its own domain**, present at founding: base
  branch not `master` (no CI, no bot), CI failing network-shaped against the ~10
  live staging origins the integration suite depends on, no external review
  recorded, PR closed unmerged, bot skipped a draft. A copy would have inherited
  zesty-eng-team's categories, which describe a different repo.
- **The metric identifies external reviewers structurally** — *not the PR author,
  no team marker* — rather than by handle. Forced by the human's instruction that
  no personal name enter the repo, and **the constraint produced a better rule
  than the parent's.** Machine-asserted (`no-hardcoded-human-identity`).
- **It starts on the correct GitHub endpoint.** `gh pr view --comments` cannot
  return inline review comments; that mistake scored zesty-eng-team's review gate
  **0.00 for three consecutive cycles.** Written into `knowledge/ci-and-review.md`
  as a rule rather than rediscovered.

**Its human gate is not Andres.** First system in the portfolio where the person
approving the work did not design the system and is doing the engineering too.
`docs/charter.md` § Who the Maintainer is states the consequence rather than
leaving it to be discovered: the Maintainer's corrections are the highest-grade
signal the loop receives, and a cycle with none is recorded `unmeasured`, not
clean.

**What review 001 should actually look at**, and it is not whether the founding
documents are good:

1. **Did its first retro cut most of what the spine talked it into?** Several of
   its rules are predictions made before anything went wrong. **A large first-retro
   § Cuts is evidence the spine over-specifies** — evidence about the spine, not
   about the child.
2. **Did the birth cost more than it returned?** It took materially longer than a
   copy. Claim I says that buys faster competence. Nobody has measured it.
3. **Does the gate hold when the gatekeeper is not the designer?** Two consecutive
   cycles with zero Maintainer findings is the tripwire, and it is the one this
   system is most likely to trip.

**Repository ownership is deliberate and temporary:** it lives under `agalin920`
so it can be handed over, and the Maintainer clones it. **That means the charter's
owner and the repo's owner are different people at founding**, which is a real gap
in the `charter-as-constitution` pattern that no existing system has hit. Review
001 should decide whether the pattern needs amending or whether handover closes it.

---

## galind-team

| | |
|---|---|
| **Domain** | Building **Galind** — an agent-native backend suite — from a strategy brief to a shipped product |
| **Status** | `active` — **founded 2026-08-22, nothing built** |
| **Loop** | Slash commands — `/decide`, `/take-item`, `/review`, `/standup`, `/retro` |
| **Cadence** | Per work item, Director-driven. `/retro` every third item **or on the F1 tripwire**, whichever comes first |
| **Architect** | `.claude/agents/architect.md`, at `/retro`. **Never run** |
| **Metric** | Director findings per work item; **machine share** (system commits ÷ system + product). Six named `unmeasured` categories, including the Director's own miss rate |
| **Theory** | `docs/thesis.md` — three claims, each with falsifiers. **Correctly has one**: this system claims an outcome rather than only doing work |
| **Handoff** | `tickets/<id>-<slug>.md` written at every step + `docs/team-log.md` current-state header + `HANDOFF.md` |
| **First commit** | 2026-08-22 · 1 commit (`00e59c6`) · **0 work items, 0 retros, 0 product repos** |

**THE PORTFOLIO'S SECOND BIRTH, three days after the first.** Grown from
`spine.md`, not copied. Full entry in `meta/architect-log.md`.

**It is a harder test of claim I than `zesty-webengine-team` was**, and the reason
is structural rather than a matter of quality. That birth landed in the
portfolio's best-populated domain — engineering delivery on an existing repo —
where a copy of `zesty-eng-team` was a live alternative and two siblings existed
to check it against. **This one has no sibling.** No tracker, no product, no
external reviewer, no user, and its first job is deciding what to build. The
spine had to carry the whole load unaided.

**The product is deliberately not in the repo.** `~/dev/galind/galind-team` is the
system; `~/dev/galind/galind-<module>` repos are subjects and **none exists yet**,
by its `D-007`. The separation was ruled structural, not conventional: it is what
makes the machine/product ratio observable at all.

**Three things it does that no existing system does:**

- **`tools/ledger.py` — a named failure mode with a real corpse behind it.** F1 is
  *building the machine instead of the product*, and unlike every other instance
  of that name in the portfolio it is not a prediction. There was a **previous
  `galind`** — an agent-run company on the Agent SDK whose stated first mission
  was to discover its own product, now a backup tarball, whose own README reads
  *"We built the machine before deciding what it makes — on purpose."*
  (`../brand-system/inventory.md:46`, `:144`, `:155`, checked 2026-08-22.) The
  script counts system commits against product commits, or days elapsed while no
  product repo exists.

  **`zesty-webengine-team` independently invented a ratio of the same family**
  four days earlier — *a cycle where `retro:` commits outnumber merged PRs*
  (`docs/charter.md:87`, checked 2026-08-22) — and neither system read the other.
  **They are not the same instrument.** WET counts inside one repo, because it
  operates on a product that already exists. This one counts across repos, and
  has a second mode counting days elapsed with no product repo at all, because
  its product does not exist. **One measures a team drifting from work it has;
  the other measures a team never starting.** Two independent adopters, zero
  fired tripwires — a promotion-gate candidate for review 001, not a pattern.
- **The independent adversary runs against strategy proposals, not only diffs.**
  Its reasoning is that a proposal becomes a ruling and rulings are what the
  product is — the same generalisation `patterns/README.md` records as an open
  spine question, arrived at independently and pointed at a different output. One
  agent with two modes, not a second agent (`D-006`); the spine's default of *no*
  held.
- **A gate whose irreversibles are not code-shaped** — money, DNS, publishing,
  credentials, and **sending email to a real address**, named first among the
  technical items because sending reputation damages permanently. `curl` and
  `wget` are denied at the permission layer on the stated reasoning that a send
  is an HTTP POST while reading the web goes through `WebFetch`.

**Two founding cuts, and they are the more interesting half.** It declined a
`proven` pattern (`overhead-ceiling`, on test 1 — nothing has grown to cap) and a
`provisional` one (executable claims, on test 2 — with ten docs and zero cycles,
reading them is cheaper), **both with recorded triggers to revisit.** **`zesty-webengine-team` adopted both of them at founding** — a 900-line
read-path cap asserted by its own `tools/verify_docs.py` (checked 2026-08-22).
**So the two spine-grown births made opposite calls on the same two mechanisms,
four days apart, without reading each other.** That is the first sign the spine is
being *read* rather than complied with, and it bears directly on claim I's second
falsifier. Which call was right is not knowable yet; review 001 should grade both
against their first retros, and *each was right locally* is a legitimate outcome
that would be evidence the three tests work.

**What review 001 should look at, and it is not the founding documents:**

1. **The size of its first `§ Cuts`.** Every rule in it is a prediction made
   before a work item ran. A large cut is evidence the spine **over-specifies** —
   about the spine, not the child. Same test the first birth is under.
2. **Whether the F1 tripwire fired on its own founder.** `ledger.py` reports
   `0 / 14` days and `1 / 25` commits at founding. If it spends its first
   fortnight improving itself, the detector it invented caught its own author,
   and the spine grew a machine that produces machines.
3. **Whether the two cuts were reversed at retro 1.** Immediate adoption of what
   it declined would mean the declines were performed discipline rather than
   exercised discipline.

**Its gate is Andres, who is also the product owner and the only user.** Unlike
`zesty-webengine-team` — where the gate is someone who did not design the system —
here the gate designed it, owns the domain, and is the sole source of feedback.
Its charter names that as F4 and records a cycle with zero Director corrections as
`unmeasured` rather than clean. **Two of the eight systems now state a
gate-shaped failure mode, from opposite causes**, which is a question for the
spine and not a defect in either.

**Open:** `galind.io` is claimed by two systems. Andres ruled 2026-08-22 that the
product takes it and `brand-system` moves; **the ruling has not been executed** and
is carried in `proposals/2026-08-22-brand-system.md`. `brand-system` uses the
string as its own name in three files, so it is a rename and not a DNS change.
Registered here because a decision made and not executed is what gets
rediscovered as a surprise.

---

## the-debrief

| | |
|---|---|
| **Domain** | Building **The Debrief** — an interactive corpus of every discovery, invention, work and mind that changed what humanity knew, chronological and geographically anchored |
| **Status** | `active` — **founded 2026-08-24, zero entries** |
| **Loop** | Slash commands — `/slice`, `/verify`, `/standup`, `/retro` |
| **Cadence** | Per slice, Director-driven. `/retro` every third slice **or on the F1 or F2 tripwire**, whichever comes first |
| **Architect** | `.claude/agents/architect.md`, at `/retro`. **Never run** |
| **Metric** | Entries shipped and rejected per slice; adversary findings and downgrade rate; **Director findings, and whether they came from inside the gate sample or outside it**. Six named `unmeasured` categories, the first of which is the project's entire point |
| **Theory** | `docs/thesis.md` — three claims, each with observable falsifiers, plus a § stating what the system structurally cannot test |
| **Handoff** | `slices/<NNN>-<slug>.md` written at every step + `docs/project-log.md` current-state header + `HANDOFF.md` |
| **First commit** | 2026-08-24 · **2 commits** · **0 slices, 0 retros, 0 entries, no site** |

**THE PORTFOLIO'S THIRD BIRTH, two days after the second and five after the
first.** Grown from `spine.md`, not copied. Full entry in `meta/architect-log.md`.

**It is worth less as evidence than either predecessor and it says so itself.**
The first two births were run by sessions that had not read each other. **This one
was run from inside this layer**, by a session that had read the spine, the
catalog, both prior birth entries and both children's founding decisions. Every
choice it shares with a sibling is a **`carried` adoption**. Three are labelled as
carries in its own `docs/decision-log.md` at founding.

**The one that matters here:** its `tools/audit.py ledger` is a third instance of
the improvement-versus-delivery ratio family. **It must not be counted as a third
adopter** — the promotion-gate candidate recorded on 2026-08-22 still stands at
two independent inventions. Its `D-006` says so; so does the log entry; so does
this row.

**The gap it opened, and it is the reason the birth was worth running:** this is
**the first system in the portfolio whose human gate cannot scale with its
output.** Every other gate reviews a diff, a ticket, a draft, a pipeline, a CSV
row — volume that fits a person. This one will hold thousands of factual claims
about human history and has one reviewer.

`patterns/human-gate.md` is about **irreversibility** and is silent on
**unreviewable volume**, which is a different failure: the history is perfectly
revertible and the gate fails anyway, because a gate asked to approve more than it
can read approves it. **The consequence is worse than in a delivery system** — a
rubber-stamped corpus ships a confidently wrong artifact whose whole pedagogical
claim is that the reader builds a structure from it.

**Its answer is a bet, written down as `D-002` so it can be graded:** the gate is
on the *slice*, and the independent adversary **nominates the gate sample** — 8 to
12 entries weighted toward what it could not confirm, contested and lost, marked
manufactured, or judged a link of convenience, plus one or two it is confident
about, unlabelled. The grading instrument is specific: **did the Director's
findings come from inside the sample or outside it.**

**Two more things no sibling does**, both forced by the domain:

- **`verification` is a first-class field the product must render.** The
  `honest-metric` `unmeasured` discipline pushed **out of the log and into the
  artifact** — `verified` / `contested` / `unverified`, with `unverified`
  shippable and the charter forbidding any implication of unearned confidence.
  Every prior instance of that pattern keeps its honesty in a metric section
  nobody outside the system reads. **First time it is a user-visible property of
  the output.**
- **A coverage floor rather than a proportion.** A proportion is satisfiable by
  deleting European entries, which improves the number and the corpus not at all.
  It also names what the instrument cannot do — it counts regions in a declared
  vocabulary, so unexamined traditions read as absent and the audit reports clean
  — and files that under `unmeasured`.

**A cross-system disagreement, found at founding and deliberately not settled.**
`personal-university` covers overlapping subject matter and holds the opposite
position on the mechanism both rest on.

> **Check, 2026-08-24 in `../personal-university`:** `curriculum/history.md:5` —
> *"Organized by mechanism, not by chronology... No survey courses."*
> `progress/connections.md:8` — *"A connection handed over is a nice sentence
> he'll forget."* `git ls-files | grep -E '\.json$|^data/|\.csv$'` → **no
> output** — no corpus to reuse, and not a duplicate.

The new system is a chronological survey whose headline feature hands the reader
the connections. **Nothing was dispatched to `personal-university` and it was not
corrected** — `charter.md` § Never own a system's domain. The tension is written
into the new system's own thesis with both quotes, and its Architect is told to
treat the tension quietly vanishing from that file as a finding. **Review 001
decides whether it is two purposes or one error.**

**Its detector falsified itself on day one**, the third instrument in the
portfolio to do so: the ledger counted the founding commit as product work on the
strength of `data/README.md` and `src/README.md`. Corrected, recorded, not
smoothed away.

> **Check, 2026-08-24:** `python3 tools/audit.py selftest` → `18/18 passed`;
> `corpus` → `0 entries · 0 stop, 0 note`; `ledger` → `0 product, 1 machinery`.

**Founded with zero corpus entries, deliberately and for two reasons.** Founding a
system is not doing its work — and **a session sitting in this layer writing
corpus content would be the meta layer doing a child's domain work.** The
consequence, an untested validator, was handled with an in-memory `selftest`
rather than by admitting content through the back door.

**No git remote**, same as `galind-team`; `gh repo create` denied at its own
permission layer, so creating one is Andres's call.

**Its gate is Andres**, who is also the editorial owner and the only reader.
**Three of ten systems now state a gate-shaped failure mode, from three different
causes** — a gate who did not design the system (`zesty-webengine-team`), a gate
who is also the only user (`galind-team`), and a gate who cannot read the output
(this one). That is a question for `patterns/human-gate.md` and not a defect in
any of the three.

## resale-desk

| | |
|---|---|
| **Domain** | What second-hand goods are worth, both directions — appraising Vinted listings to flip or to keep, and drafting the listings that sell what Andres owns |
| **Status** | `active` — **founded 2026-08-29, zero units, zero pounds** |
| **Loop** | Slash commands — `/source`, `/list`, `/settle`, `/standup`, `/retro` |
| **Cadence** | **Every tenth resolved unit, or any charter tripwire.** Deliberately not a calendar — the unit of learning is a resolved trade and time does not produce those |
| **Architect** | `.claude/agents/architect.md`, at `/retro`. **Never run** |
| **Metric** | Realized margin per resolved unit, and appraisal error (predicted sale against realized gross), reported signed in both directions. `flip` and `keep` never averaged (D-009). `unmeasured`: Andres's hours, and any unit missing an observed fee |
| **Theory** | `docs/thesis.md` — four claims, each with a falsifier, plus a § on the structural condition that forced two control groups |
| **Handoff** | `desk/events.jsonl` (append-only, the fact) + `desk.py state` (derived) + `HANDOFF.md` (narrative, forbidden from restating a computed number) |
| **First commit** | 2026-08-29 · **2 commits, 21 files, 1,802 lines** · 0 candidates, 0 units, 0 listings, 0 retros |

**THE PORTFOLIO'S FOURTH BIRTH, in eleven days.** Grown from `spine.md`. Full
entry in `meta/architect-log.md`, which leads with the birth rate rather than
with the system, because at four that is the larger fact.

**Worth as little as the third for claim I, for the same reason** — run from
inside this layer by a session that had read the spine, the catalog and all three
prior birth entries. Three founding decisions are labelled `carried` in its own
`docs/decision-log.md` (D-005 dependency-free Python, D-007 no read-path cap with
a trigger, D-012 zero content at founding).

**It declined to build a fourth ratio detector, on purpose** (`D-006`). It has the
failure mode and three siblings have the instrument. It was cut because a fourth
instance, built by a session that had read all three, would put a data point that
looks like convergence into the exact promotion-gate decision where a miscount
does damage. **That is a child being designed around this layer's measurement
problem, and whether that is discipline or contamination is a question for review
001.**

**The gap it opens, and the reason the birth was worth running: this is the first
system whose charter contains clauses the human does not own.** Rules 1 and 2 —
never transact, never publish — are quoted verbatim from Vinted's stated
conditions of access, retrieved 2026-08-29, not authored by Andres.

`patterns/charter-as-constitution.md` rests on a charter being **the fixed point
the system is measured against, human-owned, changeable only by him.** Here part
of that fixed point belongs to a third party, **can change without notice, and no
ruling by Andres can amend it.** He cannot decide that Vinted permits automated
purchases. That is a different failure from the two already on the record — a gate
who did not design the system (`zesty-webengine-team`) and a gate who cannot read
the output (`the-debrief`) — and it is the first one where the charter itself has
an owner outside the portfolio.

**And it is the first system whose feedback is censored.** It only ever observes
the outcome of what Andres actually bought; a flip it passed on sells to someone
else and the desk never learns. False positives are measurable, **false negatives
are structurally invisible**, and a desk under that condition gets steadily more
timid while every number it reports improves. Its answer is two control groups
built at founding — a decline sample with re-check dates, and one blind unlabelled
control item per session (`D-011`). Both cost Andres a step per session and both
are on tripwires for that reason.

**No git remote, and the reason is not the sibling convention.** `desk/events.jsonl`
will hold what he paid for things and what he earns doing this. That is personal
financial history, and a private remote is still a copy on someone else's disk.

**Facebook Marketplace was in the founding ask and is out of scope**, on a check
rather than a judgment: `facebook.com/robots.txt` is `Disallow: /` with no
exception for `/marketplace`, behind authentication. The trigger that would open
it is stated (`D-003`) and the manual path — Andres pasting listings himself — is
available today and is not the desk fetching anything.

## Not in the portfolio

`manager-ui` and `studio-bridge` are product repos that zesty-eng-team operates
on. The ~30 `mpulsemobile` service repos and the four DPI repos under `dpi/` are
the same thing for the two mPulse teams. They are subjects, not systems. Nothing
here governs them and the Meta-Architect does not read them.

`agentic-development-tools` is a harder case and is deliberately **not**
registered. It is an agent-tooling repo — skills, hooks, domain agents, a PHI
sanitizer — which makes it look like a portfolio system. It is not one:
**mpulsemobile owns it, other engineers depend on it, and the human cannot
unilaterally change it.** Every system in this registry rests on a single human
gate that makes it reviewable and revertible. That property does not hold here,
so nothing in this layer applies to it and the Meta-Architect does not review
it.

It does matter to the portfolio in exactly one way: both mPulse teams
deliberately diverge from it, and both accept drift as a cost. That is recorded
against those systems, not as an entry of its own.


---

## Distribution, measured 2026-08-18

Counted with `git log --oneline | wc -l` per repo, not derived from prior
figures. **Two numbers in an earlier draft of this file were derived by adding a
window count to a stale total and both were wrong** (ZET 181 vs a true 196, MET
92 vs 103) — recorded because it is the same defect both engineering teams spent
their retros on, appearing here.

| System | Total commits | Since 2026-08-14 | Last commit |
|---|---|---|---|
| zesty-eng-team | 196 | 43 | 2026-08-18 |
| mpulse-engage-team | 103 | 41 | 2026-08-18 |
| mpulse-dpi-team | 14 | 9 | 2026-08-18 |
| personal-university | 31 | 1 | 2026-08-18 |
| brand-system | 10 | 3 | 2026-08-16 |
| media-log | 18 | 0 | 2026-08-09 |
| **meta-architecture** | 17 | 3 | 2026-08-15 |
| zesty-webengine-team | 1 | 1 | 2026-08-19 · **founded** |

**84 of the 101 commits since 2026-08-14 are in the two mPulse/Zesty delivery teams**, and
those are the two repos this layer has now read three times running. **That is
attention being followed, not audited** — `meta/architect.md` § 1 says the shape
over time is the signal, and the shape has been the same shape three times.

**What this table cannot tell you**, and must not be read as telling you: whether
personal-university's 1 commit and brand-system's 3 are misses or deliberate.
There is no stated capacity here — it was cut on 2026-08-09 and must not be
reintroduced — so *"they slipped"* and *"they were deprioritised"* look identical
from this layer. **mpulse-dpi-team is the one case where the ambiguity is
resolved**, by the human's ruling of 2026-08-14, and it resolved to deliberate.
The other two are open questions for review 001 and are questions for the human,
not findings.
