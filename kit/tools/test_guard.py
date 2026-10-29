"""Feed synthetic hook payloads to kernel_guard.py and report deny / ask / allow.

Usage: python3 tools/test_guard.py <path to kernel_guard.py> [marker]
"""
import json, os, subprocess, sys, tempfile

GUARD = os.path.expanduser(sys.argv[1])
M = sys.argv[2] if len(sys.argv) > 2 else "<!-- SYSTEM-NAME -->"
root = tempfile.mkdtemp()
os.makedirs(os.path.join(root, "docs"))

CASES = [
    # locks: deny
    ("DENY", "Edit", {"file_path": "docs/charter.md"}),
    ("DENY", "Edit", {"file_path": "docs/CHARTER.md"}),
    ("DENY", "Write", {"file_path": os.path.join(root, "scoreboard/score.py")}),
    ("DENY", "Write", {"file_path": os.path.join(root, "Scoreboard/Score.py")}),
    ("DENY", "Write", {"file_path": "~/.claude/settings.json"}),
    ("DENY", "Edit", {"file_path": ".claude/agents/change-reviewer.md"}),
    ("DENY", "Write", {"file_path": ".claude/hooks/spawn_log.py"}),
    ("allow", "Edit", {"file_path": "docs/loop.md"}),
    ("allow", "Write", {"file_path": "log/events-2026-10.md"}),
    # log/raw/: raw evidence (Andres's prompts), written only by the prompt_log hook
    ("DENY", "Write", {"file_path": "log/raw/prompts-2026-10.jsonl"}),
    ("DENY", "Edit", {"file_path": os.path.join(root, "log/raw/prompts-2026-10.jsonl")}),
    ("DENY", "Write", {"file_path": "LOG/Raw/prompts-2026-10.jsonl"}),
    ("DENY", "Bash", {"command": "echo '{}' >> log/raw/prompts-2026-10.jsonl"}),
    ("DENY", "Bash", {"command": "rm log/raw/prompts-2026-10.jsonl"}),
    ("DENY", "Bash", {"command": "sed -i '' 1d log/raw/prompts-2026-10.jsonl"}),
    ("allow", "Bash", {"command": "grep -c session log/raw/prompts-2026-10.jsonl"}),
    ("allow", "Bash", {"command": "tail -3 log/raw/prompts-2026-10.jsonl | jq .time"}),
    ("DENY", "Bash", {"command": "echo x >> docs/charter.md"}),
    ("DENY", "Bash", {"command": "echo x >> DOCS/Charter.MD"}),
    ("DENY", "Bash", {"command": "python3 -c \"open('docs/charter.md','a').write('x')\""}),
    ("DENY", "Bash", {"command": "sed -i '' s/a/b/ charter.md"}),
    ("DENY", "Bash", {"command": "cat > .claude/settings.local.json <<EOF\n{}\nEOF"}),
    ("DENY", "Bash", {"command": "git checkout HEAD~1 -- docs/charter.md"}),
    ("DENY", "Bash", {"command": "scoreboard/relock"}),
    ("DENY", "Bash", {"command": "./scoreboard/apply S-002"}),
    ("DENY", "Bash", {"command": "cp /tmp/x .claude/hooks/kernel_guard.py"}),
    ("allow", "Bash", {"command": "cat docs/charter.md | grep goal"}),
    ("allow", "Bash", {"command": "git log --oneline -- scoreboard/ 2>/dev/null"}),
    ("allow", "Bash", {"command": "python3 scoreboard/score.py --summary"}),
    ("allow", "Bash", {"command": "python3 scoreboard/score.py --summary > log/scores/2026-10-29.txt"}),
    ("DENY", "Bash", {"command": "python3 scoreboard/score.py --summary > scoreboard/x.txt"}),
    ("allow", "Bash", {"command": "python3 scoreboard/verdicts.py --all"}),
    ("allow", "Bash", {"command": "python3 .claude/hooks/boot_check.py --write-env --model claude-opus-5-5"}),
    # marker: deny (a correctness rule; the agent fixes the body)
    ("DENY", "Bash", {"command": "gh pr comment 12 --body \"looks good\""}),
    ("allow", "Bash", {"command": f"gh pr comment 12 --body \"{M} looks good\""}),
    ("allow", "Bash", {"command": "gh pr view 12 --comments"}),
    ("allow", "Bash", {"command": "gh api repos/o/r/pulls/12/comments"}),
    ("DENY", "Bash", {"command": "gh api repos/o/r/pulls/12/comments/9/replies -f body=ok"}),
    # outside world: ask
    ("ask", "Bash", {"command": "gh pr merge 12 --squash"}),
    ("ask", "Bash", {"command": "gh api -X PUT repos/o/r/pulls/12/merge"}),
    ("ask", "Bash", {"command": "gh api -X DELETE repos/o/r/issues/comments/5"}),
    ("ask", "Bash", {"command": "gh api -X POST repos/o/r/releases -f tag_name=v1"}),
    ("ask", "Bash", {"command": "gh api -X PATCH repos/o/r -f default_branch=x --input settings.json"}),
    ("ask", "Bash", {"command": "git push --force origin main"}),
    ("ask", "Bash", {"command": "git push --mirror origin"}),
    ("ask", "Bash", {"command": "curl -X PURGE https://cdn.example.com/x"}),
    ("ask", "Bash", {"command": "curl -X DELETE https://api.example.com/v1/items/3"}),
    ("ask", "Bash", {"command": "curl -s -X POST https://hooks.slack.com/services/x -d '{}'"}),
    ("ask", "Bash", {"command": "curl --request PUT api.example.com/v1/x"}),
    ("ask", "Bash", {"command": "curl -d 'a=b' https://api.example.com/v1/x"}),
    ("ask", "Bash", {"command": "curl -X POST \"$URL\""}),
    ("allow", "Bash", {"command": "curl -X POST http://localhost:3000/api/x -d '{}'"}),
    ("allow", "Bash", {"command": "curl -X DELETE http://127.0.0.1:8080/x"}),
    ("allow", "Bash", {"command": "curl -s https://api.example.com/v1/x"}),
    ("ask", "Bash", {"command": "docker exec -it postgres psql -U app -c 'delete from users'"}),
    ("ask", "Bash", {"command": "docker compose exec db mysql -e 'select 1'"}),
    ("ask", "Bash", {"command": "docker run --rm mongo:7 mongosh --host x"}),
    ("allow", "Bash", {"command": "docker exec web npm test"}),
    ("allow", "Bash", {"command": "docker ps"}),
    # deny beats ask when both apply
    ("DENY", "Bash", {"command": "gh pr merge 12 && echo x >> docs/charter.md"}),
    ("allow", "Bash", {"command": "npm test > out.txt 2>&1"}),
    ("allow", "Bash", {"command": "git -C ../manager-ui log --oneline -5"}),
]


def outcome(out):
    if '"deny"' in out:
        return "DENY"
    if '"ask"' in out:
        return "ask"
    return "allow"


bad = 0
for want, tool, inp in CASES:
    p = subprocess.run([sys.executable, GUARD], input=json.dumps({"tool_name": tool, "tool_input": inp, "cwd": root}),
                       capture_output=True, text=True, env={**os.environ, "CLAUDE_PROJECT_DIR": root})
    got = outcome(p.stdout)
    ok = got == want and not p.returncode
    bad += not ok
    print(("ok  " if ok else "FAIL"), got.ljust(5), tool, json.dumps(inp)[:90], "" if ok else p.stderr[-200:])
print(f"{len(CASES) - bad}/{len(CASES)} as expected")
sys.exit(1 if bad else 0)
