# go-engineering-security-rules Specification

## MODIFIED Requirements

### Requirement: Repository SHALL provide a compressed Go engineering/security rule

The repository SHALL provide a repo-visible rule for Go backend, service,
security, dependency, and modernization work that is derived from compressed
article learning, official/GitHub Go best-practice evidence, and the
user-confirmed local stack convention. The rule SHALL own Go-specific behavior
and SHALL reference common/global behavior assets for generic constraints.

#### Scenario: Go backend or service work is requested

- **WHEN** a task creates, reviews, or modifies Go backend/service code
- **THEN** the agent SHALL load the repo Go engineering/security rule before
  implementation or review

#### Scenario: Large Go file guidance is needed

- **WHEN** a Go file crosses the loaded global large-file guardrail threshold
- **THEN** the agent SHALL treat the file as refactor-first according to the
  global guardrail
- **AND** the Go rule SHALL NOT define a separate local file-size threshold

#### Scenario: Official/GitHub source evidence is used

- **WHEN** official Go docs, Google Go style guidance, or GitHub-hosted style
  guides inform the rule
- **THEN** the repo SHALL preserve source-learning evidence
- **AND** it SHALL promote only compressed, Go-specific guidance into the rule
- **AND** it SHALL NOT copy full upstream guides or adopt unofficial project
  layouts as mandatory policy
