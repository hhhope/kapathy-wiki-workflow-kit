---
name: exception-handler
description: Use when implementing or adapting DDD Spring Boot exception handling, ErrorCode models, global exception handlers, error-code tables, MQ consumer exception handling, Dubbo exception propagation, or Feign error decoding.
---

# 异常处理组件 Skill

## Skill 说明

本 skill 封装了完整的异常处理组件设计决策，用于在 **DDD 领域模型 + Spring Boot 3 + JDK 21** 架构下，生成**可直接使用的代码骨架**。所有设计决策已固化，AI 的职责是按规范生成代码，不重复讨论已定稿的设计。

参考示例见 `references/example-order-bc.md`（Order BC 完整代码示例）。

---

## 已固化的核心设计决策

在生成任何代码前，必须理解以下决策，**不得偏离**：

| 决策项 | 选定方案 | 原因 |
|--------|----------|------|
| 错误码载体 | Enum + DB 双轨 | Enum 管结构，DB 管文案和策略，支持热更新 |
| DB 主键 | Enum name（如 ORDER_NOT_FOUND） | ordinal 不稳定，name 永远不变 |
| 序号生成 | ordinal + 1 自动生成 | 团队规范保障只在末尾追加 |
| 异常类 | 抽象类层次 | 强制子类携带必要字段 |
| ErrorType | BIZ / SYS / PARAM / INFRA 四种 | INFRA 单独拆出，告警策略与 SYS 不同 |
| gRPC 映射 | GrpcStatusMapper 单独维护 | interface 保持干净，非 gRPC 服务不实现无意义方法 |
| 对外码粒度 | BIZ 细粒度，SYS 统一 SYS-ERROR | 安全：内部系统细节不对外暴露 |
| 国际化 | DB 按 locale 存文案 | 支持多语言，支持运营热更新 |
| MQ | 多种并存（RocketMQ/Kafka/RabbitMQ） | 抽象统一接口，各 MQ 独立适配 |
| Dubbo 返回风格 | 统一 Result-T 包装 | 错误传递透明，不依赖 Java 序列化传异常 |
| JDK 21 特性 | 保守使用 | 不引入 sealed class，优先稳定性 |

---

## 模块结构：基于当前项目 + QA 确认落位

**不预设固定模块名**。先识别当前项目的模块结构（如根 pom 的 `<modules>` 或工程目录），再通过 QA 与用户确认「每类能力写入哪个现有模块、包名是什么」，将确认结果写入 `confirm-and-edit.md` 或项目内约定文档，再按该结果生成代码。

### 第一步：识别当前项目模块

- 读取根 pom 的 `<modules>` 或列出项目顶层目录，得到**现有模块列表**（如 `account-common`、`account-domain`、`account-start` 等）。
- 若项目无多模块，则视为单模块，列出可用的包路径（如 `com.xxx.common`）。

### 第二步：QA 确认（逐项询问或提供选项由用户勾选/填写）

将下表交给用户确认或填写，**确认结果必须落档**（写入 confirm-and-edit 或同等文档）：

| 能力分类 | 说明 | 请选择落位模块（填现有模块名） | 包名（如 com.xxx.common.exception） |
|----------|------|-------------------------------|--------------------------------------|
| **异常核心** | ErrorCode、ErrorType、BaseException、DomainException、CommonErrorCode 等，零框架依赖 | 例：account-common | 例：com.mandao.account.common.exception |
| **配置与解析** | ErrorCodeConfig、Cache、ErrorMessageResolver、DDL 脚本，需 Spring + JDBC | 同上或独立模块 | 例：同上 .config 子包 |
| **REST 出口** | ErrorResponse、GlobalExceptionHandler | 同上或启动层/适配层 | 例：同上 .web 子包 |
| **gRPC 出口** | GrpcStatusMapper 等 | 可选，填模块或「不做」 | 可选 |
| **MQ 消费** | MqConsumerExceptionHandler、DefaultMqExceptionHandler | 可选 | 可选 .mq 子包 |
| **Dubbo 双端** | RpcErrorEnvelope、Provider Filter、ResultUnwrapper | 可选 | 可选 .dubbo / .rpc 子包 |
| **Feign 适配** | FeignExceptionDecoder、FeignTraceInterceptor | 可选 | 可选 .feign 子包 |
| **starter 装配** | AutoConfiguration 按 classpath 装配 | 可选，或合入上述某模块 | 可选 |

