# Systems Registry

Every system in the portfolio, what it is, and whether it is alive.

Maintained by the Meta-Architect. **Status is a decision, not an observation** —
a system with no activity is `dormant` only if someone decided that. Otherwise
it is `unreviewed`, and deciding is the Meta-Architect's job.

_Last reconciled: 2026-08-09._

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

## Not in the portfolio

`manager-ui` and `studio-bridge` are product repos that zesty-eng-team operates
on. They are subjects, not systems. Nothing here governs them and the
Meta-Architect does not read them.
