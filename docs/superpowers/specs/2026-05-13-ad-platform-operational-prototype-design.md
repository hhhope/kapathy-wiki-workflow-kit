# Ad Platform Operational Prototype Design

## Context

The previous `ad-growth-cockpit-h5` prototype drifted toward a customer-facing
Growth Cockpit demo. The corrected requirement is different: build an actually
operable advertising delivery system prototype that covers system architecture
and concrete PRD flows.

This design is for a repo-local prototype, not a customer demo, not a slide deck,
and not a Feishu-ready publication.

## Source Requirement

Source: `inbox/ad-desgin.md` and the user's corrected request.

The prototype must cover:

1. 投流方模块
2. 流量方模块
3. 平台模块
4. 广告核心系统 / 智能投放策略
5. 规则引擎
6. 财务管理系统
7. 数据埋点与三方对接方案
8. 数据报表与实时监控

The output should also include system architecture, module-level architecture,
functional PRD design, and sequence-diagram surfaces.

## Goal

Build an operational backstage prototype for an advertising delivery platform.
The prototype should let a reviewer click through modules, submit forms, update
local state, inspect architecture diagrams, and inspect module-level sequence
flows.

It should feel like a real internal operating system, not a marketing H5.

## Chosen Approach

Chosen approach: **module-workbench prototype**.

- Full module coverage.
- Local mock data is operable.
- A unified platform backstage is the main shell.
- Roles can be switched in the top bar.
- Each module has at least one meaningful operation that changes local state.

Rejected approaches:

- Customer Growth Cockpit: too presentation-oriented and not close enough to the
  requested PRD/system design.
- Flow-only wizard: clear for one end-to-end demo, but weak for a real platform
  with advertiser, traffic-side, platform, finance, rules, and monitoring roles.
- Design-document-with-embedded-panels: close to the document request, but risks
  becoming a PPT-like deliverable instead of an operable system prototype.

## Product Shape

The prototype is a desktop-first enterprise SaaS backstage.

Global layout:

- Left navigation:
  - 总览
  - 投流方
  - 流量方
  - 平台运营
  - 广告核心
  - 规则引擎
  - 财务管理
  - 埋点与三方
  - 报表监控
- Top bar:
  - Role switcher: 平台管理员, 广告主/优化师, 流量方, 财务, 运维
  - Current tenant / advertiser
  - Simulated time
  - Global search
  - Notification entry
- Main work area:
  - The selected module's table, forms, detail drawer, diagrams, or dashboard.
- Right side state rail:
  - Active alerts
  - Rule execution log
  - Budget / balance state
  - Recent operations
  - Data refresh status

Visual direction:

- Light, professional SaaS backstage.
- Dense but readable tables and forms.
- No hero-style marketing layout.
- Minimal decorative motion.
- Tables, filters, tabs, drawers, modals, forms, state tags, and diagrams are the
  primary UI elements.

## Module Scope

### 1. Overview

Purpose: platform-level entry and health surface.

Required surfaces:

- KPI cards for spend, impressions, clicks, conversions, CPA, ROAS, balance, and
  active alerts.
- Cross-module shortcuts.
- Recent rule executions.
- Budget warnings.
- Media API status.
- System architecture panel with tabs:
  - Overall architecture
  - Data flow
  - Module map

Representative operation:

- Click a KPI or alert to jump to the relevant module and highlight the related
  row or panel.

### 2. 投流方模块

Purpose: advertiser / optimizer operations.

Required features:

- Budget configuration:
  - Daily budget
  - Total budget
  - Time-window budget
  - Account / campaign / ad-group levels
- Strategy configuration:
  - Cost control
  - Volume-first
  - ROI-first
- Monitoring metric configuration:
  - CPA
  - ROI
  - Spend spike
  - Conversion drop
- Real-time delivery data:
  - Account, campaign, ad group, creative drill-down.
- Review report:
  - Generate daily or weekly report.

Representative operations:

- Create or edit budget, then update campaign budget state and operation log.
- Choose a delivery strategy, then update the campaign's strategy badge.
- Create a monitoring rule, then create a linked alert rule.
- Generate a review report, then append a report record.

### 3. 流量方模块

Purpose: traffic-side resource access and performance visibility.

Required features:

- Traffic-source registration.
- App creation.
- Ad placement creation:
  - Splash
  - Rewarded video
  - Native feed
  - Interstitial
  - Banner
