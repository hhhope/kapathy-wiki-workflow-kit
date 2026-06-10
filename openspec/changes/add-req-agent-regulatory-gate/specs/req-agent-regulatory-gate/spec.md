## ADDED Requirements

### Requirement: req-agent SHALL expose a regulatory obligation gate

`req-agent` SHALL include a regulatory obligation gate in normal requirements
readiness evidence.

#### Scenario: Non-regulatory case is checked

- **GIVEN** a requirements case does not include `risk_compliance`
- **AND** it has no explicit regulatory, identity, authorization, consent,
  personal-information, SMS-link, token, or compliance signals
- **WHEN** strict requirements readiness is checked
- **THEN** `regulatory_gate.passed` SHALL be true
- **AND** `regulatory_gate.mode` SHALL be `not_triggered`

#### Scenario: Risk compliance case lacks regulatory obligations

- **GIVEN** a requirements case includes `risk_compliance`
- **AND** it has no `soft_evidence.regulatory_obligations`
- **WHEN** strict requirements readiness is checked
- **THEN** the checker SHALL block requirement readiness
- **AND** the checker SHALL report `regulatory_obligations_missing`

### Requirement: Regulatory obligations SHALL be case-local evidence objects

Triggered requirements cases SHALL carry case-local regulatory obligations
instead of relying on generic domain labels.

#### Scenario: Regulatory obligation is confirmed and mapped

- **GIVEN** a triggered requirements case has a regulatory obligation with
  `status: confirmed`
- **AND** it has owner refs, source basis, obligation text, acceptance function
  refs, and an evidence anchor
- **WHEN** strict requirements readiness is checked
- **THEN** the regulatory gate SHALL accept that obligation

#### Scenario: Regulatory obligation is unresolved

- **GIVEN** a triggered requirements case has a regulatory obligation with
  `status: unresolved`
- **WHEN** strict requirements readiness is checked
- **THEN** the checker SHALL block requirement readiness
- **AND** it SHALL report `regulatory_obligation_unresolved`

#### Scenario: Regulatory waiver lacks evidence

- **GIVEN** a triggered requirements case has a regulatory obligation with
  `status: waived`
- **AND** it has no waiver reason or waiver reference
- **WHEN** strict requirements readiness is checked
- **THEN** the checker SHALL block requirement readiness

### Requirement: req-agent SHALL route regulatory obligations through workers

`req-agent` SHALL identify regulatory obligations after domain analysis, assign
ownership during scope, convert confirmed obligations to acceptance functions,
and verify synchronization during human review.

#### Scenario: SMS legal representative verification requirement

- **GIVEN** source material mentions legal representative SMS verification,
  compliance, identity binding, H5 links, token, or personal information
- **WHEN** `req-agent` routes the requirement lifecycle
- **THEN** `req-domain-analysis` SHALL surface regulatory obligation questions
- **AND** `req-scope` SHALL require owner assignment or blockers
- **AND** `req-acceptance` SHALL require observable acceptance mappings
- **AND** `req-human-review` SHALL require every regulatory demand fact to be
  synchronized into the machine case before handoff
