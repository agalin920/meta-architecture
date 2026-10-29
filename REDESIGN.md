# Redesign: from architecture council to self-evolving colony

**Audience:** the coding agent carrying out this change.
**Author of the decisions:** Andres (the human owner), in a design session on
2026-10-28, after review 001. Every ruling below is his. Cite this file as the
authority for the changes you make.

Read this whole file before touching anything. It says what to build, why, what
must not be lost, and when you stop to show Andres your work. It does not give
you step-by-step instructions on purpose: you are expected to find the best way
to reach the outcome.

---

## 1. Why we are doing this

We first built these AI systems the way people build companies: managers,
roles, standups, retros and sign-offs, because that is the only shape of
collective work we knew. But those structures exist to work around **human**
limits: memory that fades, attention that runs out, and trust that has to be
earned one approval at a time. AI does not share those limits. Copying our org
charts caps it at our imagination.

So we stop designing the team. Each system gets a **purpose**, a **shared
memory**, an **honest way to know when it is winning**, and **freedom to
reshape itself**, including how it learns. The right specialists and ways of
working should emerge on their own, including ones Andres would never think to
invent. His role moves from managing the work to setting direction and watching
it grow.

**The guiding image is the spiders in *Children of Time*.** What one
generation learns is written into the DNA, so the next one is born already
knowing it. The spine is that DNA. Each system's hard-won lessons get written
back into it, and every new system starts smarter. The same book carries the
warning: bad lessons are inherited just as faithfully as good ones. **That is
why real-world results, not opinions or essays, decide what enters the DNA.**

## 2. The evidence that forced it

Review 001 (`meta/architect-log.md`, entry dated 2026-10-28) found:

1. **Everything that depended on Andres's attention stopped.** Retros only run
   when he types `/retro`. The-debrief printed "eleven slices overdue" in its
   own boot state and still never ran one. Five of nine Architects have never
   run. Every mechanism needing a recurring human step (`budget.md`, the
   student prediction, ambient input) was eventually cut.
2. **Every self-change waits for his approval**, even though almost all of them
   are edits to the system's own notes and rules, which are reversible in
   seconds. He is the bottleneck on evolution, not the safeguard for it.
3. **The promotion engine can barely turn.** A pattern becomes `proven` only
   when two systems invent it independently, but every new system is grown
   from the spine, so it can never independently invent what it already
   inherited. Nine of ten `proven` patterns fail that bar.
4. **The meta layer is too heavy.** `meta/architect-log.md` is about 3,500
   lines, mostly essays about its own rules. The memory works; the
   compression does not.
5. **What did work:** Architects grade themselves honestly when they run; the
   changes that survived are the ones that **measure a number or force a
   trade-off**; and zesty-eng-team's second reviewer on its improvement
   proposals caught real mistakes, including a proposal to delete a rule that
   was still true.

## 3. Before and after

| | Before | After |
|---|---|---|
| Image | Company headquarters with branch offices | A colony whose DNA carries what it learned |
| A system is | An engineering team: manager, roles, rituals | Memory + a learning loop, with whatever structure it grows |
| Improvement | `/retro`, triggered by Andres | Continuous, part of normal work, never waiting on a person |
| Who approves self-changes | Andres, every one | An independent reviewer agent; Andres only when it is unsure |
| What Andres gates | Almost everything | The charter, the scoreboard, and irreversible or outside-world actions |
| How he follows along | Reading logs and proposals | A plain-language changelog: "what changed and did it help?" |
| How a lesson enters the DNA | Two independent inventions (almost never happens) | It measurably helped somewhere, and still helps when tried elsewhere |
| Meta layer | Architecture council that proposes and never edits children | DNA keeper that harvests lessons and can write them into children |

**Where it is better:** faster evolution, far less friction for Andres, it fits
any kind of project, and he can read a clear story of how each system changed.

**Where it is worse, and the guard for each:**

1. Systems can drift in bad directions between his look-ins. *Guard: a
   scoreboard the system cannot edit, plus automatic rollback.*
