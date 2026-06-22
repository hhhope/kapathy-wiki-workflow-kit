# 中间件使用指南（扩展）

与 [repository-rules.md](repository-rules.md) §6 配套。配置项**统一走 Apollo**，键名使用 kebab-case 或点分，**禁止**在业务代码写死超时、重试、TTL。

---

## 1. 超时与重试（总则）

### 1.1 原则

| 原则 | 说明 |
|------|------|
| 配置外置 | 所有超时、重试、连接池参数在 Apollo，支持按环境覆盖 |
| 调用链一致 | 下游超时 < 上游超时，避免级联挂死 |
| 幂等才重试 | 写操作默认 `retries=0`；读操作可有限重试 |
| 可观测 | 超时/重试需打日志（含 traceId、接口名、耗时） |

### 1.2 推荐默认值（Apollo，可按服务调优）

| 配置键 | 建议默认 | 说明 |
|--------|----------|------|
| `dubbo.consumer.timeout` | `3000` | 消费方调用超时（ms） |
| `dubbo.provider.timeout` | `5000` | 提供方执行超时（ms），≥ consumer |
| `dubbo.consumer.retries` | `0` | 非幂等接口必须为 0 |
| `dubbo.consumer.check` | `false` | 启动不强依赖提供方（按环境） |
| `http.client.connect-timeout` | `3000` | HTTP 连接超时（ms） |
| `http.client.read-timeout` | `10000` | HTTP 读超时（ms） |
| `http.client.connection-request-timeout` | `3000` | 从连接池取连接超时（ms） |

### 1.3 Dubbo

- **接口级**优先：在 facade 接口 `@DubboService` / 消费方 `@DubboReference` 用 `timeout`、`retries`，值引用配置占位或统一常量，**禁止**魔法数字散落在 adapter/application
- **全局默认**在 `application.yml` 或 Apollo：

```yaml
dubbo:
  consumer:
    timeout: ${dubbo.consumer.timeout:3000}
    retries: ${dubbo.consumer.retries:0}
  provider:
    timeout: ${dubbo.provider.timeout:5000}
```

- 慢查询/批处理接口：单独命名空间或 `dubbo.consumer.timeout.{interfaceName}` 覆盖
- **禁止**无超时调用；**禁止** consumer.timeout > 网关/上游 SLA

### 1.4 HTTP（RestTemplate / WebClient / Feign）

- 封装在 `infrastructure` 的 `*HttpClient` / `*Gateway`，application 只调端口接口
- 每个下游系统一组超时配置：

```properties
# Apollo 示例
http.client.{downstream}.connect-timeout=3000
http.client.{downstream}.read-timeout=10000
```

- 连接池：`max-total`、`max-per-route` 走配置；禁止每请求 new 客户端
- 对外暴露的 HTTP API：在网关层设超时；服务内 Controller 不做长阻塞（>30s 改异步+回调/MQ）

### 1.5 超时层级示例

```text
网关(60s) > BFF(30s) > 本服务 Dubbo consumer(3s) > 下游 Dubbo provider(5s) > DB(2s)
```

---

## 2. Redis

### 2.1 模块与职责

| 用途 | 模块 | 说明 |
|------|------|------|
| 缓存 | infrastructure | `*CacheRepository`，key 规范见下 |
| 分布式锁 | infrastructure | 统一 `DistributedLock` 端口 + 实现 |
| 限流/幂等 | infrastructure 或 common 组件 | 与锁区分 key 前缀 |

- **禁止**在 domain 直接依赖 `RedisTemplate` / `RedissonClient`
- 连接、密码、集群节点：**仅 Apollo**

### 2.2 Key 命名

```text
{app}:{env}:{biz}:{resource}[:{id}]
```

示例：`account-subscribe:pro:subscription:config:{merchantId}`

- 必须设置 **TTL**（缓存）；业务含义的 TTL 定义为 common 常量或配置项
- PRD 类「缓存 ≤5s」场景：`ttl` 走 Apollo，默认 ≤5s，禁止写死 `5000` 在代码里

### 2.3 分布式锁（Redis）

