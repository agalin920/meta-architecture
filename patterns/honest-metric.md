# Honest metric

**Status:** `provisional`
**Invented in:** zesty-eng-team
**Missing from:** personal-university, brand-system

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

## Adoption notes

Three questions per metric:

1. What is the denominator, exactly?
2. Which datapoints did not test the thing, and are they named as excluded?
3. Could the system improve this number without improving?

## How it fails

- **Too many metrics.** Two with trends beats eight in a table.
- **Measuring the easy thing.** The chat-versus-GitHub problem is the general
  case: the honest denominator is usually harder to collect than the tidy one.
