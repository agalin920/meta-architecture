# Append-only log + rewritten current state

**Status:** `proven`
**Invented in:** convergent.

## The pattern

Two memory shapes, kept strictly separate:

- **The event log** — append-only, never edited. What happened, dated, in
  sequence. `session-log.md`, dated entries in `team-log.md`, `pipeline.md`.
- **Current state** — rewritten in place, always short. What is true *now*.

Confusing them is the failure. An edited history cannot be audited; a
current-state section that grew by appending is a log nobody can act on.

## Why it works

The Architect needs history it can trust was not tidied. The operator needs a
paragraph that describes the world as it is. These are different jobs and the
same file cannot do both.

Append-only is also what makes supersession honest: every Architect in this
portfolio is instructed that findings are withdrawn **in writing**, never
quietly edited.

## Evidence

- `zesty-eng-team/docs/team-log.md` — the cleanest split. *"The 'Current state'
  header is rewritten in place and stays short. Session entries are append-only
  and never edited."*
- `personal-university/progress/session-log.md` — append-only, newest at the
  bottom, per-domain `progress/<domain>.md` files as the rewritten rollups.
- `brand-system/pipeline.md` — item states are rewritten as items move, killed
  items are never deleted. **Partial:** no current-state header anywhere; see
  [handoff record](handoff-record.md).

## How it fails

- **Unbounded growth.** personal-university is at 234 log lines after 5
  sessions. zesty-eng-team names the fix: the Architect condenses older entries
  at a retro, *"never silently, and never by deleting anything that explains a
  decision."*
- **The current-state section quietly becoming a log.** If it has dates in it,
  it has stopped being current state.
