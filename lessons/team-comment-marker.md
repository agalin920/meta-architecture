# A marker on the team's own comments

**Status:** `retired` **as a prose rule** (it decayed wherever it depended on
memory). Since 2026-10-29 the marker is enforced by the kernel guard in all three
core systems instead: a post without it is refused, so it no longer depends on a
session remembering. The lesson below is why it moved from prose to the harness.

**Lesson.** Tagging every team comment with an HTML marker, so metrics can
tell the team from outside reviewers, decays: it depends on every session
remembering to write it. Selecting by author (structure) works where the
author identity is available.

**Evidence**
- mpulse-dpi-team: the marker was on 26% of team comments and on none after
  2026-10-01; the rule was retired and counting moved to author:
  `mpulse-dpi-team: docs/team-log.md:1143`, `:1161`.
- mpulse-engage-team: the marker stopped after 2026-10-07; the cut was held:
  `mpulse-engage-team: docs/team-log.md:5813`.
- zesty-eng-team: the marker was never written on 6 of 17 PRs; selection moved
  to author: `zesty-eng-team: docs/decision-log.md:800`.

**Where it failed / limits**
- zesty-eng-team keeps it: sessions with no transcript have no other way to
  attribute a comment: `archive/meta/architect-log.md:3392-3395`.
- Residual cost at mpulse-dpi-team: the owner's own unmarked comments can be
  mistaken for team feedback: `mpulse-dpi-team: docs/team-log.md:1147`.
- Key on structure, not identity (an outside reviewer is "not the author and
  no team marker"): `archive/meta/architect-log.md:2372-2377`.

**Origin.** zesty-eng-team, 2026-08; copied to both mPulse teams.
