# Meta-Architect Log

Findings, proposals, and whether they landed. Append-only; supersession is
stated in writing, never quietly edited.

**Proposals go to a child system's Architect, never around it.** This layer
never edits a child repo.

## Entry format

```markdown
## Meta review — <window>, <date>

### Budget
<Committed load vs real capacity. Which cadences were met. Where misses landed.>

### The Architects
<Per system: has it run, proposals made/approved/effective, has it ever
withdrawn a finding or proposed killing something.>

### Catalog
<Matrix verified against the repos. Gaps, new patterns, retired patterns.>

### Falsifier check
<All four from meta/thesis.md, each answered in writing.>

### Prior proposals — did they land?
<Every proposal from last review and what it actually did.>

### Proposals
1. <finding> — to: <which system's Architect> — evidence: <cite>

### Watching
```

---

## Review 000 — portfolio established, 2026-08-09

Not a review. The founding entry, recording what exists and what was done on the
day the layer was created, so review 001 has a baseline to measure against.

### State of the portfolio

**All four systems are two days old or less.** First commits: media-log and
zesty-eng-team 2026-08-08; brand-system and personal-university 2026-08-09.
Commit counts at registry time: ZET 62, PU 21, ML 18, BS 5.

**Do not read BS's low count as stalling.** It is one day old. The registry
entry says so explicitly because the reading is tempting and would be wrong.

Operational maturity is very uneven and that is the most important fact here:
zesty-eng-team has shipped real PRs against an external repo that pushes back,
and is the only system that has survived contact with anything outside itself.
Everything else is architecture that has not yet been tested by use.

### Changes applied today (by the human, before this layer existed)

Three catalog patterns moved between systems on 2026-08-09:

1. **brand-system gained the Critic** — `agents/critic.md`, an independent
   adversary, plus `progress/critic-log.md` to score it. Adopted from
   personal-university's Examiner and zesty-eng-team's reviewer. Its own
   Architect is now instructed to propose cutting it if `human_divergence` never
   resolves.
2. **brand-system gained the untrusted-input boundary** — copied from
   zesty-eng-team, with two domain-specific corollaries.
3. **personal-university cut the human half of predict-then-check** — see
   `patterns/predict-then-check.md`. The most instructive of the three, because
   it is a pattern being *removed* with its cost recorded rather than smoothed.

### Findings

**F1 — brand-system's README describes a state the repo has left.**
`README.md` says *"Session Zero has not been run"* and that `inventory.md`,
`voice/voice-guide.md` and `positioning.md` are *"marked STATUS: NOT YET RUN."*
The repo disagrees: `voice-guide.md` is `STATUS: PROVISIONAL — derived`,
`inventory.md` reads *"Session Zero — Part 1 in progress"*, `positioning.md`
reads *"Session Zero, Part 3 — recorded 2026-08-09"*, and there are 16 pipeline
items and 5 decision-log entries.

Not a typo — it is the drift that zesty-eng-team already wrote a rule against:
*"if `Current state` disagrees with what GitHub actually says, GitHub is right."*
brand-system has no reconciliation rule and no current-state file to reconcile.

**→ Proposal, to brand-system's Architect:** correct the README's start-here
section to describe the reduced Session Zero that actually ran, and add a
reconcile-against-reality step to the Orchestrator's Phase 1.

**F2 — brand-system has no handoff record.** See
`patterns/handoff-record.md`. A cycle interrupted between the Writer and the
gate leaves a draft on disk and no record of what was decided about it.
`pipeline.md` item states imply progress but nothing captures mid-cycle
position, and there is no current-state header anywhere in the repo. The other
two agentic systems both have this — ZET's ticket worklogs written at every
step, PU's `NEXT-SESSION.md`.

**→ Proposal, to brand-system's Architect:** adopt the pattern. ZET's version is
the reference: written *during*, not at close.

**F3 — PU's handoff is written at session close, not during.**
`NEXT-SESSION.md` is regenerated at the end of each session, so an interrupted
session loses its own state — the exact failure the pattern exists to prevent.
It is stronger than ZET's on a different axis (it carries *why*, not just
where), so this is a small amendment, not a rewrite.

**→ Proposal, to PU's Architect:** update `NEXT-SESSION.md` at phase boundaries
within the session protocol, not only at close.

**F4 — Nothing measures the Architects, and none has run yet.** Zero Architect
reviews have been completed across the portfolio. Every claim about whether this
propose-never-apply loop actually works is currently untested. Recorded as the
baseline: at review 001, the question is how many have run on cadence.

**F5 — `budget.md` cannot be filled by this layer and is the blocker for its
main claim.** Thesis claim II — that cadence collides globally — is the primary
justification for this repo and it is **untested and untestable** until the
human states real capacity. The Meta-Architect is forbidden from inferring it.
Ten minutes of human time gates the most important thing here.

### Falsifier check

Run honestly, because the first one indicts most of this entry.

**1. "Two consecutive reviews with no finding a local Architect couldn't have
made."** Going finding by finding:

- **F1 — a local Architect could have found this.** brand-system's Architect
  reads the repo and would catch the README contradiction at its first review.
- **F2 — a local Architect could have found this**, though it is less likely:
  nothing in brand-system's Architect prompt points at the absence of a handoff
  record, because absences are harder to see than drift. The *catalog* is what
  made it visible. Partial credit at best.
- **F3 — same.** Found by comparison, not by reading PU alone.
- **F4 and F5 are genuinely cross-system** and no local Architect could produce
  either.

**Honest verdict: three of five findings were within reach of a local
Architect.** This entry does not clear the bar on its own. It is entry 000 and
the bar applies to reviews, not to founding — but review 001 must do better, and
if it does not, the two-review clock starts there.

**2. "Cross-system pattern adoption never happens."** Not yet checkable. Three
adoptions happened today, before the catalog existed, driven by the human. The
test is whether the *catalog* drives the next one.

**3. "The budget is never binding."** Not yet checkable — see F5.

**4. "Findings are things a child Architect already had in its Watching
section."** Not checkable; no child Architect has run.

### Applied same day — F2 and F3

Appended 2026-08-09, after the entry above. Recorded rather than folded in,
because the log is append-only.

The human accepted both handoff proposals and applied them. **Note the route:
this layer did not edit either repo** — the proposals were carried by the human,
which is the designed flow and the only one that keeps the child systems'
gates intact.

- **F2 — brand-system gained `CYCLE-STATE.md`.** Rewritten in place at every
  phase boundary, read before `pipeline.md`, with `pipeline.md` named as the
  record of record on disagreement. The specific loss it closes: a human
  decision made at the gate but not yet in `decision-log.md` exists only in the
  transcript, and re-asking produces a cleaned-up second answer instead of their
  first blunt one — which corrupts the §4.4 raw data.
- **F3 — personal-university's handoff is now written during the session.**
  `NEXT-SESSION.md` gained an `IN PROGRESS` marker and is touched at three
  points: after the brief, after teaching, and the moment the student gives
  engagement and friction. Full regeneration still happens at Phase 5.

**For review 001:** both were adoptions *from the catalog* rather than from the
human's memory. That is the first evidence bearing on thesis falsifier 2 —
whether the catalog actually drives adoption. One instance, on the day it was
written, with the same person in the loop. Weak evidence. Do not count it as
settled.