2. He loses the deep understanding that came from approving each change.
   *Guard: the changelog, written for him in plain language.*
3. A bad lesson can spread faster under looser proof rules. *Guard: a lesson
   enters the DNA only on measured results in more than one system, and the
   DNA changes more slowly than any system.*

## 4. Andres's rulings (2026-10-28)

These settle review 001's open items and set the new direction. Record them in
the meta layer's history as rulings.

1. **Founding status: accepted** (review 001, M-1, option A). The original spine
   invariants are labelled `founding`. Stop trying to re-prove them through
   independent invention.
2. **Core vs side projects.** The three core systems are **zesty-eng-team,
   mpulse-engage-team and mpulse-dpi-team**. They always matter and get the
   full migration. Everything else (personal-university, brand-system,
   galind-team, the-debrief, resale-desk, zesty-webengine-team) is a side
   project. **A quiet side project is paused, not failed.** The layer stops
   treating inactivity as something to fix. Side projects may die, and that is
   fine.
3. **Compact the meta layer's memory.** Keep every lesson and every result;
   compress the debate. Nothing is deleted from history.
4. **Rituals are optional.** Manager, standup and retro are no longer part of
   the spine. The spine states the goal of the learning loop, not its form.
   The improvement method itself may evolve.
5. **Self-changes do not need Andres's approval.** A reviewer agent that did not
   make the change checks it, lets routine changes through, and escalates to
   him only when unsure.
6. **Andres still gates:** the charter, changes to what the scoreboard
   measures, and anything irreversible or touching the outside world (section
   6).
7. **The scoreboard can evolve, through a slower door.** The goal in plain words
   is fixed. The measurements under it can change, but a new one is **added
   next to** the old ones, never swapped in quietly, and Andres okays it.
8. **Subagents are a starting crew, not an org chart.** Existing agents stay
   and may be tuned, merged, retired or invented by the system. Every such
   change lands in the changelog.
9. **The "never edit a child repo" rule is revoked.** The meta layer may now
   change child systems directly, with everything logged and reversible.
10. **Full migration of the core systems**, with permission to restructure
    whatever is needed, **as long as no knowledge or memory is lost.**
11. **Any session is the colony.** There is no manager persona. Whatever
    session Andres opens knows what the colony knows, pulls in subagents as
    needed, and answers two kinds of request: "here's what I want" and "what
    has changed?"
12. **Company boundaries hold.** Zesty and mPulse systems work in their own
    repos and never exchange domain content. The DNA carries mechanism only.
    This repo is public, so nothing employer-internal ever enters it.
13. **Token cost is not a constraint.** Do not trade quality for spend.

## 5. The kernel: what every system is built from

This replaces "what every system inherits" in `spine.md`. Keep it small enough
to state on one page. Everything else becomes an optional add-on in the
catalog.

1. **Purpose (locked).** A charter with the goal in plain words and the hard
   lines (section 6). Andres owns it. Agents cannot edit it.
2. **Memory.** Three layers, each doing one job:
   - an **event log**: append-only, and **committed** (an uncommitted log is
     neither append-only nor a log; review 001 found six of ten systems with
     uncommitted state);
   - **current state**: rewritten in place, read at boot;
   - **knowledge**: what is true and not otherwise recoverable, maintained
     rather than merely appended (mpulse-dpi-team's finding: stale facts, not
     filler, are the real failure).
3. **The loop.** After every unit of work, the system notices what happened,
   compares it to what it expected, and changes itself if that helps. No human
   trigger. A light check every unit; deeper changes when the scores or the
   evidence say so. How it does this is the system's own business and may
   evolve.
4. **Scoreboard (locked).** The goal in plain words, plus measurements computed
   **by scripts from outside data** wherever possible (GitHub reviews, Jira
   bugs, reverts, sales), not hand-reported. Keep the honest-metric discipline:
   name what is not measured.
5. **Self-change reviewer.** An agent that did not make a change reviews it
   before it lands. Routine and clearly beneficial: it lands. Unsure, or it
   touches anything gated: it escalates to Andres.
