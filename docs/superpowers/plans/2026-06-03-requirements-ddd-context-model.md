# Requirements DDD Context Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the first OpenSpec change that replaces the flat requirements taxonomy with a DDD context model for payment and Agent-service ecosystems.

**Architecture:** This plan implements only `replace-requirements-taxonomy-with-ddd-context-model`. It creates the OpenSpec change, adds a focused taxonomy-structure validator, replaces `requirements/config/requirements-taxonomy.yaml` with version 2 DDD model data, and records validation. It intentionally does not modify `check_requirements_case.py`, req-agent behavior, or historical cases.

**Tech Stack:** OpenSpec markdown specs, YAML, Python standard library, PyYAML, `unittest`.

---

### Task 1: Create OpenSpec Change Artifacts

**Files:**
- Create: `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/proposal.md`
- Create: `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/design.md`
- Create: `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/tasks.md`
- Create: `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/specs/requirements-ddd-context-model/spec.md`

- [ ] **Step 1: Create proposal**

Create `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/proposal.md`:

```markdown
# Proposal

## Why

The current requirements taxonomy is a flat `domains` and `roles` vocabulary.
It can classify simple requirements, but it cannot carry DDD concepts such as
business ecosystem, subdomain, bounded context, aggregate root, lifecycle,
invariant, context handoff, fact owner, role obligation, or candidate evolution.

That gap caused the Agent service subscription payment draft to miss the
`account_balance` collaboration and funds/ledger owners after real funds
processing was confirmed.

## What Changes

- Replace the flat requirements taxonomy model with a DDD context model.
- Define `payment_ecosystem` and `agent_service_ecosystem`.
- Define payment subdomains, bounded contexts, aggregate roots, fact owners, and
  disambiguation rules.
- Define context-map handoffs for command, event, policy decision, and evidence.
- Define candidate subdomain/context evolution rules.
- Add a DDD taxonomy structure validator for this model.
- Include the Agent service subscription payment case mapping example.

## What Does Not Change

- Does not update `check_requirements_case.py`.
- Does not update `req-agent`, `req-domain-analysis`, or `req-scope` runtime behavior.
- Does not migrate historical requirement cases.
- Does not archive previous OpenSpec changes.
- Does not publish the final Feishu standard.

## Source Design

- `docs/superpowers/specs/2026-06-03-requirements-ddd-context-model-design.md`
```

- [ ] **Step 2: Create design**

Create `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/design.md` with these exact sections:

```markdown
# Design

## Scope

This change replaces the requirements taxonomy data model with a DDD context
model. It is a standards and configuration change with a structural validator.
It does not change the current requirements readiness gate or req-agent runtime
behavior.

## Model Layers

- `business_ecosystem`: broad ecosystem such as `payment_ecosystem`.
- `subdomain`: stable business problem space inside an ecosystem.
- `bounded_context`: model boundary with consistent language, aggregate
  lifecycle, rules, and fact ownership.
- `aggregate_root`: object that owns lifecycle and consistency rules.
- `context_map`: command, event, policy decision, query, report, or evidence
  handoff between contexts.
- `role_obligation`: fact-owner role required because a context, aggregate,
  handoff, or trigger rule is present.
- `candidate_subdomain` and `candidate_context`: proposed model extensions when
  existing skeleton cannot explain a requirement.

## Ecosystem Skeleton

The first model includes `payment_ecosystem` and adjacent
`agent_service_ecosystem`.

`payment_ecosystem` subdomains:

- `merchant_platform_relationship`
- `billing_revenue`
- `payment_transaction`
- `account_balance`
- `funds_movement_settlement`
- `financial_operations`
- `risk_compliance`
- `embedded_financial_products`

`agent_service_ecosystem` subdomains:

- `agent_entitlement`
- `agent_usage_metering`
- `agent_workspace_seat`
- `agent_service_catalog`
- `agent_service_delivery`

## Disambiguation

High-conflict terms are context-specific language, not global objects. The model
must disambiguate terms such as `subscription`, `account`, `settlement`,
`payment`, `balance`, `merchant`, `entitlement`, `invoice`, and `refund`.

## Trigger Rules

`real_funds_processing=true` requires:

- `account_balance`
- `balance_ledger_context`
- `funds_account_owner`
- `ledger_owner`
- `balance_state_owner`

`paid_agent_service_access=true` requires:

- `agent_service_ecosystem`
- `agent_entitlement_context`

`recurring_payment=true` requires:

- `mandate_authorization_context`

## Proof Boundary

This change proves the DDD model exists in taxonomy and passes structural
validation. It does not prove old readiness checker compatibility and does not
prove runtime req-agent output changes.
```

