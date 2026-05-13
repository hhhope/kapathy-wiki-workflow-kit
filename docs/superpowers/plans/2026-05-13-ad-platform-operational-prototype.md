# Ad Platform Operational Prototype Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repo-local, actually operable advertising delivery platform backstage prototype that covers all requested modules, architecture surfaces, PRD flows, and local-state interactions.

**Architecture:** Create a new OpenSpec change, then build a standalone HTML/CSS/JavaScript prototype with seeded mock state, `localStorage` persistence, module navigation, forms, status changes, diagrams, and operation logs. Add contract tests and a repo-visible report gate review that records the correction from customer-facing Growth Cockpit demo to operational system prototype.

**Tech Stack:** Static HTML/CSS/JavaScript, browser `localStorage`, Python `unittest`, Playwright for browser interaction verification, no backend, no external dependencies.

---

## File Structure

- Create `openspec/changes/build-ad-platform-operational-prototype/proposal.md`
  - Scope boundary for the corrected operational prototype.
- Create `openspec/changes/build-ad-platform-operational-prototype/design.md`
  - Implementation design copied and condensed from `docs/superpowers/specs/2026-05-13-ad-platform-operational-prototype-design.md`.
- Create `openspec/changes/build-ad-platform-operational-prototype/tasks.md`
  - Execution checklist for this plan.
- Create `openspec/changes/build-ad-platform-operational-prototype/specs/ad-platform-operational-prototype/spec.md`
  - OpenSpec delta requirements.
- Create `tests/test_ad_platform_operational_prototype.py`
  - Static contract tests for module coverage, operation hooks, diagrams, state contract, and gate review artifact.
- Create `wiki/reports/ad-platform-operational-prototype.html`
  - Standalone operable backstage prototype.
- Create `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`
  - Public/report gate review record with intent correction, proof boundary, and final verification notes.

Do not modify or extend `openspec/changes/build-ad-growth-cockpit-h5/`; that change is complete and the old H5 is superseded for this corrected requirement.

---

### Task 1: OpenSpec Boundary

**Files:**
- Create: `openspec/changes/build-ad-platform-operational-prototype/proposal.md`
- Create: `openspec/changes/build-ad-platform-operational-prototype/design.md`
- Create: `openspec/changes/build-ad-platform-operational-prototype/tasks.md`
- Create: `openspec/changes/build-ad-platform-operational-prototype/specs/ad-platform-operational-prototype/spec.md`

- [ ] **Step 1: Create the OpenSpec proposal**

Create `openspec/changes/build-ad-platform-operational-prototype/proposal.md`:

```markdown
# Build Ad Platform Operational Prototype

## Why

The existing Growth Cockpit H5 explored a customer-facing demo, but the corrected
requirement is an actually operable advertising delivery system prototype. The
new prototype must cover the requested architecture, module-level PRD flows, and
local-state operations across the full advertising platform.

## What Changes

- Add a standalone operational backstage prototype at `wiki/reports/ad-platform-operational-prototype.html`.
- Add contract tests for module coverage, stateful interaction hooks, architecture and sequence surfaces, and drift prevention.
- Add a repo-visible report gate review that records the intent correction and proof boundary.

## Non-Goals

- No real backend, login, payment, invoice, media API, SDK network call, or attribution API call.
- No Feishu sync or production readiness claim.
- No deletion of the existing Growth Cockpit H5 unless requested separately.

## Impact

- Adds one prototype HTML artifact.
- Adds one test file.
- Adds one ops gate review artifact.
- Leaves existing completed Growth Cockpit artifacts intact as exploratory output.
```

- [ ] **Step 2: Create the OpenSpec design**

Create `openspec/changes/build-ad-platform-operational-prototype/design.md`:

```markdown
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
```

- [ ] **Step 3: Create OpenSpec tasks**

Create `openspec/changes/build-ad-platform-operational-prototype/tasks.md`:

```markdown
# Tasks

- [ ] 1. Add OpenSpec boundary
  - Create proposal, design, tasks, and spec delta.
  - Validate the change with `openspec validate build-ad-platform-operational-prototype --strict`.

- [ ] 2. Add RED contract test
  - Create `tests/test_ad_platform_operational_prototype.py`.
  - Verify it fails before the prototype and gate review exist.

- [ ] 3. Build standalone operational prototype
  - Create `wiki/reports/ad-platform-operational-prototype.html`.
  - Implement required modules, mock state, operations, architecture surfaces,
    sequence surfaces, and reset/persistence behavior.

- [ ] 4. Add report gate review
  - Create `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`.
  - Record intent correction, proof boundary, and verification status.

- [ ] 5. Verify and record completion
  - Run unit/static tests.
  - Run behavior asset check.
  - Run wiki frontmatter check and record unrelated legacy drift separately.
  - Run browser interaction verification.
  - Update this task list and the gate review evidence.
```

