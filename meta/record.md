# Meta record: lessons, rulings and results from the architect log

This is the compact record of the meta layer's history from 2026-08-09 to 2026-10-28, written under the redesign (ruling 3, REDESIGN.md §4).
The verbatim log, 3,532 lines, is at `archive/meta/architect-log.md`. Its line numbers are unchanged, and every citation below points into it.
This record keeps every lesson, every ruling by Andres, every measured result and every decision. It drops the debate, the restated arguments, and the line-by-line evidence trails.
The "Lessons" section gives each lesson a standing: `kept` means it is still true under the colony design; `superseded` names the redesign element that replaced it; `retired` means it no longer applies.
Employer-internal detail is left out on purpose (ticket and PR identifiers, tracker keys, employer repo and file names, regulation names). The verbatim archive holds whatever was there.

## Rulings

### 2026-10-28: the colony redesign (REDESIGN.md §4)

Every ruling here is Andres's. Each line paraphrases REDESIGN.md §4 closely.

1. **Founding status accepted** (review 001 M-1, option A). The original spine invariants are labelled `founding` and are no longer re-proved through independent invention.
2. **Core vs side projects.** The core systems are zesty-eng-team, mpulse-engage-team and mpulse-dpi-team. Everything else is a side project. A quiet side project is paused, not failed, and side projects may die.
3. **Compact the meta layer's memory.** Keep every lesson and result and compress the debate. Nothing is deleted from history. This file is the result.
4. **Rituals are optional.** Manager, standup and retro leave the spine. The spine states the learning loop's goal, not its form, and the method itself may evolve.
5. **Self-changes do not need Andres's approval.** A reviewer agent that did not make the change checks it, passes routine changes, and escalates only when it is unsure.
6. **Andres still gates** the charter, changes to what the scoreboard measures, and anything irreversible or touching the outside world.
7. **The scoreboard evolves through a slower door.** The plain-words goal is fixed. A new measure is added next to the old ones, never swapped in, and Andres okays it.
8. **Subagents are a starting crew, not an org chart.** The system may tune, merge, retire or invent agents. Every such change lands in the changelog.
9. **"Never edit a child repo" is revoked.** The meta layer may change child systems directly, with everything logged and reversible.
10. **Full migration of the core systems**, restructuring whatever is needed, provided no knowledge or memory is lost.
11. **Any session is the colony.** There is no manager persona. A session answers two requests: "here's what I want" and "what has changed?".
12. **Company boundaries hold.** Zesty and mPulse never exchange domain content, and the DNA carries mechanism only. This repo is public, so nothing employer-internal enters it.
13. **Token cost is not a constraint.** Do not trade quality for spend.

Andres's Phase 1 answers, 2026-10-28 (design/phase-1.md §7):

- zesty-webengine-team is not a running system and is registered `dormant`. The Zesty core system is zesty-eng-team. This answers review 001's ask 4.
- The weekly harvest task is approved. It is a desktop-app scheduled task (`dna-harvest`) that catches up on next launch.
- Close the guard gaps: yes.
- The flagged PHI (one test-member identifier in an engage worklog) is removed from the current file on engage's migration branch. Earlier history was not rewritten.
- The architect log is archived verbatim. That is `archive/meta/architect-log.md`.
- Engage's build-team skill is kept as is and reworked later.

Review 001's proposals and asks, as settled on 2026-10-28:

- **M-1 accepted as `founding`** (ruling 1). The nine pre-bar invariants move to `founding`, and `overhead-ceiling` keeps `proven`. archive/meta/architect-log.md:3482-3484
- **M-3 folded into the kernel:** read `git status` beside `git log`, and the registry carries an *uncommitted* column. archive/meta/architect-log.md:3488-3489
- **M-5 folded into the kernel:** "an append-only log that is not committed is neither append-only nor a log". archive/meta/architect-log.md:3492-3494
- **M-2 superseded** by the continuous loop (ruling 4). M-2 had proposed cutting the Architect audit to "has it run" and rewriting claim IV. archive/meta/architect-log.md:3485-3487
- **M-4 superseded** by the redesign's falsifier (design/phase-1.md §6.5). M-4 was the sharper engine falsifier. archive/meta/architect-log.md:3490-3491
- Ask 2 (status of the six stopped systems) is answered by ruling 2: they are side projects, `dormant`. Ask 3 (their uncommitted work) is answered by REDESIGN.md §9: leave it exactly as it is. archive/meta/architect-log.md:3508-3515

### Earlier rulings in the log

