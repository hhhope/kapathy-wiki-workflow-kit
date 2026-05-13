## ADDED Requirements

### Requirement: Operational advertising platform prototype

The repository SHALL provide a standalone repo-local advertising delivery
platform prototype that behaves as an operable backstage system rather than a
customer-facing marketing demo.

#### Scenario: Prototype exposes the full module workbench

- **WHEN** a reviewer opens the prototype
- **THEN** it SHALL show module entries for 总览, 投流方, 流量方, 平台运营, 广告核心, 规则引擎, 财务管理, 埋点与三方, and 报表监控
- **AND** it SHALL provide role switching and a right-side state/log rail.

#### Scenario: Prototype supports local-state operations

- **WHEN** a reviewer submits budgets, strategies, rules, recharge, alerts,
  reports, tracking events, or cross-media operations
- **THEN** the prototype SHALL update local mock state and show the result in
  tables, badges, logs, or detail panels without requiring a backend.

#### Scenario: Prototype includes architecture and PRD flow surfaces

- **WHEN** a reviewer inspects system design details
- **THEN** the prototype SHALL include overall architecture, module architecture,
  and sequence-flow surfaces covering the requested advertising platform flows.

#### Scenario: Prototype preserves proof boundary

- **WHEN** the prototype is claimed complete
- **THEN** a repo-visible gate review SHALL record that this is local prototype
  evidence only, with no Feishu sync, no real external API integration, and no
  production readiness claim.
