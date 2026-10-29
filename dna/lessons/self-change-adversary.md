# An adversary on the improvement loop

**Status:** `candidate`. Now kernel 5, the self-change reviewer.

**Lesson.** Changes a system proposes to itself are its highest-blast-radius
output, and the pass that proposes them cannot audit its own evidence. A second
reviewer that did not write the proposal checks it, and runs commands the first
pass was never told to run.

**Evidence**
- zesty-eng-team retro 3, first run: pass 2 corrected the headline metric from
  0.00 to 0.83 (n=6). Of 13 applied changes, six came from pass 2; pass 1 alone
  would have shipped a false metric and two false statements:
  `zesty-eng-team: docs/decision-log.md:484`, `:501`.
- Retro 5: pass 2 corrected 1.50 → 2.00, **caught pass 1 proposing to delete a
  blocker that was still true**, and caught a proposal to add a rule the team
  had already written and ignored: `zesty-eng-team: docs/decision-log.md:602`.
- Retro 6: pass 2 showed two rules graded "failed" had fired and had their
  output deleted downstream: `zesty-eng-team: docs/decision-log.md:738`.
- galind-team: an adversary on a strategy proposal; the recommendation was
  withdrawn after each of passes 2-4: `galind-team: docs/decision-log.md:96-112`.

**Where it failed / limits**
- **mpulse-engage-team declined it twice** on its own evidence: it had no
  counting defect (27 findings reported, 27 returned):
  `archive/patterns/README.md:388-402`.
- **A cold judge is not the same thing:** a fresh-session judge (AR-1) was
  rejected at both teams; it cannot see findings given in chat:
  `archive/meta/architect-log.md:1950-1965`.
- **Cost:** about 80 minutes per retro at zesty-eng-team's scale:
  `zesty-eng-team: docs/decision-log.md:469`; galind-team stopped after four.
- An audit agent that has found nothing is under pressure to invent something:
  `zesty-eng-team: .claude/commands/retro.md:37`.

**Origin.** zesty-eng-team, retro 3, 2026-08-13 (`ac65e24`).
