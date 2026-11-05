# GPT-5.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.5
- 模型名称：GPT-5.5
- 发布日期：2026-04-23
- 最近检查时间：2026-11-05T07:39+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：1
- 收集前已有成绩数量：31
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- OpenAI API 文档确认 GPT-5.5 快照为 gpt-5.5-2026-04-23；DeepSWE 榜单中的 gpt-5.5[xhigh] 可对应本地该模型。
- 本轮将已有 SWE-Bench Pro 58.6 行来源修正为 OpenAI 原始发布页，并移除无法确认是评测日期的 2026-05-28；该行未标 Pro V2，仍不计入目标 V2。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 67 (metric=pass rate; version=1.1; dataset=113 tasks; effort=xhigh; harness=mini-swe-agent) | [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [OpenAI GPT-5.5 API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5) | 2026-11-05T07:39+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| terminal-bench-v4 | 待核实 | 78.2 (metric=success rate; version=2.1; harness=Terminus-2); 84.1 (metric=pass@1; version=2.1; variant=xhigh; harness=Codex); 75.8 (metric=pass@1; version=2.1; variant=medium; harness=Codex); 73.4 (metric=pass@1; version=2.1; variant=medium; harness=Cursor CLI); 82.7 (metric=success rate; version=2.0) | [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/), [OSWorld-V2 v2.1 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| chartography | 已收录 | 31 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=xHigh; harness=Inspect AI) | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测代码与方法](https://github.com/surge-ai/chartography) | 2026-11-05T07:39+08:00 |
| humanitys-last-exam | 已存在 | 41.4 (metric=accuracy; variant=no tools); 52.2 (metric=accuracy; variant=with tools) | [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/), [OpenAI GPT-5.5 API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5) | 2026-11-05T07:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis GPT-5.5 型号页](https://artificialanalysis.ai/models/gpt-5-5), [Artificial Analysis Intelligence Index V5 说明](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T07:34+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GPT-5.5 High vs Xhigh 比较页](https://artificialanalysis.ai/models/comparisons/gpt-5-5-high-vs-gpt-5-5), [Artificial Analysis GPT-5.5 型号页](https://artificialanalysis.ai/models/gpt-5-5) | 2026-11-05T07:34+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2 旧版榜单](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T07:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 67
- metric: pass rate
- version: 1.1
- dataset: 113 tasks
- effort: xhigh
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [OpenAI GPT-5.5 API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5)

研究备注：
- 官方榜单显示 gpt-5.5[xhigh] 为 67%±6%，v1.1、113 tasks，所有配置使用 mini-swe-agent；OpenAI API 文档确认快照 gpt-5.5-2026-04-23。
- 官方方法称其为 aggregate pass rates，没有明确写为 pass@1；源 TOML 保留原始指标 pass rate，但因与仓库定义 pass@1 的口径未核实，暂不计入覆盖率。

尚未解决的问题：
- 原始资料未明确该 aggregate pass rate 是否与本地定义的 pass@1 统计口径相同。

最近核验时间：2026-11-05T07:39+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 发布页的 SWE-Bench Pro (Public) 58.6% 未标 Pro V2；本地对应原始行保留但不计作 V2。Scale V2 是 642-task 更新 split，当前可见榜单未确认 GPT-5.5 V2 结果。

尚未解决的问题：
- 无法把 OpenAI 未版本化的 SWE-Bench Pro 结果映射为 Pro V2。

最近核验时间：2026-11-05T07:34+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 78.2
- metric: success rate
- version: 2.1
- harness: Terminus-2
- source: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)
- date: 2026-05-28
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 84.1
- metric: pass@1
- version: 2.1
- variant: xhigh
- harness: Codex
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 75.8
- metric: pass@1
- version: 2.1
- variant: medium
- harness: Codex
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 73.4
- metric: pass@1
- version: 2.1
- variant: medium
- harness: Cursor CLI
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Terminal-Bench
- score: 82.7
- metric: success rate
- version: 2.0
- source: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)
- date: 2026-04-23
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 原始发布结果为 Terminal-Bench 2.0 82.7%；本地还有 Terminal-Bench 2.1 条目，均不是 v4。Vals/Artificial Analysis 当前可见页未找到明确的 GPT-5.5 v4 行。

