---
artifact_type: source-analysis
title: unified-gateway-field-metadata / domain-split / 2026-06-09
canonical_object: unified-gateway-field-metadata
layer: sources
domain: account-clearing
source_type: inbox-material-analysis
created: 2026-06-09
status: draft-analysis
derived_from:
  - inbox/统一网关字段元数据合并版.md
  - requirements/config/requirements-taxonomy.yaml
---

# 统一网关字段元数据 / 领域拆分分析 / 2026-06-09

## 结论

当前材料本质上是统一网关字段注册表，不是领域模型。它的现有分类同时包含字段形态分类和接口场景分类：

| 类型 | 当前分类 | 用途 |
|---|---|---|
| 字段形态 | 单号类、标识类、编码类、金额类、类型类、状态类、时间类、通用字段 | 管字段命名、格式、长度、字典、生命周期 |
| 接口场景 | 认证类、支付类、退款类、分账类、代付类 | 管字段常出现在哪类对外接口 |

建议不要把原字段注册表直接拆散。更稳妥的做法是保留统一字段注册表，再增加一层领域归属映射：

| 建议新增映射字段 | 含义 |
|---|---|
| `primary_subdomain` | 字段表达的主业务事实归属 |
| `secondary_subdomain` | 接口使用时可能涉及的次领域 |
| `bounded_context` | 领域模型里的上下文 |
| `fact_owner` | 字段事实应由哪个业务事实所有者解释 |
| `is_gateway_common_metadata` | 是否属于网关公共契约，不应强行归业务领域 |
| `classification_note` | 边界说明、歧义、待确认点 |

## 领域归属规则

| 领域 | 判断标准 |
|---|---|
| `merchant_platform_relationship` | 商户、应用、子商户、门店、终端、产品能力、商户服务关系 |
| `payment_transaction` | 支付意图、支付订单、渠道交易、退款、交易状态、交易时间、支付方式授权结果 |
| `risk_compliance` | 签约协议、扣款授权、银行卡认证、身份信息、风控参数、终端风险信号、合规证据 |
| `funds_movement_settlement` | 分账、代付、转账、结算金额、收款方、批次、资金划拨 |
| `account_balance` | 资金账户、账户类型、可用余额、不可用余额、冻结/保留余额、余额流水、可用时间、余额状态 |
| `financial_operations` | 账单、对账下载、费用、手续费、渠道响应、异常备注、财务运营证据 |
| `gateway_common_contract` | 请求时间、回调地址、通知类型、保留域、业务参数集合等网关公共协议字段 |

## 字段领域映射

