---
title: 代运营商户开户及产品开通样例材料
type: source
source_path: /mnt/c/Users/yan/Desktop/1/开户及产品开通.txt
source_type: local-note
language: zh-CN
layer: sources
domain: account-clearing
audience: project
knowledge_level: working
period: 2026
status: draft
updated_at: 2026-06-15
ai_generated: true
---

# 代运营商户开户及产品开通样例材料

## Source Note

原始材料为本地文本 `C:\Users\yan\Desktop\1\开户及产品开通.txt`，包含代运营开户进件、协议支付产品 144 开通、分账产品 421 开通的请求和响应样例。

原始请求中包含手机号、身份证号、邮箱、企业名称、文件 UUID、签名报文等敏感或环境相关信息。本页只提炼接入指引所需的流程、关键字段和响应判断，不复制完整请求报文。

## 提炼出的关键事实

1. 代运营开户进件成功后返回商户 `uid`，后续产品开通均使用该 `uid`。
2. 代运营商户类型使用 `merchantType=COMPANY`、`merchantProperties=AGENT_MEMBER`。
3. 协议支付产品 144 的开通请求中，`feeRuleList.productId=144`，样例 `productModelId=M2503000004`。
4. 分账产品 421 的开通请求中，`feeRuleList.productId=421`，`productModelId=10370560005`。
5. 分账产品 421 开通需要传 `prodExtendInfo`，样例包含：
   - `openSupplyInfo.supplyFiles`
   - `openSupplyInfo.techSupportPhone`
   - `openSupplyInfo.shareProdRatio`
   - `openSupplyInfo.techSupportFlag`
   - `bankType=HT`
6. 分账产品 421 开通成功响应中返回 `openState=1` 和 `openApplyNo`。

## 接入指引中的风险提示

1. 不应把 144 和 421 当作同一个货架下的一次性产品开通。
2. 对该代理商，144 需要按协议支付对应货架开通；421 需要单独按 `10370560005` 货架开通。
3. 分账接收方必须完成进件和绑定关系后，才具备分账条件。
4. 如果一个分账接收方需要接收多个代运营商户的分账，应使用“分账接收方绑定代运营商户”接口逐一绑定。