### Superseded same day — F5 withdrawn

`budget.md` was cut on 2026-08-09, unfilled. **F5 is withdrawn**, not resolved:
the human declined to state and maintain weekly capacity, and the file asked for
a recurring commitment in exchange for a benefit he did not want.

The finding behind F5 still stands in reduced form. Split by who pays, per
`patterns/predict-then-check.md`:

- **Kept, free:** observed distribution from `git log` across the four repos.
  Enough for what claim II is actually about — *where the misses cluster*, and
  whether the affected system's own Architect is about to misread them as a
  local cadence problem. That comparison never needed a denominator.
- **Lost:** any statement that the portfolio is overcommitted in absolute terms.
  Deliberate deprioritisation and quiet neglect now look identical from here.
  `meta/architect.md` instructs asking rather than assuming, because a layer
  that reads every quiet system as neglect is a guilt generator.

`meta/thesis.md` §II is amended and falsifier 3 restated. Recorded as a real
reduction in what this layer can claim.

**Second-order note, for review 001 and not actionable now.** This is the second
mechanism cut in one day for costing the human a recurring step, after the
student prediction in personal-university. Both were right on their merits and
both are documented. **A run of them would be comfort drift with good prose**,
and this layer is the only thing positioned to see a run — PU's Architect can
only see its own. At n=2, on the day the portfolio was built, this is not
evidence of anything. Check it at review 001.

### Watching

- **Whether BS's Critic ever kills a draft or disagrees with the Writer.** Never
  doing either makes it decoration that reads as rigour — its own Architect is
  instructed to catch this, so this is a check on that Architect as much as on
  the Critic.
- **Whether the 2026-08-09 cut of the student prediction was discipline or the
  first instance of comfort drift.** PU's architect log flags the second-order
  check itself. One cut with that reasoning is discipline; a run of them is §9.
  This layer is better placed to see a *run* than PU's Architect is.
- **Whether ZET's operational maturity transfers.** It is the only system that
  has been tested by an external world. Its patterns are the best-evidenced in
  the catalog and are all currently under-adopted.
- **Whether four systems is too many.** Not a finding — two days is no evidence.
  It is the question review 001 exists to answer, and the answer will come from
  `budget.md`, not from this log.

---

## Entry 000b — purpose restated, 2026-08-10

**Not a review.** A restatement of the layer's purpose by the human, applied to
the documents. Recorded here because it changes what future reviews are for, and
a review that inherited the new charter without knowing when or why it changed
would be reading a different repo than the one entry 000 describes.

The two-review clock does not start here. It still starts at review 001.

### What changed

**The layer was doing two jobs and had only written down one.** `charter.md`
described a passive evaluator — quarterly, hands-off, produces nothing but
findings, deletes itself if it stops being useful. In practice `patterns/` was
already the thing new systems were built from, and nothing said so.

Restated as **two jobs on two clocks**:

- **Generative, on demand.** New systems are grown from the spine. Zero cadence.
  Captured in the new `spine.md`.
- **Evolutionary, quarterly.** Proven divergence is carried back into the spine.
  Slow because evidence accumulates slowly, and because a spine change reaches
  every system built afterwards.

The asymmetry is the design: divergence is cheap and local, convergence is
expensive and deliberate.

### The kill condition is removed

Two consecutive reviews producing no finding a local Architect couldn't have made
no longer deletes the repo. That condition was correct for a pure observer and is
wrong for the thing systems are grown from — it measured a seed by the harvest of
a season it wasn't planted in.

**What replaces it is a bar on action rather than existence:** the spine does not
change until the children have earned the change. Reasoning in `charter.md` § On
self-judgment and `meta/thesis.md` § On falsifiers and existence.

The falsifiers survive and are still checked in writing every review. They test
claims now, not the repo's right to exist. **Entry 000's failed falsifier check —
three of five findings within reach of a local Architect — should be re-read
under this frame: it is evidence about thesis claims III and IV, not a countdown.**

### The founding convergence claim is withdrawn as stated

Entry 000 and the original thesis treated four systems converging on one spine as
proof the spine is architecturally necessary. **Four systems built by one person
across two days is one derivation repeated, not four independent ones.**

This repo already applies exactly that skepticism one level down — the mPulse
columns are marked `†` and barred from the convergence claim on the grounds that
copies are not evidence. Applying it downward while exempting the founding set
was this layer's first blind spot, and it is the kind of error nothing below was
positioned to catch either.

**What survives:** the spine is a well-motivated hypothesis with a plausible
mechanism behind every element and no evidence yet. Sufficient to build from,
insufficient to be confident about. The real evidence comes from systems grown
separately and left to diverge — which is what the two-clock design is for.

### Consequences for review 001

- **The eight `proven` statuses have not been audited against the new
  independence bar** (`patterns/README.md`), which now requires two or more
  independent adopters plus evidence of a changed outcome. Some will not survive.
  **This is a demotion exercise and it is review 001's first job.**
- The next new system should be **grown from `spine.md`, not copied**. Copying is
  the path of least resistance and produced zero convergence evidence twice on
  2026-08-10. Claim I has no other route to evidence.

### Files changed

`charter.md`, `README.md`, `HANDOFF.md`, `meta/thesis.md`, `meta/architect.md`,
`patterns/README.md` rewritten. `spine.md` created. `systems.md` untouched — the
registry is still accurate and reconciling it is review 001's job, not
bookkeeping's.

### Watching

- **Whether the generative half stays a resource.** The pull toward writing an
  instantiation procedure will be strong the first time someone starts a project
  and wants a checklist. The reasoning against it — a procedure freezes one
  model's understanding into the framework — is recorded in three places on
  purpose.
- **Whether the spine changes before review 001.** It should not. Any change
  between now and then is premature evolution by definition, since no review has
  produced evidence.
- **Two public repos, no recorded decision.** `personal-university` and now
  `meta-architecture`, which names and describes five private ones.

---

## Review 001a — the two engineering teams, 2026-08-08 → 2026-08-13

**Run scoped, not folded into review 001.** Stated here because the flag asked
for the call either way.

The argument that decided it: review 001's first job is re-auditing the eight
`proven` statuses against the independence bar, and that needs all six systems.
This flag covers two. Folding them together would either delay the demotion
exercise behind a two-system window or let a two-system window contaminate a
portfolio-wide re-audit. **001a is scoped to the open items it can actually
answer and promotes nothing.** Review 001 is undischarged and its first job is
unchanged.

**Input:** `inbox/2026-08-13-flag.md` and `inbox/2026-08-13-evidence-eng-teams.md`,
assembled by a session outside the portfolio. Both say to verify before use.
**Every figure below was re-derived from the repos**, and the verification found
two errors in the brief — recorded under § What the brief got wrong, because a
brief that is right about 40 things and wrong about 2 is more dangerous than one
that is wrong about all of them.

### Distribution

Observed from `git log`. No stated capacity, and none inferred — `charter.md`.

| System | Commits at 000 (08-09/10) | Commits at 001a (08-13) | Δ | Architect runs |
|---|---|---|---|---|
| zesty-eng-team | 62 | **138** | +76 | **3** (08-08, 08-09, 08-13) |
| mpulse-engage-team | 1 | **51** | +50 | **1** (retro 001, 08-13) |
| personal-university | 24 | not read this window | — | not read |
| brand-system | 7 | not read this window | — | not read |
| mpulse-dpi-team | 1 | not read this window | — | not read |
| media-log | 18 | not read this window | — | not read |

