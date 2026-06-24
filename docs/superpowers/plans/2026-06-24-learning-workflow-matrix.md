# Learning Workflow Matrix Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved learning workflow matrix as a repo-governed `learning-capture` controller update with modular references, structural checkers, and behavior evidence.

**Architecture:** OpenSpec owns the lifecycle state; the Superpowers design stays as input evidence. Keep `.codex/skills/learning-capture/SKILL.md` as a compact controller, move the matrix into `references/`, and add Python validation for L2/L3 structured learning records. Behavior proof lives in the OpenSpec change `evaluation.md`.

**Tech Stack:** Markdown skills and references, OpenSpec change artifacts, Python 3 standard library plus existing `yaml` dependency, pytest, `scripts/check_behavior_assets.py`, `scripts/repo_health_check.py`.

---

## File Structure

**Create**

- `openspec/changes/add-learning-workflow-matrix/proposal.md`
  - Lifecycle proposal for the learning matrix implementation.
- `openspec/changes/add-learning-workflow-matrix/design.md`
  - Implementation design and boundaries.
- `openspec/changes/add-learning-workflow-matrix/tasks.md`
  - Authoritative checklist for implementation.
- `openspec/changes/add-learning-workflow-matrix/evaluation.md`
  - Skill behavior proof, pressure scenarios, RED/GREEN evidence, prior-art/common-rule dedupe.
- `openspec/changes/add-learning-workflow-matrix/specs/learning-capture/spec.md`
  - New or updated normative requirements for the learning workflow.
- `.codex/skills/learning-capture/references/levels.md`
  - L0-L3 learning depth contract.
- `.codex/skills/learning-capture/references/learning-types.md`
  - Technical, business, company case, industry trend, output expression, and governance learning types.
- `.codex/skills/learning-capture/references/research-methods.md`
  - Case study, process tracing, triangulation, evidence sufficiency, saturation, and due-diligence layering.
- `.codex/skills/learning-capture/references/evidence-strength.md`
  - Evidence status and source-layer vocabulary.
- `.codex/skills/learning-capture/references/source-queue.md`
  - L3 source queue field contract.
- `.codex/skills/learning-capture/references/output-contract.md`
  - L1/L2/L3 structured output fields.
- `.codex/skills/learning-capture/references/public-writing-method.md`
  - Reader-facing transformation method.
- `tests/test_learning_record_checker.py`
  - TDD coverage for the new checker.
- `scripts/check_learning_record.py`
  - Structural validator for L2/L3 learning YAML files.
- `scripts/examples/learning-record-l2-valid.yaml`
  - Passing checker fixture.
- `scripts/examples/learning-record-l3-missing-proof-boundary.yaml`
  - Failing checker fixture.

**Modify**

- `.codex/skills/learning-capture/SKILL.md`
  - Add compact routing rules for learning level/type and reference loading.
- `.codex/skills/learning-capture/references/pressure-scenarios.md`
  - Add matrix-specific pressure scenarios.
- `tests/test_learning_capture_consolidation.py`
  - Add regression tests that references exist and `SKILL.md` stays compact.
- `wiki/ops/learning-agent-architecture-patterns-2026-06-24.md`
  - Read only unless implementation reveals a factual correction.
- `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`
  - Read only; do not rewrite the approved brainstorming spec during implementation.

**Do Not Modify**

- `AGENTS.md`
- `PROJECT.md`
- Existing unrelated dirty `wiki/`, `inbox/`, `tmp/`, dot-agent, or report files.
- Any OpenSpec archive.
- Any frontmatter checker or behavior-asset checker unless a failing test proves the checker itself is wrong.

---

### Task 1: Create the OpenSpec Change Skeleton

**Files:**
- Create: `openspec/changes/add-learning-workflow-matrix/proposal.md`
- Create: `openspec/changes/add-learning-workflow-matrix/design.md`
- Create: `openspec/changes/add-learning-workflow-matrix/tasks.md`
- Create: `openspec/changes/add-learning-workflow-matrix/specs/learning-capture/spec.md`
- Read: `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`

- [ ] **Step 1: Create the OpenSpec directories**

Run:

```bash
mkdir -p openspec/changes/add-learning-workflow-matrix/specs/learning-capture
```

Expected:

```text
openspec/changes/add-learning-workflow-matrix/specs/learning-capture
```

- [ ] **Step 2: Write `proposal.md`**

Create `openspec/changes/add-learning-workflow-matrix/proposal.md` with:

```markdown
# Add Learning Workflow Matrix

## Why

`learning-capture` currently routes external articles, repos, READMEs, and examples, but it does not define how to choose learning depth, learning type, evidence strength, research methods, or reader-facing output transformation.

The Stripe research discussion exposed this gap: a long company-path case with a source queue, process tracing, cross-validation, saturation judgment, and H5/report output cannot be handled as an ordinary source summary.

## What Changes

- Keep `learning-capture` as a compact controller.
- Add modular references for learning levels, learning types, research methods, evidence strength, source queues, output contracts, and public-writing transformation.
- Add structural validation for L2/L3 learning records.
- Add local pressure-test evidence for OCR-style technical learning, Stripe-style company reconstruction, public article/H5 transformation, and governance/agent workflow learning.

## Out Of Scope

- No full state machine or graph runtime in the first implementation.
- No function-calling runtime dependency.
- No `AGENTS.md` behavior change.
- No automatic source fetching or citation verification.
- No claim that Python validates business or technical judgment correctness.
```

