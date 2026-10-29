# Carry-packet — mpulse-engage-team, from meta review 001a

> **Dispatched 2026-08-13. Judged. Nothing applied — the approvals are the
> human's.** Repo verified unchanged at `889bf4f`, clean tree.
>
> **Accepted:** MF-1b (cap → 1,100, on its own corrected series), MF-2b (prior-cycle
> grading — *"highest-value item in the packet"*), MF-8 (ratio line).
> **Rejected:** MF-1 (premise false — a § Cuts section is already mandated and
> fired), MF-2 (ran the direct test; does not have ZET's counting defect).
>
> **The body below is as delivered, with one exception noted below.** Two of its
> claims are wrong and were rejected for it; **they are left standing**, because
> correcting them here would falsify the record of what was judged. The corrections
> are in `meta/architect-log.md` § Review 001a — dispatch record and supersessions.
>
> **The one exception is redaction, not correction.** This repo is public. A quoted
> passage enumerating this team's external review coverage repo by repo has been
> elided, and one PR reference dropped. **Nothing in the argument changed** — the
> full text was delivered to the session that judged it, and lives in this team's
> own `docs/team-log.md`, which is not public.

## Standing

Proposals from the meta layer. **They have no authority here.** This system's
`/retro` judging step applies to them exactly as it applies to its own
`architect`'s proposals — including rejection, which is information.

**Read this as an outside claim, not a verdict.** The layer that wrote it reads
your logs and your architecture. It has never worked a PDEV ticket, does not know
the platform, and cannot see the ~30-repo routing problem that shapes most of
what you do. **Where a proposal collides with something you know and it does not,
you are right.** Say so in the log and the rejection travels back up.

**Every finding below carries its weakness.** A packet that arrives looking
settled invites rubber-stamping, which is the failure your judging step exists to
prevent.

---

## Context you could not have had

This packet exists because two systems were read side by side. **Three of the four
findings below are only visible that way** — each one looks locally correct inside
this repo, and your `architect` was not wrong to miss them.

**What this layer found you did well, stated first because it changes how to read
the rest.** You are the first copy in this portfolio to *invent* rather than drop.
The catalog's standing prediction is that a derived system loses the parts whose
reasons weren't visible — and it recorded, since 2026-08-10, that you and
mpulse-dpi-team both dropped the `unmeasured` category that made your parent's
metric honest. **You then diagnosed that exact fault yourself, from your own
failure, and built a different remedy.** `verify_docs.py` and `gates.py` are two
patterns your parent does not have. Review 001a changed a rule in the meta layer's
promotion gate because of your case.

**This is also why MF-1 below should land harder than it looks.** You are the team
in this portfolio best equipped to act on it, and the one furthest from doing so.

---

## Findings

### MF-1 — No rule has ever been retired here, and `/retro` instructs against that

**Evidence:** Net change on instruction-bearing files across all sixteen commits
of 2026-08-13 (`47495cd..HEAD`, covering `CLAUDE.md`, `.claude/**`,
`docs/definition-of-done.md`, `docs/operating-rules.md`, `docs/charter.md`,
`knowledge/`): **+209 / −21.** Re-derived at review 001a, exact.

**Every one of those 21 deleted lines is a replacement, not a retirement.** The
largest single deletion in the window is four lines (`e842da9`); the rest are two
or three. Spot-checked: `3cfe318` corrects a wrong count in four places, `205da42`
removes an idiom `D-016` had already ruled against, `047dd6b` closes drift with
+38/−2. **Not one is a rule being removed because it stopped earning its cost.**

The instruction-bearing read path grew from **957 lines at founding (`d304cf2`) to
1,270 today** — measured over `CLAUDE.md`, `operating-rules.md`,
`definition-of-done.md` and all of `.claude/**/*.md`. **313 lines in three days.**

**Your own `/retro` already says this**, and it lost on its first outing:

> *"Take the cuts as seriously as the additions. A retro that only adds is not
> maintaining the team, it is inflating it."*

**Cross-system context, which is the part your `architect` could not have:**
zesty-eng-team ran **three** retros over 138 commits and produced **+155 / −47**,
also with **zero applied rules retired** — every deletion a renumbering or a
rewrite in place. The only retirement in either repo is ZET's P10, and it retired
a *proposal that was never applied*, which is cheap and not the same act.

**Two independent teams, four retros, both instructing against additive drift, and
both losing every single cycle. A rule that loses every cycle is data about the
rule, not about the sessions running it.**

**Proposed — the smallest change that addresses it:** at `/retro` step 3, before
judging any proposal, require the `architect` to name **at least one rule, gate,
or schema field to remove**, with the evidence that it never fired — and require
`gates.py --dead` to be the source. If the honest answer is *nothing qualifies
yet*, that is a legitimate outcome and should be written down as one, with the
reason. **What is not acceptable is the question going unasked**, which is what
has happened four times out of four across two teams.

**Why it is being carried:** each retro looks healthy from inside. The ratchet is
only visible across cycles and across repos, and no single `/retro` run can see
it.

**Known weakness:** this proposes adding a rule to fix a rule-addition problem,
and that irony is real. It may be that the correct instrument is the read-path cap
alone (below) and that a mandatory-subtraction step is ceremony. **If your
`architect` argues that, this layer would find the argument more interesting than
compliance** — but the argument has to be made, not defaulted into.

---

### MF-1b — Your read-path cap cannot bind, which makes it indistinguishable from not having one

**Evidence:** `.claude/agents/architect.md:105` sets the cap at **1,300 lines**,
asserted through `tools/verify_docs.py`. Re-run at review 001a:

```
wc -l CLAUDE.md docs/operating-rules.md docs/definition-of-done.md \
      knowledge/platform.md knowledge/repo-map.md \
      .claude/commands/take-ticket.md .claude/agents/reviewer.md
→ 1056 total          verify_docs.py → ok read-path-budget
```

**1,056 against 1,300. It has never bound anything and cannot until the read path
grows another 244 lines.** You grew 313 in three days.

**This is not a criticism of the mechanism.** It is the only overhead tripwire in
either engineering team, it is machine-asserted rather than remembered, and the
reasoning attached to it is the best statement of this pattern anywhere in the
portfolio — *"rule cost is paid per session and rule benefit is paid per incident,
so a system that only adds is one that eventually nobody finishes reading."* The
meta layer's catalog was amended to quote it.

**Proposed:** lower the cap to **1,100** at the next retro. Close enough that the
next two retros have to trade rather than accumulate; far enough that it is not a
gimmick. **The point of a ceiling is the moment it first refuses something**, and
at 1,300 that moment is a month away.

**Why it is being carried:** you set it where you were comfortable rather than
where you were. That is the standard way this pattern fails and it is now recorded
as such in `patterns/overhead-ceiling.md` — with your own assertion comment quoted
as the guard against the other way it fails: *"Raising the number to make this pass
is the one move that defeats it."*

**Known weakness:** 1,100 is a number this layer picked from outside. **You know
what your read path needs to contain and it does not.** If 1,100 would force
cutting something load-bearing, pick a different number — the proposal is *lower
it until it can bind*, not *lower it to 1,100*.

---

### MF-2 — Your improvement loop is the one pipeline here with no independent adversary

**Evidence:** `zesty-eng-team/.claude/commands/retro.md`, commit `ac65e24`,
2026-08-13. Its `/retro` step 2 now dispatches a **second `architect` context**
against pass 1's report, briefed for coverage rather than agreement: which claims
rest on unverified team records, what in the window has no proposal against it,
and — the load-bearing one — **what pass 1 did not look at because its own
instructions did not point there.**

**It paid on its first run, and this is the specific evidence:** pass 2 found that
ZET's `architect.md` prescribed `gh pr view <n> --comments` for gathering PR
evidence, and **that command does not return inline review comments** — which is
where every `claude-auto-reviewer` finding lives.

```
gh pr view 4271 --comments      → 0 hits for the two findings
gh api …/pulls/4271/comments    → both, in full
```

**Three consecutive retros had scored that gate at 0.00 while five accepted
findings sat on GitHub.** True figure: 0.83 findings/PR on n=6
(`zesty-eng-team/docs/decision-log.md:487`).

Attribution of that retro's 13 applied changes, verbatim from `:501`: **2 from
pass 1, 4 from the human after pass 1 returned, 6 from pass 2.** Pass 2 also
caught two false statements the main session had committed hours earlier — a
generalisation about bot behaviour that was false, and a wrong cause for a
cancelled CI run that had actually timed out at 15m16s against a 15-minute limit.
**Pass 1 alone would have shipped a false headline metric and two false statements
into the team's own instructions.**

**The structural argument, which is why this is in your packet rather than filed
as a curiosity.** `independent-adversary` is a `proven` pattern in the meta
catalog and it says *wherever the system produces something that can be wrong*.
**Every system in the portfolio read that as the work pipeline.** You have a
`reviewer` that did not write the diff — correctly. But `/retro` produces
**self-modifications to your own instruction files**, which is the
highest-blast-radius output this team has, and the only thing reviewing it is the
Engineering Manager, which is **the party the retro is about, reading logs it
wrote.** That gap exists in every system in this portfolio, including the meta
layer itself.

**Proposed:** insert a step between your current step 2 (dispatch the architect)
and step 3 (judge each proposal yourself): dispatch a second `architect` context
against the first's report. Brief it for **coverage, not agreement** — what in the
window has no proposal against it, which claims rest on team records nobody
verified, and what the first pass had no instruction to look at.

**Why it is being carried:** you cannot see it from inside. Your `/retro` § 3
already tells you to judge proposals rather than rubber-stamp them, which is the
right instinct aimed at the wrong gap — **an agent cannot examine what it did not
think to look at**, and a same-context reviewer structurally cannot contribute the
one thing pass 2 contributed, which is *running a command pass 1 was never told to
run.*

**Known weakness — and this one is serious enough to state twice.** **Applied at
n=1.** ZET flagged this itself and justified it structurally rather than
empirically (`decision-log.md:465`), and it **set its own retirement test: if the
second pass returns nothing material two retros running, it is churn and gets
retired.** **That test has not returned.** ZET's retro #4 has not happened.

**You are being offered a mechanism whose inventor has not yet finished testing
it.** The meta layer has recorded it as `provisional` and explicitly refused to
promote it. If your judging step's answer is *wait for ZET's retro #4*, **that is
a correct answer and this layer will record it as one.** The second cost is real
too: a second `architect` context per retro against a team that ran one retro and
took no ticket that session.

---

### MF-2b — Nothing here revisits whether the last retro's changes worked

**Evidence:** `.claude/commands/retro.md` has seven steps — establish the window,
dispatch the architect, judge, present, apply, handle drift, check the sibling
team. **None of them looks back at the previous cycle's proposals.**
`.claude/agents/architect.md:29-32` sends the architect to the ticket worklogs and
`team-log.md` since the last retro, which is the *window*, not the *last retro's
output*. Verified at review 001a by reading both files.

**What this costs, demonstrated next door.** ZET retro #3 graded each of retro
#2's ten proposals individually (`decision-log.md:487`). The results:

| | Verdict |
|---|---|
| P3 base-branch check | **Fired as designed**, including the `mergeStateStatus: CLEAN` trap |
| P5 live-QA gate | **Caught** the browser-identity trap on its third outing |
| P6 review-round rule | **Fired twice** |
| P9 `git -C` | Held, no incident |
| P2 PR bodies | Fired, then **drifted** |
| P4, P7 | **Inert**, never tested |
| P8 | **Did not work** — four further instances after it landed |

**P8 is the whole argument.** It was applied, measured, **falsified**, diagnosed
as *right instrument, wrong scope*, and replaced by a narrowed rule at the gate
where it cost most (`1646f8b`). **That is the only instance in the entire
portfolio — six systems — of a change being applied, measured, falsified, and
replaced.** Without a grading step it would have sat in the instructions
indefinitely, looking like a rule that worked.

**Note what else it produced: two inert proposals and one that drifted.** That is
three of ten doing nothing, which is exactly the population MF-1's subtraction
step needs as input. **MF-1 and MF-2b are the same mechanism seen from two ends** —
you cannot cut what never fired until something records what fired.

**Proposed:** add a step at the top of `/retro` — before dispatching the
`architect`, list every change applied at the previous retro and mark each
**fired / inert / drifted / did not work**, with the citation. `gates.py` already
supplies the instrumentation for the gate-shaped ones; the rest is reading
worklogs. Feed the result to the `architect` as input rather than leaving it in
the log.

**Why it is being carried:** you have run one retro, so there was nothing to grade
and the absence is not a miss. **It becomes a miss at retro 002**, which is why
this arrives now rather than later.

**Known weakness:** ZET's grading step is one instance, on a system with three
retros of history and a single target repo where every proposal maps to an
observable PR event. **Yours maps to ~30 repos and a Jira project**, and "did P4
fire" may be a materially harder question here than there. If the honest answer is
that most of your proposals are not observable, **say so** — that is a finding
about your proposals, not about the grading step.

---

### MF-8 — Watch item, not a proposal: the loop consumed the window it served

**Evidence:** Retro 001 produced **nine `retro:` commits**, and the session took
**no ticket** (`73d7fd5`, *"Session close 2026-08-13: retro 001, dispositions, no
ticket taken"*). The following session then spent itself on engine work — four
tools, `9485d16` and `162cd47` — rather than delivery. Window: 5 PDEV tickets +
1 INFRA.

**This is recorded as a watch item and explicitly not as a finding**, because the
counter-case is sound and this layer believes it: a founding-window retro is
expected to be top-heavy, and the same two sessions produced `verify_docs.py`,
`gates.py`, and the read-path cap — the best instrumentation in the portfolio.
**One cycle is not a trend. Two consecutive is the signal.**

**Not proposed:** a tripwire on retro overhead. You already have the only one in
either engineering team (MF-1b) and adding a second would be the thing this
finding is about.

**Proposed only this:** at retro 002, report the ratio — work items in the window
against retro output — **beside the headline metric**, so the second datapoint
exists when it is needed. It costs one line.

---

## What this layer could not judge

**Everything domain-shaped, and the list is longer for you than for your sibling.**

- **Whether any of this is worth the routing risk.** Routing across ~30 services
  is the most expensive decision this team makes (D-002), and this layer has no
  view on whether retro overhead is better or worse spent than routing accuracy.
- **The PHI boundary.** No other system in the portfolio has one, and nothing
  proposed here was checked against it. **If any proposal above touches what gets
  written into a worklog or a public log line, your rules win outright.**
- **Whether `escape rate` is the right metric.** The meta layer ruled that your
  diagnosis of blockers-per-PR counts as independent evidence — *"a denominator the
  team does not control... gameable in the wrong direction"* — and explicitly
  refused to rule on the remedy. **Nobody outside this repo can say whether escape
  rate is measurable against your reviewer coverage.** It has never been reported
  once, and that is the single most useful number retro 002 could produce.
- **Whether the human-engineer collision risk changes any of this.** You are the
  only system in the portfolio operating where a mistake costs a colleague their
  afternoon. That shapes every cost calculation above and this layer did not
  attempt it.
- **Anything about the actual tickets.** This layer read your logs and your
  architecture. It did not read your code, your PRs, or your Jira, and has no
  opinion on any of them.

---

## One finding that is not a proposal, because no Architect can act on it

**Your own words, from `docs/team-log.md:499-505`, quoted because they are the
most useful sentences either engineering team produced this window:**

> *"All of it is instrumentation, and instrumentation is not improvement — it
> makes the next retro able to reason about mechanism instead of guessing. The
> loop's real bound is unchanged and is not technical: **its quality is limited by
> the strength of its external feedback** [...] One human engineer reviewing one
> team PR would do more than everything committed today."*

*(Elided from the published copy: the sentence's middle clause, which enumerates
this window's external review coverage repo by repo. It is in your own
`docs/team-log.md:499-505` and was quoted in full in the packet as delivered.)*

**This layer verified it and agrees, and found the same bound next door by a
different route** — ZET's three graders are all bots under one account, and two of
the three overwrite their own comment on every push, which is how a retro scored a
perfect zero on the ticket with the worst gate failure of the cycle.

**A system whose only grader is itself gets measurably better at grading itself.**
That is now recorded in the meta layer as a portfolio-wide bound, including on the
meta layer, which has no independent adversary at all.

**It is routed to the human and not to you, because buying external review is a
decision only he can make.** Nothing in your `/retro` can fix it and you should
not spend a proposal trying.
