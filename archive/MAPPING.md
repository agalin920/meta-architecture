# Mapping: where every pre-migration file now lives

Pre-migration state is tag `pre-colony-2026-10` (`8258888`). Nothing was deleted;
every original is under `archive/`, verbatim (moved with `git mv` or copied before rewrite).
`inbox/` is gitignored and was never tracked; it is untouched on Andres's machine.

| Pre-migration file | Where its content lives now |
|---|---|
| `.claude/settings.json` | Rewritten (ruling 9 + kernel locks). Original verbatim: archive/.claude/settings.json |
| `.gitignore` | Unchanged |
| `HANDOFF.md` | Rewritten as current state. Original verbatim: archive/HANDOFF.md |
| `README.md` | Rewritten. Original verbatim: archive/README.md |
| `charter.md` | Rewritten in place (locked). Original verbatim: archive/charter.md |
| `meta/architect-log.md` | Moved verbatim: archive/meta/architect-log.md. Every lesson, ruling and result: meta/record.md (cited by line) |
| `meta/architect.md` | Moved verbatim: archive/meta/architect.md. Replaced by meta/keeper.md |
| `meta/dispatch.md` | Moved verbatim: archive/meta/dispatch.md. Replaced by meta/keeper.md and dna/trials.md |
| `meta/thesis.md` | Rewritten with a dated falsifier. Original verbatim: archive/meta/thesis.md; its results in meta/record.md |
| `patterns/README.md` | Verbatim: archive/patterns/README.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/append-only-log.md` | Verbatim: archive/patterns/append-only-log.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/architect-on-cadence.md` | Verbatim: archive/patterns/architect-on-cadence.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/boot-ritual.md` | Verbatim: archive/patterns/boot-ritual.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/cadence-defence.md` | Verbatim: archive/patterns/cadence-defence.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/charter-as-constitution.md` | Verbatim: archive/patterns/charter-as-constitution.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/falsifiable-thesis.md` | Verbatim: archive/patterns/falsifiable-thesis.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/handoff-record.md` | Verbatim: archive/patterns/handoff-record.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/honest-metric.md` | Verbatim: archive/patterns/honest-metric.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/human-gate.md` | Verbatim: archive/patterns/human-gate.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/independent-adversary.md` | Verbatim: archive/patterns/independent-adversary.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/knowledge-vs-log.md` | Verbatim: archive/patterns/knowledge-vs-log.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/named-failure-modes.md` | Verbatim: archive/patterns/named-failure-modes.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/overhead-ceiling.md` | Verbatim: archive/patterns/overhead-ceiling.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/predict-then-check.md` | Verbatim: archive/patterns/predict-then-check.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/single-source-claims.md` | Verbatim: archive/patterns/single-source-claims.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `patterns/untrusted-input.md` | Verbatim: archive/patterns/untrusted-input.md. Restructured into dna/lessons/ (see dna/lessons/README.md for the old → new map) |
| `proposals/2026-08-13-mpulse-engage-team.md` | Moved verbatim: archive/proposals/2026-08-13-mpulse-engage-team.md |
| `proposals/2026-08-13-zesty-eng-team.md` | Moved verbatim: archive/proposals/2026-08-13-zesty-eng-team.md |
| `proposals/2026-08-14-mpulse-engage-team.md` | Moved verbatim: archive/proposals/2026-08-14-mpulse-engage-team.md |
| `proposals/2026-08-14-zesty-eng-team.md` | Moved verbatim: archive/proposals/2026-08-14-zesty-eng-team.md |
| `proposals/2026-08-15-mpulse-engage-team.md` | Moved verbatim: archive/proposals/2026-08-15-mpulse-engage-team.md |
| `proposals/2026-08-15-zesty-eng-team.md` | Moved verbatim: archive/proposals/2026-08-15-zesty-eng-team.md |
| `proposals/2026-08-22-brand-system.md` | Moved verbatim: archive/proposals/2026-08-22-brand-system.md |
| `spine.md` | Replaced by dna.md. Original verbatim: archive/spine.md |
| `systems.md` | Rewritten as a compact registry. Original verbatim: archive/systems.md |

## Completeness check

Run 2026-10-28: 35 files at `pre-colony-2026-10`; 35 found byte-identical at `archive/<path>` or unchanged at `<path>`; 0 not: none.
