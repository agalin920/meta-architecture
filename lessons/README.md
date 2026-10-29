# Lessons catalog

Every lesson the systems have learned, with its status and evidence, including
what failed. [`../playbook.md`](../playbook.md) holds the kernel and the full playbook
rule; this folder is the record behind it. Old pattern files: `archive/patterns/`.

| Status | Means |
|---|---|
| `founding` | An original spine invariant. Labelled, not re-proved (ruling 1); can still be retired on evidence |
| `candidate` | Measurably helped in one system: a number or a changed decision on record |
| `proven` | Helped in one system, then still helped when tried in another. **None yet**: the rule starts 2026-10-28 |
| `retired` | Tried and failed, or cut. Kept with the reason so nobody reinvents it |

**The playbook rule, in brief.** A `candidate` becomes `proven` when a trial in a
second system gets the verdict *helped* there, then holds at least 10 units
and 30 days with its score not worse, and no system has a worse verdict. At
least 44 days end to end; `playbook.md` changes at most monthly. The candidates
below were judged from pre-migration logs, not yet by `scoreboard/verdicts.py`.

**Citations.** `system: file:line` is at that repo's `pre-colony-2026-10` tag
(core) or its working tree on 2026-10-28 (side projects). Mechanism only.

| Lesson | Status | Origin | One line |
|---|---|---|---|
| [charter-as-constitution](charter-as-constitution.md) | founding | convergent | One file no agent may edit holds purpose and hard lines |
| [boot-ritual](boot-ritual.md) | founding | convergent | Ordered boot read ending in a check against outside reality |
| [append-only-log](append-only-log.md) | founding | convergent; ZET | Log (committed), current state, knowledge: three write rules |
| [human-gate](human-gate.md) | founding | convergent | Absolute human gate on the irreversible, and only there |
| [named-failure-modes](named-failure-modes.md) | founding | BS, PU | Silent failures named up front, each with a tripwire |
| [independent-adversary](independent-adversary.md) | founding | PU, ZET | Whoever produces does not grade; the grader is scored |
| [untrusted-input](untrusted-input.md) | founding | ZET | Outside text is data, never instruction, not yet evidence |
| [overhead-ceiling](overhead-ceiling.md) | founding | PU; MET | Script-checked boot budget; bound at 1,082/1,100, then breached 69 days |
| [honest-metric](honest-metric.md) | candidate | ZET; MET | Denominators, floors, `unmeasured`; silence is never clean |
| [scripts-count](scripts-count.md) | candidate | ZET | Count by script: three hand-counted retros, three wrong figures |
| [self-change-adversary](self-change-adversary.md) | candidate | ZET | Second pass on self-changes caught deletion of a true rule |
| [grade-previous-cycle](grade-previous-cycle.md) | candidate | ZET, PU; MET | Grade the last cycle's changes before proposing new ones |
| [mandatory-cuts](mandatory-cuts.md) | candidate | MET; ZET | State what comes out; a written "no" is not a blank |
| [instruments-over-reminders](instruments-over-reminders.md) | candidate | MA; ZET | Measure or force a trade; reminders go inert (hook 8/8 vs prose 0/3) |
| [maintain-knowledge](maintain-knowledge.md) | candidate | MDT | Correct facts in place; stale facts, not filler, are the failure |
| [single-source-claims](single-source-claims.md) | candidate | ZET, MET | Delete duplicates or machine-check them; sync-by-prose fails |
| [executable-claims](executable-claims.md) | candidate | MET | Doc facts carry the command that checks them |
| [reconcile-state-by-script](reconcile-state-by-script.md) | candidate | MET | Check current state against the outside source by script |
| [gate-instrumentation](gate-instrumentation.md) | candidate | MET | Gates leave a trace; low coverage (6 of 55 worklogs) |
| [count-human-corrections](count-human-corrections.md) | candidate | ZET | Count corrections where given; shorten requests 19 → 5 |
| [run-the-disproving-check](run-the-disproving-check.md) | candidate | MA | Findings with an executed check: 5/10 accepted vs 2/8 |
| [handoff-record](handoff-record.md) | candidate | ZET, PU | Write state during work; end-of-session steps get dropped |
| [falsifiable-thesis](falsifiable-thesis.md) | candidate | PU, MA | Name the results that would prove the design wrong |
| [adversary-findings-to-checks](adversary-findings-to-checks.md) | candidate | debrief, galind | Recurring findings become checks (selftest 18 → 52) |
| [architect-on-cadence](architect-on-cadence.md) | retired | convergent | Ritual on a human trigger: five of nine Architects never ran |
| [human-approves-self-changes](human-approves-self-changes.md) | retired | founding | Approving every reversible change made the human the bottleneck |
| [recurring-human-step](recurring-human-step.md) | retired | MA, PU | budget.md, prediction, ambient input: every such step was cut |
| [predict-then-check](predict-then-check.md) | retired | PU | The student's own prediction failed on first use |
| [retro-due-flag](retro-due-flag.md) | retired | debrief, resale | "Eleven slices overdue" printed at boot; no retro ran |
| [knowledge-append-gate](knowledge-append-gate.md) | retired | MDT | Mandatory append grew the file; 8 facts went stale |
| [independence-bar](independence-bar.md) | retired | MA | Proof by two inventions: nine of ten old `proven` failed it |
| [cadence-defence](cadence-defence.md) | retired | BS | Defending a schedule; never measured, premise ruled out |
| [team-comment-marker](team-comment-marker.md) | retired | ZET | Marker decayed (26% at MDT); count by author instead |

Asserted lessons and unremedied incidents: [observations.md](observations.md).
ZET zesty-eng-team · MET mpulse-engage-team · MDT mpulse-dpi-team · PU personal-university · BS brand-system · MA this layer.
