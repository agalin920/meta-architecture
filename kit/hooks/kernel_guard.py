#!/usr/bin/env python3
"""
PreToolUse hook: the kernel's locks, enforced by the harness rather than prose.

Two outcomes besides allow (Andres ruled 2026-10-29):

  deny  flatly refused, even with his approval in the moment:
        - writes to locked files (any spelling, any case), connectors (.mcp.json,
          ~/.claude.json), declared schedules (.claude/schedules/), and the app's
          task prompts and task store;
        - writes to log/raw/, the raw evidence S3 is counted from (Andres's
          prompts). The prompt_log hook writes it through Python, not a tool,
          so it is unaffected; sessions may read it, never edit it;
        - running scoreboard/apply or scoreboard/relock, or applying a
          log/pending/S-* patch (those are his, in his own terminal);
        - an agent-posted GitHub body without this system's marker. That one is
          a correctness rule, not a gate: fix the body and retry.
  ask   a permission prompt Andres approves in the moment (outside-world acts):
        - pushes to another repo's protected branches;
        - force, --all, --mirror and delete pushes, in any repo, this one included;
        - gh pr merge; gh api writes to refs, contents, merges, branches,
          releases or settings, and any DELETE; GraphQL mutations that merge,
          close or move refs;
        - curl PURGE/DELETE/POST/PUT to a non-localhost host;
        - docker exec/run against a database container;
        - creating, changing, deleting or starting a scheduled task, session cron
          or routine; `claude mcp` and `claude plugin` changes.
  deny  also: a user-level skill or agent whose files live outside TOOL_ROOTS and
        ~/.claude itself, and any read of FOREIGN_TOOLING (the other employer's
        shared tooling).

This cannot stop every spelling of a write: a shell can always build a path the
guard does not anticipate. scoreboard/lock.sha256 and the boot check are the
tripwire for that case. Locks make tampering hard; the tripwire makes it loud.

Configure the constants below per system. This file is itself locked.
"""

import json
import os
import fnmatch
import glob
import re
import subprocess
import sys
from urllib.parse import urlsplit

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
    ".mcp.json",                            # connectors reach outside the repo
    ".claude/schedules/",                   # declared unattended runs
]
# Branches of OTHER repos this system must never push to (any spelling). Its own
# repo is exempt (pushing its own main is how memory reaches the remote).
PROTECTED = ["main", "master", "develop", "dev", "stage", "beta", "stable", "production", "release/*"]
# -----------------------------------------------------------------------------

HOME_LOCKED = [os.path.expanduser("~/.claude/settings.json"), os.path.expanduser("~/.claude/scheduled-tasks/"),
               os.path.expanduser("~/.claude.json")]       # user and local connectors live here
# The app's scheduled-task store (times, folders, enabled flags), wherever the account keeps it.
HOME_GLOBS = [os.path.expanduser("~/Library/Application Support/Claude/claude-code-sessions/*/*/scheduled-tasks.json")]
# Evidence written only by hooks: sessions read it, never write it (Andres, 2026-10-29).
RAW = ["log/raw/"]

# Tools that create, change or start a run nobody watches: scheduled tasks, session crons, cloud routines.
SCHEDULE_TOOLS = re.compile(r"^(mcp__scheduled-tasks__(create|update|delete|run)_scheduled_task|CronCreate|CronDelete|RemoteTrigger)$")
# User-level skills and agents are links into each employer's shared tooling. One runs
# here only if its files live under TOOL_ROOTS, or are real files in ~/.claude itself; the
# other employer's tooling is not read either (Andres, 2026-10-31). Empty: only ~/.claude itself.
TOOL_ROOTS = []
FOREIGN_TOOLING = []
# Commands that add or remove a connector or plugin without naming a file.
CONNECTOR_CMD = re.compile(r"\bclaude\s+(?:mcp\s+(?:add|add-json|add-from-claude-desktop|remove)|plugins?\s+(?:install|uninstall|enable|disable|marketplace))\b")