- 可补充一问：「是否全部落入同一模块（如 XX-common）？」若用户选是，则上表除「落位模块」统一外，包名按同一根包 + 子包（.code、.config、.web…）约定。

### 第三步：落档与执行

- 将用户确认的**落位模块 + 包名**写入 `confirm-and-edit.md`（或当前任务约定的「需确认/可修改」文档），格式清晰可回溯。
- 后续 Part 1～Part 11 的代码生成**严格按该文档中的模块与包名**落位；若文档中无某项，则按「不做」或与用户再确认。

### 参考：能力与常见落位对应（仅参考，以 QA 结果为准）

| 能力 | 依赖要求 | 常见落位 |
|------|----------|----------|
| 异常核心 | 仅 slf4j，零 Spring | 公共/通用模块 |
| 配置与解析 | Spring、JdbcTemplate | 同上有 JDBC 的模块，或 config 模块 |
| REST 出口 | Spring Web | 通用模块或 adapter/start |
| gRPC/MQ/Dubbo/Feign | 对应 classpath | 同上或独立 adapter 模块 |

---

## Part 1：ErrorCode Interface（落位到 QA 确认的模块/包，下同）

以下各 Part 的**包名与落位模块**均以「模块结构：基于当前项目 + QA 确认落位」的落档结果为准；示例中的 `com.example.exception` 仅为占位，生成时**替换为 QA 确认的包名**。

### 1.1 接口定义规范

```java
// package 以 QA 确认的「异常核心」包为准，如 com.mandao.account.common.exception.code
package com.example.exception.core.code;

public interface ErrorCode {

    // ── 必须实现（每个 Enum 定义）──────────────────────────
    ErrorType getType();
    String getBcPrefix();               // 限界上下文前缀，如 "ORDER"
    String getBcExternalPrefix();       // 对外码前缀，如 "ORD"
    String getDefaultMessage();         // 兜底文案（中文硬编码）
    boolean isRetryable();              // MQ 消费失败是否允许重试

    // ── default 实现（Enum 不需要重复写）───────────────────
    default String getCode() {
        // 格式：ORDER-BIZ-0001
        return getBcPrefix() + "-" + getType().name() + "-"
               + String.format("%04d", ((Enum<?>) this).ordinal() + 1);
    }

    default String getEnumName() {
        return ((Enum<?>) this).name();  // DB 主键，永远稳定
    }

    default String getExternalCode() {
        return switch (getType()) {
            case BIZ, PARAM -> getBcExternalPrefix() + "-"
                + String.format("%04d", ((Enum<?>) this).ordinal() + 1);
            case SYS, INFRA -> "SYS-ERROR";
        };
    }

    default int getDefaultHttpStatus() {
        return switch (getType()) {
            case BIZ   -> 422;
            case PARAM -> 400;
            case SYS   -> 500;
            case INFRA -> 503;
        };
    }

    default boolean isAlertRequired() {
        return getType() == ErrorType.SYS || getType() == ErrorType.INFRA;
    }
}
```

### 1.2 ErrorType 枚举

```java
public enum ErrorType {
    BIZ,    // 业务可预期错误 → WARN，不打堆栈，4xx，细粒度对外码
    SYS,    // 系统内部错误  → ERROR，打堆栈，500，SYS-ERROR
    PARAM,  // 参数校验错误  → WARN，400，含字段级 details
    INFRA   // 基础设施故障  → ERROR，打堆栈，503，告警，可重试
}
```

### 1.3 BC 前缀注册表（所有 BC 必须在此登记，防止冲突）

| 限界上下文 | 内部前缀 | 外部前缀 | Enum 类名 |
|-----------|---------|---------|-----------|
| 通用       | COMMON  | CMN     | CommonErrorCode |
| 订单       | ORDER   | ORD     | OrderErrorCode  |
| 支付       | PAY     | PAY     | PaymentErrorCode |
| 库存       | INV     | INV     | InventoryErrorCode |

---

## Part 2：ErrorCode Enum 模板

### 黄金规则（必须遵守，CI 检查）

> 已发布版本的 Enum 条目**只能在末尾追加**，**禁止中间插入**，**禁止删除**，**禁止重命名**。
> 废弃的条目用 @Deprecated 标记但不删除。

### Enum 文件模板（以 Order BC 为例）

