---
name: galind-team
description: The portfolio's second spine-grown birth (2026-08-22) — builds Galind, an agent-native backend suite — plus the dead predecessor whose failure its whole design is aimed at.
metadata:
  type: project
---

`~/dev/galind/galind-team` — founded **2026-08-22**, the portfolio's **second
birth**, grown from `spine.md` three days after [[zesty-webengine-team]].

**Domain: build Galind** — an agent-native backend suite (email, storage, auth,
analytics, billing under one brand, one API key, one bill), delivered through an
MCP server. Launch module is **email**; storage is a trap for launch because
egress scales with use. The thesis is that *the MCP install is the entire
distribution battle*, because models reach for what they were trained on.

**The design constraint that explains everything in the repo: there was a
previous `galind`.** An agent-run company on the Agent SDK whose first mission
was to discover its own product. It never did, and is a backup tarball now, logged
at `brand-system/inventory.md:46,125,144,155`. Its README's own epitaph:
*"We built the machine before deciding what it makes — on purpose."* Its tarball
contains a `.env`, which is why that repo can't be opened without a secrets pass.

**So the product is deliberately NOT in the system repo.** `galind-team` is the
team; `~/dev/galind/galind-<module>` repos are subjects and **none exists yet**.
The separation is what makes `tools/ledger.py` possible — it counts system
commits against product commits, or days elapsed with no product repo at all.
Failure mode F1 has a real corpse behind it, not a prediction.

**Three rulings by Andres at founding**, all in its `docs/decision-log.md`:
separate repos (D-002), **the team proposes strategy and he decides** (D-003), and
**Galind takes `galind.io` while the personal brand moves** (D-008).

**The galind.io ruling is not executed.** `brand-system` owns that domain in 16
tracked files and uses the string as *its own name* in three of them, so it is a
rename, not a DNS change. Carry-packet:
`meta-architecture/proposals/2026-08-22-brand-system.md`. **It has a blocking
precondition** — that repo has 8 files uncommitted since 2026-08-16, including
`CYCLE-STATE.md`. Ask whether that cycle is done before dispatching.

**The finding worth more than the birth:** the two spine-grown systems made
**opposite calls on the same two mechanisms** four days apart without reading each
other — WET adopted the read-path cap and executable claims, `galind-team`
declined both with triggers. That is evidence the spine is *read*, not complied
with. Both also independently invented an improvement-versus-delivery ratio.
**Recorded as a candidate in `meta/architect-log.md`, deliberately not added to
`patterns/`** — review 001 decides.

**Nothing has been built and no command has ever run.** The next move is
`/decide Q1` (smallest useful Galind Email), not `/take-item`. Seven questions
open; Q7 (the test allowlist) was raised at founding because the charter forbids
sending mail to anything not on a list that does not exist.

Portfolio context: [[meta-architecture-portfolio]]. Why it was grown rather than
copied, and why the packet expects pushback: [[child-architects-push-back-hard]],
[[verify-preconditions-in-the-target-repo]].
