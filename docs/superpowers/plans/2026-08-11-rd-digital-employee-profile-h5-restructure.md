# 研发数字员工画像 H5 重构 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将现有研发数字员工 H5 重构为“企业 AI 全链路 → 企业采用现状 → Agent 问题 → 我们的画像 → 上岗考核 → 一天回放”的六页研究型一图流。

**Architecture:** 保留单页 HTML、单个 CSS 和单个原生 JavaScript 文件，不引入构建工具或第三方依赖。HTML 承担全部可降级语义内容，CSS 承担六个不同信息关系的一图流布局，JavaScript 只增强章节导航、企业筛选和局部展开；静态验证脚本锁定文件路径、六页结构、关键概念和本地资源安全。

**Tech Stack:** HTML5、CSS Grid/Flexbox、原生 JavaScript、Python `html.parser`/`unittest`、本地 Chromium 视觉检查。

## Global Constraints

- 主文件使用 `wiki/reports/rd-数字员工-v1-h5.html`；不恢复已删除的英文同名旧文件。
- 维持两章、六个内容页，ID 固定为 `page-01` 到 `page-06`。
- 白色主题；蓝、青、橙、紫承担信息角色；不得退化成六页同构卡片。
- L1—L6 只表示企业落地成熟度；A0—A4 只表示单个研发数字员工自治边界。
- 企业案例采用官方材料或政府案例，并同时展示证据缺口；不把采用率直接等同于等级。
- JavaScript 关闭时所有正文、企业表格和评级说明仍可阅读。
- 不增加第三方前端依赖，不发布、不部署、不同步飞书。
- 未完成 1440×1000 与 390×844 fresh visual QA 时，不声称视觉完成。

---

## File Responsibility Map

| 文件 | 责任 |
|---|---|
| `wiki/reports/rd-数字员工-v1-h5.html` | 六页语义内容、企业证据表、所有无脚本降级文本和可访问性标签 |
| `wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css` | 白色一图流视觉系统、七层架构、表格/L轴、因果图、画像环、岗位档案和时间轴响应式布局 |
| `wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js` | 阅读进度、章节高亮、企业筛选、局部详情展开、无动画降级 |
| `scripts/verify_rd_digital_employee_h5.py` | 生产 H5 路径、六页结构、关键短语、本地资源和安全边界验证 |
| `tests/test_verify_rd_digital_employee_h5.py` | 验证器回归测试及新叙事结构契约 |
| `wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md` | 参考结构、证据映射、漂移复核、静态与视觉验收结果 |

---

### Task 1: 修复并升级 H5 静态验证契约

**Files:**
- Modify: `scripts/verify_rd_digital_employee_h5.py:12-27`
- Modify: `tests/test_verify_rd_digital_employee_h5.py:1-60`

**Interfaces:**
- Consumes: 生产目标 `wiki/reports/rd-数字员工-v1-h5.html`。
- Produces: `verifier.HTML_PATH` 指向中文文件名；`REQUIRED_PHRASES` 锁定新六页叙事；`main() -> int` 继续返回 `0/1`。

- [ ] **Step 1: 写生产路径和新叙事的失败测试**

在 `tests/test_verify_rd_digital_employee_h5.py` 增加：

```python
def test_production_path_uses_current_chinese_h5_name(self) -> None:
    self.assertEqual(
        "rd-数字员工-v1-h5.html",
        verifier.HTML_PATH.name,
    )

def test_required_phrases_cover_restructured_story(self) -> None:
    required = set(verifier.REQUIRED_PHRASES)
    self.assertTrue(
        {
            "企业 AI 全链路",
            "L1—L6",
            "Agent 解决的问题",
            "研发数字员工画像",
            "A0—A4",
            "数字员工的一天",
        }.issubset(required)
    )
```

- [ ] **Step 2: 运行测试并确认失败**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5.RdDigitalEmployeeH5VerifierTest.test_production_path_uses_current_chinese_h5_name tests.test_verify_rd_digital_employee_h5.RdDigitalEmployeeH5VerifierTest.test_required_phrases_cover_restructured_story -v`

Expected: FAIL，旧 `HTML_PATH` 仍指向 `rd-digital-employee-profile-v1-h5.html`，新短语尚未进入契约。

- [ ] **Step 3: 最小修改验证器**

将生产路径和短语改为：

```python
HTML_PATH = ROOT / "wiki/reports/rd-数字员工-v1-h5.html"
REQUIRED_PHRASES = (
    "企业 AI 全链路",
    "L1—L6",
    "Agent 解决的问题",
    "Orchestration",
    "SOP",
    "状态机",
    "研发数字员工画像",
    "A0—A4",
    "使用场景",
    "如何考核",
    "数字员工的一天",
)
```

- [ ] **Step 4: 运行验证器单测**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5 -v`

