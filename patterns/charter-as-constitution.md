# Charter as constitution

**Status:** `proven` — all four systems, independently
**Invented in:** convergent. No single origin.

## The pattern

One file states what the system is for and what it owes the human. **No agent
may edit it, including the Architect.** Agents may propose changes to it; only
the human applies them.

Everything else in the system is derived and negotiable. The charter is not.

## Why it works

A self-modifying system needs one thing it cannot modify, or its improvement
loop has no fixed point. Without it, an Architect optimizing the system will
eventually optimize the definition of success — not maliciously, just because a
charter that is editable is one more variable in the search space.

It also gives every downstream agent an authority to appeal to. brand-system's
Writer refuses a brief by citing the charter's receipts rule, not by having an
opinion.

## Evidence

- `personal-university/charter.md` — "yours alone to edit," enforced in
  `agents/architect.md`: *"`charter.md` you may propose edits to but never
  edit."*
- `brand-system/charter.md` — same rule, same wording in `agents/architect.md`.
- `zesty-eng-team/docs/operating-rules.md` — *"The Director owns this document;
  the architect may propose changes at a retro but never applies them
  unilaterally."* Split across `CLAUDE.md` + `operating-rules.md` rather than
  one file, which is a weaker version — there is no single place to read the
  contract.
- `media-log/CLAUDE.md` — the degenerate case, and the proof the pattern
  reproduces at any scale: *"Do NOT rewrite the Rules... describe the proposed
  change to the user and apply it only if they confirm."*

## How it fails

- **Splitting it.** zesty-eng-team's contract lives in two files plus a settings
  allowlist. Nothing is wrong, but "what am I actually committed to" has no
  single answer.
- **Drift by accretion.** If the operating loop grows rules the charter never
  authorised, the charter stops being the contract and becomes a preamble.
- **A charter that only says nice things.** personal-university's works because
  it contains an *anti*-rule — the anti-rigor tripwire, distinguishing "boring
  because beneath me" from "uncomfortable because hard." A charter with no
  clause that can rule against the human's momentary preference is decoration.
