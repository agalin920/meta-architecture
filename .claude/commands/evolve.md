---
description: Optional deep pass over how the system is doing. Nothing depends on anyone running it; the loop triggers it when the evidence says so.
---

Run the deeper pass described in `docs/loop.md` § Deeper pass.

1. Run `python3 scoreboard/score.py --summary` and `python3 scoreboard/verdicts.py --all`.
2. Read `log/` events since the last deeper pass (the last `lesson` or `change` event marked `deep pass`), the worklogs of the units in that window, and `lessons.md`.
3. Hand that brief to the `evolver` agent. It returns at most three proposed self-changes, each with its evidence and a claim, plus its **Cuts**: what should be removed, or "nothing, because …".
4. Take each proposal through `docs/loop.md` § A self-change. The change-reviewer decides. Nothing here needs Andres unless the reviewer escalates.
5. Write a `lesson` event with ref `deep pass`, summarising what was found and what landed.
