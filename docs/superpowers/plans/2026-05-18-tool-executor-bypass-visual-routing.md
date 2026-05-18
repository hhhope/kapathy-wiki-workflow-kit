# Tool Executor Bypass Visual Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prevent delivery-sensitive report visual work from bypassing parent workflows, then produce the H5's requested section visuals through the correct visual pipeline.

**Architecture:** This change has two layers. First, a repo workflow behavior change formalizes the `Tool Executor Bypass` anti-pattern inside the public report gate and proves it with OpenSpec plus scenario replay. Second, the H5 visual work follows the repaired route: article-level visual plan, per-image scripts, image-model or hybrid assets, HTML embedding, and visual QA.

**Tech Stack:** OpenSpec markdown artifacts, repo-local `.codex/skills/public-report-quality-gate`, wiki ops drift/replay records, existing H5 report HTML, generated bitmap assets, optional deterministic Chinese overlay using local HTML/SVG/PIL tooling.

---

## File Structure

- Create: `openspec/changes/harden-tool-executor-bypass-routing/proposal.md`
  - Explains why this workflow behavior change is needed.
- Create: `openspec/changes/harden-tool-executor-bypass-routing/design.md`
  - Defines the route and proof boundary.
- Create: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`
  - Tracks implementation and verification.
- Create: `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md`
  - Adds the public report gate requirement for `Tool Executor Bypass`.
- Create: `openspec/changes/harden-tool-executor-bypass-routing/evaluation.md`
  - Records RED/GREEN scenario replay for the skill behavior change.
- Create: `wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md`
  - Preserves the live drift incident and corrected route.
- Modify: `.codex/skills/public-report-quality-gate/SKILL.md`
  - Adds a compact anti-pattern section and reinforces parent-gate delegation.
- Modify: `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`
  - Adds executor-bypass replay cases.
- Create: `wiki/ops/agentic-product-engineering-collaboration-workway-visual-production-brief-2026-05-18.md`
  - Holds the article-level visual package and per-image scripts outside the reader-facing H5.
- Create: `wiki/reports/agentic-collaboration-images/workway-02-local-overload.png`
- Create: `wiki/reports/agentic-collaboration-images/workway-03-operating-system.png`
- Create: `wiki/reports/agentic-collaboration-images/workway-04-capability-layers.png`
- Create: `wiki/reports/agentic-collaboration-images/workway-06-technical-route.png`
- Create: `wiki/reports/agentic-collaboration-images/workway-08-work-graph.png`
- Create: `wiki/reports/agentic-collaboration-images/workway-09-evidence-system.png`
- Modify: `wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html`
  - Moves the data strip to the later evidence section and embeds the new assets in the relevant sections.
- Modify: `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md`
  - Records the visual route, generated assets, verification evidence, and remaining share-zip boundary.

## Task 1: Create OpenSpec Change Artifacts

**Files:**
- Create: `openspec/changes/harden-tool-executor-bypass-routing/proposal.md`
- Create: `openspec/changes/harden-tool-executor-bypass-routing/design.md`
- Create: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`
- Create: `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md`

- [ ] **Step 1: Create the change directory and spec directory**

Run:

```bash
mkdir -p openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate
```

Expected: directories exist.

- [ ] **Step 2: Add `proposal.md`**

Create `openspec/changes/harden-tool-executor-bypass-routing/proposal.md` with:

```markdown
# harden-tool-executor-bypass-routing

## Why

The current H5 visual work exposed a workflow bypass: the request needed a
reader-facing report visual package, but execution jumped directly to
`imagegen` after the user mentioned image-model output.

This bypass skipped the parent public report gate, article-level visual
planning, per-image script compression, existing-visual inspection, and review
evidence. The repository already has pressure scenarios for this failure, but
the anti-pattern needs a reusable name and replay evidence so future agents do
not treat low-level tools as parent workflows.

## What Changes

- Add the `Tool Executor Bypass` anti-pattern to
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Add pressure scenarios that verify image generation, Feishu writing, and
  search/browser tools remain executors under parent workflows.
- Record the 2026-05-18 drift evidence in `wiki/ops`.
- Add evaluation evidence for RED baseline and GREEN corrected route.
- Use the corrected route before producing the H5 visual assets.

## Out of Scope

- Editing root agent rules.
- Replacing `knowledge-article-visual`, `infographic-onepager`, or `imagegen`.
- Adding a long trigger-word list to `AGENTS.md`.
- Regenerating the report share zip unless explicitly requested after H5 visual
  updates are accepted.

## Source Design

- `docs/superpowers/specs/2026-05-18-tool-executor-bypass-visual-routing-design.md`
```

