# Overhead ceiling (boot read-path budget)

**Status:** `founding`; the only one that survived review 001's audit.
Absorbs the 001a candidate `read-path-budget`.

**Lesson.** Cap, as a number checked by script, what a session must read before
it can work, and cut anything no decision reads. The cap forces the trade at
the moment of adding, because rule cost is paid every session and rule benefit
only per incident.

**Evidence**
- Survived the audit (engage re-derived it): `archive/meta/architect-log.md:3236`.
- **It bound once and changed a decision.** engage's 1,100-line cap held at
  1,082 (from 1,098); the cut that made room "paid for everything else", and
  the budget reversed a cut two passes had wanted:
  `archive/patterns/README.md:106-111`; `mpulse-engage-team: docs/decision-log.md:536`.
- **Then it was breached to 1,477 for 69 days**, from 2026-08-20; retro 003
  cut it to 1,030: `mpulse-engage-team: docs/team-log.md:5805`, `:5846`;
  `archive/meta/architect-log.md:3277-3283`.
- The pruning half fired at personal-university: `duration_min` was unknown in
  11 of 15 sessions and was deleted:
  `personal-university: meta/architect-log.md:1262-1272`.

**Where it failed / limits**
- **A tripwire whose remedy waits for a retro.** Every ticket from 08-20
  reported the breach and deferred it "for the retro":
  `mpulse-engage-team: docs/team-log.md:5808`. The kernel checks it by script
  and fixes it in the loop instead.
- **Set above the current value it never binds** (1,300 against 1,056):
  `archive/patterns/overhead-ceiling.md:89-93`.
- **Over the wrong file set it is worse than none.** This layer proposed
  capping ~777 lines while zesty-eng-team's real boot read was 1,474:
  `archive/patterns/overhead-ceiling.md:76-88`.
- **Raising the number to pass** is the one move that defeats it:
  `mpulse-engage-team: .claude/agents/architect.md:143`.
- **Cutting rigour instead of admin:** one cut is discipline, a run of them is
  comfort drift: `archive/patterns/overhead-ceiling.md:98-102`.

**Origin.** personal-university (~10% admin cap), 2026-08; re-derived at
mpulse-engage-team 2026-08-13. Kernel default: the boot budget.
