# Design

## Evidence Sources

The rule uses these source classes:

- Go official documentation for module layout and review guidance.
- Google Go style guidance for clarity, simplicity, line-length caution, and
  context usage.
- GitHub-hosted community/company guides such as Uber Go Style as supporting
  references, not wholesale policy.
- `golang-standards/project-layout` as a cautionary reference: useful as a map,
  not an official mandatory layout.

## Threshold Ownership

The `300` threshold belongs to the already-loaded global `Large-file
guardrails`, which currently states Go/Rust/Java files `> 300` lines are
refactor-first. The Go rule must reference that source instead of defining a
local threshold.

## Rule Additions

Add only high-confidence Go-specific guidance:

- pass `context.Context` as an explicit first argument across request/dependency
  boundaries; do not store it in structs
- define interfaces near the consuming package when practical; avoid premature
  interfaces created only for mocks
- use `cmd/` and `internal/` as helpful module layout tools without forcing a
  large template on small services
- reject fixed Go-local file-length or line-length thresholds

## Proof Boundary

Tests assert the local rule and source-learning evidence. They do not prove that
every external guide stays unchanged over time.