**The four unread rows are the finding, not the two read ones.** A scoped review
sees attention where it was pointed, which is the one thing a distribution audit
must not do. Nothing here supports a claim about where the misses landed, and
none is made. **Review 001 still owes the real distribution table.**

What can be said: the human's attention over this window went overwhelmingly to
the two engineering teams, and both are `active` and delivering. That is a fact
about the window, not a judgment about the other four.

### The Architects

**F4 of review 000 is now false and that is the headline.** Its baseline —
*"Zero Architect reviews have been completed across the portfolio"* — held for
four days. Four reviews have now run.

**zesty-eng-team's Architect — the only one in the portfolio with a track record.**

- **Ran three times**, on cadence (at `/retro`), 08-08, 08-09, 08-13.
- **Has graded its own prior cycle proposal by proposal** (`docs/decision-log.md:487`).
  Verified: P3 fired as designed, P5 caught the browser-identity trap, P6 fired
  twice, P9 held, P2 fired then drifted, P4 and P7 inert, **P8 did not work** —
  four further instances after it landed, replaced by `1646f8b` at a narrower
  scope. This is the only instance in the portfolio of a change being applied,
  measured, **falsified**, and replaced. It answers thesis claim IV's question in
  the affirmative for one Architect.
- **Has proposed killing something:** P10, retired at retro #3 (`:407`).
  Qualified — it retired a *proposal that was never applied*, which is cheap.
  **It has never retired an applied rule.**
- **Has withdrawn findings.** Two false statements it had itself committed hours
  earlier in `aa5a5f4` were corrected in `c2fa6be` (`:507`). Verified both.

**mpulse-engage-team's Architect — one run, and the un-run mechanism ran.**

- **Retro 001, 2026-08-13.** Nine `retro:` commits plus dispositions.
- **`HANDOFF.md` open item 4 is answered.** The drift check against
  `agentic-development-tools` — registered at 000 as *"an un-run mechanism
  guarding a live liability"* — ran, and **found real drift**: `047dd6b`
  (+38/−2 across `definition-of-done.md`, `platform.md`, `repo-map.md`), recorded
  as D-018 and D-019. Verified. The mechanism is no longer hypothetical.
- **Has not graded a prior cycle** — there was none, and `.claude/commands/retro.md`
  has no step for it. That is a structural gap, not a miss, and it is in the
  carry-packet.
- **Has not proposed killing an applied rule.** Nor has ZET. See MF-1.

**Neither Architect has been running long enough for the stability-versus-sleep
test.** Not applicable at n=3 and n=1.

### Catalog

Verified against the repos, not read from the matrix.

**Corrections applied to the matrix:**

| Cell | Was | Now | Basis |
|---|---|---|---|
| MET × overhead ceiling | ❌ | **✅** | 1,300-line read-path cap in `.claude/agents/architect.md:105`, machine-asserted through `tools/verify_docs.py`; plus the pruning half, `tools/gates.py --dead`, wired into the same file |
| MET × honest metric | ⚠️ | **✅** | D-019 excludes the release PR from the denominator **by name**, reported as excluded in `docs/team-log.md:360`. That is the `unmeasured` discipline, independently re-derived |

**Both ✅ carry a footnote and it matters: neither has fired.** The read-path cap
is 1,300 against a current 1,056 (`wc -l` on the seven read-path files, re-run) —
**it has never bound anything.** `tools/gates.py` reports **12 of 12 declared
gates unrecorded** — re-run, exact. Presence is what the matrix records; effect
is what the promotion gate requires, and these have the first without the second.

**MET now holds two patterns its parent lacks** — executable claims
(`verify_docs.py`, 244 lines, 6 assertions, re-run 6/6 passing) and gate
instrumentation (`gates.py`, 157 lines). **This is the first instance in the
portfolio of a copy inventing rather than dropping.** The `†` note is amended to
say so, because it qualifies how far that column can be discounted.

**Candidates recorded. Nothing promoted. `spine.md` untouched.**

| Candidate | Origin | Adopters | Changed outcome? | Recorded as |
|---|---|---|---|---|
| Adversary on the improvement loop | ZET `ac65e24` | 1 | **Yes** | `provisional`, retirement test at ZET retro #4 |
| Grade the previous cycle's proposals | ZET `decision-log.md:487` | 1 | **Yes** | `provisional` |
| Gate instrumentation | MET `gates.py` | 1 | **No** — 12/12 unrecorded | `proposed` |
| Executable claims | MET `verify_docs.py` | 1 | Partial | `proposed` |
| Read-path budget | MET `verify_docs.py` | 1 | **No** — has never bound | `proposed` |

**Four of five have one adopter and nothing measured.** Recording them with
origin and cost is the whole job; promoting any of them on a five-day window is
the named failure mode, in the exact form `charter.md` describes it — *a fresh
idea from a live project is the most persuasive thing that will ever cross this
layer's desk.* The two with real evidence are still `provisional` at one adopter.

### Ruling on the MF-5 gate question

The flag asked for a ruling in either direction so it stops being ambiguous.
**Here it is, and it is a narrow yes.**

**The question.** MET is a copy. It inherited ZET's blockers-per-PR metric
*complete with the flaw* — the matrix already records both mPulse teams dropping
the `unmeasured` category. It then independently diagnosed the fault and built a
**different** remedy. Does that count as evidence, when *copies are not evidence*?

**Ruling: a copy provides independent evidence for a pattern it demonstrably did
not inherit.** The independence bar exists to stop counting a pattern that
arrived as part of a package. It was never aimed at a copy re-deriving something
its own inheritance omitted. The inheritance explains the flaw; it does not
explain the diagnosis.

**The test is documentary, not inferential** — and it has to be, or this becomes
a hole in the bar:

> The catalog must **already record the copy lacking the pattern**, or the copy's
> own log must record deriving it from its own failure. Absent that record, the
> default holds: copies are not evidence. The exception is available once per
> pattern per copy, at the moment the gap is on the record, and **cannot be
> claimed retroactively** for a pattern that was simply never checked.

Here the record exists and predates the evidence: `patterns/README.md` has
carried *"Both inherited `⚠️` on the honest metric"* since 2026-08-10, written as
an example of a copy losing something. That is exactly the documentation the
test requires, and it was written before anyone knew it would be needed.

**What the ruling does not do: it does not promote `honest-metric`.** It stays
`provisional`, and **the reason it stays changes**, which is the useful part.

- **Old reason:** one independent adopter.
- **New reason:** two independent adopters, **neither remedy measured.** ZET's
  `retro-metric.py` is one day old. MET's escape rate has never been reported
  once.

**Two independent diagnoses of the same fault, with two different remedies, is
strong evidence the fault is real and no evidence either remedy works.** That is
a sharper statement than the old one and it names exactly what review 002 has to
find: has either remedy changed a number.

`patterns/README.md` and `patterns/honest-metric.md` are amended with this.
**It is a clarification of the gate in the catalog. `spine.md` is not touched**,
and the higher bar for the spine is why.

### Falsifier check

All four, in writing. This is the first window that produced data bearing on any
of them.