- [ ] **Step 4: Create OpenSpec requirement delta**

Create `openspec/changes/build-ad-platform-operational-prototype/specs/ad-platform-operational-prototype/spec.md`:

```markdown
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
```

- [ ] **Step 5: Validate OpenSpec change**

Run:

```bash
openspec validate build-ad-platform-operational-prototype --strict
```

Expected: output contains `Change 'build-ad-platform-operational-prototype' is valid`. PostHog network flush errors may appear after the validation line and are non-blocking.

- [ ] **Step 6: Commit the OpenSpec boundary**

Run:

```bash
git add openspec/changes/build-ad-platform-operational-prototype/proposal.md \
  openspec/changes/build-ad-platform-operational-prototype/design.md \
  openspec/changes/build-ad-platform-operational-prototype/tasks.md \
  openspec/changes/build-ad-platform-operational-prototype/specs/ad-platform-operational-prototype/spec.md
git commit -m "docs: propose ad platform operational prototype"
```

---

### Task 2: RED Contract Test

**Files:**
- Create: `tests/test_ad_platform_operational_prototype.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_ad_platform_operational_prototype.py`:

```python
import re
import unittest
from pathlib import Path


HTML = Path("wiki/reports/ad-platform-operational-prototype.html")
GATE_REVIEW = Path("wiki/ops/ad-platform-operational-prototype-report-gate-review.md")


class AdPlatformOperationalPrototypeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = HTML.read_text(encoding="utf-8")

    def test_shell_and_all_modules_exist(self) -> None:
        for label in [
            "总览",
            "投流方",
            "流量方",
            "平台运营",
            "广告核心",
            "规则引擎",
            "财务管理",
            "埋点与三方",
            "报表监控",
        ]:
            self.assertIn(label, self.html)

        for module_id in [
            "overview",
            "advertiser",
            "traffic",
            "platform",
            "core",
            "rules",
            "finance",
            "integration",
            "reports",
        ]:
            self.assertIn(f'data-module="{module_id}"', self.html)
            self.assertIn(f'id="module-{module_id}"', self.html)

        self.assertIn('id="roleSwitcher"', self.html)
        self.assertIn('id="stateRail"', self.html)
        self.assertIn('id="resetPrototype"', self.html)

    def test_requirement_mapping_is_operational_not_demo(self) -> None:
        required_phrases = [
            "日预算",
            "总预算",
            "时段预算",
            "成本控制",
            "量级优先",
            "ROI 最优",
            "广告位",
            "CPM",
            "CPC",
            "CPA",
            "CPS",
            "跨媒体复制",
            "自动调价",
            "预算分配",
            "创意轮播",
            "多维度归因",
            "LTV 回传",
            "无代码",
            "商户充值",
            "退款",
            "开票",
            "AppKey",
            "AppSecret",
            "SDK",
            "API",
            "实时监控",
            "自定义报表",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, self.html)

        forbidden_phrases = [
            "客户演示驾驶舱",
            "投放增长驾驶舱",
            "查看本周投放复盘",
            "营销落地页",
        ]
        for phrase in forbidden_phrases:
            self.assertNotIn(phrase, self.html)

    def test_state_contract_and_persistence_hooks_exist(self) -> None:
        for state_key in [
            "advertisers",
            "trafficSources",
            "mediaAccounts",
            "campaigns",
            "budgets",
            "strategies",
            "rules",
            "alerts",
            "financeLedger",
            "trackingEvents",
            "reports",
            "operationsLog",
        ]:
            self.assertIn(state_key, self.html)

        for function_name in [
            "seedState",
            "loadState",
            "saveState",
            "resetState",
            "setActiveModule",
            "switchRole",
            "updateLog",
            "render",
        ]:
            self.assertIn(f"function {function_name}", self.html)

        self.assertIn("localStorage", self.html)
        self.assertIn("ad-platform-operational-prototype-state", self.html)
        self.assertIn("window.AdPrototype", self.html)

    def test_operational_actions_are_wired(self) -> None:
        action_contracts = {
            "budgetForm": "submitBudget",
            "strategyForm": "submitStrategy",
            "trafficPlacementForm": "createTrafficPlacement",
            "handleFunnelAlert": "handleFunnelAlert",
            "copyCampaignAcrossMedia": "copyCampaignAcrossMedia",
            "runAutoBidSimulation": "runAutoBidSimulation",
            "redistributeBudget": "redistributeBudget",
            "sendLtvCallback": "sendLtvCallback",
            "testRule": "testRule",
            "publishRule": "publishRule",
            "rechargeForm": "rechargeMerchant",
            "refundForm": "submitRefund",
            "invoiceForm": "submitInvoice",
            "generateCredentials": "generateCredentials",
            "sendTestEvent": "sendTestEvent",
            "saveReportTemplate": "saveReportTemplate",
            "confirmMonitoringAlert": "confirmMonitoringAlert",
            "generateReviewReport": "generateReviewReport",
        }
        for element_id, function_name in action_contracts.items():
            self.assertIn(element_id, self.html)
            self.assertIn(f"function {function_name}", self.html)

    def test_architecture_and_sequence_surfaces_exist(self) -> None:
        for diagram in [
            "overall-architecture",
            "advertiser-architecture",
            "traffic-architecture",
            "platform-architecture",
            "core-architecture",
            "rules-architecture",
            "finance-architecture",
            "integration-architecture",
            "reports-architecture",
        ]:
            self.assertIn(f'data-diagram="{diagram}"', self.html)

        for sequence in [
            "budget-sequence",
            "traffic-placement-sequence",
            "revenue-evaluation-sequence",
            "funnel-alert-sequence",
            "cross-media-copy-sequence",
            "auto-bid-sequence",
            "rule-execution-sequence",
            "finance-sequence",
            "tracking-sequence",
            "realtime-report-sequence",
        ]:
            self.assertIn(f'data-sequence="{sequence}"', self.html)

    def test_gate_review_artifact_exists(self) -> None:
        content = GATE_REVIEW.read_text(encoding="utf-8")
        for phrase in [
            "Article Intent Contract",
            "operable advertising delivery system prototype",
            "not a customer demo",
            "No Feishu sync",
            "local prototype",
        ]:
            self.assertIn(phrase, content)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the RED test**

Run:

```bash
python3 -m unittest tests.test_ad_platform_operational_prototype -v
```

Expected: fail with `FileNotFoundError` because `wiki/reports/ad-platform-operational-prototype.html` does not exist yet.

- [ ] **Step 3: Commit the RED test**

Run:

```bash
git add tests/test_ad_platform_operational_prototype.py
git commit -m "test: cover ad platform operational prototype"
```

---

### Task 3: Standalone Operational Prototype

**Files:**
- Create: `wiki/reports/ad-platform-operational-prototype.html`

- [ ] **Step 1: Create the HTML shell**

Create `wiki/reports/ad-platform-operational-prototype.html` as a standalone document:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>广告投流系统 · 可操作原型</title>
  <style>
    /* Implement desktop-first enterprise SaaS backstage styling here. */
  </style>
</head>
<body>
  <div class="app-shell">
    <aside class="side-nav" aria-label="主模块导航">
      <button data-module="overview" type="button">总览</button>
      <button data-module="advertiser" type="button">投流方</button>
      <button data-module="traffic" type="button">流量方</button>
      <button data-module="platform" type="button">平台运营</button>
      <button data-module="core" type="button">广告核心</button>
      <button data-module="rules" type="button">规则引擎</button>
      <button data-module="finance" type="button">财务管理</button>
      <button data-module="integration" type="button">埋点与三方</button>
      <button data-module="reports" type="button">报表监控</button>
    </aside>
    <div class="workspace">
      <header class="top-bar">
        <select id="roleSwitcher" aria-label="角色切换">
          <option>平台管理员</option>
          <option>广告主/优化师</option>
          <option>流量方</option>
          <option>财务</option>
          <option>运维</option>
        </select>
        <span id="currentTenant">当前租户：示例广告主</span>
        <button id="resetPrototype" type="button">重置模拟数据</button>
      </header>
      <main id="mainContent">
        <section id="module-overview" class="module-page"></section>
        <section id="module-advertiser" class="module-page"></section>
        <section id="module-traffic" class="module-page"></section>
        <section id="module-platform" class="module-page"></section>
        <section id="module-core" class="module-page"></section>
        <section id="module-rules" class="module-page"></section>
        <section id="module-finance" class="module-page"></section>
        <section id="module-integration" class="module-page"></section>
        <section id="module-reports" class="module-page"></section>
      </main>
    </div>
    <aside id="stateRail" class="state-rail" aria-label="状态与日志"></aside>
  </div>
  <script>
    /* Implement the state contract and operations from the following steps. */
  </script>
</body>
</html>
```

