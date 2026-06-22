# req-agent kit

`req-agent kit` 是一套需求评审工作流安装包，用来把松散的 PRD、会议纪要、Jira 文本或口头材料，整理成可审查、可追溯、可阻断的需求状态。

它不是单独的 skill 包。它会一起安装：

- `req-agent` 控制器 skill
- `req-*` 分工 worker skills
- 需求领域 taxonomy
- Python 证据脚本
- 单元测试和 fixture
- OpenSpec 审计材料
- AGENTS 路由片段

正常入口只有一个：

```text
$req-agent <需求材料或问题>
```

普通用户不需要直接调用 Python 脚本，也不需要直接调用 `req-intake`、`req-domain-analysis`、`req-scope` 等 worker skills。它们是 `req-agent` 内部使用的证据工具和分工模块。

## 这个 kit 解决什么

它解决的是一个高频问题：AI 看到需求材料后，很容易直接跳到方案、接口、DDL 或实现。`req-agent` 把这个动作挡住，先做需求识别、领域分析、范围澄清、故事和验收覆盖，再决定是否允许 OpenSpec handoff。

核心目标：

- 先识别这是不是需求工作，而不是实现工作
- 先找或创建需求 case，而不是散聊散写
- 先用 taxonomy 做 DDD 领域分析，而不是靠感觉分类
- 先补 stories、acceptance、coverage 和 blockers
- 只在 requirement readiness 通过后创建 OpenSpec draft
- OpenSpec draft 仍然不是实现批准

## Taxonomy 和 DDD 模型

需求领域词表在：

```text
requirements/config/requirements-taxonomy.yaml
```

它是需求领域 taxonomy，不是 wiki frontmatter taxonomy。它的核心价值不是“给需求贴分类标签”，而是对我们现有支付生态做 DDD 解构和重塑：先把业务问题拆成稳定的领域对象，再让需求故事、context 协作、验收闭环都回到同一套领域语言上。

这条主线不能丢：

```text
+------------+     +----------+     +----------+     +----------+     +--------+
| classify   | --> | model    | --> | standard | --> | discuss  | --> | reuse  |
| 分类       |     | 建模     |     | 标准     |     | 讨论     |     | 复利   |
+------------+     +----------+     +----------+     +----------+     +--------+
```

- 分类是行为：识别需求落在哪些支付子域和相邻生态。
- 建模是目的：把 story、bounded context、aggregate、handoff、fact owner 对齐。
- 标准是产物：把可复用的领域判断沉到 taxonomy、gate、coverage 和 acceptance 类型里。
- 讨论是协作方式：产品、研发、财务、风控、运营围绕同一套对象讨论，而不是各说各话。
- 复利是长期收益：下一次需求不是从零开始，而是在已有领域语言、验收面和协作边界上继续扩展。

两类 taxonomy 的边界必须分开：

```text
+-----------------------------------------------+
| requirements/config/requirements-taxonomy.yaml |
|                                               |
| Owns: requirement readiness vocabulary         |
| Used by: req-agent, checker scripts, gates     |
+--------------------------+--------------------+
                           |
                           | separate from
                           v
+-----------------------------------------------+
| wiki/config/frontmatter-taxonomy.yaml          |
|                                               |
| Owns: wiki page identity and metadata          |
| Used by: wiki routing / page classification    |
+-----------------------------------------------+
```

当前 taxonomy 按 DDD 思路组织。以当前数据为准，它有 2 个 `business_ecosystems`、13 个 `subdomains`：支付生态 8 个核心 subdomain，Agent 服务相邻生态 5 个 subdomain。

```text
+----------------------------------+
| requirements DDD taxonomy        |
+----------------+-----------------+
                 |
                 v
+-------------------------------+      +-------------------------------+
| payment_ecosystem             |      | agent_service_ecosystem       |
| 8 core payment subdomains     |      | 5 adjacent service subdomains |
+---------------+---------------+      +---------------+---------------+
                |                                      |
                v                                      v
+-------------------------------+      +-------------------------------+
| merchant_platform_relationship|      | agent_entitlement             |
| billing_revenue               |      | agent_usage_metering          |
| payment_transaction           |      | agent_workspace_seat          |
| account_balance               |      | agent_service_catalog         |
| funds_movement_settlement     |      | agent_service_delivery        |
| financial_operations          |      +-------------------------------+
| risk_compliance               |
| embedded_financial_products   |
+-------------------------------+
```

支付生态的 8 个核心 subdomain 是我们对现有支付领域的第一层解构：