# A command that names a locked path is allowed only if it shows none of these.
WRITE_SIGNS = re.compile(
    r"""
      (?<![0-9&])>(?!\s*/dev/null)(?!&)     # redirection, except to /dev/null or fd dup
    | \btee\b | \bsed\s+(-[a-zA-Z]*\s+)*-[a-zA-Z]*i | \bperl\b.*\s-[a-zA-Z]*i
    | \b(mv|cp|rm|rmdir|ln|chmod|chown|chflags|touch|truncate|dd|install|rsync|unlink|patch|ed|ex|vi|vim|nano)\b
    | \bgit\s+(?:-C\s+\S+\s+)*(checkout|restore|reset|rm|mv|apply|am|stash|clean|update-index|filter-branch|filter-repo|cherry-pick|merge|rebase|commit\s+.*--amend)\b
    | \b(python3?|node|ruby|perl|osascript|bash|sh|zsh|awk|deno|bun)\b
    """,
    re.VERBOSE,
)

# Reads and the kernel's own scripts that legitimately mention locked paths.
READ_OK = re.compile(
    r"^\s*(?:cd\s+\S+\s*&&\s*)?(?:/\S*/)?python3\s+(?:\./)?"
    r"(?:scoreboard/(?:score|verdicts)\.py|\.claude/hooks/boot_check\.py)\b(?![^;&|>]*--baseline)[^;&|>]*"
    r"(?:>\s*log/scores/[\w.-]+\.txt\s*)?$"     # the loop saves score snapshots here
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


ASKS = []


def ask(reason):
    """Outside-world act: Andres approves it in the moment. A deny found later still wins."""
    ASKS.append(reason)


def finish():
    if ASKS:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": " ".join(dict.fromkeys(ASKS)),
            }
        }))
    sys.exit(0)


def project_dir(payload):
    return os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()


def locked_abs(root):
    paths = [os.path.realpath(os.path.join(root, p)) for p in LOCKED]
    return paths + [os.path.realpath(p) for p in HOME_LOCKED] + [os.path.realpath(os.path.join(root, p)) for p in RAW]


def is_locked_file(path, root):
    # Compare case-folded: macOS filesystems are case-insensitive, so CHARTER.md is charter.md.
    target = os.path.realpath(os.path.join(root, os.path.expanduser(path))).casefold()
    for lp, rel in zip(locked_abs(root), LOCKED + HOME_LOCKED + RAW):
        lp = lp.casefold()
        if rel.endswith("/"):
            if target == lp or target.startswith(lp.rstrip("/") + "/"):
                return rel
        elif target == lp:
            return rel
    return None


def names_locked(cmd):
    cmd = cmd.casefold()
    hits = []
    for rel in LOCKED + RAW + ["~/.claude/settings.json", ".claude/settings", "/.claude/scheduled-tasks", "scheduled-tasks.json", "~/.claude.json"]:
        key = rel.rstrip("/").casefold()
        base = os.path.basename(key)
        # Bare file names count too (a session may have cd'd), but only
        # distinctive ones: "settings.json" alone is too common to lock.
        bare = "." in base and base != "settings.json" and base in cmd
        if key in cmd or bare:
            hits.append(rel)
    return hits


def segments(cmd):
    """Split a shell command into simple commands (good enough for a guard)."""
    return [x for x in re.split(r"&&|\|\||[;|\n]|\$\(|`", cmd) if x.strip()]


def runs_kernel_script(cmd):
    """Is relock or apply being executed (not merely read), by any spelling?"""
    wrappers = {"bash", "sh", "zsh", "exec", "env", "command", "nohup", "time", "sudo", "xargs", "source", "."}
    for seg in segments(cmd):
        toks = seg.strip().split()
        while toks and (re.match(r"^\w+=", toks[0]) or toks[0] in wrappers or toks[0].startswith("-")):
            toks = toks[1:]
        if not toks:
            continue
        t = toks[0].strip("'\"")
        base = os.path.basename(t)
        if base == "relock" or (base == "apply" and "/" in t and ("scoreboard" in t or "scoreboard" in cmd)):
            return base
    return None


def is_protected(branch):
    b = branch.replace("refs/heads/", "").strip("'\"")
    return any(fnmatch.fnmatch(b, p) for p in PROTECTED)


