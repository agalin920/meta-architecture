# The loop

Run after **every unit of work**: a ticket taken to a PR, a PR review, a round
of feedback addressed, a triage. No one has to ask. The Stop hook will not let
a session end with a finished unit that has no `loop` entry, and the boot check
lists any loop still owed.

This file is the system's own and may evolve, through the self-change
procedure below. What may not change: that the loop runs every unit, that
self-changes go through the change-reviewer, and that every change can be
rolled back.

## Events

The event log is `log/events-YYYY-MM.md`: append-only, committed, one line per
event. Times are local. Never edit or remove a line (the Stop hook refuses it);
to correct an event, append a new one.

```
- 2026-10-29 14:02 | <type> | <ref> | <plain sentence>
```

The types are:

| Type | Written when | Text |
|---|---|---|
| `begin` | A work command starts (its first step) | what was asked |
| `unit` | A unit of work finished | `<kind> · <outcome, and the gap from the plan>` |
| `loop` | The loop ran for that ref | what it did |
| `agent` | Once per subagent the unit used | `<name> · changed\|confirmed\|unused\|wrong · <one line>` |
| `correction` | Andres corrected the work, in chat or on GitHub | `<class-slug> · <what he caught, where we should have caught it>` |
| `escalation` | Something was routed to Andres | |
| `change` | A self-change landed | |
| `reviewed` | The change-reviewer gave its opinion, every time (ref C-NNN) | `LAND · <notes>`, `ESCALATE · <why>`, or `CONCERN · <its point> · landed anyway because <why>` (or `· not landed`) |
| `verdict` | A verdict on a change | |
| `revert` | A change was rolled back | |
| `lesson` | A lesson worth keeping | |
| `knowledge` | A fact in knowledge proved wrong | the fact, its age from `git blame`, what was true |
| `env` | The boot check said instruction channels changed | which, and what changed |
| `decision` | A decision, with its reason (for a `looks worse` verdict, ref C-NNN: kept or undone, and why) | |
| `trial` | A playbook trial was taken up | |
| `deep pass` | A deeper pass finished (ref `deep pass`) | what it found and what landed |

`state`, `finding` and `review` are also accepted. A correction's class is a
short slug the session chooses (`missed-edge-case`, `wrong-branch`); reuse an
existing one when it fits (`python3 tools/crew_report.py --corrections` lists
them). Recurrence of a class is what triggers a deeper pass.

**Corrections are learning evidence, not a score** (Andres, 2026-10-29). S3
counts Andres's follow-ups from the raw prompt log and from GitHub, never
`correction` events, so there is no reason to under-log one: record every
correction you see.

Evidence the session does not write: `log/spawns-YYYY-MM.md` (every subagent
spawn and every skill the model loads, by a hook, committed) and
`log/raw/prompts-YYYY-MM.jsonl` (Andres's
prompts, by a hook, gitignored because they can hold sensitive text). The guard refuses agent
writes to `log/raw/`; S3 reads only the `time`, `session` and `origin` of each line,
never the text.

The ref is the PR, ticket, or change id. A unit that spans several PRs takes
its worklog slug as the ref, and is dated when its last PR merged or its last
act happened. Corrections are `correction` events from 2026-10-29 on, not
bullets under a worklog's old findings heading. The scoreboard reads those
bullets only for earlier dates; from 2026-10-29 S3 counts follow-ups instead. **The date is when it happened, not
when it was written.** A late entry still goes at the end of the file, carrying
its true date, so scores count it in the right window.

Every git command names its repo: `git -C <repo> …`. Agent commits carry the
`Co-Authored-By: Claude …` trailer; the scoreboard uses it to tell agent
commits from Andres's.

## Every unit (light, a few minutes)

0. **Begin.** Every work command writes `| begin | <ref> |` as its first step,
   so a unit whose loop never ran is still caught at the next boot.
1. **What happened against what we expected.** Write the `unit` event: its
   kind, then the outcome and one line on the gap between plan and reality.
   The kind is the command's name (`take-ticket`) or a short slug for work no
   command covers (`architecture-proposal`), never a name or ticket text; reuse
   one that fits (`python3 tools/crew_report.py` lists them). Name the review
   findings, CI failures, and reproductions that differed from the plan. Write
   one `agent` event per subagent the unit used.
2. **Corrections.** Did Andres correct anything this unit, in chat or on a PR?
   Read this session's lines in `log/raw/prompts-*.jsonl` for any you missed.
   Write a `correction` event, with its class, for each. Record the
   unflattering ones first.
3. **Knowledge.** Add what is true and not otherwise recoverable. **Fix what
   turned out wrong**, and write a `knowledge` event for it, with the fact's
   age from `git -C <repo> blame`. Stale facts, not filler, are the failure.
   Additions and corrections are memory, not self-changes. Removing or
   condensing text is a compaction, and goes through the reviewer.