Replace the comments with real CSS/JS in this task before committing. The comments above only mark the required shell placement and must not remain in the final file.

- [ ] **Step 2: Implement seeded state and persistence**

Inside the `<script>`, implement the following state contract:

```javascript
const STORAGE_KEY = "ad-platform-operational-prototype-state";

function seedState() {
  return {
    activeModule: "overview",
    role: "平台管理员",
    advertisers: [{ id: "adv-001", name: "示例广告主", balance: 128000, roas: 3.8 }],
    trafficSources: [{ id: "ts-001", name: "自营流量 App", placement: "信息流", status: "测试中", impressions: 860000, conversions: 1840 }],
    mediaAccounts: [
      { id: "ma-001", media: "巨量引擎", status: "已授权" },
      { id: "ma-002", media: "腾讯广告", status: "已授权" },
      { id: "ma-003", media: "Google Ads", status: "待同步" },
      { id: "ma-004", media: "Meta", status: "未授权" },
      { id: "ma-005", media: "自营媒体", status: "已授权" }
    ],
    campaigns: [{ id: "camp-001", name: "春促 ROI 计划", status: "投放中", budget: 30000, spent: 18420, bid: 18.6, strategy: "ROI 最优" }],
    budgets: [{ id: "budget-001", campaignId: "camp-001", daily: 10000, total: 30000, timeWindow: "09:00-22:00", frozen: 30000, spent: 18420 }],
    strategies: [{ id: "strategy-001", campaignId: "camp-001", type: "ROI 最优", targetCpa: 20, bidInterval: "10 分钟" }],
    rules: [{ id: "rule-001", name: "CPA 超标自动降价", status: "运行中", condition: "CPA > 目标 * 1.2", action: "自动调价 -5%" }],
    alerts: [{ id: "alert-001", type: "漏斗断崖", status: "未处理", level: "P1", action: "通知优化师" }],
    financeLedger: [{ id: "ledger-001", type: "充值", amount: 50000, status: "成功" }],
    trackingEvents: [{ id: "event-001", event: "purchase", source: "SDK", status: "已入库" }],
    reports: [{ id: "report-001", name: "投流日报", status: "已生成" }],
    operationsLog: ["系统加载 seeded mock state"]
  };
}

let state = loadState();

function loadState() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return seedState();
  try {
    return JSON.parse(raw);
  } catch (_error) {
    return seedState();
  }
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function resetState() {
  state = seedState();
  saveState();
  render();
}

function updateLog(message) {
  state.operationsLog.unshift(`${new Date().toLocaleTimeString()} ${message}`);
  state.operationsLog = state.operationsLog.slice(0, 12);
  saveState();
}

window.AdPrototype = {
  get state() {
    return state;
  },
  seedState,
  loadState,
  saveState,
  resetState
};
```