- [ ] **Step 3: Write `design.md`**

Create `openspec/changes/add-learning-workflow-matrix/design.md` with:

````markdown
# Design: Learning Workflow Matrix

## Architecture

Use:

```text
learning-capture controller
  -> references/levels.md
  -> references/learning-types.md
  -> references/research-methods.md
  -> references/evidence-strength.md
  -> references/source-queue.md
  -> references/output-contract.md
  -> references/public-writing-method.md
  -> scripts/check_learning_record.py
  -> evaluation.md pressure scenarios
```

`SKILL.md` owns trigger and routing only. Reference files own tables and detailed method contracts. Python scripts own structural checks only.

## Behavior Boundary

When a request reaches L2 or L3, the agent must state:

- learning level;
- learning type;
- required inputs;
- methods to use;
- expected outputs;
- whether the task must split.

When a claim affects behavior assets, OpenSpec specs, AGENTS guidance, public reports, H5, PPT, or Feishu-facing review output, the agent must preserve promotion boundaries instead of promoting directly from a source note.

## Checker Boundary

`scripts/check_learning_record.py` validates required fields and evidence/proof-boundary presence. It does not decide whether a business strategy, technical architecture, or market judgment is correct.

## Prior Art

The implementation references:

- repo `AGENTS.md` workflow gates;
- `openspec/specs/skill-authoring-contract/spec.md`;
- `openspec/specs/skill-evaluation-evidence/spec.md`;
- `openspec/specs/local-skill-pressure-tests/spec.md`;
- `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`;
- `wiki/ops/learning-agent-architecture-patterns-2026-06-24.md`.
````

- [ ] **Step 4: Write `tasks.md`**

Create `openspec/changes/add-learning-workflow-matrix/tasks.md` with:

```markdown
# Tasks

- [ ] Create OpenSpec change skeleton and spec delta.
- [ ] Record RED baseline pressure scenarios before semantic skill edits.
- [ ] Add learning matrix reference files under `.codex/skills/learning-capture/references/`.
- [ ] Update `.codex/skills/learning-capture/SKILL.md` as a compact controller.
- [ ] Add checker tests before checker implementation.
- [ ] Implement `scripts/check_learning_record.py`.
- [ ] Add checker fixtures under `scripts/examples/`.
- [ ] Update pressure scenarios and evaluation evidence.
- [ ] Run focused tests.
- [ ] Run behavior asset and repo health checks.
```

- [ ] **Step 5: Write the spec delta**

Create `openspec/changes/add-learning-workflow-matrix/specs/learning-capture/spec.md` with:

```markdown
# learning-capture Specification

## Requirements

### Requirement: Learning capture SHALL classify learning level before deep work

`learning-capture` SHALL classify reusable learning requests into L0, L1, L2, or L3 before deep analysis when the request is non-trivial.

#### Scenario: User asks for ordinary source learning
- **WHEN** the user asks to learn reusable points from a normal article, repo, README, or example
- **THEN** the agent SHALL default to L1 unless stronger signals apply
- **AND** the output SHALL include reusable point and non-transfer boundary

#### Scenario: User asks for local adaptation or value judgment
- **WHEN** the source may affect local reports, skills, OpenSpec, AGENTS guidance, H5, PPT, Feishu review, or public artifacts
- **THEN** the agent SHALL route as at least L2
- **AND** the agent SHALL state method, input inventory, value judgment, and transfer boundary

#### Scenario: User asks for company path or long-horizon reconstruction
- **WHEN** the task involves company evolution, industry trend, future judgment, long timeline, multi-source evidence pool, or source queue
- **THEN** the agent SHALL route as L3
- **AND** the agent SHALL use research reconstruction, evidence matrix, and proof-boundary concepts

### Requirement: Learning capture SHALL classify learning type

`learning-capture` SHALL classify non-trivial learning as technical, business, company case, industry trend, output expression, or governance/agent workflow before selecting methods.

#### Scenario: Technical repo learning
- **WHEN** the user provides a GitHub repo and asks whether its approach helps local CR-agent work
- **THEN** the agent SHALL route as technical learning
- **AND** the agent SHALL distinguish architecture/tooling learning from code-quality claims

#### Scenario: Stripe-style company learning
- **WHEN** the user asks for Stripe-style company path research
- **THEN** the agent SHALL route as company-case L3 learning
- **AND** the agent SHALL use case study, process tracing, triangulation, evidence sufficiency, and source layering

### Requirement: L2 and L3 learning records SHALL use structured output contracts

L2 and L3 learning records SHALL include machine-checkable YAML fields for level, type, methods, input inventory, evidence, value judgment, and proof boundary.

#### Scenario: L3 record lacks proof boundary
- **WHEN** a L3 learning record has no proof boundary
- **THEN** the checker SHALL fail the record

### Requirement: Public writing transformation SHALL be separate from learning capture

Reader-facing articles, H5/share drafts, PPTs, and public reports SHALL use a writing transformation layer after learning capture.

#### Scenario: Research note is intended for H5 output
- **WHEN** the learning result will feed a reader-facing H5 or report
- **THEN** the output SHALL include article intent, reader path, thesis, evidence placement, claim-strength control, citation surface, and section drift review
```

