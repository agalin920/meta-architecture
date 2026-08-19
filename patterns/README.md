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

**Independent** means grown separately, not copied **and not carried**. A system
derived from another inherits its patterns as a package and provides no evidence
that anyone would have arrived at them again. Two adopters where one is a copy of
the other is **one** piece of evidence.

**Nor does a pattern this layer dispatched into a system count as that system
arriving at it.** That third route was unnamed until 2026-08-18 and, unnamed, it
read as independent — which would let this layer promote its own proposals into
the spine by carrying them. See § The third case: `carried`.

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
| [Overhead ceiling](overhead-ceiling.md) | `proven` | ✅ | ❌ | ⚠️ | n/a | ✅ | ✅ | ❌ |
| [Knowledge layer vs event log](knowledge-vs-log.md) | `provisional` | ⚠️ | ✅ | ❌ | n/a | n/a | ✅ | ✅ |
| [Honest metric](honest-metric.md) | `proven` | ❌ | ✅ | ❌ | n/a | ⚠️ | ✅ | ⚠️ |
| [Cadence defence](cadence-defence.md) | `provisional` | ⚠️ | ❌ | ✅ | n/a | n/a | ❌ | ❌ |
| [Predict-then-check](predict-then-check.md) | `provisional` | ⚠️ | ❌ | ❌ | n/a | ❌ | ❌ | ❌ |
| [Single-source claims](single-source-claims.md) | `provisional` | ? | ✅ | ? | n/a | ⚠️ | ✅ | ❌ |

✅ adopted · ⚠️ partial · ❌ missing · n/a doesn't apply to this domain ·
**‡ present but has never fired** — see below · **? not checked** in the session
that last touched the row

**`?` was added 2026-08-18** and it is not decoration. A ❌ asserts a pattern is
absent, which is a claim about a repo, which under `meta/architect.md` § Output
requires a check. The 2026-08-18 scoped read covered ZET, MET and MDT and did
**not** open personal-university or brand-system. Marking those two ❌ on
single-source claims would have been an unchecked assertion wearing a verified
mark, which is the failure this whole column exists to prevent.

**MA gained ✅ on named failure modes on 2026-08-10**, when `charter.md` was
rewritten with three named failures and their tripwires. Previously ❌.

**Two cells changed at review 001a, 2026-08-13**, both MET, both verified against
the repo rather than the record:

- **Overhead ceiling ❌ → ✅‡.** A 1,300-line cap on the per-ticket read path
  (`.claude/agents/architect.md:105`), machine-asserted through
  `tools/verify_docs.py` — plus the pruning half the pattern says matters more,
  `tools/gates.py --dead`, wired into the same file. **The only overhead tripwire
  in either engineering team.**
- **Honest metric ⚠️ → ✅‡.** D-019 excludes the release PR from the denominator
  **by name**, and `docs/team-log.md:360` reports it as excluded. That is the
  `unmeasured` discipline, independently re-derived — see below.

**Both MET ‡ marks were cleared on 2026-08-18, on measurement.** The
distinction below is unchanged and still load-bearing; these two cells simply
stopped qualifying.

- **Overhead ceiling ✅‡ → ✅.** The read-path cap **bound for the first time**.
  MET retro 002 landed at **1,082 lines against a 1,100 cap** (from 1,098), and
  the cut that made room — a 37-line block moved out of `knowledge/platform.md`
  behind a routing row — is reported by that team as the one that *"paid for
  everything else."* The pruning half of the pattern, which the pattern file
  says matters more than the cap, is what fired. `tools/gates.py` also produced
  its first datapoint and it was a falsification of its own coverage claim: it
  reported gate lines *"across 8 ticket worklog(s)"* when **all 27 come from
  one**; the header now reads "1 of 8".
  > **Check, 2026-08-18:** `python3 tools/verify_docs.py` → `9/9 passed`,
  > including `ok   read-path-budget   .claude/agents/architect.md:107`.
- **Honest metric ✅‡ → ✅**, and promoted to `proven`. Evidence in
  [`honest-metric.md`](honest-metric.md) § Promoted 2026-08-18.

**‡ means present and never fired**, and it is a separate mark because the
distinction was being lost. **The matrix records presence. The promotion gate
requires effect.** A ✅‡ is evidence for the first column and none at all for the
second.

