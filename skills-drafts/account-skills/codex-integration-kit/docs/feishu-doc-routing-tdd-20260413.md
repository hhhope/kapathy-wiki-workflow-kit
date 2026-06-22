# Feishu Doc Routing TDD

Date: `2026-04-13`

## Problem

After adding `feishu-doc-writing`, there was a real routing risk:

- the new skill could capture “写一个飞书文档” as a writing task
- but fail to trigger `lark-doc`
- resulting in good content planning with no actual CLI write to the remote document

## RED

Baseline issue:

- `feishu-doc-writing` described writing quality and structure
- but did not explicitly require pairing with `lark-doc` for remote Feishu document operations

That meant requests like these were under-specified:

1. “帮我写一个飞书文档并直接更新”
2. “把这段整理成飞书文档发上去”
3. “更新这个飞书文档，顺便把结构理顺”

## GREEN

The skill now contains an explicit pairing rule:

- content structure and readability belong to `feishu-doc-writing`
- real document I/O belongs to `lark-doc`
- mixed requests must use both instead of choosing one

## Acceptance Matrix

| Prompt | Expected routing |
|---|---|
| “帮我起草一篇飞书分享稿” | `feishu-doc-writing` |
| “帮我创建一个飞书文档并把这篇分享稿写进去” | `feishu-doc-writing` + `lark-doc` |
| “更新这个飞书文档，结构太乱了” | `feishu-doc-writing` + `lark-doc` |
| “读一下这个飞书文档内容” | `lark-doc` |
| “给这个飞书文档插入图片” | `lark-doc` |

## Result

The routing contract is now explicit enough to prevent the “只写内容、不走 CLI” failure mode.
