---
name: api-test-generator
description: 根据接口文档生成测试用例代码（Request/Result DTO、Service、Test类）。触发条件：用户提到需要生成接口测试代码、添加新的API接口、或者提供接口报文编号/接口文档时使用。
---

# API 测试代码生成 Skill

## 核心流程

1. 收集接口文档信息
2. 确认信息完整性
3. 创建 Git 分支
4. 参考现有代码生成文件
5. 提交代码

---

## Step 1：收集信息

| 信息项 | 说明 |
|--------|------|
| 接口名称 | 如"日终余额查询" |
| 报文编号 | 如 "BJR1-8002-001-01" |
| 请求/响应参数 | 直接粘贴文档 |
| 接口类型 | 查询类 / 创建类 / 其他 |

> 如果用户没有提供完整信息，先询问确认后再继续

---

## Step 2：确认信息完整性

**在创建分支前**，确保以下信息都已获取：
- [ ] 接口名称
- [ ] 报文编号
- [ ] 请求参数列表
- [ ] 响应参数列表

如果信息不全，**先询问用户补充**，不要盲目继续。

---

## Step 3：创建分支

```bash
git checkout -b {分支名}
```

### 分支命名规范

```
agent-generative/{接口名小写用连字符分隔}-{YYYYMMDD}
```

**示例**：`agent-generative/daily-balance-query-20260317`

---

## Step 4：生成代码

### 4.1 选择基类（重要！）

根据接口类型选择要继承的基类：

| 接口类型 | 基类 | 参考实现 |
|----------|------|----------|
| 查询类 | `BaseService` | `VirtualBankAccountQueryService`、`DailyBalanceQueryService` |
| 创建类 | `CommonService` | `MerchantCreationService`、`UploadFileService` |

**判断规则**：
- **查询类**：只获取数据，不创建资源 → 继承 `BaseService`
- **创建类**：会创建/修改数据 → 继承 `CommonService`

### 4.2 参考现有实现

找到对应的参考文件：

| 类型 | 路径 |
|------|------|
| 查询类 Service | `src/main/java/service/VirtualBankAccountQueryService.java` |
| 创建类 Service | `src/main/java/service/MerchantCreationService.java` |
| Request DTO | `src/main/java/util/BaseRequest.java` |
| Result DTO | `src/main/java/util/BaseResult.java` |
| ApiEndpointEnum | `src/main/java/util/ApiEndpointEnum.java` |
| ResponseProcessor | `src/main/java/service/ResponseProcessor.java` |

### 4.3 创建/修改文件

**按顺序执行**：

#### 第一批（DTO）

| 文件 | 路径 | 说明 |
|------|------|------|
| `{Name}Request.java` | `src/main/java/util/` | 请求DTO，继承 `BaseRequest` |
| `{Name}Result.java` | `src/main/java/util/` | 响应DTO，继承 `BaseResult` |

#### 第二批（Service）

| 文件 | 路径 | 说明 |
|------|------|------|
| `{Name}Service.java` | `src/main/java/service/` | 服务类，继承对应基类 |

#### 第三批（枚举和处理器）

| 文件 | 路径 | 修改内容 |
|------|------|----------|
| `ApiEndpointEnum.java` | `src/main/java/util/` | 添加枚举值，如 `{NAME}_QUERY` |
| `ResponseProcessor.java` | `src/main/java/service/` | 添加响应处理方法 `process{Name}Response` |

#### 第四批（测试类）

| 文件 | 路径 | 说明 |
|------|------|------|
| `{Name}Test.java` | `src/test/java/` | 测试类 |

---

## ⚠️ 常见错误（生成时特别注意）

### 1. BaseService vs CommonService 选错

```java
// 错误：BaseService 不需要 createResultInstance
public class XXXService extends BaseService<XXXRequest, XXXResult> {
    @Override
    protected XXXResult createResultInstance() {  // ❌ 不要加！
        return new XXXResult();
    }
}

// 正确：BaseService 只需要实现 buildRequestBody
public class XXXService extends BaseService<XXXRequest, XXXResult> {
    @Override
    protected String buildRequestBody(XXXRequest request) throws Exception {
        // 实现逻辑
    }
}
```

### 2. buildRequestHeader 报错

如果基类是 `BaseService`，需要从同类 Service（如 `DailyBalanceQueryService`）复制 `buildRequestHeader` 方法实现。

### 3. @Override 报错

只有**重写基类已有方法**时才加 `@Override`。新增的自定义方法不要加。

### 4. 测试类 import 缺失

确保添加：
```java
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
```
**不要**写 `package test;`，直接使用默认包。

### 5. Service 类 import 缺失

**所有 Service 类统一使用通配符导入：**

```java
// 错误：分散导入容易遗漏
import util.ApiEndpointEnum;
import util.BaseRequest;
import util.FeeEstimateRequest;
import util.FeeEstimateResult;
// 缺少 import util.MerchantCreationException; ← 编译报错！

// 正确：使用通配符
import util.*;
```

### 6. 证书/密钥路径硬编码

```java
// 错误
private String publicKeyPath = "D:\\baofoo\\baofu2048.cer";

// 正确
private String publicKeyPath = System.getProperty("user.dir") + "/baofu2048.cer";
```

---

## Step 5：提交代码

```bash
git add {新增/修改的文件}
git commit -m "feat: 新增{接口名}接口
- 新增 {Name}Request 请求DTO
- 新增 {Name}Result 响应DTO
- 新增 {Name}Service 服务类
- 新增 {Name}Test 测试类
- ApiEndpointEnum 添加 {NAME}_QUERY 枚举
- ResponseProcessor 添加 process{Name}Response 方法
报文编号：{报文编号}"
```

---

## Step 6：验证（可选）

- 编译：`mvn compile`
- 测试：`mvn test -Dtest={Name}Test`

> 注意：首次编译需下载依赖，耗时较长，可根据实际情况决定是否执行