**首选 Redisson**（或团队统一的 `SET key value NX PX` + Lua 解锁封装）。

| 规则 | 要求 |
|------|------|
| 锁粒度 | 业务资源级，如 `orderId`、`accountId`，禁止全局大锁 |
| Key | `{app}:lock:{biz}:{resourceId}` |
| 租约 | 必须 `leaseTime`，防止死锁；评估业务最长执行时间 × 1.5 |
| 等待 | `tryLock(waitTime, leaseTime, unit)`，禁止无限 `lock()` |
| 释放 | `finally` 中释放；必须校验 lock token（Redisson 自带） |
| 可重入 | 默认可重入；跨线程禁止误用 |
| 与事务 | 锁范围 > 事务范围；先拿锁再开事务，先提交事务再释锁 |

```java
// 模式示例（application 层）
if (lock.tryLock("subscription", accountId, 3, 30, SECONDS)) {
    try {
        // 业务
    } finally {
        lock.unlock("subscription", accountId);
    }
} else {
    throw new BizException(ErrorCode.LOCK_CONFLICT);
}
```

- **禁止**：用缓存 key 兼做锁、用 `SETNX` 不设过期、释锁不校验 value
- 高并发抢锁失败：返回明确错误码，禁止吞异常

### 2.4 与 DB 一致性

- 缓存更新：**先 DB 后删缓存** 或 Canal/订阅 binlog；禁止只更新缓存
- 双写场景：以 DB 为准，缓存 TTL 作为兜底

---

## 3. Zookeeper 锁与协调

### 3.1 适用场景

| 适用 | 不适用 |
|------|--------|
| 选主、调度互斥、低频资源协调 | 高 QPS 业务分布式锁（用 Redis） |
| 与 Dubbo 注册中心同集群的轻量互斥 | 长时间持锁（>分钟级） |

- 使用 **Curator** `InterProcessMutex` / `InterProcessSemaphoreMutex`
- 实现放在 **infrastructure**，对上层暴露 `ClusterLock` 或复用 `DistributedLock` 的 ZK 实现

### 3.2 ZNode 路径

```text
/{app}/locks/{biz}/{resourceId}
```

示例：`/account-subscribe/locks/subscription/acc_12345`

- 创建 **Ephemeral Sequential** 节点语义由 Curator 封装，不手写原生 ZK API
- `lock.acquire(timeout, unit)` 必须带超时；`release()` 在 `finally`
- Session 超时、重连策略走 Apollo，与 Dubbo 注册 ZK 配置分离命名空间

### 3.3 Redis vs ZK 选型

| 维度 | Redis 锁 | ZK 锁 |
|------|----------|-------|
| 性能 | 高 | 中低 |
| 一致性 | 租约 + 红锁视集群而定 | 强一致 |
| 典型用途 | 订单、账户、防重提交 | 定时任务单实例、Leader 选举 |

**默认业务防重/并发控制用 Redis；** 仅当已有 ZK 且为协调类场景时用 ZK。

---

## 4. MQ（RocketMQ / 通用 MQ）

### 4.1 模块

| 组件 | 模块 |
|------|------|
| Producer 封装 | infrastructure |
| Consumer 监听 | adapter（或 infrastructure + adapter 薄委托） |
| 消息体 DTO | facade 或 common（与外部契约一致时放 facade） |

### 4.2 命名

| 类型 | 格式 | 示例 |
|------|------|------|
| Topic | `{app}_{biz}_{event}` | `account_subscribe_order_paid` |
| Consumer Group | `{app}_{biz}_{consumer}` | `account_subscribe_notify_consumer` |
| Tag | 业务子类型 | `CREATE` / `CANCEL` |

### 4.3 发送

- 同步发送：核心链路、需明确成功/失败
- 异步发送：非核心通知；仍需 Callback 打日志
- **消息 Key** = 业务主键（orderId、requestId），便于排查
- 消息体含：`messageId`、`traceId`、`timestamp`、`payload`
- 事务消息：仅在与本地 DB 强一致时使用；实现放 infrastructure

### 4.4 消费

