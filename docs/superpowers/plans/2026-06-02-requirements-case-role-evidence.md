# Requirements Case Role Evidence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Strengthen `req-agent` requirements readiness by using case-local role instances, strict `role_ref` checks, and object-aware evidence anchors.

**Architecture:** Keep `RequirementCase` as the workflow state and keep `requirements/config/requirements-taxonomy.yaml` as the vocabulary authority. Add strict checker behavior for OpenSpec handoff, while preserving compatibility mode for legacy case files. Migrate only `embedded-account-phase1` as the golden sample.

**Tech Stack:** Python 3 standard library, `unittest`, YAML via existing scripts, OpenSpec CLI.

---

## File Structure

- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/proposal.md`
  - OpenSpec proposal for the workflow behavior change.
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/design.md`
  - Authoritative implementation design copied from the approved Superpowers spec, adjusted to OpenSpec lifecycle language.
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md`
  - OpenSpec implementation checklist.
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/specs/requirements-analysis-agent/spec.md`
  - Requirements that make role instances, strict checking, and evidence anchors lifecycle-owned.
- Modify: `tests/test_requirements_checker_gate.py`
  - Add RED tests for strict role/evidence gates and compatibility mode.
- Modify: `tests/test_requirements_analysis_agent.py`
  - Update ready-case fixtures to strict role instance shape and assert draft handoff blocks candidate roles.
- Modify: `scripts/check_requirements_case.py`
  - Add evidence anchor helper, role instance normalization, strict mode, compatibility mode, and richer blockers.
- Modify: `scripts/requirements_case.py`
  - Render role instances, `role_ref`, and evidence anchors in markdown summaries without breaking legacy machine data.
- Modify: `scripts/requirements_analysis_agent.py`
  - Generate role instances and keep unknown actors as `candidate_pending`.
- Modify: `scripts/requirements_openspec_draft.py`
  - Require strict checker pass before draft creation and preserve traceability.
- Modify: `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`
  - Migrate this single case as the golden sample.
- Optional Modify: `.codex/skills/req-agent/SKILL.md`, `.codex/skills/req-scope/SKILL.md`, `.codex/skills/req-stories/SKILL.md`, `.codex/skills/req-acceptance/SKILL.md`, `.codex/skills/req-handoff/SKILL.md`
  - Only if implementation changes user-visible routing language. If changed, add behavior-asset evaluation evidence.

## Task 1: Create OpenSpec Change

**Files:**
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/proposal.md`
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/design.md`
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md`
- Create: `openspec/changes/strengthen-requirements-role-evidence-gate/specs/requirements-analysis-agent/spec.md`

- [ ] **Step 1: Write proposal**

Create `openspec/changes/strengthen-requirements-role-evidence-gate/proposal.md`:

```markdown
# strengthen-requirements-role-evidence-gate

## Why

The current requirements checker can mark a case ready when user stories refer
only to taxonomy buckets such as `system_actor`. A real pressure test with
`embedded-account-phase1` showed that this hides which case-local actor performs
the behavior. The same pressure test showed that evidence must be enforced by a
traceable anchor contract, not by one mandatory field name.

## What Changes

- Add case-local role instances with `status` and `confirmed_as`.
- Require strict `role_ref` from user stories to confirmed role instances for
  OpenSpec handoff.
- Add object-aware evidence anchor validation.
- Preserve compatibility reading for legacy cases.
- Migrate only `embedded-account-phase1` as the golden sample.

## Out Of Scope

- No requirements taxonomy changes.
- No wiki frontmatter taxonomy changes.
- No batch migration of historical requirements cases.
- No weights, RAG, embeddings, cross-case entity merge, or full knowledge graph.
```

- [ ] **Step 2: Write design**

Create `openspec/changes/strengthen-requirements-role-evidence-gate/design.md`:

````markdown
# Design

## Model

`RequirementCase` remains the workflow state. The taxonomy remains the
vocabulary. The checker remains the readiness gate.

Roles become case-local role instances:

```yaml
roles:
  - id: R-embedded-account-front
    mention: 嵌入式账户前置
    confirmed_as: system_actor
    status: confirmed
    category: system_actors
    source_actors:
      - 嵌入式账户前置
    evidence_anchor:
      source_section: "5.1 参与角色/系统"
```

User stories reference role instances:

```yaml
user_stories:
  - id: US-006
    role_ref: R-embedded-account-front
    want: 按已绑卡优先级轮询发起快捷支付
    benefit: 高优先级卡明确失败后继续尝试低优先级卡
    acceptance_function_ids:
      - AF-012
    evidence_anchor:
      source_functions:
        - F-006
```

Acceptance functions can use existing source anchors:

```yaml
acceptance_functions:
  - id: AF-014
    source_acceptance: AC-014
    source_functions:
      - F-006
      - F-007
    user_story_ids:
      - US-006
      - US-007
    then: 当前卡支付结果未明时，系统先查单，不直接切下一张卡。
