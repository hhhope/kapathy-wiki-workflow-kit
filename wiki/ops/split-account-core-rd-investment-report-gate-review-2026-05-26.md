---
title: split-account-core-rd-investment / report gate review
layer: ops
domain: account-clearing
ops_area: report-quality
canonical_object: split-account-core-rd-investment
artifact_type: gate-review
language: zh-CN
audience: internal
knowledge_level: working
period: 2026-05-26
source_links:
  - ../sources/split-account-core-rd-investment-source-2026-05-26.md
  - ../reports/split-account-core-rd-investment-analysis-2026-05-26.html
status: draft
updated_at: 2026-05-26
ai_generated: true
---

# split-account-core-rd-investment / report gate review

## Article Intent Contract

- Reader: management /研发管理视角。
- Reader decision: 判断分账核心改造中研发、测试、修复、代码生成分别占用了多久，以及后续应该盯哪些闭环指标。
- Main line: 研发投入不是单看编码，而是从工单人日、代码量、fix、主干合入和测试占用共同看闭环成本。
- Non-goals: 不做个人绩效排名；不把“规范化提交候选”直接等同于真实 AI 产出；不推断没有日期字段的独立任务周分布。
- User-owned judgments: 是否把 Git 规范提交正式定义为 AI 代码量；是否补充 account-book-query 的准确本地仓库。

## Reference Output Shape

- Selected shape: `inbox/nirvana/preview .html` 的管理 H5 风格。
- Retained patterns: 深色渐变头部、四张摘要卡、白底分区、legend、表格、扫描式甘特/条形视图、橙色 note 风险提示。
- Modified patterns: 原甘特图改为周投入堆叠条、代码提交/AI 出码复核表、按项目拆分的 Git 修复鱼骨图和结论卡。
- Rejected patterns: 不做纯表格堆叠；不做个人排名式榜单。

## Evidence Map

| Claim | Evidence | Boundary |
| --- | --- | --- |
| 主工单 311.65 人日 | `主工单任务底表` 348 条计入人日的子工单，`日百分比/100` 汇总 | `日百分比` 解释为人日；需业务确认是否有其他权重 |
| 总占用 356.4 人日 | 主工单 311.65 + 独立任务 44.75 | 独立任务缺日期，不进入周曲线 |
| 04/20-04/26 峰值 53.05 人日 | 主工单解决日期按 ISO 周聚合，H5 主标签改为周日期区间 | fallback 日期仅在解决日期缺失时使用；2026-W17 保留为辅助口径 |
| 研发投入持续甘特 | 按组别、子工单内容主题、ISO 周汇总人日 | 主题为内容审阅分桶，用于解释持续占用，不是 Jira 原生字段 |
| 账户组 112.3 人日内部消耗 | `研发部-账户组` 117 条计入人日子工单，按子工单概要关键词分桶 | 分桶是内容审阅口径，不等同 Jira 原生分类 |
| Excel 代码净增 +51,271 | `代码量统计` sheet | Excel 行数口径由源表给出，未验证其采集脚本 |
| Git 源码 +48,729 / -17,059 | 本地 `/mnt/d` 仓库 `git log --numstat --no-merges` | 只统计常见源码/配置后缀；本地仓库可能不是完整远端状态 |
| 本地 Git 总提交 746 | 相关仓库全分支扫描，Merge 296、非 Merge 450 | 全分支口径用于观察研发流转，不等同最终主干提交数 |
| AI/规范化候选 141 与返工信号 97 | 提交前缀和标题关键词扫描 | 这是出码后返工/重构信号，不是作者身份或绩效归因 |
| 日均出码 | 65 天扫描窗口下 Excel 新增约 +1,080 行/天，本地源码净增约 +750 行/天，AI/规范化候选约 2.2 次/天 | 吞吐指标，不等同稳定交付质量 |
| 开户/客户关系类 AI 替代率信号 | mandao-customer 75/110 非 Merge = 68.2%，cm-post 6/6 = 100% | 规范化候选代理指标，不证明真实作者身份；cm-post 样本小 |
| 清算和账户类人工复核红线 | cm-settle 2/149 候选占比低；clearing-trade 12/13 候选但 fix/refactor 4/13 | 资金、账户、清算类可提升出码比例，但不能取消人工复核 |
| 测试右移 | 05/04-05/24 测试相关投入 37.0 人日，占测试总量 47.5 人日的 77.9% | 后三周口径用于说明右移压力，不代表所有测试只发生在后段 |
| 接口范围与版本治理盲点 | 用户补充口径：新增 10 个内部接口、8 个对外接口，API Fox 管理下仍出现对外接口版本管理盲点 | 用户补充事实；未从 workbook 自动抽取，作为结论层管理判断使用 |
| 生产问题、产品、研发与测试要求 | 用户补充 2026-05-19 至 2026-05-22 聊天证据：自助结算影响银企云、凌晨结算验证、客户结算规则告警、准生产缺陷与新增报表仍在调 | 用户补充事实；作为生产问题闭环分析，不替代事故复盘或资金最终影响确认 |
| Git 修复鱼骨图 | 04-10 到 05-21 的业务开发、fix、refactor、merge、CR 提交，按 cm-settle、auxiliary-trade、mandao-customer、clearing-trade、cm-post/manager 分组 | 鱼骨图用于解释各项目研发消耗位置，主干合入不等同线上完成；项目分组是阅读结构，不是新的统计口径 |

## Section Drift Review