- 2026-08-09: Andres accepted review 000's F2 (BS handoff record) and F3 (PU in-progress marker) and applied them himself. archive/meta/architect-log.md:157-160
- 2026-08-09: `budget.md` was cut unfilled because he declined to state weekly capacity. F5 was withdrawn, not resolved, and falsifier 3 was restated. archive/meta/architect-log.md:181-198
- 2026-08-10: the purpose was restated as two jobs on two clocks: generative (on demand, `spine.md` created) and evolutionary (quarterly). archive/meta/architect-log.md:229-249
- 2026-08-10: the kill condition ("two reviews with no cross-system finding deletes the repo") was removed. A bar on action replaced it: the spine does not change until children earn the change. archive/meta/architect-log.md:254-263
- 2026-08-10: the founding convergence claim was withdrawn, since four systems by one person in two days are one derivation. Review 001's first job was set as re-auditing the `proven` statuses. archive/meta/architect-log.md:270-292
- 2026-08-10: `meta-architecture` was made public by a deliberate decision. archive/meta/architect-log.md:1029
- 2026-08-13: both 001a packets were dispatched on his verbal instruction before any charter amendment. That covered the one instance and did not move the boundary. archive/meta/architect-log.md:757-761
- 2026-08-13 (publication note): `inbox/`, the per-repo external-review coverage map, and target-repo PR and ticket identifiers are held back. Nothing else is cut or softened. archive/meta/architect-log.md:1025-1054
- 2026-08-14: he commissioned an off-cadence advisory with a wider read than `meta/architect.md` permits. archive/meta/architect-log.md:1069-1074
- 2026-08-14: he approved both teams' offered self-found fixes, and each team applied its own. archive/meta/architect-log.md:1266-1270
- 2026-08-14: he approved all seven 001a/advisory accepts. Not approved: the charter dispatch amendment (open 7), MF-7, and the deny list (open 9). archive/meta/architect-log.md:1502-1506
- 2026-08-14: the application dispatch was authorised to write (Edit/Write allowed, push denied). archive/meta/architect-log.md:1517-1520
- 2026-08-14 goal ruling 1: the engine is the product and delivery is the constraint. The constraint wins in the moment and the product wins in the schedule. archive/meta/architect-log.md:1829-1831
- 2026-08-14 goal ruling 2: earned autonomy, scoped small. Process and knowledge change-classes may graduate to post-hoc review. Work product, roster changes and final calls never graduate. archive/meta/architect-log.md:1832-1836
- 2026-08-14 goal ruling 3: the engine scoreboard is births, promotions and transfer yield, plus a two-quarter falsifier. archive/meta/architect-log.md:1837-1839
- 2026-08-14 goal ruling 4: the human driver is the primary external feedback channel, with a miss-rate clause and two instruments (escape tracking, calibration sample). archive/meta/architect-log.md:1840-1843
- 2026-08-14 goal ruling 5: the sharing bridge is this layer, carrying architecture only. AF-5's peer channel is rejected across companies, and cadence is quarterly with a human flag as the fast path. archive/meta/architect-log.md:1844-1849
- 2026-08-14 goal ruling 6: a hands-on Director, permanently the major gate, with the bandwidth ceiling accepted as the cost of quality. archive/meta/architect-log.md:1850-1851
- 2026-08-14 goal ruling 7: no birth is forced, and a toy system counts for nothing. If there is no real domain, the falsifier fires honestly. archive/meta/architect-log.md:1852-1853
- 2026-08-14 goal ruling 8: mpulse-dpi-team is `active — low-cadence, by decision`. Its wake-up item is to fix four command files routing the tracker through a dead MCP, which made a false sanitisation claim. archive/meta/architect-log.md:1854-1859
- 2026-08-14: open 7 closed (dispatch amendment applied to `charter.md`). Open 9 closed (`.claude/settings.json` deny list on `../**` and child paths, both verbs, applied on his instruction). archive/meta/architect-log.md:1863-1871
- 2026-08-15: he instructed all four AR proposals applied. AR-4 (self-claims carry an executed check or an *unverified* label) went into `meta/architect.md` § Output. archive/meta/architect-log.md:1885-1891, 1926-1933
- 2026-08-19: he asked for zesty-webengine-team for a colleague, and instructed that no personal name enter the repo. archive/meta/architect-log.md:2286-2289, 2372-2377
- 2026-08-22: galind-team was born on his domain, with Andres as Director, product owner and gate. He ruled that the product takes `galind.io` and the personal brand moves. archive/meta/architect-log.md:2434-2435, 2530-2532
- 2026-08-24: the-debrief was born from his proposal draft v0.2. Not creating a git remote was his call. archive/meta/architect-log.md:2634-2640
- 2026-08-29: resale-desk was born on his request: find wants and flips (primarily Vinted), then, added mid-session, sell his items and draft listings. archive/meta/architect-log.md:2866-2870
- 2026-08-29: the same day, he overturned three founding rulings. The desk may drive his signed-in browser on both markets and post his sell listings. Buying, scheduling and disguise stay forbidden. archive/meta/architect-log.md:3122-3125, 3179-3193

## Entries