```

## Evidence Anchors

The checker uses `has_evidence_anchor(item, object_type)`.

Common anchors:

- `evidence_refs`
- `evidence_anchor`
- `source_section`
- `source_quote`
- `source_line`

Object-specific anchors:

- UserStory: `source_functions`
- AcceptanceFunction: `source_acceptance`, `source_functions`
- Role: `source_actors` plus `normalization_note`, with `evidence_anchor`
  preferred for new cases

## Checker Modes

Strict mode is required for OpenSpec handoff. Compatibility mode lets legacy
case files remain readable.

Strict mode blocks:

- story has no `role_ref`
- `role_ref` points to a missing role
- `role_ref` points to non-confirmed role
- referenced role's `confirmed_as` does not map to taxonomy
- story or acceptance function lacks an evidence anchor

Compatibility mode allows legacy `story.role` checks and reports
`legacy_shape: true` in the summary.

## Golden Sample

Only `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`
is migrated as a golden sample. Other historical cases are left untouched.
````

- [ ] **Step 3: Write tasks**

Create `openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md`:

```markdown
# Tasks

- [ ] 1. Add OpenSpec requirements for strict role instance and evidence anchor gates.
- [ ] 2. Add failing checker tests for strict role/evidence behavior.
- [ ] 3. Implement checker strict mode, compatibility mode, and rich blockers.
- [ ] 4. Update requirements case rendering for role instances and role refs.
- [ ] 5. Update requirements analysis generation for role instances and candidate roles.
- [ ] 6. Require strict readiness before OpenSpec draft generation.
- [ ] 7. Migrate embedded-account-phase1 as the golden sample.
- [ ] 8. Add golden sample regression tests.
- [ ] 9. Run unit tests and OpenSpec validation.
- [ ] 10. Update skill text and behavior evidence only if user-visible routing changes.
```

- [ ] **Step 4: Write spec**

Create `openspec/changes/strengthen-requirements-role-evidence-gate/specs/requirements-analysis-agent/spec.md`:

```markdown
## ADDED Requirements

### Requirement: Requirements cases SHALL use case-local role instances for strict handoff

Strict requirements readiness SHALL require user stories to reference confirmed
case-local role instances rather than bare taxonomy role buckets.

#### Scenario: Story references a confirmed role instance

- **GIVEN** a requirements case has role `R-embedded-account-front`
- **AND** the role has `status: confirmed`
- **AND** `confirmed_as: system_actor` maps to requirements taxonomy
- **WHEN** user story `US-006` has `role_ref: R-embedded-account-front`
- **THEN** the strict checker SHALL accept the story role reference

#### Scenario: Story uses legacy bare role

- **GIVEN** a user story has `role: system_actor`
- **AND** it has no `role_ref`
- **WHEN** strict readiness is checked
- **THEN** the checker SHALL block with `story_role_ref_missing`

### Requirement: Requirements checker SHALL validate object-aware evidence anchors

The checker SHALL require traceable evidence anchors without requiring every
object to use the field name `evidence_refs`.

#### Scenario: Acceptance function has source acceptance

- **GIVEN** acceptance function `AF-014` has `source_acceptance: AC-014`
- **WHEN** strict readiness is checked
- **THEN** evidence validation for that acceptance function SHALL pass

#### Scenario: Acceptance function has no evidence anchor

- **GIVEN** an acceptance function has no `evidence_refs`, `evidence_anchor`,
  `source_section`, `source_quote`, `source_line`, `source_acceptance`, or
  `source_functions`
- **WHEN** strict readiness is checked
- **THEN** the checker SHALL block with `acceptance_evidence_missing`

### Requirement: Legacy case files SHALL remain readable

Compatibility mode SHALL allow existing legacy case files to be checked without
requiring immediate migration.

#### Scenario: Legacy case checked in compatibility mode

- **GIVEN** a legacy case uses `story.role`
- **WHEN** compatibility mode is used
- **THEN** the checker SHALL use existing taxonomy role validation
- **AND** the summary SHALL mark the case as legacy-compatible

### Requirement: OpenSpec draft generation SHALL require strict readiness

OpenSpec draft creation SHALL use strict readiness and SHALL NOT generate drafts
from candidate or legacy-only role mappings.

#### Scenario: Candidate role is referenced by a story

