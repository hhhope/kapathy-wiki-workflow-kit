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
| 背后看出什么 | 从数据回到管理结论 | Retain |

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
