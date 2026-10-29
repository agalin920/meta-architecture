# Keeping the playbook

The procedure for this layer's one job. It replaces `meta/architect.md` (the
quarterly review) and `meta/dispatch.md` (carry-packets). Both are archived
under [`archive/meta/`](../archive/meta/). It runs:

- **weekly**, from the "Weekly lessons review" scheduled task;
- **at the boot of any session in this repo**;
- when Andres asks.

It is idempotent: running it twice does nothing new.

## 1. Read what changed (read-only)

For each **core** system (zesty-eng-team, mpulse-engage-team, mpulse-dpi-team):

- `git -C <repo> log` and **`git -C <repo> status`**. A system with uncommitted
  memory looks idle in `git log` and is not (review 001, M-3).
- Its `CHANGELOG.md`: new self-changes, verdicts and reverts.
- Its `lessons.md`: new `candidate` and `retired` lessons.
- Its scoreboard: `python3 scoreboard/score.py --summary`, run in that repo.
- Its boot check: `python3 .claude/hooks/boot_check.py < /dev/null`, run in
  that repo. **A `LOCK BROKEN` goes straight to Andres.**

Side projects are dormant. Read them only if Andres revives one.

## 2. Collect

For each new candidate or retirement:

- Write or update `lessons/<slug>.md` with the system, the change, the claim
  and the verdict numbers.
- **Mechanism only.** Strip every product, ticket, code, company or regulatory
  detail before it enters this public repo. If the lesson cannot be stated
  without them, it stays local.
- **A retirement is worth as much as a promotion.** Write it with the reason.

## 3. Choose trials

A `candidate` may be trialled in another core system whose own scoreboard
could show the same effect.

- Write one entry to [`trials.md`](../trials.md), addressed to that
  system, with the lesson, the claim to test, and the source verdict.
- **Cross-company trials carry mechanism only.**
- At most **one open trial per system** at a time, so its verdicts stay
  readable.

## 4. Judge trials

When a trial's verdict lands in the receiving system's changelog:

- **Helped**: once it has held there for 10 units and 30 days with its score
  not worse, mark the lesson `proven`.
- **Worse or no effect**: the lesson stays local. Mark it "does not transfer"
  with the numbers.

## 5. Update the playbook (at most monthly)

Proven lessons enter `playbook.md` in **one batch per month**, through this layer's
own `change-reviewer`. A change that would weaken a kernel guard goes to Andres.

## 6. Roll up what is waiting on Andres

Every run, rewrite the section `## Waiting on Andres — from the systems` in
`HANDOFF.md` from scratch. For each core system, list:

- each open proposal in `log/pending/S-*.md`: its id, kind, one-sentence change,
  and "approve: `scoreboard/apply S-NNN` in that repo";
- the count of other items under its `## Waiting on Andres`, with the oldest
  one in a line;
- `LOCK BROKEN`, first and loudest, if any boot check printed it.

If anything is listed, send Andres **one** push notification: how many items
are waiting, and the single most important one. Send nothing in a week where
nothing is waiting. The roll-up only reports; deciding stays with Andres, in
the system concerned.

## 7. Keep this layer's own kernel

- Record each run as a `review` event in `log/`.
- Compute this layer's scoreboard: `python3 scoreboard/score.py`.
- Take this layer's own self-changes through `kit/docs/loop.md`, as every
  system does.
- Check [`thesis.md`](thesis.md)'s falsifier on its dates.

## What this layer may and may not do

- **May** edit core systems directly when Andres runs it (ruling 9). Log it in
  that system's changelog, one reversible commit per change, through that
  system's reviewer.
- **May not:**
  - write into a child's working tree from the unattended weekly run;
  - change any charter or scoreboard measure;
  - touch side projects, product repos, `media-log` or
    `agentic-development-tools`;
  - push or merge anything.

**No finding without an executed check.** Every claim about a system cites the
command run in that system's repo and what it returned. In the old dispatch
record, ten of eleven rejections were the same failure: an assertion about a
target repo that nobody had checked in that repo.
