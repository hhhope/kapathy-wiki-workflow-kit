---
title: 清算的内容
type: source
layer: sources
source_path: inbox/nirvana/清算的内容.png
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

# 清算的内容

## Source Metadata

- Source system: inbox
- Source class: architecture image
- Ownership hint: 账户/清结算链路说明
- Sync state: manual visual capture
- Intake confidence: medium

## 中文摘要

这张图展示账户应用分层中的开户与动账链路，重点是 CDP 与 `fi-hub` 到账户、清算相关服务的调用关系。

主要分层：

- 业务系统：CDP 负责开户，`fi-hub` 负责动账。
- 账户服务：CDP 下接 `account-gateway`，`fi-hub` 下接 `facade`。
- 账户布置：涉及 `clearing-trade`、`yqy-clear`、`account-front-hsq`。
- 账户核心：涉及 `ma-service`、`cloud-account`、`yqy-account`、`mandao-account-book`、`account-hsq`。
- 数据处理：涉及 `clearing-data-deal`、`cloud-account-task`、`yqy-async-account`、`account-hsq-asy`。

图中用不同颜色区分开户链路和动账链路：开户链路从 CDP 进入 `account-gateway` 后分发到账户核心和清算相关服务；动账链路从 `fi-hub` 进入 `facade` 后连接清算、账户前置和账户核心服务。

## Reused By

- 待关联到清结算、账户中心或协议支付分账方案页。
