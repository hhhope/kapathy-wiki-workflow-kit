# Account Group Onboarding H5 Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the account-group onboarding H5 so every section carries real account-domain structure, including capability map, system architecture, core chain, project entry, and AI-assisted engineering practice.

**Architecture:** Treat the existing H5 as a delivery shell, not as authoritative content. Create a new OpenSpec change for the rewrite, update the gate review with the failed-draft diagnosis and revised evidence map, then rewrite the H5 in bounded passes: account-domain screens first, AI/newcomer screens second, verification last.

**Tech Stack:** Static HTML/CSS under `wiki/reports/`, markdown gate review under `wiki/ops/`, OpenSpec change artifacts under `openspec/changes/`, verification with `python3 -m html.parser`, `rg`, `git diff --check`, and Playwright screenshots.

---

## File Structure

- Modify: `wiki/reports/account-group-onboarding-h5.html`
  - Responsibility: reader-facing local H5 draft.
  - Rewrite approach: keep standalone HTML/CSS, but replace thin content with domain-dense visual sections.
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
  - Responsibility: public-output gate record, drift diagnosis, revised source-to-screen mapping, sensitive boundary, and final verification evidence.
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/proposal.md`
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/design.md`
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/specs/account-group-onboarding-h5/spec.md`
  - Responsibility: authoritative lifecycle for the rewrite. The prior `build-account-group-onboarding-h5` change is complete and must not be reopened for implementation.
- Modify only if final index text becomes inaccurate: `wiki/reports/index.md`
  - Current link can remain unless title or description changes.

## Required Content Standard

The rewrite must preserve the approved chapter order but replace generic prose with these minimum content anchors:

- The first domain section must not use generic onboarding wording as the main reader promise. It should say, in substance: `账户组管的是资金结果`, `我们手里有哪些能力`, and `新人能练到哪些硬能力`.
- Account capability map:
  - account basic capability;
  - account lifecycle;
  - account type management;
  - personal wallet account;
  - parent-child account relation;
  - multi-account model;
  - mother-real-child-virtual account direction;
  - unified accounting capability;
  - accounting query;
  - daily cut;
  - reverse / adjustment;
  - entry-rule engine;
  - standard posting model;
  - clearing/settlement capability;
  - settlement / withdrawal / clearing result handling;
  - reconciliation platform / basic reconciliation / difference handling;
  - unified balance capability;
  - available balance;
  - real-time balance;
  - frozen balance;
  - data/report/service capability;
  - balance query;
  - report capability;
  - data external service;
  - revenue capability where source-backed.
- Exclusions:
  - do not make `授信能力` a capability group;
  - do not make `垫资能力` a capability group.
- System architecture:
  - entrance/gateway: API, H5, BM, upstream product entrance;
  - product layer: payment split-account product, account product;
  - service layer: base service, member system, transaction system, clearing system, risk system, refund center, agent system, channel system, account posting;
  - data layer: merchant, user, payment, channel, finance, risk data;
  - external connections: bank union / network union / self-owned payment channels / partner banks;
  - operation/back-office sides: operation management platform, AD, BM.
- Core chain:
  - entry / onboarding / account opening;
  - account model and bank-account relation;
  - transaction / collection / payment;
  - split account / withdrawal / refund;
  - accounting / voucher / balance;
  - clearing and settlement;
  - reconciliation / reports / difference handling;
  - risk, monitoring, observability.
- AI system:
  - OpenSpec / Lore / Graphify / lore-bootstrap must be explained as account-domain engineering aids: duplicate capability checks, historical design lookup, structure lookup, design/review/verification evidence, and knowledge reuse.

## Task 1: Create Rewrite OpenSpec Change

**Files:**
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/proposal.md`
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/design.md`
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`
- Create: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/specs/account-group-onboarding-h5/spec.md`

- [ ] **Step 1: Write `proposal.md`**

```markdown
# Proposal: Rewrite Account Group Onboarding H5 Domain Depth

## Why

The first account-group onboarding H5 draft has acceptable chapter order but fails the reader job. It compresses account-group domain content into generic cards, omits system architecture, and does not explain key engineering domains such as account model, bank-account relation, accounting, balance, clearing/settlement, reconciliation, reports, parent-child accounts, and multi-account model with enough structure for fresh graduates.

