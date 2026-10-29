# Executable claims

**Status:** `candidate` (at mpulse-engage-team). The carried copy at
zesty-eng-team stayed inert.

**Lesson.** A fact a doc asserts carries the command that checks it, and a
script runs every such check on routine runs. A failing check means the doc
drifted; never edit the assertion to match the doc.

**Evidence**
- engage's `verify_docs.py` passed 9/9 by 2026-08-18, and its preamble-copy
  check caught drift no retro had noticed:
  `archive/patterns/single-source-claims.md:65-86`.
- Retro 003 went from 6/9 to 17/17 passing:
  `mpulse-engage-team: docs/team-log.md:5805`, `:5846`.
- The rule against editing the assertion:
  `mpulse-engage-team: .claude/agents/architect.md:54`.
- the-debrief's form: every number in a boot file carries the command that
  produced it: `the-debrief: CLAUDE.md:25-27` *(uncommitted)*.

**Where it failed / limits**
- **Aimed wrong, it is inert.** zesty-eng-team's carried blocks ran and
  passed, and the claims that died in the window carried no block:
  `archive/meta/architect-log.md:2222-2227`, `:3462-3466`.
- **Pinned on facts others change, it raises false alarms.** A count pin failed
  11 ≠ 10 when a human engineer added a new type, a false alarm, and the pin
  was retired: `mpulse-engage-team: docs/team-log.md:5807`, `:5834`. (This
  layer had counted the same firing as a catch:
  `archive/meta/architect-log.md:3473`.)
- **Its first run tends to correct its author:** a check matched its own text:
  `archive/meta/architect-log.md:1636-1642`.
- **A failing check nobody acts on:** three failures sat 69 days, deferred
  "for the retro": `mpulse-engage-team: docs/team-log.md:5808`.
- A reachability check proves a filename appears, not that anything routes a
  session to it.

**Origin.** mpulse-engage-team, 2026-08-13; carried to zesty-eng-team (MF-4).
