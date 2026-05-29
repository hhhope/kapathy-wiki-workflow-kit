# Account Group Onboarding H5 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone internal H5 training draft that helps account-group newcomers understand the account domain, active project entry points, AI collaboration system, and practical growth path.

**Architecture:** Implement one static HTML report under `wiki/reports/` using inline CSS and semantic sections, plus one report gate-review artifact under `wiki/ops/`. Keep source evidence, reader intent, sensitive-info boundaries, and verification results outside the H5 body in the gate-review page. Update `wiki/reports/index.md` only after the H5 exists and passes local checks.

**Tech Stack:** Static HTML/CSS, no JavaScript framework, no build step, browser verification through local file URL or `playwright screenshot`, markdown gate review.

---

## File Structure

- Create: `wiki/reports/account-group-onboarding-h5.html`
  - Responsibility: reader-facing long-scroll H5 with 14 sections, rebuilt visuals in HTML/CSS, no raw internal URLs, credentials, personal contact details, or slide dumps.
- Create: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`
  - Responsibility: public-report gate evidence: reader intent, output shape, evidence map, sensitive-info boundary, section drift review, and verification log.
- Modify: `wiki/reports/index.md`
  - Responsibility: add one index entry linking to the H5 after verification passes.
- Do not create by default: `wiki/reports/assets/account-group-onboarding/`
  - Use only if implementation proves an extracted source image is necessary and cannot be redrawn clearly in HTML/CSS.

## Task 1: Create Gate Review Artifact

**Files:**
- Create: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`

- [ ] **Step 1: Create the gate review file**

Use `apply_patch` to add `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md` with this content:

```markdown
---
title: account-group-onboarding-h5 / report gate review
layer: ops
domain: account-clearing
ops_area: report-quality
canonical_object: account-group-onboarding-h5
artifact_type: gate-review
language: zh-CN
audience: internal
knowledge_level: working
period: 2026-05-29
source_links:
  - ../reports/account-group-onboarding-h5.html
  - ../sources/split-account-core-rd-investment-source-2026-05-26.md
status: draft
updated_at: 2026-05-29
ai_generated: true
---

# account-group-onboarding-h5 / report gate review

## Article Intent Contract

- Reader: 账户组新入职应届生。
- Reader job: 快速理解账户组做什么、核心链路怎么串、正在做哪些项目、自己能从哪里上手，以及 AI 协作体系如何进入日常工程。
- Main line: 先建立账户领域地图，再落到真实项目入口，最后给出新人 3 天、第一周、30/60/90 天成长路径。
- Non-goals: 不复刻 PPT；不做管理述职；不暴露账号、密码、内网地址、联系人、测试环境细节；不把 AI 体系讲成泛化工具宣传。
- User-owned judgments: H5 优先；复用历史技术 H5 风格；必须包含规划、正在做的项目、新人能做什么和能获得什么；新增 AI 体系建设。

## Reference Output Shape

- Selected shape: 技术架构海报式 + 培训路线式长页 H5。
- Retained patterns: 粗线条技术海报、能力地图、深色/暖纸对比、信息卡片、路线图、任务池。
- Modified patterns: 管理驾驶舱的高密度数据只用于项目入口，不作为主视觉；新人路径用更清晰的 3 天 / 第一周 / 30-60-90 结构承接。
- Rejected patterns: 纯 PPT 搬运、长表格堆叠、个人名单/联系人曝光、单纯 AI 工具清单。

## Evidence Map

| H5 Section | Source | Use | Boundary |
| --- | --- | --- | --- |
| 你加入的是什么小组 | `账户组技术规划与述职 _v6.pptx` | 职责边界、系统规模、治理方向 | 只保留职责和规模级别，不放负责人姓名 |
| 账户体系能力地图 | `账户组技术规划与述职 _v6.pptx`, `4.0清结算账户体系概述.pdf` | 开户、账户、账务、余额、结算、对账、渠道、风险能力 | 以新人认知地图表达，不复刻源图 |
| 核心业务链路 | `账户组技术现状分享.pptx`, `4.0清结算账户体系概述.pdf` | 开户、收单/付款、分账/提现、记账、对账主链路 | 不展开敏感系统地址或客户细节 |
| 典型业务对象 | `账户组技术现状分享.pptx` | 多渠道收款、宝财通、宝户通、银企云/银企通 | 只讲对象和关系，不讲内部访问方式 |
| 常见问题 | `账户组技术现状分享.pptx` | 无法提现、开户失败、入金失败、入账慢、热点更新、压测调优 | 改写为训练场景，不做事故复盘 |
| 正在做的项目 | `wiki/sources/split-account-core-rd-investment-source-2026-05-26.md` | 宝财通/二级商户、结算/出款/清算、报表联调、余额账本验证 | 不使用个人投入排名 |
| 技术规划 | `账户组技术规划与述职 _v6.pptx` | 统一账户、余额中心、账务标准化、结算对账收敛、可观测、风险地图 | 只保留方向和新人可理解的价值 |
| AI 协作体系 | Feishu `Account Harness：总览` | OpenSpec / Lore / Graphify / lore-bootstrap 四层模型 | 讲工程协作边界，不讲仓库内部治理细节 |
| AI Coding 成熟度 | Feishu `AICoding L1-L4 路线图` | 当前 L2，下一步 L2 -> L3 阶段协作固定化 | 不承诺已经达到 L3/L4 |
| 新人上手路径 | Feishu `账户组技术小组新人入职指引`, `IT技术小组新人入职指引` | Day 1/2/3、第一周任务、规范、环境、第一项任务 | 去除账号、密码、内网 URL、联系人 |

## Sensitive Information Boundary

The H5 must not contain:

- account names, passwords, SSH setup details, VPN setup details, test-system URLs, internal IP addresses, personal owner names, personal emails, or group QR codes;
- exact production incident timelines unless rewritten as generic training scenarios;
- raw person-day tables or personal contribution ranking;
- Feishu document tokens or internal source URLs in the reader-facing body.

Allowed in the H5:

- business object names such as 宝财通、宝户通、多渠道收款、银企云/银企通;
- capability names such as 开户、账务、余额、结算、对账、报表、风险地图;
- AI collaboration names such as OpenSpec、Lore、Graphify、lore-bootstrap;
- aggregate onboarding rhythm: Day 1 / Day 2 / Day 3 / 第一周 / 30-60-90.

## Section Drift Review

| Section | Objective | Status |
| --- | --- | --- |
| Cover | Establish the training promise | Planned |
| Group and capability map | Build first mental model | Planned |
| Business chain and objects | Explain domain flow | Planned |
| Problems and active projects | Show real work entry | Planned |
| Technical planning | Connect work to future direction | Planned |
| AI collaboration and maturity | Explain AI体系建设 as engineering gates | Planned |
| Newcomer path and task pool | Tell newcomer what to do and gain | Planned |
| Closing | Reframe newcomer role from requirement receiver to accountable engineer | Planned |

## Verification Log

- Pending: HTML parser check.
- Pending: source-to-screen mapping check.
- Pending: sensitive-info grep.
- Pending: desktop screenshot.
- Pending: mobile screenshot.
- Pending: final index link check.
```

