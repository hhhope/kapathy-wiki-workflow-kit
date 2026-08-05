# 研发数字员工画像 V1.0 H5 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一份白色编辑型、两大章六个内容页、桌面与移动端均可直接浏览的“研发数字员工画像 V1.0”静态 H5。

**Architecture:** 使用单个语义 HTML 承载全部可读内容，独立 CSS 负责白色主题、横向关系图与响应式，独立 JavaScript 负责章节导航、进度、能力详情、状态/SOP 切换和图片灯箱。页面不依赖构建步骤或外部网络；一份 Python 标准库校验脚本约束两章六页、关键内容、本地资源和无外链依赖。

**Tech Stack:** HTML5、CSS3、原生 JavaScript、Python 3 标准库、浏览器手工视觉验证。

## Global Constraints

- 页面结构固定为两大章、六个内容页；Hero、整体一图流和结论不计入内容页。
- 第一章三个内容页：Agent、组成与研发 Agent；同业现状与人机分工；研发数字员工定位与必要条件。
- 第二章三个内容页：完整员工画像与定级；使用场景与考核；数字员工的一天。
- 白色、克制、专业；系统中文无衬线字体；不加载外部字体、脚本、样式或图片。
- 每个内容页必须有承担解释任务的横向关系图，不用装饰性图标代替信息结构。
- 同业产品现状必须在实现时使用官方产品页或官方文档重新核验，并把核验日期、能力边界和官方链接写入研究记录。
- 不使用“80% 替代”“零失误”“完全自主”等无证据结论。
- V1.0 聚焦 A2–A3；A4 只作为非默认目标展示。
- JavaScript 不可用时，全部正文与 SOP 仍然可读。
- 本轮只生成仓库内 H5、校验脚本和视觉检查证据；不部署、不发布、不外部同步。

---

## File Structure

- Create: `wiki/reports/rd-digital-employee-profile-v1-h5.html` — 两章六页的语义结构、正文、横向图节点和降级内容。
- Create: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css` — 白色视觉系统、章节布局、横向图、响应式、焦点与 reduced-motion。
- Create: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js` — 进度、章节高亮、移动导航、能力详情、SOP 状态切换、灯箱和返回顶部。
- Create: `scripts/verify_rd_digital_employee_h5.py` — 标准库静态验收器，检查文件、两章六页、关键语义、资源路径和外部依赖。
- Create: `wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md` — 同业官方证据与展示边界。
- Create: `wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md` — 桌面、移动、交互、内容和残余风险的门禁记录。
- Reuse: `wiki/reports/assets/rd-digital-employee-profile-v1/rd-digital-employee-profile-v1-onepager.png` — 已确认的一图流。

### Task 1: 核验同业研发 Agent 并冻结页面文案

**Files:**
- Create: `wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md`
- Reference: `wiki/sources/rd-digital-employee-agent-source-study-2026-08-05.md`
- Reference: `wiki/ops/rd-digital-employee-profile-v1-2026-08-05.md`

**Interfaces:**
- Consumes: 当前画像研究、九项必要条件、A0–A4 定级和两章六页设计。
- Produces: H5 内容页 02 可直接引用的四类同业图谱、官方证据、核验日期与人机边界文案。

- [ ] **Step 1: 建立官方证据记录骨架**

写入固定字段：`核验日期`、`官方来源`、`官方明确能力`、`未确认能力`、`归属类型`、`H5 可展示判断`。候选对象至少覆盖官方的编码辅助、任务执行、流程协同或企业治理能力；不以媒体文章或产品排行榜作为事实来源。

- [ ] **Step 2: 浏览并核验官方产品页或官方文档**

优先核验 GitHub Copilot、OpenAI Codex、Google Jules、Amazon Q Developer 等官方资料；只记录官方页面明确写出的能力。若候选产品官方材料无法支持当前展示结论，则在“未确认能力”中说明并从 H5 示例中移除。

- [ ] **Step 3: 形成四类覆盖图和人机边界文案**

