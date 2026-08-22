# Carry-packet — brand-system, from the birth of `galind-team`, 2026-08-22

## Standing

**This packet is unusual and the difference is load-bearing.**

Every prior packet carried a *proposal* from this layer, which had no authority
and could be rejected on the receiver's evidence. **BF-1 below is not a proposal.
It is a ruling by Andres**, made 2026-08-22, and he is this system's human gate
as well as the portfolio's.

**What is his and settled:** `galind.io` goes to the Galind product; the personal
brand moves.

**What is this system's and is not settled:** what the brand is called instead,
what the new host is, when the move happens, and how the 16 files are changed.
**This layer has no standing on any of that** — `charter.md` § Never own a
system's domain — and this packet does not propose an answer to it. Where it
looks like it is proposing one, that is a defect in the packet and the Architect
should say so.

**BF-2 is an ordinary finding** and has no authority here at all.

---

## BF-1 — `galind.io` is ruled to the product; this system moves

**Class:** ruling (human), carried

**Evidence:** a new system, `~/dev/galind/galind-team`, was founded 2026-08-22 to
build **Galind** — an agent-native backend suite. Its founding brief names
`galind.io` as the product's domain and records it as already owned. Andres ruled
the collision in favour of the product, and the ruling is recorded in that
system's decision log as `D-008` and as `O-1` in its charter.

**Check run in the target repo, 2026-08-22:**

```
git grep -l "galind\.io"        → 16 tracked files
git grep -c "galind\.io" | sort → agents/distributor.md 4 · README.md 3 ·
    site/src/layouts/Base.astro 2 · site/README.md 2 · progress/traction.md 2 ·
    pipeline.md 2 · CYCLE-STATE.md 2 · and 9 files at 1
```

**Three of them use the string as this system's own name, not as a host:**

| File | Line | Content |
|---|---|---|
| `README.md` | 1 | `# Brand System — galind.io` |
| `site/src/pages/index.astro` | 14 | `<h1>galind.io</h1>` |
| `site/src/layouts/Base.astro` | 10 | `const siteName = 'galind.io';` |

**So this is a rename of the brand, not a DNS change**, and the packet says so
rather than presenting it as mechanical. That distinction is the reason the
*how* is explicitly left to this system.

**The timing fact, which is the actual reason this is being carried now rather
than held for review 001:**

```
dig +short galind.io A   → (empty)
dig +short galind.io NS  → dns1.registrar-servers.com. dns2.registrar-servers.com.
```

**Registered, not deployed.** Nothing is serving, nothing is indexed, and there
are no inbound links to break. `pipeline.md:40`
(`url: https://galind.io/writing/why-i-stopped`) and `progress/traction.md:40`
(`platform: galind.io`) are **schema examples in optional-field blocks, not
published items** — checked, and worth stating because a URL in a pipeline file
reads like a live post.

**The cost of this move is at its permanent minimum today and rises the day
`site/` deploys.** `CYCLE-STATE.md:134` records the publish path as waiting on
exactly that deploy, so the window is open and is not open indefinitely.

**Proposed — and only the shape, not the answer:** that this system's Architect
treat the move as a cycle's work rather than a chore, and that it produce the
name and the host as a decision through its own gate, in its own voice. The 16
files are the small half.

**Why it is being carried:** neither system can see this. `galind-team` was
founded today and does not know what this repo contains; this repo has no way to
know a product now claims its domain. **The collision is only visible from the
layer that holds both**, which is the one case `meta/thesis.md` claim III says
justifies a layer at all.

**Known weakness, stated plainly:** this layer has never carried a human ruling
before, and the mechanism was built for proposals that could be rejected. **The
failure mode is that "the ruling is settled" bleeds outward into the parts that
are not** — the name, the host, the timing, the file-by-file approach. If this
packet is read as instructing any of those, it has failed and the Architect
should reject the overreach while honouring the ruling. There is no precedent for
how to write this and it should be graded as a first attempt.

---

## BF-2 — the `galind` tarball's `.env` is still an unresolved liability

**Class:** finding

**Evidence:** `inventory.md:125` lists `galind` as a corpus repo with
`⧗ check for secrets first — tarball contains a .env`, and `HANDOFF.md:99` repeats
it as the exception blocking the open-it-up pass. It has been in that state since
2026-08-09 and is recorded as a *condition on publishing*, not as a *secret that
may be live*.

**Check run in the target repo, 2026-08-22:**

```
git grep -n "\.env" -- inventory.md HANDOFF.md
  inventory.md:125  ⧗ check for secrets first — tarball contains a .env
  HANDOFF.md:99     (`galind` is the exception — its tarball contains a .env ...)
```

Both framings are about **whether the repo can be opened**. Neither is about
whether the credentials in that file are still valid somewhere.

**Proposed:** separate the two questions in whichever file the Architect thinks
owns it. *"Do not publish until checked"* and *"these credentials may still work"*
have different urgencies and only the first is currently written down. The second
needs no publishing decision to matter, and it does not depend on the tarball ever
being opened.

**Why it is being carried:** it surfaced because `galind-team` was founded from
that same lineage, and its charter forbids agent-authored credentials with this
tarball cited by name as the precedent (`docs/charter.md` § The human gate, item
7). This layer was reading both repos at once. **No review would have found it** —
it is not a pattern, a cadence, or a divergence, and it is exactly the kind of
thing that stays unresolved because it is filed under a decision nobody has taken.

**Known weakness:** this layer **has not opened the tarball and did not look for
it** — `find ~ -maxdepth 5 -iname "galind*.tar*"` returned nothing, so it is not
where this layer could see, and its contents are unverified. The finding is about
**how the note is written**, not about what the file contains, and it should not
be read as a claim that live credentials are exposed. It may already be resolved
in a way neither file records, in which case the fix is to record it.

---

## Precondition, checked before dispatching — read this first

**`brand-system` has uncommitted work in flight and it is not this layer's.**

> **Check, executed 2026-08-22:** `git -C ../brand-system status --porcelain` →
> **8 modified files** — `CYCLE-STATE.md`, `ledger.md`, `pipeline.md`,
> `positioning.md`, `progress/critic-log.md`, `voice/voice-feedback.md`, and the
> draft and `.mdx` for item 0017. **All eight were last written 2026-08-16**, six
> days before this packet, against a last commit of `ff11586` on the same day.

**Nothing in that repo was touched by the session that wrote this packet** — it
was opened read-only, with `git grep` and `dig`, and its working tree is exactly
as its own last session left it.

**Do not dispatch into this state without resolving it first.** `CYCLE-STATE.md`
is among the modified files, which means the receiving session's own handoff
record is mid-write; a packet arriving on top of that would be judged against a
state neither file describes. **Ask Andres whether the 08-16 cycle is finished
before the packet goes in**, and if it is not, the packet waits — BF-1's timing
argument is measured in the weeks before `site/` deploys, not in days.

**This check exists because the layer has been wrong this way before**: a
cross-system finding can be correct in the abstract and false about the repo it
was aimed at. Verify in the target, not from here.

## What was deliberately not carried

**Nothing about `site/`, the voice, the pipeline, or the cadence.** This layer
opened `brand-system` for one reason — a domain collision it alone could see — and
read only what that required. `brand-system` has not had a proper review since
2026-08-13 and **this packet is not one and must not be counted as one.** Its
README is still recorded as stale (open item 2 in `HANDOFF.md`) and **this layer
did not re-verify that**, deliberately, because doing so from here would be the
substitute-for-review-001 failure the handoff warns about in writing.
