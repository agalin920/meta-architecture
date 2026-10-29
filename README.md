# meta-architecture

The DNA of a colony of self-evolving, agent-run systems, and the layer that
keeps it.

Each system gets four things:

- a **purpose**;
- a **shared memory**;
- an **honest way to know when it is winning**;
- **freedom to reshape itself**, including how it learns.

There are no managers, standups or retros. The right specialists and ways of
working emerge on their own. Every system's hard-won lessons are written back
into the DNA, so every new system starts smarter, but only lessons whose
real-world results held up in more than one system get in.

The full reasoning, and Andres's rulings, are in [`REDESIGN.md`](REDESIGN.md)
(2026-10-28).

## What's here

```
dna.md            what every system is built from: the kernel, lesson statuses,
                  the DNA rule, the harvest. Start here if you are building
dna/lessons/      every lesson, with status and evidence: founding, candidate,
                  proven, retired
dna/trials.md     lessons being tried in a second system
kit/              working implementations of the kernel's mechanism (locks,
                  boot and stop checks, rollback, reviewer, the loop) to copy
charter.md        this layer's purpose and hard lines. Andres's; locked
systems.md        the registry: 3 core systems, 6 dormant side projects
scoreboard/       this layer's own scoreboard. Locked
CHANGELOG.md      how this layer has changed itself, and whether it helped
HANDOFF.md        current state, including what is waiting on Andres
meta/keeper.md    the DNA-keeping procedure (weekly, and at boot)
meta/thesis.md    why this should work, and what would prove it wrong
meta/record.md    every lesson, ruling and result from before the redesign
archive/          everything that came before, verbatim; MAPPING.md says where it went
design/phase-1.md the approved design for the migration
```

## The systems

| System | Status |
|---|---|
| [zesty-eng-team](../zestyio/zesty-eng-team) | core, `active` |
| [mpulse-engage-team](../mpulsemobile/mpulse-engage-team) | core, `active` |
| [mpulse-dpi-team](../mpulsemobile/mpulse-dpi-team) | core, `active` |
| personal-university, brand-system, galind-team, the-debrief, resale-desk, zesty-webengine-team | side projects, `dormant` |
| media-log | `dataset` |

Details in [`systems.md`](systems.md). Relative links assume everything sits
under `~/dev/`.

## Using it

Open a session here and say what you want, or ask "what has changed?".
The harvest runs itself every Monday.