| id | date | type | archive lines |
|---|---|---|---|
| E0 | — | header and entry template | 1-36 |
| E1 | 2026-08-09 | Review 000: founding entry, F1–F5, applied and withdrawn the same day | 38-225 |
| E2 | 2026-08-10 | Entry 000b: purpose restated by Andres | 227-317 |
| E3 | 2026-08-08 → 08-13 | Review 001a: scoped review of the two engineering teams, MF-1–MF-9 | 319-750 |
| E4 | 2026-08-13 | Review 001a: dispatch record and supersessions, MF-10 | 752-996 |
| E5 | 2026-08-13 | Review 001a: closed | 998-1021 |
| E6 | 2026-08-13 | Publication note (Andres's decision) | 1023-1065 |
| E7 | 2026-08-14 | Advisory: holistic assessment, AF-1–AF-7 | 1067-1158 |
| E8 | 2026-08-14 | Advisory: dispatch record | 1160-1277 |
| E9 | 2026-08-14 → 08-15 | Rulings on SQ-1–SQ-3, then application dispatches and validation | 1279-1813 |
| E10 | 2026-08-14 | Rulings on the goal (eight rulings) | 1815-1881 |
| E11 | 2026-08-15 | Architectural proposals AR-1–AR-4, with dispatch and application | 1883-2029 |
| E12 | 2026-08-18 | Scoped read of two child retros, F-1–F-6, first promotion | 2031-2282 |
| E13 | 2026-08-19 | Birth: zesty-webengine-team | 2284-2426 |
| E14 | 2026-08-22 | Birth: galind-team | 2428-2630 |
| E15 | 2026-08-24 | Birth: the-debrief, built by the layer itself | 2632-2862 |
| E16 | 2026-08-29 | Birth: resale-desk, with a same-day partial withdrawal | 2864-3201 |
| E17 | 2026-08-19 → 10-28 | Review 001: full portfolio | 3203-3532 |

## Results

Abbreviations: ZET is zesty-eng-team, MET is mpulse-engage-team, MDT is mpulse-dpi-team, WET is zesty-webengine-team, PU is personal-university, BS is brand-system, ML is media-log.

### 2026-08-09: Review 000

- Commits at registry: ZET 62, PU 21, ML 18, BS 5. All four systems were at most two days old. archive/meta/architect-log.md:45-47
- BS README described a state the repo had left (16 pipeline items and 5 decision-log entries existed). archive/meta/architect-log.md:74-80
- Zero Architect reviews had been completed anywhere in the portfolio. archive/meta/architect-log.md:110-113
- Falsifier 1 check: 3 of 5 findings were within a local Architect's reach, so entry 000 did not clear the bar. archive/meta/architect-log.md:138-141

### 2026-08-13: Review 001a and its dispatch

- ZET went from 62 to 138 commits (+76) with 3 Architect runs. MET went from 1 to 51 (+50) with 1 run. Four of six systems were not read. archive/meta/architect-log.md:345-355
- ZET's Architect graded its prior cycle proposal by proposal. P3, P5, P6 and P9 worked. P2 fired, then drifted. P4 and P7 were inert. P8 failed four more times and was replaced. This is the only portfolio instance of a change that was applied, measured, falsified and replaced. archive/meta/architect-log.md:370-376
- MET's drift check against the employer's shared toolkit found real drift (+38/−2 across three files). archive/meta/architect-log.md:386-390
- MET read-path cap: 1,300 lines against an actual 1,056, so it never bound. Its `gates.py` had 12 of 12 declared gates unrecorded. `verify_docs.py` (244 lines) passed 6 of 6 assertions. archive/meta/architect-log.md:410-418
- Five catalog candidates and zero promotions. Four of five had one adopter and nothing measured. archive/meta/architect-log.md:422-436
- Instruction-file totals as re-derived: ZET 679→777, MET 957→1,270. The brief's 447→584 and 742→942 did not reproduce. Net change: ZET +155/−47, MET +209/−21. archive/meta/architect-log.md:576-586
- Zero applied rules were retired across 138 + 51 commits. archive/meta/architect-log.md:595-599
- Structural self-assessment produced four instances and four declines, all about roles. archive/meta/architect-log.md:615-628
- ZET delivery numbers: 0.83 auto-reviewer findings per PR and 2.00 Director findings per ticket. archive/meta/architect-log.md:880-882
- Ratio: five of eight findings were cross-system and three were within local reach. Two of the five cross-system findings later proved to rest on false premises. archive/meta/architect-log.md:559-563, 922-929
- Dispatch outcome: five accepts and five rejects. Six of ten proposals were rejected or materially amended by the audited Architects. archive/meta/architect-log.md:785-787, 911-913
- MET re-ran `gh api` across six PRs and found 27 external findings against the 27 counted. archive/meta/architect-log.md:897-909
- Overhead was rescoped. MET's capped set grew 709→1,056 (+140 in the last window), and MET accepted a cap of 1,100. ZET's real per-ticket read was 1,474 lines and had grown about +895 (team log 93→547). archive/meta/architect-log.md:834-844
- ZET could not reproduce the layer's starting figure (679 vs 671). It was the third unreproducible line count in the review. archive/meta/architect-log.md:856-861

### 2026-08-14 → 08-15: Advisory, spine questions, application, AR proposals

- The layer corrected its own chat claim before dispatch: 4 of 10 ZET worklogs carry `## Director findings`, not 2 of 9. archive/meta/architect-log.md:1084-1086
- Advisory packets: roughly 2 of 8 items survived, both amended, against 5 of 10 for 001a. archive/meta/architect-log.md:1181-1188
- AF-3's central claim died. The script records "absent ≠ zero". Post-mandate collection was 4 of 7, with the one miss already named. archive/meta/architect-log.md:1192-1199
- MET's one external blocker landed on its highest test-surface diff ever (~14:1 test to production lines). archive/meta/architect-log.md:1207-1213
- First context-per-ticket baseline: ~14.4M tokens across four tickets, one of them 50.5% of the window. archive/meta/architect-log.md:1219-1223
- 18 dispatched items across four packets carried no command and its result, including all 7 survivors. archive/meta/architect-log.md:1341-1350
- 11 rejections. Ten had a recorded reason, and all ten were the same failure: an assertion about the target repo's own mechanism, never checked in that repo. archive/meta/architect-log.md:1352-1368
- Delivery-side items: 4 of the advisory's 8 against 0 of 001a's 10. All 4 died. archive/meta/architect-log.md:1323-1328
- This repo's `.claude/settings.local.json` had no `deny` key at all, only 21 `allow` entries. archive/meta/architect-log.md:1438-1448
- Prior-proposals check on 08-14: none of the seven approved items had landed (0 matches each). archive/meta/architect-log.md:1477-1500
- The first application dispatch applied 1 of 5 at MET. MET's read path was 1,056 against the accepted 1,100, leaving 44 lines of headroom. archive/meta/architect-log.md:1530-1534, 1566-1569
- Tally: 2 of 7 applied by dispatch, then 7 of 7 by the end of 08-14 (2 by dispatch, 5 by Andres at a keyboard). Both dispatch-landed items were improved by the child. archive/meta/architect-log.md:1652-1656, 1760-1763
- MET re-measured 17 transcripts (4,246 `isSidechain: false`, 1,914 absent, zero `true`) against this log's 16. The token figure is a main-loop floor. archive/meta/architect-log.md:1685-1687, 1740-1744
- MET's branch was merged, and the "stranded on a branch" and `.claude/**` harness-block findings were withdrawn. archive/meta/architect-log.md:1769-1785
- MET's `settings.local.json` held 71 lines of shadow grants, including unrestricted push, invisible to retros. archive/meta/architect-log.md:1877
- AR-1: `grep` for a fresh/cold-session rule in `/retro` returned 0 at both teams. AR-2: the hooks key appeared in neither settings file (0/0). archive/meta/architect-log.md:1893-1912
- AR dispatch: 1 of 4 survived (AR-3, amended). `preflight.py` took 10.9 s and 15+ API calls per boot. A 135-line knowledge file was referenced nowhere. archive/meta/architect-log.md:1945-1985
- AR-3 plus AF-3's doc half was projected to land MET's read path at about 1,072/1,100. archive/meta/architect-log.md:2017-2022

### 2026-08-18: Scoped read of two retros

- 84 of 100 commits since 08-14 were in the two engineering teams. PU had 1 and BS had 3, and four of six systems went unexamined for the third time. archive/meta/architect-log.md:2049-2054
- **First promotion: `honest-metric` → `proven`.** ZET's metric printed 0.00 on n=1 (silently false). It was corrected to 1.50, then to 2.00 per PR as a floor on n=2, against 1.17 on n=6. archive/meta/architect-log.md:2062-2078
- MET's context cost was at least 1,356,714 output tokens. archive/meta/architect-log.md:2079-2087
- `single-source-claims` was derived independently at both teams. At ZET a stale claim survived in eight files and drove a 106-line script the Director rejected. At MET `verify_docs.py` passed 9 of 9 with the new copies-agree assertion. archive/meta/architect-log.md:2094-2117
- Both teams dated their retros a day into the future (UTC written as a local date). archive/meta/architect-log.md:2171-2185
- MDT discharged its wake-up item on 08-14 without the layer knowing. It had run zero retros ever. archive/meta/architect-log.md:2187-2203
- Audit of past proposals: every item recorded as harness-blocked had landed. archive/meta/architect-log.md:2207-2210
- MET's 1,100 cap bound (1,098 → 1,082), and a cut was reversed on the measurement. MF-8 measured 4 PRs merged against 0 retro output. archive/meta/architect-log.md:2212-2220
- MF-4's three Verify blocks ran and passed, but they were inert. The two claims that died had no block. archive/meta/architect-log.md:2222-2227
- **Transfer yield: 4 of 7 items produced a datapoint, and 1 changed a decision.** The scoreboard had been at zero before. archive/meta/architect-log.md:2229-2235
- Local reach: four of six findings were available locally. archive/meta/architect-log.md:2247-2253
- The session's derived commit counts were wrong (ZET 181 and MET 92, against a measured 196 and 103). archive/meta/architect-log.md:2259
- Structural packets to date: eighteen items and eleven rejections. One survivor rested on a measured defect. archive/meta/architect-log.md:2276-2280

### 2026-08-19 → 08-29: Four births

- Births went 0 → 1 → 2 → 3 → 4 (08-19, 08-22, 08-24, 08-29). Promotions stayed at 1, nothing was delivered, and review 001 went 16 days undischarged. archive/meta/architect-log.md:2293-2295, 2883-2889
- WET preconditions: a human reviews 6 of the last 20 PRs. The `gh pr view --comments` endpoint had scored ZET's gate 0.00 for three cycles against a true 0.83. The integration suite hits about 10 live staging origins. archive/meta/architect-log.md:2346-2359
- WET's `no-hardcoded-human-identity` assertion failed on its first run by matching its own text. archive/meta/architect-log.md:2383-2386
- galind-team's `ledger.py` reported 0 of 14 days and 1 of 25 commits on product. archive/meta/architect-log.md:2513-2526
- `galind.io` appeared in 16 tracked BS files. It was registered but not deployed (`dig` A empty). archive/meta/architect-log.md:2534-2543
- The first two births made opposite calls on the same two mechanisms (WET adopted a 900-line read-path cap and executable claims; galind-team declined both). archive/meta/architect-log.md:2567-2579
- Both spine-grown births independently invented an improvement-vs-delivery ratio. That makes two adopters and no outcome yet, so `provisional` at best. archive/meta/architect-log.md:2596-2620
- the-debrief: founded with 23 files and 2,631 lines. The gate faces about 2,000 entries, so it samples 8–12 adversary-nominated entries. `audit.py selftest` passed 18/18, and `ledger` corrected itself to 0 product / 1 machinery. archive/meta/architect-log.md:2638, 2722-2750, 2801-2812
- MET's `gates.py` first datapoint had claimed "across 8 ticket worklogs" when all 27 came from one. archive/meta/architect-log.md:2814-2816
- resale-desk: founded with 21 files and 1,802 lines. The read-path claim of about 620 was really 410, so the 900 trigger could never bind and was cut to 650. `desk.py selftest` passed 19/19. archive/meta/architect-log.md:2872, 3048-3073

### 2026-10-28: Review 001 (window 2026-08-19 → 10-28, 70 days)

- The review ran 76 days late and read 11 repos. archive/meta/architect-log.md:3205-3206
- **Nine of ten pre-bar `proven` patterns fail the independence bar.** Only `overhead-ceiling` keeps the status (MET re-derived it). HANDOFF said eight, but grep returned eleven files including `honest-metric`. archive/meta/architect-log.md:3217-3243
- **MET's read-path cap bound at 1,082/1,100 on 08-18, was breached on 08-20 and reached 1,477 at its widest, for 69 days.** Retro 003 cut it to 1,030. archive/meta/architect-log.md:3277-3283
- Window commits: MET 528, ZET 372, MDT 48, ML 14, PU 6, this layer 6, the-debrief 4, resale-desk 3, galind-team 2, WET 1, BS 0. archive/meta/architect-log.md:3290-3302
- **ZET + MET made 900 of 984 window commits (91%).** The previous window was 84 of 101 (83%). archive/meta/architect-log.md:3304-3305
- Every employer-fed system kept running. Every self-directed system stopped: BS 08-16, PU 08-23, galind-team 08-23, resale-desk 08-31, the-debrief 10-06, and WET never started. archive/meta/architect-log.md:3307-3316
- `git log` alone misread four systems. the-debrief really held 65 entries across 14 slices (one commit of 20,632 lines). **Six of ten systems had uncommitted operating state.** archive/meta/architect-log.md:3318-3323
- No birth since 08-29. `~/dev/living-universe` is a human project, correctly unregistered. archive/meta/architect-log.md:3325-3328
- Retro cadence: MET went 69 days between retros, MDT ran its first at 79 days, PU ran at 15 sessions against a due point of 10, BS (due every 4 weeks) never ran in 80 days, and the-debrief printed "eleven slices overdue" at boot and never ran one. archive/meta/architect-log.md:3335-3351
- Grading: ZET found a change "run in 5 of 13+ sessions". PU found "three of four proposals approved 2026-08-11 did not produce their effect". archive/meta/architect-log.md:3365-3372
- **Five of nine Architects never ran.** Every one that ran graded itself accurately and harshly. archive/meta/architect-log.md:3374-3380
- Knowledge gate (MDT): a 1,550-line file had 9 lines cut and 8 stale facts corrected. The predicted filler was under 1%. Staleness was the real failure, and the candidate moved to `provisional`. archive/meta/architect-log.md:3399-3404
- The run of human-step cuts reached three: `budget.md`, the student prediction, and PU's ambient input. archive/meta/architect-log.md:3406-3413
- Claim I output: WET had 0 tickets in 70 days. resale-desk ran 3 days (30 verdicts, 12 listings, 0 resolved). the-debrief delivered 14 slices, 65 entries and 52 machine checks, with an adversary that caught fabricated citations. archive/meta/architect-log.md:3417-3424
- Claim III was biting with data for the first time. Claim IV was falsified as stated (seventh consecutive hit). archive/meta/architect-log.md:3435-3438
- Local reach: five of seven findings were not locally available, up from 2 of 6 cross-system on 08-18. archive/meta/architect-log.md:3440-3445
- Transfer yield, re-checked:
  - MF-1b changed a decision once, then failed as a tripwire.
  - MF-2b, MF-8/AF-6 (105 PRs and 48 worklogs against 0 proposals; at least 17.9M output tokens) and ZET's § Cuts (fired at #6–#8) are yielding.
  - AR-3 fired (five orphan files) but was ignored for 69 days.
  - MF-4's four Verify blocks are not yielding.

  archive/meta/architect-log.md:3449-3466
- BS's stale README (review 000's F1) was still stale after 80 days. archive/meta/architect-log.md:3467-3468
- `single-source-claims` retirement test: MET's `verify_docs` fired on a drifted pin (11 ≠ 10). The pattern survives one cycle. archive/meta/architect-log.md:3473-3476
- Unpacketed child defects: resale-desk's `state` printed a negative count (−12). galind-team's ledger read 100% machine, partly because the product repo's 24 files were never committed. archive/meta/architect-log.md:3498-3503
- The six stopped systems had been inactive by their own records for 22 to 73 days. archive/meta/architect-log.md:3508-3511