- Exposure and conversion board:
  - Impressions
  - Clicks
  - CTR
  - Conversions
  - Revenue
- Integration status:
  - Pending
  - Testing
  - Online
  - Error
  - Disabled

Representative operation:

- Create an ad placement; status moves from pending to testing or online and a
  test event appears in the right-side log.

### 4. 平台模块

Purpose: platform operation and advertiser value evaluation.

Required features:

- Advertiser revenue ranking.
- ROI / LTV / CAC comparison.
- CPM -> CPC -> CPA -> CPS funnel.
- Funnel anomaly warning:
  - Funnel cliff
  - Cost overrun
  - Traffic anomaly
- Alert handling actions:
  - Pause campaign
  - Notify optimizer
  - Record observation

Representative operation:

- Handle a funnel alert; alert status changes and may update campaign status or
  trigger a rule/action log.

### 5. 广告核心系统 / 智能投放策略

Purpose: cross-media account and delivery execution center.

Required features:

- Media account management:
  - 巨量引擎
  - 腾讯广告
  - Google Ads
  - Meta
  - 自营媒体
- Account authorization status.
- Cross-media copy:
  - Source media / campaign
  - Target media
  - Field mapping preview
  - Copy task result
- Automated bidding:
  - CPA over target -> lower bid
  - Spend under pace -> raise bid
  - Single adjustment cap
- Budget redistribution:
  - Move budget from low-efficiency campaign to high-ROAS campaign.
- Creative rotation:
  - Uniform rotation
  - CTR-weighted rotation
  - Explore/exploit
- Attribution and LTV callback:
  - Conversion callback
  - LTV callback
  - Media optimization feedback

Representative operations:

- Copy one campaign across media; create copy task and resulting target campaign.
- Run auto-bid simulation; update bid and append strategy log.
- Move budget; update budget values and finance/budget log.
- Trigger LTV callback; append attribution event.

### 6. 规则引擎

Purpose: no-code visual rule configuration.

Required features:

- Visual rule editor:
  - Condition blocks
  - AND / OR logic
  - Action blocks
- Conditions:
  - Spend
  - CPA
  - ROI
  - Conversion count
  - Time window
  - Media
  - Campaign
- Actions:
  - Adjust bid
  - Change budget
  - Pause campaign
  - Switch creative
  - Send alert
- Rule lifecycle:
  - Draft
  - Tested
  - Published
  - Running
  - Paused
  - Rolled back

Representative operations:

- Build a rule, test it against mock data, publish it, and show it as running in
  the right-side rule log.

### 7. 财务管理

Purpose: merchant balance, budget consumption, refund, and invoice operations.

Required features:

- Recharge:
  - Amount
  - Payment channel
  - Payment callback simulation
- Budget consumption:
  - Freeze
  - Deduct
  - Release
  - Ledger detail
- Refund:
  - Apply
  - Review
  - Execute
- Invoice:
  - Select consumption records
  - Submit invoice information
  - Generate invoice request

Representative operations:

- Recharge; merchant balance increases and finance ledger receives a recharge
  record.
- Submit refund; refund status becomes pending review.
- Submit invoice; invoice request appears in the invoice list.

### 8. 数据埋点与三方对接

Purpose: integration documentation and test event simulation.

Required features:

- SDK / API integration docs:
  - Web SDK
  - Android SDK
  - iOS SDK
  - Server API
- AppKey / AppSecret generation.
- Event test sender:
  - Exposure
  - Click
  - Conversion
  - Purchase
- Attribution partner configuration:
  - AppsFlyer
  - Adjust
  - 热云
  - 自建归因
- Callback URL and event mapping.

Representative operation:

- Generate credentials or send a test event; event appears in tracking log and
  real-time monitoring.

### 9. 数据报表与实时监控

Purpose: reporting and system monitoring.

Required features:

- Real-time report:
  - Spend
  - Impressions
  - Clicks
  - Conversions
  - CPA
  - ROAS
- Custom report builder:
  - Select dimensions
  - Select metrics
  - Save template
- Real-time system monitoring:
  - QPS
  - Tracking failure rate
  - Media API latency
  - Budget overrun count
- Alert center:
  - Confirm
  - Assign
  - Close

Representative operations:

- Save a custom report template.
- Confirm or close a monitoring alert.

## Shared State Model

The prototype uses local mock state. It should not be a collection of isolated
screens.

Core entities:

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

State-flow examples:

- Campaign lifecycle:
  - Draft -> budget configured -> strategy configured -> running -> paused/end.
