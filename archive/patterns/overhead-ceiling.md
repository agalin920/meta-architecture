# Overhead ceiling

**Status:** `proven` — one strong implementation, one qualitative, one mechanical
**Invented in:** personal-university
**Partial in:** brand-system (qualitative, no number)
**Adopted, never fired:** mpulse-engage-team (2026-08-13)
**Missing from:** zesty-eng-team, mpulse-dpi-team

## The pattern

A **stated numeric ceiling** on how much of the system's time may be spent on
the system rather than the work — plus a standing rule that prunes:

> **If a schema field is never read by a decision, propose deleting it.**

## Why it works

Every logging system accretes. Each field is individually defensible at the
moment it is added, and nothing ever removes one. Without a ceiling the ritual
grows until it competes with the work, and the human quietly stops.

The pruning rule is the operative half. A ceiling with no mechanism is a wish;
"never read by a decision" is a test an Architect can actually run against the
logs.

## Evidence

- `personal-university/charter.md` and `agents/architect.md` — admin capped at
  ~10% of session time; *"If a schema field is never read by a decision, propose
  deleting it. If admin exceeds roughly 10% of session time, cut fields."* The
  README hands the student the trigger directly: *"If you find yourself doing
  more admin than those three fields, tell the Architect to cut fields."*
- **It fired.** The 2026-08-09 cut of the student's prediction was made on
  exactly this basis — the friction was real, the signal was already collected
  more cheaply by `friction_type`, and the field had not earned its cost. The
  ceiling is the reason that was a principled decision rather than a preference.
- `brand-system/agents/architect.md` — *"Time spent in `meta/` should be a
  rounding error next to time spent shipping."* Real but unquantified, and
  therefore arguable every time.
- **zesty-eng-team has none.** Its ticket worklogs, team log, decision log and
  knowledge files are all load-bearing today, but nothing bounds their growth
  and nothing licenses cutting a field.
- **mpulse-engage-team has both halves, mechanically, and neither has fired**
  (review 001a). The number is a **1,300-line cap on the per-ticket read path**,
  asserted in `.claude/agents/architect.md:105` and **checked by
  `tools/verify_docs.py`** rather than remembered. Its stated reasoning is the
  cleanest version of this pattern's argument anywhere in the portfolio: *"rule
  cost is paid per session and rule benefit is paid per incident, so a system
  that only adds is one that eventually nobody finishes reading. **If a retro's
  net additions would breach it, the retro must cut to fit.**"* The pruning half
  is `tools/gates.py --dead`, and the architect prompt says plainly that **before
  it existed, the instruction to cut rules that never fire was unimplementable.**
  **Neither has produced a datapoint:** the cap is 1,300 against a current 1,056,
  and `gates.py` reports 12 of 12 declared gates unrecorded.

**The gap between those two entries is the whole finding of review 001a.** ZET
has no ceiling and has retired zero applied rules across three retros. MET has a
ceiling that cannot bind and has retired zero across one. **Across 189 commits
and four retros in this portfolio, no applied rule has ever been removed** —
which is what this pattern's absence looks like from outside, and it is invisible
from inside either repo because each individual retro looks healthy.

## Adoption notes

Two parts, and the second matters more:

1. A number. Any defensible number; its job is to make the question askable.
2. The pruning test — *is this field ever read by a decision?* — assigned to the
   Architect on its cadence.

## How it fails

- **A ceiling with no mechanism.** Nobody measures percentage of session time
  directly; what actually enforces it is the pruning rule and the human's
  license to complain.
- **A ceiling measured over the wrong file set.** Added after review 001a's
  dispatch, because **this layer committed it while proposing the pattern.** It
  proposed capping zesty-eng-team at ~777 lines — a set that carries ~430 lines of
  slash commands **no ticket session opens** and **excludes every file that
  system's boot ritual mandates.** What a ticket session there actually reads is
  **1,474 lines**, grown ~+895 over the window, almost entirely in files outside
  the proposed cap: `team-log.md` 93→547, `knowledge/manager-ui.md` 54→336,
  `knowledge/product.md` 0→122. **The proposal would have bound the
  slowest-growing eighth of the problem.** Its Architect's rejection is the rule:
  **a ceiling that binds the wrong set is worse than none, because it licenses
  cutting the wrong thing.** Define the capped set as *what a session reads before
  it can start work*, enumerate it, and check it against the boot ritual — not
  against whatever directory the files happen to live in.
- **A ceiling set above the current value.** Added at review 001a. MET's cap is
  1,300 against a current 1,056, so it has never bound anything and cannot until
  it is lowered or the docs grow 244 lines. **A ceiling that has never bound is
  indistinguishable from no ceiling** and reads as one that is being respected.
  Set it at or just above where you actually are, not where you are comfortable.
- **Raising the number to make it pass.** MET names this itself, in the assertion
  comment: *"Raising the number to make this pass is the one move that defeats
  it."* A machine-checked ceiling converts the failure from forgetting into an
  explicit edit — which is the point, and also the exact line to watch in a diff.
- **Cutting rigour instead of admin.** The real risk. personal-university guards
  it with the anti-rigor tripwire, and its architect log entry for the 2026-08-09
  cut explicitly flags the second-order check: *one cut with this reasoning is
  discipline; a run of them is comfort drift.* Any system adopting a ceiling
  needs that counterweight.
