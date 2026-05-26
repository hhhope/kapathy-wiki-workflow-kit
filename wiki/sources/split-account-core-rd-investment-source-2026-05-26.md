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

| 周日期 | ISO 周 | 合计人日 | 账户组 | 支付组 | 商业应用组 | 测试部 | 通用服务组 | 产品SBU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03/16-03/22 | 2026-W12 | 0.2 | 0.2 | 0 | 0 | 0 | 0 | 0 |
| 03/23-03/29 | 2026-W13 | 3.1 | 1 | 0 | 1 | 0 | 0 | 1.1 |
| 03/30-04/05 | 2026-W14 | 9.4 | 2 | 2 | 5 | 0 | 0 | 0.4 |
| 04/06-04/12 | 2026-W15 | 17.9 | 10 | 1 | 5.9 | 1 | 0 | 0 |
| 04/13-04/19 | 2026-W16 | 48.2 | 22.7 | 11.6 | 9.9 | 2 | 2 | 0 |
| 04/20-04/26 | 2026-W17 | 53.05 | 22 | 15.55 | 12 | 1.5 | 2 | 0 |
| 04/27-05/03 | 2026-W18 | 45 | 9.8 | 15.2 | 11 | 6 | 3 | 0 |
| 05/04-05/10 | 2026-W19 | 47.4 | 17 | 7.4 | 8.1 | 10.9 | 4 | 0 |
| 05/11-05/17 | 2026-W20 | 44.1 | 12.7 | 8 | 6 | 13.4 | 4 | 0 |
| 05/18-05/24 | 2026-W21 | 43.3 | 14.9 | 9.7 | 3 | 12.7 | 1.8 | 1.2 |

## Cross-Group Effort Gantt

| 投入内容 | 03/16-03/22 | 03/23-03/29 | 03/30-04/05 | 04/06-04/12 | 04/13-04/19 | 04/20-04/26 | 04/27-05/03 | 05/04-05/10 | 05/11-05/17 | 05/18-05/24 | 合计 | 持续原因 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 账户组｜宝财通/二级商户关系 |  | 1 |  | 1 | 8 | 11 | 1 | 3 | 3 | 6 | 34.0 | 二级升特约、SMID、会员号、开户/客户号从 04/13 持续到 05/24 |
| 账户组｜结算/出款/清算 |  |  | 1 | 4 | 8.7 | 5 | 5 | 1 | 2 | 1.3 | 28.0 | 提现、代付、清算接口从 03/30 到 05/24 都在改造/验证 |
| 账户组｜对接/账本/发布验证 |  |  |  | 1 |  |  | 2 | 8 | 5.7 | 6.6 | 23.3 | 05/04 后变成报表、对账、账本验证和发布准备 |
| 支付组｜退款/退回/垫资 |  |  | 1 | 1 | 7 | 7 | 8 | 0.5 | 1.2 | 2 | 27.7 | 退款、垫资、共同出款从早期开发延续到末期问题修复 |
| 支付组｜交易/收单/订单 |  |  |  |  | 4.6 | 5.05 | 4.2 | 3.1 | 1.1 | 1.9 | 19.95 | 收单、订单、聚合交易链路在 04/13-05/24 持续投入 |
| 支付组｜清结算/修复/发布 |  |  |  |  |  | 1.5 | 2 | 3.1 | 2.1 | 4.8 | 13.5 | 05/04-05/24 仍有计费、问题处理和上线发布占用 |
| 商业应用｜接口/网关/联调 |  |  | 1 | 0.9 | 2.5 | 5 | 3 | 2.9 | 1 |  | 16.3 | 接口、网关、联调从 03/30 持续到 05/17 |
| 商业应用｜商户入网/关系 |  |  |  |  | 1.5 | 2 | 5 | 2.9 | 1 |  | 12.4 | 宝财通、商户、入网和关系在 04/13-05/17 消耗明显 |
| 商业应用｜验证/修复/配置 |  |  | 2 | 3 | 1 | 2 | 1 | 1 | 2 | 3 | 15.0 | 配置、验证、问题优化贯穿开发后段 |
| 通用服务｜数据/报表/查询 |  |  |  |  | 1 | 1 | 1 | 2 | 4 | 0.8 | 9.8 | AD/BM、报表、导出、查询支撑从 04/13 延续到 05/24 |
| 通用服务｜配置/资源/环境 |  |  |  |  | 1 | 1 | 2 |  |  |  | 4.0 | 配置和环境资源集中在 04/13-05/03，为后续验证铺路 |
| 测试部｜功能/回归/测试支持 |  |  |  | 1 | 2 | 1.5 | 6 | 10.9 | 12.4 | 4.5 | 38.3 | 测试从 04/06 介入，05/04-05/24 进入高峰 |
| 测试部｜准生产/上线验证 |  |  |  |  |  |  |  |  | 1 | 8.2 | 9.2 | 05/11-05/24 上线前验证和问题复盘集中出现 |
| 产品SBU｜需求/文档/对齐 |  | 1.1 | 0.4 |  |  |  |  |  |  | 1.2 | 2.7 | 早期需求评审后，05/18 又回到接口文档和会议串联 |

