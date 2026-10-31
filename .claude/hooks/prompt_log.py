#!/usr/bin/env python3
"""
UserPromptSubmit hook: keep Andres's prompts, locally, for the loop.

Appends {"time", "session", "origin", "text"} to log/raw/prompts-YYYY-MM.jsonl.
The loop reads it to find and classify corrections he made in chat, so a
correction is not lost because the session did not notice it. log/raw/ is
gitignored: prompts can hold sensitive text (patient data at mPulse) and are
never committed. Prints nothing (stdout here would enter the session's context).
Never blocks. This file is locked.

`origin` says who wrote the prompt, from its opening tag: "andres", or "agent"
(a message from another session), "notification" (a background task finished)
or "shell" (a command run from the prompt box). S3 counts only "andres".

    python3 .claude/hooks/prompt_log.py --backfill   # tag lines written before origin existed
"""

import datetime as dt
import fcntl
import glob
import json
import os
import re
import sys

ORIGINS = {
    "agent-message": "agent", "side-sessions-event": "agent",
    "task-notification": "notification", "ci-monitor-event": "notification",
    "bash-input": "shell", "bash-stdout": "shell", "bash-stderr": "shell",
}


def origin(text):
    m = re.match(r"\s*<([a-z][a-z-]*)[\s>]", text)
    return ORIGINS.get(m.group(1), "andres") if m else "andres"


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    text = payload.get("prompt")
    if not text:
        return
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    now = dt.datetime.now()
    d = os.path.join(root, "log", "raw")
    os.makedirs(d, exist_ok=True)
    rec = {"time": now.isoformat(timespec="seconds"), "session": payload.get("session_id") or "",
           "origin": origin(text), "text": text}
    with open(os.path.join(d, f"prompts-{now:%Y-%m}.jsonl"), "a", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)                 # backfill holds it while it rewrites
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def backfill(root):
    """Add `origin` to lines that lack it, in place and under the file lock, so a prompt logged meanwhile
    waits rather than being lost. Other lines are kept byte for byte. Prints counts only, never text."""
    counts = {}
    for p in sorted(glob.glob(os.path.join(root, "log", "raw", "prompts-*.jsonl"))):
        with open(p, "r+", encoding="utf-8", errors="surrogateescape") as fh:
            fcntl.flock(fh, fcntl.LOCK_EX)
            out = []
            for line in fh.read().splitlines(keepends=True):
                try:
                    rec = json.loads(line)
                except ValueError:
                    out.append(line)
                    continue
                if isinstance(rec, dict) and "origin" not in rec:
                    rec["origin"] = origin(str(rec.get("text") or ""))
                    counts[rec["origin"]] = counts.get(rec["origin"], 0) + 1
                    line = json.dumps(rec, ensure_ascii=False) + "\n"
                out.append(line)
            fh.seek(0)
            fh.write("".join(out))
            fh.truncate()
    print("tagged:", counts or "nothing to tag")


if __name__ == "__main__":
    if sys.argv[1:] == ["--backfill"]:
        backfill(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
        sys.exit(0)
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
