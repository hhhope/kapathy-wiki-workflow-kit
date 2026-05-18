---
artifact_type: ops-handoff
title: agentic-product-engineering-collaboration / session handoff
canonical_object: agentic-product-engineering-collaboration
layer: ops
domain: product-engineering-collaboration
ops_area: workflow-trace
created: 2026-05-11
updated: 2026-05-11 15:09 CST
status: active
derived_from:
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md
  - wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md
  - wiki/reports/agentic-product-engineering-collaboration-management-report.md
  - wiki/reports/agentic-product-engineering-collaboration-newspaper.html
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/assets/account-wiki-runtime-card.png
  - wiki/reports/assets/account-wiki-validation-card.png
  - wiki/reports/agentic-visual-assets/
---

# Agentic Product Engineering Collaboration / Session Handoff

## Purpose

This note preserves the live-session context before compaction. It records what
was collected, what the user rejected, what requirements emerged, which skills
were corrected, and what the next agent should do.

North star: produce a reader-facing Chinese article/report about how AI agents
change product-engineering collaboration, with source-backed argumentation and
real visual assets. The desired output is not a chat recap, not a text-heavy H5,
and not a set of decorative charts.

## Current User Correction

The user pointed to `wiki/reports/assets/` as visual examples and said the
current generated images are still poor because they are H5/HTML-based outputs,
not image-model or high-quality infographic outputs.

Important interpretation:

- Treat `wiki/reports/assets/*.png` as the visual reference set.
- Treat `wiki/reports/agentic-visual-assets/*.png` as a failed or partial
  attempt, even though they render Chinese text correctly.
- Do not defend the current PNGs as "images" merely because Playwright exported
  screenshots.
- The next step is to inspect the reference visual grammar, then regenerate the
  article visuals in that grammar or with an explicit image-model / hybrid
  pipeline.

## Source Collection Requirements Learned

The source work expanded several times because the first pass was too narrow.

Current source inventory:

| Layer | Count | File | Use Boundary |
|---|---:|---|---|
| Curated source map | 43 | `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md` | Main cited source map. |
| Broad scan leads | 88 | `wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md` | Discovery breadth; not every lead is deeply read. |
| Public timeline | 95 | `wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md` | Chronological public discussion layer. |
| Podcast/video discussion pool | 36 | `wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md` | Role and operating-model language; transcript capture needed before hard quoting. |
| Total entries/leads | 262 | across the four source files | Not deduplicated and not "all web" coverage. |

Requirements that emerged:

- Do not stop at articles and product posts. Add podcast, video, interview, and
  operator discussion layers.
- Count sources by class, not as one undifferentiated pile.
- Separate primary company posts, research/survey material, operator
  interviews, secondary summaries, Chinese syntheses, and discovery indexes.
- WeChat posts and podcast summaries can route claims, but final hard claims
  need upstream interview, memo, transcript, company post, or report evidence.
- Use "broad scan" or "public source pool"; do not claim exhaustive "全网".
- The evidence model must say what each source class can and cannot support.

Timeline counts currently used in the visual/report draft:

| Month | Public timeline | Podcast/video | Combined |
|---|---:|---:|---:|
| 2026-01 | 11 | 10 | 21 |
| 2026-02 | 23 | 7 | 30 |
| 2026-03 | 16 | 11 | 27 |
| 2026-04 | 26 | 7 | 33 |
| 2026-05 through 2026-05-11 | 19 | 1 | 20 |

## Article And Report Requirements Learned

The first versions were rejected because they did not follow the quality gate:
too much text, not enough visuals, weak evidence handling, and the "讨论如何推进"
piece was just timeline text rather than a readable chart.

Active article intent:

| Field | Current Contract |
|---|---|
| Reader | Mixed management: business owner, product engineering lead, technical lead. |
| Reader decision | Decide whether to run a 30-60 day pilot for AI-agent-assisted product-engineering collaboration. |
| Main line | AI agents do not create a middle layer from nothing; they turn part of existing human/process middle work into executable, reviewable, reusable operating work. |
| Non-goals | Do not claim full automation, universal replacement, or neutral proof from vendor metrics. |
| User-owned judgment | Final strategic stance, pilot scope, org ownership, and local boundary of human judgment. |

Required chapters / argument blocks:

1. `行业在争什么`
   - Show the dispute axes directly.
   - Include quantities and change over time.
   - Make the discussion source-backed, not impressionistic.