Expected: 17 个既有资源安全测试和 2 个新增契约测试全部 PASS；若 Windows 临时目录受限，设置 `$env:TEMP="$PWD\.codex-tmp"` 后重跑，不修改测试语义。

- [ ] **Step 5: 提交验证契约**

```powershell
git add scripts/verify_rd_digital_employee_h5.py tests/test_verify_rd_digital_employee_h5.py
git commit -m "test: align digital employee H5 contract"
```

---

### Task 2: 重写六页语义内容与证据表

**Files:**
- Modify: `wiki/reports/rd-数字员工-v1-h5.html:1-538`
- Modify: `tests/test_verify_rd_digital_employee_h5.py`

**Interfaces:**
- Consumes: Task 1 的六页短语与文件路径契约。
- Produces: `.architecture-stack`、`.enterprise-research`、`.problem-map`、`.employee-blueprint`、`.job-profile`、`.day-timeline` 六个视觉根容器；企业行使用 `data-industry` 和 `data-level`。

- [ ] **Step 1: 写六个视觉根容器和企业表格的失败测试**

增加生产文件结构测试：

```python
def test_production_h5_exposes_six_distinct_visual_roots(self) -> None:
    html = verifier.HTML_PATH.read_text(encoding="utf-8")
    for class_name in (
        "architecture-stack",
        "enterprise-research",
        "problem-map",
        "employee-blueprint",
        "job-profile",
        "day-timeline",
    ):
        self.assertIn(f'class="{class_name}', html)
    self.assertGreaterEqual(html.count("data-industry="), 8)
    self.assertIn("data-level=\"L5\"", html)
```

- [ ] **Step 2: 运行测试并确认失败**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5.RdDigitalEmployeeH5VerifierTest.test_production_h5_exposes_six_distinct_visual_roots -v`

Expected: FAIL，旧页面没有六个新根容器，也没有 8 条企业研究行。

- [ ] **Step 3: 重写首屏、导航与页面 01—03**

实现下列固定结构：

```html
<nav aria-label="章节导航">
  <a data-chapter-link="chapter-1" href="#chapter-1">行业全景</a>
  <a data-chapter-link="chapter-2" href="#chapter-2">我们的画像</a>
</nav>
```

- `page-01`：七层 `.architecture-stack`，每层使用 `data-layer="1"` 到 `data-layer="7"`；右侧 `.ai-comparison`；底部 `.onboarding-path` 九步链路。
- `page-02`：`.enterprise-research` 内包含筛选区、8—10 行 `<table>`、证据说明和 `.enterprise-level-map`。首版行至少包含腾讯、Block、Salesforce、IBM、工商银行、兴业银行、新网银行、国网杭州。
- `page-03`：`.problem-map` 的七条“问题 → 能力”映射；`.ai-agent-employee-comparison` 三列对照；`.mechanism-triad` 明确 SOP、Orchestration、状态机关系。

页面 02 每一行使用同一数据接口：

```html
<tr data-industry="支付" data-level="L4">
  <th scope="row">Block / Cash App</th>
  <td>客服与研发</td>
  <td>75%+ 员工使用 AI；65% 客服案例由 AI 处理；90%+ 代码提交含 AI 参与</td>
  <td>系统连接、岗位能力、人工升级</td>
  <td><span class="level-mark">L4+</span></td>
  <td>高；未证明统一多 Agent 控制面</td>
</tr>
```

- [ ] **Step 4: 重写页面 04—06**

- `page-04`：`.employee-blueprint` 使用岗位核心与六个能力环；内容涵盖身份权限、知识记忆、SOP/编排、工具行动、行为能力、评测进化。
- `page-05`：`.job-profile` 组合身份卡、十维雷达、A0—A4、任务适配矩阵和七组考核指标；明确 L 与 A 是两条轴。
- `page-06`：`.day-timeline` 使用数字员工、状态/编排、企业系统、人类主管四条泳道，节点为接单、准入、理解、规划、实现、验证、Gate、交付、复盘。

- [ ] **Step 5: 运行结构测试和生产验证器**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5 -v`

Run: `python scripts/verify_rd_digital_employee_h5.py`

Expected: 全部 PASS，输出 `PASS: rd-digital-employee-profile-v1-h5`。

- [ ] **Step 6: 提交语义重构**

