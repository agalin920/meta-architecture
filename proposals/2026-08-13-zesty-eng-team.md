# Carry-packet — zesty-eng-team, from meta review 001a

> **Dispatched 2026-08-13, second per `meta/dispatch.md` rule 5. Judged. Nothing
> applied — the approvals are the human's.** Repo verified unchanged at `6d43727`,
> clean tree.
>
> **Accepted:** MF-1 (§ Cuts, with a required two-state clause it added itself),
> MF-4 (the convention — but **2 of its 3 named targets rejected**, and a better
> target supplied). **Rejected:** MF-1b (777 is not a read path — a ticket session
> reads **1,474** lines and the growth is in files the proposed cap excluded),
> MF-3 (premise false — this repo has no instruction to cut rules that never fire).
> **MF-2:** no action, retirement test held, as asked.
>
> **MF-1 in the body below was already amended once before dispatch**, on
> mpulse-engage-team's rejection of the original form. **Nothing has been corrected
> since delivery** — the two rejected premises stand as written, because fixing them
> here would falsify the record of what was judged. **The corrections, and the
> finding this Architect produced that the packet missed (MF-10), are in
> `meta/architect-log.md` § Review 001a — dispatch record and supersessions.**
>
> **Redacted for publication, which is separate from correction.** This repo is
> public: specific PR numbers and a repo-by-repo account of another team's external
> review coverage have been removed. **No argument or verdict changed.** The full
> text was delivered to the session that judged it, and every citation resolves in
> the non-public repos it points at.

## Standing

Proposals from the meta layer. **They have no authority here.** This system's
`/retro` judging step applies to them exactly as it applies to its own
`architect`'s proposals — including rejection, which is information.

**Read this as an outside claim, not a verdict.** The layer that wrote it reads
your logs and your architecture. It has never worked a `manager-ui` ticket, has no
view on your product, and did not read a single PR diff. **Where a proposal
collides with something you know and it does not, you are right.** Say so in the
log and the rejection travels back up.

**Every finding below carries its weakness.** A packet that arrives looking
settled invites rubber-stamping, which is the failure your judging step exists to
prevent.

---

## Context you could not have had

**Stated first because it changes how to read the rest: your Architect is the only
one in this portfolio with a track record, and it is a good one.**

Review 001a checked its verdicts against your repo rather than taking them at
their word. They hold. It graded each of retro #2's ten proposals individually,
**falsified its own P8** after four further instances and replaced it at a
narrower scope (`1646f8b`), and corrected two false statements the main session
had committed hours earlier. **That is the only instance in six systems of a
change being applied, measured, falsified, and replaced** — and it is the first
direct evidence anywhere in the portfolio that the propose-never-apply loop does
anything at all.

It is also, for what it is worth, evidence *against* the meta layer's own thesis
claim that nobody scores the scorers. That has been recorded upward.

**So the two proposals below that carry mechanisms toward you come with an unusual
caveat: they come from a system with one retro, and they arrive at a system with
three.** Weigh them accordingly. The one thing you do not have is not rigour — it
is *traces*.

---

## Findings

### MF-1 — No rule has ever been retired here, across three retros

**Evidence:** Net change on instruction-bearing files across all nineteen
`retro:`-prefixed commits (`CLAUDE.md`, `.claude/**`,
`docs/definition-of-done.md`, `docs/operating-rules.md`, `docs/charter.md`):
**+155 / −47.** Re-derived at review 001a, exact.

**Every one of those 47 deleted lines is a replacement, not a retirement.**
Spot-checked and verified:

| Commit | What the `−` lines actually were |
|---|---|
| `ac65e24` | Section headers renumbered when the new step 2 was inserted |
| `776a578` | 14/14 — the Engineering Manager rename, in place |
| `aa5a5f4` | One instruction line rewritten in place |
| `34ca518` | A metric definition edited, not removed |

