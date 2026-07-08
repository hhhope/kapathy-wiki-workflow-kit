---
name: compound-learning
description: 经验复利系统——项目级错题本+通用能力库的双层外部记忆。⚠️强制约束：收到任务目标后必须先检查是否存在 PROJECT.md，不存在则创建；必须执行 Phase 0（PRD锁定），禁止跳过。触发时机：(1)上下文中存在PROJECT.md时，收到任务目标后先读PRD和错题本再执行；(2)任务完成后，对话中出现过纠错/追问/路径调整则自动附上PROJECT.md更新；(3)Sprint第5天无条件输出Sprint复盘；(4)用户说"复盘"、"定期回顾"、"查错题"、"注入Skill"、"项目结案"。加载后读取references/RULE.md获取完整行为约束。
---

# 经验复利系统

> **经验库根目录**：`/home/yan/.claude/projects/<项目名>/memory/`
> - 例如：`/home/yan/.claude/projects/baofoo-open-demo/memory/`

## 文件结构

```
memory/                           ← 经验库根目录
├── INDEX.md                      ← 放入System Prompt，永远轻量
├── general/
│   └── general.md                ← 跨项目晋升层（≥2项目才进）
└── projects/
    ├── _template/
    │   └── PROJECT.md            ← 新项目复制此模板
    ├── project-a/
    │   └── PROJECT.md           ← 进行中
    └── archive/                 ← 已结案项目
```

**上下文加载策略**：INDEX在System Prompt中常驻；当前项目PROJECT.md按需上传；general.md只在定期回顾时加载。不全量加载，上下文成本不随积累膨胀。

---

## Phase 0：PRD锁定（执行的前置条件）

> **进入条件**：用户给出**新的任务目标**时，必须先检查 PROJECT.md 是否存在：
> - 已存在且 PRD 已锁定 → 进入 Phase 1
> - 已存在但 PRD 未锁定 → 完成 PRD 锁定
> - 不存在 → 创建 PROJECT.md，然后执行 Phase 0

**完整流程**：
1. 收集需求 → 2. 产出PRD草稿 → 3. 拆分Task → 4. 标记需要澄清项 → 5. 确认后锁定

### 步骤1：收集需求
收到任务目标后，先确认理解需求边界：
- 目标是什么？
- 验收标准有哪些？
- 明确不在范围内的事项（Out of Scope）

### 步骤2：产出PRD草稿
- 列出验收标准（每条必须可验证）
- 列出 Out of Scope
- **标注风险点**：哪些对自己最容易完成的部分

### 步骤3：拆分Task（重要！）⚠️
**必须使用 Task 工具创建任务**

使用 Task 工具创建每个子任务：
```
TaskCreate(
  subject: "验收子项",
  description: "具体描述 + 预计时间(秒)",
  priority: P1/P2/P3,
  status: pending
)
```

拆分规则：
- 单个 Task 预计时间 > 60秒 → 必须拆分
- 高优先级（P1）优先执行
- 完成后 TaskUpdate(status: completed)

### 步骤4：标记需要澄清项 ⚠️
识别需要用户澄清的事项，**必须降优先级**：
```
### 需要澄清 [Notify]
| 事项 | 优先级 | 原因 |
|------|--------|------|
| XXX文件的具体要求 | P2 | 缺少上下文 |
| XXX接口的约束条件 | P2 | 未明确 |
```
- 降为 P2 或 P3
- 优先执行无需澄清的部分

### 步骤5：确认后锁定
- 你确认或修改PRD
- 你说「锁定」，PRD不得在执行中修改
- Task 优先级已确定

**PRD未锁定 = 不执行。硬规则。**

---

## Phase 1：Kickoff（收到目标后）

### 完整流程
1. 加载 PROJECT.md → 确认项目状态
2. 检查 Progress → 如已有进度则从断点继续
3. 读 PRD / 错题本 → 标记高风险节点
4. 执行或继续执行

### 步骤1：加载 PROJECT.md

**PROJECT.md 查找路径**（按优先级）：
1. `/home/yan/.claude/projects/<当前项目名>/memory/PROJECT.md`
2. `./memory/PROJECT.md`（当前工作目录下）
3. `./PROJECT.md`

