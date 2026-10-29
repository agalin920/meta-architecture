---
name: child-architects-push-back-hard
description: "The child Architects reject meta proposals on their own evidence and are usually right — at review 001a six of ten were rejected or materially amended. Write packets to be judged, not accepted, and treat a rejection as the layer's best output."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2daf9026-c21e-4028-91a6-1f1fb6627fde
  modified: 2026-08-14T05:35:23.558Z
---

First real test of the propose-never-apply loop, 2026-08-13: two carry-packets dispatched, ten proposals judged, **five accepted and five rejected — and the rejections were better than the accepts.**

Both Architects **checked this layer's premises against their own repos rather than deferring.** `mpulse-engage-team` ran `gh api` across six PRs to test whether it had `zesty-eng-team`'s counting defect before rejecting the fix for it — 27 external findings against 27 counted — and concluded *"we'd be buying a fix for a bug we don't have."* `zesty-eng-team` measured its actual read path and killed a ceiling proposal that would have capped the slowest-growing eighth of the problem.

**Why this matters beyond the individual verdicts:** `meta/thesis.md` claim IV says nobody scores the scorers, and an Architect grading its own record is the coupling an independent adversary exists to break. **The evidence so far runs the other way** — `zesty-eng-team`'s Architect graded its own prior cycle, falsified its own P8, and corrected two false statements it had itself committed. Claim IV is not withdrawn (one dispatch is not "review after review") but it is the thesis claim in most trouble, and the thesis itself says what follows if it holds: **cut the audit-the-Architects job to a spot check.**

**How to apply:**

- Write every packet finding with its **weakness stated** — n=1, untested, cost unmeasured. A packet that arrives looking settled invites rubber-stamping, which is the failure the child's judging step exists to prevent.
- **A rejection is the most useful signal this layer produces** (`meta/dispatch.md` rule 3) — it means the local Architect had context this layer did not, which is a finding *about the layer*. Record it and do not re-dispatch it.
- **Do not follow up** (rule 4). Read the outcome at the next review like any other evidence.
- **Dispatch to the inventor first** when a finding originates in one child and carries to another (rule 5).
- **Amend a packet mid-dispatch when an earlier rejection invalidates it.** At 001a the `zesty-eng-team` packet was corrected on `mpulse-engage-team`'s rejection before it was sent, and the corrected finding was accepted. Amending a packet *after* delivery falsifies the record of what was judged — add an outcome header instead and leave the body as delivered.

Portfolio rules and the dispatch procedure: [[meta-architecture-portfolio]]. Why the premises were wrong in the first place: [[verify-preconditions-in-the-target-repo]].
