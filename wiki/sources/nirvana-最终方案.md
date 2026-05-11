---
title: 最终方案
type: source
source_path: inbox/nirvana/最终方案.png
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

# 最终方案

## Source Metadata

- Source system: inbox
- Source class: architecture image
- Ownership hint: Nirvana 最终产品/服务边界方案
- Sync state: manual visual capture
- Intake confidence: medium

## 中文摘要

这张图在“优化后图示”的基础上补充了更完整的最终产品边界，除商户接入、统一网关、解决方案、收单/代付/账户核心、渠道服务和下家渠道外，还加入右侧风控与产品开通能力。

关键新增区域：

- 产品层：H5、API、商户入网及产品开通 BM/AD。
- CDP 流程与权限管控：新会员入网、会员流程管控、产品签约、产品货架。
- MA 会员信息：商户分类、商户层级、商户关系、客户信息、客户资产、账户关系。
- 账户中心：个人账户、银行电子户账户、备付金账户、记账账户。
- 清结算：清分、结算、分润、计费、收费。
- 认证渠道：OCR、企查查、风控名单信息核验、严重违法、企业四要素、企亚经营异常、简易注销、法人三要素、法大大签约、服务受益人两要素。

收单核心扩展：

- `fi-hub` 增加供转、失败重复支付、移企付、聚分期等能力。
- `fo-hub`/`fo-route` 承接联合放款、委托付款、充值代付、小额鉴权、代付路由。
- `account-hub` 承接充转提、开户/冻结。

## Reused By

- 待关联到 Nirvana 最终方案说明和产品上架范围页。
