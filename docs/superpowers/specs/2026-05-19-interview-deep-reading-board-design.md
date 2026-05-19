# Interview Deep Reading Board Skill Design

> Supports a future OpenSpec change. This Superpowers design is not
> authoritative lifecycle state until it is copied into OpenSpec and reviewed
> there.

## Context

The triggering incident was a Li Xiang and Luo Yonghao interview deep-reading
workflow. The first artifact treated the request as a word-cloud problem. That
made the output visually navigable, but it compressed the interview into loose
keywords and lost important speaker-turn logic.

The user clarified the real requirement through repeated corrections:

- the word cloud must connect to the interview timeline;
- a horizontal "temperature" axis should be draggable and should reveal
  evidence, not just filter decorative terms;
- the full interview must not be compressed into a few theme cards;
- `Agent to C` and `Agent` must not collapse into the same undifferentiated
  keyword cluster;
- user-highlighted passages, such as the section about code volume, Feishu,
  internal Coworker, stable employee Agent, subagents, data, and MCP, must
  appear as explicit reading windows.

The repaired H5 shape split the interview into many ordered reading windows and
made the word cloud a navigation surface, not the primary content container.

## Design Goal

Create a repository-local interview-specific skill that catches future
interview, podcast transcript, and dialogue deep-reading requests before they
degrade into compressed summaries or decorative word clouds.

The skill must ask the user whether to use the "full-window interview reading
board" output type when the source and request match this pattern.

## Approaches Considered

### Recommended: Interview-Specific Reading Board Skill

Add `interview-deep-reading-board` as a focused module. It handles interview
deep-reading shape, source-order windows, speaker-turn logic, temperature-axis
navigation, keyword-to-evidence linking, and H5 reference examples.

Pros:

- Directly addresses the failure mode from this conversation.
- Keeps interview-specific rules out of generic material processing.
- Keeps `public-report-quality-gate` as the outer reader-facing output gate.
- Allows this H5 to become a reusable output-shape reference.

Cons:

- Requires coordinated changes across the skill, output gate, `AGENTS.md`, and
  example/reference material.

### Alternative: Wordcloud Timeline Skill

Create a narrower skill for interview word clouds with timeline and slider
interactions.

Pros:

- Smaller surface.
- Directly names the first requested artifact.

Cons:

- Keeps the form too central.
- Risks repeating the original error: turning deep reading into visual keyword
  decoration.

### Alternative: General Long-Form Reading Board Skill

Create one generic skill for articles, interviews, speeches, meeting notes, and
long transcripts.

Pros:

- Broader reuse.
- Could cover future long-form material types.

Cons:

- Too broad for the failure being repaired.
- Risks weakening the interview-specific speaker-turn and dialogue-sequence
  requirements.

## Runtime Trigger Design

The new skill should trigger when the source or task is clearly interview-like:

- interview, podcast transcript, dialogue, Q&A, conversation, or speaker-turn
  material;
- user requests deep reading, word cloud, timeline, temperature axis, draggable
  evidence, or H5 exploration;
- user complains that output is too compressed, too fragmented, loses full-text
  coverage, or fails to show a named passage;
- user asks for article reading but the source structure is primarily a
  multi-speaker interview.

The skill should ask a fork-point question before producing the output:

> This interview is suitable for a full-window reading board: split by source
> order into enough reading windows, preserving speaker turns, timeline,
> temperature axis, keywords, and evidence. Do you want this output type?

The Chinese-facing wording used in normal conversation can be:

> 这类访谈适合做“全文窗口式精读板”：按访谈顺序拆成足够多的阅读窗口，保留人物回合、时间线、温度轴、关键词和证据。要不要做这个类型？

## Skill Boundary

`interview-deep-reading-board` is a module, not the outer reader-facing gate.

It owns:

- interview source-order windowing;
- speaker-turn and adjacent-window continuity;
- temperature-axis semantics;
- keyword-to-window and keyword-to-evidence linking;
- user-highlighted passage protection;
- interview H5 output-shape reference guidance;
- copyright-safe evidence handling.

It does not own:

- public reader intent, review-ready claims, Feishu sync, publication, or H5
  share-readiness;
- generic material processing;
- WeChat fetching;
- OpenSpec lifecycle;
- final visual QA gates.

## Output Gate Integration

`public-report-quality-gate` should remain the parent gate for reader-facing
HTML, H5, share drafts, and report outputs.

Add a delegation route:

| Public output need | Delegate to |
|---|---|
| interview deep reading, interview word cloud, interview timeline, temperature-axis evidence board | `interview-deep-reading-board` |

Add a gate check:

- If the source is interview-like and the requested reader-facing output
  includes deep reading, word cloud, timeline, temperature axis, draggable
  evidence, or "do not compress the full text", the agent must not jump
  straight into ordinary report drafting or HTML production. It must route
  through `interview-deep-reading-board` first.

The public gate still owns Article Intent Contract, Reference Output Shape Gate,
Learning Use Map, Judgment Ownership Gate, Visual Gate, Publish Gate, and
reader-visible citation expectations.

