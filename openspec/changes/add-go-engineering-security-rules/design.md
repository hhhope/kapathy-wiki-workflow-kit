# Design

## Rule Placement

The desired `.codex/rules` path could not be created in this repository because
the filesystem reported it as read-only during this run. The rule is therefore
stored in `rules/go/engineering-security.md` and routed from repo `AGENTS.md`.

This keeps the rule repo-visible without changing global agent configuration.

## Compression Model

The source articles are compressed into rule groups:

- Stack convention
- Go version and migration boundary
- Security-critical coding
- HTTP/API boundary
- Persistence and cache boundary
- Concurrency and resource lifecycle
- Observability
- Tests and CI
- Project layout and documentation
- Dependency and code-generation hygiene
- Framework selection boundary

Repeated examples, code snippets, star rankings, and article-specific phrasing
are intentionally excluded.

## `go tool fix` Boundary

`go tool fix` and `go fix` are treated as migration tools for Go release
upgrades:

- Use only during explicit Go-version upgrade or modernization work.
- First inspect available rewrites with the local toolchain.
- Preview with `go tool fix -diff` before rewriting.
- Commit only reviewed, task-scoped rewrites.
- Never use it as a normal format/lint step.

## Evidence Boundary

The article learning note records source metadata, compressed learning, rejected
promotion moves, and local adoption boundaries. It is not a source dump.