```java
public enum OrderErrorCode implements ErrorCode {

    // ── BIZ 类（用户侧问题，422，不告警）── 只能末尾追加 ──
    ORDER_NOT_FOUND,           // ORDER-BIZ-0001 / ORD-0001
    ORDER_INVALID_STATUS,      // ORDER-BIZ-0002 / ORD-0002
    ORDER_ALREADY_PAID,        // ORDER-BIZ-0003 / ORD-0003
    ORDER_EXPIRED,             // ORDER-BIZ-0004 / ORD-0004

    // ── PARAM 类（参数校验，400）──────────────────────────
    ORDER_PARAM_MISSING,       // ORDER-PARAM-0005 / ORD-0005
    ORDER_AMOUNT_INVALID,      // ORDER-PARAM-0006 / ORD-0006

    // ── SYS 类（服务内部 Bug，500，告警）─────────────────
    ORDER_INTERNAL_ERROR,      // ORDER-SYS-0007 / SYS-ERROR

    // ── INFRA 类（外部依赖故障，503，告警，可重试）────────
    ORDER_DB_ERROR,            // ORDER-INFRA-0008 / SYS-ERROR
    ORDER_MQ_PUBLISH_FAILED;   // ORDER-INFRA-0009 / SYS-ERROR

    @Override public String getBcPrefix()         { return "ORDER"; }
    @Override public String getBcExternalPrefix() { return "ORD"; }

    @Override
    public ErrorType getType() {
        int o = ordinal();
        if (o <= 3) return ErrorType.BIZ;
        if (o <= 5) return ErrorType.PARAM;
        if (o == 6) return ErrorType.SYS;
        return ErrorType.INFRA;
    }

    @Override
    public boolean isRetryable() {
        return getType() == ErrorType.INFRA;
    }

    @Override
    public String getDefaultMessage() {
        return switch (this) {
            case ORDER_NOT_FOUND         -> "订单不存在";
            case ORDER_INVALID_STATUS    -> "订单状态不合法";
            case ORDER_ALREADY_PAID      -> "订单已支付";
            case ORDER_EXPIRED           -> "订单已过期";
            case ORDER_PARAM_MISSING     -> "订单参数缺失";
            case ORDER_AMOUNT_INVALID    -> "订单金额不合法";
            case ORDER_INTERNAL_ERROR    -> "订单服务内部错误";
            case ORDER_DB_ERROR          -> "订单数据库异常";
            case ORDER_MQ_PUBLISH_FAILED -> "订单消息发送失败";
        };
    }
}
```

---

## Part 3：异常类层次结构（落位以 QA 确认的异常核心包为准）

### BaseException

```java
public abstract class BaseException extends RuntimeException {
    private final ErrorCode errorCode;
    private final String traceId;                      // 构造时从 MDC 自动注入
    private final Map<String, Object> context;         // 诊断上下文（不对外暴露）

    protected BaseException(ErrorCode errorCode,
                            Map<String, Object> context,
                            Throwable cause) {
        super(errorCode.getDefaultMessage(), cause);
        this.errorCode = errorCode;
        this.traceId   = MDC.get("traceId");           // 自动注入
        this.context   = context != null ? context : Map.of();
    }

    public abstract String getBoundedContext();
}
```

### DomainException（各 BC 子类为具体类，用 ErrorCode 区分场景）

```java
// 抽象基类
public abstract class DomainException extends BaseException {
    protected DomainException(ErrorCode errorCode, Map<String, Object> context) {
        super(errorCode, context, null);
    }
}

// Order BC 具体类
public class OrderException extends DomainException {
    @Override
    public String getBoundedContext() { return "ORDER"; }

    // 工厂方法（禁止直接 new）
    public static OrderException of(OrderErrorCode code) {
        return new OrderException(code, Map.of());
    }
    public static OrderException of(OrderErrorCode code, Map<String, Object> ctx) {
        return new OrderException(code, ctx);
    }
}

// 推荐用法
throw OrderException.of(OrderErrorCode.ORDER_NOT_FOUND, Map.of("orderId", orderId));
```

### AppException 和 InfraException

```java
public abstract class AppException extends BaseException {
    private final boolean alertRequired; // 覆盖 DB 配置的紧急开关
}

// 参数校验专用
public class AppValidationException extends AppException {
    private final List<FieldError> fieldErrors;
    public record FieldError(String field, String reason) {}
}

public abstract class InfraException extends BaseException {
    private final InfraType infraType;   // DB / MQ / RPC / CACHE / HTTP_CLIENT
    private final String targetService;

    public enum InfraType { DB, MQ, RPC, CACHE, HTTP_CLIENT }
}
```

