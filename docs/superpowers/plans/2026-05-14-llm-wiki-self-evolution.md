# LLM-WIKI Self-Evolution Medical Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Formalize the LLM-WIKI medical-loop model as a repo-scoped OpenSpec and wiki ops record without adding write automation.

**Architecture:** Implement only the first scoped change from the design: `formalize-llm-wiki-medical-loop`. The change creates OpenSpec artifacts and one wiki ops model record that define lifecycle vocabulary, artifact boundaries, and escalation rules while explicitly deferring review-decision, treatment, surgery, and recovery execution workflows.

**Tech Stack:** Markdown, OpenSpec CLI, repo-local wiki ops records, existing behavior-replay governance.

---

## Scope Check

The design identifies five future OpenSpec changes:

1. `formalize-llm-wiki-medical-loop`
2. `add-wiki-review-decisions`
3. `add-wiki-treatment-workflow`
4. `add-wiki-surgery-workflow`
5. `add-wiki-recovery-records`

This plan implements only item 1. Items 2-5 are intentionally out of scope
because they define separate workflows and, later, possible execution capability.

## File Structure

- Create: `openspec/changes/formalize-llm-wiki-medical-loop/proposal.md`
  - Owns problem statement, scope, non-goals, and success criteria.
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/design.md`
  - Owns architecture, lifecycle vocabulary, artifact placement, and boundaries.
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`
  - Owns implementation checklist for the OpenSpec change.
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/specs/llm-wiki-medical-loop/spec.md`
  - Owns formal `SHALL` requirements for the lifecycle model.
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/evaluation.md`
  - Owns validation evidence, behavior replay, prior-art dedupe, and residual risk.
- Create: `wiki/ops/llm-wiki-self-evolution-medical-loop.md`
  - Owns the human-readable repo ops record for the model.

## Out Of Scope

- No `wiki-surgery`, `wiki-treat`, `wiki-checkup`, or `wiki-recovery` skill.
- No changes to `.codex/skills/*`.
- No frontmatter, taxonomy, relation, MOC, ADR, AGENTS, or OpenSpec archive mutation.
- No application of current doctor findings.
- No new scripts or CLI flags.

## Task 1: Create OpenSpec Skeleton

**Files:**
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/proposal.md`
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/design.md`
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`

- [ ] **Step 1: Write the proposal**

Create `openspec/changes/formalize-llm-wiki-medical-loop/proposal.md`:

```markdown
# Proposal: formalize LLM-WIKI medical loop

## Summary

Formalize the LLM-WIKI self-evolution lifecycle as a medical loop:

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

The change defines vocabulary, artifact expectations, and escalation boundaries.
It does not add write automation.

## Problem

The repository now has diagnostic capability through `wiki-doctor` review
records, but the broader self-evolution process is still implicit in chat and
design notes. Without a formal lifecycle, later agents may confuse diagnosis,
human confirmation, repair, verification, and archive as interchangeable steps.

The repository needs a stable model that explains how LLM-assisted wiki
evolution moves from health signals to durable memory while preserving OpenSpec,
human review, and proof boundaries.

## Scope

In scope:

- Define the medical-loop lifecycle vocabulary.
- Define required artifact classes for each lifecycle stage.
- Define treatment versus surgery escalation rules.
- Define proof, approval, write, and archive boundaries.
- Add a repo-visible wiki ops model record.
- Add behavior replay evidence for future routing expectations.

Out of scope:

- New skills or commands.
- Automated treatment or surgery.
- Applying frontmatter, taxonomy, relation, MOC, ADR, AGENTS, or OpenSpec state
  changes.
- Implementing review-decision, treatment, surgery, or recovery workflows.
- Archiving this change.

## Success Criteria

- OpenSpec validation passes for `formalize-llm-wiki-medical-loop`.
- A wiki ops record explains the model for future agents.
- Requirements explicitly preserve `doctor` as diagnosis-only.
- Requirements explicitly state that treatment and surgery require later scoped
  approval before writes.
- Evaluation records behavior replay, prior-art dedupe, validation commands, and
  residual risk.
