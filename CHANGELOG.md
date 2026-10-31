# Changelog

How this system has changed itself, written for Andres. Newest first.
Each self-change is one commit, `evolve(C-NNN): …`. Its claim names the one
measure (M1–M4) it should move. `scoreboard/verdicts.py` judges it once its
window closes: the later of 14 days or 5 review runs, capped at 30 days.
Changes are kept by default: the verdict is evidence, and a change is reverted
only for clear harm (Andres, 2026-10-29), with the failure kept in `lessons/`.
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
and S4 cannot be claimed in a core system (see `kit/docs/loop.md`).

## M-007 · 2026-10-30 · vinted-shopper is a core system
<!-- claim: maintenance none; landed: 2026-10-30; files: systems.md,README.md,meta/record.md,meta/keeper.md,meta/thesis.md,.claude/commands/what-changed.md,.claude/kit-deviations.md,kit/tools/lock_test.sh,HANDOFF.md -->
Not a self-change: Andres's ruling ("Core"). It runs the full kernel and is in active use; it is personal, not an employer system.

- **What changed:**
  - **Registry.** `systems.md` moves it from New systems to Core systems; `README.md`, `meta/record.md`, `meta/keeper.md` § 1, `/what-changed`, `kit/tools/lock_test.sh` and the weekly review's prompt now list it. Keeper's mechanism-only rule now also strips anything personal from it (items, sizes, prices, sellers).
  - **Kit 2.3 in vinted-shopper** (its C-002): skills and commands in the loop, kinds of work, the crew report.
  - **Locked half, waiting on Andres:** the charter row, the guard's `EDIT_ROOTS`, `scoreboard/score.py` (adds it to CORE; M1 reads each system's first baseline instead of 2026-10-28, since vinted-shopper's is 2026-10-29), and vinted-shopper's kit 2.3 hooks.
  - **Not changed: the thesis.** `tools/thesis_check.py` and its pre-registered falsifier stay on the three migrated systems; adding a system after registration would move the goalposts.
- **Why:** the charter table, the weekly review and this layer's edit rights listed three core systems; a fourth was running outside all of them.
- **Verdict:** n/a (decisions)

## M-006 · 2026-10-30 · Kit 2.3: commands are judged too; recurring work gets a skill
<!-- claim: maintenance none; landed: 2026-10-30 -->
Not a self-change: Andres's ruling that the loop judges commands as it judges
agents and skills, and that work which keeps recurring with nothing behind it
gets a command or skill, so each system grows what its own work calls for
rather than the ticket pipeline it was copied with.