固定四类为：`编码辅助型`、`任务执行型`、`全流程协同型`、`企业研发平台型`。每个产品只标注官方证据能够支持的覆盖范围，不把产品名称等同于成熟度评级。

- [ ] **Step 4: 自查研究记录**

Run:

```powershell
Select-String -Path 'wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md' -Pattern '核验日期','官方来源','未确认能力','H5 可展示判断'
```

Expected: 四个固定字段均至少出现一次，所有展示对象均有官方链接与边界说明。

- [ ] **Step 5: Commit**

```powershell
git add wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md
git commit -m "docs: verify R&D agent peer landscape"
```

### Task 2: 建立两章六页的静态验收器

**Files:**
- Create: `scripts/verify_rd_digital_employee_h5.py`
- Test target: `wiki/reports/rd-digital-employee-profile-v1-h5.html`

**Interfaces:**
- Consumes: 目标 HTML、CSS、JavaScript 和一图流相对路径。
- Produces: `main() -> int`；成功输出 `PASS: rd-digital-employee-profile-v1-h5`，失败逐项输出 `FAIL: ...` 并返回 1。

- [ ] **Step 1: 编写预期失败的校验脚本**

使用 `html.parser.HTMLParser` 统计 `data-chapter` 和 `data-content-page`，并检查：恰好 2 个主章、恰好 6 个内容页、内容页 ID 为 `page-01` 到 `page-06`、存在 `main`/`nav`/`section`、存在一图流文件、CSS/JS 均为本地相对路径、HTML 不含 `http://` 或 `https://` 资源依赖、关键短语全部出现。

关键短语固定为：`Agent 是什么`、`研发 Agent`、`Orchestration`、`SOP`、`状态机`、`Human on the Loop`、`A2`、`A3`、`使用场景`、`如何考核`、`数字员工的一天`。

- [ ] **Step 2: 运行校验并确认红灯**

Run:

```powershell
python scripts/verify_rd_digital_employee_h5.py
```

Expected: exit code 1，至少包含 `FAIL: missing HTML`。

- [ ] **Step 3: Commit**

```powershell
git add scripts/verify_rd_digital_employee_h5.py
git commit -m "test: add R&D digital employee H5 verifier"
```

### Task 3: 实现两章六页的语义 HTML

**Files:**
- Create: `wiki/reports/rd-digital-employee-profile-v1-h5.html`
- Reference: `wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md`
- Reference: `wiki/reports/assets/rd-digital-employee-profile-v1/rd-digital-employee-profile-v1-onepager.png`

**Interfaces:**
- Consumes: Task 1 的官方核验文案、设计稿全部结论和 Task 2 的固定 ID。
- Produces: `#chapter-1`、`#chapter-2`；`#page-01` 至 `#page-06`；`.capability-trigger[data-capability]`；`.state-trigger[data-state]`；`#onepager-lightbox`。

- [ ] **Step 1: 写入 Hero、总览和两章容器**

Hero 只保留主标题、结论、三个关键词和两个动作；总览区复用既有 PNG，并提供完整 `alt`、图片失败时可见的文字摘要和灯箱按钮。主导航只列“从 Agent 到研发数字员工”和“画像、使用与评价”。

- [ ] **Step 2: 写入第一章三个内容页**

`page-01` 同屏包含 `大模型 → Agent → 研发 Agent → 研发数字员工`、Agent 八类组成、运行闭环，以及 SOP / Orchestration / 状态机辨析卡。`page-02` 同屏包含四类同业覆盖轴和 Human on the Loop 双泳道。`page-03` 包含成熟度轴和九项必要条件检查带。

- [ ] **Step 3: 写入第二章三个内容页**

`page-04` 组合身份卡、七项行为特征、十维能力带和 A0–A4 定级轴。`page-05` 左侧为任务适配轴与场景卡，右侧为考核指标，中央共用“工作单输入 → 运行反馈”横轴。`page-06` 使用后端接口缺陷修复案例，按 09:00–17:00 呈现八个时间节点及状态、SOP、工具、权限、Gate、恢复和指标。

- [ ] **Step 4: 保证无 JavaScript 降级可读**