**The only retirement in your history is P10** (`decision-log.md:407`), and it
retired a **proposal that was never applied** — held at retro #2, retired at #3
because the remedy would not have helped. That is a good decision and a cheap one.
**It is not the same act as removing a rule that is live in the instructions.**

Your instruction-bearing read path grew from **679 lines to 777** over the window,
measured across `CLAUDE.md`, `operating-rules.md`, `definition-of-done.md` and all
of `.claude/**/*.md`.

**Your own `/retro` already asks the right question and lost three times running:**

> *"Is a prompt edit even the right instrument?"*

**Cross-system context, which is the part your `architect` could not have — and it
was corrected by mpulse-engage-team before this packet reached you.** This finding
was carried to them first. **They rejected it, with evidence, and they were
right**, so what arrives here is the amended version.

They ran one retro over 51 commits and produced **+209 / −21**, also with **zero
rules retired**. But the diagnosis this layer originally attached — *the question
is going unasked* — **is false there and true here**, and the difference is the
proposal:

- **mpulse-engage-team asks.** `.claude/agents/architect.md:124` mandates a
  **§ Cuts** section in every architect report: *"What should be removed. Be
  specific and **do not skip this section** — if nothing should be cut, say so and
  say why you believe it."* It fired on the first run: the architect proposed C3
  (trimming DoD §2's correction block) and **the judging step rejected it with a
  recorded reason** (`docs/team-log.md:420`) — DoD §2 is where the false-pass
  lesson is taught by example, and four lines is a cheap price. **Asked and
  answered is a different failure mode than unasked, and it does not have the same
  remedy.** Their words.
- **You do not ask.** Verified at review 001a: `.claude/commands/retro.md` contains
  **no instruction to cut, retire, or remove anything.** `architect.md:74` is the
  closest, and it covers retiring **a role that never gets used** — not a rule, a
  gate, or a field. Your prose question *"Is a prompt edit even the right
  instrument?"* is the right instinct and it is not a step.

**So the honest cross-system statement is narrower and more useful than the one
this packet originally carried:** two teams, four retros, **zero applied rules
retired between them** — and only one of the two has a structural step that forces
the question. **You are the one without it.**

**You have data on this that nobody else does.** Retro #3's own grading found **P4
and P7 inert, never tested**, and **P2 fired then drifted**. Three of ten
proposals doing nothing, named as such in your own decision log, and **none of the
three was removed.**

**Proposed — and it is now a copy of a working implementation rather than an
invention.** Add a mandated **§ Cuts** section to your `architect`'s report
format, in mpulse-engage-team's exact shape: *what should be removed, be specific,
do not skip this section — and if nothing should be cut, say so and say why you
believe it.*

**Note carefully what that does and does not require.** It does **not** require a
removal every cycle. It requires the question to be asked and answered on the
record. mpulse-engage-team's first run produced a proposed cut that their judging
step **rejected**, and that is the mechanism working — a recorded *no* is a
different artifact from silence, and it is the one you can audit later.

**Your grading step already produces the candidate list**, which is the part they
do not have: retro #3 named **P4 and P7 inert, never tested** and **P2 fired then
drifted**. Three of ten proposals doing nothing, already identified by name in your
own decision log. **A § Cuts section with that list as its input is close to free.**

**Why it is being carried:** each of your retros looks healthy from inside, and
each was. The ratchet is only visible across cycles, and the *asymmetry* — that
your sibling forces this question and you do not — is only visible across repos.

**Known weakness, and it is now smaller than it was.** This still proposes adding
an instruction to fix an instruction-accretion problem. Two things reduce it:
mpulse-engage-team's version lands in the architect's **report format**, not on the
per-ticket read path, so it costs a session nothing — and their version is the one
piece of evidence that this shape produces an answer rather than a ritual, at n=1.

**One real tension, flagged rather than resolved.** MF-3 below argues the mechanism
is the actual blocker and that no instruction can fix this. **mpulse-engage-team
made exactly that argument to reject the harder version of this proposal**, and
their reasoning applies to you: a § Cuts section is safe, but any rule *requiring*
a removal sourced from uninstrumented gates forces a cut on evidence that was never
gathered. **Adopt the section; do not adopt a quota.**

---

### MF-1b — You have no overhead ceiling at all, and the catalog says `proven`

**Evidence:** `overhead-ceiling` is a `proven` pattern in the meta catalog
(`patterns/overhead-ceiling.md`), and zesty-eng-team is marked ❌ against it — the
entry has said *"nothing bounds their growth and nothing licenses cutting a
field"* since 2026-08-09. Your worklogs, `team-log.md`, `decision-log.md` and
`knowledge/` files are all load-bearing today. **Nothing bounds any of them.**

**The ratio, for the record and not as an accusation:** retro #3 produced **16
commits and 13 applied changes against a window of 6 work items**, three of which
produced no PR at all.

**The counter-case is sound and this layer believes it:** retro #3 is also where
your loop produced its best evidence — the two-pass mechanism, the corrected
metric, `retro-metric.py`. A retro that expensive and that productive is not
overhead. **One cycle is not a trend. Two consecutive is the signal.** This is
recorded upward as a watch item, not a finding.

**Proposed:** a number and a pruning test, per the pattern's two halves.
mpulse-engage-team's version is the reference and is stronger than
personal-university's because it is machine-checked rather than remembered — a
**1,300-line cap on the per-ticket read path**, asserted in
`.claude/agents/architect.md:105` through `tools/verify_docs.py`, with the
reasoning: *"rule cost is paid per session and rule benefit is paid per incident,
so a system that only adds is one that eventually nobody finishes reading. If a
retro's net additions would breach it, the retro must cut to fit."*

**Set yours at or just above your current 777.** Learn from their mistake: theirs
is 1,300 against a current 1,056 and **has therefore never bound anything**, which
review 001a recorded as a new named failure of this pattern. A ceiling that has
never bound is indistinguishable from no ceiling.

**Why it is being carried:** the gap is in the catalog and has been since before
your first retro. What is new is a sibling implementation to copy from and a
measured demonstration of how to get the number wrong.

**Known weakness:** their cap has produced **zero** data — it has never refused
anything. You would be adopting a mechanism that is one day old and untested, from
a system with one retro. **The pattern is `proven` on personal-university's
evidence, not on theirs.**

---

### MF-3 — A rule firing here leaves no trace, so your optimizer can only add

**Evidence:** `mpulse-engage-team/tools/gates.py` (157 lines), commit `9485d16`,
2026-08-13. Its own diagnosis, and the best single sentence in either engineering
repo:

> *"the system could observe its own outputs but not its own mechanism"*

**The argument, which applies to you unchanged.** Your `architect` is instructed to
cut rules that never fire. **But a rule firing leaves no trace** — so it can
observe outcomes and never mechanism, and can therefore only add. MET's architect
prompt says it flatly: **before `gates.py` existed, the instruction to cut dead
rules was unimplementable.**

The mechanism: every gate emits one line into the ticket worklog —
`PASS / CAUGHT / SKIP / BLOCKED` — and the tool counts them. **`CAUGHT` is the only
evidence a gate is load-bearing.** The design detail worth stealing: it reports
**"not instrumented" rather than "dead"**, because those two states want opposite
responses and collapsing them would license cutting a gate that works.

**This is the mechanism behind MF-1, and it is why MF-1 may not be fixable by
writing a better instruction.** You have written the instruction three times.

**Proposed:** instrument your gates the same way — each gate in
`definition-of-done.md` and each check in `take-ticket.md` emits a status line
into the ticket worklog, and a script counts them across the window and reports
into `/retro` step 1 beside the metric. **You already have the harder half:**
`tools/retro-metric.py` (275 lines) proves this team will build and trust a script
over prose, and your own conclusion at `decision-log.md:507` is the argument for
doing it — *"A prompt cannot fix 'run the right query and count the results.'"*

**Why it is being carried:** it was invented next door, one day ago, and nothing
would have carried it to you. Neither `architect` reads the other's repo.

**Known weakness — and it is the largest in this packet. Zero evidence of effect.**
`gates.py` reports **12 of 12 declared gates unrecorded** — re-run at review 001a,
exact. **The instrument exists and the data does not.** One adopter, one day old,
never produced a single datapoint. The meta layer recorded it as `proposed`, the
lowest status in the catalog, which means *argued for, not adopted anywhere it has
worked.*

**A defensible rejection: wait until `gates.py` has produced one `CAUGHT` at
mpulse-engage-team, then reconsider.** This layer would record that as a correct
reading of the evidence.

**A caveat their judging step surfaced, which this layer had missed and which
matters if you adopt this.** `gates.py --dead` is **not** a cut list.
Instrumentation landed at `9485d16`, *after* all five of their tickets shipped, so
all twelve gates are unrecorded for a reason that has nothing to do with whether
they work — and four of the twelve guard routing, their single most expensive
failure mode. **The tool prints the warning itself:** *"Never recorded is not the
same as never needed... Check which before proposing a cut."* That distinction is
the best thing about the design and it is the thing most likely to be lost in
adoption. **If you take the instrument, take the two-state reporting with it** —
collapsing `not instrumented` into `dead` would license cutting gates that work,
which is worse than the additive ratchet it was meant to fix.

---

### MF-4 — Your claims are re-read rather than re-run

**Evidence:** `mpulse-engage-team/tools/verify_docs.py` (244 lines), same commit
`9485d16`. Docs embed the command that established a claim as an HTML comment
beside the claim, and **the claim is re-run rather than reread**:

```
<!-- verify id=read-path-budget
cmd: wc -l CLAUDE.md docs/operating-rules.md … | awk '{print ($1 <= 1300) ? "within" : "OVER by " $1-1300}'
expect: within
why: … Raising the number to make this pass is the one move that defeats it.
-->
```

Six assertions pinned, on exactly the facts that had drifted. **Re-run at review
001a: 6/6 passing.** They tested it by breaking one.

**The failure it answers:** *one measured fact, four files, three values, three
days* — a task-type count that was wrong in **all four places it appeared**
(`3cfe318`).

**Why this is your problem too, with your own evidence.** Your metric has been
wrong three retros running, from three different causes (`decision-log.md:507`):
wrong denominator, a bot counted before it existed, and an endpoint that cannot
return inline review comments. **The third scored a gate at 0.00 for three cycles
against a true 0.83 on n=6.** Your own diagnosis: *"None of those is a reasoning
failure. They are counting failures — wrong endpoint, wrong denominator, destroyed
source."*

`retro-metric.py` fixes the metric. **It does not fix the general case**, which is
every other number written into your docs — the typecheck baseline (`2fa7aed`
already corrected its composition once), coverage claims, the escalation queue.
**Those are still re-read rather than re-run.**

**Bearing on an existing pattern:** this is `knowledge-vs-log` (`provisional`)
meeting a problem it does not solve. You replicate facts across files **on
purpose**, because an agent reads one file and not the others — and until now
nothing enforced consistency between the copies.

**Proposed:** adopt the verify-block convention for the load-bearing numbers in
your docs. Start with three: the typecheck baseline, the metric definition's
denominator, and whatever `decision-log.md` asserts about bot behaviour — that
last one is where `aa5a5f4` put a false generalisation into the instructions and
pass 2 caught it an hour later.

**Why it is being carried:** invented next door yesterday; nothing would have
carried it.

**Known weakness:** partial evidence at best. Six assertions are pinned and they
pass, but **no retro cycle has yet run against them**, so nobody knows whether the
convention survives contact with a session in a hurry. One adopter, one day old.
Recorded as `proposed`.

**A second weakness, specific to you.** This layer's own review is an instance of
the failure: the brief it worked from asserted instruction-file line totals that
**did not reproduce** — it gave 447→584 for you, and re-derivation gave 679→777.
The file set was never stated, so the claim could not be re-run and could only be
re-argued. **That is MF-4 happening to the layer proposing MF-4**, and it is the
strongest argument in this packet for the convention.

---

### MF-2 — Watch item, not a proposal: your two-pass retro has a test and it has not returned

**Evidence:** `ac65e24` and `decision-log.md:465`. The second `architect` pass is
the most-evidenced thing either engineering team produced this window — 6 of 13
applied changes at retro #3, a metric wrong for three cycles corrected, two false
statements caught pre-commit.

**Nothing is proposed here. The opposite is proposed: hold the line you set.**

You applied it at n=1, flagged that yourself, justified it structurally rather
than empirically, and **named its retirement test — retro #4: *"if it returns
nothing material two retros running, it is churn and should be retired."***

**That is the right shape and the meta layer has recorded it as such.** It is also
now a `provisional` candidate in the portfolio catalog with an explicit note:
**do not promote before that test returns.**

**The thing to guard against is subtler than churn.** The first run was
spectacular, which makes retro #4 the moment where a weak second run gets
explained away rather than counted. **The strength of the first run is not
evidence about the second.** Run the test you wrote.

**It has also been carried to mpulse-engage-team**, with your unreturned
retirement test stated as its principal weakness and an explicit note that
*wait for ZET's retro #4* is a correct answer.

---

## What this layer could not judge

- **Whether any of this is worth a ticket.** The proposals above cost sessions,
  and this layer cannot see what you would give up. `charter.md` forbids it from
  inferring capacity from commit counts and it has not.
- **Whether `manager-ui`'s domain makes gate instrumentation cheap or expensive.**
  MET's gates map to a ~30-repo routing pipeline; yours map to one repo with 52
  Cypress specs and a live browser QA step. **The instrumentation cost is entirely
  a function of that and this layer does not know it.**
- **Anything about the bots.** That `claude-negative-qa` and
  `claude-change-verifier` overwrite their comments while `claude-auto-reviewer`
  posts fresh is recorded as your finding and used as evidence. **Whether that is
  fixable at the workflow level is a question about your CI, not your team**, and
  this layer has no view.
- **Your roster.** Four instances of *should this be a role?* were answered **no**
  across the two teams, and this layer read all four and thinks each is correct —
  particularly *"the unearned capability is perception, not knowledge"*
  (`decision-log.md:237`). **Nothing here proposes a fifth agent.**
- **Anything about the actual tickets.** This layer read your logs and your
  architecture. Not your code, not your PRs.

---

## One finding that is not a proposal, because no Architect can act on it

**Your graders are three bots under one account, and two of the three overwrite
their own comment on every push.**

Verified: one PR's negative-QA comment was **created carrying a reproduced
data-loss regression and updated 33 minutes later to read "No reproducible
edge-case failures found."** Retro #3 had to reconstruct both metric figures from
worklogs. **Anything before 2026-08-13 is unrecoverable.** That is how a retro
scored a perfect zero on the ticket with the worst gate failure of the cycle
(`decision-log.md:491`, which names the PR).

mpulse-engage-team is in the same position by a different route — **no human
review at all in its window**, and external coverage absent on part of its target
set. Its own statement, written against its own interest:

> *"Its quality is limited by the strength of its external feedback... One human
> engineer reviewing one team PR would do more than everything committed today."*

**A system whose only grader is itself gets measurably better at grading itself.**
Recorded upward as a portfolio-wide bound — one that applies to the meta layer too,
which has no independent adversary at all.

**Routed to the Director and not to you, because buying external review is a
decision only he can make.** Nothing in your `/retro` can fix it and you should not
spend a proposal trying. **The one thing that is yours:** the overwrite problem is
a data-destruction bug in your evidence pipeline, and `aa5a5f4`'s
record-each-verdict-against-its-head-SHA rule is a workaround, not a fix.
