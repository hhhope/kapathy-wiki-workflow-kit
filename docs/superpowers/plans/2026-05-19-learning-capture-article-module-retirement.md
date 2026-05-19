# Learning Capture Article Module Retirement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `learning-capture` the only active learning runtime entry, retire the `article-learning-capture` skill surface, preserve useful article-specific rules as references, and make durable learning output Chinese-first by default.

**Architecture:** Create a new OpenSpec change first, then migrate article workflow content into `learning-capture` references. Remove the active `article-learning-capture/SKILL.md` trigger surface and verify with behavior-asset checks plus direct `rg` routing checks.

**Tech Stack:** Markdown behavior assets, OpenSpec change artifacts, repo-local Codex skills, `rg`, `openspec validate`, Python repository checkers.

---

## File Structure

Create:

- `openspec/changes/retire-article-learning-skill-surface/proposal.md` - user-facing OpenSpec motivation, scope, and non-goals.
- `openspec/changes/retire-article-learning-skill-surface/design.md` - detailed routing, migration, language-policy, and evidence design.
- `openspec/changes/retire-article-learning-skill-surface/tasks.md` - authoritative task checklist for implementation.
- `openspec/changes/retire-article-learning-skill-surface/evaluation.md` - RED/GREEN evidence, pressure scenarios, prior-art scan, and verification results.
- `openspec/changes/retire-article-learning-skill-surface/specs/learning-capture-runtime/spec.md` - delta requirements for single-entry learning routing and Chinese-first durable learning output.
- `.codex/skills/learning-capture/references/article-sop.md` - article-specific workflow steps migrated from the retired article skill.
- `.codex/skills/learning-capture/references/article-scorecard.md` - article scorecard and thresholds migrated from the retired article skill.
- `.codex/skills/learning-capture/references/article-wiki-template.md` - Chinese-first durable article learning template.
- `.codex/skills/learning-capture/references/article-pressure-scenarios.md` - pressure scenarios for article learning within the `learning-capture` router.

Modify:

- `.codex/skills/learning-capture/SKILL.md` - add Chinese-first durable learning output rule and point article workflow to references.
- `.codex/skills/learning-capture/references/article.md` - replace delegation to `article-learning-capture` with self-contained article module routing.
- `.codex/skills/learning-capture/references/pressure-scenarios.md` - add routing pressure cases proving article requests enter through `learning-capture`.

Delete:

- `.codex/skills/article-learning-capture/SKILL.md` - removes the active trigger description.
- `.codex/skills/article-learning-capture/references/pressure-scenarios.md` - migrated into `learning-capture` references.
- `.codex/skills/article-learning-capture/references/scorecard.md` - migrated into `learning-capture` references.
- `.codex/skills/article-learning-capture/references/sop.md` - migrated into `learning-capture` references.
- `.codex/skills/article-learning-capture/references/wiki-template.md` - migrated into `learning-capture` references.

Do not modify unrelated dirty files already present in the worktree.

## Task 1: Create OpenSpec Change and RED Baseline

**Files:**

- Create: `openspec/changes/retire-article-learning-skill-surface/proposal.md`
- Create: `openspec/changes/retire-article-learning-skill-surface/design.md`
- Create: `openspec/changes/retire-article-learning-skill-surface/tasks.md`
- Create: `openspec/changes/retire-article-learning-skill-surface/evaluation.md`
- Create: `openspec/changes/retire-article-learning-skill-surface/specs/learning-capture-runtime/spec.md`

- [ ] **Step 1: Confirm git truth before creating OpenSpec files**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: unrelated dirty files may remain; no files under `openspec/changes/retire-article-learning-skill-surface/` exist yet.

- [ ] **Step 2: Run RED baseline commands**

Run:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md .codex/skills/learning-capture/references/article.md .codex/skills/article-learning-capture/references/wiki-template.md
rg -n '^# <Topic> / Reading Notes|## Source|## Reading Draft|### Problem|### Structured Translation Notes' .codex/skills/article-learning-capture/references/wiki-template.md
```

Expected: first command returns hits in `.codex/skills/article-learning-capture/SKILL.md` and the `learning-capture` article reference delegation; second command returns English headings from the current article wiki template.

- [ ] **Step 3: Create OpenSpec proposal**

Create `openspec/changes/retire-article-learning-skill-surface/proposal.md`:

```markdown
# Retire Article Learning Skill Surface

## Why

