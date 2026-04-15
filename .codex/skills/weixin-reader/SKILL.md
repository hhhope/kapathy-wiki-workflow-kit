---
name: weixin-reader
description: Use when the user provides an mp.weixin.qq.com article link and wants to read, analyze, summarize, or extract the article content
---

# Weixin Reader

## Overview

读取微信公众号文章内容，并把正文转成可继续分析的 Markdown。

## When to Use

适用于这些场景：

- 用户给出 `mp.weixin.qq.com` 文章链接
- 用户要分析、总结、提取公众号文章内容
- 用户希望先把文章正文拉下来，再继续做比较、归纳或结构化处理

不适用于：

- 普通网页抓取
- 不需要正文，只要链接元信息

## Command

```bash
python3 .codex/skills/weixin-reader/scripts/fetch_weixin.py "<微信文章URL>"
```

## Output

脚本返回 Markdown 格式内容，包含：

- `title`
- `author`
- `date`
- `url`
- `content`

## Dependencies

首次使用需要这些依赖：

```bash
pip install playwright beautifulsoup4 lxml
playwright install chromium
```

## Limitations

- 微信页面可能触发环境验证或反爬限制
- 如果页面未能加载 `#js_content`，需要把错误结果当成抓取失败处理

## Flow

1. 运行抓取脚本
2. 读取返回的 Markdown
3. 再按用户需求做总结、分析或提取