### 异常跨层传播规则（严格遵守）

```
Domain 层     只抛 DomainException 子类
     ↓
Application 层  捕获 DomainException → 转为 AppException → 继续传播
                捕获第三方异常 → 包装为 InfraException → 继续传播
     ↓
Interface 层    只处理 AppException 和 InfraException
                永远不直接捕获 DomainException
```

---

## Part 4：DB 配置表（落位以 QA 确认的配置/解析模块与包为准）

### error_code_config 表 DDL

```sql
CREATE TABLE error_code_config (
    enum_name            VARCHAR(100)  NOT NULL, -- 主键：Enum name
    locale               VARCHAR(10)   NOT NULL, -- zh_CN / en_US，联合主键
    user_message         VARCHAR(500)  NOT NULL, -- 用户可见文案，支持 {orderId} 占位符
    internal_message     VARCHAR(500),
    expose_detail        BOOLEAN       DEFAULT TRUE,
    http_status_override INT,                    -- 覆盖 Enum 默认 HTTP 状态码
    alert_required       BOOLEAN       DEFAULT FALSE,
    retryable_override   BOOLEAN,                -- 覆盖 Enum 中的 isRetryable()
    PRIMARY KEY (enum_name, locale)
);
```

### ErrorCodeConfigCache（启动全量加载，支持热刷新）

```java
@Component
public class ErrorCodeConfigCache {
    // key: enumName + ":" + locale
    private final ConcurrentHashMap<String, ErrorCodeConfig> cache = new ConcurrentHashMap<>();

    @PostConstruct
    public void loadAll() { /* 从 DB 全量加载 */ }

    public Optional<ErrorCodeConfig> get(String enumName, String locale) {
        // 优先精确 locale，fallback 到 zh_CN，最终 fallback 到 null
    }

    // 管理端调用触发热刷新，不重启服务
    public void refresh() { loadAll(); }
}
```

### ErrorMessageResolver（三级 fallback）

```java
// 优先级：DB 配置 → i18n messages.properties → Enum defaultMessage
public String resolve(ErrorCode errorCode, Locale locale) {
    // 1. 查 DB Cache（支持运营热更新）
    Optional<ErrorCodeConfig> config = cache.get(errorCode.getEnumName(), locale.toString());
    if (config.isPresent()) {
        return placeholderResolver.replace(config.get().getUserMessage(), errorCode);
    }
    // 2. 查 i18n
    try {
        return messageSource.getMessage("error." + errorCode.getEnumName().toLowerCase(),
                                        null, locale);
    } catch (NoSuchMessageException ignored) {}
    // 3. Enum 兜底
    return errorCode.getDefaultMessage();
}
```

---

## Part 5：REST 出口（落位以 QA 确认的 REST 出口模块与包为准）

### ErrorResponse 结构

```java
public record ErrorResponse(
    String code,              // 对外码：ORD-0001 或 SYS-ERROR
    String message,           // 从 DB 按 locale 解析的用户文案
    String traceId,
    String timestamp,
    String path,
    List<FieldError> details  // 仅 PARAM 类填充，其他为空数组
) {}
```

### GlobalExceptionHandler 核心处理策略

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    // BIZ/PARAM → 4xx，细粒度对外码，WARN 不打堆栈
    @ExceptionHandler(AppException.class)
    public ResponseEntity<ErrorResponse> handleApp(AppException ex, HttpServletRequest req) { }

    // PARAM → 400，含 details
    @ExceptionHandler(AppValidationException.class)
    public ResponseEntity<ErrorResponse> handleValidation(...) { }

    // INFRA → 503，SYS-ERROR，触发告警，ERROR 打堆栈
    @ExceptionHandler(InfraException.class)
    public ResponseEntity<ErrorResponse> handleInfra(...) { }

    // Spring 参数校验 → 归一化为 AppValidationException
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleMethodArgument(...) { }

    // 兜底 → 500，SYS-ERROR，强告警，ERROR 打堆栈
    @ExceptionHandler(Throwable.class)
    public ResponseEntity<ErrorResponse> handleUnknown(...) { }
}
```

### 日志分级规则

| 异常类型 | 日志级别 | 打堆栈 | 告警 |
|---------|---------|-------|------|
| AppException(BIZ/PARAM) | WARN | 否 | 否 |
| AppException(SYS) | ERROR | 是 | 是 |
| InfraException | ERROR | 是 | 是 |
| MQ 进死信 | ERROR | 是 | 强告警 |
| 未知兜底 | ERROR | 是 | 强告警 |

---

## Part 6：gRPC 出口（落位以 QA 确认的 gRPC 模块/包为准，不做则跳过）

### GrpcStatusMapper（不放在 ErrorCode interface，单独维护）

```java
@Component
public class GrpcStatusMapper {
    // 先查精确映射表，找不到再按 ErrorType 做默认映射
    public Status.Code map(ErrorCode errorCode) {
        return CODE_MAP.getOrDefault(
            errorCode.getEnumName(),
            switch (errorCode.getType()) {
                case PARAM -> Status.Code.INVALID_ARGUMENT;
                case BIZ   -> Status.Code.FAILED_PRECONDITION;
                case INFRA -> Status.Code.UNAVAILABLE;
                default    -> Status.Code.INTERNAL;
            }
        );
    }