- [ ] **Step 6: Verify the skeleton**

Run:

```bash
find openspec/changes/add-learning-workflow-matrix -maxdepth 3 -type f | sort
```

Expected:

```text
openspec/changes/add-learning-workflow-matrix/design.md
openspec/changes/add-learning-workflow-matrix/proposal.md
openspec/changes/add-learning-workflow-matrix/specs/learning-capture/spec.md
openspec/changes/add-learning-workflow-matrix/tasks.md
```

- [ ] **Step 7: Commit the skeleton**

Run:

```bash
git add openspec/changes/add-learning-workflow-matrix/proposal.md openspec/changes/add-learning-workflow-matrix/design.md openspec/changes/add-learning-workflow-matrix/tasks.md openspec/changes/add-learning-workflow-matrix/specs/learning-capture/spec.md
git commit -m "Add learning workflow matrix OpenSpec change"
```

---

### Task 2: Record RED Baseline Evaluation Before Skill Edits

**Files:**
- Create: `openspec/changes/add-learning-workflow-matrix/evaluation.md`
- Read: `.codex/skills/learning-capture/SKILL.md`
- Read: `.codex/skills/learning-capture/references/pressure-scenarios.md`

- [ ] **Step 1: Create `evaluation.md` with pressure scenarios and RED baseline**

Create `openspec/changes/add-learning-workflow-matrix/evaluation.md` with:

````markdown
# Evaluation: Learning Workflow Matrix

## Pressure Scenarios

| Case | Input or situation shape | Trigger condition | Expected route | Repo-visible artifact | Expected output | Promotion or non-promotion boundary | Proof boundary |
|---|---|---|---|---|---|---|---|
| positive technical OCR learning | User provides `https://github.com/alibaba/open-code-review` and asks whether it helps `cr-agent` | GitHub repo in active learning/adaptation thread | `learning-capture` -> technical L2 | `.codex/skills/learning-capture/references/learning-types.md` | Distinguish architecture/tooling learning from code-quality claims | Do not promote into CR-agent behavior without OpenSpec | Local pressure evidence only |
| positive Stripe research | User asks for Stripe company path with source queue and public H5 output | Company path, long timeline, multi-source evidence pool | `learning-capture` -> company-case L3 | `.codex/skills/learning-capture/references/source-queue.md` | Research reconstruction, evidence matrix, proof boundary, output transformation | Do not claim saturation without P0/P1 source stability | Local pressure evidence only |
| positive public writing | User asks to turn research learning into an external article/H5/PPT | Reader-facing output intent | `learning-capture` -> public writing method reference | `.codex/skills/learning-capture/references/public-writing-method.md` | Article intent, reader path, thesis, evidence placement, claim strength | Public gate remains separate | Local pressure evidence only |
| positive governance workflow | User asks whether learning workflow should change `learning-capture` or AGENTS | Behavior asset effect | `learning-capture` -> governance L2/L3 plus OpenSpec boundary | `openspec/changes/add-learning-workflow-matrix/` | Prior-art scan, promotion boundary, pressure tests | Do not edit behavior assets from conversation alone | Local pressure evidence only |
| negative should-not-trigger quick lookup | User asks latest factual answer with no local reuse intent | No learning, reuse, wiki, or method-calibration context | Do not trigger `learning-capture` | none | Answer lookup directly | No durable learning artifact | Local pressure evidence only |
| negative should-not-trigger raw fetch | User asks only to fetch raw WeChat body text | Raw extraction only | Use `weixin-reader` or source fetch path | none | Raw extracted text or fetch blocker | No learning matrix output | Local pressure evidence only |

## RED Baseline

Baseline command:

```bash
sed -n '1,140p' .codex/skills/learning-capture/SKILL.md
```

Observed baseline:

- Existing controller routes by evidence object: article, repo/README, example, or unclear source.
- Existing controller does not define L0/L1/L2/L3.
- Existing controller does not define learning type selection.
- Existing controller does not define source queue, evidence saturation, or public-writing transformation.
- Existing pressure scenarios do not cover OCR technical learning, Stripe L3 company reconstruction, public-writing transformation, or governance behavior promotion.

RED result: FAIL. The old wording cannot route the approved matrix.

## GREEN Result

Planned GREEN evidence commands:

```bash
python3 -m pytest tests/test_learning_capture_consolidation.py tests/test_learning_record_checker.py -q
python3 scripts/check_behavior_assets.py
python3 scripts/repo_health_check.py
```

Planned manual replay result: each pressure scenario above must be updated
with observed GREEN behavior before implementation is claimed complete.

## Prior-Art / Common-Rule Dedupe

Scanned:

- repo `AGENTS.md`
- `PROJECT.md`
- `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`
- `wiki/ops/learning-agent-architecture-patterns-2026-06-24.md`
- `openspec/specs/skill-authoring-contract/spec.md`
- `openspec/specs/skill-evaluation-evidence/spec.md`
- `openspec/specs/local-skill-pressure-tests/spec.md`
- `.codex/skills/learning-capture/SKILL.md`
- `.codex/skills/learning-capture/references/pressure-scenarios.md`
- `/home/yan/.codex/skills/writing-skills/SKILL.md`
- `/home/yan/.codex/skills/test-driven-development/SKILL.md`

Owns:

- Learning-level and learning-type routing inside `learning-capture`.
- Structured L2/L3 learning output contracts.
- Source queue and proof-boundary concepts for L3 learning.

References:

- Repo workflow gates and OpenSpec lifecycle remain owned by `AGENTS.md` and OpenSpec specs.
- Skill-authoring test discipline remains owned by writing-skills and test-driven-development.
- Public report readiness remains owned by the public-report gate.

Rejects:

- Promoting conversation-only learning directly into `AGENTS.md`.
- Creating a full state machine in the first implementation.
- Treating local wiki artifacts as industry benchmark materials.

## Residual Risks

- Local pressure evidence is not multi-end rollout proof.
- The checker validates structure, not judgment correctness.
- Public citation verification remains a separate future capability.
````

- [ ] **Step 2: Run behavior asset checker and confirm RED state is acceptable before skill edits**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected:

```text
No behavior asset evaluation drift found.
```

If existing unrelated active changes fail the checker, copy the exact failing paths into `evaluation.md` under `## Residual Risks` before continuing.

- [ ] **Step 3: Commit RED baseline evidence**

Run:

```bash
git add openspec/changes/add-learning-workflow-matrix/evaluation.md
git commit -m "Record learning matrix evaluation baseline"
```

---

### Task 3: Add Learning Matrix Reference Files

**Files:**
- Create: `.codex/skills/learning-capture/references/levels.md`
- Create: `.codex/skills/learning-capture/references/learning-types.md`
- Create: `.codex/skills/learning-capture/references/research-methods.md`
- Create: `.codex/skills/learning-capture/references/evidence-strength.md`
- Create: `.codex/skills/learning-capture/references/source-queue.md`
- Create: `.codex/skills/learning-capture/references/output-contract.md`
- Create: `.codex/skills/learning-capture/references/public-writing-method.md`

- [ ] **Step 1: Write `levels.md`**

Create `.codex/skills/learning-capture/references/levels.md` with the L0-L3 table from `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`, preserving these required rules:

```markdown
# Learning Levels

Use this reference after `learning-capture` decides the request has reusable learning intent.

| Level | Name | Goal | Input Strength | Method Strength | Output | Stop Condition |
|---|---|---|---|---|---|---|
| L0 | quick judgment | Decide whether a source is worth continuing | 1-3 accessible sources; README/abstract/entry page is enough | source class and relevance judgment | short conclusion, continue/skip, next step | enough to answer whether to continue |
| L1 | ordinary learning | Extract reusable points | 3-8 core sources or one complete material package | grounding, reuse/modify/reject, boundary | what was learned, transferable practices, non-transfer boundary | reusable point and boundary are clear |
| L2 | deep learning | Support a technical, product, or business judgment | multiple evidence types; at least two-way cross-validation | input decomposition, triangulation, evidence sufficiency, selected framework | input inventory, method used, value judgment, output map, transfer boundary | load-bearing claims have evidence strength |
| L3 | research-grade learning | Reconstruct an object and produce research-grade judgment | preset evidence pool, P0/P1 reading, source queue when needed | case study, process tracing, triangulation, evidence sufficiency, data saturation, due-diligence source layering | object reconstruction, causal chain, evidence matrix, method layer, value judgment, output transformation plan | new P0/P1 sources no longer change the main judgment, and residual gaps have proof boundaries |

## Defaults

- Unspecified depth starts at L1.
- Local reuse, adaptation, or value judgment upgrades non-trivial work to at least L2.
- OpenSpec, skills, AGENTS, agent behavior, H5, PPT, Feishu review, or public report impact requires at least L2.
- Company path, industry trend, future judgment, long timeline, multi-source evidence pool, or source queue requires L3.
- If there is not enough context for L3, split the work instead of compressing it into L1.
```

- [ ] **Step 2: Write `learning-types.md`**

Create `.codex/skills/learning-capture/references/learning-types.md` with:

