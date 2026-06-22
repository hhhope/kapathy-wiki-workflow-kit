# Context 确认清单模板

生成文档后，在产出物顶部或回复用户时粘贴本表（已填值）。

```markdown
## Context 确认清单

| 信息项 | 确认内容 |
|--------|----------|
| 协议模式 | HTTP / Dubbo / both |
| 项目名 | |
| 编写人 | |
| 调用方 | |

### HTTP（仅 http 或 both）

| 信息项 | 确认内容 |
|--------|----------|
| baseUrl 前缀 | |
| 路径风格 | REST / 动作路径 |
| 默认 HTTP 方法 | |
| 统一响应结构 | |
| 鉴权 | |

### Dubbo（仅 dubbo 或 both）

| 信息项 | 确认内容 |
|--------|----------|
| basePackage | |
| Facade 类名 | |
| Facade 全限定名 | {basePackage}.api.{Facade} |
| Result 包装类 | |
| request DTO 包 | |
| response DTO 包 | |
| dubbo.group | |
| dubbo.version | |
| 默认 timeout(ms) | |
| 注册中心 | |
| 维护方式 | 手动 / Nacos / IDEA 插件 |

### 接口范围

| 接口 | 模式 | 方法名/路径 |
|------|------|-------------|
| | | |
```
