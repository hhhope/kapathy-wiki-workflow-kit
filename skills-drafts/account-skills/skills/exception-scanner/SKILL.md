---
name: exception-scanner
description: Use when scanning exception-related code for compliance with exception-handler rules, ErrorCode interfaces, DomainException factories, BC prefixes, or exception CR findings.
---

# Exception Scanner Skill

Use this when the work is to review or scan exception-related code rather than
to generate the exception framework itself.

## 执行流程

### 1. 扫描 Exception 代码

检查以下文件是否符合 exception-handler 规范：

```
account-common/src/main/java/com/mandao/account/common/exception/**/*.java
```

### 2. 检查点清单

使用 cr-dated-output 中的 **Exception 专项检查**：

- [ ] ErrorCode Enum 是否实现 ErrorCode 接口
- [ ] 是否使用默认实现（移除手工 code 字段）
- [ ] 迁移接口时是否清理废弃接口的残留方法（如 getDesc）
- [ ] 迁移后调用方是否仍依赖废弃接口
- [ ] DomainException 子类是否有工厂方法
- [ ] BC 前缀注册表是否存在

### 3. 输出

扫描完成后：
1. 调用 cr-dated-output skill 生成 CR 报告
2. 使用 cr-dated-output 的报告模板
3. 将检查结果填入"本次新增逻辑问题"章节