`learning-capture` is the intended runtime router for learning requests, but
`.codex/skills/article-learning-capture/SKILL.md` still exposes a directly
triggerable description for article, WeChat, deep-reading, and learning
extraction requests. That creates two runtime entry signals for the same
learning workflow.

Durable learning templates also set `language: zh-CN` while retaining English
reading-note headings, which can still steer wiki learning output toward
English.

## What Changes

- Make `learning-capture` the only active learning runtime skill.
- Migrate useful article-specific workflow rules into `learning-capture`
  references.
- Remove the active `article-learning-capture` skill trigger surface.
- Make durable wiki learning notes Chinese-first by default.
- Preserve English-first authoring for behavior assets such as `SKILL.md`.

## Out Of Scope

- Reprocessing historical wiki learning notes.
- Changing external source fetching behavior.
- Changing README/repo or example learning semantics except where routing
  pressure scenarios prove they are not captured by the article module.
- Promoting article takeaways into `AGENTS.md`, specs, or hard skill rules
  without evidence.
```

- [ ] **Step 4: Create OpenSpec design**

Create `openspec/changes/retire-article-learning-skill-surface/design.md` with these sections:

```markdown
# Design

## Runtime Routing

`learning-capture` is the only active runtime skill for learning requests. It
classifies whether the input is learning material, then routes by evidence
object to article, repo/README, example/reference, or mixed-source references.

`article-learning-capture` is retired as a skill surface. Article workflow
content may survive only as `learning-capture` reference material or historical
archive context.

## Article Rule Migration

The implementation classifies old article-skill content before migration:

- Keep article-only source metadata, source class, source grounding,
  score-first triage, copyright boundary, structured translation notes,
  transferable learning, rejected moves, and promotion boundaries.
- Deduplicate general learning routing and promotion rules already owned by
  `learning-capture` and repo governance.
- Delete old skill description wording, compatibility-entry wording, and
  trigger-oriented `When To Use` text.

## Chinese-First Durable Learning Output

Durable internal learning artifacts in `wiki/sources` and `wiki/ops` default to
Chinese. English remains valid when the user asks for English, the target
artifact is English-first, or the audience requires English.

## Evidence

The change records RED baseline, prior-art/common-rule dedupe, GREEN result,
pressure scenarios, behavior replay, OpenSpec validation, and behavior-asset
checker output in `evaluation.md`.
```

- [ ] **Step 5: Create OpenSpec tasks**

Create `openspec/changes/retire-article-learning-skill-surface/tasks.md`:

```markdown
## 1. OpenSpec Baseline

- [ ] 1.1 Record RED baseline for active article skill description pollution.
- [ ] 1.2 Record RED baseline for English article wiki template body prompts.
- [ ] 1.3 Record prior-art and common-rule ownership scan.

## 2. Skill Surface Retirement

- [ ] 2.1 Add Chinese-first durable learning output rule to `learning-capture`.
- [ ] 2.2 Migrate useful article-specific rules into `learning-capture`
  references.
- [ ] 2.3 Remove the active `article-learning-capture` skill surface.
- [ ] 2.4 Remove or rewrite references that imply `article-learning-capture`
  remains a runtime entry.

## 3. Evidence and Verification

- [ ] 3.1 Add pressure scenarios for article, WeChat, README/repo, example, and
  English-target learning requests.
- [ ] 3.2 Add behavior replay evidence for future routing.
- [ ] 3.3 Run `openspec validate retire-article-learning-skill-surface --strict`.
- [ ] 3.4 Run `python3 scripts/check_behavior_assets.py` and preserve output.
- [ ] 3.5 Run `python3 scripts/check_wiki_frontmatter.py` if template or
  frontmatter changes require it.
- [ ] 3.6 Commit only task-related files.
```

- [ ] **Step 6: Create OpenSpec delta spec**

Create `openspec/changes/retire-article-learning-skill-surface/specs/learning-capture-runtime/spec.md`:

```markdown
# learning-capture-runtime Specification

## ADDED Requirements

### Requirement: Single Learning Runtime Entry

Learning requests SHALL route through `learning-capture` as the only active
runtime skill entry.

#### Scenario: Article learning request

- **WHEN** the user provides an article, blog, paper, WeChat post, or article
  collection as learning, reference, reuse, or adaptation material
- **THEN** the agent SHALL load `learning-capture`
- **AND** the agent SHALL use the article reference module from within
  `learning-capture`
- **AND** no active `article-learning-capture` skill description SHALL be
  available as a separate runtime trigger.

#### Scenario: Repo or README learning request