- [ ] **Step 3: Add `design.md`**

Create `openspec/changes/harden-tool-executor-bypass-routing/design.md` with:

```markdown
# Design

## Parent Workflow Boundary

Delivery-sensitive work must enter the workflow that owns intent, output shape,
review, and evidence before any low-level executor runs.

For reader-facing reports and H5 pages, `public-report-quality-gate` remains the
outer gate. When the work needs visual assets, it delegates article-level visual
planning to `knowledge-article-visual`, per-image scripts to
`infographic-onepager`, and bitmap generation to `imagegen`.

## Anti-pattern

`Tool Executor Bypass` means routing directly to a low-level tool because the
user mentioned the tool, while skipping the parent workflow that owns the
deliverable.

The first local example is visual production: user asks for H5 section images
and mentions image model; the agent jumps to `imagegen` before inspecting
existing visuals or creating per-image scripts.

## Proof Boundary

The behavior asset and replay evidence improve repo-visible routing. They do
not prove every future client will automatically load the right skill. The proof
only covers repository instructions, skill text, pressure scenarios, and the
current H5 visual route.

## Visual Production Boundary

The H5 visual assets must reuse the existing report grammar: warm paper
background, thick black marker outlines, large handwritten Chinese headings,
colored number badges, boxed modules, arrows, doodle icons, and bottom takeaway
banners.

Image-model output may be used directly only if Chinese text is readable. If
text quality fails, use a hybrid route: image-model background or texture plus
deterministic Chinese text overlay.
```

- [ ] **Step 4: Add `tasks.md`**

Create `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` with:

```markdown
# Tasks

- [ ] 1. Create OpenSpec change artifacts.
- [ ] 2. Record 2026-05-18 tool executor bypass drift evidence.
- [ ] 3. Update public report gate skill wording and pressure scenarios.
- [ ] 4. Add skill evaluation replay evidence.
- [ ] 5. Create H5 visual production brief and per-image scripts.
- [ ] 6. Generate or assemble project-local visual assets.
- [ ] 7. Embed assets in the H5 and update the gate review.
- [ ] 8. Run validation, visual QA, and commit final state.
```

- [ ] **Step 5: Add spec delta**

Create `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md` with:

```markdown
## ADDED Requirements

### Requirement: Public report gate SHALL prevent tool executor bypass

The public report gate SHALL prevent delivery-sensitive reader-facing report
work from routing directly to low-level executors when a parent workflow owns
the output shape, review boundary, or evidence boundary.

#### Scenario: H5 visual request mentions image model

- **WHEN** a reader-facing H5 or report needs new visual assets
- **AND** the user mentions image-model output or another low-level image tool
- **THEN** the public report gate SHALL remain the parent route
- **AND** the workflow SHALL inspect existing visuals when they exist
- **AND** the workflow SHALL produce or reference an article-level visual plan
  and per-image scripts before bitmap generation
- **AND** bitmap generation SHALL be treated as the final executor, not the
  route owner

#### Scenario: Feishu write request follows report drafting

- **WHEN** a reader-facing report or review draft needs Feishu writing
- **THEN** Feishu writing SHALL be treated as an executor after publish,
  judgment, image-boundary, and read-back gates
- **AND** the Feishu tool SHALL NOT replace the workflow that owns readiness
  and evidence

#### Scenario: Research lookup follows source-learning work

- **WHEN** a source-learning or public-report task needs search or browser tools
- **THEN** search and browser tools SHALL be treated as executors under the
  workflow that owns source selection, citation boundary, and evidence
  classification
```

- [ ] **Step 6: Validate OpenSpec formatting**

Run:

```bash
openspec validate harden-tool-executor-bypass-routing --strict
```

Expected: passes. If the local CLI uses another validation shape, run
`openspec status --change harden-tool-executor-bypass-routing --json` and record
the result in the evaluation.

- [ ] **Step 7: Commit Task 1**

Run:

```bash
git status --short
git add openspec/changes/harden-tool-executor-bypass-routing/proposal.md openspec/changes/harden-tool-executor-bypass-routing/design.md openspec/changes/harden-tool-executor-bypass-routing/tasks.md openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md
git commit -m "docs: propose executor bypass routing hardening"
```

