#!/usr/bin/env python3
"""
Stop hook: a session does not end with the loop owed or memory uncommitted.

Steps scheduled for "the end" are the ones that get dropped; one side project
measured seven instances across four mechanisms. So the end is enforced here:
if a finished unit of work has no loop entry, or memory is uncommitted, the
stop is blocked once with the reason. The second attempt is let through
(stop_hook_active) so a session can never be trapped, and the boot check
reports whatever is still owed. This file is locked.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from boot_check import owed_loops, uncommitted  # noqa: E402


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    if payload.get("stop_hook_active"):
        sys.exit(0)
    root = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    problems = []
    owed = owed_loops(root)
    if owed:
        problems.append("The loop is owed for: " + ", ".join(owed) +
                        ". Run docs/loop.md for each, then write its `loop` event.")
    dirty = uncommitted(root)
    if dirty:
        problems.append(f"{len(dirty)} memory file(s) are uncommitted ({', '.join(dirty[:6])}). "
                        "Commit them with a `memory:` commit; an uncommitted log is not a log.")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
