---
title: agentic-company-playbook / quality failure root cause explore
canonical_object: agentic-product-engineering-collaboration
artifact_type: explore_trace
status: exploring
source_path: chat://openspec-explore/agentic-company-playbook-quality-failure/2026-05-11
updated: 2026-05-11
---

# Agentic Company Playbook Quality Failure Root Cause Explore

## Trigger

The user invoked `$report-wiki-portfolio:openspec-explore` after rejecting the
company playbook draft multiple times and asked whether the root cause was a
skill problem or something else.

## Boundary

This trace is exploratory only. Do not continue editing the HTML report inside
this explore step. The goal is to identify failure causes and repair direction.

## Initial Failure Shape

- The page mixed company evidence, local operating advice, and visual prompt
  scaffolding into one reader-facing artifact.
- The company sections compressed evidence into table cells, so the researched
  facts were not felt as article content.
- Visual styling used colored panels and H5-like layout despite the user asking
  for image-model / Hybrid final visuals.
- The gate review labeled the draft invalid but implementation still continued
  as if a draft with partial gates was acceptable.

## Working Hypothesis

The failure was not caused by a single broken skill. It was caused by incorrect
skill use and missing re-anchor:

- `public-report-quality-gate` had the right hard rules but was applied after
  drafting instead of as a real blocker before drafting.
- `knowledge-article-visual` correctly warns not to replace image-model /
  Hybrid output with H5/SVG, but its sketchnote style cues were misapplied to
  the HTML report shell.
- `openspec-explore` was used to explore direction, but the implementation did
  not preserve the user's later correction that the page should be about company
  collaboration status, not generic "what we do".

## Investigation To Continue

- Compare the skills' stated rules with actual behavior in the rejected drafts.
- Identify whether any skill wording invited the bad output.
- Separate skill deficiency from agent execution failure.
- Decide whether a repo-visible behavior replay or skill update is warranted.

## Findings

### 1. The main failure is execution discipline, not a broken skill

`public-report-quality-gate` already contains the relevant blockers:

- create the Article Intent Contract before drafting
- map learning and reference use before drafting
- route complex reader-facing drafts to reviewer flow when escalation signals
  are present
- treat voice, paragraph drift, judgment ownership, and visual information
  design as hard gates
- mark the scorecard `INVALID` when gates are partial or failed

The rejected output violated the spirit of those rules even when a gate artifact
existed. The artifact was used as a post-hoc diagnostic wrapper, not as a
pre-draft blocker.

### 2. The visual skills were misapplied to the report shell

`knowledge-article-visual` and `infographic-onepager` correctly say that when
the user asks for image model / Hybrid, the agent must not silently replace that
with H5/SVG. They also describe sketchnote visual styles with pastel accents.

The bad behavior came from applying visual-asset style cues to the HTML report
page itself. The requested final visual was supposed to be a separate
image-model/Hybrid artifact. The HTML report should have stayed evidence-led and
reader-facing, not become a pseudo-infographic with colored company panels and a
visual prompt block.

### 3. The live correction was not re-anchored hard enough

The user corrected the goal from:

- "现有公司的人该怎么做 / 我们应该怎么做"

to:

- "我要的是这几家公司的协作现状"
- "四个样本，各自代表一种协作模式"
- "每个公司都应该展开"
- "裁员、招聘岗位、JD 要求都要作为组织协作判断点"
- "所有论据都要有数据支撑"

That correction should have invalidated the old "role actions / 30-day loop /
local operating loop" frame immediately. Instead, the implementation kept trying
to preserve a local-reading section and then compressed company evidence into
small table cells.

### 4. The gate review itself became too generous

The gate review marked the draft `INVALID`, which was correct. But its paragraph
review still over-scored weak sections and used language such as "Retain for
draft" for sections that the user later identified as the core problem. That
made the artifact look like a controlled draft rather than a failed draft that
needed structural replacement.

### 5. Search evidence was gathered but not converted into article substance

Evidence existed:

- OpenAI: Harness Engineering, Symphony, Codex Careers, Core Agents JD
- Anthropic: Claude Code internal use cases, PM / design role signals
- Stripe: ACP, Shared Payment Token, Instant Checkout, Agentic Commerce roles
- Block: 95% AI usage, 50 Champions, automated PR growth, 0 current jobs page,
  layoff reporting

The page used these mostly as labels or table bullets. That is why the user saw
"只有一个标题其余的没了": the information existed technically, but it was not
written as readable company analysis.

## Root Cause

The root cause is a multi-step process failure:

1. **Mode conflation**: report page, visual asset plan, and local playbook were
   mixed into one artifact.
2. **Gate non-enforcement**: `public-report-quality-gate` was loaded but not used
   as a stop mechanism before drafting.
