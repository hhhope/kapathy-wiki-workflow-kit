# Requirements Analysis Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an intent-aware requirements analysis agent that normalizes requirement material, gates requirement readiness, and creates reviewed OpenSpec drafts only after hard-gate readiness.

**Architecture:** Add an OpenSpec change first, then implement a small Python workflow mirroring the repo's medical-case pattern. The agent owns intent and domain recognition; `requirements/config/requirements-taxonomy.yaml` owns readiness vocabulary; `scripts/check_requirements_case.py` provides deterministic gate evidence.

**Tech Stack:** Python standard library, YAML via existing `pyyaml`, repo-local `unittest`, existing OpenSpec markdown structure, JSON data blocks embedded in Markdown case files.

---

## File Structure

- Create `openspec/changes/add-requirements-analysis-agent/proposal.md`
  - Describes why the workflow is needed and the first-version boundary.
- Create `openspec/changes/add-requirements-analysis-agent/design.md`
  - Copies the approved Superpowers design into OpenSpec lifecycle authority.
- Create `openspec/changes/add-requirements-analysis-agent/tasks.md`
  - Tracks implementation tasks and verification.
- Create `openspec/changes/add-requirements-analysis-agent/specs/requirements-analysis-agent/spec.md`
  - Defines SHALL requirements for intent recognition, domain candidates, hard gate, and OpenSpec draft handoff.
- Create `requirements/config/requirements-taxonomy.yaml`
  - Independent requirement-readiness taxonomy; not wiki frontmatter taxonomy.
- Create `scripts/requirements_case.py`
  - Builds, renders, writes, and loads requirements case files with machine-readable JSON blocks.
- Create `scripts/check_requirements_case.py`
  - Loads taxonomy and case data, emits deterministic hard-gate and soft-warning reports.
- Create `scripts/requirements_analysis_agent.py`
  - Classifies user intent, resolves domain match/candidates, resolves active case, routes status and draft handoff.
- Create `scripts/build_requirements_analysis_agent.py`
  - CLI wrapper returning JSON for normal user-facing use.
- Create `tests/test_requirements_case.py`
  - Case rendering/loading tests.
- Create `tests/test_requirements_checker.py`
  - Taxonomy and hard-gate tests.
- Create `tests/test_requirements_analysis_agent.py`
  - Intent/domain routing and OpenSpec draft handoff tests.

## Task 1: Create OpenSpec Change Artifacts

**Files:**
- Create: `openspec/changes/add-requirements-analysis-agent/proposal.md`
- Create: `openspec/changes/add-requirements-analysis-agent/design.md`
- Create: `openspec/changes/add-requirements-analysis-agent/tasks.md`
- Create: `openspec/changes/add-requirements-analysis-agent/specs/requirements-analysis-agent/spec.md`

- [ ] **Step 1: Create proposal**

Create `openspec/changes/add-requirements-analysis-agent/proposal.md`:

```markdown
# add-requirements-analysis-agent

## Why

Implementation can begin before requirements are clear enough to code. The
repeated failure pattern is missing requirement shape: unclear domain, unnamed
roles, weak user stories, and acceptance functions that do not map back to user
stories.

The repository already has wiki taxonomy and medical-agent case-file patterns.
This change adds a separate requirements analysis agent so requirement readiness
can be checked without turning wiki frontmatter or detailed-design content into
requirement authority.

## What Changes

- Add `requirements/config/requirements-taxonomy.yaml` as the independent
  requirement-readiness contract.
- Add requirements case-file helpers with machine-readable JSON blocks.
- Add `scripts/check_requirements_case.py` for deterministic hard-gate evidence.
- Add `scripts/requirements_analysis_agent.py` for intent recognition, domain
  recognition, case routing, and OpenSpec draft handoff.
- Add a CLI wrapper for normal use.
- Add focused tests for intent classification, domain candidates, hard-gate
  behavior, mixed-document soft warnings, and OpenSpec draft blocking.

## Out of Scope

- API correctness validation.
- DDL correctness validation.
- Full architecture review.
- Release readiness validation.
- Automatic implementation after OpenSpec draft creation.
- Forcing unknown domains into existing domain IDs.

## Source Design

- `docs/superpowers/specs/2026-05-29-requirements-analysis-agent-design.md`
```

- [ ] **Step 2: Create OpenSpec design**

Create `openspec/changes/add-requirements-analysis-agent/design.md`:

```markdown
# Design

## Boundary

The requirements analysis agent is an intent-aware lifecycle controller. It is
not a generic detailed-design reviewer.

The first version hard gate checks only:

- confirmed domain
- roles
- user stories
- acceptance functions

Business rules, exception scenarios, ADRs, APIs, DDL, test plans, and release
plans are classified as soft warnings or design evidence.

## Authority

`requirements/config/requirements-taxonomy.yaml` owns requirement-readiness
vocabulary. `wiki/config/frontmatter-taxonomy.yaml` remains limited to wiki page
identity and graph-facing metadata.

Requirements case files own diagnosis, confirmation, normalization, and
readiness. OpenSpec owns formal change lifecycle after readiness.

## Lifecycle

The state model is:

```text
intake -> diagnose -> confirm -> normalize -> gate -> recovery -> archive
```

OpenSpec draft handoff occurs only after the hard gate passes.

## Intent Recognition

The agent classifies user intent before taking action. Supported first-version
intents are:

- `new_requirement_intake`
- `append_material`
- `diagnose_requirement`
- `confirm_requirement`
- `normalize_requirement`
- `check_requirements_ready`
- `create_openspec_draft`
- `status`

## Domain Recognition

Known domains are matched from `requirements-taxonomy.yaml`. Unknown domains
remain candidates until the user confirms them. A case cannot become
`requirements_ready` with an unconfirmed domain.

## OpenSpec Draft Handoff

Draft creation writes:

```text
openspec/changes/<change-id>/
  proposal.md
  design.md
  tasks.md
  specs/<capability>/spec.md
```

Drafts require user review before implementation planning.
```

- [ ] **Step 3: Create task checklist**

Create `openspec/changes/add-requirements-analysis-agent/tasks.md`:

```markdown
# Tasks

- [ ] 1. Create OpenSpec change artifacts.
- [ ] 2. Add requirements taxonomy and taxonomy loading tests.
- [ ] 3. Add requirements case-file helpers and tests.
- [ ] 4. Add requirements checker hard gate and soft-warning tests.
- [ ] 5. Add intent and domain recognition tests.
- [ ] 6. Implement requirements analysis agent routing and CLI.
- [ ] 7. Add OpenSpec draft handoff and tests.
- [ ] 8. Run focused tests and record verification evidence.
- [ ] 9. Commit verified implementation and stop at OpenSpec hard stop.
```

