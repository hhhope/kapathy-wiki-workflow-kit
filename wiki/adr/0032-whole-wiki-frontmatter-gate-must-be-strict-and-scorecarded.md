---
layer: adr
domain: none
canonical_object: whole-wiki-frontmatter-gate
artifact_type: adr
formalizes:
  - wiki-frontmatter-taxonomy-gate
derived_from:
  - wiki-frontmatter-model
  - stabilize-wiki-frontmatter-taxonomy
---

# ADR-0032 Whole Wiki Frontmatter Gate Must Be Strict And Scorecarded

## Status

Accepted

## Context

The repository has a frontmatter model and a taxonomy checker, but the checker
does not yet enforce the full model across the wiki.

Two misses exposed the gap:

- `wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md` lacks required ops
  taxonomy fields but was not reported.
- `wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md`
  lacks taxonomy fields, and ADR pages were not part of taxonomy path rules.

This made `wiki-status` look stronger than the evidence. A narrow drift report
was presented close to whole-wiki health, even though completeness was not being
checked across all layers.

## Decision

The repository adopts a strict whole-wiki frontmatter gate.

- All `wiki/**` markdown pages are governed by frontmatter rules.
- Rule coverage, required fields, blocking severities, and score weights live
  in `wiki/config/frontmatter-taxonomy.yaml`.
- The checker must emit both detailed findings and a scorecard.
- `taxonomy drift`, `frontmatter completeness`, graph identity coverage, and
  relation shape are separate health concerns.
- `wiki-status` must show the strict gate result and scorecard, not only drift
  counts.
- A narrow checker result must never be described as whole-wiki compliance.

## Consequences

- Existing legacy debt becomes visible immediately.
- A strict checker failure is expected until legacy pages are migrated or
  explicitly excepted in configuration.
- Archive review and frontmatter compliance claims must read checker evidence.
- Exceptions must be explicit config entries with reason and owner; chat-only
  exceptions do not count.