**Claim I — a spine read as a resource produces better systems than starting
fresh.** *Falsified by: spine-grown systems are no better than cold-built ones,
or the spine is read then ignored at instantiation.*

**Still unchecked, and the reason is unchanged: no system has been grown from the
spine.** Both systems in this window are copies of ZET. `HANDOFF.md` said on
08-10 that the next system must be grown rather than copied and none has been
built since. **Claim I has had no route to evidence for four days and still has
none.** Not a failure of the claim — an absence of the experiment.

**Claim II — convergence must be slow and gated.** *Falsified by: thin-evidence
spine changes turn out fine repeatedly; or the gate is so high nothing crosses
and the spine freezes while children diverge into unrelated systems.*

**The second half is now live and this window is the first real test of it.**
Five candidates arrived, two with genuine evidence, and the gate held — nothing
promoted, `spine.md` unchanged. That is the gate working as designed at one
review. It is also exactly what the freeze failure looks like at one review, and
the two are indistinguishable from here. **The distinguishing test is whether
anything crosses at review 002 or 003 when the evidence has accumulated.** Named
now so it cannot be quietly re-read later as vindication.

Divergence is real and measurable: ZET grew **epistemic** (better at knowing
whether its beliefs are true — a second adversarial pass, a metric that refuses
false zeros); MET grew **mechanical** (better at leaving traces — four tools, a
read-path cap). Five days from a common ancestor. **That is the divergence this
layer needs as input, arriving on schedule.**

**Claim III — cadence is a shared resource and every local Architect is blind to
it.** *Falsified by: every system meets its cadence, window after window, no
misses cluster.*

**Not checkable this window and I will not pretend otherwise.** Four of six
systems were not read. The two that were both met their cadence and both ran
their Architect. On a two-system sample that is not evidence for the claim or
against it. **Review 001 owes this one.**

**Claim IV — nobody is scoring the scorers.** *Falsified by: the Architects'
self-audits turn out accurate and self-critical when checked against the logs,
review after review.*

**This claim took its first real hit and it is against the layer.** ZET's
Architect graded its own prior cycle proposal by proposal, **falsified its own
P8**, and corrected two false statements it had itself committed. I checked those
verdicts against the repo and they hold. That is a self-audit that was accurate
and self-critical, which is precisely the falsifying condition.

**One instance is not "review after review", so the claim is not withdrawn.** But
it is now the claim most likely to fail, and the honest statement is that the
best evidence available is *against* it. If ZET's Architect is this rigorous
again at retro #4, the audit-the-Architects job should be cut to a spot check, as
the thesis itself says. **Recorded so review 002 cannot read past it.**

**The ratio — could a local Architect have found this?**

Answered finding by finding, because review 000 failed this three of five and
said so.

| Finding | Local Architect could have found it? |
|---|---|
| MF-1 additive ratchet | **No** — needs both repos side by side. Each looks locally like a healthy retro |
| MF-2 adversary on the improvement loop | **Yes** — ZET invented it unaided. Carrying it to MET is the layer's job, finding it was not |
| MF-3 gate instrumentation | **Yes** — MET invented it unaided |
| MF-4 executable claims | **Yes** — MET invented it unaided |
| MF-5 both fixed the metric two ways | **No** — the gate question only exists holding both repos |
| MF-6 structural questions only ever answer no | **No** — four instances across two repos, each locally correct |
| MF-7 every system is a closed loop | **No** — MET stated its half; that all systems share it is not visible from inside one |
| MF-8 loop overhead | **Partly** — each could see its own; neither has a tripwire, and that both lack one is cross-system |

**Five of eight cross-system, three within local reach.** Review 000 was three of
five *the other way*. This is better and should not be read as more than it is:
the three local findings are the three inventions, and this layer did not
generate them — it carried them. **The carrying is the value in those three
cases, and carrying is a service, not an insight.**

### What the brief got wrong

Recorded because `meta/architect.md` requires reading the repo rather than the
record, and because this is what that instruction is for.

1. **"Matrix, ZET × honest metric | ⚠️ | Argue it."** — **wrong about the current
   state.** ZET is already **✅** on honest metric in the matrix and has been
   since it was written; ZET *invented* the pattern. No change was needed. The
   substantive point behind it — that `unmeasured` is now enforced by
   `tools/retro-metric.py` rather than merely instructed — is real and is recorded
   in `patterns/honest-metric.md` as a strengthening, not a matrix change.
2. **Instruction-file line totals do not reproduce.** The brief gives ZET
   447→584 and MET 742→942. Re-derived over `CLAUDE.md`, `docs/operating-rules.md`,
   `docs/definition-of-done.md` and all of `.claude/**/*.md`: **ZET 679→777, MET
   957→1,270.** The file set is not stated in the brief, so this is a definitional
   difference rather than a contradiction — and it is a live example of MF-4, a
   claim that cannot be re-run because the command that produced it was not
   carried with it. **The direction and the conclusion survive unchanged: both
   grew monotonically, MET fastest.** The absolute numbers should not be quoted.

**Everything else re-derived exactly**, including the figures most load-bearing
for the findings: ZET **+155/−47** and MET **+209/−21** on instruction files, to
the line; `gates.py` **12/12 unrecorded**; the read path at **1,056** against
1,300; `verify_docs.py` **6/6 passing**; every `decision-log.md` line citation;
tool line counts; and all four structural-question instances.

### Findings

Numbered `MF-n` to match the flag. **Accepted as stated except where noted.**

- **MF-1 — no system has ever removed an applied rule. Accepted.** Verified: every
  deletion in both repos is a replacement, a renumbering, or a correction. **Zero
  retirements across 138 + 51 commits.** Both `/retro` files instruct against this
  and both lose every cycle. **A rule that is losing every cycle is data about the
  rule, not about the sessions running it.** → both carry-packets.
- **MF-2 — the improvement loop was the one pipeline with no independent adversary.
  Accepted.** `independent-adversary` is `proven` and in `spine.md`, which says
  *wherever the system produces something that can be wrong*. Every system read
  that as the work pipeline. **The retro produces self-modifications — the
  highest-blast-radius output any of these systems has — and it was exempt
  everywhere, including here.** → MET's packet; and a spine question, below.
- **MF-3 — a rule firing left no trace, so the optimizer could only add. Accepted.**
  MET's own sentence is the best in either repo: *"the system could observe its own
  outputs but not its own mechanism."* This is the mechanism behind MF-1 and the
  reason MF-1 is not fixable by writing a better instruction. → ZET's packet.
- **MF-4 — claims are re-read rather than re-run. Accepted**, and this review is
  itself an instance of the failure it names (see § What the brief got wrong, 2).
  → ZET's packet.
- **MF-5 — ruled on above.** No proposal to either child. The finding was about
  this layer's gate and it has been answered here.
- **MF-6 — structural self-assessment happens, but only ever answers no. Accepted,
  and it is the finding that belongs here rather than in the children.** Verified
  all four instances (ZET `:170`, `:188`/`:237`, `:465`; MET `:58`). **Four
  structural questions, four declines, all about roles.** Every one is locally
  correct and well-reasoned; the finding is the shape of the set. Rules only ever
  get added (MF-1); structure only ever gets refused. Both ratchets point away
  from change and **neither Architect can see it, because each decision is locally
  right.** Nobody in either repo has asked whether the memory substrate is right
  (both team logs ~500 lines, append-only), whether the pipeline shape is right,
  or whether the main session is overloaded — it holds **at least five jobs**:
  dispatcher, judge of proposals, applier of diffs, reporter of the metric, and
  the party the retro is about. ZET's own `/retro` names that conflict and answers
  it with *another review pass*, not less load. **That may be right. Nobody has
  asked.** → the spine, and `meta/architect.md`.
