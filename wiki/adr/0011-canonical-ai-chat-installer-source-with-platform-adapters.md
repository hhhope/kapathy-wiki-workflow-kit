# ADR-0011 Canonical AI Chat Installer Source With Platform Adapters

- Status: accepted
- Date: 2026-04-17

## Context

仓库已经形成了一套完整但偏本地的 AI workflow 结构：

- `AGENTS.md` 承载 repo 默认治理边界
- `.codex/skills/` 承载正式 workflow / principle skills
- `wiki/` 承载 durable guidance、样例和分享材料

当这套结构需要被安装到 Cursor、Claude、Codex 等不同 AI chat 运行面时，出现了两个风险：

- 把不同平台硬讲成“同一个 skill 原样复制”
- 把 canonical workflow 语义和平台安装细节混写在一起，导致长期漂移

## Decision

- 仓库级 AI chat 安装能力采用“canonical source + platform adapters”模型。
- 仓库内部只维护一套 canonical workflow source。
- Codex、Cursor、Claude 都通过各自 adapter 输出消费这套真源。
- 飞书分享物是正式输出，但不充当运行时真源。

## Consequences

- 跨平台安装有统一语义源，不需要分别维护三套独立 workflow 说明。
- 平台差异被显式记录，而不是被“万能 skill”叙事掩盖。
- 分享材料可以稳定复用，但不会取代 repo 真源、ADR 或 OpenSpec artifacts。
