# Trigger Validation

Use this file when validating whether the skill triggers too broadly or too narrowly.

## Should Trigger

1. `Generate a management H5 weekly report from this gantt and capability map.`
2. `Turn these schedule updates into a single-file HTML project report with milestones.`
3. `I need a project weekly report for leadership with gantt, capability map, and technical construction.`
4. `Make a PPT weekly report from this project schedule and capability status.`
5. `Here are the workstreams, MVP target, and milestones. Turn them into a management report.`
6. `Use the latest schedule and output a long H5 update for leadership.`

## Should Not Trigger

1. `Write a daily standup summary from today's tasks.`
2. `Beautify this generic PPT deck about product strategy.`
3. `Create a detailed design document for split billing.`
4. `Summarize this Jira ticket into acceptance criteria.`

## Known Ambiguous Cases

1. `Make a project update slide.`
Resolution: trigger only if gantt, capability-map, milestone, or technical-construction structure is present or requested.

2. `Write an executive project summary.`
Resolution: trigger only if the request is schedule-driven and management-report structured, not a generic status memo.
