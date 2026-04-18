# Evaluation

## Pressure Scenarios

1. active change 引用了 `.codex/skills/`，但没有 `evaluation.md`
2. active change 引用了 `.codex/skills/`，且 `evaluation.md` 含完整行为证据段落

## RED Baseline

- `python3 -m unittest tests.test_repo_health_check`
- 结果：4 个测试全部失败，因为 `repo_health_check` 只返回 `draft-skill-runtime-surface`，还没有 `skill-evaluation-evidence` 这条检查
- `python3 scripts/repo_health_check.py --repo-root .`
- 旧实现不会暴露缺失的行为证据文件

## GREEN Result

- `python3 -m unittest tests.test_repo_health_check`
- 结果：通过，health-check 现在会对缺失 `evaluation.md` 的 skill change 报错
- `python3 scripts/repo_health_check.py --repo-root .`
- 在补齐本仓库缺失的 `evaluation.md` 后，`skill-evaluation-evidence` 检查可恢复为通过

## Residual Risks

- 当前检查通过 `.codex/skills/` 字符串来判断 change 是否触及 formal skill publication。
- 如果未来有人绕开正式路径表达 skill 变更，这条检查可能漏报。
- 这是当前 repo 正式发布模型下可接受的第一版 gate，后续可再收紧。