- **幂等**：消费前查幂等表/Redis(`{app}:mq:idempotent:{msgId}`)，已处理则 ack 跳过
- **重试**：遵循 Broker 重试阶梯；超过次数进 **DLQ（死信）**，禁止无限 reconsume
- 单条消费逻辑 < 30s；更长流程拆单或转异步任务
- 异常分类：不可重试（参数错误）→ 进 DLQ；可重试（下游超时）→ 重试
- 禁止在 Consumer 里直接调 Mapper，经 application 服务

### 4.5 配置（Apollo）

```properties
mq.{biz}.topic=...
mq.{biz}.consumer.group=...
mq.{biz}.consume-thread-min=5
mq.{biz}.consume-thread-max=20
mq.{biz}.send-timeout=3000
```

---

## 5. Kafka

### 5.1 适用

- 日志采集、大数据管道、高吞吐事件流；**核心业务强一致**仍优先事务 MQ（按团队标准）

### 5.2 规范

| 项 | 规范 |
|----|------|
| Topic | `{app}.{biz}.{event}` 或团队统一前缀 |
| Consumer Group | `{app}-{biz}-{purpose}` |
| Key | 业务分区键（accountId），保证同键有序 |
| acks | 重要事件 `all`；日志类可用 `1` |
| 序列化 | 团队统一 JSON / Avro，禁止混用 |
| 提交 | 业务处理成功后再 `commitSync`/`ack`；处理失败不提交 |

### 5.3 模块与配置

- Producer/Consumer 工厂在 **infrastructure**
- `spring.kafka.*` 或原生客户端参数全部 Apollo：

```properties
kafka.bootstrap-servers=...
kafka.consumer.group-id=...
kafka.consumer.max-poll-records=100
kafka.consumer.session-timeout-ms=30000
kafka.producer.acks=all
kafka.producer.retries=3
```

- 消费幂等同 MQ；大消息走对象存储（DFS），Kafka 只传引用

---

## 6. DFS（分布式文件存储）

### 6.1 模块

- 客户端封装在 **infrastructure**（FastDFS / MinIO / OSS 等）
- 对 application 暴露 `FileStorageService` 端口：上传、下载、预签名 URL

### 6.2 路径与元数据

```text
/{biz}/{yyyyMMdd}/{uuid}.{ext}
```

- 返回 **访问 URL 或 fileId**，禁止把内网物理路径返回给调用方
- 元数据（原始文件名、大小、MIME、上传者）入 DB，文件入 DFS
- 敏感文件：私有桶 + **短时预签名 URL**，禁止永久 public URL

### 6.3 约束

| 规则 | 说明 |
|------|------|
| 大小限制 | 上传前校验，配置 `dfs.max-file-size` |
| 类型白名单 | 配置允许 MIME/扩展名 |
| 病毒扫描 | 生产按安全要求对接（异步） |
| 密钥 | endpoint/accessKey 仅 Apollo，禁止入库 |

---

## 7. 中间件引入检查清单

新增任一中间件时 PR 需包含：

- [ ] 父 POM `dependencyManagement` 登记版本
- [ ] 依赖落在正确模块（见上文表格）
- [ ] Apollo 键名清单与 DEV 默认值
- [ ] 超时/重试/TTL 无魔法值
- [ ] 日志与监控（Micrometer/自定义 metric）埋点
- [ ] `.harness/memory/MEMORY.md` 更新
- [ ] 回滚方案（关闭开关或降级读 DB）

---

## 8. 配置键索引（复制到 Apollo 模板）

```properties
# Dubbo
dubbo.consumer.timeout=3000
dubbo.consumer.retries=0
dubbo.provider.timeout=5000

# HTTP
http.client.connect-timeout=3000
http.client.read-timeout=10000

# Redis
redis.lock.default-wait-ms=3000
redis.lock.default-lease-ms=30000
redis.cache.default-ttl-seconds=300

# ZK
zk.lock.default-wait-ms=5000

# MQ
mq.send-timeout-ms=3000

# Kafka
kafka.producer.acks=all
kafka.consumer.max-poll-records=100

# DFS
dfs.max-file-size-bytes=10485760
dfs.presign-expire-seconds=3600
```