- **GIVEN** a story references role `R-unknown-ops`
- **AND** that role has `status: candidate_pending`
- **WHEN** OpenSpec draft creation is requested
- **THEN** draft creation SHALL be blocked
```

- [ ] **Step 5: Validate OpenSpec change**

Run:

```bash
openspec validate strengthen-requirements-role-evidence-gate --strict
```

Expected:

```text
Change 'strengthen-requirements-role-evidence-gate' is valid
```

PostHog DNS errors may print after validation in restricted network conditions. Treat validation as successful if the command exits 0 and prints the valid line.

- [ ] **Step 6: Commit**

Run:

```bash
git add openspec/changes/strengthen-requirements-role-evidence-gate
git commit -m "docs: propose requirements role evidence gate"
```

Expected: one commit containing only the new OpenSpec change.

## Task 2: Add Strict Checker RED Tests

**Files:**
- Modify: `tests/test_requirements_checker_gate.py`

- [ ] **Step 1: Add strict fixture helper**

In `tests/test_requirements_checker_gate.py`, update `_package` roles and user stories to the new strict shape:

```python
            "roles": [
                {
                    "id": "R-finance",
                    "mention": "finance",
                    "confirmed_as": "finance",
                    "status": "confirmed",
                    "category": "operation_owners",
                    "source_actors": ["finance"],
                    "evidence_anchor": {"source_section": "roles"},
                },
                {
                    "id": "R-system",
                    "mention": "system",
                    "confirmed_as": "system_actor",
                    "status": "confirmed",
                    "category": "system_actors",
                    "source_actors": ["system"],
                    "evidence_anchor": {"source_section": "roles"},
                },
            ],
            "user_stories": [
                {
                    "id": "US-1",
                    "role_ref": "R-finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-001"]},
                }
            ],
            "acceptance_functions": [
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "given": "entries exist",
                    "when": "finance opens reconciliation",
                    "then": "unreconciled entries are visible",
                    "source_acceptance": "AC-001",
                }
            ],
