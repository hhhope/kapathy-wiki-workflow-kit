---
title: 优化后图示
type: source
layer: sources
source_path: inbox/nirvana/优化后图示.png
source_type: image
language: zh-CN
domain: nirvana
audience: project
knowledge_level: working
period: evergreen
source_links: []
status: draft
updated_at: 2026-05-11
ai_generated: true
---

# 优化后图示

## Source Metadata

- Source system: inbox
- Source class: architecture image
- Ownership hint: Nirvana 产品/基础服务架构梳理
- Sync state: manual visual capture
- Intake confidence: medium

## 中文摘要

这张图展示协议支付/收单相关能力的优化后架构分层。

主要结构：

- 入口层：商户接入，提供 H5 和 API 两类入口。
- 统一网关：`api-gateway` 承接收单、代付；`protocol-notice-center` 承接收单通知、代付通知、分账通知。
- 解决方案层：`cutpayment`，包含双层验签、失败重复支付、合并支付、双指令、宝付代扣。
- 收单核心：`fi-hub`、`query-hub`、`fi-route`，承接组合支付、交易中签约、二次支付、协议支付、签约支付、新代收、订单支付、网银、聚合支付、交易分账、转账支付、线下打款等能力。
- 渠道服务：`cgwfi-paid-service` 负责绑卡/支付，`cgwfi-account-service` 负责退款/退款结果查询，`cgwfi-bank-order-service` 负责下家订单号生成/更新。
- 下家渠道：网联、银联、支付宝、微信、合利宝。

## Reused By

- 待关联到 Nirvana 架构演进或产品上架梳理页。
