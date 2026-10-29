# Architect on cadence

**Status:** `proven` — all three agentic systems
**Invented in:** convergent, with a documented lineage — zesty-eng-team's
decision log records the retro loop as carried over from an earlier project.

## The pattern

A meta-agent that improves the system rather than operating it. It:

- **Runs on a cadence, never on impulse** — every 10 sessions, every 4 weeks,
  every retro.
- **Never runs inside a production cycle.**
- **Proposes; never applies.** The human applies accepted proposals.
- **Cites evidence for every finding.** No finding without a session id, PR
  number, draft filename, or date.
- **Audits its own past proposals.** *A proposal whose effect you never checked
  was a guess.*
- **Withdraws findings in writing** when later evidence contradicts them.

## Why it works

The propose-never-apply gate is the whole thing. It is what makes a
self-modifying system reviewable and revertible, and zesty-eng-team says so
directly: *"That single gate is what keeps a self-modifying system reviewable
and revertible — do not route around it."*

The cadence limit is equally load-bearing and less obvious. Every one of these
Architects carries a warning about its own overuse, in nearly the same words:
*"if Architect sessions start outnumbering lessons, that is the failure mode
announcing itself: building the school is more fun than doing the work in it."*

## Evidence

- `personal-university/agents/architect.md` — every 10 sessions. Audits
  calibration first, checks all four thesis falsifiers, absorbs two roles that
  were considered and rejected rather than spawning them.
- `zesty-eng-team/.claude/agents/architect.md` — proposals must be **precise
  diffs**: exact file, exact text before and after, the specific observed
  failure, and what should change by the next retro. The strongest proposal
  format in the portfolio.
- `brand-system/agents/architect.md` — every 4 weeks; runs the emergent
  signature clustering first, and includes a self-invalidating check (*is this
  the operator's signature or the Scout's?*).

## Notable sub-patterns worth copying

- **Precise-diff proposals** (ZET) — *"A proposal without evidence behind it is
  a preference, and preferences do not go in."* Also: prefer the smallest change,
  because rewriting an agent wholesale destroys the evidence about which part
  was wrong.
- **Stability is a valid finding** (ZET) — *"If two retros in a row produce no
  evidence-backed proposal, say so. Churn for its own sake makes the team worse."*
- **Propose retirement, not just tuning** (ZET) — watch for a role that never
  gets used, or one where the fix is a different model or a split rather than a
  prompt edit.
- **Run the invalidating check first** (BS) — before proposing a signature,
  check the thing that would make it spurious.

## How it fails

- **Running too often.** Named by every implementation.
- **Only ever adding.** An Architect that has never proposed cutting a role, a
  field, or a cadence is not reading its own overhead ceiling.
- **Grading its own homework.** It audits its own proposals, which is right and
  not sufficient — the same coupling the [adversary](independent-adversary.md)
  exists to break one level down. This is why `meta/architect.md` in this repo
  audits the Architects.