```

- [ ] **Step 2: Write the design**

Create `openspec/changes/formalize-llm-wiki-medical-loop/design.md`:

```markdown
# Design: LLM-WIKI medical loop

## Source Design

This change formalizes the accepted design in:

- `docs/superpowers/specs/2026-05-14-llm-wiki-self-evolution-design.md`

## Lifecycle

The repository uses this vocabulary for LLM-WIKI self-evolution:

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

- `checkup`: health snapshots and dry-run checks.
- `doctor`: diagnosis records only.
- `review`: human confirmation of diagnosis.
- `treatment`: low-risk, narrow, explicitly confirmed fixes.
- `surgery`: large, structural, or governance-sensitive repair.
- `recovery`: post-repair verification with fresh evidence.
- `archive`: durable case-history preservation and optional later promotion.

## Boundary Model

```text
doctor diagnoses; review confirms; treatment or surgery writes; recovery proves;
archive preserves.
```

The model is a routing and governance contract. It does not grant write
permission by itself.

## Artifact Model

Each stage should leave or consume a repo-visible artifact:

- `checkup`: `wiki/status/*`, frontmatter checker reports, graph/status output,
  MOC dry-run output.
- `doctor`: `wiki/ops/wiki-doctor-runs/*-review.md`.
- `review`: future `wiki/ops/wiki-review-decisions/YYYY-MM-DD-*.md`.
- `treatment`: future narrow commits, accepted-item lists, and verification
  evidence.
- `surgery`: future OpenSpec change, batch plan, no-touch zones, rollback
  boundary, and per-batch recovery evidence.
- `recovery`: future checker, doctor, graph, status, and MOC dry-run evidence.
- `archive`: future linked case history and optional stable ADR promotion.

## Escalation

Treatment is appropriate only for low-risk, narrow, explicitly confirmed
repairs. Surgery is required for broad batch writes, relation rebuilding, MOC
projection writes, ADR or governance pages, OpenSpec-required findings,
high-volume weak relation evidence, drift traces, or repository behavior
changes.

## Current Case Interpretation

The current detailed wiki-doctor record is a surgery candidate because it has
large scope, governance risk, relation evidence warnings, and ADR/OpenSpec
sensitivity. Small confirmed subsets may later become treatment batches after a
review-decision workflow exists.
```

- [ ] **Step 3: Write the task checklist**

Create `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`:

```markdown
# Tasks

- [ ] 1. Create OpenSpec proposal, design, tasks, and spec delta for the medical loop.
- [ ] 2. Add a repo-visible wiki ops record for the LLM-WIKI self-evolution model.
- [ ] 3. Add evaluation evidence for behavior replay, prior-art dedupe, and validation.
- [ ] 4. Run OpenSpec validation and focused content checks.
- [ ] 5. Commit the completed formalization artifacts.
```

- [ ] **Step 4: Inspect status before commit**

Run:

```bash
git status --short
```

Expected: the three new OpenSpec files appear as untracked. Existing unrelated
dirty files may still appear; do not stage them.

- [ ] **Step 5: Commit the skeleton**

Run:

```bash
git add openspec/changes/formalize-llm-wiki-medical-loop/proposal.md openspec/changes/formalize-llm-wiki-medical-loop/design.md openspec/changes/formalize-llm-wiki-medical-loop/tasks.md
git commit -m "spec: add llm wiki medical loop proposal"
```

Expected: commit succeeds with only those three files.

## Task 2: Add Formal Requirements

**Files:**
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/specs/llm-wiki-medical-loop/spec.md`
- Modify: `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`

- [ ] **Step 1: Write the spec delta**

Create `openspec/changes/formalize-llm-wiki-medical-loop/specs/llm-wiki-medical-loop/spec.md`:

```markdown
## Purpose

Define the repository's LLM-WIKI self-evolution lifecycle as a medical loop while
preserving review, write, verification, and archive boundaries.

## ADDED Requirements

### Requirement: Repository SHALL define the LLM-WIKI medical loop

The repository SHALL define LLM-WIKI self-evolution as a staged lifecycle:
`checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive`.

#### Scenario: Future agent explains self-evolution stages

- **WHEN** a future agent needs to describe the LLM-WIKI self-evolution process
- **THEN** it SHALL use the medical-loop lifecycle vocabulary
- **AND** it SHALL preserve each stage as a distinct responsibility.

### Requirement: Repository SHALL separate diagnosis, confirmation, write, proof, and archive

The repository SHALL preserve the boundary that doctor diagnoses, review
confirms, treatment or surgery writes, recovery proves, and archive preserves.

#### Scenario: Doctor output exists

- **WHEN** a doctor diagnosis record exists
- **THEN** the repository SHALL treat it as diagnosis evidence only
- **AND** it SHALL NOT treat diagnosis as approval for frontmatter, taxonomy,
  relation, MOC, ADR, AGENTS, skill, or OpenSpec mutation.

#### Scenario: Repair is requested from diagnosis output

- **WHEN** a repair request is based on doctor findings
- **THEN** the repository SHALL require a human review decision or a later
  scoped OpenSpec change before write-capable workflows execute.

### Requirement: Repository SHALL define artifact expectations for each stage

The repository SHALL expect repo-visible artifacts at each lifecycle stage so
important state does not live only in stdout or chat.

#### Scenario: Lifecycle stage is discussed

- **WHEN** checkup, doctor, review, treatment, surgery, recovery, or archive is
  discussed as a repository workflow stage
- **THEN** the repository SHALL identify the repo-visible artifact class for that
  stage
- **AND** it SHALL preserve proof and approval boundaries in that artifact.

### Requirement: Repository SHALL route broad or governance-sensitive repair to surgery planning

The repository SHALL classify large, structural, or governance-sensitive repair
as surgery planning rather than treatment.

#### Scenario: Doctor output includes structural or governance risk

- **WHEN** doctor output includes broad batch writes, relation rebuilding, MOC
  projection writes, ADR or governance pages, OpenSpec-required findings,
  high-volume weak relation evidence, drift traces, or repository behavior
  changes
- **THEN** the repository SHALL classify the case as a surgery candidate
- **AND** it SHALL NOT execute the repair as ordinary treatment.

### Requirement: Repository SHALL keep later workflow capabilities out of this change

This change SHALL NOT create write-capable treatment, surgery, recovery, or
review-decision workflows.

#### Scenario: The medical loop is formalized

- **WHEN** this change is complete
- **THEN** no new skill, command, script, frontmatter write, relation write, MOC
  write, ADR mutation, AGENTS mutation, or OpenSpec archive mutation SHALL be
  introduced by this change.
```

- [ ] **Step 2: Validate the spec delta**

Run:

```bash
openspec validate formalize-llm-wiki-medical-loop --strict
```

Expected: validation passes. A PostHog DNS flush warning is acceptable if the
OpenSpec validation itself reports success.

- [ ] **Step 3: Mark Task 1 complete**

Modify `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec proposal, design, tasks, and spec delta for the medical loop.
- [ ] 2. Add a repo-visible wiki ops record for the LLM-WIKI self-evolution model.
- [ ] 3. Add evaluation evidence for behavior replay, prior-art dedupe, and validation.
- [ ] 4. Run OpenSpec validation and focused content checks.
- [ ] 5. Commit the completed formalization artifacts.
```

- [ ] **Step 4: Commit the spec delta**

Run:

```bash
git add openspec/changes/formalize-llm-wiki-medical-loop/specs/llm-wiki-medical-loop/spec.md openspec/changes/formalize-llm-wiki-medical-loop/tasks.md
git commit -m "spec: define llm wiki medical loop requirements"
```

Expected: commit succeeds with only the spec delta and task checklist.

## Task 3: Add Wiki Ops Model Record

**Files:**
- Create: `wiki/ops/llm-wiki-self-evolution-medical-loop.md`
- Modify: `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`

- [ ] **Step 1: Write the wiki ops record**

