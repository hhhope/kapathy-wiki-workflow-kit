---
artifact_type: ops-execution-plan
title: agentic-product-engineering-collaboration / split execution
canonical_object: agentic-product-engineering-collaboration
created: 2026-05-11
status: active
derived_from:
  - wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
  - wiki/reports/assets/
  - wiki/reports/agentic-visual-assets/
---

# Agentic Product Engineering Collaboration / Split Execution

## Purpose

This file splits the next work into independent tracks. The immediate goal is
to stop mixing article editing, H5 layout, chart repair, source capture, and
image production into one loop.

North star: rebuild the visual package and article evidence separately, then
only reconnect them after each track has passed its own check.

## Split Tracks

| Track | Owns | Does Not Own | First Output |
|---|---|---|---|
| A. Visual Production | 5 standalone image assets, reference style, image-model/hybrid route, visual QA | Final article prose, Feishu sync, H5 polish | `wiki/ops/agentic-product-engineering-collaboration-visual-production-brief-2026-05-11.md` |
| B. Article Evidence | Chapter claims, evidence load, citation boundaries, hard-reference gaps | Image layout, H5 styling, Feishu sync | `wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md` |
| C. Workflow Gate | Execution order, gates, allowed transitions, anti-drift rules | Writing all prose or drawing all images | `wiki/ops/agentic-product-engineering-collaboration-workflow-gate-2026-05-11.md` |

## Track A: Visual Production

Status: split into dedicated brief.

Required assets:

1. `00-total-infographic`
2. `01-industry-debate`
3. `02-company-dumbbell`
4. `03-operating-system`
5. `04-reviewable-loop`

Reference style:

- Use `wiki/reports/assets/account-wiki-onepager.png` for the total long-poster
  grammar.
- Use `wiki/reports/assets/account-wiki-runtime-card.png` and
  `wiki/reports/assets/account-wiki-validation-card.png` for horizontal
  teaching-card grammar.
- Current files under `wiki/reports/agentic-visual-assets/` are content drafts,
  not the visual quality bar.

Mandatory route decision:

- If exact Chinese and dense text dominate, use hybrid: image-model or
  illustration-like background plus deterministic Chinese text overlay.
- If a pure image model is used, it must be treated as a style draft until
  Chinese readability is inspected.
- HTML may be used only as an image renderer or overlay tool, not as an H5
  substitute for image output.

Dedicated output:

- `wiki/ops/agentic-product-engineering-collaboration-visual-production-brief-2026-05-11.md`

Acceptance:

- First glance reads as hand-drawn Chinese knowledge infographic, not webpage or
  PPT screenshot.
- Every main module has a concrete visual object or action.
- Thumbnail reveals structure; zoom reveals details.
- Chinese text is readable and not distorted.
- No overclaim: 262 is source-pool size, not all-web total.

## Track B: Article Evidence

Status: split into dedicated matrix.

Chapters to handle:

1. `行业在争什么`
2. `公司的位置更像哑铃`
3. `作业系统变了`
4. `Agent 把中间执行层变成可审查的工作循环`
5. `人怎么变`

For every chapter, record:

- Core claim.
- Evidence that can carry the claim.
- Evidence that is only a route or discussion signal.
- Boundary sentence.
- Hard references still needed before publication.

Acceptance:

- No chapter rests mainly on vendor marketing copy.
- Podcast/video claims are not quoted without transcript capture.
- WeChat and secondary summaries are marked as claim routers.
- The dumbbell model remains a candidate observation frame.
- Human judgment ownership remains explicit.

Dedicated output:

- `wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md`

## Track C: Workflow Gate

Status: split into dedicated gate.

Required order:

1. Confirm split route.
2. Build visual scripts and evidence matrix.
3. Generate or redraw standalone image assets.
4. Inspect image outputs against reference grammar.
5. Update report gate review.
6. Only then decide whether to embed images into H5.
7. Feishu sync remains out of scope until the report gate passes.

Stop conditions:

- If the output is only H5 sections, stop and reroute to visual production.
- If image model text is unreadable, stop and switch to hybrid overlay.
- If a chapter needs hard claims from podcasts/videos, stop before public
  citation and capture transcript or source notes.
- If a visual is decorative and does not carry a claim, remove or redesign it.

Dedicated output:

- `wiki/ops/agentic-product-engineering-collaboration-workflow-gate-2026-05-11.md`

## Current Decision

Proceed with parallel preparation only. Do not modify the H5 or overwrite
current image assets until the five-image production route and chapter evidence
matrix are explicit.
