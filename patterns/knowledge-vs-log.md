# Knowledge layer vs event log

**Status:** `provisional`
**Invented in:** zesty-eng-team
**Partial in:** personal-university (`reference/` holds external material only)
**Missing from:** brand-system

## The pattern

Two distinct memory stores, with different write rules:

- **The log** — append-only history. *What happened, when.*
- **Knowledge** — rewritten in place. *What is true about operating in this
  domain.* Environment facts, traps, how to drive the product, which tests are
  flaky.

A hard-won operational fact buried in a dated log entry is functionally lost.
Nobody re-reads session 12 to find out that bare `npm` is a broken nvm shim.

## Why it works

The two have opposite lifecycles. History must never change; operational truth
must always be current. Forcing both into one file means either the history gets
edited or the truth goes stale, and both are silent failures.

It also shortens the boot ritual. A new session reads *current knowledge* plus
*current state*, not the whole history.

## Evidence

- `zesty-eng-team/knowledge/` — three files with clear separation of concerns:
  `manager-ui.md` (environment, verification facts, flaky specs), `product.md`
  (how to *drive* the product as a user), `studio.md` (deploy mechanics and
  operational traps). `CLAUDE.md` routes writes deliberately: *"Surprises about
  the codebase go to `knowledge/manager-ui.md`; decisions with rationale go to
  `docs/decision-log.md`."*
- **It has already paid.** `product.md` exists because not knowing how to drive
  the product cost an hour on ticket #4255, and the boot ritual now names that
  incident when telling you to read it.
- **The pointer discipline.** *"`../manager-ui/CLAUDE.md` is the authoritative
  reference. Do not duplicate its contents into this repo — link to it."* Two
  copies of a fact is one stale fact waiting.
- `personal-university/reference/` — external material (Atlas, Library, prior
  logs), not learned operating knowledge. There is no file for *things we found
  out the hard way about running this school.* The precedence rules at the foot
  of its README are exactly that kind of knowledge, and they live in a README.

## Adoption notes

Cheap to start: one file, written to whenever something surprising is learned,
rewritten rather than appended. The routing rule matters more than the structure
— **surprises to knowledge, decisions to the log** — because without it
everything lands in the log by default.

## How it fails

- **Duplicating an authoritative source.** Link, don't copy.
- **Becoming a second log.** If entries are dated and never revised, it is a log
  with a different name.
- **Nobody trimming it.** Subject to the same [overhead
  ceiling](overhead-ceiling.md): knowledge that is no longer true is worse than
  absent, because it is trusted.
