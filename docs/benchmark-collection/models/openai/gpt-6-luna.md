# GPT-6 Luna Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-6-luna
- 模型名称：GPT-6 Luna
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T08:12+08:00
- 整体处理状态：待复核
- 新增成绩数量：15
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：6

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 66.6 (metric=score; version=1.1; dataset=113 tasks; effort=max) | [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/), [DeepSWE v1.1 methodology and task set](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T08:12+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/) | 2026-11-04T08:12+08:00 |
| terminal-bench-v4 | 冲突 | 13.64 ± 1.51 (metric=accuracy; version=4.0; dataset=66 tasks; effort=max; variant=avg@3 (three full runs; each run scored pass@1); harness=Mini-SWE-agent) | [Vals GPT-6 Luna profile](https://www.vals.ai/models/openai_gpt-6-luna), [Vals Terminal-Bench 4.0 leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-4), [Terminal-Bench 4.0 official specification](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T08:12+08:00 |
| terminal-bench-science-v0.1 | 冲突 | 4.29 ± 2.44 (metric=accuracy; version=0.1.0; dataset=70 tasks; effort=max; variant=pass@1; single run; harness=Mini-SWE-agent) | [Vals GPT-6 Luna profile](https://www.vals.ai/models/openai_gpt-6-luna), [Vals Terminal-Bench-Science leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-science), [Terminal-Bench-Science 0.1 official specification](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T08:12+08:00 |
| automationbench-v1.0.6 | 已收录 | 1.2 (metric=task_completed_correctly; version=1.0.6; effort=Low; variant=Zapier official leaderboard pass rate); 9.4 (metric=task_completed_correctly; version=1.0.6; effort=Medium; variant=Zapier official leaderboard pass rate); 14.5 (metric=task_completed_correctly; version=1.0.6; effort=High; variant=Zapier official leaderboard pass rate); 20.7 (metric=task_completed_correctly; version=1.0.6; effort=Max; variant=best observed published pass rate) | [Zapier AutomationBench model comparison and results data](https://zapier.com/benchmarks/gemini-carbon-4-report), [Zapier AutomationBench 1.0.6 leaderboard and method](https://zapier.com/benchmarks) | 2026-11-04T08:12+08:00 |
| osworld-v2.1 | 未找到 | — | [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/), [OSWorld V2 official project and scoring](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T08:12+08:00 |
| chartography | 待核实 | 29.1 (metric=accuracy/mean; dataset=full 100-task set; effort=Max; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official protocol and leaderboard configuration](https://github.com/surge-ai/chartography/blob/main/README.md) | 2026-11-04T08:12+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/) | 2026-11-04T08:12+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 28 (metric=index score; version=5.0.1; effort=Max); 23 (metric=index score; version=5.0.1; effort=Xhigh); 21 (metric=index score; version=5.0.1; effort=High); 18 (metric=index score; version=5.0.1; effort=Medium); 10 (metric=index score; version=5.0.1; effort=Low); 9 (metric=index score; version=5.0.1; variant=Non-reasoning) | [Artificial Analysis GPT-6 Luna release variants](https://artificialanalysis.ai/models/releases/gpt-6-luna), [GPT-6 Luna Max](https://artificialanalysis.ai/models/gpt-6-luna/), [GPT-6 Luna Xhigh](https://artificialanalysis.ai/models/gpt-6-luna-xhigh), [GPT-6 Luna High](https://artificialanalysis.ai/models/gpt-6-luna-high), [GPT-6 Luna Medium](https://artificialanalysis.ai/models/gpt-6-luna-medium), [GPT-6 Luna Low](https://artificialanalysis.ai/models/gpt-6-luna-low), [GPT-6 Luna Non-reasoning](https://artificialanalysis.ai/models/gpt-6-luna-non-reasoning), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T08:12+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1052 (-22/+22) (metric=Elo rating; version=2.1; dataset=220 tasks; variant=Non-reasoning; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 leaderboard and method](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GPT-6 Luna vs GPT-6 Astra](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-astra) | 2026-11-04T08:12+08:00 |
| vals-index-v2.2 | 已收录 | 52.32 ± 1.12 (metric=performance score; version=2.2; effort=max; variant=default provider: OpenAI; fallback rate: 0%) | [Vals GPT-6 Luna profile and score uncertainty](https://www.vals.ai/models/openai_gpt-6-luna), [Vals Index v2.2 leaderboard and method](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T08:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 66.6
- metric: score
- version: 1.1
- dataset: 113 tasks
- effort: max
- source: [https://openai.com/index/introducing-gpt-6-sol-and-luna/](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [DeepSWE v1.1 methodology and task set](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 现有记录的模型、DeepSWE v1.1、66.6% 和 max effort 均由 OpenAI 发布页确认；方法页确认 v1.1 有 113 项任务。已把 effort 改为官方原名 max，移除与模型发布日期相同但未证实为评测日的 date。
- 源文只称 score，未说明此条是否按本地定义的 pass@1 计算；原始行保留且不计入精确定义映射。

尚未解决的问题：
- 需核实 OpenAI 的 score 指标是否等同本地定义的 pass@1。

最近核验时间：2026-11-04T08:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

研究备注：
- 检查了 Scale 的公开 V2 榜单和 OpenAI 发布页；未找到 GPT-6 Luna 的准确 V2 成绩。未把其他 SWE-bench 版本的分数移用。

最近核验时间：2026-11-04T08:12+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 13.64 ± 1.51
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- effort: max
- variant: avg@3 (three full runs; each run scored pass@1)
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals GPT-6 Luna profile](https://www.vals.ai/models/openai_gpt-6-luna)
- [Vals Terminal-Bench 4.0 leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Terminal-Bench 4.0 official specification](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- TOML 保存 Vals 当前榜单行：13.64% ±1.51，版本 4.0，66 项，max effort，Mini-SWE-agent，avg@3（三次全量运行，每次 pass@1）。源标签为 accuracy，因此原样记录；本地定义映射待核实。
- Vals 在 2026-09-22 的 Luna 更新文字另报 9.60%；它没有说明与当前 13.64% 的条件差异。

尚未解决的问题：
- 同一 Vals profile 的 9.60% 与当前排行榜 13.64% 不一致；旧结果缺少可比较的 harness/运行条件，尚不能判定是否为不同配置或结果修订。

最近核验时间：2026-11-04T08:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 4.29 ± 2.44
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- effort: max
- variant: pass@1; single run
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals GPT-6 Luna profile](https://www.vals.ai/models/openai_gpt-6-luna)
- [Vals Terminal-Bench-Science leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Terminal-Bench-Science 0.1 official specification](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- TOML 保存 Vals 当前榜单行：4.29% ±2.44，upstream v0.1.0、70 项、max effort、Mini-SWE-agent、单次 pass@1。源指标 accuracy 原样保留。
- Vals 在 2026-09-22 的 Luna 更新文字另报 10.00%；该旧结果未给出可解释差异的测试配置。

尚未解决的问题：
- 同一 Vals profile 的 10.00% 与当前排行榜 4.29% 不一致；旧结果的 harness/运行条件未说明，尚不能判定是否为不同配置或结果修订。

最近核验时间：2026-11-04T08:12+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 1.2
- metric: task_completed_correctly
- version: 1.0.6
- effort: Low
- variant: Zapier official leaderboard pass rate
- source: [https://zapier.com/benchmarks/gemini-carbon-4-report](https://zapier.com/benchmarks/gemini-carbon-4-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 9.4
- metric: task_completed_correctly
- version: 1.0.6
- effort: Medium
- variant: Zapier official leaderboard pass rate
- source: [https://zapier.com/benchmarks/gemini-carbon-4-report](https://zapier.com/benchmarks/gemini-carbon-4-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 14.5
- metric: task_completed_correctly
- version: 1.0.6
- effort: High
- variant: Zapier official leaderboard pass rate
- source: [https://zapier.com/benchmarks/gemini-carbon-4-report](https://zapier.com/benchmarks/gemini-carbon-4-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: AutomationBench
- score: 20.7
- metric: task_completed_correctly
- version: 1.0.6
- effort: Max
- variant: best observed published pass rate
- source: [https://zapier.com/benchmarks/gemini-carbon-4-report](https://zapier.com/benchmarks/gemini-carbon-4-report)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench model comparison and results data](https://zapier.com/benchmarks/gemini-carbon-4-report)
- [Zapier AutomationBench 1.0.6 leaderboard and method](https://zapier.com/benchmarks)

研究备注：
- 记录官方公开的 Low 1.2%、Medium 9.4%、High 14.5% 和 Max 20.7% 四个 effort。指标为 task_completed_correctly/pass rate；对应 Zapier held-out leaderboard。来源没有给 GPT-6 Luna 的实际评测日期，date 留空。

最近核验时间：2026-11-04T08:12+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [OSWorld V2 official project and scoring](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OpenAI 只发布 OSWorld 2.0 offline 的 partial-reward 结果；该版本、数据子集和指标均不符合本地 OSWorld v2.1 binary task-completion 定义。官方 V2 项目资料中未找到 Luna 的 v2.1 成绩。

最近核验时间：2026-11-04T08:12+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 29.1
- metric: accuracy/mean
- dataset: full 100-task set
- effort: Max
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official protocol and leaderboard configuration](https://github.com/surge-ai/chartography/blob/main/README.md)

研究备注：
- Surge 榜单列出 GPT-6 Luna (Max reasoning) 29.1%。官方 README 指明排行榜用完整 100 项、每项 10 次运行和 Gemini 3.5 Flash judge，评分字段为 accuracy/mean；TOML 保留这些原始条件。来源未提供评测日期或语义版本。

尚未解决的问题：
- 本地定义采用 accuracy (mean; Pass@1)，而排行榜值为 10 次运行的 accuracy/mean；需确认是否在本地定义下计为同一指标/版本。

最近核验时间：2026-11-04T08:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [OpenAI GPT-6 Sol and Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

研究备注：
- 当前 Artificial Analysis Intelligence Index 报告的是 HLE-Diamond，不等同本地指定的原始 HLE；没有据此写入分数。当前 HLE 页面也未能直接复核 GPT-6 Luna 的原始 HLE 成绩。
- 研究中发现一个历史 AA 比较页面曾显示 Luna Max 39%，但当前页面无法直接复核该行，因此没有写入 TOML。

尚未解决的问题：
- 需找到能直接核验 GPT-6 Luna 原始 HLE 分数、子集及条件的来源；历史 39% 目前仅有过期页面线索。

最近核验时间：2026-11-04T08:12+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 28
- metric: index score
- version: 5.0.1
- effort: Max
- source: [https://artificialanalysis.ai/models/gpt-6-luna/](https://artificialanalysis.ai/models/gpt-6-luna/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 23
- metric: index score
- version: 5.0.1
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/gpt-6-luna-xhigh](https://artificialanalysis.ai/models/gpt-6-luna-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 21
- metric: index score
- version: 5.0.1
- effort: High
- source: [https://artificialanalysis.ai/models/gpt-6-luna-high](https://artificialanalysis.ai/models/gpt-6-luna-high)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Artificial Analysis Intelligence Index
- score: 18
- metric: index score
- version: 5.0.1
- effort: Medium
- source: [https://artificialanalysis.ai/models/gpt-6-luna-medium](https://artificialanalysis.ai/models/gpt-6-luna-medium)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Artificial Analysis Intelligence Index
- score: 10
- metric: index score
- version: 5.0.1
- effort: Low
- source: [https://artificialanalysis.ai/models/gpt-6-luna-low](https://artificialanalysis.ai/models/gpt-6-luna-low)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 6

- name: Artificial Analysis Intelligence Index
- score: 9
- metric: index score
- version: 5.0.1
- variant: Non-reasoning
- source: [https://artificialanalysis.ai/models/gpt-6-luna-non-reasoning](https://artificialanalysis.ai/models/gpt-6-luna-non-reasoning)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GPT-6 Luna release variants](https://artificialanalysis.ai/models/releases/gpt-6-luna)
- [GPT-6 Luna Max](https://artificialanalysis.ai/models/gpt-6-luna/)
- [GPT-6 Luna Xhigh](https://artificialanalysis.ai/models/gpt-6-luna-xhigh)
- [GPT-6 Luna High](https://artificialanalysis.ai/models/gpt-6-luna-high)
- [GPT-6 Luna Medium](https://artificialanalysis.ai/models/gpt-6-luna-medium)
- [GPT-6 Luna Low](https://artificialanalysis.ai/models/gpt-6-luna-low)
- [GPT-6 Luna Non-reasoning](https://artificialanalysis.ai/models/gpt-6-luna-non-reasoning)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前页面可核实六个配置：Max 28、Xhigh 23、High 21、Medium 18、Low 10、Non-reasoning 9。源页面标明 Index v5.0.1；每条 TOML 记录了原始版本，没有把它改写为本地定义的 5.0。评测日未公布。

尚未解决的问题：
- 本地定义版本为 5.0，AA 当前发布结果为 5.0.1；精确版本映射待复核。

最近核验时间：2026-11-04T08:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1052 (-22/+22)
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- variant: Non-reasoning
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and method](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GPT-6 Luna vs GPT-6 Astra](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-astra)

研究备注：
- 当前官方榜单直接列出 GPT-6 Luna (Non-reasoning) 1052 Elo（−22/+22），220 项，Stirrup harness；该行已写入 TOML。未填写评测日期。
- 历史 AA 比较页曾出现 Luna Max 1445 Elo 的搜索快照，但当前官方榜单/比较正文无法直接复核该分数，故未写入。

尚未解决的问题：
- 需进一步核实历史 Max 1445 Elo 是否为现行 v2.1 结果；当前可直接核验的 1052 是 Non-reasoning 配置。

最近核验时间：2026-11-04T08:12+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 52.32 ± 1.12
- metric: performance score
- version: 2.2
- effort: max
- variant: default provider: OpenAI; fallback rate: 0%
- source: [https://www.vals.ai/models/openai_gpt-6-luna](https://www.vals.ai/models/openai_gpt-6-luna)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals GPT-6 Luna profile and score uncertainty](https://www.vals.ai/models/openai_gpt-6-luna)
- [Vals Index v2.2 leaderboard and method](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 官方模型页与 v2.2 榜单列出 52.32% ±1.12；模型页标示 max effort、OpenAI provider 和 0% fallback。来源未给出实际评测日期，date 留空。

最近核验时间：2026-11-04T08:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-6 Luna release variants",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-luna"
        },
        {
          "label": "GPT-6 Luna Max",
          "url": "https://artificialanalysis.ai/models/gpt-6-luna/"
        },
        {
          "label": "GPT-6 Luna Xhigh",
          "url": "https://artificialanalysis.ai/models/gpt-6-luna-xhigh"
        },
        {
          "label": "GPT-6 Luna High",
          "url": "https://artificialanalysis.ai/models/gpt-6-luna-high"
        },
        {
          "label": "GPT-6 Luna Medium",
          "url": "https://artificialanalysis.ai/models/gpt-6-luna-medium"
        },
        {
          "label": "GPT-6 Luna Low",
          "url": "https://artificialanalysis.ai/models/gpt-6-luna-low"
        },
        {
          "label": "GPT-6 Luna Non-reasoning",
          "url": "https://artificialanalysis.ai/models/gpt-6-luna-non-reasoning"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前页面可核实六个配置：Max 28、Xhigh 23、High 21、Medium 18、Low 10、Non-reasoning 9。源页面标明 Index v5.0.1；每条 TOML 记录了原始版本，没有把它改写为本地定义的 5.0。评测日未公布。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义版本为 5.0，AA 当前发布结果为 5.0.1；精确版本映射待复核。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench model comparison and results data",
          "url": "https://zapier.com/benchmarks/gemini-carbon-4-report"
        },
        {
          "label": "Zapier AutomationBench 1.0.6 leaderboard and method",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "记录官方公开的 Low 1.2%、Medium 9.4%、High 14.5% 和 Max 20.7% 四个 effort。指标为 task_completed_correctly/pass rate；对应 Zapier held-out leaderboard。来源没有给 GPT-6 Luna 的实际评测日期，date 留空。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official protocol and leaderboard configuration",
          "url": "https://github.com/surge-ai/chartography/blob/main/README.md"
        }
      ],
      "notes": [
        "Surge 榜单列出 GPT-6 Luna (Max reasoning) 29.1%。官方 README 指明排行榜用完整 100 项、每项 10 次运行和 Gemini 3.5 Flash judge，评分字段为 accuracy/mean；TOML 保留这些原始条件。来源未提供评测日期或语义版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义采用 accuracy (mean; Pass@1)，而排行榜值为 10 次运行的 accuracy/mean；需确认是否在本地定义下计为同一指标/版本。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Sol and Luna release",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        },
        {
          "label": "DeepSWE v1.1 methodology and task set",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "现有记录的模型、DeepSWE v1.1、66.6% 和 max effort 均由 OpenAI 发布页确认；方法页确认 v1.1 有 113 项任务。已把 effort 改为官方原名 max，移除与模型发布日期相同但未证实为评测日的 date。",
        "源文只称 score，未说明此条是否按本地定义的 pass@1 计算；原始行保留且不计入精确定义映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实 OpenAI 的 score 指标是否等同本地定义的 pass@1。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and method",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GPT-6 Luna vs GPT-6 Astra",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-astra"
        }
      ],
      "notes": [
        "当前官方榜单直接列出 GPT-6 Luna (Non-reasoning) 1052 Elo（−22/+22），220 项，Stirrup harness；该行已写入 TOML。未填写评测日期。",
        "历史 AA 比较页曾出现 Luna Max 1445 Elo 的搜索快照，但当前官方榜单/比较正文无法直接复核该分数，故未写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需进一步核实历史 Max 1445 Elo 是否为现行 v2.1 结果；当前可直接核验的 1052 是 Non-reasoning 配置。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "OpenAI GPT-6 Sol and Luna release",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        }
      ],
      "notes": [
        "当前 Artificial Analysis Intelligence Index 报告的是 HLE-Diamond，不等同本地指定的原始 HLE；没有据此写入分数。当前 HLE 页面也未能直接复核 GPT-6 Luna 的原始 HLE 成绩。",
        "研究中发现一个历史 AA 比较页面曾显示 Luna Max 39%，但当前页面无法直接复核该行，因此没有写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "需找到能直接核验 GPT-6 Luna 原始 HLE 分数、子集及条件的来源；历史 39% 目前仅有过期页面线索。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Sol and Luna release",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        },
        {
          "label": "OSWorld V2 official project and scoring",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OpenAI 只发布 OSWorld 2.0 offline 的 partial-reward 结果；该版本、数据子集和指标均不符合本地 OSWorld v2.1 binary task-completion 定义。官方 V2 项目资料中未找到 Luna 的 v2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "OpenAI GPT-6 Sol and Luna release",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        }
      ],
      "notes": [
        "检查了 Scale 的公开 V2 榜单和 OpenAI 发布页；未找到 GPT-6 Luna 的准确 V2 成绩。未把其他 SWE-bench 版本的分数移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Vals GPT-6 Luna profile",
          "url": "https://www.vals.ai/models/openai_gpt-6-luna"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science 0.1 official specification",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "TOML 保存 Vals 当前榜单行：4.29% ±2.44，upstream v0.1.0、70 项、max effort、Mini-SWE-agent、单次 pass@1。源指标 accuracy 原样保留。",
        "Vals 在 2026-09-22 的 Luna 更新文字另报 10.00%；该旧结果未给出可解释差异的测试配置。"
      ],
      "status": "冲突",
      "unresolved": [
        "同一 Vals profile 的 10.00% 与当前排行榜 4.29% 不一致；旧结果的 harness/运行条件未说明，尚不能判定是否为不同配置或结果修订。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Vals GPT-6 Luna profile",
          "url": "https://www.vals.ai/models/openai_gpt-6-luna"
        },
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Terminal-Bench 4.0 official specification",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "TOML 保存 Vals 当前榜单行：13.64% ±1.51，版本 4.0，66 项，max effort，Mini-SWE-agent，avg@3（三次全量运行，每次 pass@1）。源标签为 accuracy，因此原样记录；本地定义映射待核实。",
        "Vals 在 2026-09-22 的 Luna 更新文字另报 9.60%；它没有说明与当前 13.64% 的条件差异。"
      ],
      "status": "冲突",
      "unresolved": [
        "同一 Vals profile 的 9.60% 与当前排行榜 13.64% 不一致；旧结果缺少可比较的 harness/运行条件，尚不能判定是否为不同配置或结果修订。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T08:12+08:00",
      "checked_sources": [
        {
          "label": "Vals GPT-6 Luna profile and score uncertainty",
          "url": "https://www.vals.ai/models/openai_gpt-6-luna"
        },
        {
          "label": "Vals Index v2.2 leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "官方模型页与 v2.2 榜单列出 52.32% ±1.12；模型页标示 max effort、OpenAI provider 和 0% fallback。来源未给出实际评测日期，date 留空。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T08:12+08:00",
  "model_id": "openai/gpt-6-luna",
  "new_records": 15,
  "overall_status": "待复核"
}

-->
