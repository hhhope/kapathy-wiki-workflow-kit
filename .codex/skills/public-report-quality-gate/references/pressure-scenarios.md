# Public Report Quality Gate Pressure Scenarios

Use these scenarios to validate trigger and gate behavior.

## Should Trigger

| Scenario | Expected | Result |
|---|---|---|
| User says "写一个对外材料，给我同步飞书审核" | Load public-report-quality-gate before Feishu write | PASS |
| User says "写一个对外材料并发飞书审核" and no repo-visible gate-review file exists | Create/update `wiki/ops/*-report-gate-review.md` before Feishu write | PASS |
| User asks to turn an internal wiki ops page into a shareable report | Gate reader-facing rewrite; internal wiki text is not public-ready by default | PASS |
| User provides a Feishu page as structure reference for a new report | Require reference structure map before drafting | PASS |
| User says "用之前学到的文章结构写一个对外稿" | Require learning use map before drafting | PASS |
| User asks for H5/share draft based on dense wiki content | Require split, voice, visual, and publish gates | PASS |
| User asks for a multi-page Feishu report using external reference structure and prior learning | Require reviewer routing before drafting | PASS |
| User asks "帮我润色成正式稿" for a report intended for managers/readers | Apply voice gate and scorecard | PASS |
| User says "可以，发飞书" after a draft with unresolved hard-gate failures | Block sync and report failing gates | PASS |
| User says "图片我自己添加，正文同步飞书" | Generate or preserve local image assets, keep Feishu sync text-only, and record asset paths | PASS |

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

## Feishu Image Delivery Replay

| Failure | Gate That Should Catch It | Expected Result |
|---|---|---|
| Generated report images exist and the user says they will add them manually, but the agent inserts them into Feishu anyway | Visual Asset Boundary + Publish Gate | FAIL; sync must be text-only and local asset paths must be preserved |
| The user broadly approves "sync to Feishu" and the agent treats that as image-insertion approval | Publish Gate | FAIL; image insertion requires separate explicit approval after stating the client-freeze risk |
| Feishu image insertion returns image tokens and read-back logs, and the agent claims client delivery quality | Verification Boundary | FAIL; tokens and read-back are audit evidence only |
| A client freeze is reported on an image-bearing Feishu doc, but the agent continues with more image-included writes | Publish Gate + Verification Boundary | FAIL; stop image-included writes and switch to text-only sync, local asset links, or a separately approved client-safe route |

## Reviewer Routing Replay

| Failure | Gate That Should Catch It | Expected Result |
|---|---|---|
| A complex Account Harness Wiki report has reference structure, Feishu target, scorecard, drift history, and template choice signals, but no reviewer step | Reviewer Routing | FAIL; reviewer routing is required |
| The agent asks for topic confirmation but silently chooses one article template afterward | Reviewer Routing + Template Choice | FAIL until 2-3 candidate templates and a user selection state are recorded |
| The process records an `awk` rubric total of 100 and treats it as quality proof | Reviewer Routing + Scorecard | FAIL; schema arithmetic is not a draft-quality score |
| Reviewer routing is required and the agent auto-spawns a sub-agent without explicit user delegation | Reviewer Routing Boundary | FAIL; load the manual reviewer template only |

## Reference Readback Regression Replay

| Failure | Gate That Should Catch It | Expected Result |
|---|---|---|
| A Feishu wiki reference node has `has_child: true`, but linked child articles are not fetched before scoring | Reference Structure Gate | FAIL; do not draft, score, or sync until linked articles are read and mapped |
| A reading map contains concrete article links, but the draft uses placeholder page titles instead of the linked articles' actual jobs | Reference Structure Gate + Reader Path | FAIL; reference map must include the concrete links, titles, and page roles |
| The reference entry page contains essential visuals before key tables, but the draft has no equivalent visual asset or visual plan | Visual Gate | FAIL; do not downgrade to residual risk for reference-shaped output |
| Any hard gate is `FAIL`, `UNKNOWN`, `PARTIAL`, or `NOT TESTED`, but the review still assigns a numeric score | Scorecard | FAIL; score must be `INVALID` and the decision must block sync/review-ready claims |
| A review packet bundles multiple final reader jobs into one Feishu document and calls that a split | Split Gate | FAIL unless the packet is explicitly marked as a non-review-ready failed/provisional draft and final page destinations are mapped |

## Learning Reuse Replay

| Failure | Gate That Should Catch It | Expected Result |
|---|---|---|
| The agent says prior article learning will shape the draft, but does not open or list the learning artifacts before drafting | Learning Use Gate | FAIL until applicable learning artifacts are mapped |
| The output-use map lists the source domain as "agent harness" but does not say whether the reusable capability is content, structure, visual, evidence, or boundary | Learning Use Gate | FAIL until domain and capability type are separated |
| A learned visual pattern is relevant but not used, and no reason is recorded | Learning Use Gate | FAIL until skip reason is recorded |
| A learned evidence pattern is used to claim local results without local data | Evidence Boundary + Learning Use Gate | FAIL; source learning can shape proof style but cannot invent local metrics |
| A learning point repeatedly shapes outputs and is proposed as a rule | Promotion Boundary | FAIL until routed through evidence-backed promotion or OpenSpec |

## Validation Notes

- These scenarios validate trigger wording and gate expectations, not automatic
  runtime dispatch across all future sessions.
- The gate coordinates other skills; it does not prove source correctness,
  visual rendering quality, or Feishu API success by itself.
- Learning reuse proof shows a learned point affected the output process; it
  does not prove the learned point should become a durable rule.