*The figures that earned the mark, as of review 001a (2026-08-13) and superseded
by the entry above: the read-path cap was 1,300 against a current 1,056, so it
had never bound anything, and `tools/gates.py` reported 12 of 12 declared gates
unrecorded. Both are now false — the cap is 1,100 against 1,082 and has bound,
and `gates.py` has 27 recorded lines. Kept here dated rather than deleted,
because the mark only means something if you can see what it looked like when it
applied.*

**† MET and MDT are derived columns and prove nothing *by default*.** Both were
adapted directly from zesty-eng-team on 2026-08-10. Their ✅ marks record that the
pattern is *present*, not that two more systems arrived at it independently. **Do
not promote a pattern on the strength of these two columns** unless the exception
below applies and its documentary test is met. A pattern at `provisional` with
adopters ZET, MET, and MDT normally has exactly one piece of evidence.

They are worth reading for two things now, where it used to be one.

**Where a copy dropped something.** Both mPulse teams inherited ZET's metric and
lost the named `unmeasured` category that made it honest. That is the copy losing
the part whose reason wasn't visible on the surface, and it is the kind of finding
only this layer is positioned to make.

**Where a copy invented something.** Added at review 001a, because the catalog
predicted only the first kind and MET did the opposite. On 2026-08-13 MET built
`verify_docs.py` and `gates.py` and **now holds two patterns its parent lacks.**
The prediction that copies only lose is wrong as stated: a copy inherits an
architecture and then meets its own domain, and MET's domain — ~30 repos, no
written architecture, READMEs that actively mislead — produced pressures ZET's
single-repo target never applies. **How much the `†` discount is worth depends on
which of these a given cell is**, and that now has to be read rather than assumed.

## The independence bar and copies that re-derive

Ruled at review 001a, 2026-08-13, because the case was outside what the bar was
written against and leaving it ambiguous would have let it be decided by whoever
read the matrix next.

**A copy provides independent evidence for a pattern it demonstrably did not
inherit.**

The bar exists to stop counting a pattern that arrived as part of a package. It
was never aimed at a copy re-deriving something its own inheritance *omitted*.
MET inherited ZET's blockers-per-PR metric **complete with the flaw** — the ⚠️
this catalog has recorded since 2026-08-10 — then diagnosed the fault from its own
failure and built a different remedy. **The inheritance explains the flaw; it does
not explain the diagnosis.**

**The test is documentary, not inferential**, and it has to be or this becomes a
hole in the bar:

> The catalog must **already record the copy lacking the pattern**, or the copy's
> own log must record deriving it from its own failure. Absent that record, the
> default holds: **copies are not evidence.** The exception is available once per
> pattern per copy, at the moment the gap is on the record, and **cannot be
> claimed retroactively** for a pattern that was simply never checked.

Here the record existed before anyone knew it would be needed, which is the only
reason the exception is safe to grant.

## The third case: `carried` — adoption through this layer's own dispatch

Added 2026-08-18. The bar above has two cases — **independent invention**, and
**copy-as-package** — and it turns out there is a third that neither covers: a
pattern that arrived at a system because **this layer dispatched it there.**

Under the wording as it stood, a carried adoption reads as independent. It was
not grown from a copied repo, so the `†` discount does not apply; it appeared
in a system that did not invent it, which is what a second adopter looks like.

**That is a hole, and it is now live rather than hypothetical.**
`executable-claims` is the instance. It was invented at mpulse-engage-team
(`tools/verify_docs.py`, recorded as a candidate at review 001a). zesty-eng-team
now has it — three `**Verify.**` blocks — and it has them because **this layer
dispatched MF-4 to that repo.** Two adopters, and the second one is this
layer's own proposal coming back to it as evidence.

> **Check, executed 2026-08-18 in `../zestyio/zesty-eng-team`:**
> `grep -rn "Verify\." docs/ .claude/ CLAUDE.md` → blocks at
> `docs/charter.md:44` and `docs/operating-rules.md:56`; provenance stated in
> that repo's own record at `docs/decision-log.md:531`, headed *"Retro #4, MF-4"*.

**If carried adoptions count as independent evidence, this layer can promote its
own proposals into the spine by dispatching them.** Propose, carry, count the
acceptance as a second adopter, promote, and the pattern becomes default
inheritance for every system built afterwards — with no system having arrived at
it twice. Every step of that is currently permitted by the gate.

**The third status, and the asymmetry that makes it not merely another
discount:**

| Route | Counts toward `proven`? | What it *is* evidence of |
|---|---|---|
| **Independent** — grown separately | **Yes** | Two systems met the same problem and both built this |
| **Copied** (`†`) — inherited as a package | **No** | Nothing. The pattern came with the repo |
| **Carried** — dispatched from this layer | **No** | **That the pattern transfers** — which a copy is *not* evidence of, and which is a real and separate thing worth recording |

