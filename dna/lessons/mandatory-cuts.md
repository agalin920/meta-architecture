# Mandatory cuts, with a written "no"

**Status:** `candidate`.

**Lesson.** Every improvement pass states what should come out. "Nothing should
be cut this cycle, because…" is a valid answer and must be written, since a
blank cannot be told apart from a section nobody wrote. A removal quota is not
this lesson.

**Evidence**
- Before it: across 189 commits and four retros, no applied rule had ever been
  removed: `archive/patterns/overhead-ceiling.md:56-61`.
- zesty-eng-team (carried, MF-1) wrote the two-state rule
  (`zesty-eng-team: .claude/agents/architect.md:88-95`). It fired at retro 5
  with three cuts (`zesty-eng-team: docs/decision-log.md:624`) and again at
  retros 6, 7 and 8: `archive/meta/architect-log.md:3461`.
- mpulse-engage-team, the origin, asked and answered: its retro 001 proposed a
  cut and the judge rejected it with a reason:
  `archive/patterns/README.md:451-455`.

**Where it failed / limits**
- **A cut can be wrong.** One of retro 5's three cuts would have deleted a
  blocker that was still true; pass 2 caught it. Keep the adversary
  ([self-change-adversary](self-change-adversary.md)).
- **A quota would cut something load-bearing**: rules unfired for reasons
  unrelated to whether they work: `archive/patterns/README.md:462-465`.
- **Untested in new systems:** no born system ever ran a first retro, so the
  cut test there has no datapoint:
  `archive/meta/architect-log.md:3422-3424`.

**Origin.** mpulse-engage-team (`.claude/agents/architect.md`, § Cuts),
2026-08-13; carried to zesty-eng-team 2026-08-14.
