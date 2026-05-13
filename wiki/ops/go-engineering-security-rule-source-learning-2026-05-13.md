---
title: go-engineering-security-rule / source-learning
type: learning
canonical_object: go-engineering-security-rule
artifact_type: source-learning
language: zh-CN
audience: agent
knowledge_level: working
layer: ops
domain: unclassified
classification_needed: true
ops_area: learning-capture
status: active
confidence: candidate
updated_at: 2026-05-13
ai_generated: true
derived_from:
  - https://mp.weixin.qq.com/s/3hQC4BYmU1-h_WfbOmXOhg
  - https://mp.weixin.qq.com/s/8SoRM1Q_nR_JtXuQhLMafg
  - https://mp.weixin.qq.com/s/NpDiSiiG_PFX15vYheEsqw
  - https://mp.weixin.qq.com/s/SxnMbThrsgB3Q6hTZRX69Q
  - https://mp.weixin.qq.com/s/KcKm8BNBYV91zlbxTIz9yw
  - https://mp.weixin.qq.com/s/pJSibD0QYrbhSqcy4V4EMQ
  - https://mp.weixin.qq.com/s/sWnXjrWpTjYO9ZGTaOIlJQ
  - https://go.dev/doc/modules/layout
  - https://go.dev/wiki/CodeReviewComments
  - https://google.github.io/styleguide/go/guide
  - https://github.com/uber-go/guide
  - https://github.com/golang-standards/project-layout
notes_scope: Compressed source learning for a repo-local Go engineering/security
  rule. This page records what was reused, modified, rejected, and bounded; it
  does not copy article bodies.
---

# Go Engineering Security Rule / Source Learning

## Source Set

| Source | Use | Local Decision |
|---|---|---|
| Go代码安全指南（腾讯） | Security checklist source | Reused as security dimensions, not copied examples. |
| 编写优秀的 Go 服务的准则 | Service engineering principles | Reused for correctness, context, bounded concurrency, observability, and tests. |
| 一些开发者应该遵循的 Go 编码规范 | Idiomatic Go coding reference | Reused for early returns, lock safety, explicit errors, DI, and table tests. |
| go 服务工程规范 | Service repository and CI structure | Reused for Makefile, dependency, tests, observability, README/docs boundaries. |
| 告别旧写法，拥抱新姿势 | `go tool fix` discussion | Reused only for migration awareness; corrected against local `go tool fix -help`. |
| 编写地道Go代码的n条建议：第二部分 代码组织 | Package and project organization | Reused for package cohesion, internal boundary, file organization, dependencies. |
| Golang框架全景封神榜 | Framework selection background | Rejected as hard rule; user-confirmed stack wins. |
| https://go.dev/doc/modules/layout | Official module layout guidance | Reused for `internal/` and conditional `cmd/` guidance; not used as a large-template mandate. |
| https://go.dev/wiki/CodeReviewComments | Official Go review guidance | Reused for context, goroutine lifecycle, interface placement, package naming, and error handling. |
| https://google.github.io/styleguide/go/guide | Google Go style guidance | Reused for clarity/simplicity framing and rejection of fixed Go-local line-length thresholds. |
| https://github.com/uber-go/guide | GitHub-hosted company style guide | Supporting reference only; not copied wholesale into the repo rule. |
| https://github.com/golang-standards/project-layout | Popular GitHub project layout repo | Reused as a cautionary map only; rejected as official or mandatory layout. |

## Admission And Score

Score timing: retrospective, because the user asked for immediate rule creation
while adding more links in the same thread.

| Criterion | Score | Reason |
|---|---:|---|
| Source access and provenance | 18/20 | URLs, titles, authors, and dates were fetched for the source set. |
| Evidence or method density | 18/25 | Several sources contain concrete checklist/process points; many examples and rankings were repetitive or promotional. |
| Local capability gain | 24/25 | Directly improves Go service implementation/review routing. |
| Transfer path | 15/15 | Clear target: repo rule plus AGENTS route and tests. |
| Verification path | 13/15 | Tests can verify stack, route, and `go tool fix` boundary; source quality itself remains external. |
| Total | 88/100 | Deep enough to create a compressed candidate rule with explicit boundaries. |

Decision: use compressed learning. Do not preserve article bodies.

## Reused Learning

| Area | Compressed Local Rule |
|---|---|
| Stack | Default to Go `1.25.1`, Gin, gin-contrib, validator, GORM, and go-redis unless user overrides. |
| Security | Validate all external input before memory, file, command, SQL, URL, header, template, auth, or response use. |
| HTTP boundary | Gin handlers stay thin; validation and response mapping happen at the boundary. |
| Persistence | DB/Redis calls need context, bounds, idempotency, transaction/TTL decisions. |
| Concurrency | Goroutines need exit paths; queues and fan-out must be bounded; shared state needs ownership or locks. |
| Observability | Logs, metrics, and traces must make latency, errors, saturation, and dependency failures visible. |
| Tests | Include table tests, error assertions, race-sensitive checks, timeout/cancel/retry/partial failure cases. |
| Organization | Prefer `cmd/`, `internal/`, cohesive packages, explicit dependencies, generated-code boundaries, docs split. |
| Migration | `go tool fix` is a Go upgrade tool; inspect available rewrites and preview with `-diff`. |
| Official-source boundary | Promote only compressed Go-specific practices; keep generic policy in global/common rules. |
| Large-file threshold | Go/Rust/Java `> 300` lines is referenced from global `Large-file guardrails`; the Go rule must not redefine it locally. |
| Context | Pass `context.Context` explicitly through request/dependency boundaries and do not store request-scoped context in structs. |
| Interfaces | Prefer defining interfaces near consumers; avoid premature interfaces only for hypothetical mocks. |
| Layout | Use `cmd/` and `internal/` when helpful; do not force a large project-layout template onto small services. |

## Modified Or Rejected

- Rejected full source copying and code-example copying.
- Rejected article repetition and long checklist duplication.
- Rejected framework star ranking as a default selection rule.
- Rejected `500` lines as a local or article-derived threshold. The current
  threshold evidence is Go/Rust/Java `> 300` lines, referenced from global
  `Large-file guardrails`.
- Rejected fixed Go-local line-length thresholds; Go style sources favor
  readability, simplicity, and refactoring over hard local numeric limits.
- Rejected `golang-standards/project-layout` as official or mandatory policy.
  It remains a useful map, not a repo rule template.
- Modified `go tool fix` guidance after checking local `go doc cmd/fix` and
  `go tool fix -help`: available rewrites depend on the installed Go toolchain.
- Modified Go-version guidance because this machine reports `go1.22.2` while
  the user-confirmed target project convention is `go 1.25.1`.

## Adoption Boundary

This learning supports `rules/go/engineering-security.md` and the repo
`AGENTS.md` route. It does not by itself prove that every future Go repository
already has Gin/GORM/Redis installed; project-local `go.mod` remains the raw
data to validate before implementation.
