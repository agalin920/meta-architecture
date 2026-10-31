# Current state

Rewritten in place, never appended to. The pre-redesign handoff is at
[`archive/HANDOFF.md`](archive/HANDOFF.md).

**As of 2026-10-29:** the migration ran on 2026-10-28 under
[`REDESIGN.md`](REDESIGN.md), in this repo and in
the three core systems. **Merged to `main` and pushed on 2026-10-29**, at Andres's
request, in all four repos (fast-forward; nothing on the remotes was overwritten).

## Where things stand

- **Playbook:** `playbook.md` states the kernel, the lesson statuses, the playbook rule and the
  review. The lessons catalog is in `lessons/`.
- **Trials:** none open. The earliest possible candidate is 14 days after a
  core system's first self-change.
- **Core systems:** four. The three work systems migrated to the kernel with
  baselines recorded 2026-10-28; vinted-shopper was built on it, baseline
  2026-10-29, and made core on 2026-10-30. See `systems.md`.
- **Side projects:** dormant and untouched. Lessons collected.
- **Weekly review:** the "Weekly lessons review" task (Monday morning, Claude desktop
  app), plus this repo's boot.
- **Falsifier checks:** 2027-01-31 and 2027-03-31 (`meta/thesis.md`).
- **S3 re-baseline due 2026-11-29.** S3 changed definition on 2026-10-29 (Andres's
  follow-up prompts instead of hand-kept findings), so until then it reads
  "worse" against the old baselines in M1 and the systems' boot checks without
  anything having got worse (each system's `definitions.md` § Definition
  breaks). From that date, with 30 days under the new definition, each work
  system writes a scoreboard proposal (`log/pending/S-NNN`) for a fresh S3
  baseline, and the weekly review lists it here for Andres. Until then, read
  S3 "worse" as the break, not a result.

## Waiting on Andres: system


## Waiting on Andres: work


- 2026-10-28 — Commit or leave the side projects' uncommitted work. Much of their
  measured evidence lives only there (`systems.md`). Not urgent.

## Waiting on Andres — from the systems

Rewritten by every weekly lessons review (`meta/keeper.md` § 6). Last run:
2026-10-29 09:30, the scheduled run. No `LOCK BROKEN`: every boot check printed
"Locks intact". Kit drift: 0 undeclared in all three (`docs/loop.md` evolved,
system-owned). No side project revived (no commits since their registry rows).

**System-level: 2 waiting.** Push attempted; not delivered (Remote Control inactive).

- **zesty-eng-team · S-001 (charter, open):** name a second product repo the
  system has already been working on in the charter's roster, or confirm it is
  out of scope (if declined, the system denies edits there and hands its two
  open PRs back). Approve: `scoreboard/apply S-001` in that repo.
- **mpulse-dpi-team · scope question** (`state.md` § Waiting on Andres: system):
  do two open PRs on repos outside its roster count as its work? Its score
  snapshot already counts two of them among merged PRs.

**Stale in the systems' own lists** (resolved by your relock commits at 08:26;
each system's next session should clear them, nothing for you to do):
- zesty-eng-team: "relock owed", "charter line now false" and "reviewer is the
  kit v1 copy". Checked: boot "Locks intact (16 files)"; the carry-over line is
  gone from `docs/charter.md`; `change-reviewer.md` matches the kit.
- mpulse-engage-team: "settings.json not written" and "ask, not forbid not
  applied". Checked: `settings.json` has 121 ask rules and the six kit hook
  events; charter line 52 reads "without Andres's approval in the moment".

**Work lists (counts only):**
- zesty-eng-team: 6 work items, 2 older than 14 days.
- mpulse-engage-team: 5 work items, 4 older than 14 days.
- mpulse-dpi-team: 14 work items, 8 older than 14 days.

Also seen, for the systems' own loops: engage and dpi report a deeper pass due
(a new escape and S2 above baseline in their first snapshots), and dpi's boot
asks for an `env` event for a changed local settings file.

## Last asked

"What has changed?": never.
