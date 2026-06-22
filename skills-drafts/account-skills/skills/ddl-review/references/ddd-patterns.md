# 金融领域 DDD 常见模式

## 值对象（Value Object）

### 账户值对象

账户在支付系统中通常由两个字段联合定义，这是一个典型的值对象：

```sql
-- ❌ 拆散写在表里的写法（四张表各写一遍）
account_id       bigint  NOT NULL
account_id_type  int     NOT NULL

-- ✅ 值对象应封装为独立概念
-- Java 侧：AccountId { Long id; AccountType type; }
-- 数据库侧：列名和类型至少要跨表统一
```

**识别信号：** 同一对字段（id + type / no + type）在多张表重复出现超过 2 次。

**改动代价说明：** 已上线的字段无法轻易合并，但可以：
1. 在领域层封装值对象，让应用代码不直接操作裸字段
2. 后续新表不再重复，统一用 account_ref_id + account_ref_type 命名

---

## 聚合根（Aggregate Root）

### 批次-明细聚合

```
Batch（聚合根）
  ├── 持有：total_count, success_count, fail_count, balance
  ├── 状态机：PENDING → PROCESSING → SETTLED / FAILED
  └── Item（聚合内实体）[]
        ├── 持有：balance, state
        └── 状态机：PENDING → SETTLED / FAILED

不变性约束：
  sum(Item.balance) == Batch.balance
  all(Item.state == SETTLED) => Batch.state == SETTLED
  any(Item.state == FAILED) => Batch.fail_count++
```

**缺少聚合根约束的症状：**
- 批次表和明细表各自有 balance，没有 sum 校验
- 批次状态靠定时任务扫描明细来更新，而不是在聚合根写入时触发
- 明细可以在批次已结算后再更新（无聚合根保护）

---

## BC（限界上下文）划分

### 结算域典型 BC 划分

```
支付 BC（Payment）
  └── 负责：交易受理、资金冻结、支付成功事件
  
结算 BC（Settlement）
  └── 负责：待结算记录生成、T+N 到期结算、批次管理
  └── 消费：支付成功事件（防腐层：PaymentSettledEvent）
  
退款 BC（Refund）
  └── 负责：退款申请、退款执行、退款到账
  └── 消费：结算记录（通过 Anti-Corruption Layer）
```

**判断是否需要拆 BC：**

| 信号 | 判断 |
|------|------|
| 两张表结构相似但字段有差异 | 先问：这两个流程的触发条件、执行人、审批规则是否独立？是 → 不同 BC |
| 正向流水和退款流水共用同一批次表 | 混用 → BC 边界模糊，退款应有自己的聚合根 |
| `deal_code` 区分业务类型，但状态机逻辑不同 | 用 deal_code 区分但状态机差异大 → 应拆表或拆 BC |

---

## 扩展字段治理

### 核心表膨胀的识别

```sql
-- 症状：核心结算表里出现业务线专属字段
bzz_flag          tinyint  -- 保证金业务线
cbpay_flag        tinyint  -- 跨境购汇业务线
cbpay_notify_state tinyint -- 跨境购汇业务线

-- 问题：每加一个业务线，主表就加字段
-- 三年后主表可能有 60+ 字段，80% 对某条记录是 NULL
```

### 推荐的扩展模式

**方案 A：扩展属性表（适合字段多且稀疏）**
```sql
CREATE TABLE cm_acct_unsettle_ext (
  id         bigint PRIMARY KEY,
  unsettle_id bigint NOT NULL,  -- 关联主表
  ext_type   varchar(32),       -- 扩展类型：CBPAY / BZZ
  ext_key    varchar(64),       -- 字段名
  ext_value  varchar(256),      -- 字段值（JSON 或字符串）
  INDEX (unsettle_id, ext_type)
)
```

**方案 B：业务线扩展表（适合字段少且固定）**
```sql
CREATE TABLE cm_acct_unsettle_cbpay_ext (
  unsettle_id    bigint PRIMARY KEY,
  cbpay_flag     tinyint(4),
  notify_state   tinyint(4),
  -- 只有跨境记录才有这张表的数据
)
```

---

## 事件溯源（Event Sourcing for Settlement）

### 最小化审计日志表

结算域不需要完整事件溯源，但需要状态变更日志：

```sql
CREATE TABLE cm_settle_event_log (
  id          bigint PRIMARY KEY AUTO_INCREMENT,
  biz_type    varchar(32)  NOT NULL COMMENT '业务类型：BATCH/ITEM',
  biz_id      bigint       NOT NULL COMMENT '业务ID',
  from_state  tinyint      NOT NULL COMMENT '变更前状态',
  to_state    tinyint      NOT NULL COMMENT '变更后状态',
  operator_id bigint       COMMENT '操作人（系统操作填0）',
  reason      varchar(256) COMMENT '变更原因/错误原因',
  create_time timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_biz (biz_type, biz_id),
  INDEX idx_create_time (create_time)
) COMMENT = '结算状态变更日志';
```

**触发时机：** 任何改变 state 字段的操作都必须同时写一条 event_log，用同一个事务保证。
