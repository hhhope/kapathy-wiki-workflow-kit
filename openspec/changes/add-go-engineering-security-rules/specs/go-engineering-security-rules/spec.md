# go-engineering-security-rules Specification

## ADDED Requirements

### Requirement: Repository SHALL provide a compressed Go engineering/security rule

The repository SHALL provide a repo-visible rule for Go backend, service,
security, dependency, and modernization work that is derived from compressed
article learning and the user-confirmed local stack convention.

#### Scenario: Go backend or service work is requested

- **WHEN** a task creates, reviews, or modifies Go backend/service code
- **THEN** the agent SHALL load the repo Go engineering/security rule before
  implementation or review

#### Scenario: Rule content is derived from external articles

- **WHEN** external articles are used to support the rule
- **THEN** the repo SHALL preserve a compressed learning note with source URLs,
  reusable learning, rejected moves, and adoption boundaries
- **AND** it SHALL NOT copy full article bodies or article code examples into
  the rule

### Requirement: Go stack convention SHALL be explicit

The Go rule SHALL record the user-confirmed default stack convention.

#### Scenario: New Go service stack is unspecified

- **WHEN** the user asks for a Go service and does not provide a conflicting
  stack
- **THEN** the agent SHALL default to Go `1.25.1` in `go.mod`, Gin,
  `gin-contrib`, `go-playground/validator`, GORM, and `go-redis`

### Requirement: `go tool fix` SHALL be migration-scoped

The Go rule SHALL treat `go tool fix` as a Go-version migration and
modernization tool, not a routine lint or formatting command.

#### Scenario: Agent considers running `go tool fix`

- **WHEN** the agent considers using `go tool fix` or `go fix`
- **THEN** it SHALL require an explicit Go-version migration or modernization
  task
- **AND** it SHALL inspect local available rewrites before relying on article
  claims about analyzers
- **AND** it SHALL preview changes with `-diff` before rewriting files
- **AND** it SHALL review and commit only task-scoped rewrites

#### Scenario: Normal Go code formatting or linting is needed

- **WHEN** the task only requires normal formatting, linting, or CI checks
- **THEN** the agent SHALL use `gofmt`, `goimports`, `go vet`,
  `golangci-lint`, or repo Makefile targets as applicable
- **AND** it SHALL NOT use `go tool fix` as a substitute
