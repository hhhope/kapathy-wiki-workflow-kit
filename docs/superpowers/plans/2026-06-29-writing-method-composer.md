# Writing Method Composer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repo-local `writing-method-composer` controller that forces article-class work through a Writing Method Contract before learning, drafting, visual production, or public report gates.

**Architecture:** First create an OpenSpec change because this is repo workflow and semantic skill behavior. Then use TDD to add a YAML contract checker, publish one compact controller skill with registry references, add minimal integration text to `learning-capture` and `public-report-quality-gate`, and record behavior replay/evaluation evidence.

**Tech Stack:** Markdown behavior assets, OpenSpec change files, Python 3, PyYAML, pytest, existing repo behavior-asset checker.

---

## File Structure

Create:

- `openspec/changes/add-writing-method-composer/proposal.md` - lifecycle proposal and scope.
- `openspec/changes/add-writing-method-composer/design.md` - implementation design copied from the approved Superpowers spec into OpenSpec authority.
- `openspec/changes/add-writing-method-composer/tasks.md` - OpenSpec task checklist.
- `openspec/changes/add-writing-method-composer/evaluation.md` - RED/GREEN behavior evidence, prior-art dedupe, pressure scenarios.
- `openspec/changes/add-writing-method-composer/specs/writing-method-composer/spec.md` - durable requirements delta.
- `.codex/skills/writing-method-composer/SKILL.md` - compact runtime controller.
- `.codex/skills/writing-method-composer/references/writing-methodology-registry.md` - article/output method registry.
- `.codex/skills/writing-method-composer/references/analysis-framework-registry.md` - proof/thinking framework registry.
- `.codex/skills/writing-method-composer/references/expression-pattern-registry.md` - expression pattern registry.
- `.codex/skills/writing-method-composer/references/collaboration-mode-registry.md` - staged collaboration mode registry.
- `.codex/skills/writing-method-composer/references/contract-schema.md` - Writing Method Contract schema and examples.
- `.codex/skills/writing-method-composer/references/capability-ownership.md` - owner/delegate/reference boundaries.
- `.codex/skills/writing-method-composer/references/pressure-scenarios.md` - runtime pressure scenarios.
- `.codex/skills/writing-method-composer/evaluation.md` - skill-local pressure-test summary.
- `scripts/check_writing_method_contract.py` - deterministic YAML contract checker.
- `scripts/eval_writing_method_boundaries.py` - behavior asset boundary checker for description pollution and route ownership.
- `scripts/examples/writing-method-contract-valid.yaml` - positive checker fixture.
- `scripts/examples/writing-method-contract-invalid.yaml` - negative checker fixture.
- `tests/test_writing_method_contract.py` - checker unit tests.
- `tests/test_writing_method_boundaries.py` - boundary evaluator unit tests.

Modify:

- `.codex/skills/learning-capture/SKILL.md` - minimal upstream contract routing for article/share/report output targets.
- `.codex/skills/learning-capture/references/article.md` - distinguish article-as-input-source from article-as-output-target.
- `.codex/skills/learning-capture/references/output-contract.md` - allow `writing_method_contract_ref`.
- `.codex/skills/public-report-quality-gate/SKILL.md` - preserve outer gate while requiring the writing contract for complex article/H5/report composition.
- `openspec/changes/add-writing-method-composer/tasks.md` - mark tasks complete as execution progresses.
- `openspec/changes/add-writing-method-composer/evaluation.md` - append RED/GREEN and command output summaries.

Do not modify in this plan:

- `visual-agent`
- `knowledge-article-visual`
- `visual-knowledge-onepager`
- `interview-deep-reading-board`
- `material-collaboration-defaults`
- `product-discovery-wiki-capture`
- `khazix-writer`
- PM/business skill descriptions
- global files under `/home/yan/.codex/skills`

## Task 1: Create OpenSpec Change And RED Baseline

**Files:**
- Create: `openspec/changes/add-writing-method-composer/proposal.md`
- Create: `openspec/changes/add-writing-method-composer/design.md`
- Create: `openspec/changes/add-writing-method-composer/tasks.md`
- Create: `openspec/changes/add-writing-method-composer/evaluation.md`
- Create: `openspec/changes/add-writing-method-composer/specs/writing-method-composer/spec.md`

- [ ] **Step 1: Create the OpenSpec directories**

Run:

```bash
mkdir -p openspec/changes/add-writing-method-composer/specs/writing-method-composer
```

Expected: command exits `0`.

- [ ] **Step 2: Write `proposal.md`**

Create `openspec/changes/add-writing-method-composer/proposal.md` with:

```markdown
# Add Writing Method Composer

## Why

Article-class work currently starts too late in the workflow. The repository
has `learning-capture`, `public-report-quality-gate`, visual routing, and style
workers, but no upstream controller that decides what article or sharing
artifact is being made before learning and drafting begin.

This causes source summaries, framework stacking, unclear proof modules, and
reader-facing drafts whose evidence work does not match the intended output.

## What Changes

- Add `writing-method-composer` as a compact repo-local controller skill.
- Add method registries for writing methodology, analysis frameworks,
  expression patterns, and collaboration modes.
- Require a Writing Method Contract for article-class learning/drafting routes.
- Add Python checkers for contract structure and capability ownership.
- Add minimal integration wording in `learning-capture` and
  `public-report-quality-gate`.
- Add evaluation evidence with RED baseline, GREEN replay, prior-art dedupe,
  and residual risks.

## Out Of Scope

- No full writing agent runtime or state machine.
- No changes to `visual-agent`, `khazix-writer`, or PM/business skill
  descriptions.
- No automatic source fetching, citation verification, or article generation.
- No promotion of this Superpowers spec by itself into archive-ready state.
```

