---
layer: ops
domain: unclassified
classification_needed: true
ops_area: learning-capture
canonical_object: baofu-legal-sms-verification-best-practice-learning
artifact_type: learning-note
status: draft
created_at: 2026-06-10
---

# 宝付法人短信认证最佳实践参考记录

## Learning Route

- Source kind: mixed external reference and example-shaped security practice.
- Topic: 法人短信认证、H5 链接、安全 token、核身、合规证据链。
- Reusable capability type: evidence, boundary, acceptance-shape.
- Repo target: `wiki/ops/requirements-cases/2026-06-09-015054-baofu-multi-channel-legal-sms-verification.md` and its human review companion.

## Source References

| Source | URL | What was reused |
| --- | --- | --- |
| 中国人民银行《关于加强支付受理终端及相关业务管理的通知》 | <https://www.pbc.gov.cn/tiaofasi/144941/3581332/4359567/index.html> | 特约商户身份信息核实、法人/负责人/被授权人风险提示、最小必要核心信息采集、一致性和不可篡改性作为支付监管语境下的参考。 |
| OWASP Forgot Password Cheat Sheet | <https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html> | 一次性 URL token 的随机性、长度、安全存储、短有效期、使用后失效、HTTPS、可信域名、防暴力枚举和 Referer 泄露控制。 |
| OWASP Authentication Cheat Sheet | <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html> | 敏感动作需要重新认证或更强认证，不能只靠页面按钮隐藏或弱认证完成高风险动作。 |
| NIST SP 800-63B | <https://pages.nist.gov/800-63-3/sp800-63b.html> | SMS/PSTN out-of-band 属于受限认证参考，适合提示“短信验证码只能证明手机号可达或受控，不等同于法人身份”。 |
| NIST SP 800-63A | <https://pages.nist.gov/800-63-3/sp800-63a.html> | 身份核验需要身份材料、权威来源验证和主体绑定，适合提示“法人手机号来源和身份绑定依据必须确认”。 |

## Reused

- 把短信 URL 长度和承载方式从实现细节提升为验收事实：短信模板必须有长度预算，链接应采用可信域名下短路径或短 token，不应携带明文敏感参数。
- 把链接 token 安全补为验收事实：HTTPS、可信域名、不可枚举、短有效期、可失效、频控、日志脱敏和 Referer 防泄露。
- 把“短信验证码通过”降级为手机号可达性证据：完成法人真实意愿核验还需要手机号来源、法人身份绑定、二次核身或人工兜底。
- 把合规证据链补为验收事实：页面文案版本、短信模板版本、发送/重发、核身方式、验证码结果、意愿确认动作、时间、IP/设备、操作人和失败原因。

## Modified

- 没有直接采用外部身份等级或认证等级；本需求只借用风险判断形态，具体核身强度由宝付合规/法务/安全 owner 确认。
- 没有把 NIST 或 OWASP 作为中国支付监管合规依据；它们只作为安全最佳实践参考。
- 没有要求立即选定短链服务；当前只要求给出短信承载方案、可信域名、短 token、超长降级和安全边界。

## Not Formalized

- 未正式确认适用法规条款、留存期限、可审计字段和监管报送口径。
- 未正式确认短信渠道的长度限制、拆分策略、签名模板限制和短链可用性。
- 未正式确认法人手机号来源、法人身份绑定字段、二次核身字段或人工兜底流程。
- 未正式确认 token 有效期、单次/多次访问语义、重发后旧 token 是否失效、频控阈值和告警策略。

## Next Step

- 在需求 case 中保留新增 AC-017 到 AC-020。
- 由产品、合规、法务、安全、短信渠道 owner 补齐上述未确认项后，重新运行 requirements checker 并进行人工复核。
