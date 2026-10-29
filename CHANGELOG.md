# Changelog

How this system has changed itself, written for Andres. Newest first.
Each self-change is one commit, `evolve(C-NNN): …`. Its claim names the one
measure (M1–M4) it should move. `scoreboard/verdicts.py` judges it once its
window closes: the later of 14 days or 5 review runs, capped at 30 days. A
change that did not help is reverted, and the failure is kept in `lessons/`.
M-entries record Andres's decisions; they are not self-changes.

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

Maintenance changes claim `<!-- claim: maintenance none; landed: … -->`. S1
cannot be claimed (see `docs/loop.md`).

## M-002 · 2026-10-29 · Audits, kit v2: every evolvable part has evidence, a trigger and a verdict
<!-- claim: maintenance none; landed: 2026-10-29 -->
Not a self-change: Andres asked for no holistic misses. Independent audits of
all four repos and a design-level review found that several parts of each
system could not evolve on evidence.

- **What changed:**
  - **The crew is visible.** Every subagent spawn is logged by a hook. Units record each one's effect, `tools/crew_report.py` shows each agent's record, and the change-reviewer is scored too.
  - **Triggers no longer wait on memory.** The boot check computes when a deeper pass is due, overdue verdicts, stale or broken score snapshots, unlogged units, changes to instruction channels, and queue age.
  - **Verdicts have statistics:** a minimum sample, a 10% effect, shared credit, and "insufficient data" never read as failure.
  - **Safety model.** Locks stay flatly refused. Outside-world actions ask Andres in the moment instead of being refused (his ruling). Guard loopholes are closed: pushes and apply by any spelling, `gh api` writes, marker bypasses, case-variant paths.
  - **This layer:** its scoreboard was blind (wrong key) and now isn't. Its public settings no longer name product repos. Kit drift and side-project revivals are checked weekly. The falsifier runs on 2027-01-31 and 2027-03-31.
  - **The three systems:** kit v2, audit fixes and simplification. Their locked-file changes wait for Andres to apply them in his own terminal, because the agents were refused, correctly.
- **Why:** "if we don't have insight into the crew, how can it evolve."
- **Verdict:** n/a (decisions)

## M-001 · 2026-10-29 · First day: names, proposals, two lists, clean slate
<!-- claim: maintenance none; landed: 2026-10-29 -->
Not a self-change: Andres's decisions on the first day after the migration, applied across this layer and the three core systems.

- **What changed:**
  - **Neutral names.** `dna.md` became `playbook.md`; "colony", "DNA" and "harvest" are gone from live files. The playbook now says to fan out agents freely; "default no" covers only permanent rules, files and steps.
  - **Proposals.** Systems may propose charter or scoreboard changes (`log/pending/S-NNN`, one open per kind). Andres approves with `scoreboard/apply` in his own terminal; sessions are refused.
  - **Two waiting lists.** *System* (proposals, escalated changes, locks) and *work* (merges, approvals, product or security calls). The weekly review rolls up and pushes system items only. Work items over 14 days are re-checked.
  - **Clean slate.** The three systems' instructions now state today's rules without history, with originals archived. Old queues were parked and work lists re-checked and dated. Boot reads are now 564, 695 and 627 lines.
  - **Charters.** The comment-marker rule moved out of the charters into scoreboard mechanism.
  - **Kit fixes** found by the first live tests: the changelog parser, unjudgeable S1 claims, the instrument switch, uncommitted locked edits, inert deny rules, a lock test that passed without running. All are recorded in `lessons/observations.md`.
  - **Two mPulse systems stay separate** (Andres's ruling), revisited at the 2027-01-31 check.
  - **The live lock test passed** in all four repos: 8 of 8 attempts refused.
- **Why:** keep Andres out of the middle and keep the loop free of old baggage.
- **Verdict:** n/a (decisions)

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
