---
title: 研发数字员工画像 V1.0 H5 门禁复核
layer: ops
domain: public-report-output
ops_area: report-quality
canonical_object: rd-digital-employee-profile-v1-h5
artifact_type: report-gate-review
language: zh-CN
audience: internal
knowledge_level: working
period: 2026-q3
source_links:
  - ../reports/rd-digital-employee-profile-v1-h5.html
  - ../sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md
status: active
updated_at: 2026-08-05
ai_generated: true
---

# 研发数字员工画像 V1.0 H5 门禁复核

## Review Target

- **目标：**`研发数字员工画像 V1.0` 白色编辑型单页 H5。
- **目标文件：**`wiki/reports/rd-digital-employee-profile-v1-h5.html`。
- **读者：**研发人员、技术负责人、产品经理、研发管理者，以及需要选择数字员工试点范围的业务负责人。
- **本轮范围：**Windows Edge/Chromium 下的 1440×1000 桌面验收、390×844 移动触控仿真、逐页视觉、交互、无 JavaScript、reduced-motion、事实边界与本地静态校验。
- **非范围：**不发布、不部署、不同步飞书，不把画像 V1.0 提升为组织制度、人员替代结论、采购建议或生产授权标准。

## Reviewer Routing

- **结论：**本轮不追加独立 public-report reviewer。
- **已检查信号：**复杂 H5、视觉交付物、同业事实引用；但输出结构已由设计稿确认，前五个实现任务已经逐轮审查，本轮仅执行最终门禁、必要修复与复验，没有结构漂移或未决用户判断。
- **使用路径：**`public-report-quality-gate -> frontend-visual-governor -> real-browser QA`。
- **模板状态：**沿用已确认的“两章六页 + 一图流 + 结论”输出形态，不另选模板。

## Article Intent Contract

| 字段 | 本页合同 |
|---|---|
| Reader | 研发与产品管理相关读者 |
| Reader decision or action | 区分模型、Agent、研发 Agent 与数字员工，并用岗位契约、自治边界和结果指标选择试点任务 |
| Main line | 研发数字员工不是“会写代码的 Agent”，而是“岗位责任 + Agent 能力 + 工程治理”的有界工作系统 |
| Non-goals | 不讨论人员替代，不承诺零失误或完全自治，不授予自动合并/生产发布权限，不把同业功能等同于组织授权 |
| User-owned judgments | 两章六页结构、白色编辑型方向、V1.0 聚焦 A2–A3、以低到中风险真实任务回放 |
| Agent-allowed work | 视觉与交互实现、官方证据映射、事实边界收紧、浏览器验收与可逆缺陷修复 |

## Reference Structure Map

| 来源 | Reader job / reading path | 视觉逻辑 | 写作与复用边界 |
|---|---|---|---|
| `docs/superpowers/specs/2026-08-05-rd-digital-employee-profile-h5-design.md` | Hero → 整体一图流 → 第一章三页 → 第二章三页 → 结论 | 白色编辑型滚动叙事；横轴承载概念、覆盖、成熟度、适配、结果链与一天时间线 | 保留两章六页和先概念、后画像、最后综合案例的顺序；不改成仪表盘或长图背景 |
| `wiki/reports/assets/rd-digital-employee-profile-v1/rd-digital-employee-profile-v1-onepager.png` | 先给全局地图，再分章阅读 | 原比例画框 + 灯箱，不作为背景或替代正文 | 图片只承担概览，正文仍可独立阅读；图片失败有替代说明 |
| `wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md` | 页面 02 判断同业覆盖与 Human on the Loop 边界 | 四类覆盖轴 + 双泳道 | 只复用官方明确能力；产品名不等于成熟度或自治等级 |

## Reference Output Shape

