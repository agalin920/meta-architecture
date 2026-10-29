#!/usr/bin/env python3
"""
PostToolUse hook (matcher Task|Agent): one line per subagent spawn.

    log/spawns-YYYY-MM.md
    - 2026-10-29 14:02 | spawn | 1a2b3c4d | reviewer | Review PR 4443 against the plan

Evidence the system does not write itself: tools/crew_report.py reads it beside
the session's `agent` events, so the crew's record does not depend on anyone
remembering to log a spawn. The prompt is never written (it can carry patient
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
    if payload.get("tool_name") not in ("Task", "Agent"):
        return
    inp = payload.get("tool_input") or {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    now = dt.datetime.now()
    kind = clean(inp.get("subagent_type") or "general-purpose", 40)
    desc = clean(inp.get("description") or "(no description)", 60)
    sid = clean(payload.get("session_id") or "unknown", 200)[:8]
    path = os.path.join(root, "log", f"spawns-{now:%Y-%m}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write(f"# Spawns — {now:%Y-%m}\n\nWritten by .claude/hooks/spawn_log.py, one line per subagent spawn. "
                    "Append-only and committed. Never the prompt.\n\n")
        f.write(f"- {now:%Y-%m-%d %H:%M} | spawn | {sid} | {kind} | {desc}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