- [ ] **Step 4: Create spec delta**

Create `openspec/changes/add-requirements-analysis-agent/specs/requirements-analysis-agent/spec.md`:

```markdown
## Purpose

Define an intent-aware requirements analysis agent that gates requirement
readiness before OpenSpec draft handoff.

## ADDED Requirements

### Requirement: Agent SHALL classify requirements intent before action

The agent SHALL classify user intent before creating, updating, checking, or
handoff-routing a requirements case.

#### Scenario: User provides new requirement material

- **WHEN** the user provides a requirement document or requirement-like material
- **THEN** the agent SHALL return intent `new_requirement_intake`
- **AND** it SHALL NOT run implementation or OpenSpec draft generation directly

#### Scenario: User asks if the requirement is ready

- **WHEN** the user asks whether the requirement can proceed
- **THEN** the agent SHALL return intent `check_requirements_ready`
- **AND** it SHALL run the requirements case checker when a case is available

### Requirement: Agent SHALL surface domain candidates for unknown domains

The agent SHALL not force unknown domains into existing domain IDs.

#### Scenario: Requirement material does not match a known domain

- **WHEN** no domain in `requirements-taxonomy.yaml` clearly matches the material
- **THEN** the agent SHALL return domain status `candidate_pending`
- **AND** it SHALL include candidate domains with reasons
- **AND** it SHALL require user confirmation before hard-gate readiness

### Requirement: Checker SHALL enforce the first-version hard gate

The checker SHALL block requirement readiness unless confirmed domain, roles,
user stories, and acceptance functions are complete and traceable.

#### Scenario: User story lacks acceptance mapping

- **WHEN** a user story has no acceptance function reference
- **THEN** the checker SHALL fail the hard gate
- **AND** it SHALL include a blocking reason naming the user story

### Requirement: Checker SHALL classify detailed-design material as soft warning

Detailed design sections SHALL not become first-version requirement authority.

#### Scenario: Case contains API or DDL evidence

- **WHEN** a requirements case includes API, DDL, ADR, test-plan, or release-plan
  sections
- **THEN** the checker SHALL classify them as soft warnings or design evidence
- **AND** it SHALL NOT fail the hard gate solely because of those sections

### Requirement: Agent SHALL block OpenSpec draft before readiness

The agent SHALL create OpenSpec drafts only after the requirements hard gate has
passed.

#### Scenario: Draft requested while case is blocked

- **WHEN** user intent is `create_openspec_draft`
- **AND** the requirements case is not `requirements_ready`
- **THEN** the agent SHALL block draft creation
- **AND** it SHALL return checker blocking reasons

### Requirement: Agent SHALL create traceable OpenSpec drafts after readiness

The agent SHALL generate OpenSpec draft artifacts from confirmed requirement
data after readiness passes.

#### Scenario: Draft requested for ready case

- **WHEN** user intent is `create_openspec_draft`
- **AND** the requirements case status is `requirements_ready`
- **THEN** the agent SHALL create proposal, design, tasks, and spec draft files
- **AND** each OpenSpec requirement SHALL trace to user story and acceptance
  function IDs
- **AND** implementation SHALL still require user review after draft creation
```

- [ ] **Step 5: Run OpenSpec validation**

Run:

```bash
openspec validate add-requirements-analysis-agent --strict
```

Expected: pass, or fail only because the local OpenSpec CLI is unavailable. If
the CLI is unavailable, record that exact blocker in the change evaluation
before the final commit.

- [ ] **Step 6: Commit**

Run:

```bash
git add openspec/changes/add-requirements-analysis-agent
git commit -m "docs: propose requirements analysis agent"
```

Expected: commit includes only the new OpenSpec change artifacts.

## Task 2: Add Requirements Taxonomy

**Files:**
- Create: `requirements/config/requirements-taxonomy.yaml`
- Create: `tests/test_requirements_checker.py`

- [ ] **Step 1: Write failing taxonomy loading test**

Create `tests/test_requirements_checker.py`:

```python
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_requirements_case import load_requirements_taxonomy


class RequirementsCheckerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-checker-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_loads_account_clearing_taxonomy(self) -> None:
        root = self.tmpdir
        config_dir = root / "requirements" / "config"
        config_dir.mkdir(parents=True)
        (config_dir / "requirements-taxonomy.yaml").write_text(
            """version: 1
domains:
  account-clearing:
    aliases:
      - account
      - 账户
role_sets:
  account-clearing:
    business_actors:
      - retail_customer
    operation_owners:
      - product_owner
    system_actors:
      - account_system
    delivery_owners:
      - engineering_owner
hard_gate:
  required:
    - domain
    - roles
    - user_stories
    - acceptance_functions
""",
            encoding="utf-8",
        )

        taxonomy = load_requirements_taxonomy(root)

        self.assertEqual(taxonomy["version"], 1)
        self.assertIn("account-clearing", taxonomy["domains"])
        self.assertIn("retail_customer", taxonomy["role_sets"]["account-clearing"]["business_actors"])
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.test_requirements_checker.RequirementsCheckerTest.test_loads_account_clearing_taxonomy
```

Expected: fail with `ModuleNotFoundError` or `ImportError` because
`scripts.check_requirements_case` does not exist yet.

- [ ] **Step 3: Add taxonomy config**

Create `requirements/config/requirements-taxonomy.yaml`:

```yaml
version: 1

domains:
  account-clearing:
    aliases:
      - account
      - clearing
      - settlement
      - 账户
      - 结算
      - 清分
      - 清算
      - 清结算

role_sets:
  account-clearing:
    business_actors:
      - retail_customer
      - financial_customer
      - merchant
      - split_recipient
      - agent_partner

    operation_owners:
      - retail_operator
      - financial_operator
      - finance_operator
      - clearing_operator
      - settlement_operator
      - compliance_operator
      - risk_operator
      - channel_operator
      - member_operator
      - product_owner

    system_actors:
      - member_system
      - product_shelf_system
      - account_system
      - clearing_system
      - settlement_system
      - payment_system
      - billing_system
      - reconciliation_system
      - risk_system
      - channel_system

    delivery_owners:
      - product_owner
      - engineering_owner
      - test_owner
      - release_owner
      - operations_owner

hard_gate:
  required:
    - domain
    - roles
    - user_stories
    - acceptance_functions

soft_warning_sections:
  - business_rules
  - exception_scenarios
  - api_candidates
  - ddl_candidates
  - adr_candidates
  - test_plan_candidates
  - release_plan_candidates
```

- [ ] **Step 4: Add minimal taxonomy loader**

