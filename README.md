# Meta-Architecture

The layer that agent-run systems are **grown from**, and that **learns back**
from what they become.

Every system in this portfolio was seeded from a shared spine. Each then runs
its own loop, adapts to its own domain, and improves itself on its own cadence.
They diverge. Most of that divergence is local and correct. Some of it belongs
back in the spine, where every system built afterwards inherits it — and this
repo is the only thing positioned to notice, judge, and carry it.

**Two jobs, two clocks.**

| | Generative | Evolutionary |
|---|---|---|
| **What** | New systems are grown from the spine | Proven divergence is carried back into the spine |
| **Clock** | On demand. No cadence | Quarterly, never faster than the fastest child Architect |
| **Why that speed** | Pulling costs nothing and should block nothing | A spine change reaches every future system; it needs evidence, and evidence accumulates slowly |
| **Read** | [`spine.md`](spine.md) | [`meta/architect.md`](meta/architect.md) |

**Divergence is cheap and local; convergence is expensive and deliberate.** Fast
outward, slow and selective on the way back in. That asymmetry is the design.

## What's here

```
spine.md                what a new system inherits — start here if you're building
patterns/               the catalog: evidence, origin, adoption, failure modes
charter.md              what this layer is for — the human's alone to edit
systems.md              the registry: domain, cadence, metric, status
HANDOFF.md              state of play for a cold session
meta/
  thesis.md             why a layer above is worth anything, with falsifiers
  architect.md          the review procedure — the evolutionary clock
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

**Three of the six are the same system.** The two mPulse teams were copied from
zesty-eng-team on 2026-08-10, not grown independently from the spine. That is a
fact about the evidence base, not a criticism of the copies — see the note on
the adoption matrix in [`patterns/README.md`](patterns/README.md). Copies never
count toward promotion.

Relative links assume everything sits under `~/dev/`, where all seven repos are
checked out as of 2026-08-10.

## The rules

1. **Never edit a child repo.** Findings go to that system's Architect; the
   human carries them. This holds for spine changes too — a new spine version
   does not retrofit itself into existing children. Every system below depends
   on a single human gate for being reviewable and revertible, and a meta-layer
   that routes around it destroys the property it exists to protect.
2. **The spine changes on evidence, not on interest.** Only `proven` patterns
   are default inheritance, and derived copies never count toward promotion.
   Premature evolution is the failure mode this design invites.
3. **The evolutionary clock stays under 1% of the portfolio's time.** Pulling
   from the spine doesn't count — that isn't overhead, it's the point.

## Building something new

Read [`spine.md`](spine.md). It states what every system inherits, where systems
are expected to differ, and the three tests before adopting any pattern.

It is a resource, not a procedure — deliberately. There is no scaffold command
and no checklist, because a procedure would pin the portfolio to the
capabilities of whatever wrote it. Take the reasoning and build what your domain
actually needs.

## Running a review

```bash
claude "Read meta/architect.md and run a review."
```

Quarterly, or when something feels structurally wrong across systems. It
proposes; you carry proposals to the child Architect; that system's own gate
still applies.

Then [`HANDOFF.md`](HANDOFF.md) for where things actually stand and what is
open.
