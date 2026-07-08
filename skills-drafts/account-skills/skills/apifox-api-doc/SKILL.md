---
name: apifox-api-doc
description: Use when producing Apifox-importable API documentation, OpenAPI 3 HTTP specs, Dubbo API docs, API import assets, or interface definitions that must keep HTTP and Dubbo modes separate.
---

# Apifox 接口文档生成 Skill

## 角色与边界

- 产出物供 **Apifox** 使用；HTTP 与 Dubbo **格式不可互换**。
- **禁止**：用 OpenAPI 冒充 Dubbo；在 Dubbo 文档里写 URL/POST；在用户未选模式前默认 HTTP。
- 字段命名默认 **camelCase**；若用户提供库表 DDL，字段与表列驼峰对齐。
- 不替代业务决策：错误码、鉴权细节缺失时标 `[TBD]`，不捏造。

---

## Step 0：模式选择（强制，第一步）

用户未明确说「HTTP」或「Dubbo」时，**必须先问**，不得假设：

```
请确认 Apifox 接口文档模式（二选一）：

1. **HTTP 模式** — REST/网关，产出 OpenAPI 3.0（.yaml），导入 Apifox「HTTP 项目」
2. **Dubbo 模式** — RPC，产出 Dubbo 说明文档（.md）+ 可选 Java 接口草案，在 Apifox「Dubbo 项目」中维护或从注册中心/IDEA 同步

你选哪种？若两种都要，请说明各自范围（例如对外 HTTP、对内 Dubbo）。
```

用户已明确（如「我们是 Dubbo」「生成 OpenAPI」）则记录模式，**无需重复询问**，但需在输出顶部 **Context 确认清单** 中写明。

---

## Step 1：收集 Context（强制）

按模式收集；**必填缺一则询问，禁止跳过**。

### 1.1 通用必填（两种模式都要）

| # | 信息项 | 说明 |
|---|--------|------|
| 1 | 服务/项目名 | 如 `wallet-account` |
| 2 | 接口清单 | 名称 + 一句话职责；或详设/需求粘贴 |
| 3 | 请求/响应字段 | 参数表、DDL、DTO、或示例 JSON |
| 4 | 文档编写人 | 元信息；无则填 `待补充` |

### 1.2 HTTP 模式专用

| # | 信息项 | 默认 / 示例 |
|---|--------|-------------|
| H1 | **baseUrl 前缀** | 如 `https://api.example.com/wallet-account` 或 `/api/v1` |
| H2 | 路径风格 | RESTful 资源路径 vs 动作路径（如 `/open-and-bind`） |
| H3 | HTTP 方法 | 默认 POST（金融对内接口常见）；GET 需用户确认 |
| H4 | 统一响应包装 | 如 `{ code, message, data, requestId }` |
| H5 | 鉴权方式 | Header 名称、Token 类型；无则 TBD |
| H6 | 错误码表 | 可选；无则用占位表 |

### 1.3 Dubbo 模式专用

| # | 信息项 | 默认 / 示例 |
|---|--------|-------------|
| D1 | **基础包名 basePackage** | 如 `com.baofu.wallet.account` |
| D2 | **API 接口类名** | 如 `WalletAccountFacade`（全名 = basePackage + `.api.` + 类名） |
| D3 | **DTO 子包** | 默认 `{basePackage}.api.dto.request` / `.response` |
| D4 | **统一返回类型** | 如 `com.baofu.common.api.Result<T>` |
| D5 | Dubbo group / version | 如 `wallet` / `1.0.0`；无则 TBD |
| D6 | 注册中心 | Nacos / ZK / 仅手动维护 |
| D7 | 默认 timeout(ms) | 如 3000 |

### 1.4 选填

性能要求、调用方、敏感字段加密说明、幂等键字段名。

### 收集话术（信息不足时）

```
生成 Apifox 文档前还需要确认：

【模式】HTTP 还是 Dubbo？
【HTTP】baseUrl 前缀是？统一响应结构？
【Dubbo】基础包名？Facade 类名？Result 全类名？group/version？
【通用】接口列表和字段从哪来（DDL / 详设 / 口述）？
```

---

## Step 2：生成前检查（门禁）