| 组别 | 活跃日期 | 主要内容消耗 | 工作性质 |
| --- | --- | --- | --- |
| 研发部-账户组 | 03/16-05/24 | 宝财通/二级商户与会员关系 34；结算/出款/清算链路 28；其他账户支持 23 | 开发/改造 76.2；验证/回归 21.5；上线/发布 5.6 |
| 研发部-支付组 | 03/30-05/24 | 退款/退回/垫资链路 27.7；交易/收单/订单改造 19.95；其他支付支持 9.3 | 开发/改造 40.8；验证/回归 13.8；CR/梳理/沟通 7.35 |
| 研发部-商业应用组 | 03/23-05/24 | 其他商业应用支持 18.2；接口/网关/联调对接 16.3；宝财通/商户入网与关系 12.4 | 开发/改造 31.7；验证/回归 13.3；修复/排查 8 |
| 研发部-通用服务组 | 04/13-05/24 | 数据/报表/查询支撑 9.8；配置/资源/环境支撑 4；通用服务支持 2 | 开发/改造 13.8；验证/回归 2；其他 1 |
| 测试部 | 04/06-05/24 | 其他测试支持 34.5；准生产/上线验证 8.2；测试环境功能/回归 3.8 | 验证/回归 47；其他 0.5 |


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

## Daily Code Output Snapshot

Daily figures use the 65-day local Git scan window from `2026-03-19` to `2026-05-22`. They are directional throughput indicators, not a quality score.

| 指标 | 总量 | 日均 | 说明 |
| --- | --- | --- | --- |
| Excel 业务项目新增 | +70,204 行 | 约 +1,080 行/天 | Workbook project baseline; shows single-day output speed is high. |
| Excel 业务项目净增 | +51,271 行 | 约 +789 行/天 | New minus deleted code in workbook-selected project scope. |
| 本地 Git 全量提交 | 746 次 | 约 11.5 次/天 | Includes merge commits and branch flow. |
| 本地 Git 非 Merge 提交 | 450 次 | 约 6.9 次/天 | Closer to coding, fixing, refactor, docs/CR activity. |
| 本地 Git 源码净增 | +48,729 行 | 约 +750 行/天 | Local source-like suffix scan; differs from workbook line-count rules. |
| AI/规范化候选提交 | 141 次 | 约 2.2 次/天 | Proxy indicator, not definitive authorship. |
| AI/规范化候选新增 | +19,743 行 | 约 +304 行/天 | Proxy output volume under convention-based classification. |

## AI / Human-Review Boundary Signals

| 领域/项目 | AI/规范化候选占比 | 可读结论 | 边界 |
| --- | --- | --- | --- |
| 开户/客户关系类：mandao-customer | 75 / 110 非 Merge = 68.2% | 边界相对清晰的开户、客户关系出码自动化信号较高。 | Proxy indicator; not definitive AI authorship. |
| cm-post | 6 / 6 非 Merge = 100% | 小范围功能补齐也呈现高规范化候选占比。 | Sample small; should not be overgeneralized. |
| 清结算主干：cm-settle | 2 / 149 非 Merge = 1.3% | 清结算主干仍主要依赖人工处理和复核。 | cm-settle includes many branch/optimization/CR flows. |
| clearing-trade | 12 / 13 非 Merge = 92.3%; fix/refactor 4 / 13 = 30.8% | 即使候选占比高，资金处理、账户类型和空指针仍需要强人工复核。 | High-risk clearing/trade logic; replacement rate does not remove review responsibility. |

## Test Right-Shift Signal

| 口径 | 数值 | 说明 |
| --- | --- | --- |
| 测试部总投入 | 47.5 人日 | Group investment baseline. |
| 05/04-05/24 测试相关投入 | 37.0 人日 | Functional/regression support 27.8 + pre-production/launch validation 9.2. |
| 后三周占测试总量 | 77.9% | Shows testing and validation were heavily right-shifted into the late delivery window. |

## Interface Scope Supplement

This is a user-provided review supplement for the H5 conclusion layer, not an independently extracted workbook field.