def check_push(cmd, root):
    """Force, mirror, all and delete pushes anywhere, and pushes to another repo's protected branches: ask."""
    for seg in segments(cmd):
        m = re.search(r"\bgit\b((?:\s+-[Cc]\s+\S+)*)\s+push\b(.*)$", seg)
        if not m:
            continue
        args = m.group(2).split()
        flags = [a for a in args if a.startswith("-")]
        pos = [a for a in args if not a.startswith("-")]
        if any(f in ("-f", "-d", "--all", "--mirror", "--delete", "--prune") or f.startswith("--force") for f in flags) \
                or any(r.startswith(("+", ":")) for r in pos[1:]):
            ask("A force, mirror, --all or delete push rewrites or removes history on a shared remote. "
                "Andres approves it in the moment.")
        cd = re.search(r"-C\s+(\S+)", m.group(1))
        if cd:
            d = cd.group(1)
        else:
            before = cmd[:cmd.find(seg)]
            cds = re.findall(r"\bcd\s+(\S+)", before)
            d = cds[-1] if cds else "."
        d = os.path.realpath(os.path.join(root, os.path.expanduser(d.strip("'\""))))
        if d == os.path.realpath(root):
            continue                                  # this system's own repo
        targets = [r.split(":")[-1] for r in pos[1:]]
        if not targets:
            try:
                targets = [subprocess.run(["git", "-C", d, "rev-parse", "--abbrev-ref", "HEAD"],
                                          capture_output=True, text=True, timeout=5).stdout.strip()]
            except Exception:
                targets = ["(unknown)"]
        for t in targets:
            if t in ("HEAD", "(unknown)", "") or is_protected(t):
                ask(f"Pushing to '{t or '(unknown)'}' of {os.path.basename(d)}: protected branches of other repos "
                    f"are Andres's to approve. A feature branch pushed by name needs no approval.")


GH_WRITE_PATHS = re.compile(r"git/refs|/contents/|/merges\b|/merge\b|/branches/|/rulesets|/hooks|/collaborators|"
                            r"/actions/|/environments|/deployments|/releases|/settings|/keys\b|/secrets|/pages\b")
GQL_MOVES = re.compile(r"merge|deleteRef|updateRef|createRef|updateRefs|closePullRequest|closeIssue|reopen|delete|"
                       r"dismiss|enablePullRequestAutoMerge|transfer|archive", re.I)


def check_gh_writes(cmd):
    """gh may read, comment and review freely. Merges, ref moves, content writes and deletes: ask."""
    for seg in segments(cmd):
        if re.search(r"\bgh\s+pr\s+merge\b", seg):
            ask("gh pr merge ships code. Andres approves merges in the moment.")
        if not re.search(r"\bgh\s+api\b", seg):
            continue
        if re.search(r"\bgraphql\b", seg) and re.search(r"\bmutation\b", seg, re.I):
            if GQL_MOVES.search(seg):
                ask("This GraphQL mutation merges, moves refs, closes or deletes. Andres approves it in the moment.")
            continue
        mm = re.search(r"(?:-X|--method)\s*=?\s*([A-Za-z]+)", seg)
        method = mm.group(1).upper() if mm else (
            "POST" if re.search(r"\s(-f|-F|--field|--raw-field|--input)\b", seg) else "GET")
        if method == "GET":
            continue
        repo_settings = re.search(r"(?:^|\s)/?(?:repos/[^/\s]+/[^/\s]+|orgs/[^/\s]+)/?(?=\s|$)", seg)
        if method == "DELETE" or GH_WRITE_PATHS.search(seg) or repo_settings:
            ask("gh api writes to refs, contents, merges, branches, releases or settings, and any DELETE, "
                "are Andres's to approve in the moment.")


LOCAL_HOSTS = re.compile(r"^(?:localhost|127\.\d+\.\d+\.\d+|::1|0\.0\.0\.0|[\w.-]+\.(?:localhost|test))$", re.I)
DB_SIGNS = re.compile(r"postgres|psql|pg_|mysql|maria|mongo|redis|\bdb\b|[-_]db\b|\bdb[-_]|database|sql|clickhouse|"
                      r"cassandra|cockroach|elastic|opensearch|dynamo|couch|neo4j|influx", re.I)


