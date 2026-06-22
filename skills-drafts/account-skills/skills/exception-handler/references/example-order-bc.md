# 完整示例：Order BC 异常处理代码

本文档展示 Order 限界上下文的完整异常处理实现，可直接作为其他 BC 的参照模板。

---

## 1. 目录结构

```
order-service/
├── src/main/java/com/example/order/
│   ├── domain/
│   │   ├── exception/
│   │   │   └── OrderException.java          ← Domain 层异常
│   │   └── service/
│   │       └── OrderDomainService.java      ← 抛出 OrderException 示例
│   │
│   ├── application/
│   │   └── service/
│   │       └── OrderAppService.java         ← 捕获并转换为 AppException
│   │
│   └── infrastructure/
│       └── repository/
│           └── OrderRepositoryImpl.java     ← 捕获 DB 异常转为 InfraException
│
└── pom.xml                                  ← 只依赖 exception-starter
```

---

## 2. OrderErrorCode.java（完整实现）

```java
package com.example.order.domain.code;

import com.example.exception.core.code.ErrorCode;
import com.example.exception.core.code.ErrorType;

public enum OrderErrorCode implements ErrorCode {

    // ── BIZ 类 ── ordinal: 0-3 ───────────────────────────
    ORDER_NOT_FOUND,           // ORDER-BIZ-0001 → ORD-0001
    ORDER_INVALID_STATUS,      // ORDER-BIZ-0002 → ORD-0002
    ORDER_ALREADY_PAID,        // ORDER-BIZ-0003 → ORD-0003
    ORDER_EXPIRED,             // ORDER-BIZ-0004 → ORD-0004

    // ── PARAM 类 ── ordinal: 4-5 ─────────────────────────
    ORDER_PARAM_MISSING,       // ORDER-PARAM-0005 → ORD-0005
    ORDER_AMOUNT_INVALID,      // ORDER-PARAM-0006 → ORD-0006

    // ── SYS 类 ── ordinal: 6 ─────────────────────────────
    ORDER_INTERNAL_ERROR,      // ORDER-SYS-0007 → SYS-ERROR

    // ── INFRA 类 ── ordinal: 7-8 ─────────────────────────
    ORDER_DB_ERROR,            // ORDER-INFRA-0008 → SYS-ERROR
    ORDER_MQ_PUBLISH_FAILED;   // ORDER-INFRA-0009 → SYS-ERROR

    @Override
    public String getBcPrefix() { return "ORDER"; }

    @Override
    public String getBcExternalPrefix() { return "ORD"; }

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

## 3. OrderException.java（Domain 层）

```java
package com.example.order.domain.exception;

import com.example.exception.core.exception.DomainException;
import com.example.order.domain.code.OrderErrorCode;
import java.util.Map;

public class OrderException extends DomainException {

    private OrderException(OrderErrorCode code, Map<String, Object> context) {
        super(code, context);
    }

    @Override
    public String getBoundedContext() { return "ORDER"; }

    // 工厂方法，禁止直接 new
    public static OrderException of(OrderErrorCode code) {
        return new OrderException(code, Map.of());
    }

    public static OrderException of(OrderErrorCode code, Map<String, Object> context) {
        return new OrderException(code, context);
    }
}
```

---

## 4. OrderDomainService.java（Domain 层如何抛异常）

```java
@Component
public class OrderDomainService {

    public Order getOrder(String orderId) {
        Order order = orderRepository.findById(orderId)
            .orElseThrow(() -> OrderException.of(
                OrderErrorCode.ORDER_NOT_FOUND,
                Map.of("orderId", orderId)   // 诊断上下文，不对外暴露
            ));
        return order;
    }

    public void payOrder(Order order) {
        if (order.isPaid()) {
            throw OrderException.of(
                OrderErrorCode.ORDER_ALREADY_PAID,
                Map.of("orderId", order.getId(), "paidAt", order.getPaidAt())
            );
        }
        // 业务逻辑...
    }
}
```

---

## 5. OrderAppService.java（Application 层如何转换异常）

```java
@Service
public class OrderAppService {

    public OrderDTO getOrder(String orderId) {
        try {
            Order order = orderDomainService.getOrder(orderId);
            return OrderDTO.from(order);
        } catch (OrderException e) {
            // DomainException 不允许直接穿透到 Interface 层
            // 在 Application 层转换为 AppException
            throw new AppException(e.getErrorCode(), e.getContext(), e);
        }
    }