- **WHEN** the user provides a GitHub/GitLab repo or README for reuse learning
- **THEN** the agent SHALL load `learning-capture`
- **AND** the agent SHALL route to the repo/README reference module, not the
  article module.

### Requirement: Chinese-First Durable Learning Output

Durable internal wiki learning artifacts SHALL default to Chinese output while
behavior assets remain English-first.

#### Scenario: Chinese article learning note

- **WHEN** the user provides a Chinese article or WeChat post for durable wiki
  learning
- **THEN** the generated `wiki/sources` or `wiki/ops` learning page SHALL use
  Chinese headings and body prompts by default
- **AND** the page SHALL preserve source metadata, source grounding, scoring,
  transferable learning, and promotion boundaries.

#### Scenario: English-first target artifact

- **WHEN** the learning output is a `SKILL.md`, public English README/doc, or
  external English-facing artifact
- **THEN** English output remains allowed
- **AND** the Chinese-first durable wiki default SHALL NOT override that target
  artifact's language contract.
```

- [ ] **Step 7: Create evaluation baseline**

Create `openspec/changes/retire-article-learning-skill-surface/evaluation.md`:

```markdown
# Evaluation

## RED Baseline

### Active Article Skill Description Pollution

Command:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md .codex/skills/learning-capture/references/article.md .codex/skills/article-learning-capture/references/wiki-template.md
```

Expected baseline: the command returns the active
`.codex/skills/article-learning-capture/SKILL.md` description and delegation
references.

### English Article Template Body

Command:

```bash
rg -n '^# <Topic> / Reading Notes|## Source|## Reading Draft|### Problem|### Structured Translation Notes' .codex/skills/article-learning-capture/references/wiki-template.md
```

Expected baseline: the command returns English headings.

## Prior-Art / Common-Rule Dedupe

| Source | Ownership |
|---|---|
| `AGENTS.md` | Repo workflow gates, OpenSpec boundary, behavior-asset prior-art gate, skill authoring contract |
| `PROJECT.md` | OpenSpec as source of truth and wiki purpose |
| `.codex/skills/learning-capture/SKILL.md` | Learning intent routing and evidence-object module map |
| `wiki/ops/learning-capture-routing.md` | Historical rationale for learning domain router and module references |
| `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md` | English-first behavior asset contract and repo language carve-out |
| `wiki/adr/0026-retire-draft-skills-as-runtime-surface.md` | Runtime surface must not keep misleading draft/duplicate skill signals |
| `openspec/changes/archive/2026-05-06-formalize-article-learning-capture/*` | Historical article-learning source grounding and score-first design |
```

- [ ] **Step 8: Validate the OpenSpec skeleton**

Run:

```bash
openspec validate retire-article-learning-skill-surface --strict
```

Expected: PASS. If validation fails, fix only the new OpenSpec files.

- [ ] **Step 9: Commit OpenSpec baseline**

Run:

```bash
git status --short
git add openspec/changes/retire-article-learning-skill-surface
git commit -m "docs: propose learning capture article retirement"
```

Expected: commit includes only the new OpenSpec change directory.

## Task 2: Migrate Article Workflow Into Learning Capture

**Files:**

- Modify: `.codex/skills/learning-capture/SKILL.md`
- Modify: `.codex/skills/learning-capture/references/article.md`
- Create: `.codex/skills/learning-capture/references/article-sop.md`
- Create: `.codex/skills/learning-capture/references/article-scorecard.md`
- Create: `.codex/skills/learning-capture/references/article-wiki-template.md`
- Create: `.codex/skills/learning-capture/references/article-pressure-scenarios.md`
- Modify: `.codex/skills/learning-capture/references/pressure-scenarios.md`
- Modify: `openspec/changes/retire-article-learning-skill-surface/evaluation.md`

- [ ] **Step 1: Load required skill-authoring references**

Run:

```bash
sed -n '1,220p' ~/.codex/skills/writing-skills/SKILL.md
sed -n '1,220p' ~/.codex/skills/test-driven-development/SKILL.md
```

Expected: both files are readable. Apply their guidance to this semantic skill edit.

- [ ] **Step 2: Update `learning-capture` hard rules**

Modify `.codex/skills/learning-capture/SKILL.md` by adding this hard rule after the output-use hint rule:

```markdown
- Durable internal wiki learning notes default to Chinese output for
  `wiki/sources` and `wiki/ops`; keep behavior assets such as `SKILL.md` and
  English-facing public artifacts English-first unless the user asks otherwise.
```

Modify the `Article, blog, paper, WeChat post, article collection` module row to keep `references/article.md` as the loaded file.

- [ ] **Step 3: Replace article module delegation**

Replace `.codex/skills/learning-capture/references/article.md` with this structure:

```markdown
# Article Module

Use this module for articles, blogs, papers, WeChat posts, newsletters, and
article collections after `learning-capture` has classified the request as
learning material.

## Runtime Boundary

`learning-capture` is the only runtime entry. This module does not delegate to
an `article-learning-capture` skill and must not recreate a second trigger
surface.

## Required Gates

- Preserve original URL, title, publisher or author when available, publication
  date when available, and access date.
- Classify source before scoring: primary source, secondary interpretation,
  structure reference, or low-relevance/general-interest.
- Preserve source grounding before analysis: extracted markdown when permitted,
  source map with bounded excerpts, or retrieval-failure note.
- Score before deep reading.
- Use the article scorecard threshold: 75+ deep-read, 60-74 brief candidate,
  below 60 skip reason.
- Mark retrospective scoring explicitly; it is not score-first admission
  evidence.
- Respect copyright boundaries: no full verbatim copyrighted article text and no
  full verbatim translation.
- Separate article comprehension from local transfer extraction.
- Distinguish source domain/topic from reusable output capability type when
  recording transferable learning.
- Write durable internal wiki learning output in Chinese by default, unless the
  user or target artifact requires English.

## References

- SOP: `article-sop.md`
- Scorecard: `article-scorecard.md`
- Wiki template: `article-wiki-template.md`
- Pressure scenarios: `article-pressure-scenarios.md`
```

- [ ] **Step 4: Create article SOP reference**

Create `.codex/skills/learning-capture/references/article-sop.md` by migrating useful workflow content from `.codex/skills/article-learning-capture/references/sop.md`.

The new file must include these headings:

```markdown
# Article Learning SOP

## 1. Source Intake

## 2. Admission and Score

## 3. Reading Draft

## 4. Transferable Learning

## 5. Promotion Boundary

## 6. Output Language
```

In `## 6. Output Language`, include:

```markdown
Durable internal wiki learning notes default to Chinese. Use English only when
the user asks for English, the target artifact is English-first, or the audience
requires English.
```

- [ ] **Step 5: Create article scorecard reference**

Create `.codex/skills/learning-capture/references/article-scorecard.md` by migrating useful scorecard content from `.codex/skills/article-learning-capture/references/scorecard.md`.

The file must preserve this threshold text:

```markdown
## Decision Thresholds

- 75-100: deep-read and write durable wiki learning notes.
- 60-74: brief-read and keep a candidate note.
- Below 60: record source and skip reason.
```

- [ ] **Step 6: Create Chinese-first article wiki template**

Create `.codex/skills/learning-capture/references/article-wiki-template.md` with Chinese headings and prompts. Use four-backtick fences around the embedded wiki template so the outer reference remains readable:

````markdown
# Article Learning Wiki Template

Use this template for durable internal article-learning pages. The default body
language is Chinese unless the user or target artifact requires English.

```markdown
---
title: <canonical-object> / reading-notes
type: learning
canonical_object: <canonical-object>
artifact_type: reading-notes
language: zh-CN
audience: self
knowledge_level: working
layer: ops
domain: <real-topic-domain-or-none>
ops_area: learning-capture
classification_needed: true
status: active
confidence: candidate
updated_at: YYYY-MM-DD
ai_generated: true
derived_from:
  - <original-url>
related_objects:
  - <related-object>
notes_scope: Source-grounded article learning. This page records reading notes,
  scoring, transferable learning, and promotion boundaries; it does not directly
  create AGENTS, skill, spec, or policy changes.
---

# <主题> / 阅读笔记

## 来源

## 原文依据

## 准入判断

## 评分

## 阅读草稿

### 问题

### 方法 / 架构 / 流程

### 证据类型

### 结构化翻译笔记

### 适用条件

### 不能证明什么

## 可迁移学习

## 拒绝动作

## 下一步
```
````

- [ ] **Step 7: Create article pressure scenarios**

Create `.codex/skills/learning-capture/references/article-pressure-scenarios.md`:

```markdown
# Article Module Pressure Scenarios

| Scenario | Expected behavior |
|---|---|
| User provides a Chinese WeChat article and says "学一下，落 wiki" | Load `learning-capture`, route to article module, produce Chinese durable learning notes |
| User says "article learning 这套复用一下" | Load `learning-capture`, not a separate `article-learning-capture` skill |
| User provides a GitHub README for reuse | Load `learning-capture`, route to repo/README module |
| User provides an output-shape example | Load `learning-capture`, route to example/reference module |
| User asks for an English public README update | Keep the target artifact English-first |
```

- [ ] **Step 8: Update shared learning pressure scenarios**

Append the same five pressure scenarios to `.codex/skills/learning-capture/references/pressure-scenarios.md` under a new heading:

```markdown
## Article Surface Retirement
```

- [ ] **Step 9: Record migration evidence**

Append to `openspec/changes/retire-article-learning-skill-surface/evaluation.md`:

```markdown
## Migration Classification

| Old content | Result | Reason |
|---|---|---|
| Article metadata and source grounding | Keep | Article-specific audit value |
| Score-first thresholds | Keep | Article-specific admission value |
| Copyright boundary | Keep | Article-specific source handling |
| Structured translation notes | Keep | Article-specific reading value |
| Transferable learning and rejected moves | Keep | Article-specific local transfer value |
| General learning intent routing | Deduplicate | Owned by `learning-capture` |
| Promotion into behavior assets | Reference only | Owned by repo governance and behavior-asset gates |
| Old `description` and `When To Use` entry wording | Delete | It recreates runtime trigger pollution |
```

- [ ] **Step 10: Run focused checks before commit**

Run:

```bash
rg -n 'article-learning-capture|Delegate|compatibility entry|Use when the user provides external articles' .codex/skills/learning-capture
```

Expected: no matches for `Delegate`, `compatibility entry`, or the old direct-trigger phrase. Matches for `article-learning-capture` are allowed only if they explicitly describe the retired surface in pressure/evidence text.

- [ ] **Step 11: Commit learning-capture migration**

Run:

```bash
git status --short
git add .codex/skills/learning-capture openspec/changes/retire-article-learning-skill-surface/evaluation.md
git commit -m "docs: migrate article learning into learning capture"
```

Expected: commit includes only `learning-capture` reference changes and evaluation evidence.

## Task 3: Remove Active Article Skill Surface

**Files:**

- Delete: `.codex/skills/article-learning-capture/SKILL.md`
- Delete: `.codex/skills/article-learning-capture/references/pressure-scenarios.md`
- Delete: `.codex/skills/article-learning-capture/references/scorecard.md`
- Delete: `.codex/skills/article-learning-capture/references/sop.md`
- Delete: `.codex/skills/article-learning-capture/references/wiki-template.md`
- Modify: `openspec/changes/retire-article-learning-skill-surface/evaluation.md`

- [ ] **Step 1: Remove the retired skill directory files**

Delete the five files under `.codex/skills/article-learning-capture/`. Use `apply_patch` delete hunks or an explicitly reviewed `git rm` command.

Expected deleted paths:

```text
.codex/skills/article-learning-capture/SKILL.md
.codex/skills/article-learning-capture/references/pressure-scenarios.md
.codex/skills/article-learning-capture/references/scorecard.md
.codex/skills/article-learning-capture/references/sop.md
.codex/skills/article-learning-capture/references/wiki-template.md
```

- [ ] **Step 2: Verify no active skill surface remains**

Run:

```bash
find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'article-learning-capture|learning-capture'
```

Expected: output includes `.codex/skills/learning-capture/SKILL.md` and does not include `.codex/skills/article-learning-capture/SKILL.md`.

- [ ] **Step 3: Verify active descriptions are clean**

Run:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md
```

Expected: no active `article-learning-capture` skill description. Any remaining `learning-capture` description should describe the domain router, not a separate article skill.

- [ ] **Step 4: Record GREEN routing result**

Append to `openspec/changes/retire-article-learning-skill-surface/evaluation.md`:

```markdown
## GREEN Result

### Active Skill Surface

Command:

```bash
find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'article-learning-capture|learning-capture'
```

Expected result: only `.codex/skills/learning-capture/SKILL.md` appears for
learning capture.

### Active Description Scan

Command:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md
```

Expected result: no active `article-learning-capture` description remains.
```

- [ ] **Step 5: Commit retired skill surface deletion**

Run:

```bash
git status --short
git add .codex/skills/article-learning-capture openspec/changes/retire-article-learning-skill-surface/evaluation.md
git commit -m "docs: retire article learning skill surface"
```

Expected: commit records deletion of the retired skill files and evaluation update.

## Task 4: Final Evidence, Validation, and OpenSpec Task Closure

**Files:**

- Modify: `openspec/changes/retire-article-learning-skill-surface/evaluation.md`
- Modify: `openspec/changes/retire-article-learning-skill-surface/tasks.md`

- [ ] **Step 1: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: PASS, or a known pre-existing non-zero result preserved verbatim in `evaluation.md` with a note that it is unrelated to this change.

- [ ] **Step 2: Run frontmatter checker because the article wiki template changed**

Run:

```bash
python3 scripts/check_wiki_frontmatter.py
```

Expected: PASS, or a known pre-existing non-zero result preserved verbatim in `evaluation.md` with a note that no actual wiki page frontmatter was changed by this task.

- [ ] **Step 3: Run OpenSpec validation**

Run:

```bash
openspec validate retire-article-learning-skill-surface --strict
```

Expected: PASS.

- [ ] **Step 4: Run final routing scans**

Run:

```bash
rg -n 'article-learning-capture' .codex/skills AGENTS.md PROJECT.md openspec/specs openspec/changes/retire-article-learning-skill-surface wiki/adr wiki/ops
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)' .codex/skills/*/SKILL.md
rg -n 'language: zh-CN|# <主题> / 阅读笔记|## 来源|## 阅读草稿|## 可迁移学习' .codex/skills/learning-capture/references/article-wiki-template.md
```

Expected:

- `article-learning-capture` appears only in historical/evaluation/archive context or in the current OpenSpec change as a retired surface.
- Active skill descriptions do not advertise a separate article-learning entry.
- The article wiki template contains `language: zh-CN` and Chinese body headings.

- [ ] **Step 5: Append final verification evidence**

Append a final verification table to `openspec/changes/retire-article-learning-skill-surface/evaluation.md`. Build the `Result` cells from the actual command output observed in Steps 1-4:

```markdown
## Final Verification

