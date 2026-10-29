#!/usr/bin/env python3
"""
UserPromptSubmit hook: keep Andres's prompts, locally, for the loop.

Appends {"time", "session", "text"} to log/raw/prompts-YYYY-MM.jsonl. The loop
reads it to find and classify corrections he made in chat, so a correction is
not lost because the session did not notice it. log/raw/ is gitignored: prompts
can hold sensitive text (patient data at mPulse) and are never committed.
Prints nothing (stdout here would enter the session's context). Never blocks.
This file is locked.
"""

import datetime as dt
import json
import os
import sys


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
    rec = {"time": now.isoformat(timespec="seconds"), "session": payload.get("session_id") or "", "text": text}
    with open(os.path.join(d, f"prompts-{now:%Y-%m}.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
