# article-learning-capture Specification

## Purpose
TBD - created by archiving change formalize-article-learning-capture. Update Purpose after archive.
## Requirements
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

### Requirement: Article learning SHALL score sources before deep reading

Article learning SHALL triage article value before investing in deep reading.

#### Scenario: Article is below the deep-reading threshold

- **WHEN** an article scores below the configured deep-reading threshold
- **THEN** the result SHALL record the source and skip reason
- **AND** it SHALL NOT produce full deep-reading notes unless the user explicitly
  overrides the threshold

### Requirement: Article learning SHALL preserve source-first reading notes

Article learning SHALL preserve enough source context for later review without
storing full copyrighted article text.

#### Scenario: Deep-reading notes are written

- **WHEN** article learning produces durable wiki notes
- **THEN** the notes SHALL include original URL, title, author or publisher when
  available, publication date when available, access date, source class, source
  artifact type, source grounding, score, structured translation notes or
  paraphrased reading notes, evidence references, and promotion boundary
- **AND** the notes SHALL NOT store full verbatim copyrighted article text or a
  full verbatim translation

### Requirement: Article learning SHALL separate comprehension from transfer extraction

Article learning SHALL distinguish reading the article from extracting local
candidate practices.

#### Scenario: Transferable learning is extracted

- **WHEN** article learning extracts a point that may affect local repo or agent
  behavior
- **THEN** the extracted point SHALL preserve:
  - source
  - claim
  - evidence
  - local usefulness
  - adoption boundary
  - status

### Requirement: Article learning SHALL not promote unsupported claims into behavior assets

Article learning SHALL preserve candidate observations unless promotion evidence
exists.

#### Scenario: Article takeaway is proposed as a rule or skill behavior

- **WHEN** an article takeaway is used to support a behavior-asset rule, hard
  constraint, skill rule, spec requirement, or archive-ready conclusion
- **THEN** the promotion SHALL satisfy the repository evidence-backed best
  practice gate or route into a scoped OpenSpec change for further validation

