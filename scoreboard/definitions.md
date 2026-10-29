# Scoreboard: meta-architecture

**Locked.** Andres owns what this measures. A new measure is added beside the
old ones with his okay, never swapped in quietly.

**Goal, in plain words:** core systems getting better without needing Andres
more, and lessons that help in one system reaching the others.

Computed by `scoreboard/score.py` from the core systems' own scoreboards, event
logs and changelogs, never by hand.

| | Measure | Direction | Source |
|---|---|---|---|
| **M1** | Per core system, per measure (S1–S4, G1): the last 30 days against that system's `baseline-2026-10-28.json`, as better / flat / worse. Summed as "measures better", "flat", "worse" | more better | each system's `scoreboard/score.py` |
| **M2** | Escalations to Andres per core system per week, last 4 weeks | down (not zero by hiding: S4 in each system counts the same events) | `escalation` events in each system's `log/` |
| **M3** | Playbook flow: lessons by status (founding, candidate, proven, retired); open trials | candidates and proven up | `lessons/`, `trials.md` |
| **M4** | Share of judged self-changes that were reverted, across core systems | a healthy band, not zero: zero means nothing was risked or nothing was judged | each system's `CHANGELOG.md` |

Units for this layer's own rollback windows are **review runs** (`review`
events in `log/`).

## Not measured

- How long Andres spends reading changelogs.
- Lessons that helped but were never written down.
- Side-project health. Side projects are dormant by decision; paused is not
  failed.
- Whether a lesson that helped at Zesty helps at mPulse *for the same reason*.
  The scoreboard sees the verdict, not the mechanism.

## Baseline

`baseline-2026-10-28.json`, written at migration.

- **M1** is "baseline" by definition on that date.
- **M2** has no pre-migration instrument; escalations were not logged as
  events.
- **M3** is the catalog as collected at migration.
- **M4** is n/a, because no self-change had been judged.
