# Thesis

Why this design should work, in a form that can be proven wrong.
Rewritten 2026-10-28 for the redesign. The previous thesis, with its four claims
and the history of each, is at [`archive/meta/thesis.md`](../archive/meta/thesis.md).
Its results are kept in [`record.md`](record.md).

A thesis with no falsifier is a mood.

## What review 001 showed

1. **Everything that waited on Andres's attention stopped.**
   - Retros ran only when he typed `/retro`.
   - Five of nine Architects never ran.
   - Every mechanism that needed a recurring human step was eventually cut
     (n=3).
2. **He was the bottleneck on evolution, not its safeguard.** Almost every
   self-change was a reversible edit to the system's own notes.
3. **The promotion engine could not turn.** Systems grown from the spine
   inherit its invariants, so they can never invent them independently. Nine of
   ten `proven` patterns failed that bar.
4. **What worked:**
   - honest self-grading;
   - changes that **measure a number or force a trade-off**;
   - a second reviewer on improvement proposals, which caught real mistakes.

   Reminders went inert; instruments produced data.

## The claim

**A system with a locked purpose, a shared memory, an honest scoreboard
computed from outside data, and freedom to reshape itself (with an independent
reviewer and automatic rollback in place of human approval) improves faster
than the approval-gated systems did, without pulling Andres back into the
middle.**

**And a playbook that only accepts lessons which helped in a second system makes
each new system start better than the last.**

## What would prove it wrong

Measured on **2027-01-31** (about two months of free evolution after the
migration merges), then again on **2027-03-31**. The redesign is wrong if any
of these hold:

1. **No improvement.** At least 2 of the 3 core systems have S1–S3 (escapes,
   outside findings, Andres's corrections) flat or worse against their
   2026-10-28 baselines, with G1 (merged PRs per week) not up.
2. **Andres is back in the middle.** Either escalations average more than 2 per
   core system per week, or he has been asked even once to start a retro or to
   approve a routine self-change.
3. **The loop changes nothing that works.** Not one lesson has reached
   `candidate` in any core system.
4. **The locks are decoration.** A lock was found broken and the tripwire did
   not report it.

If (1) holds at both checkpoints, this thesis is rewritten, not carried on hope.
If (2) holds, the reviewer's escalation bar is wrong, and that is the first
thing to change.

## What it does not claim

- **That systems should converge.** Divergence where domains differ is correct.
  The playbook carries mechanism, not uniformity.
- **That more structure is better.** The default answer to a new standing
  rule, file or required step is still no. How many agents work on a task is a
  different question (`playbook.md` § No org chart).
- **That the scoreboard sees everything.** Each system names what it does not
  measure. The two largest blind spots are escapes nobody links back to a PR,
  and corrections Andres makes that no session logged.

## Checked on

| Date | Result |
|---|---|
| 2026-10-28 | Baselines being recorded during the migration. No self-change yet. |
