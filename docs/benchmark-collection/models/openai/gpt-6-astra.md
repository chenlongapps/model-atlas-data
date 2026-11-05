# GPT-6 Astra Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-6-astra
- 模型名称：GPT-6 Astra
- 发布日期：2026-09-04
- 最近检查时间：2026-11-04T12:54+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 收集前已有成绩数量：51
- 当前已收录的对应成绩数量：38

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 74.1 (metric=pass@1; version=1.1); 73.23008849557522 (metric=pass@1; version=1.1; dataset=113 tasks; effort=max; variant=4 whole-benchmark passes; 452 scored attempts; errors excluded; harness=mini-swe-agent); 74.11504424778761 (metric=pass@1; version=1.1; dataset=113 tasks; effort=xhigh; variant=4 whole-benchmark passes; 452 scored attempts; errors excluded; harness=mini-swe-agent); 73.23008849557522 (metric=pass@1; version=1.1; dataset=113 tasks; effort=high; variant=4 whole-benchmark passes; 452 scored attempts; errors excluded; harness=mini-swe-agent); 72.78761061946902 (metric=pass@1; version=1.1; dataset=113 tasks; effort=medium; variant=4 whole-benchmark passes; 452 scored attempts; errors excluded; harness=mini-swe-agent); 67.03539823008849 (metric=pass@1; version=1.1; dataset=113 tasks; effort=low; variant=4 whole-benchmark passes; 452 scored attempts; errors excluded; harness=mini-swe-agent) | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T12:54+08:00 |
| swe-bench-pro-v2 | 已存在 | 96.9 (metric=task resolution rate; version=2.0.0; dataset=Full (642 tasks); effort=high; variant=offline agent phase; fresh-sandbox re-grading; harness=Codex) | [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro dataset and V2 protocol](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-04T12:54+08:00 |
| terminal-bench-v4 | 已存在 | 57.9 (metric=task resolution rate; version=4.0.0); 59.0909090909091 (metric=task resolution rate; version=4.0.0; dataset=Full (66 tasks); effort=max; variant=pass@1 averaged over 3 repeats; 500-step limit; harness=mini-swe-agent); 59.5959595959596 (metric=task resolution rate; version=4.0.0; dataset=Full (66 tasks); effort=xhigh; variant=pass@1 averaged over 3 repeats; 500-step limit; harness=mini-swe-agent); 54.040404040404 (metric=task resolution rate; version=4.0.0; dataset=Full (66 tasks); effort=high; variant=pass@1 averaged over 3 repeats; 500-step limit; harness=mini-swe-agent); 49.4949494949495 (metric=task resolution rate; version=4.0.0; dataset=Full (66 tasks); effort=medium; variant=pass@1 averaged over 3 repeats; 500-step limit; harness=mini-swe-agent); 41.9191919191919 (metric=task resolution rate; version=4.0.0; dataset=Full (66 tasks); effort=low; variant=pass@1 averaged over 3 repeats; 500-step limit; harness=mini-swe-agent); 59.6 (metric=task resolution rate; version=4.0.0; dataset=Full (66 tasks); variant=avg@3 (mean of three pass@1 runs); 8-hour task limit; no step or cost limit; harness=mini-swe-agent) | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [Artificial Analysis Astra evaluation results](https://artificialanalysis.ai/models/releases/gpt-6-astra), [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0), [Vals Terminal-Bench 4 result](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T12:54+08:00 |
| terminal-bench-science-v0.1 | 已存在 | 64.6 (metric=task resolution rate; version=0.1.0); 63.3333333333333 (metric=task resolution rate; version=0.1.0; dataset=Full (70 tasks); effort=max; variant=pass@1 averaged over 3 repeats; 1000-step limit; harness=mini-swe-agent); 54.7619047619048 (metric=task resolution rate; version=0.1.0; dataset=Full (70 tasks); effort=xhigh; variant=pass@1 averaged over 3 repeats; 1000-step limit; harness=mini-swe-agent); 59.5238095238095 (metric=task resolution rate; version=0.1.0; dataset=Full (70 tasks); effort=high; variant=pass@1 averaged over 3 repeats; 1000-step limit; harness=mini-swe-agent); 53.3333333333333 (metric=task resolution rate; version=0.1.0; dataset=Full (70 tasks); effort=medium; variant=pass@1 averaged over 3 repeats; 1000-step limit; harness=mini-swe-agent); 37.1428571428571 (metric=task resolution rate; version=0.1.0; dataset=Full (70 tasks); effort=low; variant=pass@1 averaged over 3 repeats; 1000-step limit; harness=mini-swe-agent); 62.86 (metric=task resolution rate; version=0.1.0; dataset=Full (70 tasks); variant=single pass@1 run; ungraded infrastructure/provider errors retried; 8-hour task limit; harness=mini-swe-agent) | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [Artificial Analysis Astra evaluation results](https://artificialanalysis.ai/models/releases/gpt-6-astra), [Terminal-Bench Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement), [Vals Terminal-Bench Science result](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T12:54+08:00 |
| automationbench-v1.0.6 | 已存在 | 41.4 (metric=success rate); 41.4 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=Max); 38.96 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=XHigh); 37.14 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=High) | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/) | 2026-11-04T12:54+08:00 |
| osworld-v2.1 | 已收录 | 72.6 (metric=partial score; version=2.0; dataset=V2-Offline (v2026.08.08)); 34.3 (metric=binary task completion rate; version=osworld-v2.1; dataset=108 real-world workflows; effort=max; harness=Common internal framework) | [Meta comparison with GPT-6 Astra results](https://dev.meta.ai/resources/blog/build-with-muse-wonder), [Meta Muse Wonder model card and OSWorld V2.1 methodology](https://research.meta.ai/static/muse-wonder-model-card/), [OpenAI GPT-6 Astra release (separate V2.0 result)](https://openai.com/index/gpt-6-astra/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T12:54+08:00 |
| chartography | 已存在 | 71 (metric=accuracy (mean; Pass@1); version=unspecified; effort=Max; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography leaderboard configuration and metric](https://github.com/surge-ai/chartography#leaderboard-configuration) | 2026-11-04T12:54+08:00 |
| humanitys-last-exam | 已存在 | 57.2 (metric=accuracy; variant=with tools) | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T12:54+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 61 (metric=index score; version=4.1.1; effort=max); 56.8538559596797 (metric=index score; version=5.0; effort=max); 55.2557468569681 (metric=index score; version=5.0; effort=xhigh); 54.849838322506 (metric=index score; version=5.0; effort=high); 51.4548393864113 (metric=index score; version=5.0; effort=medium); 43.0349823228524 (metric=index score; version=5.0; effort=low) | [Artificial Analysis GPT-6 Astra release results](https://artificialanalysis.ai/models/releases/gpt-6-astra), [Artificial Analysis Intelligence Index methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Data API version documentation](https://artificialanalysis.ai/data-api/docs) | 2026-11-04T12:54+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1583.69 (metric=Elo rating; version=2.1; dataset=220 public GDPval tasks; effort=max; harness=Stirrup); 1569.36 (metric=Elo rating; version=2.1; dataset=220 public GDPval tasks; effort=xhigh; harness=Stirrup); 1536.04 (metric=Elo rating; version=2.1; dataset=220 public GDPval tasks; effort=high; harness=Stirrup); 1498.47 (metric=Elo rating; version=2.1; dataset=220 public GDPval tasks; effort=medium; harness=Stirrup); 1403.26 (metric=Elo rating; version=2.1; dataset=220 public GDPval tasks; effort=low; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [GPT-6 Astra high vs GPT-6 Terra xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-5-6-terra-xhigh), [GPT-6 Astra medium vs xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-gpt-6-astra-xhigh) | 2026-11-04T12:54+08:00 |
| vals-index-v2.2 | 已存在 | 65.02 (metric=performance score; version=2.2) | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals GPT-6 Astra model results](https://www.vals.ai/models/openai_gpt-6-astra) | 2026-11-04T12:54+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 74.1
- metric: pass@1
- version: 1.1
- source: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 73.23008849557522
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: max
- variant: 4 whole-benchmark passes; 452 scored attempts; errors excluded
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: DeepSWE
- score: 74.11504424778761
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: xhigh
- variant: 4 whole-benchmark passes; 452 scored attempts; errors excluded
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: DeepSWE
- score: 73.23008849557522
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: high
- variant: 4 whole-benchmark passes; 452 scored attempts; errors excluded
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: DeepSWE
- score: 72.78761061946902
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: medium
- variant: 4 whole-benchmark passes; 452 scored attempts; errors excluded
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: DeepSWE
- score: 67.03539823008849
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: low
- variant: 4 whole-benchmark passes; 452 scored attempts; errors excluded
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 已有 OpenAI pass@1 v1.1 结果和五档 DeepSWE 官方榜单结果；榜单条目使用 113 tasks 和 mini-swe-agent，effort 各自保留。

最近核验时间：2026-11-04T12:54+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 96.9
- metric: task resolution rate
- version: 2.0.0
- dataset: Full (642 tasks)
- effort: high
- variant: offline agent phase; fresh-sandbox re-grading
- harness: Codex
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro dataset and V2 protocol](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- 已有 Scale 官方 V2.0.0、642 tasks、high-effort、Codex offline agent phase 与 fresh-sandbox re-grading 记录。

最近核验时间：2026-11-04T12:54+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 57.9
- metric: task resolution rate
- version: 4.0.0
- source: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 59.0909090909091
- metric: task resolution rate
- version: 4.0.0
- dataset: Full (66 tasks)
- effort: max
- variant: pass@1 averaged over 3 repeats; 500-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 59.5959595959596
- metric: task resolution rate
- version: 4.0.0
- dataset: Full (66 tasks)
- effort: xhigh
- variant: pass@1 averaged over 3 repeats; 500-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 54.040404040404
- metric: task resolution rate
- version: 4.0.0
- dataset: Full (66 tasks)
- effort: high
- variant: pass@1 averaged over 3 repeats; 500-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Terminal-Bench
- score: 49.4949494949495
- metric: task resolution rate
- version: 4.0.0
- dataset: Full (66 tasks)
- effort: medium
- variant: pass@1 averaged over 3 repeats; 500-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: Terminal-Bench
- score: 41.9191919191919
- metric: task resolution rate
- version: 4.0.0
- dataset: Full (66 tasks)
- effort: low
- variant: pass@1 averaged over 3 repeats; 500-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 7

- name: Terminal-Bench
- score: 59.6
- metric: task resolution rate
- version: 4.0.0
- dataset: Full (66 tasks)
- variant: avg@3 (mean of three pass@1 runs); 8-hour task limit; no step or cost limit
- harness: mini-swe-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [Artificial Analysis Astra evaluation results](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0)
- [Vals Terminal-Bench 4 result](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 已有 OpenAI 57.9% 结果、Artificial Analysis 五档 66-task mini-swe-agent 三次重复结果，以及独立 Vals avg@3 结果；各配置分开保留。

最近核验时间：2026-11-04T12:54+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 64.6
- metric: task resolution rate
- version: 0.1.0
- source: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 63.3333333333333
- metric: task resolution rate
- version: 0.1.0
- dataset: Full (70 tasks)
- effort: max
- variant: pass@1 averaged over 3 repeats; 1000-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Terminal-Bench-Science
- score: 54.7619047619048
- metric: task resolution rate
- version: 0.1.0
- dataset: Full (70 tasks)
- effort: xhigh
- variant: pass@1 averaged over 3 repeats; 1000-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Terminal-Bench-Science
- score: 59.5238095238095
- metric: task resolution rate
- version: 0.1.0
- dataset: Full (70 tasks)
- effort: high
- variant: pass@1 averaged over 3 repeats; 1000-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Terminal-Bench-Science
- score: 53.3333333333333
- metric: task resolution rate
- version: 0.1.0
- dataset: Full (70 tasks)
- effort: medium
- variant: pass@1 averaged over 3 repeats; 1000-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: Terminal-Bench-Science
- score: 37.1428571428571
- metric: task resolution rate
- version: 0.1.0
- dataset: Full (70 tasks)
- effort: low
- variant: pass@1 averaged over 3 repeats; 1000-step limit
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 7

- name: Terminal-Bench-Science
- score: 62.86
- metric: task resolution rate
- version: 0.1.0
- dataset: Full (70 tasks)
- variant: single pass@1 run; ungraded infrastructure/provider errors retried; 8-hour task limit
- harness: mini-swe-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [Artificial Analysis Astra evaluation results](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- [Terminal-Bench Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement)
- [Vals Terminal-Bench Science result](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- 已有 OpenAI 64.6% 结果、Artificial Analysis 五档 70-task mini-swe-agent 三次重复结果，以及独立 Vals 单次运行结果；各配置分开保留。

最近核验时间：2026-11-04T12:54+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 41.4
- metric: success rate
- source: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 41.4
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: Max
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 38.96
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: XHigh
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: AutomationBench
- score: 37.14
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: High
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)

研究备注：
- 已有三条 Zapier 官方 leaderboard 记录，版本 1.0.6、指标 task_completed_correctly、held-out private set；另保留 OpenAI 发布页中语义不同且未注明版本的 success rate 记录。

最近核验时间：2026-11-04T12:54+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 72.6
- metric: partial score
- version: 2.0
- dataset: V2-Offline (v2026.08.08)
- source: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: OSWorld
- score: 34.3
- metric: binary task completion rate
- version: osworld-v2.1
- dataset: 108 real-world workflows
- effort: max
- harness: Common internal framework
- source: [https://dev.meta.ai/resources/blog/build-with-muse-wonder](https://dev.meta.ai/resources/blog/build-with-muse-wonder)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Meta comparison with GPT-6 Astra results](https://dev.meta.ai/resources/blog/build-with-muse-wonder)
- [Meta Muse Wonder model card and OSWorld V2.1 methodology](https://research.meta.ai/static/muse-wonder-model-card/)
- [OpenAI GPT-6 Astra release (separate V2.0 result)](https://openai.com/index/gpt-6-astra/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 新增 Meta 官方比较表 GPT-6 Astra (max) 的 34.3 binary completion，v2.1、108 workflows、common internal framework。原有 OSWorld v2.0 72.6 partial score 使用 V2-Offline v2026.08.08，版本及指标均不同，保留为另一条记录。来源未披露评测日期，date 留空。

最近核验时间：2026-11-04T12:54+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 71
- metric: accuracy (mean; Pass@1)
- version: unspecified
- effort: Max
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography leaderboard configuration and metric](https://github.com/surge-ai/chartography#leaderboard-configuration)

研究备注：
- 已有 Surge 官方 leaderboard 71 分记录，metric accuracy (mean; Pass@1)、Max effort、10 runs/task、Inspect AI harness 和 Gemini 3.5 Flash judge；页面未公布目标定义的明确语义版本，因此仍使用 unspecified。

最近核验时间：2026-11-04T12:54+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 57.2
- metric: accuracy
- variant: with tools
- source: [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 已有 OpenAI 发布页报告的 accuracy 57.2 with tools 记录。来源未报告数据子集、effort 或 harness，不补猜。

最近核验时间：2026-11-04T12:54+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 61
- metric: index score
- version: 4.1.1
- effort: max
- source: [https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 56.8538559596797
- metric: index score
- version: 5.0
- effort: max
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 55.2557468569681
- metric: index score
- version: 5.0
- effort: xhigh
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Artificial Analysis Intelligence Index
- score: 54.849838322506
- metric: index score
- version: 5.0
- effort: high
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Artificial Analysis Intelligence Index
- score: 51.4548393864113
- metric: index score
- version: 5.0
- effort: medium
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: Artificial Analysis Intelligence Index
- score: 43.0349823228524
- metric: index score
- version: 5.0
- effort: low
- source: [https://artificialanalysis.ai/models/releases/gpt-6-astra](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GPT-6 Astra release results](https://artificialanalysis.ai/models/releases/gpt-6-astra)
- [Artificial Analysis Intelligence Index methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Data API version documentation](https://artificialanalysis.ai/data-api/docs)

研究备注：
- 已有五档 version 5.0 index score。当前 Artificial Analysis 方法页显示 v5.0.1，并记有 2026 年 11 月的重评；AA Data API 说明 patch 版本未必体现在 major.minor 字段。无法从公开精度确认本地小数对应的评测快照，暂保留全部记录并待复核版本/精度。

尚未解决的问题：
- 已有五档 version 5.0 index score。当前 Artificial Analysis 方法页显示 v5.0.1，并记有 2026 年 11 月的重评；AA Data API 说明 patch 版本未必体现在 major.minor 字段。无法从公开精度确认本地小数对应的评测快照，暂保留全部记录并待复核版本/精度。

最近核验时间：2026-11-04T12:54+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1583.69
- metric: Elo rating
- version: 2.1
- dataset: 220 public GDPval tasks
- effort: max
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1569.36
- metric: Elo rating
- version: 2.1
- dataset: 220 public GDPval tasks
- effort: xhigh
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: GDPval-AA
- score: 1536.04
- metric: Elo rating
- version: 2.1
- dataset: 220 public GDPval tasks
- effort: high
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: GDPval-AA
- score: 1498.47
- metric: Elo rating
- version: 2.1
- dataset: 220 public GDPval tasks
- effort: medium
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: GDPval-AA
- score: 1403.26
- metric: Elo rating
- version: 2.1
- dataset: 220 public GDPval tasks
- effort: low
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [GPT-6 Astra high vs GPT-6 Terra xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-5-6-terra-xhigh)
- [GPT-6 Astra medium vs xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-gpt-6-astra-xhigh)

研究备注：
- 已有五档 v2.1、220 public tasks、Stirrup Elo 记录。当前官方页面按整数显示的 high 档为 1537，而本地高精度记录为 1536.04；页面没有显示足以判断差异原因的精度。保留现有记录并待核实，其他四档显示值与记录四舍五入后吻合。

尚未解决的问题：
- 已有五档 v2.1、220 public tasks、Stirrup Elo 记录。当前官方页面按整数显示的 high 档为 1537，而本地高精度记录为 1536.04；页面没有显示足以判断差异原因的精度。保留现有记录并待核实，其他四档显示值与记录四舍五入后吻合。

最近核验时间：2026-11-04T12:54+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 65.02
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals GPT-6 Astra model results](https://www.vals.ai/models/openai_gpt-6-astra)

研究备注：
- 已有 Vals Index v2.2 performance score 65.02，精确匹配当前官方榜单。排行榜更新时间不作为 benchmark date。

最近核验时间：2026-11-04T12:54+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-6 Astra release results",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-astra"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology and version history",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Data API version documentation",
          "url": "https://artificialanalysis.ai/data-api/docs"
        }
      ],
      "notes": [
        "已有五档 version 5.0 index score。当前 Artificial Analysis 方法页显示 v5.0.1，并记有 2026 年 11 月的重评；AA Data API 说明 patch 版本未必体现在 major.minor 字段。无法从公开精度确认本地小数对应的评测快照，暂保留全部记录并待复核版本/精度。"
      ],
      "status": "待核实",
      "unresolved": [
        "已有五档 version 5.0 index score。当前 Artificial Analysis 方法页显示 v5.0.1，并记有 2026 年 11 月的重评；AA Data API 说明 patch 版本未必体现在 major.minor 字段。无法从公开精度确认本地小数对应的评测快照，暂保留全部记录并待复核版本/精度。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        }
      ],
      "notes": [
        "已有三条 Zapier 官方 leaderboard 记录，版本 1.0.6、指标 task_completed_correctly、held-out private set；另保留 OpenAI 发布页中语义不同且未注明版本的 success rate 记录。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography leaderboard configuration and metric",
          "url": "https://github.com/surge-ai/chartography#leaderboard-configuration"
        }
      ],
      "notes": [
        "已有 Surge 官方 leaderboard 71 分记录，metric accuracy (mean; Pass@1)、Max effort、10 runs/task、Inspect AI harness 和 Gemini 3.5 Flash judge；页面未公布目标定义的明确语义版本，因此仍使用 unspecified。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "已有 OpenAI pass@1 v1.1 结果和五档 DeepSWE 官方榜单结果；榜单条目使用 113 tasks 和 mini-swe-agent，effort 各自保留。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "GPT-6 Astra high vs GPT-6 Terra xhigh comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-5-6-terra-xhigh"
        },
        {
          "label": "GPT-6 Astra medium vs xhigh comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-gpt-6-astra-xhigh"
        }
      ],
      "notes": [
        "已有五档 v2.1、220 public tasks、Stirrup Elo 记录。当前官方页面按整数显示的 high 档为 1537，而本地高精度记录为 1536.04；页面没有显示足以判断差异原因的精度。保留现有记录并待核实，其他四档显示值与记录四舍五入后吻合。"
      ],
      "status": "待核实",
      "unresolved": [
        "已有五档 v2.1、220 public tasks、Stirrup Elo 记录。当前官方页面按整数显示的 high 档为 1537，而本地高精度记录为 1536.04；页面没有显示足以判断差异原因的精度。保留现有记录并待核实，其他四档显示值与记录四舍五入后吻合。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "已有 OpenAI 发布页报告的 accuracy 57.2 with tools 记录。来源未报告数据子集、effort 或 harness，不补猜。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Meta comparison with GPT-6 Astra results",
          "url": "https://dev.meta.ai/resources/blog/build-with-muse-wonder"
        },
        {
          "label": "Meta Muse Wonder model card and OSWorld V2.1 methodology",
          "url": "https://research.meta.ai/static/muse-wonder-model-card/"
        },
        {
          "label": "OpenAI GPT-6 Astra release (separate V2.0 result)",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "新增 Meta 官方比较表 GPT-6 Astra (max) 的 34.3 binary completion，v2.1、108 workflows、common internal framework。原有 OSWorld v2.0 72.6 partial score 使用 V2-Offline v2026.08.08，版本及指标均不同，保留为另一条记录。来源未披露评测日期，date 留空。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro dataset and V2 protocol",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "已有 Scale 官方 V2.0.0、642 tasks、high-effort、Codex offline agent phase 与 fresh-sandbox re-grading 记录。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "Artificial Analysis Astra evaluation results",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-astra"
        },
        {
          "label": "Terminal-Bench Science 0.1 announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Vals Terminal-Bench Science result",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "已有 OpenAI 64.6% 结果、Artificial Analysis 五档 70-task mini-swe-agent 三次重复结果，以及独立 Vals 单次运行结果；各配置分开保留。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "Artificial Analysis Astra evaluation results",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-astra"
        },
        {
          "label": "Terminal-Bench 4.0 official release",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Vals Terminal-Bench 4 result",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "已有 OpenAI 57.9% 结果、Artificial Analysis 五档 66-task mini-swe-agent 三次重复结果，以及独立 Vals avg@3 结果；各配置分开保留。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T12:54+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals GPT-6 Astra model results",
          "url": "https://www.vals.ai/models/openai_gpt-6-astra"
        }
      ],
      "notes": [
        "已有 Vals Index v2.2 performance score 65.02，精确匹配当前官方榜单。排行榜更新时间不作为 benchmark date。"
      ],
      "status": "已存在",
      "unresolved": []
    }
  },
  "existing_records": 51,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T12:54+08:00",
  "model_id": "openai/gpt-6-astra",
  "new_records": 1,
  "overall_status": "待复核"
}

-->