6. **Rollback.** Every self-change is its own commit, tied to a changelog entry
   that states the expected effect and which score should move. If the score
   worsens, or the expected effect does not appear within a stated window, the
   change is reverted and the failure is kept as a lesson.
7. **Changelog.** A plain-language record of how the system evolved: what
   changed, why, what it was expected to do, and whether it did. Written for
   Andres, readable in two minutes. This is how he answers "what has changed?"
8. **DNA link.** Lessons that prove out locally are marked as candidates for
   the DNA; lessons from the DNA can be received and trialled.

Keep a boot read-path budget in every system (`overhead-ceiling` is the one
founding pattern that survived the audit). Keep the untrusted-input boundary as
a default for any system that reads content it did not write.

## 6. What stays gated, and how it is enforced

**Gated by Andres:**

- the charter (purpose and hard lines);
- adding or changing a scoreboard measurement;
- anything irreversible or outside-world: merging or pushing to shared
  remotes, shipping code, sending messages or email, spending money,
  publishing, credentials, deleting data, and **anything touching patient data
  (PHI) on the mPulse platform**;
- reviewer escalations.

**Enforce with locks, not just words.** Put the fixed parts physically out of
the agent's reach using `.claude/settings.json` deny rules in each system: the
charter, the scoreboard scripts and their definitions, and **the settings file
itself** (otherwise the agent can remove its own lock). Keep every existing deny
rule that protects product repos, sibling repos and shared company tooling.

**Test every lock.** `systems.md` notes that `Write(...)` deny rules may be
inert and only `Edit(...)` is matched. Do not trust that note or the rule
text: in each system, attempt an edit to a locked file from a session in that
repo and confirm it is refused. Report the result.

## 7. The DNA (the meta layer's new job)

The meta layer becomes the keeper of the DNA. It harvests lessons from the
systems, trials them elsewhere, and writes the proven ones into what new
systems are born with.

- **Lesson statuses.** `founding` (the original invariants, ruling 1);
  `candidate` (measurably helped in one system); `proven` (helped in one
  system, then **still helped when tried in another**. A carried trial now
  counts, because it is a real test); `retired` (tried and failed, kept with
  the reason so nobody reinvents it).
- **The DNA changes more slowly than any system,** because a change there
  reaches everything born afterwards. Define what "slower" means concretely
  (for example, a minimum number of units or days a lesson must hold in its
  second system).
- **Harvesting must not depend on anyone remembering.** Choose a trigger that
  runs on its own (a scheduled task, harvesting at the boot of any session,
  or something better), and say which you chose.
- **Mechanism only across companies.** A lesson from a Zesty system may be
  trialled in an mPulse system and the reverse, as mechanism. No code,
  tickets, practices or internals cross.
- The meta layer runs the same kernel as every child: its own scoreboard,
  changelog, reviewer and rollback. It is not exempt from itself.

## 8. Open design questions you must answer in Phase 1

Propose an answer to each, with your reasoning. A sensible default is given;
improve on it if you can.

1. **Compaction.** How memory compresses without losing lessons. *Default:*
   when a file exceeds its budget, distil it into knowledge and lessons and
   move the raw text to an `archive/` folder that is kept but not on the boot
   path. Compaction may drop prose. It may never drop a lesson, a result, a
   decision or a number. The reviewer checks compaction diffs specifically,
   because that is where knowledge silently disappears.
2. **The starting scoreboard for each core system.** *Default:* the goal is
   roughly "ship working software with zero defects, using less of Andres's
   time." Start from what each system already measures (external-reviewer
   blockers per PR, Director/Manager findings per unit, escape rate, routing
   errors, knowledge staleness) and move each measure to a script fed by
   GitHub and Jira. Add escape tracking (bugs and reverts traced back to the
   PR), which nothing measures well today.
3. **Effortless human signal.** Andres's corrections are the best signal, but he
   will not fill in forms. *Default:* capture them automatically: his PR review
   comments, reverts, edits he makes to agent output, and corrections he gives
   in chat, written to the event log by the session that sees them.
