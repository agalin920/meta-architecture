# Systems Registry

Every system in the portfolio, what it is, and whether it is alive.

Maintained by the Meta-Architect. **Status is a decision, not an observation** —
a system with no activity is `dormant` only if someone decided that. Otherwise
it is `unreviewed`, and deciding is the Meta-Architect's job.

_Last reconciled: 2026-08-10._

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
| **First commit** | 2026-08-08 · 21 commits · 5 sessions run |

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
| **First commit** | 2026-08-08 · 62 commits · real PRs shipped |

By far the most operationally exercised system, and the only one that has
survived contact with an external world that pushes back. Source of the honest
metric, the handoff record, and the untrusted-input boundary.

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
| **First commit** | 2026-08-10 · 1 commit · no ticket run yet |

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

**Open:** `docs/decision-log.md` D-001 accepts drift from the org's shared
`agentic-development-tools` as the price of an independent pipeline, and names
`/retro`'s drift check as the only mechanism that catches it. **That is an
un-run mechanism guarding a live liability** — worth checking at the first
review whether the retro actually happens.

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
| **First commit** | 2026-08-09 · 5 commits · Session Zero run reduced; 16 pipeline items, 5 decisions logged |

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
