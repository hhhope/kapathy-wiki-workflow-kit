# Feishu Doc Progressive Template

## Overview Page

Use this when the topic has multiple deep-dive branches.

```md
# 标题

## 一句话结论

2-3 句说清主题、适用场景、核心判断。

## 这篇文档解决什么问题

优先用表格或 3-4 条短项，不要写成长段引子。

- 问题 1
- 问题 2
- 问题 3

## 适合谁看 / 不适合谁看

- 适合：
- 不适合：

## 关键结论 / 操作路径

如果是“场景 -> 去哪读 / 做什么”的内容，优先改成表格。

1. 先看什么
2. 再看什么
3. 哪些情况跳转到子文档

## 主题拆分

### 主题 A

短摘要 + 子文档链接

### 主题 B

短摘要 + 子文档链接

## 延伸阅读 / 相关文档

- 文档 A
- 文档 B

## 你现在该从哪一层开始

- 优先写成 `场景 | 建议先读 | 为什么` 表格
```

## Deep-Dive Page

Use this when the page should explain one dense topic well.

```md
# 标题

## 一句话结论

## 适用范围

## 关键结论

- 结论 1
- 结论 2
- 结论 3

## 关键表格

在这些情况优先加表格：

- 指标 / 结果
- 场景 / 动作
- 步骤 / 目的 / 完成标志
- 风险 / 边界

## 详细说明

### 小节 1

### 小节 2

## 边界 / 注意点

- 风险 1
- 风险 2

## 相关文档 / 返回入口

- 返回 overview
- 继续阅读
```

## Update Checklist

When refreshing an existing Feishu-facing doc, check:

1. Does the parent overview still describe this page correctly?
2. Do sibling docs still have the right titles and links?
3. Did this edit leave behind any stale TODO or “to be continued” text?
4. Is the new first screen cheaper to read than before?
5. Do page titles still belong to one consistent naming system?
6. Does any old image / whiteboard still encode the previous model?
7. Does the page still read like a document rather than a cleaned-up conversation?
8. Did at least one comparison-heavy section get converted into a table?

## Visual Companion Decision

Choose one:

1. `No visual`
   Use when the text is already light and the structure is obvious.
2. `Infographic / long-image / one-page HTML`
   Pair with `xiaohongshu-retro-grid-content` when the content needs a condensed visual summary.
3. `Editable diagram`
   Pair with `lark-whiteboard` when the content needs a layer diagram, flow diagram, or architecture map inside Feishu.

## Publish Checklist

Before declaring the Feishu update done:

1. Re-read the first screen only.
   If the reader still cannot answer “这页讲什么 / 我为什么现在要看 / 我下一步去哪”，继续改。
2. Check whether list-shaped information should be a table.
3. Check whether the visual still matches the current naming and section model.
4. Fetch the remote doc again after update and verify the final visible shape.
