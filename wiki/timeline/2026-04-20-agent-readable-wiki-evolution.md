# 2026-04-20 Agent-Readable Wiki Evolution Timeline

这页只做一件事：把今天这条 wiki 治理主线按时间拉直，方便回看什么属于原始需求，什么属于后来的漂移。

## 早上确认的主线

原始需求是把这套 wiki 做成一个更容易让 agent 看懂历史分歧和决策演变的底座。

当时确认的顺序是：

1. naming
2. frontmatter
3. graph extraction
4. relation analysis
5. small migration

## 先沿原始主线推进的阶段

### 命名与结构层

- `b68d568` propose wiki naming model
- `6156cb4` archive wiki naming model change
- `2987012` propose wiki frontmatter
- `f197dfb` archive wiki frontmatter model change

这一段仍然属于“让对象更容易被识别”的原始主线。

### 结构提取与关系分析层

- `22459b2` propose wiki graph extraction
- `c2c9182` archive wiki graph extraction change
- `0b3cab0` propose wiki relation analysis
- `f28599a` archive wiki relation analysis change

这一段仍然可以被理解为“先把对象和关系提出来，再谈阅读”。

### 小范围迁移层

- `4878902` propose small wiki naming migration pilot
- `80c6232` archive small wiki naming migration pilot

这一段是原始主线里的收敛试点。

## 偏移开始的阶段

### 从分析层滑向 runtime 链

后面开始出现的链条是：

- semantic scoring
- utilization
- runtime context
- source integration
- auto routing
- context injection
- bounded self-directed execution

对应提交链起点大致从这里开始明显偏离：

- `0e8afec` propose wiki semantic scoring
- `b6724a9` propose wiki runtime context
- `6643992` propose runtime context source integration
- `45c1c24` propose runtime auto routing
- `8c0905f` propose automatic context injection
- `b0531cd` propose bounded self-directed execution

这些步骤在技术上连续，但已经不再等同于早上确认过的阅读主线。

## 回锚阶段

当用户明确指出“完全偏了”“回到早上的需求”之后，这条争议被正式记录：

- [live-conversation-reanchor-gate / retro](/mnt/d/cloud/account-meeting-lore/wiki/ops/live-conversation-reanchor-gate-retro.md)
- [ADR-0024 Live Conversation Re-Anchor Before Continued Implementation](/mnt/d/cloud/account-meeting-lore/wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md)

这一阶段重新确认了：

- 争议已经被记录
- runtime 链不再继续默认扩展
- 当前要回到最基础的阅读问题

## 当前回到的阅读问题

现在剩下的不是继续补 runtime，而是补三个阅读视图：

1. 时间线视图
2. 同类文档视图
3. 可读图谱 / 关系视图

## 这页怎么用

- 想看“今天怎么一步步偏的”，先看这页
- 想看“原始主线和偏移链分别是什么”，先看这页
- 想看“为什么现在要回到阅读层”，先看这页，再去同类文档视图和关系视图
