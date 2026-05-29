## ADDED Requirements

### Requirement: The system SHALL support embedded account opening with first-card binding

The system SHALL support merchant-initiated embedded account opening with first-card binding as the account activation path.

Trace: user story `US-001`; acceptance functions `AF-001, AF-002, AF-003, AF-004, AF-005, AF-020, AF-023, AF-024`.

#### Scenario: 终端用户正常开户

Trace: user story `US-001`; acceptance function `AF-001`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 首卡绑定成功后，系统返回开户成功。

#### Scenario: 首卡绑定失败导致开户失败

Trace: user story `US-001`; acceptance function `AF-002`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 首卡绑定失败时，系统返回开户失败，不生成成功账户状态。

#### Scenario: 同一商户用户重复开户

Trace: user story `US-001`; acceptance function `AF-003`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 同一商户用户已开户成功后再次开户，系统返回已存在账户成功，不重复创建账户。

#### Scenario: 历史开户处理中再次开户

Trace: user story `US-001`; acceptance function `AF-004`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 历史开户处理中再次开户，系统返回处理中。

#### Scenario: 历史开户失败重新开户

Trace: user story `US-001`; acceptance function `AF-005`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 历史开户失败后，系统允许重新走开户流程。

#### Scenario: 开户受理后异步通知商户

Trace: user story `US-001`; acceptance function `AF-020`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 开户受理后用户完成绑卡且系统收敛最终结果，商户收到最终开户结果通知。

#### Scenario: 异步通知失败后主动查询

Trace: user story `US-001`; acceptance function `AF-023`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 通知未送达时，调用方主动查询可获得唯一最终状态。

#### Scenario: 开户命中正常账户

Trace: user story `US-001`; acceptance function `AF-024`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 开户命中同商户同证件正常账户时，系统直接返回已存在账户成功，不重复开户。

### Requirement: The system SHALL support terminal-user card binding flows

The system SHALL support terminal-user card binding flows initiated through the merchant journey.

Trace: user story `US-002`; acceptance functions `AF-001, AF-006, AF-007, AF-021`.

#### Scenario: 终端用户正常开户

Trace: user story `US-002`; acceptance function `AF-001`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 首卡绑定成功后，系统返回开户成功。

#### Scenario: 开户后追加绑卡成功

Trace: user story `US-002`; acceptance function `AF-006`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 开户后追加绑卡成功，系统返回绑卡成功，新卡可用于支付。

#### Scenario: 多卡识别后用户选择绑卡

Trace: user story `US-002`; acceptance function `AF-007`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 通道识别多张卡后，系统按用户选择结果完成绑卡。

#### Scenario: 绑卡受理后异步通知商户

Trace: user story `US-002`; acceptance function `AF-021`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 绑卡受理后用户完成绑卡且系统收敛最终结果，商户收到最终绑卡结果通知。

### Requirement: The system SHALL support additional card binding after account opening

The system SHALL support additional card binding after an embedded account has been opened.

Trace: user story `US-003`; acceptance functions `AF-006, AF-007, AF-021, AF-023, AF-025`.

#### Scenario: 开户后追加绑卡成功

Trace: user story `US-003`; acceptance function `AF-006`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 开户后追加绑卡成功，系统返回绑卡成功，新卡可用于支付。

#### Scenario: 多卡识别后用户选择绑卡

Trace: user story `US-003`; acceptance function `AF-007`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 通道识别多张卡后，系统按用户选择结果完成绑卡。

#### Scenario: 绑卡受理后异步通知商户

Trace: user story `US-003`; acceptance function `AF-021`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 绑卡受理后用户完成绑卡且系统收敛最终结果，商户收到最终绑卡结果通知。

#### Scenario: 异步通知失败后主动查询

Trace: user story `US-003`; acceptance function `AF-023`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 通知未送达时，调用方主动查询可获得唯一最终状态。

#### Scenario: 商户未开通一键绑卡权限

Trace: user story `US-003`; acceptance function `AF-025`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 商户未开通一键绑卡权限时，调用绑卡或解绑接口被拒绝并返回权限不足。

### Requirement: The system SHALL support account-card relationship unlinking

The system SHALL support unlinking the account-to-card relationship and excluding unlinked cards from payment.

Trace: user story `US-004`; acceptance functions `AF-008, AF-009, AF-016, AF-017, AF-025`.

#### Scenario: 解绑银行卡关系成功

Trace: user story `US-004`; acceptance function `AF-008`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 账户已绑定银行卡时调用解绑接口，系统成功解除账户与银行卡关系。

#### Scenario: 解绑后卡不可继续支付

Trace: user story `US-004`; acceptance function `AF-009`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 某张卡已解绑后再次发起账户支付，系统不再使用该卡支付。

#### Scenario: 已解绑卡在自动扣款中被跳过

