---
name: database-migrations
description: "Use for schema/data migration planning or review. Trigger phrases: migration, schema change, backfill, import historical data, rollback plan, validation SQL. Even if the user does not say migration, trigger when a requested DB change affects table/column structure or bulk data movement. Exclude ordinary CRUD/API code changes with no schema or backfill impact."
---

# Database Migrations

Compact migration starter card. Use it as a checklist after the migration objective is known, then localize names, paths, and ownership rules for the target repository before wiring it into local governance.

## Do Not

- Do not edit the semantics of an already-applied migration file; add a new forward migration instead.
- Do not collapse DDL, large DML backfill, and legacy cleanup into one opaque step.
- Do not rename/drop legacy physical fields before compatibility code and validation are in place.
- Do not run an import/apply step without row-count and ownership validation SQL.

## Intent Routing

| Intent | Required Artifact | Required Checks |
|--------|-------------------|-----------------|
| Add a table or column | New forward migration and bootstrap-schema alignment if fresh environments use a generated baseline | nullable/default strategy, index impact, API/ORM model alignment, ownership field semantics |
| Physical rename of tables or columns | Expand/contract migration plan + compatibility notes | support for old and new names during transition, no route/service breakage, ownership preserved |
| Historical JSON/raw import | Dry-run/apply migration command + validation SQL | import order, transaction rollback boundary, row counts, ownership mapping |
| Data backfill | Forward migration script + batch strategy | DDL/DML split, batch size, lock risk, retry behavior, idempotency |
| Migration review | Diff review + verification SQL | no destructive one-shot rename/drop before code switch, no mutation of already-applied migration semantics |

## Localize Before Use

Before this skill becomes repository truth, replace placeholders with local decisions for:

- migration file locations and bootstrap schema location
- ownership or tenant/team scoping fields
- metadata columns such as versioning, timestamps, and soft-delete markers
- rollout order for compatibility reads/writes
- validation SQL or verification commands that fit the target stack

## Error / Risk Index

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Fresh bootstrap creates an outdated schema | Baseline schema was not updated alongside the forward migration | Update the bootstrap schema or schema-generation pipeline and verify a fresh install |
| Old environment breaks after a rename | Migration dropped legacy names before compatibility code was deployed | Use an expand/contract sequence and keep compatibility reads during the transition |
| Rows appear under the wrong owner or tenant | Import script mapped ownership incorrectly or omitted scope fields | Re-check source-to-owner mapping and add validation SQL before apply |
| Soft-deleted rows reappear or versions drift | Migration omitted soft-delete/version semantics or backfilled inconsistent metadata | Align schema fields with runtime CRUD expectations and verify with targeted SQL |
| Apply takes long locks or stalls writes | Large-table DDL/DML was executed in one heavy step | Split schema and backfill, batch data writes, and document lock/rollback boundaries |

## Output Template

```markdown
# Migration Plan

## Scope
- [tables/fields/data in scope]

## Expand/Contract Steps
1. [compatibility addition]
2. [application switch]
3. [backfill/import]
4. [legacy cleanup]

## Risk Check
- Lock risk:
- Rollback boundary:
- Backward compatibility:
- Validation SQL/API checks:

## Verification
- Dry-run command:
- Apply command:
- Row-count/ownership checks:
```
