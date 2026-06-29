---
title: 涅槃零售商户接入统一网关接口迁移视图 2026-06-29
type: source
layer: sources
source_path: inbox/nirvana/preview .html
source_type: report
language: zh-CN
domain: nirvana-project
audience: project
knowledge_level: working
period: 2026-w27
source_links: []
status: draft
updated_at: 2026-06-29
ai_generated: true
---

# 涅槃零售商户接入统一网关接口迁移视图 2026-06-29

## Source Metadata

- Source system: inbox manual drop
- Source class: weekly html preview plus interface migration materials
- Primary output: `inbox/nirvana/preview .html`
- Supporting files:
  - `inbox/nirvana/账户组对外接口文档汇总.xlsx`
  - `inbox/nirvana/聚合业务接入统一网关接口梳理.xlsx`
  - `inbox/nirvana/涅槃焕新周报.xlsx`
  - `wiki/sources/nirvana-协议支付涅槃需求文档.md`
- Intake confidence: medium

## 中文摘要

本次材料把原 `preview .html` 从 2026-04-13 的项目全景图，调整为面向 `Q4 前解决零售商户接入难` 的周推进视图。

核心变化：

- 目标从单点项目状态汇报，改为零售商户接入攻坚。
- `Q4 前` 按 `2026-09-30 前` 处理；用户原文 `20260931` 不是有效日期。
- 当前主线改为 `统一会员入网 + 统一网关 + 多渠道交易 + 结算/分账/查询/商户服务承接`。
- 周报口径显示：协议支付与一键绑卡相关 `12 个接口` 完成迁移开发，预计下周一提测。
- 周报口径显示：聚合 `7 个接口` 完成迁移开发，仍剩余 `50 个接口`。
- `聚合业务接入统一网关接口梳理.xlsx` 原始台账包含 `60` 条接口记录，覆盖聚合网关和商户服务。
- `账户组对外接口文档汇总.xlsx` 覆盖结算、对账、老前置、资金付款、账户网关、宝财通 2.0/3.0、宝户通等对外接口入口。

## 本次输出调整

`preview .html` 调整为三段：

1. `Q4 前交付路径`：从 2026-06-29 所在周到 2026-09-30 前，拆成里程碑重排、协议支付/一键绑卡、聚合支付、结算/账户、会员入网/电子户、慧收钱/商户服务/代理商。
2. `零售商户接入能力地图`：按入网、电子户、交易、结算、分账、数据查询、商户服务、代理商八类诉求组织。
3. `接口迁移与验证口径`：把协议支付 12 个接口、聚合接口、结算与账户接口、ASL/Nacos、开发者站点、产品方案评审分别落到验证动作。

## 证据边界

- 本页不确认未评审的协议支付对接方式和退款产品方案。
- 本页不把 `开发完成` 视为 `可对客`。
- 聚合接口数量同时保留周报口径和台账口径：周报说 `7 个完成、剩余 50 个`，台账实际抽取到 `60` 条接口记录。

## Reused By

- [涅槃零售商户接入统一网关接口迁移 intake 2026-06-29](../ops/nirvana-retail-gateway-interface-migration-intake-2026-06-29.md)