## What Changes

- Rewrite the existing local H5 content while keeping the H5-first delivery form.
- Replace the three-card capability map with a real account-domain capability graph.
- Add a layered system architecture section based on the source architecture slides.
- Rewrite the core chain to include account model, bank-account relation, transaction, accounting, balance, clearing/settlement, reconciliation, reports, difference handling, and observability.
- Rewrite project and newcomer task sections so they map to real account-domain modules.
- Reconnect AI collaboration content to account-domain design, review, verification, and knowledge reuse.
- Update the public-output gate review with drift diagnosis, revised evidence map, verification evidence, and sensitive-info boundary.

## Out of Scope

- Feishu publishing or sync.
- Exposing credentials, personal contacts, internal test URLs, group QR codes, or access instructions.
- Treating `授信能力` or `垫资能力` as account-group capability groups.
- Reopening the completed `build-account-group-onboarding-h5` change.

## Impact

- The existing H5 file will be rewritten in place.
- The report index link remains valid unless the title changes.
- The gate review becomes the evidence surface for why the first draft failed and how the rewrite fixes it.
```

- [ ] **Step 2: Write `design.md`**

```markdown
# Design: Account Group Onboarding H5 Domain Rewrite

## Approach

The rewrite keeps the approved chapter order but changes the depth standard. The H5 must stop reading like a motivational newcomer guide and start reading like an account-domain engineering map.

## Content Model

The page has fifteen screens:

1. Cover.
2. Group responsibility.
3. Account capability map.
4. System architecture.
5. Core business chain.
6. Business objects.
7. Typical problems.
8. Active project entries.
9. Technical planning.
10. AI collaboration system.
11. AI Coding maturity.
12. Three-day and first-week path.
13. 30/60/90 growth path.
14. Task pool and gained capabilities.
15. Closing.

## Visual Model

- Capability map: dense node graph with grouped capability clusters.
- System architecture: layered stack from entrance to data and external connections.
- Core chain: horizontal or wrapped flow with domain checkpoints.
- Project entries: cards with domain position, what changes, newcomer task, and trained capability.
- AI sections: engineering workflow cards tied to account-domain work.

## Sensitive Boundary

The H5 may name business products and capability names, but must not include personal contacts, credentials, internal test URLs, group QR codes, Feishu source URLs, token strings, or account-opening access instructions.

## Verification

Verification must include HTML parser, revised source-to-screen coverage, required content grep, excluded capability grep, sensitive-info grep, desktop screenshot, mobile screenshot, and `git diff --check`.
```

- [ ] **Step 3: Write `tasks.md`**

```markdown
# Tasks

- [ ] 1. Create rewrite gate baseline
  - Record the failed-draft diagnosis, revised article intent, revised content standard, and source-to-section map in the gate review.
  - Commit only the gate review and this tasks file if needed.

- [ ] 2. Rewrite account-domain H5 sections
  - Rewrite cover, group responsibility, capability map, system architecture, core chain, business objects, typical problems, active projects, and technical planning.
  - Verify required account-domain content and excluded capability groups.
  - Commit only the H5, gate review, and this tasks file if needed.

- [ ] 3. Rewrite AI and newcomer sections
  - Rewrite AI collaboration, AI maturity, 3-day / first-week path, 30/60/90 path, task pool, and closing.
  - Tie AI content to account-domain engineering work.
  - Commit only the H5, gate review, and this tasks file if needed.

- [ ] 4. Verify visual quality and sensitive boundary
  - Run HTML parser.
  - Run required content grep.
  - Run excluded capability grep.
  - Run sensitive-info grep.
  - Take and inspect desktop and mobile screenshots.
  - Run `git diff --check`.
  - Commit only the gate review and this tasks file if needed.

- [ ] 5. Final local review status
  - Update gate review decision.
  - Verify report index still links to the H5.
  - Run `openspec validate rewrite-account-group-onboarding-h5-domain-depth --strict`.
  - Commit only final review/status files if needed.
```

- [ ] **Step 4: Write spec delta**

```markdown
# account-group-onboarding-h5 Spec Delta

## ADDED Requirements

### Requirement: Domain-Dense Capability Map

