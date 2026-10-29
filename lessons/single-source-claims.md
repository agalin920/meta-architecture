# Single-source claims

**Status:** `candidate`. Two systems invented it on the same day; no trial.

**Lesson.** A claim copied into N files has N places to be wrong, and every
correction fixes whichever copy it found. Delete the duplicate, or make the
copies' agreement machine-checked. An instruction to keep them in sync is not
a remedy.

**Evidence**
- zesty-eng-team: a struck claim stayed live in eight places, all four agent
  preambles among them, and displaced a one-line CI fix into a 106-line script
  the Director rejected. Remedy: grep every copy when striking:
  `zesty-eng-team: CLAUDE.md:93`.
- mpulse-engage-team: one measured fact in four files, three values, three
  days: `mpulse-engage-team: docs/team-log.md:868-869`. A deliberately
  duplicated preamble drifted; an assertion now hashes all copies:
  `mpulse-engage-team: .claude/agents/architect.md:155`.
- mpulse-dpi-team: "correcting the prose and leaving the executable
  instructions stale is a repeatable failure mode":
  `mpulse-dpi-team: docs/team-log.md:65`.

**Where it failed / limits**
- **grep finds verbatim copies, not paraphrases.**
- **The rule did not finish the job:** at the 2026-10-28 inventory the struck
  zesty-eng-team claim was still live in a handoff README.
- mpulse-dpi-team carries a known drifted preamble copy into its next retro:
  `archive/meta/architect-log.md:3475-3476`.
- The old catalog hit it while recording it: "N copies, one updated, on the
  first try": `archive/patterns/single-source-claims.md:121-127`.
- An assertion can match its own text: anchor it:
  `archive/patterns/single-source-claims.md:79-82`.

**Origin.** zesty-eng-team and mpulse-engage-team, independently, 2026-08-18.