## Lessons

There are 76 distinct lessons. Each gives the first citation, then its standing under the colony design.

### Evidence

1. Copies are not evidence: one person's derivation repeated is one derivation. archive/meta/architect-log.md:274-280. `superseded`, by the DNA rule (measured help in a second system, REDESIGN.md §7).
2. A copy is independent evidence for a pattern it demonstrably did not inherit. The test is documentary and never retroactive. archive/meta/architect-log.md:448-461. `superseded`, by the DNA rule.
3. Carried adoptions are not independent; otherwise the layer could promote its own proposals by dispatching them. archive/meta/architect-log.md:2131-2157. `superseded`: a carried trial now counts (REDESIGN.md §7).
4. "Inherited" is a fourth route. Spine-grown systems can never independently adopt spine invariants, so claim I and the promotion gate pull against each other. archive/meta/architect-log.md:3248-3256. `superseded`, by `founding` status (ruling 1).
5. Two independent diagnoses with two remedies show the fault is real, not that either remedy works. archive/meta/architect-log.md:476-479. `kept`.
6. Presence is not effect: a mechanism that never fired is not evidence. archive/meta/architect-log.md:410-414. `kept`, as the rollback "no visible effect → revert" rule.
7. Births are evidence only through what they decline or invent. Opposed, reasoned adoptions show the spine is read, not complied with. archive/meta/architect-log.md:2575-2587. `superseded`, by the results-based DNA rule.
8. A birth count is not a result. Write the falsifier before results exist ("choosing the target after the shot"). archive/meta/architect-log.md:2297-2311. `kept`, because the falsifier in phase-1 §6.5 is pre-registered.
9. A child designed around the layer's measurement needs has had its architecture set from above. archive/meta/architect-log.md:3032-3041. `kept`.

