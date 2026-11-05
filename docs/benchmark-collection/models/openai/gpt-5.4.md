# GPT-5.4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.4
- 模型名称：GPT-5.4
- 发布日期：2026-03-05
- 最近检查时间：2026-11-05T12:12+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：2
- 收集前已有成绩数量：2
- 当前已收录的对应成绩数量：6

## 模型身份与范围说明

- DeepSWE live JSON 将模型记作 gpt-5-4；OpenAI GPT-5.4 API 快照和 2026-03-05 发布资料确认该别名对应 GPT-5.4。
- 原有 SWE-Bench Pro 59.1 行没有版本且指标写为 resolve rate；OpenAI 原始发布页另报 SWE-Bench Pro (Public) 57.7%，当前 V2 榜单未显示可核实的精确 GPT-5.4 V2 行，故不合并或覆盖。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 51.76991150442478 (metric=pass@1; version=1.1; dataset=113 tasks; effort=xhigh; variant=4 runs; harness=mini-swe-agent) | [DeepSWE v1.1 live leaderboard JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4) | 2026-11-05T12:12+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-Bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4) | 2026-11-05T12:12+08:00 |
| terminal-bench-v4 | 待核实 | 69.8 (metric=pass@1; version=2.1; variant=medium; harness=Codex); 64.7 (metric=pass@1; version=2.1; variant=medium; harness=Cursor CLI); 75.1 (metric=success rate; version=2.0) | [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/), [Artificial Analysis GPT-5.4 profile](https://artificialanalysis.ai/models/gpt-5-4), [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/) | 2026-11-05T12:12+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench-Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4) | 2026-11-05T12:12+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/) | 2026-11-05T12:12+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2.1 evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld V2 official project](https://github.com/xlang-ai/OSWorld-V2), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4), [OpenAI GPT-5.5 comparison table](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T12:12+08:00 |
| chartography | 已收录 | 29.6 (metric=accuracy (mean; Pass@1); version=unspecified; dataset=surgeai/chartography; effort=xHigh; variant=10 runs; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official methodology and harness](https://github.com/surge-ai/chartography), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4) | 2026-11-05T12:12+08:00 |
| humanitys-last-exam | 已收录 | 39.8 (metric=accuracy; effort=xhigh; variant=no tools); 52.1 (metric=accuracy; effort=xhigh; variant=with tools); 44 (metric=accuracy; dataset=Original HLE set (2,500 questions); effort=Xhigh) | [OpenAI GPT-5.4 release and HLE table](https://openai.com/index/introducing-gpt-5-4/), [Artificial Analysis GPT-5.4 vs GPT-5 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5), [Artificial Analysis HLE evaluation definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T12:12+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis GPT-5.4 profile](https://artificialanalysis.ai/models/gpt-5-4), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4) | 2026-11-05T12:12+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1247 (metric=Elo rating; version=2.1; dataset=220 tasks; effort=Xhigh; harness=Stirrup) | [Artificial Analysis GPT-5.4 vs GPT-5 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5), [GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4) | 2026-11-05T12:12+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals GPT-5.4 model profile](https://www.vals.ai/models/openai_gpt-5.4-2026-03-05), [Vals historical Index V2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T12:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 51.76991150442478
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: xhigh
- variant: 4 runs
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [DeepSWE v1.1 live leaderboard JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)

研究备注：
- 榜单精确行是 gpt-5-4 / mini-swe-agent / xhigh；pass_at_1 原值 0.5176991150442478 按定义的 percent 单位换算为 51.76991150442478。113 项任务、4 次完整运行；来源未公布该行评测日期。

最近核验时间：2026-11-05T12:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-Bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)

研究备注：
- 本地 59.1 public 行缺 version 且 metric 为 resolve rate；OpenAI 官方 GPT-5.4 发布页报 57.7% SWE-Bench Pro (Public)，未说明是 V2。当前 V2 榜单未能确认 GPT-5.4 的精确 V2 行。

尚未解决的问题：
- 需确认本地 public 记录是否属于 642-task V2，且与 57.7% 是否为相同评测条件；暂不把两者当成同一成绩。

最近核验时间：2026-11-05T12:12+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 69.8
- metric: pass@1
- version: 2.1
- variant: medium
- harness: Codex
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 64.7
- metric: pass@1
- version: 2.1
- variant: medium
- harness: Cursor CLI
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 75.1
- metric: success rate
- version: 2.0
- source: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)
- date: 2026-04-23
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/)
- [Artificial Analysis GPT-5.4 profile](https://artificialanalysis.ai/models/gpt-5-4)
- [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/)

研究备注：
- 本地 69.8 是 Terminal-Bench 2.1 的 Codex pass@1；OpenAI 官方 GPT-5.5 对照表列 GPT-5.4 的 75.1% 为 Terminal-Bench 2.0。均不能映射到目标 4.0；本次官方 4.0 动态榜单未提供可核实的精确分数。

尚未解决的问题：
- 需从完整官方 4.0 结果确认 GPT-5.4 的 exact score 与配置。

最近核验时间：2026-11-05T12:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench-Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)

