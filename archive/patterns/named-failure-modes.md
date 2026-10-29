# Named failure modes with tripwires

**Status:** `proven`
**Invented in:** brand-system (the risk table), personal-university (§9 + the
anti-rigor tripwire)
**Partial in:** zesty-eng-team — risks are recorded per-incident in the decision
log rather than collected anywhere
**Missing from:** media-log

## The pattern

The system's likely failures are enumerated **up front**, each with an owner and
an **observable tripwire** — a specific thing you could check that would tell
you it is happening.

Not "we should watch for drift." A tripwire is: *referrers in `traction.md` are
overwhelmingly direct.*

## Why it works

The failures these systems are shaped around are **silent**. Voice drift, grade
inflation, comfort drift, curation capture — each looks fine at every individual
step and is only visible in aggregate. Naming them converts a vague worry into
something an Architect can check on a schedule.

The tripwire is the part that does the work. A named risk with no observable is
a mood; it will be nodded at every review and never resolved either way.

## Evidence

- `brand-system/README.md` — a seven-row table, risk to tripwire. The sharpest
  entry is self-referential: **voice convergence is tripped when the Architect's
  own voice check concludes "looks fine."** The check's comfort is the signal.
- `personal-university/charter.md` — the anti-rigor tripwire, distinguishing
  three reasons a session felt bad and routing each differently. This is why
  `friction_type` exists and it is the single most load-bearing field in that
  system.
- `personal-university/agents/architect.md` — *"a rising `trivial` rate with
  flat mastery is the signature of a system going soft."* A named failure with a
  computable signature.

## How it fails

- **Tripwires nobody checks.** Each must be assigned to a role and a cadence, or
  the table is decoration.
- **Unfalsifiable entries.** "Losing focus" is not a tripwire.
- **Never updated.** The risks a system was designed around are guesses until it
  runs. The Architect should be retiring the ones that never fired and adding
  the ones that actually bit — and none of these tables has been through that
  cycle yet.