- [ ] **Step 3: Create tasks ledger**

Create `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/tasks.md`:

```markdown
# Tasks

- [ ] 1. Add requirements DDD context model OpenSpec spec.
- [ ] 2. Add DDD taxonomy structure validator and focused tests.
- [ ] 3. Replace requirements taxonomy with version 2 DDD context model.
- [ ] 4. Validate DDD taxonomy structure.
- [ ] 5. Validate OpenSpec change.
- [ ] 6. Record verification results and proof boundary.
```

- [ ] **Step 4: Create OpenSpec spec**

Create `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/specs/requirements-ddd-context-model/spec.md`:

```markdown
## ADDED Requirements

### Requirement: Requirements Taxonomy Uses DDD Context Model

The requirements taxonomy SHALL use a DDD context model instead of a flat
domain/role vocabulary as the authoritative model for new requirement domain
analysis.

#### Scenario: Taxonomy exposes DDD model roots

- **GIVEN** `requirements/config/requirements-taxonomy.yaml`
- **WHEN** the taxonomy is loaded
- **THEN** it SHALL include `business_ecosystems`, `subdomains`,
  `bounded_contexts`, `role_archetypes`, `context_map`,
  `case_classification`, `candidate_evolution`, and `readiness_gate_model`.

### Requirement: Payment Ecosystem Skeleton

The requirements taxonomy SHALL define the first `payment_ecosystem` skeleton
with stable subdomains for merchant/platform relationship, billing/revenue,
payment transaction, account/balance, funds movement/settlement, financial
operations, risk/compliance, and embedded financial products.

#### Scenario: Payment subdomains are explicit

- **GIVEN** the DDD taxonomy model
- **WHEN** `payment_ecosystem` is inspected
- **THEN** it SHALL include `merchant_platform_relationship`,
  `billing_revenue`, `payment_transaction`, `account_balance`,
  `funds_movement_settlement`, `financial_operations`, `risk_compliance`, and
  `embedded_financial_products`.

### Requirement: Agent Service Ecosystem Is Adjacent

The requirements taxonomy SHALL define `agent_service_ecosystem` as an adjacent
ecosystem for Agent entitlement, usage metering, workspace seats, service
catalog, and service delivery.

#### Scenario: Agent entitlement is not absorbed by payment

- **GIVEN** a paid Agent service requirement
- **WHEN** service access is controlled by payment or subscription state
- **THEN** the model SHALL map access control to
  `agent_service_ecosystem.agent_entitlement_context`.
- **AND** it SHALL NOT treat service access entitlement as a payment subdomain.

### Requirement: High-Conflict Terms Are Context-Specific

The requirements taxonomy SHALL treat high-conflict business terms as
context-specific language instead of globally shared objects.

#### Scenario: Subscription is disambiguated

- **GIVEN** a requirement mentions subscription
- **WHEN** the model maps the term
- **THEN** merchant subscription offering, commercial subscription, and Agent
  entitlement SHALL be represented in separate contexts.

### Requirement: Real Funds Processing Requires Account Balance

The requirements taxonomy SHALL encode a trigger rule that real funds processing
requires account/balance contexts and funds/ledger ownership.

#### Scenario: Real funds processing is in scope

- **GIVEN** `real_funds_processing=true`
- **WHEN** the case is mapped
- **THEN** `account_balance` and `balance_ledger_context` SHALL be required.
- **AND** `funds_account_owner`, `ledger_owner`, and `balance_state_owner` SHALL
  be required role obligations.

### Requirement: Candidate Evolution Is Explicit

The requirements taxonomy SHALL allow requirements to propose candidate
subdomains or bounded contexts only when existing skeletons cannot explain the
case.

#### Scenario: New term does not immediately become taxonomy

- **GIVEN** a requirement introduces a new business term
- **WHEN** existing subdomains or contexts cannot explain it
- **THEN** the model SHALL keep the item as `candidate_subdomain` or
  `candidate_context`.
- **AND** promotion SHALL require business problem, ubiquitous language,
  aggregate roots, lifecycle, invariants, fact owners, context map, and why
  existing contexts do not fit.
```

- [ ] **Step 5: Commit OpenSpec scaffold**

Run:

```bash
git add openspec/changes/replace-requirements-taxonomy-with-ddd-context-model
git commit -m "docs: propose requirements DDD context model"
```

