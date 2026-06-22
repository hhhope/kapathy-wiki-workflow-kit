# 钱包账户 Dubbo 接口文档（Apifox）

> **说明**：Apifox 的 Dubbo 接口与 HTTP/OpenAPI **不是同一套格式**，不能用 `openapi.yaml` 导入 Dubbo 项目。  
> 本文档按 Apifox Dubbo 项目要求编写，便于 **手动新建** 或配合 **IDEA Apifox 插件从 Java 接口同步**。

---

## 1. Apifox 使用方式

| 方式 | 适用场景 | 操作 |
|------|----------|------|
| **注册中心导入** | 已部署 Provider 且配置元数据中心 | 新建 Dubbo 项目 → 连接 Nacos/ZK → 导入服务 |
| **IDEA 插件同步** | 代码已有 `@DubboService` 接口 | 安装 Apifox Helper → 关联项目 → 上传/同步接口 |
| **手动新建** | 设计阶段、尚未部署 | 按下文逐条新建 Dubbo 接口，填写接口类、方法、参数类型、JSON 示例 |

**Apifox Dubbo 项目必填项（每个接口）**

- 接口类（全限定名）
- 方法名
- 参数类型列表（Java 全限定名，顺序与 Dubbo 一致）
- 返回值类型
- 请求/响应 JSON 示例（与 DTO 字段一致，驼峰命名）

**调试前置**：Registry（Nacos/ZK）、分组 `group`、版本 `version`、超时；序列化 Hessian2（Apifox 常见组合）。

---

## 2. 服务总览

| 项 | 值 |
|----|-----|
| 应用名 | `wallet-account` [TBD] |
| Dubbo 接口 | `com.baofu.wallet.account.api.WalletAccountFacade` |
| 协议 | `dubbo` |
| 分组 group | `wallet` [TBD] |
| 版本 version | `1.0.0` [TBD] |
| 超时 timeout | 开户 `3000ms`，绑卡 `3000ms`，查列表 `2000ms` |
| 调用方 | 钱包前置（Consumer） |

**统一返回包装**（与团队规范对齐，二选一，实现时定一种即可）：

```java
// 方案 A：通用 Result（推荐与现有项目一致）
com.baofu.common.api.Result<T>

// 方案 B：账户域专用
com.baofu.wallet.account.api.dto.WalletAccountResult<T>
```

下文响应体均描述 **`Result.data`** 业务载荷；失败时 `code` / `message` 见详设错误码。

---

## 3. Dubbo 接口清单

| # | 方法名 | 说明 | 请求类型 | 返回类型 |
|---|--------|------|----------|----------|
| 1 | `openAndBind` | 开户并绑卡 | `OpenAndBindRequest` | `Result<OpenAndBindResponse>` |
| 2 | `bindCard` | 单独绑卡 | `BindCardRequest` | `Result<BindCardResponse>` |
| 3 | `unbindCard` | 解绑卡 | `UnbindCardRequest` | `Result<UnbindCardResponse>` |
| 4 | `listAgreements` | 查询绑卡列表（订阅扣款） | `ListAgreementsRequest` | `Result<ListAgreementsResponse>` |
| 5 | `queryAccountOpened` | 按平台号+证件号查询是否已开户 | `QueryAccountOpenedRequest` | `Result<QueryAccountOpenedResponse>` |

---

## 4. 接口定义

### 4.1 openAndBind — 开户并绑卡

| 项 | 值 |
|----|-----|
| 接口类 | `com.baofu.wallet.account.api.WalletAccountFacade` |
| 方法 | `openAndBind` |
| 参数 | `com.baofu.wallet.account.api.dto.request.OpenAndBindRequest` |
| 返回 | `com.baofu.common.api.Result<com.baofu.wallet.account.api.dto.response.OpenAndBindResponse>` |

**业务说明**：H5/4.0 绑卡成功后，前置调用。单事务写入客户、账户、协议、资金户、余额；`bindOrder` 按 `agreementList` 顺序 1..n；`contractLevel` 默认 `I`。

**请求 JSON 示例**

```json
{
  "requestId": "req-20260518-0001",
  "platformNo": "MCH400001",
  "createdBy": "wallet-front",
  "customerBaseInfo": {
    "customerType": "PERSON",
    "customerName": "张三",
    "certificateType": "ID",
    "certificateNo": "110101199001011234",
    "certStartDate": "2010-01-01",
    "certExpiryDate": "2030-01-01",
    "gender": "M",
    "birth": "1990-01-01",
    "address": "北京市朝阳区xxx"
  },
  "agreementList": [
    {
      "cardUserName": "张三",
      "cardNo": "6222021234567890123",
      "mobileNo": "13800138000",
      "bankCode": "ICBC",
      "bankName": "中国工商银行",
      "cardType": "C",
      "cnapsCode": "",
      "publicFlag": "0",
      "bindType": 1,
      "protocolNo": "PROT20260518001",
      "depositBankProvince": "北京",
      "depositBankCity": "北京",
      "depositBankName": "工商银行北京分行"
    }
  ]
}
```

