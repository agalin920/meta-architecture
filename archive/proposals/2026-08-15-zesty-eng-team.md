# Carry-packet — zesty-eng-team, from meta architectural entry AR, 2026-08-15

## Standing
Proposals from the meta layer. **They have no authority here.** This system's
`/retro` judging step applies to them exactly as it applies to its own
architect's proposals — including rejection, which is information.

## Findings

### AR-1 — the retro's judge is the session being judged
**Class:** finding
**Evidence:** the working session dispatches the architect, judges its
proposals, applies the accepted ones, and is itself the subject of the
retro. `retro.md` names the review conflict and answers it with a second
adversarial pass (`ac65e24`) — which audits **pass 1's report**, not the
judging seat: the warm working context still judges and applies both passes'
output.
**Check run in the target repo:** `grep -ci "fresh session|cold session|new
session" .claude/commands/retro.md` → **0**. Nothing requires the retro to
run outside the session whose window it grades.
**Proposed:** a step 0 in `retro.md`: the retro runs in a session that did
none of the window's work — boot fresh, read the logs, then judge.
**Why it is being carried:** the judge/judged coupling is invisible from
inside the session that has it; this is `independent-adversary` applied to
the one place it is still missing. This team's pass-2 mechanism is the
strongest improvement-loop adversary in the portfolio, and it still reports
to a judge who spent the window inside the work.
**Known weakness:** n=0 — no recorded failure is yet attributable to a warm
judge, and this team's pass 2 may already catch the class of error a cold
seat would. Its retirement test (retro #4) has not returned; judging this
proposal alongside that result is reasonable. Cost: one session boot per
retro.

## Not carried, and why
- **AR-2 (SessionStart hook):** this repo has no preflight script to hook;
  building one is this team's call if it wants the property, not a carry.
- **AR-3 (knowledge routing):** not carried because this team is its origin —
  `CLAUDE.md:18` already routes knowledge conditionally. Cited to
  mpulse-engage-team as the inventor's shape.

## What this layer could not judge
Whether pass 2's coverage already subsumes the cold-seat benefit — only this
team's retro #4 result can say.
