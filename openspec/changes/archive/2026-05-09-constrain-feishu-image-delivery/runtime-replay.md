## Runtime Replay 2026-05-09

### Scenario

Input shape:

```text
帮我把团队知识库运行态和验证案例整理成飞书审核稿。
章节图片和一图流都要生成成本地资产，图片我自己添加到飞书。
正文可以同步飞书。
```

### Trigger Check

`public-report-quality-gate` SHOULD load because the request asks to prepare a
reader-facing Feishu review draft and mentions generated report visuals.

Loaded runtime sources in this session:

- `.codex/skills/public-report-quality-gate/SKILL.md`
- `.codex/skills/public-report-quality-gate/references/gate-review-artifact.md`
- `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`

### Expected Route

| Step | Expected behavior |
|---|---|
| Visual generation | Generate or preserve required local visual assets. |
| Visual evidence | Record local asset paths in the gate-review artifact. |
| Feishu sync | Treat Feishu sync as text-only because image insertion was not approved and the user says they will add images manually. |
| Image insertion | Do not insert image blocks into Feishu. |
| Proof boundary | Do not claim image-token or read-back evidence as client-usability proof. |

### Observed Route

| Check | Evidence | Result |
|---|---|---|
| Skill trigger | `SKILL.md` description and `When To Use` include Feishu review drafts and reader-facing reports. | PASS |
| Manual image path | `SKILL.md` hard rule says generated visuals stay local when the user will add images manually. | PASS |
| Text-only default | `gate-review-artifact.md` stable workflow says Feishu update is text-only by default when local images exist. | PASS |
| Pressure scenario | `pressure-scenarios.md` includes `图片我自己添加，正文同步飞书` and expects local assets plus text-only sync. | PASS |
| No image insertion | No Feishu command was run and no image generation was performed in this replay. | PASS |

### Replay Decision

The gate now routes the scenario to:

```text
public-report-quality-gate
  -> local visual assets
  -> Visual Asset Boundary records local paths
  -> Feishu text-only sync when separately approved
  -> user manually inserts images
```

This replay is current-session runtime evidence, not multi-session rollout
proof. It is sufficient for this change because the requested fix is the
repo-local public-report skill boundary, not a Feishu client-safe image
workflow.
