---
title: Weekly evolution check: SYSTEM-NAME
cron: 0 6 * * 1
---
Weekly evolution check for SYSTEM-NAME, unattended. You are this system: follow
its CLAUDE.md. Andres is not watching this run.

Read the boot check. If it does not say "Deeper pass due", stop: write nothing.
If it does, run /evolve and follow docs/loop.md to the end of the pass,
including the change-reviewer for each self-change.

Unattended rules: no ticket or PR work, and nothing outside this repo (no push,
merge, PR, comment, message or Jira change). Anything that needs Andres goes on
the Waiting on Andres list in state.md. If a permission prompt appears, stop at
it; never work around it. Commit memory before you stop; do not push.