- Budget lifecycle:
  - Available balance -> campaign freeze -> consumption deduction -> release or
    overrun alert.
- Rule lifecycle:
  - Draft -> tested -> published -> running -> paused/rolled back.
- Alert lifecycle:
  - Open -> auto-handling -> needs confirmation -> handled/closed.
- Traffic-source lifecycle:
  - Pending -> testing -> online -> error/disabled.
- Finance lifecycle:
  - Recharge -> balance increase.
  - Campaign start -> budget freeze.
  - Delivery event -> ledger deduction.
  - Refund request -> pending review -> refunded.
  - Invoice request -> pending invoice -> issued.

## Architecture And Sequence Diagram Surfaces

The prototype should include architecture and sequence diagram surfaces as
inspectable panels, not as the main marketing story.

Required diagram surfaces:

- Overall system architecture.
- 投流方 module architecture.
- 流量方 module architecture.
- 平台 module architecture.
- 广告核心 module architecture.
- 规则引擎 module architecture.
- 财务管理 module architecture.
- 数据埋点与三方对接 architecture.
- 数据报表与实时监控 architecture.

Required sequence-flow surfaces:

- Budget setting and budget deduction.
- Traffic placement integration.
- Revenue evaluation.
- Funnel alert handling.
- Cross-media copy.
- Automated bid adjustment.
- Rule publish and execution.
- Recharge / refund / invoice.
- SDK event tracking.
- Real-time report data flow.

The diagrams can be implemented as readable HTML/SVG/Mermaid-style static
panels. A later production version may replace them with a dedicated diagram
renderer.

## Prototype Interactions

Minimum interactive behaviors:

- Module navigation updates active module and main content.
- Role switcher updates visible role label and can alter available actions.
- KPI clicks navigate to the relevant module.
- Forms can be submitted and update local state.
- Tables can open detail drawers.
- Alerts can be handled and status changes.
- Rules can be tested and published.
- Budget, recharge, refund, invoice, report, and tracking events append records.
- Cross-media copy creates a mock copy task and a target campaign record.
- Right-side log updates after each operation.

## Non-Goals

- No real backend.
- No real authentication or permission system.
- No real payment, invoice, media API, attribution API, or SDK network call.
- No customer-facing marketing H5.
- No Feishu sync.
- No production readiness claim.

## Suggested Output Files

Implementation should be planned separately after this design is approved.

Suggested files:

- `wiki/reports/ad-platform-operational-prototype.html`
  - Static operable prototype.
- `tests/test_ad_platform_operational_prototype.py`
  - Static and behavior-surface contract tests.
- `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`
  - Public/report gate review and intent correction record.
- `openspec/changes/build-ad-platform-operational-prototype/`
  - New OpenSpec change for implementation.

The existing completed `build-ad-growth-cockpit-h5` change must not be expanded.

## Verification Plan

Minimum verification before claiming the prototype complete:

- Unit/static tests for module coverage and interaction hooks.
- `python3 scripts/check_behavior_assets.py`.
- `python3 scripts/check_wiki_frontmatter.py`, with any unrelated legacy drift
  recorded separately.
- `git diff --check`.
- Browser verification with Playwright or equivalent:
  - Nine module entries switch correctly.
  - Budget form updates campaign/budget state.
  - Strategy form updates campaign strategy.
  - Rule test/publish updates rule status and log.
  - Recharge updates merchant balance and finance ledger.
  - Alert handling updates alert state.
  - Report generation appends a report record.
  - Architecture and sequence panels are reachable.

## Implementation Decisions

- Keep the first implementation as one standalone HTML file with inline CSS and
  JavaScript. This preserves the same open-directly delivery model as earlier
  repo-local H5 artifacts and avoids adding a build chain before the prototype
  proves useful.
- Use local mock state with `localStorage` persistence and a visible reset action.
  A reviewer should be able to refresh without losing the current simulated
  state, while still being able to return to the seeded scenario.
- Give deeper browser interaction coverage to these flows:
  - Budget setup -> campaign budget state -> operation log.
  - Rule test/publish -> running rule state -> rule execution log.
  - Recharge -> merchant balance -> finance ledger.
  - Alert handling -> alert state -> linked action log.
- Treat the existing Growth Cockpit H5 as an exploratory artifact that is
  superseded for the corrected operational-prototype requirement. Do not delete
  it as part of the new implementation unless the user asks for cleanup later.
