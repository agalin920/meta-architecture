# Honest metric

**Status:** `provisional` — **two independent adopters, neither remedy measured**
**Invented in:** zesty-eng-team
**Independently re-derived in:** mpulse-engage-team (2026-08-13, review 001a)
**Missing from:** personal-university, brand-system

**Why it is still `provisional` at two independent adopters.** The independence
half of the bar is now met: mpulse-engage-team inherited this metric *with the
flaw*, diagnosed the fault from its own failure, and built a different remedy —
see `README.md` § The independence bar and copies that re-derive. **The other
half is not met.** Neither remedy has changed a measured number yet: ZET's
`retro-metric.py` is one day old and MET's escape rate has never been reported
once. **Two independent diagnoses of the same fault with two different remedies
is strong evidence the fault is real and no evidence that either remedy works.**

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
they converged on the *fault* and diverged on the *remedy* is why this is still
`provisional`.

## Adoption notes

Three questions per metric:

1. What is the denominator, exactly?
2. Which datapoints did not test the thing, and are they named as excluded?
3. Could the system improve this number without improving?

## How it fails

- **Too many metrics.** Two with trends beats eight in a table.
- **Measuring the easy thing.** The chat-versus-GitHub problem is the general
  case: the honest denominator is usually harder to collect than the tidy one.
