# Design: Ad Platform Operational Prototype

## Source

- User corrected requirement: build an operable advertising delivery system
  prototype, not a customer demo.
- Design source: `docs/superpowers/specs/2026-05-13-ad-platform-operational-prototype-design.md`.
- Input material: `inbox/ad-desgin.md`.

## Output

Create `wiki/reports/ad-platform-operational-prototype.html` as a standalone
desktop-first backstage prototype. The file must include inline CSS and
JavaScript only. It must open directly in a browser and must not depend on a
backend or external assets.

## Required Modules

- 总览
- 投流方
- 流量方
- 平台运营
- 广告核心
- 规则引擎
- 财务管理
- 埋点与三方
- 报表监控

## Required State Contract

The prototype must expose `window.AdPrototype` with seeded local mock state and
these top-level state collections:

- `advertisers`
- `trafficSources`
- `mediaAccounts`
- `campaigns`
- `budgets`
- `strategies`
- `rules`
- `alerts`
- `financeLedger`
- `trackingEvents`
- `reports`
- `operationsLog`

State must persist with `localStorage` and provide a visible reset action.

## Required Operations

- Module navigation changes active module.
- Role switcher changes visible role and action context.
- Budget submit updates campaign/budget state and operation log.
- Strategy submit updates campaign strategy.
- Traffic placement creation updates placement status and event log.
- Funnel alert handling updates alert status and action log.
- Cross-media copy creates a copy task and target campaign.
- Auto-bid simulation changes bid state and strategy log.
- Budget redistribution changes campaign budgets and finance/budget log.
- Rule test/publish updates rule status and rule execution log.
- Recharge updates merchant balance and finance ledger.
- Refund and invoice submissions create pending records.
- Credential generation and test event sending update integration/tracking logs.
- Report generation and template save append report records.

## Required Diagram Surfaces

The prototype must include visible architecture surfaces for all modules and
sequence-flow surfaces for budget setting, traffic placement integration, revenue
evaluation, funnel alert handling, cross-media copy, automated bid adjustment,
rule execution, finance flows, SDK event tracking, and real-time report data
flow.

## Verification Boundary

This is a repo-local operational prototype. Browser verification proves local
interaction behavior only. It does not prove production readiness, real API
integration, payment correctness, invoice correctness, or customer acceptance.