    // 精确映射（覆盖默认规则的特殊码）
    private static final Map<String, Status.Code> CODE_MAP = Map.of(
        "ORDER_NOT_FOUND", Status.Code.NOT_FOUND,
        "RESOURCE_NOT_FOUND", Status.Code.NOT_FOUND
    );
}
```

---

## Part 7：MQ 消费出口（落位以 QA 确认的 MQ 模块/包为准，不做则跳过）

### 三路分流逻辑（只写一次，三家 MQ 共用）

```java
public interface MqConsumerExceptionHandler {
    ConsumeAction handle(Throwable ex, int retryCount, int maxRetry);
}

public class DefaultMqExceptionHandler implements MqConsumerExceptionHandler {
    @Override
    public ConsumeAction handle(Throwable ex, int retryCount, int maxRetry) {
        // INFRA 类可重试异常 → 先重试，超限进死信
        if (ex instanceof InfraException && ex.getErrorCode().isRetryable()) {
            return retryCount < maxRetry ? ConsumeAction.RETRY : ConsumeAction.DEAD_LETTER;
        }
        // BIZ/PARAM 类 → 业务错误重试无意义，直接死信
        if (isBizOrParam(ex)) {
            return ConsumeAction.DEAD_LETTER;
        }
        // SYS 类 → 重试一次，失败进死信 + 告警
        if (ex instanceof AppException appEx && appEx.getErrorCode().getType() == ErrorType.SYS) {
            return retryCount < 1 ? ConsumeAction.RETRY : ConsumeAction.DEAD_LETTER;
        }
        // 未知异常 → 死信 + 强告警
        return ConsumeAction.DEAD_LETTER;
    }
}
```

### 三家 MQ 适配映射

| MQ | 适配类 | RETRY 实现 | DEAD_LETTER 实现 |
|----|--------|-----------|-----------------|
| RocketMQ | RocketMqExceptionAdapter | RECONSUME_LATER | CONSUME_SUCCESS + 手动发死信 |
| Kafka | KafkaExceptionAdapter | 抛出异常触发 DefaultErrorHandler | DeadLetterPublishingRecoverer |
| RabbitMQ | RabbitMqExceptionAdapter | nack(requeue=true) | nack(requeue=false) |

---

## Part 8：Dubbo 双端适配（落位以 QA 确认的 Dubbo 模块/包为准，不做则跳过）

### RpcErrorEnvelope（与异常核心同包或 QA 确认的 rpc 包，双端共享）

```java
public record RpcErrorEnvelope(
    boolean success,
    String errorCode,       // 内部码字符串，如 ORDER-BIZ-0001
    String errorType,       // BIZ / SYS / PARAM / INFRA
    String externalCode,    // 对外码，Consumer 可直接透传
    String message,         // 已按 locale 解析好的文案
    String traceId,
    boolean retryable,
    Map<String, Object> context
) implements Serializable {}
```

### Provider 侧 Filter

```java
@Activate(group = CommonConstants.PROVIDER)
public class DubboProviderExceptionFilter implements Filter {
    @Override
    public Result invoke(Invoker<?> invoker, Invocation invocation) {
        Result result = invoker.invoke(invocation);
        if (result.hasException()) {
            RpcErrorEnvelope envelope = buildEnvelope(result.getException());
            // 以 RpcErrorEnvelope 作为正常返回值（不抛异常），Consumer 侧检查 success 字段
            return AsyncRpcResult.newDefaultAsyncResult(envelope, invocation);
        }
        return result;
    }
}
```

### ResultUnwrapper（防止 Consumer 忽略 success 检查）

```java
// 所有 Dubbo Consumer 调用必须经过此方法解包，禁止直接 result.getData()
public class ResultUnwrapper {
    public static <T> T unwrap(Result<T> result) {
        if (result == null) {
            throw AppException.of(CommonErrorCode.RPC_UNAVAILABLE);
        }
        Object value = result.getValue();
        if (value instanceof RpcErrorEnvelope envelope && !envelope.success()) {
            throw DubboResultErrorExtractor.restore(envelope);
        }
        return (T) value;
    }
}
```

### TraceId 跨进程传递

```java
// Consumer 调用前写入
RpcContext.getContext().setAttachment("traceId", MDC.get("traceId"));

