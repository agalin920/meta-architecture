---
name: verify-preconditions-in-the-target-repo
description: "Before routing a cross-system finding to a child Architect, verify its precondition in that child's repo — not just the pattern across repos. Two of review 001a's most confident findings had false premises and both children caught it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2daf9026-c21e-4028-91a6-1f1fb6627fde
  modified: 2026-08-14T17:17:13.159Z
---

At review 001a (2026-08-13) two of the three findings this layer ranked most confident had **false premises in the repo they were aimed at**, and both child Architects caught it on their own evidence:

- **MF-1** claimed the subtraction question was "going unasked, four times out of four." `mpulse-engage-team` already mandates a `§ Cuts` section (`.claude/agents/architect.md:124`), produced one at retro 001, proposed a cut, and **rejected it with a recorded reason.** *Asked-and-answered is a different failure mode than unasked, and it does not have the same remedy.*
- **MF-3** argued "your architect is told to cut rules that never fire but a rule firing leaves no trace." That instruction exists in **MET's** `architect.md:102`, not in `zesty-eng-team`, whose equivalent line covers retiring an unused *role*.

The mechanism of the error: **reading a mechanism in one child repo and asserting its precondition in the other without checking.** The cross-system *pattern* was right both times — zero applied rules retired anywhere, verified. The *diagnosis* was wrong, and the diagnosis is where the proposal lives.

**Why:** `meta/architect.md` already says read the repo, do not trust the record — and this layer applied that to the incoming brief and then failed to apply it to its own findings. A finding assembled by comparing two repos inherits the shape of whichever one you read first.

**How to apply:** before a finding goes into a carry-packet, grep the *target* repo for the instruction, gate, or file the finding claims exists or is missing there. Cite the line. If the precondition is absent, the finding is about the other system and the packet says so.

**Sharpened after the 2026-08-14 advisory dispatch (2 of 8 survived, vs 5 of 10 for the measured 001a packets): grepping is not enough — run the artifact.** That advisory accused `retro-metric.py` of conflating absent-with-zero without executing it; the script prints "absent is not zero" by design. It also claimed a test-surface premise a `gh pr view --json files` loop disproved at both teams. The rule the children forced: **a finding is worth what its disproving command returned; a packet item that never ran one is a well-written guess.** Three known forms of the failure now: (1) asserting a precondition from the wrong repo, (2) reading a file instead of running it, (3) inheriting a fact that is stale *in the repo that recorded it* (the Jira Opus 5 field was fixed after MET logged it broken — read the live `allowedValues`, not the log). Related: review 000's falsifier asks "could a local Architect have made this?" — it never asks "could a local Architect have *corrected* it?", and that is a defect in the falsifier, recorded in `meta/architect-log.md`.

Also from that review: **measure a "read path" as what a session reads before it can start work**, enumerated against the boot ritual — not by directory. Proposing a ceiling over `.claude/**` at `zesty-eng-team` would have capped ~777 lines while the real read path is ~1,474 and the growth was in `docs/team-log.md` (93→547) and `knowledge/`. A ceiling that binds the wrong set licenses cutting the wrong thing.

Portfolio rules: [[meta-architecture-portfolio]]. The structural blind spot behind all of this: [[meta-layer-sees-only-the-improvement-loop]].
