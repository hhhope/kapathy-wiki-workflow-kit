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
- Feishu source/trunk URL: `https://my.feishu.cn/docx/Q5TCdjeIXoKO1DxuTYNc5Iasnuf`
- This turn's operation: updated the repo draft as the Feishu access-guide trunk candidate.
- Feishu write boundary: no Feishu update or copy was performed in this turn; writing back requires explicit confirmation of overwrite versus new copy.

## Article Intent Contract

| Field | Contract |
|---|---|
| Reader | 入网、产品、接入、运营、技术同事 |
| Reader decision or action | 明确代运营商户开户、`144 + 421` 一次性产品开通、421 补充资料、分账接收方进件绑定、交易验证和结算核对的执行口径。 |
| Main line | 以飞书原接入指引为主干：`144 + 421` 一次性产品开通，两个产品的 `productModelId` 均为 `10370560005`；421 补充资料不要求 `bankType` 和技术支持字段，分账类产品补充附件重点选择 `9915999`。 |
| Non-goals | 不替代正式接口文档，不展示敏感身份信息，不确认最终合规准入资料，不直接写回飞书。 |
| User-owned judgments | 合规资料最终必传清单、协议授权表述、分账比例、是否复用会员创建/修改阶段已上传资料、是否覆盖飞书原文档。 |
| Agent-allowed work | 读取飞书主干，结合用户补充口径，整理可继续迭代的接入指引正文、验收清单、常见错误和待确认事项。 |

## Source Use Map

| Source | Used for | Boundary |
|---|---|---|
| Feishu doc `Q5TCdjeIXoKO1DxuTYNc5Iasnuf` fetched via `lark-cli docs +fetch` | 确认主干标题、`144 + 421` 一次性产品开通、接口范围、交易验证、结算说明、验收清单和常见错误结构。 | 原文中 `bankType` 和技术支持字段已被新口径修正，不照搬旧字段。 |
| 用户 2026-06-23 补充沟通口径 | 修正 421 是否传银行类型、技术支持字段、补充资料上传条件、`9915999` 文件类型选择。 | 合规准入资料仍需合规/姚世杰确认。 |
| `wiki/sources/agent-merchant-opening-product-144-421-2026-06-15.md` | 保留本地样例来源、敏感信息不复制原则、产品开通响应判断依据。 | 不复制 PII、文件 UUID、签名报文和完整请求。 |

## Section Drift Review

| Section | Objective | Result |
|---|---|---|
| 接入目标 | 保留飞书主干的一次性开通和完整交易验证链路。 | PASS |
| 涉及接口 | 覆盖开户、开产品、绑卡扣款、接收方进件绑定、分账、查询、结算。 | PASS |
| 接入流程 | 从开户到结算按执行顺序组织。 | PASS |
| 开户资料 | 纳入代扣代运营开户资料 1 至 6，并标明合规确认边界。 | PASS |
| 一次性开通 | 保留 `144 + 421` 同请求、`productModelId=10370560005` 主干。 | PASS |
| 421 扩展信息 | 删除旧的 `bankType=HT` 和技术支持必传表达，保留分账比例和 `9915999` 条件口径。 | PASS |
| 补充资料规则 | 明确已上传不重复、未上传且开分账类产品需补传、不开分账类产品通常不需产品补充材料。 | PASS |
| 验收和错误 | 加入 `9915999`、不传 `bankType`、不收技术支持电话、避免重复上传的检查项。 | PASS |
| 待确认 | 将合规资料、授权表述、资料复用、分账比例、绑定策略列为用户/业务确认项。 | PASS |

## Gate Results

| Gate | Result |
|---|---|
| Article intent | PASS |
| Reference output shape | PASS for repo draft: Feishu trunk was fetched and its access-guide shape was preserved while updating incorrect 421 field口径。 |
| Voice quality | PASS |
| Judgment ownership | PASS: 未替用户确认合规材料最终清单、分账比例或飞书覆盖策略。 |
| Publish gate | PARTIAL: repo draft updated; Feishu write intentionally not performed without overwrite/new-copy confirmation。 |

## Residual Risks

1. 合规准入资料 2 至 6 的最终必传清单仍需合规/姚世杰确认。
2. 委托划扣授权书的协议位置和法人授权表述仍需合规或法务确认。
3. 资料已在会员创建/修改阶段上传时，产品开通审核是否可直接复用，需要产品/运营确认。
4. 本次未写回飞书；飞书正文仍可能保留旧的 `bankType` 和技术支持字段，需用户确认后再覆盖或复制新文档。

## Verification Evidence

| Item | Evidence |
|---|---|
| Feishu read | `lark-cli docs +fetch --doc https://my.feishu.cn/docx/Q5TCdjeIXoKO1DxuTYNc5Iasnuf --format pretty` returned the source trunk title and body. |
| Repo source update | `wiki/sources/agent-merchant-opening-product-144-421-2026-06-15.md` records the 2026-06-23 supplemental口径。 |
| Repo draft update | `wiki/reports/agent-merchant-144-421-access-guide.md` now uses the Feishu trunk and updated 421 supplement rules. |
| Feishu write | Not executed in this turn. |
