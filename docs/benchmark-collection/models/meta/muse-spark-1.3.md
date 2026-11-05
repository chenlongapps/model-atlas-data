# Muse Spark 1.3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-spark-1.3
- 模型名称：Muse Spark 1.3
- 发布日期：2026-09-02
- 最近检查时间：2026-11-04T14:25+08:00
- 整体处理状态：待复核
- 新增成绩数量：13
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：7

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 75.4 (metric=pass@1; version=1.1; variant=max effort; harness=mini-swe-agent) | [Meta 评测方法](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology), [Meta 发布说明](https://research.meta.ai/blog/introducing-muse-spark-1-3), [Meta 成绩卡](https://research.meta.ai/articles/introducing-muse-1-3/benchmarks/benchmark-scorecard-v6.webp) | 2026-11-04T14:25+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Meta 评测方法](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology), [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T14:25+08:00 |
| terminal-bench-v4 | 待核实 | 88.8 (metric=pass@1; version=2.1; variant=max effort; harness=Muse Code); 33 (metric=pass@1; version=4.0; dataset=66 tasks; effort=Max; variant=mean of 3 repeats per task; harness=mini-swe-agent); 17 (metric=pass@1; version=4.0; dataset=66 tasks; effort=Xhigh; variant=mean of 3 repeats per task; harness=mini-swe-agent) | [Artificial Analysis Max / Xhigh 对比结果](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh), [Terminal-Bench 4.0 评测方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Meta 评测方法](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology) | 2026-11-04T14:25+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 11 (metric=pass@1; version=0.1.0; dataset=70 tasks; effort=Max; variant=mean of 3 repeats per task; harness=mini-swe-agent); 4 (metric=pass@1; version=0.1.0; dataset=70 tasks; effort=Xhigh; variant=mean of 3 repeats per task; harness=mini-swe-agent) | [Artificial Analysis Max / Xhigh 对比结果](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh), [Terminal-Bench-Science 0.1 评测方法](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T14:25+08:00 |
| automationbench-v1.0.6 | 已收录 | 49.6 (metric=pass@1; dataset=public v3 task set; variant=max effort); 20.7 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out workflows; variant=API mode; 50-step cap) | [Zapier AutomationBench 官方榜单 / 方法](https://zapier.com/benchmarks), [Fireworks 精确成绩行](https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench) | 2026-11-04T14:25+08:00 |
| osworld-v2.1 | 待核实 | 66.9 (metric=mean partial score; version=2.0; dataset=08.08; variant=max effort; harness=Meta internal evaluation framework); 32.0 (metric=binary completion rate; version=2.0; dataset=08.08; variant=max effort; harness=Meta internal evaluation framework); 69.6 (metric=mean partial score; version=v2.1; dataset=108 tasks; effort=max; variant=batch tool; up to 500 actions); 39.3 (metric=binary task completion rate; version=v2.1; dataset=108 tasks; effort=max; variant=batch tool; up to 500 actions) | [OSWorld 2.1 团队结果汇总](https://www.aib.vote/en/benchmarks/osworld-2-1), [XLANG Lab OSWorld V2](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T14:25+08:00 |
| chartography | 已收录 | 27.6 (metric=accuracy (mean; Pass@1); dataset=100 expert-authored tasks; effort=xHigh reasoning; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge AI 官方 Chartography 榜单](https://surgehq.ai/benchmarks/chartography), [Surge AI Chartography README / 方法](https://github.com/surge-ai/chartography/blob/main/README.md) | 2026-11-04T14:25+08:00 |
| humanitys-last-exam | 已收录 | 49 (metric=accuracy; dataset=original HLE; 2,500 questions; effort=Max); 47 (metric=accuracy; dataset=original HLE; 2,500 questions; effort=Xhigh) | [Artificial Analysis Max 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high), [Artificial Analysis Xhigh 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling), [Artificial Analysis HLE 方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [HLE 官方网站](https://lastexam.ai/) | 2026-11-04T14:25+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 37 (metric=index score; version=5.0.1; effort=Max) | [Artificial Analysis Muse Spark 1.3 模型页](https://artificialanalysis.ai/models/muse-spark-1-3), [Artificial Analysis 指数版本历史与方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T14:25+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1754 (metric=Elo; version=2; variant=max effort; harness=Stirrup); 1681 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Max; variant=shell and web access; blind pairwise comparisons; harness=Stirrup); 1627 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Xhigh; variant=shell and web access; blind pairwise comparisons; harness=Stirrup) | [Artificial Analysis GDPval-AA Max 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high), [Artificial Analysis GDPval-AA Xhigh 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling), [GDPval-AA v2.1 评测方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T14:25+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index), [Vals AI Muse Spark 1.3 模型页](https://www.vals.ai/models/meta_muse_spark_1_3) | 2026-11-04T14:25+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 75.4
- metric: pass@1
- version: 1.1
- variant: max effort
- harness: mini-swe-agent
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Meta 评测方法](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)
- [Meta 发布说明](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- [Meta 成绩卡](https://research.meta.ai/articles/introducing-muse-1-3/benchmarks/benchmark-scorecard-v6.webp)

研究备注：
- 现有 75.4 pass@1、v1.1、max effort、mini-swe-agent 记录与 Meta 方法资料对应；保留原成绩。
- 此模型文件原有 12 条 Meta 成绩均把发布文章日期 2026-09-02 写作 date；方法资料没有提供评测日期，已仅移除这些 date 字段，保留所有原分数、测试条件和来源。

最近核验时间：2026-11-04T14:25+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Meta 评测方法](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)
- [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 未找到 Muse Spark 1.3 的 SWE-bench Pro V2 结果；Scale 榜单中的 Muse Spark Open 是不同模型身份，未当作本模型成绩。

最近核验时间：2026-11-04T14:25+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 88.8
- metric: pass@1
- version: 2.1
- variant: max effort
- harness: Muse Code
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 33
- metric: pass@1
- version: 4.0
- dataset: 66 tasks
- effort: Max
- variant: mean of 3 repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 17
- metric: pass@1
- version: 4.0
- dataset: 66 tasks
- effort: Xhigh
- variant: mean of 3 repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Max / Xhigh 对比结果](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh)
- [Terminal-Bench 4.0 评测方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Meta 评测方法](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)

研究备注：
- Artificial Analysis 独立评测列出 Max 33% 与 Xhigh 17%；两档分别保留，配置为 66 tasks、mini-swe-agent、pass@1 每任务三次运行均值。
- Meta 发布说明另有 Terminal-Bench 2.1 的 88.8 pass@1（Muse Code），版本和 Harness 不同，单独保留。

尚未解决的问题：
- 本地定义要求版本 4.0.0 与指标 task resolution rate；来源记录为 4.0 与 pass@1，保留来源字段，暂不计入精确映射覆盖率。

最近核验时间：2026-11-04T14:25+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 11
- metric: pass@1
- version: 0.1.0
- dataset: 70 tasks
- effort: Max
- variant: mean of 3 repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 4
- metric: pass@1
- version: 0.1.0
- dataset: 70 tasks
- effort: Xhigh
- variant: mean of 3 repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Max / Xhigh 对比结果](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh)
- [Terminal-Bench-Science 0.1 评测方法](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- Artificial Analysis 独立评测列出 Max 11% 与 Xhigh 4%；两档分别保留，70 tasks、mini-swe-agent、pass@1 每任务三次运行均值。

尚未解决的问题：
- 本地定义指标为 task resolution rate；来源指标为 pass@1，未将其强行改写成定义值，因此不计入精确映射覆盖率。

最近核验时间：2026-11-04T14:25+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 49.6
- metric: pass@1
- dataset: public v3 task set
- variant: max effort
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 20.7
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out workflows
- variant: API mode; 50-step cap
- source: [https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench](https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench 官方榜单 / 方法](https://zapier.com/benchmarks)
- [Fireworks 精确成绩行](https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench)

研究备注：
- Muse Spark 1.3 20.7% 行见 Fireworks 榜单镜像；Zapier 官方页面确认当前榜单版本 1.0.6 与确定性全断言通过规则，但其文本视图未展开 Muse 行。记录使用官方指标 task_completed_correctly，657 个 held-out workflows、API mode、每项最多 50 步。
- 现有 49.6 pass@1 是 Meta public v3 task set，版本与数据集不同，分别保留。未把排行榜更新时间写入 date。

最近核验时间：2026-11-04T14:25+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 66.9
- metric: mean partial score
- version: 2.0
- dataset: 08.08
- variant: max effort
- harness: Meta internal evaluation framework
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: OSWorld
- score: 32.0
- metric: binary completion rate
- version: 2.0
- dataset: 08.08
- variant: max effort
- harness: Meta internal evaluation framework
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: OSWorld
- score: 69.6
- metric: mean partial score
- version: v2.1
- dataset: 108 tasks
- effort: max
- variant: batch tool; up to 500 actions
- source: [https://www.aib.vote/en/benchmarks/osworld-2-1](https://www.aib.vote/en/benchmarks/osworld-2-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: OSWorld
- score: 39.3
- metric: binary task completion rate
- version: v2.1
- dataset: 108 tasks
- effort: max
- variant: batch tool; up to 500 actions
- source: [https://www.aib.vote/en/benchmarks/osworld-2-1](https://www.aib.vote/en/benchmarks/osworld-2-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [OSWorld 2.1 团队结果汇总](https://www.aib.vote/en/benchmarks/osworld-2-1)
- [XLANG Lab OSWorld V2](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 团队结果表同时列出 69.6% partial score 与 39.3% all-checks-passed 二元成功率；作为不同指标分开记录。条件为 108 tasks、max、batch tool、最多 500 actions。页面所示 2026-09-02 是模型发布日期，不是评测日期。
- 此前 66.9 mean partial score 和 32.0 binary completion rate 属于 OSWorld 2.0、08.08 数据集，继续保留。

尚未解决的问题：
- 来源版本标签为 v2.1，本地定义字段为 osworld-v2.1；保留来源原标签，等待确认本地映射规范。69.6 partial score 也不是本地定义的 binary task completion rate。

最近核验时间：2026-11-04T14:25+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 27.6
- metric: accuracy (mean; Pass@1)
- dataset: 100 expert-authored tasks
- effort: xHigh reasoning
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI 官方 Chartography 榜单](https://surgehq.ai/benchmarks/chartography)
- [Surge AI Chartography README / 方法](https://github.com/surge-ai/chartography/blob/main/README.md)

研究备注：
- 确认 Muse Spark 1.3 (xHigh reasoning) 27.6%；使用 100 个专家编写任务，accuracy (mean; Pass@1)，Inspect AI。README 说明 Gemini 3.5 Flash judge；版本未指定，未编造 version/date。

最近核验时间：2026-11-04T14:25+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 49
- metric: accuracy
- dataset: original HLE; 2,500 questions
- effort: Max
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 47
- metric: accuracy
- dataset: original HLE; 2,500 questions
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Max 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high)
- [Artificial Analysis Xhigh 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling)
- [Artificial Analysis HLE 方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [HLE 官方网站](https://lastexam.ai/)

研究备注：
- Max 49% 与 Xhigh 47% 是原版 Humanity’s Last Exam accuracy，分别记录；数据集为 2,500 题。没有把 HLE-Diamond 结果混入，也未推测 Harness 或评测日期。

最近核验时间：2026-11-04T14:25+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 37
- metric: index score
- version: 5.0.1
- effort: Max
- source: [https://artificialanalysis.ai/models/muse-spark-1-3](https://artificialanalysis.ai/models/muse-spark-1-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.3 模型页](https://artificialanalysis.ai/models/muse-spark-1-3)
- [Artificial Analysis 指数版本历史与方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Muse Spark 1.3 Max 当前分数 37，模型页将当前指数标为 v5.0.1；没有为 Xhigh 找到该版本分数。

尚未解决的问题：
- 本地定义版本为 5.0，来源结果为 5.0.1；保留来源版本，不计入版本 5.0 的精确覆盖率。

最近核验时间：2026-11-04T14:25+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1754
- metric: Elo
- version: 2
- variant: max effort
- harness: Stirrup
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1681
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Max
- variant: shell and web access; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: GDPval-AA
- score: 1627
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Xhigh
- variant: shell and web access; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA Max 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high)
- [Artificial Analysis GDPval-AA Xhigh 成绩](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling)
- [GDPval-AA v2.1 评测方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Max 1681 Elo、Xhigh 1627 Elo，版本 v2.1（来源标题及方法页为 2.1）；各档分别记录。数据集 220 tasks / 44 occupations / 9 industries，Stirrup，shell 与 web 访问、盲测 pairwise 比较。已有的 1754 Elo 属于 GDPval-AA v2，保留为独立版本。

最近核验时间：2026-11-04T14:25+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI Muse Spark 1.3 模型页](https://www.vals.ai/models/meta_muse_spark_1_3)

研究备注：
- 当前 v2.2 榜单未列出 Muse Spark 1.3 的分数；模型页 44.99% 是通用 accuracy，不能据此推断 Vals Index。榜单中 Muse Spark Open 是其他模型身份，也未作替代。

最近核验时间：2026-11-04T14:25+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.3 模型页",
          "url": "https://artificialanalysis.ai/models/muse-spark-1-3"
        },
        {
          "label": "Artificial Analysis 指数版本历史与方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Muse Spark 1.3 Max 当前分数 37，模型页将当前指数标为 v5.0.1；没有为 Xhigh 找到该版本分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义版本为 5.0，来源结果为 5.0.1；保留来源版本，不计入版本 5.0 的精确覆盖率。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单 / 方法",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Fireworks 精确成绩行",
          "url": "https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench"
        }
      ],
      "notes": [
        "Muse Spark 1.3 20.7% 行见 Fireworks 榜单镜像；Zapier 官方页面确认当前榜单版本 1.0.6 与确定性全断言通过规则，但其文本视图未展开 Muse 行。记录使用官方指标 task_completed_correctly，657 个 held-out workflows、API mode、每项最多 50 步。",
        "现有 49.6 pass@1 是 Meta public v3 task set，版本与数据集不同，分别保留。未把排行榜更新时间写入 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Surge AI 官方 Chartography 榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge AI Chartography README / 方法",
          "url": "https://github.com/surge-ai/chartography/blob/main/README.md"
        }
      ],
      "notes": [
        "确认 Muse Spark 1.3 (xHigh reasoning) 27.6%；使用 100 个专家编写任务，accuracy (mean; Pass@1)，Inspect AI。README 说明 Gemini 3.5 Flash judge；版本未指定，未编造 version/date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Meta 评测方法",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        },
        {
          "label": "Meta 发布说明",
          "url": "https://research.meta.ai/blog/introducing-muse-spark-1-3"
        },
        {
          "label": "Meta 成绩卡",
          "url": "https://research.meta.ai/articles/introducing-muse-1-3/benchmarks/benchmark-scorecard-v6.webp"
        }
      ],
      "notes": [
        "现有 75.4 pass@1、v1.1、max effort、mini-swe-agent 记录与 Meta 方法资料对应；保留原成绩。",
        "此模型文件原有 12 条 Meta 成绩均把发布文章日期 2026-09-02 写作 date；方法资料没有提供评测日期，已仅移除这些 date 字段，保留所有原分数、测试条件和来源。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA Max 成绩",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high"
        },
        {
          "label": "Artificial Analysis GDPval-AA Xhigh 成绩",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling"
        },
        {
          "label": "GDPval-AA v2.1 评测方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Max 1681 Elo、Xhigh 1627 Elo，版本 v2.1（来源标题及方法页为 2.1）；各档分别记录。数据集 220 tasks / 44 occupations / 9 industries，Stirrup，shell 与 web 访问、盲测 pairwise 比较。已有的 1754 Elo 属于 GDPval-AA v2，保留为独立版本。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Max 成绩",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-gpt-5-6-sol-high"
        },
        {
          "label": "Artificial Analysis Xhigh 成绩",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-xhigh-vs-inkling"
        },
        {
          "label": "Artificial Analysis HLE 方法",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "HLE 官方网站",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "Max 49% 与 Xhigh 47% 是原版 Humanity’s Last Exam accuracy，分别记录；数据集为 2,500 题。没有把 HLE-Diamond 结果混入，也未推测 Harness 或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 2.1 团队结果汇总",
          "url": "https://www.aib.vote/en/benchmarks/osworld-2-1"
        },
        {
          "label": "XLANG Lab OSWorld V2",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "团队结果表同时列出 69.6% partial score 与 39.3% all-checks-passed 二元成功率；作为不同指标分开记录。条件为 108 tasks、max、batch tool、最多 500 actions。页面所示 2026-09-02 是模型发布日期，不是评测日期。",
        "此前 66.9 mean partial score 和 32.0 binary completion rate 属于 OSWorld 2.0、08.08 数据集，继续保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源版本标签为 v2.1，本地定义字段为 osworld-v2.1；保留来源原标签，等待确认本地映射规范。69.6 partial score 也不是本地定义的 binary task completion rate。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Meta 评测方法",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        },
        {
          "label": "Scale SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "未找到 Muse Spark 1.3 的 SWE-bench Pro V2 结果；Scale 榜单中的 Muse Spark Open 是不同模型身份，未当作本模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Max / Xhigh 对比结果",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh"
        },
        {
          "label": "Terminal-Bench-Science 0.1 评测方法",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "Artificial Analysis 独立评测列出 Max 11% 与 Xhigh 4%；两档分别保留，70 tasks、mini-swe-agent、pass@1 每任务三次运行均值。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义指标为 task resolution rate；来源指标为 pass@1，未将其强行改写成定义值，因此不计入精确映射覆盖率。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Max / Xhigh 对比结果",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-3-xhigh"
        },
        {
          "label": "Terminal-Bench 4.0 评测方法",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Meta 评测方法",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        }
      ],
      "notes": [
        "Artificial Analysis 独立评测列出 Max 33% 与 Xhigh 17%；两档分别保留，配置为 66 tasks、mini-swe-agent、pass@1 每任务三次运行均值。",
        "Meta 发布说明另有 Terminal-Bench 2.1 的 88.8 pass@1（Muse Code），版本和 Harness 不同，单独保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义要求版本 4.0.0 与指标 task resolution rate；来源记录为 4.0 与 pass@1，保留来源字段，暂不计入精确映射覆盖率。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T14:25+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI Muse Spark 1.3 模型页",
          "url": "https://www.vals.ai/models/meta_muse_spark_1_3"
        }
      ],
      "notes": [
        "当前 v2.2 榜单未列出 Muse Spark 1.3 的分数；模型页 44.99% 是通用 accuracy，不能据此推断 Vals Index。榜单中 Muse Spark Open 是其他模型身份，也未作替代。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T14:25+08:00",
  "model_id": "meta/muse-spark-1.3",
  "new_records": 13,
  "overall_status": "待复核"
}

-->