Expected: commit includes only the new OpenSpec artifacts.

## Task 2: Record Drift Evidence

**Files:**
- Create: `wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md`
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`

- [ ] **Step 1: Run frontmatter precheck for the new page**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md
```

Expected: target repair hints show required ops frontmatter. Repo-wide warnings
may exist; do not claim whole-repo taxonomy success from this command.

- [ ] **Step 2: Add drift trace**

Create `wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md` with:

```markdown
---
layer: ops
domain: product-engineering-collaboration
ops_area: report-quality
canonical_object: agentic-product-engineering-collaboration-tool-executor-bypass-drift
artifact_type: retro
title: agentic-product-engineering-collaboration tool executor bypass drift 2026-05-18
type: retro
language: zh-CN
status: active
created_at: 2026-05-18
updated_at: 2026-05-18
ai_generated: true
derived_from:
  - chat://2026-05-18/tool-executor-bypass-visual-routing
  - docs/superpowers/specs/2026-05-18-tool-executor-bypass-visual-routing-design.md
related_objects:
  - public-report-quality-gate
  - visual-output-routing-drift
  - agentic-product-engineering-collaboration-our-operating-system
notes_scope: 记录 H5 章节配图任务直接跳到 imagegen 的路由漂移，并锚定 Tool Executor Bypass 作为后续修复对象。
---

# agentic-product-engineering-collaboration tool executor bypass drift 2026-05-18

## Trigger

用户要求为 H5 多个章节重写生成图片，并明确提到图片模型。随后指出：

- 这类任务应该走 `knowledge-article-visual` 和 `infographic-onepager`。
- 不能因为提到图片模型就直接跳到 `imagegen`。
- 原有配图是中文手绘信息图，不是无字插画。

## Original Intent

用户要的是延续原 H5 的视觉语法，为当前文章章节生成可读的中文信息图：

- 先看原有配图。
- 说明每张图要承载的问题。
- 走正确的文章视觉包和单图脚本流程。
- 最后才使用图片模型或混合方案出图。

## Drift Chain

### Drift 1: 把图片模型当成主路由

响应直接进入 `imagegen`，把它当作主流程，而不是最终位图执行器。

### Drift 2: 跳过文章视觉包

没有先由 `knowledge-article-visual` 定义整篇文章的视觉系列和每张图的
位置、职责、递进关系。

### Drift 3: 跳过单图脚本

没有先由 `infographic-onepager` 把章节压缩成标题、结构、模块、图内
元素和底部结论。

### Drift 4: 风格误判

原有图是手绘中文信息图；响应却生成了 generic editorial illustration
风格，并刻意要求无文字，偏离了参考视觉语法。

## Rejected Framing

不采用以下修复方式：

- 在 root 或 repo 主规则中添加一长串图片关键词。
- 把 `imagegen` 作为视觉产物的父流程。
- 用无字氛围图替代原有中文信息图体系。

## Corrected Framing

本次问题归类为 `Tool Executor Bypass`：

> 低层执行器绕过了拥有意图、输出形态、评审和证据边界的上层工作流。

正确顺序：

1. `public-report-quality-gate` 作为 reader-facing H5 外层门禁。
2. `knowledge-article-visual` 定义文章级视觉系列。
3. `infographic-onepager` 产出每张图的脚本和格式。
4. `imagegen` 只作为最终图片模型执行器。

## Next Allowed Action

通过 OpenSpec change 修改 repo 行为资产，补充 scenario replay，然后再按正确视觉链路生产 H5 图片。
```

- [ ] **Step 3: Re-run frontmatter precheck**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md
```

Expected: no target-specific blockers.

- [ ] **Step 4: Mark Task 2 complete in OpenSpec tasks**

Change line 2 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 2. Record 2026-05-18 tool executor bypass drift evidence.
```

- [ ] **Step 5: Commit Task 2**

Run:

```bash
git status --short
git add wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md openspec/changes/harden-tool-executor-bypass-routing/tasks.md
git commit -m "docs: record executor bypass drift"
```

Expected: commit includes only drift evidence and task progress.

## Task 3: Update Public Report Gate And Pressure Scenarios

**Files:**
- Modify: `.codex/skills/public-report-quality-gate/SKILL.md`
- Modify: `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`

