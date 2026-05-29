# embedded-account-phase1

## Why

This draft was generated from requirements case `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md` after the requirements hard gate passed.

## What Changes

- Capability: embedded-account-phase1
- Confirmed domain: account
- Implementation requires user review before planning or coding.

## Requirement Trace
- US-001 -> AF-001, AF-002, AF-003, AF-004, AF-005, AF-020, AF-023, AF-024: role=financial_customer 商户希望通过 API 为终端用户开立嵌入式账户，并在开户流程内完成首卡绑定。 (为订阅支付场景建立可用的账户与首张可支付银行卡基础。)
- US-001 -> AF-001: 终端用户正常开户 (acceptance trace)
- US-001 -> AF-002: 首卡绑定失败导致开户失败 (acceptance trace)
- US-001 -> AF-003: 同一商户用户重复开户 (acceptance trace)
- US-001 -> AF-004: 历史开户处理中再次开户 (acceptance trace)
- US-001 -> AF-005: 历史开户失败重新开户 (acceptance trace)
- US-001 -> AF-020: 开户受理后异步通知商户 (acceptance trace)
- US-001 -> AF-023: 异步通知失败后主动查询 (acceptance trace)
- US-001 -> AF-024: 开户命中正常账户 (acceptance trace)
- US-002 -> AF-001, AF-006, AF-007, AF-021: role=retail_customer 终端用户希望在商户引导下完成首卡绑定或追加绑卡。 (后续账户支付可以使用已绑定银行卡完成扣款。)
- US-002 -> AF-001: 终端用户正常开户 (acceptance trace)
- US-002 -> AF-006: 开户后追加绑卡成功 (acceptance trace)
- US-002 -> AF-007: 多卡识别后用户选择绑卡 (acceptance trace)
- US-002 -> AF-021: 绑卡受理后异步通知商户 (acceptance trace)
- US-003 -> AF-006, AF-007, AF-021, AF-023, AF-025: role=financial_customer 商户希望在账户开户成功后为终端用户追加绑定银行卡。 (提高账户支付成功率并支持多卡支付准备。)
- US-003 -> AF-006: 开户后追加绑卡成功 (acceptance trace)
- US-003 -> AF-007: 多卡识别后用户选择绑卡 (acceptance trace)
- US-003 -> AF-021: 绑卡受理后异步通知商户 (acceptance trace)
- US-003 -> AF-023: 异步通知失败后主动查询 (acceptance trace)
- US-003 -> AF-025: 商户未开通一键绑卡权限 (acceptance trace)
- US-004 -> AF-008, AF-009, AF-016, AF-017, AF-025: role=financial_customer 商户希望解除账户与银行卡之间的绑定关系。 (已解绑卡不再参与账户支付或订阅自动扣款。)
- US-004 -> AF-008: 解绑银行卡关系成功 (acceptance trace)
- US-004 -> AF-009: 解绑后卡不可继续支付 (acceptance trace)
- US-004 -> AF-016: 已解绑卡在自动扣款中被跳过 (acceptance trace)
- US-004 -> AF-017: 所有卡不可用时支付失败 (acceptance trace)
- US-004 -> AF-025: 商户未开通一键绑卡权限 (acceptance trace)
- US-005 -> AF-010, AF-011, AF-026: role=financial_customer 商户希望在订阅支付中显式选择账户支付。 (订阅支付可以接入嵌入式账户能力且不发生自动支付方式路由。)
- US-005 -> AF-010: 订阅支付选择账户支付 (acceptance trace)
- US-005 -> AF-011: 账户支付成功 (acceptance trace)
- US-005 -> AF-026: 商户未开通协议支付权限 (acceptance trace)
- US-006 -> AF-012, AF-013, AF-014, AF-015, AF-016, AF-017: role=system_actor 嵌入式账户前置希望按已绑卡优先级轮询发起快捷支付。 (在高优先级卡明确失败后可以继续尝试低优先级卡。)
- US-006 -> AF-012: 按优先级先扣高优先级卡 (acceptance trace)
- US-006 -> AF-013: 高优先级卡失败切换低优先级卡 (acceptance trace)
- US-006 -> AF-014: 支付结果未明禁止直接切卡 (acceptance trace)
- US-006 -> AF-015: 银行卡查询超过上限 (acceptance trace)
- US-006 -> AF-016: 已解绑卡在自动扣款中被跳过 (acceptance trace)
- US-006 -> AF-017: 所有卡不可用时支付失败 (acceptance trace)
- US-007 -> AF-014, AF-018, AF-019, AF-022, AF-023, AF-026: role=system_actor 嵌入式账户前置希望在支付异常或结果未明时通过查单与补偿收敛结果。 (保证单笔支付只有一个唯一最终状态且不重复扣款。)
- US-007 -> AF-014: 支付结果未明禁止直接切卡 (acceptance trace)
- US-007 -> AF-018: 支付异常后查询收敛结果 (acceptance trace)
- US-007 -> AF-019: 异常补偿不重复支付 (acceptance trace)
- US-007 -> AF-022: 支付处理中异步通知订阅产品 (acceptance trace)
- US-007 -> AF-023: 异步通知失败后主动查询 (acceptance trace)
- US-007 -> AF-026: 商户未开通协议支付权限 (acceptance trace)

## Out of Scope

- Automatic implementation after draft creation.
