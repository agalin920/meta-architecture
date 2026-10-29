# Reconcile current state by script

**Status:** `candidate`.

**Lesson.** Check the current-state file against the outside source of truth
with a script at boot. People outside the system (a manager merging, a ticket
moved) change state without a team event, so a hand-kept state file drifts.

**Evidence**
- mpulse-engage-team's `state_check.py` found nine PRs listed OPEN that had
  merged, and retro 003 reconciled ten drifts:
  `mpulse-engage-team: docs/team-log.md:5809-5810`, `:5841`.
- The hand-kept equivalent at zesty-eng-team: 9 of 16 PR entries wrong at
  retro 7 and 6 of 11 at retro 8:
  `zesty-eng-team: docs/decision-log.md:816`, `:888`.
- resale-desk goes further and derives state from its event log, so the
  narrative may not restate a computed number:
  `resale-desk: docs/decision-log.md:150-168`.

**Where it failed / limits**
- **It reported coverage it did not have:** one check printed nothing for 70
  days because it sat outside the one block parsed:
  `mpulse-engage-team: docs/team-log.md:5810-5811`.
- **Not run, it does nothing:** zesty-eng-team's script ran in 5 of 13+
  sessions: `zesty-eng-team: docs/decision-log.md:888`.
- **Derived state can be impossible** (`-12` from a schema gap):
  `resale-desk: tools/desk.py:282`.

**Origin.** mpulse-engage-team, 2026-08 (`tools/state_check.py`);
zesty-eng-team's Orient rule "GitHub is right".
