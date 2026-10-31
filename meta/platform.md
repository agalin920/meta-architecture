# Platform watch

What Claude Code itself can do, read every week by the lessons review
(`keeper.md` § 7). Mechanism only: this repo is public.

**Last read:** 2.1.312, on 2026-10-30, the version running at kit 2.4.

## Building blocks in use (kit 2.4)

- **Hooks:** SessionStart (boot check), UserPromptSubmit (prompt log),
  UserPromptExpansion (commands typed), PreToolUse (guard), PostToolUse (spawns
  and skills), Stop (stop check), SessionEnd (live marker).
- **Body:** CLAUDE.md, skills, commands, subagents with a `model:` line,
  `tools/` scripts.
- **Frame:** settings allow, ask and deny rules, `.mcp.json` and
  `~/.claude.json` connectors (locked), declared scheduled tasks (locked).

## Found

Newest first: the date, the version, the building block, and what was done
(trial, proposal, system-level line, or nothing, and why).

- 2026-10-30 · 2.1.312 · `claude mcp add` writes `~/.claude.json` without
  naming `.mcp.json` · it bypassed the connector lock; closed in kit 2.4.
- 2026-10-30 · 2.1.312 · scheduled tasks run in the folder of the session that
  created them · this layer's tasks ran without its guards; kit 2.4 declares
  them and the boot check compares.
- 2026-10-30 · 2.1.312 · skills (`.claude/skills/`) · missed until kit 2.2;
  this watch exists because of it.