A carried adoption is genuinely informative: it means a pattern survived being
judged by a child Architect on that child's own evidence, in a repo that did not
invent it. Given this layer's dispatch record — **eighteen items, eleven
rejections**, and AR-1 rejected at both teams on grounds neither shared — an
acceptance is not a rubber stamp. **It is just not the thing `proven` measures.**
`proven` asks whether anyone would have arrived here again. A carry answers a
different question, and the two were being conflated because there was no word
for the second one.

**Mark carried adoptions in the matrix with the pattern's own origin note**, and
say who carried it and when, the way `†` is marked. Where a carried adoption
later produces a *diagnosis the receiver made itself* — as MET did with
`honest-metric` — the documentary exception above applies on its own terms and
the adoption stops being merely carried.

**What this changes retroactively: nothing, checked.** `honest-metric`'s
promotion on 2026-08-18 rests on ZET (invention) and MET (independent
re-derivation, ruled at 001a on the documentary test). **Neither is a carry.**
The other `proven` statuses predate all of this and are still awaiting the
re-audit that is review 001's first job.

**What the ruling did not do: it did not promote anything.** `honest-metric`
stayed `provisional`, and the reason it stayed changed — from *one independent
adopter* to *two independent adopters, neither remedy measured.* **Two
independent diagnoses of the same fault, with two different remedies, is strong
evidence the fault is real and no evidence that either remedy works.** That is
what review 002 had to look for.

> **Discharged 2026-08-18, and the answer was yes.** Both remedies were
> exercised in the window 2026-08-15 → 08-18 and both changed an already-published
> number: ZET's script returned a silent false 0.00 that the discipline caught
> and corrected to 2.00 (FLOOR, n=2), inverting the reported trend from flat to
> rising; MET reported **both** cuts of its headline (1/4 in-window, 5/5
> including a straddling PR), refused to pick, and wrote its context cost as a
> floor with the reason. **`honest-metric` is `proven` as of 2026-08-18** —
> evidence and executed checks in [`honest-metric.md`](honest-metric.md)
> § Promoted 2026-08-18. This is the portfolio's **first promotion under the
> independence bar**, and `meta/thesis.md` § The engine's scoreboard is updated
> from zero accordingly.

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

## Candidate recorded 2026-08-14 — the human driver as primary feedback

**The human driver is the primary external feedback channel.** Stated by the
human, 2026-08-14, as the abstraction behind every system here: the agents
produce, the human corrects, and the corrections are the highest-grade signal
the system receives. The evidence is real — ZET's Director findings per ticket,
MDT's mandatory `## Manager findings` heading, MET's 129→30-line scope
correction — and the pattern is currently implicit in every system and stated
in none.

**Its failure mode, which is the load-bearing half:** a feedback channel that
is also the approver and the bottleneck **cannot measure its own miss rate.**
What the human catches is logged; what he misses is counted by nowhere. The
honest form of the pattern therefore requires instrumenting what escapes him:

- **Escape tracking** — defects surfacing later (bug tickets, incidents,
  reverts) traced to the originating PR. MET's preferred escape-rate metric is
  this instrument; it currently has no feed.
- **A calibration sample** — one team PR per quarter reviewed by a second
  human, findings diffed against the driver's. Predict-then-check aimed at the
  reviewer.

Status: `proposed`. Present implicitly everywhere, instrumented nowhere. It
enters the catalog proper when one system builds either instrument and it
produces a datapoint.

## Candidates recorded at review 001a, 2026-08-13

Five, from the two engineering teams. **None promoted. `spine.md` untouched.**
Ranked by evidence so you can stop reading where the evidence stops.

| Candidate | Origin | Adopters | Evidence it changed an outcome | Status |
|---|---|---|---|---|
| **An adversary on the improvement loop** | ZET `ac65e24` | 1 | **Yes** — corrected a metric wrong for three cycles; caught two false statements pre-commit | `provisional` |
| **Grade the previous cycle's proposals** | ZET `decision-log.md:487` | 1 + 1 **carried** | **Yes** — P8 falsified after four further instances, replaced by `1646f8b` | `provisional` |
| **Gate instrumentation** | MET `tools/gates.py` | 1 | **No** — 12/12 declared gates unrecorded | `proposed` |
| **Executable claims** | MET `tools/verify_docs.py` | 1 + 1 **carried** | Partial — 6 assertions pinned on facts that had drifted; no cycle has run against it | `proposed` |
| **Read-path budget** | MET `verify_docs.py` | 1 | **No** — 1,300 against a current 1,056; it has never bound | `proposed` |