4. **Rollback triggers.** What exact condition reverts a change, over what
   window, and who notices. *Default:* the reviewer agent checks each open
   change's named score after a set number of units and reverts if it got
   worse or did not move as claimed.
5. **The DNA rule.** The concrete "still helps in a second system" test and the
   "slower than any system" threshold from section 7.

## 9. Scope of the migration

**Repos** (all under `~/dev/`):

- `meta-architecture`: fully rewritten around this design.
- `zestyio/zesty-eng-team`, `mpulsemobile/mpulse-engage-team`,
  `mpulsemobile/mpulse-dpi-team`: **full migration.**
- Side projects (`personal-university`, `brand-system`, `galind/galind-team`,
  `the-debrief`, `resale-desk`, `zestyio/zesty-webengine-team`): **do not
  modify them.** Read them, harvest their lessons into the DNA, and mark them
  `dormant` in the registry. Several have uncommitted work (the-debrief 46
  files, resale-desk a charter amendment and 109 events, galind-team ticket 001
  plus the uncommitted `galind-email` repo, brand-system 8 files and 3 unpushed
  commits). Leave all of it exactly as it is. A side project gets migrated when
  Andres revives it.
- `media-log` is a dataset, not a system. Leave it alone.

**Never touch:** product and subject repos (`manager-ui`, `studio-bridge`, the
mPulse service repos, the DPI repos under `dpi/`, `galind-*` product repos) and
`agentic-development-tools`, which mPulse owns.

**In each core system, the migration must:**

- rewrite the charter around purpose, hard lines and scoreboard;
- replace `/retro` with the continuous loop (you may keep a manual command for
  a deep pass, but nothing may depend on it being run);
- add the self-change reviewer, rollback, changelog and a way to ask "what has
  changed?";
- turn the existing subagents into the starting crew, marked as free to evolve;
- keep the work commands (`/take-ticket`, `/review-pr`, `/address-feedback`,
  `/triage` and the rest) working, adapted as needed;
- carry over **all** knowledge, decisions, logs and tickets, compacted where
  over budget, with the raw originals archived;
- preserve every safety boundary, especially the PHI boundary and the deny
  rules on sibling, product and shared repos;
- add locks and test them (section 6);
- **record baseline scores** before any self-change happens, so evolution can be
  judged against a real "before."

**In meta-architecture, the migration must:**

- rewrite `charter.md`, `spine.md` (rename it to something like `dna.md` if that
  reads better, and fix every link), `README.md`, `HANDOFF.md`, `systems.md`
  and `meta/thesis.md`;
- keep a falsifiable thesis: state what result would prove this redesign wrong
  (for example, core-system scores flat or worse after two months of free
  evolution compared with the baseline, or reviewer escalations so frequent
  that Andres is back in the middle of everything);
- replace `meta/dispatch.md` and `meta/architect.md` with the DNA-keeping
  procedure;
- restructure `patterns/` around the new statuses, applying `founding`;
- archive `meta/architect-log.md` verbatim under `archive/` and write a compact
  record of every lesson, ruling and result from it;
- fold in review 001's M-3 (read `git status` beside `git log`) and M-5 (the
  uncommitted-log failure mode); M-2 and M-4 are superseded by this design;
- record these rulings.

## 10. Safety rules for doing the migration itself

1. **Snapshot first.** Before changing any repo, tag its current HEAD
   (`pre-colony-2026-10`). If the working tree has uncommitted changes, commit
   them as-is in a snapshot commit on the migration branch before anything
   else, so nothing in flight is lost.
2. **Work on a branch** named `colony-migration` in each repo, created from the
   currently checked-out HEAD. Do not switch, rebase, merge or rewrite existing
   branches. mpulse-engage-team is on `program-build-skill`, 35 commits ahead
   of `origin/main`; branch from it and say so in your report.
3. **Do not push and do not merge.** Andres merges and pushes after reviewing.
4. **Never delete knowledge.** Move it to `archive/` instead. For each repo,
   produce a mapping of every pre-migration knowledge, decision and log file to
   where its content now lives. Nothing may be unaccounted for.
