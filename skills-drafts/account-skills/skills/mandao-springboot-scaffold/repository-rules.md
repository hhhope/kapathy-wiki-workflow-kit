# Mandao 仓库级规范（Repository Rules）

适用于本模板衍生的所有 Java 微服务仓库。Cursor 规则摘要见 `.cursor/rules/`；本文档为完整参考。

---

## 1. Maven 依赖规则

### 1.1 版本管理

- **唯一版本源**：根 `pom.xml` 的 `<properties>` + `<dependencyManagement>`
- 子模块依赖**不写 `<version>`**（除非注释说明的例外）
- 使用 `${revision}` + `flatten-maven-plugin` 统一 CI 友好版本
- 禁止在子模块覆盖父 POM 已管理的 Spring Boot / Dubbo / MyBatis 主版本

### 1.2 依赖声明顺序

子模块 `<dependencies>` 建议顺序：

1. 本工程其他模块（common → 上层）
2. Spring / Spring Boot starters
3. 中间件（Dubbo、MyBatis、Apollo 等）
4. 工具库（Hutool、Guava、commons-lang3）
5. 测试依赖（scope=test）

### 1.3 允许 / 禁止的依赖

| 规则 | 说明 |
|------|------|
| ✅ 上层依赖下层 | start 可依赖 adapter、infrastructure、common |
| ❌ 下层依赖上层 | common 不得依赖 domain/application/adapter |
| ❌ domain 依赖 Spring | domain 仅纯 Java + 允许的 util |
| ❌ facade 依赖 infrastructure | API 契约与实现分离 |
| ✅ facade 依赖 dubbo（API 注解） | 仅 `dubbo` 核心，非 starter |
| ❌ 随意引入新 starter | 新中间件须在父 POM 登记版本并在本文档或 MEMORY 说明用途 |

### 1.4 部署属性

- 除 `common`、`facade` 外，业务模块设置 `<maven.deploy.skip>true</maven.deploy.skip>`
- `facade` 单独发布供调用方依赖；`common` 随 facade 传递

### 1.5 编译插件

- `maven-compiler-plugin` 配置 Lombok + MapStruct 注解处理器路径（与父 POM 一致）
- 需要 MapStruct 的模块显式依赖 `mapstruct`；processor 在父级或模块 scope=provided

---

## 2. 模块依赖与分层规则

### 2.1 依赖方向（严格）

```text
start → adapter → application → domain → infrastructure → facade → common
```

**无反向依赖。** 若下层需要上层能力：上移接口到 domain/facade，或抽到 common。

### 2.2 各层职责

| 层 | 放什么 | 不放什么 |
|----|--------|----------|
| common | 常量、枚举、异常、通用 Result、工具 | 业务编排、DB、RPC 实现 |
| facade (api) | Dubbo 接口、Req/Resp/DTO | 实现类、Spring 注解 |
| domain | 实体、值对象、领域服务、**仓储接口** | MyBatis Mapper、@Service |
| application | 应用服务、用例编排、事务边界 | HTTP/Dubbo 入口 |
| infrastructure | Mapper、仓储实现、外部 Client | 对外 API 定义 |
| adapter | Controller、Dubbo Provider、消息监听 | 复杂领域逻辑 |
| start | 启动类、全局配置、组件扫描 | 业务代码 |

### 2.3 跨模块引用

- 应用服务只通过 **domain 仓储接口** 或 **infrastructure 已注入的 Bean** 访问数据，避免 adapter 直调 Mapper
- 模块间 DTO 转换：优先 **MapStruct**，转换器放在 application 或 infrastructure，不放在 domain

---

## 3. 类名与包名规则

### 3.1 通用命名

| 元素 | 规范 | 示例 |
|------|------|------|
| 包名 | 全小写，点分 | `com.mandao.account.subscribe.domain` |
| 类名 | PascalCase | `AccountSubscriptionService` |
| 方法/字段 | camelCase | `findByAccountId` |
| 常量 | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| 表名 | snake_case | `account_subscription` |
| YAML 配置项 | kebab-case | `spring.application.name` |

### 3.2 类型后缀（推荐）

| 后缀 | 层次 | 含义 |
|------|------|------|
| `*Application` | start | Spring Boot 入口 |
| `*Facade` / `*Service`（接口在 api 包） | facade | Dubbo 对外 API |
| `*Service` | application | 应用服务 |
| `*DomainService` | domain | 领域服务 |
| `*Repository` | domain | 仓储接口 |
| `*RepositoryImpl` / `*Mapper` | infrastructure | 持久化 |
| `*Controller` / `*Provider` | adapter | HTTP / Dubbo 实现 |
| `*Req` / `*Resp` / `*DTO` | facade | 传输对象 |
| `*DO` / `*PO` | infrastructure | 数据对象 |
| `*Converter` / `*Mapper`（MapStruct） | application/infra | 对象转换 |
| `*Enum` | common/domain | 枚举 |
| `*Constants` | common | 常量类 |

