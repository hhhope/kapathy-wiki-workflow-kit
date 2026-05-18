# frontmatter-producer-warning-gate Specification

## ADDED Requirements

### Requirement: Frontmatter recovery SHALL distinguish blockers from warnings

The wiki frontmatter precheck used by recovery SHALL fail on configured
blocking findings and SHALL NOT fail solely because non-blocking warnings are
present.

#### Scenario: Warning-only producer findings do not block recovery

- **GIVEN** the frontmatter precheck reports `blocking_count: 0`
- **AND** the remaining findings are warning severity
- **WHEN** recovery runs the frontmatter precheck
- **THEN** the frontmatter precheck SHALL exit successfully
- **AND** warning details SHALL remain visible in the output

#### Scenario: Blocking frontmatter errors still block recovery

- **GIVEN** the frontmatter precheck reports one or more blocking findings
- **WHEN** recovery runs the frontmatter precheck
- **THEN** the frontmatter precheck SHALL exit nonzero
- **AND** recovery SHALL preserve the failed check as evidence