- [ ] **Step 3: Write `design.md`**

Create `openspec/changes/add-writing-method-composer/design.md` with:

```markdown
# Design

## Source

Accepted Superpowers design:
`docs/superpowers/specs/2026-06-29-writing-method-composer-design.md`.

## Architecture

Use one controller skill:

```text
writing-method-composer
  -> classify writing/output intent
  -> build Writing Method Contract
  -> validate contract
  -> route learning/search/writing/visual/report skills
```

The controller owns method composition only. It delegates learning depth and
source scoring to `learning-capture`, public output review to
`public-report-quality-gate`, visual routing to `visual-agent`, and prose style
execution to style workers such as `khazix-writer`.

## Runtime Contract

Every normal route exposes:

```text
- Using writing-method-composer
- Intent
- Target Artifact
- Reader Decision
- Mainline
- Proof Modules
- Analysis Frameworks
- Expression Frameworks
- Evidence Needs
- L0-L3 Learning Route
- Allowed Action
- Blocked Action
- Next Action
```

The hard artifact is a YAML Writing Method Contract. Proposed method choices are
not executable until structurally valid.

## Implementation Shape

- Keep `SKILL.md` compact.
- Put method definitions in `references/*`.
- Validate YAML contracts with `scripts/check_writing_method_contract.py`.
- Validate skill ownership wording with
  `scripts/eval_writing_method_boundaries.py`.
- Record behavior evidence in both the OpenSpec `evaluation.md` and
  `.codex/skills/writing-method-composer/evaluation.md`.

## Boundaries

Do not widen existing skill descriptions. Do not copy PM framework bodies into
the new registry. Registries may point to worker skills with
`delegates_to_skill`, but the worker remains the method body owner.
```

- [ ] **Step 4: Write `tasks.md`**

Create `openspec/changes/add-writing-method-composer/tasks.md` with:

```markdown
# Tasks

- [ ] Create OpenSpec proposal, design, spec delta, and RED evaluation baseline.
- [ ] Add failing tests for Writing Method Contract validation.
- [ ] Implement `scripts/check_writing_method_contract.py`.
- [ ] Add valid and invalid contract fixtures.
- [ ] Add failing tests for capability ownership and description pollution.
- [ ] Implement `scripts/eval_writing_method_boundaries.py`.
- [ ] Publish compact `writing-method-composer` skill and references.
- [ ] Integrate minimal routing text into `learning-capture`.
- [ ] Integrate minimal outer-gate text into `public-report-quality-gate`.
- [ ] Add skill-local evaluation evidence.
- [ ] Run focused pytest checks.
- [ ] Run behavior asset checker.
- [ ] Update OpenSpec evaluation with GREEN results and residual risks.
```

- [ ] **Step 5: Write RED baseline `evaluation.md`**

Create `openspec/changes/add-writing-method-composer/evaluation.md` with:

```markdown
# Evaluation

## RED Baseline

Before this change, the repository has no `writing-method-composer` skill, no
Writing Method Contract checker, and no controller-level owner for selecting
article methodology before learning or drafting.

Baseline failures expected before implementation:

- Bare link in a writing thread can route directly to summary or learning.
- Article/H5/report output targets can rely only on `learning-capture` public
  writing references after learning has already started.
- PM frameworks can be stacked without a named proof task.
- No checker can reject a proof module missing `proof_task`,
  `required_evidence`, or `proof_boundary`.
- No boundary checker can fail description pollution in the new controller.

## Pressure Scenarios

### Positive trigger: article-class method composition

Input: "我给你一个 Stripe 链接，帮我准备一篇分享稿，先告诉我要怎么学。"

Expected: route through `writing-method-composer`, ask or infer target artifact,
build a Writing Method Contract, assign L0-L3 per proof module, then delegate
research to `learning-capture`.

### Negative trigger: raw lookup

Input: "查一下 Stripe 最新估值。"

Expected: do not use `writing-method-composer`; this is lookup unless the user
turns it into article-class composition.

### Parent gate preservation

Input: "把这个复杂分析做成 H5 分享稿。"

Expected: `writing-method-composer` builds the contract; `public-report-quality-gate`
remains the outer reader-facing gate; `visual-agent` owns visual routing.

## Prior-Art / Common-Rule Dedupe

- `learning-capture` owns learning admission, source scoring, L0-L3 method
  details, and learning output contracts.
- `public-report-quality-gate` owns reader-facing publish/review gates.
- `visual-agent` owns visual route control.
- Existing PM/business skills own their full framework bodies.
- `writing-method-composer` owns only article-class method composition and the
  Writing Method Contract.

## GREEN Result

No GREEN result is recorded in the RED baseline. Add GREEN evidence only after
the checker, boundary evaluator, focused tests, and behavior asset check have
run in later tasks.

## Residual Risks

- The baseline records expected failures only.
- Future GREEN evidence must not be claimed from this baseline text.
- The checker will validate structure, not business judgment truth.
```

- [ ] **Step 6: Write spec delta**

Create `openspec/changes/add-writing-method-composer/specs/writing-method-composer/spec.md` with:

```markdown
# writing-method-composer Specification

## Requirements

### Requirement: Repository SHALL provide an article-method controller

The repository SHALL provide a compact repo-local skill named
`writing-method-composer` for article-class method composition before learning,
drafting, public report preparation, or visual production.

#### Scenario: User asks how to prepare an article-class output

- **WHEN** the user asks to prepare, structure, research, or compose an article,
  H5/share draft, long-form analysis, case analysis, PPT script, speech, or
  method article
- **THEN** the agent SHALL route through `writing-method-composer`
- **AND** the route SHALL identify target artifact, reader decision, mainline,
  proof modules, evidence needs, and next action before downstream execution

### Requirement: Writing Method Contract SHALL be structurally validated

The repository SHALL define a Writing Method Contract and a checker that
validates the minimum structure for article-class tasks.

#### Scenario: Contract lacks proof module evidence needs

- **WHEN** a Writing Method Contract contains an L2 or L3 proof module without
  `required_evidence` or `proof_boundary`
- **THEN** the checker SHALL fail
- **AND** the task SHALL NOT claim the contract is execution-ready

### Requirement: Frameworks SHALL attach to proof tasks

Analysis frameworks and expression patterns SHALL be attached to proof modules
with named proof tasks rather than listed as global decoration.

#### Scenario: Framework pile has no proof tasks

- **WHEN** a contract lists frameworks such as JTBD, SWOT, Five Forces, AB, or
  cohort analysis without a proof task
- **THEN** the checker SHALL fail or the skill SHALL reject the route as method
  stacking

### Requirement: Existing workflow owners SHALL remain authoritative

The writing-method controller SHALL not replace learning, public report,
visual, style, OpenSpec, or PM framework owners.

#### Scenario: Reader-facing H5 output

- **WHEN** the target artifact is a reader-facing H5/share draft
- **THEN** the Writing Method Contract SHALL identify downstream
  `public-report-quality-gate`
- **AND** visual production SHALL remain downstream of `visual-agent`
```

- [ ] **Step 7: Verify OpenSpec files are present**

Run:

```bash
find openspec/changes/add-writing-method-composer -type f | sort
```

Expected output includes exactly:

```text
openspec/changes/add-writing-method-composer/design.md
openspec/changes/add-writing-method-composer/evaluation.md
openspec/changes/add-writing-method-composer/proposal.md
openspec/changes/add-writing-method-composer/specs/writing-method-composer/spec.md
openspec/changes/add-writing-method-composer/tasks.md
```

- [ ] **Step 8: Commit OpenSpec skeleton**

Run:

```bash
git status --short
git add openspec/changes/add-writing-method-composer
git commit -m "Propose writing method composer"
```

Expected: commit includes only `openspec/changes/add-writing-method-composer/*`.

## Task 2: Add Contract Checker Tests First

**Files:**
- Create: `tests/test_writing_method_contract.py`

- [ ] **Step 1: Write failing checker tests**

Create `tests/test_writing_method_contract.py` with:

```python
from __future__ import annotations

import tempfile
from pathlib import Path

from scripts.check_writing_method_contract import check_writing_method_contract


def write_yaml(text: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="writing-method-contract-")) / "contract.yaml"
    tmp.write_text(text, encoding="utf-8")
    return tmp


def test_valid_contract_passes() -> None:
    contract = write_yaml(
        """
target_artifact:
  kind: h5_share
  audience: product leaders
  delivery_surface: h5
reader_decision:
  reader_needs_to_understand_or_decide: Decide why transaction infrastructure changes in the AI era.
  non_goals:
    - produce final copy
mainline:
  question: How is the transaction system changing?
  thesis: AI shifts transaction systems from payment endpoints to programmable control planes.
  reader_takeaway: Evaluate Stripe as one company case, not the whole market.
  primary_frameworks:
    - company_evolution_case
proof_modules:
  - module_id: company_path
    article_position: body
    proof_task: Show how product and API capability accumulated over time.
    analysis_frameworks:
      - process_tracing
      - source_layering
    expression_frameworks:
      - timeline
    required_evidence:
      - annual letters
      - product docs
      - API docs
    l_level: L3
    proof_boundary: Future judgment remains bounded by public sources.
source_roles:
  content_sources:
    - user brief
  evidence_sources:
    - official docs
  style_references: []
  excluded_sources: []
collaboration_mode:
  id: research_outline_review_draft
  stages:
    - contract
    - research
    - outline_review
quality_gates:
  required_checkers:
    - check_writing_method_contract
  downstream_gates:
    - public-report-quality-gate
    - visual-agent
"""
    )

    assert check_writing_method_contract(contract) == []


def test_missing_reader_decision_fails() -> None:
    contract = write_yaml(
        """
target_artifact:
  kind: longform_article
  audience: founders
  delivery_surface: markdown
mainline:
  question: Why does this matter?
  thesis: It changes the workflow.
proof_modules:
  - module_id: module_a
    proof_task: Prove the user need.
    analysis_frameworks: [jtbd]
    expression_frameworks: [concrete_event_opening]
    required_evidence: [user scenario]
    l_level: L2
    proof_boundary: Needs more source evidence.
"""
    )

    messages = check_writing_method_contract(contract)

    assert "missing required field: reader_decision.reader_needs_to_understand_or_decide" in messages


def test_l2_module_without_evidence_and_boundary_fails() -> None:
    contract = write_yaml(
        """
target_artifact:
  kind: deep_report
  audience: operators
  delivery_surface: markdown
reader_decision:
  reader_needs_to_understand_or_decide: Decide whether the trend is real.
mainline:
  question: Is the trend real?
  thesis: It is early but visible.
proof_modules:
  - module_id: evidence
    proof_task: Prove the trend has market evidence.
    analysis_frameworks: [market_sizing]
    expression_frameworks: [contrast_table]
    l_level: L2
"""
    )

    messages = check_writing_method_contract(contract)

    assert "proof_modules[0] missing required field: required_evidence" in messages
    assert "proof_modules[0] missing required field: proof_boundary" in messages


def test_framework_without_proof_task_fails() -> None:
    contract = write_yaml(
        """
target_artifact:
  kind: longform_article
  audience: product team
  delivery_surface: markdown
reader_decision:
  reader_needs_to_understand_or_decide: Understand customer need.
mainline:
  question: What does the customer need?
  thesis: The job is underserved.
proof_modules:
  - module_id: need
    analysis_frameworks: [jtbd, swot]
    expression_frameworks: [concrete_event_opening]
    required_evidence: [customer scenario]
    l_level: L1
    proof_boundary: Internal example only.
"""
    )

    messages = check_writing_method_contract(contract)

    assert "proof_modules[0] missing required field: proof_task" in messages
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
pytest tests/test_writing_method_contract.py -q
```

Expected: FAIL during import with:

```text
ModuleNotFoundError: No module named 'scripts.check_writing_method_contract'
```

- [ ] **Step 3: Commit RED test**

Run:

```bash
git status --short
git add tests/test_writing_method_contract.py
git commit -m "Test writing method contract checker"
```

Expected: commit includes only `tests/test_writing_method_contract.py`.

## Task 3: Implement Contract Checker And Fixtures

**Files:**
- Create: `scripts/check_writing_method_contract.py`
- Create: `scripts/examples/writing-method-contract-valid.yaml`
- Create: `scripts/examples/writing-method-contract-invalid.yaml`
- Modify: `openspec/changes/add-writing-method-composer/evaluation.md`
- Modify: `openspec/changes/add-writing-method-composer/tasks.md`

- [ ] **Step 1: Implement checker**

Create `scripts/check_writing_method_contract.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml


TOP_LEVEL_REQUIRED = (
    "target_artifact",
    "reader_decision",
    "mainline",
    "proof_modules",
)

NESTED_REQUIRED = (
    ("target_artifact", "kind"),
    ("target_artifact", "audience"),
    ("target_artifact", "delivery_surface"),
    ("reader_decision", "reader_needs_to_understand_or_decide"),
    ("mainline", "question"),
    ("mainline", "thesis"),
)

PROOF_MODULE_REQUIRED = (
    "module_id",
    "proof_task",
    "analysis_frameworks",
    "expression_frameworks",
    "required_evidence",
    "l_level",
    "proof_boundary",
)

L_LEVELS = {"L0", "L1", "L2", "L3"}


def load_contract(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    return data


def _missing(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


def _list_field(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)


def check_writing_method_contract(path: Path) -> list[str]:
    contract = load_contract(path)
    messages: list[str] = []

    for field in TOP_LEVEL_REQUIRED:
        if _missing(contract.get(field)):
            messages.append(f"missing required field: {field}")

    for parent, child in NESTED_REQUIRED:
        value = contract.get(parent)
        if not isinstance(value, dict) or _missing(value.get(child)):
            messages.append(f"missing required field: {parent}.{child}")

    proof_modules = contract.get("proof_modules")
    if proof_modules is None:
        return messages
    if not isinstance(proof_modules, list):
        messages.append("proof_modules must be a list")
        return messages
    if not proof_modules:
        messages.append("proof_modules must contain at least one module")
        return messages

    for index, module in enumerate(proof_modules):
        prefix = f"proof_modules[{index}]"
        if not isinstance(module, dict):
            messages.append(f"{prefix} must be a mapping")
            continue
        for field in PROOF_MODULE_REQUIRED:
            if _missing(module.get(field)):
                messages.append(f"{prefix} missing required field: {field}")

        l_level = str(module.get("l_level", "")).upper()
        if l_level and l_level not in L_LEVELS:
            messages.append(f"{prefix} l_level must be one of L0, L1, L2, L3")

        for list_field in ("analysis_frameworks", "expression_frameworks", "required_evidence"):
            value = module.get(list_field)
            if value is not None and not _list_field(value):
                messages.append(f"{prefix}.{list_field} must be a list of strings")

    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Writing Method Contract YAML file.")
    parser.add_argument("path", help="Writing Method Contract YAML path")
    args = parser.parse_args()

    messages = check_writing_method_contract(Path(args.path))
    for message in messages:
        print(message)
    return 1 if messages else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Add valid fixture**

Create `scripts/examples/writing-method-contract-valid.yaml` with the same YAML body from `test_valid_contract_passes`.

- [ ] **Step 3: Add invalid fixture**

Create `scripts/examples/writing-method-contract-invalid.yaml` with:

```yaml
target_artifact:
  kind: deep_report
  audience: operators
  delivery_surface: markdown
reader_decision:
  reader_needs_to_understand_or_decide: Decide whether the trend is real.
mainline:
  question: Is the trend real?
  thesis: It is early but visible.
proof_modules:
  - module_id: evidence
    analysis_frameworks: [market_sizing]
    expression_frameworks: [contrast_table]
    l_level: L2
```

- [ ] **Step 4: Run focused tests**

Run:

```bash
pytest tests/test_writing_method_contract.py -q
```

Expected:

```text
4 passed
```

- [ ] **Step 5: Run checker manually**

Run:

```bash
python3 scripts/check_writing_method_contract.py scripts/examples/writing-method-contract-valid.yaml
python3 scripts/check_writing_method_contract.py scripts/examples/writing-method-contract-invalid.yaml
```

Expected:

```text
# first command exits 0 with no output
# second command exits 1 and prints missing proof_task, required_evidence, proof_boundary
```

- [ ] **Step 6: Update OpenSpec task/evaluation**

In `openspec/changes/add-writing-method-composer/tasks.md`, check:

```markdown
- [x] Add failing tests for Writing Method Contract validation.
- [x] Implement `scripts/check_writing_method_contract.py`.
- [x] Add valid and invalid contract fixtures.
```

In `openspec/changes/add-writing-method-composer/evaluation.md`, replace `## GREEN Result` with:

```markdown
## GREEN Result

Contract checker evidence:

- `pytest tests/test_writing_method_contract.py -q` passed.
- Valid fixture exits `0` with no output.
- Invalid fixture exits `1` and reports missing proof module fields.
```

- [ ] **Step 7: Commit checker**

Run:

```bash
git status --short
git add scripts/check_writing_method_contract.py scripts/examples/writing-method-contract-valid.yaml scripts/examples/writing-method-contract-invalid.yaml tests/test_writing_method_contract.py openspec/changes/add-writing-method-composer/tasks.md openspec/changes/add-writing-method-composer/evaluation.md
git commit -m "Add writing method contract checker"
```

Expected: commit includes only checker, fixtures, test, and OpenSpec evidence updates.

## Task 4: Add Boundary Evaluator Tests And Implementation

**Files:**
- Create: `tests/test_writing_method_boundaries.py`
- Create: `scripts/eval_writing_method_boundaries.py`
- Modify: `openspec/changes/add-writing-method-composer/evaluation.md`
- Modify: `openspec/changes/add-writing-method-composer/tasks.md`

- [ ] **Step 1: Write failing boundary tests**

Create `tests/test_writing_method_boundaries.py` with:

```python
from __future__ import annotations

import tempfile
from pathlib import Path

from scripts.eval_writing_method_boundaries import check_skill_description, check_registry_entry


def test_clean_description_passes() -> None:
    description = (
        "Use when choosing article methodology, proof modules, thinking frameworks, "
        "expression patterns, and a Writing Method Contract before drafting."
    )

    assert check_skill_description(description) == []


def test_polluted_description_fails() -> None:
    description = "Use for all H5 reports PPT public materials learning visuals and PM analysis."

    messages = check_skill_description(description)

    assert "description claims broad output ownership: H5" in messages
    assert "description claims broad output ownership: visuals" in messages


def test_registry_entry_must_not_copy_worker_body() -> None:
    entry = {
        "id": "market_sizing",
        "type": "analysis_framework",
        "use_when": "Need market size.",
        "proves": "Opportunity scale.",
        "required_evidence": ["market data"],
        "article_use": "proof_module",
        "delegates_to_skill": "market-sizing",
        "full_method_body": "TAM SAM SOM full copied method",
    }

    messages = check_registry_entry(entry)

    assert "registry entry must delegate instead of copying full_method_body" in messages
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
pytest tests/test_writing_method_boundaries.py -q
```

Expected: FAIL during import with:

```text
ModuleNotFoundError: No module named 'scripts.eval_writing_method_boundaries'
```

- [ ] **Step 3: Implement boundary evaluator**

Create `scripts/eval_writing_method_boundaries.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


BROAD_OWNERSHIP_TERMS = (
    "H5",
    "reports",
    "PPT",
    "public materials",
    "learning",
    "visuals",
    "PM analysis",
)


def check_skill_description(description: str) -> list[str]:
    messages: list[str] = []
    lowered = description.lower()
    for term in BROAD_OWNERSHIP_TERMS:
        if term.lower() in lowered:
            messages.append(f"description claims broad output ownership: {term}")
    return messages


def check_registry_entry(entry: dict[str, Any]) -> list[str]:
    messages: list[str] = []
    if entry.get("full_method_body"):
        messages.append("registry entry must delegate instead of copying full_method_body")
    if entry.get("delegates_to_skill") and not entry.get("article_use"):
        messages.append("delegated registry entry must still define article_use")
    return messages


def extract_description(skill_text: str) -> str:
    match = re.search(r"^description:\s*(.+)$", skill_text, flags=re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip().strip('"')


def check_skill_file(path: Path) -> list[str]:
    return check_skill_description(extract_description(path.read_text(encoding="utf-8")))


def check_registry_file(path: Path) -> list[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        return []
    messages: list[str] = []
    for index, entry in enumerate(data):
        if isinstance(entry, dict):
            for message in check_registry_entry(entry):
                messages.append(f"{path}:{index}: {message}")
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate writing-method-composer ownership boundaries.")
    parser.add_argument("--skill", help="Path to writing-method-composer SKILL.md")
    parser.add_argument("--registry", action="append", default=[], help="Registry YAML path")
    args = parser.parse_args()

    messages: list[str] = []
    if args.skill:
        messages.extend(check_skill_file(Path(args.skill)))
    for registry in args.registry:
        messages.extend(check_registry_file(Path(registry)))

    for message in messages:
        print(message)
    return 1 if messages else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run boundary tests**

Run:

```bash
pytest tests/test_writing_method_boundaries.py -q
```

Expected:

```text
3 passed
```

- [ ] **Step 5: Update OpenSpec evidence**

In `openspec/changes/add-writing-method-composer/tasks.md`, check:

```markdown
- [x] Add failing tests for capability ownership and description pollution.
- [x] Implement `scripts/eval_writing_method_boundaries.py`.
```

Append to `openspec/changes/add-writing-method-composer/evaluation.md`:

```markdown
Boundary evaluator evidence:

- `pytest tests/test_writing_method_boundaries.py -q` passed.
- Polluted descriptions that claim all H5/report/PPT/learning/visual/PM work fail.
- Registry entries with copied `full_method_body` fail.
```

- [ ] **Step 6: Commit boundary evaluator**

Run:

```bash
git status --short
git add scripts/eval_writing_method_boundaries.py tests/test_writing_method_boundaries.py openspec/changes/add-writing-method-composer/tasks.md openspec/changes/add-writing-method-composer/evaluation.md
git commit -m "Add writing method boundary checks"
```

Expected: commit includes only evaluator, test, and OpenSpec evidence updates.

## Task 5: Publish `writing-method-composer` Skill And References

**Files:**
- Create: `.codex/skills/writing-method-composer/SKILL.md`
- Create: `.codex/skills/writing-method-composer/references/writing-methodology-registry.md`
- Create: `.codex/skills/writing-method-composer/references/analysis-framework-registry.md`
- Create: `.codex/skills/writing-method-composer/references/expression-pattern-registry.md`
- Create: `.codex/skills/writing-method-composer/references/collaboration-mode-registry.md`
- Create: `.codex/skills/writing-method-composer/references/contract-schema.md`
- Create: `.codex/skills/writing-method-composer/references/capability-ownership.md`
- Create: `.codex/skills/writing-method-composer/references/pressure-scenarios.md`
- Create: `.codex/skills/writing-method-composer/evaluation.md`
- Modify: `openspec/changes/add-writing-method-composer/tasks.md`

- [ ] **Step 1: Create skill directory**

Run:

```bash
mkdir -p .codex/skills/writing-method-composer/references
```

Expected: command exits `0`.

- [ ] **Step 2: Write compact `SKILL.md`**

Create `.codex/skills/writing-method-composer/SKILL.md` with:

```markdown
---
name: writing-method-composer
description: Use when choosing article methodology, proof modules, analysis frameworks, expression patterns, and a Writing Method Contract before article-class learning or drafting.
---

# Writing Method Composer

Use this skill as the controller for article-class method composition before
learning execution, drafting, public report preparation, or visual routing.

## Trigger

Use when the user asks to prepare, structure, research, or compose an article,
H5/share draft, long-form analysis, case analysis, PPT script, speech, or
method article and the method of writing or learning is not already fixed.

If the user only gives a link or topic and the target artifact is unclear, ask
for or infer the target artifact before summary, durable learning capture, or
drafting.

## Required Route Block

Every normal run must show:

```text
- Using writing-method-composer
- Intent
- Target Artifact
- Reader Decision
- Mainline
- Proof Modules
- Analysis Frameworks
- Expression Frameworks
- Evidence Needs
- L0-L3 Learning Route
- Allowed Action
- Blocked Action
- Next Action
```

## Hard Rules

- Build or update a Writing Method Contract before downstream article-class
  learning or drafting.
- Keep one mainline. Complex work may have multiple proof modules, but every
  module must name its proof task.
- Attach analysis frameworks and expression patterns to proof modules, not to a
  global decoration list.
- Assign L0-L3 learning depth per proof module.
- Use registries as method references; do not copy worker skill method bodies.
- Preserve downstream owners: `learning-capture` for learning, `public-report-quality-gate`
  for reader-facing output, `visual-agent` for visual routing, and style
  workers for prose execution.

## Load

- Contract schema: `references/contract-schema.md`
- Writing methods: `references/writing-methodology-registry.md`
- Analysis frameworks: `references/analysis-framework-registry.md`
- Expression patterns: `references/expression-pattern-registry.md`
- Collaboration modes: `references/collaboration-mode-registry.md`
- Capability ownership: `references/capability-ownership.md`
- Pressure scenarios: `references/pressure-scenarios.md`

## Common Mistakes

- Starting with a source summary before deciding the target artifact.
- Listing JTBD, SWOT, Five Forces, AB, or cohort analysis without a proof task.
- Treating learning notes as publish-ready article structure.
- Replacing `public-report-quality-gate` or `visual-agent` instead of routing to them.
```

- [ ] **Step 3: Write `contract-schema.md`**

Create `.codex/skills/writing-method-composer/references/contract-schema.md` using the YAML schema from the approved Superpowers design, including all fields under `target_artifact`, `reader_decision`, `mainline`, `proof_modules`, `source_roles`, `collaboration_mode`, and `quality_gates`.

- [ ] **Step 4: Write registry files**

Create each registry with concrete starter entries:

`writing-methodology-registry.md` includes:

```markdown
# Writing Methodology Registry

## company_evolution_case

- use_when: The article explains how a company, product, or organization
  reached its current position.
- mainline_shape: "How did the object evolve, what capability accumulated, and
  what judgment should the reader take away?"
- typical_proof_modules: company path, capability accumulation, market context,
  evidence boundary.
- required_reader_decision: Understand whether the case proves a broader trend
  or only the object itself.
- failure_modes: chronology without judgment; company praise without evidence;
  future claims without proof boundary.

## trend_report

- use_when: The article argues that a market, workflow, or technology is
  changing.
- mainline_shape: "What changed, why now, what evidence proves it, and what
  should the reader do with the trend?"
- typical_proof_modules: trigger, pressure, evidence, counterexample, implication.
- required_reader_decision: Decide whether the trend is real and relevant.
- failure_modes: examples without trend mechanism; speculation without evidence.
```

`analysis-framework-registry.md` includes entries for `jtbd`, `market_sizing`,
`process_tracing`, `source_layering`, `people_background_mapping`,
`ab_validation`, and `cohort_analysis`.

`expression-pattern-registry.md` includes entries for `concrete_event_opening`,
`timeline`, `contrast_table`, `layered_reveal`, and `callback`.

`collaboration-mode-registry.md` includes entries for
`research_outline_review_draft`, `link_intake_contract_first`, and
`h5_share_contract_visual_route`.

- [ ] **Step 5: Write ownership and pressure references**

Create `capability-ownership.md` with:

```markdown
# Capability Ownership

`writing-method-composer` owns method composition and the Writing Method
Contract. It does not own learning capture, public report gates, visual
production, prose style execution, PM framework bodies, or OpenSpec lifecycle.

One behavior owner per capability. Other skills may reference or delegate only.
```

Create `pressure-scenarios.md` with the scenarios from OpenSpec evaluation:
bare link, company case, short article, H5/share, framework pile, people
background, AB/cohort, duplicate capability.

- [ ] **Step 6: Write skill-local evaluation**

Create `.codex/skills/writing-method-composer/evaluation.md` with:

```markdown
# Evaluation

## Pressure Scenarios

- Positive trigger: article-class method composition.
- Negative trigger: raw lookup.
- Parent gate preservation: H5/share route keeps public report and visual gates.
- Framework pile rejection: frameworks without proof tasks fail.

## RED Baseline

Before this skill, no repo-local controller produced a Writing Method Contract.

## GREEN Result

No GREEN result is recorded at skill publication time. Add GREEN evidence only
after the focused tests and behavior asset check have run.

## Residual Risks

Future agents must still load this skill; checker validates structure, not the
truth of business judgment.
```

- [ ] **Step 7: Run boundary evaluator on the new skill**

Run:

```bash
python3 scripts/eval_writing_method_boundaries.py --skill .codex/skills/writing-method-composer/SKILL.md
```

Expected: exits `0` with no output.

- [ ] **Step 8: Update tasks and commit**

In `openspec/changes/add-writing-method-composer/tasks.md`, check:

```markdown
- [x] Publish compact `writing-method-composer` skill and references.
```

Run:

```bash
git status --short
git add .codex/skills/writing-method-composer openspec/changes/add-writing-method-composer/tasks.md
git commit -m "Add writing method composer skill"
```

Expected: commit includes only new skill files and tasks update.

## Task 6: Integrate Minimal Routing Into Existing Skills

**Files:**
- Modify: `.codex/skills/learning-capture/SKILL.md`
- Modify: `.codex/skills/learning-capture/references/article.md`
- Modify: `.codex/skills/learning-capture/references/output-contract.md`
- Modify: `.codex/skills/public-report-quality-gate/SKILL.md`
- Modify: `openspec/changes/add-writing-method-composer/tasks.md`

- [ ] **Step 1: Update `learning-capture/SKILL.md` minimally**

In `.codex/skills/learning-capture/SKILL.md`, replace the current reader-facing routing bullet:

```markdown
5. For reader-facing articles, H5, PPT, or public reports, load
   `references/public-writing-method.md` after learning capture; do not treat
   learning notes as publish-ready output.
```

with:

```markdown
5. For reader-facing articles, H5, PPT, sharing scripts, or public reports where
   the target artifact is the reason for learning, route through
   `writing-method-composer` before L2/L3 learning execution. The Writing
   Method Contract decides which proof modules need L0-L3 learning. Keep
   `references/public-writing-method.md` for learning-to-output handoff context;
   do not treat learning notes as publish-ready output.
```

- [ ] **Step 2: Update `article.md` boundary**

Append this section to `.codex/skills/learning-capture/references/article.md`:

```markdown
## Article As Input vs Output Target

Article-shaped sources are input evidence. Article-class deliverables are output
targets. If the user provides an article link and asks to learn from it, this
module owns source grounding and learning capture. If the user asks to write,
prepare, structure, or research an article/H5/share/PPT artifact, route first
through `writing-method-composer` so the target artifact determines the proof
modules and L0-L3 learning route.
```

- [ ] **Step 3: Update `output-contract.md`**

Append this field description to `.codex/skills/learning-capture/references/output-contract.md`:

```markdown
## Optional Writing Method Contract Reference

For article-class learning driven by a target output, include:

```yaml
writing_method_contract_ref: path-or-inline-contract-id
```

This reference identifies the upstream Writing Method Contract that selected
the proof modules and L0-L3 learning depth. It does not replace the learning
record's evidence matrix or proof boundary.
```

- [ ] **Step 4: Update `public-report-quality-gate/SKILL.md` minimally**

In the delegation map, add this row after `source or reference learning`:

```markdown
| article-class method composition before complex article/H5/report drafting | `writing-method-composer` |
```

In Hard Rules, add after the Article Intent Contract rule:

```markdown
- For complex article-class outputs where the writing method, proof modules,
  evidence search, or L0-L3 learning route is not already fixed, require a
  Writing Method Contract from `writing-method-composer` before drafting. This
  contract does not replace this gate's Article Intent Contract, judgment
  ownership, citation surface, visual gate, or publish gate.
```

- [ ] **Step 5: Run focused boundary checks**

Run:

```bash
python3 scripts/eval_writing_method_boundaries.py --skill .codex/skills/writing-method-composer/SKILL.md
pytest tests/test_writing_method_contract.py tests/test_writing_method_boundaries.py -q
```

Expected:

```text
# boundary command exits 0
7 passed
```

- [ ] **Step 6: Update tasks and commit**

In `openspec/changes/add-writing-method-composer/tasks.md`, check:

```markdown
- [x] Integrate minimal routing text into `learning-capture`.
- [x] Integrate minimal outer-gate text into `public-report-quality-gate`.
```

Run:

```bash
git status --short
git add .codex/skills/learning-capture/SKILL.md .codex/skills/learning-capture/references/article.md .codex/skills/learning-capture/references/output-contract.md .codex/skills/public-report-quality-gate/SKILL.md openspec/changes/add-writing-method-composer/tasks.md
git commit -m "Route article methods through writing composer"
```

Expected: commit includes only the four skill/reference edits and tasks update.

## Task 7: Final Evaluation And Behavior Asset Checks

**Files:**
- Modify: `openspec/changes/add-writing-method-composer/evaluation.md`
- Modify: `openspec/changes/add-writing-method-composer/tasks.md`
- Modify: `.codex/skills/writing-method-composer/evaluation.md`

- [ ] **Step 1: Run focused tests**

Run:

```bash
pytest tests/test_writing_method_contract.py tests/test_writing_method_boundaries.py -q
```

Expected:

```text
7 passed
```

- [ ] **Step 2: Run contract fixtures**

Run:

```bash
python3 scripts/check_writing_method_contract.py scripts/examples/writing-method-contract-valid.yaml
python3 scripts/check_writing_method_contract.py scripts/examples/writing-method-contract-invalid.yaml
```

Expected:

```text
# first command exits 0 with no output
# second command exits 1 with missing proof module fields
```

- [ ] **Step 3: Run boundary evaluator**

Run:

```bash
python3 scripts/eval_writing_method_boundaries.py --skill .codex/skills/writing-method-composer/SKILL.md
```

Expected: exits `0` with no output.

- [ ] **Step 4: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: exits according to current repo baseline. If it returns non-zero for
unrelated existing active changes, copy the relevant output summary into
`openspec/changes/add-writing-method-composer/evaluation.md` and mark it as
residual repo baseline, not as this change passing silently.

- [ ] **Step 5: Update OpenSpec evaluation**

Update `openspec/changes/add-writing-method-composer/evaluation.md` so it contains:

```markdown
## GREEN Result

- Contract checker tests passed.
- Boundary evaluator tests passed.
- Valid fixture passed and invalid fixture failed with expected messages.
- `writing-method-composer` description passed the boundary evaluator.
- Behavior asset checker result recorded below.

## Behavior Asset Check

Command: `python3 scripts/check_behavior_assets.py`

Record one of these exact result shapes after running the command:

- `Result: passed with exit code 0.`
- `Result: failed with exit code 1. Existing unrelated repo baseline issues were reported; this change's paths were not identified as missing evaluation or prior-art evidence.`
- `Result: failed with exit code 1. This change was identified; fix the listed issue before continuing.`

## Residual Risks

- The checker validates structure, not the truth of business or market judgment.
- Future runtime behavior still depends on agents loading the correct skill.
- Broader weak PM/business skills are not repaired in this change; they remain
  delegated workers or future capability debt.
```

Update `.codex/skills/writing-method-composer/evaluation.md` with the same GREEN summary.

- [ ] **Step 6: Complete OpenSpec tasks**

In `openspec/changes/add-writing-method-composer/tasks.md`, check:

```markdown
- [x] Add skill-local evaluation evidence.
- [x] Run focused pytest checks.
- [x] Run behavior asset checker.
- [x] Update OpenSpec evaluation with GREEN results and residual risks.
```

- [ ] **Step 7: Commit final evaluation**

Run:

```bash
git status --short
git add openspec/changes/add-writing-method-composer/evaluation.md openspec/changes/add-writing-method-composer/tasks.md .codex/skills/writing-method-composer/evaluation.md
git commit -m "Evaluate writing method composer"
```

Expected: commit includes only evaluation/task evidence files.

## Task 8: Stop At OpenSpec Completion Boundary

**Files:**
- Read: `openspec/changes/add-writing-method-composer/tasks.md`
- Read: `openspec/changes/add-writing-method-composer/evaluation.md`

- [ ] **Step 1: Verify task completion**

Run:

```bash
rg -n "\[ \]" openspec/changes/add-writing-method-composer/tasks.md
```

Expected: no output.

- [ ] **Step 2: Verify latest commit and worktree**

Run:

```bash
git log -1 --oneline
git status --short
```

Expected: latest commit is the final evaluation commit. Worktree may still show
unrelated user changes; do not claim clean unless it is actually clean.

- [ ] **Step 3: Stop implementation**

Do not archive. Do not continue into adjacent skill cleanup. Report:

```text
OpenSpec implementation tasks are complete for add-writing-method-composer.
Next default action is archive review, not immediate archive or additional cleanup.
```
