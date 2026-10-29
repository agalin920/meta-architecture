---
name: meta-architecture-portfolio
description: The ten agent-system repos and where they are checked out; meta-architecture is the layer above them and its rules constrain what may be edited.
metadata: 
  node_type: memory
  type: project
  originSessionId: 597868c9-aa47-4718-b7fd-31ff5e4bb24a
  modified: 2026-08-14T05:34:40.532Z
---

`~/dev/meta-architecture` is a **layer above** ten agent-run systems, not a peer. All eleven repos are checked out under `~/dev/`:

```
~/dev/personal-university   brand-system   media-log   meta-architecture
~/dev/zestyio/zesty-eng-team
~/dev/mpulsemobile/mpulse-engage-team   mpulse-dpi-team
~/dev/zestyio/zesty-webengine-team      # added 2026-08-19 — see [[zesty-webengine-team]]
~/dev/galind/galind-team                # added 2026-08-22 — see [[galind-team]]
~/dev/the-debrief                       # added 2026-08-24 — see [[the-debrief]]
~/dev/resale-desk                       # added 2026-08-29 — see [[resale-desk]]
```

**`galind-team` is the exception to the checkout layout and to the ownership
line below:** it sits in its own `~/dev/galind/` directory alongside the
`galind-*` product repos it will build, and **it has no GitHub remote at all** —
`gh repo create` is denied at its own permission layer, so creating one is
Andres's call.

**Both clocks turned on 2026-08-18/19 and the generative one turned again on
08-22.** `honest-metric` promoted to `proven` (first promotion ever);
`zesty-webengine-team` (first birth) and `galind-team` (second) both grown from
the spine. **None of it tests any claim** — the promoted pattern was already
running at both engineering teams, and both new systems have delivered nothing.
**Do not repeat any of it as a result.**

**Four births in eleven days, while review 001 stayed undischarged, is now itself
an agenda item for that review** — not a closing paragraph, which is what the
second, third and fourth birth entries each made it. The generative clock is exempt from the 1% overhead
ceiling by design, and that exemption was written when the birth count was zero.
**The third birth (2026-08-24, [[the-debrief]]) was run by this layer itself**,
having read both prior births — so it is a set of carries and proves nothing
about claim I. Do not count its ratio detector as a third adopter.

**The promotion gate gained a third case, `carried`** (2026-08-18): a pattern
this layer *dispatched* into a child is not that child arriving at it. Under the
old wording a carry read as independent, which would have let the layer promote
its own proposals into the spine. Copies, carries, and independent invention are
now three different things.

**`the-debrief` and `resale-desk` also have no GitHub remote**, same as
`galind-team`. `resale-desk` is the one with a reason beyond the permission layer:
its event log holds what Andres paid for things and what he earns reselling them.

**The fourth birth (2026-08-29, [[resale-desk]]) was also run by this layer**, so
like the third it is a set of carries and tests nothing. **It declined to build a
fourth ratio detector on purpose** (its `D-006`) — which keeps the promotion-gate
candidate honest at two, and simultaneously raises a new question: a child that
omits a mechanism to protect an upstream statistic has had its architecture set
from above. Logged as a question about the layer, not a credit to it.

All are private on GitHub under `agalin920` except **`personal-university` and `meta-architecture`, which are both public.** Andres decided this deliberately on 2026-08-10 and the exposure was named and accepted — `meta-architecture` lists five private systems by name and domain, and `systems.md` goes further. **This is settled; do not re-open it as a check.** (Superseded the earlier note that it was an unrecorded open item.)

**Its hard rules, which apply to any work in this repo:**

- **Never edit a child repo from the meta layer.** Not a typo, not an obviously correct one-word fix. A meta layer that routes around each system's human gate destroys the property it exists to protect.
- **Findings reach children as carry-packets**, written to `proposals/<date>-<system>.md` **in this repo** — see `meta/dispatch.md`. A dispatch hands the packet to a session running *inside* the child, under that repo's charter and Architect, and **ends at a presentation to Andres — never at a commit.** Run dispatches with `Write`/`Edit`/`git commit` denied at the tool layer, not merely asked against in the prompt. **`charter.md` still does not permit dispatch** — it bans editing and is silent on this, the amendment is drafted at the bottom of `meta/dispatch.md`, and it is Andres's file alone to edit.
- **`charter.md` is his alone. `spine.md` changes only on evidence a review earned.** The catalog is a record and may be edited at review; the spine is inheritance and the bar is higher.
- **Reviews are quarterly**, never more often than the fastest child Architect, and adding systems is *not* a reason to review early. Review 001a (2026-08-13) fired on a human flag against a data condition, not on interest.
- **Registration is bookkeeping; reconciliation is the review.** Don't blur them.

**The adoption matrix in `patterns/` is an evidence base, not a scoreboard.** `mpulse-engage-team` and `mpulse-dpi-team` were copied from `zesty-eng-team`, are marked `†`, and normally must never be counted as additional evidence for a pattern's status. **One narrow exception, ruled at review 001a:** a copy provides independent evidence for a pattern it *demonstrably did not inherit* — but the test is documentary (the catalog must already record the gap, or the copy's log must record deriving it from its own failure), available once per pattern per copy, and **never claimable retroactively.**

**The prediction that copies only ever lose things is wrong as stated.** `mpulse-engage-team` invented `verify_docs.py`, `gates.py`, a machine-asserted read-path cap, and the carry-packet convention — it now holds patterns its parent lacks. A copy inherits an architecture and then meets its own domain. Read each cell rather than applying the `†` discount uniformly.

The two mPulse teams are described in [[mpulse-two-teams]]. How to run this role without repeating its known mistakes: [[verify-preconditions-in-the-target-repo]], [[meta-layer-sees-only-the-improvement-loop]].
