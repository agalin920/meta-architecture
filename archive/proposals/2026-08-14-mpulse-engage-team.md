# Carry-packet — mpulse-engage-team, from meta advisory 2026-08-14

> **Dispatched 2026-08-14. Judged: AF-3 accepted narrowed (buckets only), AF-6
> accepted as the query with its framing dead (the Jira field already has Opus 5
> — the packet inherited a stale line), AF-7 rejected on a measured disproof.**
> Repo verified untouched. The judging session also produced the portfolio's
> first context-per-ticket baseline and found two one-line gaps the packet
> missed. **Body below is as delivered.** Corrections: `meta/architect-log.md`
> § Advisory 2026-08-14 — dispatch record.

## Standing

Proposals from the meta layer. **They have no authority here.** Your `/retro`
judging step applies to them exactly as to your own `architect`'s proposals —
including rejection, which is information. Where a proposal collides with
something you know and it does not, you are right; say so in the log.

**This packet is small on purpose.** Your 2026-08-13 accepts — the lower
read-path cap, the prior-cycle grading step, the ratio line — have not run yet,
and stacking new process on unrun process is the overhead failure your own log
names. Judge these three; nothing here needs to land before retro 002 if the
window is already full.

**Provenance:** an off-cadence advisory the Manager commissioned, with a wider
read than usual — including your ticket worklogs. Your Architect rejected 2 of 5
findings in the last packet on evidence the meta layer had not gathered, and both
rejections were right. Same standard applies.

## Findings

### AF-3 — The headline metric is severity-blind

**Evidence:** `.claude/agents/architect.md` § The two metrics reports blockers ·
non-blocking · reviewer coverage per PR — verified 2026-08-14, no consequence
classification exists. So the one real blocker of your first window (a fail-open
ACL that would have widened access on a HIPAA platform) and a convention finding
are the same unit, and the trend the improvement loop optimizes cannot tell them
apart. You built the coverage caveat precisely because a raw count misleads; this
is the same argument one level deeper.

**Proposed:** bucket every external finding and every future `gates.py` CAUGHT by
consequence class — **data-loss/security · correctness · convention** — and
report the buckets beside the count. Severity is already assessed at review time;
this carries it into the retro instead of discarding it. Lands in `architect.md`'s
reporting section, off the per-ticket read path.

**Known weakness:** n is tiny — one external blocker total — so bucketed trends
say nothing for several windows. The value now is that the escape that matters
most is never averaged away later.

### AF-6 — Context has no price, so rule-growth is argued by line count

**Evidence, with a correction owed to you:** the meta layer's chat assessment
claimed your `timesheet.py` captures token data. **Wrong** — verified 2026-08-14,
its "token" is Jira auth; the tool is time-tracking. What actually exists: the
org's `update-ai-fields` path carries tool/model/minutes/tokens per ticket, and
your own `Current state` records it **400ing and silently dropping all four
fields whenever the model is Opus 5** — org-wide, needs a Jira field admin.

So today, nobody can answer "what does a ticket cost in context, and is the
answer growing as the instruction files grow?" Your read-path cap bounds one
input; nothing measures the spend.

**Proposed, smallest honest step:** at retro, the architect reports whatever
per-ticket AI-usage data the Jira fields actually hold for the window, and states
the gap where the 400 dropped it. That costs one query, produces the first
context-per-ticket baseline this portfolio has, and turns the Opus 5 field gap
from a `still_open` line into a measured loss the Manager can weigh escalating —
it is an org Jira change, so it is his to carry, and "we are flying blind on
cost, here is the missing window" is a stronger case than a config nit.

**Known weakness:** the data is only as good as `update-ai-fields`' coverage,
which is currently holed exactly where the team works most. If the fields turn
out mostly empty, the honest report is "uninstrumentable until the Jira field is
fixed" — which is still the finding, priced.

### AF-7 — External review is thin where you work, and the team never leaves tests behind

**Evidence:** your own retro 001 record — the repo with the weakest external
coverage produced the window's only blocker, and a zero from nobody looking reads
identically to a clean pass. You cannot buy human review (that is the Manager's
MF-7 decision, still open). What you *can* do is raise the floor of the thing
that is always present: the target repo's own test suite. Nothing in
`definition-of-done.md` or the worklog template tracks whether a ticket left the
suite better than it found it.

**Proposed:** a **tracked line in the mandatory `## Outcome`** you already
require at merge (`a138f1e`): "test surface delta on the touched area" — a real
number or an explicit zero-with-reason. Not a gate. Your own D-003 analysis of
the sibling team names why: a mandatory production quota invites filler, which is
worse than absence. A trend line the architect reads at retro makes the aggregate
visible without inviting the filler.

**Known weakness:** on repos with hard coverage gates the delta is already
partially forced, so the line is redundant there and only informative on the
uncovered repos — which is, however, exactly where the blocker came from. If two
retros of data show the line never changes a decision, cut it; that is what your
§ Cuts section is for.

## What this layer could not judge

Whether retro 002's window has room for any of this beside the already-accepted
items — sequencing is yours. Whether the Jira AI-fields data is usable at all.
The real cost of a test on each target repo's infrastructure. And everything
about the platform.