### 3.3 禁止的类名

- 无业务含义的 `Util`、`Helper` 泛滥；单一职责工具可 `XxxUtils`
- 禁止 `Manager`、`Handler` 除非团队已有统一语义
- 禁止与 JDK/Spring 冲突的短名类（如单独 `Service`、`Config`）

---

## 4. 魔法值规则

### 4.1 定义

**魔法值**：代码中出现的、能表达业务或协议含义的字面量（数字、字符串、状态码），未通过命名常量/枚举/配置暴露。

### 4.2 必须提取的场景

| 场景 | 放置位置 |
|------|----------|
| 业务状态码、错误码 | `common` 枚举或 `ErrorCode` 常量类 |
| 字典类固定取值 | 枚举 `{Business}StatusEnum` |
| 对外协议字段名 | facade 常量或注解文档 |
| 重试次数、超时、分页默认 | `common` 常量或 `@ConfigurationProperties` |
| 缓存 key 前缀 | `{Module}CacheConstants` |
| 日志业务标识 | 使用枚举/常量，避免重复字符串 |

### 4.3 允许字面量的场景

- 单元测试中的 given 数据
- 日志模板中的固定标点（非业务语义）
- 注解属性 `value = "..."` 且仅此一处
- `0`、`1` 用于循环/数组下标且无业务含义

### 4.4 配置 vs 常量

| 类型 | 用法 |
|------|------|
| 环境相关、可运维调整 | Apollo / `application.yml` + `@Value` 或 `@ConfigurationProperties` |
| 全环境不变的业务规则 | `common` 常量或枚举 |
|  secrets | **仅** Apollo 密文或密钥服务，禁止进 Git |

---

## 5. Git 与提交规则

### 5.1 分支命名

- 功能：`feature/<short-description>`
- 修复：`fix/<issue-id>-<short-description>`
- 个人开发：`user/<username>/<date>`

### 5.2 Commit Message（Conventional Commits）

```text
<type>(<scope>): <subject>

<body>
```

| type | 用途 |
|------|------|
| feat | 新功能 |
| fix | 缺陷修复 |
| refactor | 重构 |
| test | 测试 |
| docs | 文档 |
| chore | 杂项 |
| build | 构建/依赖 |

- `scope`：模块或领域，如 `domain`、`adapter`、`facade`
- `subject`：祈使句、小写开头、无句号、≤72 字符
- `body`：说明 why，非必需

示例：

```text
feat(domain): add AccountSubscription entity

fix(adapter): handle null response from downstream RPC
```

### 5.3 提交前检查

- `mvn clean compile` 或相关模块测试通过
- 不提交 `target/`、`.flattened-pom.xml`、IDE 配置、密钥文件

---

## 6. 中间件引入与使用规则

### 6.1 Dubbo

- **接口**定义在 `facade`（`api` 包），**实现**在 `adapter`（`@DubboService`）
- `dubbo.scan.base-packages` = `{basePackage}`（根包，覆盖 adapter）
- 应用名与 `spring.application.name` 一致
- 超时、重试、版本号在接口注解或 Apollo 配置，不散落在业务代码

### 6.2 MyBatis

- Mapper 接口与 XML 仅在 `infrastructure`
- `@MapperScan(basePackages = "{basePackage}.infrastructure")` 仅在 start 主类
- SQL 禁止 `SELECT *`；表名/字段与 DO 映射一致（snake_case → camelCase）
- 多数据源使用 `dynamic-datasource`，配置在 Apollo

### 6.3 Apollo

- `apollo.bootstrap.enabled=true`，命名空间默认 `application`
- `apollo-configuration.properties`：`app.id`、`env`、`idc` 使用 Maven 资源过滤 `@apollo.env@`
- Profile：DEV（默认）、UAT、PRO — 与 `.harness/docs/git-workflow.md` 一致
- 禁止在仓库提交生产密钥、数据库密码

### 6.4 MySQL

- 驱动由 infrastructure 引入；连接池、URL 走配置中心
- 迁移脚本放独立目录（如 `db/migration`），与代码变更同 PR 说明

### 6.5 Spring Web

- 对外 HTTP 入口在 `adapter`
- 统一健康检查：start 模块 `GET /monitor` 返回 `OK`
- Actuator 暴露 `health,info`，生产环境收紧暴露面

