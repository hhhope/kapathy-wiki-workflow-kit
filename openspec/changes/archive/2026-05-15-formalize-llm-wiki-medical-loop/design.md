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
