# Systems

The registry of systems. Rewritten 2026-10-28 for the redesign. The previous
registry (771 lines, every system's history through review 001) is kept
verbatim at [`archive/systems.md`](archive/systems.md).

**Status is a decision, not an observation.** These are the states:

| Status | Means |
|---|---|
| `active` | Running the full kernel |
| `dormant` | Paused by decision. Not a failure, and nothing is expected of it |
| `dead` | Retired. Kept for its history |
| `dataset` | Not an agentic system |

**Read `git status` as well as `git log`.** Four systems looked idle in
`git log` and held uncommitted work (review 001, M-3).

## Core systems

These always matter and run the full kernel. Zesty and mPulse systems never
exchange domain content.

| System | Path | Purpose | Scoreboard | Migrated |
|---|---|---|---|---|
| **zesty-eng-team** | `../zestyio/zesty-eng-team` | Ticket in, reviewable PR out, on a Zesty product repo | S1–S4 + G1, GitHub | 2026-10-28; merged to `main` 2026-10-29 |
| **mpulse-engage-team** | `../mpulsemobile/mpulse-engage-team` | Ticket in, reviewable PR out, across the mPulse Engage services | S1–S4 + G1, GitHub + tracker (structure-only reads) | 2026-10-28; merged to `main` 2026-10-29 (branch began from `program-build-skill`) |
| **mpulse-dpi-team** | `../mpulsemobile/mpulse-dpi-team` | Ticket in, reviewable PR out, on the DPI product | S1–S4 + G1, GitHub + tracker (structure-only reads) | 2026-10-28; merged to `main` 2026-10-29 |
| **vinted-shopper** | `../vinted-shopper` | Find second-hand things Andres wants on Vinted, at a good price; he buys, it never does | G1 hit rate, S2 price against asking, S3 follow-ups; S1 returns and S4 escalations as guardrails. From its own shortlist log and his `data/orders.csv` | Installed 2026-10-29 by Andres (`f5208d4`) on kit 2.1; core by his ruling 2026-10-30, kit 2.3 the same day. Baseline 2026-10-29, empty at founding; no remote |

The two mPulse teams were copied from zesty-eng-team on 2026-08-10, not grown
independently. vinted-shopper is personal, not an employer system: only mechanism
crosses between it and the others, as between Zesty and mPulse.

**Baselines**, window 2026-08-29 → 10-28. Each is computed by its own repo's
`scoreboard/score.py` and locked at `scoreboard/baseline-2026-10-28.json`.

| | S1 escapes/PR | S2 outside findings/PR | S3 Andres follow-ups/PR | S4 escalations/unit | G1 merged PRs/week | Boot lines |
|---|---|---|---|---|---|---|
| zesty-eng-team | 0.00 (n=7) | 2.82 | 1.65 | n/a | 1.98 | 2,120 → 564 |
| mpulse-engage-team | 0.23 (n=22) | 2.12 | 0.79 | n/a | 6.65 | ~6,600 → 695 |
| mpulse-dpi-team | 0.17 (n=6) | 2.73 | 0.55 | n/a | 6.4 | 3,127 → 627 |

**Read the systems against their own baselines, not against each other.**
- Definitions differ per system: each system's `scoreboard/definitions.md`
  names its sources and its definition breaks.
- S1 counts only PRs merged by 09-28.
- S4 had no instrument before the migration.


## Side projects (dormant, not modified)

Each was read on 2026-10-28 and its mechanism lessons collected into
[`lessons/`](lessons/README.md). **None was touched.** Uncommitted work
is listed so nobody mistakes it for idleness. It stays exactly as it is until
Andres revives the system, and a revival is when a side project gets migrated.

| System | Path | Purpose | Last activity | Uncommitted / unpushed at review |
|---|---|---|---|---|
| personal-university | `../personal-university` | A classical education for one student | 2026-08-23 | none |
| brand-system | `../brand-system` | Public presence for galind.io | 2026-08-16 | 8 modified files; 3 commits never pushed |
| galind-team | `../galind/galind-team` | Building an agent-native backend suite | 2026-08-23 | 2 modified, 2 untracked (proposal, ticket 001); `../galind/galind-email` has 15 files staged, never committed |
| the-debrief | `../the-debrief` | An interactive corpus of the discoveries and works that changed what humanity knew | 2026-10-06 | 46 modified, 1 untracked adversary report |
| resale-desk | `../resale-desk` | Appraising and listing second-hand goods | 2026-08-31 | events, the applied charter amendment, D-019; `drafts/` untracked |
| zesty-webengine-team | `../zestyio/zesty-webengine-team` | Engineering delivery on a Zesty product repo | 2026-08-19 (founding only, 0 tickets) | none. Andres confirmed 2026-10-28 that it is not running anywhere |

**Much of their measured evidence lives only in those uncommitted files.** The
review quotes it, but the originals would be lost if those working trees were
discarded. Whether to commit them is Andres's call.

## Not systems

- **media-log** (`../media-log`): a dataset. It has a spec and a human gate,
  nothing more.
- **Product and subject repos.** The Zesty product repos, the mPulse service
  repos, the DPI repos under `dpi/`, and the `galind-*` product repos. Systems
  work *on* them; nothing here governs them.
- **agentic-development-tools.** Owned by mPulse, and other engineers depend
  on it. Nothing in this layer applies to it.
- **living-universe.** A human project, correctly unregistered.