尚未解决的问题：
- 当前公开榜单为动态/部分模型视图，不能据缺席判为无成绩。

最近核验时间：2026-11-05T07:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- Vals 当前可见 Terminal-Bench Science 榜单未显示 GPT-5.5；没有目标版本的原始结果可加入。

尚未解决的问题：
- 当前榜单为动态视图，无法据页面缺席判定无成绩。

最近核验时间：2026-11-05T07:34+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 2026-07 后续公告中的 GPT-5.5 AutomationBench 12.9% 未标 1.0.6 版本、metric 或 harness；Zapier 1.0.6 当前只显示前 10 项，剩余 119 项折叠。未录入。

尚未解决的问题：
- 后续公告分数与目标基准版本/测试条件未确认，折叠榜单无法完整检查。

最近核验时间：2026-11-05T07:34+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 v2.1 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 首发页的 78.7% 是 OSWorld-Verified；后续 GPT-5.6 公告中的 47.5% 明确为 OSWorld 2.0。均不是目标 OSWorld 2.1。

尚未解决的问题：
- v2.1 单独更新了任务快照/评估流程，不能将 Verified 或 v2.0 结果迁移。

最近核验时间：2026-11-05T07:34+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 31
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: xHigh
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测代码与方法](https://github.com/surge-ai/chartography)

研究备注：
- Surge 官方榜单列 GPT-5.5 (xHigh reasoning) 31%。官方评测代码将分数定义为 accuracy/mean (Pass@1)，仓库定义相同；GitHub 仓库注明使用 Inspect AI harness，基准包含 100 项任务。未确认单条成绩运行次数或评分器配置，因此未填写这些条件。

最近核验时间：2026-11-05T07:39+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 41.4
- metric: accuracy
- variant: no tools
- source: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)
- date: 2026-04-23
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 52.2
- metric: accuracy
- variant: with tools
- source: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)
- date: 2026-04-23
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI GPT-5.5 API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5)

研究备注：
- 本地已有两条同一版本来源记录：41.4 accuracy（no tools）及 52.2 accuracy（with tools）；均来自 OpenAI GPT-5.5 公告，保留为不同工具条件。
- API 文档确认快照 gpt-5.5-2026-04-23；公告日期已存在于源 TOML date 字段，本轮没有新增或更改这些行。

