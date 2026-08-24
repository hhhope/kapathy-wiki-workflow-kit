# 宝财通 2.0 → 3.0 产品研发联合评审 H5 设计

Date: 2026-08-24
Status: written-review-pending
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.

## Goal

将用户提供的两张宝财通 2.0/3.0 收单、分账、退款、提现与账户升级方案截图，整理为一份可编辑、可浏览、可截图的内部评审 H5。页面用于产品与研发联合评审，帮助读者快速看懂现状、目标方案、关键差异、改造范围、异常路径和待确认事项。

本输出是本地评审草稿，不是正式发布材料，也不默认同步飞书。

## Article Intent Contract

- Reader: 产品经理、研发、测试，以及参与资金链路评审的合规相关人员。
- Reader job: 在一次评审中建立共同的账户与资金流模型，明确 2.0 到 3.0 的变化、实现影响和需决策问题。
- Main line: 现状 -> 方案演进 -> 推荐方案 -> 改造范围 -> 风险与待确认 -> 评审结论。
- Non-goals: 不扩写截图外的商业收益；不伪造接口名、字段或规则；不把低清截图直接当成核心正文；不在未确认前把推测写成定论。
- User-owned judgments: 采用评审决策型 H5；面向产品与研发联合评审；以 3.0 作为推荐方向，2.0 作为对照；采用专业金融科技风格。
- Agent-allowed work: 重绘流程、重组文字、生成差异矩阵和交互结构；对无法可靠辨认的字段标记“待原文确认”。

## Source And Reference Structure Map

Primary sources:

1. `C:/Users/yan/AppData/Local/Temp/codex-clipboard-422211ee-7948-4916-ba48-59aade5eb2b5.png`
   - 2.0 与 3.0 账户关系和资金流主图。
   - 开户、收单、分账、退款、提现、余额调账、查收支、对账的现状与改造说明。
2. `C:/Users/yan/AppData/Local/Temp/codex-clipboard-e4df0527-cd32-442a-b7e2-c5ae57a06363.png`
   - 多种账户/电子户模式的补充图。
   - 2.0、3.0 方案说明、问题清单和改造内容的补充文本。

Source roles:

- Content source: 两张截图中的账户主体、资金流、业务规则、改造项和问题清单。
- Style source: 无；不复制截图的白底流程图视觉，仅保留其业务结构。
- Executor: 独立 HTML/CSS/JavaScript H5，核心流程使用确定性 HTML/CSS/SVG 重绘。

Source handling:

- 实施前把临时截图复制到仓库可追踪的 `wiki/sources` 对应素材目录；不得依赖临时路径作为最终证据。
- 先形成可读的 `wiki/sources` 结构化摘录，再生成 H5；素材中包含行动和风险信号时，补充关联的 `wiki/ops` 评审记录。
- OCR 或视觉转写不确定项保持显式待确认，不用模型猜测补齐。

## Chosen Approach

采用“评审决策型长滚动 H5”，而不是全程双栏对照或规格文档式堆叠。

原因：

- 产品与研发需要先形成共同判断，再进入规则细节。
- 资金流适合图形主导，复杂规则适合折叠查看。
- 桌面端支持并排比较，移动端可退化为纵向卡片，不牺牲可读性。

## Information Architecture

1. 封面与评审目标。
2. 一分钟看懂核心变化。
3. 宝财通 2.0 现状资金与账户链路。
4. 宝财通 3.0 目标资金与账户链路。
5. 2.0 / 3.0 差异矩阵。
6. 七个业务环节的改造说明。
7. 关键规则与异常路径。
8. 风险、依赖及待确认事项。
9. 评审结论与下一步。

## Screen Plan

### 0. Cover

标题：`宝财通收单与分账方案演进`。
副标题：`2.0 → 3.0 产品与研发联合评审`。
给出评审范围、版本状态和“内部评审稿”标识。

### 1. Core Changes

四张摘要卡：开户、收单、分账、资金处理。只使用截图支持的事实。主文案使用“核心变化”，不把“降低复杂度”等收益判断写成已验证结论。

### 2. 2.0 Current Flow

重绘宝财通 2.0 收单商户号、二级户、升级后商户、分账接收方、绑定卡/结算卡之间的关系。区分：

- 账户或商户关系；
- 收单资金流；
- 分账资金流；
- 提现流；
- 升级动作。

### 3. 3.0 Target Flow

以同一视觉语法重绘 3.0 目标链路，确保可以与 2.0 一键切换或并排对照。所有节点名称以截图原文为准。