```

- [ ] **Step 2: Add missing role_ref test**

Add this test method:

```python
    def test_strict_story_without_role_ref_fails(self) -> None:
        package = self._package(
            user_stories=[
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-001"]},
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("story_role_ref_missing", {blocker["code"] for blocker in report["blockers"]})
```

- [ ] **Step 3: Add candidate role block test**

Add this test method:

```python
    def test_strict_story_referencing_candidate_role_fails(self) -> None:
        package = self._package(
            roles=[
                {
                    "id": "R-ops",
                    "mention": "operations",
                    "confirmed_as": "financial_operations",
                    "status": "candidate_pending",
                    "source_actors": ["operations"],
                    "evidence_anchor": {"source_section": "roles"},
                }
            ],
            user_stories=[
                {
                    "id": "US-1",
                    "role_ref": "R-ops",
                    "want": "process exception entries",
                    "benefit": "exceptions are resolved",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-001"]},
                }
            ],
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("story_role_not_confirmed", {blocker["code"] for blocker in report["blockers"]})
```

- [ ] **Step 4: Add evidence anchor tests**

Add these test methods:

```python
    def test_acceptance_source_acceptance_counts_as_evidence_anchor(self) -> None:
        path = self._write_case(self._package())

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertEqual(report["blockers"], [])

    def test_acceptance_without_evidence_anchor_fails(self) -> None:
        package = self._package(
            acceptance_functions=[
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "then": "unreconciled entries are visible",
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("acceptance_evidence_missing", {blocker["code"] for blocker in report["blockers"]})
```

- [ ] **Step 5: Add legacy compatibility test**

Add this test method:

```python
    def test_legacy_case_shape_remains_readable_in_compatibility_mode(self) -> None:
        package = self._package(
            roles=[{"id": "finance", "label": "finance"}],
            user_stories=[
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                }
            ],
            acceptance_functions=[
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "then": "unreconciled entries are visible",
                }
            ],
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=False)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertTrue(report["summary"]["legacy_compatible"])
```

- [ ] **Step 6: Run tests and verify RED**

Run:

```bash
python3 -m unittest tests.test_requirements_checker_gate
```

Expected: failures mentioning unexpected keyword argument `strict` or missing strict blocker codes. These failures prove the new tests are exercising absent behavior.

- [ ] **Step 7: Commit RED tests**

Run:

```bash
git add tests/test_requirements_checker_gate.py
git commit -m "test: add strict requirements role evidence gate cases"
```

Expected: one commit containing only the checker tests.

## Task 3: Implement Checker Strict Mode

**Files:**
- Modify: `scripts/check_requirements_case.py`
- Modify: `tests/test_requirements_checker_gate.py`

- [ ] **Step 1: Add blocker shape and evidence helper**

In `scripts/check_requirements_case.py`, replace `_blocker` with:

```python
def _blocker(
    code: str,
    reason: str,
    *,
    field: str = "",
    question: str = "",
    evidence: str = "",
) -> dict[str, str]:
    item = {"code": code, "reason": reason}
    if field:
        item["field"] = field
    if question:
        item["question"] = question
    if evidence:
        item["evidence"] = evidence
    return item
```

Add:

```python
def _has_value(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set)):
        return any(_has_value(item) for item in value)
    if isinstance(value, dict):
        return any(_has_value(item) for item in value.values())
    return value is not None


def has_evidence_anchor(item: dict[str, Any], object_type: str) -> bool:
    common_fields = (
        "evidence_refs",
        "evidence_anchor",
        "source_section",
        "source_quote",
        "source_line",
    )
    if any(_has_value(item.get(field)) for field in common_fields):
        return True
    if object_type == "user_story":
        return _has_value(item.get("source_functions"))
    if object_type == "acceptance_function":
        return _has_value(item.get("source_acceptance")) or _has_value(item.get("source_functions"))
    if object_type == "role":
        return _has_value(item.get("source_actors")) and _has_value(item.get("normalization_note"))
    return False
```

- [ ] **Step 2: Add role instance lookup helpers**

Add:

```python
def _role_confirmed_as(role: dict[str, Any]) -> str:
    return str(role.get("confirmed_as") or role.get("id") or role.get("role") or role.get("label") or "").strip()


def _role_instance_id(role: dict[str, Any]) -> str:
    return str(role.get("id") or role.get("role") or role.get("label") or "").strip()
```

- [ ] **Step 3: Update check function signature and role validation**

Change:

```python
def check_requirements_case(case_data: dict[str, Any], taxonomy: dict[str, Any]) -> dict[str, Any]:
```

to:

```python
def check_requirements_case(
    case_data: dict[str, Any],
    taxonomy: dict[str, Any],
    *,
    strict: bool = True,
) -> dict[str, Any]:
```

Replace the role block with:

```python
    case_roles = _dict_items(case_data.get("roles"))
    role_instances: dict[str, dict[str, Any]] = {}
    declared_roles: set[str] = set()
    legacy_compatible = False
    if not case_roles:
        blockers.append(_blocker("roles_missing", "roles are required", field="roles"))
    for role in case_roles:
        role_id = _role_instance_id(role)
        canonical_source = _role_confirmed_as(role)
        canonical = role_lookup.get(canonical_source)
        if role_id:
            role_instances[role_id] = role
        if not role_id or not canonical:
            blockers.append(_blocker("role_unknown", f"role is missing or unknown: {role_id or canonical_source or 'missing'}", field=f"roles.{role_id or 'missing'}"))
        else:
            declared_roles.add(canonical)
        if strict and role.get("status") == "confirmed" and not has_evidence_anchor(role, "role"):
            blockers.append(_blocker("role_evidence_missing", f"role {role_id} has no evidence anchor", field=f"roles.{role_id}"))
```

- [ ] **Step 4: Update story role validation**

Inside the story loop, replace legacy role validation with:

```python
        role_ref = str(story.get("role_ref", "")).strip()
        if strict:
            if not role_ref:
                blockers.append(
                    _blocker(
                        "story_role_ref_missing",
                        f"user story {story_id} must reference a confirmed case-local role instance",
                        field=f"user_stories.{story_id}.role_ref",
                        question=f"Select the role instance that performs {story_id}.",
                        evidence=", ".join(_string_list(story.get("source_functions"))),
                    )
                )
            elif role_ref not in role_instances:
                blockers.append(_blocker("story_role_ref_unknown", f"user story {story_id} references missing role {role_ref}", field=f"user_stories.{story_id}.role_ref"))
            else:
                role = role_instances[role_ref]
                role_status = str(role.get("status", "")).strip()
                canonical = role_lookup.get(_role_confirmed_as(role))
                if role_status != "confirmed":
                    blockers.append(_blocker("story_role_not_confirmed", f"user story {story_id} references non-confirmed role {role_ref}", field=f"user_stories.{story_id}.role_ref"))
                if not canonical:
                    blockers.append(_blocker("story_role_taxonomy_unknown", f"user story {story_id} role {role_ref} does not map to requirements taxonomy", field=f"user_stories.{story_id}.role_ref"))
        else:
            story_role = str(story.get("role", "")).strip()
            story_role_canonical = role_lookup.get(story_role)
            if story_role:
                legacy_compatible = True
            if not story_role:
                blockers.append(_blocker("story_role_missing", f"user story {story_id} has no role", field=f"user_stories.{story_id}.role"))
            elif not story_role_canonical:
                blockers.append(_blocker("story_role_unknown", f"user story {story_id} has unknown role: {story_role}", field=f"user_stories.{story_id}.role"))
            elif story_role_canonical not in declared_roles:
                blockers.append(_blocker("story_role_not_declared", f"user story {story_id} role is not declared: {story_role}", field=f"user_stories.{story_id}.role"))
```

- [ ] **Step 5: Add story evidence validation**

After story role validation, add:

```python
        if strict and not has_evidence_anchor(story, "user_story"):
            blockers.append(_blocker("story_evidence_missing", f"user story {story_id} has no evidence anchor", field=f"user_stories.{story_id}"))
```

- [ ] **Step 6: Add acceptance evidence validation**

Inside the acceptance function loop, after observable-content validation, add:

```python
        if strict and not has_evidence_anchor(function, "acceptance_function"):
            blockers.append(_blocker("acceptance_evidence_missing", f"acceptance function {function_id} has no evidence anchor", field=f"acceptance_functions.{function_id}"))
```

- [ ] **Step 7: Return strict metadata**

Change the summary return block to include:

```python
            "strict": strict,
            "legacy_compatible": legacy_compatible,
```

- [ ] **Step 8: Update file-level wrapper and CLI**

Change:

```python
def check_requirements_case_file(case_file: Path | str, repo_root: Path | str = ".") -> dict[str, Any]:
```

to:

```python
def check_requirements_case_file(
    case_file: Path | str,
    repo_root: Path | str = ".",
    *,
    strict: bool = True,
) -> dict[str, Any]:
```

and return:

```python
    return check_requirements_case(case_data, taxonomy, strict=strict)
```

In `main`, add:

```python
    parser.add_argument("--compat", action="store_true", help="Use legacy compatibility mode instead of strict handoff mode.")
```

and call:

```python
    report = check_requirements_case_file(args.case_file, repo_root=args.repo_root, strict=not args.compat)
```

- [ ] **Step 9: Run checker tests**

Run:

```bash
python3 -m unittest tests.test_requirements_checker_gate
```

Expected:

```text
OK
```

- [ ] **Step 10: Commit checker implementation**

Run:

```bash
git add scripts/check_requirements_case.py tests/test_requirements_checker_gate.py
git commit -m "feat: add strict requirements role evidence checker"
```

Expected: one commit containing checker code and tests.

## Task 4: Update Case Rendering And Analysis Generation

**Files:**
- Modify: `scripts/requirements_case.py`
- Modify: `scripts/requirements_analysis_agent.py`
- Modify: `tests/test_requirements_analysis_agent.py`

- [ ] **Step 1: Update ready fixture in analysis tests**

In `tests/test_requirements_analysis_agent.py`, update `_package` role/story/acceptance fixtures to strict shape:

```python
            "roles": [
                {
                    "id": "R-finance",
                    "mention": "finance",
                    "confirmed_as": "finance",
                    "status": "confirmed",
                    "source_actors": ["finance"],
                    "evidence_anchor": {"source_section": "roles"},
                },
                {
                    "id": "R-system",
                    "mention": "system",
                    "confirmed_as": "system_actor",
                    "status": "confirmed",
                    "source_actors": ["system"],
                    "evidence_anchor": {"source_section": "roles"},
                },
            ],
            "user_stories": [
                {
                    "id": "US-1",
                    "role_ref": "R-finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-001"]},
                }
            ],
            "acceptance_functions": [
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "given": "entries exist",
                    "when": "finance opens reconciliation",
                    "then": "unreconciled entries are visible",
                    "source_acceptance": "AC-001",
                }
            ],
