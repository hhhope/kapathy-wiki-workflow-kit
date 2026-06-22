# 命名推导参考

给定 `projectName` 与 `basePackage`，按下表生成**全部**对外标识。生成后输出一张命名表供用户确认，再动手改文件。

## 示例

| 输入 | 值 |
|------|-----|
| projectName | `payment-notify` |
| basePackage | `com.mandao.payment.notify` |

| 推导项 | 值 |
|--------|-----|
| PascalCase | `PaymentNotify` |
| camelCase | `paymentNotify` |
| 主类 FQCN | `com.mandao.payment.notify.config.PaymentNotifyApplication` |
| 模块列表 | `payment-notify-common` … `payment-notify-start` |
| spring.application.name | `payment-notify` |
| dubbo.application.name | `payment-notify` |
| 打包 finalName | `payment-notify` |

## 推导规则

### kebab-case → PascalCase / camelCase

1. 按 `-` 分段
2. PascalCase：每段首字母大写后拼接 → `account-subscribe` → `AccountSubscribe`
3. camelCase：首段小写，其余段首字母大写 → `accountSubscribe`

### 模块 artifactId

```
{projectName}-common
{projectName}-facade
{projectName}-domain
{projectName}-application
{projectName}-infrastructure
{projectName}-adapter
{projectName}-start
```

### Java 包路径

基础路径 = `basePackage` 的点分路径转目录。

| 模块 artifact | Java 根包 |
|---------------|-----------|
| *-common | `{basePackage}.common` |
| *-facade | `{basePackage}.api` |
| *-domain | `{basePackage}.domain` |
| *-application | `{basePackage}.app` |
| *-infrastructure | `{basePackage}.infrastructure` |
| *-adapter | `{basePackage}.adapter` |
| *-start | `{basePackage}.config`（主类） |

> facade 模块物理名含 `facade`，包名用 `api`；application 模块包名用 `app`。与 `account-subscribe` 保持一致。

### 类名

| 用途 | 模式 |
|------|------|
| 启动类 | `{PascalCase}Application` |
| 模块占位 | 仅需 `package-info.java`，无需业务类 |

### 配置文件键

| 文件 | 需与 projectName 一致的键 |
|------|---------------------------|
| application.yml | `spring.application.name`、`dubbo.application.name` |
| dubbo.properties | `dubbo.application.name` |
| 主类日志 | `[{projectName}] started successfully` |

### Maven

| 项 | 值 |
|----|-----|
| groupId | 默认 `com.mandao` |
| 父 artifactId | `{projectName}` |
| 子 artifactId | `{projectName}-<layer>` |
| start 模块 finalName | `{projectName}` |
