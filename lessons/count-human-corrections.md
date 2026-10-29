# Count the human's corrections where they happen

**Status:** `candidate`.

**Lesson.** The human's corrections are the best signal a system gets. Count
them where they actually happen (chat as well as review comments), and turn a
recurring one into a rule whose effect is then measured.

**Evidence**
- zesty-eng-team counted 19 requests to shorten, median reply 224 words
  (n=230), and made "answer first, under 150 words" a rule:
  `zesty-eng-team: docs/decision-log.md:811`. Next window: median 168 words,
  5 shorten requests (`:890`).
- It counts Director findings "from wherever they said it"; a review-comment
  count alone read zero where real defects were caught:
  `zesty-eng-team: .claude/agents/architect.md:62`.
- mpulse-engage-team: a production diff went 129 → 30 lines after two pushbacks
  and became a rule: `mpulse-engage-team: docs/decision-log.md:411-416`.
- mpulse-dpi-team logs every correction under one heading:
  `mpulse-dpi-team: CLAUDE.md:108`.

**Where it failed / limits**
- **Partial:** 55% of zesty-eng-team replies were still over 150 words.
- **What the human misses is counted nowhere.** Escape tracking has no feed:
  `archive/patterns/README.md:316-323`.
- mpulse-dpi-team's ~40 logged corrections were never aggregated into a count.
- He will not fill in forms; capture must be automatic (phase-1 §4.3).

**Origin.** zesty-eng-team, 2026-08; named at this layer 2026-08-14 as "the
human driver as primary feedback".