| 指标 | 数值 | 管理含义 |
| --- | --- | --- |
| 新增内部接口 | 10 | Scope is broad enough to create cross-system coordination and regression pressure. |
| 新增对外接口 | 8 | External contract changes require version ownership, not only interface documentation. |
| API Fox 管理边界 | Existing API Fox management did not prevent an external-interface version-management blind spot | API documentation exists, but external version governance still needs explicit review and release gating. |

## Git AI/Rework Signal Snapshot

| 指标 | 数值 | 说明 |
| --- | --- | --- |
| 本地 Git 总提交 | 746 | `/mnt/d` 相关仓库全分支扫描，2026-03-19 to 2026-05-22 |
| Merge 提交 | 296 | 反映多分支合入、test/uat/master 流转和主干稳定动作 |
| 非 Merge 提交 | 450 | 更接近实际编码、修复、重构、文档/CR 动作 |
| AI/规范化候选 | 141 | feat 41, fix 25, refactor 9, docs 62, chore/style 4；提交格式代理指标，不证明作者身份 |
| 返工/重构信号 | 97 | 标题含 fix、优化、调整、修复、问题、CR、审查、重构等 |
| 分账/账户主题返工信号 | 34 | 返工信号中命中分账、账户、接收户、宝财通、退款等关键词 |

| 项目 | 总提交 | Merge/非Merge | 源码行 | AI/规范化候选 | fix/refactor | 返工信号 |
| --- | --- | --- | --- | --- | --- | --- |
| cm-settle | 227 | 78 / 149 | +13,495 / -2,492 | 2 | 0 / 0 | 28 |
| mandao-customer | 130 | 20 / 110 | +22,451 / -12,934 | 75 | 5 / 3 | 14 |
| auxiliary-trade | 338 | 174 / 164 | +7,533 / -1,278 | 45 | 17 / 5 | 47 |
| clearing-trade | 23 | 10 / 13 | +3,465 / -274 | 12 | 3 / 1 | 6 |
| cm-post | 14 | 8 / 6 | +1,104 / -37 | 6 | 0 / 0 | 1 |
| clearing-manager | 10 | 6 / 4 | +628 / -32 | 1 | 0 / 0 | 0 |

## Git Repair Fishbone Evidence

The H5 uses a project-based fishbone view instead of a flat timeline. The fishbone keeps the same Git evidence but groups it by repository so the reader can see where post-code-generation effort was consumed.

| 项目 | 时间 | Git 证据 | 研发消耗点 |
| --- | --- | --- | --- |
| cm-settle | 04-10 - 05-21 | 未结算明细/目标账户；多次代码优化/逻辑优化/自主结算代码优化；分账接收户下发传代理商 id 多次提交和 test 合入；docs(cr) 代码评审报告 | 清结算入口补齐、自主结算重构、代理商 ID 下发、CR 与主干稳定 |
| auxiliary-trade | 04-21 - 05-21 | 主动建单退款 fix；RCYW-17140 特约商户接口请求方式和字段校验 fix；RCYW-17224 连续 fix 自主结算提现、商户 ID 类型转换、缺失字段、订单号处理、余额查询账户类型；RCYW-17343/17224 多次合入 master_springboot | 退款、字段校验、提现补偿、账户类型、master 合入 |
| mandao-customer | 05-11 - 05-21 | transaction type、代理关系控制、代理商配置 refactor；fix 新特约关系查询、终端密钥类型 | 会员/代理关系、客户关系查询、类型兼容、规范化提交后的关系边界修复 |
| clearing-trade | 04-10 - 05-20 | 新增分账接收户退款未结算；fix 账户类型异常、fix 分账接收户资金处理及空指针校验；refactor 移除未使用退款待结算状态更新；fix 费用账户 ID 空指针 | 分账接收户退款、账户类型、资金处理、空指针、退款状态重构 |
| cm-post / clearing-manager | 04-10 - 05-21 | cm-post 支持退款未结算目标账户；clearing-manager 添加待分账户和分账接收户枚举；管理侧主干合入 | 退款目标账户、枚举兼容、跨系统联调入口 |

Fishbone management buckets:

- 业务链路补齐：未结算、退款、目标账户、分账接收户。
- 出码后重构：代码优化、refactor、字段校验、类型转换。
- 测试暴露修复：空指针、账户类型、查询关系、缺失字段。
- 主干/发布稳定：master 合入、test 合入、CR 报告、上线前修复。

## Evidence Boundary

- `其他独立任务工单` has no weekly date field, so it is not added to the weekly curve.
- `account-book-query` local mapping is not confirmed; both `/mnt/d/cloud/account-query` and `/mnt/d/whale/account-query` had no matching commits in the scan window.
- Local Git stats and workbook stats differ because workbook likely uses business-selected projects and line-count rules, while local audit counts source-like file suffixes from local repositories.