研究备注：
- 已核对 0.1 基准公告和 Harbor 动态榜单；当前公开视图未能核实 GPT-5.4 的精确分数。

尚未解决的问题：
- 需从可读取的完整 0.1 榜单或原始运行记录确认。

最近核验时间：2026-11-05T12:12+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [OpenAI GPT-5.4 release](https://openai.com/index/introducing-gpt-5-4/)

研究备注：
- Zapier 页面展示部分榜单行，剩余行折叠；本次未能确认 GPT-5.4 的精确 held-out 成绩。

尚未解决的问题：
- 需核对官方榜单完整折叠结果及其私有 held-out 数据集配置。

最近核验时间：2026-11-05T12:12+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2.1 evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld V2 official project](https://github.com/xlang-ai/OSWorld-V2)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)
- [OpenAI GPT-5.5 comparison table](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- 官方提供了 GPT-5.4 的 v2.1 runner 示例，但本地 75.0% 是 OSWorld-Verified，测试定义不同；未核实到 GPT-5.4 的 OSWorld V2.1 分数。

尚未解决的问题：
- 需确认 v2.1 精确运行结果；不将 OSWorld-Verified 作为 V2.1 成绩。

最近核验时间：2026-11-05T12:12+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 29.6
- metric: accuracy (mean; Pass@1)
- version: unspecified
- dataset: surgeai/chartography
- effort: xHigh
- variant: 10 runs; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official methodology and harness](https://github.com/surge-ai/chartography)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)

研究备注：
- 榜单列出 GPT 5.4 (xHigh reasoning) 29.6%。官方方法仓库指定 accuracy/mean（即 Pass@1）、完整榜单配置 10 次运行、Gemini 3.5 Flash judge、Inspect AI harness；未公布该行评测日期。

最近核验时间：2026-11-05T12:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 39.8
- metric: accuracy
- effort: xhigh
- variant: no tools
- source: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 52.1
- metric: accuracy
- effort: xhigh
- variant: with tools
- source: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 3

- name: Humanity's Last Exam
- score: 44
- metric: accuracy
- dataset: Original HLE set (2,500 questions)
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5](https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [OpenAI GPT-5.4 release and HLE table](https://openai.com/index/introducing-gpt-5-4/)
- [Artificial Analysis GPT-5.4 vs GPT-5 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5)
- [Artificial Analysis HLE evaluation definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 已有 OpenAI 原始成绩：39.8% no tools、52.1% with tools；GPT-5.4 发布页直接列出，设置为 xhigh。另新增 AA 独立评测 44% accuracy，比较页标明 GPT-5.4 (Xhigh)；没有推断未公布的工具条件、harness 或日期。

最近核验时间：2026-11-05T12:12+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GPT-5.4 profile](https://artificialanalysis.ai/models/gpt-5-4)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)

研究备注：
- 精确 AA profile 当前未提供可映射到 V5.0.1 的指数分数；可见旧版指数或估值不作为 V5 成绩。

尚未解决的问题：
- 需确认 GPT-5.4 是否已在 V5.0.1 完成评测；V5.0.1 与历史 v4 指数组成不同。

最近核验时间：2026-11-05T12:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1247
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- effort: Xhigh
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5](https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis GPT-5.4 vs GPT-5 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5)
- [GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [GPT-5.4 API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4)

研究备注：
- AA 比较页对 GPT-5.4 (Xhigh) 明列 1247 Elo；v2.1 定义页说明 220 个任务、Stirrup agent loop 和 pairwise Elo。OpenAI 的 GDPval 83.0% 是不同测试，不映射到此项。

最近核验时间：2026-11-05T12:12+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals GPT-5.4 model profile](https://www.vals.ai/models/openai_gpt-5.4-2026-03-05)
- [Vals historical Index V2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- GPT-5.4 profile 列 65.91%，但未标明 V2.2；当前 V2.2 榜单只展示各实验室最佳模型，未展示 GPT-5.4。旧版 V1/V2 不作版本替代。

尚未解决的问题：
- 需从 Vals 确认 65.91% 是否属于 v2.2。

最近核验时间：2026-11-05T12:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.4 profile",
          "url": "https://artificialanalysis.ai/models/gpt-5-4"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        }
      ],
      "notes": [
        "精确 AA profile 当前未提供可映射到 V5.0.1 的指数分数；可见旧版指数或估值不作为 V5 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 GPT-5.4 是否已在 V5.0.1 完成评测；V5.0.1 与历史 v4 指数组成不同。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "OpenAI GPT-5.4 release",
          "url": "https://openai.com/index/introducing-gpt-5-4/"
        }
      ],
      "notes": [
        "Zapier 页面展示部分榜单行，剩余行折叠；本次未能确认 GPT-5.4 的精确 held-out 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核对官方榜单完整折叠结果及其私有 held-out 数据集配置。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official methodology and harness",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        }
      ],
      "notes": [
        "榜单列出 GPT 5.4 (xHigh reasoning) 29.6%。官方方法仓库指定 accuracy/mean（即 Pass@1）、完整榜单配置 10 次运行、Gemini 3.5 Flash judge、Inspect AI harness；未公布该行评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 live leaderboard JSON",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "OpenAI GPT-5.4 release",
          "url": "https://openai.com/index/introducing-gpt-5-4/"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        }
      ],
      "notes": [
        "榜单精确行是 gpt-5-4 / mini-swe-agent / xhigh；pass_at_1 原值 0.5176991150442478 按定义的 percent 单位换算为 51.76991150442478。113 项任务、4 次完整运行；来源未公布该行评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.4 vs GPT-5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5"
        },
        {
          "label": "GDPval-AA v2.1 evaluation and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        }
      ],
      "notes": [
        "AA 比较页对 GPT-5.4 (Xhigh) 明列 1247 Elo；v2.1 定义页说明 220 个任务、Stirrup agent loop 和 pairwise Elo。OpenAI 的 GDPval 83.0% 是不同测试，不映射到此项。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-5.4 release and HLE table",
          "url": "https://openai.com/index/introducing-gpt-5-4/"
        },
        {
          "label": "Artificial Analysis GPT-5.4 vs GPT-5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-4-vs-gpt-5"
        },
        {
          "label": "Artificial Analysis HLE evaluation definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "已有 OpenAI 原始成绩：39.8% no tools、52.1% with tools；GPT-5.4 发布页直接列出，设置为 xhigh。另新增 AA 独立评测 44% accuracy，比较页标明 GPT-5.4 (Xhigh)；没有推断未公布的工具条件、harness 或日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 evaluation guide",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld V2 official project",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        },
        {
          "label": "OpenAI GPT-5.5 comparison table",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "官方提供了 GPT-5.4 的 v2.1 runner 示例，但本地 75.0% 是 OSWorld-Verified，测试定义不同；未核实到 GPT-5.4 的 OSWorld V2.1 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 v2.1 精确运行结果；不将 OSWorld-Verified 作为 V2.1 成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "SWE-Bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "OpenAI GPT-5.4 release",
          "url": "https://openai.com/index/introducing-gpt-5-4/"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        }
      ],
      "notes": [
        "本地 59.1 public 行缺 version 且 metric 为 resolve rate；OpenAI 官方 GPT-5.4 发布页报 57.7% SWE-Bench Pro (Public)，未说明是 V2。当前 V2 榜单未能确认 GPT-5.4 的精确 V2 行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认本地 public 记录是否属于 642-task V2，且与 57.7% 是否为相同评测条件；暂不把两者当成同一成绩。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench-Science Harbor leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "label": "GPT-5.4 API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4"
        }
      ],
      "notes": [
        "已核对 0.1 基准公告和 Harbor 动态榜单；当前公开视图未能核实 GPT-5.4 的精确分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从可读取的完整 0.1 榜单或原始运行记录确认。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Artificial Analysis GPT-5.4 profile",
          "url": "https://artificialanalysis.ai/models/gpt-5-4"
        },
        {
          "label": "OpenAI GPT-5.4 release",
          "url": "https://openai.com/index/introducing-gpt-5-4/"
        }
      ],
      "notes": [
        "本地 69.8 是 Terminal-Bench 2.1 的 Codex pass@1；OpenAI 官方 GPT-5.5 对照表列 GPT-5.4 的 75.1% 为 Terminal-Bench 2.0。均不能映射到目标 4.0；本次官方 4.0 动态榜单未提供可核实的精确分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从完整官方 4.0 结果确认 GPT-5.4 的 exact score 与配置。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals GPT-5.4 model profile",
          "url": "https://www.vals.ai/models/openai_gpt-5.4-2026-03-05"
        },
        {
          "label": "Vals historical Index V2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "GPT-5.4 profile 列 65.91%，但未标明 V2.2；当前 V2.2 榜单只展示各实验室最佳模型，未展示 GPT-5.4。旧版 V1/V2 不作版本替代。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从 Vals 确认 65.91% 是否属于 v2.2。"
      ]
    }
  },
  "existing_records": 2,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T12:12+08:00",
  "model_id": "openai/gpt-5.4",
  "model_notes": [
    "DeepSWE live JSON 将模型记作 gpt-5-4；OpenAI GPT-5.4 API 快照和 2026-03-05 发布资料确认该别名对应 GPT-5.4。",
    "原有 SWE-Bench Pro 59.1 行没有版本且指标写为 resolve rate；OpenAI 原始发布页另报 SWE-Bench Pro (Public) 57.7%，当前 V2 榜单未显示可核实的精确 GPT-5.4 V2 行，故不合并或覆盖。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
