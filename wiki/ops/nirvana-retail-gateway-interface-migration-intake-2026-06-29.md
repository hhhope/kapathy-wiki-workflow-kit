---
title: 涅槃零售商户接入统一网关接口迁移 intake 2026-06-29
type: intake
layer: ops
domain: nirvana-project
ops_area: source-intake
canonical_object: nirvana-retail-gateway-interface-migration
artifact_type: intake
language: zh-CN
source_path: inbox/nirvana/preview .html
source_type: report
audience: project
knowledge_level: working
period: 2026-w27
confidence: medium
status: draft
updated_at: 2026-06-29
ai_generated: true
related_sources:
  - ../sources/nirvana-retail-gateway-interface-migration-2026-06-29.md
  - ../sources/nirvana-协议支付涅槃需求文档.md
project_name: 涅槃
milestone: M2 统一网关与会员建设
weekly_status: active
drift_signal: high
codex_handoff_candidate: no
---

# 涅槃零售商户接入统一网关接口迁移 intake 2026-06-29

## 输入摘要

本次 intake 来自用户补充的 `inbox/nirvana` 接口材料、上周涅槃周报口径和零售商户接入目标。材料已经触发 `preview .html` 的内容调整。

## 本周进展

- 协议支付相关 `12 个接口` 完成迁移开发，预计下周一提测。
- 聚合 `7 个接口` 完成迁移开发，剩余 `50 个接口` 需要继续拆批。
- 涅槃账户防腐层 `ASL` 完成流量验证。
- 账户/结算口径已复核：结算 `2` 个接口，对账 `1` 个文件下载接口；账户 7 月聚焦冻结、解冻、待分账户、余额查询、收支明细查询、账单查询和对账管理。
- 宝财通按 `2.0` 方案支撑余额支付即可，`3.0` 本轮不迁移。
- `涅槃产品上架梳理0629.xlsx` 明确 `慧收钱网关迁移` 在 `2026-07-01` 至 `2026-07-30` 做接口集成。

## 偏移判断

- 原页面仍停留在 4 月项目全景图，不能承接当前 `Q4 前解决零售商户接入难` 的目标。
- M2 目标已从 `基础协议支付` 扩展为 `统一网关与会员建设`，需要用 `2026-09-30 前` 或 `2026-10-01` 修正无效日期 `20260931`。
- 当前推进重点不只是协议支付接口，而是要按产品门户能力对象组织：统一会员、快速入网、多渠道收款控台+API、新控台框架、产品货架模型、商户入网流程、直销模式业务支持、代销模式业务支持。
- 慧收钱不能放成 8 月后的后续排期；0629 排期显示它是 7 月已经在做的统一网关接口集成。
- 账户、结算、资金付款、宝财通 3.0 不能混写成一个“结算/账户接口迁移”主线；这种表达会误导为 Q4 前全量迁移。

## 当前风险

- 协议支付对接方式与退款产品方案未评审，负责人线索为任利利。
- 开发者站点仍缺接口梳理和对接指引，负责人线索为 yanpeng、caoyang。
- 聚合接口台账与周报口径需要冻结：周报说 `7 个完成、剩余 50 个`，台账抽取到 `60` 条接口记录。
- 4.0 账户、账户网关、资金付款、宝财通 2.0/3.0 的接口数量需要继续作为拆解依据，但页面交付承诺必须只写已确认范围。
- 瞭望塔本轮只验证到静态入口标题，登录态能力树未读取；页面采用 0629 表的里程碑能力对象来对齐。
- 复杂代理商、金融、二级户混合场景不能默认纳入 Q4 前首版。

## 下周动作

1. 完成涅槃里程碑调整，并把无效日期修正为可执行目标。
2. 完成协议支付迁移统一网关验证。
3. 完成网关 Nacos 准生产验证。
4. 按 `2026-07-01` 至 `2026-07-30` 的排期推进慧收钱网关迁移，不再把它作为后置事项表达。
5. 冻结聚合已完成接口名单和剩余接口拆批测试排期。
6. 冻结账户 7 月支持项、宝财通 2.0 余额支付和结算/对账接口清单，避免再次回到全量迁移表述。
7. 推动协议支付对接方式、退款产品方案、开发者站点对接指引评审。

## Codex 候选判断

- 当前判断：`no`
- 理由：这次主要是周报和预览页材料调整。后续如果产品方案评审、接口名单、验收口径冻结，可以升级为研发 handoff。

## 输出链接

- 来源页：[涅槃零售商户接入统一网关接口迁移视图 2026-06-29](../sources/nirvana-retail-gateway-interface-migration-2026-06-29.md)
- 预览页：`inbox/nirvana/preview .html`