The H5 SHALL include a capability map with more than three capability groups and SHALL cover account basic capability, parent-child or multi-account model, unified accounting capability, clearing/settlement capability, reconciliation/reporting/data-service capability, unified balance capability, and source-backed revenue capability.

#### Scenario: capability map is reviewable
- **WHEN** a reviewer reads the capability map section
- **THEN** they can identify account lifecycle, account type management, parent-child account relation, multi-account model, accounting query, daily cut, reverse or adjustment, clearing/settlement, reconciliation or difference handling, available balance, real-time balance, frozen balance, report capability, and data/service capability.

### Requirement: Excluded Capability Groups

The H5 SHALL NOT present `授信能力` or `垫资能力` as account-group capability groups.

#### Scenario: rejected capability groups are absent
- **WHEN** a reviewer greps the H5 for `授信能力|垫资能力`
- **THEN** there are no reader-facing capability-group matches.

### Requirement: Layered System Architecture

The H5 SHALL include a layered architecture section covering entrance/gateway, product layer, service layer, data layer, payment channel or partner bank connections, and operation/back-office sides.

#### Scenario: architecture section is present
- **WHEN** a reviewer reads the system architecture section
- **THEN** it names API/H5/BM or upstream entrance, product layer, service layer, data layer, payment channels or partner banks, and operation/back-office sides.

### Requirement: Complete Core Chain

The H5 SHALL describe the core chain from entry/account opening through account model and bank-account relation, transaction or payment, split account or withdrawal or refund, accounting/voucher/balance, clearing/settlement, reconciliation/report/difference handling, and risk/monitoring/observability.

#### Scenario: core chain includes account-domain checkpoints
- **WHEN** a reviewer reads the core chain section
- **THEN** they can follow how identity/account relation, fund movement, internal accounting/balance, external clearing/settlement, and reconciliation/reporting connect.

### Requirement: Account-Domain AI Collaboration

The H5 SHALL explain OpenSpec, Lore, Graphify, and lore-bootstrap as account-domain engineering aids rather than generic AI tools.

#### Scenario: AI section is tied to account work
- **WHEN** a reviewer reads the AI collaboration section
- **THEN** it explains at least historical design lookup, duplicate capability checks, structure lookup, design/review/verification evidence, or reusable knowledge capture for account-domain work.
```

- [ ] **Step 5: Validate and commit**

Run:

```bash
openspec validate rewrite-account-group-onboarding-h5-domain-depth --strict
```

Expected:

```text
Change 'rewrite-account-group-onboarding-h5-domain-depth' is valid
```

Nonblocking note: PostHog telemetry network warnings may appear after validation.

Commit:

```bash
git add openspec/changes/rewrite-account-group-onboarding-h5-domain-depth
git commit -m "docs: propose account onboarding h5 rewrite"
```

## Task 2: Create Rewrite Gate Baseline

**Files:**
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
- Modify: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`

- [ ] **Step 1: Add failed-draft diagnosis**

Add this section before `## Verification Log`:

```markdown
## Rewrite Diagnosis

- User feedback: the chapter order is acceptable, but the content is too thin.
- Failure mode: the first draft collapsed the account capability map into generic cards and omitted the real system architecture.
- Missing domain depth: account model, bank-account / channel connection, accounting, balance, clearing/settlement, reconciliation, reports, parent-child account, multi-account model, and difference handling were not explained as an engineering structure.
- Corrected boundary: `授信能力` and `垫资能力` must not be presented as account-group capability groups; reconciliation and parent-child account capability must be present.
- Rewrite standard: each section must explain real domain objects, module boundaries, chain dependencies, and newcomer task entry.
```

- [ ] **Step 2: Add revised source-to-section map**

Add this table after the diagnosis:

```markdown
## Revised Source-To-Section Map

| H5 Section | Required Source Anchor | Rewrite Use |
| --- | --- | --- |
| Capability map | `账户体系能力地图` slide | Rebuild as multi-cluster capability graph; include account basic, unified accounting, clearing/settlement, unified balance, data/report/service, revenue, reconciliation, parent-child and multi-account model; exclude 授信/垫资 groups. |
| System architecture | 宝财通 architecture slide, 多渠道收款 architecture slide | Rebuild layered architecture: entrance/gateway, product, service, data, payment channels, partner banks, operation/back-office. |
| Core chain | 账户技术现状 + 规划 slides | Explain entry/opening, account model, bank-account relation, transaction, split/withdraw/refund, accounting/voucher/balance, clearing/settlement, reconciliation/report/difference, monitoring/risk. |
| Business objects | 多渠道收款、宝户通、宝财通、银企通/债转 slides | Show product objects by architecture position, not as isolated product names. |
| Problems | Typical problem slide | Map withdrawal failure, opening failure, deposit failure, slow posting, reconciliation difference, settlement difference, account/balance inconsistency to chain checkpoints. |
| Projects | Split-account source and 2026 planning slides | Map project entries to account model, parent-child account, balance-ledger verification, settlement/clearing, reconciliation/reporting, bank-account/channel access. |
| AI collaboration | Account Harness and AICoding roadmap | Explain how AI supports account-domain design, review, verification, structure lookup, and knowledge reuse. |
| Newcomer path | Account and IT onboarding docs | Keep Day 1/2/3 and first-week rhythm while removing credentials, URLs, personal contacts, and QR-code instructions. |
```

- [ ] **Step 3: Mark Task 1 complete and commit**

Update the rewrite OpenSpec tasks:

```markdown
- [x] 1. Create rewrite gate baseline
```

Commit:

```bash
git add wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md
git commit -m "docs: record account onboarding h5 rewrite baseline"
```

## Task 3: Rewrite Account-Domain H5 Sections

**Files:**
- Modify: `wiki/reports/account-group-onboarding-h5.html`
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
- Modify: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`

- [ ] **Step 1: Replace account-domain section content**

Rewrite H5 sections from cover through technical planning. The H5 must include these visible section headings:

```text
账户组体系：从资金账户链路到 AI 协作成长
账户组管的是资金结果
账户体系能力地图
系统架构怎么看
核心业务链路
典型业务对象
常见问题怎么入手
正在做的项目入口
技术规划看什么
```

- [ ] **Step 2: Add capability map content**

The `账户体系能力地图` section must include these exact or near-exact visible phrases:

```text
账户基础能力
账户生命周期
账户类型管理
母子账户关系
多账户模型
母实子虚账户
统一账务能力
账务查询
日切处理
冲正调账能力
分录规则引擎
标准记账模型
清结算能力
统一对账平台
基础对账
轧差能力
统一余额能力
可用余额
实时余额
冻结余额
数据与服务
报表能力
数据对外服务
收益能力
```

- [ ] **Step 3: Add system architecture content**

The `系统架构怎么看` section must include these exact or near-exact visible phrases:

```text
网关层
产品层
服务层
数据层
支付渠道
合作银行
API
H5
BM
支付分账户产品
账户产品
会员系统
交易系统
清算系统
风控系统
退款中心
代理商系统
渠道系统
商户数据
用户数据
支付数据
渠道数据
财务数据
风控数据
银联
网联
自有支付渠道
银企通
运营管理平台
```

- [ ] **Step 4: Add core chain content**

The `核心业务链路` section must include these exact or near-exact visible phrases:

```text
进件 / 开户
账户模型
银行账户关系
交易 / 收款 / 付款
分账 / 提现 / 退款
账务 / 凭证 / 余额
清算 / 结算
对账 / 报表 / 差错处理
风险 / 监控 / 可观测
```

- [ ] **Step 5: Verify account-domain content**

Run:

```bash
rg -n "账户基础能力|账户生命周期|账户类型管理|母子账户关系|多账户模型|母实子虚账户|统一账务能力|账务查询|日切处理|冲正调账能力|分录规则引擎|标准记账模型|清结算能力|统一对账平台|基础对账|轧差能力|统一余额能力|可用余额|实时余额|冻结余额|数据与服务|报表能力|数据对外服务|收益能力|网关层|产品层|服务层|数据层|支付渠道|合作银行|会员系统|交易系统|清算系统|风控系统|退款中心|代理商系统|渠道系统|银行账户关系|清算 / 结算|差错处理" wiki/reports/account-group-onboarding-h5.html
```

Expected: multiple matches across account-domain sections.

Run:

```bash
rg -n "授信能力|垫资能力" wiki/reports/account-group-onboarding-h5.html
```

Expected: exit code 1 with no output.

- [ ] **Step 6: Record verification and commit**

Add verification lines:

```markdown
- Rewrite account-domain content check: passed after capability map, system architecture, core chain, business objects, problem handling, active project entries, and technical planning were rewritten with domain-dense content.
- Excluded capability check: passed after `授信能力` and `垫资能力` were absent from the reader-facing H5.
```

Mark Task 2 complete:

```markdown
- [x] 2. Rewrite account-domain H5 sections
```

Commit:

```bash
git add wiki/reports/account-group-onboarding-h5.html wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md
git commit -m "feat: rewrite account onboarding domain h5"
```

## Task 4: Rewrite AI And Newcomer Sections

**Files:**
- Modify: `wiki/reports/account-group-onboarding-h5.html`
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
- Modify: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`

