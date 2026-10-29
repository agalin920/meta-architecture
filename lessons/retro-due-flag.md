# Defining and surfacing "retro due"

**Status:** `retired` (review 001; ruling 4).

**Lesson.** Writing down when a retro is due, and even printing "overdue" where
the session reads it at boot, did not make one run. The trigger was still a
human typing a command.

**Evidence**
- Every system that defined "due" missed it as badly as the one that did not,
  or worse: `archive/meta/architect-log.md:3347-3351`.
- **the-debrief** wrote "eleven slices overdue" in its own boot-read state
  header from at least 09-24; its retro input was compiled; no retro ran:
  `archive/meta/architect-log.md:3342`; `the-debrief: docs/retro-input-001.md:1-10`.
- **resale-desk** triggered on resolved units; with 0 resolved it never
  fired: `resale-desk: docs/decision-log.md:230-243`.
- galind-team's F1 printed "A retro must open with this"; none opened:
  `archive/meta/architect-log.md:3341`.

**Why retired**
- "Defining due is not the fix and neither is surfacing it":
  `archive/meta/architect-log.md:3351-3352`. The kernel's loop runs after every
  unit with no human trigger.

**Where it failed / limits**
- engage added the same kind of line on 2026-10-28
  (`mpulse-engage-team: tools/state_check.py:361-379`); review 001 predicted
  it would print and not fire. That one has not been observed failing; it is
  retired on the others' evidence.
- mpulse-dpi-team rejected a fixed cadence and was hurt by uncommitted memory,
  not by timing: `archive/meta/architect-log.md:3358-3361`.

**Origin.** the-debrief, resale-desk, galind-team, personal-university,
brand-system; carried to mpulse-engage-team.