### Verification

10. Re-run claims instead of re-reading them. A number whose command was not carried cannot be checked. archive/meta/architect-log.md:576-583, 610-612. `kept`, because scores are computed by script.
11. A finding is worth what its disproving command returned. Verification depth explains 5/10 vs 2/8. archive/meta/architect-log.md:1256-1264. `kept`.
12. The check must run in the repo the claim is about. It was the cause of 10 of 11 rejections. archive/meta/architect-log.md:1352-1377. `kept`.
13. Do not assert a precondition in one repo from a mechanism seen in another, and do not verify an adopter with the proposer's implementation detail. archive/meta/architect-log.md:812-819, 1644-1650. `kept`.
14. A fact can be stale in the repo that recorded it, because outside admins change state. Open items need a re-check date. archive/meta/architect-log.md:1214-1219, 1272-1274. `kept`.
15. Check the precondition before writing the instruction. archive/meta/architect-log.md:1569-1575, 1692-1694. `kept`.
16. A refusal is evidence about a refusal and nothing else. Never explain a block with an unchecked mechanism. archive/meta/architect-log.md:1552-1556, 1787-1793. `kept`.
17. The layer's claims about itself need executed checks too (AR-4). archive/meta/architect-log.md:1801-1806, 1926-1933. `kept`: the layer runs the same kernel.
18. Verify by artifact, not by commit subject. "Applied" and "on `main`" come apart, so check for a PR before flagging. archive/meta/architect-log.md:1496-1500, 1769-1774. `kept`.
19. A packet that names the command that would kill it is worth more than one that runs a command that confirms it. archive/meta/architect-log.md:1471-1475. `kept`, as "every self-change states its claim" (phase-1 §4.4).
20. A filter that rejects everything that worked is a moratorium, not a discriminator. archive/meta/architect-log.md:1347-1350. `kept`.
21. A brief right about 40 things and wrong about 2 is more dangerous than one wrong about all. archive/meta/architect-log.md:335-337. `kept`.
22. A machine assertion's first run tends to correct its author, not its target. archive/meta/architect-log.md:1636-1642, 2814-2821. `kept`.

