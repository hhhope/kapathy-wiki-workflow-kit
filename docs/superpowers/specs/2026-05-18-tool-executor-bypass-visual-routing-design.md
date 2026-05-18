# Tool Executor Bypass And Visual Routing Design

## Context

The current H5 report work exposed a routing failure: a reader-facing report
visual request was routed directly to `imagegen` after the user mentioned image
model output. That bypassed the parent report workflow and the visual planning
skills.

The repository already has relevant evidence:

- `public-report-quality-gate` delegates article-level visual packages to
  `knowledge-article-visual`, per-image scripts to `infographic-onepager`, and
  bitmap generation to `imagegen`.
- `public-report-quality-gate/references/pressure-scenarios.md` already marks a
  reader-facing H5 visual request routed directly to `imagegen` as a failure.
- `wiki/ops/visual-output-routing-drift-explore-2026-05-11.md` records prior
  visual routing drift around H5/SVG versus image-model output.
- The current H5 has existing hand-drawn Chinese infographic assets, so new
  visuals must first match the report's visual grammar before image generation.

## Approved Direction

Use option B from the brainstorming discussion:

1. Record drift evidence.
2. Strengthen the behavior rule with a generalized anti-pattern:
   `Tool Executor Bypass`.
3. Add scenario replay evidence that this class of request must route through
   the parent workflow before low-level executors.
4. Then produce the requested H5 visuals through the correct chain:
   `public-report-quality-gate -> knowledge-article-visual ->
   infographic-onepager -> imagegen`.

## Design

### 1. Drift Evidence

Create or update a `wiki/ops` drift trace for the 2026-05-18 incident.

It should record:

- Original intent: update H5 report visuals using the article's existing visual
  grammar.
- Drift: the response treated `imagegen` as the main route, generated generic
  low-text illustrations, and skipped article-level visual planning.
- Rejected framing: keyword lists or direct image generation as the primary fix.
- Corrected framing: low-level tools are executors; delivery-sensitive outputs
  must first pass the workflow that owns intent, output shape, review, and
  evidence.
- Next action: route the visual work through `knowledge-article-visual` and
  `infographic-onepager` before any image generation.

### 2. Behavior Asset Change

Open a small OpenSpec change because this modifies repo workflow behavior.

The behavior change should be scoped to repo report/visual routing assets, not
root rules. The current evidence is local to reader-facing report/H5 visual
production.

Preferred target:

- `.codex/skills/public-report-quality-gate/SKILL.md`
- `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`

Do not add a long keyword list to repo `AGENTS.md`.

### 3. Anti-pattern Wording

Add a generalized anti-pattern under the public report gate:

```md
### Anti-pattern: Tool Executor Bypass

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

This keeps the rule reusable without turning it into a brittle trigger-word
patch.

### 4. Scenario Replay

Add replay cases that fail the old behavior and pass the corrected route.

Minimum cases:

- A reader-facing H5 asks for new chapter visuals and mentions image-model
  output. Expected: `public-report-quality-gate` remains the parent route;
  `knowledge-article-visual` owns the visual series; `infographic-onepager`
  scripts each image; `imagegen` is only the final bitmap executor.
- A reader-facing report asks for Feishu sync. Expected: `lark-doc` is only an
  executor after publish gates and read-back boundaries.
- A research task asks to look something up. Expected: web/search is an
  executor after the research or learning workflow owns source selection and
  evidence boundaries.

Record the scenario replay in the OpenSpec evaluation or a repo-visible
`wiki/ops` replay artifact, then reference it from the gate review.

### 5. Visual Production

After the behavior route is repaired, produce the requested visual assets.

Use existing report visuals as the visual reference:

- Warm paper background
- Thick black marker outlines
- Large handwritten Chinese title
- Colored numbered badge
- Boxed modules, doodle icons, and arrows
- Bottom takeaway banner
- 16:9 horizontal teaching-card format for section visuals

The new assets should cover:

1. `02 · 现场对照`: split-account-core information overload, one-person
   bottleneck, and cross-team friction.
2. `03 · 先看结论图`: AI operating system, not an AI tool.
3. `04 · 能力拆法`: AI as eyes, knowledge connector, hands, and feedback loop.
4. `06 · 技术路线图`: one real chain from requirement to knowledge, plan,
   execution, validation, and writeback.
5. `08 · 工作流`: complex demand becomes an AI-participating work graph.
6. `09 · 工程重塑`: delivery pipeline becomes evidence-driven collaboration.

Use `knowledge-article-visual` for the visual series structure, then
`infographic-onepager` for each card script. Because existing assets contain
Chinese text and the user expects the same information-graphic grammar, prefer a
hybrid route if direct image-model text quality is poor: image-model visual
style plus deterministic Chinese overlay.

## Boundaries

- Do not edit root agent rules in this change.
- Do not treat `imagegen` as a parent workflow.
- Do not generate or embed images before the visual scripts exist.
- Do not claim review-ready or share-ready until H5 visual QA is performed.
- Do not include prompt text or production notes inside the reader-facing H5.

## Verification

Before completion, verify:

- OpenSpec change exists for behavior asset edits.
- Drift evidence exists under `wiki/ops`.
- Skill scenario replay covers the executor-bypass case.
- H5 contains the new image references and no prompt residue.
- Generated assets are saved under the repo, not only under the default image
  generation directory.
- HTML parses successfully.
- Desktop and mobile screenshots show the inserted visuals without overlap or
  broken image links.

## Residual Risks

- Direct image-model Chinese text may still be inaccurate; hybrid overlay may be
  required.
- The anti-pattern does not prove automatic future routing. It improves the
  behavior asset and replay evidence, but future execution still depends on
  agents loading and following the gate.
- Share zip regeneration is a separate step and should not be assumed from H5
  asset updates.
