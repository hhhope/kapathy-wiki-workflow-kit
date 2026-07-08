---
name: feishu-doc-writing
description: "Use when creating or updating Feishu-facing share docs, wiki overview pages, governance summaries, or other human-readable knowledge documents that need progressive structure, document splitting, and context-linked updates. Also use when content is too dense for one page or when an existing doc refresh risks leaving stale TODOs or broken continuation links. Exclude raw meeting notes, API references, or purely machine-facing specs."
---

# Feishu Doc Writing

Write Feishu-facing knowledge docs for readers, not for transcript storage.

The output must stay readable, progressive, context-complete, and visually disciplined after updates.

## Do Not

- Do not dump high-density knowledge into one page when overview + deep-dive split is cheaper to read.
- Do not add a new top-level section just because new information appeared; first decide whether it belongs inside an existing section or a child doc.
- Do not update one document in isolation if the change invalidates neighboring overview, status, or follow-up pages.
- Do not leave published TODO markers, dangling “continued later” text, or known unfinished transitions after claiming the doc is updated.
- Do not start with dense detail before the reader can answer “what is this doc for” and “where should I go next”.
- Do not optimize only for completeness while ignoring scanability, section rhythm, and first-screen readability.
- Do not let a page read like chat transcript cleanup when it is supposed to be a stable knowledge page.
- Do not default to long bullet dumps when a compact table or comparison block would lower reading cost.
- Do not add or keep a visual that repeats text without improving orientation, compression, or recall.

## Intent Routing

| Situation | Use this shape |
|---|---|
| New share / overview doc | Build an entry page with progressive summary first, then route readers into subtopics |
| Existing doc refresh | Check surrounding docs first, then update the target doc plus any broken context links |
| Topic is knowledge-dense | Split into overview + focused deep-dive docs instead of one overloaded page |
| Status or retrospective refresh | Replace stale status/TODO text with resolved facts, boundaries, and next-read links |

## Pairing Rule

This skill defines **content structure and reader-facing quality**, not remote transport.

When the user asks to operate on a real Feishu/Lark document, use this skill together with `lark-doc`:

- `feishu-doc-writing`: decide structure, split strategy, and progressive writing shape
- `lark-doc`: create, fetch, search, or update the actual remote document through `lark-cli`

Default routing:

| User request shape | Route |
|---|---|
| “帮我写一个飞书分享稿/知识总览” without remote write | `feishu-doc-writing` only |
| “创建/更新/覆盖这个飞书文档” | `feishu-doc-writing` + `lark-doc` |
| “读取/搜索/下载这个飞书文档内容” | `lark-doc` first, then `feishu-doc-writing` only if content restructuring is requested |
| “插图/附件/画板/媒体” | `lark-doc` (or paired Lark media skill) |

If the request includes both writing quality and real document I/O, do not choose between them. Use both.

When the request also needs a visual summary, pair deliberately instead of improvising:

- `feishu-doc-writing` + `visual-agent` + `visual-knowledge-onepager`
  Use for high-density infographic blocks, one-page HTML, long-image, or poster-like summary visuals.
- `feishu-doc-writing` + `lark-whiteboard`
  Use for editable architecture / flow / layer diagrams that should stay native in Feishu.
- `feishu-doc-writing` + `lark-doc` + one visual skill
  Use when the user wants both content restructuring and direct remote Feishu delivery.

## Core Rules

### 1. Classify the document before writing

Pick one primary role:

- `overview`: entry page, routing, high-level context
- `how-to`: operational steps and boundaries
- `status`: what changed, what is done, what remains
- `deep-dive`: dense explanation, evidence, or edge cases

If a page is trying to do all four, split it.

Before adding a new section, ask one question:

- does this information change the job of the page, or is it only another detail under the same job?

If the page job does not change:

- prefer updating an existing section
- or move the detail into the correct child doc
- do not expand the overview page just because the detail is important

### 2. Keep the first screen cheap

The opening screen should answer:

1. What this document is about
2. Why the reader should care now
3. Where to go next for deeper detail

Preferred opening order:

1. one-line conclusion
2. short context paragraph
3. key bullets or decision table
4. deeper sections

### 3. Write progressively

Order the document from low-cost to high-density:

- summary first
- boundaries and scope next
- concrete guidance after that
- dense explanation and evidence last

If the reader must absorb too much before they can route themselves, the document is structured wrong.

### 3B. Prefer document language, not dialogue language

Published Feishu docs should read like stable guidance, not like a conversation replay.

Rewrite or remove:

- “你可能会问”
- “可以这样理解”
- “如果你看到这里”
- “我们刚才说过”
- direct references to the authoring conversation unless the page is explicitly a retrospective transcript

Prefer:

- direct conclusions
- short explanatory paragraphs
- tables for comparisons, paths, or boundaries
- explicit section labels instead of rhetorical transitions

### 3C. Default to table-first when structure is list-shaped

Use a table instead of prose or long bullets when the content is naturally comparative or matrix-shaped:

- role / responsibility split
- scenario -> tool / route
- signal -> action
- metric -> result
- risk -> mitigation
- before / after
- step -> purpose -> completion signal

Do not use tables just for decoration. Use them when they reduce scanning cost.

### 4. Split when density gets too high

Split the document when:

- one page contains more than 3 dense themes
- explanation starts burying action
- the summary is no longer visible without scrolling through details
- different readers need different depth

When splitting:

- keep the overview page as the stable entry point
- give each child doc one clear purpose
- add explicit “read this next” links
- do not strand detail without a parent overview

### 4C. Keep overview pages on-role

For overview pages:

- keep focus on system model, reading order, decision surface, and doc routing
- keep install prerequisites, CLI setup, and command-level gate details in install/how-to pages
- when new install or gate detail appears, link to the install page instead of re-explaining the whole procedure in the overview