- [ ] **Step 3: Implement module navigation and role switching**

Implement these functions and wire them to the sidebar and top bar:

```javascript
function setActiveModule(moduleId) {
  state.activeModule = moduleId;
  updateLog(`切换模块：${moduleId}`);
  render();
}

function switchRole(role) {
  state.role = role;
  updateLog(`切换角色：${role}`);
  render();
}

document.querySelectorAll("[data-module]").forEach((button) => {
  button.addEventListener("click", () => setActiveModule(button.dataset.module));
});

document.getElementById("roleSwitcher").addEventListener("change", (event) => {
  switchRole(event.target.value);
});

document.getElementById("resetPrototype").addEventListener("click", resetState);

Object.assign(window.AdPrototype, { setActiveModule, switchRole, updateLog });
```

- [ ] **Step 4: Implement operational functions**

Implement the required operations with these exact function names:

```javascript
function submitBudget(event) {
  event.preventDefault();
  const daily = Number(document.getElementById("budgetDaily").value || 12000);
  const campaign = state.campaigns[0];
  campaign.budget = daily * 3;
  const budget = state.budgets[0];
  budget.daily = daily;
  budget.total = campaign.budget;
  budget.frozen = campaign.budget;
  updateLog(`预算已更新：日预算 ${daily}，总预算 ${campaign.budget}`);
  render();
}

function submitStrategy(event) {
  event.preventDefault();
  const type = document.getElementById("strategyType").value;
  state.campaigns[0].strategy = type;
  state.strategies[0].type = type;
  updateLog(`投流策略已切换为：${type}`);
  render();
}

function createTrafficPlacement(event) {
  event.preventDefault();
  const name = document.getElementById("placementName").value || "新广告位";
  state.trafficSources.push({ id: `ts-${Date.now()}`, name, placement: "激励视频", status: "测试中", impressions: 0, conversions: 0 });
  state.trackingEvents.unshift({ id: `event-${Date.now()}`, event: "placement_test", source: name, status: "测试中" });
  updateLog(`流量方广告位进入测试：${name}`);
  render();
}

function handleFunnelAlert() {
  state.alerts[0].status = "已处理";
  state.alerts[0].action = "已通知优化师并暂停低效计划";
  state.campaigns[0].status = "观察中";
  updateLog("漏斗异常已处理：暂停低效计划并通知优化师");
  render();
}

function copyCampaignAcrossMedia() {
  state.campaigns.push({ id: `camp-${Date.now()}`, name: "腾讯复制计划", status: "复制完成", budget: 8000, spent: 0, bid: 16, strategy: state.campaigns[0].strategy });
  updateLog("跨媒体复制完成：巨量计划复制到腾讯广告");
  render();
}

function runAutoBidSimulation() {
  state.campaigns[0].bid = Number((state.campaigns[0].bid * 0.92).toFixed(2));
  updateLog(`自动调价执行：当前出价 ${state.campaigns[0].bid}`);
  render();
}

function redistributeBudget() {
  state.budgets[0].daily += 1500;
  state.financeLedger.unshift({ id: `ledger-${Date.now()}`, type: "预算分配", amount: 1500, status: "已转移" });
  updateLog("预算分配执行：低效计划预算转向高 ROAS 计划");
  render();
}

function sendLtvCallback() {
  state.trackingEvents.unshift({ id: `event-${Date.now()}`, event: "ltv_callback", source: "归因服务", status: "已回传媒体" });
  updateLog("LTV 回传完成：媒体模型已收到价值信号");
  render();
}

function testRule() {
  state.rules[0].status = "已测试";
  updateLog("规则测试通过：CPA 超标样本命中自动降价动作");
  render();
}

function publishRule() {
  state.rules[0].status = "运行中";
  updateLog("规则已发布并运行：CPA 超标自动降价");
  render();
}

function rechargeMerchant(event) {
  event.preventDefault();
  const amount = Number(document.getElementById("rechargeAmount").value || 10000);
  state.advertisers[0].balance += amount;
  state.financeLedger.unshift({ id: `ledger-${Date.now()}`, type: "商户充值", amount, status: "成功" });
  updateLog(`商户充值成功：${amount}`);
  render();
}

function submitRefund(event) {
  event.preventDefault();
  state.financeLedger.unshift({ id: `ledger-${Date.now()}`, type: "退款", amount: 3000, status: "待审核" });
  updateLog("退款申请已提交：待审核");
  render();
}

function submitInvoice(event) {
  event.preventDefault();
  state.financeLedger.unshift({ id: `ledger-${Date.now()}`, type: "开票", amount: 6000, status: "待开票" });
  updateLog("开票申请已提交：待开票");
  render();
}

function generateCredentials() {
  state.trackingEvents.unshift({ id: `event-${Date.now()}`, event: "credential_generated", source: "接入门户", status: "AppKey/AppSecret 已生成" });
  updateLog("接入凭证已生成：AppKey / AppSecret");
  render();
}

function sendTestEvent() {
  state.trackingEvents.unshift({ id: `event-${Date.now()}`, event: "purchase", source: "SDK/API", status: "已入库" });
  updateLog("测试事件已发送：purchase");
  render();
}

function saveReportTemplate() {
  state.reports.unshift({ id: `report-${Date.now()}`, name: "自定义媒体效益报表", status: "模板已保存" });
  updateLog("自定义报表模板已保存");
  render();
}

function confirmMonitoringAlert() {
  const openAlert = state.alerts.find((alert) => alert.status !== "已处理") || state.alerts[0];
  openAlert.status = "已确认";
  updateLog(`监控告警已确认：${openAlert.type}`);
  render();
}

function generateReviewReport() {
  state.reports.unshift({ id: `report-${Date.now()}`, name: "投流周报", status: "已生成" });
  updateLog("投流复盘报告已生成：投流周报");
  render();
}

Object.assign(window.AdPrototype, {
  submitBudget,
  submitStrategy,
  createTrafficPlacement,
  handleFunnelAlert,
  copyCampaignAcrossMedia,
  runAutoBidSimulation,
  redistributeBudget,
  sendLtvCallback,
  testRule,
  publishRule,
  rechargeMerchant,
  submitRefund,
  submitInvoice,
  generateCredentials,
  sendTestEvent,
  saveReportTemplate,
  confirmMonitoringAlert,
  generateReviewReport
});
```