```markdown
# Learning Types

| Type | Typical Question | Core Methods | High-Quality Industry References | Local Samples / Replay |
|---|---|---|---|---|
| Technical | How does it work? What is reusable? | architecture decomposition, execution-chain tracing, interface/data-flow analysis, capability mapping | official engineering docs, high-quality OSS architecture docs, protocol specs | OpenCodeReview learning, CR-agent migration candidates |
| Business | Why does this strategy matter? Where is the value? | value-chain analysis, business model decomposition, unit economics, competitive position, customer segmentation | annual reports, shareholder letters, market reports, audited filings | Stripe source pack, Stripe report gate review |
| Company Case | How did this company evolve? | case study research, process tracing, triangulation, evidence sufficiency | company annual letters, product update archives, investor materials, business-school style cases | Stripe H5 reanchor, Stripe drift retro |
| Industry Trend | Where is this trend going? | trend layering, time constants, scenario analysis, key-variable analysis, counterexample analysis | market guides, regulatory records, central-bank/international-organization reports, state-of-industry reports | AI payment / agent commerce chapters |
| Output Expression | Why does this article/H5/PPT work? | structure mapping, reader-job analysis, narrative skeleton, visual-evidence relation, paragraph rhythm | high-quality visual explainers, public company update pages, benchmark report pages | Stripe H5 redesign drift, public-report gate reviews |
| Governance / Agent Workflow | Should this behavior be formalized? | failure replay, promotion boundary, prior-art scan, OpenSpec formalization, pressure tests | OpenAI/Anthropic docs, LangGraph docs, MCP docs, mature OSS contributor guides | learning-capture routing, visual-agent drift, openspec-router replay |

High-quality industry references are external benchmark materials. Local artifacts are replay samples, pressure tests, or implementation evidence.
```

- [ ] **Step 3: Write `research-methods.md`**

Create `.codex/skills/learning-capture/references/research-methods.md` with sections for:

````markdown
# Research Methods

## Case Study Research / 案例研究

Use for company, product system, tool, organization, or workflow reconstruction.

## Process Tracing / 过程追踪

Use the chain:

```text
what happened -> why it happened -> what capability accumulated -> how later events reused that capability
```

## Triangulation / 交叉验证

Validate load-bearing claims across source, type, time, actor, and positive/negative evidence.

## Evidence Sufficiency / 证据充分性

Label claims as promoted, candidate, route-only, proof-boundary, or rejected.

## Data Saturation / 资料饱和

Claim module saturation only when new P0/P1 sources no longer change the main judgment.

## Due Diligence Source Layering / 尽调式材料分层

Separate official first-party material, audited or financial data, product/API docs, partner material, customer cases, media reports, analyst writing, community interpretation, and speculation.
````

- [ ] **Step 4: Write `evidence-strength.md`, `source-queue.md`, `output-contract.md`, and `public-writing-method.md`**

Create `.codex/skills/learning-capture/references/evidence-strength.md` with:

```markdown
# Evidence Strength

Use this reference for L2/L3 learning records and for any load-bearing claim.

## Claim Status

| Status | Meaning | Allowed Use |
|---|---|---|
| promoted | Enough evidence for visible output | May appear in learning artifact or reader-facing draft with citation route |
| candidate | Plausible but not sufficiently proven | May guide analysis; do not present as settled |
| route-only | Useful source lead only | Keep for follow-up queue |
| proof-boundary | Important but insufficiently proven | State as boundary or open risk |
| rejected | Unsupported or too risky | Do not reuse as claim |

## Cross-Validation Dimensions

- source: official, financial, docs, media, peer, analyst;
- type: metric, product release, API doc, acquisition, hiring, customer case;
- time: early path, middle accumulation, current stage;
- actor: self-claim, peer action, partner, protocol, regulator;
- positive/negative: support, boundary, counterexample, missing evidence.
```

Create `.codex/skills/learning-capture/references/source-queue.md` with:

```markdown
# Source Queue

Use this reference for L3 research cases where source order, coverage, and saturation matter.

## Required Fields

| Field | Meaning |
|---|---|
| source_id | Stable local source identifier |
| priority | P0, P1, P2, or backlog |
| source_type | official, financial, product-doc, partner, customer, media, analyst, community, speculative |
| status | unread, skimmed, read, promoted, rejected, deferred |
| evidence_role | What the source can prove or bound |
| claim_link | Claim id or section id this source supports |
| promoted | yes/no; whether it can support visible output |
| saturation_area | Area this source helps saturate |

## Saturation Rule

Do not claim an area is saturated until new P0/P1 sources no longer change the main judgment and only add detail.
```

Create `.codex/skills/learning-capture/references/output-contract.md` with:

````markdown
# Output Contract

Use this reference when producing L1/L2/L3 learning output.

## L1 Minimum Output

- source kind;
- what was learned;
- reusable point;
- non-transfer or non-promotion boundary.

## L2 Required YAML Fields

```yaml
learning_level: L2
learning_type: Technical
methods_used: []
input_inventory: []
evidence_matrix: []
value_judgment: ""
proof_boundary: ""
```