## AGENTS Routing Integration

`AGENTS.md` should receive only a lightweight routing row. It should not copy
the full interview-window rules.

Proposed routing entry:

| Situation | Load | Ownership |
|---|---|---|
| Interview, podcast transcript, dialogue, or Q&A material where the user asks for deep reading, word cloud, timeline, temperature axis, draggable evidence, or says not to compress the full text | `.codex/skills/interview-deep-reading-board/SKILL.md` | repo-owned module under material/public output gates |

This keeps `AGENTS.md` as a router and keeps detailed behavior in the skill.

## H5 Reference and Example Plan

The Li Xiang interview H5 must become a reference/example, not just an
implementation artifact.

Reference inputs:

- `wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html`
- `wiki/reports/lixiang-luoyonghao-ai-agent-reading-board-data.js`
- `wiki/sources/agentic-product-engineering-collaboration-lixiang-luoyonghao-ai-agent-reading-2026-05-18.md`

Counterexample input:

- `wiki/reports/lixiang-luoyonghao-ai-agent-wordcloud.html`

Expected new reference assets:

- `.codex/skills/interview-deep-reading-board/references/h5-output-shape.md`
- `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`

The reference should explain the output shape:

- source-order reading windows as the primary content unit;
- temperature axis as a horizontal reading control, not a decoration;
- word cloud as index only;
- evidence panel linked to selected windows;
- timeline markers that preserve interview sequence;
- default focus on user-highlighted or highest-risk missed passage when
  repairing a drifted output;
- copyright boundary: short evidence plus paraphrase and source position, not
  full verbatim transcript storage.

## OpenSpec Scope

Implementation requires a new OpenSpec change because this changes repo
workflow routing and semantic skill behavior.

Expected change id:

```text
add-interview-deep-reading-board
```

Expected files:

```text
openspec/changes/add-interview-deep-reading-board/proposal.md
openspec/changes/add-interview-deep-reading-board/design.md
openspec/changes/add-interview-deep-reading-board/tasks.md
openspec/changes/add-interview-deep-reading-board/evaluation.md
.codex/skills/interview-deep-reading-board/SKILL.md
.codex/skills/interview-deep-reading-board/evaluation.md
.codex/skills/interview-deep-reading-board/references/h5-output-shape.md
.codex/skills/public-report-quality-gate/SKILL.md
AGENTS.md
wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md
```

## Evaluation Plan

The OpenSpec and skill evaluation must include pressure scenarios.

### RED Baseline

- Long interview request for word cloud routes to compressed keyword output.
- The output loses timeline continuity and speaker-turn logic.
- The Coworker / Feishu / stable Agent / subagent / MCP section is summarized
  away or hidden under generic "Agent" keywords.
- Reader-facing H5 production can bypass the public report gate.
- `AGENTS.md` has no route for interview-specific deep-reading boards.

### GREEN Result

- Interview deep-reading trigger asks whether to create the full-window
  reading board.
- Confirmed output requires enough source-order windows for meaningful
  coverage.
- User-highlighted passages become explicit windows or window groups.
- Word cloud links into windows and evidence instead of replacing reading.
- Temperature axis connects to timeline and evidence.
- Reader-facing H5 routes through `public-report-quality-gate` first, then
  delegates interview-specific structure to `interview-deep-reading-board`.
- `AGENTS.md` has a lightweight route to the new skill.
- The Li Xiang H5 is available as a validated reference/example.

### Residual Risks

- "Full coverage" cannot mean storing the entire copyrighted source verbatim.
  The skill must preserve coverage through windows, paraphrase, source
  position, and short evidence snippets.
- Window counts are guidance, not a rigid numeric mandate. Very short
  interviews should not be inflated.
- A visually polished H5 can still fail if the source-order reading map is
  incomplete.

## Verification Plan

Expected checks after implementation:

```bash
python3 scripts/check_behavior_assets.py
rg -n 'interview-deep-reading-board|访谈|temperature|full-window|全文窗口' AGENTS.md .codex/skills openspec/changes/add-interview-deep-reading-board wiki/examples
python3 -m html.parser wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html
```

Manual replay evidence should include:

- input shape: user asks for interview word cloud or deep reading;
- trigger condition: interview-like material plus compression-sensitive output;
- expected route: ask whether to make the full-window reading board;
- expected non-route: do not produce ordinary word cloud as the primary output;
- parent gate: public report output still goes through
  `public-report-quality-gate`;
- reference evidence: Li Xiang H5 reference/example is visible to future
  agents.

## Success Criteria

The change succeeds when a future agent handling an interview like the Li Xiang
conversation asks the output-type fork question before building, routes
reader-facing H5 work through the public gate, uses the H5 reference shape, and
does not compress user-highlighted interview passages into generic keyword
summaries.

## Decision

Use the recommended interview-specific module approach:

- create `interview-deep-reading-board`;
- update `public-report-quality-gate` routing;
- update `AGENTS.md` routing;
- preserve this H5 as reference/example;
- prove the behavior through RED/GREEN skill evaluation and behavior replay.