- [ ] **Step 2: Verify frontmatter and required sections exist**

Run:

```bash
rg -n "Article Intent Contract|Reference Output Shape|Evidence Map|Sensitive Information Boundary|Verification Log" wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
```

Expected: five matching section headings.

- [ ] **Step 3: Commit the gate review artifact**

Run:

```bash
git add wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
git commit -m "docs: add account onboarding h5 gate review"
```

Expected: commit succeeds and stages only the gate review file.

## Task 2: Create H5 Skeleton And Visual System

**Files:**
- Create: `wiki/reports/account-group-onboarding-h5.html`

- [ ] **Step 1: Add the static HTML skeleton**

Use `apply_patch` to add `wiki/reports/account-group-onboarding-h5.html` with a complete document shell. The initial file must include the section IDs and empty content containers shown below:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>账户组体系新人培训 H5</title>
  <style>
    :root {
      --paper: #f8efd8;
      --sheet: #fffaf0;
      --ink: #141414;
      --muted: #5b6472;
      --line: rgba(20, 20, 20, .22);
      --navy: #14213d;
      --blue: #2f77c5;
      --green: #0f9d7a;
      --orange: #e96b2c;
      --purple: #7d55a8;
      --yellow: #f3c64f;
      --card: #ffffff;
      --shadow: 0 14px 0 rgba(20, 20, 20, .08);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background:
        linear-gradient(rgba(20, 20, 20, .045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(20, 20, 20, .045) 1px, transparent 1px),
        #efe6d2;
      background-size: 28px 28px;
      color: var(--ink);
      font-family: "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", Arial, sans-serif;
      letter-spacing: 0;
      line-height: 1.55;
    }
    .page { width: min(1180px, calc(100vw - 28px)); margin: 0 auto; padding: 22px 0 56px; }
    .hero, .section {
      border: 4px solid var(--ink);
      border-radius: 22px;
      background: var(--sheet);
      box-shadow: var(--shadow);
      margin: 0 0 18px;
      padding: 24px;
      overflow: hidden;
    }
    .hero { min-height: 560px; display: grid; align-content: space-between; }
    .kicker { display: inline-flex; width: fit-content; border: 3px solid var(--ink); border-radius: 999px; background: var(--orange); color: #fff; padding: 6px 12px; font-weight: 900; }
    h1, h2, h3, p { margin-top: 0; }
    h1 { max-width: 860px; font-size: clamp(38px, 7vw, 82px); line-height: 1.02; text-decoration: underline; text-decoration-color: var(--yellow); text-decoration-thickness: 8px; text-underline-offset: 10px; }
    h2 { font-size: clamp(26px, 4vw, 42px); line-height: 1.14; }
    .lead { color: var(--muted); font-size: clamp(17px, 2vw, 22px); font-weight: 800; }
    .grid-2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; }
    .card { border: 2px solid var(--line); border-radius: 14px; background: var(--card); padding: 14px; }
    .card b { display: block; margin-bottom: 6px; font-size: 18px; }
    .tag { display: inline-flex; width: fit-content; border-radius: 999px; padding: 4px 9px; background: #eef2ff; color: #3730a3; font-size: 12px; font-weight: 900; }
    .flow { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; align-items: stretch; }
    .flow .node { border: 3px solid var(--ink); border-radius: 16px; background: #fff; padding: 14px; min-height: 120px; }
    .capability-map { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }
    .capability-group { border: 3px solid var(--ink); border-radius: 16px; background: #fff; padding: 14px; }
    .roadmap { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
    .level { border: 3px solid var(--ink); border-radius: 16px; background: #fff; padding: 14px; min-height: 170px; }
    .level.current { background: #faf5ff; border-color: var(--purple); }
    .footer-note { border: 2px dashed var(--blue); border-radius: 16px; background: #f8fafc; padding: 16px; font-weight: 800; }
    @media (max-width: 860px) {
      .page { width: min(100vw - 18px, 680px); padding-top: 10px; }
      .hero, .section { border-width: 3px; border-radius: 18px; padding: 18px; }
      .grid-2, .grid-3, .grid-4, .flow, .capability-map, .roadmap { grid-template-columns: 1fr; }
      .hero { min-height: auto; gap: 28px; }
    }
  </style>
</head>
<body>
  <main class="page">
    <section class="hero" id="cover"></section>
    <section class="section" id="group"></section>
    <section class="section" id="capability-map"></section>
    <section class="section" id="business-chain"></section>
    <section class="section" id="business-objects"></section>
    <section class="section" id="typical-problems"></section>
    <section class="section" id="active-projects"></section>
    <section class="section" id="technical-planning"></section>
    <section class="section" id="ai-collaboration"></section>
    <section class="section" id="ai-maturity"></section>
    <section class="section" id="first-week"></section>
    <section class="section" id="growth-path"></section>
    <section class="section" id="task-pool"></section>
    <section class="section" id="closing"></section>
  </main>
</body>
</html>
```

- [ ] **Step 2: Run a basic HTML parse check**

Run:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
path = Path("wiki/reports/account-group-onboarding-h5.html")
class Parser(HTMLParser):
    pass
Parser().feed(path.read_text(encoding="utf-8"))
print("html-parse-ok")
PY
```

Expected: `html-parse-ok`.

- [ ] **Step 3: Verify all section IDs exist**

Run:

```bash
rg -n 'id="(cover|group|capability-map|business-chain|business-objects|typical-problems|active-projects|technical-planning|ai-collaboration|ai-maturity|first-week|growth-path|task-pool|closing)"' wiki/reports/account-group-onboarding-h5.html
```

Expected: 14 matches.

- [ ] **Step 4: Commit the skeleton**

Run:

```bash
git add wiki/reports/account-group-onboarding-h5.html
git commit -m "feat: add account onboarding h5 skeleton"
```

Expected: commit succeeds and stages only the H5 file.

## Task 3: Fill Account Domain Sections

**Files:**
- Modify: `wiki/reports/account-group-onboarding-h5.html`
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`

- [ ] **Step 1: Replace the first eight empty sections with account-domain content**

Use `apply_patch` to replace `cover`, `group`, `capability-map`, `business-chain`, `business-objects`, `typical-problems`, `active-projects`, and `technical-planning` section bodies with concise reader-facing content. The H5 must include these exact phrases somewhere in the account-domain sections:

```text
账户组不是单个系统，而是一组围绕资金账户链路的能力。
开户、账户、账务、余额、结算、对账、报表、渠道、风险治理
开户 -> 收单/付款 -> 分账/提现 -> 记账 -> 对账
多渠道收款
宝财通
宝户通
银企云 / 银企通
无法提现
开户失败
入金失败
入账慢
宝财通 / 二级商户关系
结算 / 出款 / 清算
接口 / 报表 / 联调
余额 / 账本验证
统一账户模型
余额中心
账务标准化
结算对账收敛
可观测
风险地图
```

The implementation can use this card pattern repeatedly:

```html
<div class="card">
  <span class="tag">项目入口</span>
  <b>宝财通 / 二级商户关系</b>
  <p>新人可以从字段理解、接口联调、关系校验和回归用例开始，逐步理解会员号、客户号、SMID 与商户关系如何影响账户链路。</p>
</div>
```

- [ ] **Step 2: Run account-domain content assertions**

Run:

```bash
rg -n "资金账户链路|开户、账户、账务、余额、结算、对账、报表、渠道、风险治理|开户 -> 收单/付款 -> 分账/提现 -> 记账 -> 对账|宝财通 / 二级商户关系|统一账户模型|风险地图" wiki/reports/account-group-onboarding-h5.html
```

Expected: all six assertions match.

- [ ] **Step 3: Update gate review verification log**

Append this line under `## Verification Log`:

```markdown
- Account-domain content check: passed after sections 0-7 included capability map, business chain, business objects, typical problems, active projects, and technical planning.
```

- [ ] **Step 4: Run HTML parse check again**

Run:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
HTMLParser().feed(Path("wiki/reports/account-group-onboarding-h5.html").read_text(encoding="utf-8"))
print("html-parse-ok")
PY
```

Expected: `html-parse-ok`.

- [ ] **Step 5: Commit account-domain content**

Run:

```bash
git add wiki/reports/account-group-onboarding-h5.html wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
git commit -m "feat: add account onboarding domain content"
```

Expected: commit succeeds with only the H5 and gate-review files staged.

## Task 4: Fill AI Collaboration And Newcomer Path Sections

**Files:**
- Modify: `wiki/reports/account-group-onboarding-h5.html`
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`

- [ ] **Step 1: Replace the remaining six empty sections with AI and onboarding content**

Use `apply_patch` to fill `ai-collaboration`, `ai-maturity`, `first-week`, `growth-path`, `task-pool`, and `closing`. The H5 must include these exact phrases:

```text
OpenSpec 管变更
Lore 管记忆
Graphify 管结构
lore-bootstrap 管安装
当前更接近 L2
下一步是把 L2 -> L3 的阶段协作固定下来
Day 1：账号、设备、基础工具
Day 2：环境、代码、项目跑通
Day 3：规范、小任务、第一次反馈
第一周：跑通一条核心业务流程
30 天：听懂链路
60 天：参与模块
90 天：独立排障和交付小任务
你不是来接需求，而是学习如何管住资金账户链路。
```

Use this maturity card pattern:

```html
<div class="level current">
  <span class="tag">当前阶段</span>
  <b>L2：按约束完成单次任务</b>
  <p>人定义目标和边界，AI 按 gate 执行。下一步不是堆更多工具，而是把需求、设计、研发、CR、验收、沉淀固定成阶段协作。</p>
</div>
```

- [ ] **Step 2: Run AI and onboarding content assertions**

Run:

```bash
rg -n "OpenSpec 管变更|Lore 管记忆|Graphify 管结构|lore-bootstrap 管安装|当前更接近 L2|L2 -> L3|Day 1：账号、设备、基础工具|第一周：跑通一条核心业务流程|30 天：听懂链路|90 天：独立排障和交付小任务|你不是来接需求" wiki/reports/account-group-onboarding-h5.html
```

Expected: all assertions match.

- [ ] **Step 3: Update gate review verification log**

Append this line under `## Verification Log`:

```markdown
- AI and onboarding content check: passed after sections 8-13 included four-layer AI collaboration, L1-L4 maturity, 3-day onboarding, first-week task, 30/60/90 growth path, and task pool.
```

- [ ] **Step 4: Run HTML parse check again**

Run:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
HTMLParser().feed(Path("wiki/reports/account-group-onboarding-h5.html").read_text(encoding="utf-8"))
print("html-parse-ok")
PY
```

Expected: `html-parse-ok`.

- [ ] **Step 5: Commit AI and onboarding content**

Run:

```bash
git add wiki/reports/account-group-onboarding-h5.html wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
git commit -m "feat: add account onboarding ai growth path"
```

Expected: commit succeeds with only the H5 and gate-review files staged.

## Task 5: Run Sensitive-Info And Visual Verification

**Files:**
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`

- [ ] **Step 1: Run sensitive-info grep**

Run:

```bash
rg -n "密码|账号已开通|Ethan|@baofu|10\\.254|http://10\\.|https://test-|云枢|VPN|扫码|二维码|GitLab|Jira|王竹|彬彬|杨锋将|token=|feishu.cn/wiki|feishu.cn/docx" wiki/reports/account-group-onboarding-h5.html
```

Expected: no output and exit code 1. If it prints matches, remove or abstract the matched text before continuing.

- [ ] **Step 2: Run source-to-screen coverage check**

Run:

```bash
rg -n "账户组技术规划与述职|账户组技术现状分享|4.0清结算账户体系概述|分账核心改造|账户组技术小组新人入职指引|IT技术小组新人入职指引|Account Harness|AICoding L1-L4" wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
```

Expected: at least the source names relevant to the evidence map are present.

- [ ] **Step 3: Take desktop screenshot**

Run:

```bash
playwright screenshot --viewport-size=1440,1800 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/account-group-onboarding-h5.html /tmp/account-group-onboarding-desktop.png
```

Expected: screenshot file `/tmp/account-group-onboarding-desktop.png` is created.

- [ ] **Step 4: Take mobile screenshot**

Run:

```bash
playwright screenshot --viewport-size=390,1200 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/account-group-onboarding-h5.html /tmp/account-group-onboarding-mobile.png
```

Expected: screenshot file `/tmp/account-group-onboarding-mobile.png` is created.

- [ ] **Step 5: Manually inspect screenshots**

Use `view_image` on both screenshots. Pass criteria:

- cover text is visible and not clipped;
- capability map cards stack cleanly on mobile;
- business-chain flow does not overflow the viewport on mobile;
- AI maturity cards are legible;
- 30/60/90 and task-pool sections remain readable;
- no obvious overlapping text.

- [ ] **Step 6: Update gate review verification log**

Append these lines under `## Verification Log`:

```markdown
- Sensitive-info grep: passed; reader-facing H5 contains no credentials, internal IPs, personal contacts, Feishu tokens, or raw internal URLs.
- HTML parser: passed after final content.
- Desktop screenshot: `/tmp/account-group-onboarding-desktop.png`; no visible clipping or overlapping in manual inspection.
- Mobile screenshot: `/tmp/account-group-onboarding-mobile.png`; stacked layout remains readable in manual inspection.
```

- [ ] **Step 7: Commit verification evidence update**

Run:

```bash
git add wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
git commit -m "docs: record account onboarding h5 verification"
```

Expected: commit succeeds with only the gate-review file staged.

## Task 6: Add Reports Index Entry

**Files:**
- Modify: `wiki/reports/index.md`
- Modify: `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`

- [ ] **Step 1: Add the report index entry**

Insert this bullet under `## Current Pages` in `wiki/reports/index.md`:

```markdown
- [账户组体系新人培训 H5](account-group-onboarding-h5.html): internal H5 onboarding draft explaining the account-group capability map, business chain, active project entries, AI collaboration system, and newcomer growth path.
```

- [ ] **Step 2: Verify the link path exists**

Run:

```bash
test -f wiki/reports/account-group-onboarding-h5.html && rg -n "账户组体系新人培训 H5|account-group-onboarding-h5.html" wiki/reports/index.md
```

Expected: command succeeds and prints the new index entry.

- [ ] **Step 3: Update gate review final decision**

Append this block to `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`:

```markdown
## Decision

- Local H5 draft is ready for user review.
- Feishu sync is not approved by default and remains a separate follow-up.
- Extracted image assets were not required because primary visuals were rebuilt in HTML/CSS.
```

- [ ] **Step 4: Run final diff check**

Run:

```bash
git diff --check -- wiki/reports/account-group-onboarding-h5.html wiki/reports/index.md wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
```

Expected: no output.

- [ ] **Step 5: Commit index and final gate decision**

Run:

```bash
git add wiki/reports/index.md wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md
git commit -m "docs: list account onboarding h5 report"
```

Expected: commit succeeds with only the index and gate-review files staged.

## Final Verification

- [ ] **Step 1: Check git truth**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: latest commit is `docs: list account onboarding h5 report`. Pre-existing unrelated dirty files may remain; do not stage or revert them.

- [ ] **Step 2: Report completion boundary**

Final response must include:

- path to `wiki/reports/account-group-onboarding-h5.html`;
- path to `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`;
- screenshot paths if generated;
- statement that Feishu sync was not performed.

