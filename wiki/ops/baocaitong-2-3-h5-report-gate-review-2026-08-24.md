# 宝财通 2.0 → 3.0 联合评审 H5 Gate Review

Date: 2026-08-24
Status: `PASS — local review draft; business confirmation items remain visible`
Target: `wiki/reports/baocaitong-2-3-review-h5.html`

## Article Intent Contract

- Reader: 产品经理、研发、测试，以及参与资金链路评审的合规相关人员。
- Reader job: 在一次评审中建立共同的账户与资金流模型，明确 2.0 到 3.0 的变化、实现影响和需决策问题。
- Main line: 现状 → 方案演进 → 推荐方案 → 改造范围 → 风险与待确认 → 评审结论。
- Non-goals: 不扩写截图外收益；不伪造接口或字段；不把低清内容补成确定规则。
- User-owned judgment: 3.0 为推荐方向、2.0 为对照；交付形态为产品与研发联合评审 H5。
- Agent-allowed work: 结构化转写、流程重绘、差异矩阵、交互和验证。

## Source-to-Screen Map

| 来源 | 页面位置 | 用途 |
|---|---|---|
| `01-main-comparison.png` 左上 | 2.0 现状 | 账户关系、收单、分账、提现 |
| `01-main-comparison.png` 右上 | 3.0 目标 | 代付商户号与升级链路 |
| `01-main-comparison.png` 下部 | 差异、规则、改造项 | 开户、分账、退款、调账等 |
| `02-mode-options.png` 顶部 | 方案演进 | 保留电子户备选模式边界 |
| `02-mode-options.png` 中下部 | 风险与待确认 | 历史兼容、账户与余额边界 |

全部事实映射见 `wiki/sources/baocaitong-2-3-plan-source-2026-08-24.md` 和 `content.json` 的 F-001 至 F-044。

## Reference Output Shape

Selected shape: 评审决策型长滚动 H5。页面保留已确认的九段结构，不替换为截图画廊、PPT 克隆或纯规格文档。流程图承担账户与资金关系；表格承担差异；折叠区承担规则；问题卡承担决策缺口。

## Section And Paragraph Drift Review

| Section | Decision | Reason |
|---|---|---|
| 封面与核心变化 | retain | 建立共同阅读目标 |
| 2.0 / 3.0 流程 | rewrite | 用一致视觉语法重绘，不贴低清图 |
| 差异矩阵 | retain | 同时呈现产品与研发影响 |
| 七项改造 | compress | 首屏摘要，细节折叠 |
| 业务规则 | compress | 结论优先，条件展开 |
| 风险与待确认 | retain | 不把转写不确定性藏入正文 |
| 评审结论 | retain | 判断由评审人填写 |

## Judgment Ownership

PASS. 页面明确显示 3.0 是用户确认的推荐方向，但没有把“降低复杂度”“提升效率”或“合规通过”写成已验证结论。所有 `needs_confirmation` 内容进入橙色待确认区；H5 不自动生成最终业务判断。

## Visual QA

- Static visual contract: PASS（设计 tokens、四类流程语义、响应式和减弱动画规则已验证）。
- Desktop 1440 × 1000: PASS；9 个章节完整，页面无非预期横向溢出。
- Mobile 390 × 844: PASS；流程单列堆叠、正文 15px、顶部章节导航可见，无页面级横向溢出。
- Interactions: PASS；2.0 单看、3.0 单看、并排对照、负责人筛选、节点详情和阅读进度均工作。
- Console: PASS；0 console errors，0 page errors。
- Evidence: `.codex-tmp/baocaitong-2-3-h5-review/desktop-1440.png`、`mobile-390.png`、`qa.json`。
- Runner: 本地 Edge 无头真实页面验收。Browser 插件运行时因 Node kernel assets 路径错误不可用，改用同机 Edge + 本地 Playwright 执行；未改变被测页面或验收尺寸。

## Security And Delivery Boundary

- Local resources only: PASS。
- External loading dependencies: none detected。
- Credentials, private URLs, production identifiers: none introduced。
- No Feishu sync。
- No publication or external write。

## Residual Risks

1. 截图小字号导致部分接口字段、账户名称和校验公式仍需原始需求文档确认。
2. H5 的流程图表达用于评审沟通，不替代账务、合规或接口权威文档。
3. 历史订单、退款资金来源和跨主体调账仍是阻塞最终业务结论的开放问题。
4. 页面已通过本地 Edge 桌面与手机验收；最终业务批准仍取决于截图中标记为待确认的权威字段。