### Ratchets

23. Rules only get added and structure only gets refused, with each decision locally right. A rule losing every cycle is data about the rule. archive/meta/architect-log.md:595-628. `kept`; the remedy is rollback (phase-1 §4.4).
24. "Asked and answered no" is a different failure from "unasked", with a different remedy. archive/meta/architect-log.md:805-807. `kept`.
25. Never-recorded is not never-needed. An empty § Cuts cannot be told apart from one nobody wrote. archive/meta/architect-log.md:821-827, 1727-1729. `kept`.
26. Self-modification is the highest-blast-radius output, and the retro had no independent adversary. archive/meta/architect-log.md:600-605. `superseded`, by the self-change reviewer agent (ruling 5).
27. The improvement loop can consume the capacity it serves. Two consecutive cycles is the signal. archive/meta/architect-log.md:638-644. `kept`.
28. Ceilings fail three ways: set above the current value, set over the wrong file set, or routing their remedy to an unscheduled retro. archive/meta/architect-log.md:410-412, 846-854, 3277-3283. `kept`, with the budget now checked at every boot.
29. Instruction files become archives on the read path (the "history tax"). archive/meta/architect-log.md:1105-1111. `kept`, via compaction (phase-1 §4.1). The mechanism is unconfirmed.
30. Items that instrument a number or force a trade produce datapoints. Items that ask a session to remember something are inert. archive/meta/architect-log.md:2229-2235. `kept`.
31. Structural arguments from this layer lose, and measured present defects survive. archive/meta/architect-log.md:1995-2000. `kept`: results, not essays, enter the DNA.
32. A mechanism can be right and aimed wrong, and the aiming was the layer's part. archive/meta/architect-log.md:2222-2227. `kept`.
33. A claim duplicated across N files has N places to be wrong (`single-source-claims`). archive/meta/architect-log.md:2094-2117. `kept`.
34. A knowledge file's real failure is appended facts going stale, not filler. archive/meta/architect-log.md:3399-3404. `kept`.

### Reach

