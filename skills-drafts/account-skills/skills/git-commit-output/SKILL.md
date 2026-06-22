---
name: git-commit-output
description: Git 提交后自动输出项目信息和分支规范约束。
---

# Git Commit 输出 Skill

当完成 git commit 操作后执行。

## 强制约束

1. **Project 标识**：从当前工作目录或 git remote 获取项目名
2. **分支规范**：
   - component 分支：`component/{YYYY-MM-DD}-{模块}`
   - cr 分支：`cr/{project}-{YYYY-MM-DD}`
   - feature 分支：`feature/{issue-id}-{描述}`
3. **唯一性**：Project + 分支类型 + 日期 作为唯一标识

## 输出内容

提交完成后，输出：

```
✅ 已提交到分支: {branch}
👤 作者: {git_username}

分支规范：
- 组件/问题分析：component/{YYYY-MM-DD}-{模块}
- 代码评审：cr/{project}-{YYYY-MM-DD}
- 功能开发：feature/{issue-id}-{描述}
```

**获取方式**：
- branch: `git branch --show-current`
- git_username: `git config user.name`

## Project 映射表

| 项目目录 | Project 标识 |
|---------|------------|
| account-asl | account-asl |
| order-bc | order-bc |
| 其他 | 取目录名 |
