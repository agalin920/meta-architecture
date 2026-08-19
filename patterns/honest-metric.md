# Honest metric

**Status:** `proven` — **promoted 2026-08-18. Two independent adopters, both
remedies measured, both changed a reported number.**
**Invented in:** zesty-eng-team
**Independently re-derived in:** mpulse-engage-team (2026-08-13, review 001a)
**Missing from:** personal-university, brand-system

**Superseded 2026-08-18.** This file previously read *"`provisional` — two
independent adopters, neither remedy measured"*, and explained that **two
independent diagnoses of the same fault with two different remedies is strong
evidence the fault is real and no evidence that either remedy works.** That
reasoning was correct and its condition has now been met. Both remedies ran in
the window 2026-08-15 → 08-18 and both changed a figure that had already been
reported. Evidence below, under § Promoted 2026-08-18.

**What the promotion does and does not do.** It moves this pattern into default
inheritance for systems grown after 2026-08-18. It does **not** retrofit into
any existing child, and it does **not** change `spine.md`, which already carries
the load-bearing half under § Where systems are expected to differ — *"what does
not vary is honesty about what is not being measured."* The spine wording was
checked against this promotion and needs no edit; recording that check is the
point, because a promotion that silently rewrites the spine is the churn
`patterns/README.md` warns about.

## The pattern

A small number of named metrics — **two, not a dashboard** — each reported with
its previous figure, and each with an explicit **`unmeasured`** category for
datapoints that did not actually test anything.

Excluded datapoints are reported as excluded, by name, so a silently smaller
denominator cannot flatter the trend.

## Why it works

The failure this prevents is specific and easy to miss: a metric that quietly
averages over cases where the mechanism never ran. It will improve while nothing
gets better, and the improvement is indistinguishable from the real thing.

Reporting the prior figure every time is what turns a number into a trend, and a
trend is the only form in which these numbers mean anything.

## Evidence

- `zesty-eng-team/.claude/agents/architect.md`, verbatim: *"**A PR based on
  anything other than `dev` gets no bots and no CI, so it is not a datapoint** —
  report it as unmeasured with its base branch named, and never let a stacked PR
  silently improve the average."*
- Second metric, and the subtler design: *"Director findings per ticket —
  counted **from wherever they said it**: a GitHub comment, or the working
  conversation as recorded under `## Director findings` in the ticket worklog.
  This team's Director reviews mostly in chat, so a GitHub-only count reads zero
  on tickets where they caught real defects."* The metric was designed around
  where the evidence actually lives rather than where it is easy to collect.
- Paired with an attribution mechanism: the team signs its own GitHub comments
  with `<!-- zesty-eng-team -->`, because it posts under the Director's account
  and *"without it the headline metric cannot separate what a reviewer raised
  from what the team said about itself, which quietly turns the number into
  self-assessment."*
- **The gaps.** personal-university tracks mastery and calibration but has no
  named unmeasured category — imported sessions 0001–0004 carry no engagement or
  friction data and the decision matrix correctly excludes them, but that
  exclusion lives in prose. brand-system's traction has the same exposure: a
  piece that was never actually distributed will average in alongside ones that
  were.

### Added at review 001a, 2026-08-13

**The instruction was not enough, in the system that invented it.** ZET ran
**three retros and reported three wrong figures, from three different causes**
(`docs/decision-log.md:507`): n=1 with no denominator discipline; a bot counted
before it existed; and `gh pr view --comments`, which **cannot return inline
review comments** — where every `claude-auto-reviewer` finding lives. That last
one **scored the gate 0.00 for three cycles against a true 0.83 on n=6.**

Its own diagnosis is the part worth carrying: *"None of those is a reasoning
failure. They are counting failures — wrong endpoint, wrong denominator,
destroyed source. **A prompt cannot fix 'run the right query and count the
results.'**"* Every prior retro had responded to a bad number by writing more
careful prose about deriving it, and the number stayed wrong.

The remedy is `tools/retro-metric.py` (275 lines): queries GitHub directly, uses
the correct endpoint per bot, and **refuses to report a clean zero for a bot that
edited its own comment in place** — it prints a floor and names the worklogs to
read instead. **`unmeasured` moved from instructed to enforced.**

**mpulse-engage-team arrived at the same fault by a different route and fixed it
differently.** Its headline was a low blockers-per-PR figure, published with three
caveats it says *matter more than the number*: the window's external review
coverage was incomplete across the target repos, the repo with the weakest
coverage produced the only blocker it did find, and nearly all of its non-blocking
findings carried a policy tag with the same finding repeated across PRs. Its
conclusion: blockers-per-PR *"has a denominator the team does not control... its
variance is dominated by who was looking, not by diff quality, and it is gameable
in the wrong direction — route work to unreviewed repos and it improves."* Its
remedy is coverage reported beside every count, D-019 excluding the release PR
from the denominator by name, and a move toward **escape rate** — caught by the
internal gate vs reached an external reviewer — *"because that is about the gate,
which is the thing being improved, and it does not move when a bot is switched
off."*

