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
| `unit` | A unit of work finished | outcome, and the gap from the plan |
| `loop` | The loop ran for that ref | what it did |
| `agent` | Once per subagent the unit used | `<name> · changed\|confirmed\|unused\|wrong · <one line>` |
| `correction` | Andres corrected the work, in chat or on GitHub | `<class-slug> · <what he caught, where we should have caught it>` |
| `escalation` | Something was routed to Andres | |
| `change` | A self-change landed | |
| `reviewed` | The change-reviewer decided, every time, REJECTs included (ref C-NNN) | `LAND\|ESCALATE\|REJECT · <one line>` |
| `verdict` | A verdict on a change | |
| `revert` | A change was rolled back | |
| `lesson` | A lesson worth keeping | |
| `knowledge` | A fact in knowledge proved wrong | the fact, its age from `git blame`, what was true |
| `env` | The boot check said instruction channels changed | which, and what changed |
| `decision` | A decision, with its reason | |
| `trial` | A playbook trial was taken up | |
| `deep pass` | A deeper pass finished (ref `deep pass`) | what it found and what landed |

`state`, `finding` and `review` are also accepted. A correction's class is a
short slug the session chooses (`missed-edge-case`, `wrong-branch`); reuse an
existing one when it fits (`python3 tools/crew_report.py --corrections` lists
them). Recurrence of a class is what triggers a deeper pass.

Evidence the session does not write: `log/spawns-YYYY-MM.md` (every subagent
spawn, by a hook, committed) and `log/raw/prompts-YYYY-MM.jsonl` (Andres's
prompts, by a hook, gitignored because they can hold sensitive text).

The ref is the PR, ticket, or change id. A unit that spans several PRs takes
its worklog slug as the ref, and is dated when its last PR merged or its last
act happened. Corrections are `correction` events from 2026-10-29 on, not
bullets under a worklog's old findings heading, which the scoreboard reads
only for earlier dates. **The date is when it happened, not
when it was written.** A late entry still goes at the end of the file, carrying
its true date, so scores count it in the right window.

Every git command names its repo: `git -C <repo> …`. Agent commits carry the
`Co-Authored-By: Claude …` trailer; the scoreboard uses it to tell agent
commits from Andres's.

## Every unit (light, a few minutes)

0. **Begin.** Every work command writes `| begin | <ref> |` as its first step,
   so a unit whose loop never ran is still caught at the next boot.
1. **What happened against what we expected.** Write the `unit` event: the
   outcome, and one line on the gap between plan and reality. Name the review
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
decisions and their outcomes), with one standing question: **for each subagent
and the change-reviewer, would we define this one today, given its record?**
It proposes at most three self-changes, each with a claim. It must say what it
would **cut**; "nothing should be cut, because…" is a valid answer, and silence
is not. It ends with a `deep pass` event.

## Escape tripwire

When an escape lands (S1 counts a new one), list every change that landed in
the 30 days before that PR merged. The next deeper pass looks at them first.

## A self-change

A self-change is anything that changes how the system behaves: `CLAUDE.md`,
`docs/`, `.claude/agents/`, `.claude/commands/`, `tools/`, and any removal or
condensing of knowledge.

1. Make the edit in the working tree. Do not commit yet.
2. Draft its CHANGELOG entry (format in `CHANGELOG.md`), with a claim: one
   leading measure (S2, S3, S4, G1 or a health reading) and a direction, or
   `maintenance none; …; files: a,b` listing every file it touches. **S1 cannot be claimed.** Escapes only count once a PR
   is 30 days old, so no window can see a change move them. S1 is watched by
   the tripwire below.
3. For a compaction, run `python3 tools/conservation_check.py` and move the
   original verbatim to `archive/` first.
4. Hand the diff, the entry, and any check output to the **change-reviewer**
   agent. Write a `reviewed` event for its decision, whatever it is.
   - `LAND`: commit only that change, as `evolve(C-NNN): <what>`, with the
     entry. Fill in the `commit:` sha in a follow-up memory commit. Write a
     `change` event.
   - `ESCALATE`: save the diff to `log/pending/C-NNN.patch`, restore the
     files, and add one line under `## Waiting on Andres: system` in `state.md`.
     When Andres approves it, the session applies `log/pending/C-NNN.patch`,
     commits it as `evolve(C-NNN): <what>` with "approved by Andres" in the
     message, and writes a `reviewed` event (`LAND · approved by Andres`) and a
     `change` event.
   - `REJECT`: restore the files. Write a `lesson` event if the rejection
     taught something.

## Waiting on Andres: two lists

`state.md` keeps two lists, because they need different things from him.

- **`## Waiting on Andres: system`**: charter or scoreboard proposals (S-NNN),
  self-changes the change reviewer escalated (C-NNN), and anything about the
  locks. These are about how the system works. Every session leads with them,
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

1. **One open proposal per kind** (one for the charter, one for the scoreboard).
   If one is already open, strengthen it or withdraw it; don't add a second.
2. Write `log/pending/S-NNN.md`:

   ```
   # S-NNN · <the change in one sentence>
   - **Kind:** scoreboard | charter
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
| `worse` | Ask the change-reviewer to confirm. Then `git -C <repo> revert <commit>`, set **Verdict** to `reverted: worse (<numbers>)`, and add the lesson to `lessons.md` as `retired`, with the reason |
| `no effect` | Revert the same way, set **Verdict** to `reverted: no effect (<numbers>)`, and record the lesson with status "no measured effect". It is retryable, not retired |
| `insufficient data` | Leave it open; set **Verdict** to `open (extended to <date>: insufficient data)` as the script says |
| re-read | A kept change over 60 days old is listed once. Append `re-read <date>: <result>` to its Verdict; if it turned worse, take it to the change-reviewer |

Write a `verdict` event for each. `verdicts.py` names other changes on the same
measure in an overlapping window; say in the Verdict that the credit is shared.
