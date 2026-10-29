# Current state

Rewritten in place, never appended to. The pre-redesign handoff is at
[`archive/HANDOFF.md`](archive/HANDOFF.md).

**As of 2026-10-28:** the colony migration ran today under
[`REDESIGN.md`](REDESIGN.md), on branch `colony-migration` in this repo and in
the three core systems. **Merged to `main` and pushed on 2026-10-29**, at Andres's
request, in all four repos (fast-forward; nothing on the remotes was overwritten).

## Where things stand

- **DNA:** `dna.md` states the kernel, the lesson statuses, the DNA rule and the
  harvest. The lessons catalog is in `dna/lessons/`.
- **Trials:** none open. The earliest possible candidate is 14 days after a
  core system's first self-change.
- **Core systems:** all three migrated to the kernel, with baselines recorded
  2026-10-28. See `systems.md`.
- **Side projects:** dormant and untouched. Lessons harvested.
- **Harvest:** the weekly `dna-harvest` task (Monday morning, Claude desktop
  app), plus this repo's boot.
- **Falsifier checks:** 2027-01-31 and 2027-03-31 (`meta/thesis.md`).

## Waiting on Andres

- Commit or leave the side projects' uncommitted work. Much of their measured
  evidence lives only there (`systems.md`).
- Run the `dna-harvest` scheduled task once from the app ("Run now") and
  approve its tools, so the Monday runs don't pause on permission prompts.

## Last asked

"What has changed?": never.
