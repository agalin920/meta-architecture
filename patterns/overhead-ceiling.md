# Overhead ceiling

**Status:** `proven` — one strong implementation, one qualitative
**Invented in:** personal-university
**Partial in:** brand-system (qualitative, no number)
**Missing from:** zesty-eng-team

## The pattern

A **stated numeric ceiling** on how much of the system's time may be spent on
the system rather than the work — plus a standing rule that prunes:

> **If a schema field is never read by a decision, propose deleting it.**

## Why it works

Every logging system accretes. Each field is individually defensible at the
moment it is added, and nothing ever removes one. Without a ceiling the ritual
grows until it competes with the work, and the human quietly stops.

The pruning rule is the operative half. A ceiling with no mechanism is a wish;
"never read by a decision" is a test an Architect can actually run against the
logs.

## Evidence

- `personal-university/charter.md` and `agents/architect.md` — admin capped at
  ~10% of session time; *"If a schema field is never read by a decision, propose
  deleting it. If admin exceeds roughly 10% of session time, cut fields."* The
  README hands the student the trigger directly: *"If you find yourself doing
  more admin than those three fields, tell the Architect to cut fields."*
- **It fired.** The 2026-08-09 cut of the student's prediction was made on
  exactly this basis — the friction was real, the signal was already collected
  more cheaply by `friction_type`, and the field had not earned its cost. The
  ceiling is the reason that was a principled decision rather than a preference.
- `brand-system/agents/architect.md` — *"Time spent in `meta/` should be a
  rounding error next to time spent shipping."* Real but unquantified, and
  therefore arguable every time.
- **zesty-eng-team has none.** Its ticket worklogs, team log, decision log and
  knowledge files are all load-bearing today, but nothing bounds their growth
  and nothing licenses cutting a field.

## Adoption notes

Two parts, and the second matters more:

1. A number. Any defensible number; its job is to make the question askable.
2. The pruning test — *is this field ever read by a decision?* — assigned to the
   Architect on its cadence.

## How it fails

- **A ceiling with no mechanism.** Nobody measures percentage of session time
  directly; what actually enforces it is the pruning rule and the human's
  license to complain.
- **Cutting rigour instead of admin.** The real risk. personal-university guards
  it with the anti-rigor tripwire, and its architect log entry for the 2026-08-09
  cut explicitly flags the second-order check: *one cut with this reasoning is
  discipline; a run of them is comfort drift.* Any system adopting a ceiling
  needs that counterweight.