Create `wiki/ops/llm-wiki-self-evolution-medical-loop.md`:

```markdown
---
canonical_object: llm-wiki-self-evolution
artifact_type: ops-model
layer: ops
domain: wiki
ops_area: wiki-runtime
title: LLM-WIKI 自进化医疗闭环
status: draft
created_at: 2026-05-14
derived_from:
  - docs/superpowers/specs/2026-05-14-llm-wiki-self-evolution-design.md
  - openspec/changes/formalize-llm-wiki-medical-loop
---

# LLM-WIKI 自进化医疗闭环

## 一句话

LLM-WIKI 自进化不是 `doctor -> 自动改 wiki`，而是：

```text
体检 -> 诊断 -> 确诊 -> 治疗 -> 手术 -> 复查 -> 归档
```

英文工作名：

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

## 分工

- `checkup / 体检`：看 wiki 健康状态，例如 frontmatter、taxonomy、graph、status、MOC dry-run。
- `doctor / 诊断`：生成诊断病历，不写结构，不批准修复。
- `review / 确诊`：人确认哪些是误报、哪些可治疗、哪些要手术、哪些要 OpenSpec。
- `treatment / 治疗`：小范围、低风险、明确确认后的修复。
- `surgery / 手术`：大范围结构性修复，例如批量 frontmatter、关系重建、MOC 投影、ADR 或治理漂移。
- `recovery / 复查`：修复后重新跑 checker、doctor、graph、status、MOC dry-run。
- `archive / 归档`：把诊断、确认、修复、复查串成后续 agent 可读的病历链。

## 硬边界

```text
doctor diagnoses; review confirms; treatment or surgery writes; recovery proves;
archive preserves.
```

对应中文：

```text
医生只诊断；病人确认病情；治疗或手术才写入；复查才证明；归档才沉淀。
```

## 当前 wiki-doctor 结果怎么解释

当前详细诊断记录显示：

- 153 个候选
- 144 个 review-focus 条目
- 71 个 drift/governance 风险
- 112 个关系证据 warning
- 9 个 safe frontmatter 候选

这个整体是 `surgery candidate / 手术候选`。原因是范围大，并且牵涉治理、
关系证据、ADR、OpenSpec 和 MOC 边界。

但其中少量已经确认且低风险的条目，可以在后续 `review-decision` 工作流存在
后拆成 `treatment batch / 治疗批次`。

## 升级规则

- `safe_to_apply_frontmatter=true` 只表示可以进入治疗候选，不是自动批准。
- `relation_weak_evidence` 不能批量接受。
- `openspec_required` 不能通过治疗绕过。
- drift、retro、reanchor、runtime behavior 相关条目不能当普通 markdown 修补。
- MOC 写入属于结构投影写入，需要明确批准或后续 OpenSpec。

## 后续拆分

建议顺序：

1. `formalize-llm-wiki-medical-loop`
2. `add-wiki-review-decisions`
3. `add-wiki-treatment-workflow`
4. `add-wiki-surgery-workflow`
5. `add-wiki-recovery-records`

本页只记录总模型，不授权自动修复。
```

- [ ] **Step 2: Run frontmatter precheck on the new page**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/llm-wiki-self-evolution-medical-loop.md
```

Expected: the new page has no blocking unknown taxonomy value. If the command
reports unrelated whole-wiki drift, record that as pre-existing in
`evaluation.md` during Task 4.

- [ ] **Step 3: Mark Task 2 complete**

Modify `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec proposal, design, tasks, and spec delta for the medical loop.
- [x] 2. Add a repo-visible wiki ops record for the LLM-WIKI self-evolution model.
- [ ] 3. Add evaluation evidence for behavior replay, prior-art dedupe, and validation.
- [ ] 4. Run OpenSpec validation and focused content checks.
- [ ] 5. Commit the completed formalization artifacts.
```

- [ ] **Step 4: Commit the wiki ops record**

Run:

```bash
git add wiki/ops/llm-wiki-self-evolution-medical-loop.md openspec/changes/formalize-llm-wiki-medical-loop/tasks.md
git commit -m "docs: add llm wiki medical loop ops model"
```

Expected: commit succeeds with only the ops record and task checklist.

## Task 4: Add Evaluation Evidence

**Files:**
- Create: `openspec/changes/formalize-llm-wiki-medical-loop/evaluation.md`
- Modify: `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`

- [ ] **Step 1: Write evaluation evidence**

Create `openspec/changes/formalize-llm-wiki-medical-loop/evaluation.md`:

```markdown
# Evaluation: formalize LLM-WIKI medical loop