## L3 Required YAML Fields

```yaml
learning_level: L3
learning_type: Company Case
methods_used: []
input_inventory: []
research_reconstruction_model: {}
evidence_matrix: []
value_judgment: ""
proof_boundary: ""
output_transformation_plan: {}
```
````

Create `.codex/skills/learning-capture/references/public-writing-method.md` with:

```markdown
# Public Writing Method

Use this reference after learning capture when the output is a reader-facing article, H5/share draft, PPT, public report, or Feishu review draft.

Reader-facing output is not a polished learning note. Transform the learning through:

| Field | Purpose |
|---|---|
| article_intent_contract | Define reader, reader decision, main line, non-goals, and user-owned judgments |
| reader_path | Define the order in which the reader should understand the argument |
| thesis | Name the main judgment before section drafting |
| section_structure | Map sections to reader decisions and evidence roles |
| evidence_placement | Attach every chart, metric, quote, and visual to a named claim |
| visual_role | Define what each visual proves or clarifies |
| claim_strength_control | Separate assertion, candidate, boundary, and speculation |
| citation_surface | Provide reader-visible evidence for load-bearing claims |
| section_drift_review | Check each section against the intent contract |

Do not claim public-review-ready output when citation surface or section drift review is missing.
```

- [ ] **Step 5: Verify reference names**

Run:

```bash
find .codex/skills/learning-capture/references -maxdepth 1 -type f | sort | rg 'levels|learning-types|research-methods|evidence-strength|source-queue|output-contract|public-writing-method'
```

Expected: all seven new reference files are listed.

- [ ] **Step 6: Commit references**

Run:

```bash
git add .codex/skills/learning-capture/references/levels.md .codex/skills/learning-capture/references/learning-types.md .codex/skills/learning-capture/references/research-methods.md .codex/skills/learning-capture/references/evidence-strength.md .codex/skills/learning-capture/references/source-queue.md .codex/skills/learning-capture/references/output-contract.md .codex/skills/learning-capture/references/public-writing-method.md
git commit -m "Add learning matrix references"
```

---

### Task 4: Update the Learning Capture Controller and Pressure Scenarios

**Files:**
- Modify: `.codex/skills/learning-capture/SKILL.md`
- Modify: `.codex/skills/learning-capture/references/pressure-scenarios.md`
- Modify: `tests/test_learning_capture_consolidation.py`

- [ ] **Step 1: Add a failing compact-controller test**

Append to `tests/test_learning_capture_consolidation.py`:

```python
def test_learning_capture_controller_links_matrix_references_and_stays_compact() -> None:
    skill = Path(".codex/skills/learning-capture/SKILL.md")
    text = skill.read_text(encoding="utf-8")

    assert "references/levels.md" in text
    assert "references/learning-types.md" in text
    assert "references/output-contract.md" in text
    assert "references/public-writing-method.md" in text
    assert len(text.splitlines()) <= 140
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
python3 -m pytest tests/test_learning_capture_consolidation.py::test_learning_capture_controller_links_matrix_references_and_stays_compact -q
```

Expected:

```text
FAILED
```

Failure reason should mention one missing reference link.

- [ ] **Step 3: Update `SKILL.md` as controller only**

Add this section after `## Module Map` in `.codex/skills/learning-capture/SKILL.md`:

```markdown
## Learning Matrix Routing

For non-trivial learning requests, classify level and type before deep work:

1. Load `references/levels.md` to choose L0/L1/L2/L3.
2. Load `references/learning-types.md` to choose technical, business, company-case, industry-trend, output-expression, or governance learning.
3. For L2/L3, load `references/research-methods.md`, `references/evidence-strength.md`, and `references/output-contract.md`.
4. For L3 source pools, load `references/source-queue.md`.
5. For reader-facing articles, H5, PPT, or public reports, load `references/public-writing-method.md` after learning capture; do not treat learning notes as publish-ready output.
```

- [ ] **Step 4: Add pressure scenarios**

Append to `.codex/skills/learning-capture/references/pressure-scenarios.md`:

```markdown
## Learning Matrix Scenarios

| Scenario | Expected behavior |
|---|---|
| User asks what OpenCodeReview teaches local `cr-agent` | Trigger `learning-capture`, classify as technical L2, distinguish architecture/tooling from code-quality claims |
| User asks for Stripe-style company path research with source queue | Trigger `learning-capture`, classify as company-case L3, use source queue, evidence matrix, and proof boundary |
| User asks to turn research into H5/public article/PPT | Use learning capture first, then public-writing method; do not claim publish-ready without citation surface |
| User asks whether a learning insight should change a skill or AGENTS | Classify as governance/agent workflow, preserve OpenSpec and behavior-asset gates |
| User asks a latest-fact lookup with no local reuse intent | Do not trigger learning capture |
```

- [ ] **Step 5: Run focused tests and verify GREEN**

Run:

```bash
python3 -m pytest tests/test_learning_capture_consolidation.py -q
```

