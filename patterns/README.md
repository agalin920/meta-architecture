# Pattern Catalog

The shared spine, written down once. **Four systems converged on most of this
independently, in two days, without coordination** — that convergence is the
evidence these patterns are load-bearing rather than stylistic.

Each file records: what the pattern is, why it works, **where it was invented**,
who has adopted it, and how it fails. A pattern with no named source repo and no
evidence is an opinion and does not belong here.

## Status vocabulary

| Status | Means |
|---|---|
| `proven` | Adopted in more than one system, with evidence it works |
| `provisional` | Adopted somewhere, not yet enough evidence |
| `proposed` | Argued for, not yet adopted anywhere |
| `retired` | Tried and cut. **Kept, with why** — so it is not reinvented |

## Adoption matrix

PU = personal-university · ZET = zesty-eng-team · BS = brand-system ·
ML = media-log · **MA = meta-architecture (this repo)**

| Pattern | Status | PU | ZET | BS | ML | MA |
|---|---|---|---|---|---|---|
| [Charter as constitution](charter-as-constitution.md) | `proven` | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| [Boot ritual](boot-ritual.md) | `proven` | ✅ | ✅ | ✅ | n/a | ✅ |
| [Append-only log + current state](append-only-log.md) | `proven` | ✅ | ✅ | ✅ | n/a | ✅ |
| [Handoff record](handoff-record.md) | `proven` | ✅ | ✅ | ✅ | n/a | ⚠️ |
| [Independent adversary](independent-adversary.md) | `proven` | ✅ | ✅ | ✅ | n/a | ❌ |
| [Human gate on the irreversible](human-gate.md) | `proven` | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Architect on cadence](architect-on-cadence.md) | `proven` | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| [Named failure modes with tripwires](named-failure-modes.md) | `proven` | ✅ | ⚠️ | ✅ | ❌ | ❌ |
| [Falsifiable thesis](falsifiable-thesis.md) | `provisional` | ✅ | ❌ | ❌ | n/a | ✅ |
| [Untrusted input boundary](untrusted-input.md) | `proven` | n/a | ✅ | ✅ | n/a | n/a |
| [Overhead ceiling](overhead-ceiling.md) | `proven` | ✅ | ❌ | ⚠️ | n/a | ✅ |
| [Knowledge layer vs event log](knowledge-vs-log.md) | `provisional` | ⚠️ | ✅ | ❌ | n/a | n/a |
| [Honest metric](honest-metric.md) | `provisional` | ❌ | ✅ | ❌ | n/a | ⚠️ |
| [Cadence defence](cadence-defence.md) | `provisional` | ⚠️ | ❌ | ✅ | n/a | n/a |
| [Predict-then-check](predict-then-check.md) | `provisional` | ⚠️ | ❌ | ❌ | n/a | ❌ |

✅ adopted · ⚠️ partial · ❌ missing · n/a doesn't apply to this domain

**MA is in its own matrix on purpose.** A layer exempt from its own catalog is
exactly what it would flag in a child. Its three ❌ are probably correct
absences for something that runs quarterly and produces only findings — but they
are absences, and review 001 assesses them rather than skipping the row.

**The matrix goes stale.** The Meta-Architect verifies it against the repos
every review rather than trusting it — a stale catalog is worse than none,
because it reads as verified.

## Reading the gaps

A ❌ is not automatically a defect. Three tests before proposing adoption:

1. **Does this system have the failure mode the pattern prevents?** If not, the
   gap is correct.
2. **Is the signal already collected some cheaper way?** This is the one most
   often skipped. Predict-then-check was cut from personal-university on
   2026-08-09 precisely because `friction_type` already answered the question by
   observation instead of inference.
3. **What does it cost the human per use?** A pattern that adds a human step
   every cycle needs to clear a much higher bar than one that runs inside an
   agent turn.

## Do not propose uniformity

Divergence where domains genuinely differ is correct. zesty-eng-team uses
context-isolated subagents; personal-university and brand-system adopt roles in
sequence within a single turn. That is a real architectural fork with real
tradeoffs, not drift, and both are right for their domain.

A finding that amounts to *"these two should be more alike"* is a preference
unless it names the failure being prevented.