**Updated 2026-08-18** against ZET retro #5 and MET retro 002. The table above is
the 001a state; the adopter counts now carry the `carried` distinction added that
day. What the two retros returned, candidate by candidate:

| Candidate | What changed | Status now |
|---|---|---|
| **An adversary on the improvement loop** | Retirement test run a **second** time and nowhere near met. ZET's pass 2 corrected the headline metric 1.50 → 2.00, found a counting defect cutting the opposite way, **caught pass 1 proposing to delete a blocker that is true**, and caught pass 1's P3 proposing a rule the team had already written and already ignored | `provisional` — **still one adopter.** MET has now rejected it twice on its own evidence (n=27 coverage check at 001a; AR-1 at 2026-08-15) |
| **Grade the previous cycle's proposals** | **Ran at MET** — grades committed at `0f92b45` *before* the architect was dispatched. Also ran at ZET, producing the strongest grade in either repo: MF-4's blocks were *"correctly built, pointed at the wrong claims"* | `provisional` — the second adopter is **carried** (MF-2b), so it is one independent adopter still |
| **Gate instrumentation** | **First datapoint, and it falsified its own coverage claim.** `gates.py` reported gate lines *"across 8 ticket worklog(s)"*; all 27 come from one. Header corrected to "1 of 8" | `proposed` → **`provisional`.** An instrument whose first output is a correction to itself has fired |
| **Executable claims** | MET 7/7 → **9/9**, and the new `team-preamble-copies-agree` assertion caught real drift no retro had noticed. ZET's three blocks all ran and all passed — **inert**, and the two claims that died in the window both had the shape and neither carried a block | `proposed` → **`provisional`.** Second adopter is **carried** (MF-4). The ZET grade is the more useful half: it is evidence about *aiming*, not about the mechanism |
| **Read-path budget** | **Bound for the first time.** Cap 1,300 → 1,100 (carried as MF-1b); read path 1,098 → 1,082; the cut that made room is the one MET says *"paid for everything else"*; and D-021 records the budget **reversing a cut** two prior passes had wanted | `proposed` → **`provisional`**, and the strongest of the three. It is the only one that changed a decision rather than a document |

**None promoted, and `spine.md` is untouched.** Three moved `proposed` →
`provisional` on first datapoints. Every one of them is single-adopter once the
`carried` column is applied honestly, which is the whole reason that column was
added the same day.

**The one graduation is `single-source-claims`** — recorded 2026-08-18 as a full
catalog entry rather than a candidate, because unlike every row above it arrived
with **two independent adopters and neither was carried.** It is still
`provisional`, deliberately, at a few hours old. See
[`single-source-claims.md`](single-source-claims.md).

**Two have real evidence and three do not**, and all five are one adopter.
Recording them with their origin and cost is the whole job here. **Promoting any
of them on a five-day, two-system window would be premature evolution in the
exact form `charter.md` names it** — *a fresh idea from a live project is the most
persuasive thing that will ever cross this layer's desk.*

**An adversary on the improvement loop is the one to watch**, and not because it
is the best-evidenced. It is `independent-adversary` — already `proven`, already
in `spine.md` — applied one level up. The spine says *wherever the system produces
something that can be wrong*; **every system in the portfolio read that as the
work pipeline, and the retro produces self-modifications, which is the
highest-blast-radius output any of these systems has.** It was exempt everywhere,
including in this repo. That is a question about the spine's wording rather than a
new pattern, and it is review 001's to answer.

**Its weakness is on the record and is load-bearing:** applied at n=1, justified
structurally rather than empirically, with its own retirement test named for ZET's
retro #4. **Do not promote before that test returns**, and do not let the strength
of its first run substitute for the test.

**First transfer attempt, 2026-08-13: offered to mpulse-engage-team and
rejected — on evidence, and the rejection is data about the candidate.** MET ran
the direct test rather than accepting the argument: ZET's payoff was a broken
evidence command (`gh pr view --comments` cannot return inline review comments), so
MET checked whether it had the same defect. It does not — retro 001 reported 27
external findings, and `gh api …/pulls/N/comments` across its six non-release PRs
returns exactly **27**. *"We'd be buying a fix for a bug we don't have."*