```text
payment_ecosystem
  |
  +-- merchant_platform_relationship
  |     +-- merchant / platform / capability / service offering / responsibility
  |
  +-- billing_revenue
  |     +-- subscription / invoice / usage rating / dunning / revenue recovery
  |
  +-- payment_transaction
  |     +-- intent / attempt / authorization / charge / refund / dispute
  |
  +-- account_balance
  |     +-- payment account / balance / ledger / fund state / reserve
  |
  +-- funds_movement_settlement
  |     +-- transfer / split / settlement batch / payout / schedule
  |
  +-- financial_operations
  |     +-- reconciliation / fee accounting / reporting / exception / close
  |
  +-- risk_compliance
  |     +-- KYB/KYC / AML / mandate / risk decision / monitoring
  |
  +-- embedded_financial_products
        +-- issuing / treasury / spend management / capital
```

Agent 服务生态不是支付生态的替代品，而是相邻生态。比如 Agent 订阅支付同时落在 `billing_revenue`、`payment_transaction`、`account_balance`、`financial_operations`、`risk_compliance`，也会碰到 `agent_entitlement`、`agent_usage_metering` 或 `agent_workspace_seat`。这就是 context 重叠和协作边界出现的地方。

领域判断如何形成需求闭环：

```text
+------------------+
| domain/subdomain |
+--------+---------+
         |
         v
+------------------+
| bounded contexts |
| overlap/handoff  |
+--------+---------+
         |
         v
+------------------+
| aggregate roots  |
| lifecycle/state  |
+--------+---------+
         |
         v
+------------------+
| stories          |
| role + want      |
+--------+---------+
         |
         v
+------------------+
| acceptance       |
| state/handoff/   |
| failure/evidence |
+--------+---------+
         |
         v
+------------------+
| coverage gates   |
| reusable standard|
+------------------+
```

每层的含义：

| 层级 | 作用 |
|---|---|
| `business_ecosystems` | 最大业务生态，例如支付生态、Agent 服务生态 |
| `subdomains` | 需求问题域，例如计费收入、支付交易、账户余额、清结算、风控合规 |
| `bounded_contexts` | 规则、状态和职责边界相对稳定的上下文 |
| `aggregate_roots` | 有生命周期、状态变化或验收覆盖要求的业务对象 |
| `fact_owners` | 事实责任方，是义务，不一定是用户故事里的真实 actor |
| `trigger_rules` | 当某些条件出现时，强制引入额外上下文、子域或 owner 义务 |

## Taxonomy 如何维护和继续建立

维护 taxonomy 时不要只问“这个词放在哪个分类下”，而要问“它是否形成了可复用的业务模型和讨论标准”。

新增或调整规则：

| 对象 | 什么时候可以新增 | 不应该怎么做 |
|---|---|---|
| `subdomain` | 能说明独立 business problem，并能承载一组稳定 contexts、aggregates、owners | 只因为一个页面、一个功能名或一个团队名就新增 |
| `bounded_context` | 有独立规则、状态、生命周期、owner 或集成边界 | 把所有协作都压进一个大 context |
| `aggregate_root` | 有明确生命周期、状态变化、账务事实或验收覆盖价值 | 把报表、页面、流程名当 aggregate |
| `fact_owner` | 代表事实责任、规则责任或证据责任 | 直接冒充 user story actor |
| `trigger_rule` | 某个条件一出现就必然引入额外 context、subdomain、owner 或 evidence | 写成泛泛提醒，不能驱动 gate |

context 重叠时的处理方式：

- 不急着合并 context，先记录 handoff。
- 不急着争论归属，先识别谁拥有事实、谁发起状态变化、谁提供证据。
- 一个 story 可以引用多个 domain/context，但必须说明主责和协作边界。
- 验收必须覆盖 state change、handoff、failure path、evidence surface，而不是只验 UI 或 happy path。
- 没确认的领域不要硬塞进 taxonomy；保留为 candidate、open question 或 follow-up。

维护入口：

- 当前 taxonomy 数据：[requirements-taxonomy.yaml](payload/requirements/config/requirements-taxonomy.yaml)
- DDD taxonomy 结构校验：[check_requirements_ddd_taxonomy.py](payload/scripts/check_requirements_ddd_taxonomy.py)
- DDD readiness gate：[requirements_ddd_readiness.py](payload/scripts/requirements_ddd_readiness.py)
- domain coverage gate：[requirements_domain_coverage.py](payload/scripts/requirements_domain_coverage.py)
- domain coverage 测试：[test_requirements_domain_coverage_gate.py](payload/tests/test_requirements_domain_coverage_gate.py)
- req-agent 规范入口：[spec.md](payload/openspec/changes/req-agent/specs/req-agent/spec.md)

关键约束：