能力详情和每天的 SOP 证据默认存在于 HTML；JavaScript 只改变选中态和展示密度，不通过脚本动态生成唯一内容。所有按钮使用原生 `button`，所有图的横向滚动容器提供 `tabindex="0"` 和可读标签。

- [ ] **Step 5: 运行校验并观察仅样式/脚本相关失败**

Run:

```powershell
python scripts/verify_rd_digital_employee_h5.py
```

Expected: 两章六页、固定 ID 和关键文案检查通过；若 CSS/JS 尚未创建，仅报告对应本地文件缺失。

- [ ] **Step 6: Commit**

```powershell
git add wiki/reports/rd-digital-employee-profile-v1-h5.html
git commit -m "feat: add R&D digital employee H5 content"
```

### Task 4: 实现白色主题和响应式横向图

**Files:**
- Create: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css`
- Modify: `wiki/reports/rd-digital-employee-profile-v1-h5.html`

**Interfaces:**
- Consumes: Task 3 的章节、内容页、图轴、卡片、泳道、能力带和时间轴类名。
- Produces: `--ink`、`--muted`、`--line`、`--blue`、`--mint`、`--orange`、`--violet`、`--danger` 设计变量；桌面 1440×1000 与移动 390×844 布局。

- [ ] **Step 1: 建立统一视觉令牌和基础排版**

使用 `#FFFFFF` 背景、接近黑色正文、浅灰边框、清透蓝主色、薄荷绿/柔和橙/淡紫辅助色。统一圆角、间距、边框和极浅阴影；系统字体栈包含 `-apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif`。

- [ ] **Step 2: 完成两章层级与六页密度**

主章标题形成明显分隔，内容页以大留白和一个主判断组织；桌面右侧只显示两章导航，六页用弱化进度点表达，不把每个小节做成独立菜单。

- [ ] **Step 3: 完成六类横向信息图样式**

分别实现概念递进/运行闭环、同业轴/泳道、成熟度/条件带、画像档案/能力带/定级轴、任务适配/考核闭环和全天时间轴。窄屏使用 `overflow-x: auto`，图内设置合理 `min-width`，正文不随横向图一起溢出。

- [ ] **Step 4: 完成可访问状态与降级样式**

实现 `:focus-visible`、按钮 hover/active、图片失败摘要、`noscript` 提示和 `@media (prefers-reduced-motion: reduce)`。红色仅用于越权、禁止和高风险；A4 用灰色虚线。

- [ ] **Step 5: 运行静态校验**

Run:

```powershell
python scripts/verify_rd_digital_employee_h5.py
```

Expected: CSS 路径存在、无外部资源依赖；只允许尚未实现的 JavaScript 文件检查失败。

- [ ] **Step 6: Commit**

```powershell
git add wiki/reports/rd-digital-employee-profile-v1-h5.html wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css
git commit -m "feat: style R&D digital employee H5"
```

### Task 5: 实现轻量交互与无障碍行为

**Files:**
- Create: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js`
- Modify: `wiki/reports/rd-digital-employee-profile-v1-h5.html`

**Interfaces:**
- Consumes: `data-chapter`、`data-content-page`、`data-capability`、`data-state` 和 `#onepager-lightbox`。
- Produces: `initProgress()`、`initChapterNav()`、`initReveal()`、`initCapabilityPanel()`、`initStatePanel()`、`initLightbox()`、`initBackToTop()`；每个初始化函数在目标节点不存在时安全返回。

- [ ] **Step 1: 实现阅读进度和两章导航**

滚动时根据文档高度更新顶部进度条；用 IntersectionObserver 高亮当前主章。Observer 不可用时直接显示全部内容，并以锚点导航维持基本可用性。

- [ ] **Step 2: 实现能力详情与一天状态切换**

点击或键盘触发 `.capability-trigger` 时，仅更新对应详情卡的选中态和 `aria-selected`。点击 `.state-trigger` 时展示该时间节点的状态、SOP、工具/权限、Gate、恢复和指标；所有内容原本已在 HTML 中，脚本只切换可见层级。

- [ ] **Step 3: 实现一图流灯箱**