- [ ] **Step 1: Load required semantic skill-edit guidance**

Run:

```bash
sed -n '1,220p' /home/yan/.codex/skills/writing-skills/SKILL.md
sed -n '1,220p' /home/yan/.codex/skills/test-driven-development/SKILL.md
```

Expected: guidance is read before semantic skill edits.

- [ ] **Step 2: Add anti-pattern to public report gate**

Insert this section before `## Common Mistakes` in
`.codex/skills/public-report-quality-gate/SKILL.md`:

```markdown
## Anti-pattern: Tool Executor Bypass

Do not route a delivery-sensitive task directly to a low-level executor when a
parent workflow owns the output shape.

Example: if a reader-facing H5 report needs new visual assets, do not jump
straight to image generation because the user mentioned an image model. First
follow the report visual workflow: confirm the visual job, inspect existing
visuals, create the article-level visual plan, script each visual, and only then
use the image tool as the final executor.

The same principle applies outside visuals: search, browser, image generation,
Feishu writing, and code execution tools are executors, not substitutes for the
workflow that owns intent, output shape, review, and evidence.
```

- [ ] **Step 3: Add pressure scenarios**

In `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`,
under `## Public Output Delegation Replay`, add these rows:

```markdown
| User asks for a reader-facing H5 report's section images and mentions image-model output, but no visual package or per-image script exists | Outer Gate Role + Visual Gate + Tool Executor Bypass | FAIL; `public-report-quality-gate` remains the parent route, `knowledge-article-visual` owns the visual series, `infographic-onepager` scripts each image, and `imagegen` is only the final bitmap executor |
| User asks to sync a reader-facing report to Feishu and the agent jumps directly to `lark-doc` | Publish Gate + Tool Executor Bypass | FAIL; Feishu writing is an executor after readiness, judgment, image-boundary, and read-back gates |
| User asks for source-backed report research and the agent jumps directly to search/browser results without source workflow boundaries | Learning Use Gate + Evidence Boundary + Tool Executor Bypass | FAIL; search and browser tools are executors under the workflow that owns source selection, citation boundary, and evidence classification |
```

- [ ] **Step 4: Mark Task 3 complete**

Change line 3 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 3. Update public report gate skill wording and pressure scenarios.
```

- [ ] **Step 5: Commit Task 3**

Run:

```bash
git status --short
git add .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/public-report-quality-gate/references/pressure-scenarios.md openspec/changes/harden-tool-executor-bypass-routing/tasks.md
git commit -m "docs: prevent tool executor bypass"
```

Expected: commit includes only the public report gate, pressure scenarios, and task progress.

## Task 4: Add Skill Evaluation Replay Evidence

**Files:**
- Create: `openspec/changes/harden-tool-executor-bypass-routing/evaluation.md`
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`

- [ ] **Step 1: Add evaluation evidence**

Create `openspec/changes/harden-tool-executor-bypass-routing/evaluation.md` with:

```markdown
# Evaluation: tool executor bypass routing

## Pressure Scenarios

### Scenario 1: H5 visual request mentions image model

Input shape: user names an existing reader-facing H5 and asks for section
visuals using image-model output.

RED baseline: route goes directly to `imagegen`; no existing visual inspection,
no article-level visual plan, no per-image script.

GREEN result: `public-report-quality-gate` remains the parent route;
`knowledge-article-visual` owns the visual series; `infographic-onepager`
scripts each visual; `imagegen` is final bitmap executor only.

### Scenario 2: Feishu sync request

Input shape: user asks to sync a reader-facing report to Feishu.

RED baseline: route goes directly to `lark-doc`.

GREEN result: publish, judgment, image-boundary, and read-back gates run before
Feishu writing; `lark-doc` is only the executor.

### Scenario 3: Source-backed report research

Input shape: user asks for source-backed report research.

RED baseline: route jumps directly to search/browser output and treats search
results as source judgment.

GREEN result: source workflow owns source selection, citation boundary, and
evidence classification; search/browser is only the executor.

## RED Baseline

The 2026-05-18 H5 visual incident demonstrates RED behavior: `imagegen` was
used as the main route after the user mentioned image-model output. The response
did not first inspect existing report visuals, create an article-level visual
plan, or script each visual.

## GREEN Result

The updated public report gate names `Tool Executor Bypass` and pressure
scenarios require the parent route before executor use. The current H5 visual
work will use:

`public-report-quality-gate -> knowledge-article-visual -> infographic-onepager -> imagegen`

## Prior-Art / Common-Rule Dedupe

- Repo `AGENTS.md` already owns general Agent Intent Routing and High-Frequency
  Skills.
- `public-report-quality-gate` already owns reader-facing report/H5 output.
- This change does not duplicate root git, testing, file-size, or generic
  engineering rules.
- This change does not add a second route table; it adds an anti-pattern inside
  the existing public report gate.

## Proof Boundary

This evidence proves repo-visible wording and replay coverage. It does not
prove every future agent will load and follow the skill automatically.

## Residual Risks

- Direct image-model Chinese text may still require hybrid overlay.
- Existing pressure scenarios are markdown evidence, not executable dispatch
  tests.
- Root agent behavior is intentionally unchanged.
```

