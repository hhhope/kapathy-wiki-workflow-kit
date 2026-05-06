---
canonical_object: no-repo-local-commit-hook-default
artifact_type: adr
formalizes:
- no-repo-local-commit-hook-default
related_objects:
- repo-agents-governance-phase0
derived_from:
- agents-governance-drift
---

# no-repo-local-commit-hook-default / adr

- Status: accepted
- Date: 2026-05-06

## Context

Repo Phase 0 required the repo-local commit-gate status to be explicit before
Phase 1 repo `AGENTS.md` migration. Candidate governance material discussed Git
hooks as one possible enforcement layer, but no repo-local hook exists in this
repository and the current governance direction favors repo-visible decisions,
OpenSpec evidence, wiki records, and skill boundaries over a default local hook.

Leaving the hook question implicit would let future Phase 1 work accidentally
inherit hook assumptions from candidate pages.

## Decision

Repo-local commit hooks are not part of the default governance path for
`agents-governance-drift`.

Phase 1 repo `AGENTS.md` compression or proxy migration may proceed without a
repo-local commit hook. If a future change wants hook-based enforcement, it must
explicitly reverse this default in a new OpenSpec change and record:

- the exact hook scope
- the failure mode it catches
- evidence that the hook improves behavior
- rollback and bypass boundaries

## Consequences

- Phase 1 repo `AGENTS.md` work no longer waits on a hook implementation.
- Candidate hook discussions remain historical context, not accepted default
  policy.
- The repository still may adopt hooks later, but only through an explicit
  reversal change.