```
- [ ] 已确认 protocolMode: http | dubbo | both
- [ ] 通用必填 1–4 已齐
- [ ] HTTP：baseUrl 已确认（H1）
- [ ] Dubbo：basePackage + Facade 类名 + Result 类型已确认（D1–D4）
- [ ] 未混用格式（Dubbo 产出无 paths/servers；HTTP 产出无 @DubboService）
```

**both 模式**：分别生成两套文件，文件名必须带 `-http-` / `-dubbo-` 区分。

---

## Step 3：按模式生成

### 3.1 HTTP 模式

1. 读取 [references/http-output-spec.md](references/http-output-spec.md)
2. 生成 **OpenAPI 3.0 YAML**：
   - 文件名：`apifox-{项目名}-http-openapi.yaml`
   - `servers[0].url` = 用户给的 **baseUrl 前缀**（含 scheme 则用完整 URL；仅路径则写在 paths 前拼接说明）
   - 每个接口：`summary`、`operationId`、requestBody schema、response schema、**example**
3. 文首 YAML 注释写明 **Apifox 导入步骤**（见 [references/apifox-import-guide.md](references/apifox-import-guide.md) §HTTP）

### 3.2 Dubbo 模式

1. 读取 [references/dubbo-output-spec.md](references/dubbo-output-spec.md)
2. 生成 **Markdown 接口文档**：
   - 文件名：`apifox-{项目名}-dubbo.md`
   - 含：服务总览、方法表、每方法「接口类/方法/参数类型/返回类型」、JSON 示例、DTO 字段表、Java `interface` 草案
   - 全限定类名严格使用用户 **basePackage**、**Facade 类名**、**DTO 子包**
3. 可选：同目录生成 `apifox-{项目名}-dubbo-api.java`（仅 Facade + 空方法签名，便于 IDEA 插件）
4. 文首写明 **Apifox Dubbo 项目** 维护方式（禁止写「导入 OpenAPI」）

### 3.3 输出目录

默认保存到：

```
skills/apifox-api-doc/outputs/
```

用户指定其他路径时从其指定。

---

## Step 4：交付清单（回复用户时必须包含）

1. **Context 确认清单**（表格：模式、baseUrl/包名、类名等）
2. **生成文件路径**列表
3. **Apifox 导入/维护步骤**（从 import-guide 摘录 5–8 条，与模式一致）
4. **模式互斥提醒**（一句）：HTTP yaml 不能导入 Dubbo 项目，反之亦然
5. **最小交付集检查**（见下）

---

## 最小交付集检查

### HTTP

- [ ] OpenAPI 3.0 合法结构（openapi/info/paths/components）
- [ ] 每个接口有 example
- [ ] 字段 camelCase，与 DDL/DTO 一致
- [ ] 注释或附带有 import 步骤

### Dubbo

- [ ] 每个方法有 Java 参数类型 + JSON 示例
- [ ] Facade 全限定名 = `{basePackage}.api.{FacadeClassName}`
- [ ] 未出现 HTTP path 作为主入口
- [ ] 含 Apifox Dubbo 维护/导入说明

---

## 约束速查（禁止项）

| 禁止 | 原因 |
|------|------|
| 未问模式就生成 | 格式错误无法导入 |
| Dubbo 文档只给 .yaml OpenAPI | Apifox Dubbo 项目不识别 |
| HTTP 文档只给 .md 无 OpenAPI | 无法批量导入 HTTP 项目 |
| 擅自改用户包名/ baseUrl | 与代码/网关不一致 |
| 伪造错误码/鉴权 | 误导联调 |

---

## 参考文件

| 文件 | 用途 |
|------|------|
| [references/apifox-import-guide.md](references/apifox-import-guide.md) | Apifox 导入/同步操作（HTTP & Dubbo） |
| [references/http-output-spec.md](references/http-output-spec.md) | OpenAPI 结构与模板 |
| [references/dubbo-output-spec.md](references/dubbo-output-spec.md) | Dubbo 文档结构与模板 |
| [references/context-template.md](references/context-template.md) | Context 确认清单模板 |

---

## 示例：模式推断

| 用户说法 | 模式 |
|----------|------|
| 「生成 Apifox 文档，我们是 Dubbo」 | dubbo |
| 「OpenAPI 导入 Apifox」 | http |
| 「wallet-account 给前置调，RPC」 | dubbo |
| 「REST API /gateway」 | http |
| 「接口文档」且未说明 | **必须先问 Step 0** |
