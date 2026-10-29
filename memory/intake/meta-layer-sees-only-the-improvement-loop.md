---
name: meta-layer-sees-only-the-improvement-loop
description: "The Meta-Architect reads only children's logs and architecture, so every proposal it makes is about the improvement loop — never the work — whatever the system's actual failure rate is doing. Found by zesty-eng-team's Architect, not by this layer."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2daf9026-c21e-4028-91a6-1f1fb6627fde
  modified: 2026-08-14T05:35:08.622Z
---

Recorded as MF-10 at review 001a, and it came from `zesty-eng-team`'s Architect rejecting a carry-packet, not from this layer:

> *"All four proposals target the retro loop; none touches the ticket pipeline... a packet that can only see the meta-loop will only ever propose against the meta-loop, and this team's demonstrated failure rate is downstream of it."*

Its numbers made it concrete: 0.83 auto-reviewer findings/PR and 2.00 Director findings/ticket at retro #3, **both non-zero, both on delivery** — and all four proposals it received were about the retro.

**Why:** the bound is written into `meta/architect.md` — *"You read the children's logs and architecture, not their content."* That instruction is correct; it is what stops this layer forming opinions about a blog post or a curriculum topic. **Nobody wrote down its consequence.** A layer restricted to logs and architecture can only see the improvement loop, so every proposal it produces will be about the improvement loop.

It compounds two other findings from the same review: rules only ever get added and structure only ever gets refused (MF-6), and the improvement loop consumes the capacity it serves (MF-8). **Three ratchets pointing the same way, and this one is the layer's own.**

**How to apply:** when a review's proposals are all aimed at `/retro`, architect prompts, or logging, say so in the entry and name what was not examined. Do not "fix" it by reading child content — that is the thing the charter forbids for good reason. It is an open spine question for review 001, deliberately unresolved, and stating the limit is the honest move rather than manufacturing a delivery-side proposal to balance the list.

**The related humility check:** at 001a, five of eight findings were cross-system and three of those were child *inventions* this layer merely carried. **Carrying is a service, not an insight** — do not report a carried invention as a cross-system finding without saying which it is.

Portfolio rules: [[meta-architecture-portfolio]]. The other lesson from that review: [[verify-preconditions-in-the-target-repo]].