2. `公司的位置更像哑铃`
   - Must compare traditional collaboration and AI-era collaboration.
   - Traditional collaboration already had middle layers: PM, TL, QA, Ops,
     meetings, Jira, docs, scripts, RPA, and human/process translation.
   - The "dumbbell" is a candidate observation frame, not an established
     industry conclusion.
   - One end: execution automation surfaces such as issue, IDE, PR, CI, agent
     queues.
   - Other end: organization governance such as permissions, audit, ownership,
     accountability, knowledge, and risk.
   - Middle bridge: spec, eval, review, owner, and writeback systems.

3. `作业系统变了`
   - The shift is from person-to-person handoff to work objects that agents can
     read, execute, verify, and write back.
   - Ticket, spec, PR, eval, wiki, CI, logs, and review packet become production
     objects.

4. `循环图：Agent 把中间执行层变成可审查的工作循环`
   - Do not imply there was no middle layer before.
   - Agent value is not "first middle layer"; it is making part of middle work
     callable, auditable, replayable, and reusable.
   - The loop should show target setting, executable context, agent queue,
     review packet, replay trail, and system writeback.

5. `人怎么变`
   - Must answer what existing company roles should do.
   - Suggested role view: CEO/GM, Product/PM, Designer/Research,
     Engineer/TL, QA/Data/Ops, Manager/HR.
   - Human responsibility moves toward goals, boundaries, acceptance,
     judgment, risk, and system design.

## Public Report Quality Gate State

The gate artifact is
`wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`.

Current state:

- Overall score remains `INVALID`.
- Reference Structure Gate: `PARTIAL`.
- Paragraph Drift Gate: `PARTIAL`.
- Judgment Ownership Gate: `PARTIAL`.
- Visual Gate: `PARTIAL`.
- Publish Gate: `FAIL`.
- Draft can be used for internal discussion only.
- Do not claim review-ready, Feishu-ready, or publish-ready.

The key unresolved failure is visual output quality. The H5 now has more
sections and charts, and standalone PNGs exist, but the current visual language
does not match the reference examples or the user's image-output expectation.

## Visual Reference Inspection

Reference images:

- `wiki/reports/assets/account-wiki-onepager.png`
- `wiki/reports/assets/account-wiki-runtime-card.png`
- `wiki/reports/assets/account-wiki-validation-card.png`

Observed reference grammar:

- Hand-drawn educational poster style, not SaaS dashboard or webpage card.
- Warm paper background with subtle texture.
- Thick black marker outlines, slightly imperfect borders, and visible
  sketch-like strokes.
- Large handwritten Chinese titles, high hierarchy, and marker underlines.
- Colored section labels and numbered badges.
- Doodle icons carry meaning: documents, folders, magnifier, signpost, pencil,
  clipboard, chains, arrows, star, chart.
- Content density is high, but each area is chunked into panels with a clear
  reading order.
- Visual explanation is primary; text supports the drawing rather than filling
  a web card.
- Bottom golden sentence / takeaway banner is a stable pattern.

Current generated visual assets:

- `wiki/reports/agentic-visual-assets/00-total-infographic.png`
- `wiki/reports/agentic-visual-assets/01-industry-debate-card.png`
- `wiki/reports/agentic-visual-assets/02-company-dumbbell-card.png`
- `wiki/reports/agentic-visual-assets/03-operating-system-card.png`
- `wiki/reports/agentic-visual-assets/04-reviewable-loop-card.png`
- HTML sources in the same directory.

Why current assets are insufficient:

- They are deterministic HTML/CSS screenshots exported to PNG.
- They render Chinese, but visually read as browser/H5 cards rather than
  image-model or sketchnote infographic output.
- The total infographic is more like a table of text blocks than a visual map.
- The dumbbell card uses large empty circles but too few internal visual cues;
  it says the concept more than it draws the transformation.
- The card system has limited doodle/icon evidence, weak hand-drawn texture,
  and too much UI/card geometry.
- It does not use the reference images' marker strokes, illustration density,
  or strong visual metaphors.

Card-level visual diagnosis:

| Current asset | Problem |
|---|---|
| `00-total-infographic.png` | Long image exists, but the structure is mostly two columns of text modules. It lacks the reference poster's mixed visual language: objects, flows, contrasts, callouts, and chapter-by-chapter teaching rhythm. |
| `01-industry-debate-card.png` | Debate is expressed as grid cards, not as a visual dispute map. It needs a compass, tension axis, scale, arena, or other metaphor that shows conflict before the reader reads every word. |
| `02-company-dumbbell-card.png` | The dumbbell appears as two clean CSS circles and a bridge, with too much empty space. It needs concrete objects for execution automation, organization governance, and middle review/spec/eval ownership. |
| `03-operating-system-card.png` | The content is directionally right, but it still uses pills/cards to list concepts. It should draw the old handoff surface transforming into executable system objects. |
| `04-reviewable-loop-card.png` | The topic is a loop, but the image reads as horizontal modules. It needs visible return arrows, review packets, replay traces, writeback, failure gates, and human review nodes. |