Expected:

```text
4 passed
```

- [ ] **Step 6: Commit controller and pressure updates**

Run:

```bash
git add .codex/skills/learning-capture/SKILL.md .codex/skills/learning-capture/references/pressure-scenarios.md tests/test_learning_capture_consolidation.py
git commit -m "Route learning capture through matrix references"
```

---

### Task 5: Add the Learning Record Checker with TDD

**Files:**
- Create: `tests/test_learning_record_checker.py`
- Create: `scripts/check_learning_record.py`
- Create: `scripts/examples/learning-record-l2-valid.yaml`
- Create: `scripts/examples/learning-record-l3-missing-proof-boundary.yaml`

- [ ] **Step 1: Write checker tests first**

Create `tests/test_learning_record_checker.py` with:

```python
from __future__ import annotations

import tempfile
from pathlib import Path

from scripts.check_learning_record import check_learning_record


def write_yaml(text: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="learning-record-")) / "record.yaml"
    tmp.write_text(text, encoding="utf-8")
    return tmp


def test_l2_record_requires_core_fields() -> None:
    record = write_yaml(
        """
learning_level: L2
learning_type: Technical
methods_used:
  - triangulation
input_inventory:
  - repo README
evidence_matrix:
  - claim_id: C1
    status: promoted
    evidence_ids: [S1]
value_judgment: Reusable controller pattern.
proof_boundary: Local architecture fit still needs implementation replay.
"""
    )

    assert check_learning_record(record) == []


def test_l3_record_requires_reconstruction_and_output_plan() -> None:
    record = write_yaml(
        """
learning_level: L3
learning_type: Company Case
methods_used:
  - case study research
  - process tracing
  - triangulation
input_inventory:
  - annual letters
research_reconstruction_model:
  object: Stripe
  time_span: "2010-2026"
evidence_matrix:
  - claim_id: C1
    status: promoted
    evidence_ids: [S1, S2]
value_judgment: Payment infrastructure capability accumulated over phases.
output_transformation_plan:
  article_intent_contract: Explain the company path.
proof_boundary: Future judgment remains bounded by available public sources.
"""
    )

    assert check_learning_record(record) == []


def test_l3_record_without_proof_boundary_fails() -> None:
    record = write_yaml(
        """
learning_level: L3
learning_type: Company Case
methods_used:
  - process tracing
input_inventory:
  - annual letters
research_reconstruction_model:
  object: Stripe
evidence_matrix:
  - claim_id: C1
    status: promoted
    evidence_ids: [S1]
value_judgment: Capability accumulated.
output_transformation_plan:
  article_intent_contract: Explain the path.
"""
    )

    messages = check_learning_record(record)

    assert "missing required field: proof_boundary" in messages
```

- [ ] **Step 2: Run tests and verify RED**

Run:

```bash
python3 -m pytest tests/test_learning_record_checker.py -q
```

Expected:

```text
FAILED
```

Failure reason should be import failure for `scripts.check_learning_record`.

- [ ] **Step 3: Implement minimal checker**

Create `scripts/check_learning_record.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

COMMON_REQUIRED = (
    "learning_level",
    "learning_type",
    "methods_used",
    "input_inventory",
    "evidence_matrix",
    "value_judgment",
    "proof_boundary",
)

L3_REQUIRED = (
    "research_reconstruction_model",
    "output_transformation_plan",
)


def load_record(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    return data


def check_learning_record(path: Path) -> list[str]:
    record = load_record(path)
    messages: list[str] = []

    for field in COMMON_REQUIRED:
        if not record.get(field):
            messages.append(f"missing required field: {field}")

    level = str(record.get("learning_level", "")).upper()
    if level == "L3":
        for field in L3_REQUIRED:
            if not record.get(field):
                messages.append(f"missing required field: {field}")

    evidence = record.get("evidence_matrix")
    if evidence is not None and not isinstance(evidence, list):
        messages.append("evidence_matrix must be a list")

    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a structured L2/L3 learning record.")
    parser.add_argument("path", help="YAML learning record path")
    args = parser.parse_args()

    messages = check_learning_record(Path(args.path))
    for message in messages:
        print(message)
    return 1 if messages else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests and verify GREEN**

Run:

```bash
python3 -m pytest tests/test_learning_record_checker.py -q
```

Expected:

```text
3 passed
```

- [ ] **Step 5: Add fixtures**

Create `scripts/examples/learning-record-l2-valid.yaml` using the valid L2 YAML from the first test.

Create `scripts/examples/learning-record-l3-missing-proof-boundary.yaml` using the invalid L3 YAML from the third test.

- [ ] **Step 6: Verify CLI fixture behavior**

Run:

```bash
python3 scripts/check_learning_record.py scripts/examples/learning-record-l2-valid.yaml
```

Expected: exit code `0` and no output.

Run:

```bash
python3 scripts/check_learning_record.py scripts/examples/learning-record-l3-missing-proof-boundary.yaml
```

Expected:

```text
missing required field: proof_boundary
```

- [ ] **Step 7: Commit checker**

Run:

```bash
git add tests/test_learning_record_checker.py scripts/check_learning_record.py scripts/examples/learning-record-l2-valid.yaml scripts/examples/learning-record-l3-missing-proof-boundary.yaml
git commit -m "Add learning record structure checker"
```

---

### Task 6: Complete Evaluation Evidence and Health Checks

**Files:**
- Modify: `openspec/changes/add-learning-workflow-matrix/evaluation.md`
- Modify: `openspec/changes/add-learning-workflow-matrix/tasks.md`

- [ ] **Step 1: Update GREEN result evidence**

Replace the planned command block under `## GREEN Result` in `openspec/changes/add-learning-workflow-matrix/evaluation.md` with observed evidence:

