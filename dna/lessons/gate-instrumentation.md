# Gate instrumentation

**Status:** `candidate`, weakest of the measured ones: it produced numbers, but
over a small share of the work.

**Lesson.** Every gate writes a one-line trace when it runs (caught, pass,
skip or blocked, with severity), so the improvement pass can see the mechanism,
not only its outputs, and can find gates that never fire.

**Evidence**
- The need: engage's first retro could observe its outputs but not its
  mechanism, so the architect could only add rules:
  `mpulse-engage-team: docs/team-log.md:860-863`.
- Its first datapoint corrected its own coverage claim ("across 8 worklogs";
  all 27 lines came from one): `archive/patterns/README.md:353`.
- It supplies the escape-rate numerator: 14 caught (7 blockers) at retro 002;
  3 of 23 blockers escaped at retro 003:
  `mpulse-engage-team: docs/team-log.md:5822`. Its `--dead` mode shows 6 of 12
  declared gates recorded but never caught (`tools/gates.py`, pre-migration
  tag).

**Where it failed / limits**
- **Coverage.** Gate lines appear in 6 of 55 worklogs; escape rate was
  measurable on 6 of 80 PRs; 54% of team PRs carry no ticket key, so that work
  has no worklog and no trace: `mpulse-engage-team: docs/team-log.md:5822`,
  `:5829`.
- **The trace is written by the session**, so it fails the way reminders do;
  see [instruments-over-reminders](instruments-over-reminders.md).
- 44 gate ids in use against 12 declared: the vocabulary drifted.

**Origin.** mpulse-engage-team, 2026-08-13 (`tools/gates.py`).