```powershell
git add wiki/reports/rd-数字员工-v1-h5.html tests/test_verify_rd_digital_employee_h5.py
git commit -m "feat: restructure digital employee H5 narrative"
```

---

### Task 3: 建立六种一图流布局和响应式视觉系统

**Files:**
- Modify: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css:1-376`
- Modify: `tests/test_verify_rd_digital_employee_h5.py`

**Interfaces:**
- Consumes: Task 2 的六个视觉根容器和内部类名。
- Produces: `--layer-raw`、`--layer-system`、`--layer-knowledge`、`--layer-memory`、`--layer-context`、`--layer-job`、`--layer-employee` 颜色令牌；桌面与移动断点布局。

- [ ] **Step 1: 写 CSS 视觉契约失败测试**

```python
def test_stylesheet_has_distinct_visual_systems_and_mobile_guards(self) -> None:
    css_path = (
        verifier.HTML_PATH.parent
        / "assets/rd-digital-employee-profile-v1-h5/styles.css"
    )
    css = css_path.read_text(encoding="utf-8")
    for selector in (
        ".architecture-stack",
        ".enterprise-research",
        ".problem-map",
        ".employee-blueprint",
        ".job-profile",
        ".day-timeline",
    ):
        self.assertIn(selector, css)
    self.assertIn("@media (max-width: 620px)", css)
    self.assertIn("overflow-x: auto", css)
```

- [ ] **Step 2: 运行测试并确认失败**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5.RdDigitalEmployeeH5VerifierTest.test_stylesheet_has_distinct_visual_systems_and_mobile_guards -v`

Expected: FAIL，旧样式缺少至少一个新视觉根选择器。

- [ ] **Step 3: 重建基础视觉令牌和页面 01—03**

使用以下固定视觉语法：

```css
:root {
  --paper: #fff;
  --ink: #172033;
  --muted: #667085;
  --line: #d8e0ec;
  --layer-raw: #4f7ff2;
  --layer-system: #159c9b;
  --layer-knowledge: #eb8a3d;
  --layer-memory: #7757d7;
  --layer-context: #36a66c;
  --layer-job: #d64b70;
  --layer-employee: #27489b;
}
```

- `.architecture-stack`：七个不同颜色的横向层，不使用七张漂浮卡。
- `.enterprise-research`：冻结表头、清晰行分隔、高亮强证据行；等级轴与表格共用颜色语义。
- `.problem-map`：左右问题/能力列，中间箭头；三列对照使用垂直分隔而非卡片阴影。

- [ ] **Step 4: 实现页面 04—06 的不同视觉语法**

- `.employee-blueprint`：中心岗位核心，桌面端六个环围绕；移动端转为有编号的纵向关系链。
- `.job-profile`：身份卡为文档样式，能力雷达用 CSS/SVG 网格，A0—A4 使用横轴，考核用矩阵。
- `.day-timeline`：四泳道网格，时间节点纵向对齐；移动端保留局部横向滚动，不压缩文字到不可读。

- [ ] **Step 5: 实现响应式和无动画降级**

在 `900px` 和 `620px` 断点处理：

- 页面容器不得整体横向溢出。
- 企业表和时间轴只在 `.horizontal-scroll` 内横向滚动。
- 所有正文最小字号 `12px`，主要说明文字不低于 `14px`。
- `prefers-reduced-motion: reduce` 关闭平移和滚动动画。

- [ ] **Step 6: 运行 CSS 契约与静态验证**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5 -v`

Run: `python scripts/verify_rd_digital_employee_h5.py`

Expected: PASS；CSS 外部资源检查无新增失败。

- [ ] **Step 7: 提交视觉系统**

```powershell
git add wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css tests/test_verify_rd_digital_employee_h5.py
git commit -m "style: build infographic systems for digital employee H5"
```

---

### Task 4: 增加企业筛选与一图流局部展开

**Files:**
- Modify: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js:1-272`
- Modify: `wiki/reports/rd-数字员工-v1-h5.html`

**Interfaces:**
- Consumes: `[data-company-filter]`、`tr[data-industry][data-level]`、`[data-detail-toggle]` 和对应 `[data-detail-panel]`。
- Produces: `initCompanyFilters(): void`、`initDetailToggles(): void`；隐藏行使用 `hidden` 属性；展开按钮同步 `aria-expanded`。

- [ ] **Step 1: 在 HTML 中加入可降级筛选和展开接口**