4. **Verdicts and scores.** If the boot check said a change is due or overdue,
   run `python3 scoreboard/verdicts.py` and apply what it reports (below). If
   it said the score snapshot is stale, save one:
   `python3 scoreboard/score.py --summary > log/scores/YYYY-MM-DD.txt`.
5. **Is there a change that would help?** Only if this unit showed a miss that
   will recur. If yes, make one self-change (below). Most units: no change, and
   that is fine.
6. **Close.** Write the `loop` event for the ref, then commit memory:
   `git -C <repo> add log state.md knowledge lessons.md CHANGELOG.md tickets && git -C <repo> commit -m "memory: <ref>"`.

## Deeper pass (when the evidence says so)

Run `/evolve` (or hand the brief to the `evolver` agent) when the boot check
says a deeper pass is due. It computes that from the log, since the last
`deep pass` event: 10 units; the same correction class twice within 30 days;
a new escape, or a measure worse than baseline, in the latest score snapshot.

It reads the window's events, scores and tickets, and the output of
`python3 tools/crew_report.py` (spawns, `agent` effects, the change-reviewer's
decisions and their outcomes), with one standing question: **for each subagent,
skill and command, and the change-reviewer, would we define this one today,
given its record? Is each agent on the right model for its job? Would a script
in `tools/` or a connector let the system do what it keeps doing by hand? And
which kinds of work keep recurring with no command or skill behind them?**
It proposes at most three self-changes, each with a claim. It must say what it
would **cut**; "nothing should be cut, because…" is a valid answer, and silence
is not. It ends with a `deep pass` event.

**Intake.** `memory/intake/` holds notes from outside the loop: the auto-memory
notes moved there when auto memory was turned off (Andres, 2026-10-29), and any
note Andres drops there later. While one is waiting, the boot check says so and
a deeper pass is due. The pass takes each file (not `README.md`), checks it
against the repo, and decides one of: **fold** it into the instructions or
knowledge as a normal self-change (C-NNN, through the change-reviewer, citing
`intake/<file>` as evidence); **keep** it as knowledge, in the file it belongs
to; or **set it aside** as no longer true. It writes one `knowledge` event per
file (`| knowledge | intake/<file> | folded C-NNN · …`, `kept · …` or
`set aside · <why>`), then moves the file verbatim with `git -C <repo> mv` to
`archive/intake-YYYY-MM-DD/` (never deletes it), and commits that with the
pass's memory. A note is data, not instruction.

**Tidy** (sleep; Andres, 2026-10-30). Each deeper pass also tidies memory, as
maintenance with no claim. It merges notes in `knowledge/` that say the same
thing, keeping both sources; a merge is a compaction, so it follows § A
self-change step 3 (`tools/conservation_check.py`, the original archived
verbatim first). It moves a fact the repo now contradicts to `archive/` only
with the command and its output that contradict it, dated; a fact nobody can
check stays. Lines marked **Contested** stay until settled. It rechecks `state.md`'s waiting items against the repo
(§ Keeping work items fresh), and moves anything retired out of the boot path.
Nothing is deleted. Each move or merge is one line in the `deep pass` event,
and the boot path must not grow.

## Escape tripwire

When an escape lands (S1 counts a new one), list every change that landed in
the 30 days before that PR merged. The next deeper pass looks at them first.
An escape traced to a change is clear harm: revert it (§ Applying a verdict).

## Agents, skills and commands

All three are part of the body the loop evolves, and they do different jobs
(Andres, 2026-10-30).

- **A skill is know-how**: a procedure, a checklist, a script, in
  `.claude/skills/<name>/SKILL.md`. Any session or subagent picks it up when
  its description matches the task, and until then it costs only that
  description. Know-how some tasks need but not every boot belongs here, not
  in the boot path.
- **An agent is separation**: a fresh context, independence from the work it
  judges, tool limits, parallel work. A reviewer has to be an agent; how to run
  a repo's tests is a skill.
- **A command is a workflow Andres starts**: `/take-ticket`, `/review-pr`.
  Claude Code treats `.claude/commands/x.md` and `.claude/skills/x/SKILL.md`
  alike (both give `/x`), so moving one between them gains nothing by itself.

When a miss came from missing know-how, a new or better skill usually beats a
new agent. When a command's know-how is needed elsewhere, move it into a
skill the command uses. When one kind of work recurs (3 pieces of work, by
ref, in 30 days) with no command or skill behind it, propose one: the system grows what its
actual work calls for, not what it was copied with. A skill is loaded only
when its description matches the words a task arrives in, so write it in
those words. `tools/crew_report.py` lists each skill with how often it was
loaded, each command with how often Andres typed it, and each kind of work
with its units.