Trace: user story `US-004`; acceptance function `AF-016`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 自动扣款命中已解绑高优先级卡时，系统自动跳过并继续处理下一张可用卡。

#### Scenario: 所有卡不可用时支付失败

Trace: user story `US-004`; acceptance function `AF-017`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 所有卡均已解绑或不可用时，系统返回支付失败。

#### Scenario: 商户未开通一键绑卡权限

Trace: user story `US-004`; acceptance function `AF-025`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 商户未开通一键绑卡权限时，调用绑卡或解绑接口被拒绝并返回权限不足。

### Requirement: The system SHALL support explicit account payment in subscription payment

The system SHALL support explicit account-payment selection in subscription payment.

Trace: user story `US-005`; acceptance functions `AF-010, AF-011, AF-026`.

#### Scenario: 订阅支付选择账户支付

Trace: user story `US-005`; acceptance function `AF-010`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 商户显式传入账户支付时，订阅支付正确调用账户支付接口。

#### Scenario: 账户支付成功

Trace: user story `US-005`; acceptance function `AF-011`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 支付前置条件满足时调用账户支付接口，支付成功且订阅支付结果同步成功。

#### Scenario: 商户未开通协议支付权限

Trace: user story `US-005`; acceptance function `AF-026`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 商户未开通协议支付权限时，调用账户支付接口被拒绝并返回权限不足。

### Requirement: The system SHALL attempt account payment by bound-card priority

The system SHALL attempt account payment through bound cards according to configured card priority rules.

Trace: user story `US-006`; acceptance functions `AF-012, AF-013, AF-014, AF-015, AF-016, AF-017`.

#### Scenario: 按优先级先扣高优先级卡

Trace: user story `US-006`; acceptance function `AF-012`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 用户绑定多张卡后发起账户支付，系统优先使用高优先级卡支付。

#### Scenario: 高优先级卡失败切换低优先级卡

Trace: user story `US-006`; acceptance function `AF-013`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 高优先级卡明确失败后，系统切换低优先级卡继续支付。

#### Scenario: 支付结果未明禁止直接切卡

Trace: user story `US-006`; acceptance function `AF-014`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 当前卡支付结果未明时，系统先查单，不直接切下一张卡。

#### Scenario: 银行卡查询超过上限

Trace: user story `US-006`; acceptance function `AF-015`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 银行卡查询超过配置上限时，系统按配置上限最多处理 5 张卡。

#### Scenario: 已解绑卡在自动扣款中被跳过

Trace: user story `US-006`; acceptance function `AF-016`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 自动扣款命中已解绑高优先级卡时，系统自动跳过并继续处理下一张可用卡。

#### Scenario: 所有卡不可用时支付失败

Trace: user story `US-006`; acceptance function `AF-017`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 所有卡均已解绑或不可用时，系统返回支付失败。

### Requirement: The system SHALL converge unclear payment outcomes without duplicate payment

The system SHALL converge unclear or exceptional payment outcomes through query and compensation without duplicate payment.

Trace: user story `US-007`; acceptance functions `AF-014, AF-018, AF-019, AF-022, AF-023, AF-026`.

#### Scenario: 支付结果未明禁止直接切卡

Trace: user story `US-007`; acceptance function `AF-014`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 当前卡支付结果未明时，系统先查单，不直接切下一张卡。

#### Scenario: 支付异常后查询收敛结果

Trace: user story `US-007`; acceptance function `AF-018`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 通道未返回明确支付结果后，系统调用查询接口并收敛出唯一最终支付结果。

#### Scenario: 异常补偿不重复支付

Trace: user story `US-007`; acceptance function `AF-019`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 补偿流程执行查询、补偿、重试时，不发生重复扣款，仅保留唯一有效支付结果。

#### Scenario: 支付处理中异步通知订阅产品

Trace: user story `US-007`; acceptance function `AF-022`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 支付处理中或异常后异步处理完成，订阅支付产品收到最终支付结果通知。

#### Scenario: 异步通知失败后主动查询

Trace: user story `US-007`; acceptance function `AF-023`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 通知未送达时，调用方主动查询可获得唯一最终状态。

#### Scenario: 商户未开通协议支付权限

Trace: user story `US-007`; acceptance function `AF-026`.

- **GIVEN** the requirement preconditions are met
- **WHEN** the user performs the required action
- **THEN** 商户未开通协议支付权限时，调用账户支付接口被拒绝并返回权限不足。

### Requirement: The embedded-account-phase1 draft SHALL require review before implementation

The OpenSpec draft SHALL block implementation until user review is accepted.

Implementation requires user review after draft creation.

#### Scenario: Draft is created

- **WHEN** the OpenSpec draft files are generated
- **THEN** implementation remains blocked until user review is accepted
