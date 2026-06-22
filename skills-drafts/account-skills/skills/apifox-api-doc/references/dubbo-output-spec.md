# Dubbo 模式产出规范

## 文件命名

| 文件 | 说明 |
|------|------|
| `apifox-{project}-dubbo.md` | 主文档（Apifox 手动维护 + 联调参考） |
| `apifox-{project}-dubbo-api.java` | 可选，Facade 接口草案 |

## 文首说明（必填）

```markdown
> **Apifox Dubbo 项目** — 勿将 OpenAPI 导入本项目。
> 维护方式：注册中心导入 / IDEA 插件同步 / 按本文手动新建。
> 详见 import：skills/apifox-api-doc/references/apifox-import-guide.md §二
```

## 命名计算（使用用户 Context）

| 占位 | 公式 |
|------|------|
| Facade 全限定名 | `{basePackage}.api.{facadeClassName}` |
| Request DTO | `{basePackage}.api.dto.request.{Name}Request` |
| Response DTO | `{basePackage}.api.dto.response.{Name}Response` |
| 返回类型 | `{resultWrapper}<{Response}>` 如 `com.baofu.common.api.Result<OpenAndBindResponse>` |

用户自定义 `dtoSubPackage` 时替换 `.api.dto.request` 段。

## 文档章节结构

```markdown
# {项目名} Dubbo 接口文档（Apifox）

## 1. Apifox 使用方式（摘要 import-guide §二）
## 2. 服务总览（应用名、Facade、group、version、timeout、调用方）
## 3. 接口清单表（方法名 | 说明 | Request | Response）
## 4. 接口定义（每个方法一节）
### 4.x {methodName}
- 接口类 / 方法 / 参数类型 / 返回类型（表格）
- 业务说明
- 请求 JSON 示例
- 响应 JSON 示例（Result.data）
## 5. 数据模型（DTO 字段表，camelCase + DB 列）
## 6. Java Facade 草案
## 7. 错误码
## 8. 与 HTTP 文档关系（若有双模式）
```

## 每个方法必填表

| 项 | 示例 |
|----|------|
| 接口类 | `com.baofu.wallet.account.api.WalletAccountFacade` |
| 方法 | `openAndBind` |
| 参数 | `com.baofu.wallet.account.api.dto.request.OpenAndBindRequest` |
| 返回 | `com.baofu.common.api.Result<...OpenAndBindResponse>` |

## 字段规则

同 HTTP：camelCase、DDL 对齐、敏感字段注明加密。

## Dubbo 扩展参数（服务级）

在「服务总览」列出，供 Apifox 调试：

```markdown
| group | {dubboGroup} |
| version | {dubboVersion} |
| timeout | {defaultTimeoutMs} |
| registry | Nacos / ZK [TBD] |
```

## Java 草案模板

```java
package {basePackage}.api;

import {basePackage}.api.dto.request.*;
import {basePackage}.api.dto.response.*;
import {resultWrapper};

public interface {facadeClassName} {
    {resultWrapper}<XxxResponse> methodName(XxxRequest request);
}
```

Provider 注释（可选）：

```java
// @DubboService(group = "{dubboGroup}", version = "{dubboVersion}", timeout = {defaultTimeoutMs})
```

## 禁止出现在 Dubbo 主文档

- `POST /api/v1/...` 作为唯一入口描述
- 「导入 OpenAPI」为主步骤
- 未展开的 `paths:` YAML 块（可放附录并标注 HTTP 专用）