支持打开按钮、关闭按钮、遮罩点击和 Escape；打开时把焦点移入关闭按钮，关闭后归还触发按钮；使用 `aria-modal="true"` 和 `hidden` 控制状态。

- [ ] **Step 4: 实现返回顶部和 reduced-motion**

当用户偏好减少动画时使用即时滚动；否则允许平滑滚动。所有初始化包裹在 `DOMContentLoaded`，单个模块失败不阻断正文阅读。

- [ ] **Step 5: 运行完整静态校验**

Run:

```powershell
python scripts/verify_rd_digital_employee_h5.py
```

Expected: exit code 0，输出 `PASS: rd-digital-employee-profile-v1-h5`。

- [ ] **Step 6: Commit**

```powershell
git add wiki/reports/rd-digital-employee-profile-v1-h5.html wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js
git commit -m "feat: add R&D digital employee H5 interactions"
```

### Task 6: 桌面与移动视觉门禁

**Files:**
- Create: `wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md`
- Modify if defects found: `wiki/reports/rd-digital-employee-profile-v1-h5.html`
- Modify if defects found: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css`
- Modify if defects found: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js`

**Interfaces:**
- Consumes: 完整本地 H5。
- Produces: 1440×1000 与 390×844 的视觉检查结果、交互检查结果、内容门禁和残余风险。

- [ ] **Step 1: 在本地浏览器打开 H5**

使用仓库内静态文件或本地静态服务器打开 `wiki/reports/rd-digital-employee-profile-v1-h5.html`；不引入网络资源。

- [ ] **Step 2: 检查桌面视口 1440×1000**

逐屏检查两章层级、六页密度、右侧两章导航、一图流灯箱、所有横轴、卡片对齐、文字重叠、裁切、误导性空白和控制台错误。

- [ ] **Step 3: 检查移动视口 390×844**

检查正文单列、横轴可控滚动、两章移动导航、触控目标、灯箱退出、长词换行、时间轴可读和页面不存在整体水平溢出。

- [ ] **Step 4: 检查交互与降级**

验证进度条、章节高亮、能力详情、一天状态/SOP、Escape 关闭灯箱、焦点归还、返回顶部和 reduced-motion。临时禁用 JavaScript，确认六页正文、能力说明和 SOP 证据仍可阅读。

- [ ] **Step 5: 写入门禁记录并修复发现的问题**

记录每个视口的结果、修复项、尚未验证项和残余风险；不得只写“通过”。同业产品事实与研究记录逐项对照，确认页面没有扩大官方能力声明。

- [ ] **Step 6: 运行最终校验**

Run:

```powershell
python scripts/verify_rd_digital_employee_h5.py
```

Expected: exit code 0，输出 `PASS: rd-digital-employee-profile-v1-h5`。

- [ ] **Step 7: 检查任务相关 Git 差异**

Run:

```powershell
git diff --check -- wiki/reports/rd-digital-employee-profile-v1-h5.html wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js scripts/verify_rd_digital_employee_h5.py wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md
```

Expected: exit code 0，无空白错误。

- [ ] **Step 8: Commit**

```powershell
git add wiki/reports/rd-digital-employee-profile-v1-h5.html wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js scripts/verify_rd_digital_employee_h5.py wiki/sources/rd-digital-employee-h5-peer-landscape-2026-08-05.md wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md
git commit -m "docs: verify R&D digital employee H5"
```

## Self-Review

- Spec coverage: 两章六页、官方同业核验、横向图、SOP/Orchestration/状态机、人机 Gate、A2–A3、使用场景、考核、一天案例、响应式和降级均有对应任务。
- Placeholder scan: 计划不含 TBD、TODO、“稍后实现”或未定义接口；产品候选必须通过 Task 1 官方核验才能进入 H5。
- Interface consistency: HTML 固定使用 `page-01` 至 `page-06`；JavaScript 和校验器消费相同的 `data-*` 接口；灯箱固定为 `#onepager-lightbox`。
- Scope boundary: 不创建框架项目、不增加第三方依赖、不部署、不同步外部平台。