3. **Re-anchor failure**: the user's correction from "how we do it" to "company
   collaboration status" did not fully replace the previous frame.
4. **Evidence compression**: researched evidence was compressed into labels and
   small cards instead of expanded into company-by-company analysis.
5. **Visual misrouting**: image-model/Hybrid requirements were represented as
   prose and H5 styling instead of a separate visual production path.

## Skill Assessment

| Skill | Problem caused by skill? | Assessment |
|---|---:|---|
| `openspec-explore` | No | It explicitly says explore is thinking, not implementation. The implementation happened after proceed signals, not because explore instructed it. |
| `public-report-quality-gate` | No, but enforcement failed | The skill had the right rules. The failure was treating an `INVALID` gate as acceptable draft bookkeeping rather than a stop/re-plan condition. |
| `knowledge-article-visual` | Partly misapplied | The skill's visual style suggestions are for visual assets. They should not have governed the HTML article palette. |
| `infographic-onepager` | Partly misapplied | It says to produce poster scripts/assets and respect output mode. It did not require inserting prompt/script prose into the report. |
| `office-hours` | Process noise in this context | The user invoked it, but after a quality complaint the right use was root-cause framing, not A/B option forcing. |

## Repair Direction

Before editing the page again, the next implementation should use this stricter
contract:

- No `local reading`, no `我们怎么做`, no visual prompt block in the report body.
- Neutral newspaper palette for the HTML shell; no sketchnote pastel company
  panels.
- Each company gets article prose, not only table cells:
  - current path
  - public evidence
  - hiring/JD signal
  - org collaboration interpretation
  - risk boundary
- The final image-model/Hybrid visual is a separate artifact after the article
  is content-correct.
- Gate review should mark the old version as failed, not "partial but retained",
  when the user has already rejected the frame.

## Open Question

No skill edit is clearly required yet. A repo behavior replay may be useful if
this repeats: "when user rejects a report frame as generic, public-report gate
must force structural re-plan before further HTML edits."

## 2026-05-11 Continuation: Visual Constraint Placement

The user asked to add a constraint after a fresh failure: an HTML report named in
the request was edited directly even though the user asked for `一图流` and
`章节知识卡`, then asked why the route did not use the image model.

### Constraint Candidate

The missing runtime constraint is not "always use image model." The stricter
constraint should be:

- If the request contains visual-deliverable words such as `一图流`, `知识卡`,
  `章节配图`, `图片`, `生图`, `跑图`, or `图片模型`, do not treat an `.html`
  target path as permission to satisfy the request by adding H5 sections.
- First classify the output mode:
  - standalone image-model asset
  - hybrid image-model background plus deterministic Chinese overlay
  - deterministic SVG/HTML renderer with exported image asset
  - H5/HTML page section
- If the user already complained that prior output was H5/SVG-like, default to
  image-model or hybrid mode unless they explicitly re-choose H5/SVG.
- HTML edits may happen only after the standalone visual route is accepted, or
  when the user explicitly says the desired output is an in-page H5/HTML module.

### Does Behavior Replay Gate Apply?

Yes, if this becomes a real repository or skill constraint.

Reason: the proposed wording changes future runtime behavior. It says a future
agent should stop, route, or refuse a direct HTML edit when the input shape is
visual-deliverable wording plus an HTML target. That is exactly the behavior
class covered by `behavior-replay-gate`: future trigger / route / stop behavior.

The minimum replay evidence should include:

| Field | Evidence Needed |
|---|---|
| input / situation shape | User names an existing `.html` report and asks to add `一图流` / `章节知识卡`. |
| trigger condition | Visual-deliverable wording is present, or user has rejected H5/SVG-like output. |
| expected route / stop | Stop direct HTML editing; route to visual package script and image-model/hybrid mode decision first. |
| repo-visible artifact | The skill or repo guidance file that contains the new rule, plus this explore trace. |
| expected output / non-output | Output visual script / asset plan first; do not output only new H5 sections. |
| promotion boundary | This does not mean every report edit requires image generation; ordinary text/H5 edits remain allowed when visual wording is absent. |
| residual risk / proof boundary | Local replay proves the route decision, not image quality or multi-session rollout reliability. |

### Implementation Boundary

Because this would change normal repository behavior, it should not be patched
directly during explore. The implementation route should be an OpenSpec change
that updates the relevant skill / gate text and includes behavior replay
evidence. The likely affected assets are:

- `.codex/skills/public-report-quality-gate/SKILL.md`
- `knowledge-article-visual` route wording if it is the active visual package
  owner
- `infographic-onepager` output-mode fork wording if the ambiguity remains
- a pressure scenario covering "existing H5/article + 一图流/知识卡"