- [ ] **Step 5: Render all module pages**

Implement `render()` so each required `section` contains real controls and readable content:

```javascript
function render() {
  document.getElementById("roleSwitcher").value = state.role;
  document.querySelectorAll("[data-module]").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.module === state.activeModule);
  });
  document.querySelectorAll(".module-page").forEach((section) => {
    section.hidden = section.id !== `module-${state.activeModule}`;
  });

  renderOverview();
  renderAdvertiser();
  renderTraffic();
  renderPlatform();
  renderCore();
  renderRules();
  renderFinance();
  renderIntegration();
  renderReports();
  renderStateRail();
  saveState();
}
```

Each `render*` function must produce actual HTML with the IDs required by the test:

- `budgetForm`, `budgetDaily`, `strategyForm`, `strategyType`, `generateReviewReport`
- `trafficPlacementForm`, `placementName`
- `handleFunnelAlert`
- `copyCampaignAcrossMedia`, `runAutoBidSimulation`, `redistributeBudget`, `sendLtvCallback`
- `testRule`, `publishRule`
- `rechargeForm`, `rechargeAmount`, `refundForm`, `invoiceForm`
- `generateCredentials`, `sendTestEvent`
- `saveReportTemplate`, `confirmMonitoringAlert`

Also wire the form submit and button click handlers after rendering:

```javascript
function bindRenderedActions() {
  const bindSubmit = (id, handler) => {
    const element = document.getElementById(id);
    if (element) element.addEventListener("submit", handler);
  };
  const bindClick = (id, handler) => {
    const element = document.getElementById(id);
    if (element) element.addEventListener("click", handler);
  };

  bindSubmit("budgetForm", submitBudget);
  bindSubmit("strategyForm", submitStrategy);
  bindSubmit("trafficPlacementForm", createTrafficPlacement);
  bindSubmit("rechargeForm", rechargeMerchant);
  bindSubmit("refundForm", submitRefund);
  bindSubmit("invoiceForm", submitInvoice);
  bindClick("handleFunnelAlert", handleFunnelAlert);
  bindClick("copyCampaignAcrossMedia", copyCampaignAcrossMedia);
  bindClick("runAutoBidSimulation", runAutoBidSimulation);
  bindClick("redistributeBudget", redistributeBudget);
  bindClick("sendLtvCallback", sendLtvCallback);
  bindClick("testRule", testRule);
  bindClick("publishRule", publishRule);
  bindClick("generateCredentials", generateCredentials);
  bindClick("sendTestEvent", sendTestEvent);
  bindClick("saveReportTemplate", saveReportTemplate);
  bindClick("confirmMonitoringAlert", confirmMonitoringAlert);
  bindClick("generateReviewReport", generateReviewReport);
}
```

Call `bindRenderedActions()` at the end of `render()`.

- [ ] **Step 6: Add architecture and sequence surfaces**

Add a diagrams area in the Overview module and detail diagram cards in module pages. Each required surface must have a `data-diagram` or `data-sequence` attribute exactly matching the test.

Use readable HTML/SVG-like blocks, for example:

```html
<article class="diagram-card" data-diagram="overall-architecture">
  <h3>整体架构</h3>
  <div class="diagram-flow">
    <span>用户层</span><span>接入层</span><span>业务中台</span><span>数据智能</span><span>基础设施</span><span>外部媒体</span>
  </div>
</article>

<article class="diagram-card" data-sequence="budget-sequence">
  <h3>预算设置与扣减时序</h3>
  <ol>
    <li>优化师提交预算配置</li>
    <li>预算服务冻结计划预算</li>
    <li>媒体回传消耗</li>
    <li>预算扣减并检查阈值</li>
    <li>异常时写入告警中心</li>
  </ol>
</article>
```

Include all required `data-diagram` and `data-sequence` values from the test.

- [ ] **Step 7: Run the contract test**

Run:

```bash
python3 -m unittest tests.test_ad_platform_operational_prototype -v
```

Expected: fail only because the gate review artifact does not exist yet. All HTML checks should pass.

- [ ] **Step 8: Commit the prototype**

Run:

```bash
git add wiki/reports/ad-platform-operational-prototype.html
git commit -m "feat: add ad platform operational prototype"
```

---

### Task 4: Report Gate Review

**Files:**
- Create: `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`

- [ ] **Step 1: Create the gate review artifact**

Create `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`:

