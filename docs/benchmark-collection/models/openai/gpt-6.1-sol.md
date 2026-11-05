# GPT-6.1 Sol Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-6.1-sol
- 模型名称：GPT-6.1 Sol
- 发布日期：2026-09-29
- 最近检查时间：2026-11-04T06:26+08:00
- 整体处理状态：待复核
- 新增成绩数量：20
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：20

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [OpenAI GPT-6.1 Sol 发布说明](https://openai.com/index/introducing-gpt-6-1-sol/), [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T06:26+08:00 |
| swe-bench-pro-v2 | 已收录 | 96.11 (metric=task resolution rate; version=2.0.0; dataset=V2 Full (642 tasks); effort=xhigh; harness=mini-swe-agent) | [Scale AI SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T06:26+08:00 |
| terminal-bench-v4 | 已收录 | 58.2 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=max; harness=Codex); 55.05 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; variant=avg@3; three full runs, each run scored pass@1; harness=mini-swe-agent); 56 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=Max; variant=pass@1 averaged over three repeats; 500 agent step cap; harness=mini-swe-agent); 54 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=Xhigh; variant=pass@1 averaged over three repeats; 500 agent step cap; harness=mini-swe-agent); 52 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=High; variant=pass@1 averaged over three repeats; 500 agent step cap; harness=mini-swe-agent); 48 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=Medium; variant=pass@1 averaged over three repeats; 500 agent step cap; harness=mini-swe-agent); 31 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; effort=Low; variant=pass@1 averaged over three repeats; 500 agent step cap; harness=mini-swe-agent) | [Terminal-Bench 4.0 官方榜单（Codex）](https://www.tbench.ai/?efforts=all&version=4.0), [Vals Terminal-Bench 4 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4), [Vals GPT-6.1 Sol model profile](https://www.vals.ai/models/openai_gpt-6.1-sol), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Max comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol), [Artificial Analysis Xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low), [Artificial Analysis High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low), [Artificial Analysis Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium), [Artificial Analysis Low comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh) | 2026-11-04T06:26+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 52.86 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; variant=single run per model; pass@1; harness=mini-swe-agent); 58 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; effort=Max; variant=pass@1 averaged over three repeats; 1,000 agent step cap; harness=mini-swe-agent); 50 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; effort=Xhigh; variant=pass@1 averaged over three repeats; 1,000 agent step cap; harness=mini-swe-agent); 46 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; effort=High; variant=pass@1 averaged over three repeats; 1,000 agent step cap; harness=mini-swe-agent); 37 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; effort=Medium; variant=pass@1 averaged over three repeats; 1,000 agent step cap; harness=mini-swe-agent); 11 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; effort=Low; variant=pass@1 averaged over three repeats; 1,000 agent step cap; harness=mini-swe-agent) | [Vals Terminal-Bench-Science leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-science), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Max comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol), [Artificial Analysis Xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low), [Artificial Analysis High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low), [Artificial Analysis Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium), [Artificial Analysis Low comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh) | 2026-11-04T06:26+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [OpenAI GPT-6.1 Sol 发布说明](https://openai.com/index/introducing-gpt-6-1-sol/), [Zapier AutomationBench 1.0.6 official leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench) | 2026-11-04T06:26+08:00 |
| osworld-v2.1 | 未找到 | — | [OpenAI GPT-6.1 Sol 发布说明](https://openai.com/index/introducing-gpt-6-1-sol/), [OSWorld official benchmark site](https://os-world.github.io/) | 2026-11-04T06:26+08:00 |
| chartography | 未找到 | — | [Surge AI benchmark leaderboard](https://surgehq.ai/benchmarks), [Surge AI Chartography benchmark article](https://surgehq.ai/blog/chartography) | 2026-11-04T06:26+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale AI Humanity’s Last Exam official leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis GPT-6.1 Sol profile](https://artificialanalysis.ai/models/gpt-6-1-sol), [Artificial Analysis HLE and HLE-Diamond methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T06:26+08:00 |
| artificial-analysis-intelligence-index-v5 | 冲突 | 55 (metric=index score; version=5.0; dataset=V5 composite (9 evaluations); effort=Max); 52 (metric=index score; version=5.0; dataset=V5 composite (9 evaluations); effort=Xhigh); 50 (metric=index score; version=5.0; dataset=V5 composite (9 evaluations); effort=High); 46 (metric=index score; version=5.0; dataset=V5 composite (9 evaluations); effort=Medium); 35 (metric=index score; version=5.0; dataset=V5 composite (9 evaluations); effort=Low) | [Artificial Analysis GPT-6.1 Sol current model profile](https://artificialanalysis.ai/models/gpt-6-1-sol), [Artificial Analysis GPT-6.1 Sol release page](https://artificialanalysis.ai/models/releases/gpt-6-1-sol), [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Max comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol), [Artificial Analysis Xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low), [Artificial Analysis High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-luna-high), [Artificial Analysis Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium), [Artificial Analysis Low comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh) | 2026-11-04T06:26+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GPT-6.1 Sol release article](https://artificialanalysis.ai/articles/gpt-6-1-sol-replaces-gpt-6-sol-after-just-7-days-with-near-astra-intelligence), [Artificial Analysis GDPval-AA v2.1 evaluation and leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa) | 2026-11-04T06:26+08:00 |
| vals-index-v2.2 | 已收录 | 63.94 (metric=performance score; version=2.2; dataset=finance, coding, legal, and tax tasks) | [Vals GPT-6.1 Sol model profile](https://www.vals.ai/models/openai_gpt-6.1-sol), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T06:26+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-6.1 Sol 发布说明](https://openai.com/index/introducing-gpt-6-1-sol/)
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- OpenAI 只披露相对 GPT-6 Sol 最佳成绩高 6.4 个百分点，没有公布 GPT-6.1 Sol 绝对分数、effort、harness 或评测日期。
- 研究代理核对的官方榜单显示 113 项任务数据更新时间早于本模型发布日期；不从相对提升反推绝对成绩。

尚未解决的问题：
- 需找到 GPT-6.1 Sol 准确版本的公开绝对成绩及测试条件。

最近核验时间：2026-11-04T06:26+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 96.11
- metric: task resolution rate
- version: 2.0.0
- dataset: V2 Full (642 tasks)
- effort: xhigh
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 官方 Full leaderboard 的 GPT-6.1-Sol (mini-swe-agent), xhigh 行为 96.11±1.24%；V2 Full 数据集为 642 tasks。模型 TOML 保留点估计 96.11，原始页面保留不确定度。
- 没有使用 HARD 子集分数，也没有填写排行榜更新时间作为评测日期。

最近核验时间：2026-11-04T06:26+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 58.2
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: max
- harness: Codex
- source: [https://www.tbench.ai/?efforts=all&version=4.0](https://www.tbench.ai/?efforts=all&version=4.0)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 55.05
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- variant: avg@3; three full runs, each run scored pass@1
- harness: mini-swe-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 56
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: Max
- variant: pass@1 averaged over three repeats; 500 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 54
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: Xhigh
- variant: pass@1 averaged over three repeats; 500 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Terminal-Bench
- score: 52
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: High
- variant: pass@1 averaged over three repeats; 500 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: Terminal-Bench
- score: 48
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: Medium
- variant: pass@1 averaged over three repeats; 500 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 7

- name: Terminal-Bench
- score: 31
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- effort: Low
- variant: pass@1 averaged over three repeats; 500 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Terminal-Bench 4.0 官方榜单（Codex）](https://www.tbench.ai/?efforts=all&version=4.0)
- [Vals Terminal-Bench 4 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Vals GPT-6.1 Sol model profile](https://www.vals.ai/models/openai_gpt-6.1-sol)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Max comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol)
- [Artificial Analysis Xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low)
- [Artificial Analysis High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low)
- [Artificial Analysis Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium)
- [Artificial Analysis Low comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh)

研究备注：
- 保留了三种公开条件：Terminal-Bench 官方榜 Codex/max 58.2%（来源报告 ±3.1）；Vals mini-swe-agent 55.05%（avg@3，三次完整运行）；Artificial Analysis mini-swe-agent 按 Max/Xhigh/High/Medium/Low 分别为 56/54/52/48/31（各次 pass@1 平均三次，500 步上限）。
- 不同 harness 或执行配置的成绩分别保留；没有用最高分替代其他结果。Vals 页面报告 ±1.82 标准误，AA 页面以整数百分数展示。

最近核验时间：2026-11-04T06:26+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 52.86
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- variant: single run per model; pass@1
- harness: mini-swe-agent
- source: [https://vals-ai.com/benchmarks/terminal-bench-science](https://vals-ai.com/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 58
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- effort: Max
- variant: pass@1 averaged over three repeats; 1,000 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Terminal-Bench-Science
- score: 50
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- effort: Xhigh
- variant: pass@1 averaged over three repeats; 1,000 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Terminal-Bench-Science
- score: 46
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- effort: High
- variant: pass@1 averaged over three repeats; 1,000 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Terminal-Bench-Science
- score: 37
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- effort: Medium
- variant: pass@1 averaged over three repeats; 1,000 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: Terminal-Bench-Science
- score: 11
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- effort: Low
- variant: pass@1 averaged over three repeats; 1,000 agent step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Terminal-Bench-Science leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-science)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Max comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol)
- [Artificial Analysis Xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low)
- [Artificial Analysis High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low)
- [Artificial Analysis Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium)
- [Artificial Analysis Low comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh)

研究备注：
- Vals 的官方 leaderboard 明确显示 Mini-SWE-agent 52.86%，70 项任务；其方法为单次运行、pass@1。
- Artificial Analysis 的独立评测按 Max/Xhigh/High/Medium/Low 分别为 58/50/46/37/11，使用完整 70 项、mini-swe-agent、三次 pass@1 平均和 1,000 步上限。配置不同的值均保留。

最近核验时间：2026-11-04T06:26+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-6.1 Sol 发布说明](https://openai.com/index/introducing-gpt-6-1-sol/)
- [Zapier AutomationBench 1.0.6 official leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)

研究备注：
- OpenAI 只报告 medium effort 下相对 GPT-6 Sol 提高 4.8 个百分点及相对 Opus 的差值，没有公布 Sol 的绝对分数。
- 当前 Zapier 榜单公开展示前十名，GPT-6.1 Sol 未在可读榜单条目中；不以相对差值计算成绩。

尚未解决的问题：
- 需核实 GPT-6.1 Sol 是否有公开的 AutomationBench 1.0.6 绝对分数及精确 effort。

最近核验时间：2026-11-04T06:26+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-6.1 Sol 发布说明](https://openai.com/index/introducing-gpt-6-1-sol/)
- [OSWorld official benchmark site](https://os-world.github.io/)

研究备注：
- OpenAI 报告的是 OSWorld 2.0 offline set、partial reward、v2026.08.08、max effort 的相对成绩；仓库目标是 OSWorld 2.1 binary completion rate，不能将该结果映射到 v2.1。
- 未找到属于 GPT-6.1 Sol 准确版本且匹配 v2.1 目标的公开绝对成绩。

最近核验时间：2026-11-04T06:26+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI benchmark leaderboard](https://surgehq.ai/benchmarks)
- [Surge AI Chartography benchmark article](https://surgehq.ai/blog/chartography)

研究备注：
- Surge 的 Chartography 榜单可见 GPT-6 Astra Max 等结果；检索到的 GPT-6 Sol Max 条目属于不同模型，没有找到 GPT-6.1 Sol 准确版本成绩。
- GPT-6.1 Sol 支持图像输入，因此该 Benchmark 适用；无分数不代表 0。

最近核验时间：2026-11-04T06:26+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI Humanity’s Last Exam official leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis GPT-6.1 Sol profile](https://artificialanalysis.ai/models/gpt-6-1-sol)
- [Artificial Analysis HLE and HLE-Diamond methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 仓库定义指原始 2,500 题 HLE。当前 AA GPT-6.1 Sol 页面列出的是 HLE-Diamond，属于不同的 1,000 题集合；AA 原始 HLE 方法使用完整 HLE 中的 2,158 道 text-only 题，但没有找到此模型对应的绝对成绩。
- Scale 的原始 HLE 当前榜单未列出 GPT-6.1 Sol。

最近核验时间：2026-11-04T06:26+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 55
- metric: index score
- version: 5.0
- dataset: V5 composite (9 evaluations)
- effort: Max
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 52
- metric: index score
- version: 5.0
- dataset: V5 composite (9 evaluations)
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 50
- metric: index score
- version: 5.0
- dataset: V5 composite (9 evaluations)
- effort: High
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-luna-high](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-luna-high)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Artificial Analysis Intelligence Index
- score: 46
- metric: index score
- version: 5.0
- dataset: V5 composite (9 evaluations)
- effort: Medium
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Artificial Analysis Intelligence Index
- score: 35
- metric: index score
- version: 5.0
- dataset: V5 composite (9 evaluations)
- effort: Low
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GPT-6.1 Sol current model profile](https://artificialanalysis.ai/models/gpt-6-1-sol)
- [Artificial Analysis GPT-6.1 Sol release page](https://artificialanalysis.ai/models/releases/gpt-6-1-sol)
- [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Max comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol)
- [Artificial Analysis Xhigh comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low)
- [Artificial Analysis High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-luna-high)
- [Artificial Analysis Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium)
- [Artificial Analysis Low comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh)

研究备注：
- 五种 effort 的指数分数均有模型专属资料：Max 55、Xhigh 52、High 50、Medium 46、Low 35。比较页把对应指数标记为 v5.0，因此源 TOML 按该精确版本收录。
- 当前 AA 模型页及方法页另将最新指数标记为 v5.0.1。该版本标签与比较页 v5.0 存在不一致；先保留比较页直接支持的 v5.0 分数，并将该项标记为冲突待核实。

尚未解决的问题：
- 需确认这五档分数对应 v5.0 还是 v5.0.1；当前 benchmark 定义为 v5.0。

最近核验时间：2026-11-04T06:26+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GPT-6.1 Sol release article](https://artificialanalysis.ai/articles/gpt-6-1-sol-replaces-gpt-6-sol-after-just-7-days-with-near-astra-intelligence)
- [Artificial Analysis GDPval-AA v2.1 evaluation and leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)

研究备注：
- AA 发布文章只报告 GPT-6.1 Sol 相对 GPT-6 Sol 的 GDPval-AA v2.1 提升 5 分，没有公布绝对 Elo。当前可读 leaderboard 未找到 GPT-6.1 Sol 的行；没有把 Intelligence Index 分数或旧模型分数转用到本项。

尚未解决的问题：
- 需找到准确模型版本的绝对 Elo、effort 和评测条件。

最近核验时间：2026-11-04T06:26+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 63.94
- metric: performance score
- version: 2.2
- dataset: finance, coding, legal, and tax tasks
- source: [https://www.vals.ai/models/openai_gpt-6.1-sol](https://www.vals.ai/models/openai_gpt-6.1-sol)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals GPT-6.1 Sol model profile](https://www.vals.ai/models/openai_gpt-6.1-sol)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 模型页精确报告 63.94% ±1.07；Benchmark 页面标明 Vals Index v2.2 聚合 finance、coding、legal、tax。TOML 保留点估计 63.94。
- 页面更新时间不是评测日期，因此没有写入 date。

最近核验时间：2026-11-04T06:26+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-6.1 Sol current model profile",
          "url": "https://artificialanalysis.ai/models/gpt-6-1-sol"
        },
        {
          "label": "Artificial Analysis GPT-6.1 Sol release page",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-1-sol"
        },
        {
          "label": "Artificial Analysis Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol"
        },
        {
          "label": "Artificial Analysis Xhigh comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low"
        },
        {
          "label": "Artificial Analysis High comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-luna-high"
        },
        {
          "label": "Artificial Analysis Medium comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium"
        },
        {
          "label": "Artificial Analysis Low comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh"
        }
      ],
      "notes": [
        "五种 effort 的指数分数均有模型专属资料：Max 55、Xhigh 52、High 50、Medium 46、Low 35。比较页把对应指数标记为 v5.0，因此源 TOML 按该精确版本收录。",
        "当前 AA 模型页及方法页另将最新指数标记为 v5.0.1。该版本标签与比较页 v5.0 存在不一致；先保留比较页直接支持的 v5.0 分数，并将该项标记为冲突待核实。"
      ],
      "status": "冲突",
      "unresolved": [
        "需确认这五档分数对应 v5.0 还是 v5.0.1；当前 benchmark 定义为 v5.0。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6.1 Sol 发布说明",
          "url": "https://openai.com/index/introducing-gpt-6-1-sol/"
        },
        {
          "label": "Zapier AutomationBench 1.0.6 official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "OpenAI 只报告 medium effort 下相对 GPT-6 Sol 提高 4.8 个百分点及相对 Opus 的差值，没有公布 Sol 的绝对分数。",
        "当前 Zapier 榜单公开展示前十名，GPT-6.1 Sol 未在可读榜单条目中；不以相对差值计算成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实 GPT-6.1 Sol 是否有公开的 AutomationBench 1.0.6 绝对分数及精确 effort。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Surge AI benchmark leaderboard",
          "url": "https://surgehq.ai/benchmarks"
        },
        {
          "label": "Surge AI Chartography benchmark article",
          "url": "https://surgehq.ai/blog/chartography"
        }
      ],
      "notes": [
        "Surge 的 Chartography 榜单可见 GPT-6 Astra Max 等结果；检索到的 GPT-6 Sol Max 条目属于不同模型，没有找到 GPT-6.1 Sol 准确版本成绩。",
        "GPT-6.1 Sol 支持图像输入，因此该 Benchmark 适用；无分数不代表 0。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6.1 Sol 发布说明",
          "url": "https://openai.com/index/introducing-gpt-6-1-sol/"
        },
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 方法说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "OpenAI 只披露相对 GPT-6 Sol 最佳成绩高 6.4 个百分点，没有公布 GPT-6.1 Sol 绝对分数、effort、harness 或评测日期。",
        "研究代理核对的官方榜单显示 113 项任务数据更新时间早于本模型发布日期；不从相对提升反推绝对成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需找到 GPT-6.1 Sol 准确版本的公开绝对成绩及测试条件。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-6.1 Sol release article",
          "url": "https://artificialanalysis.ai/articles/gpt-6-1-sol-replaces-gpt-6-sol-after-just-7-days-with-near-astra-intelligence"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation and leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        }
      ],
      "notes": [
        "AA 发布文章只报告 GPT-6.1 Sol 相对 GPT-6 Sol 的 GDPval-AA v2.1 提升 5 分，没有公布绝对 Elo。当前可读 leaderboard 未找到 GPT-6.1 Sol 的行；没有把 Intelligence Index 分数或旧模型分数转用到本项。"
      ],
      "status": "待核实",
      "unresolved": [
        "需找到准确模型版本的绝对 Elo、effort 和评测条件。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Scale AI Humanity’s Last Exam official leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis GPT-6.1 Sol profile",
          "url": "https://artificialanalysis.ai/models/gpt-6-1-sol"
        },
        {
          "label": "Artificial Analysis HLE and HLE-Diamond methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "仓库定义指原始 2,500 题 HLE。当前 AA GPT-6.1 Sol 页面列出的是 HLE-Diamond，属于不同的 1,000 题集合；AA 原始 HLE 方法使用完整 HLE 中的 2,158 道 text-only 题，但没有找到此模型对应的绝对成绩。",
        "Scale 的原始 HLE 当前榜单未列出 GPT-6.1 Sol。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6.1 Sol 发布说明",
          "url": "https://openai.com/index/introducing-gpt-6-1-sol/"
        },
        {
          "label": "OSWorld official benchmark site",
          "url": "https://os-world.github.io/"
        }
      ],
      "notes": [
        "OpenAI 报告的是 OSWorld 2.0 offline set、partial reward、v2026.08.08、max effort 的相对成绩；仓库目标是 OSWorld 2.1 binary completion rate，不能将该结果映射到 v2.1。",
        "未找到属于 GPT-6.1 Sol 准确版本且匹配 v2.1 目标的公开绝对成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "官方 Full leaderboard 的 GPT-6.1-Sol (mini-swe-agent), xhigh 行为 96.11±1.24%；V2 Full 数据集为 642 tasks。模型 TOML 保留点估计 96.11，原始页面保留不确定度。",
        "没有使用 HARD 子集分数，也没有填写排行榜更新时间作为评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science leaderboard and methodology",
          "url": "https://vals-ai.com/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Intelligence Benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol"
        },
        {
          "label": "Artificial Analysis Xhigh comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low"
        },
        {
          "label": "Artificial Analysis High comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low"
        },
        {
          "label": "Artificial Analysis Medium comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium"
        },
        {
          "label": "Artificial Analysis Low comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh"
        }
      ],
      "notes": [
        "Vals 的官方 leaderboard 明确显示 Mini-SWE-agent 52.86%，70 项任务；其方法为单次运行、pass@1。",
        "Artificial Analysis 的独立评测按 Max/Xhigh/High/Medium/Low 分别为 58/50/46/37/11，使用完整 70 项、mini-swe-agent、三次 pass@1 平均和 1,000 步上限。配置不同的值均保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方榜单（Codex）",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        },
        {
          "label": "Vals Terminal-Bench 4 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals GPT-6.1 Sol model profile",
          "url": "https://www.vals.ai/models/openai_gpt-6.1-sol"
        },
        {
          "label": "Artificial Analysis Intelligence Benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-sol"
        },
        {
          "label": "Artificial Analysis Xhigh comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-sol-low"
        },
        {
          "label": "Artificial Analysis High comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol-low"
        },
        {
          "label": "Artificial Analysis Medium comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium"
        },
        {
          "label": "Artificial Analysis Low comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-xhigh"
        }
      ],
      "notes": [
        "保留了三种公开条件：Terminal-Bench 官方榜 Codex/max 58.2%（来源报告 ±3.1）；Vals mini-swe-agent 55.05%（avg@3，三次完整运行）；Artificial Analysis mini-swe-agent 按 Max/Xhigh/High/Medium/Low 分别为 56/54/52/48/31（各次 pass@1 平均三次，500 步上限）。",
        "不同 harness 或执行配置的成绩分别保留；没有用最高分替代其他结果。Vals 页面报告 ±1.82 标准误，AA 页面以整数百分数展示。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T06:26+08:00",
      "checked_sources": [
        {
          "label": "Vals GPT-6.1 Sol model profile",
          "url": "https://www.vals.ai/models/openai_gpt-6.1-sol"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 模型页精确报告 63.94% ±1.07；Benchmark 页面标明 Vals Index v2.2 聚合 finance、coding、legal、tax。TOML 保留点估计 63.94。",
        "页面更新时间不是评测日期，因此没有写入 date。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T06:26+08:00",
  "model_id": "openai/gpt-6.1-sol",
  "new_records": 20,
  "overall_status": "待复核"
}

-->