Create `scripts/check_requirements_case.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = Path("requirements/config/requirements-taxonomy.yaml")


@dataclass(frozen=True)
class RequirementFinding:
    kind: str
    severity: str
    message: str
    field: str = ""
    item_id: str = ""


def load_requirements_taxonomy(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config_file = root_path / CONFIG_PATH
    with config_file.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"requirements taxonomy must be a mapping: {config_file}")
    return data


def build_report(case_path: Path | str, root: Path | str = ROOT) -> dict[str, Any]:
    return {
        "case_path": str(case_path),
        "passed": False,
        "status": "blocked",
        "blocking_reasons": ["requirements case parsing is not implemented yet"],
        "soft_warnings": [],
        "findings": [
            asdict(
                RequirementFinding(
                    kind="case_parser_missing",
                    severity="error",
                    message="requirements case parsing is not implemented yet",
                )
            )
        ],
        "proof_boundary": [
            "This checker validates requirement readiness only.",
            "It does not validate API, DDL, architecture, release, or implementation correctness.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check requirements case readiness.")
    parser.add_argument("case_path")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--json-output")
    args = parser.parse_args()

    report = build_report(Path(args.case_path), Path(args.root))
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.json_output:
        Path(args.json_output).write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run taxonomy test to verify it passes**

Run:

```bash
python3 -m unittest tests.test_requirements_checker.RequirementsCheckerTest.test_loads_account_clearing_taxonomy
```

Expected: pass.

- [ ] **Step 6: Commit**

Run:

```bash
git add requirements/config/requirements-taxonomy.yaml scripts/check_requirements_case.py tests/test_requirements_checker.py
git commit -m "feat: add requirements taxonomy"
```

Expected: commit includes taxonomy, minimal checker loader, and taxonomy test.

## Task 3: Add Requirements Case File Helpers

**Files:**
- Create: `scripts/requirements_case.py`
- Create: `tests/test_requirements_case.py`

- [ ] **Step 1: Write failing case helper tests**

Create `tests/test_requirements_case.py`:

```python
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_case import (
    build_requirements_case_package,
    load_requirements_case_file,
    render_requirements_case_markdown,
    write_requirements_case_file,
)


class RequirementsCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-case-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_builds_case_package_with_intent_and_domain_candidates(self) -> None:
        package = build_requirements_case_package(
            title="Embedded Wallet",
            intent="new_requirement_intake",
            source_materials=["/tmp/Embedded Wallet.md"],
            candidate_domains=[
                {
                    "domain_id": "wallet-payment",
                    "confidence": "medium",
                    "reason": "wallet account, card binding, and balance payment are the core scenario",
                }
            ],
            timestamp="2026-05-29T01:02:03+00:00",
        )

        self.assertEqual(package["mode"], "requirements_case")
        self.assertEqual(package["status"], "awaiting_domain_confirmation")
        self.assertEqual(package["intent"], "new_requirement_intake")
        self.assertEqual(package["domain_resolution"]["candidate_domains"][0]["domain_id"], "wallet-payment")
        self.assertEqual(package["confirmed_requirements"]["user_stories"], [])

    def test_renders_and_loads_machine_readable_case_data(self) -> None:
        package = build_requirements_case_package(
            title="Split Account Opening",
            intent="new_requirement_intake",
            confirmed_domain="account-clearing",
            timestamp="2026-05-29T01:02:03+00:00",
        )
        markdown = render_requirements_case_markdown(package)

        self.assertIn("<!-- requirements-case-data:start -->", markdown)
        self.assertIn('"mode": "requirements_case"', markdown)
        self.assertIn("## Confirmed Requirements", markdown)

        case_path = write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "requirements" / "cases",
            timestamp="2026-05-29T01:02:03+00:00",
        )
        loaded = load_requirements_case_file(case_path)

        self.assertEqual(case_path.name, "2026-05-29-010203-split-account-opening.md")
        self.assertEqual(loaded["title"], "Split Account Opening")
        self.assertEqual(loaded["domain_resolution"]["confirmed_domain"], "account-clearing")
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
python3 -m unittest tests.test_requirements_case
```

Expected: fail because `scripts.requirements_case` does not exist.

- [ ] **Step 3: Implement case helpers**

Create `scripts/requirements_case.py`:

```python
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REQUIREMENTS_CASE_DIR = Path("requirements/cases")
CASE_DATA_START = "<!-- requirements-case-data:start -->"
CASE_DATA_END = "<!-- requirements-case-data:end -->"


def _iso_timestamp(timestamp: datetime | str | None = None) -> str:
    if timestamp is None:
        return datetime.now(timezone.utc).isoformat()
    if isinstance(timestamp, datetime):
        return timestamp.astimezone(timezone.utc).isoformat()
    return timestamp