**响应 JSON 示例（Result.data）**

```json
{
  "customerNo": "CUS202605180001",
  "contractNo": "WA2026051800001",
  "accountNo": "ACC2026051800001",
  "contractLevel": "I",
  "agreementList": [
    {
      "agreementNo": "AGR202605180001",
      "bindOrder": 1,
      "protocolNo": "PROT20260518001",
      "lastCardNo": "0123",
      "status": 0
    }
  ]
}
```

---

### 4.2 bindCard — 单独绑卡

| 项 | 值 |
|----|-----|
| 方法 | `bindCard` |
| 参数 | `com.baofu.wallet.account.api.dto.request.BindCardRequest` |
| 返回 | `Result<BindCardResponse>` |

**请求 JSON 示例**

```json
{
  "requestId": "req-20260518-0101",
  "platformNo": "MCH400001",
  "contractNo": "WA2026051800001",
  "createdBy": "wallet-front",
  "agreement": {
    "cardUserName": "张三",
    "cardNo": "6228481234567890123",
    "mobileNo": "13800138000",
    "bankCode": "ABC",
    "bankName": "中国农业银行",
    "cardType": "C",
    "bindType": 1,
    "protocolNo": "PROT20260518099"
  }
}
```

**响应 JSON 示例**

```json
{
  "agreementNo": "AGR202605180002",
  "bindOrder": 2,
  "protocolNo": "PROT20260518099"
}
```

---

### 4.3 unbindCard — 解绑卡

| 项 | 值 |
|----|-----|
| 方法 | `unbindCard` |
| 参数 | `com.baofu.wallet.account.api.dto.request.UnbindCardRequest` |
| 返回 | `Result<UnbindCardResponse>` |

**请求 JSON 示例**

```json
{
  "requestId": "req-20260518-0201",
  "contractNo": "WA2026051800001",
  "updatedBy": "wallet-front",
  "agreementNo": "AGR202605180001",
  "endReason": "用户主动解绑"
}
```

**响应 JSON 示例**

```json
{
  "agreementNo": "AGR202605180001",
  "status": 1,
  "endDate": "2026-05-18T10:30:00"
}
```

---

### 4.4 listAgreements — 查询绑卡列表

| 项 | 值 |
|----|-----|
| 方法 | `listAgreements` |
| 参数 | `com.baofu.wallet.account.api.dto.request.ListAgreementsRequest` |
| 返回 | `Result<ListAgreementsResponse>` |

**请求 JSON 示例**

```json
{
  "requestId": "req-20260518-0301",
  "contractNo": "WA2026051800001"
}
```

**响应 JSON 示例**

```json
{
  "contractNo": "WA2026051800001",
  "platformNo": "MCH400001",
  "agreementList": [
    {
      "agreementNo": "AGR202605180001",
      "contractNo": "WA2026051800001",
      "platformNo": "MCH400001",
      "cardUserName": "张*",
      "cardNo": "****0123",
      "lastCardNo": "0123",
      "mobileNo": "138****8000",
      "bankCode": "ICBC",
      "bankName": "中国工商银行",
      "cardType": "C",
      "bindType": 1,
      "bindOrder": 1,
      "protocolNo": "PROT20260518001",
      "status": 0,
      "createdAt": "2026-05-18T09:00:00",
      "updatedAt": "2026-05-18T09:00:00"
    }
  ]
}
```

---

### 4.5 queryAccountOpened — 查询是否已开户

| 项 | 值 |
|----|-----|
| 方法 | `queryAccountOpened` |
| 参数 | `com.baofu.wallet.account.api.dto.request.QueryAccountOpenedRequest` |
| 返回 | `Result<QueryAccountOpenedResponse>` |

**业务说明**：商户/前置在发起 H5 绑卡开户前调用。根据 `platformNo` + `certificateNo` 判断该用户在该平台下是否已有**正常**钱包账户。

**查询逻辑**：

1. `certificateNo` 按与落库相同规则加密后，匹配 `t_customer_base_info.certificate_no`
2. 关联 `t_customer_account`（`customer_no` + `platform_no`）
3. `accountOpened=true` 当且仅当：客户 `status=NORMAL` 且账户 `status=NORMAL`（已注销视为未开户）
4. 若存在多条（异常数据），返回最近创建的一条并记告警日志 `[TBD 治理策略]`

