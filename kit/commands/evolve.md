---
description: Optional deep pass over how the system is doing. Nothing depends on anyone running it; the boot check says when it is due.
---

Run the deeper pass described in `docs/loop.md` § Deeper pass.

1. Save a score snapshot, `python3 scoreboard/score.py --summary > log/scores/YYYY-MM-DD.txt` (today's date; the boot check reads it as seen by this pass), then run `python3 scoreboard/verdicts.py --all`, `python3 tools/crew_report.py` and `python3 tools/crew_report.py --corrections`.
2. Read `log/` events since the last `deep pass` event, the worklogs of the units in that window, and `lessons.md`.
3. Hand that brief, with the crew report, to the `evolver` agent. Ask it the standing question: for each subagent and the change-reviewer, would we define this one today, given its record? It returns at most three proposed self-changes, each with its evidence and a claim, plus its **Cuts**: what should be removed, or "nothing, because …".
4. Take each proposal through `docs/loop.md` § A self-change. The change-reviewer decides; write a `reviewed` event for each decision. Nothing here needs Andres unless the reviewer escalates.
5. Write a `deep pass` event (ref `deep pass`) summarising what was found and what landed.
