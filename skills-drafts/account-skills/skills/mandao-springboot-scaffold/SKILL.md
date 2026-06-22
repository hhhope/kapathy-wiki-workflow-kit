---
name: mandao-springboot-scaffold
description: Scaffolds a new Mandao-style Java 21 Spring Boot multi-module Maven project from project name and base package only, mirroring account-subscribe layering, dependencies, and conventions. Use when creating a new microservice, bootstrapping a repo, cloning the DDD-lite skeleton, or when the user mentions 新建项目、脚手架、Spring Boot 多模块.
---

# Mandao Spring Boot 项目脚手架

以 `account-subscribe` 为黄金模板，仅输入 **项目名** 与 **基础包名** 即可生成同构工程。详细规范见 [repository-rules.md](repository-rules.md)，命名推导见 [naming-derivation.md](naming-derivation.md)。

## 必需输入

| 输入 | 格式 | 示例 |
|------|------|------|
| `projectName` | kebab-case，与 Maven artifact 一致 | `account-subscribe` |
| `basePackage` | 合法 Java 包名，不含模块后缀 | `com.mandao.account.subscribe` |

## 可选输入（有默认值）

| 输入 | 默认 |
|------|------|
| `groupId` | `com.mandao` |
| `revision` | `1.0.0-SNAPSHOT` |
| `targetDir` | 当前工作区或用户指定空目录 |
| `apolloAppId` | 占位 `000000000`，提醒用户在 Apollo 申请后替换 |

## 命名推导（执行前必须算清）

从 `projectName` + `basePackage` 推导全部标识，**禁止手写不一致的名称**：

```
PascalCase     = kebab → AccountSubscribe        (主类、日志前缀)
camelCase      = accountSubscribe                 (变量、Bean 名)
modulePrefix   = projectName                      (account-subscribe-common)
scanPackage    = basePackage                      (Spring/Dubbo 扫描根)
mainClass      = {PascalCase}Application          (AccountSubscribeApplication)
finalName      = projectName                      (打包 jar 名)
springAppName  = projectName                      (spring.application.name)
```

各模块 Java 包根（在 `basePackage` 下）：

| 模块 | 包后缀 |
|------|--------|
| common | `.common` |
| facade | `.api` |
| domain | `.domain` |
| application | `.app` |
| infrastructure | `.infrastructure` |
| adapter | `.adapter` |
| start | `.config`（主类所在） |

## 脚手架工作流

复制 checklist，逐项打勾：

```
- [ ] 1. 校验输入（kebab-case 项目名、包名无模块后缀）
- [ ] 2. 推导命名表（见 naming-derivation.md）
- [ ] 3. 创建 7 模块目录与 pom.xml（父 POM + 子模块，版本与 account-subscribe 父 POM 对齐）
- [ ] 4. 写入各模块 package-info.java 与空包结构
- [ ] 5. 配置 start：主类、application.yml、apollo-configuration.properties、dubbo.properties
- [ ] 6. 复制/生成 .gitignore、README.md、.harness/docs（code-standards、git-workflow）
- [ ] 7. 复制 .cursor/rules/ 与 .cursor/skills/mandao-springboot-scaffold/
- [ ] 8. 全局替换占位符（见下方「替换清单」）
- [ ] 9. 验证：mvn clean compile -q
```

### 推荐方式：以本仓库为模板复制

在**空目录**执行（PowerShell 示例，按实际路径调整）：

```powershell
$src = "D:\workspace-baofu\account-subscribe"
$dst = "D:\workspace-baofu\<projectName>"
robocopy $src $dst /E /XD target .git .idea /XF *.class
Remove-Item -Recurse -Force $dst\.git -ErrorAction SilentlyContinue
```

然后按 [naming-derivation.md](naming-derivation.md) 做**目录重命名 + 全文替换**，比从零手写 POM 更不易漏项。

### 替换清单（模板复制后必做）

| 占位 / 旧值 | 新值 |
|-------------|------|
| `account-subscribe` | `{projectName}` |
| `AccountSubscribe` | `{PascalCase}` |
| `accountSubscribe` | `{camelCase}` |
| `com.mandao.account.subscribe` | `{basePackage}` |
| `app.id=111000122` | `app.id={apolloAppId}` |
| 模块目录 `account-subscribe-*` | `{projectName}-*` |

重命名：根目录、`*.iml` 若存在、所有 `account-subscribe-*` 文件夹。

## 模块与依赖（不可改顺序）

```
{projectName}-start
  → adapter → application → domain → infrastructure → facade → common
```

各模块 `pom.xml` 依赖边界以 `account-subscribe` 对应模块为准，**禁止反向依赖**。细则见 [repository-rules.md](repository-rules.md#模块依赖规则)。

## 技术栈版本（与父 POM 锁定）

| 项 | 版本 |
|----|------|
| Java | 21 |
| Spring Boot | 3.5.11 |
| Dubbo | 3.2.19 |
| MyBatis Spring Boot | 3.0.3 |
| Apollo Client | 2.1.0.BF |
| MapStruct | 1.5.5.Final |
| Lombok | 1.18.32 |

新版本仅在父 POM `properties` 统一升级，子模块不写版本号（由 `dependencyManagement` 管理）。

## 中间件默认接入

| 中间件 | 接入模块 | 说明 |
|--------|----------|------|
| Spring Web + Actuator | start | 端口 8080，`/monitor` 健康探测 |
| Dubbo | adapter + facade + start | `@EnableDubbo`，`dubbo.scan.base-packages={basePackage}` |
| MyBatis | infrastructure + start | `@MapperScan` 指向 `...infrastructure` |
| MySQL + 动态数据源 | infrastructure | 连接信息走 Apollo，不入库明文 |
| Apollo | start | `apollo.bootstrap.enabled=true`，Maven profile DEV/UAT/PRO |
| Zookeeper/Curator | start（discovery） | 与 Dubbo 注册中心配套 |

可选中间件（Redis 锁、ZK 协调、MQ/Kafka、DFS）及 **Dubbo/HTTP 超时** 约定见 [middleware-guide.md](middleware-guide.md)。

## 完成后交付物

- 可 `mvn clean compile` 的空骨架
- `README.md` 含模块说明与启动命令：`mvn -pl {projectName}-start -am spring-boot:run`
- `.cursor/rules/` 仓库级规范（已复制或已生成）
- 提醒用户：在 Apollo 创建 app、申请 `app.id`、配置数据源与 Dubbo 注册中心

## 禁止事项

- 不要在 domain 引入 Spring/MyBatis 注解
- 不要在子模块 POM 写与父 POM 冲突的第三方版本
- 不要把业务魔法值散落在 service 实现里（见 repository-rules 魔法值章节）
- 不要跳过 `mvn clean compile` 就宣称脚手架完成

## 延伸阅读

- [repository-rules.md](repository-rules.md) — Maven、Git、命名、魔法值、中间件等仓库级规则
- [middleware-guide.md](middleware-guide.md) — Redis/ZK 锁、MQ/Kafka、DFS、Dubbo/HTTP 超时与重试
- [naming-derivation.md](naming-derivation.md) — 输入到标识符的推导表与示例
- 模板源码：仓库根目录 `account-subscribe` 各模块
