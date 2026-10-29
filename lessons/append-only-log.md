# Memory in three layers: log, current state, knowledge

**Status:** `founding` (ruling 1). Absorbs the old `knowledge-vs-log`.

**Lesson.** Keep three stores with opposite write rules: an **event log**,
append-only and committed; a short **current state**, rewritten in place; and
**knowledge**, what is true and not otherwise recoverable, maintained in place.
Mixing them is the failure: an edited history cannot be audited, and a state
section that grows by appending is a log nobody can act on.

**Evidence**
- zesty-eng-team's knowledge layer paid on first use: a knowledge file exists
  because not knowing how to drive the product cost an hour, and the boot
  names that incident: `archive/patterns/knowledge-vs-log.md:37-39`.
- **Six of ten systems** had operating-log state uncommitted at some point in
  the review 001 window; `git log` alone misread four of them (the-debrief: 4
  commits, 65 entries): `archive/meta/architect-log.md:3318-3323`.
- mpulse-dpi-team found three weeks of memory uncommitted at its first retro
  and added a commit-at-close step: `mpulse-dpi-team: CLAUDE.md:111`
  (`d391cbd`); its 08-31 → 10-27 backlog was committed only at that retro
  (`edfbb2f`).

**Where it failed / limits**
- **An uncommitted log is neither append-only nor a log** (review 001, M-5):
  a ledger counting commits reads "clear" over an empty, uncommitted interval:
  `the-debrief: docs/retro-input-001.md:150-168`.
- **Current state becomes a log.** engage's grew to 2,129 lines and was cut to
  about 490: `mpulse-engage-team: docs/team-log.md:5841`.
- **Rewritten state drifts** when people outside change things: see
  [reconcile-state-by-script](reconcile-state-by-script.md).
- **Knowledge goes stale rather than filling with junk:** see
  [maintain-knowledge](maintain-knowledge.md).
- **Derived state can be impossible:** resale-desk computes state from its
  event log and printed `held, not listed = -12` from a schema gap its 19/19
  selftest missed: `resale-desk: tools/desk.py:282`.

**Origin.** Log and state: convergent founding (zesty-eng-team,
personal-university, brand-system). Knowledge layer: zesty-eng-team. Kernel 2.