An overview page may mention a gate in one sentence, but it should not turn into the install manual.

### 4B. Keep the document set coherent

If a topic spans multiple docs, keep the set consistent:

- use one naming scheme across overview / runtime / install / validation pages
- keep the same visual language and heading rhythm
- keep overview pages lightweight and child pages single-purpose
- update child-doc labels in the parent page immediately after retitling or reframing

Do not let one page say `Lore / Lore Bootstrap / OpenSpec` while a sibling page already uses `Account Harness`.

### 5. Update context, not just the target page

Before closing an update, check whether the change also requires edits to:

- parent overview pages
- sibling deep-dive docs
- status / evidence pages
- link labels and “updated as of” references

A locally correct edit is still wrong if it leaves surrounding docs inconsistent.

### 6. No dangling TODOs in published updates

Before treating the doc as complete, remove or resolve:

- `TODO`
- `later补`
- `继续写`
- stale placeholders
- outdated next steps that are already done

If something truly remains unfinished, convert it into an explicit boundary or follow-up link rather than leaving an author note in the main flow.

### 7. Close stale visual artifacts

When a document is reframed, also check:

- old diagrams that still encode the previous model
- screenshots or images whose labels no longer match the text
- whiteboards still showing the old hierarchy

Do not keep a stale visual just because the text was updated.

### 7B. Visuals must have a job

Every visual in a Feishu-facing doc should do one of these jobs:

- orient the reader quickly at the top of the doc
- compress a dense multi-part model into one view
- show a structure or flow that is harder to explain with text alone

If a visual does none of the above, remove it.

Default visual choices:

- overview / executive summary: infographic or long-image summary
- architecture / flow / layered relationship: editable Feishu whiteboard
- evidence-heavy page: usually no visual unless it compresses a benchmark or rollout state

### 7C. Match the visual to the reader question

Choose the visual by the question the document must answer:

| Reader question | Preferred visual |
|---|---|
| “这套系统由哪些层组成，谁约束谁，真相源在哪里？” | layered system map / SVG / whiteboard |
| “一次请求或一次执行按什么顺序发生？” | sequence diagram |
| “复杂知识如何一眼总结？” | infographic / retro-grid summary |
| “哪些步骤、角色、结果要并排对照？” | table first, then add a visual only if the table is still too heavy |

Do not default to a sequence diagram when the real goal is to explain:

- how the user drives the agent
- how `AGENTS.md`, `rules`, and `skills` constrain execution
- which tools are execution-only vs truth-bearing
- what artifacts are produced across the lifecycle

For those cases, prefer a layered system map that separates:

- operator / decision authority
- governance and routing constraints
- knowledge and planning surfaces
- execution and verification tools
- artifacts and publishing surfaces

When a document set has both overview and deep-dive pages:

- keep the strongest summary visual on the overview page
- avoid repeating the same visual unchanged across child pages
- make sure visual labels match the current naming system

## Progressive Template

Use this default shape unless the document type clearly needs a different one:

1. `一句话结论`
2. `这篇文档解决什么问题`
3. `适合谁看 / 不适合谁看`
4. `关键结论 / 操作路径`
5. `分主题展开`
6. `延伸阅读 / 相关文档`

When the page is an overview page, add:

7. `你现在该从哪一层开始`

When the page needs a visual companion, load:

- `references/template.md`
- then use `visual-agent` to decide whether the visual should be an infographic
  or long-image (`visual-knowledge-onepager`) or an editable Feishu whiteboard
  (`lark-whiteboard`)

For deeper structure and split guidance, load:

- `references/template.md`

## Format And Layout Checks

Before publishing or syncing, normalize the visible shape:

- one page = one primary job
- opening section fits in one screen where possible
- long list-shaped sections are converted into tables
- paragraphs stay short enough to scan
- headings are parallel and reusable across sibling docs
- callouts are used sparingly for the few points worth visually isolating
- code blocks appear only when commands or exact syntax matter
- evidence pages lead with metric tables before interpretation prose

If the page still feels like “a cleaned-up chat answer”, rewrite it again.

## Human-Readability Checks

Before publishing or syncing, verify:

- first screen is understandable in under 30 seconds
- headings form a logical reading path
- paragraphs are short enough to scan
- tables or callouts are used where they reduce reading cost
- transitions between overview and child docs are explicit
- no unresolved author-side TODO remains in reader-facing content
- page and child-doc titles use one consistent naming scheme
- old diagrams or screenshots are not contradicting the rewritten text

## Publish Gate

Do not treat the Feishu update as complete until all of these are true:

1. the target page reads like a document, not a dialogue
2. at least one table is used where the content is naturally comparative or step-shaped
3. titles across overview / child docs are consistent
4. visuals are either updated, removed, or explicitly left out for a reason
5. a post-update readback confirms the remote doc actually matches the intended shape
6. any system-level visual matches the reader question and is not reduced to a misleading command-order diagram

## Common Failures

| Failure | Root cause | Fix |
|---|---|---|
| One page feels “complete” but impossible to scan | Too many dense themes in one page | Split into overview + deep dives |
| New information keeps becoming new sections | The writer reacts to each addition instead of preserving the page job | Re-classify the page role, then merge into an existing section or move to the correct child doc |
| Updated page still points to stale surrounding docs | Only the target page was edited | Run a context-link pass before closing |
| Reader sees unfinished TODOs after an “update” | Author notes were left in published content | Convert TODO into resolved content or explicit boundary |
| Knowledge is correct but reading experience is poor | Writing optimized for capture, not for reading | Rebuild the first screen and section rhythm progressively |
| Overview page starts explaining install gates and command setup | Page role drifted from overview into how-to | Leave only the summary in overview and move detailed setup to the install page |