- **MF-7 — every system is a closed loop, and that bounds the thesis. Accepted.**
  MET states it against its own interest and it is verified verbatim at
  `docs/team-log.md:499-505`. ZET is in the same position by a different route:
  three graders, all bots, one account, two of three overwriting their own comment
  on every push — which is how a retro scored a perfect zero on the ticket with
  the worst gate failure of the cycle. **This is not a child finding. A system
  whose only grader is itself gets measurably better at grading itself**, and that
  includes this layer, which has no independent adversary at all (`systems.md`
  records the absence). → the spine, and the human.
- **MF-8 — the improvement loop is consuming the capacity it serves. Recorded as a
  watch item, not a finding.** The counter-case is sound: retro #3 is also where
  the loop produced its best evidence, and a founding-window retro is expected to
  be top-heavy. **Two consecutive cycles is the signal; one is not.** What is not
  a watch item and goes in both packets: `overhead-ceiling` is `proven` and
  **neither team has a tripwire of any kind.** The tripwire is the proposal; the
  overhead figure is what it would measure.
- **MF-9 — new, found during verification and not in the brief. MET independently
  invented the carry-packet.** `.claude/commands/retro.md` § 7, *Check the sibling
  team*: **"Do not edit the other team's repo. Report it and let him carry it
  across."** That is `meta/dispatch.md`'s rule, arrived at one level down, by a
  system that has never read this repo. **It is the second independent arrival at
  never-edit-a-sibling-report-and-let-the-human-carry**, and it is evidence for
  the dispatch design that does not come from the person who wrote it. → recorded
  as a candidate; routes to the human as support for the charter amendment.

### Corrections to stale facts

Not findings. A stale catalog reads as verified, which is why
`meta/architect.md` requires checking it. Applied this review:

- **`HANDOFF.md` open 2** — *"No Architect has run anywhere"* → four reviews have
  run, ZET ×3 and MET ×1. Open item closed with what it measured.
- **`HANDOFF.md` open 4** — *"MET's drift check un-run"* → ran 08-13, found real
  drift, `047dd6b`. Closed.
- **`systems.md` ZET** — 62 commits → **138**.
- **`systems.md` MET** — 1 commit, no ticket run → **51 commits, 5 PDEV + 1 INFRA
  ticket, 7 PRs, 1 retro**, and the D-001 open item resolved.
- **Adoption matrix** — the two cells above, plus the `†` note amended to record
  a copy inventing.

### Prior proposals — did they land?

Review 000's F1 — brand-system's stale README — **was not checked this window.**
brand-system was not read. It remains open and moves to review 001 unchanged.
F2 and F3 landed on 2026-08-09 and were recorded then. F5 was withdrawn.

**This is a scoped review's structural weakness, stated rather than papered
over:** a review that reads two repos cannot audit proposals made against a
third, and the open item survives the review that was supposed to close it.

### Proposals

1. **Mandatory subtraction at every retro** — to: **both** Architects — evidence:
   +155/−47 and +209/−21, zero retirements, both `/retro` files instructing
   against it and losing. Carried in both packets.
2. **Gate instrumentation** — to: **ZET's** Architect — evidence: MET `gates.py`,
   12/12 unrecorded baseline. Carried with its weakness: zero evidence of effect.
3. **Executable claims** — to: **ZET's** Architect — evidence: MET
   `verify_docs.py`, 6 assertions, re-run 6/6.
4. **An adversarial second pass on the retro** — to: **MET's** Architect —
   evidence: ZET `ac65e24`; 6 of 13 applied changes from pass 2; a metric wrong
   for three cycles corrected. Carried with ZET's own retirement test unreturned.
5. **Grade the previous cycle's proposals** — to: **MET's** Architect — evidence:
   ZET `decision-log.md:487`, P8 falsified and replaced.
6. **An overhead tripwire** — to: **both** Architects — evidence: `overhead-ceiling`
   `proven`, ❌ for both, MF-8's ratios.
7. **To the human, not to any child: `charter.md` § What it must never do should
   say whether dispatching is permitted.** `meta/dispatch.md` is installed and the
   packets are written; **the amendment is not made and it is his file alone.**
   Suggested wording is in `meta/dispatch.md`. **The packets are held until he
   makes it** — reading the charter's silence as permission is how a boundary
   erodes without anyone deciding to move it, which is the argument in that file
   and it applies to this layer first.
8. **To the human, not to any child: MF-7 needs money or time, not a rule.**
   Both teams' graders are bots. MET's window drew no human review at all and its
   external coverage was incomplete across the target repos; ZET's three graders
   are all bots under one account. **One human engineer reviewing one team PR
   would do more than everything either team committed on 08-13** — MET's words,
   and the evidence supports them. **Buying external feedback is a decision only
   he can make and no Architect anywhere can propose it.**
9. **A spine question, deliberately not a spine change.** `spine.md` gives every
   system *an Architect on a cadence that proposes and never applies* and says
   nothing about **the scope of what it may propose.** Both children read that
   scope as the contents of the existing files (MF-6). And `independent-adversary`
   says *wherever the system produces something that can be wrong*, which every
   system read as the work pipeline and not the improvement loop (MF-2).
   **Neither is a promotion and neither changes `spine.md` today** — one review,
   two systems, five days. **Recorded as the two spine questions review 001 must
   answer**, with the evidence attached, so they arrive at that review already
   argued instead of being re-derived.

**`meta/architect.md` § 3 gains no counterpart question this review.** It asks
*has it ever proposed killing something?* and MF-6 says it needs *has it ever
proposed a change to the system's shape?* **That edit is correct and I am not
making it on one window.** It is proposal 9's other half and belongs with it.

### Watching

- **Whether ZET's retro #4 returns anything material.** The two-pass retro set its
  own retirement test — *if it returns nothing material two retros running, it is
  churn.* **Do not promote it before that test returns**, and do not let the
  strength of its first run substitute for the test.
- **Whether either team ever retires an applied rule.** MF-1's proposal is in both
  packets. **If both reject it, that is the more interesting outcome** — it would
  mean the additive ratchet is load-bearing for a reason neither this layer nor
  either Architect has articulated, and `meta/dispatch.md` rule 3 is right that a
  rejected meta proposal is the most useful signal this layer produces.
- **Whether `gates.py` ever records a `CAUGHT`.** 12/12 unrecorded is the
  baseline. **The instrument exists and the data does not**, and until it does,
  MF-3 is an argument rather than a finding.
- **Whether the read-path cap ever binds.** 1,056 against 1,300. It cannot bind
  until it is lowered or the docs grow 244 lines, and MET grew 313 in three days,
  so it will bind soon — **which is the first moment it becomes evidence.**
- **Claim IV, and specifically against the layer.** ZET's Architect has once done
  exactly what the claim says nobody does. A second instance at retro #4 makes the
  audit-the-Architects job a spot check.
