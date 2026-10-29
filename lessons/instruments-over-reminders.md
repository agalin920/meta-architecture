# Instruments over reminders

**Status:** `candidate`.

**Lesson.** Changes that measure a number or force a trade produce data;
changes that ask a session to remember something go inert. Put a rule where a
script or the harness fires it, at the moment it applies.

**Evidence**
- This layer's transfers: 4 of 7 produced a datapoint. The ones that
  instrumented a number or forced a trade did; the one that asked a session to
  remember was inert: `archive/meta/architect-log.md:2229-2235`.
- zesty-eng-team: a Stop hook fired in 8 sessions and all 8 pushed, against 0
  of 3 for the prose rule it replaced:
  `zesty-eng-team: docs/decision-log.md:824`.
- personal-university: a self-executing clause ("a third skip deletes it")
  fired and nobody acted on it:
  `personal-university: meta/architect-log.md:1185-1188`.
- Review 001's summary of what survived: changes that measure a number or
  force a trade (`REDESIGN.md:57-61`).

**Where it failed / limits**
- **A script someone must remember to run is still a reminder.**
  zesty-eng-team's Orient script ran in 5 of 13+ sessions:
  `zesty-eng-team: docs/decision-log.md:888`.
- **An instrument with nobody to act on it** is inert the other way: engage's
  preflight reported the same failures for 69 days:
  `mpulse-engage-team: docs/team-log.md:5808`.
- A rule attached to a command instead of the moment of use never fires
  (mis-sited, not inert): `zesty-eng-team: docs/decision-log.md`, retro 6
  and 7 grades (`bde6349`, `beb4509`).
- Hooks are standing configuration: zesty-eng-team held them for the human
  (`docs/decision-log.md:824`); under the new kernel they still need review.

**Origin.** This layer, 2026-08-18 and review 001; zesty-eng-team's hooks.