- 不要把弱匹配词强塞进已有 taxonomy ID
- 不要把 `subscription_owner` 这类 fact owner 直接当成用户故事 actor
- 不确定的词保留为 candidate、open question、light coverage、out of scope 或 follow-up

## 需求评审流程

整个流程是分阶段的，目的不是让 AGI 一步到位，而是让每一步都有证据和停止条件。

```text
+--------------------+
| 1. intent routing  |
| req-agent          |
+---------+----------+
          |
          v
+--------------------+
| 2. case resolution |
| find/create case   |
+---------+----------+
          |
          v
+--------------------+
| 3. intake          |
| req-intake         |
+---------+----------+
          |
          v
+--------------------+
| 4. domain analysis |
| req-domain-analysis|
+---------+----------+
          |
          v
+--------------------+
| 5. scope           |
| req-scope          |
+---------+----------+
          |
          v
+--------------------+
| 6. stories         |
| req-stories        |
+---------+----------+
          |
          v
+--------------------+
| 7. acceptance      |
| req-acceptance     |
+---------+----------+
          |
          v
+--------------------+
| 8. readiness gate  |
| req-handoff        |
+---------+----------+
          |
          v
+--------------------+
| OpenSpec draft     |
| stop, no implement |
+--------------------+
```

每个阶段的职责：

| 阶段 | Worker | 产物 |
|---|---|---|
| 1. 识别意图 | `req-agent` | 判断用户是在 intake、分析、澄清范围、补验收、查 ready，还是要 handoff |
| 2. 解析 case | `req-agent` + scripts | 找到当前需求 case，或按仓库策略创建/追加 |
| 3. 收集材料 | `req-intake` | source、provenance、assumptions、immediate gaps |
| 4. 领域分析 | `req-domain-analysis` | DDD `domain_model`、候选分类、coverage obligations |
| 5. 范围澄清 | `req-scope` | actors、owners、boundaries、unknowns |
| 6. 用户故事 | `req-stories` | role/want/benefit，并挂 domain/context/aggregate/evidence anchors |
| 7. 验收函数 | `req-acceptance` | `state_change`、`handoff`、`failure_path`、`evidence` 类型验收 |
| 8. 就绪门禁 | `req-handoff` | readiness report；通过后才生成 OpenSpec draft |

## 我们如何识别需求

`req-agent` 先把需求意图和实现意图区分开。

常见需求信号：

- PRD、会议纪要、Jira ticket、用户访谈材料
- 用户要求“梳理需求”“拆需求”“补验收标准”
- 用户询问范围、角色、边界、依赖、风险、ready 状态
- 用户要求把需求转成 OpenSpec 草案

常见非直接实现信号：

- 材料还没有 owner
- 业务规则没有定口径
- 系统边界没有确认
- 只有目标，没有 acceptance 或 current state

识别后，`req-agent` 必须输出：

- Intent
- Case
- State
- Allowed Action
- Blocked Action，若当前被阻断
- Next Action
- Evidence

## 我们如何进行需求分析

需求分析不是只写用户故事。它先拆四层证据：

```text
+------------------+      +------------------+
| source material  | ---> | actors           |
| PRD / meeting    |      | real people/sys  |
+------------------+      +------------------+
          |
          v
+------------------+      +------------------+
| taxonomy match   | ---> | domain_model     |
| DDD vocabulary   |      | ecosystem/context|
+------------------+      +------------------+
          |
          v
+------------------+      +------------------+
| context rules    | ---> | role_obligations |
| trigger_rules    |      | owner duties     |
+------------------+      +------------------+
          |
          v
+------------------+      +------------------+
| coverage checks  | ---> | domain_coverage  |
| stories/accept   |      | covered/blocked  |
+------------------+      +------------------+
```

四层含义：

- `actors`：材料中真实出现的人、组织、系统或自动化主体
- `domain_model`：基于 taxonomy 的 DDD 分类
- `role_obligations`：由上下文、handoff、trigger rule 推导出的事实责任义务
- `domain_coverage`：每个 in-scope subdomain/context/aggregate 是否有 story、acceptance 和 review note

这样做可以避免两个常见错误：

- 把 owner obligation 当成真实用户 actor
- 只写 owner story，却漏掉 aggregate lifecycle、handoff、failure path 和 evidence acceptance

## 我们会产出什么

根据 case 状态，工作流会产出：

- requirements case
- source provenance 和 open questions
- DDD `domain_model`
- candidate classification table
- domain coverage obligations
- roles、ownership、boundaries、unknowns
- user stories
- acceptance functions
- readiness report
- OpenSpec draft

OpenSpec draft 是 handoff，不是实现批准。生成 draft 后应停止，等待用户 review 和后续明确指令。

## 我们如何与 AGI 协作