```

- [ ] **Step 2: Add candidate draft block test**

Add to `tests/test_requirements_analysis_agent.py`:

```python
    def test_create_openspec_draft_blocks_candidate_role_reference(self) -> None:
        case_file = self._write_case(
            self._package(
                roles=[
                    {
                        "id": "R-ops",
                        "mention": "operations",
                        "confirmed_as": "financial_operations",
                        "status": "candidate_pending",
                        "source_actors": ["operations"],
                        "evidence_anchor": {"source_section": "roles"},
                    }
                ],
                user_stories=[
                    {
                        "id": "US-1",
                        "role_ref": "R-ops",
                        "want": "process exception entries",
                        "benefit": "exceptions are resolved",
                        "acceptance_function_ids": ["AF-1"],
                        "evidence_anchor": {"source_functions": ["F-001"]},
                    }
                ],
            )
        )

        result = create_openspec_draft_from_case(
            case_file,
            "draft-candidate-role",
            repo_root=self.tmpdir,
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["reason"], "requirements_not_ready")
        self.assertFalse((self.tmpdir / "openspec" / "changes" / "draft-candidate-role").exists())
        self.assertIn("story_role_not_confirmed", {blocker["code"] for blocker in result["blockers"]})
```

- [ ] **Step 3: Run test to verify RED if generator/draft still legacy**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent
```

Expected: failures around draft generation or fixture rendering if strict support is incomplete.

- [ ] **Step 4: Update markdown role rendering**

In `scripts/requirements_case.py`, replace `_role_line` with:

```python
def _role_line(item: dict[str, Any]) -> str:
    role_id = str(item.get("id") or item.get("role") or "unknown")
    mention = str(item.get("mention") or item.get("label") or role_id)
    confirmed_as = str(item.get("confirmed_as") or item.get("role") or item.get("label") or "")
    status = str(item.get("status") or "")
    category = str(item.get("category", ""))
    parts = [mention]
    if confirmed_as:
        parts.append(f"as={confirmed_as}")
    if status:
        parts.append(f"status={status}")
    if category:
        parts.append(f"category={category}")
    return f"- {role_id}: {'; '.join(parts)}"
```