def _timestamp_slug(timestamp: datetime | str | None) -> str:
    if timestamp is None:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    if isinstance(timestamp, datetime):
        return timestamp.astimezone(timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d-%H%M%S")


def _slugify(value: str | None) -> str:
    text = str(value or "requirements-case").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "requirements-case"


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def build_requirements_case_package(
    *,
    title: str,
    intent: str,
    source_materials: list[str] | None = None,
    context_source: str = "supplied_material_only",
    candidate_domains: list[dict[str, Any]] | None = None,
    confirmed_domain: str = "",
    timestamp: datetime | str | None = None,
) -> dict[str, Any]:
    generated_at = _iso_timestamp(timestamp)
    status = "requirements_ready" if confirmed_domain else "awaiting_domain_confirmation"
    return {
        "generated_at": generated_at,
        "mode": "requirements_case",
        "title": title,
        "case_slug": _slugify(title),
        "status": status,
        "active": True,
        "context_source": context_source,
        "intent": intent,
        "source_materials": [str(item) for item in (source_materials or [])],
        "domain_resolution": {
            "matched_domain": confirmed_domain,
            "candidate_domains": list(candidate_domains or []),
            "confirmed_domain": confirmed_domain,
        },
        "confirmed_requirements": {
            "domain": confirmed_domain,
            "roles": [],
            "user_stories": [],
            "acceptance_functions": [],
        },
        "design_evidence": [],
        "soft_warnings": [],
        "gate": {
            "status": "not_checked",
            "blocking_reasons": [],
            "checker_report": "",
        },
        "openspec_handoff": {
            "status": "not_ready",
            "change_id": "",
            "draft_paths": [],
        },
        "proof_boundary_notes": [
            "The requirements case validates requirement readiness only.",
            "Detailed design evidence is not implementation authority.",
        ],
    }


def render_requirements_case_markdown(package: dict[str, Any]) -> str:
    title = str(package.get("title") or "requirements-case")
    data = json.dumps(package, ensure_ascii=False, indent=2, sort_keys=True)
    confirmed = package.get("confirmed_requirements", {})
    domain = confirmed.get("domain", "") if isinstance(confirmed, dict) else ""
    return "\n".join(
        [
            f"# Requirements Case: {title}",
            "",
            "## Status",
            "",
            f"- Intent: `{package.get('intent', '')}`",
            f"- Status: `{package.get('status', '')}`",
            f"- Domain: `{domain}`",
            "",
            "## Confirmed Requirements",
            "",
            "- Roles, user stories, and acceptance functions are stored in the machine data block.",
            "",
            "## Gate",
            "",
            f"- Gate status: `{package.get('gate', {}).get('status', '')}`",
            "",
            "## OpenSpec Handoff",
            "",
            f"- Handoff status: `{package.get('openspec_handoff', {}).get('status', '')}`",
            "",
            "## Machine Case Data",
            "",
            CASE_DATA_START,
            data,
            CASE_DATA_END,
            "",
        ]
    )


def write_requirements_case_file(
    package: dict[str, Any],
    root: Path | str,
    *,
    output_dir: Path | str | None = None,
    timestamp: datetime | str | None = None,
) -> Path:
    root_path = Path(root)
    target_dir = Path(output_dir) if output_dir is not None else root_path / DEFAULT_REQUIREMENTS_CASE_DIR
    if not target_dir.is_absolute():
        target_dir = root_path / target_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    slug = _slugify(str(package.get("case_slug") or package.get("title") or "requirements-case"))
    filename = f"{_timestamp_slug(timestamp or package.get('generated_at'))}-{slug}.md"
    path = target_dir / filename
    path.write_text(render_requirements_case_markdown(package), encoding="utf-8")
    return path.resolve()


def load_requirements_case_file(path: Path | str) -> dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    if CASE_DATA_START not in text or CASE_DATA_END not in text:
        raise ValueError(f"requirements case data block missing: {path}")
    raw = text.split(CASE_DATA_START, 1)[1].split(CASE_DATA_END, 1)[0].strip()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError(f"requirements case data must be a JSON object: {path}")
    return data
```

- [ ] **Step 4: Run tests to verify they pass**

Run:

```bash
python3 -m unittest tests.test_requirements_case
```

Expected: pass.

- [ ] **Step 5: Commit**

Run:

```bash
git add scripts/requirements_case.py tests/test_requirements_case.py
git commit -m "feat: add requirements case files"
```

Expected: commit includes requirements case helpers and tests.

## Task 4: Implement Requirements Checker Hard Gate

**Files:**
- Modify: `scripts/check_requirements_case.py`
- Modify: `tests/test_requirements_checker.py`

- [ ] **Step 1: Add failing hard-gate and soft-warning tests**

Append to `tests/test_requirements_checker.py` inside `RequirementsCheckerTest`:

```python
    def _write_case(self, package: dict) -> Path:
        from scripts.requirements_case import write_requirements_case_file

        return write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "requirements" / "cases",
            timestamp="2026-05-29T01:02:03+00:00",
        )

    def _ready_case_package(self) -> dict:
        from scripts.requirements_case import build_requirements_case_package

        package = build_requirements_case_package(
            title="Split Account Opening",
            intent="new_requirement_intake",
            confirmed_domain="account-clearing",
            timestamp="2026-05-29T01:02:03+00:00",
        )
        package["confirmed_requirements"]["roles"] = [
            {
                "role_id": "merchant",
                "role_type": "business_actor",
                "responsibilities": ["initiates wallet opening"],
                "boundary": "merchant-facing business actor",
                "user_story_refs": ["US-001"],
            }
        ]
        package["confirmed_requirements"]["user_stories"] = [
            {
                "story_id": "US-001",
                "role_id": "merchant",
                "goal": "open a wallet for a member",
                "value": "member can pay inside merchant platform",
                "acceptance_function_refs": ["AF-001"],
            }
        ]
        package["confirmed_requirements"]["acceptance_functions"] = [
            {
                "function_id": "AF-001",
                "name": "wallet opening",
                "user_story_refs": ["US-001"],
                "observable_result": "wallet account status is opened",
            }
        ]
        return package

    def test_checker_passes_ready_case(self) -> None:
        from scripts.check_requirements_case import build_report

        case_path = self._write_case(self._ready_case_package())

        report = build_report(case_path, self.tmpdir)

        self.assertTrue(report["passed"])
        self.assertEqual(report["status"], "requirements_ready")
        self.assertEqual(report["blocking_reasons"], [])

    def test_checker_blocks_user_story_without_acceptance_mapping(self) -> None:
        from scripts.check_requirements_case import build_report

        package = self._ready_case_package()
        package["confirmed_requirements"]["user_stories"][0]["acceptance_function_refs"] = []
        case_path = self._write_case(package)

        report = build_report(case_path, self.tmpdir)

        self.assertFalse(report["passed"])
        self.assertIn("user_story US-001 has no acceptance_function_refs", report["blocking_reasons"])

    def test_checker_classifies_design_evidence_as_soft_warning(self) -> None:
        from scripts.check_requirements_case import build_report

        package = self._ready_case_package()
        package["design_evidence"] = [
            {"kind": "ddl_candidates", "source": "Embedded Wallet.md", "summary": "wallet_account table found"}
        ]
        case_path = self._write_case(package)

        report = build_report(case_path, self.tmpdir)

        self.assertTrue(report["passed"])
        self.assertEqual(report["soft_warnings"][0]["kind"], "design_evidence_present")
        self.assertEqual(report["soft_warnings"][0]["source_kind"], "ddl_candidates")
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
python3 -m unittest tests.test_requirements_checker
```

Expected: hard-gate tests fail because `build_report` is still a stub.

- [ ] **Step 3: Implement checker**

Replace `scripts/check_requirements_case.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = Path("requirements/config/requirements-taxonomy.yaml")

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.requirements_case import load_requirements_case_file


@dataclass(frozen=True)
class RequirementFinding:
    kind: str
    severity: str
    message: str
    field: str = ""
    item_id: str = ""
    source_kind: str = ""


def load_requirements_taxonomy(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config_file = root_path / CONFIG_PATH
    with config_file.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"requirements taxonomy must be a mapping: {config_file}")
    return data


def _list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _require_non_empty(findings: list[RequirementFinding], value: Any, field: str) -> None:
    if value:
        return
    findings.append(
        RequirementFinding(
            kind="missing_required_field",
            severity="error",
            field=field,
            message=f"confirmed_requirements.{field} is required",
        )
    )


