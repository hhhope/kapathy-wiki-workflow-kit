---
title: 协议支付涅槃需求文档
type: source
source_path: inbox/nirvana/协议支付涅槃需求文档.docx
source_type: attachment
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

# 协议支付涅槃需求文档

## Source Metadata

- Source system: inbox
- Source class: supporting attachment
- Ownership hint: Nirvana / 协议支付产品梳理
- Sync state: manual source capture
- Intake confidence: medium

## Audience Decision

- Source pages are usually for `self` or `project`, not `team`.
- Keep `knowledge_level: working` because source pages are evidence, not promoted team knowledge.

## 中文摘要

这份文档是协议支付产品能力清单和迁移需求说明，覆盖绑卡、支付、查询、对账、回单、退款、撞库、分账、失败计费、签约支付/新代收/路由重发等能力。

核心产品范围：

- 绑卡：预绑卡/确认绑卡、一键绑卡、解绑银行卡、绑卡流水查询、绑卡结果查询。
- 支付：预支付/确认支付、直接支付、组合支付、交易中签约。
- 交易后链路：支付结果查询、支付对账、支付回单、退款。
- 迁移与扩展：撞库、协议支付用于分账、失败计费、签约支付、新代收、路由重发。

关键业务规则：

- 确认绑卡短信验证码输错 5 次失效。
- 预支付短信 5 分钟内有效；5 分钟内确认支付时验证码最多验证 5 次。
- 交易中签约场景中，确认绑卡短信验证码半小时内输错 5 次失效。
- 直接支付入参包含商户号、门店编号、商户订单号、协议号、交易金额等；出参包含宝付订单号、交易状态、成功/失败时间、失败原因、渠道订单号等。
- 退款支持部分退款和全额退款，BM 发起退款需要填写退款方式、退款金额和退款原因；若商户开启退款审核权限，BM 发起退款需要审核。

需要重点复用的迁移线索：

- BM 查询需要新增协议支付交易类型、对方名称/账户半脱敏展示、明细导出、退款金额字段。
- 对账文件字段扩展到支付、退款、分账、手续费、订单时间、清算日期等多维信息。
- 分账场景支持收单后进入待分账户，后续发起分账；也支持收单时传分账信息并请求分账系统。
- 撞库用于商户已有四要素但无法重新绑卡的迁移场景，支持 MD5 和 RSA。
- 文档末尾指向协议支付老 AD 迁移菜单梳理、异步通知参数整理等外部表格，后续如进入实施需要补齐链接可访问性和字段对照。

## English Notes



## Reused By

- `wiki/ops/nirvana-协议支付涅槃需求文档-intake.md`