- [ ] **Step 1: Rewrite AI collaboration as account-domain practice**

The AI collaboration sections must include these visible phrases:

```text
OpenSpec 管变更
Lore 管记忆
Graphify 管结构
lore-bootstrap 管安装
查历史详设
识别重复能力
定位模块边界
留下验证证据
沉淀可复用知识
```

- [ ] **Step 2: Rewrite maturity and newcomer path**

The newcomer sections must include these visible phrases:

```text
当前更接近 L2
L2 -> L3
需求 -> 设计 -> 研发 -> CR -> 验收 -> 沉淀
Day 1
Day 2
Day 3
第一周：跑通一条核心账户链路
30 天：听懂对象和链路
60 天：进入一个模块
90 天：独立排障并交付小任务
```

- [ ] **Step 3: Verify AI/newcomer content**

Run:

```bash
rg -n "OpenSpec 管变更|Lore 管记忆|Graphify 管结构|lore-bootstrap 管安装|查历史详设|识别重复能力|定位模块边界|留下验证证据|沉淀可复用知识|当前更接近 L2|L2 -> L3|需求 -> 设计 -> 研发 -> CR -> 验收 -> 沉淀|Day 1|Day 2|Day 3|第一周：跑通一条核心账户链路|30 天：听懂对象和链路|60 天：进入一个模块|90 天：独立排障并交付小任务" wiki/reports/account-group-onboarding-h5.html
```

Expected: all phrases are represented by visible text.

- [ ] **Step 4: Record verification and commit**

Add verification line:

```markdown
- Rewrite AI/newcomer content check: passed after AI collaboration was tied to account-domain design, module lookup, verification evidence, and knowledge reuse, and after Day 1/2/3, first-week, and 30/60/90 paths were rewritten.
```

Mark Task 3 complete:

```markdown
- [x] 3. Rewrite AI and newcomer sections
```

Commit:

```bash
git add wiki/reports/account-group-onboarding-h5.html wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md
git commit -m "feat: rewrite account onboarding ai path"
```

## Task 5: Verify Visual Quality And Sensitive Boundary