def _check_roles(findings: list[RequirementFinding], roles: list[Any]) -> None:
    for role in roles:
        item = _dict(role)
        role_id = str(item.get("role_id") or "")
        if not role_id:
            findings.append(
                RequirementFinding(
                    kind="role_missing_id",
                    severity="error",
                    field="roles",
                    message="role has no role_id",
                )
            )
            continue
        if not _list(item.get("responsibilities")):
            findings.append(
                RequirementFinding(
                    kind="role_missing_responsibilities",
                    severity="error",
                    field="roles",
                    item_id=role_id,
                    message=f"role {role_id} has no responsibilities",
                )
            )
        if not str(item.get("boundary") or ""):
            findings.append(
                RequirementFinding(
                    kind="role_missing_boundary",
                    severity="error",
                    field="roles",
                    item_id=role_id,
                    message=f"role {role_id} has no boundary",
                )
            )


def _check_user_stories(findings: list[RequirementFinding], user_stories: list[Any]) -> None:
    for story in user_stories:
        item = _dict(story)
        story_id = str(item.get("story_id") or "")
        if not story_id:
            findings.append(
                RequirementFinding(
                    kind="user_story_missing_id",
                    severity="error",
                    field="user_stories",
                    message="user story has no story_id",
                )
            )
            continue
        for field in ["role_id", "goal", "value"]:
            if not str(item.get(field) or ""):
                findings.append(
                    RequirementFinding(
                        kind="user_story_missing_field",
                        severity="error",
                        field=field,
                        item_id=story_id,
                        message=f"user_story {story_id} has no {field}",
                    )
                )
        if not _list(item.get("acceptance_function_refs")):
            findings.append(
                RequirementFinding(
                    kind="user_story_missing_acceptance_refs",
                    severity="error",
                    field="acceptance_function_refs",
                    item_id=story_id,
                    message=f"user_story {story_id} has no acceptance_function_refs",
                )
            )


def _check_acceptance_functions(
    findings: list[RequirementFinding],
    acceptance_functions: list[Any],
    user_story_ids: set[str],
) -> None:
    for function in acceptance_functions:
        item = _dict(function)
        function_id = str(item.get("function_id") or "")
        if not function_id:
            findings.append(
                RequirementFinding(
                    kind="acceptance_function_missing_id",
                    severity="error",
                    field="acceptance_functions",
                    message="acceptance function has no function_id",
                )
            )
            continue
        refs = [str(ref) for ref in _list(item.get("user_story_refs")) if str(ref)]
        if not refs:
            findings.append(
                RequirementFinding(
                    kind="acceptance_function_missing_user_story_refs",
                    severity="error",
                    field="user_story_refs",
                    item_id=function_id,
                    message=f"acceptance_function {function_id} has no user_story_refs",
                )
            )
        for ref in refs:
            if ref not in user_story_ids:
                findings.append(
                    RequirementFinding(
                        kind="acceptance_function_unknown_user_story_ref",
                        severity="error",
                        field="user_story_refs",
                        item_id=function_id,
                        message=f"acceptance_function {function_id} references unknown user_story {ref}",
                    )
                )
        if not str(item.get("observable_result") or ""):
            findings.append(
                RequirementFinding(
                    kind="acceptance_function_missing_observable_result",
                    severity="error",
                    field="observable_result",
                    item_id=function_id,
                    message=f"acceptance_function {function_id} has no observable_result",
                )
            )


def _design_evidence_warnings(case_data: dict[str, Any]) -> list[RequirementFinding]:
    warnings: list[RequirementFinding] = []
    for item in _list(case_data.get("design_evidence")):
        evidence = _dict(item)
        source_kind = str(evidence.get("kind") or "design_evidence")
        warnings.append(
            RequirementFinding(
                kind="design_evidence_present",
                severity="warn",
                source_kind=source_kind,
                message=f"{source_kind} is classified as design evidence, not requirement authority",
            )
        )
    return warnings


