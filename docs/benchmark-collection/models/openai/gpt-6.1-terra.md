# GPT-6.1 Terra Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-6.1-terra
- 模型名称：GPT-6.1 Terra
- 发布日期：2026-10-26
- 最近检查时间：2026-11-04T01:09+08:00
- 整体处理状态：待复核
- 新增成绩数量：10
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：10

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T01:09+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro dataset](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-04T01:09+08:00 |
| terminal-bench-v4 | 已收录 | 50.3 (metric=task resolution rate; version=4.0.0; effort=maximum reasoning effort); 55.6 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=max; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [OpenAI GPT-6.1 Terra release and score](https://openai.com/index/introducing-gpt-6-1-terra/), [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0), [Artificial Analysis independent comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra), [Artificial Analysis Terminal-Bench 4.0 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T01:09+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 57.6 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; effort=max; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [OpenAI GPT-6.1 Terra release](https://openai.com/index/introducing-gpt-6-1-terra/), [Artificial Analysis independent comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra), [Artificial Analysis Terminal-Bench-Science method](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Terminal-Bench-Science official project](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T01:09+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Artificial Analysis AutomationBench-AA comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra), [Klu comparison of AutomationBench-AA results](https://klu.ai/benchmarks/automationbench) | 2026-11-04T01:09+08:00 |
| osworld-v2.1 | 待核实 | — | [OpenAI GPT-6.1 Terra release](https://openai.com/index/introducing-gpt-6-1-terra/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2 project and scoring](https://osworld-v2.xlang.ai/) | 2026-11-04T01:09+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge AI Chartography repository](https://github.com/surge-ai/chartography) | 2026-11-04T01:09+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis HLE evaluation and methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis model page](https://artificialanalysis.ai/models/gpt-6-1-terra), [Scale AI finalized HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [OpenRouter model benchmark summary](https://openrouter.ai/openai/gpt-6.1-terra/), [Klu HLE result aggregation](https://klu.ai/benchmarks/humanitys-last-exam) | 2026-11-04T01:09+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 51 (metric=index score; version=5.0; effort=Max); 45 (metric=index score; version=5.0; effort=Xhigh); 42 (metric=index score; version=5.0; effort=High); 38 (metric=index score; version=5.0; effort=Medium); 30 (metric=index score; version=5.0; effort=Non-reasoning); 29 (metric=index score; version=5.0; effort=Low) | [Artificial Analysis GPT-6.1 Terra release results](https://artificialanalysis.ai/models/releases/gpt-6-1-terra), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T01:09+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1286 (metric=Elo rating; version=2.1; dataset=OpenAI GDPval (220 tasks); variant=Non-reasoning; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa) | 2026-11-04T01:09+08:00 |
| vals-index-v2.2 | 冲突 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [GPT-6.1 Terra Vals AI model page and Oct 26 result](https://www.vals.ai/models/openai_gpt-6.1-terra) | 2026-11-04T01:09+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Datacurve 官方榜单当前可读内容标注 2026-09-22 更新、113 个任务；该快照早于模型 2026-10-26 发布。没有从已查官方页面核实 Terra 的精确分数，旧榜单缺席不能证明发布后从未有结果。

尚未解决的问题：
- 需要在首轮模型覆盖完成后再次检查是否有发布后的官方结果。

最近核验时间：2026-11-04T01:09+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro dataset](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- Scale AI 的 Pro V2 榜单说明默认 V2 为 642 项任务，当前可读榜单标注 2026-09-22 更新，早于 Terra 发布。未从现有官方页面核实到准确版本与默认 642-task 配置下的 Terra 成绩。

尚未解决的问题：
- 榜单快照早于模型发布；需在首轮覆盖完成后复查发布后结果。

最近核验时间：2026-11-04T01:09+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 50.3
- metric: task resolution rate
- version: 4.0.0
- effort: maximum reasoning effort
- source: [https://openai.com/index/introducing-gpt-6-1-terra/](https://openai.com/index/introducing-gpt-6-1-terra/)

#### 已确认成绩 2

- name: Terminal-Bench
- score: 55.6
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: max
- variant: pass@1 averaged over three repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra)

已检查的主要资料：
- [OpenAI GPT-6.1 Terra release and score](https://openai.com/index/introducing-gpt-6-1-terra/)
- [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0)
- [Artificial Analysis independent comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra)
- [Artificial Analysis Terminal-Bench 4.0 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- OpenAI 发布文章报告 max reasoning effort 下 50.3%。Artificial Analysis 独立评测为 55.6%，其方法为 66 项、mini-swe-agent、pass@1 三次重复均值；条件不同，分别保留。

最近核验时间：2026-11-04T01:09+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 57.6
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- effort: max
- variant: pass@1 averaged over three repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra)

已检查的主要资料：
- [OpenAI GPT-6.1 Terra release](https://openai.com/index/introducing-gpt-6-1-terra/)
- [Artificial Analysis independent comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra)
- [Artificial Analysis Terminal-Bench-Science method](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Terminal-Bench-Science official project](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Artificial Analysis 独立评测报告 max 下 57.6%；使用完整 70 项、mini-swe-agent，pass@1 三次重复均值。OpenAI 发布文章确认评估过该项目，但没有给出可核实的数值。

最近核验时间：2026-11-04T01:09+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis AutomationBench-AA comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra)
- [Klu comparison of AutomationBench-AA results](https://klu.ai/benchmarks/automationbench)

研究备注：
- Zapier 官方榜单确认版本 1.0.6 与确定性成功条件，但可读页面只列前 10 条并提示另有 119 条；无法从当前页面确认隐藏列表中是否有 Terra。Artificial Analysis / Klu 提供的 AutomationBench-AA 是另一种部分分数和评测，不等同于仓库定义的 Zapier task_completed_correctly。

尚未解决的问题：
- 需取得完整官方排行榜或官方模型行后再判断；没有写入 AA 的 AutomationBench-AA 分数。

最近核验时间：2026-11-04T01:09+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-6.1 Terra release](https://openai.com/index/introducing-gpt-6-1-terra/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2 project and scoring](https://osworld-v2.xlang.ai/)

研究备注：
- OpenAI 发布文章确认 Terra 在 OSWorld 2.1 offline set、medium effort 下做过评测，但正文未给出数值，也没有说明使用 OSWorld V2.1 的 binary completion rate 还是 partial reward。

尚未解决的问题：
- 待确认分数及其与仓库 binary task completion rate 指标的对应关系；未从图表转写数值。

最近核验时间：2026-11-04T01:09+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge AI Chartography repository](https://github.com/surge-ai/chartography)

研究备注：
- Surge AI 官方 Chartography 榜单列出已发布模型与分数，包括 GPT-6 Astra、GPT-6 Sol 等，但未列 GPT-6.1 Terra。榜单未声明语义版本，本仓库定义保持 unspecified；模型有图像输入能力，因此不是不适用。

最近核验时间：2026-11-04T01:09+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis HLE evaluation and methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis model page](https://artificialanalysis.ai/models/gpt-6-1-terra)
- [Scale AI finalized HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [OpenRouter model benchmark summary](https://openrouter.ai/openai/gpt-6.1-terra/)
- [Klu HLE result aggregation](https://klu.ai/benchmarks/humanitys-last-exam)

研究备注：
- Artificial Analysis 官方方法页说明其评估原始 HLE 的 2,158 道 text-only 题，full revision 是 2,500 题，并使用 pass@1。官方可读页面未呈现 Terra 的原始 HLE 分数；当前 AA Index 使用 HLE-Diamond，不可作为 HLE 原始版成绩。OpenRouter/Klu 二手汇总可见约 46.2%–46.25% 的 Max text-only 线索，未据此写入。

尚未解决的问题：
- 需要从 AA 原始榜单或可核对的原始评测报告确认准确分值及对应 effort。

最近核验时间：2026-11-04T01:09+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 51
- metric: index score
- version: 5.0
- effort: Max
- source: [https://artificialanalysis.ai/models/releases/gpt-6-1-terra](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)

#### 已确认成绩 2

- name: Artificial Analysis Intelligence Index
- score: 45
- metric: index score
- version: 5.0
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/releases/gpt-6-1-terra](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)

#### 已确认成绩 3

- name: Artificial Analysis Intelligence Index
- score: 42
- metric: index score
- version: 5.0
- effort: High
- source: [https://artificialanalysis.ai/models/releases/gpt-6-1-terra](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)

#### 已确认成绩 4

- name: Artificial Analysis Intelligence Index
- score: 38
- metric: index score
- version: 5.0
- effort: Medium
- source: [https://artificialanalysis.ai/models/releases/gpt-6-1-terra](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)

#### 已确认成绩 5

- name: Artificial Analysis Intelligence Index
- score: 30
- metric: index score
- version: 5.0
- effort: Non-reasoning
- source: [https://artificialanalysis.ai/models/releases/gpt-6-1-terra](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)

#### 已确认成绩 6

- name: Artificial Analysis Intelligence Index
- score: 29
- metric: index score
- version: 5.0
- effort: Low
- source: [https://artificialanalysis.ai/models/releases/gpt-6-1-terra](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)

已检查的主要资料：
- [Artificial Analysis GPT-6.1 Terra release results](https://artificialanalysis.ai/models/releases/gpt-6-1-terra)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 当前发布页列出 Index V5.0 六个 Terra effort 结果；指数是 9 项评测的综合分，其中包含 HLE-Diamond，而不是 HLE 原始版。各档位逐条保留。

最近核验时间：2026-11-04T01:09+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 已确认成绩 1

- name: GDPval-AA
- score: 1286
- metric: Elo rating
- version: 2.1
- dataset: OpenAI GDPval (220 tasks)
- variant: Non-reasoning
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)

研究备注：
- Artificial Analysis v2.1 榜单的 GPT-6.1 Terra (Non-reasoning) 行为 1286 Elo，置信区间 -23/+23，发布月份显示 Oct 2026。方法页说明 220 项 OpenAI GDPval 任务由 Stirrup agentic harness 执行；没有把月份作为评测日期写入。

最近核验时间：2026-11-04T01:09+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：冲突。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [GPT-6.1 Terra Vals AI model page and Oct 26 result](https://www.vals.ai/models/openai_gpt-6.1-terra)

研究备注：
- Vals AI 当前 v2.2 榜单和 Terra 概览报告 60.54%；同一模型页的 2026-10-26 更新日志明确写 v2.2、max effort 下 60.17%。版本和档位相同，页面未解释分数变化，因此未选择其一写入。

尚未解决的问题：
- 请 Vals AI 的后续修订说明或可追溯 run 记录解释 60.17% 与 60.54% 的差异。

最近核验时间：2026-11-04T01:09+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-6.1 Terra release results",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-1-terra"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 当前发布页列出 Index V5.0 六个 Terra effort 结果；指数是 9 项评测的综合分，其中包含 HLE-Diamond，而不是 HLE 原始版。各档位逐条保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T01:09+08:00",
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
          "label": "Artificial Analysis AutomationBench-AA comparison",
          "url": "https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra"
        },
        {
          "label": "Klu comparison of AutomationBench-AA results",
          "url": "https://klu.ai/benchmarks/automationbench"
        }
      ],
      "notes": [
        "Zapier 官方榜单确认版本 1.0.6 与确定性成功条件，但可读页面只列前 10 条并提示另有 119 条；无法从当前页面确认隐藏列表中是否有 Terra。Artificial Analysis / Klu 提供的 AutomationBench-AA 是另一种部分分数和评测，不等同于仓库定义的 Zapier task_completed_correctly。"
      ],
      "status": "待核实",
      "unresolved": [
        "需取得完整官方排行榜或官方模型行后再判断；没有写入 AA 的 AutomationBench-AA 分数。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge AI Chartography repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge AI 官方 Chartography 榜单列出已发布模型与分数，包括 GPT-6 Astra、GPT-6 Sol 等，但未列 GPT-6.1 Terra。榜单未声明语义版本，本仓库定义保持 unspecified；模型有图像输入能力，因此不是不适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Datacurve 官方榜单当前可读内容标注 2026-09-22 更新、113 个任务；该快照早于模型 2026-10-26 发布。没有从已查官方页面核实 Terra 的精确分数，旧榜单缺席不能证明发布后从未有结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要在首轮模型覆盖完成后再次检查是否有发布后的官方结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        }
      ],
      "notes": [
        "Artificial Analysis v2.1 榜单的 GPT-6.1 Terra (Non-reasoning) 行为 1286 Elo，置信区间 -23/+23，发布月份显示 Oct 2026。方法页说明 220 项 OpenAI GDPval 任务由 Stirrup agentic harness 执行；没有把月份作为评测日期写入。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE evaluation and methodology",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis model page",
          "url": "https://artificialanalysis.ai/models/gpt-6-1-terra"
        },
        {
          "label": "Scale AI finalized HLE leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "OpenRouter model benchmark summary",
          "url": "https://openrouter.ai/openai/gpt-6.1-terra/"
        },
        {
          "label": "Klu HLE result aggregation",
          "url": "https://klu.ai/benchmarks/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis 官方方法页说明其评估原始 HLE 的 2,158 道 text-only 题，full revision 是 2,500 题，并使用 pass@1。官方可读页面未呈现 Terra 的原始 HLE 分数；当前 AA Index 使用 HLE-Diamond，不可作为 HLE 原始版成绩。OpenRouter/Klu 二手汇总可见约 46.2%–46.25% 的 Max text-only 线索，未据此写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要从 AA 原始榜单或可核对的原始评测报告确认准确分值及对应 effort。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6.1 Terra release",
          "url": "https://openai.com/index/introducing-gpt-6-1-terra/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2 project and scoring",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "OpenAI 发布文章确认 Terra 在 OSWorld 2.1 offline set、medium effort 下做过评测，但正文未给出数值，也没有说明使用 OSWorld V2.1 的 binary completion rate 还是 partial reward。"
      ],
      "status": "待核实",
      "unresolved": [
        "待确认分数及其与仓库 binary task completion rate 指标的对应关系；未从图表转写数值。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro dataset",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "Scale AI 的 Pro V2 榜单说明默认 V2 为 642 项任务，当前可读榜单标注 2026-09-22 更新，早于 Terra 发布。未从现有官方页面核实到准确版本与默认 642-task 配置下的 Terra 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单快照早于模型发布；需在首轮覆盖完成后复查发布后结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6.1 Terra release",
          "url": "https://openai.com/index/introducing-gpt-6-1-terra/"
        },
        {
          "label": "Artificial Analysis independent comparison",
          "url": "https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science method",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science official project",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "Artificial Analysis 独立评测报告 max 下 57.6%；使用完整 70 项、mini-swe-agent，pass@1 三次重复均值。OpenAI 发布文章确认评估过该项目，但没有给出可核实的数值。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6.1 Terra release and score",
          "url": "https://openai.com/index/introducing-gpt-6-1-terra/"
        },
        {
          "label": "Terminal-Bench 4.0 official release",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Artificial Analysis independent comparison",
          "url": "https://artificialanalysis.ai/models/releases/comparisons/gpt-6-1-terra-vs-gpt-6-astra"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 method",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "OpenAI 发布文章报告 max reasoning effort 下 50.3%。Artificial Analysis 独立评测为 55.6%，其方法为 66 项、mini-swe-agent、pass@1 三次重复均值；条件不同，分别保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T01:09+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "GPT-6.1 Terra Vals AI model page and Oct 26 result",
          "url": "https://www.vals.ai/models/openai_gpt-6.1-terra"
        }
      ],
      "notes": [
        "Vals AI 当前 v2.2 榜单和 Terra 概览报告 60.54%；同一模型页的 2026-10-26 更新日志明确写 v2.2、max effort 下 60.17%。版本和档位相同，页面未解释分数变化，因此未选择其一写入。"
      ],
      "status": "冲突",
      "unresolved": [
        "请 Vals AI 的后续修订说明或可追溯 run 记录解释 60.17% 与 60.54% 的差异。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T01:09+08:00",
  "model_id": "openai/gpt-6.1-terra",
  "new_records": 10,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
