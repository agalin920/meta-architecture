# Changelog

How this system has changed itself, written for Andres. Newest first.
Each self-change is one commit, `evolve(C-NNN): …`. Its claim names the one
score it should move. `scoreboard/verdicts.py` judges it once its window closes:
the later of 14 days or 5 merged PRs, capped at 30 days. A change that did not
help is reverted, and the failure is kept in `lessons.md`.

Entry format (keep it; the scripts parse it). Examples sit indented in a code
block so the scripts skip them:

```
    ## C-001 · 2026-10-29 · <what changed, in a few words>
    <!-- claim: S2 down; landed: 2026-10-29 -->
    - **Why:** <the event, correction or number that prompted it>
    - **Expect:** <what should happen, in plain words>
    - **Reviewer:** LAND — <one line>
    - **Verdict:** open
```

Maintenance changes claim `<!-- claim: maintenance none; landed: …; files: a,b -->`,
listing every file they touch. S1 cannot be claimed (see `docs/loop.md`). The
landing commit's sha goes in as `; commit: <sha>` after `landed:`.