**Neither inherited the other's fix, and the two remedies are not the same
pattern.** One makes the count honest; the other changes what is counted. That
they converged on the *fault* and diverged on the *remedy* was the reason this
stayed `provisional` through 2026-08-18 — **and, once both remedies were
measured, the reason the promotion means anything: the fault is
remedy-independent.** See § Promoted 2026-08-18.

*(This paragraph ended `...is why this is still provisional` until 2026-08-18.
It was left behind by the promotion edit and caught in the same session that
recorded `single-source-claims`. Two copies of a status, one updated. The
pattern does not exempt the catalog.)*


### Promoted 2026-08-18 — both remedies measured, in the same window

Review 001a left exactly one condition for this pattern and named who had to
check it: *"Two independent diagnoses of the same fault, with two different
remedies, is strong evidence the fault is real and no evidence that either
remedy works. **That is what review 002 has to look for.**"* Both remedies were
exercised on 2026-08-18, independently, and each changed a number that had
already been published.

**zesty-eng-team — the instrument was wrong four ways and the discipline caught
it.** `tools/retro-metric.py --since 2026-08-14` returned **0.00 on n=1**, and
returned it silently: `team_prs()` filters on the `<!-- zesty-eng-team -->`
**body** marker, and #4275 — the window's largest PR at +972/−191 across 16
files — carries no such marker. Forcing the PR list gave 1.50/PR. A second pass
then found a third auto-reviewer finding that had landed after the first pass
ran. **Final: 2.00 per PR, reported as a FLOOR on n=2**, against 1.17 on n=6 at
retro #3. The published conclusion inverted — *flat* became *rising* — and the
`unmeasured` category grew a second condition it did not have: a PR **closed
unmerged** now flags, where #4279 had previously scored indistinguishable from
clean on a metric defined as findings per PR from reviewers the team does not
control.

> **Check, executed 2026-08-18 in `../zestyio/zesty-eng-team`:**
> `git log --oneline --follow -- tools/retro-metric.py` → **two commits only**,
> `404932e` (2026-08-13, the script) and `ca472bf` (2026-08-18, the four
> counting defects). `grep -n UNMEASURED tools/retro-metric.py` → **lines 168,
> 174, 291**; none present before `ca472bf`.

**mpulse-engage-team — the discipline applied to a boundary it could not
resolve.** Retro 002 reported **both** cuts of its headline and refused to pick
one: 1 blocker per 4 PRs opened in-window, or 5 per 5 counting `apollo#4981`,
whose review landed seven hours before the window opened. Neither is obviously
the honest cut, so both are on the record and the boundary rule is deferred to
retro 003. The window's context cost is written as a floor, `≥1,356,714` output
tokens, **with the reason for the floor stated** — subagent usage is absent from
the transcripts and this team delegates implementation by default. Its architect
argued for `≥1,482,595` on a different treatment of one straddling session;
**both figures are recorded and neither is called wrong.**

> **Check, executed 2026-08-18 in `../mpulsemobile/mpulse-engage-team`:**
> `.claude/commands/retro.md:49` carries the floor instruction with its own
> measurement (*"`isSidechain` is never true — measured 2026-08-14 across 17
> transcripts: 4,246 `false`, 1,914 absent, zero `true`"*) and requires the
> figure be written with a `≥`. `.claude/agents/architect.md:54` — *"A zero with
> no reviewer configured is not a zero. **Release PRs are excluded from the
> denominator** (D-019) and their blockers reported separately."*

**The two remedies stayed different, and that is the finding.** One makes the
count honest; the other changes what is counted and what gets reported alongside
it. Review 001a held this apart as the reason the pattern could not promote.
It is now the reason the promotion is worth something: **the fault is
remedy-independent.** Two systems that diagnosed the same fault built unlike
instruments, and both instruments produced a corrected public number rather
than a more careful paragraph about deriving one.

**What is still not evidence.** MET's preferred metric — escape rate — has now
been reported once, bucketed (14 CAUGHT: 7 blocker, 7 suggestion, 0 nit, 0
unspecified), but it still has no feed from defects surfacing *after* release.
The promotion rests on the `unmeasured`-and-floors discipline, which both
systems exercised, not on escape rate, which one system has reported once.

## Adoption notes

Three questions per metric:

1. What is the denominator, exactly?
2. Which datapoints did not test the thing, and are they named as excluded?
3. Could the system improve this number without improving?

## How it fails

- **Too many metrics.** Two with trends beats eight in a table.
- **Measuring the easy thing.** The chat-versus-GitHub problem is the general
  case: the honest denominator is usually harder to collect than the tidy one.
