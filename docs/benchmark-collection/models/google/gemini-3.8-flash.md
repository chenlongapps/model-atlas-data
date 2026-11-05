# Gemini 3.8 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.8-flash
- 模型名称：Gemini 3.8 Flash
- 发布日期：2026-09-02
- 最近检查时间：2026-11-04T14:03+08:00
- 整体处理状态：待复核
- 新增成绩数量：11
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：7

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 73.7 (metric=pass@1; version=1.1; variant=high thinking; harness=mini-swe-agent) | [Google Gemini 3.8 Flash 发布与评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-flash), [Google Gemini 3.8 Flash 发布文章](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/), [Datacurve DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T14:03+08:00 |
| swe-bench-pro-v2 | 待核实 | 94.86 (metric=resolve rate; version=V2; dataset=642-task public split; effort=high; variant=reported ±1.46; web tools disabled; network-locked protocol; uncapped cost; 250-turn limit; harness=mini-swe-agent) | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T14:03+08:00 |
| terminal-bench-v4 | 待核实 | 89.4 (metric=pass@1; version=2.1; harness=Terminus 2); 19.1 (metric=pass@1; version=4.0); 19.7 (metric=accuracy; version=4.0; dataset=66 tasks; effort=high; variant=avg@3; reported ±2.31 standard error; no step or cost limit; 8-hour task timeout; harness=Mini-SWE-agent) | [Google Gemini 3.8 Flash evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-8-flash), [Terminal-Bench official site](https://www.tbench.ai/), [Vals Terminal-Bench 4.0 model results](https://www.vals.ai/models/google_gemini-3.8-flash), [Vals Terminal-Bench 4.0 methodology](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T14:03+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 10.0 (metric=share of tasks passed (pass@1); version=0.1.0; dataset=70 tasks; effort=High; variant=average of three repeats per task; harness=mini-swe-agent); 8.57 (metric=accuracy; version=0.1.0; dataset=70 upstream tasks; variant=single run per model; infrastructure or provider errors retried only; harness=Mini-SWE-agent) | [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite), [Artificial Analysis Terminal-Bench-Science 0.1 method](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Vals Terminal-Bench-Science leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-science), [Vals Gemini 3.8 Flash model results](https://www.vals.ai/models/google_gemini-3.8-flash) | 2026-11-04T14:03+08:00 |
| automationbench-v1.0.6 | 已收录 | 29.7 (metric=task_completed_correctly; version=1.0.6; effort=Medium); 29.7 (metric=task_completed_correctly; version=1.0.6; effort=High) | [Zapier Gemini 4 Carbon release report with AutomationBench comparison](https://zapier.com/benchmarks/gemini-carbon-4-report), [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T14:03+08:00 |
| osworld-v2.1 | 未找到 | 59 (metric=partial score; version=2.0; dataset=before 2026-08-08 patch; variant=batched tool calls; best of 3 runs; 500 steps; harness=Gemini CUA) | [Google Gemini 3.8 Flash evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-8-flash), [Official OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T14:03+08:00 |
| chartography | 已收录 | 40.9 (metric=accuracy (mean; Pass@1); dataset=100 expert chart tasks; effort=High reasoning; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge AI Chartography official README](https://github.com/surge-ai/chartography/blob/main/README.md) | 2026-11-04T14:03+08:00 |
| humanitys-last-exam | 已收录 | 48 (metric=accuracy; effort=High) | [Artificial Analysis Gemini 3.8 Flash (High) comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3), [Artificial Analysis Humanity’s Last Exam method](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T14:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 31 (metric=index score; version=5.0.1; effort=high) | [Artificial Analysis Gemini 3.8 Flash model profile](https://artificialanalysis.ai/models/gemini-3-8-flash), [Artificial Analysis Gemini 3.8 Flash comparison showing V5.0.1](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite) | 2026-11-04T14:03+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1545 (metric=Elo; version=2); 1436 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=High; variant=shell and web browsing; blind pairwise comparisons; harness=Stirrup) | [Artificial Analysis Gemini 3.8 Flash (High) comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3), [Artificial Analysis GDPval-AA v2.1 method](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T14:03+08:00 |
| vals-index-v2.2 | 已收录 | 55.95 (metric=performance score; version=2.2; dataset=six private and two public benchmarks; effort=high; variant=reported ±1.14; Google provider; default temperature, top-p, and top-k; 65,536 max output tokens) | [Vals Gemini 3.8 Flash model profile](https://www.vals.ai/models/google_gemini-3.8-flash), [Vals Index v2.2 board and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T14:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 73.7
- metric: pass@1
- version: 1.1
- variant: high thinking
- harness: mini-swe-agent
- source: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Google Gemini 3.8 Flash 发布与评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-flash)
- [Google Gemini 3.8 Flash 发布文章](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- [Datacurve DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 已有 73.7 pass@1、DeepSWE 1.1、mini-swe-agent、高 thinking 记录；Google 方法页确认准确模型及配置，Datacurve 公榜显示的约 74% 是取整值。

最近核验时间：2026-11-04T14:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 94.86
- metric: resolve rate
- version: V2
- dataset: 642-task public split
- effort: high
- variant: reported ±1.46; web tools disabled; network-locked protocol; uncapped cost; 250-turn limit
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Scale V2 公榜列 Gemini 3.8 Flash (mini-swe-agent) high，94.86，旁列 ±1.46；V2 公集为 642 项，关闭 web 工具并使用 locked protocol。

尚未解决的问题：
- 源资料使用版本名 V2 和指标 resolve rate；仓库定义要求 2.0.0 与 task resolution rate。保留来源原写法，不强行改写以匹配定义，故映射待复核。

最近核验时间：2026-11-04T14:03+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 89.4
- metric: pass@1
- version: 2.1
- harness: Terminus 2
- source: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 19.1
- metric: pass@1
- version: 4.0
- source: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 19.7
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- effort: high
- variant: avg@3; reported ±2.31 standard error; no step or cost limit; 8-hour task timeout
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/models/google_gemini-3.8-flash](https://www.vals.ai/models/google_gemini-3.8-flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google Gemini 3.8 Flash evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-8-flash)
- [Terminal-Bench official site](https://www.tbench.ai/)
- [Vals Terminal-Bench 4.0 model results](https://www.vals.ai/models/google_gemini-3.8-flash)
- [Vals Terminal-Bench 4.0 methodology](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 保留 Google 来源的 19.1 pass@1 / v4.0；另记 Vals 独立测得的 19.70 accuracy，Mini-SWE-agent、66 项、avg@3，页面给出 ±2.31 标准误。Artificial Analysis 的比较页仅显示约 20%，与 Vals 结果相同量级，未重复添加取整行。

尚未解决的问题：
- 两个来源的版本写作 4.0，指标分别为 pass@1 与 accuracy；本地定义要求 4.0.0 / task resolution rate。原值保留，精确映射待复核。

最近核验时间：2026-11-04T14:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 10.0
- metric: share of tasks passed (pass@1)
- version: 0.1.0
- dataset: 70 tasks
- effort: High
- variant: average of three repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 8.57
- metric: accuracy
- version: 0.1.0
- dataset: 70 upstream tasks
- variant: single run per model; infrastructure or provider errors retried only
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite)
- [Artificial Analysis Terminal-Bench-Science 0.1 method](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Vals Terminal-Bench-Science leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Vals Gemini 3.8 Flash model results](https://www.vals.ai/models/google_gemini-3.8-flash)

研究备注：
- Artificial Analysis 报 10.0%，70 项、mini-swe-agent、每项三次 pass@1 平均；Vals 报 8.57%，同为上游 v0.1.0 的 70 项和 mini-swe-agent，但其方法为每模型单次运行且仅对基础设施或 provider 错误重试。两种配置分开保留。

尚未解决的问题：
- 来源指标写作 share of tasks passed (pass@1) 和 accuracy；本地定义 metric 为 task resolution rate。精确映射待复核。

最近核验时间：2026-11-04T14:03+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 29.7
- metric: task_completed_correctly
- version: 1.0.6
- effort: Medium
- source: [https://zapier.com/benchmarks/gemini-carbon-4-report](https://zapier.com/benchmarks/gemini-carbon-4-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 29.7
- metric: task_completed_correctly
- version: 1.0.6
- effort: High
- source: [https://zapier.com/benchmarks/gemini-carbon-4-report](https://zapier.com/benchmarks/gemini-carbon-4-report)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier Gemini 4 Carbon release report with AutomationBench comparison](https://zapier.com/benchmarks/gemini-carbon-4-report)
- [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 官方报告的结果表列 Gemini 3.8 Flash Medium 29.7% 与 High 29.7%；指标 task_completed_correctly、版本 1.0.6。报告没有给这两条 Gemini 行独立评测日期或 harness，因此未填。

最近核验时间：2026-11-04T14:03+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 59
- metric: partial score
- version: 2.0
- dataset: before 2026-08-08 patch
- variant: batched tool calls; best of 3 runs; 500 steps
- harness: Gemini CUA
- source: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google Gemini 3.8 Flash evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-8-flash)
- [Official OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 现有 59 是 Google 自测 OSWorld 2.0 partial score，使用 08-08 补丁前数据；OSWorld-V2.1 官方资料未见 Gemini 3.8 Flash 对应成绩。旧版成绩不转换为 2.1。

最近核验时间：2026-11-04T14:03+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 40.9
- metric: accuracy (mean; Pass@1)
- dataset: 100 expert chart tasks
- effort: High reasoning
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge AI Chartography official README](https://github.com/surge-ai/chartography/blob/main/README.md)

研究备注：
- 官方榜列 Gemini 3.8 Flash (High reasoning) 40.9%。README 说明公开集 100 项、accuracy/mean (Pass@1)、榜单配置每题十次并使用 Gemini 3.5 Flash judge；Inspect AI harness。未公布该模型评测日期。

最近核验时间：2026-11-04T14:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 48
- metric: accuracy
- effort: High
- source: [https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Gemini 3.8 Flash (High) comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3)
- [Artificial Analysis Humanity’s Last Exam method](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- AA 历史对比页将 Gemini 3.8 Flash (High) 的 Humanity’s Last Exam 原始项列为 48% accuracy；Google 公布的 54.9% 是 HLE-Verified，不能代替本项。原始页未显示本次确切子集或评测日期，未推定这些字段。

最近核验时间：2026-11-04T14:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 31
- metric: index score
- version: 5.0.1
- effort: high
- source: [https://artificialanalysis.ai/models/gemini-3-8-flash](https://artificialanalysis.ai/models/gemini-3-8-flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Gemini 3.8 Flash model profile](https://artificialanalysis.ai/models/gemini-3-8-flash)
- [Artificial Analysis Gemini 3.8 Flash comparison showing V5.0.1](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite)

研究备注：
- 当前模型页列出 31 index points、版本 v5.0.1；V5.0.1 组件含 HLE-Diamond，不是原始 HLE。

尚未解决的问题：
- 来源版本 v5.0.1 与仓库定义 5.0 不一致，保留来源版本并待复核映射。

最近核验时间：2026-11-04T14:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1545
- metric: Elo
- version: 2
- source: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1436
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: High
- variant: shell and web browsing; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Gemini 3.8 Flash (High) comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3)
- [Artificial Analysis GDPval-AA v2.1 method](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA 历史对比页准确列 v2.1 成绩 1436 Elo；方法为 220 项、44 种职业、9 个行业，Stirrup 提供 shell/web browsing 并以盲测 pairwise comparison 聚合。现有 1545 是 Google 的 GDPval-AA v2，保留但不映射到 v2.1。

最近核验时间：2026-11-04T14:03+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 55.95
- metric: performance score
- version: 2.2
- dataset: six private and two public benchmarks
- effort: high
- variant: reported ±1.14; Google provider; default temperature, top-p, and top-k; 65,536 max output tokens
- source: [https://www.vals.ai/models/google_gemini-3.8-flash](https://www.vals.ai/models/google_gemini-3.8-flash)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Gemini 3.8 Flash model profile](https://www.vals.ai/models/google_gemini-3.8-flash)
- [Vals Index v2.2 board and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 模型页列 Vals Index v2.2 55.95%（页面同时显示 ±1.14），reasoning effort high、Google provider、temperature/top-p/top-k 默认、最大输出 65,536；汇总六项 private 和两项 public benchmarks。排行榜更新时间不视为成绩评测日期。

最近核验时间：2026-11-04T14:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 3.8 Flash model profile",
          "url": "https://artificialanalysis.ai/models/gemini-3-8-flash"
        },
        {
          "label": "Artificial Analysis Gemini 3.8 Flash comparison showing V5.0.1",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite"
        }
      ],
      "notes": [
        "当前模型页列出 31 index points、版本 v5.0.1；V5.0.1 组件含 HLE-Diamond，不是原始 HLE。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源版本 v5.0.1 与仓库定义 5.0 不一致，保留来源版本并待复核映射。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Zapier Gemini 4 Carbon release report with AutomationBench comparison",
          "url": "https://zapier.com/benchmarks/gemini-carbon-4-report"
        },
        {
          "label": "Zapier AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Zapier 官方报告的结果表列 Gemini 3.8 Flash Medium 29.7% 与 High 29.7%；指标 task_completed_correctly、版本 1.0.6。报告没有给这两条 Gemini 行独立评测日期或 harness，因此未填。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge AI Chartography official README",
          "url": "https://github.com/surge-ai/chartography/blob/main/README.md"
        }
      ],
      "notes": [
        "官方榜列 Gemini 3.8 Flash (High reasoning) 40.9%。README 说明公开集 100 项、accuracy/mean (Pass@1)、榜单配置每题十次并使用 Gemini 3.5 Flash judge；Inspect AI harness。未公布该模型评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash 发布与评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-flash"
        },
        {
          "label": "Google Gemini 3.8 Flash 发布文章",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/"
        },
        {
          "label": "Datacurve DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "已有 73.7 pass@1、DeepSWE 1.1、mini-swe-agent、高 thinking 记录；Google 方法页确认准确模型及配置，Datacurve 公榜显示的约 74% 是取整值。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 3.8 Flash (High) comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 method",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA 历史对比页准确列 v2.1 成绩 1436 Elo；方法为 220 项、44 种职业、9 个行业，Stirrup 提供 shell/web browsing 并以盲测 pairwise comparison 聚合。现有 1545 是 Google 的 GDPval-AA v2，保留但不映射到 v2.1。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 3.8 Flash (High) comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-hy3"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam method",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "AA 历史对比页将 Gemini 3.8 Flash (High) 的 Humanity’s Last Exam 原始项列为 48% accuracy；Google 公布的 54.9% 是 HLE-Verified，不能代替本项。原始页未显示本次确切子集或评测日期，未推定这些字段。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-flash"
        },
        {
          "label": "Official OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "现有 59 是 Google 自测 OSWorld 2.0 partial score，使用 08-08 补丁前数据；OSWorld-V2.1 官方资料未见 Gemini 3.8 Flash 对应成绩。旧版成绩不转换为 2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Scale V2 公榜列 Gemini 3.8 Flash (mini-swe-agent) high，94.86，旁列 ±1.46；V2 公集为 642 项，关闭 web 工具并使用 locked protocol。"
      ],
      "status": "待核实",
      "unresolved": [
        "源资料使用版本名 V2 和指标 resolve rate；仓库定义要求 2.0.0 与 task resolution rate。保留来源原写法，不强行改写以匹配定义，故映射待复核。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-5-flash-lite"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 0.1 method",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Vals Gemini 3.8 Flash model results",
          "url": "https://www.vals.ai/models/google_gemini-3.8-flash"
        }
      ],
      "notes": [
        "Artificial Analysis 报 10.0%，70 项、mini-swe-agent、每项三次 pass@1 平均；Vals 报 8.57%，同为上游 v0.1.0 的 70 项和 mini-swe-agent，但其方法为每模型单次运行且仅对基础设施或 provider 错误重试。两种配置分开保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源指标写作 share of tasks passed (pass@1) 和 accuracy；本地定义 metric 为 task resolution rate。精确映射待复核。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-flash"
        },
        {
          "label": "Terminal-Bench official site",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Vals Terminal-Bench 4.0 model results",
          "url": "https://www.vals.ai/models/google_gemini-3.8-flash"
        },
        {
          "label": "Vals Terminal-Bench 4.0 methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "保留 Google 来源的 19.1 pass@1 / v4.0；另记 Vals 独立测得的 19.70 accuracy，Mini-SWE-agent、66 项、avg@3，页面给出 ±2.31 标准误。Artificial Analysis 的比较页仅显示约 20%，与 Vals 结果相同量级，未重复添加取整行。"
      ],
      "status": "待核实",
      "unresolved": [
        "两个来源的版本写作 4.0，指标分别为 pass@1 与 accuracy；本地定义要求 4.0.0 / task resolution rate。原值保留，精确映射待复核。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T14:03+08:00",
      "checked_sources": [
        {
          "label": "Vals Gemini 3.8 Flash model profile",
          "url": "https://www.vals.ai/models/google_gemini-3.8-flash"
        },
        {
          "label": "Vals Index v2.2 board and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "模型页列 Vals Index v2.2 55.95%（页面同时显示 ±1.14），reasoning effort high、Google provider、temperature/top-p/top-k 默认、最大输出 65,536；汇总六项 private 和两项 public benchmarks。排行榜更新时间不视为成绩评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T14:03+08:00",
  "model_id": "google/gemini-3.8-flash",
  "new_records": 11,
  "overall_status": "待复核"
}

-->