AGI 在这里不是业务真相来源，而是结构化评审和证据整理伙伴。

```text
+------------------+      +------------------+
| human            |      | AGI / req-agent  |
| business intent  | ---> | routing          |
| source material  |      | analysis         |
| rule decisions   | <--- | gaps/questions   |
| waiver decisions |      | evidence report  |
+------------------+      +------------------+
          |
          v
+------------------+
| OpenSpec / code   |
| only after gates  |
+------------------+
```

分工原则：

- 人负责业务材料、当前状态、规则口径、系统边界和 waiver 决策
- `req-agent` 负责路由、状态报告、下一步 allowed action
- worker skills 每次只做一个边界清晰的动作
- Python scripts 负责机器可检查的证据
- AGI 必须保留不确定性，不能脑补当前状态、规则参数、会计处理或系统边界

## 质量门

需求就绪和详细设计就绪是两件事。

```text
+------------------------+
| domain_model_gate      |
| taxonomy ids valid     |
+-----------+------------+
            |
            v
+------------------------+
| domain_coverage_gate   |
| coverage explicit      |
+-----------+------------+
            |
            v
+------------------------+
| requirement_delivery   |
| stories + acceptance   |
+-----------+------------+
            |
            v
+------------------------+
| requirements_ready     |
| OpenSpec draft allowed |
+-----------+------------+
            |
            v
+------------------------+
| detailed_design_gate   |
| current state/rules/   |
| system boundary needed |
+-----------+------------+
            |
            v
+------------------------+
| design or implement    |
| still needs approval   |
+------------------------+
```

门禁说明：

| Gate | 含义 |
|---|---|
| `domain_model_gate` | domain model 使用已知 taxonomy ID，或把未知项显式记录为 candidate/open question |
| `domain_coverage_gate` | in-scope domain、context、aggregate lifecycle、handoff、failure path、evidence surface 已覆盖或显式分类 |
| `requirement_delivery_gate` | stories、acceptance、mapping、provenance、traceability 可审查 |
| `detailed_design_gate` | 进入 API、DDL/schema、状态机、规则模型、集成契约、工程拆解前，产品侧设计输入必须存在或被显式 waiver |

`requirements_ready` 只表示需求骨架可审查，不表示可以开始详细设计或实现。

详细设计至少需要：

- current-state material package
- business rule position table
- system boundary contract table

## 安装内容

- Codex skills：`.codex/skills/req-*`
- 需求脚本：`scripts/*requirements*.py`
- 需求 taxonomy：`requirements/config/requirements-taxonomy.yaml`
- 验证测试：`tests/`
- 样例：`docs/req-agent/examples/embedded-account-phase1.md`
- 回归 fixture：`wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`
- OpenSpec 审计材料：`openspec/changes/req-agent/`
- AGENTS 路由片段：`docs/req-agent/AGENTS_SNIPPET.md`

## 安装方式

从本地 package 目录安装：

```bash
npm install -g /path/to/account-skills/req-agent-kit/req-agent
req-agent-install /path/to/target-repo --mode codex-repo --update-agents --verify
```

从 tarball 安装：

```bash
cd /path/to/account-skills/req-agent-kit/req-agent
npm pack
npm install -g ./account-skills-req-agent-installer-0.1.0.tgz
req-agent-install /path/to/target-repo --mode codex-repo --update-agents --verify
```

发布到 npm 后安装：

```bash
npm install -g @account-skills/req-agent-installer
req-agent-install /path/to/target-repo --mode codex-repo --update-agents --verify
```

直接从目标仓库根目录安装：

```bash
bash /path/to/account-skills/req-agent-kit/req-agent/install.sh . --mode codex-repo --update-agents --verify
```

如果目标仓库已有不同内容，installer 会停止覆盖。确认要替换时使用：

```bash
bash /path/to/account-skills/req-agent-kit/req-agent/install.sh . --mode codex-repo --update-agents --force --verify
```

## 运行要求

- `python3`
- `PyYAML` 可通过 `import yaml` 导入
- 可选：`openspec` CLI，用于 OpenSpec validation

## 还有什么未做

- 当前包内 OpenSpec 审计材料描述的是核心 `req-agent` 包；后续 DDD/domain coverage 加硬主要体现在 payload tests 和行为资产里，还没有完全合并成一份包级 OpenSpec 历史。
- installer 能验证本地脚本和测试，但不能证明未来每次 AGI 会自动选出完美 domain coverage；仍需要人审。
- kit 不会自动改目标仓库的业务 taxonomy 或治理策略；接入团队仍要确认 taxonomy fit、owner 命名和 case 存储约定。
- OpenSpec draft 仍只是 handoff，不是实现批准。
