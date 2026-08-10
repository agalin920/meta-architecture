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
