---
description: Optional deeper pass over how this layer (the playbook keeper) works. Nothing depends on anyone running it.
---

1. Run `python3 scoreboard/score.py` and `python3 scoreboard/verdicts.py --all`.
2. Read `log/` since the last event with ref `deep pass`, `meta/keeper.md`, and the last four weekly `review` events.
3. Propose at most three changes to how this layer works, each with its evidence and a claim on one of M1–M4. Also say what should be **cut**: "nothing, because…" is valid; silence is not.
4. Take each proposal through `kit/docs/loop.md` § A self-change, using `.claude/agents/change-reviewer.md`. This repo is public: the reviewer rejects anything employer-internal.
5. Write a `lesson` event with ref `deep pass`.