- **强制检查**：IF PROJECT.md 不存在 THEN 创建后再执行
- 检查 PRD 状态：是否已锁定？
  - 已锁定 → 继续步骤2
  - 未锁定 → 引导进入 Phase 0

### 步骤2：检查 Progress（断点续传）
使用 Task 工具检查任务状态：
```
TaskList() → 查看 pending/in_progress 任务
TaskGet(taskId: "xxx") → 查看具体任务详情
```
- 如有进行中的任务 → 从断点继续（使用 TaskGet 获取详情）
- 全部完成 → 正常开始新任务

### 步骤3：读错题本
- 标记高风险节点
- 有高度相关历史错误 → 一句话说明后执行
- 无 → 静默执行

---

## Phase 2：执行

### 必须使用 Task 工具跟踪
- 每个子任务创建后：TaskUpdate(status: in_progress)
- 完成后：TaskUpdate(status: completed)
- 中断恢复：TaskList 查看状态，从断点继续

### 执行规则
- 出现纠错/追问 → 任务pivot到新目标继续执行，内部静默标记偏差点
- 判断分叉 → 参照PRD和错题本内部决策，不提问
- 唯一可提问：PRD未覆盖的外部事实缺口，一次问完

---

## Phase 3：任务完成 — 交付+经验写入一次完成

输出结构：
```
[任务产出本体]

---
[PROJECT.md 更新版本]
```

触发附上PROJECT.md更新的条件（满足任一）：
- 执行中出现过纠错/追问/路径调整
- Sprint第5天

否则只交付任务产出，不附PROJECT.md。

---

## 错误归因框架

每条错题写入前必须过此判断链：

```
Claude执行时信息是否充足？
│
├─ 不充足 → Claude有没有追问？
│   ├─ 没追问就执行 → Claude的错（应问未问）→ 注入Skill
│   └─ 追问了，补充仍不清晰 → 你的错（描述问题）→ 记你的错题本
│
└─ 充足 → Claude判断对不对？
    ├─ 判断错 → Claude的错 → 注入Skill
    └─ 判断对但你改了预期 → 目标未对齐 → 检查PRD
```

PROJECT.md更新格式：
```
## 复盘 [任务名/Sprint N] [日期]
PRD验收：✅ / ⚠️[一句话] / ❌[一句话]

[错误名] | 主人：你/Claude | 归因：描述不清/应问未问/判断错误/目标漂移
触发条件：[具体信号]
决策链：IF [信号] THEN [动作]
晋升通用层：是/否
```

---

## Phase 4：项目结案

用户说「项目结案」时触发：
- 错题本中标"晋升：是"的条目 → 写入general.md
- 更新INDEX项目列表
- 输出：更新后的general.md + INDEX + 归档PROJECT.md

**晋升条件**：同类错误/能力出现在≥2个项目，一次不晋升。

---

## Phase 5：定期回顾（每2-4周）

用户上传所有PROJECT.md + general.md，说「定期回顾」：
1. 扫描跨项目重复错误模式
2. 更新通用能力成熟度（🌱→🔥→✅）
3. 关闭已达标学习计划（先关再开）
4. 生成新学习计划（≤3条活跃，无验收标准的拒绝输出）
5. 输出全部变更文件

---

## 输出规范

| 内容 | 上限 |
|------|------|
| 单次复盘 | 300字 |
| 单条错题 | 80字 |
| 单条Skill注入建议 | 60字 |
| 单条学习计划 | 100字 |

超出 = 提炼不够，重压缩。

---

## 经验质量自检

每条错题输出前：
- ✅ 有具体触发信号，不是"情况复杂时"
- ✅ 决策链是动作不是意图
- ✅ 有失效边界
- ✅ 6个月后看到能立刻改变决策
- ❌ 读完只感觉有道理但行为不变 → 重写

---

## 参考文件

- `references/RULE.md` — 完整行为约束，skill加载后读取
- `references/INDEX-template.md` — 经验库索引模板（放入System Prompt）
- `references/PROJECT-template.md` — 项目文件模板（新项目复制）
- `references/general-template.md` — 通用能力库模板
