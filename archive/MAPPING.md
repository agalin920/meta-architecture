# Mapping: where every pre-migration file now lives

Pre-migration state is tag `pre-colony-2026-10` (`8258888`). Nothing was deleted;
every original is under `archive/`, verbatim (moved with `git mv` or copied before rewrite).
`inbox/` is gitignored and was never tracked; it is untouched on Andres's machine.

| Pre-migration file | Where its content lives now |
|---|---|
| `.claude/settings.json` | Rewritten (ruling 9 + kernel locks). Original verbatim: archive/.claude/settings.json |
| `.gitignore` | Updated (archive path, `__pycache__/`). Original verbatim: archive/.gitignore.pre-colony |
| `HANDOFF.md` | Rewritten as current state. Original verbatim: archive/HANDOFF.md |
| `README.md` | Rewritten. Original verbatim: archive/README.md |
| `charter.md` | Rewritten in place (locked). Original verbatim: archive/charter.md |
| `meta/architect-log.md` | Moved verbatim: archive/meta/architect-log.md. Every lesson, ruling and result: meta/record.md (cited by line) |
| `meta/architect.md` | Moved verbatim: archive/meta/architect.md. Replaced by meta/keeper.md |
| `meta/dispatch.md` | Moved verbatim: archive/meta/dispatch.md. Replaced by meta/keeper.md and trials.md |
| `meta/thesis.md` | Rewritten with a dated falsifier. Original verbatim: archive/meta/thesis.md; its results in meta/record.md |
| `patterns/README.md` | Verbatim: archive/patterns/README.md. Now: lessons/README.md and independence-bar.md; its parked candidates went to self-change-adversary, grade-previous-cycle, gate-instrumentation, executable-claims, overhead-ceiling, knowledge-append-gate, maintain-knowledge, count-human-corrections, mandatory-cuts |
| `patterns/append-only-log.md` | Verbatim: archive/patterns/append-only-log.md. Now: lessons/append-only-log.md |
| `patterns/architect-on-cadence.md` | Verbatim: archive/patterns/architect-on-cadence.md. Now: lessons/architect-on-cadence.md (retired) |
| `patterns/boot-ritual.md` | Verbatim: archive/patterns/boot-ritual.md. Now: lessons/boot-ritual.md |
| `patterns/cadence-defence.md` | Verbatim: archive/patterns/cadence-defence.md. Now: lessons/cadence-defence.md (retired) |
| `patterns/charter-as-constitution.md` | Verbatim: archive/patterns/charter-as-constitution.md. Now: lessons/charter-as-constitution.md |
| `patterns/falsifiable-thesis.md` | Verbatim: archive/patterns/falsifiable-thesis.md. Now: lessons/falsifiable-thesis.md |
| `patterns/handoff-record.md` | Verbatim: archive/patterns/handoff-record.md. Now: lessons/handoff-record.md |
| `patterns/honest-metric.md` | Verbatim: archive/patterns/honest-metric.md. Now: lessons/honest-metric.md |
| `patterns/human-gate.md` | Verbatim: archive/patterns/human-gate.md. Now: lessons/human-gate.md |
| `patterns/independent-adversary.md` | Verbatim: archive/patterns/independent-adversary.md. Now: lessons/independent-adversary.md |
| `patterns/knowledge-vs-log.md` | Verbatim: archive/patterns/knowledge-vs-log.md. Now: lessons/append-only-log.md (merged) |
| `patterns/named-failure-modes.md` | Verbatim: archive/patterns/named-failure-modes.md. Now: lessons/named-failure-modes.md |
| `patterns/overhead-ceiling.md` | Verbatim: archive/patterns/overhead-ceiling.md. Now: lessons/overhead-ceiling.md |
| `patterns/predict-then-check.md` | Verbatim: archive/patterns/predict-then-check.md. Now: lessons/predict-then-check.md (retired) |
| `patterns/single-source-claims.md` | Verbatim: archive/patterns/single-source-claims.md. Now: lessons/single-source-claims.md |
| `patterns/untrusted-input.md` | Verbatim: archive/patterns/untrusted-input.md. Now: lessons/untrusted-input.md |
| `proposals/2026-08-13-mpulse-engage-team.md` | Moved verbatim: archive/proposals/2026-08-13-mpulse-engage-team.md |
| `proposals/2026-08-13-zesty-eng-team.md` | Moved verbatim: archive/proposals/2026-08-13-zesty-eng-team.md |
| `proposals/2026-08-14-mpulse-engage-team.md` | Moved verbatim: archive/proposals/2026-08-14-mpulse-engage-team.md |
| `proposals/2026-08-14-zesty-eng-team.md` | Moved verbatim: archive/proposals/2026-08-14-zesty-eng-team.md |
| `proposals/2026-08-15-mpulse-engage-team.md` | Moved verbatim: archive/proposals/2026-08-15-mpulse-engage-team.md |
| `proposals/2026-08-15-zesty-eng-team.md` | Moved verbatim: archive/proposals/2026-08-15-zesty-eng-team.md |
| `proposals/2026-08-22-brand-system.md` | Moved verbatim: archive/proposals/2026-08-22-brand-system.md |
| `spine.md` | Replaced by playbook.md. Original verbatim: archive/spine.md |
| `systems.md` | Rewritten as a compact registry. Original verbatim: archive/systems.md |

## Completeness check

Re-run 2026-10-29: 35 files at `pre-colony-2026-10`; 35 found byte-identical at `archive/<path>` (or `archive/.gitignore.pre-colony`) or unchanged at `<path>`; 0 not: none.