- **Whether four unread systems stay unread.** Two scoped reviews in a row on the
  same two repos would be this layer following attention instead of auditing its
  distribution, which is the inverse of its job and would look like productivity
  the whole way down.

---

## Review 001a — dispatch record and supersessions, 2026-08-13

**Appended, not folded in.** The log is append-only and the entry above stands as
written, including the parts this section corrects.

**Both packets were dispatched the same day, on the human's explicit instruction,
before the `charter.md` amendment was made.** Open item 7 stays open: he
authorised the act, and the amendment that would make it durable for a future
session is still his to write. Verbal authorisation covered this instance; it did
not move the boundary.

**Order:** mpulse-engage-team first, then zesty-eng-team, per `meta/dispatch.md`
rule 5.

**Both child repos verified before and after: `HEAD` unchanged (`889bf4f`,
`6d43727`), working tree clean, zero untracked files.** Write, Edit and
`git commit/push/add` were denied at the tool layer rather than requested in the
prompt, so *apply nothing yet* was enforced rather than trusted. **This layer
still edited nothing.** Both presentations were relayed to the human verbatim;
the approvals are his and no change has been applied anywhere.

### Outcomes

| Finding | mpulse-engage-team | zesty-eng-team |
|---|---|---|
| MF-1 mandated § Cuts | **Rejected** — premise false there | **Accepted**, with a non-optional amendment |
| MF-1b overhead ceiling | **Accepted** at 1,100, math corrected | **Rejected** — wrong file set |
| MF-2 adversary on the retro | **Rejected** on its own evidence | No action; retirement test held |
| MF-2b grade the prior cycle | **Accepted** — its highest-value item | n/a (already does it) |
| MF-3 gate instrumentation | n/a (inventor) | **Rejected**; one clause salvaged |
| MF-4 executable claims | n/a (inventor) | **Convention accepted, 2 of 3 targets rejected** |
| MF-8 overhead ratio | **Accepted** | Watch item, unchanged |

**Five accepts, five rejects, across two repos.** `meta/dispatch.md` rule 3 says a
rejected meta proposal is the most useful signal this layer produces. **It was
right, and the rejections were better than the accepts.**

### Supersessions — three claims in the entry above are wrong

**1. MF-1's diagnosis was false for mpulse-engage-team. Withdrawn as stated.**

The entry above says the subtraction question is *"going unasked, four times out
of four."* **It is asked there.** `.claude/agents/architect.md:124` mandates a
§ Cuts section — *"do not skip this section — if nothing should be cut, say so and
say why you believe it."* Retro 001 produced one, proposed C3, and **the judging
step rejected it with a recorded reason** (`docs/team-log.md:420`). Verified
directly after the rejection came back.

**What survives, narrower and better:** zero applied rules have been retired
across both repos — that figure is unchanged and re-verified. But the *cause*
differs by system, and only one of them is the cause this layer named. **ZET does
not ask** (`retro.md` contains no instruction to cut anything; `architect.md:74`
covers retiring a role, `CLAUDE.md:88` a standing blocker, neither a rule).
**MET asks and answered no, on the record.** Their sentence, which is the
correction: *"asked-and-answered is a different failure mode than unasked, and it
does not have the same remedy."*

The ZET packet was amended before dispatch and MF-1 was accepted there in its
corrected form.

**2. MF-3's premise was false for zesty-eng-team. Withdrawn as applied to ZET.**

MF-3 argues: *your architect is instructed to cut rules that never fire, but a
rule firing leaves no trace, so the instruction is unimplementable.* **The first
half is not true of ZET.** `architect.md:74` is about retiring an unused *role*.
The instruction MF-3 answers is in **MET's** `architect.md:102` — which is where
`gates.py` was invented, and correctly so. **This layer read a mechanism in one
repo and asserted its precondition in the other without checking.**

MF-3 stands as a finding about MET and is withdrawn as a proposal to ZET. **ZET
salvaged the one part that transfers** — `gates.py`'s two-state reporting, *never
recorded is not the same as never needed* — and wrote it into its MF-1 acceptance
as a required clause, on evidence this layer had not gathered: its own inert
proposals P4 and P7 are both unfired for reasons unrelated to whether they work.
**As-is, the candidate list this layer called "close to free" was a list of two
things it would be actively harmful to cut.**

**3. The overhead measurement was scoped wrong, in both directions. Withdrawn.**

The entry above reports instruction-file totals as a proxy for the read path.
**Both children measured it properly and both corrected it, differently:**

- **MET:** 957→1,270 is the whole instruction corpus and includes files no ticket
  session opens. The capped set is **709 → 1,056**, net **+140 in the last window
  alone**. 1,300 is under two windows out, not "a month" — the accept stands at
  1,100, justified on their series rather than this layer's.
- **ZET:** 777 **is not a read path.** It carries ~430 lines of slash commands no
  ticket session opens and **excludes every file the boot ritual mandates.** What
  a ticket session actually reads today is **1,474** lines including
  `../manager-ui/CLAUDE.md`, grown **~+895** over the window —
  `docs/team-log.md` 93→547, `knowledge/manager-ui.md` 54→336,
  `knowledge/product.md` 0→122. **This layer measured the slowest-growing eighth
  of the problem and proposed capping that.**

ZET's rejection is the sharper form of this layer's own argument: **a ceiling that
binds the wrong set is worse than none, because it licenses cutting the wrong
thing.** It named its real gap itself — `CLAUDE.md:90` tells the architect to
condense `team-log.md` at a retro, it is prose with no number, and 93→547 says it
has never fired.

`patterns/overhead-ceiling.md` is amended. **The failure mode this layer recorded
at 001a — a ceiling set above the current value — is now joined by a worse one it
committed itself: a ceiling measured over the wrong file set.**

**Also corrected, minor:** ZET could not reproduce this layer's own start figure
(679 vs 671 on the stated file set). **That is the third unreproducible line count
in this review**, after the two already recorded under § What the brief got wrong.
Three, in a review that carried MF-4 as a proposal. The finding is not that the
numbers were far off — they were not — it is that **none of the three could be
re-run, only re-argued.**

### MF-10 — the layer can only propose against the loop it can see

**New, and it came from zesty-eng-team's Architect rather than from here.** It is
the most valuable thing either dispatch returned:

> *"All four proposals target the retro loop; none touches the ticket pipeline...
> a packet that can only see the meta-loop will only ever propose against the
> meta-loop, and this team's demonstrated failure rate is downstream of it."*

**This is a structural bound and it is written into `meta/architect.md`:** *"You
read the children's logs and architecture, not their content."* That instruction
is correct — it is what stops this layer developing opinions about a blog post or
a curriculum topic — **and it has a consequence nobody wrote down.** A layer
restricted to logs and architecture can only ever see the improvement loop, so
every proposal it makes will be about the improvement loop, **whatever the
system's actual failure rate is doing.**

ZET's numbers make it concrete: 0.83 auto-reviewer findings/PR and 2.00 Director
findings/ticket at retro #3, both non-zero, both on **delivery** — and all four
proposals it received were about the retro.

**This compounds MF-6 and MF-8 into something worse than either.** MF-6: rules
only get added, structure only gets refused. MF-8: the improvement loop consumes
the capacity it serves. **MF-10: the only layer positioned to notice is
constitutionally aimed at the improvement loop as well.** All three ratchets point
the same way, and this one is the layer's own.

