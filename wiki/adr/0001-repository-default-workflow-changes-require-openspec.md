# ADR-0001 Repository-Default Workflow Changes Require OpenSpec

- Status: accepted
- Date: 2026-04-15

## Context

仓库之前把默认协作行为分散在 `wiki/` 页面和对话里，没有一条硬规则要求“仓库默认工作流变化必须先走 OpenSpec”。这会让仓库级行为变化被误当成普通页面修改。

## Decision

涉及这些主题的默认行为变化，一律视为 OpenSpec 级 change：

- repository-default workflow
- collaboration behavior
- routing defaults
- escalation boundaries
- default output rules

## Consequences

- 这类变化必须先创建或选定 active OpenSpec change
- 不能先做临时 wiki 修补，再回填 OpenSpec