5. **Keep it small.** The old layer's failure was weight. The kernel fits on a
   page, boot paths stay inside their budgets, and when in doubt, add nothing.

## 11. Order of work and the one checkpoint

- **Phase 0: inventory and snapshot.** Read everything in scope, tag, snapshot,
  and confirm you can edit each in-scope repo. Change nothing else yet. If this
  file sits outside `meta-architecture`, copy it into that repo's
  `colony-migration` branch as `REDESIGN.md` (the decision record), and commit
  it there.
- **Phase 1: design, then stop.** Present to Andres, in plain language:
  - the new meta charter and the new charter for each core system (goal, hard
    lines, scoreboard);
  - the kernel as it will be written into the DNA;
  - your answers to the five open questions in section 8;
  - your migration plan per repo.

  **Then stop and wait for his approval.** Charters and scoreboards are the
  things he owns, so this is the only stop in the whole job.
- **Phase 2: migrate.** Meta-architecture first, then zesty-eng-team as the
  pilot, then mpulse-engage-team and mpulse-dpi-team. Carry lessons from the
  pilot into the next two.
- **Phase 3: verify.** In each core system: the locks refuse edits; the
  scoreboard scripts run and the baselines are recorded; the knowledge mapping
  is complete; and the loop, run against the most recent completed unit of
  work, produces a sensible result end to end, reviewer included.

## 12. Definition of done

Andres can open any session in a core system and:

- say what he wants, and the system does it, bringing in whatever subagents it
  needs;
- ask "what has changed?" and get a short, honest story of how the system
  evolved and whether each change helped;
- never be asked to start a retro or approve a routine self-change.

And:

- nothing from before the migration is lost, and the mapping proves it;
- the charter, scoreboard and settings are locked, and the locks were tested;
- baseline scores exist for every core system;
- the DNA states the kernel, the lesson statuses and the harvest trigger, and
  is shorter than today's `spine.md` plus `patterns/README.md`;
- every repo has a `colony-migration` branch, unpushed, with a plain-language
  summary of what changed.

**Final report to Andres:** short and in plain language. What changed in each
repo, the branches to merge and push, the baseline scores, anything you could
not do, and these questions for him:

- Is zesty-webengine-team running somewhere this layer cannot see, or is it a
  dormant side project?
- Anything else you could not resolve on your own.

## Amendment 2026-10-29: trust over gates

Andres's ruling, the day after the migration: "give the AI more trust and
ability to evolve and do its own thing … not gated by humans." It amends
§ 5 (reviewer, rollback) and § 8 question 4 (rollback triggers); everything
else stands: locks, charters, outside-world asks, patient-data rules, the
playbook flow, hooks.

- **Keep by default.** At about two merged PRs a week the per-change verdict
  is mostly noise: a change that does nothing reads "helped" or "worse" about
  40% of the time each. Verdicts become evidence the system reads. *Helped*:
  keep, playbook candidate. *No effect*, or insufficient data at the 60-day
  cap: keep, "unproven". *Looks worse*: the system decides on its own
  judgement and records a `decision` event; it is reported, not escalated.
  A change is reverted only for clear harm: an escape traced to it, Andres
  saying it made things worse, or the system's own judgement.
- **Guardrails.** S1 (escapes) and S4 (escalations) cannot be claimed. Both are
  printed beside every verdict, over the same windows, as counter-metrics.
- **Reviewer as second opinion.** Decisions are `LAND`, `CONCERN` (the system
  may land anyway and records why) and `ESCALATE`, which is kept for changes
  that weaken a hard line or safety instruction, change how evidence is
  recorded, or trace back to outside content. `REJECT` is gone.
- **S3 is no longer self-graded.** It counts Andres's follow-ups per merged
  PR: every prompt in a session after its first, from the hook-written prompt
  log (time and session only), plus unmarked GitHub comments and untrailered
  commits. `correction` events stay as learning evidence and are not scored.
  Agents may not write the raw prompt log.
