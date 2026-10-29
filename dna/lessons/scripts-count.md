# Scripts count, prose does not

**Status:** `candidate`.

**Lesson.** Anything counted (metrics, findings, line totals) is counted by a
script from the source, not by an agent following careful prose. A prompt
cannot fix "run the right query and count the results".

**Evidence**
- zesty-eng-team: **three retros, three wrong metric figures, three causes**.
  Retro 3 reported 0.00 against a true 0.83 (n=6): the command used cannot
  return inline review comments. "None of those is a reasoning failure":
  `zesty-eng-team: docs/decision-log.md:507-509`.
- The script reproduced the independent hand derivation exactly (0.83 per PR,
  2.00 Director findings per ticket): `zesty-eng-team: docs/decision-log.md:515`.
- mpulse-dpi-team's hand count was uncountable (the marker was on 26% of team
  comments), and its raw crawl was not kept:
  `mpulse-dpi-team: docs/team-log.md:1143`.
- This layer could not reproduce three of its own line counts:
  `archive/meta/architect-log.md:856-861`.

**Where it failed / limits**
- **The script is wrong too, differently each cycle.** Retro 5: a silent 0.00
  from a body-marker filter (`zesty-eng-team: docs/decision-log.md:596`). Retro
  7: a heading rename made 11 of 15 verdicts unreadable, and edited comments
  were counted twice (`:800`). Retro 8: it printed a figure that needed a fix.
- So a script needs the adversary and honest-metric's floors; it is not
  trusted for being a script. See [honest-metric](honest-metric.md).
- Hand adjustments (dedup, exclusions) are still applied at every retro.

**Origin.** zesty-eng-team, 2026-08-13 (`tools/retro-metric.py`). Kernel 4:
measures computed by scripts from outside data.