| Section | Objective | Judgment |
| --- | --- | --- |
| 摘要卡 | 快速给出投入、占用、峰值、代码量 | Retain |
| 周投入 | 体现各组按周研发投入 | Retain |
| 研发投入持续甘特 | 回答为什么开发完成后研发人力仍未释放 | Retain with classification boundary |
| 各组占用 | 防止只看总人日，看不到组间压力 | Retain |
| 账户组内部消耗 | 回答账户组人力具体耗在哪些子工单内容上 | Retain with classification boundary |
| 代码提交与 AI 出码复核 | 合并 Excel 代码量、本地 Git 总提交、规范化候选、返工信号 | Retain with boundary |
| Git 修复鱼骨图 | 按项目解释研发被消耗在哪里，避免线性时间轴只像流水账 | Retain with boundary |
| 背后看出什么 | 同时说清楚做得好的、红线和暴露的问题 | Retain with user-supplied interface boundary |
| 生产问题、产品、研发与测试要求 | 单独列出生产问题，并把 cm-settle / clearing-trade / 账户 / 结算链路拆成产品、研发和测试要求 | Retain as draft with chat-evidence boundary |

## Decision

- Draft may be used as internal review H5.
- Do not claim final authoritative AI code volume until Git convention-to-AI ownership is confirmed.
- Next useful validation: confirm `account-book-query` exact local repository and whether Excel `日百分比` should be interpreted as exactly `人日 * 100`.

## Verification Update: Git Repair Fishbone

- HTML parser: passed for `wiki/reports/split-account-core-rd-investment-analysis-2026-05-26.html`.
- Frontmatter precheck: passed for `wiki/sources/split-account-core-rd-investment-source-2026-05-26.md` with 0 blocking entries; repo-level producer warnings remain unrelated.
- Full frontmatter checker: passed with 0 blocking entries.
- `git diff --check`: passed for the changed H5, source, gate review, and tar package.
- Package check: `split-account-core-rd-investment-analysis-2026-05-26.tar.gz` contains the updated H5.
- Playwright desktop screenshot: generated `/tmp/split-account-rd-fishbone-desktop.png`; fishbone section has 5 project rows and 20 bones, no console errors, no desktop horizontal overflow.
- Playwright mobile screenshot: generated `/tmp/split-account-rd-fishbone-mobile.png`; fishbone itself fits within the viewport and stacks correctly. The WSL browser environment lacks a Chinese CJK font, so screenshot text renders as tofu boxes in that environment.

## Verification Update: Week Date Labels

- Reader feedback: W12-W21 table labels were hard to read.
- Change: H5 primary weekly labels now use date ranges from 03/16-03/22 through 05/18-05/24; ISO week labels are kept only as secondary hints in the weekly bar chart and source evidence.
- Boundary: data aggregation remains ISO-week based; this is a display/readability change, not a recalculation.
- HTML parser, frontmatter precheck, full frontmatter checker, and `git diff --check` passed after the date-label update.
- Playwright screenshots: `/tmp/split-account-rd-week-dates-desktop.png` and `/tmp/split-account-rd-week-dates-mobile.png`.
- Playwright layout assertion: 10 weekly bar labels and 10 Gantt date headers rendered without clipping; desktop and mobile console checks had no errors. The wide Gantt table remains horizontally scrollable by design.

## Verification Update: Good / Bad Findings

- Reader feedback: section 8 should cover both good and bad findings; testing right-shift must be explicit; section 6 should include daily code-output analysis.
- Change: section 6 adds a daily throughput table; section 8 is rewritten into six findings covering total investment visibility, opening/customer AI substitution signal, daily output speed, clearing/account human-review redline, testing right shift, and interface version-governance blind spot.
- Boundary: AI substitution uses the existing convention-based proxy. The 10 internal / 8 external interface count is recorded as user-provided review input, not independently extracted workbook data.
- HTML parser, frontmatter precheck, full frontmatter checker, and `git diff --check` passed after the rewrite.
- Playwright screenshots: `/tmp/split-account-rd-good-bad-desktop.png` and `/tmp/split-account-rd-good-bad-mobile.png`.
- Playwright layout assertion: section 8 renders 6 finding cards with no undersized boxes; the daily-output table renders 3 rows; section 8 contains both the 77.9% testing right-shift signal and the 10 internal / 8 external interface governance signal; desktop and mobile console checks had no errors.

## Verification Update: Production / Product / Engineering / Testing Requirements

- Reader feedback: production issues need a separate column, and cm-settle / clearing-trade / account / settlement should be pulled out with product, R&D, and testing requirements.
- Change: H5 adds section 9 with columns `生产问题`, `证据/影响`, `牵涉链路`, `产品要求`, `研发要求`, and `测试要求`.
- Source update: records the 2026-05-19 to 2026-05-22 chat supplement as production-issue evidence.
- Boundary: production issue claims come from user-provided chat evidence and should not be treated as final incident postmortem, final funding impact, or independently reconciled settlement data.
- HTML parser, frontmatter precheck, full frontmatter checker, `git diff --check`, and tar package listing passed after the production issue update.
- Playwright screenshots after adding R&D requirements: `/tmp/split-account-rd-production-engineering-desktop.png` and `/tmp/split-account-rd-production-engineering-mobile.png`.
- User follow-up: remove the data-sync settlement-abnormal row from section 9 and the linked source supplement.
- User follow-up: the monitoring dashboard, SQL check, rollback standard, and named-owner preparation belongs to R&D; add R&D into this section.
- Playwright layout assertion after adding R&D requirements: section 9 renders 4 production issue rows; headers include product, R&D, and testing requirement columns; the removed row text no longer appears; the launch-success row puts monitoring dashboard, SQL checks, rollback standard, and named-owner preparation under R&D instead of testing; desktop and mobile console checks had no errors.
- Mobile boundary: overall body width is 624px at a 390px viewport because existing wide tables remain horizontally scrollable; the new section 9 content itself is present and readable in the mobile DOM check.
