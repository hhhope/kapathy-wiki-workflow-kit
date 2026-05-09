# llm-wiki-core-contract Specification

## Purpose
TBD - created by archiving change define-llm-wiki-core-contract. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL define an LLM Wiki core product contract

The repository SHALL preserve a repo-visible product contract that states the
LLM Wiki north star and distinguishes core value from enhancements.

#### Scenario: Future agent needs product orientation

- **WHEN** a future agent is asked to continue LLM Wiki productization
- **THEN** it SHALL be able to find a repo-visible product contract
- **AND** the contract SHALL state that the LLM Wiki core value is durable
  compiled context for agents and humans

### Requirement: LLM Wiki core SHALL use a four-part loop

The product contract SHALL define the LLM Wiki core loop as Capture, Compile,
Retrieve, and Apply.

#### Scenario: A capability is classified

- **WHEN** the repository classifies a product capability or gap
- **THEN** it SHALL map core capabilities to Capture, Compile, Retrieve, or
  Apply
- **AND** it SHALL avoid treating unrelated enhancement backlogs as core
  capabilities

### Requirement: Repository SHALL separate enhancements from core LLM Wiki value

The repository SHALL treat agent self-service learning, scorecard calibration,
graph/lint dashboards, and learning-to-change orchestration as enhancements
unless a later OpenSpec change promotes a specific item into core scope.

#### Scenario: Agent-learning work is discussed

- **WHEN** the user discusses external repo learning, scorecards, graph gaps, or
  multi-change orchestration
- **THEN** the repository SHALL preserve whether the item is core LLM Wiki work
  or an enhancement
- **AND** it SHALL NOT silently replace the LLM Wiki north star with the latest
  enhancement pain point

### Requirement: External LLM Wiki references SHALL be adapted through the core loop

External wiki references such as `Ar9av/obsidian-wiki` SHALL be compared by how
they support Capture, Compile, Retrieve, and Apply, rather than copied as an
undifferentiated feature list.

#### Scenario: External wiki project is used as learning

- **WHEN** an external LLM Wiki project informs this repository's roadmap
- **THEN** the comparison SHALL identify which core-loop stage each reused idea
  supports
- **AND** it SHALL record local modifications and non-adoptions