**请求 JSON 示例**

```json
{
  "requestId": "req-20260518-0401",
  "platformNo": "MCH400001",
  "certificateType": "ID",
  "certificateNo": "110101199001011234"
}
```

**响应 JSON 示例 — 已开户**

```json
{
  "accountOpened": true,
  "customerNo": "CUS202605180001",
  "contractNo": "WA2026051800001",
  "platformNo": "MCH400001",
  "certificateNo": "110101199001011234",
  "customerStatus": "NORMAL",
  "contractStatus": "NORMAL",
  "contractLevel": "I",
  "createdAt": "2026-05-18T09:00:00"
}
```

**响应 JSON 示例 — 未开户**

```json
{
  "accountOpened": false,
  "platformNo": "MCH400001",
  "certificateNo": "110101199001011234"
}
```

---

## 5. 数据模型（Apifox「数据模型」/ Java DTO）

字段与库表驼峰一致；`String`/`Integer`/`Long`/`BigDecimal`/`Date`/`LocalDate`/`LocalDateTime` 按 Java 惯例。

### 5.1 OpenAndBindRequest

| 字段 | Java 类型 | 必填 | 对应表/说明 |
|------|-----------|------|-------------|
| requestId | String | Y | 幂等键 |
| platformNo | String | Y | t_customer_account.platform_no |
| createdBy | String | Y | 审计 |
| customerBaseInfo | CustomerBaseInfoDTO | Y | t_customer_base_info |
| agreementList | List\<CustomerAgreementDTO\> | Y | t_customer_agreement，≥1 |

### 5.2 CustomerBaseInfoDTO

| 字段 | Java 类型 | 必填 | DB 列 |
|------|-----------|------|-------|
| customerType | String | Y | customer_type，默认 PERSON |
| customerName | String | Y | customer_name（加密） |
| nameIsEncry | Integer | N | name_is_encry，服务端写 |
| certificateType | String | Y | certificate_type |
| certificateNo | String | Y | certificate_no（加密） |
| certStartDate | LocalDate | N | cert_start_date |
| certExpiryDate | LocalDate | N | cert_expiry_date |
| gender | String | N | gender |
| birth | LocalDate | N | birth |
| nation | String | N | nation |
| issuingAuthority | String | N | issuing_authority |
| address | String | N | address |
| businessExtended | Integer | N | business_extended |
| businessTerm | LocalDate | N | business_term |
| registerCapital | Long | N | register_capital |
| businessScope | String | N | business_scope |
| corporateIdCardExtended | Integer | N | corporate_id_card_extended |
| corporateIdCardTerm | LocalDate | N | corporate_id_card_term |
| corporateIdCard | String | N | corporate_id_card |
| corporateName | String | N | corporate_name |

### 5.3 CustomerAgreementDTO（入参）

| 字段 | Java 类型 | 必填 | DB 列 |
|------|-----------|------|-------|
| cardUserName | String | Y | card_user_name（加密） |
| cardNo | String | Y | card_no（加密） |
| lastCardNo | String | N | last_card_no，服务端截取 |
| mobileNo | String | N | mobile_no（加密） |
| bankCode | String | Y | bank_code |
| bankName | String | Y | bank_name |
| cardType | String | Y | card_type，C/D |
| cnapsCode | String | N | cnaps_code |
| publicFlag | String | N | public_flag，默认 0 |
| bindType | Integer | Y | bind_type，1/2 |
| bindOrder | Integer | N | bind_order，服务端生成 |
| protocolNo | String | Y | protocol_no |
| remark | String | N | remark |
| depositBankProvince | String | N | deposit_bank_province |
| depositBankCity | String | N | deposit_bank_city |
| depositBankName | String | N | deposit_bank_name |

### 5.4 CustomerAgreementVO（出参/列表项）

在 DTO 基础上增加：

| 字段 | Java 类型 | DB 列 |
|------|-----------|-------|
| id | Long | id |
| agreementNo | String | agreement_no |
| contractNo | String | contract_no |
| platformNo | String | platform_no |
| status | Integer | status，0 正常 1 解绑 |
| endDate | LocalDateTime | end_date |
| endReason | String | end_reason |
| createdBy | String | created_by |
| createdAt | LocalDateTime | created_at |
| updatedBy | String | updated_by |
| updatedAt | LocalDateTime | updated_at |

### 5.5 QueryAccountOpenedRequest

