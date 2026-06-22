# 字段类型选型速查（金融场景）

## 数值类型

| 场景 | 推荐类型 | 禁止用 | 原因 |
|------|---------|--------|------|
| 金额（元） | `decimal(18,2)` | `float/double` | 浮点精度丢失 |
| 金额（分，整数存储） | `bigint(20)` | `int` | int 最大 21 亿分，约 2100 万元，高频场景会溢出 |
| 状态枚举（>2值） | `tinyint(4)` | `tinyint(1)` | tinyint(1) 被 JDBC 映射为 Boolean |
| 状态枚举（只有是/否） | `tinyint(1)` | `char(1)` | 语义清晰，存储节省 |
| 主键、外键 | `bigint(20)` | `int(11)` | 高并发系统 int 容易溢出 |
| 版本号（乐观锁） | `int(11) DEFAULT 0` | `bigint` | 版本号不需要 bigint |

---

## 时间类型

| 场景 | 推荐 | 说明 |
|------|------|------|
| 创建时间 | `timestamp DEFAULT CURRENT_TIMESTAMP` | 自动填入 |
| 更新时间 | `timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | **必须有 ON UPDATE** |
| 业务日期（不含时分秒） | `date` | 结算日期、到期日期 |
| 超过 2038 年的时间 | `datetime` | timestamp 有 2038 问题 |
| 存毫秒级时间戳 | `bigint(20)` | 可以，但可读性差，慎用 |

---

## 字符串类型

| 场景 | 推荐 | 说明 |
|------|------|------|
| 业务流水号（定长） | `char(32)` | MD5/UUID 长度固定，char 比 varchar 快 |
| 业务流水号（变长） | `varchar(64)` | 不要超过 64，否则索引效率下降 |
| 手机号 | `varchar(20)` | 国内 11 位，国际最长 15 位 |
| 姓名 | `varchar(50)` | 不要用 varchar(255) |
| 备注/描述 | `varchar(500)` | 超过 500 考虑 text，但 text 不能加索引 |
| 枚举字符串 | `varchar(32)` + 应用层枚举 | 比 int 枚举可读性好，但不要用 varchar(255) |
| 币种 | `char(3)` | ISO 4217 标准，CNY/USD/EUR 均为 3 位 |

---

## 索引选型

| 场景 | 建议 |
|------|------|
| 主键 | 自增 bigint，不用 UUID 做主键（写入性能差） |
| 唯一业务键 | UNIQUE INDEX，同时是幂等保障 |
| 时间范围查询 | 单独建 `idx_create_time`，不要和其他字段组合（除非总是联合查） |
| 高频 JOIN 字段 | 必须建索引，且类型必须和对端一致 |
| 低基数字段（状态、类型） | 单独建索引意义不大，考虑和时间或 member_id 组合 |
| 复合索引 | 最左前缀原则；把过滤性强的字段放左边 |

---

## 金融领域必备字段清单

### 所有业务主表

```sql
`id`          bigint(20)    NOT NULL AUTO_INCREMENT,
`deleted`     tinyint(4)    NOT NULL DEFAULT '0' COMMENT '软删除 0正常 1已删除',
`creator_id`  bigint(20)    DEFAULT NULL COMMENT '创建人ID',
`create_time` timestamp     NOT NULL DEFAULT CURRENT_TIMESTAMP,
`update_time` timestamp     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
`version`     int(11)       NOT NULL DEFAULT '0' COMMENT '乐观锁版本号',
```

### 批次聚合根额外需要

```sql
`total_count`   int(11)       DEFAULT '0' COMMENT '总条数',
`success_count` int(11)       DEFAULT '0' COMMENT '成功条数',
`fail_count`    int(11)       DEFAULT '0' COMMENT '失败条数',
`fail_reason`   varchar(500)  DEFAULT NULL COMMENT '失败原因',
`settle_type`   tinyint(4)    DEFAULT NULL COMMENT '结算类型 1=T+N 2=实时 3=手动',
`auditor_id`    bigint(20)    DEFAULT NULL COMMENT '审核人ID',
`auditor_name`  varchar(100)  DEFAULT NULL COMMENT '审核人名称',
`settle_time`   timestamp     DEFAULT NULL COMMENT '实际结算时间',
```

### 对外交互的流水表额外需要

```sql
`business_no`   char(32)      NOT NULL COMMENT '业务流水号（幂等键）',
`channel`       varchar(32)   DEFAULT NULL COMMENT '渠道',
`currency`      char(3)       DEFAULT 'CNY' COMMENT '币种 ISO 4217',
```

---

## 跨表一致性检查要点

关联字段类型必须完全一致，否则 JOIN 时隐式转换导致索引失效：

```sql
-- ❌ 明细表 int，批次表 bigint，JOIN 走不了索引
-- cm_acct_unsettle_target.member_id     int(11)
-- cm_acct_unsettle_target_batch.member_id bigint(20)

-- ✅ 统一为 bigint(20)
```

检查清单：
- [ ] `member_id` 类型跨表一致
- [ ] `account_id` 类型跨表一致  
- [ ] `batch_id` 外键类型与主键一致
- [ ] `state` 枚举值跨表一致（值和含义）
- [ ] `version` 初始值跨表一致（建议统一为 0）
