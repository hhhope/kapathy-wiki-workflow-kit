# HTTP 模式产出规范（OpenAPI 3.0）

## 文件命名

`apifox-{project}-http-openapi.yaml`

## 文首注释（必填）

```yaml
# Apifox HTTP 项目导入说明：
# 1. 新建或打开 HTTP 类型项目（非 Dubbo）
# 2. 项目设置 → 导入数据 → OpenAPI/Swagger → 选择本文件
# 3. 环境管理中配置 baseUrl: {用户确认的 baseUrl}
# 4. Dubbo 服务请勿使用本文件，见 apifox-{project}-dubbo.md
```

## 结构要求

```yaml
openapi: 3.0.3
info:
  title: {服务名} API
  version: 1.0.0
  description: |
    baseUrl 前缀: {baseUrl}
    统一响应: {code, message, data, requestId} 或用户定义
servers:
  - url: {baseUrl}   # 用户自定义前缀，完整 URL 或路径前缀
paths:
  /{path}:
    post:            # 默认 post，除非用户指定
      summary:
      operationId:   # camelCase，唯一
      requestBody:
        content:
          application/json:
            schema: ...
            examples: ...
      responses:
        '200':
          content:
            application/json:
              schema: ...
components:
  schemas: ...
  parameters:
    RequestIdHeader:  # 可选 X-Request-Id
```

## 字段规则

| 规则 | 说明 |
|------|------|
| 命名 | camelCase |
| DDL 对齐 | `customer_no` → `customerNo` |
| 敏感字段 | description 注明「明文入参，服务端加密」 |
| 每个接口 | 至少 1 个 request example + 1 个 success response example |
| 业务失败 | HTTP 200 + body.code ≠ 0000（若团队惯例如此） |

## 路径约定

- 用户给前缀 `/api/v1/wallet-account` 时，paths 可写相对路径 `/open-and-bind`，server 写前缀
- 或 paths 写全路径，server 只写 host；**二选一**，在 description 说明

## 统一响应 Schema 模板

```yaml
ApiResponse:
  type: object
  required: [code, message]
  properties:
    code:
      type: string
      example: "0000"
    message:
      type: string
    data:
      type: object
    requestId:
      type: string
```

业务 DTO 放在 `components.schemas`，通过 `allOf` 引用 `ApiResponse`。

## 错误码

用户提供则用；否则附默认表于 `info.description` 或独立 schema enum，并标 TBD。
