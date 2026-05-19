## REMOVED Requirements

### Requirement: Repository SHALL provide a dedicated skill for external article learning capture

The repository SHALL provide a repo-local skill for requests that use external
articles, blogs, papers, WeChat posts, or article collections as learning inputs
for repository workflow, agent practice, output methods, or behavior-asset
candidates.

#### Scenario: User asks to deeply learn from external articles

- **WHEN** the user provides one or more external articles and asks to `精读`,
  learn, extract useful points, score, write to wiki, or create a reusable SOP
- **THEN** the system SHALL route the task through the dedicated article learning
  capture skill

## ADDED Requirements

### Requirement: Article learning SHALL survive as learning-capture module content

Article-specific gates and reference content SHALL remain available through
`learning-capture` module references after the dedicated active article skill
surface is retired.

#### Scenario: User asks to deeply learn from external articles

- **WHEN** the user provides one or more external articles and asks to `精读`,
  learn, extract useful points, score, write to wiki, or create a reusable SOP
- **THEN** the system SHALL route the task through `learning-capture`
- **AND** the system SHALL use article-specific module references for source
  metadata, source grounding, score-first triage, copyright boundaries,
  structured reading or translation notes, transferable learning, rejected
  moves, and promotion boundaries
- **AND** the system SHALL NOT require or expose a dedicated active
  `article-learning-capture` skill surface.