## Behavior Replay

### Scenario: Future agent sees doctor output and user says to repair

- Input shape: user asks to act on a `wiki-doctor` diagnosis record.
- Trigger condition: diagnosis output contains review-focus, relation evidence,
  governance, ADR, MOC, or OpenSpec-sensitive findings.
- Expected route: explain that doctor is diagnosis-only and route to review,
  treatment, or surgery depending on confirmed scope.
- Repo-visible artifact: `wiki/ops/llm-wiki-self-evolution-medical-loop.md`.
- Expected non-output: no automatic frontmatter, taxonomy, relation, MOC, ADR,
  AGENTS, skill, or OpenSpec lifecycle mutation from diagnosis alone.
- Promotion boundary: execution capability requires later OpenSpec changes.
- Residual risk: the model gives vocabulary and boundaries, not executable
  enforcement.

### Scenario: Future agent sees 9 safe frontmatter candidates

- Input shape: doctor output reports `safe_to_apply_frontmatter=true` on a small
  subset.
- Trigger condition: user asks whether those can be fixed.
- Expected route: classify them as treatment candidates only after human review
  confirmation.
- Repo-visible artifact: future `wiki-review-decisions` record; not created by
  this change.
- Expected non-output: no automatic write from the safe flag alone.
- Promotion boundary: `add-wiki-review-decisions` and
  `add-wiki-treatment-workflow` must define the execution path.
- Residual risk: until those changes exist, the safe candidates remain
  diagnosis material.

### Scenario: Future agent sees broad governance and relation drift

- Input shape: doctor output reports high-volume weak relation evidence, drift,
  ADR, or OpenSpec-required reasons.
- Trigger condition: user says this is a large range and asks whether it is
  surgery.
- Expected route: classify as a surgery candidate and create or select a later
  OpenSpec plan before structural writes.
- Repo-visible artifact: future surgery OpenSpec change; not created by this
  change.
- Expected non-output: no batch relation acceptance or MOC projection write.
- Promotion boundary: `add-wiki-surgery-workflow` must define batching,
  no-touch zones, rollback, and recovery evidence.
- Residual risk: this change does not implement surgery planning templates.

## Prior-Art / Common-Rule Dedupe

- Repo `AGENTS.md` already owns workflow-change gating and OpenSpec lifecycle.
  This change references that boundary and does not restate git or health-check
  rules.
- ADR-0033 already separates wiki-react, eval, apply, repair labels, and
  OpenSpec. This change preserves that boundary and adds only the broader
  medical-loop vocabulary.
- `wiki-doctor` review records already define diagnosis evidence. This change
  does not change the skill; it places doctor in the larger lifecycle.
- `wiki-self-directed-execution` already defines bounded execution guidance.
  This change does not claim unrestricted autonomy or execution proof.

## Validation

- `openspec validate formalize-llm-wiki-medical-loop --strict`
  - Result: not recorded in the initial evidence draft. Task 4 Step 4 replaces
    this line with the actual command result before the evidence commit.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/llm-wiki-self-evolution-medical-loop.md`
  - Result: not recorded in the initial evidence draft. Task 4 Step 4 replaces
    this line with the actual command result before the evidence commit.

## Residual Risks

- This change formalizes vocabulary and boundaries only.
- Review-decision, treatment, surgery, and recovery records still need separate
  OpenSpec changes.
- Existing whole-wiki frontmatter drift may still make broad frontmatter checks
  fail outside this change.
```

- [ ] **Step 2: Run OpenSpec validation**

