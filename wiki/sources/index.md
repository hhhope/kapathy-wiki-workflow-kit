# Sources

Source pages represent upstream evidence such as Feishu documents, meeting notes, and attachments.

## Current Pages

- [Feishu Weekly Sync Sample](feishu-weekly-sync-sample.md): starter evidence page with link metadata and downstream usage
- [Feishu Wiki Source FYDcwFGaOi6A1Bkg9rfcIp3DnCS](feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md): recorded original Feishu wiki URL with current fetch blocker notes
- [涅槃项目周报 2026-04-13](nirvana-weekly-2026-04-13.md): 第一条真实项目周推进来源页，承接 `inbox/nirvana/涅槃焕新周报.xlsx`
- [涅槃项目周视图 2026-04-13](nirvana-weekly-view-2026-04-13.md): 对应 `preview .html` 的周视图来源页，承接甘特图、能力地图和技术建设视角

## Usage Notes

- Record source metadata even when the body stays external.
- Track which domain, report, and timeline pages depend on the source.

## 会议纪要放置规则

- 原始会议纪要文件先进入 `inbox/`
- 会议纪要的长期整理页放在 `wiki/sources/`
- 如果纪要进一步被提炼成管理汇报或项目汇报，再在 `wiki/reports/` 里组装输出
- 如果纪要触发了个人待办、提醒或 handoff，再额外链接到 `wiki/ops/`

推荐命名：

- 文件投递：`inbox/<project-or-topic>/<原始文件名>`
- 来源页：`wiki/sources/<project-or-topic>-meeting-YYYY-MM-DD.md`
