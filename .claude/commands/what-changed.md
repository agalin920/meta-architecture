---
description: Tell Andres, in two minutes, how the systems and the playbook have changed, and whether it helped.
---

Andres asked "what has changed?". Answer across all systems, in plain language, short enough to read in two minutes.

1. Run `echo '{}' | python3 .claude/hooks/boot_check.py` here, and in each core system (`../zestyio/zesty-eng-team`, `../mpulsemobile/mpulse-engage-team`, `../mpulsemobile/mpulse-dpi-team`). If any prints **LOCK BROKEN**, lead with that and stop.
2. Run `python3 scoreboard/score.py`: each system against its baseline (M1), escalations (M2), playbook flow (M3) and rollbacks (M4).
3. Read `CHANGELOG.md` here and in each core system, since the date under "Last asked" in `HANDOFF.md` (or the last 30 days).
4. Write, in this order and nothing else:
   - **Waiting on you**: `HANDOFF.md` § Waiting on Andres: system, then § Waiting on Andres — from the systems, then the work list, each item with its date.
   - **Per system**: one line per self-change, with its verdict so far (helped with numbers; unproven and kept; looks worse, with what the system decided and why; reverted for harm and the harm; or open and when it is due). *Looks worse* verdicts and reviewer CONCERNs landed anyway are information, not items waiting on Andres.
   - **The scores**: one line per system from M1, naming what is not measured where it matters.
   - **The playbook**: lessons collected, trials open, anything proven.
5. Update "Last asked" in `HANDOFF.md` to today and commit it: `git -C . add HANDOFF.md && git -C . commit -m "memory: what-changed"`.

No process narrative. Name numbers and commits. Say what you did not verify.
