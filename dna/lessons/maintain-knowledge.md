# Maintain knowledge, don't append it

**Status:** `candidate`. It changed a rule after a measured finding; the new
rule has not yet run a full cycle.

**Lesson.** Before writing to knowledge, search it. If the work contradicted a
recorded fact, correct it in place with a dated strike. The failure to watch is
facts going stale, not filler.

**Evidence**
- mpulse-dpi-team predicted that its every-ticket knowledge gate would breed
  filler: `mpulse-dpi-team: docs/decision-log.md:47`.
- Its first retro graded it: filler was **under 1%** (9 lines of restatement
  cut), but **8 recorded facts had gone stale** through later merges, in a
  1,550-line knowledge file: `archive/meta/architect-log.md:3399-3404`;
  `mpulse-dpi-team: docs/team-log.md:1147` (`a2956f2`, `0a7ba7b`).
- The gate changed from append to maintain:
  `mpulse-dpi-team: docs/definition-of-done.md:124` (`444b364`). The kernel's
  knowledge layer takes this wording (`REDESIGN.md:147-149`).

**Where it failed / limits**
- **Not graded yet.** No cycle has run since the rule changed.
- **Merges elsewhere falsify knowledge silently:** zesty-eng-team recorded
  three such cases (a test trigger, a CI scope, a type-check baseline).
- **Open questions sat untouched** for two months; a fact that can go stale
  needs a re-check date: `archive/meta/architect-log.md:1272-1274`.
- **Knowledge no read path reaches is an archive:** engage found five orphan
  knowledge files: `mpulse-engage-team: docs/team-log.md:5807`.

**Origin.** mpulse-dpi-team, retro 1, 2026-10-28. Replaces the retired
[knowledge-append-gate](knowledge-append-gate.md).