- **Selected shape：**单页滚动 H5，两章六个内容页；首屏与一图流不计入六页。
- **Retained：**桌面右侧两章导航、移动顶部两章导航、章内弱进度、11 个横向关系图、一图流灯箱、能力/一天状态详情、结论入口。
- **Rejected：**仪表盘化、长图替代正文、能力数值评分、同业排行榜、自动化替代叙事、实现说明泄漏到读者页面。
- **User-approved shape changes：**无；本轮没有改变已确认结构。
- **Gate：**PASS。H5 保持设计稿输出形态，未出现结构替换或生产说明残留。

## Learning Use Map

| 学习/事实资产 | 能力类型 | 用于 H5 的位置 | 未复用边界 |
|---|---|---|---|
| 同业官方核验图谱 | product capability evidence | 内容页 02 的四类覆盖图、官方链接与负向边界 | 不把公开功能扩展为自动合并、生产发布、组织授权或人员替代 |
| 设计稿中的 Agent/Harness/SOP/Orchestration/状态机关系 | concept model | 内容页 01 的概念轴、组成、运行闭环与三张关系卡 | 不用口号替代定义，不把状态机等同于 Orchestration |
| 画像 V1.0 的岗位契约、九项条件、A0–A4 | evaluation model | 内容页 03–05 | 不按模型版本、拟人程度或伪精确分数定级 |

## Newspaper Citation Surface

- **适用性：**本页不是报纸式 H5；Newspaper Citation Surface 不适用。
- **等价读者证据面：**内容页 02 的五个产品名直接链接厂商官方文档，页面注明核验日期 `2026-08-05`；结论区提供同业研究页入口。

## Section And Paragraph Drift Review

| 区段 | 目标与实际主张 | Mainline role | Target fit | Drift | Evidence fit | 判断来源 | 动作 |
|---|---|---|---:|---:|---:|---|---|
| Hero + 一图流 | 给出“岗位契约 + 可靠交付 + 工程治理”的控制结论和全局地图 | setup | 5 | 0 | 5 | 已确认设计稿 | retain |
| 页面 01 | 区分 Agent、研发 Agent、Harness、SOP、Orchestration 与状态机 | explanation | 5 | 0 | 5 | 设计稿/画像材料 | retain |
| 页面 02 | 说明四类公开覆盖形态与人机责任边界 | evidence + contrast | 5 | 0 | 5 | 官方核验图谱 | retain |
| 页面 03 | 从能力系统推进到岗位化数字工作单元和九项必要条件 | transition | 5 | 0 | 5 | 已确认设计稿 | retain |
| 页面 04 | 展示身份、行为、十维能力与 A2–A3 聚焦 | explanation | 5 | 0 | 5 | 已确认画像 | retain |
| 页面 05 | 将试点适配与被接受结果的七类指标对应 | decision support | 5 | 0 | 5 | 已确认设计稿 | retain |
| 页面 06 + 结论 | 以一天案例回放状态、SOP、Gate、恢复和指标；不增加新概念 | synthesis + conclusion | 5 | 0 | 5 | 已确认设计稿 | retain |

## Judgment Ledger

- **用户已确认：**白色编辑型单页 H5；两章六页；先概念与同业边界，后画像、使用、评价和一天案例；V1.0 聚焦 A2–A3。
- **来源支持：**五个同业产品在 H5 中的展示能力、官方链接、核验日期和不得外推边界。
- **本轮工程判断：**将小字蓝色加深、补非原生 dialog Escape、移除增强 tablist 容器的冗余焦点停靠、补足移动触控目标、收敛页面 06 的桌面空白。
- **未知/待用户确认：**无会阻断本地 H5 门禁的未知判断。

## Environment And Commands