### merchant_platform_relationship

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `app_id` | 应用ID | `merchant_platform_relationship` | 开放平台、公众平台或调起支付使用的应用标识，表达商户/平台应用关系。不是支付订单事实。 |
| `merchant_id` | 商户号 | `merchant_platform_relationship` | 渠道分配给商户的标识，用于识别交易或能力归属主体。不是资金账户号。 |
| `sub_merchant_id` | 子商户ID | `merchant_platform_relationship` | 服务商或平台模式下的子商户主体标识，表达平台和子商户关系。 |
| `sub_merchant_name` | 子商户名称 | `merchant_platform_relationship` | 子商户展示或登记名称，配合 `sub_merchant_id` 识别经营主体。 |
| `sub_merchant_service_name` | 子商户服务名称 | `merchant_platform_relationship` | 子商户提供给用户的服务名称，属于商户服务关系。 |
| `sub_merchant_service_description` | 子商户服务描述 | `merchant_platform_relationship` | 子商户服务说明，如免密支付场景说明；若用于签约展示，次领域涉及 `risk_compliance`。 |
| `product_code` | 产品码 | `merchant_platform_relationship` | 商户和平台签约的产品能力编码，表达商户被授予或使用的产品能力。 |
| `store_id` | 门店号 | `merchant_platform_relationship` | 商户侧门店标识，用来说明交易、终端或产品能力发生在哪个经营门店。接口里可随支付报文出现，但字段本身是商户经营资源标识。 |
| `store_name` | 门店名称 | `merchant_platform_relationship` | 商户侧门店名称，配合 `store_id` 识别门店。可用于支付展示或风控，但主领域仍是门店/商户经营资源。 |
| `area_code` | 地区编码 | `merchant_platform_relationship` | 门店地区编码，描述门店或经营资源所在区域。 |
| `division_code` | 行政区划编码 | `merchant_platform_relationship` | 中国标准城市区域码，通常服务于门店、主体地址或地区规则。 |
| `device_id` | 商户端设备号 | `merchant_platform_relationship` | 商户侧设备标识，表达商户经营资源下的设备。交易风控使用时次领域涉及 `risk_compliance`。 |
| `device_type` | 终端设备类型 | `merchant_platform_relationship` | 受理终端设备类型，主领域是终端资源；被风控消费时属于风险信号。 |
| `serial_no` | 终端序列号 | `merchant_platform_relationship` | 特定终端设备类型下的硬件序列号，用于识别终端资源。 |
| `address` | 详细地址 | `merchant_platform_relationship` | 门店详细地址，主领域是经营资源资料；如用于合规或风控，应标次领域。 |
| `specified_seller_name` | 指定卖家名称 | `merchant_platform_relationship` | 特殊交易展示的卖家名称，主领域是交易展示主体/商户展示关系，支付接口内使用。 |

### payment_transaction

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `out_trade_no` | 商户订单号 | `payment_transaction` | 商户系统内部订单号，用于关联一笔支付意图或支付订单。 |
| `trade_no` | 平台交易号 | `payment_transaction` | 平台侧生成的交易号，是平台支付交易主标识。 |
| `channel_order_no` | 渠道订单号 | `payment_transaction` | 渠道或平台订单号，用于对齐外部渠道交易。 |
| `payment_amount` | 支付金额 | `payment_transaction` | 本次支付金额，单位分。支付成功不等于资金可结算。 |
| `payment_total_amount` | 支付总金额 | `payment_transaction` | 支付成功或交易汇总金额，仍归支付交易事实。 |
| `discount_amount` | 商品优惠金额 | `payment_transaction` | 订单优惠金额，影响交易展示和实付计算；若用于财务核算可次归 `financial_operations`。 |
| `currency` | 货币类型 | `payment_transaction` | 支付币种，支付金额的基础属性。 |
| `trade_type` | 交易类型 | `payment_transaction` | 订单交易类型，如 JSAPI，描述支付方式或交易形态。 |
| `channel_trade_status` | 渠道交易状态 | `payment_transaction` | 渠道处理状态，属于渠道交易生命周期。 |
| `trade_status` | 交易状态 | `payment_transaction` | 平台订单交易状态，属于支付订单生命周期。 |
| `trade_status_desc` | 交易状态描述 | `payment_transaction` | 交易状态说明，解释 `trade_status` 或渠道状态。 |
| `timeout_express` | 订单相对超时时间 | `payment_transaction` | 从交易创建开始计算的最晚付款时间，属于支付订单生命周期规则。 |
| `success_time` | 支付完成时间 | `payment_transaction` | 支付完成时间。 |
| `successful_payment_time` | 成功支付时间 | `payment_transaction` | 支付成功时间，来源字段 `succ_time`。 |
| `description` | 商品描述 | `payment_transaction` | 商品或订单描述，是支付展示和订单上下文信息。 |
| `scene_info` | 场景信息 | `payment_transaction` | 支付场景对象；其子字段可能分别落到商户、终端、风险等领域。 |
| `open_id` | 用户标识 | `payment_transaction` | 用户在商户应用下的唯一标识。若沉淀用户主体模型，可能需要单独用户上下文；当前模型中按支付方法/交易参与方处理。 |
| `merchant_user_id` | 商户用户ID | `payment_transaction` | 商户平台内用户标识，用于关联交易用户；不是商户主体。 |
| `out_refund_no` | 商户退款单号 | `payment_transaction` | 商户系统内部退款单号，属于退款聚合事实。 |
| `refund_no` | 支付退款单号 | `payment_transaction` | 平台退款单号，属于退款聚合事实。 |
| `refund_status` | 退款状态 | `payment_transaction` | 退款生命周期状态。 |
| `refund_total_amount` | 退款总金额 | `payment_transaction` | 退款金额事实。涉及结算冲正时次领域是 `funds_movement_settlement`。 |
| `payer_refund` | 用户退款金额 | `payment_transaction` | 退给用户的金额，主领域是退款；财务处理需另看账务规则。 |
| `discount_refund` | 优惠退款金额 | `payment_transaction` | 优惠部分退款金额，主领域是退款明细。 |
| `reason` | 退款原因 | `payment_transaction` | 退款发起原因，属于退款业务上下文。 |
| `funds_account` | 退款资金来源 | `payment_transaction` | 在退款接口中说明退款资金来源；若表达真实出资账户状态，次领域为 `account_balance`。 |

