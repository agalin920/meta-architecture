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
event.

```
- 2026-10-29 14:02 | <type> | <ref> | <plain sentence>
```

The types are:

| Type | Written when |
|---|---|
| `unit` | A unit of work finished |
| `loop` | The loop ran for that ref |
| `correction` | Andres corrected the work, in chat or on GitHub. What he caught, and where we should have caught it |
| `escalation` | Something was routed to Andres |
| `change` | A self-change landed |
| `verdict` | A verdict on a change |
| `revert` | A change was rolled back |
| `lesson` | A lesson worth keeping |
| `decision` | A decision, with its reason |
| `trial` | A playbook trial was taken up |

The ref is the PR, ticket, or change id. A unit that spans several PRs takes
its worklog slug as the ref, and is dated when its last PR merged or its last
act happened. Corrections are `correction` events from 2026-10-29 on, not
bullets under a worklog's old findings heading, which the scoreboard reads
only for earlier dates. **The date is when it happened, not
when it was written.** A late entry still goes at the end of the file, carrying
its true date, so scores count it in the right window.

## Every unit (light, a few minutes)

1. **What happened against what we expected.** Write the `unit` event: the
   outcome, and one line on the gap between plan and reality. Name the review
   findings, CI failures, and reproductions that differed from the plan.
2. **Corrections.** Did Andres correct anything this unit, in chat or on a PR?
   Write a `correction` event for each. Record the unflattering ones first.
3. **Knowledge.** Add what is true and not otherwise recoverable. **Fix what
   turned out wrong.** Stale facts, not filler, are the failure. Additions and
   corrections are memory, not self-changes. Removing or condensing text is a
   compaction, and goes through the reviewer.
4. **Verdicts.** If the boot check said a change is due, run
   `python3 scoreboard/verdicts.py` and apply what it reports (below).
5. **Is there a change that would help?** Only if this unit showed a miss that
   will recur. If yes, make one self-change (below). Most units: no change, and
   that is fine.
6. **Close.** Write the `loop` event for the ref, then commit memory:
   `git add log state.md knowledge lessons.md CHANGELOG.md tickets && git commit -m "memory: <ref>"`.

## Deeper pass (when the evidence says so)

Run `/evolve` (or hand the brief to the `evolver` agent) when any of these
holds:

- a score worsened at its last computation (`python3 scoreboard/score.py --summary`);
- the same kind of correction appears twice in 30 days;
- an escape landed (S1);
- 10 units have passed since the last deeper pass.

It reads the window's events, scores and tickets, and proposes at most three
self-changes, each with a claim. It must say what it would **cut**; "nothing
should be cut, because…" is a valid answer, and silence is not.

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
   `maintenance none`. **S1 cannot be claimed.** Escapes only count once a PR
   is 30 days old, so no window can see a change move them. S1 is watched by
   the tripwire below.
3. For a compaction, run `python3 tools/conservation_check.py` and move the
   original verbatim to `archive/` first.
4. Hand the diff, the entry, and any check output to the **change-reviewer**
   agent.
   - `LAND`: commit only that change, as `evolve(C-NNN): <what>`, with the
     entry. Fill in the `commit:` sha in a follow-up memory commit. Write a
     `change` event.
   - `ESCALATE`: save the diff to `log/pending/C-NNN.patch`, restore the
     files, and add one line under `## Waiting on Andres: system` in `state.md`.
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
| `worse` or `no effect` | Ask the change-reviewer to confirm. Then `git revert <commit>`, set **Verdict** to `reverted: <why>`, and add the lesson to `lessons.md` as `retired`, with the reason |