- **OS / shell：**Windows，PowerShell。
- **Browser：**Microsoft Edge（Chromium），`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`，Playwright 驱动；桌面 1440×1000，移动 390×844 且启用 `is_mobile`/`has_touch`。
- **入口：**本地 `file://` URL；页面未加载网络资源。
- **浏览器门禁：**`python .superpowers/sdd/2026-08-05-rd-digital-employee-profile-h5/task-6-browser-qa.py`。
- **交互回归：**`python .superpowers/sdd/2026-08-05-rd-digital-employee-profile-h5/task-5-browser-test.py`。
- **专项 verifier：**`python scripts/verify_rd_digital_employee_h5.py`。
- **目标 unittest：**`python -m unittest tests.test_verify_rd_digital_employee_h5 -v`。
- **语法：**`node --check wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js`。
- **差异卫生：**按 Task 6 brief 的目标路径运行 `git diff --check -- ...`。

## Desktop Visual Gate — 1440×1000

- **页面边界：**`innerWidth=1440`，`documentElement.scrollWidth=1440`，整页无水平溢出；页面高度 `12052px`。
- **导航与总进度：**右侧 fixed 导航仅两章；滚动到第二章时 `aria-current=true`，页底进度为 `100%`。
- **Hero / 一图流：**Hero 的主结论、三个关键词和双入口层级清楚；一图流实际加载尺寸 `866×1817`，画框无裁切，灯箱不会空白。
- **页面 01：**四级概念轴、八类组成、六步运行闭环和 SOP/Orchestration/状态机三卡对齐；箭头不压字。
- **页面 02：**四类覆盖卡以高度差表达覆盖深度，所有边界文案可读；Human on the Loop 的 Agent / Gate / Human 三栏关系明确。
- **页面 03：**五级成熟度轴和九项必要条件均匀对齐，无断线、重叠或伪精确评分。
- **页面 04：**身份卡两列对齐；能力带四组有区分；A2–A3 聚焦、A4 灰色虚线和禁止项层级可辨。
- **页面 05：**输入到反馈横轴完整；任务适配与七类结果指标并置，红色只落在治理风险。
- **页面 06：**八个时间节点完整；增强后的当前状态详情跨满桌面网格并以两列展示七类证据，消除了原先半宽卡造成的误导性空白。
- **Console：**`console.error=0`，`pageerror=0`，warning `0`。

## Mobile Visual Gate — 390×844

- **页面边界：**`innerWidth=390`，`documentElement.scrollWidth=390`，不存在整页横滚；页面高度 `14845px`。
- **正文与导航：**正文单列；顶部 sticky 导航仅两章，每个导航触控高度至少 `44px`。
- **横向关系图：**11 个 `.horizontal-diagram` 均为 `overflow-x:auto`；实测内容宽度从 `768px` 到 `2083px`，右侧露出后续内容并保留“横向滑动”提示，没有把横轴挤成不可读多行。
- **长词与卡片：**`R&D Delivery Digital Employee`、`Orchestration`、`Issue / Change Request` 等在容器内换行，无容器外溢。
- **时间轴与触控：**时间轴卡可触控横滑；页面主要触控目标最小高度 `44px`。
- **灯箱：**触控打开后遮罩、图像和标题均可见；关闭按钮为 `56×44.25px` 且保持横向“关闭”，不再拆成竖排两字。
- **Console：**`console.error=0`，`pageerror=0`，warning `0`。

## Interaction And Degradation Gate

| 项目 | 实际结果 |
|---|---|
| 阅读进度 | 桌面和移动滚至页底均为 `100%` |
| 章节高亮 | 第二章进入观察区后，两端均只把 chapter-2 标为 current |
| 能力详情 | 10 个能力触发器增强为 tab；点击/触控与方向键都更新选中态，始终只有 1 个面板可见 |
| 一天状态 / SOP | 8 个状态触发器增强为 tab；触控“验证”后只显示对应状态，其 SOP、工具、权限、Gate、恢复、指标均存在 |
| 灯箱 | 原生 dialog 的按钮、Escape、遮罩三条关闭路径可用；焦点回到原触发器 |
| 非原生 dialog fallback | 禁用 `showModal` 后 Escape 可关闭，`hidden` 恢复且焦点归还 |
| Focus | 键盘 Tab 后 active element 的 `outline-style` 非 none、宽度非 0 |
| tablist 焦点 | 能力带与一天时间轴增强后，容器 `tabindex` 均被移除；只保留活动 tab 的 roving focus |
| 返回顶部 | 既有真实浏览器回归确认普通模式用 smooth，reduced-motion 用 auto |
| reduced-motion | 6 页全部直接 revealed；动画数 `0`，`scroll-behavior:auto`，transform `none`，opacity `1` |
| 无 JavaScript | 6 页正文、10 个能力详情、8 个状态详情、8 组 SOP 均可见；`scrollWidth=390` |