**Not resolved here, and deliberately not.** The fix is not obvious — reading
child *content* is the thing `meta/architect.md` forbids for good reasons, and
loosening it would be this layer acquiring opinions about `manager-ui`. **Recorded
as review 001's third spine question**, alongside the two in proposal 9.

### Falsifier check — amended

**Claim IV takes a second hit, and it is now the claim in most trouble.**

The entry above recorded ZET's Architect performing an accurate, self-critical
self-audit — claim IV's falsifying condition, at n=1. **The dispatch produced n=2
and n=3, in a harder form.** Both child Architects were handed proposals from the
layer that audits them, and both:

- **checked the layer's premises against their own repos rather than deferring**
  — MET ran `gh api` across six PRs to test whether it had ZET's endpoint defect
  before rejecting MF-2, and found 27 external findings against 27 counted;
- **found the layer's premises false**, twice, in the two findings the layer had
  ranked most confident;
- **rejected on evidence and said why**, in a form this layer could verify and did.

**Six of ten proposals from the auditing layer were rejected or materially
amended by the audited Architects, on evidence the layer had not gathered.** That
is the opposite of the coupling claim IV asserts.

**Claim IV is not withdrawn — it has never been tested at the cadence it
describes, and one dispatch is not "review after review."** But its status is
downgraded from *untested* to *contradicted at every instance so far*, and
`meta/thesis.md` says plainly what follows if this holds: the
audit-the-Architects job *"should be cut to a spot check."* **That is a live
proposal at review 001, not a hypothetical.**

**The ratio, restated honestly.** The entry above claimed five of eight findings
were cross-system. **Two of those five had false premises in the repo they were
aimed at** (MF-1 at MET, MF-3 at ZET), and both were caught locally. The corrected
reading: **this layer's cross-system findings were right about the pattern and
wrong about the mechanism**, and the mechanism is where the proposal lives. **A
finding no local Architect could make is not the same as a finding no local
Architect could correct**, and review 000's falsifier only ever asked the first
question. **That is a defect in the falsifier, not just in this review.**

### Watching — added

- **Whether MF-1's § Cuts section, accepted at ZET, ever produces a removal.** It
  is accepted with the explicit understanding that a recorded *no* is a valid
  output. **If it produces only recorded nos for two cycles, that is the same
  ratchet wearing the mechanism this layer proposed** — and MET's C3 rejection is
  already one such no.
- **Whether escape rate is computable at all.** MET reports it is **structurally
  zero until the first instrumented ticket ships**, since `gates.py` shows 0
  CAUGHT. The entry above called it *"the single most useful number retro 002
  could produce."* **That was wrong and is corrected: it cannot be produced until
  a ticket runs under the new instrumentation.**
- **MET's comment marker, found by MET and not by this layer.**
  `operating-rules.md:96` requires `<!-- mpulse-engage-team -->` on every team
  comment so the metric can separate team from external. **It missed once.** The
  miss landed on the repo with the weakest external coverage — the one that
  produced the window's only blocker — so a grep at retro 002 reads the team's own
  comment as an external review. **One unmarked comment is one phantom external
  review**, in the metric that MF-7 says is already measuring almost nothing. The
  specific PR is in MET's own log; it is not reproduced here.
- **Whether the dispatch mechanism survives its own first outcome.** It worked —
  no repo was edited, both presentations reached the human, and the rejections
  improved the second packet before it was sent. **The ZET packet was amended
  mid-dispatch on MET's rejection**, which is the loop doing something no
  hand-carried packet would have done. **That is one instance and it was
  supervised. `meta/dispatch.md` is `provisional` at best and should not be read
  as validated.**

### MF-9 strengthened — the sibling boundary is enforced, not instructed

Recorded at 001a from `mpulse-engage-team/.claude/commands/retro.md` § 7: *"Do not
edit the other team's repo. Report it and let him carry it across."* **The dispatch
surfaced that this is not only prose.** `.claude/settings.json` there denies
`Edit` and `Write` on `../mpulse-dpi-team/**`, `../dpi/**` and
`../agentic-development-tools/**` — the sibling team, the product repos, and the
shared org toolkit it does not control — alongside push denials on six named
service repos and `gh pr merge`.

**That is `human-gate` — `proven` — implemented as a harness constraint rather than
an instruction, and it is the strongest form of the pattern anywhere in the
portfolio, because it does not depend on the agent complying.** Every other system
in this registry, including this layer, relies on an agent reading a rule and
following it. MET is the only one where the boundary holds against an agent that
decides otherwise.

**Two things follow and neither is a promotion.**

First, this is a **candidate in its own right** — *enforce the boundary at the
permission layer, not only in the prompt* — with one adopter and no measured
instance of it stopping anything. `proposed`. It is also the natural answer to a
question this layer has never asked about itself: **nothing prevents a
Meta-Architect session from writing to a child repo except the instruction not
to.** Both dispatches were run with writes denied at the tool layer for exactly
that reason, and that was a decision made in the moment rather than a property of
this repo. **`.claude/settings.local.json` here has no such guard.** Review 001's
business, not a change to make on one instance.

Second, a defect worth carrying if this is ever adopted elsewhere: **the
`Write(...)` deny lines are inert.** The harness matches only `Edit(path)` for
file-writing tools and says so on every session start. MET's guard holds because
every protected path carries both forms — but a system copying only the `Write`
half would have a boundary that reads as enforced and is not. **That is the
copies-lose-the-invisible-part failure with a new surface**, and it is the first
instance of it in a config file rather than a document.

---

## Review 001a — closed, 2026-08-13

**What this review produced:** one scoped log entry with all four falsifiers
answered, a ruling on the independence bar, five catalog candidates and zero
promotions, `spine.md` untouched, six stale facts corrected, two carry-packets
written and dispatched, ten proposals judged by the two Architects they were aimed
at, and **three of this layer's own claims withdrawn on the children's evidence.**

**What it could not do, stated so the next session does not assume otherwise:**

- **`charter.md` is unamended and dispatch remains unwritten into it.** That file
  is the human's alone — the rule is in its first two lines and restated in
  `meta/architect.md` and `meta/dispatch.md`. **This layer may not edit it to close
  its own open item**, and the fact that the packets went out anyway on verbal
  instruction makes writing it down more urgent, not less.
- **The five accepted proposals are not applied.** They belong to each child's
  human gate and `meta/dispatch.md` rule 4 forbids this layer following up.
  Whatever happens to them is read at review 002 as evidence, not chased.
- **Review 001 is undischarged.** Four of six systems unread, brand-system's F1
  still open from review 000, and the eight `proven` statuses still un-audited
  against the independence bar. **001a did not touch any of it.**
- **MF-7 is unanswered and only the human can answer it.**

---

## Publication note — what this public repo does not carry, 2026-08-13

**Decided by the human at the moment of publishing review 001a.** Recorded here
rather than done silently, because an undocumented redaction is indistinguishable
from a gap in the evidence, and this log is the evidence base.

`meta-architecture` is public by a deliberate decision on 2026-08-10, and that
decision was made when this repo described **systems**. Review 001a is the first
entry to carry **operating detail about a regulated third-party platform** — one
this portfolio does not own, whose other engineers did not consent to being
written about, and which `systems.md` already declines to govern for exactly that
reason.