- **What changed:**
  - **Kit 2.3.** `kit/docs/loop.md` § Agents, skills and commands; `unit` events start with a kind (a command's name or a generic slug, never a name or ticket text); the deeper pass and `kit/commands/evolve.md` ask of each command too, and which kinds of work recur with no command or skill. `kit/tools/crew_report.py` lists typed commands and kinds of work, flagging a kind seen on 3 distinct refs within 30 days with nothing behind it.
  - **Commands stay where they are.** `.claude/commands/x.md` and `.claude/skills/x/SKILL.md` both give `/x`; moving them would churn locked paths and open verdict windows for nothing.
  - **Systems.** zesty C-006, engage C-007 and dpi C-005 landed the same. All four change-reviewers escalated the `unit` kind prefix (it changes how events are recorded); Andres approved it in chat.
  - **Typed-command logging.** The kit hook logs each typed command by name on UserPromptExpansion (tested on 2.1.312; arguments and prompt never written). It changes how evidence is recorded: `log/pending/M-006-command-logging.patch` and each repo's locked hook and settings wait on Andres.
  - **Observation.** `lessons/observations.md` records how this layer missed skills: a design drawn from a team metaphor, checked against the metaphor rather than the platform's building blocks.
- **Why:** each system's recent work was mostly freehand (architecture proposals, investigations) that no command or skill covered, and nothing asked whether it should be.
- **Verdict:** n/a (decisions)

## M-005 · 2026-10-30 · Kit 2.2: skills are part of the evolvable body
<!-- claim: maintenance none; landed: 2026-10-30 -->
Not a self-change: Andres's ruling that the systems build and improve skills as
well as agents. A skill holds know-how any session or agent loads when the task
matches its description; an agent holds separation.

- **What changed:**
  - **Kit 2.2.** `kit/docs/loop.md` gains § Agents and skills and names `.claude/skills/` as part of a self-change; the deeper pass and `kit/commands/evolve.md` ask of each skill what they ask of each agent; `kit/tools/crew_report.py` lists every skill with its load count.
  - **Playbook.** § No org chart gains one bullet: skills hold know-how, agents hold separation, and "a skill usually beats a new agent" is a heuristic each system's loop may revise.
  - **Systems.** zesty C-005, engage C-006 and dpi C-004 landed the same docs, `/evolve` and crew report, each through its own change-reviewer (two CONCERNs and one LAND, every point fixed before landing).
  - **Skill-load logging escalated.** This layer's change-reviewer said ESCALATE: the kit hook and settings matcher change how evidence is recorded. The kit half is `log/pending/M-005-skill-logging.patch`; each repo's locked hook and matcher are staged. Both wait on Andres (`HANDOFF.md`); until then every skill reads "never loaded".
- **Why:** agents were the only unit the loop could grow, so know-how had to become another agent or sit in the boot path.
- **Verdict:** n/a (decisions)

## M-004 · 2026-10-29 · Auto memory off; its notes go to intake for the loop
<!-- claim: maintenance none; landed: 2026-10-29 -->
Not a self-change: Andres's decision. Claude Code's auto memory kept
machine-local notes that loaded into every session, outside git and outside
the loop, so nothing ever judged them.

- **What changed:**
  - **Auto memory off.** `"autoMemoryEnabled": false` is in `kit/settings.kernel.json`, and staged in each repo's locked `.claude/settings.json` for Andres to apply.
  - **Intake.** Each repo has `memory/intake/`. The existing notes were copied there verbatim, neither imposed nor archived unread. The loop judges each one at the next deeper pass: fold it in as a self-change, keep it as knowledge, or set it aside, with a `knowledge` event, then archive it (`kit/docs/loop.md` § Deeper pass, `meta/keeper.md` § 9). Andres may drop notes there too.
  - **Trigger.** The kit boot check prints how many notes are waiting and counts them as a reason a deeper pass is due (staged for the locked copies).
  - **Public repo.** This layer's intake holds 7 of its 11 files; the rest stay machine-local because they carry employer-internal detail or a colleague's name.
- **Why:** memory the loop cannot see is memory nothing can correct.
- **Verdict:** n/a (decisions)

## M-003 · 2026-10-29 · Trust over gates: keep by default, reviewer as second opinion, S3 from follow-ups
<!-- claim: maintenance none; landed: 2026-10-29 -->
Not a self-change: Andres's ruling, "give the AI more trust and ability to
evolve and do its own thing … not gated by humans". At about two merged PRs a
week the per-change verdict is mostly noise: a change that does nothing reads
"helped" or "worse" about 40% of the time each, and both "no effect" and
"worse" reverted it, so useful changes were undone on a coin flip.

- **What changed:**
  - **Keep by default.** A verdict is evidence the system reads, never an automatic revert. *Helped* stays and becomes a playbook candidate. *No effect*, or too little data by the 60-day cap, stays as "unproven". *Looks worse* is the system's own call, recorded with its reasoning, and shown in "what has changed?" and the weekly roll-up as information, not as a request. A change is reverted only for clear harm: an escape traced to it, Andres saying it made things worse, or the system's own judgement.
  - **Guardrails.** Escapes (S1) and escalations (S4) can no longer be claimed; claiming fewer escalations was the gaming path. Both are printed beside every verdict.
  - **The change-reviewer is a second opinion.** It says LAND, CONCERN ("I would not, here is why"; the system may land anyway and records why) or ESCALATE. It escalates only a change that weakens a hard line or safety rule, changes how evidence is recorded, or traces back to outside content rather than the system's own evidence.
  - **S3 stops being self-graded.** It now counts Andres's follow-ups per merged PR: follow-up prompts from the raw prompt log (time and session only, never the text) plus the GitHub signals as before. Correction notes the agents write stay as learning evidence but are no longer scored, so nothing rewards under-logging them. Agents can no longer edit the raw prompt log.
  - **Kit 2.1** carries all of this. The locked half in each repo (charter line, scoreboard, hooks, reviewer) is staged for Andres to apply and relock in his own terminal.
- **Why:** "give the AI more trust and ability to evolve and do its own thing … not gated by humans."
- **Verdict:** n/a (decisions)

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
