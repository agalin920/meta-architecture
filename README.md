# Meta-Architecture

The layer above four repo-based, agent-run systems. It owns the thing none of
them can see: **the space between them.**

Each system below has its own charter, its own operating loop, and its own
Architect that improves it on a cadence. That works. What none of them can do is
notice that they share one human and one week, that a pattern proven in one
never crossed to the others, or that nobody is checking the Architects.

## What's here

```
HANDOFF.md              state of play for a cold session — read first
charter.md              what this layer is for — yours alone to edit
systems.md              the registry: domain, cadence, metric, status
patterns/               the catalog — this is the deliverable
meta/
  thesis.md             why a layer above is worth anything, with kill conditions
  architect.md          the review procedure
  architect-log.md      findings, proposals, and whether they landed
```

## The systems

| System | Domain | Status | Architect |
|---|---|---|---|
| [personal-university](../personal-university) | Broad classical education | `active` | every 10 sessions |
| [zesty-eng-team](../zestyio/zesty-eng-team) | Engineering delivery — `manager-ui` | `active` | every retro |
| [mpulse-engage-team](../mpulsemobile/mpulse-engage-team) | Engineering delivery — mPulse Engage, ~30 repos | `active` | every retro |
| [mpulse-dpi-team](../mpulsemobile/mpulse-dpi-team) | Engineering delivery — DPI, 4 repos | `active` | every retro |
| [brand-system](../brand-system) | Public presence | `active` | every 4 weeks |
| [media-log](../media-log) | Media database | `dataset` | none, correctly |

Details in [`systems.md`](systems.md).

**Three of the six are the same system.** The two mPulse teams were derived from
zesty-eng-team on 2026-08-10, not arrived at independently. That is a fact about
the evidence base, not a criticism of the copies — see the note on the adoption
matrix in [`patterns/README.md`](patterns/README.md).

Relative links assume everything sits under `~/dev/`, where all seven repos are
checked out as of 2026-08-10 — the four systems above plus
[`zesty-eng-team`](../zestyio/zesty-eng-team) and the two mPulse teams under
`../mpulsemobile/`.

## The three hard rules

1. **Never edit a child repo.** Findings go to that system's Architect; the
   human carries them. Every system below depends on a single human gate for
   being reviewable and revertible, and a meta-layer that routes around it
   destroys the property it exists to protect.
2. **Quarterly, and never more often than the fastest child Architect.**
3. **Under 1% of the portfolio's time.** Every system here names the same
   failure — building the system is more fun than using it — and this repo is
   the most exposed thing in the portfolio to it.

## Kill condition

**If two consecutive reviews produce no finding a local Architect couldn't have
made, delete this repo.**

It is in [`charter.md`](charter.md) so the thing being judged cannot renegotiate
it, and the Meta-Architect checks it every review, finding by finding.

## Run a review

```bash
claude "Read meta/architect.md and run a review."
```

Quarterly, or when something feels structurally wrong across systems. It
proposes; you carry proposals to the child Architect; that system's own gate
still applies.

## Start here

Read [`patterns/README.md`](patterns/README.md). The adoption matrix is the
whole point in one table: fifteen patterns, six systems, and which of them
independently converged on what — noting that only four of the columns are
independent, and the matrix says which.

Then [`HANDOFF.md`](HANDOFF.md) for where things actually stand and what is open.
