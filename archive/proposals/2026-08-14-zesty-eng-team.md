# Carry-packet — zesty-eng-team, from meta advisory 2026-08-14

> **Dispatched 2026-08-14. Judged: 0 of 5 survive as proposed.** Repo verified
> untouched by the judging session. AF-1 and AF-3's evidence was misattributed or
> false against the artifact; AF-2 aimed at the wrong half of the file; AF-4 lost
> to an existing mechanism that fired and worked; AF-7's premise was false. The
> judging session also found live `Current state` drift the packet missed.
> **Body below is as delivered — the rejected premises stand so the record of
> what was judged stays true.** Corrections: `meta/architect-log.md` § Advisory
> 2026-08-14 — dispatch record.

## Standing

Proposals from the meta layer. **They have no authority here.** Your `/retro`
judging step applies to them exactly as to your own `architect`'s proposals —
including rejection, which is information. Where a proposal collides with
something you know and it does not, you are right; say so in the log.

**Provenance, honestly stated:** this packet comes from an off-cadence advisory
the Director commissioned, with a wider read than the meta layer normally gets —
including your ticket worklogs. Your Architect rejected 2 of 4 findings in the
last packet on evidence the meta layer had not gathered, and both rejections were
right. Judge this one the same way.

## Findings

### AF-1 — Your reviewer never reviews the plan's frame, and you have paid for that twice

**Evidence:** `.claude/agents/reviewer.md` starts its work order at
"1. Correctness" — verified 2026-08-14, no framing or unit-check language exists
anywhere in the file. Your sibling team added a **§ 0 — review the framing before
the implementation** after two review rounds confirmed a flawless implementation
of the wrong unit (their `reviewer.md` § 0, added 2026-08-11): is the *unit*
right, is this the defect or an instance of it, would the fix survive a rename.

Your own history carries the same failure class, named in your own log: the 08-09
postmortem — *"a design mismatch shipped past every gate"* — and #1358, where the
declining argument against a review observation was self-consistent and wrong,
which `docs/definition-of-done.md` § 5 now warns about. Both are plan-frame
errors, not implementation errors. Your reviewer receives the plan beside the
diff, so the plan's frame is the easiest thing in the review to accept without
noticing.

**Proposed:** adopt § 0 in your sibling's shape, adjusted for your domain: before
any line of code, two minutes on the plan itself — the unit question ("what class
does the special-cased thing belong to, and did anyone measure the class?"), the
defect-vs-instance question, and the hardcoded-coupling question. A wrong frame
is a **blocker** even when the implementation is flawless.

**Why carried:** invented next door three days ago; no channel would have brought
it here before the next quarterly review.

**Known weakness:** n=1 at its inventor, one window old, and its firing record is
one incident retrospectively. Cost is ~15 lines in `reviewer.md`, which is not on
any per-ticket read path a session boots.

### AF-2 — Your log-condensation rule has never fired, and nothing can make it fire

**Evidence:** `CLAUDE.md:90` assigns the architect to condense `docs/team-log.md`
at a retro "when the log grows unwieldy." It is prose with no trigger.
`team-log.md` went **93 → 547 lines** over the window; `knowledge/manager-ui.md`
54 → 336. Three retros have run and the instruction has fired zero times —
"unwieldy" is a judgment nobody is forced to make.

**Proposed:** give the condensation rule a number. Your Architect picks it — the
meta layer got burned proposing a specific figure for your repo last packet and
your rejection was correct. The shape that survives: a stated line ceiling on
`team-log.md` (current state + entries), checked at every retro, and **when
breached, the retro must condense before it appends** — same trade-forcing logic
as your sibling's read-path cap, aimed at the file set *you* identified as your
real growth (their rejection of the last ceiling proposal named `team-log.md` as
the actual gap, and this proposal is that rejection taken seriously).

**Known weakness:** the sibling's cap has never bound either, so this mechanism
has zero firing evidence anywhere. The counter-argument that condensation loses
decision-explaining context is real — your own rule already forbids deleting
anything that explains a decision, and the ceiling must inherit that.

### AF-3 — Your best metric cannot distinguish "no corrections" from "nobody wrote them down"

**Evidence:** `CLAUDE.md` mandates logging every Director correction under
`## Director findings`. Re-derived 2026-08-14: **4 of 10** real worklogs carry
the section; six have no heading at all. Either six tickets drew zero corrections
or the data was never collected — and `retro-metric.py`'s Director-findings count
cannot tell which. A metric whose gaps are ambiguous is the exact failure your
`unmeasured` category exists to prevent, one level up.

**Proposed:** an explicit line at worklog close — `## Director findings` with
entries, or the literal line "Director findings: none this ticket." Your
sibling's mandatory `## Outcome` (their commit `a138f1e`, backfilled across all
five worklogs) is the working precedent. Cost: one line per ticket.

