# Independent adversary

**Status:** `proven` — all three agentic systems
**Invented in:** personal-university (the Examiner), independently in
zesty-eng-team (the reviewer)
**Adopted by:** brand-system 2026-08-09 (the Critic)

## The pattern

**Whoever produces does not grade.** A separate role, with no investment in the
work existing, judges it before it reaches the human — and that role never
produces.

It must be able to fail the work, and it is itself measured on whether its
verdicts predict what the human later finds.

## Why it works

Self-review is structurally blind. The context that wrote the sentence is the
least able to see what is generic about it; the context that wrote the fix is
the least able to see what it broke. This is not a capability problem and a
better prompt does not solve it.

The deeper argument is about **leading versus lagging indicators**, and
personal-university's thesis makes it exactly: the review queue catches grade
inflation weeks later, *after the Planner has already acted on the lie.* The
adversary catches it in the same session.

## Evidence

- `personal-university/agents/examiner.md` — never teaches, and the score that
  goes in the log is the Examiner's where they diverge. Divergence is tracked
  per Professor as the grade-inflation signal.
- `zesty-eng-team/.claude/agents/reviewer.md` — *"Adversarial review of a diff
  it did not write. Mandatory before every PR."* Its value is documented in
  practice: on ticket #3909 the cold review caught `wordHighlighter` sharing the
  crash's failure shape and **materially changed the fix.**
- `brand-system/agents/critic.md` — added 2026-08-09. Before it, the only
  per-cycle check on the system's own named #1 failure was the Writer critiquing
  its own draft.

## Design requirements

Learned across the three implementations:

1. **It must never produce.** The Critic is forbidden from supplying prose; the
   moment it does, it is an editor and the separation is gone.
2. **It must be able to kill**, not just flag. A role that can only suggest gets
   routed around.
3. **It must be scored.** Examiner-vs-Professor divergence; Critic-vs-human
   divergence in `brand-system/progress/critic-log.md`. **An adversary nobody
   scores becomes an approver**, and reads as rigour while providing none.
4. **"Looks fine" is not an available verdict.** Both the Critic and the
   Architect voice check say this explicitly.

## How it fails

- **Never disagreeing.** Then it is ceremony with a cost.
- **Always disagreeing.** Then it is noise and the producer learns to ignore it.
- **Being merged back for efficiency.** personal-university names this as a
  thesis falsifier: if Examiner and Professor never diverge, the separation is
  ceremony and should be merged. That is the honest version — cut it on
  evidence, not on convenience.