## Peer Facts Boundary

| H5 对象 | 页面实际声明 | 与官方研究记录的边界结论 |
|---|---|---|
| GitHub Copilot Chat | 建议、解释、单元测试生成、缺陷修复建议 | 未称其独立完成研发交付或替代评审 |
| OpenAI Codex / Google Jules | 读取上下文、修改文件、形成待审查候选变更 | 未把测试能力错误共归给 Jules；明确不自动合并、生产发布或承担业务目标风险 |
| GitLab Duo Agent Platform | 多 Agent 嵌入生命周期并连接 Issue/MR/commit/CI/CD 上下文 | 明确“贯穿生命周期”不等于无需人审或默认部署权限 |
| Amazon Q Developer | IAM 约束下的研发辅助、质量/安全/部署风险与依赖审查 | 未声称组织级多 Agent 编排、端到端自动交付或生产放行 |

页面没有“80% 替代”“零失误”“完全自主”等正向承诺；出现“自动合并”“生产发布”“无需人审”时均处于明确的否定或边界句中。

## Fixes Applied

1. `--blue` 从 `#2878e1` 调整为 `#226bc5`：对白色对比度从约 `4.32:1` 提升到 `5.28:1`；对最不利的淡紫底仍为 `4.66:1`，覆盖 12px 普通小字。
2. 非原生 dialog fallback 新增单独 Escape 处理，并确保关闭后恢复 `hidden`、移除 `open`、归还触发器焦点。
3. 能力与状态容器增强为 tablist 时移除原 `tabindex=0`，消除 active tab 前的冗余焦点停靠。
4. 移动两章导航补 `min-height:44px`；灯箱关闭按钮补最小 `44×44`、禁止换行。
5. 桌面增强态的当前“一天状态”详情跨两列并在内部按两列排证据，修复半宽卡带来的大块误导性空白；无 JavaScript 的八卡双列降级保持不变。

## Hard Gate Results

| Gate | Result | Evidence |
|---|---|---|
| Learning Use | PASS | 同业官方核验图谱逐产品映射到页面 02 |
| Reference Structure | PASS | 两章六页、一图流、结论路径与设计稿一致 |
| Reference Output Shape | PASS | 未替换为仪表盘、长图正文或通用卡片站 |
| Split | PASS | 单页只服务“理解画像并选择试点”一个主读者任务；六页完成渐进拆分 |
| Voice | PASS | 无聊天残留、实现说明或仓库路径进入读者正文 |
| Narrative | PASS | 主线始终从 Agent 能力推进到岗位责任与工程治理 |
| Paragraph Drift | PASS | 六页逐节对照均 retain，drift=0 |
| Judgment Ownership | PASS | 组织授权、人员替代与生产责任均保留为明确非目标/人工边界 |
| Visual | PASS | 1440×1000 与 390×844 逐页截图、灯箱和无 JS 证据已人工查看 |
| Publish | PASS for local review; external publish not authorized | 本页记录来源、边界、修复、未验证项和残余风险；本轮不外发 |

## Scorecard

