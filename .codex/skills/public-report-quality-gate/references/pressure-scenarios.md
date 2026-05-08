# Public Report Quality Gate Pressure Scenarios

Use these scenarios to validate trigger and gate behavior.

## Should Trigger

| Scenario | Expected | Result |
|---|---|---|
| User says "写一个对外材料，给我同步飞书审核" | Load public-report-quality-gate before Feishu write | PASS |
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

## Validation Notes

- These scenarios validate trigger wording and gate expectations, not automatic
  runtime dispatch across all future sessions.
- The gate coordinates other skills; it does not prove source correctness,
  visual rendering quality, or Feishu API success by itself.
