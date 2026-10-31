#!/usr/bin/env python3
"""
PostToolUse hook (matcher Task|Agent|Skill): one line per subagent spawn, and
one per skill the model loads.

    log/spawns-YYYY-MM.md
    - 2026-10-29 14:02 | spawn | 1a2b3c4d | reviewer | Review PR 4443 against the plan
    - 2026-10-29 14:05 | skill | 1a2b3c4d | run-tests

Evidence the system does not write itself: tools/crew_report.py reads it beside
the session's `agent` events, so the crew's record does not depend on anyone
remembering to log a spawn. The prompt, and a skill's arguments, are never written (it can carry patient
data, and this file is committed memory); only the type and a short description.
Never blocks. This file is locked.
"""

import datetime as dt
import json
import os
import re
import sys


def clean(text, n):
    text = re.sub(r"\s+", " ", str(text or "")).replace("|", "/").strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    tool = payload.get("tool_name")
    if tool not in ("Task", "Agent", "Skill"):
        return
    inp = payload.get("tool_input") or {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    now = dt.datetime.now()
    sid = clean(payload.get("session_id") or "unknown", 200)[:8]
    if tool == "Skill":
        line = f"- {now:%Y-%m-%d %H:%M} | skill | {sid} | {clean(inp.get('skill') or '?', 80)}\n"
    else:
        kind = clean(inp.get("subagent_type") or "general-purpose", 40)
        desc = clean(inp.get("description") or "(no description)", 60)
        line = f"- {now:%Y-%m-%d %H:%M} | spawn | {sid} | {kind} | {desc}\n"
    path = os.path.join(root, "log", f"spawns-{now:%Y-%m}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write(f"# Spawns — {now:%Y-%m}\n\nWritten by .claude/hooks/spawn_log.py, one line per subagent spawn "
                    "or skill load. Append-only and committed. Never the prompt.\n\n")
        f.write(line)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