| 维度 | 分数 | 说明 |
|---|---:|---|
| Reference fidelity | 15/15 | 设计结构与读者路径完整保留 |
| Learning reuse | 10/10 | 同业事实逐项映射且保留负向边界 |
| Core narrative | 20/20 | 六页和结论没有改变主线 |
| Progressive split | 15/15 | 两章六页分工明确，一天案例只做综合回放 |
| Reader path | 15/15 | Hero、概览、章节导航、章内进度和结论入口完整 |
| Visual information design | 15/15 | 11 个横轴均承载结构/顺序/边界，桌面移动均已检查 |
| Report voice | 5/5 | 正式、克制，无工作流泄漏 |
| Evidence boundary | 5/5 | 页面内官方链接、核验日期、负向边界和研究入口完整 |
| **Total** | **100/100** | 全部 hard gates 通过；仅适用于本地 review，不代表外部发布授权 |

## Test Results

| 命令 | 退出码 / 原始摘要 |
|---|---|
| Task 6 real-browser QA | `0`；18 项断言全部 `PASS`，含两端横滚、console、触控、灯箱、fallback、focus、no-JS、reduced-motion |
| Task 5 browser regression | `0`；`Ran 7 tests ... OK` |
| `python scripts/verify_rd_digital_employee_h5.py` | `0`；`PASS: rd-digital-employee-profile-v1-h5` |
| `python -m unittest tests.test_verify_rd_digital_employee_h5 -v` | `0`；`Ran 7 tests ... OK` |
| `node --check .../app.js` | `0`；无语法错误输出 |
| Task 6 target `git diff --check` | `0`；无 whitespace error；仅 PowerShell 提示工作区 LF 后续可能由 Git 转为 CRLF |
| Targeted frontmatter precheck | exit `1`（仓库基线）；全库 `29 errors / 6 warnings`，target `entry_count: 0`，没有目标页违规条目 |
| `python scripts/check_wiki_frontmatter.py --root .` | exit `1`（仓库基线）；JSON 同为 `29 errors / 6 warnings`，目标页违规列表为空 |

## Visual Evidence

- **全页：**`.superpowers/sdd/2026-08-05-rd-digital-employee-profile-h5/task-6-desktop-full.png`；`task-6-mobile-full.png`。
- **逐页：**同目录 `task-6-desktop-page-01.png` 至 `page-06.png`；`task-6-mobile-page-01.png` 至 `page-06.png`。
- **灯箱：**`task-6-desktop-lightbox.png`；`task-6-mobile-lightbox.png`。
- **无 JavaScript：**`task-6-mobile-no-js-page-06.png`。
- **结构化原始结果：**`task-6-browser-qa.json`。

## Decision

`PASS_FOR_LOCAL_REVIEW`。当前 H5 在已验证的 Windows Edge/Chromium 环境满足桌面、移动、交互、降级和事实边界门禁；可作为仓库内本地评审版本。该结论不授权部署、外发或飞书同步。

## Residual Risks And Unverified Areas

1. 未在 iOS Safari、Android WebView、Firefox 或真实物理手机上执行；移动结论来自 Edge/Chromium 的 390×844 触控仿真。
2. 未用 VoiceOver/NVDA 等屏幕阅读器做真人走查；已验证语义角色、roving focus、可见焦点、Escape 与焦点归还。
3. Task 6 未重新访问外网；同业事实以 `2026-08-05` 的仓库内官方核验记录为准。后续若产品能力或官方页面变化，应先刷新 source 记录再改 H5。
4. 一图流位图在高倍放大时清晰度受源文件 `866×1817` 限制；当前桌面/移动灯箱没有裁切或空白，但不是无限缩放矢量资产。

## Feishu Update Verification

- **Result：**not applicable；本轮没有 Feishu 写入或发布操作。

## Visual Asset Boundary

- **Local asset：**`wiki/reports/assets/rd-digital-employee-profile-v1/rd-digital-employee-profile-v1-onepager.png`。
- **Local H5 assets：**`wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css`、`app.js`。
- **Feishu：**未同步，未插图，未产生 image token 或客户端可用性声明。