| Check | Command | Result |
|---|---|---|
| Behavior asset checker | `python3 scripts/check_behavior_assets.py` | PASS or recorded unrelated blocker summary from this run |
| Wiki frontmatter checker | `python3 scripts/check_wiki_frontmatter.py` | PASS or recorded unrelated blocker summary from this run |
| OpenSpec validation | `openspec validate retire-article-learning-skill-surface --strict` | PASS |
| Active skill surface scan | `find .codex/skills -maxdepth 2 -name SKILL.md \| sort \| rg 'article-learning-capture\|learning-capture'` | Only `learning-capture` remains |
| Chinese template scan | `rg -n 'language: zh-CN\|# <主题> / 阅读笔记\|## 来源' .codex/skills/learning-capture/references/article-wiki-template.md` | PASS |
```

- [ ] **Step 6: Mark OpenSpec tasks complete only after evidence exists**

Update `openspec/changes/retire-article-learning-skill-surface/tasks.md` by changing completed items from `- [ ]` to `- [x]`. Do not mark a task complete if its evidence is missing from `evaluation.md`.

- [ ] **Step 7: Commit final evidence**

Run:

```bash
git status --short
git add openspec/changes/retire-article-learning-skill-surface/evaluation.md openspec/changes/retire-article-learning-skill-surface/tasks.md
git commit -m "docs: verify learning capture article retirement"
```

Expected: commit includes only OpenSpec task/evaluation closure.

## Task 5: Final Git Review and Stop Condition

**Files:**

- No file edits unless verification reveals a task-related blocker.

- [ ] **Step 1: Review task-related commit history**

Run:

```bash
git log --oneline -5
```

Expected: recent commits include the design spec and the implementation commits for this change.

- [ ] **Step 2: Review final worktree state**

Run:

```bash
git status --short
```

Expected: unrelated pre-existing dirty files may remain. There should be no unstaged or untracked files from `retire-article-learning-skill-surface` implementation.

- [ ] **Step 3: Stop after OpenSpec tasks are complete**

Expected behavior: do not archive the change automatically. Per repo hard stop, completion means default next action is archive review, not immediate archive.

## Self-Review Checklist

- Spec coverage: Tasks cover single-entry routing, article content migration, Chinese-first durable learning output, OpenSpec evidence, behavior replay, and verification.
- Placeholder scan: The plan was searched for writing-plans red-flag tokens. Angle-bracket text appears only inside template examples that are intentionally copied into wiki templates.
- Type/path consistency: All paths use `retire-article-learning-skill-surface` for OpenSpec and `.codex/skills/learning-capture/references/article-*` for migrated article module content.
