# 使用示例

## 示例 1：yqt-trade 类业务仓库（OpenSpec + Superpowers TDD）

**背景：** `openspec/changes/add-webank-split-account-withdraw-pay/` 已有 `proposal.md`、`design.md`、`tasks.md` 与 delta spec，准备写实现计划。

**用户：**「OpenSpec 都写好了，用 Superpowers 出实现计划并开始 TDD。」

**Agent 动作：**

1. 宣布使用 `openspec-superpowers-bridge`。
2. 在业务仓库根目录执行：

```bash
python skills/openspec-superpowers-bridge/scripts/build-planning-brief.py openspec/changes/add-webank-split-account-withdraw-pay
```

（若 skill 仅在 `~/.cursor/skills/`，改用该目录下 `scripts/build-planning-brief.py` 的绝对路径。）

3. 阅读 `planning-brief-for-superpowers.md`，核对 §4 每个 **R*** 有 **S***，§2 含 non-goals。
4. 调用 `superpowers:writing-plans`，仅以 brief 为 OpenSpec 输入。
5. 计划落盘 `docs/superpowers/plans/YYYY-MM-DD-webank-split-account-withdraw-pay.md`。
6. 接续 `test-driven-development` → `executing-plans`；**不**使用 `/opsx:apply`。

**期望结果：** 计划内每个 Scenario 对应测试或验证步骤；一个 OpenSpec **T*** 拆成多个 2–5 分钟 TDD 步；进度勾选在 plan 文件内。

---

## 示例 2：account-skills 治理变更（归档 change 回放 brief）

**背景：** 需要从已归档 change 生成 brief，供回顾或在新会话中重写 Superpowers 计划。

**用户：**「把 archive 里 team-lore routing 那次变更整理成 writing-plans 输入。」

**Agent 动作：**

```bash
cd /path/to/account-skills
python skills/openspec-superpowers-bridge/scripts/build-planning-brief.py \
  openspec/changes/archive/2026-04-14-harden-team-lore-language-and-routing
```

检查输出 `planning-brief-for-superpowers.md` 的 §6 追溯表，在 writing-plans 阶段手动细化 R*↔T* 映射。

**期望结果：** brief §8 列出 `proposal`/`design`/`tasks`/`spec.md` 的 present/missing；§9 handoff checklist 全部可在最终 plan 中勾选完成。