### risk_compliance

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `payment_protocol_no` | 支付协议号 | `risk_compliance` | 签约协议号，表达扣款或支付协议授权。不是普通支付单号。 |
| `external_agreement_no` | 商户签约号 | `risk_compliance` | 代扣协议中标识用户的商户侧签约号，属于授权/同意记录。 |
| `payment_protocol_list` | 支付协议列表 | `risk_compliance` | 协议列表密文或协议信息集合，属于支付授权材料。 |
| `single_deduct_amount` | 单次扣款最大金额 | `risk_compliance` | 周期扣款每次最大扣款金额，是授权约束，不是单笔交易金额。 |
| `period_type` | 周期类型 | `risk_compliance` | 周期扣款类型，如 DAY、MONTH，属于授权和扣款规则。 |
| `deduct_period` | 扣款周期数 | `risk_compliance` | 周期扣款周期数，属于授权范围和执行规则。 |
| `execute_time` | 首次执行时间 | `risk_compliance` | 周期扣款首次执行时间，属于授权后的扣款计划约束。 |
| `period_rule_params` | 周期管控规则参数 | `risk_compliance` | 签约周期扣款产品的管控规则，主领域是授权合规和风险控制。 |
| `bank_card_no` | 银行卡号 | `risk_compliance` | 敏感支付工具标识，当前表里用于银行卡认证或扣款，不应只按普通标识处理。 |
| `bank_card_type` | 银行卡类型 | `risk_compliance` | 银行卡认证或支付工具类型字段。 |
| `identity_document_no` | 证件号 | `risk_compliance` | 敏感身份信息，属于 KYC/认证材料。 |
| `identity_document_type` | 证件类型 | `risk_compliance` | 身份认证材料类型。 |
| `bank_card_auth_info` | 银行卡认证信息 | `risk_compliance` | 银行卡号、持卡人、证件号、手机号等认证集合。 |
| `risk_control_info` | 风控参数 | `risk_compliance` | 风控参数 JSON，属于风险信号输入。 |
| `payer_client_ip` | 用户终端IP | `risk_compliance` | 用户客户端 IP，主要用于交易风险识别；也可作为网关公共请求属性。 |
| `location` | 终端经纬度 | `risk_compliance` | 终端实时位置，通常用于终端合规、交易风控或场景校验。 |
| `real_name` | 收款用户姓名 | `risk_compliance` | 敏感身份信息；原描述为异常退款收款用户姓名，退款场景中使用但主属性是身份认证信息。 |
| `payee_identity_no` | 收款人证件号 | `risk_compliance` | 收款人身份材料，代付场景中使用但事实归属偏身份合规。 |
| `payee_mobile` | 收款人手机号 | `risk_compliance` | 收款人联系/认证材料，代付场景中使用但涉及敏感个人信息。 |