### 4. Difference Matrix

对比维度：账户主体、开户方式、产品开通、收单识别、分账逻辑、退款出口、提现账户、余额调账、查余额、查收支、对账与历史兼容。

每一行包含：2.0 做法、3.0 做法、研发影响、状态（明确/待确认）。

### 5. Seven Change Areas

折叠面板承载：

1. 宝财通开户；
2. 材料补查；
3. 开户 H5；
4. 升待约接口简化；
5. 分账商户关系批量绑定；
6. 宝财通平台模式切换配置；
7. 余额调账能力。

### 6. Business Rules

按收单、分账、退款、提现、余额查询、收支查询、对账七类组织。默认展示结论摘要；展开后展示条件、路径、影响对象和例外。

### 7. Risks And Open Questions

至少包含：

- 已分账与未分账资金的处理边界；
- 资金能否跨主体划转；
- 历史订单是否能够继续分账；
- 退款资金来源与兼容路径；
- 分账关系、余额与调账校验；
- 收单商户未满足规则时的失败处理；
- 截图中无法可靠辨认或表述互相冲突的字段。

支持按产品、研发、测试/合规筛选。

### 8. Review Decision

保留“已确认项、待确认项、负责人、下一步、目标时间”填写区。H5 本身不自动产生业务结论。

## Visual Direction

- Professional fintech review style.
- Palette: 深海军蓝作为主色，科技蓝作为 3.0 强调，灰蓝作为 2.0 对照，青绿表示到账/成功，橙色表示风险或待确认。
- Account nodes: 矩形卡片；银行卡: 圆角胶囊；动作: 小型状态标签。
- Flow semantics: 资金流用实线，关系/升级用虚线；箭头必须带动作标签。
- Layout: 桌面端宽屏评审画布；移动端转为纵向卡片。
- Typography: 中文系统字体优先，强调可读性；不依赖在线字体或外部 CDN。
- No decorative metrics, charts, or claims unsupported by the source.

## Components And Interaction

- Fixed chapter navigation with active-section highlighting.
- 2.0/3.0 switch plus desktop side-by-side compare mode.
- Clickable flow nodes open a local detail panel.
- Accordion sections for detailed business rules.
- Owner filters for open questions.
- Reading progress indicator.
- Keyboard focus, visible focus state, reduced-motion support, and semantic buttons.
- JavaScript failure fallback: all core content remains visible and readable; interaction is progressive enhancement only.

## Data And Content Model

Keep source-derived content in one local structured data object separated from rendering. Each fact records:

- source image;
- source section;
- fact text;
- confidence (`confirmed`, `transcribed`, `needs_confirmation`);
- target screen;
- owner category where relevant.

The H5 must not fetch remote data. No credentials, private URLs, personal information, or production identifiers are introduced.

## Error And Ambiguity Handling

- Unreadable text: show `待原文确认`, never silently omit or invent.
- Conflicting source statements: show both statements with a conflict note.
- Empty filter result: show a readable empty state.
- Unsupported or disabled JavaScript: preserve linear reading order and all essential text.
- Narrow viewport: stack flows vertically instead of shrinking labels below readable size.

## Output Boundary

Planned outputs after spec approval and planning:

- structured source summary under `wiki/sources/`;
- linked review/gate record under `wiki/ops/`;
- standalone editable H5 under `wiki/reports/`;
- local CSS/JS assets only if splitting improves maintainability;
- desktop and mobile review screenshots as verification evidence.

No Feishu sync, publishing, or external write is included.

## Verification Plan

Before claiming review-ready:

1. Source-to-screen audit for every business claim.
2. Confirm all 2.0/3.0 nodes and arrows against the screenshots.
3. Confirm all uncertain fields are visibly marked.
4. Run local HTML validation/build checks available in the repo.
5. Open the real page and test navigation, switches, accordions, filters, and detail panels.
6. Inspect browser console for errors.
7. Inspect desktop and mobile viewports for clipping, overlap, uncontrolled horizontal scrolling, and unreadable labels.
8. Confirm SVG/flow output is nonblank and arrow labels remain readable.
9. Confirm no external dependency, secret, private URL, or production identifier is present.
10. Create/update the public-report gate-review artifact before a review-ready claim.

## Implementation Boundary

This document approves the design only. Because the repository declares OpenSpec as the source of truth and the H5 is a multi-artifact implementation, implementation must not start until:

1. the user reviews this written design;
2. a writing plan is produced;
3. an active OpenSpec change with clear tasks authorizes implementation.