The HTML sources reveal the issue: fixed artboards, grids, modules, rounded
rectangles, shadows, and consistent CSS classes. Those are useful for drafts,
but they create a webpage-screenshot feel.

## Correct Visual Pipeline Going Forward

The corrected pipeline should be:

1. Use `knowledge-article-visual` for article-level visual routing:
   one total high-density infographic plus four chapter visuals.
2. Use `infographic-onepager` for each visual artifact's format:
   vertical one-page infographic or horizontal teaching card.
3. If the user says `图`, `出图`, `图片`, `图片模型`, `知识卡`, `一图流`, or
   `章节配图`, do not silently stop at H5.
4. Produce standalone visual assets first. H5 embedding is optional and later.
5. For dense Chinese text, use one of two honest modes:
   - deterministic SVG/HTML/PPT-style text overlay when exact Chinese is
     critical;
   - hybrid image-model background/illustration plus deterministic Chinese text
     overlay when image-model aesthetics are required.
6. Inspect final PNG/SVG for nonblank render, Chinese readability, visual
   hierarchy, no overlap, and reference-style match.

Important: if using a pure image model, Chinese text may break. For final
reader-facing diagrams with dense Chinese, the likely best path is hybrid:
generate or draw the visual illustration layer, then overlay exact Chinese text
deterministically.

## Skill Corrections Made Outside This Repo

The user asked why `knowledge-article-visual` did not route correctly and
whether `infographic-onepager` was the right skill. The skills were inspected
and semantically edited outside this repository.

Changed files:

- `/home/yan/.codex/skills/knowledge-article-visual/SKILL.md`
- `/home/yan/.codex/skills/knowledge-article-visual/references/one_page_infographic_template.md`
- `/home/yan/.codex/skills/knowledge-article-visual/evaluation.md`
- `/home/yan/.codex/skills/infographic-onepager/SKILL.md`
- `/home/yan/.codex/skills/infographic-onepager/evaluation.md`

Correction summary:

- `knowledge-article-visual` now has explicit intent routing.
- Requests for `图`, `出图`, `生图`, `图片`, `一图流`, `知识卡`, and
  `章节配图` must not stop at H5 text edits.
- `knowledge-article-visual` must call `infographic-onepager` for the
  per-image format decision.
- Added output modes:
  - direct image generation;
  - deterministic layout image mode;
  - hybrid image model plus exact text overlay.
- Removed the Account Wiki hard-coded template drift from generic one-page
  infographic flow.
- Added evaluation evidence files for before/after behavior.

Boundary:

- These skill edits are global under `/home/yan/.codex/skills`, not committed in
  this repository.
- The current repo contains evidence and outputs, not the global skill history.

## Office-Hours Diagnosis Preserved

The `$office-hours` framing was used to re-check drift:

- Demand reality: the user wants actual high-density visual assets for a
  decision article, not prettier H5 sections.
- Status quo workaround: the agent kept switching among H5, knowledge cards,
  and infographic skills without enforcing image-output intent.
- Narrow wedge: fix one article visual package first: one total infographic plus
  four chapter visuals.
- Desperate specificity: the reader needs to see what the industry is arguing
  about, where the company sits, how the operating system changes, what Agent
  adds, and what each role should do next.
- Observation: deterministic HTML solved Chinese rendering but missed the
  user's image-model / infographic quality expectation.
- Future-fit: the reusable workflow should route external source collection,
  article structure, and visual generation without losing the output form.

## Artifact Chain

Main source and report files:

- `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`
- `wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md`
- `wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md`
- `wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md`
- `wiki/reports/agentic-product-engineering-collaboration-management-report.md`
- `wiki/reports/agentic-product-engineering-collaboration-newspaper.html`
- `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`

Reference visuals:

- `wiki/reports/assets/account-wiki-onepager.png`
- `wiki/reports/assets/account-wiki-runtime-card.png`
- `wiki/reports/assets/account-wiki-validation-card.png`

Current partial visual assets:

- `wiki/reports/agentic-visual-assets/index.html`
- `wiki/reports/agentic-visual-assets/00-total-infographic.html`
- `wiki/reports/agentic-visual-assets/00-total-infographic.png`
- `wiki/reports/agentic-visual-assets/01-industry-debate-card.html`
- `wiki/reports/agentic-visual-assets/01-industry-debate-card.png`
- `wiki/reports/agentic-visual-assets/02-company-dumbbell-card.html`
- `wiki/reports/agentic-visual-assets/02-company-dumbbell-card.png`
- `wiki/reports/agentic-visual-assets/03-operating-system-card.html`
- `wiki/reports/agentic-visual-assets/03-operating-system-card.png`
- `wiki/reports/agentic-visual-assets/04-reviewable-loop-card.html`
- `wiki/reports/agentic-visual-assets/04-reviewable-loop-card.png`

Recent commit chain for this topic:

- `996f4e4 docs: draft agentic product engineering report`
- `8f7d985 docs: broaden agentic collaboration source map`
- `9eefc84 docs: add broad agentic collaboration scan`
- `c252502 docs: add 2026 agentic collaboration timeline`
- `6b95148 docs: add paypal source chain to agentic timeline`
- `47e644d docs: expand agentic org collaboration sources`
- `88c34d2 docs: add agentic collaboration podcast sources`
- `b06dc90 docs: draft agentic collaboration newspaper h5`
- `1540d61 docs: add visual scorecard charts to agentic h5`
- `8308819 docs: refine agentic h5 visual model`
- `add87c0 docs: reframe agent value and role changes`
- `99ef177 docs: apply knowledge article visual structure`
- `0bff8ed docs: add agentic visual card assets`

## Current Git / Worktree Caution

As of this handoff, latest commit observed before the handoff file was:

- `0bff8ed docs: add agentic visual card assets`

Known dirty/untracked items existed before this handoff work and should not be
reverted or bundled into the handoff commit:

- `wiki/ops/account-knowledge-base-structure-explore.md`
- `wiki/ops/agent-harness-article-learning.md`
- `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`
- `wiki/reports/nirvana-phase1-direct-sales-brief.html`
- `wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md`
- `.claude/`, `.idea/`, `.obsidian/`, `.codex/skills/*.zip`, `inbox/`, `mnt/`

Do not clean, restore, or commit those unless the user explicitly asks.

## Next Action After Compaction

Recommended next step:

1. Re-open this handoff note first.
2. Re-open the three reference images in `wiki/reports/assets/`.
3. Decide the next visual-production mode explicitly:
   - image model;
   - deterministic SVG/HTML image;
   - hybrid image model plus exact Chinese text overlay.
4. Rebuild the five visuals in the reference grammar:
   - total high-density infographic;
   - industry debate visual;
   - company dumbbell comparison visual;
   - operating-system shift visual;
   - reviewable Agent loop visual.
5. Inspect PNG outputs, then update the gate review.
6. Only after the visuals are accepted, decide whether to embed them into the H5.

Do not jump straight to Feishu sync, H5 polish, or article expansion before the
visual route is corrected.

Suggested visual requirements for the next version:

- Each visual must have one primary metaphor:
  - industry debate: dispute compass / debate arena / tension map;
  - company position: dumbbell with concrete execution and governance objects;
  - operating system: old handoff surface becoming system objects;
  - reviewable loop: agent queue plus review packet plus writeback loop;
  - total infographic: one chaptered long poster, not a text table.
- Each module should start from an object or action, then add short text.
- Keep module copy to one short title, one claim, and two or three keywords.
- Put long explanations in the MD article, not inside the image.
- Use the reference grammar: paper texture, thick black marker outline,
  hand-drawn title, colored smear highlights, numbered badges, doodle arrows,
  star marks, and a bottom takeaway banner.
- Thumbnail test: the structure should be understandable before zooming in.
- Zoom test: the details should be readable without overlapping text.

## Do Not Do

- Do not claim the current visual assets are good enough because they are PNGs.
- Do not call the source pool exhaustive "全网".
- Do not use the podcast/video pool for hard quotes without transcript capture.
- Do not present the dumbbell model as a proven industry conclusion.
- Do not imply Agent creates the middle layer from nothing.
- Do not publish or mark review-ready while the gate review remains `INVALID`.
- Do not silently choose H5 when the user asks for images.

## Open Questions

- Should the next visual version use a pure image model, or hybrid generation
  with deterministic Chinese text overlay?
- Should the reference style be copied closely as hand-drawn sketchnote, or used
  as density/structure reference while changing the theme for this article?
- Should the H5 be repaired after the images pass, or should the deliverable be
  a standalone image set first?
- Which source claims should be promoted into final public citations after
  transcript capture?
