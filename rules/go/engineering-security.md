# Go Engineering And Security Rule

Use this rule before creating, reviewing, or modifying Go backend/service code.
This is a compressed repo rule, not a copied article summary.

## Default Stack

Use this stack when the user asks for a Go service and does not override it:

- Go version in target `go.mod`: `go 1.25.1`
- HTTP framework: Gin (`github.com/gin-gonic/gin`)
- Gin middleware family: `gin-contrib` for CORS, gzip, sessions, static assets,
  and similar concerns
- Parameter validation: `github.com/go-playground/validator`
- Database access: GORM, with the project-selected MySQL, PostgreSQL, or SQLite
  driver
- Cache: Redis through `go-redis`

Do not use framework popularity rankings as a stronger signal than this stack.

## Common Rule Boundaries

This rule owns Go-specific engineering and security behavior. It does not own
generic repository workflow policy.

- File-size thresholds and refactor-first behavior come from the global
  `Large-file guardrails` in `~/.codex/AGENTS.md`.
- Git discipline, commit boundaries, and dirty-worktree handling come from the
  global/root instructions.
- General behavior-asset evaluation and prior-art dedupe come from repo
  `AGENTS.md`, `wiki/config/behavior-asset-evaluation.yaml`, and
  `scripts/check_behavior_assets.py`.
- General testing policy comes from `~/.codex/rules/common/testing.md`; this
  rule only adds Go-specific test emphasis.
- Do not define repo-local file length thresholds here.

## Official Go Practice Boundary

- Apply official Go guidance in compressed form. Do not copy full upstream
  style guides into this rule.
- Prefer clarity, small cohesive packages, explicit ownership, and simple
  control flow over article-derived checklist volume.
- Reject fixed Go-local file-length or line-length thresholds. Use global
  large-file guardrails and refactor when code is hard to understand.

## Version And Migration

- Treat `go.mod` as the source of truth for the target Go version.
- If the local `go version` is older than the target `go.mod`, do not run
  upgrade rewrites or version-specific checks as if the local toolchain were
  authoritative.
- `go tool fix` / `go fix` is for Go-version migration and modernization after a
  Go upgrade. It is not a daily formatter, linter, or cleanup command.
- Before any `go tool fix` rewrite:
  - confirm the task is a Go migration or modernization task
  - inspect local rewrites with `go tool fix -help`
  - preview with `go tool fix -diff`
  - restrict rewrites with `-r` when only a subset is intended
  - review the diff before staging
- Use `gofmt`, `goimports`, `go vet`, `golangci-lint`, and repo Makefile/CI
  targets for normal formatting and quality checks.

## Security-Critical Code

Reject or stop for redesign when code violates these boundaries:

- External input used for slice indexes, allocation sizes, integer conversion,
  file paths, shell commands, URLs, SQL fragments, HTTP headers, templates, or
  auth decisions must be validated before use.
- File operations must prevent path traversal and set least-privilege file
  permissions.
- Shell execution must avoid shell interpolation. If command execution is
  required, use explicit executable allowlists and argument arrays.
- SQL must use parameter binding. Dynamic table names, order fields, or raw SQL
  fragments require allowlists.
- Outbound HTTP requests using user-controlled URLs require scheme, host, DNS/IP,
  private-network, and redirect validation.
- Secrets must not be hardcoded, logged, returned in API responses, committed,
  embedded in images, or stored in generated rule files.
- TLS verification must not be disabled in production paths.
- Sensitive operations require authentication, authorization, and CSRF or
  equivalent request-origin protection when applicable.

## Gin API Boundary

- Validate request bodies, path params, query params, and headers at the
  boundary with `go-playground/validator` or an equivalent explicit whitelist.
- Keep handlers thin: parse and validate request, call service/usecase, map
  response.
- Use explicit response types and set correct `Content-Type`.
- Add security headers where the service exposes browser-facing surfaces.
- CORS must use explicit allowed origins. Do not use wildcard CORS with
  credentials.
- Do not expose debug mode, panic traces, SQL errors, secret values, or internal
  topology to clients.

## GORM And Redis

- Keep database access behind repository/store interfaces owned by the service
  layer.
- Use context-aware DB and Redis calls when the library supports them.
- Bound query size, pagination, lock duration, retry count, and Redis TTL.
- For writes that affect money, quota, account state, permissions, or delivery
  state, define idempotency and transaction boundaries before implementation.
- Do not use Redis as the only source of truth for durable business state unless
  the requirement explicitly says so.

## Concurrency And Resource Lifecycle

- Always pass `context.Context` as an explicit first argument after the receiver
  for request-scoped and dependency-scoped work.
- Do not store request-scoped context in structs.
- Every goroutine needs a cancellation or exit path, normally through
  `context.Context`.
- Avoid unbounded queues, unbounded goroutine fan-out, and unbounded buffering.
  Prefer bounded channels, rate limits, backpressure, or circuit breakers.
- Close channels from a single owner. Do not close a channel from multiple
  branches.
- Protect shared mutable state with mutexes, atomics, channels, or ownership
  transfer. Never concurrently write a map without protection.
- When a helper must be called under lock, name it with a clear locked/internal
  convention and keep it private where possible.
- Use `defer unlock/close` when it makes ownership safer and does not hide
  long-held resources.

## Error Handling And Observability

- Return errors early. Keep the happy path shallow.
- Use sentinel errors or typed errors with `errors.Is` / `errors.As`; do not
  branch on error strings.
- Wrap errors with context using `%w`, but do not leak sensitive internals to
  clients.
- Use structured logs with request ID / trace ID.
- Expose or record latency, error rate, saturation, queue depth, retry count,
  timeout, and dependency-failure signals for production services.

## Go Tests And CI

- Prefer table-driven tests for input/output behavior and edge cases.
- Tests must check returned errors; do not discard errors silently.
- Test timeouts, cancellation, retries, partial failures, race-sensitive paths,
  and boundary validation.
- Avoid naked sleeps in tests; use polling with timeout or controlled fakes.
- Run race detection for concurrency-sensitive code and CI gates where feasible.
- Performance claims require benchmarks or measurements, not comments.
- Use common testing rules for generic verification workflow and report only
  Go-specific additions from this rule.

## Go Project Shape

- Prefer `cmd/<service>` for binaries and `internal/` for private application
  code.
- Do not force a large project-layout template onto small services; add
  directories when the service shape needs them.
- Keep package responsibility narrow and names aligned with contents.
- Define interfaces near the consuming package when practical. Do not introduce
  interfaces only because a future mock might need them.
- Keep stable interfaces separate from frequently changing implementations.
- Avoid circular dependencies; break cycles with smaller packages or interfaces.
- Use explicit module versions. Do not rely on `latest`, `master`, or omitted
  versions in durable project rules.
- Generated code must be marked, reproducible, and not edited by hand.
- README/docs publication quality is governed by the repo public-output gate;
  this rule only expects Go entry points and generated artifacts to be
  discoverable.

## Framework Selection Boundary

The default stack above is the rule. Framework ranking articles are only
background. Changing the default framework requires an explicit user decision or
a scoped architecture change.