Run:

```bash
openspec validate formalize-llm-wiki-medical-loop --strict
```

Expected: validation passes. If there is a telemetry DNS warning but the change
is valid, record the valid result and warning in `evaluation.md`.

- [ ] **Step 3: Run focused frontmatter precheck**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/llm-wiki-self-evolution-medical-loop.md
```

Expected: the target page is not blocked by unknown taxonomy values. If the
checker reports pre-existing whole-wiki drift, record the result and boundary in
`evaluation.md`.

- [ ] **Step 4: Update validation results in evaluation**

Modify the `## Validation` section in
`openspec/changes/formalize-llm-wiki-medical-loop/evaluation.md` so it contains
the actual command results:

```markdown
## Validation

- `openspec validate formalize-llm-wiki-medical-loop --strict`
  - Result: pass. OpenSpec reported the change as valid. PostHog DNS flush
    warnings, if present, were telemetry-only.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/llm-wiki-self-evolution-medical-loop.md`
  - Result: pass for the new target page, or bounded expected failure only if
    the command reports pre-existing whole-wiki drift unrelated to this page.
```

- [ ] **Step 5: Mark Tasks 3 and 4 complete**

Modify `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec proposal, design, tasks, and spec delta for the medical loop.
- [x] 2. Add a repo-visible wiki ops record for the LLM-WIKI self-evolution model.
- [x] 3. Add evaluation evidence for behavior replay, prior-art dedupe, and validation.
- [x] 4. Run OpenSpec validation and focused content checks.
- [ ] 5. Commit the completed formalization artifacts.
```

- [ ] **Step 6: Commit evaluation evidence**

Run:

```bash
git add openspec/changes/formalize-llm-wiki-medical-loop/evaluation.md openspec/changes/formalize-llm-wiki-medical-loop/tasks.md
git commit -m "test: record llm wiki medical loop evidence"
```

Expected: commit succeeds with only evaluation evidence and task checklist.

## Task 5: Final Verification And Stop

**Files:**
- Modify: `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`

- [ ] **Step 1: Run final OpenSpec validation**

Run:

```bash
openspec validate formalize-llm-wiki-medical-loop --strict
```

Expected: validation passes.

- [ ] **Step 2: Inspect staged and unstaged files**

Run:

```bash
git status --short
```

Expected: only unrelated pre-existing dirty files remain unstaged. If files from
this change remain unstaged, stage only those files.

- [ ] **Step 3: Mark Task 5 complete**

Modify `openspec/changes/formalize-llm-wiki-medical-loop/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec proposal, design, tasks, and spec delta for the medical loop.
- [x] 2. Add a repo-visible wiki ops record for the LLM-WIKI self-evolution model.
- [x] 3. Add evaluation evidence for behavior replay, prior-art dedupe, and validation.
- [x] 4. Run OpenSpec validation and focused content checks.
- [x] 5. Commit the completed formalization artifacts.
```

- [ ] **Step 4: Commit final task completion**

Run:

```bash
git add openspec/changes/formalize-llm-wiki-medical-loop/tasks.md
git commit -m "spec: complete llm wiki medical loop formalization"
```

Expected: commit succeeds with only the task checklist.

- [ ] **Step 5: Stop at OpenSpec hard stop**

Do not archive the change in this plan. Once every checkbox is complete, stop
implementation. The default next action is archive review, not automatic archive.

Run:

```bash
git log -1 --oneline
git status --short
```

Expected: latest commit is `spec: complete llm wiki medical loop formalization`.
Unrelated pre-existing dirty files may still appear.

## Self-Review Checklist

- Spec coverage: the plan implements lifecycle vocabulary, artifact boundaries,
  treatment/surgery escalation, non-goals, behavior replay, and validation.
- Scope boundary: review decisions, treatment, surgery, and recovery execution
  remain future changes.
- Completion scan: the plan contains no unfinished fill-in sections; command
  results are captured during Task 4 after the commands run.
- Type consistency: all paths use the single change id
  `formalize-llm-wiki-medical-loop`.