**Held back from publication, and only these:**

- **`inbox/` is not published.** The source brief and its evidence companion are
  held on the human's machine. Every citation in this entry that points at
  `inbox/` resolves there. **The findings are reproduced in full above** — what is
  withheld is the raw brief's granularity, not its conclusions.
- **Repo-by-repo external review coverage for mpulse-engage-team.** The finding
  stands in full: MF-7 says both teams are closed loops graded only by bots, that
  the window drew no human review, and that one engineer reviewing one PR would
  outweigh everything either team committed. **What is not published is the map** —
  which repos had no external reviewer, in what proportion.
- **Specific PR and ticket identifiers** on both engineering teams' target repos.
  Citations now point at the child's own `decision-log.md` line, which is a better
  citation anyway and resolves for anyone with repo access.

**Nothing else was cut, and no argument, verdict, or number that bears on a
finding was softened.** The line drawn is between *what this layer concluded*,
which is the whole point of a public evidence base, and *the operational surface
of an employer's regulated platform*, which is not this layer's to publish.

**What this costs, stated because the pattern this layer preaches requires it:**
`meta/architect.md` says no finding without evidence, and every claim must cite a
file, commit, or line. **Three of MF-7's citations are now unresolvable to a
public reader.** That is a real reduction in this entry's checkability and it is
the price of the repo being public. **If the portfolio keeps producing findings
that cannot be published with their evidence, that is an argument about the
repo's visibility, not a reason to keep trimming the evidence** — and it belongs
to the human, who owns both decisions.

---

## Advisory 2026-08-14 — holistic assessment of the framework, on the human's request

**Not a review.** Commissioned off-cadence by the human with an explicitly wider
read than `meta/architect.md` permits: both engineering teams' full architecture
**and their delivery-side worklogs** — the surface MF-10 established no packet had
ever examined. Recorded here because `meta/dispatch.md` requires findings to be in
the log with evidence before they dispatch. The numbered-review clock is
untouched; review 001 remains next and undischarged.

**Delivery-side verdict, first vantage anyone has had on it:** the work product is
stronger than the improvement loop's paper trail suggests. ZET `tickets/1358-*`
and MET `tickets/PDEV-23733-*` are model artifacts — root cause at file:line,
judgment calls with their authority basis, "noticed, deliberately left alone"
sections, PHI described structurally in fixtures. MET's D-012 disposition record
distinguishes *declined to decide* from *accepted the risk* in writing, which is
governance hygiene most human teams lack.

**Verification corrections, mine, caught before dispatch this time:** the
assessment as delivered in chat said 2 of 9 ZET worklogs carry `## Director
findings` — re-derived, it is **4 of 10**. And it claimed MET's `timesheet.py`
captures token data — false; its "token" is Jira auth, and AI-usage fields flow
through the org's `update-ai-fields` path, which MET's log records as currently
400ing for Opus 5. Both packets below carry the corrected form. That is two
false claims caught by re-running my own greps, in an assessment that cites the
verify-before-report doctrine approvingly. The doctrine is earning its keep
against its own author.

### Findings AF-1 … AF-7

- **AF-1 — the plan is the one artifact with no independent gate.** The reviewer
  gates the diff; the plan arrives beside it and its frame is the easiest thing to
  accept unnoticed. MET paid (PDEV-23733: two rounds confirmed a flawless
  implementation of the wrong unit) and invented reviewer **§0** — framing before
  implementation: unit-check, defect-vs-instance, rename-survival. **ZET's
  reviewer has no equivalent** (verified: no framing/unit language anywhere in the
  file) and ZET's own history carries plan-frame failures — the 08-09
  design-mismatch postmortem, the #1358 declined-observation loss. Highest-value
  single carry available. → ZET packet.
- **AF-2 — instruction files are becoming archives on the read path.** Rules ship
  wrapped in founding incidents (run IDs, correction blockquotes); every session
  pays the history tax. Distinct mechanism from MF-1: *evidence* accretes inside
  the normative path. ZET's `CLAUDE.md:90` condensation instruction has never
  fired against `team-log.md` 93→547. → ZET packet (trigger with a number); MET's
  read-path cap already forces this trade if 001a's accept lands — nothing new
  carried there.
- **AF-3 — the headline metric is severity-blind, and ZET's human-metric
  collection is unverifiable.** A data-loss escape and a comment-noise finding are
  one unit. Both teams classify severity in review output; the headline erases it.
  And ZET: 4 of 10 worklogs carry `## Director findings` — the other six are
  either zero-correction tickets or uncollected data, and the metric cannot tell
  which. → both packets (buckets); ZET packet (explicit "none" line at close, on
  the pattern of MET's mandatory `## Outcome`, `a138f1e`).
- **AF-4 — state should be derived, not written.** ZET's costliest self-inflicted
  class is stale self-authored state (auth-state.json ×3 retros; 2 of 3 escalation
  items settled). Its remedy is rules-about-verifying; MET's is `state_check.py`
  deriving `Current state` from GitHub/Jira. Verified: ZET `tools/` has no
  equivalent. → ZET packet.
- **AF-5 — cross-team inventions sit unshared for a quarter.** Reviewer §0,
  `gates.py`, `state_check.py`, the two-pass retro, the grading step: each
  invented in one team with the other equally exposed, and the only channels are
  the human and this layer's quarterly clock. MET already runs the shape of the
  fix (upstream drift check; retro § 7 sibling report). Candidate mechanism: each
  architect reads the sibling's `decision-log.md` delta at retro as evidence
  input — read-only, no authority, judged locally. **Spine question — it changes
  an Architect's read-list. → review 001, not a packet.**
- **AF-6 — context economics are unmeasured, so rule-growth has no price.**
  Corrected form: no instrument currently captures context-per-ticket
  (`timesheet.py` is Jira time-tracking; `update-ai-fields` carries tool/time/
  tokens but 400s on Opus 5 and nobody feeds it back to the retro). MF-1 argues
  from line counts because that is the only ruler. → MET packet (smallest honest
  step: surface what update-ai-fields already collects, note the 400).
- **AF-7 — the test surface never grows.** ZET ships "no spec covers this,
  honestly" per-ticket into a repo with no unit tests; MET ships into repos where
  external review coverage is thin. Agent labor is the cheapest spec-backfill
  that exists and nothing tracks it. Not a gate (D-003's filler lesson) — a
  tracked Outcome line. → both packets.

**Also recorded, not packet material:** the standing `meta/architect.md` read-list
(logs and architecture only) would have prevented AF-1, AF-3's collection half,
and AF-7 from ever being found here — direct evidence for amending § Read at
review 001 to include delivery-side worklogs (not code). The untested core
assumption stands: nothing yet shows 364 net instruction lines in five days
outperform frozen founding files; `gates.py` CAUGHT counts at MET are the
cheapest falsifier built for that question. And the two teams' opposed bets —
redundant cognition vs instrumentation — are the live A/B; instrument the
comparison at review 001, do not converge it.

**Packets:** `proposals/2026-08-14-zesty-eng-team.md` (AF-1, AF-2, AF-3, AF-4,
AF-7) and `proposals/2026-08-14-mpulse-engage-team.md` (AF-3, AF-6, AF-7 — small
on purpose; its 001a accepts should run first). Written, not yet dispatched.