| 字段 | Java 类型 | 必填 | DB 列 / 说明 |
|------|-----------|------|--------------|
| requestId | String | Y | 链路追踪 |
| platformNo | String | Y | t_customer_account.platform_no |
| certificateType | String | N | t_customer_base_info.certificate_type，默认 ID |
| certificateNo | String | Y | t_customer_base_info.certificate_no（入参明文，查询时加密匹配） |

### 5.6 QueryAccountOpenedResponse

| 字段 | Java 类型 | 必填 | 说明 |
|------|-----------|------|------|
| accountOpened | Boolean | Y | 是否已开户 |
| platformNo | String | Y | 回显 |
| certificateNo | String | N | 回显（脱敏 [TBD]） |
| customerNo | String | N | 已开户时返回 |
| contractNo | String | N | 已开户时返回，钱包账户号 |
| customerStatus | String | N | t_customer_base_info.status |
| contractStatus | String | N | t_customer_account.status |
| contractLevel | String | N | t_customer_account.contract_level |
| createdAt | LocalDateTime | N | 账户创建时间 t_customer_account.created_at |

### 5.7 BindCardRequest / UnbindCardRequest / ListAgreementsRequest

见第 4 节 JSON；`UnbindCardRequest` 中 `agreementNo` 与 `protocolNo`/`cardNo` 二选一。

### 5.8 OpenAndBindResponse

| 字段 | Java 类型 | 说明 |
|------|-----------|------|
| customerNo | String | 客户编号 |
| contractNo | String | 钱包账户号 |
| accountNo | String | 资金账号 |
| contractLevel | String | 默认 I |
| agreementList | List\<AgreementBriefVO\> | agreementNo、bindOrder、protocolNo、lastCardNo、status |

### 5.9 BindCardResponse / UnbindCardResponse / ListAgreementsResponse

与第 4 节响应 JSON 一致。

### 5.10 服务端落库默认值（非接口字段）

| 表 | 字段 | 开户默认值 |
|----|------|------------|
| t_customer_base_info | status | NORMAL |
| t_customer_account | contractType | ALL |
| t_customer_account | status | NORMAL |
| t_customer_account | contractLevel | I |
| t_customer_account_info | accountType | 00 |
| t_customer_account_info | accountSubType | BALANCE |
| t_customer_account_info | ccy | CNY |
| t_customer_account_balance | availableBalance | 0.00 |
| t_customer_account_balance | frozenBalance | 0.00 |
| t_customer_agreement | status | 0 |

---

## 6. Java 接口草案（供 IDEA 插件 / 代码生成）

```java
package com.baofu.wallet.account.api;

import com.baofu.common.api.Result;
import com.baofu.wallet.account.api.dto.request.*;
import com.baofu.wallet.account.api.dto.response.*;

/**
 * 钱包账户 Dubbo 服务 — 供钱包前置调用
 */
public interface WalletAccountFacade {

    /** 开户并绑卡 */
    Result<OpenAndBindResponse> openAndBind(OpenAndBindRequest request);

    /** 单独绑卡（4.0 成功后） */
    Result<BindCardResponse> bindCard(BindCardRequest request);

    /** 解绑卡（4.0 成功后） */
    Result<UnbindCardResponse> unbindCard(UnbindCardRequest request);

    /** 查询有效绑卡列表，按 bindOrder 升序 */
    Result<ListAgreementsResponse> listAgreements(ListAgreementsRequest request);

    /** 按平台号+证件号查询是否已开户 */
    Result<QueryAccountOpenedResponse> queryAccountOpened(QueryAccountOpenedRequest request);
}
```

```java
// Provider 示例
@DubboService(group = "wallet", version = "1.0.0", timeout = 3000)
public class WalletAccountFacadeImpl implements WalletAccountFacade { ... }
```

---

## 7. 错误码（Result.code）

| code | 说明 |
|------|------|
| 0000 | 成功 |
| 1001 | 参数校验失败 |
| 2001 | 账户不存在 |
| 2002 | 协议不存在 |
| 2003 | 卡已解绑 |
| 2004 | 客户已注销 |
| 3001 | 幂等重复（openAndBind） |
| 5000 | 系统异常 |

---

## 8. 与 HTTP 版文档关系

| 文件 | 用途 |
|------|------|
| `wallet-account-openapi-apifox.yaml` | **HTTP/OpenAPI**，仅适用于 HTTP 项目或网关 REST 透出；**不能导入 Dubbo 项目** |
| `wallet-account-dubbo-apifox.md`（本文） | **Dubbo 专用**，Apifox 手动建接口或 IDEA 同步 |

若对外仅暴露 Dubbo，请以 **本文档 + Java api 模块** 为准；HTTP YAML 可归档或删除。
