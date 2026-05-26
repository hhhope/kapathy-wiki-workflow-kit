---
title: 分账核心改造账户和宝财通研发投入证据摘录
type: source
layer: sources
source_path: inbox/分账核心改造账户和宝财通改造内容.xlsx
source_type: spreadsheet
language: zh-CN
domain: account-clearing
audience: management
knowledge_level: working
period: weekly
source_links: []
status: draft
updated_at: 2026-05-26
ai_generated: true
---

# 分账核心改造账户和宝财通研发投入证据摘录

## Source Metadata

- Source workbook: `inbox/分账核心改造账户和宝财通改造内容.xlsx`
- Local Git scan window: `2026-03-19` to `2026-05-22`
- Main task date basis: `解决日期` first, then `子工单提测时间` / planned dates as fallback.
- Person-day interpretation: `日百分比 / 100 = 人日`.
- Git convention interpretation: non-merge commits whose subject starts with `feat:`, `fix:`, `refactor:`, `style:`, `chore:`, `docs:`, `test:`, or `perf:` are treated as `AI/规范化提交候选`; this is an audit proxy, not a definitive authorship claim.

## Workbook Sheets Used

- `主工单任务底表`: 348 条子工单，合计 311.65 人日，覆盖 2026-03-19 to 2026-05-21.
- `主工单人力透视`: used as cross-check for group/person effort.
- `其他独立任务工单`: 44.75 人日，缺少日期字段，单列为额外占用。
- `账户和宝财通改造内容`: used for scope framing.
- `代码量统计`: used as workbook-provided project code-volume baseline.

## Weekly Main-Task Investment

| 周 | 合计人日 | 账户组 | 支付组 | 商业应用组 | 测试部 | 通用服务组 | 产品SBU |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-W12 | 0.2 | 0.2 | 0 | 0 | 0 | 0 | 0 |
| 2026-W13 | 3.1 | 1 | 0 | 1 | 0 | 0 | 1.1 |
| 2026-W14 | 9.4 | 2 | 2 | 5 | 0 | 0 | 0.4 |
| 2026-W15 | 17.9 | 10 | 1 | 5.9 | 1 | 0 | 0 |
| 2026-W16 | 48.2 | 22.7 | 11.6 | 9.9 | 2 | 2 | 0 |
| 2026-W17 | 53.05 | 22 | 15.55 | 12 | 1.5 | 2 | 0 |
| 2026-W18 | 45 | 9.8 | 15.2 | 11 | 6 | 3 | 0 |
| 2026-W19 | 47.4 | 17 | 7.4 | 8.1 | 10.9 | 4 | 0 |
| 2026-W20 | 44.1 | 12.7 | 8 | 6 | 13.4 | 4 | 0 |
| 2026-W21 | 43.3 | 14.9 | 9.7 | 3 | 12.7 | 1.8 | 1.2 |

## Group Investment

| 组别 | 主工单人日 | 占主工单 |
| --- | --- | --- |
| 研发部-账户组 | 112.3 | 36.0% |
| 研发部-支付组 | 70.45 | 22.6% |
| 研发部-商业应用组 | 61.9 | 19.9% |
| 测试部 | 47.5 | 15.2% |
| 研发部-通用服务组 | 16.8 | 5.4% |
| 产品管理部-SBU | 2.7 | 0.9% |

## Account Group Internal Breakdown

Account group scope: 117计入人日子工单，合计112.3人日。Classification basis: child ticket summary keywords, grouped by consumed business/technical content.

| 内容主题 | 人日 | 账户组占比 | 主要内容信号 |
| --- | --- | --- | --- |
| 宝财通/二级商户与会员关系 | 34 | 30.3% | 二级升特约、SMID、会员号、开户、客户号 |
| 结算/出款/清算链路 | 28 | 24.9% | 结算、提现、代付、特下、清算 |
| 其他账户支持 | 23 | 20.5% | 分账接受方开通、计费配置、账户侧支持 |
| 接口/报表/联调对接 | 10 | 8.9% | 报表、对账 SQL、商户对账、联调 |
| 余额查询/账本验证 | 6.7 | 6.0% | 余额、查询、账本、记账结果 |
| 发布验证/CR/历史梳理 | 6.6 | 5.9% | 发布、上线、准生产验证、CR、历史逻辑 |
| 待分/接收户账户模型 | 4 | 3.6% | 待分账户、分账接收户、账户模型 |

