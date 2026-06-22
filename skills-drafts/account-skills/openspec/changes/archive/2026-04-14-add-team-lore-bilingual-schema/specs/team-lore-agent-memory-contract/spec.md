## ADDED Requirements

### Requirement: Durable shared Lore pages SHALL expose retrieval-first operating sections
The system SHALL require durable shared Lore pages to expose a retrieval-first structure so that an agent can determine applicability and load minimal working context without depending on long-form prose.

#### Scenario: A durable page exposes operating sections
- **WHEN** a shared durable page is created or materially updated
- **THEN** it MUST expose explicit operating sections for scope, applicability, exclusion, top facts, watchpoints, and related pages
- **AND** any longer rationale MUST be separated from those operating sections

#### Scenario: A page is rejected as not retrieval-ready
- **WHEN** a durable shared page only contains human-readable narrative without explicit operating sections
- **THEN** it MUST NOT be considered retrieval-ready enough for agent memory rollout

### Requirement: Durable facts SHALL be written as atomic operating facts
The system SHALL require `Top Facts` and equivalent operating sections to use atomic facts rather than blended narrative blocks.

#### Scenario: Top facts are written atomically
- **WHEN** a page records stable operating knowledge
- **THEN** each top fact MUST express one stable constraint, fact, or boundary per bullet
- **AND** it MUST avoid combining unrelated facts and rationale in one prose-heavy paragraph

#### Scenario: Watchpoints are separated from explanation
- **WHEN** a page records risks or fragile areas
- **THEN** those watchpoints MUST appear in an explicit watchpoint section
- **AND** explanatory rationale MAY appear later without replacing the operating signal

### Requirement: Shared memory SHALL support agent applicability decisions
The system SHALL allow an agent to decide quickly whether a page applies to the current task or should be rejected.

#### Scenario: A page declares applicability
- **WHEN** an agent reads a durable shared page
- **THEN** the page MUST state the task scenes, problem shapes, or system boundaries where it applies

#### Scenario: A page declares exclusion
- **WHEN** an agent reads a durable shared page
- **THEN** the page MUST state at least one exclusion or not-for signal when neighboring pages could otherwise be confused

### Requirement: Bootstrap SHALL produce agent-ready starter pages
The system SHALL require `lore-bootstrap` starter pages to be retrieval-ready rather than merely non-empty.

#### Scenario: Starter pages are retrieval-ready at bootstrap completion
- **WHEN** bootstrap completes a new shared wiki or new project starter area
- **THEN** the generated index and overview pages MUST satisfy the retrieval-first page model
- **AND** bootstrap completion MUST NOT be claimed if starter pages exist only as prose-capable shells

### Requirement: Weekly review SHALL promote durable knowledge in agent-ready form
The system SHALL require weekly-review absorption to update durable pages in retrieval-first shape so future agents can reuse the result efficiently.

#### Scenario: Weekly review promotes operating facts
- **WHEN** weekly review accepts a durable lesson
- **THEN** the destination page MUST be updated in a way that improves scope, top facts, watchpoints, related pages, or other operating sections
- **AND** accepted durable knowledge MUST NOT be recorded only as appended narrative explanation

#### Scenario: Local logs remain local until promotion
- **WHEN** a review batch processes project-local logs
- **THEN** the logs themselves MAY remain local-language and unstructured
- **AND** only the promoted durable result MUST satisfy the shared-memory contract

### Requirement: Language support SHALL be defined as agent compatibility
The system SHALL treat mixed-language support as part of agent memory usability rather than as a standalone translation-only concern.

#### Scenario: Mixed-language routing support is present
- **WHEN** a durable shared page uses terminology that may differ across Chinese and English prompts
- **THEN** the page MUST include aliases, summaries, or equivalent mixed-language routing aids required by the page class

#### Scenario: Retrieval metrics do not overclaim language completeness
- **WHEN** validation reports successful English or mixed-language query routing
- **THEN** those results MUST NOT alone be used to claim language-complete shared memory support
- **AND** page-model completeness and language-support completeness MUST be reported separately

#### Scenario: Alias support is the minimum first-slice language contract
- **WHEN** this change is evaluated for first-slice rollout or archive readiness
- **THEN** alias-based mixed-language routing aids MAY satisfy the minimum language-support bar for this change
- **AND** that result MUST NOT be used to claim full bilingual first-load interpretation or mirrored body-content completeness

### Requirement: OpenSpec SHALL remain outside the knowledge retrieval layer
The system SHALL keep OpenSpec as the process-plane truth source rather than merging it into the Lore/Graphify knowledge retrieval layer.

#### Scenario: Process questions route to OpenSpec
- **WHEN** a question asks about change scope, proposal state, design state, or task progress
- **THEN** the system MUST route that question to OpenSpec artifacts rather than treating it as Lore or Graphify retrieval

#### Scenario: Knowledge questions do not overwrite process truth
- **WHEN** a Lore or Graphify result is returned
- **THEN** that result MUST NOT be used to claim task completion, change completion, or archive readiness

### Requirement: Lore SHALL remain the durable semantic truth source inside the knowledge plane
The system SHALL treat Lore pages as the durable truth-bearing memory layer for shared rules, boundaries, pitfalls, principles, and stable facts.

#### Scenario: Rule and boundary questions route to Lore
- **WHEN** a question asks which rule applies, which pitfall fits, or which stable facts and boundaries matter
- **THEN** the system MUST route that question through Lore pages first

#### Scenario: Graphify does not replace Lore truth
- **WHEN** Graphify provides code-topology evidence
- **THEN** that evidence MUST NOT be treated as a substitute for durable Lore facts or page boundaries

### Requirement: Graphify SHALL be treated as code-topology evidence inside the knowledge plane
The system SHALL treat Graphify as a structural evidence layer for code entry points, neighbors, bridge nodes, and likely code paths.

#### Scenario: Structure questions route to Graphify
- **WHEN** a question asks where code lives, which nodes connect, or which module is structurally central
- **THEN** the system MAY route that question to Graphify without first treating it as a Lore page-retrieval problem

#### Scenario: Mixed questions use Lore before Graphify
- **WHEN** a question needs both durable semantic framing and code-topology evidence
- **THEN** the system MUST route to Lore first to identify the scene and stable facts
- **AND** it MUST use Graphify second to provide structural code evidence for that scene