def curl_hosts(seg):
    hosts = []
    for tok in seg.split():
        tok = tok.strip("'\"")
        if "://" in tok:
            hosts.append(urlsplit(tok).hostname or "")
        elif re.match(r"^(?:localhost|[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}|\d+\.\d+\.\d+\.\d+)(?::\d+)?(?:/|$)", tok):
            hosts.append(re.split(r"[:/]", tok)[0])
    return hosts


def check_outside_writes(cmd):
    """curl writes to the outside world, and docker exec/run against databases: ask."""
    for seg in segments(cmd):
        if re.search(r"\bcurl\b", seg):
            mm = re.search(r"(?:-X|--request)\s*=?\s*['\"]?([A-Za-z]+)", seg)
            method = mm.group(1).upper() if mm else (
                "POST" if re.search(r"\s(-d|--data[\w-]*|-F|--form|--json|-T|--upload-file)\b", seg) else "GET")
            if method in ("PURGE", "DELETE", "POST", "PUT", "PATCH"):
                hosts = curl_hosts(seg)
                # No recognisable host (a $URL variable, say) counts as outside.
                if not hosts or not all(LOCAL_HOSTS.match(h) for h in hosts):
                    ask(f"curl {method} to a non-local host changes something in the outside world. "
                        f"Andres approves it in the moment.")
        if re.search(r"\bdocker(?:\s+compose|-compose)?\s+(?:container\s+)?(?:exec|run)\b", seg) and DB_SIGNS.search(seg):
            ask("docker exec/run against a database container can change or read data Andres guards. "
                "He approves it in the moment.")


def check_marker(cmd, root):
    pr_create = re.search(r"\bgh\s+pr\s+create\b", cmd)
    graphql_post = re.search(r"\bgh\s+api\s+graphql\b", cmd) and re.search(r"\bmutation\b", cmd, re.I) \
        and re.search(r"\bbody\b", cmd)
    if not pr_create and not graphql_post and (not GH_POST.search(cmd) or not BODY_SIGNS.search(cmd)):
        return
    if not pr_create and not graphql_post and cmd.startswith("gh api") and not re.search(r"(comments|reviews|issues|pulls|replies)", cmd):
        return
    if not graphql_post and re.search(r"\bgh\s+api\b", cmd) and not re.search(r"(-X\s*(POST|PATCH|PUT)|--method\s+(POST|PATCH|PUT)|\s-f\s|\s-F\s|--field|--raw-field|--input)", cmd):
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


def _user_tools():
    """{(kind, name): [realpath]} for user-level skills and agents, by folder or file name and by
    frontmatter `name:`, so a renamed definition cannot slip past."""
    out = {}
    def add(kind, name, real):
        out.setdefault((kind, name.strip().lower()), []).append(real)
    for f in glob.glob(os.path.expanduser("~/.claude/skills/*/SKILL.md")):
        real = os.path.realpath(f)
        add("skill", os.path.basename(os.path.dirname(f)), real)
        m = re.search(r"^name:\s*(\S+)", (open(real, errors="replace").read(2000) if os.path.isfile(real) else ""), re.M)
        if m:
            add("skill", m.group(1), real)
    for f in glob.glob(os.path.expanduser("~/.claude/agents/**/*.md"), recursive=True):
        real = os.path.realpath(f)
        add("agent", os.path.basename(f)[:-3], real)
        m = re.search(r"^name:\s*(\S+)", (open(real, errors="replace").read(2000) if os.path.isfile(real) else ""), re.M)
        if m:
            add("agent", m.group(1), real)
    return out


def _outside(real, roots):
    allowed = [os.path.realpath(os.path.expanduser("~/.claude"))] + [os.path.realpath(os.path.expanduser(r)) for r in roots]
    return not any(real == a or real.startswith(a + os.sep) for a in allowed)


