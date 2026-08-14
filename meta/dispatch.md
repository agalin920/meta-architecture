# Dispatch

**How findings from this layer reach a child system without this layer editing
one.**

`charter.md` forbids editing a child repo, and the reason is stated there: every
system below depends on a single human gate for being reviewable and revertible,
and a meta-layer reaching past that gate destroys the property it exists to
protect.

**Dispatching is not editing.** This procedure hands a carry-packet to a session
running *inside* the child repo, under that repo's own charter, its own Architect,
and its own human gate. The Meta-Architect writes nothing there and nothing lands
without the child's judging step and the human's approval.

**It exists because hand-carrying markdown between repos is a step the human pays
every cycle, and `patterns/README.md` test 3 is exactly that question.** The
answer here is that the cost is real and the gate is preserved, so automate the
carrying and not the applying.

---

## What may be dispatched

**Only findings already recorded in `meta/architect-log.md`.** A dispatch is the
delivery of a proposal that has been through a review; it is not a way to have an
idea and put it in a repo. If it is not in the log with evidence, it does not go.

## What a carry-packet contains

One file per child, written to `proposals/<date>-<system>.md` **in this repo**.

```markdown
# Carry-packet — <system>, from meta review <nnn>

## Standing
Proposals from the meta layer. **They have no authority here.** This system's
`/retro` judging step applies to them exactly as it applies to its own
architect's proposals — including rejection, which is information.

## Findings
### MF-n — <one line>
**Evidence:** <file, commit, or log line, in this repo or another>
**Proposed:** <the smallest change that addresses it>
**Why it is being carried:** <what this layer could see that the local architect could not>
**Known weakness:** <n=1, untested, cost not yet measured — state it>

## What this layer could not judge
<Anything requiring domain knowledge the meta layer does not have.>
```

**Every finding carries its weakness.** A packet that arrives looking settled
invites rubber-stamping, which is the failure the judging step exists to prevent.

## The dispatch

```bash
cd ~/dev/<org>/<system>
claude "Read ../../meta-architecture/proposals/<date>-<system>.md.
        These are proposals from the meta layer with no authority here.
        Run /retro step 3 against them — judge each one on this repo's own
        evidence tests, reject what fails, and present what survives to me
        with your reasoning. Apply nothing yet."
```

**`Apply nothing yet` is load-bearing.** The dispatch ends at the presentation.
The human approves, and only then does the child apply and commit with its
`retro:` prefix. A dispatch that ran straight through to commits would have
converted the human gate into after-the-fact review of a pile of diffs, which is
the same loss as editing the repo directly, arrived at more slowly.

## Rules

1. **Never edit a child repo.** Unchanged. Dispatching does not relax it, and the
   Meta-Architect still never opens a file there with intent to write.
2. **One packet per system per review.** If a review produces nothing for a
   system, it gets no packet. An empty packet is churn.
3. **The child may reject anything.** Record the rejection and its reason in
   `meta/architect-log.md` at the next review. **A rejected meta proposal is the
   most useful signal this layer produces** — it means the local Architect had
   context this layer did not, and that is a finding about the layer.
4. **Dispatch does not follow up.** The Meta-Architect does not check whether the
   child complied, and does not re-dispatch a rejected finding. It reads the
   outcome at the next review like any other evidence.
5. **The order is not arbitrary.** Where a finding was invented in one child and
   is being carried to another, dispatch to the *inventor* first if the finding
   also proposes a change there. A pattern being carried outward while its origin
   is still being revised produces two divergent versions and no lineage.

## What this does not solve

**The human still decides.** Every packet ends at a presentation, so the number
of decisions per cycle is unchanged — the saving is in carrying, not in judging.
If the decision load is the actual constraint, this procedure does not touch it
and something else should.

---

# Charter amendment, for the human

**`charter.md` is the human's alone to edit.** The Meta-Architect may propose this
and may not apply it. Suggested wording, to be added under § What it must never
do, after the *never edit a child repo* bullet:

> **Dispatching is not editing.** This layer may hand a carry-packet to a session
> running inside a child repo, under that repo's charter, its Architect, and its
> human gate. It writes nothing there, and a dispatch ends at a presentation to
> the human — never at a commit. See `meta/dispatch.md`. If a dispatch ever
> results in a change the human did not approve, the mechanism has failed and
> goes, not the rule it was meant to respect.

**The amendment is worth making explicitly rather than reading dispatch as
already permitted.** The current wording bans editing and is silent on dispatch,
and silence is how a boundary erodes without anyone deciding to move it.
