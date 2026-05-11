---
artifact_type: intake
title: visual-output-routing-drift / explore
canonical_object: visual-output-routing-drift
created: 2026-05-11
status: exploring
trace_mode: openspec-explore
source_path: chat://openspec-explore/visual-output-routing-drift/2026-05-11
related_artifacts:
  - /home/yan/.codex/skills/knowledge-article-visual/SKILL.md
  - /home/yan/.codex/skills/infographic-onepager/SKILL.md
  - wiki/ops/agentic-product-engineering-collaboration-workflow-gate-2026-05-11.md
  - wiki/ops/agentic-product-engineering-collaboration-image-model-visual-qa-2026-05-11.md
---

# Visual Output Routing Drift / Explore

## Trigger

The user explicitly invoked `$report-wiki-portfolio:openspec-explore` and asked
why the visual skills kept routing requested images toward H5/SVG instead of
the image model, causing weak visual quality.

The user also clarified the desired decision rule: drawing/output mode must be
chosen by the user. The agent should not silently decide between simple H5,
deterministic SVG/HTML, image model, or hybrid overlay.

## Opening Question

Why did the workflow repeatedly choose H5/SVG/Playwright output after the user
asked for image-model quality visuals?

## Current Hypothesis

The active skill text contains conflicting incentives:

- It says requests for `图`, `图片模型`, and `出图` should use image generation.
- It also says dense Chinese, formal review, Feishu-facing, or exact wording
  should use deterministic SVG/HTML first.
- The second rule was treated as the default escape hatch, so image quality was
  sacrificed for text control without asking the user.

## Findings

### 1. The image request was treated as an artifact request, not a mode decision

`knowledge-article-visual` correctly says not to stop at H5 blocks when the user
asks for `图`, `出图`, `图片`, `一图流`, or `知识卡`. But it groups multiple
outputs together: image prompts, direct image generation, deterministic SVG/HTML,
and hybrid overlay.

That means "produce a visual artifact" was satisfied too early by SVG/HTML PNG
exports, even though the user's quality expectation was image-model aesthetics.

### 2. Dense Chinese created an automatic SVG/HTML fallback

Both visual skills contain this routing pressure:

- dense Chinese / formal / exact wording / Feishu-facing -> deterministic
  SVG/HTML first
- requested image model -> direct image generation unless dense Chinese makes
  deterministic layout safer

The agent repeatedly chose the "safer Chinese text" path without asking whether
the user preferred visual quality over text accuracy for that iteration.

### 3. The report quality gate already had the correct fork, but it was not used

`public-report-quality-gate` says to ask the user at real output fork-points,
including `image model vs H5/HTML`. This rule was stronger than the silent
SVG/HTML fallback, but it was not brought into the active decision at the moment
of generation.

### 4. "HTML as renderer" blurred the output boundary

The workflow used Playwright/SVG/HTML screenshots and called them image assets.
Technically they were PNGs, but visually they still carried H5/PPT/SVG grammar.
The missing distinction was:

- output container: PNG/SVG file exists
- visual generation mode: browser-rendered layout vs image-model illustration
- quality target: deterministic diagram vs hand-drawn image-model infographic

The user was objecting to the second and third points, not only file extension.

### 5. Reference fidelity was checked too late

`account-wiki-onepager.png` was available as a visual reference, but the workflow
first copied high-level labels such as "hand-drawn" and "six sections" rather
than the actual visual grammar: each section is a small explanation graphic,
not a repeated bullet card.

## Root Cause

The root cause is not missing image-generation capability. It is missing
decision ownership at the visual-output fork.

The skills let the agent infer the output mode from text density and formal
accuracy. In this case the user wanted to own the mode decision:

- simple H5 if speed/interaction matters;
- deterministic SVG/HTML if exact Chinese and editability matter;
- image model if visual quality matters;
- hybrid if both image-model aesthetics and exact Chinese are needed.

Because the agent did not stop at that fork, it kept optimizing for
controllable text and generated low-quality H5/SVG-like visuals.

## Desired Boundary

Before producing visual assets, the agent should present the output-mode fork:

- H5 / HTML: fast, simple, interactive, but not image-model quality.
- SVG / deterministic image: accurate Chinese text and editable layout, but can
  look like a diagram or slide if not designed carefully.
- Image model: strongest visual style, but Chinese text may drift and needs
  review.
- Hybrid: image-model visual layer plus deterministic Chinese text overlay.

The user should choose the mode unless they have already clearly specified it.

## Candidate Rule Change

If this becomes an implementation change, the skill behavior should likely be:

1. When the user asks for images or visual assets and the route could be H5,
   SVG/HTML, image model, or hybrid, stop and present the four-mode fork.
2. Do not use "dense Chinese" as an automatic reason to avoid image generation.
   Use it as a risk note under the mode choice.
3. If the user says `图片模型`, `跑图`, `生图`, or complains that output is H5/SVG,
   image-model or hybrid mode becomes the default until the user changes it.
4. A PNG exported from HTML/SVG must be labeled as deterministic rendering, not
   image-model output.
5. Reference images must be decomposed into visual grammar before generation,
   not reduced to generic style words.

## Non-Implementation Boundary

This trace records exploration only. It does not edit skills or repo workflow
rules. Any behavior change to skills or repository defaults needs a separate
OpenSpec change or explicit implementation step after exploration.
