# Intentional deviations from kit/

Read by `kit/tools/kit_drift.py`; anything listed here is reported as "declared".

- `.claude/hooks/kernel_guard.py`: the charter is `charter.md` at the root, not `docs/charter.md`. An `EDIT_ROOTS` rule refuses file edits outside this repo and the core systems, replacing a by-name list of product repos (this repo is public).
- `.claude/hooks/boot_check.py`: state file is `HANDOFF.md`; memory paths are this layer's; trials are `trials.md` here; score snapshots are not parsed for triggers (`DIRECTIONS = {}`), because this layer's measures are M1-M4.
- `.claude/agents/change-reviewer.md`: claims name M1-M4; adds a public-repo check (anything employer-internal is an ESCALATE, under hard line 1); escalations go to `HANDOFF.md`.
- `.claude/commands/what-changed.md`, `.claude/commands/evolve.md`: rewritten for this layer (cross-system answer; no `docs/loop.md` here, it uses `kit/docs/loop.md`).
- `scoreboard/score.py`: this layer's own measures (M1-M4), not the kit's S1-S4.
- Units are weekly reviews: `meta/keeper.md` § 0 writes `begin`, § 8 writes `unit` and `loop`.
