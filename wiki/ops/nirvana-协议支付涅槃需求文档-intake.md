---
title: 协议支付涅槃需求文档
type: intake
language: zh-CN
source_path: inbox/nirvana/协议支付涅槃需求文档.docx
source_type: attachment
audience: self
knowledge_level: working
layer: ops
domain: nirvana
ops_area: source-intake
canonical_object: nirvana-协议支付涅槃需求文档
artifact_type: intake
period: evergreen
confidence: medium
status: active
updated_at: 2026-05-11
ai_generated: true
related_sources:
  - ../sources/nirvana-协议支付涅槃需求文档.md
related_focus_threads: []
related_reminders: []
---

# 协议支付涅槃需求文档

## 输入摘要

协议支付需求文档已经具备可推进的产品范围和迁移线索：它不是普通附件，而是协议支付能力盘点、迁移菜单、BM/API 查询、退款、对账、分账和失败计费的需求输入。

## 输入类型判断

- 行为类型：产品需求归档 / 后续方案对齐输入
- 来源类型：supporting attachment
- 受众判断：self
- 当前置信度：medium

## 关键事项

- 绑卡链路需要覆盖预绑卡/确认绑卡、一键绑卡、解绑、绑卡流水查询和绑卡结果查询。
- 支付链路需要覆盖预支付确认支付、直接支付、组合支付、交易中签约。
- 交易管理需要覆盖支付查询、BM 明细、对账文件、回单下载、退款查询/审核/批量退款。
- 迁移能力需要关注撞库、分账、失败计费、签约支付、新代收和路由重发。
- 字段级工作集中在 BM 查询展示、对账文件字段、退款订单查询、异步通知参数和老 AD 迁移菜单。

## 建议关联

- 来源页：../sources/nirvana-协议支付涅槃需求文档.md
- 主线页：wiki/ops/nirvana-涅槃产品上架梳理-intake.md
- 提醒页：

## 待确认项

- 是否需要把协议支付迁移拆成接口字段对照、BM 菜单迁移、清结算/对账字段、退款流程四个执行包。
- 外部腾讯文档链接是否仍可访问，是否需要同步保存为 repo source。
- 当前文档中多处“接口不变”是否已有最终验收口径。

## English Notes