### funds_movement_settlement

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `settlement_total` | 应结订单金额 | `funds_movement_settlement` | 订单应结金额，主领域是结算事实，不等同于支付金额。 |
| `settlement_refund` | 应结退款金额 | `funds_movement_settlement` | 退款对结算金额的影响，属于结算或资金清分。 |
| `profit_sharing` | 分账标识 | `funds_movement_settlement` | 订单是否支持分账，是分账规则或结果入口。 |
| `profit_sharing_amount` | 分账总金额 | `funds_movement_settlement` | 分账总金额，单位分。 |
| `profit_sharing_receiver_amount` | 分账接收方金额 | `funds_movement_settlement` | 单个分账接收方金额，属于分账分配结果。 |
| `profit_sharing_receiver_account_no` | 分账接收方账户号 | `funds_movement_settlement` | 被分账方账户号。若要表达余额/账务状态，次领域为 `account_balance`。 |
| `profit_sharing_receiver_account_type` | 分账接收方账户类型 | `funds_movement_settlement` | 被分账方账户类型，服务于分账收款方识别。 |
| `profit_sharing_info` | 分账信息 | `funds_movement_settlement` | 分账接收方信息集合，来源字段 `sharing_info`。 |
| `profit_sharing_detail_desc` | 分账明细说明 | `funds_movement_settlement` | 分账明细说明。 |
| `profit_sharing_finish_flag` | 分账完结标识 | `funds_movement_settlement` | 是否完结分账并解冻剩余未分账金额；涉及冻结资金时次领域为 `account_balance`。 |
| `channel_batch_no` | 渠道批次号 | `funds_movement_settlement` | 平台代付交易返回批次号，属于代付批次或资金划拨批次。 |
| `transfer_amount` | 转账金额 | `funds_movement_settlement` | 转账金额，单位分。 |
| `transfer_total_amount` | 转账总金额 | `funds_movement_settlement` | 转账总金额，通常用于批量转账或代付汇总。 |
| `transfer_count` | 转账笔数 | `funds_movement_settlement` | 转账交易总笔数。 |
| `transfer_apply_time` | 转账申请时间 | `funds_movement_settlement` | 转账申请时间，属于转账生命周期。 |
| `transfer_finish_time` | 转账完成时间 | `funds_movement_settlement` | 转账完成时间，属于转账生命周期。 |
| `payer_merchant_id` | 付款方商户号 | `funds_movement_settlement` | 转账或代付中的付款方主体。若只是商户关系标识，次领域是 `merchant_platform_relationship`。 |
| `payee_merchant_id` | 收款方商户号 | `funds_movement_settlement` | 转账或分账中的收款方主体。 |
| `payee_bank_card_no` | 收款银行卡号 | `funds_movement_settlement` | 外部收款卡号，服务于代付出款；敏感属性次领域为 `risk_compliance`。 |
| `payee_bank_cnap` | 收款银行联行号 | `funds_movement_settlement` | 代付到行所需银行路由信息。 |
| `payee_name` | 收款人姓名 | `funds_movement_settlement` | 代付收款人户名；身份敏感次领域为 `risk_compliance`。 |
| `payee_bank_name` | 收款银行名称 | `funds_movement_settlement` | 收款银行名称，用于代付入账路径。 |
| `payee_bank_branch_name` | 收款开户行支行 | `funds_movement_settlement` | 收款开户行支行。 |
| `payee_bank_province` | 收款开户行省份 | `funds_movement_settlement` | 收款开户行省份。 |
| `payee_bank_city` | 收款开户行城市 | `funds_movement_settlement` | 收款开户行城市。 |
| `transfer_summary` | 转账摘要 | `funds_movement_settlement` | 转账摘要，属于转账指令说明。 |
| `transfer_purpose` | 转账用途 | `funds_movement_settlement` | 转账用途，属于转账指令说明。 |