    public void payOrder(String orderId) {
        // 简单场景：如果 Application 层不需要额外处理，可以用 AOP 统一转换
        // 但涉及事务补偿、通知等逻辑时，必须显式 catch
        orderDomainService.payOrder(orderRepository.findById(orderId)
            .orElseThrow(() -> OrderException.of(OrderErrorCode.ORDER_NOT_FOUND)));
    }
}
```

---

## 6. OrderRepositoryImpl.java（Infrastructure 层包装 DB 异常）

```java
@Repository
public class OrderRepositoryImpl implements OrderRepository {

    @Override
    public Optional<Order> findById(String orderId) {
        try {
            return jpaRepository.findById(orderId).map(OrderMapper::toDomain);
        } catch (DataAccessException e) {
            // 第三方异常（Spring DataAccessException）包装为 InfraException
            throw new DatabaseException(
                CommonErrorCode.DB_ERROR,
                Map.of("orderId", orderId),
                e
            );
        }
    }
}
```

---

## 7. DB 初始化数据示例（error_code_config）

```sql
-- Order BC 错误码多语言配置
INSERT INTO error_code_config (enum_name, locale, user_message, internal_message, expose_detail, alert_required)
VALUES
-- 中文
('ORDER_NOT_FOUND',       'zh_CN', '订单不存在，请检查订单号是否正确', '查询订单不存在: orderId={orderId}', true, false),
('ORDER_INVALID_STATUS',  'zh_CN', '当前订单状态不支持此操作',         '订单状态流转异常',                  true, false),
('ORDER_ALREADY_PAID',    'zh_CN', '该订单已完成支付，请勿重复支付',   '重复支付请求',                      true, false),
('ORDER_EXPIRED',         'zh_CN', '订单已过期，请重新下单',           '订单过期',                          true, false),
('ORDER_DB_ERROR',        'zh_CN', '服务繁忙，请稍后重试',             '订单数据库异常',                    false, true),
('ORDER_MQ_PUBLISH_FAILED','zh_CN','服务繁忙，请稍后重试',             '订单MQ发送失败',                    false, true),

-- 英文
('ORDER_NOT_FOUND',       'en_US', 'Order not found. Please check the order number.', '', true, false),
('ORDER_INVALID_STATUS',  'en_US', 'This operation is not allowed for the current order status.', '', true, false),
('ORDER_ALREADY_PAID',    'en_US', 'This order has already been paid.', '', true, false),
('ORDER_EXPIRED',         'en_US', 'Order has expired. Please create a new order.', '', true, false),
('ORDER_DB_ERROR',        'en_US', 'Service is temporarily unavailable. Please try again later.', '', false, true);
```

---

## 8. REST 响应示例

### 场景 A：BIZ 类异常（订单不存在）

```json
HTTP 422 Unprocessable Entity
{
  "code": "ORD-0001",
  "message": "订单不存在，请检查订单号是否正确",
  "traceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-03-09T10:00:00Z",
  "path": "/api/orders/ORDER-999",
  "details": []
}
```

### 场景 B：PARAM 类异常（参数校验）

```json
HTTP 400 Bad Request
{
  "code": "ORD-0005",
  "message": "订单参数缺失",
  "traceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-03-09T10:00:00Z",
  "path": "/api/orders",
  "details": [
    { "field": "userId",  "reason": "不能为空" },
    { "field": "amount",  "reason": "必须大于0" }
  ]
}
```

### 场景 C：INFRA 类异常（DB 故障，不透出细节）

```json
HTTP 503 Service Unavailable
{
  "code": "SYS-ERROR",
  "message": "服务繁忙，请稍后重试",
  "traceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-03-09T10:00:00Z",
  "path": "/api/orders/ORDER-123",
  "details": []
}
```

---

## 9. MQ 消费示例（RocketMQ）

```java
@Component
@RocketMQMessageListener(topic = "ORDER_CREATED", consumerGroup = "inventory-service")
public class OrderCreatedConsumer implements RocketMQListener<OrderCreatedEvent> {

    @Override
    public void onMessage(OrderCreatedEvent event) {
        try {
            inventoryService.reserveStock(event.getOrderId(), event.getItems());
        } catch (Exception ex) {
            // 不要在这里自己处理，交给 RocketMqExceptionAdapter
            // Adapter 会调用 DefaultMqExceptionHandler.handle() 做三路分流
            throw ex;
        }
    }
}

// 分流结果示例：
// InventoryException(BIZ: STOCK_INSUFFICIENT) → DEAD_LETTER（库存不足重试无意义）
// DatabaseException(INFRA: DB_ERROR)          → RETRY 最多3次 → 超限进 DEAD_LETTER
// NullPointerException（未知）                → DEAD_LETTER + 强告警
```