- [ ] **Step 5: Update story rendering**

In `scripts/requirements_case.py`, replace `_story_line` with:

```python
def _story_line(item: dict[str, Any]) -> str:
    story_id = str(item.get("id", "unknown"))
    role_ref = str(item.get("role_ref") or "")
    role = str(item.get("role") or "")
    want = str(item.get("want") or item.get("story") or item.get("summary") or "")
    benefit = str(item.get("benefit", ""))
    refs = ", ".join(str(ref) for ref in _as_list(item.get("acceptance_function_ids")))
    role_part = f"role_ref={role_ref}" if role_ref else f"role={role}" if role else ""
    parts = [
        part
        for part in [
            role_part,
            want,
            f"benefit={benefit}" if benefit else "",
            f"acceptance={refs}" if refs else "",
        ]
        if part
    ]
    return f"- {story_id}: {'; '.join(parts)}" if parts else f"- {story_id}"
```

- [ ] **Step 6: Add role instance helper in analysis agent**

In `scripts/requirements_analysis_agent.py`, add:

```python
def build_role_instance(
    *,
    role_id: str,
    mention: str,
    confirmed_as: str,
    status: str = "confirmed",
    category: str = "",
    source_section: str = "",
) -> dict[str, object]:
    role: dict[str, object] = {
        "id": role_id,
        "mention": mention,
        "confirmed_as": confirmed_as,
        "status": status,
        "source_actors": [mention],
    }
    if category:
        role["category"] = category
    if source_section:
        role["evidence_anchor"] = {"source_section": source_section}
    return role
```

If the file already has a better-local helper structure, keep the helper near other package-building helpers.

- [ ] **Step 7: Ensure draft generator uses strict checker**

In `scripts/requirements_openspec_draft.py`, change the readiness call to:

```python
    readiness = check_requirements_case_file(case_path, repo_root=root, strict=True)
```

If draft generation is imported from `scripts.requirements_analysis_agent`, apply the same strict argument at that call site.