### account_balance

当前原表只覆盖了账户引用，缺少真正的余额事实。按微信支付和 Stripe 的账户余额模型看，`account_balance` 至少应覆盖两层：

| 层级 | 含义 | 外部参照 |
|---|---|---|
| 账户余额快照 | 某个资金账户在某个时点的可用、不可用、冻结、保留或待结算资金状态 | 微信支付实时余额查询返回账户类型、可用余额、不可用余额；Stripe Balance 对象区分 `available` 和 `pending` |
| 余额流水/账务影响 | 每一笔交易、退款、转账、费用、提现等动作如何增加或减少余额；必须表达原始金额、费用、净额影响 | Stripe Balance Transaction 有 `amount`、`fee`、`net`、`status`、`available_on`、`source`、`type` |

#### 已有字段归属

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `payer_account_no` | 付款账户号 | `account_balance` | 付款账户标识，表达资金从哪个账户出。当前只有账号，没有余额、冻结、可用时间或记账分录。 |
| `payer_account_type` | 付款账户类型 | `account_balance` | 付款账户类型，服务于资金账户识别；应和余额账户类型字典统一。 |
| `account_type` | 资金账户类型 | `account_balance` | 申请资金账单或余额查询时使用的资金账户类型。可参考微信支付的基本账户、运营账户、手续费账户、保证金账户这类账户类型分层。 |
| `refund_fund_account_type` | 出资账户类型 | `account_balance` | 退款出资账户类型，表示退款从哪类资金账户出。主领域是账户余额，退款场景是次领域。 |

#### 建议补充字段

这些字段当前原表没有，但如果要把“账户和余额领域”补全，应作为候选字段登记：

| 建议字段 | 中文名 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `balance_account_no` | 余额账户号 | `account_balance` | 平台内部资金账户标识。不要和商户号、渠道商户号混用。 |
| `balance_account_type` | 余额账户类型 | `account_balance` | 账户类型，如基本账户、运营账户、手续费账户、保证金账户、分账接收账户等。 |
| `available_amount` | 可用余额 | `account_balance` | 当前可提现、可出款或可用于资金动作的余额。支付成功金额不能直接等于可用余额。 |
| `pending_amount` | 待可用余额 | `account_balance` | 已进入账户但尚不可用的余额，可对应待结算、在途或未到可用时间的资金。 |
| `unavailable_amount` | 不可用余额 | `account_balance` | 不可用于提现或出款的余额。可作为微信支付“不可用余额”口径的通用字段。 |
| `frozen_amount` | 冻结余额 | `account_balance` | 因风险、争议、保证金、规则限制等被冻结的资金。若冻结原因来自风控，次领域为 `risk_compliance`。 |
| `reserved_amount` | 保留余额 | `account_balance` | 预留、保证金、最低留存、网络规则保留等不能立即出款的余额。 |
| `instant_available_amount` | 即时可用余额 | `account_balance` | 可即时转出或加速提现的余额。若一期没有即时出款能力，可先不登记。 |
| `balance_currency` | 余额币种 | `account_balance` | 余额金额对应币种。不要直接复用交易币种，跨币种清结算时二者可能不同。 |
| `balance_snapshot_time` | 余额快照时间 | `account_balance` | 余额查询或余额快照生成时间，用于判断余额是否实时。 |
| `available_on` | 预计可用时间 | `account_balance` | 待可用资金预计变为可用的时间。Stripe 余额流水用这个表达净资金可用日期。 |
| `balance_transaction_no` | 余额流水号 | `account_balance` | 余额变化流水标识，用于连接交易、退款、转账、费用和账户余额变化。 |
| `balance_transaction_type` | 余额流水类型 | `account_balance` | 余额变化类型，如支付入账、退款出账、提现、转账、手续费、保留释放等。 |
| `balance_transaction_status` | 余额流水状态 | `account_balance` | 余额流水对余额的影响状态，如待可用、已可用、失败、冲正。 |
| `balance_source_no` | 余额来源单号 | `account_balance` | 触发余额变化的来源对象，如支付单、退款单、转账单、提现单、费用单。 |
| `gross_amount` | 入账/出账原始金额 | `account_balance` | 余额流水原始金额。可为正或负，表示资金进入或流出。 |
| `fee_amount` | 费用金额 | `account_balance` | 影响净额的手续费或平台费。费用核算次领域为 `financial_operations`。 |
| `net_amount` | 余额净影响金额 | `account_balance` | 一笔余额流水对账户余额的最终净影响。不要只看交易金额；手续费、平台费、退款、冲正、汇兑、保留释放等都可能改变净额。 |
| `balance_after_amount` | 变动后余额 | `account_balance` | 本次余额流水入账或出账后的账户余额。用于对账和审计；如底层系统不提供，可作为派生字段或不登记。 |
| `source_type` | 余额来源类型 | `account_balance` | 余额按来源支付方式或资金来源拆分，如银行卡、卡支付、账户余额、分账等。 |

