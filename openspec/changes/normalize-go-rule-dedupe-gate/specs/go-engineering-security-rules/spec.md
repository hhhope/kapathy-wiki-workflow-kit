# go-engineering-security-rules Specification

## MODIFIED Requirements

### Requirement: Repository SHALL provide a compressed Go engineering/security rule

The repository SHALL provide a repo-visible rule for Go backend, service,
security, dependency, and modernization work that is derived from compressed
article learning and the user-confirmed local stack convention. The rule SHALL
own Go-specific behavior and SHALL reference common/global behavior assets for
generic constraints.

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

#### Scenario: External articles suggest generic engineering limits

- **WHEN** article learning suggests generic file-size, git, testing,
  documentation, or behavior-asset policies
- **THEN** the Go rule SHALL reference the existing global/common rule instead
  of defining a Go-local duplicate
- **AND** it SHALL preserve Go-specific guidance only when the behavior depends
  on Go tooling, runtime, libraries, or project shape
