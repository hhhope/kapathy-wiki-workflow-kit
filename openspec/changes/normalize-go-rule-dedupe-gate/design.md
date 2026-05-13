# Design

## Ordering

The dedupe gate comes first. Future behavior-asset changes must prove that
their proposed rule belongs in the target asset before adding or normalizing
the asset itself.

## Prior-Art Gate

For semantic changes to `skills/*`, `rules/*`, or `AGENTS.md`, the local
checker requires evaluation evidence that records:

- what existing global/common/repo assets were scanned
- what the new change owns
- what it references instead of duplicating
- what it rejects or leaves as candidate learning

The checker remains structural on purpose. It does not try to become a full
semantic static analyzer; it verifies that the human/agent recorded ownership
and dedupe decisions in the OpenSpec evaluation artifact.

## Go Rule Normalization

The Go rule owns Go-specific stack and engineering/security boundaries:

- Go `1.25.1`
- Gin, `gin-contrib`, `go-playground/validator`
- GORM and `go-redis`
- Gin API boundary, GORM/Redis boundary, Go concurrency/resource lifecycle
- `go tool fix` as a migration-only tool

It references common/global rules for generic gates such as file-size
thresholds, git discipline, behavior-asset evaluation, and general testing.

## Rollout Boundary

Existing completed active changes are grandfathered for the newly introduced
prior-art section requirement. New changes must include the section when they
touch behavior assets.