### 6.6 超时与重试（Dubbo / HTTP）

- 所有超时、重试、连接池参数走 **Apollo**，禁止业务代码魔法数字
- 默认参考：`dubbo.consumer.timeout=3000`、`dubbo.consumer.retries=0`（非幂等）、`dubbo.provider.timeout=5000`、`http.client.connect-timeout=3000`、`http.client.read-timeout=10000`
- 原则：**下游超时 < 上游超时**；慢接口单独配置键覆盖
- Dubbo：timeout/retries 在 facade 注解或全局配置声明，不散落 adapter
- HTTP：RestTemplate/WebClient 封装在 infrastructure，按下游系统一组 `http.client.{name}.*` 配置
- 详情：[middleware-guide.md](middleware-guide.md) §1

### 6.7 Redis（缓存与分布式锁）

- 客户端与锁实现仅在 **infrastructure**；domain 通过端口接口使用
- Key：`{app}:{env}:{biz}:{resource}[:{id}]`；缓存必须 TTL
- **分布式锁**：优先 Redisson；必须 `tryLock(wait, lease)` + `finally` 释放；Key 前缀 `{app}:lock:{biz}:`
- **禁止**无限等待、无租约、用缓存 key 当锁、释锁不校验 token
- 高 QPS 并发控制用 Redis，不用 ZK
- 详情：[middleware-guide.md](middleware-guide.md) §2

### 6.8 Zookeeper 锁与协调

- 使用 Curator `InterProcessMutex`；路径 `/{app}/locks/{biz}/{resourceId}`
- 适用：选主、调度互斥、低频协调；**不适用**高 QPS 业务锁
- 必须带 acquire 超时；实现放 infrastructure
- 详情：[middleware-guide.md](middleware-guide.md) §3

### 6.9 MQ（RocketMQ 等）

- Producer 在 infrastructure；Consumer 在 adapter（委托 application）
- Topic：`{app}_{biz}_{event}`；Group：`{app}_{biz}_{consumer}`；消息 Key = 业务主键
- **幂等消费** + 死信队列；禁止无限重试；Consumer 不直调 Mapper
- 详情：[middleware-guide.md](middleware-guide.md) §4

### 6.10 Kafka

- 工厂在 infrastructure；Topic `{app}.{biz}.{event}`；重要消息 `acks=all`
- 业务成功后再提交 offset；幂等同 MQ；大 payload 传 DFS 引用
- 详情：[middleware-guide.md](middleware-guide.md) §5

### 6.11 DFS（分布式文件）

- 客户端 infrastructure；暴露 `FileStorageService` 端口
- 路径 `/{biz}/{yyyyMMdd}/{uuid}.{ext}`；返回 URL/fileId，不返回内网物理路径
- 敏感文件私有桶 + 短时预签名；大小与类型白名单走配置
- 详情：[middleware-guide.md](middleware-guide.md) §6

### 6.12 新增中间件流程

1. 在父 POM 增加 version 属性 + dependencyManagement
2. 在最贴近职责的模块引入依赖
3. 更新 `.harness/memory/MEMORY.md` 与本文档
4. 提供 Apollo 键名清单、默认值、回滚说明
5. 完成 [middleware-guide.md](middleware-guide.md) §7 检查清单

---

## 7. 代码风格与其它

- Java 21，开启 preview 特性需团队评审
- 使用 Lombok 减少样板代码，domain 层慎用
- 领域模型无 Spring 注解；事务在 application 层 `@Transactional`
- 异常：业务异常继承 common 中统一基类，不裸抛 `RuntimeException` 含魔法消息
- 日志：SLF4J，关键业务带可检索业务号，避免 `System.out`

---

## 8. 与 Cursor 规则的关系

| 文件 | 范围 |
|------|------|
| `mandao-core-standards.mdc` | 命名、魔法值、分层总则 |
| `mandao-maven.mdc` | `**/pom.xml` |
| `mandao-module-layers.mdc` | `**/*.java` |
| `mandao-git-commit.mdc` | 始终 |
| `mandao-middleware.mdc` | 中间件总则 |
| `mandao-middleware-timeouts.mdc` | Dubbo/HTTP 超时 |
| `mandao-middleware-locks.mdc` | Redis/ZK 锁 |
| `mandao-middleware-messaging.mdc` | MQ/Kafka |
| `mandao-middleware-dfs.mdc` | 分布式文件 |

完整说明：[middleware-guide.md](middleware-guide.md)

新建项目时复制 `.cursor/rules/` 与 `.cursor/skills/mandao-springboot-scaffold/` 到新仓库根目录。
