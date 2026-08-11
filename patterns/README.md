# Pattern Catalog

The evidence base. Every pattern in the portfolio: what it is, why it works,
**where it was invented**, who has adopted it, and how it fails.

**This is the record. [`spine.md`](../spine.md) is the inheritance.** They are
different documents doing different jobs: the catalog holds everything ever
tried, including what failed; the spine holds what a new system gets by default.
A pattern earns its way from one into the other through the gate below.

A pattern with no named source repo and no evidence is an opinion and does not
belong here.

## Status vocabulary and the promotion gate

Status is a **threshold on evidence, not a judgment of quality.** A well-argued
pattern with one adopter is `provisional` no matter how good it looks.

| Status | Bar | Inherited by default? |
|---|---|---|
| `proposed` | Argued for, not adopted anywhere | No |
| `provisional` | Adopted somewhere. Not enough evidence to generalise | No — pull deliberately, knowing the evidence is thin |
| `proven` | **Two or more independent adopters, plus evidence it changed an outcome** | Yes |
| `retired` | Tried and cut. **Kept, with why** — so it is not reinvented | No |

**Independent** means grown separately, not copied. A system derived from another
inherits its patterns as a package and provides no evidence that anyone would
have arrived at them again. Two adopters where one is a copy of the other is
**one** piece of evidence.

**Evidence it changed an outcome** means something observable in a log, a metric,
a commit, or a decision record — not that the pattern is present and the system
seems fine. Presence is not evidence.

**Promotion is not automatic on crossing the bar.** Clearing the threshold makes
a pattern eligible; whether it enters `spine.md` as default inheritance is a
separate and more conservative judgment, made at review only. See
`meta/architect.md` § Steward the spine. **A spine that churns is worse than a
spine that lags** — systems built a month apart stop sharing a lineage, and the
cross-system comparison this whole layer runs on stops meaning anything.

**Demotion is real.** A `proven` pattern whose evidence turns out to be a copy,
or that fails somewhere it should have worked, moves back down or to `retired`.
Say what that invalidates.

## Adoption matrix

PU = personal-university · ZET = zesty-eng-team · BS = brand-system ·
ML = media-log · **MA = meta-architecture (this repo)** ·
MET = mpulse-engage-team · MDT = mpulse-dpi-team

| Pattern | Status | PU | ZET | BS | ML | MA | MET† | MDT† |
|---|---|---|---|---|---|---|---|---|
| [Charter as constitution](charter-as-constitution.md) | `proven` | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| [Boot ritual](boot-ritual.md) | `proven` | ✅ | ✅ | ✅ | n/a | ✅ | ✅ | ✅ |
| [Append-only log + current state](append-only-log.md) | `proven` | ✅ | ✅ | ✅ | n/a | ✅ | ✅ | ✅ |
| [Handoff record](handoff-record.md) | `proven` | ✅ | ✅ | ✅ | n/a | ⚠️ | ✅ | ✅ |
| [Independent adversary](independent-adversary.md) | `proven` | ✅ | ✅ | ✅ | n/a | ❌ | ✅ | ✅ |
| [Human gate on the irreversible](human-gate.md) | `proven` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Architect on cadence](architect-on-cadence.md) | `proven` | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| [Named failure modes with tripwires](named-failure-modes.md) | `proven` | ✅ | ⚠️ | ✅ | ❌ | ✅ | ⚠️ | ⚠️ |
| [Falsifiable thesis](falsifiable-thesis.md) | `provisional` | ✅ | ❌ | ❌ | n/a | ✅ | ❌ | ❌ |
| [Untrusted input boundary](untrusted-input.md) | `proven` | n/a | ✅ | ✅ | n/a | n/a | ✅ | ✅ |
| [Overhead ceiling](overhead-ceiling.md) | `proven` | ✅ | ❌ | ⚠️ | n/a | ✅ | ❌ | ❌ |
| [Knowledge layer vs event log](knowledge-vs-log.md) | `provisional` | ⚠️ | ✅ | ❌ | n/a | n/a | ✅ | ✅ |
| [Honest metric](honest-metric.md) | `provisional` | ❌ | ✅ | ❌ | n/a | ⚠️ | ⚠️ | ⚠️ |
| [Cadence defence](cadence-defence.md) | `provisional` | ⚠️ | ❌ | ✅ | n/a | n/a | ❌ | ❌ |
| [Predict-then-check](predict-then-check.md) | `provisional` | ⚠️ | ❌ | ❌ | n/a | ❌ | ❌ | ❌ |

✅ adopted · ⚠️ partial · ❌ missing · n/a doesn't apply to this domain

**MA gained ✅ on named failure modes on 2026-08-10**, when `charter.md` was
rewritten with three named failures and their tripwires. Previously ❌.

**† MET and MDT are derived columns and prove nothing.** Both were adapted
directly from zesty-eng-team on 2026-08-10. Their ✅ marks record that the pattern
is *present*, not that two more systems arrived at it independently. **Never
promote a pattern on the strength of these two columns.** A pattern at
`provisional` with adopters ZET, MET, and MDT has exactly one piece of evidence.

They are still worth reading for one thing: **where a copy dropped something.**
Both inherited `⚠️` on the honest metric — they count external-reviewer blockers
but neither carries the named `unmeasured` category that made ZET's metric honest
in the first place. That is the copy losing the part whose reason wasn't visible
on the surface, and it is the kind of finding only this layer is positioned to
make.

**The founding four are weaker evidence than they look.** They were built by one
person over two days. That is one derivation repeated, not four independent ones
— see `meta/thesis.md` § The origin observation. The `proven` statuses in this
table were assigned before that correction and **have not been re-audited against
the independence bar.** Review 001's job.

**MA is in its own matrix on purpose.** A layer exempt from its own catalog is
exactly what it would flag in a child.

**The matrix goes stale.** The Meta-Architect verifies it against the repos every
review rather than trusting it — a stale catalog is worse than none, because it
reads as verified.

## Reading the gaps

A ❌ is not automatically a defect. Three tests before proposing adoption:

1. **Does this system have the failure mode the pattern prevents?** If not, the
   gap is correct.
2. **Is the signal already collected some cheaper way?** The one most often
   skipped. Predict-then-check was cut from personal-university on 2026-08-09
   precisely because `friction_type` already answered the question by observation
   instead of inference.
3. **What does it cost the human per use?** A pattern that adds a human step
   every cycle needs to clear a much higher bar than one that runs inside an
   agent turn.

## Candidate, not yet a pattern

**Knowledge accumulation as a gate rather than a habit.** mpulse-dpi-team makes
writing to `knowledge/dpi.md` gate 9 of its definition of done — a ticket does not
close until what it taught is recorded, because that product has no written
architecture and READMEs that actively mislead. Every other system treats its
knowledge layer as a habit, and habits lose to the task in front of you.

Not in the catalog: **one adopter, zero evidence, and an identified failure mode
its own decision log names** — a mandatory entry every ticket invites filler,
restating what the diff already shows so the box gets ticked, which is worse than
absence because it dilutes the file.

Review 001 decides. The question is not "did the file grow" but "did it grow with
things that were true and not otherwise recoverable". If it produced filler, this
becomes a `retired` entry with the reasoning, which is worth as much as a `proven`
one.

## Do not propose uniformity

Divergence where domains genuinely differ is correct, and `spine.md` names where
it is expected. zesty-eng-team uses context-isolated subagents; personal-university
and brand-system adopt roles in sequence within a single turn. That is a real
architectural fork with real tradeoffs, not drift, and both are right for their
domain.

A finding that amounts to *"these two should be more alike"* is a preference
unless it names the failure being prevented.