def foreign_tool(tool, inp, root):
    """Why this call would load or read another employer's tooling, or None."""
    if tool == "Skill":
        name = str(inp.get("skill") or "").lstrip("/")
        if not name or ":" in name:
            return None                             # plugin skills are their own channel
        hits = _user_tools().get(("skill", name.lower()), [])
    elif tool in ("Agent", "Task"):
        hits = _user_tools().get(("agent", str(inp.get("subagent_type") or "").lower()), [])
    elif tool in ("Read", "Grep", "Glob"):
        p = inp.get("file_path") or inp.get("path") or ""
        real = os.path.realpath(os.path.join(root, os.path.expanduser(p))) if p else ""
        hits = [real] if real and any(real == f or real.startswith(f + os.sep) for f in
                                      (os.path.realpath(os.path.expanduser(x)) for x in FOREIGN_TOOLING)) else []
        return "read" if hits else None
    else:
        return None
    return "load" if any(_outside(h, TOOL_ROOTS) for h in hits) else None


def foreign_cmd(cmd):
    """A shell command that names another employer's tooling: its full path, or a folder name distinctive enough."""
    cmd = os.path.expanduser(cmd)
    for x in FOREIGN_TOOLING:
        full, base = os.path.expanduser(x), os.path.basename(x)
        if full in cmd or ("-" in base and base in cmd):
            return True
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    tool = payload.get("tool_name", "")
    inp = payload.get("tool_input", {}) or {}
    root = project_dir(payload)

    hit = foreign_tool(tool, inp, root)
    if hit or (tool == "Bash" and foreign_cmd(inp.get("command", ""))):
        deny("That is another employer's shared tooling, which this system does not load or read (Andres, "
             "2026-10-31). Do not open its files by any other route; do the step with this system's own know-how.")

    if SCHEDULE_TOOLS.match(tool):
        ask("This sets up, changes or starts an unattended run. Andres approves each, and it must match a "
            "declared .claude/schedules/<id>.md (the loop doc, § Tools, connectors and schedules).")
        finish()

    if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = inp.get("file_path") or inp.get("notebook_path") or ""
        hit = is_locked_file(path, root) if path else None
        if path and any(fnmatch.fnmatch(os.path.realpath(os.path.expanduser(path)), g) for g in HOME_GLOBS):
            hit = "the app's scheduled-task store"
        if hit in RAW:
            deny(f"{hit} is raw evidence written only by a hook (Andres's prompts; S3 is counted from it). "
                 f"Sessions may read it, never edit it.")
        if hit:
            deny(f"{hit} is locked. Andres owns it; agents cannot change it. "
                 f"If it needs to change, write a proposal (docs/loop.md § Proposing a charter or scoreboard change).")
        sys.exit(0)

    if tool == "Bash":
        cmd = inp.get("command", "")
        ran = runs_kernel_script(cmd)
        if ran == "relock":
            deny("scoreboard/relock is Andres's to run, in his own terminal. "
                 "A session that could relock could hide its own edit to a locked file.")
        if ran == "apply" or (
                re.search(r"log/pending/S-\d+", cmd) and re.search(r"\b(git\s+(apply|am)|patch)\b", cmd)):
            deny("Applying a charter or scoreboard proposal is Andres's step: he runs scoreboard/apply S-NNN "
                 "in his own terminal. Leave the proposal under 'Waiting on Andres'.")
        hits = names_locked(cmd)
        if hits and not READ_OK.search(cmd) and WRITE_SIGNS.search(cmd):
            if set(hits) <= set(RAW):
                deny("This command names log/raw/ and looks like it could write. log/raw/ is raw evidence "
                     "written only by a hook (S3 is counted from it); read it with the Read tool, cat, grep, tail or jq, never edit it.")
            deny(f"This command touches a locked path ({', '.join(sorted(set(hits)))}) and looks like it "
                 f"could write. Locked files are Andres's. Reading them with cat/grep/git log is fine.")
        if CONNECTOR_CMD.search(cmd):
            ask("This adds or removes a connector or plugin, which reaches outside the repo. Andres approves it "
                "in the moment; propose it first (Kind: connector).")
        check_marker(cmd, root)
        check_push(cmd, root)
        check_gh_writes(cmd)
        check_outside_writes(cmd)
    finish()


if __name__ == "__main__":
    main()
