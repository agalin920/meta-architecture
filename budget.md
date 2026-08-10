# Budget

The one resource every system in this portfolio shares and none of them can see.

> **STATUS: NOT YET FILLED.** The allocation below is a template. Nothing here
> is inferred from behaviour — a budget the human did not state is a guess with
> a table around it, and the Meta-Architect would then audit the portfolio
> against numbers it made up.
>
> **Fill this before the first review.** Ten minutes, once.

## Why this file exists

Four systems, one human, one week.

Each system defends its own cadence, correctly and by design:

- brand-system's Orchestrator opens **every cycle** with a cadence statement,
  and is told that defending the schedule is its primary job — above taste,
  above strategy.
- personal-university's Architect is told that two consecutive misses means
  propose a slower cadence, not try harder.
- zesty-eng-team runs to whatever the Director hands it.

All of that is right, and all of it is local. **The predictable failure is that
four individually reasonable cadences are jointly impossible.** The human
silently drops whichever system has the weakest tripwire, each Architect reads
its own miss as a local cadence problem, and every system slows down while the
actual constraint — the week — is never named.

No local Architect can see this. It is the main reason this repo exists
(`meta/thesis.md` §II).

## Capacity

```
Hours available per week for the portfolio, total:      <fill>
  Of which reliably available (a bad week):             <fill>
```

The second number is the one that matters. A budget built on good weeks is a
budget that fails in week 7 — which is when brand-system's charter says cadence
collapse actually happens, not week 3.

## Allocation

| System | Cadence | Est. hours/wk | Actual (last window) | Met? |
|---|---|---|---|---|
| personal-university | per session | `<fill>` | — | — |
| zesty-eng-team | per ticket | `<fill>` | — | — |
| brand-system | weekly cycle | `<fill>` | — | — |
| media-log | ad hoc | ~0 | — | — |
| **meta-architecture** | quarterly | **<1% of the above** | — | — |
| **Total committed** | | `<fill>` | | |

**If total committed exceeds reliable capacity, that is the finding**, and it
outranks everything else in the review. The correct response is to cut or park a
system — not to ask four Architects to each try a little harder.

## Rules

- **Actuals come from `git log`, not from memory.** Commits, sessions, cycles,
  tickets over the window. Reconstructed effort is flattering.
- **Under-committing is the correct correction.** Copied from brand-system's
  Architect: a schedule the operator reliably fails against corrodes the system
  faster than a slower one they meet.
- **A dropped system is a decision or it is rot.** If something got no time this
  window, the Meta-Architect proposes `dormant` with a revisit date, or `dead`.
  Leaving it `active` and unworked is how a portfolio becomes a guilt pile.
- **This repo is inside the budget, not above it.** Under 1% of the total. If a
  review costs more than the shortest child review, it was too long.

## Revisit

Whenever the human's real week changes — job, project, life. A budget that
outlives its assumptions is worse than none, because the Meta-Architect will
audit against it with a straight face.