**That distinction matters for how this candidate is written up.** Its
demonstrated value at ZET was **finding one specific broken query**, not *having a
second pass*. The structural argument — the retro is the one pipeline with no
adversary that did not write the thing — is separable from the instance, and only
the instance has evidence. **A second adopter that has no counting defect would be
adopting the argument, not the result.** MET took the one-line coverage question
from ZET's step 3 instead, at zero per-ticket cost.

> **Withdrawn 2026-08-18 as stated. The narrowing was this layer's and it was
> wrong.** ZET retro #5's pass 2 produced two catches, and **neither is a
> counting defect**: pass 1's mandatory § Cuts proposed deleting a standing
> blocker that is **true** — it had checked the half already fixed and asserted
> the half it had not checked — and pass 1's P3 proposed adding a rule
> `docs/operating-rules.md` § Automation **had carried verbatim since the bot
> landed**, and which had produced no action on either PR it applied to. A
> second pass that catches *"you are proposing a rule you already wrote and
> already ignored"* is not a broken-query detector. The structural argument has
> content the instance did not show, and this layer narrowed it to the instance
> on one cycle's evidence.
>
> **What does not change: the candidate stays `provisional` at one adopter.**
> The withdrawal makes the argument stronger, and an argument is what MET has
> twice declined — on its own evidence both times, which is the outcome this
> mechanism is supposed to produce. Do not read a withdrawn narrowing as a
> reason to press it a third time.

**Not a candidate: mandatory subtraction.** Zero adopters — it is a *gap*, not an
invention. Across 138 + 51 commits and four retros, **no system in the portfolio
has ever retired an applied rule** (+155/−47 and +209/−21 on instruction files;
every deletion verified as a replacement or a renumbering).

> **Superseded 2026-08-18. The gap closed, and it closed because this layer's
> own proposal landed.** MF-1 — the mandatory § Cuts section, carried to ZET in
> MET's shape — is live at `.claude/agents/architect.md:85` with the two-state
> clause at `:92` (*"'Nothing should be cut this cycle' is a valid return, and
> it must be stated rather than left blank"*). At retro #5 it **fired and
> produced three cuts**, one of which was factually wrong and was caught by
> pass 2 — which that team correctly reads as an argument for keeping both
> mechanisms, not for cutting either. Separately,
> `docs/definition-of-done.md:85` was **deleted rather than reworded**, a
> genuine retirement of a live rule on the grounds that its content already
> lived in `operating-rules.md` § Standing authorizations.
>
> **Checked 2026-08-18 in `../zestyio/zesty-eng-team`:**
> `grep -n "Cuts" .claude/agents/architect.md` → lines **85** and **92**.
> `git show a2a4f6e --stat` → `docs/definition-of-done.md | 1 -`.
>
> The original sentence stands as a description of the portfolio **through
> 2026-08-14**, and is worth keeping in that form: it is the observation that
> produced the fix.

**Corrected after both packets were judged, 2026-08-13.** This layer originally
recorded the cause as *the question going unasked*. **That is true of one system
and false of the other, and the difference is the whole remedy:**

- **mpulse-engage-team asks** — `.claude/agents/architect.md:124` mandates a
  § Cuts section, *"do not skip this section"*. It fired: retro 001 proposed a cut
  and **the judging step rejected it with a recorded reason.** It rejected this
  proposal on those grounds and was right. *Asked-and-answered is a different
  failure mode than unasked.*
- **zesty-eng-team does not ask** — no cut instruction anywhere in `/retro`;
  `architect.md:74` covers a role, `CLAUDE.md:88` a standing blocker. It
  **accepted** the § Cuts section, in MET's shape.

**The useful generalisation is the one the children produced, not the one this
layer carried: a recorded *no* is a different artifact from silence, and only the
first can be audited.** A mandated section that permits *nothing should be cut,
and here is why* is the pattern. **A quota is not** — zesty-eng-team's inert
proposals P4 and P7 are both unfired for reasons unrelated to whether they work,
so a rule forcing one removal per cycle would have cut something load-bearing.

Still not a catalog entry: one adopter, accepted and not yet run.

## Do not propose uniformity

Divergence where domains genuinely differ is correct, and `spine.md` names where
it is expected. zesty-eng-team uses context-isolated subagents; personal-university
and brand-system adopt roles in sequence within a single turn. That is a real
architectural fork with real tradeoffs, not drift, and both are right for their
domain.

A finding that amounts to *"these two should be more alike"* is a preference
unless it names the failure being prevented.