- [ ] **Step 2: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: if non-zero appears because of known legacy issues, preserve the
result in evaluation or final notes. Do not claim full behavior-asset compliance
from memory.

- [ ] **Step 3: Validate OpenSpec**

Run:

```bash
openspec validate harden-tool-executor-bypass-routing --strict
```

Expected: pass.

- [ ] **Step 4: Mark Task 4 complete**

Change line 4 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 4. Add skill evaluation replay evidence.
```

- [ ] **Step 5: Commit Task 4**

Run:

```bash
git status --short
git add openspec/changes/harden-tool-executor-bypass-routing/evaluation.md openspec/changes/harden-tool-executor-bypass-routing/tasks.md
git commit -m "docs: add executor bypass replay evidence"
```

Expected: commit includes only evaluation evidence and task progress.

## Task 5: Create H5 Visual Production Brief And Scripts

**Files:**
- Create: `wiki/ops/agentic-product-engineering-collaboration-workway-visual-production-brief-2026-05-18.md`
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`

- [ ] **Step 1: Run frontmatter precheck for visual brief**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/agentic-product-engineering-collaboration-workway-visual-production-brief-2026-05-18.md
```

Expected: target repair hints show ops frontmatter requirements.

- [ ] **Step 2: Create visual production brief**

Create `wiki/ops/agentic-product-engineering-collaboration-workway-visual-production-brief-2026-05-18.md` with the following structure and content:

```markdown
---
layer: ops
domain: product-engineering-collaboration
ops_area: report-quality
canonical_object: agentic-product-engineering-collaboration-workway-visual-production
artifact_type: visual-production-brief
title: agentic-product-engineering-collaboration workway visual production brief 2026-05-18
type: visual-production-brief
language: zh-CN
status: active
created_at: 2026-05-18
updated_at: 2026-05-18
ai_generated: true
derived_from:
  - wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
  - wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md
related_objects:
  - public-report-quality-gate
  - knowledge-article-visual
  - infographic-onepager
notes_scope: 记录 H5 工作方式重写版本的章节配图脚本和图片模型 / hybrid 输出边界。
---

# agentic-product-engineering-collaboration workway visual production brief 2026-05-18

## Route

Parent gate: `public-report-quality-gate`.

Visual series owner: `knowledge-article-visual`.

Per-image script owner: `infographic-onepager`.

Bitmap executor: `imagegen`, only after scripts exist.

## Reference Visual Grammar

- 16:9 horizontal teaching-card format.
- Warm paper background.
- Thick black marker border.
- Large handwritten Chinese title.
- Colored numbered badge.
- Boxed modules, doodle icons, arrows.
- Bottom takeaway banner.
- Avoid generic no-text editorial illustrations.

## Output Mode

Preferred: hybrid if direct image-model Chinese text is not reliable.

The image model can provide paper texture, marker feel, doodle icons, rough
layout, and visual atmosphere. Exact Chinese text should be deterministic if
direct output is broken.

## Visual Scripts

### 02 现场对照

Title: 分账核心不是缺资料

Subtitle: 16 场会议、9 个需求、6 个详设、3 份纪要，仍然会信息过载。

Panels:

1. 资料很多：会议、需求、详设、日报。
2. 一号位卡点：历史需求、代码考古、接口兼容都压到一个人。
3. 团队摩擦：支付、账户、清结算、测试各有局部事实。
4. 新做法：AI 把需求、代码、接口、问题和风险连成工作图。

Bottom: 问题不是没有信息，而是没有共同维护的全局工作图。

### 03 先看结论图