### financial_operations

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `bill_type` | 账单类型 | `financial_operations` | 交易账单类型，偏账单/对账语义。 |
| `bill_date` | 账单日期 | `financial_operations` | 账单日期，服务于账单下载、对账、财务运营。 |
| `download_url` | 下载地址 | `financial_operations` | 账单下载地址。若不是账单接口，需要按接口再确认。 |
| `refund_fee` | 手续费退款金额 | `financial_operations` | 手续费退还金额，属于费用核算事实。 |
| `transfer_fee` | 转账手续费 | `financial_operations` | 转账手续费，属于费用核算事实。 |
| `fee_bearer_merchant_id` | 手续费承担方商户号 | `financial_operations` | 手续费承担主体，用于费用归属。主体身份次领域为 `merchant_platform_relationship`。 |
| `billing_merchant_id` | 计费商户号 | `financial_operations` | 计费归属商户号，用于费用或账单归属。 |
| `channel_response_code` | 渠道响应码 | `financial_operations` | 渠道响应码可用于支付处理，也可作为对账/异常处理证据。主归属建议按异常运营证据处理。 |
| `channel_remark` | 渠道备注 | `financial_operations` | 渠道错误或备注信息，主要用于异常处理、对账和运营排查。 |

### gateway_common_contract

| 字段 | 原定义 | 建议领域 | 解释与边界 |
|---|---|---|---|
| `request_time` | 请求时间 | `gateway_common_contract` | 请求发送时间，是网关公共协议字段，不是某个业务领域事实。 |
| `notify_url` | 商户回调地址 | `gateway_common_contract` | 商户接收通知的地址，是集成契约。支付接口中使用，但不属于支付订单生命周期。 |
| `event_type` | 通知的类型 | `gateway_common_contract` | 回调通知事件类型，属于通知协议。具体事件可路由到交易、退款、分账等领域。 |
| `create_time` | 通知创建时间 | `gateway_common_contract` | 通知或资源创建时间。若具体资源明确，可二次归属到对应领域。 |
| `biz_content` | 业务参数集合 | `gateway_common_contract` | 公共参数外的业务参数集合，是网关承载结构，不应作为单一业务字段归领域。 |
| `merchant_reserved_field1` | 商户保留域1 | `gateway_common_contract` | 商户保留域，含义由商户侧约定，不能稳定归业务领域。 |
| `merchant_reserved_field2` | 商户保留域2 | `gateway_common_contract` | 商户保留域，含义由商户侧约定，不能稳定归业务领域。 |
| `system_reserved_field1` | 系统保留域1 | `gateway_common_contract` | 系统保留域，含义需看具体系统使用，不建议归业务领域。 |
| `system_reserved_field2` | 系统保留域2 | `gateway_common_contract` | 系统保留域，含义需看具体系统使用，不建议归业务领域。 |

