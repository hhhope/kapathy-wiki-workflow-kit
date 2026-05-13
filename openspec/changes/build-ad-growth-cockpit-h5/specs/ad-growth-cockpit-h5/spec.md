## ADDED Requirements

### Requirement: Customer-facing ad growth cockpit H5

The repository SHALL provide a standalone customer-facing H5 prototype that
translates the advertising delivery system design into a Growth Cockpit demo for
advertisers and customer-side decision makers.

#### Scenario: Prototype exposes the customer journey

- **WHEN** a reader opens the H5 prototype
- **THEN** it SHALL present sections for live cockpit, money flow,
  optimization, anomaly handling, and review
- **AND** the content SHALL emphasize advertiser-facing outcomes instead of an
  internal PRD outline.

#### Scenario: Prototype has real demo interactions

- **WHEN** a reader uses the H5 prototype
- **THEN** section navigation, KPI jumps, money-flow view toggles, alert
  expansion, and review CTA navigation SHALL work without a backend.

#### Scenario: Prototype preserves publication boundary

- **WHEN** the prototype is prepared for review
- **THEN** the repository SHALL keep a public-output gate review record stating
  the target audience, selected Growth Cockpit direction, prototype boundary,
  and absence of Feishu sync or production rollout claims.
