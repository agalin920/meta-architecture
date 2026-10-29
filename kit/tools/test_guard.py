"""Feed synthetic hook payloads to kernel_guard.py and report allow/deny."""
import json, os, subprocess, sys, tempfile

GUARD = os.path.expanduser(sys.argv[1])
root = tempfile.mkdtemp()
os.makedirs(os.path.join(root, "docs"))

CASES = [
    ("DENY", "Edit", {"file_path": "docs/charter.md"}),
    ("DENY", "Write", {"file_path": os.path.join(root, "scoreboard/score.py")}),
    ("DENY", "Write", {"file_path": "~/.claude/settings.json"}),
    ("DENY", "Edit", {"file_path": ".claude/agents/change-reviewer.md"}),
    ("allow", "Edit", {"file_path": "docs/loop.md"}),
    ("DENY", "Bash", {"command": "echo x >> docs/charter.md"}),
    ("DENY", "Bash", {"command": "python3 -c \"open('docs/charter.md','a').write('x')\""}),
    ("DENY", "Bash", {"command": "sed -i '' s/a/b/ charter.md"}),
    ("DENY", "Bash", {"command": "cat > .claude/settings.local.json <<EOF\n{}\nEOF"}),
    ("DENY", "Bash", {"command": "git checkout HEAD~1 -- docs/charter.md"}),
    ("DENY", "Bash", {"command": "scoreboard/relock"}),
    ("DENY", "Bash", {"command": "cp /tmp/x .claude/hooks/kernel_guard.py"}),
    ("allow", "Bash", {"command": "cat docs/charter.md | grep goal"}),
    ("allow", "Bash", {"command": "git log --oneline -- scoreboard/ 2>/dev/null"}),
    ("allow", "Bash", {"command": "python3 scoreboard/score.py --summary"}),
    ("allow", "Bash", {"command": "python3 scoreboard/verdicts.py --all"}),
    ("DENY", "Bash", {"command": "gh pr comment 12 --body \"looks good\""}),
    ("allow", "Bash", {"command": "gh pr comment 12 --body \"<!-- SYSTEM-NAME --> looks good\""}),
    ("allow", "Bash", {"command": "gh pr view 12 --comments"}),
    ("allow", "Bash", {"command": "gh api repos/o/r/pulls/12/comments"}),
    ("DENY", "Bash", {"command": "gh api repos/o/r/pulls/12/comments/9/replies -f body=ok"}),
    ("allow", "Bash", {"command": "npm test > out.txt 2>&1"}),
    ("allow", "Bash", {"command": "git -C ../manager-ui log --oneline -5"}),
]

bad = 0
for want, tool, inp in CASES:
    p = subprocess.run([sys.executable, GUARD], input=json.dumps({"tool_name": tool, "tool_input": inp, "cwd": root}),
                       capture_output=True, text=True, env={**os.environ, "CLAUDE_PROJECT_DIR": root})
    got = "DENY" if '"deny"' in p.stdout else "allow"
    ok = got == want
    bad += not ok
    print(("ok  " if ok else "FAIL"), got.ljust(5), tool, json.dumps(inp)[:90])
print(f"{len(CASES) - bad}/{len(CASES)} as expected")