35. Carrying is a service, not an insight. archive/meta/architect-log.md:559-563. `superseded`: carrying is now the DNA trial (REDESIGN.md §7).
36. A finding no local Architect could make is not a finding no local Architect could correct. archive/meta/architect-log.md:926-929. `superseded`, by the thesis rewrite (phase-1 §6.5).
37. The layer can only propose against the loop it can see; it could not see delivery (MF-10). archive/meta/architect-log.md:863-893. `superseded`, by ruling 9 and the scoreboards.
38. A read-list must be closed under disproof, or it manufactures unfalsifiable findings. archive/meta/architect-log.md:1317-1321. `kept`.
39. A spine question may not be written as a proposal to dodge the evidence bar. archive/meta/architect-log.md:1405-1409. `superseded`, by the keeper procedure.
40. Following attention instead of auditing distribution looks like productivity the whole way down. archive/meta/architect-log.md:745-748, 2041-2058. `kept`, via the weekly harvest of every core system.
41. A scoped review cannot audit proposals made against repos it did not read. archive/meta/architect-log.md:675-677. `superseded`, by ruling 9.
42. Absences are harder to see than drift, and a catalog makes them visible. archive/meta/architect-log.md:130-133. `kept`.
43. A system whose only grader is itself gets better at grading itself. The fix needs money or time, not a rule. archive/meta/architect-log.md:629-637, 702-708. `kept`, as automatic human-signal capture (phase-1 §4.3).
44. Claim IV ("nobody scores the scorers") was contradicted at every instance. An Architect that does not run writes nothing about not running. archive/meta/architect-log.md:531-541, 3374-3382. `superseded`, by the continuous loop and its loop-check hook (M-2 superseded).
45. Rejections are the most useful signal the layer produces. archive/meta/architect-log.md:785-787. `kept`, as "rollback rate: healthy is some, not zero".

### Dispatch

46. Never edit a child repo; proposals go to the child's Architect, carried by the human. archive/meta/architect-log.md:6-7, 645-652. `retired`, by ruling 9.
47. Reading a charter's silence as permission erodes boundaries without anyone deciding. archive/meta/architect-log.md:697-701. `kept`.
48. Enforce boundaries at the permission layer. `Write(...)` denies are inert; only `Edit(path)` binds, and `Bash(git commit:*)` misses `git -C`. archive/meta/architect-log.md:969-994, 1166-1168, 2024-2027. `kept`, as harness locks.
49. Copies lose the invisible part. archive/meta/architect-log.md:992-994. `kept`.
50. A dispatch had no write-back. A record that says a decision was made without saying what it was is not a record. archive/meta/architect-log.md:1603-1630. `kept`, as the changelog.
51. A dispatched session writing the child's log can induce an error the layer cannot correct. archive/meta/architect-log.md:1557-1564. `superseded`, by ruling 9 plus logged, reversible edits.
52. The dispatch prompt is load-bearing: one sentence ("do not speculate") decided the outcome. archive/meta/architect-log.md:1586-1593, 2010-2015. `kept`.
53. Do not write into a dirty tree or alongside a concurrent session. archive/meta/architect-log.md:1522-1528. `kept`.
54. An undocumented redaction looks exactly like an evidence gap. Publish conclusions, not an employer's operational surface. archive/meta/architect-log.md:1025-1027, 1051-1054. `kept`, under ruling 12.
55. A packet into a system nobody is running is a document, not a dispatch. archive/meta/architect-log.md:3502-3503. `kept`: side projects are left untouched.

### Founding

56. Divergence is cheap and local, and convergence is expensive and deliberate. archive/meta/architect-log.md:243-252. `kept`: the DNA changes slower than any system.
57. Knowledge breadth is not routing breadth. Prefer the cheaply reversible choice. archive/meta/architect-log.md:2324-2333. `kept`.
58. Key on structure, not identity (an external reviewer is "not the author, no team marker"). archive/meta/architect-log.md:2372-2377. `kept`.
59. A named failure mode backed by a real failure is a different object from a predicted one. archive/meta/architect-log.md:2467-2479. `kept`.
60. A gate asked to approve more than it can read approves it anyway, and `human-gate` is silent on volume. archive/meta/architect-log.md:2722-2755. `kept`.
61. A charter's premises can be owned outside the portfolio and go stale, but the human still owns the risk decision. archive/meta/architect-log.md:2957-2982, 3141-3150. `kept`.
62. A precondition check must not quietly become a prohibition. A founding session must not substitute its risk appetite for the owner's. archive/meta/architect-log.md:3154-3172. `kept`.
63. Write prohibitions with the source quoted and dated, so overruling them is legible. archive/meta/architect-log.md:3174-3177. `kept`.
64. Proportion metrics can be gamed by deletion. Use per-category floors and name what the instrument cannot see. archive/meta/architect-log.md:2793-2799. `kept`.
65. Censored feedback hides false negatives. It needs a prediction on the road not taken. archive/meta/architect-log.md:2998-3015. `kept`.
66. Push honesty into the artifact (`verified`/`contested`/`unverified` rendered to users), not only into the log. archive/meta/architect-log.md:2785-2792. `kept`.
67. Holding live credentials while reading attacker-controlled text is a distinct failure mode (injection). archive/meta/architect-log.md:3195-3199. `kept`.
68. UTC written as a local date silently shifts date-windowed metrics, across systems by construction. archive/meta/architect-log.md:2171-2185. `kept`.
69. A rename costs least before launch. archive/meta/architect-log.md:2545-2547. `kept`.