**Files:**
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
- Modify: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`

- [ ] **Step 1: Run HTML parser**

Run:

```bash
python3 -m html.parser wiki/reports/account-group-onboarding-h5.html
```

Expected: exit code 0 with no output.

- [ ] **Step 2: Run required content grep**

Run:

```bash
rg -n "账户基础能力|系统架构怎么看|核心业务链路|银行账户关系|清算 / 结算|对账 / 报表 / 差错处理|母子账户关系|母实子虚账户|统一账务能力|统一余额能力|OpenSpec 管变更|查历史详设|第一周：跑通一条核心账户链路" wiki/reports/account-group-onboarding-h5.html
```

Expected: matches in the H5.

- [ ] **Step 3: Run excluded capability grep**

Run:

```bash
rg -n "授信能力|垫资能力" wiki/reports/account-group-onboarding-h5.html
```

Expected: exit code 1 with no output.

- [ ] **Step 4: Run sensitive-info grep**

Run:

```bash
rg -n "密码|账号已开通|Ethan|@baofu|10\\.254|http://10\\.|https://test-|云枢|VPN|扫码|二维码|GitLab|Jira|王竹|彬彬|杨锋将|token=|feishu.cn/wiki|feishu.cn/docx|docs.baofu.com|apifox.com/project" wiki/reports/account-group-onboarding-h5.html
```

Expected: exit code 1 with no output.

- [ ] **Step 5: Take screenshots**

Run:

```bash
playwright screenshot --full-page --viewport-size=1440,1800 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/account-group-onboarding-h5.html /tmp/account-group-onboarding-rewrite-desktop-full.png
playwright screenshot --full-page --viewport-size=390,1200 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/account-group-onboarding-h5.html /tmp/account-group-onboarding-rewrite-mobile-full.png
```

Expected: both screenshot commands exit 0.

Manual inspection must check:

- capability map is not collapsed into three cards;
- architecture section is readable on desktop;
- architecture section stacks without horizontal overflow on mobile;
- core chain preserves order and does not overlap;
- AI and newcomer sections remain readable;
- no text clips out of cards.

- [ ] **Step 6: Run diff check**

Run:

```bash
git diff --check -- wiki/reports/account-group-onboarding-h5.html wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md
```

Expected: no output.

- [ ] **Step 7: Record verification and commit**

Add verification lines:

```markdown
- Rewrite HTML parser check: passed with `python3 -m html.parser wiki/reports/account-group-onboarding-h5.html`.
- Rewrite required content check: passed for capability map, system architecture, core chain, account-domain AI collaboration, and newcomer path.
- Rewrite excluded capability check: passed; `授信能力` and `垫资能力` are not reader-facing capability groups.
- Rewrite sensitive-info grep: passed with no reader-facing matches for credentials, personal names, internal URLs, Feishu URLs, token strings, QR-code, GitLab, Jira, VPN, docs, or Apifox project links.
- Rewrite desktop screenshot: passed with `/tmp/account-group-onboarding-rewrite-desktop-full.png`.
- Rewrite mobile screenshot: passed with `/tmp/account-group-onboarding-rewrite-mobile-full.png`.
```

Mark Task 4 complete:

```markdown
- [x] 4. Verify visual quality and sensitive boundary
```

Commit:

```bash
git add wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md
git commit -m "docs: verify account onboarding h5 rewrite"
```

## Task 6: Final Local Review Status

**Files:**
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
- Modify: `wiki/reports/index.md` only if the index entry is inaccurate.
- Modify: `openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md`

- [ ] **Step 1: Verify report index link**

Run:

```bash
test -f wiki/reports/account-group-onboarding-h5.html
rg -n "账户组体系新人培训 H5|account-group-onboarding-h5.html" wiki/reports/index.md
```

Expected: file exists and index match is present.

- [ ] **Step 2: Add final decision**

Add or update a final decision block:

```markdown
## Rewrite Decision

- Local H5 rewrite is ready for user review.
- The rewrite fixes the failed first draft by adding real capability-map depth, layered system architecture, complete core chain, and account-domain AI collaboration.
- Feishu sync is not approved by default and remains a separate follow-up.
- Sensitive onboarding access details from Feishu source documents were intentionally excluded.
```

- [ ] **Step 3: Validate OpenSpec and mark final task**

Run:

```bash
openspec validate rewrite-account-group-onboarding-h5-domain-depth --strict
```

Expected:

```text
Change 'rewrite-account-group-onboarding-h5-domain-depth' is valid
```

Mark Task 5 complete:

```markdown
- [x] 5. Final local review status
```

- [ ] **Step 4: Commit**

Commit:

```bash
git add wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md openspec/changes/rewrite-account-group-onboarding-h5-domain-depth/tasks.md
git commit -m "docs: finalize account onboarding h5 rewrite review"
```

## Self-Review

Spec coverage:

- Revised capability-map depth: Task 3, Steps 2 and 5.
- Exclusion of 授信能力 / 垫资能力: Task 3 Step 5 and Task 5 Step 3.
- Layered system architecture: Task 3 Step 3 and Task 5 Step 2.
- Complete core chain: Task 3 Step 4 and Task 5 Step 2.
- Account-domain AI collaboration: Task 4 Steps 1 and 3.
- Sensitive Feishu boundary: Task 5 Step 4.
- Visual QA: Task 5 Step 5.
- OpenSpec lifecycle: Task 1 and Task 6.

Placeholder scan:

- The plan contains no open placeholder markers, deferred implementation notes, or unspecified test commands.
- Every verification step names exact commands and expected outcomes.

Scope check:

- The plan rewrites one existing H5 and its evidence artifacts.
- Feishu sync, publishing, and unrelated report cleanup remain out of scope.
