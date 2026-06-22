## ADDED Requirements

### Requirement: High-value shared Lore pages SHALL support mixed-language first-load interpretation beyond aliases
The system SHALL strengthen mixed-language support for the highest-value shared Lore pages so an agent can not only route to them but also load the first working facts without depending on lucky terminology overlap.

#### Scenario: Entry page exposes mixed-language first-load support
- **WHEN** a shared entry page serves as a first hop for Chinese-first and English-first prompts
- **THEN** it MUST expose mixed-language support in a form stronger than aliases alone for the page class
- **AND** that support MUST preserve retrieval-first operating sections

#### Scenario: Reusable durable page improves mixed-language loading
- **WHEN** a reusable pitfall, principle, or overview page remains important in mixed-language task startup
- **THEN** the page MUST expose enough mixed-language support for first-load interpretation of its operating sections
- **AND** it MUST NOT require mirrored full-body translation unless the page class explicitly needs it

### Requirement: Lore, OpenSpec, and Graphify routing SHALL have stronger automated evidence
The system SHALL strengthen routing validation so the Lore/OpenSpec/Graphify contract depends less on manual walkthrough evidence.

#### Scenario: Automated routing check covers representative question classes
- **WHEN** routing validation is run for this follow-up
- **THEN** it MUST include representative checks for process questions, Lore rule or boundary questions, Graphify structure questions, and mixed questions
- **AND** the results MUST report those classes separately

#### Scenario: Routing automation does not overclaim classifier completeness
- **WHEN** the automated routing checks pass for the selected cases
- **THEN** the result MUST be used to justify only the tested routing slice
- **AND** it MUST NOT be used to claim generic or fully automated question classification
