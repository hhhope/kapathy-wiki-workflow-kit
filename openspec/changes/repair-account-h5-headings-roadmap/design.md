# Design: Account H5 Heading And Fishbone Roadmap Repair

## Heading Standard

Section titles should be training-material titles, not narration about the
draft process. Avoid titles such as `这版先看...` or `...怎么看`. The page should
read like an internal onboarding artifact.

## Target Section Shape

Keep the existing H5 flow but repair the visible section titles:

1. Cover
2. 你加入的是什么小组
3. 账户体系能力地图
4. 系统架构
5. 核心业务链路
6. 我们支撑的对象
7. 常见问题
8. 正在做的项目
9. 技术规划路线
10. AI 如何与我们协作
11. AI Coding 成熟度：当前站在哪一层
12. 新人前三天和第一周
13. 30 / 60 / 90 天成长路径
14. 新人可以进入的任务池
15. Closing

## Fishbone Roadmap

Create a standalone technical roadmap fishbone:

- Spine: account-group technical planning from model convergence to reliable
  funds-result governance.
- Branches:
  - 统一账户模型
  - 余额服务规划
  - 账务标准化
  - 结算 / 对账平台收敛
  - 可观测与风险地图
  - 技术栈升级与知识复用
- Each branch should show concrete planning items from source materials rather
  than generic slogans.

## Verification

- SVG parse check for the new fishbone asset.
- PNG export and screenshot inspection.
- HTML parser check.
- Heading grep for required titles and deleted process title.
- Sensitive-info grep.
- Desktop and mobile screenshots.
- `git diff --check`.
- `openspec validate repair-account-h5-headings-roadmap --strict`.