Title: 不是 AI 工具，是 AI 作业系统

Subtitle: AI 要有眼睛、手脚和反馈链，才能进入公司体系工作。

Panels:

1. 眼睛：看见原话、需求、历史边界。
2. 知识：连接文档、代码、会议、测试。
3. 手脚：进入 repo、数据、截图、日志。
4. 反馈：真实验证、风险暴露、失败写回。

Bottom: 不是多一个聊天入口，而是重写工作方式。

### 04 能力拆法

Title: AI 放大人的判断

Subtitle: 通用模型做理解和推演，垂直知识库保存组织经验。

Panels:

1. 意图识别：把模糊需求变成可验收对象。
2. 知识关联：把历史和代码背景找出来。
3. 方案推演：多方案、反方意见、风险评分。
4. 验证反馈：真实证据和写回规则。

Bottom: 人负责目标和取舍，AI 放大判断依据。

### 06 技术路线图

Title: 先跑通一条真实链路

Subtitle: 不先搭平台，先让一个复杂需求可追踪、可比较、可验证。

Panels:

1. 需求成型：原话、对象、非目标、验收路径。
2. 知识关联：需求、详设、会议、代码、问题。
3. 方案竞争：快上、稳妥、长期、不做。
4. 执行验证：工具执行、真实数据、截图日志、写回。

Bottom: 每一步都要把判断变成可试、可证、可写回的对象。

### 08 工作流

Title: 复杂需求变成工作图

Subtitle: 从人翻材料，变成 AI 连接上下文，人做判断。

Panels:

1. 旧：人开会、人翻文档、人追状态。
2. 新：AI 连接需求、知识、代码、测试、风险。
3. 人：确认目标、边界、优先级、上线取舍。
4. 系统：留下证据、依赖、阻塞、写回。

Bottom: 会议不再同步全部信息，而是处理冲突和待判断问题。

### 09 工程重塑

Title: 从交付流水线到证据协作

Subtitle: 软件工程不只交代码，而是交可判断的证据链。

Panels:

1. 旧流水线：需求 -> 开发 -> 测试 -> 上线。
2. 新协作：意图 -> 知识 -> 方案 -> 执行 -> 验证 -> 写回。
3. 证据：真实 DB、API、权限、截图、日志。
4. 组织：一号位不再孤立判断，团队共享依据。

Bottom: 目标人定，过程可委托，结果可审计。
```

- [ ] **Step 3: Run frontmatter precheck again**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/agentic-product-engineering-collaboration-workway-visual-production-brief-2026-05-18.md
```

Expected: no target-specific blockers.

- [ ] **Step 4: Mark Task 5 complete**

Change line 5 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 5. Create H5 visual production brief and per-image scripts.
```

- [ ] **Step 5: Commit Task 5**

Run:

```bash
git status --short
git add wiki/ops/agentic-product-engineering-collaboration-workway-visual-production-brief-2026-05-18.md openspec/changes/harden-tool-executor-bypass-routing/tasks.md
git commit -m "docs: script workway report visuals"
```

Expected: commit includes visual production brief and task progress.

## Task 6: Generate Or Assemble Visual Assets

**Files:**
- Create: six `wiki/reports/agentic-collaboration-images/workway-*.png`
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`

- [ ] **Step 1: Use image model only after scripts exist**

Use the built-in image generation tool for each scripted asset. Generate image-model backgrounds or full cards. If generated Chinese text is broken, assemble hybrid cards with deterministic Chinese overlay.

Prompt shape for each asset:

```text
Create a 16:9 Chinese hand-drawn infographic teaching card in the same visual grammar as a warm paper sketchnote report card: thick black marker border, large handwritten Chinese title, colored numbered badge, boxed modules, doodle icons, arrows, pastel accents, bottom takeaway banner.

Use the following Chinese script exactly if possible:
[paste the corresponding script from the visual production brief]

Keep all Chinese text crisp and readable. No tiny text, no overlap, no QR code, no watermark, no unrelated logos.
```

- [ ] **Step 2: Copy generated assets into the repo**

For each selected generated image, copy from the generated image directory to:

```bash
cp <generated-image-path> wiki/reports/agentic-collaboration-images/workway-02-local-overload.png
cp <generated-image-path> wiki/reports/agentic-collaboration-images/workway-03-operating-system.png
cp <generated-image-path> wiki/reports/agentic-collaboration-images/workway-04-capability-layers.png
cp <generated-image-path> wiki/reports/agentic-collaboration-images/workway-06-technical-route.png
cp <generated-image-path> wiki/reports/agentic-collaboration-images/workway-08-work-graph.png
cp <generated-image-path> wiki/reports/agentic-collaboration-images/workway-09-evidence-system.png
```

Expected: files exist under `wiki/reports/agentic-collaboration-images/`.

- [ ] **Step 3: Inspect image dimensions**

Run:

```bash
file wiki/reports/agentic-collaboration-images/workway-*.png
```

Expected: six PNG files. Prefer 16:9 or near-16:9 dimensions.

- [ ] **Step 4: If Chinese text is broken, create hybrid corrected assets**

Use an HTML/SVG/PIL overlay only for the Chinese text. Keep the final file paths the same `workway-*.png`.

Validation target:

- Title readable.
- Panel labels readable.
- Bottom takeaway readable.
- No obvious overlap.

- [ ] **Step 5: Mark Task 6 complete**

Change line 6 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 6. Generate or assemble project-local visual assets.
```

- [ ] **Step 6: Commit Task 6**

Run:

```bash
git status --short
git add wiki/reports/agentic-collaboration-images/workway-02-local-overload.png wiki/reports/agentic-collaboration-images/workway-03-operating-system.png wiki/reports/agentic-collaboration-images/workway-04-capability-layers.png wiki/reports/agentic-collaboration-images/workway-06-technical-route.png wiki/reports/agentic-collaboration-images/workway-08-work-graph.png wiki/reports/agentic-collaboration-images/workway-09-evidence-system.png openspec/changes/harden-tool-executor-bypass-routing/tasks.md
git commit -m "docs: add workway report visuals"
```

Expected: commit includes only image assets and task progress.

## Task 7: Embed Visuals In H5 And Update Gate Review

**Files:**
- Modify: `wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html`
- Modify: `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md`
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`

- [ ] **Step 1: Move the data strip near evidence sections**

In the H5, move the current `<aside class="data-strip">...</aside>` from below
`</header>` to just before section `10 · 模式数据`.

Expected: opening argument no longer starts with repo metric tiles; metrics are
introduced after local story and method.

- [ ] **Step 2: Replace section 02 image**

Change the image in section `02 · 现场对照` to:

```html
<img src="agentic-collaboration-images/workway-02-local-overload.png" alt="分账核心信息过载与协作摩擦">
<p class="caption">分账核心不是资料不足，而是需求、详设、会议、测试日报、代码背景和上线风险没有形成共同维护的全局工作图。</p>
```

- [ ] **Step 3: Replace section 03 poster image**

Change the poster image in section `03 · 先看结论图` to:

```html
<img src="agentic-collaboration-images/workway-03-operating-system.png" alt="AI 作业系统总览">
```

- [ ] **Step 4: Add section 04 image**

After the source note in section `04 · 能力拆法`, add:

```html
<div class="image-band">
  <img src="agentic-collaboration-images/workway-04-capability-layers.png" alt="AI 能力层放大人的判断">
  <p class="caption">AI 的价值不是替代专业判断，而是用意图识别、知识关联、方案推演、工具执行和验证反馈放大人的能力。</p>
</div>
```

- [ ] **Step 5: Add section 06 image**

After the opening paragraph in section `06 · 技术路线图`, add:

```html
<div class="image-band">
  <img src="agentic-collaboration-images/workway-06-technical-route.png" alt="AI 作业系统技术路线图">
  <p class="caption">技术路线先跑通一条真实链路：需求成型、知识关联、方案竞争、工具执行、真实验证和失败写回。</p>
</div>
```

- [ ] **Step 6: Add section 08 image**

After the opening paragraph in section `08 · 工作流`, add:

```html
<div class="image-band">
  <img src="agentic-collaboration-images/workway-08-work-graph.png" alt="复杂需求变成 AI 可参与的工作图">
  <p class="caption">复杂需求不再靠人翻材料和反复同步，而是让 AI 连接上下文，团队围绕冲突、阻塞和待判断问题协作。</p>
</div>
```

- [ ] **Step 7: Add section 09 image**

At the start of section `09 · 工程重塑`, before `<div class="role-list">`, add:

