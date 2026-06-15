---
layer: ops
domain: account-clearing
ops_area: report-quality
canonical_object: agent-merchant-144-421-access-guide
artifact_type: report-gate-review
---

# 代运营商户 144 + 421 接入指引 gate review

## Review Target

- Target: `wiki/reports/agent-merchant-144-421-access-guide.md`
- Source: `wiki/sources/agent-merchant-opening-product-144-421-2026-06-15.md`
- Destination: new Feishu document.
- Feishu URL: `https://www.feishu.cn/docx/Q5TCdjeIXoKO1DxuTYNc5Iasnuf`
- Non-scope: 不直接同步飞书，不确认生产费率，不确认最终产品货架，不提供完整接口字段字典。

## Article Intent Contract

| Field | Contract |
|---|---|
| Reader | 入网、产品、接入、运营、技术同事 |
| Reader decision or action | 明确该代理商开通 144 和 421 时的接口顺序、货架差异、分账接收方进件与绑定要求。 |
| Main line | 该代理商不能把 144 和 421 混在一次普通产品开通里；144 按协议支付货架开，421 按 `10370560005` 单独开，分账前必须完成接收方绑定关系。 |
| Non-goals | 不复制完整请求报文，不展示敏感身份信息，不替代接口文档，不替代生产参数审批。 |
| User-owned judgments | 正式货架 ID、费率、生效时间、资质文件类型、分账比例、是否同步绑定关系。 |
| Agent-allowed work | 基于本地样例和用户给出的接口清单，整理飞书式接入指引、流程、关键字段、验收清单和待确认事项。 |

## Source Use Map

| Source | Used for | Boundary |
|---|---|---|
| `C:\Users\yan\Desktop\1\开户及产品开通.txt` | 提取开户返回 `uid`、144/421 产品开通关键参数、421 成功响应和扩展字段。 | 不复制 PII、文件 UUID、签名报文和完整请求。 |
| 用户提供的接口清单 | 确定入网、开货架、分账接收方进件、绑定代运营商户的流程范围。 | 在线文档正文当前未读取到，字段细节以正式接口文档为准。 |
| Feishu 链接 | 作为“类似飞书”输出形态参考。 | 当前工具未取到正文，不声称已读取原文结构。 |

## Section Drift Review

| Section | Objective | Result |
|---|---|---|
| 接入目标 | 说明本次不是普通开户，而是 144 + 421 + 分账接收方关系链路。 | PASS |
| 涉及接口 | 保留用户给出的接口列表和用途。 | PASS |
| 接入流程 | 给出开户、开 144、开 421、接收方进件、关系绑定的顺序。 | PASS |
| 144 开通 | 强调协议支付货架，不混入 10370560005。 | PASS |
| 421 开通 | 强调 `productModelId=10370560005` 和扩展字段。 | PASS |
| 分账接收方 | 强调进件不等于可分账，必须绑定关系。 | PASS |
| 验收和错误 | 给接入方可执行检查项。 | PASS |
| 待确认 | 保留产品货架、费率、分账比例和绑定策略的不确定性。 | PASS |

## Gate Results

| Gate | Result |
|---|---|
| Article intent | PASS |
| Reference output shape | PARTIAL: Feishu source link未读取到正文，但已按用户要求输出可贴飞书的接入指引结构。 |
| Voice quality | PASS |
| Judgment ownership | PASS: 未替用户确认生产货架、费率和绑定策略。 |
| Publish gate | PASS for requested Feishu creation: user explicitly asked “直接写飞书”, and a new document was created rather than modifying the referenced Yeepay manual. |

## Residual Risks

1. 在线 baofu 文档和飞书原文当前未通过工具读取到正文，正式字段约束仍需以接口文档为准。
2. `M2503000004` 来自本地样例，正式 144 协议支付货架需产品侧确认。
3. `shareProdRatio`、`bankType=HT`、资质文件类型等生产口径需产品/技术确认。

## Feishu Write Evidence

| Item | Evidence |
|---|---|
| Operation | Created new Feishu document, did not edit the existing Yeepay manual. |
| Title | `代运营商户开通 144 + 421 产品接入指引` |
| URL | `https://www.feishu.cn/docx/Q5TCdjeIXoKO1DxuTYNc5Iasnuf` |
| Read-back | `docs +fetch` returned the title, interface list, flow section, 144/421 sections, receiver onboarding, binding, acceptance checklist, common errors, and pending confirmations. |
