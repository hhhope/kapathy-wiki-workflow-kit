---
layer: ops
domain: ai-workflow
ops_area: report-quality
canonical_object: ai-visual-expression-workflow-guide
artifact_type: report-gate-review
---

# AI 作图表达工作流飞书分享 gate review

## Review Target

- Target: `wiki/reports/ai-visual-expression-workflow-guide.md`
- Planned Feishu title: `AI 作图不要直接出图：参考图驱动的高质量图片生成工作流`
- User intent: 写一篇给 AI 实践 / Prompt 同事看的飞书分享，主题是用 AI 高效作图来表达想法。
- Publish mode: create a new Feishu document after user approval.
- Feishu URL: `https://www.feishu.cn/docx/Kj2kdRR9ho0yfBx0HPCcbK14nvd`

## Article Intent Contract

| Field | Contract |
|---|---|
| Reader | AI 实践同事、Prompt 同事、需要用 AI 做海报/知识卡/一图流表达的人。 |
| Reader decision or action | 学会不要直接让模型出图，而是先拆参考图版式、拆内容字段、合成 prompt、人工确认，再生成和验收。 |
| Main line | AI 作图是表达工程：Prompt 负责说清楚，visual-agent 负责选对作图类型和路径，图片模型负责最后生成。 |
| Non-goals | 不做具体图片生成，不对模型能力做绝对排名，不把失败案例写成工具吐槽。 |
| User-owned judgments | 是否继续扩展成团队规范、是否后续补图例、是否把 visual-agent 规则固化成 skill 变更。 |
| Agent-allowed work | 整理飞书正文、方法论、visual-agent 分类、prompt 模板、验收清单，并创建新飞书文档。 |

## Source Use Map

| Source | Used for | Boundary |
|---|---|---|
| 用户提供的豆包对话过程 | 提炼“直接出图导致失控”的失败路径。 | 不逐字复现冗长对话，不攻击具体工具。 |
| 用户确认的 B 读者选择 | 确定面向 AI 实践 / Prompt 同事，保留工作流和模板细节。 | 不写成管理层倡议或业务普及稿。 |
| 用户补充的推荐方法 | 纳入 Prompt、visual-agent、图片模型三层分工。 | 不在正文里展开 repo 内部治理细节。 |

## Section Drift Review

| Section | Objective | Result |
|---|---|---|
| 开头问题 | 说明为什么“参考图 + 内容 + 直接出图”会失控。 | PASS |
| 五步工作流 | 给出参考图驱动的可复用流程。 | PASS |
| 推荐方法 | 加入 Prompt、visual-agent、图片模型分工。 | PASS |
| visual-agent 分类 | 单独说明流程图/结构图、海报、知识卡、H5、Hybrid 五类标准。 | PASS |
| Prompt 模板 | 提供可复制模板，强调确认前不生成。 | PASS |
| 结论 | 回到“表达先拆清楚，再生成”的主线。 | PASS |

## Gate Results

| Gate | Result |
|---|---|
| Article intent | PASS |
| Reference output shape | PASS: 按用户要求写成飞书分享文，不是 prompt 修订或图片生成。 |
| Voice quality | PASS |
| Judgment ownership | PASS: 未把模型推荐写成绝对排名，保留工具使用场景。 |
| Publish gate | PASS: user approved writing Feishu; new document created and read back. |

## Verification Evidence

| Item | Evidence |
|---|---|
| Repo draft | `wiki/reports/ai-visual-expression-workflow-guide.md` created. |
| Feishu create | `lark-cli docs +create --title "AI 作图不要直接出图：参考图驱动的高质量图片生成工作流"` returned `https://www.feishu.cn/docx/Kj2kdRR9ho0yfBx0HPCcbK14nvd`. |
| Feishu read-back | `lark-cli docs +fetch --doc https://www.feishu.cn/docx/Kj2kdRR9ho0yfBx0HPCcbK14nvd --format pretty` returned the title, five-step workflow, Prompt/visual-agent/model method split, visual-agent categories, model recommendation, template, and final conclusion. |

## Residual Risks

1. 当前正文是文字分享，没有配图；如果要作为更正式培训材料，后续可补一张“参考图到 prompt 再到出图”的流程图。
2. 如果后续要把这篇内容升级成 `visual-agent` 行为规则，需要另走 skill / OpenSpec 变更，不应从飞书正文直接改行为资产。