```markdown
---
layer: ops
domain: none
ops_area: report-quality
canonical_object: ad-platform-operational-prototype
artifact_type: report-gate-review
kind: report-gate-review
created: 2026-05-13
target: wiki/reports/ad-platform-operational-prototype.html
status: prototype-review
---

# ad-platform-operational-prototype / report-gate-review

## Review Target

Target: `wiki/reports/ad-platform-operational-prototype.html`

Destination: repo-local operational prototype.

Scope: build an operable advertising delivery system prototype with module
workbench navigation, local mock state, architecture surfaces, PRD flow
surfaces, and meaningful backstage operations.

Non-scope: No Feishu sync, no production rollout, no real backend, no real
media API, no real payment, no real invoice, and no real SDK network call.

## Reviewer Routing

Reviewer routing: required for reader-facing / report-adjacent prototype output.

Signals:

| Signal | Result |
|---|---|
| Prior output drifted toward customer demo | true |
| Corrected intent requires operable system prototype | true |
| Multi-module system design | true |
| Public publication requested | false |

## Article Intent Contract

| Field | Contract |
|---|---|
| Reader | Product / engineering reviewer of the advertising delivery system prototype. |
| Reader decision or action | Verify whether the prototype covers system modules, PRD operations, architecture surfaces, and local-state workflows. |
| Main line | This is an operable advertising delivery system prototype, not a customer demo. |
| Non-goals | No customer demo, no marketing H5, no Feishu sync, no real external integration, no production readiness claim. |
| User-owned judgments | Module-workbench approach, local mock data operability, unified platform backstage, and superseding the Growth Cockpit direction for this corrected requirement. |
| Agent-allowed work | Build repo-local prototype, mock data operations, tests, diagrams, and verification evidence. |

## Reference Structure Map

| Field | Result |
|---|---|
| Source | `inbox/ad-desgin.md` and corrected user requirement. |
| Reader job | Inspect and operate a system prototype that maps to the requested advertising platform design. |
| Page group | One standalone backstage prototype. |
| Reading path | Overview -> module navigation -> operation forms -> state rail -> architecture/sequence panels. |
| Visual logic | Dense enterprise backstage, not hero/marketing layout. |
| Writing standard | Product/engineering system language with operational labels. |
| Reuse boundary | Prior Growth Cockpit H5 is treated as exploratory and superseded for this corrected requirement. |

Reference Structure Gate: PASS for prototype.

## Section And Paragraph Drift Review

| Section | Objective | Drift Risk | Action |
|---|---|---:|---|
| Shell | Make it feel like a backstage system. | 0 | Retain. |
| Modules | Cover requested 8 areas plus overview entry. | 0 | Retain. |
| Operations | Prove local-state operability. | 0 | Retain. |
| Diagrams | Preserve architecture and sequence requirements. | 1 | Retain; diagrams are local panels, not production architecture approval. |
| Gate boundary | Prevent Feishu/production overclaim. | 0 | Retain. |

## Judgment Ledger

| Judgment | Source Class | Status | Required Action |
|---|---|---|---|
| Not a customer demo | User correction | confirmed | Enforce in test and copy. |
| Module-workbench approach | User choice | confirmed | Implement. |
| Local mock data operability | User choice | confirmed | Implement with localStorage and reset. |
| Real integrations excluded | Prototype boundary | confirmed | Keep non-goal visible. |

## Hard Gate Results

| Gate | Result | Note |
|---|---|---|
| Reader intent | PASS | Operational system prototype intent is explicit. |
| Reference/output shape | PASS | Module workbench shape matches corrected requirement. |
| Narrative drift | PASS | Customer demo language is rejected. |
| Judgment ownership | PASS | User choices are recorded. |
| Visual output | PENDING | Browser verification still required. |
| Publish gate | NOT APPLICABLE | No Feishu sync or publication requested. |

## Scorecard

Prototype score: INVALID until final local verification is recorded.

Publication score: INVALID because no Feishu sync or external publication was
requested or verified.

## Decision

Keep the artifact local until tests and browser verification pass. Do not claim
production readiness or external publication.

## Residual Risks

- Local state does not prove backend correctness.
- Static diagrams do not prove final architecture approval.
- Mock payment/invoice/media behavior must not be treated as real integration.

## Local Verification

Pending final execution:

- `python3 -m unittest tests.test_ad_platform_operational_prototype tests.test_public_report_quality_gate -v`
- `python3 scripts/check_behavior_assets.py`
- `python3 scripts/check_wiki_frontmatter.py`
- `git diff --check`
- Browser interaction verification for module navigation, budget, rule, recharge,
  alert handling, report generation, and diagram reachability.

## Feishu Update Verification

No Feishu sync. No update command run.
```

- [ ] **Step 2: Run the contract test**

Run:

```bash
python3 -m unittest tests.test_ad_platform_operational_prototype -v
```

Expected: all tests pass.

- [ ] **Step 3: Run wiki frontmatter checker**

Run:

```bash
python3 scripts/check_wiki_frontmatter.py
```

Expected: the command may fail on existing legacy taxonomy drift. Confirm that `wiki/ops/ad-platform-operational-prototype-report-gate-review.md` is not listed in `/tmp/wiki-frontmatter-taxonomy-report.md`.

- [ ] **Step 4: Commit the gate review**

Run:

```bash
git add wiki/ops/ad-platform-operational-prototype-report-gate-review.md
git commit -m "docs: gate review ad platform operational prototype"
```

---

### Task 5: Browser Verification And Completion Evidence

**Files:**
- Modify: `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`
- Modify: `openspec/changes/build-ad-platform-operational-prototype/tasks.md`

- [ ] **Step 1: Run full static verification**

Run:

```bash
python3 -m unittest tests.test_ad_platform_operational_prototype tests.test_public_report_quality_gate -v
python3 scripts/check_behavior_assets.py
git diff --check
openspec validate build-ad-platform-operational-prototype --strict
```

Expected:

- Unit tests pass.
- Behavior asset checker passes.
- Diff check has no output.
- OpenSpec validates. PostHog network flush errors after validation are non-blocking.

- [ ] **Step 2: Run browser interaction verification**