def build_report(case_path: Path | str, root: Path | str = ROOT) -> dict[str, Any]:
    load_requirements_taxonomy(root)
    case_data = load_requirements_case_file(case_path)
    confirmed = _dict(case_data.get("confirmed_requirements"))
    findings: list[RequirementFinding] = []

    _require_non_empty(findings, confirmed.get("domain"), "domain")
    roles = _list(confirmed.get("roles"))
    stories = _list(confirmed.get("user_stories"))
    functions = _list(confirmed.get("acceptance_functions"))
    _require_non_empty(findings, roles, "roles")
    _require_non_empty(findings, stories, "user_stories")
    _require_non_empty(findings, functions, "acceptance_functions")
    _check_roles(findings, roles)
    _check_user_stories(findings, stories)
    story_ids = {str(_dict(story).get("story_id")) for story in stories if str(_dict(story).get("story_id"))}
    _check_acceptance_functions(findings, functions, story_ids)

    soft_warning_findings = _design_evidence_warnings(case_data)
    error_findings = [finding for finding in findings if finding.severity == "error"]
    passed = not error_findings
    blocking_reasons = [finding.message for finding in error_findings]
    return {
        "case_path": str(case_path),
        "passed": passed,
        "status": "requirements_ready" if passed else "blocked",
        "blocking_reasons": blocking_reasons,
        "soft_warnings": [asdict(finding) for finding in soft_warning_findings],
        "findings": [asdict(finding) for finding in [*findings, *soft_warning_findings]],
        "proof_boundary": [
            "This checker validates requirement readiness only.",
            "It does not validate API, DDL, architecture, release, or implementation correctness.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check requirements case readiness.")
    parser.add_argument("case_path")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--json-output")
    args = parser.parse_args()

    report = build_report(Path(args.case_path), Path(args.root))
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.json_output:
        Path(args.json_output).write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run checker tests to verify they pass**

Run:

```bash
python3 -m unittest tests.test_requirements_checker
```

Expected: pass.

- [ ] **Step 5: Commit**

Run:

```bash
git add scripts/check_requirements_case.py tests/test_requirements_checker.py
git commit -m "feat: check requirements readiness"
```

Expected: commit includes checker hard gate and tests.

## Task 5: Add Intent And Domain Recognition

**Files:**
- Create: `scripts/requirements_analysis_agent.py`
- Create: `tests/test_requirements_analysis_agent.py`

- [ ] **Step 1: Write failing intent and domain tests**

Create `tests/test_requirements_analysis_agent.py`:

```python
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_analysis_agent import classify_requirement_intent, resolve_requirement_domain


class RequirementsAnalysisAgentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-agent-test-"))
        config_dir = self.tmpdir / "requirements" / "config"
        config_dir.mkdir(parents=True)
        (config_dir / "requirements-taxonomy.yaml").write_text(
            """version: 1
domains:
  account-clearing:
    aliases:
      - account
      - clearing
      - 账户
      - 清算
role_sets:
  account-clearing:
    business_actors: [merchant]
    operation_owners: [product_owner]
    system_actors: [account_system]
    delivery_owners: [engineering_owner]
hard_gate:
  required: [domain, roles, user_stories, acceptance_functions]
""",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_classifies_first_version_intents(self) -> None:
        self.assertEqual(classify_requirement_intent("这是一份新需求文档").intent, "new_requirement_intake")
        self.assertEqual(classify_requirement_intent("补充这个 case 的材料").intent, "append_material")
        self.assertEqual(classify_requirement_intent("诊断需求缺口").intent, "diagnose_requirement")
        self.assertEqual(classify_requirement_intent("确认领域是账户清算").intent, "confirm_requirement")
        self.assertEqual(classify_requirement_intent("规范化需求").intent, "normalize_requirement")
        self.assertEqual(classify_requirement_intent("检查是否可以进入 OpenSpec").intent, "check_requirements_ready")
        self.assertEqual(classify_requirement_intent("生成 OpenSpec 草案").intent, "create_openspec_draft")
        self.assertEqual(classify_requirement_intent("看下状态").intent, "status")

    def test_resolves_known_account_clearing_domain(self) -> None:
        result = resolve_requirement_domain("账户 清算 结算 分账", self.tmpdir)

        self.assertEqual(result["status"], "matched")
        self.assertEqual(result["matched_domain"], "account-clearing")
        self.assertFalse(result["requires_user_confirmation"])

    def test_surfaces_wallet_payment_candidate_without_forcing_domain(self) -> None:
        result = resolve_requirement_domain("钱包 支付密码 绑卡 余额支付 银行卡轮询扣款", self.tmpdir)

        self.assertEqual(result["status"], "candidate_pending")
        self.assertEqual(result["matched_domain"], "")
        self.assertEqual(result["candidate_domains"][0]["domain_id"], "wallet-payment")
        self.assertTrue(result["requires_user_confirmation"])
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent
```

Expected: fail because `scripts.requirements_analysis_agent` does not exist.

- [ ] **Step 3: Implement intent and domain recognition**

Create `scripts/requirements_analysis_agent.py`:

```python
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from scripts.check_requirements_case import load_requirements_taxonomy


@dataclass(frozen=True)
class IntentResult:
    intent: str
    reason: str = ""


def classify_requirement_intent(text: str) -> IntentResult:
    lowered = text.lower()
    if any(token in lowered for token in ["openspec", "草案", "proposal", "spec draft"]):
        return IntentResult("create_openspec_draft", "user requested OpenSpec draft")
    if any(token in lowered for token in ["可以进入", "ready", "门禁", "检查是否", "能不能写代码"]):
        return IntentResult("check_requirements_ready", "user requested readiness check")
    if any(token in lowered for token in ["规范化", "normalize"]):
        return IntentResult("normalize_requirement", "user requested normalization")
    if any(token in lowered for token in ["确认", "confirm"]):
        return IntentResult("confirm_requirement", "user confirmed requirement facts")
    if any(token in lowered for token in ["诊断", "缺口", "diagnose"]):
        return IntentResult("diagnose_requirement", "user requested diagnosis")
    if any(token in lowered for token in ["补充", "append", "追加"]):
        return IntentResult("append_material", "user appended material")
    if any(token in lowered for token in ["状态", "status", "看下"]):
        return IntentResult("status", "user requested status")
    return IntentResult("new_requirement_intake", "default requirement intake")


def _domain_score(text: str, aliases: list[Any]) -> int:
    lowered = text.lower()
    score = 0
    for alias in aliases:
        value = str(alias).lower().strip()
        if value and value in lowered:
            score += 1
    return score


def _wallet_payment_candidate(text: str) -> dict[str, str] | None:
    signals = ["钱包", "wallet", "支付密码", "绑卡", "余额支付", "银行卡", "轮询扣款"]
    hit_count = sum(1 for signal in signals if signal.lower() in text.lower())
    if hit_count < 2:
        return None
    return {
        "domain_id": "wallet-payment",
        "confidence": "medium",
        "reason": "material mentions wallet account, payment password, card binding, or balance/card payment",
    }


def resolve_requirement_domain(text: str, root: Path | str) -> dict[str, Any]:
    taxonomy = load_requirements_taxonomy(root)
    domains = taxonomy.get("domains", {})
    if not isinstance(domains, dict):
        domains = {}
    scored: list[tuple[int, str]] = []
    for domain_id, config in domains.items():
        aliases = config.get("aliases", []) if isinstance(config, dict) else []
        score = _domain_score(text, aliases if isinstance(aliases, list) else [])
        if score > 0:
            scored.append((score, str(domain_id)))
    scored.sort(reverse=True)
    if scored and scored[0][0] >= 2:
        return {
            "status": "matched",
            "matched_domain": scored[0][1],
            "candidate_domains": [],
            "requires_user_confirmation": False,
        }
    candidates: list[dict[str, str]] = []
    wallet_candidate = _wallet_payment_candidate(text)
    if wallet_candidate:
        candidates.append(wallet_candidate)
    for score, domain_id in scored:
        candidates.append(
            {
                "domain_id": domain_id,
                "confidence": "low",
                "reason": f"matched {score} registered domain alias",
            }
        )
    return {
        "status": "candidate_pending",
        "matched_domain": "",
        "candidate_domains": candidates,
        "requires_user_confirmation": True,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent
```

Expected: pass.

- [ ] **Step 5: Commit**

Run:

```bash
git add scripts/requirements_analysis_agent.py tests/test_requirements_analysis_agent.py
git commit -m "feat: classify requirements intent"
```

Expected: commit includes agent intent/domain recognition and tests.

## Task 6: Add Agent Status CLI

**Files:**
- Modify: `scripts/requirements_analysis_agent.py`
- Create: `scripts/build_requirements_analysis_agent.py`
- Modify: `tests/test_requirements_analysis_agent.py`

- [ ] **Step 1: Add failing CLI status test**

Append to `tests/test_requirements_analysis_agent.py`:

```python
    def test_cli_outputs_intent_domain_and_next_action(self) -> None:
        import json
        import subprocess
        import sys

        repo_root = Path(__file__).resolve().parents[1]

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_requirements_analysis_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "这是一份 Embedded Wallet 新需求文档，包含钱包、支付密码、绑卡和余额支付",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["intent"], "new_requirement_intake")
        self.assertEqual(payload["domain_resolution"]["status"], "candidate_pending")
        self.assertEqual(payload["next_action"], "confirm_domain")
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTest.test_cli_outputs_intent_domain_and_next_action
```

Expected: fail because CLI script does not exist.

- [ ] **Step 3: Add status payload builder**

Append to `scripts/requirements_analysis_agent.py`:

```python
def build_status_payload(root: Path | str, intent_text: str) -> dict[str, Any]:
    intent = classify_requirement_intent(intent_text)
    domain_resolution = resolve_requirement_domain(intent_text, root)
    if domain_resolution["status"] == "matched":
        next_action = "normalize_requirement"
    elif domain_resolution["status"] == "candidate_pending":
        next_action = "confirm_domain"
    else:
        next_action = "diagnose_requirement"
    return {
        "intent": intent.intent,
        "intent_reason": intent.reason,
        "case_path": "",
        "domain_resolution": domain_resolution,
        "gate": {
            "status": "not_checked",
            "blocking_reasons": [],
        },
        "next_action": next_action,
    }
```

- [ ] **Step 4: Add CLI wrapper**

Create `scripts/build_requirements_analysis_agent.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.requirements_analysis_agent import build_status_payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the requirements analysis agent.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--intent-text", required=True)
    args = parser.parse_args()

    payload = build_status_payload(Path(args.root).resolve(), args.intent_text)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run CLI test to verify it passes**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTest.test_cli_outputs_intent_domain_and_next_action
```

Expected: pass.

- [ ] **Step 6: Commit**

Run:

```bash
git add scripts/requirements_analysis_agent.py scripts/build_requirements_analysis_agent.py tests/test_requirements_analysis_agent.py
git commit -m "feat: add requirements agent cli"
```

Expected: commit includes CLI status route.

## Task 7: Add OpenSpec Draft Handoff

**Files:**
- Modify: `scripts/requirements_analysis_agent.py`
- Modify: `tests/test_requirements_analysis_agent.py`

- [ ] **Step 1: Add failing draft-block and draft-create tests**

Append to `tests/test_requirements_analysis_agent.py`:

```python
    def _ready_case_path(self) -> Path:
        from scripts.requirements_case import build_requirements_case_package, write_requirements_case_file

        package = build_requirements_case_package(
            title="Split Account Opening",
            intent="new_requirement_intake",
            confirmed_domain="account-clearing",
            timestamp="2026-05-29T01:02:03+00:00",
        )
        package["status"] = "requirements_ready"
        package["confirmed_requirements"]["roles"] = [
            {
                "role_id": "merchant",
                "role_type": "business_actor",
                "responsibilities": ["initiates wallet opening"],
                "boundary": "merchant-facing business actor",
                "user_story_refs": ["US-001"],
            }
        ]
        package["confirmed_requirements"]["user_stories"] = [
            {
                "story_id": "US-001",
                "role_id": "merchant",
                "goal": "open a wallet for a member",
                "value": "member can pay inside merchant platform",
                "acceptance_function_refs": ["AF-001"],
            }
        ]
        package["confirmed_requirements"]["acceptance_functions"] = [
            {
                "function_id": "AF-001",
                "name": "wallet opening",
                "user_story_refs": ["US-001"],
                "observable_result": "wallet account status is opened",
            }
        ]
        return write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "requirements" / "cases",
            timestamp="2026-05-29T01:02:03+00:00",
        )

    def test_blocks_openspec_draft_for_unready_case(self) -> None:
        from scripts.requirements_analysis_agent import create_openspec_draft
        from scripts.requirements_case import build_requirements_case_package, write_requirements_case_file

        package = build_requirements_case_package(
            title="Blocked Requirement",
            intent="new_requirement_intake",
            timestamp="2026-05-29T01:02:03+00:00",
        )
        case_path = write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "requirements" / "cases",
            timestamp="2026-05-29T01:02:03+00:00",
        )

        result = create_openspec_draft(self.tmpdir, case_path, "add-blocked-requirement")

        self.assertFalse(result["created"])
        self.assertEqual(result["blocked_reason"], "requirements_not_ready")
        self.assertFalse((self.tmpdir / "openspec" / "changes" / "add-blocked-requirement").exists())

    def test_creates_traceable_openspec_draft_for_ready_case(self) -> None:
        from scripts.requirements_analysis_agent import create_openspec_draft

        case_path = self._ready_case_path()

        result = create_openspec_draft(self.tmpdir, case_path, "add-split-account-opening")

        self.assertTrue(result["created"])
        change_dir = self.tmpdir / "openspec" / "changes" / "add-split-account-opening"
        self.assertTrue((change_dir / "proposal.md").exists())
        spec_text = (change_dir / "specs" / "split-account-opening" / "spec.md").read_text(encoding="utf-8")
        self.assertIn("US-001", spec_text)
        self.assertIn("AF-001", spec_text)
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTest.test_blocks_openspec_draft_for_unready_case tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTest.test_creates_traceable_openspec_draft_for_ready_case
```

Expected: fail because `create_openspec_draft` does not exist.

- [ ] **Step 3: Implement OpenSpec draft handoff**

Append to `scripts/requirements_analysis_agent.py`:

```python
import json

from scripts.check_requirements_case import build_report as build_requirements_report
from scripts.requirements_case import load_requirements_case_file


def _slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "requirements-capability"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def create_openspec_draft(root: Path | str, case_path: Path | str, change_id: str) -> dict[str, Any]:
    root_path = Path(root)
    report = build_requirements_report(case_path, root_path)
    if not report["passed"]:
        return {
            "created": False,
            "blocked_reason": "requirements_not_ready",
            "blocking_reasons": report["blocking_reasons"],
            "draft_paths": [],
        }
    case_data = load_requirements_case_file(case_path)
    confirmed = case_data["confirmed_requirements"]
    title = str(case_data.get("title") or change_id)
    capability = _slugify(title)
    change_dir = root_path / "openspec" / "changes" / change_id
    spec_dir = change_dir / "specs" / capability
    stories = confirmed.get("user_stories", [])
    functions = confirmed.get("acceptance_functions", [])

    story_lines = "\n".join(
        f"- `{story['story_id']}` role=`{story['role_id']}` goal={story['goal']} value={story['value']}"
        for story in stories
    )
    function_lines = "\n".join(
        f"- `{function['function_id']}` {function['name']} -> {function['observable_result']}"
        for function in functions
    )
    _write(
        change_dir / "proposal.md",
        "\n".join(
            [
                f"# {change_id}",
                "",
                "## Why",
                "",
                f"The confirmed requirements case `{Path(case_path).as_posix()}` is ready for OpenSpec draft review.",
                "",
                "## What Changes",
                "",
                story_lines,
                "",
                "## Out of Scope",
                "",
                "- Detailed API, DDL, release, and architecture claims remain candidate evidence until separately reviewed.",
                "",
            ]
        ),
    )
    _write(
        change_dir / "design.md",
        "\n".join(
            [
                "# Design",
                "",
                "## Requirement Source",
                "",
                f"- Case: `{Path(case_path).as_posix()}`",
                f"- Domain: `{confirmed.get('domain', '')}`",
                "",
                "## Acceptance Functions",
                "",
                function_lines,
                "",
                "## Candidate Evidence Boundary",
                "",
                "Design evidence from the requirements case is not implementation authority until reviewed.",
                "",
            ]
        ),
    )
    task_lines = "\n".join(
        f"- [ ] Implement and verify `{function['function_id']}`: {function['name']}"
        for function in functions
    )
    _write(change_dir / "tasks.md", "# Tasks\n\n" + task_lines + "\n")
    scenario_blocks = []
    for function in functions:
        refs = ", ".join(function.get("user_story_refs", []))
        scenario_blocks.append(
            "\n".join(
                [
                    f"### Requirement: {function['name']} SHALL satisfy `{function['function_id']}`",
                    "",
                    f"Trace: acceptance `{function['function_id']}`, user stories `{refs}`.",
                    "",
                    "#### Scenario: Acceptance function is observable",
                    "",
                    f"- **WHEN** the implementation handles `{function['name']}`",
                    f"- **THEN** {function['observable_result']}",
                    "",
                ]
            )
        )
    _write(
        spec_dir / "spec.md",
        "# requirements draft spec\n\n## ADDED Requirements\n\n" + "\n".join(scenario_blocks),
    )
    return {
        "created": True,
        "blocked_reason": "",
        "draft_paths": [
            (change_dir / "proposal.md").as_posix(),
            (change_dir / "design.md").as_posix(),
            (change_dir / "tasks.md").as_posix(),
            (spec_dir / "spec.md").as_posix(),
        ],
    }
```

- [ ] **Step 4: Run OpenSpec handoff tests**

Run:

```bash
python3 -m unittest tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTest.test_blocks_openspec_draft_for_unready_case tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTest.test_creates_traceable_openspec_draft_for_ready_case
```

Expected: pass.

- [ ] **Step 5: Commit**

Run:

```bash
git add scripts/requirements_analysis_agent.py tests/test_requirements_analysis_agent.py
git commit -m "feat: draft openspec from requirements"
```

Expected: commit includes OpenSpec draft handoff.

## Task 8: Run Verification And Stop At OpenSpec Hard Stop

**Files:**
- Modify: `openspec/changes/add-requirements-analysis-agent/tasks.md`
- Create or Modify: `openspec/changes/add-requirements-analysis-agent/evaluation.md`

- [ ] **Step 1: Run focused Python tests**

Run:

```bash
python3 -m unittest tests.test_requirements_case tests.test_requirements_checker tests.test_requirements_analysis_agent
```

Expected: pass.

- [ ] **Step 2: Run OpenSpec strict validation**

Run:

```bash
openspec validate add-requirements-analysis-agent --strict
```

Expected: pass. If unavailable, record the exact command failure in
`evaluation.md`.

- [ ] **Step 3: Add evaluation evidence**

Create `openspec/changes/add-requirements-analysis-agent/evaluation.md` after
running the commands. Use this exact structure, with the `Result` cells filled
with the observed command outcome:

```markdown
# Evaluation

## Verification

| Check | Command | Result |
| --- | --- | --- |
| Focused unit tests | `python3 -m unittest tests.test_requirements_case tests.test_requirements_checker tests.test_requirements_analysis_agent` | Use the observed pass/fail output from Step 1. |
| OpenSpec strict validation | `openspec validate add-requirements-analysis-agent --strict` | Use the observed pass/fail output from Step 2. |

## Behavior Replay

| Scenario | Expected |
| --- | --- |
| New wallet-like material | Agent returns `new_requirement_intake` and domain candidate `wallet-payment`; it does not force `account-clearing`. |
| Known account-clearing material | Agent returns matched domain `account-clearing`. |
| Missing acceptance mapping | Checker blocks requirements readiness. |
| API/DDL evidence present | Checker emits soft warning without blocking hard gate. |
| OpenSpec draft requested before readiness | Agent blocks draft creation. |
| OpenSpec draft requested after readiness | Agent creates proposal, design, tasks, and spec draft with user-story and acceptance-function traces. |

## Proof Boundary

This change validates requirement readiness only. It does not validate API,
DDL, architecture, release readiness, implementation correctness, or production
acceptance.
```

Do not commit `evaluation.md` until the `Result` cells contain the actual
observed pass/fail result.

- [ ] **Step 4: Mark tasks complete**

Update `openspec/changes/add-requirements-analysis-agent/tasks.md` so completed
items are checked. Do not check an item until its evidence exists.

- [ ] **Step 5: Commit final verified implementation**

Run:

```bash
git add openspec/changes/add-requirements-analysis-agent scripts/requirements_case.py scripts/check_requirements_case.py scripts/requirements_analysis_agent.py scripts/build_requirements_analysis_agent.py requirements/config/requirements-taxonomy.yaml tests/test_requirements_case.py tests/test_requirements_checker.py tests/test_requirements_analysis_agent.py
git commit -m "feat: add requirements analysis agent"
```

Expected: commit includes only task-related implementation, tests, and OpenSpec evaluation.

- [ ] **Step 6: Stop at OpenSpec hard stop**

After all checkboxes in `openspec/changes/add-requirements-analysis-agent/tasks.md`
are complete, stop implementation. The next default action is archive review,
not automatic archive.

## Self-Review Checklist

- Spec coverage:
  - Intent recognition is covered in Task 5 and Task 6.
  - Domain candidates and unknown-domain behavior are covered in Task 5.
  - Independent requirements taxonomy is covered in Task 2.
  - Case file shape is covered in Task 3.
  - Hard gate and soft warnings are covered in Task 4.
  - OpenSpec draft handoff is covered in Task 7.
  - OpenSpec lifecycle authority is covered in Task 1 and Task 8.
- Placeholder scan:
  - The plan avoids unfinished-marker language and vague edge-condition instructions.
  - The evaluation step requires actual command output before commit.
- Type consistency:
  - Case data uses `confirmed_requirements.domain`, `roles`, `user_stories`, and `acceptance_functions`.
  - User stories use `story_id`, `role_id`, `goal`, `value`, and `acceptance_function_refs`.
  - Acceptance functions use `function_id`, `name`, `user_story_refs`, and `observable_result`.
