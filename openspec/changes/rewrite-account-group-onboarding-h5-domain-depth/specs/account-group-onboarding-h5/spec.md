# account-group-onboarding-h5 Spec Delta

## ADDED Requirements

### Requirement: Domain-Dense Capability Map

The H5 SHALL include a capability map with more than three capability groups
and SHALL cover account basic capability, parent-child or multi-account model,
unified accounting capability, clearing/settlement capability,
reconciliation/reporting/data-service capability, unified balance capability,
and source-backed revenue capability.

#### Scenario: capability map is reviewable

- **WHEN** a reviewer reads the capability map section
- **THEN** they can identify account lifecycle, account type management,
  parent-child account relation, multi-account model, accounting query, daily
  cut, reverse or adjustment, clearing/settlement, reconciliation or difference
  handling, available balance, real-time balance, frozen balance, report
  capability, and data/service capability.

### Requirement: Excluded Capability Groups

The H5 SHALL NOT present `授信能力` or `垫资能力` as account-group capability
groups.

#### Scenario: rejected capability groups are absent

- **WHEN** a reviewer greps the H5 for `授信能力|垫资能力`
- **THEN** there are no reader-facing capability-group matches.

### Requirement: Layered System Architecture

The H5 SHALL include a layered architecture section covering entrance/gateway,
product layer, service layer, data layer, payment channel or partner bank
connections, and operation/back-office sides.

#### Scenario: architecture section is present

- **WHEN** a reviewer reads the system architecture section
- **THEN** it names API/H5/BM or upstream entrance, product layer, service
  layer, data layer, payment channels or partner banks, and operation/back-office
  sides.

### Requirement: Complete Core Chain

The H5 SHALL describe the core chain from entry/account opening through account
model and bank-account relation, transaction or payment, split account or
withdrawal or refund, accounting/voucher/balance, clearing/settlement,
reconciliation/report/difference handling, and risk/monitoring/observability.

#### Scenario: core chain includes account-domain checkpoints

- **WHEN** a reviewer reads the core chain section
- **THEN** they can follow how identity/account relation, fund movement,
  internal accounting/balance, external clearing/settlement, and
  reconciliation/reporting connect.

### Requirement: Account-Domain AI Collaboration

The H5 SHALL explain OpenSpec, Lore, Graphify, and lore-bootstrap as
account-domain engineering aids rather than generic AI tools.

#### Scenario: AI section is tied to account work

- **WHEN** a reviewer reads the AI collaboration section
- **THEN** it explains at least historical design lookup, duplicate capability
  checks, structure lookup, design/review/verification evidence, or reusable
  knowledge capture for account-domain work.