Use Playwright or an equivalent browser tool. If the Python Playwright launch is blocked by sandbox permissions, rerun with approval using the same pattern used for the previous H5 verification.

Use this script as the verification contract:

```bash
python3 - <<'PY'
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

url = Path("wiki/reports/ad-platform-operational-prototype.html").resolve().as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--disable-setuid-sandbox"])
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page.goto(url)

    expect(page.locator("text=广告投流系统")).to_be_visible()
    page.locator('[data-module="advertiser"]').click()
    expect(page.locator("#module-advertiser")).to_be_visible()
    page.fill("#budgetDaily", "15000")
    page.locator("#budgetForm button[type='submit']").click()
    expect(page.locator("#stateRail")).to_contain_text("预算已更新")

    page.select_option("#strategyType", label="成本控制")
    page.locator("#strategyForm button[type='submit']").click()
    expect(page.locator("#stateRail")).to_contain_text("投流策略已切换")

    page.locator('[data-module="rules"]').click()
    page.locator("#testRule").click()
    expect(page.locator("#stateRail")).to_contain_text("规则测试通过")
    page.locator("#publishRule").click()
    expect(page.locator("#stateRail")).to_contain_text("规则已发布")

    page.locator('[data-module="finance"]').click()
    page.fill("#rechargeAmount", "20000")
    page.locator("#rechargeForm button[type='submit']").click()
    expect(page.locator("#stateRail")).to_contain_text("商户充值成功")

    page.locator('[data-module="platform"]').click()
    page.locator("#handleFunnelAlert").click()
    expect(page.locator("#stateRail")).to_contain_text("漏斗异常已处理")

    page.locator('[data-module="reports"]').click()
    page.locator("#saveReportTemplate").click()
    expect(page.locator("#stateRail")).to_contain_text("自定义报表模板已保存")

    page.locator('[data-module="overview"]').click()
    expect(page.locator('[data-diagram="overall-architecture"]')).to_be_visible()
    expect(page.locator('[data-sequence="budget-sequence"]')).to_be_visible()

    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(url)
    expect(page.locator("text=广告投流系统")).to_be_visible()

    browser.close()

print("browser operational prototype checks pass")
PY
```

Expected: script prints `browser operational prototype checks pass`.

- [ ] **Step 3: Capture screenshots**

Run Playwright screenshot commands:

```bash
playwright screenshot -b chromium --viewport-size 1440,1200 --full-page --wait-for-selector '#module-overview' 'file:///mnt/d/cloud/account-meeting-lore/wiki/reports/ad-platform-operational-prototype.html' /tmp/ad-platform-operational-prototype-desktop.png
playwright screenshot -b chromium --viewport-size 390,844 --full-page --wait-for-selector '#module-overview' 'file:///mnt/d/cloud/account-meeting-lore/wiki/reports/ad-platform-operational-prototype.html' /tmp/ad-platform-operational-prototype-mobile.png
```

Expected: screenshots are generated. If the local Playwright environment renders Chinese as missing glyphs, rerun with a local fontconfig override and record that in the gate review.

- [ ] **Step 4: Update gate review and tasks**

Update `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`:

- Change `status: prototype-review` to `status: prototype-verified`.
- Change Visual output gate to PASS.
- Change prototype score to `Prototype score: 88 / 100.`.
- Add verification evidence:
  - Unit tests passed.
  - Behavior asset checker passed.
  - Frontmatter checker result and unrelated legacy drift boundary.
  - Browser interaction verification passed.
  - Screenshot paths.

Update `openspec/changes/build-ad-platform-operational-prototype/tasks.md` by checking all boxes.

- [ ] **Step 5: Commit verification evidence**

Run:

```bash
git add wiki/ops/ad-platform-operational-prototype-report-gate-review.md \
  openspec/changes/build-ad-platform-operational-prototype/tasks.md
git commit -m "docs: record ad platform operational prototype verification"
```

After this commit, stop implementation. The change is complete and the default next action is archive review, not further feature expansion.

---

## Self-Review Notes

Spec coverage:

- Full module workbench: Task 3 shell and render steps.
- Local mock state and `localStorage`: Task 3 state contract.
- Operations across budget, strategy, traffic, platform, core, rules, finance, integration, and reports: Task 3 operation functions and Task 5 browser script.
- Architecture and sequence surfaces: Task 3 diagram step and contract test.
- Gate review and corrected intent: Task 4.
- OpenSpec boundary: Task 1.

Placeholder scan:

- No unresolved markers remain.
- No unresolved implementation questions remain.
- The HTML implementation step contains exact required IDs, function names, state keys, and operation behavior.

Type/name consistency:

- Test IDs and function names match the Task 3 implementation contract.
- Gate review path matches the test.
- OpenSpec change id matches all commands.