Expected: commit includes only the new OpenSpec change files.

### Task 2: Add DDD Taxonomy Validator With Tests

**Files:**
- Create: `tests/test_requirements_ddd_taxonomy.py`
- Create: `scripts/check_requirements_ddd_taxonomy.py`

- [ ] **Step 1: Write failing validator tests**

Create `tests/test_requirements_ddd_taxonomy.py`:

```python
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.check_requirements_ddd_taxonomy import validate_taxonomy_file


class RequirementsDDDTaxonomyTests(unittest.TestCase):
    def _write_taxonomy(self, data: dict) -> Path:
        tmpdir = Path(tempfile.mkdtemp(prefix="ddd-taxonomy-test-"))
        path = tmpdir / "requirements-taxonomy.yaml"
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        self.addCleanup(lambda: path.unlink(missing_ok=True))
        self.addCleanup(lambda: tmpdir.rmdir())
        return path

    def _minimal_valid_taxonomy(self) -> dict:
        return {
            "version": 2,
            "authority": "requirements-ddd-model",
            "business_ecosystems": {
                "payment_ecosystem": {
                    "subdomains": ["billing_revenue", "account_balance"],
                },
                "agent_service_ecosystem": {
                    "subdomains": ["agent_entitlement"],
                },
            },
            "subdomains": {
                "billing_revenue": {
                    "business_ecosystem": "payment_ecosystem",
                    "bounded_contexts": ["commercial_subscription_context"],
                },
                "account_balance": {
                    "business_ecosystem": "payment_ecosystem",
                    "bounded_contexts": ["balance_ledger_context"],
                },
                "agent_entitlement": {
                    "business_ecosystem": "agent_service_ecosystem",
                    "bounded_contexts": ["agent_entitlement_context"],
                },
            },
            "bounded_contexts": {
                "commercial_subscription_context": {
                    "subdomain": "billing_revenue",
                    "aggregate_roots": ["commercial_subscription"],
                    "fact_owners": ["subscription_owner"],
                },
                "balance_ledger_context": {
                    "subdomain": "account_balance",
                    "aggregate_roots": ["payment_account", "balance", "ledger_entry", "fund_state"],
                    "fact_owners": ["funds_account_owner", "ledger_owner", "balance_state_owner"],
                },
                "agent_entitlement_context": {
                    "subdomain": "agent_entitlement",
                    "aggregate_roots": ["agent_entitlement"],
                    "fact_owners": ["agent_entitlement_owner"],
                },
            },
            "role_archetypes": {
                "subscription_owner": {"required_by_contexts": ["commercial_subscription_context"]},
                "funds_account_owner": {"required_by_contexts": ["balance_ledger_context"]},
                "ledger_owner": {"required_by_contexts": ["balance_ledger_context"]},
                "balance_state_owner": {"required_by_contexts": ["balance_ledger_context"]},
                "agent_entitlement_owner": {"required_by_contexts": ["agent_entitlement_context"]},
            },
            "context_map": [
                {
                    "id": "commercial_subscription_to_agent_entitlement",
                    "from_context": "commercial_subscription_context",
                    "to_context": "agent_entitlement_context",
                    "handoff_type": "domain_event",
                    "artifact": "CommercialSubscriptionActivated",
                }
            ],
            "case_classification": {
                "examples": {
                    "agent_service_subscription_payments": {
                        "business_ecosystem": "payment_ecosystem",
                        "adjacent_ecosystems": ["agent_service_ecosystem"],
                        "primary_subdomain": "billing_revenue",
                        "primary_contexts": ["commercial_subscription_context"],
                        "required_contexts": ["balance_ledger_context"],
                        "required_agent_service_contexts": ["agent_entitlement_context"],
                    }
                }
            },
            "candidate_evolution": {
                "promotion_required_fields": [
                    "business_problem",
                    "ubiquitous_language",
                    "aggregate_roots",
                    "lifecycle",
                    "invariants",
                    "fact_owners",
                    "context_map",
                    "why_existing_contexts_do_not_fit",
                ]
            },
            "readiness_gate_model": {
                "domain_model_gate": {
                    "required_fields": ["business_ecosystem", "primary_subdomain", "primary_contexts"]
                }
            },
        }

    def test_valid_minimal_taxonomy_passes(self) -> None:
        path = self._write_taxonomy(self._minimal_valid_taxonomy())

        report = validate_taxonomy_file(path)

        self.assertEqual(report["errors"], [])

    def test_missing_root_section_fails(self) -> None:
        data = self._minimal_valid_taxonomy()
        data.pop("bounded_contexts")
        path = self._write_taxonomy(data)

        report = validate_taxonomy_file(path)

        self.assertIn("missing root section: bounded_contexts", report["errors"])

    def test_unknown_context_reference_fails(self) -> None:
        data = self._minimal_valid_taxonomy()
        data["subdomains"]["billing_revenue"]["bounded_contexts"].append("missing_context")
        path = self._write_taxonomy(data)

        report = validate_taxonomy_file(path)

        self.assertIn("subdomain billing_revenue references unknown context missing_context", report["errors"])

    def test_real_funds_trigger_requires_balance_ledger_owner_set(self) -> None:
        data = self._minimal_valid_taxonomy()
        data["role_archetypes"].pop("ledger_owner")
        path = self._write_taxonomy(data)

        report = validate_taxonomy_file(path)

        self.assertIn("real funds trigger requires role archetype ledger_owner", report["errors"])
```

