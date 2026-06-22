# Exception 检查点

触发条件：代码涉及 `exception`、`ErrorCode`、`ErrorType` 相关的文件。

## 检查点

| ID | 检查项 | 规则 | 严重级别 |
|----|--------|------|----------|
| E001 | ErrorCode 实现接口 | Enum 实现 ErrorCode 接口 | 高 |
| E002 | ErrorCode 方法完整 | 包含 getType/getBcPrefix/getDefaultMessage/isRetryable | 高 |
| E003 | 使用默认实现 | 移除手工 code 字段，使用接口默认 getCode() | 高 |
| E004 | DomainException 工厂方法 | 子类有 of() 工厂方法 | 中 |
| E005 | 迁移清理残留方法 | 无废弃接口的残留方法（如 getDesc） | 高 |
| E006 | 调用方依赖检查 | 迁移后调用方使用新接口 | 高 |
| E007 | BC 前缀注册 | 新 BC 在 BcPrefixRegistry 登记 | 中 |
| E008 | 废弃标记 | 废弃类/接口有 @Deprecated 注解 | 低 |
| E009 | 异常层次正确 | DomainException/AppException/InfraException 分层清晰 | 中 |
| E010 | ErrorType 使用正确 | BIZ/SYS/PARAM/INFRA 分类正确 | 低 |

---

## 常见问题模式

| 模式 | 问题 |
|------|------|
| 枚举实现新接口但保留旧方法 | 导致接口默认实现不生效 |
| 迁移后调用方仍用旧接口 | 编译失败或行为不一致 |
| 手工序号 vs 自动序号 | 手工序号难以维护 |
