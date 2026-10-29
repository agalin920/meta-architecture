# Human approval of every self-change

**Status:** `retired` (rulings 5 and 9). Includes "propose, never apply" and
"never edit a child repo".

**Lesson.** Routing every reversible change a system makes to its own notes and
rules through Andres made him the bottleneck on evolution, not its safeguard.
An approver who sees everything rubber-stamps, and his approval did not catch
changes that had no effect.

**Evidence**
- Almost every self-change was a reversible edit, and each waited for him:
  `REDESIGN.md:47-49`.
- personal-university: 3 of 4 approved proposals did not produce their effect:
  `personal-university: meta/architect-log.md:1160-1190`.
- zesty-eng-team's judge accepted almost all proposals (e.g. 4/4, 9/10, 13
  applied and 1 rejected) and records that high acceptance suggests an
  uncalibrated gate: `zesty-eng-team: .claude/commands/retro.md:46`.
- Parking on the human costs: a verified team defect sat 43 days because a
  team item in the Director's queue is read as the Director's:
  `zesty-eng-team: docs/decision-log.md:818`.
- Dispatch through the human had no write-back to the child's record:
  `archive/meta/architect-log.md:1603-1630`.

**What replaces it**
- Kernel 5 and 6: a reviewer agent that did not make the change, and automatic
  rollback against a named score. Andres still gates the charter, the
  scoreboard and the irreversible ([human-gate](human-gate.md)).

**Where it failed / limits**
- The children's rejections of this layer's proposals were evidence-grade
  (eleven of eighteen): `archive/patterns/README.md:221-225`. Judging must
  stay, by a reviewer instead of the human.

**Origin.** Founding (Architect proposes, human applies), 2026-08.