- [ ] **Step 2: Run tests and verify RED**

Run:

```bash
PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy
```

Expected: fail with `ModuleNotFoundError` or import error for
`scripts.check_requirements_ddd_taxonomy`.

- [ ] **Step 3: Implement validator**

Create `scripts/check_requirements_ddd_taxonomy.py`:

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


ROOT_SECTIONS = {
    "business_ecosystems",
    "subdomains",
    "bounded_contexts",
    "role_archetypes",
    "context_map",
    "case_classification",
    "candidate_evolution",
    "readiness_gate_model",
}

REAL_FUNDS_REQUIRED_CONTEXTS = {"balance_ledger_context"}
REAL_FUNDS_REQUIRED_ROLES = {"funds_account_owner", "ledger_owner", "balance_state_owner"}


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _string_items(value: Any) -> list[str]:
    return [str(item) for item in _as_list(value) if str(item).strip()]


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"taxonomy must be a YAML mapping: {path}")
    return data


def validate_taxonomy(data: dict[str, Any]) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for section in sorted(ROOT_SECTIONS):
        if section not in data:
            errors.append(f"missing root section: {section}")

    if data.get("version") != 2:
        errors.append("version must be 2")
    if data.get("authority") != "requirements-ddd-model":
        errors.append("authority must be requirements-ddd-model")

    ecosystems = _as_dict(data.get("business_ecosystems"))
    subdomains = _as_dict(data.get("subdomains"))
    contexts = _as_dict(data.get("bounded_contexts"))
    roles = _as_dict(data.get("role_archetypes"))

    for ecosystem_id, ecosystem in ecosystems.items():
        for subdomain_id in _string_items(_as_dict(ecosystem).get("subdomains")):
            if subdomain_id not in subdomains:
                errors.append(f"ecosystem {ecosystem_id} references unknown subdomain {subdomain_id}")

    for subdomain_id, subdomain in subdomains.items():
        subdomain_data = _as_dict(subdomain)
        ecosystem_id = str(subdomain_data.get("business_ecosystem", "")).strip()
        if ecosystem_id and ecosystem_id not in ecosystems:
            errors.append(f"subdomain {subdomain_id} references unknown ecosystem {ecosystem_id}")
        for context_id in _string_items(subdomain_data.get("bounded_contexts")):
            if context_id not in contexts:
                errors.append(f"subdomain {subdomain_id} references unknown context {context_id}")

    for context_id, context in contexts.items():
        context_data = _as_dict(context)
        subdomain_id = str(context_data.get("subdomain", "")).strip()
        if subdomain_id and subdomain_id not in subdomains:
            errors.append(f"context {context_id} references unknown subdomain {subdomain_id}")
        if not _string_items(context_data.get("aggregate_roots")):
            errors.append(f"context {context_id} must define aggregate_roots")
        for role_id in _string_items(context_data.get("fact_owners")):
            if role_id not in roles:
                errors.append(f"context {context_id} references unknown fact owner {role_id}")

    for role_id, role in roles.items():
        role_data = _as_dict(role)
        for context_id in _string_items(role_data.get("required_by_contexts")):
            if context_id not in contexts:
                errors.append(f"role archetype {role_id} references unknown context {context_id}")

    for item in _as_list(data.get("context_map")):
        handoff = _as_dict(item)
        handoff_id = str(handoff.get("id", "missing"))
        for field in ("from_context", "to_context"):
            context_id = str(handoff.get(field, "")).strip()
            if context_id and context_id not in contexts:
                errors.append(f"context map {handoff_id} references unknown {field} {context_id}")
        if str(handoff.get("handoff_type", "")).strip() not in {
            "command",
            "domain_event",
            "policy_decision",
            "query",
            "report",
            "evidence",
        }:
            errors.append(f"context map {handoff_id} has invalid handoff_type")

    for context_id in sorted(REAL_FUNDS_REQUIRED_CONTEXTS):
        if context_id not in contexts:
            errors.append(f"real funds trigger requires context {context_id}")
    for role_id in sorted(REAL_FUNDS_REQUIRED_ROLES):
        if role_id not in roles:
            errors.append(f"real funds trigger requires role archetype {role_id}")

    candidate = _as_dict(data.get("candidate_evolution"))
    required = set(_string_items(candidate.get("promotion_required_fields")))
    expected = {
        "business_problem",
        "ubiquitous_language",
        "aggregate_roots",
        "lifecycle",
        "invariants",
        "fact_owners",
        "context_map",
        "why_existing_contexts_do_not_fit",
    }
    for field in sorted(expected - required):
        errors.append(f"candidate evolution missing promotion field {field}")

    return {"errors": errors, "warnings": warnings}


