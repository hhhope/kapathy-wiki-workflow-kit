# Evaluation

## Baseline Scenarios

1. 活跃分歧仍停在 chat
   - 虽然方法已经存在，但什么时候该落 `wiki/ops retro` 还主要靠操作者自己记。
2. archive review 不检查分歧 preservation / promotion
   - 即使 change 曾经产出高价值分歧材料，archive review 也可能只检查 tasks 和 spec。

## Before Results

- `wiki/ops` 已有方法页，但没有明确 runtime 路由把“有保留价值但未稳定”的分歧默认送进 `retro`。
- `AGENTS.md` 的 archive review 规则还没有显式检查 disagreement preservation / promotion。
- 结果是：
  - 分歧材料仍可能只停在 chat
  - archive review 仍可能漏掉“该留 retro / 该升 ADR / 被压平了”这三种情况

## After Results

- [分歧管理方法](../../../wiki/ops/disagreement-management-method.md) 现在新增了 runtime 路由说明。
- [sample-disagreement-retro.md](../../../wiki/ops/sample-disagreement-retro.md) 现在给出了最小 retro 形状。
- `AGENTS.md` 的 `Archive Review Default` 现在显式要求检查 disagreement preservation / promotion。
- `AGENTS.md` 的 `Disagreement Management Default` 现在把 `wiki/ops retro` 的运行边界写得更窄更明确。

## Residual Risks

- 这仍然是默认人操作的 runtime 规则，不是自动触发系统。
- `retro` 何时“足够成形”仍依赖操作者判断。
- archive review 现在会问这个问题，但还没有 executable checklist 或 bot enforcement。
