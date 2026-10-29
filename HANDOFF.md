# Handoff — state of play

Snapshot for whoever picks this up cold. Rewritten in place, never appended to.

**This layer gets the cold-start half of the handoff pattern and not the
write-during-work half.** A quarterly review runs in one sitting and its output
*is* `meta/architect-log.md`, so there is no mid-work state to lose. Do not add
phase-boundary writes here — that would be the ceremony `charter.md` names as a
failure mode.

---

## Current

```yaml
status:      REVIEW 001 RAN 2026-10-28, 76 days late, all eleven repos. Its
             rulings are PENDING WITH THE HUMAN — read § Awaiting a ruling
             before doing anything else
last_review: 001 (full, 2026-10-28). 001a was scoped (08-13). The 08-14
             rulings, 08-15 AR proposals, 08-18 scoped read and the four
             birth entries are entries, not reviews
next_review: 002 — quarterly, so not before 2027-01. Earlier only on the
             human's flag. Its agenda is § Watching in the 001 entry
proven:      AUDITED. 9 of the 10 pre-bar `proven` patterns fail the
             independence bar; overhead-ceiling and honest-metric pass. The
             demotion is PROPOSED (M-1), not applied, because the sentence it
             conflicts with is in charter.md
promotions:  1 (honest-metric, 08-18). Births: 4, none since 08-29. Zero
             births have run a first retro
dispatched:  nothing since 2026-08-15. No packet drafted at 001, on purpose
pending:     proposals/2026-08-22-brand-system.md — HOLD until brand-system's
             status is ruled. galind.io still has no A record (checked 10-28)
```

## Read this first: what review 001 found

1. **No birth can ever be an independent adopter of a spine invariant.** A
   system grown from `spine.md` *inherits* the invariants; that is the spine
   working, not anyone arriving at them again. So the founding patterns can only
   reach `proven` through a copy's documented re-derivation or a system built
   without the spine. **The more the generative clock grows, the fewer
   independent tests of the spine exist.** Neither the thesis nor the charter says
   this yet.
2. **Every self-directed system stopped; every employer-driven one kept going.**
   91% of 984 window commits are zesty-eng-team and mpulse-engage-team.
   brand-system, personal-university, galind-team, resale-desk, the-debrief and
   zesty-webengine-team are all quiet 22–73 days. **Do not read that as neglect**
   — it is item 2 below, for the human.
3. **`git log` misread four systems.** Uncommitted state at the-debrief (46
   files), resale-desk (charter + 109 events), galind-team (ticket 001 + an
   uncommitted product repo), brand-system (8 files, 3 commits never pushed).
   **Read `git status` as well, every review** (M-3).
4. **Defining when a retro is due did not make one run, anywhere.** The-debrief
   printed *"eleven slices overdue"* in its boot-read state and kept working.
   `/retro` is human-invoked in every system, so the retro clock is the human's
   attention clock. Engage's new RETRO DUE line (`carried`) is the same mechanism
   — **expect it to print and not fire.**
5. **Claim IV is done.** Seventh consecutive hit. What § 3 still catches that no
   self-audit can: **five of nine Architects have never run.**

## Awaiting a ruling — the 001 entry, § For the human's ruling

1. **M-1**: the `founding` status, and one clause in `charter.md` § The promotion
   gate. Until ruled, **the matrix still says `proven` for nine patterns that
   fail the bar** — do not cite those statuses as evidence.
2. **Dormant or dead** for the six quiet systems, each with a revisit date if
   dormant. `systems.md` marks them `active — stopped, unruled` meanwhile.
3. **The uncommitted work** in four systems. Never touch it from here.
4. **zesty-webengine-team**: handed over and running elsewhere, or never picked
   up.
5. **What the parent briefs of the 2026-10-28 retros carried**, so nothing
   carried is later counted as independent.
6. **M-2, M-3, M-4, M-5** — this layer's own files; proposed, not applied.

## What this layer is

**Two jobs, two clocks.** Generative, on demand: systems are grown from
`spine.md`, read as a resource. Evolutionary, quarterly: proven divergence is
carried back. **Divergence is cheap and local; convergence is expensive and
deliberate.**

## What exists