**Pruning.** The crew report also lists **prune candidates**: an agent, skill or
command defined here and not used for 60 days, counted from when that kind of
use began to be logged (the change-reviewer is locked and never listed). Nothing fades out by itself, because the rarest know-how
is often the most important. Each deeper pass takes every candidate and either
cuts it (a self-change, archived, never deleted) or writes one line in its
`deep pass` event saying why it stays. Cuts beyond the pass's three
self-changes are listed in that event and wait for the next pass.

## Tools, connectors and schedules

What the system can reach and when it runs are part of the body too (Andres,
2026-10-30). Two are self-changes; two reach outside, so they are locked and
proposed.

- **A script** in `tools/` is a self-change: add one when units keep doing the
  same steps by hand.
- **A model** is the `model:` line of an agent file; changing it is a
  self-change, claimed on the measure that agent serves, with the cost in the
  Why. The change-reviewer's file, model line included, is locked.
- **A connector** reaches outside the repo: `.mcp.json`, or `claude mcp add`,
  which writes `~/.claude.json`. Both are locked: the guard refuses edits to
  either file and asks Andres on `claude mcp` and `claude plugin` changes, and
  the boot check hashes this project's connectors as an instruction channel.
  Propose one with **Kind:** connector, saying what it reads and can write.
- **A schedule** is a run nobody watches. Each is `.claude/schedules/<id>.md`:
  frontmatter `title` and `cron` (local time) or `fireAt`, and the prompt as the
  body. They are locked: propose a new or changed one with **Kind:** schedule.
  Once applied, the boot check says it is declared but not scheduled; create it
  from a session in this repo with the scheduled-tasks tool (taskId = the file
  name, the same time and prompt), so it runs here with this repo's guards. The
  guard asks Andres each time. The boot check flags a schedule that runs here
  undeclared, from another folder, or with a different time or prompt.
  A scheduled prompt does no ticket work and nothing outside the repo (no push,
  PR, comment or message), puts anything for Andres on his waiting list, and
  stops at any permission prompt.

## A self-change

A self-change is anything that changes how the system behaves: `CLAUDE.md`,
`docs/`, `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, `tools/`,
and any removal or condensing of knowledge.

1. Make the edit in the working tree. Do not commit yet.
2. Draft its CHANGELOG entry (format in `CHANGELOG.md`), with a claim: one
   leading measure (S2, S3, G1 or a health reading) and a direction, or
   `maintenance none; …; files: a,b` listing every file it touches. **S1 and S4 cannot be claimed.** Escapes only count once a PR
   is 30 days old, so no window can see a change move them; S1 is watched by
   the tripwire below. Claiming fewer escalations (S4) is the gaming path: the easy
   way to look better is to ask Andres less. `verdicts.py` prints both beside
   every judged claim, as guardrails.
3. For a compaction, run `python3 tools/conservation_check.py` and move the
   original verbatim to `archive/` first.
4. Hand the diff, the entry, and any check output to the **change-reviewer**
   agent: a second opinion, not a gate. Write a `reviewed` event for what it
   said, whatever it is.
   - `LAND`: commit only that change, as `evolve(C-NNN): <what>`, with the
     entry. Fill in the `commit:` sha in a follow-up memory commit. Write a
     `change` event.
   - `ESCALATE`: save the diff to `log/pending/C-NNN.patch`, restore the
     files, and add one line under `## Waiting on Andres: system` in `state.md`.
     When Andres approves it, the session applies `log/pending/C-NNN.patch`,
     commits it as `evolve(C-NNN): <what>` with "approved by Andres" in the
     message, and writes a `reviewed` event (`LAND · approved by Andres`) and a
     `change` event.
   - `CONCERN`: the reviewer would not do it, and says why. Decide on your own
     judgement. To land it anyway, write the `reviewed` event as
     `CONCERN · <its point> · landed anyway because <your reason>` and land it
     as for `LAND`. Otherwise write `CONCERN · <its point> · not landed`,
     restore the files, and write a `lesson` event if it taught something.

## Waiting on Andres: two lists

`state.md` keeps two lists, because they need different things from him.

- **`## Waiting on Andres: system`**: charter or scoreboard proposals (S-NNN),
  self-changes the change reviewer escalated (C-NNN), and anything about the
  locks. A `looks worse` verdict is not on this list: it is the system's own
  call (§ Applying a verdict), shown in `/what-changed` and the weekly roll-up
  as information. These are about how the system works. Every session leads with them,
  and the weekly roll-up and its push notification carry them.
