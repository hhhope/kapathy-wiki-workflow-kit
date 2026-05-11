---
title: 现状
type: source
source_path: inbox/nirvana/现状.png
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

# 现状

## Source Metadata

- Source system: inbox
- Source class: architecture image
- Ownership hint: Nirvana 现状产品/系统分布图
- Sync state: manual visual capture
- Intake confidence: medium

## 中文摘要

这张图是当前产品与系统分布现状，对比多个产品线的入口、核心服务、会员/账户/清结算、计费和渠道承接。

覆盖产品线：

- 协议支付：`cutpayment`，包含网关入口、协议支付、协议支付分账、新代收、组合支付、双指令、合并支付、双层验签。
- 网银：`trade-neptune/fi-merchantgate`、`fi-service`，包含网银入口、网银支付、网银充值、订单支付、网银组合支付、网银查询、通知清算、通知商户。
- 聚合：`aggregate-api`、`aggregate-prod`、`unify-pay`，包含流量分发、网关入口、聚合收单、聚合分账、退款、支付、通知清算。
- 慧收钱：`hsq-api-gateway`、`hsq-tradecenter-core`，包含网关入口、移企付、微企付等。
- 宝财通：`cloud-product`，包含网关入口、开户进件、绑卡、充值、提现、鉴权、分账。
- 银企云：`yqy-gateway`、`yqy-tradecenter`，包含网关入口、协议支付、协议支付分账、余额支付、双指令、对公代扣、通知清算、签约绑卡、收单支付。
- 多渠道收款：`billtone/account-gateway`、`ytq-trade`，包含网关入口、开户进件、绑卡、充值、提现、销户、分账、鉴权、调拨、冻结/解冻、分润。

横向公共层：

- 会员：`ma-query/mandao-customer` 等，承接特约商户会员、慧收钱会员、银企云会员。
- 账户：`ma-account`、`ma-account/hsq-account`、`mandao-account-book`、`cloud-member/cloud-account`、`yqy-account`。
- 清结算：协议支付、慧收钱、宝财通、银企云等多条清结算链路。
- 计费/产品：`bill-cache`、`clearing-share`、`beanfit`、`cloud-billing`、`agreement` 等承接计费、分润策略和产品计费。
- 渠道：网联、银联、支付宝、微信、宝付、工行/建行/苏商/华通等银行渠道。

## Reused By

- 待关联到 Nirvana 现状对照、产品服务拆分和迁移差异分析页。