```html
<div class="image-band">
  <img src="agentic-collaboration-images/workway-09-evidence-system.png" alt="从交付流水线到证据驱动协作系统">
  <p class="caption">软件工程不只交代码，而是交可判断的证据链：意图、知识、方案、执行、验证和写回都要能被回放。</p>
</div>
```

- [ ] **Step 8: Update gate review**

In `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md`, add a new section:

```markdown
Visual routing correction on 2026-05-18:

- User feedback: section visuals must follow the existing hand-drawn Chinese
  infographic grammar and route through the report visual workflow, not direct
  `imagegen`.
- Response: added tool-executor-bypass drift evidence, OpenSpec behavior
  change, visual production brief, and six section visual assets:
  `workway-02-local-overload.png`, `workway-03-operating-system.png`,
  `workway-04-capability-layers.png`, `workway-06-technical-route.png`,
  `workway-08-work-graph.png`, and `workway-09-evidence-system.png`.
```

- [ ] **Step 9: Mark Task 7 complete**

Change line 7 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 7. Embed assets in the H5 and update the gate review.
```

- [ ] **Step 10: Commit Task 7**

Run:

```bash
git status --short
git add wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md openspec/changes/harden-tool-executor-bypass-routing/tasks.md
git commit -m "docs: embed workway report visuals"
```

Expected: commit includes only H5, gate review, and task progress.

## Task 8: Final Verification And Completion

**Files:**
- Modify: `openspec/changes/harden-tool-executor-bypass-routing/tasks.md`
- Optionally modify: `openspec/changes/harden-tool-executor-bypass-routing/evaluation.md`

- [ ] **Step 1: HTML syntax check**

Run:

```bash
python3 -m html.parser wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
```

Expected: exit code 0.

- [ ] **Step 2: Broken asset reference check**

Run:

```bash
rg -n "workway-.*\\.png|agentic-collaboration-images/" wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
file wiki/reports/agentic-collaboration-images/workway-*.png
```

Expected: every new image referenced in HTML exists under
`wiki/reports/agentic-collaboration-images/`.

- [ ] **Step 3: Old route residue check**

Run:

```bash
rg -n "直接 imagegen|直接跳到 imagegen|图片模型.*直接|prompt text|Hybrid routing" wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
```

Expected: no matches in reader-facing HTML.

- [ ] **Step 4: Visual screenshots**

Run:

```bash
playwright screenshot --full-page file:///mnt/d/cloud/account-meeting-lore/wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html /tmp/our-operating-system-workway-visuals.png
playwright screenshot --viewport-size=390,1200 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html /tmp/our-operating-system-workway-visuals-mobile.png
```

Expected: screenshots are created and show no broken image icons or obvious
layout overlap.

- [ ] **Step 5: OpenSpec validation**

Run:

```bash
openspec validate harden-tool-executor-bypass-routing --strict
```

Expected: pass.

- [ ] **Step 6: Diff check**

Run:

```bash
git diff --check
```

Expected: exit code 0.

- [ ] **Step 7: Mark Task 8 complete**

Change line 8 in `openspec/changes/harden-tool-executor-bypass-routing/tasks.md` to:

```markdown
- [x] 8. Run validation, visual QA, and commit final state.
```

- [ ] **Step 8: Commit final verification**

Run:

```bash
git status --short
git add openspec/changes/harden-tool-executor-bypass-routing/tasks.md openspec/changes/harden-tool-executor-bypass-routing/evaluation.md
git commit -m "docs: complete executor bypass visual routing"
```

Expected: commit includes final task progress and any evaluation updates.

- [ ] **Step 9: Final git truth check**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: latest commit is the final verification commit. Unrelated dirty files
may remain and must be classified as outside this task boundary.

## Self-Review

Spec coverage:

- Drift evidence is covered by Task 2.
- Public report gate anti-pattern and pressure scenarios are covered by Task 3.
- Scenario replay and skill evaluation are covered by Task 4.
- Visual scripts are covered by Task 5.
- Image generation or hybrid assembly is covered by Task 6.
- H5 embedding and gate review are covered by Task 7.
- Validation and final evidence are covered by Task 8.

Placeholder scan:

- The plan intentionally uses concrete file paths, exact markdown content, exact
  commands, and expected results.
- The phrase `Optional` appears only for an already-created evaluation file in
  Task 8 and does not leave implementation unspecified.

Scope check:

- Root agent rules are explicitly out of scope.
- Share zip regeneration is explicitly out of scope unless separately requested.