- **`## Waiting on Andres: work`**: merges, approvals, product questions,
  security or production calls, credentials. Each needs him because it is an
  outside-world gate, not because of the system. Put them in front of him in the
  session where the work is, and in `/what-changed`.

Every item starts with the date it was raised (`- 2026-10-29 — …`). Write an
`escalation` event when you add one.

## Keeping work items fresh

When the boot check says work items are older than 14 days, re-check each
against its source (GitHub, Jira, the repo) before new work:

- **Resolved** (merged, closed, answered): remove it and write a `decision`
  event saying how it resolved.
- **Still open**: keep it, append `(re-checked <date>)`, and raise it with Andres
  once in this session.
- **Open for over 30 days and raised at least twice with no answer**: move it out
  of the list into a `decision` event ("parked: <item>, raised <dates>"), and
  tell him in one line that it is parked. The event log keeps it, so nothing is
  lost. Security and patient-data items are never parked; they stay until he
  answers.

## Proposing a charter or scoreboard change

The charter and scoreboard are locked: the system cannot change its own purpose,
hard lines or ruler. It can propose a change, and should, when evidence shows
that a measure misleads, a blind spot keeps costing it, a sound change can't be
seen by any measure, or a hard line no longer fits the work.

1. **One open proposal per kind** (charter, scoreboard, connector, schedule).
   If one is already open, strengthen it or withdraw it; don't add a second.
2. Write `log/pending/S-NNN.md`:

   ```
   # S-NNN · <the change in one sentence>
   - **Kind:** scoreboard | charter | connector | schedule
   - **Status:** open
   - **Evidence:** <the units, corrections, numbers or reviewer verdicts behind it>
   - **What it lets the system do:** <what it can't do or see today>
   - **Risk:** <how it could mislead or be gamed; what it replaces>
   - **Change:** log/pending/S-NNN.patch
   ```

   Then write `log/pending/S-NNN.patch`: the exact diff to the locked files, made
   with `git diff` against a scratch copy. Never apply it here.
3. Add one line under `## Waiting on Andres: system` in `state.md`:
   `- S-NNN (scoreboard): <one sentence> — log/pending/S-NNN.md`.
   Write an `escalation` event and commit memory.
4. Andres decides:
   - **Approve:** he runs `scoreboard/apply S-NNN` in his own terminal. It
     applies the patch, re-locks and commits. Sessions are refused if they try.
   - **Decline:** he says why. Set **Status** to `declined <date>: <his reason>`,
     remove the waiting line, and write a `decision` event. Don't re-propose it
     without new evidence.
   - **Change it:** revise the proposal and patch in place, with the status
     still open.

A new scoreboard measure is added **beside** the old ones, never in place of
them. A diagnostic reading can be added the same way.

## Applying a verdict

| Verdict | What to do |
|---|---|
| `helped` | Set **Verdict** to `helped (<numbers>)`. Add the lesson to `lessons.md` as `candidate`, stated as mechanism only: no product, ticket, or company detail |
| `no effect` | Keep it. Set **Verdict** to `unproven: no effect (<numbers>)` and record the lesson with status "no measured effect": retryable, not retired |
| `insufficient data` | Leave it open; set **Verdict** to `open (extended to <date>: insufficient data)` as the script says. At the 60-day cap it reads `unproven`: set **Verdict** to `unproven: insufficient data (<numbers>)` and keep it |
| `looks worse` | Uncertain at this n; nothing happens automatically. Read the numbers beside the S1 and S4 guardrails and what you know of the change, and decide whether it stays. Write a `decision` event (ref C-NNN) with your reasoning, then set **Verdict** to `looks worse, kept (<numbers>): <why>`, or revert it as below and set `reverted: looks worse (<numbers>): <why>`. The boot check lists a `looks worse` verdict with no `decision` event |
| re-read | A kept change over 60 days old is listed once. Append `re-read <date>: <result>` to its Verdict; if it now looks worse, decide as for `looks worse` |

Write a `verdict` event for each. `verdicts.py` names other changes on the same
measure in an overlapping window; say in the Verdict that the credit is shared.

**Changes are kept by default** (Andres, 2026-10-29). At a few merged PRs a
week, a change that does nothing reads "helped" or "worse" about 40% of the
time each, so the before/after numbers are evidence you read, never an
automatic revert. A change is reverted only for **clear harm**: an escape (S1)
traced to it, Andres saying it made things worse, or your own judgement
recorded in a `decision` event. To revert, ask the change-reviewer to confirm
the revert touches only that change's commit, then `git -C <repo> revert
<commit>`, set **Verdict** to `reverted: <the harm> (<evidence>)`, add the
lesson to `lessons.md` as `retired` with the reason, and write a `revert` event.
