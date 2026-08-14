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
| **First commit** | 2026-08-08 · **24 commits** as of 2026-08-10, latest that same day · 5 sessions run at last count |

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
| **First commit** | 2026-08-08 · **138 commits** as of 2026-08-13 · real PRs shipped · **3 retros run** (08-08, 08-09, 08-13) |

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

**Open:** **zero applied rules retired**, across 138 commits and three retros
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
| **Metric** | External-reviewer blockers per PR (humans, Optibot, Copilot); routing errors |
| **Theory** | None. `docs/decision-log.md` records rationale per decision, which is not the same thing |
| **Handoff** | `tickets/PDEV-####-<slug>.md` written at every pipeline step + `docs/team-log.md` current-state header |
| **First commit** | 2026-08-10 · **51 commits** as of 2026-08-13 · **5 PDEV + 1 INFRA ticket, 7 PRs, 1 retro** (retro 001, 08-13) |

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
| **Status** | `active` |
| **Loop** | Slash commands — same six as its sibling |
| **Cadence** | Per ticket, Manager-driven |
| **Architect** | `.claude/agents/architect.md`, at `/retro` |
| **Metric** | External-reviewer blockers per PR; **did `knowledge/dpi.md` grow, and is any of it filler or wrong** |
| **Theory** | None |
| **Handoff** | `tickets/PDEV-####-<slug>.md` + `docs/team-log.md` current-state header |
| **First commit** | 2026-08-10 · 1 commit · no ticket run yet |

**Derived from zesty-eng-team**, same as its sibling, same caveat.

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
| **First commit** | 2026-08-09 · **7 commits** as of 2026-08-10 · Session Zero run reduced; 16 pipeline items, 5 decisions logged |

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
| **First commit** | 2026-08-08 · 18 commits |

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
| **Metric** | Findings a local Architect could not have made. Review 000: 2 of 5 |
| **Theory** | `meta/thesis.md` — three claims, four falsifiers |
| **Handoff** | `HANDOFF.md`, cold-start only — see the note in that file |
| **First commit** | 2026-08-09 · no review run yet |

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