Eleven repos under `~/dev/`: ten systems and this layer. Four births, all grown
from the spine (08-19, 08-22, 08-24, 08-29); the last two were grown from inside
this layer, so their agreement with any sibling is `carried`. Two copies of
zesty-eng-team (`†`). **Three systems have no remote** — galind-team, the-debrief,
resale-desk — and creating one is the human's call; resale-desk has its own
reason not to. `personal-university` and `meta-architecture` are public on
purpose. `~/dev/living-universe` is a human project, not a system, correctly
unregistered.

## Open

Renumbered 2026-10-28. Closed items keep their evidence.

1. ~~**The `proven` re-audit.**~~ **Done at 001** — result in § 0 of that entry;
   application awaits M-1.
2. **brand-system's README is stale** — `README.md:38`, 80 days. Its Architect has
   never run, so nothing local will catch it.
3. **The feedback instruments are still unbuilt.** MET reports an escape rate on
   6 of 80 PRs; nothing anywhere measures what escapes the human after release.
4. ~~**`carried` re-audit.**~~ **Done at 001**, together with item 1. It added a
   fourth route, *inherited*.
5. ~~**mpulse-dpi-team has never run a retro.**~~ **Closed 2026-10-28** — retro 1
   ran, `0a4f4af`. Its knowledge-gate candidate is graded: filler under 1%,
   staleness the real failure, gate changed from append to maintain.
6. **`single-source-claims`** survived its first test at MET (an instrument fired
   on a drifted claim). One cycle; keep `provisional`.
7. **Claim III** — the trend reversed. 001 had five of seven findings out of
   local reach, against two of six at the 08-18 scoped read.
8. **Claim IV** — acted on in M-2, pending.
9. ~~Permission guard~~, ~~seven pending items~~, ~~MDT wake-up item~~,
   ~~dispatch silence~~ — closed earlier; evidence in the log.
10. **The brand-system packet** is held, not withdrawn.

## Decisions that constrain the next session

- **`budget.md` was cut on 2026-08-09**, unfilled. It asked the human to state and
  maintain weekly capacity; he declined. The free half survives — observed
  distribution from `git log`. **Do not reintroduce a stated budget, and do not
  infer capacity from commit counts.**
- **Both public repos are public on purpose.** Decided by the human on
  2026-08-10: `personal-university` and `meta-architecture` stay public. The
  exposure was named at the time of the decision and accepted — this repo lists
  five private systems by name, domain, and cadence, and `systems.md` goes
  further. **This is settled; do not re-open it as a check.** If the calculus
  changes it is a new decision, made the same way.
- **Do not reintroduce a kill condition.** Removed deliberately on 2026-08-10
  with reasoning recorded in two places. If a future review concludes the layer
  is decoration, that is a finding for the human, not a self-executing clause.
- **`spine.md` stays a resource.** Do not turn it into a scaffold command, a
  checklist, or an instantiation procedure. The reasoning — that a procedure pins
  the framework to the capabilities of whatever wrote it — is in `charter.md` and
  `meta/thesis.md` claim I.
- **This is the second mechanism cut for costing the human a recurring step**,
  after the student prediction in personal-university. Both cuts were correct on
  their merits. **The Meta-Architect is the only thing positioned to see a *run*
  of these** — one cut is discipline, a pattern of them is comfort drift with
  better prose. **n=3 as of review 001**: personal-university retired ambient input on 2026-08-20 because the student will not do the step it depended on (`02b2aa7`). Raised in the 001 entry as an observation, not a proposal. Each cut is still correct on its merits.
- **Never edit a child repo.** Findings go to that system's Architect and the
  human carries them. F2 and F3 were applied this way and it worked. This applies
  to spine changes: a promoted pattern changes what *future* systems inherit and
  does not retrofit itself into existing ones.

- **Never carry domain content across companies.** Review 001 read the Zesty and
  mPulse retros side by side and wrote only mechanism. Keep it that way.

## Next action

**Nothing until the human rules on the five items above.** Then apply what he
approves to this layer's own files, refresh the matrix, and stop. **Review 002 is
quarterly**; a scoped read of the two busy repos before it is the failure mode
the old cadence warning named, and the warning still stands.

```bash
claude "Read HANDOFF.md, apply the rulings recorded for review 001, and stop."
```