- [ ] **Step 8: Run analysis tests**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent
```

Expected:

```text
OK
```

- [ ] **Step 9: Commit generation/rendering changes**

Run:

```bash
git add scripts/requirements_case.py scripts/requirements_analysis_agent.py scripts/requirements_openspec_draft.py tests/test_requirements_analysis_agent.py
git commit -m "feat: generate strict requirements role instances"
```

Expected: one commit containing rendering, generation, draft strictness, and tests.

## Task 5: Migrate Embedded Account Golden Sample

**Files:**
- Modify: `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`
- Modify: `tests/test_requirements_checker_gate.py`

- [ ] **Step 1: Add golden sample regression test**

Add to `tests/test_requirements_checker_gate.py`:

```python
    def test_embedded_account_golden_sample_passes_strict_gate(self) -> None:
        source = Path(__file__).resolve().parents[1] / "wiki" / "ops" / "requirements-cases" / "2026-05-29-191857-embedded-account-phase1.md"
        target_dir = self.tmpdir / "wiki" / "ops" / "requirements-cases"
        target_dir.mkdir(parents=True)
        target = target_dir / source.name
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

        report = check_requirements_case_file(target, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertEqual(report["blockers"], [])
```

- [ ] **Step 2: Add golden sample role_ref content test**

Add:

```python
    def test_embedded_account_golden_sample_uses_embedded_front_role_ref(self) -> None:
        source = Path(__file__).resolve().parents[1] / "wiki" / "ops" / "requirements-cases" / "2026-05-29-191857-embedded-account-phase1.md"
        text = source.read_text(encoding="utf-8")

        self.assertIn('"id": "R-embedded-account-front"', text)
        self.assertIn('"role_ref": "R-embedded-account-front"', text)
        self.assertNotIn('"role": "system_actor"', text)
```

- [ ] **Step 3: Run golden tests and verify RED**

Run:

```bash
python3 -m unittest tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_embedded_account_golden_sample_passes_strict_gate tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_embedded_account_golden_sample_uses_embedded_front_role_ref
```

Expected: FAIL because the golden sample has not been migrated yet.

- [ ] **Step 4: Migrate roles in machine case data**

In `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`, update the machine JSON `roles` array to include role instances. Use this role set:

```json
[
  {
    "id": "R-merchant",
    "mention": "商户",
    "confirmed_as": "financial_customer",
    "status": "confirmed",
    "category": "business_actors",
    "source_actors": ["商户", "目标客户", "权益类商户"],
    "evidence_anchor": {"source_section": "1 基本信息 / 5.1 参与角色/系统"}
  },
  {
    "id": "R-terminal-user",
    "mention": "终端用户",
    "confirmed_as": "retail_customer",
    "status": "confirmed",
    "category": "business_actors",
    "source_actors": ["商户终端用户", "终端用户"],
    "evidence_anchor": {"source_section": "0.1 一句话闭环 / 5.1 参与角色/系统"}
  },
  {
    "id": "R-merchant-system",
    "mention": "商户系统",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["商户系统"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-unified-gateway",
    "mention": "统一网关",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["统一网关"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-notification-center",
    "mention": "通知中心",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["通知中心"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-product-center",
    "mention": "产品中心",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["产品中心"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-embedded-account-front",
    "mention": "嵌入式账户前置",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["嵌入式账户前置"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-account-core",
    "mention": "账户核心",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["账户核心"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-subscription-payment-product",
    "mention": "订阅支付产品",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["订阅支付产品"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-baofoo-channel",
    "mention": "宝付通道",
    "confirmed_as": "system_actor",
    "status": "confirmed",
    "category": "system_actors",
    "source_actors": ["宝付通道"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-product-owner",
    "mention": "嵌入式账户产品需求 owner",
    "confirmed_as": "product",
    "status": "confirmed",
    "category": "delivery_owners",
    "source_actors": ["产品中心", "订阅支付产品", "嵌入式账户产品需求 owner"],
    "evidence_anchor": {"source_section": "5.1 参与角色/系统"}
  },
  {
    "id": "R-engineering",
    "mention": "相关研发团队",
    "confirmed_as": "engineering",
    "status": "confirmed",
    "category": "delivery_owners",
    "source_actors": ["嵌入式账户前置", "账户核心", "统一网关", "通知中心", "订阅支付产品相关研发团队"],
    "evidence_anchor": {"source_section": "4.1 本文档范围边界说明"}
  },
  {
    "id": "R-qa",
    "mention": "验收责任方",
    "confirmed_as": "qa",
    "status": "confirmed",
    "category": "delivery_owners",
    "source_actors": ["联调", "测试", "验收责任方"],
    "evidence_anchor": {"source_section": "10 验收标准"}
  }
]
```

- [ ] **Step 5: Migrate story role refs**

In the same machine JSON, set:

```json
"US-001": {"role_ref": "R-merchant"}
"US-002": {"role_ref": "R-terminal-user"}
"US-003": {"role_ref": "R-merchant"}
"US-004": {"role_ref": "R-merchant"}
"US-005": {"role_ref": "R-merchant"}
"US-006": {"role_ref": "R-embedded-account-front"}
"US-007": {"role_ref": "R-embedded-account-front"}
```

Remove legacy `"role": "system_actor"` from `US-006` and `US-007`. Keep `role` display metadata for business stories only if needed, but strict readiness must use `role_ref`.

- [ ] **Step 6: Add story evidence anchors**

For each story, add evidence anchors:

```json
"US-001": {"evidence_anchor": {"source_functions": ["F-001", "F-002"]}}
"US-002": {"evidence_anchor": {"source_functions": ["F-002", "F-003"]}}
"US-003": {"evidence_anchor": {"source_functions": ["F-003"]}}
"US-004": {"evidence_anchor": {"source_functions": ["F-004"]}}
"US-005": {"evidence_anchor": {"source_functions": ["F-005"]}}
"US-006": {"evidence_anchor": {"source_functions": ["F-006"]}}
"US-007": {"evidence_anchor": {"source_functions": ["F-007"]}}
```

- [ ] **Step 7: Update human-readable sections**

Update the markdown `## Roles` and `## User Stories` sections above the machine JSON to reflect role instances and `role_ref`. Keep the section concise. Example line:

```markdown
- R-embedded-account-front: 嵌入式账户前置 (system_actor, confirmed); source actors: 嵌入式账户前置
```

Example story line:

```markdown
- US-006: role_ref=R-embedded-account-front; 嵌入式账户前置希望按已绑卡优先级轮询发起快捷支付；benefit=在高优先级卡明确失败后可以继续尝试低优先级卡。
```

- [ ] **Step 8: Run golden sample tests**

Run:

```bash
python3 -m unittest tests.test_requirements_checker_gate
```

Expected:

```text
OK
```

- [ ] **Step 9: Run frontmatter target precheck**

Run:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md
```

Expected: target `entry_count` is 0. Whole-repo warnings may remain if unrelated producer warnings exist.

- [ ] **Step 10: Commit golden sample migration**

Run:

```bash
git add wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md tests/test_requirements_checker_gate.py
git commit -m "docs: migrate embedded account requirements golden sample"
```

Expected: one commit containing only the golden sample and its regression tests.

## Task 6: Full Verification And OpenSpec Evidence

**Files:**
- Modify: `openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md`
- Optional Modify: `openspec/changes/strengthen-requirements-role-evidence-gate/evaluation.md`

- [ ] **Step 1: Run focused unit tests**

Run:

```bash
python3 -m unittest tests.test_requirements_checker_gate tests.test_requirements_analysis_agent tests.test_req_agent_skills
```

Expected:

```text
OK
```

- [ ] **Step 2: Run OpenSpec validation**

Run:

```bash
openspec validate strengthen-requirements-role-evidence-gate --strict
```

Expected:

```text
Change 'strengthen-requirements-role-evidence-gate' is valid
```

- [ ] **Step 3: Run requirements checker on golden sample**

Run:

```bash
python3 -m scripts.check_requirements_case wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md
```

Expected JSON contains:

```json
"hard_gate_passed": true,
"strict": true
```

- [ ] **Step 4: Run compatibility probe**

Create a temporary legacy case using the existing old-shape fixture in a Python one-liner and check compatibility mode:

```bash
python3 - <<'PY'
import shutil
import tempfile
from pathlib import Path
from scripts.requirements_case import build_requirements_case_package, write_requirements_case_file
from scripts.check_requirements_case import check_requirements_case_file

tmp = Path(tempfile.mkdtemp(prefix="legacy-case-probe-"))
(tmp / "requirements" / "config").mkdir(parents=True)
shutil.copyfile("requirements/config/requirements-taxonomy.yaml", tmp / "requirements" / "config" / "requirements-taxonomy.yaml")
case = build_requirements_case_package(
    case_slug="legacy",
    status="requirements_ready",
    domain={"status": "confirmed", "confirmed": "account", "candidates": [{"id": "account"}]},
    roles=[{"id": "finance", "label": "finance"}],
    user_stories=[{"id": "US-1", "role": "finance", "want": "review entries", "benefit": "close books", "acceptance_function_ids": ["AF-1"]}],
    acceptance_functions=[{"id": "AF-1", "name": "list entries", "user_story_ids": ["US-1"], "then": "entries are listed"}],
    timestamp="2026-06-02T00:00:00+00:00",
)
path = write_requirements_case_file(case, tmp, output_dir=tmp / "cases", timestamp="2026-06-02T00:00:00+00:00")
report = check_requirements_case_file(path, repo_root=tmp, strict=False)
print(report["summary"])
shutil.rmtree(tmp)
PY
```

Expected output includes:

```text
'status': 'requirements_ready'
'legacy_compatible': True
```

- [ ] **Step 5: Update OpenSpec tasks evidence**

Edit `openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md` and check completed items. Add a short verification note at the bottom:

```markdown
## Verification

- `python3 -m unittest tests.test_requirements_checker_gate tests.test_requirements_analysis_agent tests.test_req_agent_skills` passed.
- `openspec validate strengthen-requirements-role-evidence-gate --strict` passed.
- Golden sample strict checker passed.
- Legacy compatibility probe passed.
```

- [ ] **Step 6: Commit verification evidence**

Run:

```bash
git add openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md
git commit -m "docs: record requirements role evidence verification"
```

Expected: one commit containing only OpenSpec task status/evidence.

## Task 7: Completion Gate

**Files:**
- Read: `openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md`
- Read: `git status --short`
- Read: `git log -1 --oneline`

- [ ] **Step 1: Re-check OpenSpec tasks**

Run:

```bash
sed -n '1,220p' openspec/changes/strengthen-requirements-role-evidence-gate/tasks.md
```

Expected: all implementation tasks are checked and verification evidence is present.

- [ ] **Step 2: Run final focused tests**

Run:

```bash
python3 -m unittest tests.test_requirements_checker_gate tests.test_requirements_analysis_agent tests.test_req_agent_skills
```

Expected:

```text
OK
```

- [ ] **Step 3: Run final OpenSpec validation**

Run:

```bash
openspec validate strengthen-requirements-role-evidence-gate --strict
```

Expected:

```text
Change 'strengthen-requirements-role-evidence-gate' is valid
```

- [ ] **Step 4: Check git truth**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: any remaining dirty files are pre-existing unrelated work or explicitly task-related follow-up. Do not claim worktree clean unless the output is clean.

- [ ] **Step 5: Stop at OpenSpec completion**

If every checkbox in `tasks.md` is complete, stop implementation. The next default action is archive review, not immediate archive or adjacent cleanup.

## Self-Review

Spec coverage:

- Role instances: Task 2, Task 3, Task 4, Task 5.
- `role_ref` strict gate: Task 2 and Task 3.
- Evidence anchor contract: Task 2 and Task 3.
- Golden sample migration: Task 5.
- Legacy compatibility: Task 2, Task 3, Task 6.
- OpenSpec lifecycle: Task 1, Task 6, Task 7.

Placeholder scan:

- The plan has no unresolved blanks or generic "add tests" steps.
- Each code-changing task includes exact file paths, concrete snippets, commands, and expected output.

Type consistency:

- `strict` is the checker mode keyword across tests, checker wrappers, CLI, and draft generation.
- Role instances use `id`, `mention`, `confirmed_as`, `status`, `source_actors`, and optional `evidence_anchor`.
- Stories use `role_ref`.
- Acceptance functions use `source_acceptance` and/or `source_functions` as evidence anchors.
