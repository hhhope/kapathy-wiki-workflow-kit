## MODIFIED Requirements

### Requirement: Article learning SHALL score sources before deep reading

Article learning SHALL triage article value before investing in deep reading.

#### Scenario: Article is below the deep-reading threshold

- **WHEN** an article scores below the configured deep-reading threshold
- **THEN** the result SHALL record the source and skip reason
- **AND** it SHALL NOT produce full deep-reading notes unless the user explicitly
  overrides the threshold

#### Scenario: Article source reaches the deep-reading threshold

- **WHEN** an article passes admission and scores 75 or higher
- **THEN** it MAY proceed to deep-reading notes

#### Scenario: Article source is a brief candidate

- **WHEN** an article scores from 60 through 74
- **THEN** it SHALL remain a brief candidate note by default
- **AND** it SHALL NOT produce durable deep-reading notes unless explicitly
  overridden

#### Scenario: Article source is scored retrospectively

- **WHEN** scoring occurs after deep reading or after conclusions were drafted
- **THEN** the score SHALL be marked retrospective
- **AND** it SHALL NOT be treated as score-first admission evidence
