# Single-source claims

**Status:** `provisional` — **two independent adopters on day one, held
deliberately.** See § Why this is not `proven` yet.
**Invented in:** zesty-eng-team and mpulse-engage-team, **independently, on
2026-08-18** — neither carried by this layer
**Recorded:** 2026-08-18

A claim duplicated across N files is a claim with N places to be wrong, and
every correction mechanism in these systems operates on **whichever copy it
happened to find.** Striking a claim where you found it is not striking it.

The remedy is one of two things, never a third:

1. **Delete the duplicate.** If the claim's real home is elsewhere, the copy is
   not a convenience, it is the mechanism by which the claim survives its own
   correction.
2. **Make agreement machine-checked.** Where duplication is deliberate — a
   preamble that genuinely must appear in four agent files — assert that the
   copies are identical, and assert it somewhere a routine run will execute.

**What is not a remedy: an instruction to keep them in sync.** Both origin
systems already had one, in prose, and both drifted anyway. That is the whole
finding.

## Why it works

These systems correct themselves by finding a wrong claim and fixing it. The
correction step has no way to know how many other copies exist, and the copies
are exactly where the claim keeps executing after everyone believes it is dead.
A struck claim living on in an agent preamble is not stale documentation — it is
**still being run**, by the agent, on the next ticket.

The asymmetry that makes this worth a pattern: writing a duplicate is one
keystroke and costs nothing at the moment of writing. Finding every duplicate
later requires knowing the phrasing you used, which is the one thing a session
correcting a claim months later does not have.

## Evidence

Two systems, same day, neither aware of the other, different remedies.

**zesty-eng-team — a struck claim kept executing and cost a thrown-out PR.**
`839508b` (2026-08-17) struck the *"token lacks `workflow` scope"* claim in
`CLAUDE.md` and `docs/operating-rules.md` and left it live in **eight more
places**: all four agent preambles, `docs/definition-of-done.md`,
`docs/workflow-improvements.md`, `docs/handoff/README.md`, and the Director's
escalation queue. The surviving copies were load-bearing. The claim became the
premise of a ticket plan's item 5 — *"Do not touch `.github/workflows/`"* —
which displaced one line of YAML into a 106-line repo script the Director
rejected outright. A concurrent session had pushed to `.github/workflows/`
successfully twenty minutes earlier, on the same token.

Its remedy, at `a2a4f6e`: a grep-every-copy rule added to `CLAUDE.md`, and
`docs/definition-of-done.md:85` **deleted rather than reworded** — who may
change CI is a permission that already lives in `operating-rules.md` § Standing
authorizations, so the DoD copy was pure duplication.

> **Check, executed 2026-08-18 in `../zestyio/zesty-eng-team`:**
> `git show a2a4f6e --stat` → 9 files, `9 insertions(+), 8 deletions(-)`;
> `docs/definition-of-done.md | 1 -`. The rule as committed reads: *"**When you
> strike a claim, `grep -rn` the phrase across this repo and fix every copy.**
> Striking it where you found it is not striking it."*

**mpulse-engage-team — a deliberate duplicate drifted and nothing was looking.**
The `TEAM-PREAMBLE` is duplicated across four agent files on purpose.
`architect.md`'s copy had lost the worklog clause the other three carry. Nothing
caught it, and the reason is precise: `/retro` §6 says to change all four
together, and says **nothing about verifying they agree when nothing changed
them.** An instruction covering the write path leaves the drift path unguarded.

Its remedy, at `c265813` (re-converge) and `0705c2d` (pin): a `verify_docs.py`
assertion, `team-preamble-copies-agree`, which shasums the marker-delimited
range in all four files and asserts one distinct hash.

> **Check, executed 2026-08-18 in `../mpulsemobile/mpulse-engage-team`:**
> `python3 tools/verify_docs.py` → `9/9 passed`, including
> `ok   team-preamble-copies-agree   .claude/agents/architect.md:115`. The
> assertion's own `why:` names the failure it was built from, and a second-order
> trap worth carrying: *"The range is anchored to the comment lines because this
> assertion's own cmd mentions both markers, and an unanchored sed matches its
> own text."*

**Both remedies changed an outcome.** ZET's correction pass found and fixed
eight live copies of a false claim. MET's assertion caught drift that two retros
had not noticed and now runs on every `verify_docs` invocation.

## Why this is not `proven` yet

**It clears the arithmetic bar on the day it was recorded** — two independent
adopters, neither derived from the other, neither carried by this layer, with
outcome evidence at both. It is being held at `provisional` anyway, and the
reason is written into `charter.md`: *the most persuasive thing that will ever
cross your desk is a fresh idea from a live project.* This one is a few hours
old at the time of recording, and both remedies are one commit deep.

**Its retirement test, named now so it cannot be set after the fact:** if
neither instrument catches a drifted or struck-but-surviving claim by the end of
the next full cycle at each origin system, this is prose that made everyone feel
careful. MET's assertion is the cheaper one to grade — it either fires or it
does not.

## Where it applies in this portfolio

**mpulse-dpi-team is the exposed case and has never run a retro.** Its
PHI-sanitizer fact — *nothing filters Jira output before you read it* — is
stated in `docs/operating-rules.md:13`, `docs/team-log.md:116`, `CLAUDE.md:53`
and `.claude/commands/take-ticket.md:17`, with three further command files
pointing at `operating-rules.md § PHI`. **The copies currently agree**, checked
2026-08-18. It is a safety-critical claim on a HIPAA platform, in four copies,
in the one engineering repo in the portfolio with **zero retro commits in its
entire history** (`git log --all --oneline | grep -ci retro` → `0`).

**This repo is exposed and, checked, is not currently drifted.** The three
adoption tests are stated in both `spine.md` and `patterns/README.md`; *"never
edit a child repo"* appears in `README.md`, `charter.md`, `HANDOFF.md`,
`meta/architect.md` and `meta/dispatch.md`. Diffed 2026-08-18: **the copies
agree in substance**; the variation is phrasing, not content. The exposure is
structural and unrealised, and saying so is more useful than inflating it.

**One realised instance here, found by applying this pattern to the catalog.**
The status reason *"neither remedy measured"* was stated in three places —
`patterns/honest-metric.md:3`, `:8`, and `patterns/README.md:148`. The
promotion edit of 2026-08-18 updated the header and left the body copy reading
*"is why this is still `provisional`"*. Caught in the same session, in the file
being edited to record this pattern. **N copies, one updated, on the first
try.**

## How it fails

- **Grepping for the phrasing you used, not the claim.** A claim restated in
  different words is invisible to `grep -rn`. Both remedies here catch verbatim
  copies; neither catches a paraphrase, and the paraphrase is the harder case.
- **Asserting agreement between copies that were always meant to differ.** A
  machine check on a range that legitimately varies per file produces a red
  build and a rule everyone learns to skip.
- **The assertion matching its own text.** MET hit this and anchored around it.
  Any check that names the thing it is checking is a candidate.
- **Treating it as a documentation-hygiene rule.** It is not. The cost at ZET
  was a rejected PR and a wasted ticket, because the surviving copies were in
  the agent preambles, where claims execute.