## 当前材料的明显问题

1. `AUTH` 分类已定义，但实际认证、签约、授权字段大多放在 `支付类`，例如 `bank_card_auth_info`、`payment_protocol_list`、`period_rule_params`。
2. `store_id`、`store_name` 这类字段出现在支付接口里，但字段事实不是支付订单，而是商户经营资源。
3. `payer_account_no`、`account_type` 这类账户字段当前只是账户引用，不足以构成完整 `account_balance` 需求；还应补可用余额、不可用余额、冻结/保留余额、余额流水和净额影响字段。
4. `refund_fee`、`transfer_fee`、`billing_merchant_id`、`fee_bearer_merchant_id` 已经显露费用/计费/财务运营语义，不宜只归为金额类或标识类。
5. 保留域、`biz_content`、回调地址等字段必须保持网关公共契约身份，不能为追求领域拆分而硬归类。

## 建议落表方式

字段注册表继续维护原字段形态分类；新增领域映射表，不替代原表：

| 字段名 | 原字段分类 | primary_subdomain | secondary_subdomain | is_gateway_common_metadata | classification_note |
|---|---|---|---|---|---|
| `store_id` | 标识类 | `merchant_platform_relationship` | `payment_transaction`, `risk_compliance` | false | 商户侧门店标识；支付报文使用不改变字段主事实归属。 |
| `payment_protocol_no` | 单号类 | `risk_compliance` | `payment_transaction` | false | 签约协议号，主语义是授权/同意。 |
| `settlement_total` | 金额类 | `funds_movement_settlement` | `financial_operations` | false | 应结金额，不等同于支付金额。 |
| `request_time` | 时间类 | `gateway_common_contract` |  | true | 请求协议时间，不是业务生命周期状态。 |
| `biz_content` | 支付类 | `gateway_common_contract` |  | true | 参数承载结构，不应作为业务事实字段。 |
| `available_amount` | 金额类 | `account_balance` | `funds_movement_settlement` | false | 可用余额，表达账户资金状态，不等同于支付成功金额。 |
| `pending_amount` | 金额类 | `account_balance` | `funds_movement_settlement` | false | 待可用或不可用余额，需结合账户口径确认是否等同冻结、在途或待结算。 |
| `balance_transaction_no` | 单号类 | `account_balance` | `financial_operations` | false | 余额变化流水号，用于追踪交易、费用、退款、提现对余额的净影响。 |
| `gross_amount` | 金额类 | `account_balance` | `financial_operations` | false | 余额流水原始金额，应和 `fee_amount`、`net_amount` 成组看。 |
| `fee_amount` | 金额类 | `account_balance` | `financial_operations` | false | 余额流水费用金额，影响净额。 |
| `net_amount` | 金额类 | `account_balance` | `financial_operations` | false | 余额流水对账户余额的最终净影响，是账户余额领域的核心字段。 |

## 外部参照

| 来源 | 可借鉴点 | 使用边界 |
|---|---|---|
| [微信支付：查询账户实时余额](https://pay.wechatpay.cn/doc/v3/partner/4012721477) | 余额查询按账户类型进入，返回可用余额和不可用余额；账户类型包括基本账户、运营账户、手续费账户等 | 只借鉴账户类型和余额状态口径，不直接搬微信字段到统一网关 |
| [Stripe Balance](https://docs.stripe.com/api/balance) | 余额对象区分 `available` 和 `pending`，并按币种、资金来源类型拆分 | 适合验证“支付成功不等于可用余额”的建模边界 |
| [Stripe Balance Transaction](https://docs.stripe.com/api/balance_transactions/object) | 余额流水记录资金进出、费用、净额、可用时间、状态、来源对象和类型 | 适合补齐余额流水，而不是只维护余额快照 |
