# Add Go Engineering Security Rules

## Why

The user provided a batch of WeChat articles about Go security, Go service
engineering, Go code organization, Go modernization, framework selection, and
`go tool fix`, then asked to turn the useful parts into our own rules without
copying or retaining duplicated article content.

The user also confirmed the target stack convention:

- Language: Go, with target projects declaring `go 1.25.1` in `go.mod`
- Web framework: Gin
- Common Gin middleware: `gin-contrib`
- Validation: `go-playground/validator`
- Database access: GORM
- Cache: `go-redis`

## What

- Add a repo-local Go engineering/security rule document.
- Route Go backend/security/service work through that rule from `AGENTS.md`.
- Preserve article-source learning as compressed evidence, not copied article
  text.
- Treat `go tool fix` as a Go-version migration tool, not a daily formatting or
  lint command.

## Non-Goals

- Do not copy source articles into repo rules.
- Do not turn framework ranking articles into mandatory framework choices.
- Do not modify root/global `~/.codex/AGENTS.md`.
- Do not run `go tool fix` against this repository.
