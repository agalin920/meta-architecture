#!/usr/bin/env python3
"""
Kit drift: how far a system's kernel files have moved from this kit.

Diffs each kernel file in the system against kit/, ignoring the per-system
configuration blocks (the lines between `# --- per-system configuration` and
the next `# -----` rule: SYSTEM, MARKER, LOCKED, PROTECTED, MEMORY, TRIALS,
state and changelog file names, and the like; and relock's file LIST).
A system may declare intentional deviations in .claude/kit-deviations.md, one
per line: `- <system path> — <reason>`. Declared ones are reported as
"declared", with the reason. Files the system owns and is meant to evolve
(docs/loop.md, the commands) are listed with a line count only.

Usage: python3 kit/tools/kit_drift.py <system-repo> [--full]
"""

import argparse
import difflib
import os
import re

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KERNEL = {
    "hooks/kernel_guard.py": ".claude/hooks/kernel_guard.py",
    "hooks/boot_check.py": ".claude/hooks/boot_check.py",
    "hooks/stop_check.py": ".claude/hooks/stop_check.py",
    "hooks/spawn_log.py": ".claude/hooks/spawn_log.py",
    "hooks/prompt_log.py": ".claude/hooks/prompt_log.py",
    "hooks/session_live.py": ".claude/hooks/session_live.py",
    "scoreboard/verdicts.py": "scoreboard/verdicts.py",
    "scoreboard/apply": "scoreboard/apply",
    "scoreboard/relock": "scoreboard/relock",
    "agents/change-reviewer.md": ".claude/agents/change-reviewer.md",
    "tools/crew_report.py": "tools/crew_report.py",
    "tools/conservation_check.py": "tools/conservation_check.py",
}
OWNED = {
    "docs/loop.md": "docs/loop.md",
    "commands/evolve.md": ".claude/commands/evolve.md",
    "commands/what-changed.md": ".claude/commands/what-changed.md",
}
BLOCKS = [(re.compile(r"^#\s*-+\s*per-system configuration"), re.compile(r"^#\s*-{10,}\s*$")),
          (re.compile(r"<<'LIST'"), re.compile(r"^LIST\s*$"))]
# Per-system values set outside the block: kit 2.7's tool scoping (each system's own employer).
LINES = re.compile(r"^(TOOL_ROOTS|FOREIGN_TOOLING) = ")


def body(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return None
    out, end = [], None
    for line in lines:
        if end is not None:
            if end.search(line):
                out.append(line)
                end = None
            continue
        for start, stop in BLOCKS:
            if start.search(line):
                out.append(line + "   [per-system block ignored]")
                end = stop
                break
        else:
            out.append(line.split(" = ")[0] + " = [per-system value ignored]" if LINES.search(line) else line)
    return out


def declared(repo):
    out = {}
    try:
        text = open(os.path.join(repo, ".claude", "kit-deviations.md"), encoding="utf-8").read()
    except OSError:
        return out
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]\s*`?([^\s`]+)`?\s*(?:—|–|-|:)\s*(.+)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--full", action="store_true", help="print whole diffs, not the first 30 lines")
    a = ap.parse_args()
    repo = os.path.abspath(os.path.expanduser(a.repo))
    version = (open(os.path.join(KIT, "VERSION")).read().strip() if os.path.exists(os.path.join(KIT, "VERSION")) else "?")
    dev = declared(repo)
    print(f"Kit drift: {repo} against kit {version}")
    same = drift = 0
    for kit_rel, sys_rel in KERNEL.items():
        k, s = body(os.path.join(KIT, kit_rel)), body(os.path.join(repo, sys_rel))
        if s is None:
            print(f"  MISSING   {sys_rel}" + (f"  (declared: {dev[sys_rel]})" if sys_rel in dev else ""))
            drift += sys_rel not in dev
            continue
        if k == s:
            same += 1
            continue
        diff = list(difflib.unified_diff(k, s, f"kit/{kit_rel}", sys_rel, lineterm="", n=1))
        add = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
        rem = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
        if sys_rel in dev:
            print(f"  declared  {sys_rel}  (+{add}/-{rem}): {dev[sys_rel]}")
            continue
        drift += 1
        print(f"  DRIFT     {sys_rel}  (+{add}/-{rem} against the kit)")
        for l in diff[2:] if a.full else diff[2:32]:
            print("      " + l)
        if not a.full and len(diff) > 32:
            print(f"      … {len(diff) - 32} more diff lines (--full)")
    for kit_rel, sys_rel in OWNED.items():
        k, s = body(os.path.join(KIT, kit_rel)), body(os.path.join(repo, sys_rel))
        if s is None:
            print(f"  missing   {sys_rel} (system-owned)")
        elif k != s:
            d = [l for l in difflib.unified_diff(k, s, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
            print(f"  evolved   {sys_rel}  ({len(d)} lines differ; system-owned, informational)")
    print(f"{same} kernel file(s) match the kit, {drift} drift undeclared.")


if __name__ == "__main__":
    main()