// Provider Filter 接收后写入 MDC
String traceId = RpcContext.getContext().getAttachment("traceId");
if (traceId != null) MDC.put("traceId", traceId);
```

---

## Part 9：OpenFeign Consumer 适配（落位以 QA 确认的 Feign 模块/包为准，不做则跳过）

```java
@Component
public class FeignExceptionDecoder implements ErrorDecoder {
    @Override
    public Exception decode(String methodKey, Response response) {
        // 4xx → 解析 ErrorResponse JSON → 还原为 AppException(BIZ)
        // 5xx → 解析 ErrorResponse JSON → 还原为 AppException(SYS)
        // 解析失败 → InfraException(HTTP_CLIENT)
        // 连接超时 → InfraException(HTTP_CLIENT, retryable=true)
    }
}

@Component
public class FeignTraceInterceptor implements RequestInterceptor {
    @Override
    public void apply(RequestTemplate template) {
        template.header("X-Trace-Id", MDC.get("traceId"));
        template.header("X-User-Id",  MDC.get("userId"));
    }
}
```

---

## Part 10：MDC 标准字段（所有出口层必须注入）

| 字段 | 说明 | 注入时机 |
|------|------|----------|
| traceId | 链路追踪 ID | 请求入口拦截器 |
| spanId | 当前 span | 请求入口拦截器 |
| userId | 当前用户 ID | 认证拦截器 |
| tenantId | 租户 ID | 认证拦截器 |
| boundedContext | 当前 BC 标识 | 应用启动时写入 |
| errorCode | 异常错误码 | 异常处理器写入（仅异常时） |

---

## Part 11：starter 自动装配（落位以 QA 确认的 starter 模块/包为准，不做则跳过）

```java
// Spring Boot 3 注册文件：
// META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports

@AutoConfiguration
public class ExceptionCoreAutoConfiguration { /* 装配 Cache, MessageResolver */ }

@AutoConfiguration
@ConditionalOnClass(name = "org.springframework.web.servlet.DispatcherServlet")
public class ExceptionWebAutoConfiguration { /* GlobalExceptionHandler, MdcTraceFilter */ }

@AutoConfiguration
@ConditionalOnClass(name = "io.grpc.Server")
public class ExceptionGrpcAutoConfiguration { /* GrpcExceptionInterceptor */ }

@AutoConfiguration
@ConditionalOnClass(name = "org.apache.dubbo.config.ReferenceConfig")
public class ExceptionDubboAutoConfiguration { /* DubboProviderExceptionFilter */ }

@AutoConfiguration
@ConditionalOnClass(name = "org.springframework.cloud.openfeign.FeignClient")
public class ExceptionFeignAutoConfiguration { /* FeignExceptionDecoder */ }
```

---

## 代码生成检查清单

生成任何模块代码前，逐项确认：

- [ ] **落位模块与包名**已按 QA 确认结果（confirm-and-edit 或约定文档）生成，未使用未确认的 exception-* 等固定名
- [ ] 异常核心所在模块无 Spring 依赖（仅 slf4j 等必要依赖）
- [ ] DomainException 子类未直接传播到 Interface 层
- [ ] ErrorCode Enum 使用 Enum name 作为 DB 主键，非 ordinal
- [ ] 新增 ErrorCode 条目只在末尾追加
- [ ] SYS/INFRA 类异常对外返回 "SYS-ERROR"，不透出内部码
- [ ] 日志级别：BIZ/PARAM 用 WARN，SYS/INFRA 用 ERROR
- [ ] Dubbo Provider 侧异常已包装为 RpcErrorEnvelope，未裸露 Java 异常
- [ ] MQ 消费异常经过三路分流，BIZ 类不重试直接死信
- [ ] MDC 六个标准字段在所有出口层均已注入
- [ ] starter 按 classpath 条件装配，非强制引入所有适配模块