| 经办人 | 人日 | 主要消耗内容 |
| --- | --- | --- |
| 竹 王 | 30.8 | 宝财通/二级商户与会员关系 18；其他账户支持 8.8；余额查询 3 |
| 彭清正 | 26.3 | 结算/出款/清算 9；宝财通/二级商户 6；其他账户支持 5 |
| 焕焕 轩 | 25 | 结算/出款/清算 8；接口/报表/联调 5；其他账户支持 4 |
| 圣彬彬 | 12.7 | 结算/出款/清算 10.7；待分/接收户账户模型 1 |
| 鹏 严 | 11 | 宝财通/二级商户 5；其他账户支持 4；发布验证/CR 2 |
| 开发 刘 | 6 | 接口/报表/联调 4；宝财通/二级商户 1；发布验证 1 |
| 龙伟 吴 | 0.3 | 结算/出款/清算 0.3 |
| 任利利 | 0.2 | 其他账户支持 0.2 |

| 工作性质 | 人日 | 账户组占比 |
| --- | --- | --- |
| 开发/改造 | 78.2 | 69.6% |
| 验证/回归 | 21.5 | 19.1% |
| 上线/发布 | 5.6 | 5.0% |
| 其他 | 4.2 | 3.7% |
| 修复/排查 | 1.5 | 1.3% |
| CR/梳理/沟通 | 1.3 | 1.2% |

## Task-Type Split

| 类型 | 人日 | 占比 |
| --- | --- | --- |
| 研发 | 246.1 | 79.0% |
| 测试 | 47.4 | 15.2% |
| 其他 | 13.15 | 4.2% |
| 产品 | 2.7 | 0.9% |
| 日常 | 2.3 | 0.7% |

## Workbook Code Volume Baseline

| 项目 | 操作人 | 提交次数 | 新增代码 | 删除代码 | 净增代码 |
| --- | --- | --- | --- | --- | --- |
| cm-settle | 彬彬 | 136 | +20,033 | -2,693 | +17,340 |
| clearing-trade | 焕焕 | 13 | +4,248 | -274 | +3,974 |
| clearing-manager | 焕焕 | 3 | +42 | -25 | +17 |
| cm-post | 焕焕 | 5 | +1,861 | -31 | +1,830 |
| mandao-customer | 王竹 | 167 | +30,770 | -15,043 | +15,727 |
| auxiliary-trade | 王竹 | 16 | +7,427 | -201 | +7,226 |
| account-book-query | 王竹 | 4 | +1,340 | -14 | +1,326 |
| bill-cache | 王竹 | 3 | +105 | -54 | +51 |
| mandao-account-book | 清正 | 18 | +4,378 | -598 | +3,780 |

Workbook total: `+70,204` / `-18,933` / net `+51,271`.

## Local Git Audit Snapshot

| 项目 | 全量提交 | 非Merge | 源码行 | AI/规范化候选 | fix次数 | 首个fix | 主干最后合入 | 修复窗口天数 | 边界 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cm-settle | 227 | 149 | +13,495/-2,492 | 2 次，+0/-0 | 0 | - | 2026-05-21 | - | - |
| clearing-trade | 23 | 13 | +3,465/-274 | 12 次，+3,091/-219 | 3 | 2026-04-14 | 2026-05-20 | 37 | - |
| clearing-manager | 10 | 4 | +628/-32 | 1 次，+23/-4 | 0 | - | 2026-05-20 | - | - |
| cm-post | 14 | 6 | +1,104/-37 | 6 次，+1,104/-37 | 0 | - | 2026-05-21 | - | Excel 项目 cm-post 映射到本地 cm-post-service。 |
| mandao-customer | 130 | 110 | +22,451/-12,934 | 75 次，+13,627/-6,058 | 5 | 2026-04-20 | 2026-05-21 | 32 | - |
| auxiliary-trade | 338 | 164 | +7,533/-1,278 | 45 次，+1,898/-489 | 17 | 2026-04-21 | 2026-05-21 | 31 | - |
| account-book-query | 0 | 0 | +0/-0 | 0 次，+0/-0 | 0 | - | - | - | 本地使用 /mnt/d/cloud/account-query 作为候选映射；未扫到相关提交，需人工确认。 |
| bill-cache | 4 | 4 | +53/-12 | 0 次，+0/-0 | 0 | - | 2026-05-21 | - | - |
| mandao-account-book | 0 | 0 | +0/-0 | 0 次，+0/-0 | 0 | - | - | - | - |

Local Git source-like total: `+48,729` / `-17,059`. AI/规范化候选 source-like total: `141` commits, `+19,743` / `-6,807`. Fix total: `25` commits, `+823` / `-118`.

## Evidence Boundary

- `其他独立任务工单` has no weekly date field, so it is not added to the weekly curve.
- `account-book-query` local mapping is not confirmed; both `/mnt/d/cloud/account-query` and `/mnt/d/whale/account-query` had no matching commits in the scan window.
- Local Git stats and workbook stats differ because workbook likely uses business-selected projects and line-count rules, while local audit counts source-like file suffixes from local repositories.
