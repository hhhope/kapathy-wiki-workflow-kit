# stripe-h5-domain-language Specification

## ADDED Requirements

### Requirement: Financial transaction design-language thesis

The Stripe AI company evolution H5 SHALL present `金融交易设计语言` as the
reader-facing mainline for this change.

#### Scenario: H5 opening states the approved thesis

- **GIVEN** the reader opens `wiki/reports/stripe-ai-company-evolution-h5.html`
- **WHEN** the first viewport is rendered
- **THEN** the H5 includes `从 Stripe 看 AI 时代金融交易设计语言`
- **AND** explains that AI lowers coding/integration cost while financial
  domain design remains scarce.

#### Scenario: Rejected thesis terms are not reader-facing mainline

- **GIVEN** the H5 is checked for old thesis terms
- **WHEN** the visible reader-facing body is searched
- **THEN** `可信交易执行层`, `控制平面`, `交易控制面`, `交易控制点`, and `交易规则层`
  are not used as the main thesis.

### Requirement: Load-bearing chapter group

The H5 SHALL implement the approved chapter group for explaining the thesis:
sample selection, financial transaction design language, and Stripe capability
accumulation.

#### Scenario: Chapters 2/3/4 are visible

- **GIVEN** the H5 is rendered
- **WHEN** the reader scans the main sections
- **THEN** the page includes `为什么用 Stripe 做观察样本`
- **AND** includes `AI 支付需要一套金融交易设计语言`
- **AND** includes `Stripe 是怎么把这套语言攒出来的`.

#### Scenario: Chapter 3 defines the domain-language model

- **GIVEN** the reader reaches the domain-language chapter
- **WHEN** the section explains the model
- **THEN** it covers object, interface, permission, rule, money relationship,
  and responsibility evidence.

### Requirement: People and hiring evidence modules

The H5 SHALL preserve LinkedIn and JD as distinct evidence modules with proof
boundaries.

#### Scenario: LinkedIn is a people-capability profile

- **GIVEN** the reader reaches the organization evidence section
- **WHEN** LinkedIn is discussed
- **THEN** it is framed as current people background and capability mapping
- **AND** it is not treated as standalone proof of Stripe strategy success.

#### Scenario: JD is hiring intent and capability build signal

- **GIVEN** the reader reaches the hiring evidence section
- **WHEN** JD material is discussed
- **THEN** it is framed as capability-building intent
- **AND** it is not treated as proof of shipped product outcome.

### Requirement: Verification evidence

The change SHALL record verification evidence for the revised H5 before
completion is claimed.

#### Scenario: Static and visual checks are recorded

- **GIVEN** implementation is complete
- **WHEN** validation is recorded
- **THEN** the report gate review includes required/rejected thesis grep,
  HTML parse, diff check, desktop screenshot, and mobile screenshot evidence.
