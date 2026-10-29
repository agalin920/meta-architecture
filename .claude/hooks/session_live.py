#!/usr/bin/env python3
"""
SessionStart / SessionEnd hook: which sessions are live in this repo.

At start it writes log/.live/<session_id> (gitignored) with the start time and
the HEAD the session started from; at end it removes it. The boot check warns
when another session's marker is under 6 hours old, so two sessions do not
overwrite each other's state files. The stop check diffs the log against the
start HEAD to see whether this session removed an event line.
A resumed or compacted session keeps its original marker. Markers older than
two days (a session that crashed before SessionEnd) are swept at start.
Prints nothing. Never blocks. This file is locked.
"""

import datetime as dt
import json
import os
import re
import subprocess
import sys
import time


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    sid = re.sub(r"[^\w-]", "", str(payload.get("session_id") or ""))
    if not sid:
        return
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    d = os.path.join(root, "log", ".live")
    path = os.path.join(d, sid)
    if payload.get("hook_event_name") == "SessionEnd":
        try:
            os.remove(path)
        except OSError:
            pass
        return
    os.makedirs(d, exist_ok=True)
    for name in os.listdir(d):
        p = os.path.join(d, name)
        try:
            if time.time() - os.path.getmtime(p) > 2 * 86400:
                os.remove(p)
        except OSError:
            pass
    if os.path.exists(path):
        return
    try:
        head = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"], capture_output=True, text=True,
                              timeout=5).stdout.strip()
    except Exception:
        head = ""
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"started {dt.datetime.now().isoformat(timespec='minutes')}\nhead {head}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
