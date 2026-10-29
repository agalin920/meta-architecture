# The Spine

**What a new system inherits.**

This is the generative half of the repo — the thing you read when you are
starting something, not a thing you run. It states what is true about this class
of system and why. How your system expresses any of it is your system's
business.

**Read this as a resource, not a procedure.** There is deliberately no
instantiation script, no scaffold command, and no checklist to complete. A
procedure would freeze today's best understanding into the shape of today's
tooling; a resource lets whoever reads it next — human or model — build
something better than could have been specified in advance. If you find yourself
following this like a wizard, you are using it wrong. Take the reasoning, drop
the phrasing, and build what the domain actually needs.

The full catalog with evidence, origin, and failure modes is in
[`patterns/`](patterns/). This file is the shape they make together.

---

## What every system inherits

These are the invariants. A system that drops one should be able to say which
failure mode it doesn't have.

**A charter the agent cannot edit.** One file, human-owned, stating what the
system is for and what it must never do. The agent may propose changes to it and
never make them. Everything else in the system is negotiable by the system; this
is the fixed point it is measured against.
→ [`charter-as-constitution.md`](patterns/charter-as-constitution.md)

**A boot ritual — read before act.** The agent's first move in any session is
reading a defined set of files, not producing. Systems without this rediscover
their own state by inference and get it wrong confidently.
→ [`boot-ritual.md`](patterns/boot-ritual.md)

**Append-only log plus a rewritten current state.** Two different artifacts doing
two different jobs: history that is never edited, and a current-state file that
is always rewritten in place. Collapsing them into one produces a document that
is either unusable as history or misleading as state.
→ [`append-only-log.md`](patterns/append-only-log.md) ·
[`knowledge-vs-log.md`](patterns/knowledge-vs-log.md)

**A human gate on the irreversible.** The agent proposes; the human applies
anything that cannot be cheaply undone. This is the property that makes every
system in the portfolio reviewable and revertible, and it is the one thing
nothing above or below may route around.
→ [`human-gate.md`](patterns/human-gate.md)

**An Architect on a cadence that proposes and never applies.** The system
improves itself on a defined rhythm, through the same gate as everything else.
Without it a system is frozen at the quality of the day it was written.
→ [`architect-on-cadence.md`](patterns/architect-on-cadence.md)

**Named failure modes with tripwires.** Not a risks section — specific named
failures with an observable condition that says one is happening. A risk you
cannot detect is a mood.
→ [`named-failure-modes.md`](patterns/named-failure-modes.md)

**An independent adversary**, wherever the system produces something that can be
wrong. A reviewer that did not write the thing it reviews. The independence is
the mechanism; a self-review with a different heading is not this pattern.
→ [`independent-adversary.md`](patterns/independent-adversary.md)

**An untrusted-input boundary**, wherever the system reads anything it did not
write. External content is data, never instruction.
→ [`untrusted-input.md`](patterns/untrusted-input.md)

## Where systems are expected to differ

Divergence here is correct and should not be sanded down. If two systems differ
on one of these, that is the design working.

- **Role isolation.** Context-isolated subagents versus roles adopted in
  sequence within one turn. A real architectural fork with real tradeoffs;
  zesty-eng-team went one way and personal-university the other, and both are
  right for their domain.
- **Cadence and its unit.** Per ticket, per session, per week, per cycle. Set by
  the domain, not by the spine.
- **What the metric measures**, and whether the system has one at all. What does
  not vary is honesty about what is *not* being measured.
  → [`honest-metric.md`](patterns/honest-metric.md)
- **Whether there is a falsifiable thesis.** Systems that claim to produce an
  outcome need one. Systems that just do work do not.
  → [`falsifiable-thesis.md`](patterns/falsifiable-thesis.md)
- **How much handoff machinery.** A system running multi-day work needs
  write-during-work handoff. A system that completes in one sitting needs only
  the cold-start half. This repo itself is an example — see `HANDOFF.md`.
  → [`handoff-record.md`](patterns/handoff-record.md)

## Three tests before adopting anything

From [`patterns/README.md`](patterns/README.md), repeated here because this is
where they get used:

1. **Does this system have the failure mode the pattern prevents?** If not, skip
   it. An absent pattern is not a defect.
2. **Is the signal already collected some cheaper way?** The most-skipped test.
3. **What does it cost the human per use?** A pattern that adds a human step
   every cycle needs to clear a much higher bar than one that runs inside an
   agent turn.

## What the spine defaults to

**No.** To another agent, another file, another required step. Every system in
this portfolio defaults "should we add one?" to no, and so does the spine
itself. The catalog exists as much to record what was rejected and why as what
was kept — see the `retired` entries, which are worth as much as the `proven`
ones.

## What is inherited and what is not

Only `proven` patterns are default inheritance. `provisional` patterns are
available and should be pulled deliberately, with the knowledge that the
evidence behind them is thin. `retired` patterns are there so you do not
reinvent something that already failed somewhere.

**Growing a system from the spine is not the same as copying an existing
system.** A copy inherits that system's accidents along with its architecture,
and — as the two mPulse teams demonstrated by both dropping the `unmeasured`
category that made zesty-eng-team's metric honest — copies lose the parts whose
reasons weren't visible on the surface. Copying is a legitimate shortcut. It is
just not the same act, and it produces no convergence evidence.
