# Carry-packet — mpulse-engage-team, from meta architectural entry AR, 2026-08-15

## Standing
Proposals from the meta layer. **They have no authority here.** This system's
`/retro` judging step applies to them exactly as it applies to its own
architect's proposals — including rejection, which is information.

## Findings

### AR-1 — the retro's judge is the session being judged
**Class:** finding
**Evidence:** the Engineering Manager session holds five jobs — dispatcher,
judge, applier, metric reporter, and the party the retro is about. `/retro`
runs in that same working context; the architect proposes from a clean seat
but the judging and applying do not.
**Check run in the target repo:** `grep -ci "fresh session|cold session|new
session" .claude/commands/retro.md` → **0**. Nothing requires or even mentions
the retro running outside the working session.
**Proposed:** a step 0 in `retro.md`: the retro runs in a session that did
none of the window's work — boot fresh, read the logs, then judge. No new
agent, one rule.
**Why it is being carried:** the judge/judged coupling is invisible from
inside the session that has it. This is `independent-adversary` — already
adopted here for the work pipeline — applied to the improvement loop's
judging seat, which is the highest-blast-radius output this system produces.
**Known weakness:** n=0; nothing has yet been shown to go wrong because the
judge was warm. This team rejected MF-2 (a second adversarial pass) on a
measurement, and while this is not a second pass — it is a colder seat for
the existing one, at zero marginal agents — the family resemblance is real
and should be weighed, not waved off. Cost: one session boot per retro.

### AR-2 — the boot ritual is compliance where it could be property
**Class:** finding
**Evidence:** `preflight.py` exists because the review gate once failed open
and produced output shape-identical to passing. It runs only where prose
remembers to invoke it.
**Check run in the target repo:** invocation sites — `grep -rn preflight
.claude/commands/ CLAUDE.md` → `take-ticket.md:11` only. Hooks — `.claude/
hooks/` absent; `"hooks"` key in neither `settings.json` nor
`settings.local.json` (0 and 0).
**Proposed:** a SessionStart hook that runs `python3 tools/preflight.py`
(or a `--quick` subset the team chooses), failing visibly. Sessions that
begin without capability checks stop being possible, rather than being
against the rules.
**Why it is being carried:** this team proved the principle — its sibling
deny-list is the strongest form of `human-gate` in the portfolio precisely
because it does not depend on the agent complying. The boot ritual is the
same class of load-bearing rule still enforced by instruction.
**Known weakness:** per-session latency cost; hook behaviour under
non-interactive dispatched sessions is unverified (label: unverified); the
right preflight subset for a hook is this team's call, not this packet's.

### AR-3 — knowledge accumulates off every path that gets read
**Class:** finding
**Evidence:** knowledge only counts if a session that needs it will meet it.
**Check run in the target repo:** `ls knowledge/` → 7 files. The read-path
assertion (`architect.md:105`) carries 2 of them (`platform.md`,
`repo-map.md`). `knowledge/test-suites-that-can-drop-a-live-db.md` — written
after QA tables were actually dropped — is referenced exactly once outside
itself: `definition-of-done.md:118`, inside a parenthetical.
**Origin:** zesty-eng-team, whose `CLAUDE.md:18` already routes knowledge
conditionally (*"Read `knowledge/product.md` too before any ticket that
changes something a user sees"*). Carried in the inventor's shape per
`meta/dispatch.md` rule 5.
**Proposed:** a short routing manifest on the read path — condition → file —
e.g. *touching apollo results → `apollo-program-results.md`; deployment
ticket → `release-deployment-tickets.md`; anything reading env config →
`test-suites-that-can-drop-a-live-db.md`*. Knowledge then grows off-path and
loads on demand, which is the only shape where "knowledge grows and grows"
and the 1,100-line cap are both satisfiable.
**Known weakness:** the manifest itself costs read-path lines (~10) against
44 of headroom; manifests go stale — a `verify` block asserting every
`knowledge/*.md` has a manifest row would pin it, and this team owns that
convention.

## What this layer could not judge
Whether the preflight subset for a SessionStart hook should include the
GitHub/Jira reachability checks (network latency per session) or only the
local ones; and what the right manifest conditions are — both are
domain-operational calls.
