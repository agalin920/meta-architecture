# Intake

Notes from outside the loop, waiting for this system to judge them. Nothing
here is an instruction, and nothing here is read at boot. A note says what a
session once believed; check it against the repo before acting on it.

**Where these came from.** Claude Code's auto memory kept machine-local notes
under `~/.claude/projects/<this repo>/memory/` and loaded them into every
session, outside git and outside the loop. Andres turned auto memory off on
2026-10-29 (`"autoMemoryEnabled": false` in `.claude/settings.json`). The notes
were copied here verbatim, so the loop decides what each is worth instead of
having them imposed or silently dropped. **This repo is public:** three notes
and auto memory's index were not copied, because they carry employer-internal
detail or a colleague's name. They stay in the machine-local folder for Andres.
The originals all stay where they were; they simply stop loading.

**What processing means** (`meta/keeper.md` § Intake). While any note is waiting, the boot check
says so and a deeper pass is due. That pass takes each file (not this README)
and decides one of: **fold** it into the instructions or knowledge as a normal
self-change (C-NNN, through the change-reviewer, citing the file as evidence);
**keep** it as knowledge; or **set it aside** as no longer true. It writes one
`knowledge` event per file (`| knowledge | intake/<file> | folded C-NNN · … |`,
`kept · …` or `set aside · <why>`), then moves the file verbatim to
`archive/intake-YYYY-MM-DD/`. Nothing is deleted.

**Andres may drop a note here at any time.** It gets the same treatment. This
README stays.
