#!/usr/bin/env python3
"""
PreToolUse hook: the kernel's locks, enforced by the harness rather than prose.

Two jobs:
  1. LOCKS. Refuse any Edit/Write to a locked path, and any Bash command that
     names a locked path and looks like it writes. Locked = the charter, the
     scoreboard, the hooks, the reviewer, and the settings files.
  2. MARKER. Refuse any agent-posted GitHub body (PR, comment, review, issue)
     that lacks this system's marker. Andres posts from the same account, so
     the marker is the only way the scoreboard can tell his words from ours.

This cannot stop every spelling of a write: a shell can always build a path the
guard does not anticipate. scoreboard/lock.sha256 and the boot check are the
tripwire for that case. Locks make tampering hard; the tripwire makes it loud.

Configure the three constants below per system. This file is itself locked.
"""

import json
import os
import re
import sys

# --- per-system configuration ------------------------------------------------
SYSTEM = "SYSTEM-NAME"                      # e.g. "zesty-eng-team"
MARKER = f"<!-- {SYSTEM} -->"
LOCKED = [                                  # relative to the repo root
    "docs/charter.md",
    "scoreboard/",
    ".claude/hooks/",
    ".claude/settings.json",
    ".claude/settings.local.json",
    ".claude/agents/change-reviewer.md",
]
# -----------------------------------------------------------------------------

HOME_LOCKED = [os.path.expanduser("~/.claude/settings.json")]

# A command that names a locked path is allowed only if it shows none of these.
WRITE_SIGNS = re.compile(
    r"""
      (?<![0-9&])>(?!\s*/dev/null)(?!&)     # redirection, except to /dev/null or fd dup
    | \btee\b | \bsed\s+(-[a-zA-Z]*\s+)*-[a-zA-Z]*i | \bperl\b.*\s-[a-zA-Z]*i
    | \b(mv|cp|rm|rmdir|ln|chmod|chown|chflags|touch|truncate|dd|install|rsync|unlink|patch|ed|ex|vi|vim|nano)\b
    | \bgit\s+(checkout|restore|reset|rm|mv|apply|am|stash|clean|update-index|filter-branch|filter-repo|cherry-pick|merge|rebase|commit\s+.*--amend)\b
    | \b(python3?|node|ruby|perl|osascript|bash|sh|zsh|awk|deno|bun)\b
    """,
    re.VERBOSE,
)

# Reads and the kernel's own scripts that legitimately mention locked paths.
READ_OK = re.compile(
    r"^\s*(?:cd\s+\S+\s*&&\s*)?(?:/\S*/)?python3\s+(?:\./)?"
    r"(?:scoreboard/(?:score|verdicts)\.py|\.claude/hooks/boot_check\.py)\b(?![^;&|>]*--baseline)[^;&|>]*$"
)

GH_POST = re.compile(
    r"\bgh\s+(?:pr\s+(?:create|comment|review|edit)|issue\s+(?:create|comment|edit)|api\b)"
)
BODY_SIGNS = re.compile(r"(--body\b|\s-b\s|--body-file\b|\s-F\s|\bbody=|--input\b)")
FILE_ARG = re.compile(r"(?:--body-file|-F|--input)\s+(?:=\s*)?['\"]?([^\s'\"]+)")


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def project_dir(payload):
    return os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()


def locked_abs(root):
    paths = [os.path.realpath(os.path.join(root, p)) for p in LOCKED]
    return paths + [os.path.realpath(p) for p in HOME_LOCKED]


def is_locked_file(path, root):
    target = os.path.realpath(os.path.join(root, os.path.expanduser(path)))
    for lp, rel in zip(locked_abs(root), LOCKED + HOME_LOCKED):
        if rel.endswith("/"):
            if target == lp or target.startswith(lp.rstrip("/") + "/"):
                return rel
        elif target == lp:
            return rel
    return None


def names_locked(cmd):
    hits = []
    for rel in LOCKED + ["~/.claude/settings.json", ".claude/settings"]:
        key = rel.rstrip("/")
        base = os.path.basename(key)
        # Bare file names count too (a session may have cd'd), but only
        # distinctive ones: "settings.json" alone is too common to lock.
        bare = "." in base and base != "settings.json" and base in cmd
        if key in cmd or bare:
            hits.append(rel)
    if re.search(r"\brelock\b", cmd):
        hits.append("scoreboard/relock")
    return hits


def check_marker(cmd, root):
    if not GH_POST.search(cmd) or not BODY_SIGNS.search(cmd):
        return
    if cmd.startswith("gh api") and not re.search(r"(comments|reviews|issues|pulls|replies)", cmd):
        return
    if re.search(r"\bgh\s+api\b", cmd) and not re.search(r"(-X\s*(POST|PATCH|PUT)|--method\s+(POST|PATCH|PUT)|\s-f\s|\s-F\s|--field|--raw-field|--input)", cmd):
        return
    if MARKER in cmd:
        return
    for f in FILE_ARG.findall(cmd):
        p = os.path.join(root, os.path.expanduser(f))
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                if MARKER in fh.read():
                    return
        except OSError:
            pass
    deny(f"GitHub text posted by this system must carry the marker {MARKER} "
         f"so the scoreboard can tell it apart from Andres's own words. Add it to the body and retry.")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    tool = payload.get("tool_name", "")
    inp = payload.get("tool_input", {}) or {}
    root = project_dir(payload)

    if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = inp.get("file_path") or inp.get("notebook_path") or ""
        hit = is_locked_file(path, root) if path else None
        if hit:
            deny(f"{hit} is locked. Andres owns it; agents cannot change it. "
                 f"If it needs to change, write a proposal (docs/loop.md § Proposing a charter or scoreboard change).")
        sys.exit(0)

    if tool == "Bash":
        cmd = inp.get("command", "")
        if re.search(r"(^|[\s/;&|])relock\b", cmd):
            deny("scoreboard/relock is Andres's to run, in his own terminal. "
                 "A session that could relock could hide its own edit to a locked file.")
        if re.search(r"(^|[\s;&|.])(\./)?scoreboard/apply\b", cmd) or (
                re.search(r"log/pending/S-\d+", cmd) and re.search(r"\b(git\s+(apply|am)|patch)\b", cmd)):
            deny("Applying a charter or scoreboard proposal is Andres's step: he runs scoreboard/apply S-NNN "
                 "in his own terminal. Leave the proposal under 'Waiting on Andres'.")
        hits = names_locked(cmd)
        if hits and not READ_OK.search(cmd) and WRITE_SIGNS.search(cmd):
            deny(f"This command touches a locked path ({', '.join(sorted(set(hits)))}) and looks like it "
                 f"could write. Locked files are Andres's. Reading them with cat/grep/git log is fine.")
        check_marker(cmd, root)
    sys.exit(0)


if __name__ == "__main__":
    main()
