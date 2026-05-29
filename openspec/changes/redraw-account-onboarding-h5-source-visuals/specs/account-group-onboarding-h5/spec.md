# account-group-onboarding-h5 Spec Delta

## ADDED Requirements

### Requirement: Source-Backed Visual Redraw

The H5 SHALL include standalone source-backed visual assets for the account
capability map, system architecture, core chain, and Nirvana/latest-project
entry map.

#### Scenario: source visuals are present

- **WHEN** a reviewer inspects the H5
- **THEN** it references local visual assets for capability map, system
  architecture, core chain, and Nirvana/latest-project entry map
- **AND** the visuals are not replaced by generic card grids alone.

### Requirement: Visual Gate Failure Record

The gate review SHALL record that the prior Visual Gate pass claim was invalid
and explain the failure mode before declaring the repaired H5 reviewable.

#### Scenario: visual failure is auditable

- **WHEN** a reviewer opens the gate review
- **THEN** it identifies the box-heavy CSS layout as a failed visual gate result
- **AND** it records the new source-to-visual mapping and repair evidence.

### Requirement: Nirvana And Latest Project Visual Coverage

The H5 SHALL visually cover Nirvana current-state pressure, target/optimized
architecture, clearing/account-service relation, and latest project entry
points relevant to account-group newcomers.

#### Scenario: project work is visible

- **WHEN** a new graduate reads the active project section
- **THEN** they can see where Nirvana, split-account/core改造, clearing,
  reconciliation/reporting, account model, and bank/channel connections enter
  real account-group work.

### Requirement: Sensitive Visual Boundary

The H5 and its local visual assets SHALL NOT expose credentials, internal URLs,
Feishu links, QR codes, personal contacts, or access instructions.

#### Scenario: sensitive text is absent

- **WHEN** a reviewer greps the H5 and visual assets for sensitive patterns
- **THEN** no reader-facing matches are found for credentials, internal URLs,
  Feishu URLs, tokens, QR-code instructions, personal emails, or access
  instructions.