````markdown
## GREEN Result

Focused checks:

```bash
python3 -m pytest tests/test_learning_capture_consolidation.py tests/test_learning_record_checker.py -q
```

Expected:

```text
7 passed
```

Checker fixtures:

```bash
python3 scripts/check_learning_record.py scripts/examples/learning-record-l2-valid.yaml
python3 scripts/check_learning_record.py scripts/examples/learning-record-l3-missing-proof-boundary.yaml
```

Expected:

- L2 valid fixture exits `0`.
- L3 missing proof-boundary fixture exits `1` and prints `missing required field: proof_boundary`.

Behavior asset gate:

```bash
python3 scripts/check_behavior_assets.py
```

Expected:

```text
No behavior asset evaluation drift found.
```

Manual replay:

| Case | Result |
|---|---|
| positive technical OCR learning | GREEN: controller links levels, learning types, research methods, output contract |
| positive Stripe research | GREEN: L3 level, company-case type, source queue, evidence matrix, proof boundary references exist |
| positive public writing | GREEN: public-writing reference exists and stays after learning capture |
| positive governance workflow | GREEN: OpenSpec and behavior-asset promotion boundary remains explicit |
| negative should-not-trigger quick lookup | GREEN: existing no-learning rule remains |
| negative should-not-trigger raw fetch | GREEN: existing raw-fetch rule remains |
````

- [ ] **Step 2: Mark tasks complete only after checks actually pass**

Update `openspec/changes/add-learning-workflow-matrix/tasks.md` by changing each completed item from `- [ ]` to `- [x]` only after the corresponding command or file edit has finished.

- [ ] **Step 3: Run final focused checks**

Run:

```bash
python3 -m pytest tests/test_learning_capture_consolidation.py tests/test_learning_record_checker.py -q
python3 scripts/check_behavior_assets.py
python3 scripts/repo_health_check.py
git diff --check -- openspec/changes/add-learning-workflow-matrix .codex/skills/learning-capture tests/test_learning_capture_consolidation.py tests/test_learning_record_checker.py scripts/check_learning_record.py scripts/examples/learning-record-l2-valid.yaml scripts/examples/learning-record-l3-missing-proof-boundary.yaml
```

Expected:

- pytest passes.
- behavior asset checker reports no behavior drift, or unrelated blockers are copied into `evaluation.md`.
- repo health passes, or unrelated blockers are copied into `evaluation.md`.
- `git diff --check` is clean.

- [ ] **Step 4: Commit final evaluation evidence**

Run:

```bash
git add openspec/changes/add-learning-workflow-matrix/evaluation.md openspec/changes/add-learning-workflow-matrix/tasks.md
git commit -m "Record learning matrix verification evidence"
```

---

### Task 7: Final Scope Review

**Files:**
- Read: `openspec/changes/add-learning-workflow-matrix/proposal.md`
- Read: `openspec/changes/add-learning-workflow-matrix/design.md`
- Read: `openspec/changes/add-learning-workflow-matrix/tasks.md`
- Read: `openspec/changes/add-learning-workflow-matrix/evaluation.md`
- Read: `.codex/skills/learning-capture/SKILL.md`

- [ ] **Step 1: Confirm no out-of-scope files were staged**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected:

- Latest commit is `Record learning matrix verification evidence`.
- Any remaining dirty files are pre-existing unrelated files or explicitly excluded local junk.

- [ ] **Step 2: Confirm implementation did not bypass OpenSpec**

Run:

```bash
find openspec/changes/add-learning-workflow-matrix -maxdepth 3 -type f | sort
```

Expected:

```text
openspec/changes/add-learning-workflow-matrix/design.md
openspec/changes/add-learning-workflow-matrix/evaluation.md
openspec/changes/add-learning-workflow-matrix/proposal.md
openspec/changes/add-learning-workflow-matrix/specs/learning-capture/spec.md
openspec/changes/add-learning-workflow-matrix/tasks.md
```

- [ ] **Step 3: Stop at OpenSpec completion boundary**

If every checkbox in `openspec/changes/add-learning-workflow-matrix/tasks.md` is complete, stop implementation. The next default action is archive review, not immediate archive or adjacent cleanup.
