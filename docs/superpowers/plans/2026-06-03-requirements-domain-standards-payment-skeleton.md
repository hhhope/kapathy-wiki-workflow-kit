# Requirements Domain Standards And Payment Skeleton Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the first OpenSpec change for DDD requirements domain standards, the payment domain skeleton, and requirements taxonomy updates.

**Architecture:** This plan creates only the first approved change: `define-requirements-domain-standards-and-payment-skeleton`. It writes OpenSpec proposal/design/tasks/spec artifacts, updates `requirements/config/requirements-taxonomy.yaml` with the first runnable payment skeleton, and validates the change without implementing `req-domain-analysis`.

**Tech Stack:** OpenSpec markdown specs, YAML requirements taxonomy, existing requirements checker scripts.

---

### Task 1: Create OpenSpec Change Artifacts

**Files:**
- Create: `openspec/changes/define-requirements-domain-standards-and-payment-skeleton/proposal.md`
- Create: `openspec/changes/define-requirements-domain-standards-and-payment-skeleton/design.md`
- Create: `openspec/changes/define-requirements-domain-standards-and-payment-skeleton/tasks.md`
- Create: `openspec/changes/define-requirements-domain-standards-and-payment-skeleton/specs/requirements-domain-model/spec.md`

- [ ] **Step 1: Create the change directory and proposal**

Write `proposal.md` with the approved scope:

```markdown
# Proposal

## Why

The requirements taxonomy currently has only `account`, `settlement`, and
`clearing`. Those values are useful for local account and clearing/settlement
work, but they do not support broader payment ecosystem requirements or
AGI-era human-Agent collaboration.

The deeper need is a DDD-based domain model that turns fragmented requirements
knowledge into reusable cognitive assets for humans and Agents.

## What Changes

- Define DDD requirements domain standards.
- Define the first runnable payment domain skeleton.
- Define domain collaboration relationships.
- Define compounding asset expectations.
- Define taxonomy admission standards.
- Map current `account`, `clearing`, and `settlement` values to the new
  skeleton.
- Update `requirements/config/requirements-taxonomy.yaml` with the first
  payment skeleton.

## What Does Not Change

- Does not implement `req-domain-analysis`; that belongs to
  `add-req-domain-analysis-skill`.
- Does not batch-migrate historical requirements cases.
- Does not modify wiki frontmatter taxonomy.
- Does not authorize implementation from a requirements case.
```

- [ ] **Step 2: Create the design**

Write `design.md` with sections for strategic DDD basis, payment skeleton, taxonomy update strategy, compatibility mapping, and proof boundaries.

- [ ] **Step 3: Create the tasks ledger**

Write `tasks.md` with these checkboxes:

```markdown
# Tasks

- [ ] 1. Add requirements domain model OpenSpec spec.
- [ ] 2. Update requirements taxonomy with payment skeleton domains and aliases.
- [ ] 3. Record compatibility mapping for `account`, `clearing`, and `settlement`.
- [ ] 4. Verify requirements checker accepts the updated taxonomy.
- [ ] 5. Validate OpenSpec change.
```

- [ ] **Step 4: Commit OpenSpec scaffolding**

Run:

```bash
git add openspec/changes/define-requirements-domain-standards-and-payment-skeleton
git commit -m "docs: propose requirements domain standards change"
```

Expected: commit succeeds with only the new OpenSpec change files.

### Task 2: Write Requirements Domain Model Spec

**Files:**
- Modify: `openspec/changes/define-requirements-domain-standards-and-payment-skeleton/specs/requirements-domain-model/spec.md`

- [ ] **Step 1: Add domain standard requirements**

Add OpenSpec requirements with `SHALL` language for:

```text
Domain definition
Strategic DDD basis
Taxonomy admission classification
Payment domain skeleton
Existing taxonomy compatibility mapping
Domain collaboration relationships
Compounding assets
Agent subscription payment mapping
```

- [ ] **Step 2: Add scenarios**

Include scenarios that prove:

```text
feature/system/team/case names are not admitted as top-level domains
payment skeleton values are the first runnable skeleton
existing account/clearing/settlement values remain mappable
Agent subscription payment maps to billing/revenue primary domain
```

- [ ] **Step 3: Commit spec**

Run:

```bash
git add openspec/changes/define-requirements-domain-standards-and-payment-skeleton/specs/requirements-domain-model/spec.md
git commit -m "docs: specify requirements domain model"
```

Expected: commit succeeds with only the spec file.

### Task 3: Update Requirements Taxonomy

**Files:**
- Modify: `requirements/config/requirements-taxonomy.yaml`

- [ ] **Step 1: Add payment skeleton domains**

Add domain IDs and aliases for:

```text
merchant_platform_relationship
payment_transaction
billing_revenue
account_balance
funds_movement_settlement
financial_operations
risk_compliance
embedded_financial_products
```

Keep existing `account`, `settlement`, and `clearing` values for compatibility.

- [ ] **Step 2: Add descriptions that preserve boundaries**

Each new domain description should state the business problem space and avoid presenting features as domains.

- [ ] **Step 3: Commit taxonomy update**

Run:

```bash
git add requirements/config/requirements-taxonomy.yaml
git commit -m "docs: add payment domain taxonomy skeleton"
```

Expected: commit succeeds with only the taxonomy file.

### Task 4: Verify And Validate

**Files:**
- Modify: `openspec/changes/define-requirements-domain-standards-and-payment-skeleton/tasks.md`

- [ ] **Step 1: Run requirements-related checks**

Run:

```bash
python3 scripts/check_requirements_case.py --help
```

Expected: command may require `PYTHONPATH=.` if direct execution cannot import `scripts`; record the actual result.

- [ ] **Step 2: Run OpenSpec validation**

Run:

```bash
openspec validate define-requirements-domain-standards-and-payment-skeleton --strict
```

Expected: validation passes, or any blocker is recorded in `tasks.md`.

- [ ] **Step 3: Update tasks ledger**

Mark completed tasks in:

```text
openspec/changes/define-requirements-domain-standards-and-payment-skeleton/tasks.md
```

- [ ] **Step 4: Commit verification ledger**

Run:

```bash
git add openspec/changes/define-requirements-domain-standards-and-payment-skeleton/tasks.md
git commit -m "docs: verify requirements domain standards proposal"
```

Expected: commit succeeds with only the tasks ledger.
