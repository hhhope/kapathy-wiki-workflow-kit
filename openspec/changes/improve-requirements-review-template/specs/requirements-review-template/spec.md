## ADDED Requirements

### Requirement: Requirements case output SHALL expose human review judgment

Strict taxonomy v2 requirements case rendering SHALL expose a structured human
review block for domain coverage and story/acceptance mappings.

#### Scenario: Reviewer can see why a story is full first-release coverage
- **GIVEN** a requirements case story is classified as in-scope full coverage
- **WHEN** the case markdown is rendered
- **THEN** the output SHALL include `review_judgment.coverage_decision`
- **AND** it SHALL include `business_meaning`, `why_this_domain`,
  `first_release_scope`, `out_of_scope`, and `future_work`
- **AND** it SHALL include a reviewer-facing question or decision prompt

#### Scenario: Derived review judgment is explicit
- **GIVEN** a legacy case has domain coverage and stories but no explicit
  review metadata
- **WHEN** the case markdown is rendered
- **THEN** the output MAY derive review metadata from existing coverage fields
- **AND** the output SHALL make the derived judgment visible rather than
  silently relying on compressed taxonomy labels

### Requirement: Taxonomy references SHALL include readable meanings

Rendered requirements case review blocks SHALL include plain-language meanings
for taxonomy IDs used in domain, context, and aggregate references.

#### Scenario: Payment transaction references are understandable
- **GIVEN** a story references `payment_transaction`,
  `payment_intent_context`, `payment_attempt_authorization_context`,
  `payment_method_context`, `payment_intent`, `payment_attempt`,
  `payment_method_authorization`, and `charge`
- **WHEN** the case markdown is rendered
- **THEN** each reference SHALL appear as structured data with an `id`
- **AND** each reference SHALL include a `meaning`

### Requirement: Review output SHALL explain gate closure and eval plan

Rendered requirements case review blocks SHALL explain how machine gates and
human review close.

#### Scenario: Machine gates and human gate are visible
- **GIVEN** a strict taxonomy v2 requirements case is rendered
- **WHEN** the reviewer reads the review block
- **THEN** the output SHALL include `gate_closure.domain_model_gate`
- **AND** it SHALL include `gate_closure.domain_coverage_gate`
- **AND** it SHALL include `gate_closure.requirement_delivery_gate`
- **AND** it SHALL include `gate_closure.human_review_gate`

#### Scenario: Evaluation expectations are visible
- **GIVEN** a strict taxonomy v2 requirements case is rendered
- **WHEN** the reviewer reads the review block
- **THEN** the output SHALL include `eval_plan.red_cases`
- **AND** it SHALL include `eval_plan.green_cases`
- **AND** the eval plan SHALL distinguish machine checker proof from human
  readability proof

### Requirement: Machine case data SHALL remain stable

Adding reviewable rendering SHALL NOT mutate the machine case data used by
requirements checkers and OpenSpec handoff.

#### Scenario: Round trip preserves machine payload
- **GIVEN** a requirements case package is rendered and loaded again
- **WHEN** the machine case data block is parsed
- **THEN** `domain_coverage`, `user_stories`, and `acceptance_functions` SHALL
  match the original package
