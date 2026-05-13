# Evaluation

## Pressure Scenarios

| Scenario | Expected Behavior |
|---|---|
| User asks for Go backend/service work with no stack specified | Agent loads `rules/go/engineering-security.md` and defaults to Go 1.25.1 + Gin + gin-contrib + validator + GORM + go-redis. |
| User cites Go framework ranking articles | Agent does not convert rankings into hard framework choices; user-confirmed stack wins. |
| User asks about `go tool fix` | Agent explains it as a Go-version migration tool, not a normal lint/format step. |
| Agent considers running `go tool fix` | Agent checks local rewrites, previews with `-diff`, and only runs it in an explicit migration/modernization task. |
| External articles are used for a rule | Agent preserves compressed source learning and does not copy article bodies or examples. |

## Replay Evidence

### Positive Trigger Scenario

| Field | Evidence |
|---|---|
| Input or situation shape | User asks for Go backend/service/security implementation or review, or says to use the confirmed Go stack convention. |
| Trigger condition | Task touches Go service code, Go API boundaries, Gin handlers, GORM/Redis access, Go security, or Go modernization. |
| Expected route | Load `rules/go/engineering-security.md` before implementation or review. |
| Repo-visible artifact | `AGENTS.md`, `rules/go/engineering-security.md`, `wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md`. |
| Expected output | Use Go 1.25.1 + Gin + gin-contrib + validator + GORM + go-redis unless the user overrides; apply the security and engineering checklist. |
| Promotion or non-promotion boundary | User-confirmed stack is promoted into the rule; framework ranking articles are not promoted into hard framework choices. |
| Proof boundary | Tests verify route, stack terms, source compression, and `go tool fix` boundary; they do not prove every future Go repo has matching dependencies installed. |

### Negative Or Should-Not-Trigger Scenario

| Field | Evidence |
|---|---|
| Input or situation shape | User asks only for ordinary Markdown/wiki/report work, non-Go code, or a one-off article summary without Go implementation/review. |
| Trigger condition | No Go service/security/modernization surface is touched. |
| Expected route | Do not load the Go engineering/security rule as a blocking gate. Use the task-specific wiki/report/learning route instead. |
| Repo-visible artifact | `AGENTS.md` route states the rule applies to Go backend/service/security work. |
| Expected output | No Go stack assumption, no Gin/GORM/Redis default, and no `go tool fix` discussion unless relevant. |
| Promotion or non-promotion boundary | External article learning remains candidate unless a scoped OpenSpec/rule change promotes it. |
| Proof boundary | This evaluation proves routing intent and local rule presence, not runtime enforcement by external editors. |

## RED Baseline

Before this change:

- `AGENTS.md` had no route to a repo-local Go engineering/security rule.
- No `rules/go/engineering-security.md` existed.
- No repo-visible compressed source-learning record existed for the provided
  WeChat article batch.
- No test asserted the user-confirmed Go stack or `go tool fix` boundary.

Expected old-state failure shape: `tests/test_go_engineering_security_rules.py`
would fail on missing route, missing rule file, missing source-learning file, and
missing stack phrases.

## GREEN Result

Verified on 2026-05-13:

- `python3 -m unittest tests.test_go_engineering_security_rules -v`: 4 tests passed.
- `openspec validate add-go-engineering-security-rules --strict`: change valid.
- `git diff --check -- AGENTS.md rules/go/engineering-security.md wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md openspec/changes/add-go-engineering-security-rules tests/test_go_engineering_security_rules.py`: passed.
- `python3 scripts/check_wiki_frontmatter.py`: non-zero from pre-existing legacy drift; the new `go-engineering-security-rule-source-learning-2026-05-13.md` page was not listed in the generated drift report.
- `go doc cmd/fix`: confirmed `go tool fix` is for old API rewrites after Go release updates and rewrites files without backups.
- `go tool fix -help`: confirmed available rewrites are local-toolchain-dependent; article analyzer lists must not be copied into hard rules without checking the local toolchain.

## Residual Risks

- This repository's local `go version` is `go1.22.2`; the user's target stack
  convention says future target Go projects use `go 1.25.1`. The rule therefore
  requires checking target `go.mod` and local toolchain before migration actions.
- `.codex/rules` could not be created in this run, so the rule is stored at
  `rules/go/engineering-security.md` and routed from repo `AGENTS.md`.
- The framework ranking article is treated only as background; changing the
  default framework still requires an explicit user or architecture decision.