最近核验时间：2026-11-05T07:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GPT-5.5 型号页](https://artificialanalysis.ai/models/gpt-5-5)
- [Artificial Analysis Intelligence Index V5 说明](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis GPT-5.5 精确型号页指向 Index v5.0.1，当前 Intelligence Index 值显示 N/A/Unknown；未发现可收录的 V5 分数。

最近核验时间：2026-11-05T07:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GPT-5.5 High vs Xhigh 比较页](https://artificialanalysis.ai/models/comparisons/gpt-5-5-high-vs-gpt-5-5)
- [Artificial Analysis GPT-5.5 型号页](https://artificialanalysis.ai/models/gpt-5-5)

研究备注：
- AA GPT-5.5 High/Xhigh 比较页候选数值 1327/1351 未能在当前可直接读取的页面或 v2.1 公共榜单上确认；未录入。OpenAI 公告中的 GDPval wins-or-ties 不是 GDPval-AA Elo。

尚未解决的问题：
- High/Xhigh 候选值只在旧比较页缓存中出现，尚无可核验的当前原始结果。

最近核验时间：2026-11-05T07:34+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2 旧版榜单](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- 当前 Vals v2.2 页未见 GPT-5.5；旧版 Vals Index v2 有 57.41%，但版本不匹配。v2.2 页面仅显示部分模型，不能因缺席判为未找到。

尚未解决的问题：
- 没有确认的 v2.2 成绩；旧版 v2 不能迁移。

最近核验时间：2026-11-05T07:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.5 型号页",
          "url": "https://artificialanalysis.ai/models/gpt-5-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 说明",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis GPT-5.5 精确型号页指向 Index v5.0.1，当前 Intelligence Index 值显示 N/A/Unknown；未发现可收录的 V5 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 2026-07 后续公告中的 GPT-5.5 AutomationBench 12.9% 未标 1.0.6 版本、metric 或 harness；Zapier 1.0.6 当前只显示前 10 项，剩余 119 项折叠。未录入。"
      ],
      "status": "待核实",
      "unresolved": [
        "后续公告分数与目标基准版本/测试条件未确认，折叠榜单无法完整检查。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:39+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测代码与方法",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 官方榜单列 GPT-5.5 (xHigh reasoning) 31%。官方评测代码将分数定义为 accuracy/mean (Pass@1)，仓库定义相同；GitHub 仓库注明使用 Inspect AI harness，基准包含 100 项任务。未确认单条成绩运行次数或评分器配置，因此未填写这些条件。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:39+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 方法说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "OpenAI GPT-5.5 API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5"
        }
      ],
      "notes": [
        "官方榜单显示 gpt-5.5[xhigh] 为 67%±6%，v1.1、113 tasks，所有配置使用 mini-swe-agent；OpenAI API 文档确认快照 gpt-5.5-2026-04-23。",
        "官方方法称其为 aggregate pass rates，没有明确写为 pass@1；源 TOML 保留原始指标 pass rate，但因与仓库定义 pass@1 的口径未核实，暂不计入覆盖率。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始资料未明确该 aggregate pass rate 是否与本地定义的 pass@1 统计口径相同。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GPT-5.5 High vs Xhigh 比较页",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-5-high-vs-gpt-5-5"
        },
        {
          "label": "Artificial Analysis GPT-5.5 型号页",
          "url": "https://artificialanalysis.ai/models/gpt-5-5"
        }
      ],
      "notes": [
        "AA GPT-5.5 High/Xhigh 比较页候选数值 1327/1351 未能在当前可直接读取的页面或 v2.1 公共榜单上确认；未录入。OpenAI 公告中的 GDPval wins-or-ties 不是 GDPval-AA Elo。"
      ],
      "status": "待核实",
      "unresolved": [
        "High/Xhigh 候选值只在旧比较页缓存中出现，尚无可核验的当前原始结果。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        },
        {
          "label": "OpenAI GPT-5.5 API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5"
        }
      ],
      "notes": [
        "本地已有两条同一版本来源记录：41.4 accuracy（no tools）及 52.2 accuracy（with tools）；均来自 OpenAI GPT-5.5 公告，保留为不同工具条件。",
        "API 文档确认快照 gpt-5.5-2026-04-23；公告日期已存在于源 TOML date 字段，本轮没有新增或更改这些行。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 v2.1 发布记录",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 首发页的 78.7% 是 OSWorld-Verified；后续 GPT-5.6 公告中的 47.5% 明确为 OSWorld 2.0。均不是目标 OSWorld 2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "v2.1 单独更新了任务快照/评估流程，不能将 Verified 或 v2.0 结果迁移。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 发布页的 SWE-Bench Pro (Public) 58.6% 未标 Pro V2；本地对应原始行保留但不计作 V2。Scale V2 是 642-task 更新 split，当前可见榜单未确认 GPT-5.5 V2 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法把 OpenAI 未版本化的 SWE-Bench Pro 结果映射为 Pro V2。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "Vals 当前可见 Terminal-Bench Science 榜单未显示 GPT-5.5；没有目标版本的原始结果可加入。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前榜单为动态视图，无法据页面缺席判定无成绩。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 原始发布结果为 Terminal-Bench 2.0 82.7%；本地还有 Terminal-Bench 2.1 条目，均不是 v4。Vals/Artificial Analysis 当前可见页未找到明确的 GPT-5.5 v4 行。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前公开榜单为动态/部分模型视图，不能据缺席判为无成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2 旧版榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "当前 Vals v2.2 页未见 GPT-5.5；旧版 Vals Index v2 有 57.41%，但版本不匹配。v2.2 页面仅显示部分模型，不能因缺席判为未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有确认的 v2.2 成绩；旧版 v2 不能迁移。"
      ]
    }
  },
  "existing_records": 31,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:39+08:00",
  "model_id": "openai/gpt-5.5",
  "model_notes": [
    "OpenAI API 文档确认 GPT-5.5 快照为 gpt-5.5-2026-04-23；DeepSWE 榜单中的 gpt-5.5[xhigh] 可对应本地该模型。",
    "本轮将已有 SWE-Bench Pro 58.6 行来源修正为 OpenAI 原始发布页，并移除无法确认是评测日期的 2026-05-28；该行未标 Pro V2，仍不计入目标 V2。"
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