def validate_taxonomy_file(path: Path | str) -> dict[str, list[str]]:
    return validate_taxonomy(_load_yaml(Path(path)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate requirements DDD taxonomy structure.")
    parser.add_argument("--taxonomy", default="requirements/config/requirements-taxonomy.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    report = validate_taxonomy_file(args.taxonomy)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for error in report["errors"]:
            print(f"ERROR {error}")
        for warning in report["warnings"]:
            print(f"WARN {warning}")
        if not report["errors"] and not report["warnings"]:
            print("requirements DDD taxonomy is valid")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run tests and verify GREEN**

Run:

```bash
PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy
```

Expected: all tests pass.

- [ ] **Step 5: Commit validator**

Run:

```bash
git add scripts/check_requirements_ddd_taxonomy.py tests/test_requirements_ddd_taxonomy.py
git commit -m "test: add requirements DDD taxonomy validator"
```

Expected: commit includes only the validator and focused tests.

### Task 3: Replace Requirements Taxonomy With DDD Model

**Files:**
- Modify: `requirements/config/requirements-taxonomy.yaml`

- [ ] **Step 1: Run validator against old taxonomy and verify expected failure**

Run:

```bash
PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml
```

Expected: fail with errors including `version must be 2` and missing DDD root
sections. This is the correct RED check against the old flat taxonomy.

- [ ] **Step 2: Replace taxonomy with version 2 model**

Replace `requirements/config/requirements-taxonomy.yaml` with version 2 data
matching the design. The top-level document must start:

```yaml
version: 2
authority: requirements-ddd-model
independent_from:
  - wiki/config/frontmatter-taxonomy.yaml

business_ecosystems:
  payment_ecosystem:
    label: payment ecosystem
    description: Payment ecosystem for merchant, platform, subscription, payment, funds, settlement, financial operations, and risk/compliance requirements.
    subdomains:
      - merchant_platform_relationship
      - billing_revenue
      - payment_transaction
      - account_balance
      - funds_movement_settlement
      - financial_operations
      - risk_compliance
      - embedded_financial_products
  agent_service_ecosystem:
    label: Agent service ecosystem
    description: Adjacent Agent service ecosystem for service access, usage, seats, catalog, and delivery.
    subdomains:
      - agent_entitlement
      - agent_usage_metering
      - agent_workspace_seat
      - agent_service_catalog
      - agent_service_delivery
```

The file must define all subdomains, bounded contexts, role archetypes,
context-map entries, case classification examples, candidate evolution, and
readiness gate model from:

```text
docs/superpowers/specs/2026-06-03-requirements-ddd-context-model-design.md
```

Required root sections:

```yaml
subdomains:
bounded_contexts:
role_archetypes:
context_map:
case_classification:
candidate_evolution:
readiness_gate_model:
```

The `case_classification.examples.agent_service_subscription_payments` entry
must include:

```yaml
business_ecosystem: payment_ecosystem
adjacent_ecosystems:
  - agent_service_ecosystem
primary_subdomain: billing_revenue
primary_contexts:
  - commercial_subscription_context
  - billing_invoice_context
  - revenue_recovery_context
required_payment_subdomains:
  - merchant_platform_relationship
  - payment_transaction
  - account_balance
  - financial_operations
  - risk_compliance
required_agent_service_contexts:
  - agent_entitlement_context
trigger_rules:
  - if: real_funds_processing=true
    require_contexts:
      - balance_ledger_context
    require_role_archetypes:
      - funds_account_owner
      - ledger_owner
      - balance_state_owner
```

- [ ] **Step 3: Run validator against new taxonomy**

Run:

```bash
PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml
```

Expected:

```text
requirements DDD taxonomy is valid
```

- [ ] **Step 4: Run focused taxonomy tests**

Run:

```bash
PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy
```

Expected: all tests pass.

- [ ] **Step 5: Record old checker boundary**

Do not run `tests.test_requirements_checker_gate` as completion evidence for
this change. That checker reads the old `domains` and `roles` shape and is
covered by the later `rewrite-requirements-readiness-gate-for-ddd-model`
change.

- [ ] **Step 6: Commit taxonomy replacement**

Run:

```bash
git add requirements/config/requirements-taxonomy.yaml
git commit -m "docs: replace requirements taxonomy with DDD context model"
```

Expected: commit includes only the taxonomy file.

### Task 4: Add Verification Evidence To OpenSpec Tasks

**Files:**
- Modify: `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/tasks.md`

- [ ] **Step 1: Run final OpenSpec validation**

Run:

```bash
openspec validate replace-requirements-taxonomy-with-ddd-context-model --strict
```

Expected: OpenSpec validation passes. PostHog telemetry DNS errors after
validation are non-blocking if the process exits with code 0.

- [ ] **Step 2: Run final DDD taxonomy validation**

Run:

```bash
PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml
PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy
```

Expected: validator prints `requirements DDD taxonomy is valid`; tests pass.

- [ ] **Step 3: Update tasks ledger**

Update `openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/tasks.md`:

```markdown
# Tasks

- [x] 1. Add requirements DDD context model OpenSpec spec.
- [x] 2. Add DDD taxonomy structure validator and focused tests.
- [x] 3. Replace requirements taxonomy with version 2 DDD context model.
- [x] 4. Validate DDD taxonomy structure.
- [x] 5. Validate OpenSpec change.
- [x] 6. Record verification results and proof boundary.

## Verification

- `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml` -> valid.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_taxonomy` -> passed.
- `openspec validate replace-requirements-taxonomy-with-ddd-context-model --strict` -> valid.

## Proof Boundary

This change proves the DDD taxonomy model and structural validator. It does not
update the old requirements readiness checker or req-agent runtime behavior.
Those belong to follow-up changes.
```

- [ ] **Step 4: Commit verification ledger**

Run:

```bash
git add openspec/changes/replace-requirements-taxonomy-with-ddd-context-model/tasks.md
git commit -m "docs: verify requirements DDD context model"
```

Expected: commit includes only the tasks ledger.

### Task 5: Final Review Before Execution Completion

**Files:**
- No file edits unless a previous step produced a validation correction.

- [ ] **Step 1: Check latest commits**

Run:

```bash
git log -5 --oneline
```

Expected: latest commits include OpenSpec proposal, validator, taxonomy
replacement, and verification ledger.

- [ ] **Step 2: Check task-related status**

Run:

```bash
git status --short openspec/changes/replace-requirements-taxonomy-with-ddd-context-model scripts/check_requirements_ddd_taxonomy.py tests/test_requirements_ddd_taxonomy.py requirements/config/requirements-taxonomy.yaml
```

Expected: no task-related paths remain modified or untracked.

- [ ] **Step 3: Stop at OpenSpec completion boundary**

Do not start `rewrite-requirements-readiness-gate-for-ddd-model`.
Do not start `upgrade-req-agent-domain-analysis-for-ddd-contexts`.
Do not archive this change.
Report the completed first-change evidence and the explicit follow-up changes.

## Self-Review

Spec coverage:

- DDD taxonomy model roots are covered by Task 1 and Task 3.
- Payment and Agent-service ecosystem skeletons are covered by Task 3.
- High-conflict term disambiguation and candidate evolution are covered by Task
  1 spec and Task 3 taxonomy content.
- Validator evidence is covered by Task 2 and Task 4.
- Checker and req-agent behavior are explicitly deferred.

Placeholder scan:

- No `TBD`, `TODO`, or "implement later" steps are present.
- Deferred checker/req-agent work is a named non-goal with follow-up change IDs.

Type consistency:

- The validator function names are `validate_taxonomy` and
  `validate_taxonomy_file`.
- The taxonomy root sections match the OpenSpec requirement names and validator
  `ROOT_SECTIONS`.