### Cadence

70. Every mechanism that needs a recurring human step gets cut. A run of such cuts is "comfort drift with good prose". archive/meta/architect-log.md:200-206, 3406-3413. `kept`: it motivates rulings 4 and 5.
71. Ask rather than infer: quiet can be deprioritisation or neglect. A layer that reads all quiet as neglect is a guilt generator. archive/meta/architect-log.md:192-195. `kept`, codified by ruling 2.
72. Defining "retro due" is not the fix, and neither is surfacing it. The retro clock is the human's attention clock. archive/meta/architect-log.md:3347-3356. `kept`; the remedy is the continuous loop (ruling 4).
73. Misses fall on every system without an outside forcing function, not on the least important ones. archive/meta/architect-log.md:3307-3316. `kept`.
74. `git log` is blind to uncommitted state. An append-only log that is not committed is neither append-only nor a log. archive/meta/architect-log.md:3318-3323, 3492-3494. `kept`, as M-3 and M-5 in the kernel.
75. Do not promote on fresh evidence ("a fresh idea from a live project is the most persuasive thing"). archive/meta/architect-log.md:433-436. `kept`, as the DNA's minimum of 44 days.
76. Gate-holding and freeze look identical at one review; the test is whether anything crosses later. archive/meta/architect-log.md:504-510. `kept`, as DNA-flow measure M3.

## Open at archive time

Items review 001 was asked to do on 08-19 → 08-29 but did not report:

- Audit the four founding charters for precondition checks that became prohibitions (the-debrief's gate sample, galind-team's test allowlist, resale-desk's original rules 1–3). archive/meta/architect-log.md:3168-3172
- resale-desk `D-006`: discipline or contamination by the layer? archive/meta/architect-log.md:3108-3110
- Does `predict-then-check` need a third half? Does Andres keep the decline sample? archive/meta/architect-log.md:3105-3107
- Does `charter-as-constitution` need an account of externally-owned premises (the "three-and-a-half gate gaps")? archive/meta/architect-log.md:3100-3104, 3148-3150
- Does `human-gate` need a volume clause? archive/meta/architect-log.md:2752-2755
- PU and the-debrief disagree about pedagogy: are they different purposes, or is one wrong? archive/meta/architect-log.md:2775-2779
- Charter owner ≠ repo owner, and a gatekeeper who is not the designer (WET). archive/meta/architect-log.md:2397-2409
- The improvement-vs-delivery ratio candidate (two adopters, and the-debrief's carried copy not counted). archive/meta/architect-log.md:2615-2628, 2839-2841
- The "first run corrects its author" catalog line. archive/meta/architect-log.md:2814-2821
- Did the-debrief's `verification` field drift toward `verified` under volume? Is resale-desk's `docs/pricing.md` filled by evidence? archive/meta/architect-log.md:2849-2851, 3111-3114
- The size of each birth's first § Cuts. No birth has run a retro. archive/meta/architect-log.md:2411-2421, 3424

Older carried items that never closed:

- The earned-autonomy classes and bar (goal ruling 2), the two feedback instruments (goal ruling 4), scoring E10's own claims, and judging MET's shadow grants. archive/meta/architect-log.md:1875-1879
- May the layer report delivery-side numbers it can compute? archive/meta/architect-log.md:1330-1337
- The UTC-date slip was to "ride with the next packet", and no packet followed. archive/meta/architect-log.md:2272-2274
- The cause of the 08-14 non-interactive `.claude/**` refusals is unknown. archive/meta/architect-log.md:1795-1799
- The dispatch write-back defect has no structural fix. archive/meta/architect-log.md:1603-1609, 1987-1993
- MET `retro.md:21` points output at the wrong path (flagged to MET), and MET `still_open` entries needed re-check dates. archive/meta/architect-log.md:1272-1274, 1705-1709
- The BS `galind.io` packet is held until Andres rules on BS. It is now `dormant`. archive/meta/architect-log.md:3469-3472
- Review 001's ask 5 is unanswered: were the three 2026-10-28 retros briefed with shared content? archive/meta/architect-log.md:3519-3523
- The review-002 watch list: engage's RETRO DUE line (predicted to print and not fire), whether 1,030 holds at MET, and the first birth retro. archive/meta/architect-log.md:3525-3532

Discrepancies found in the log while distilling it:

- The previous window is "84 of 100" commits at the 08-18 entry but "84 of 101 (83%)" in review 001. archive/meta/architect-log.md:2050, 3304
- HANDOFF counted "eight" pre-bar `proven` patterns. Review 001 found ten (eleven files including `honest-metric`). archive/meta/architect-log.md:289-292, 3217-3220
- Claim IV's hit count skips a number: the 08-14 count correction is "Claim IV's pattern", unnumbered, between the third and fifth hits. archive/meta/architect-log.md:1741-1744, 1995
- The 08-18 entry labels the local-reach check "Claim III", while elsewhere claim III is about cadence. archive/meta/architect-log.md:2247
- 001a's "five of eight cross-system" was later qualified: two of the five had false premises. archive/meta/architect-log.md:559, 922-929
- The publication rule (no target-repo PR or ticket identifiers) was not kept in later entries. A broken `[[...]]` wikilink to a private memory store appears twice. archive/meta/architect-log.md:1047-1049, 1386-1396, 1577-1582