```html
<div class="research-filters" aria-label="企业调研筛选">
  <button type="button" data-company-filter="all" aria-pressed="true">全部</button>
  <button type="button" data-company-filter="互联网">互联网</button>
  <button type="button" data-company-filter="金融">金融</button>
  <button type="button" data-company-filter="支付">支付</button>
  <button type="button" data-company-filter="AI软件">AI软件</button>
</div>
```

展开按钮使用 `aria-controls` 指向静态可读的详情区域；脚本加载后才附加可折叠状态，避免无脚本隐藏内容。

- [ ] **Step 2: 实现 `initCompanyFilters()`**

```javascript
function initCompanyFilters() {
  const buttons = Array.from(document.querySelectorAll("[data-company-filter]"));
  const rows = Array.from(document.querySelectorAll("tr[data-industry][data-level]"));
  if (!buttons.length || !rows.length) return;

  const apply = (value) => {
    rows.forEach((row) => {
      row.hidden = value !== "all" && row.dataset.industry !== value;
    });
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.companyFilter === value));
    });
  };

  buttons.forEach((button) => {
    button.addEventListener("click", () => apply(button.dataset.companyFilter));
  });
}
```

- [ ] **Step 3: 实现 `initDetailToggles()`**

规则：初始化时只折叠带 `[data-detail-enhanced]` 的面板；点击唯一按钮后切换 `hidden` 和 `aria-expanded`；找不到目标时保持静态内容可见。

- [ ] **Step 4: 在启动入口调用两个函数**

在现有初始化序列末尾加入：

```javascript
initCompanyFilters();
initDetailToggles();
```

- [ ] **Step 5: 运行语法和静态验证**

Run: `node --check wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js`

Run: `python scripts/verify_rd_digital_employee_h5.py`

Expected: 两条命令退出码均为 `0`。

- [ ] **Step 6: 提交交互增强**

```powershell
git add wiki/reports/rd-数字员工-v1-h5.html wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js
git commit -m "feat: add accessible research interactions"
```

---

### Task 5: 完成证据复核、视觉验收与门禁记录

**Files:**
- Modify: `wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md`
- Modify only if defects are found: `wiki/reports/rd-数字员工-v1-h5.html`
- Modify only if defects are found: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css`
- Modify only if defects are found: `wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js`

**Interfaces:**
- Consumes: Tasks 1—4 的完整本地 H5。
- Produces: 通过的静态检查、桌面/移动视觉检查、控制台结果和更新后的 gate review；任何未验证项保持显式阻塞。

- [ ] **Step 1: 运行完整静态检查**

Run: `python -m unittest tests.test_verify_rd_digital_employee_h5 -v`

Run: `python scripts/verify_rd_digital_employee_h5.py`

Run: `node --check wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js`

Run: `git diff --check -- wiki/reports/rd-数字员工-v1-h5.html wiki/reports/assets/rd-digital-employee-profile-v1-h5/styles.css wiki/reports/assets/rd-digital-employee-profile-v1-h5/app.js scripts/verify_rd_digital_employee_h5.py tests/test_verify_rd_digital_employee_h5.py`

Expected: 所有命令退出码为 `0`。

- [ ] **Step 2: 在 1440×1000 做桌面 fresh visual QA**

检查并记录：

- 页面 01 七层主线十秒内可理解，右栏和底部链路无裁切。
- 页面 02 表格可找到企业、数据、等级和证据缺口，筛选状态正确。
- 六页视觉语法不同，没有重新变成同构卡片。
- 页面 04 六环关系清楚，页面 06 四泳道对齐。
- 控制台 error 数量为 `0`。

- [ ] **Step 3: 在 390×844 做移动 fresh visual QA**

检查并记录：

- 页面本身 `scrollWidth === clientWidth`。
- 表格、等级轴、时间轴只在各自容器横向滚动。
- 关键正文不小于 `12px`，按钮可触控，焦点样式可见。
- 关闭 JavaScript后六页和企业表仍完整可读。

- [ ] **Step 4: 更新 gate review**

在 `wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md` 记录：

- Article Intent Contract 与最终章节逐项对应。
- 参考图的保留、改造和拒绝项。
- 企业证据来源、核验日期、评级缺口和未采用案例。
- 桌面/移动视觉结果、控制台结果和任何残余风险。
- 明确“未发布、未部署、未同步飞书”。

- [ ] **Step 5: 最终差异复核并提交**

```powershell
git status --short
git diff --check
git add wiki/ops/rd-digital-employee-profile-v1-h5-gate-review-2026-08-05.md
git commit -m "docs: record digital employee H5 visual QA"
```

提交前只暂存本任务文件；不得带入仓库中已有的其他修改或临时文件。
