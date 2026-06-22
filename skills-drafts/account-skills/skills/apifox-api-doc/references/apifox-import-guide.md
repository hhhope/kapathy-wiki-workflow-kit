# Apifox 导入与维护指南

> 生成文档时，按用户所选模式将对应章节摘要写入产出物文首「Apifox 使用说明」。

---

## 一、HTTP 模式（OpenAPI 3.0）

### 1.1 前置条件

- Apifox 项目类型为 **HTTP**（不是 Dubbo、不是 gRPC）
- 产出文件为 `.yaml` 或 `.json`，符合 OpenAPI 3.0

### 1.2 导入步骤

1. 打开 Apifox → 进入目标 **HTTP 项目**
2. **项目设置** → **导入数据**
3. 选择 **OpenAPI/Swagger**
4. 选择生成的 `apifox-*-http-openapi.yaml`
5. **导入设置**（建议）：
   - 冲突处理：按团队习惯选「覆盖」或「智能合并」
   - 勾选导入 **Schemas/数据模型**
   - 勾选导入 **示例**
6. 导入完成后在「接口」目录检查 paths、请求体、响应体
7. **环境管理**中配置 `baseUrl` 变量（若 YAML 里用了 `servers.variables`）

### 1.3 导入后必做

| 项 | 操作 |
|----|------|
| 环境 | 配置 dev/uat/prod 的 `baseUrl` 与文档一致 |
| 鉴权 | 在「环境」或「Auth」中配置 Bearer/ApiKey（按项目 TBD） |
| 调试 | 选环境 → 发送请求 → 校验与 example 一致 |
| 分享 | 需要时发布文档站或快捷分享 |

### 1.4 常见失败

| 现象 | 原因 | 处理 |
|------|------|------|
| 导入到 Dubbo 项目无接口 | 项目类型错误 | 新建 HTTP 项目再导入 |
| 路径重复 | 多次导入未合并 | 清理重复或选覆盖 |
| baseUrl 不对 | servers 未配环境 | 环境变量覆盖 server |

---

## 二、Dubbo 模式

### 2.1 前置条件

- Apifox 项目类型为 **Dubbo**
- **不能**导入 OpenAPI YAML 作为 Dubbo 接口

### 2.2 方式 A：注册中心导入（Provider 已部署）

1. 新建 **Dubbo 项目**
2. **项目设置** → 配置 **Registry**（Nacos / ZooKeeper / EDAS）
3. **导入** → 从注册中心选择 Provider 服务
4. 前提（Apifox 官方要求）：
   - Dubbo ≥ 2.7
   - Provider 配置**元数据中心**（非仅注册中心）
   - Dubbo 3 注意服务级发现配置
5. 导入后补全：请求/响应 JSON 示例、接口说明（元数据可能无业务注释）

### 2.3 方式 B：IDEA Apifox 插件（推荐，有 Java 代码）

1. 安装 **Apifox Helper** IDEA 插件
2. 在 `api` 模块配置 Apifox 项目 ID
3. 在 `{basePackage}.api.*Facade` 接口或实现类上使用插件「Upload/Sync」
4. 同步后到 Apifox Dubbo 项目核对方法签名与文档

### 2.4 方式 C：手动新建（设计阶段、无部署）

按生成的 `apifox-*-dubbo.md` 逐条创建：

1. Dubbo 项目 → **新建 Dubbo 接口**
2. 填写：
   - **接口类**：`{basePackage}.api.{FacadeClassName}`（全限定名）
   - **方法名**：如 `openAndBind`
   - **参数类型**：Java 全限定名列表，顺序与接口一致
   - **返回类型**：如 `Result<OpenAndBindResponse>` 的泛型写法按 Apifox 界面要求填写
3. **接口定义** Tab：
   - 请求：粘贴文档中的 JSON 示例，或关联数据模型
   - 响应：粘贴 `Result.data` 结构示例
4. **文档预览** Tab 检查展示
5. **调试** Tab：配置 Registry、group、version、timeout 后发起调用

### 2.5 调试环境配置

| 配置项 | 示例 |
|--------|------|
| Registry | Nacos `127.0.0.1:8848` |
| group | `wallet` |
| version | `1.0.0` |
| timeout | `3000` |
| 序列化 | Hessian2（常见） |

### 2.6 常见失败

| 现象 | 原因 | 处理 |
|------|------|------|
| 导入了 OpenAPI 仍无 Dubbo 方法 | 格式不对 | 改用手动/注册中心/IDEA |
| 注册中心无服务 | 元数据未上报 / 连错环境 | 查 Provider 配置 |
| 参数类型不匹配 | 全限定名错误 | 与 Java 源码完全一致 |

---

## 三、双模式并存（both）

| 产出 | Apifox 项目类型 | 操作 |
|------|-----------------|------|
| `*-http-openapi.yaml` | HTTP 项目 | OpenAPI 导入 |
| `*-dubbo.md` | Dubbo 项目 | 手动 / 注册中心 / IDEA |

两个项目分开维护，**不要**合并为一个 Apifox 项目。
