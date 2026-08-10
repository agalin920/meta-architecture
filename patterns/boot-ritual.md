# Boot ritual

**Status:** `proven` — all three agentic systems
**Invented in:** convergent.

## The pattern

Before any decision, the agent reads a **named, ordered, mandatory** list of
files. Not "consult as needed" — an enumerated list, in sequence, every time.

## Why it works

An agent that starts fresh each session will otherwise re-derive state from
whatever is in front of it, which is the difference between a system and a
chatbot with a nice prompt. personal-university's README says it outright:
*"It reads its own history before every decision. Skip that and it's a chatbot
with a syllabus attached."*

The ordering carries meaning. Putting the review queue at position 5 *"before
anything else that could be scheduled"* encodes a priority rule inside the read
order itself, where it cannot be forgotten.

## Evidence

- `personal-university/agents/session-protocol.md` — 10 numbered items, "do not
  skip," with the review queue positioned deliberately.
- `zesty-eng-team/CLAUDE.md` — "Orient — every session, before anything else,"
  five steps ending in `git fetch && git status` against reality.
- `brand-system/agents/*.md` — each role carries its own read-list; the Writer's
  is "read the voice guide before every draft. No exceptions."

## How it fails

- **Growth.** Every incident adds a file to the list and nothing removes one.
  Pair with [overhead ceiling](overhead-ceiling.md).
- **Reading without reconciling.** zesty-eng-team adds the step that closes
  this: *"if `Current state` disagrees with what GitHub actually says, GitHub is
  right."* A boot ritual that reads only the system's self-description will
  faithfully load a stale world. **Every read-list should end with one check
  against external reality**, where the domain has one.