**Second half, both teams:** the headline metric is severity-blind — a data-loss
escape and a comment-noise finding count as one unit each. You already classify
severity at review time; carry the classes into `retro-metric.py`'s report
(data-loss/security · correctness · convention) so the trend can distinguish the
escapes that matter.

**Known weakness:** none for the collection line beyond one line of ceremony. For
the buckets: n is tiny (a handful of external findings per window), so bucketed
trends will be noisy for several retros before they say anything.

### AF-4 — Your state is hand-written; your sibling derives theirs, and your failures are the argument

**Evidence:** your three costliest self-inflicted failures are stale self-authored
state: the `auth-state.json` blocker false for three retros, two of three
escalation-queue items already settled when checked, and a metric wrong three
times partly from destroyed source data. Your remedies so far are rules about
verifying (re-verify standing blockers; verify escalations against the world) —
all of which depend on a session remembering to run them. Your sibling built
`tools/state_check.py` (149 lines): `Current state` is **derived** from GitHub
and Jira at boot, not asserted. Verified 2026-08-14: your `tools/` has no
equivalent — `retro-metric.py` covers the metric only.

**Proposed:** a `state_check` for your world — open PRs, branch states, CI
verdicts, escalation-queue items — run at Orient, diffing `Current state` against
GitHub. You are GitHub-only, which makes this *simpler* to build here than it was
there. You already trusted a script over prose once (`retro-metric.py`, built
after three hand-counts failed); this is the same conclusion applied to state.

**Known weakness:** the sibling's tool is days old with no long-run record. And
derivation covers only machine-visible state — a blocker like "the Director must
mint a session" is not queryable, so the re-verify-or-strike rule stays
load-bearing for the remainder.

### AF-7 — You ship into a repo with no unit tests, and the team never leaves tests behind

**Evidence:** `docs/definition-of-done.md` opens with it: manager-ui CI is
Cypress-only, no unit tests exist anywhere. Your honest per-ticket line — "no
existing spec meaningfully covers this, and here is why" (#3909 is the recorded
right answer) — is correct each time and corrosive in aggregate: nothing
accumulates, and the team is the cheapest spec-writing labor the repo has ever
had.

**Proposed:** not a gate — a **tracked Outcome line**: "test surface delta on the
touched area," even when the delta is zero with a reason. The architect trends it
at retro. A gate would invite filler (the portfolio has a recorded failure mode
for exactly that); a trend line makes the aggregate visible so the Director can
decide if and when to spend tickets on it.

**Known weakness:** specs against a shared mutable dev instance are expensive and
flaky by your own records, so the marginal spec here costs more than in most
repos. If the honest trend is "zero, always, because the economics are wrong,"
that is a finding about the repo and belongs to the Director — the line still
earns its keep by making that case with data.

## What this layer could not judge

Whether any of this outranks a ticket. The cost of a spec against your shared dev
instance. Whether the Director wants `team-log.md` history condensed at all —
that file is partly written for him. And everything about the product.
