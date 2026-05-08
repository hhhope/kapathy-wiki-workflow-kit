# Public Report Quality Gate Pressure Scenarios

Use these scenarios to validate trigger and gate behavior.

## Should Trigger

| Scenario | Expected | Result |
|---|---|---|
| User says "写一个对外材料，给我同步飞书审核" | Load public-report-quality-gate before Feishu write | PASS |
| User says "写一个对外材料并发飞书审核" and no repo-visible gate-review file exists | Create/update `wiki/ops/*-report-gate-review.md` before Feishu write | PASS |
| User asks to turn an internal wiki ops page into a shareable report | Gate reader-facing rewrite; internal wiki text is not public-ready by default | PASS |
| User provides a Feishu page as structure reference for a new report | Require reference structure map before drafting | PASS |
| User asks for H5/share draft based on dense wiki content | Require split, voice, visual, and publish gates | PASS |
| User asks "帮我润色成正式稿" for a report intended for managers/readers | Apply voice gate and scorecard | PASS |
| User says "可以，发飞书" after a draft with unresolved hard-gate failures | Block sync and report failing gates | PASS |

## Should Not Trigger

| Scenario | Expected | Result |
|---|---|---|
| User asks to capture raw meeting notes into `wiki/sources` | Prefer material-collaboration-defaults; no public gate unless reader-facing output is requested | PASS |
| User asks for private scratch analysis in `wiki/ops` | Do not require public report scorecard | PASS |
| User asks to implement code and summarize the diff in chat | Do not trigger unless a reader-facing report is requested | PASS |
| User asks to fetch a Feishu doc for source capture only | Use lark-doc/source workflow; no public publish gate | PASS |

## Failed Knowledge-Base Draft Replay

| Failure | Gate That Should Catch It | Expected Result |
|---|---|---|
| Reference group had overview/runtime/install/validation/roadmap, but the draft became one long page | Reference Structure Gate + Split Gate | FAIL until split strategy exists |
| "Lore = 管现场记忆; Team Lore = 管跨项目复用; Wiki = 管结构化生产..." replaced the evolution story | Voice Gate + Narrative Gate | FAIL until rewritten as an evolution path |
| The text sounded like an agent explaining repo mechanics | Voice Gate | FAIL until rewritten in reader-facing language |
| Diagrams duplicated text and did not define visual responsibility | Visual Gate | FAIL until each diagram carries a specific relation or sequence |
| Feishu sync happened before quality gates were checked | Publish Gate | FAIL; sync should wait for gate pass |
| Feishu sync happened before `wiki/ops/*-report-gate-review.md` existed | Gate Review Artifact | FAIL; sync should wait for a repo-visible process artifact |
| A scorecard exists only in chat or `/tmp` | Gate Review Artifact | FAIL until persisted under `wiki/ops` |

## Reference Readback Regression Replay

| Failure | Gate That Should Catch It | Expected Result |
|---|---|---|
| A Feishu wiki reference node has `has_child: true`, but linked child articles are not fetched before scoring | Reference Structure Gate | FAIL; do not draft, score, or sync until linked articles are read and mapped |
| A reading map contains concrete article links, but the draft uses placeholder page titles instead of the linked articles' actual jobs | Reference Structure Gate + Reader Path | FAIL; reference map must include the concrete links, titles, and page roles |
| The reference entry page contains essential visuals before key tables, but the draft has no equivalent visual asset or visual plan | Visual Gate | FAIL; do not downgrade to residual risk for reference-shaped output |
| Any hard gate is `FAIL`, `UNKNOWN`, `PARTIAL`, or `NOT TESTED`, but the review still assigns a numeric score | Scorecard | FAIL; score must be `INVALID` and the decision must block sync/review-ready claims |
| A review packet bundles multiple final reader jobs into one Feishu document and calls that a split | Split Gate | FAIL unless the packet is explicitly marked as a non-review-ready failed/provisional draft and final page destinations are mapped |

## Validation Notes

- These scenarios validate trigger wording and gate expectations, not automatic
  runtime dispatch across all future sessions.
- The gate coordinates other skills; it does not prove source correctness,
  visual rendering quality, or Feishu API success by itself.
