# Changelog

How this system has changed itself, written for Andres. Newest first.
Each self-change is one commit, `evolve(C-NNN): …`. Its claim names the one
score it should move. `scoreboard/verdicts.py` judges it once its window closes:
the later of 14 days or 5 merged PRs, capped at 30 days. A change that did not
help is reverted, and the failure is kept in `lessons.md`.

<!-- Entry format (keep it; scripts parse it):
    ## C-001 · 2026-10-29 · <what changed, in a few words>
    <!-- claim: S2 down; landed: 2026-10-29 -->
    - **Why:** <the event, correction or number that prompted it>
    - **Expect:** <what should happen, in plain words>
    - **Reviewer:** LAND — <one line>
    - **Verdict:** open
-->

## M-000 · 2026-10-28 · The colony redesign
<!-- claim: none none; landed: 2026-10-28 -->
Not a self-change. Andres's redesign (`REDESIGN.md`), carried out on branch
`colony-migration`.

- **What changed:**
  - The architecture council became the DNA keeper. `spine.md` became
    `dna.md`: the kernel, lesson statuses, DNA rule and harvest, in about
    200 lines where `spine.md` and `patterns/README.md` together were 603.
  - `patterns/` became `dna/lessons/`. Original invariants are `founding`;
    `architect-on-cadence` is retired.
  - The 3,532-line architect log is archived verbatim, and every lesson,
    ruling and result is kept in `meta/record.md`.
  - The quarterly review and dispatch procedures were replaced by
    `meta/keeper.md`, which runs weekly on its own.
  - This layer may now edit the core systems (ruling 9).
  - This layer now runs its own kernel: a locked charter and scoreboard,
    reviewer, rollback, this changelog, and a boot check.
- **Why:** review 001 found that everything waiting on Andres's attention
  stopped, and that the promotion engine could not turn.
- **Expect:** core systems improve against their baselines without needing
  Andres more. The falsifier is in `meta/thesis.md`, checked 2027-01-31.
- **Verdict:** n/a (migration)
