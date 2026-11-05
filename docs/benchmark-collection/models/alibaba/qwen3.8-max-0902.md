# Qwen3.8 Max 0902 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-max-0902
- 模型名称：Qwen3.8 Max 0902
- 发布日期：2026-09-02
- 最近检查时间：2026-11-04T13:46+08:00
- 整体处理状态：待复核
- 新增成绩数量：7
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：3

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [Qwen earlier Qwen3.8 Max release table](https://qwen.ai/blog?id=qwen3.8), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE leaderboard changelog](https://deepswe.datacurve.ai/changelog) | 2026-11-04T13:46+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [Qwen earlier Qwen3.8 Max release table](https://qwen.ai/blog?id=qwen3.8), [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale AI SWE-bench Pro V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2) | 2026-11-04T13:46+08:00 |
| terminal-bench-v4 | 待核实 | 39 (metric=share of tasks passed (pass@1); version=4.0.0; dataset=Full (66 tasks); variant=Mean of three pass@1 runs; 500 agent-step limit; upstream task timeouts and sandbox resources; harness=mini-swe-agent); 38.89 (metric=accuracy; version=4.0.0; dataset=Full (66 tasks); variant=avg@3 (mean of three pass@1 runs); 8-hour task limit; no step or cost limit; harness=Mini-SWE-agent) | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4), [Artificial Analysis exact Qwen3.8 Max 0902 comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803), [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T13:46+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 12 (metric=share of tasks passed (pass@1); version=0.1.0; dataset=Full (70 tasks); variant=Mean of three pass@1 runs; 1,000 agent-step limit; 30-second timeout per shell command; upstream task timeouts and sandbox resources; harness=mini-swe-agent) | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [Artificial Analysis exact Qwen3.8 Max 0902 comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803), [Artificial Analysis Terminal-Bench-Science evaluation and scoring](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science implementation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Vals AI Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T13:46+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [CellCog transcription of Qwen 0902 benchmark table (secondary source)](https://cellcog.ai/blog/qwen3-8-max-0902/), [Zapier AutomationBench official leaderboard and protocol](https://zapier.com/benchmarks), [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T13:46+08:00 |
| osworld-v2.1 | 未找到 | — | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-04T13:46+08:00 |
| chartography | 待核实 | — | [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902), [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade), [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge AI Qwen 3.8 Max benchmark article](https://surgehq.ai/blog/qwen-3-8-max-scores-58-7-on-the-tuesday-work-index), [Surge AI Chartography protocol and repository](https://github.com/surge-ai/chartography) | 2026-11-04T13:46+08:00 |
| humanitys-last-exam | 已收录 | 43 (metric=accuracy) | [Artificial Analysis historical Qwen 0902 comparison (Index v4.3.2)](https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max), [Artificial Analysis Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T13:46+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 34 (metric=index score; version=5.0.1; variant=Reasoning version) | [Artificial Analysis exact Qwen3.8 Max 0902 model profile](https://artificialanalysis.ai/models/qwen3-8-max), [Artificial Analysis Index version and evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T13:46+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1668 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; harness=Stirrup) | [Artificial Analysis historical Qwen 0902 comparison (Index v4.3.2)](https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max), [Artificial Analysis GDPval-AA v2.1 evaluation and current leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T13:46+08:00 |
| vals-index-v2.2 | 已收录 | 59.05 (metric=performance score; version=2.2; dataset=Six private and two public benchmarks; variant=Default provider: Alibaba; temperature=0.7; top-p/top-k default; max output 128000) | [Vals AI exact Qwen 3.8 Max 0902 model profile](https://www.vals.ai/models/alibaba_qwen3.8-max-0902), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T13:46+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [Qwen earlier Qwen3.8 Max release table](https://qwen.ai/blog?id=qwen3.8)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE leaderboard changelog](https://deepswe.datacurve.ai/changelog)

研究备注：
- 未找到可确认属于 0902 快照的成绩。Qwen 早期发布表中的 56.6 属于之前的 Qwen3.8 Max；Datacurve 当前 qwen3.8-max[xhigh] 行的 57% 在 2026-08-04 加入，均早于 0902 快照。未将其迁移到本模型。

最近核验时间：2026-11-04T13:46+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [Qwen earlier Qwen3.8 Max release table](https://qwen.ai/blog?id=qwen3.8)
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale AI SWE-bench Pro V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2)

研究备注：
- 未找到 0902 快照在 SWE-bench Pro V2 上的成绩。Qwen 早期发布表中的 67.7 未标为 V2 且早于 0902；V2 于 2026-09-22 发布，不能据此反推 0902 使用了 V2。

最近核验时间：2026-11-04T13:46+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 39
- metric: share of tasks passed (pass@1)
- version: 4.0.0
- dataset: Full (66 tasks)
- variant: Mean of three pass@1 runs; 500 agent-step limit; upstream task timeouts and sandbox resources
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 38.89
- metric: accuracy
- version: 4.0.0
- dataset: Full (66 tasks)
- variant: avg@3 (mean of three pass@1 runs); 8-hour task limit; no step or cost limit
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Artificial Analysis exact Qwen3.8 Max 0902 comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803)
- [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- TOML 保留了两种独立配置：Vals 报告 38.89% accuracy（Mini-SWE-agent，66 项，avg@3，8 小时且无 step/cost 限制）；Artificial Analysis 报告 39%（原页精度，Mini-SWE-agent，66 项，三次 pass@1 平均，500-step 上限）。不合并分数，也不补评测日期。两来源指标分别为 accuracy 与 share of tasks passed (pass@1)，本地定义使用 task resolution rate。

尚未解决的问题：
- 来源指标与本地 Terminal-Bench 定义指标 task resolution rate 不同；保留来源原始指标，待核实映射。

最近核验时间：2026-11-04T13:46+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 12
- metric: share of tasks passed (pass@1)
- version: 0.1.0
- dataset: Full (70 tasks)
- variant: Mean of three pass@1 runs; 1,000 agent-step limit; 30-second timeout per shell command; upstream task timeouts and sandbox resources
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [Artificial Analysis exact Qwen3.8 Max 0902 comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803)
- [Artificial Analysis Terminal-Bench-Science evaluation and scoring](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science implementation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Vals AI Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Artificial Analysis 对明确标作 Qwen3.8 Max (0902) 的成绩原页显示 12%；只记录公布的整数精度，不采用二手资料的 11.9%。该评测使用 0.1.0 全部 70 项、mini-swe-agent、三次 pass@1 平均、1,000-step 上限及每条 shell 命令 30 秒上限。Vals 的 12.86% 行只标 Qwen 3.8 Max，未确认是 0902，未录入。

尚未解决的问题：
- 来源指标 share of tasks passed (pass@1) 与本地定义 task resolution rate 不同；保留来源原始指标，待核实映射。

最近核验时间：2026-11-04T13:46+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [CellCog transcription of Qwen 0902 benchmark table (secondary source)](https://cellcog.ai/blog/qwen3-8-max-0902/)
- [Zapier AutomationBench official leaderboard and protocol](https://zapier.com/benchmarks)
- [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- 二手转录表给出 AutomationBench v1.0.6 候选分数 50.8%，但无法从可访问的一手来源独立核实该行及测试条件，官方 Zapier 排行页未显示 Qwen 0902。未写入 TOML；也未混用 Artificial Analysis AutomationBench-AA 的 56%。

尚未解决的问题：
- 候选 50.8% 只有二手转录支持；需取得 Qwen 原始发布表或 Zapier 对应结果及测试条件后再考虑录入。

最近核验时间：2026-11-04T13:46+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 未在 OSWorld V2 官方仓库及 2.1 评测指南中找到 qwen3.8-max-0902 的成绩。旧版 Qwen3.8 Max 的 OSWorld 2.0 与 OSWorld-Verified 数值不属于此快照或 v2.1，未沿用。

最近核验时间：2026-11-04T13:46+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Alibaba QwenCloud exact Qwen3.8-Max-0902 model page](https://www.qwencloud.com/models/qwen3.8-max-0902)
- [Alibaba Cloud Qwen3.8 Max snapshot and alias update notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge AI Qwen 3.8 Max benchmark article](https://surgehq.ai/blog/qwen-3-8-max-scores-58-7-on-the-tuesday-work-index)
- [Surge AI Chartography protocol and repository](https://github.com/surge-ai/chartography)

研究备注：
- Surge 官方榜单/博客列出 Qwen 3.8 Max (xHigh reasoning) 29.1%，但未指明 0902 快照、API ID 或评测日期。QwenCloud 说明常规 alias 于 2026-09-05 转到 0902，但 Surge 未注明调用 alias 或测评日期，不能据此推定结果版本。未写入 TOML。

尚未解决的问题：
- 候选 29.1% 的精确模型快照和评测时间未披露，待复核是否属于 0902。

最近核验时间：2026-11-04T13:46+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 43
- metric: accuracy
- source: [https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max](https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis historical Qwen 0902 comparison (Index v4.3.2)](https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max)
- [Artificial Analysis Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis 历史对照页对确切模型 Qwen3.8 Max (0902) 报告原始 Humanity’s Last Exam 43% accuracy；该页标注 HLE，不是 HLE-Diamond。该次记录未公布评测日期、推理档位、工具设置或数据集子集，故未补写这些条件。

最近核验时间：2026-11-04T13:46+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 34
- metric: index score
- version: 5.0.1
- variant: Reasoning version
- source: [https://artificialanalysis.ai/models/qwen3-8-max](https://artificialanalysis.ai/models/qwen3-8-max)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis exact Qwen3.8 Max 0902 model profile](https://artificialanalysis.ai/models/qwen3-8-max)
- [Artificial Analysis Index version and evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 对 exact 0902 reasoning version 报告 34 index points，当前页面标明 Index v5.0.1。TOML 保留来源版本 5.0.1；本地 Benchmark 定义版本是 5.0，因此映射暂不计入覆盖率。未使用该模型在旧版 v4.3.2 的 45 分。

尚未解决的问题：
- 来源版本 v5.0.1 与本地定义版本 5.0 不完全相同；保留来源版本和分数，待确认是否调整 Benchmark 定义映射。

最近核验时间：2026-11-04T13:46+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1668
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max](https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis historical Qwen 0902 comparison (Index v4.3.2)](https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max)
- [Artificial Analysis GDPval-AA v2.1 evaluation and current leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Artificial Analysis 历史 v4.3.2 对照页对确切模型报告 GDPval-AA v2.1 为 1668 Elo。当前独立 v2.1 排行页未列出该模型，因此保留有原始页面支持的历史记录并标为待复核；没有用搜索摘要中的其他候选分数，也没有把页面更新时间填为评测日期。

尚未解决的问题：
- 当前 GDPval-AA v2.1 独立榜单未显示该模型；需确认 1668 是否仍是有效的历史成绩或已被修订/撤下。

最近核验时间：2026-11-04T13:46+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 59.05
- metric: performance score
- version: 2.2
- dataset: Six private and two public benchmarks
- variant: Default provider: Alibaba; temperature=0.7; top-p/top-k default; max output 128000
- source: [https://www.vals.ai/models/alibaba_qwen3.8-max-0902](https://www.vals.ai/models/alibaba_qwen3.8-max-0902)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI exact Qwen 3.8 Max 0902 model profile](https://www.vals.ai/models/alibaba_qwen3.8-max-0902)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals exact-model page reports 59.05% ±1.08 SE. The page shows Alibaba as the default provider, temperature 0.7, default top-p/top-k and max output 128,000; it does not publish a specific evaluation date or reasoning effort. The leaderboard update date was not used as the evaluation date.

最近核验时间：2026-11-04T13:46+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact Qwen3.8 Max 0902 model profile",
          "url": "https://artificialanalysis.ai/models/qwen3-8-max"
        },
        {
          "label": "Artificial Analysis Index version and evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 对 exact 0902 reasoning version 报告 34 index points，当前页面标明 Index v5.0.1。TOML 保留来源版本 5.0.1；本地 Benchmark 定义版本是 5.0，因此映射暂不计入覆盖率。未使用该模型在旧版 v4.3.2 的 45 分。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源版本 v5.0.1 与本地定义版本 5.0 不完全相同；保留来源版本和分数，待确认是否调整 Benchmark 定义映射。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "CellCog transcription of Qwen 0902 benchmark table (secondary source)",
          "url": "https://cellcog.ai/blog/qwen3-8-max-0902/"
        },
        {
          "label": "Zapier AutomationBench official leaderboard and protocol",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "二手转录表给出 AutomationBench v1.0.6 候选分数 50.8%，但无法从可访问的一手来源独立核实该行及测试条件，官方 Zapier 排行页未显示 Qwen 0902。未写入 TOML；也未混用 Artificial Analysis AutomationBench-AA 的 56%。"
      ],
      "status": "待核实",
      "unresolved": [
        "候选 50.8% 只有二手转录支持；需取得 Qwen 原始发布表或 Zapier 对应结果及测试条件后再考虑录入。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge AI Qwen 3.8 Max benchmark article",
          "url": "https://surgehq.ai/blog/qwen-3-8-max-scores-58-7-on-the-tuesday-work-index"
        },
        {
          "label": "Surge AI Chartography protocol and repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 官方榜单/博客列出 Qwen 3.8 Max (xHigh reasoning) 29.1%，但未指明 0902 快照、API ID 或评测日期。QwenCloud 说明常规 alias 于 2026-09-05 转到 0902，但 Surge 未注明调用 alias 或测评日期，不能据此推定结果版本。未写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "候选 29.1% 的精确模型快照和评测时间未披露，待复核是否属于 0902。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "Qwen earlier Qwen3.8 Max release table",
          "url": "https://qwen.ai/blog?id=qwen3.8"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE leaderboard changelog",
          "url": "https://deepswe.datacurve.ai/changelog"
        }
      ],
      "notes": [
        "未找到可确认属于 0902 快照的成绩。Qwen 早期发布表中的 56.6 属于之前的 Qwen3.8 Max；Datacurve 当前 qwen3.8-max[xhigh] 行的 57% 在 2026-08-04 加入，均早于 0902 快照。未将其迁移到本模型。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis historical Qwen 0902 comparison (Index v4.3.2)",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation and current leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Artificial Analysis 历史 v4.3.2 对照页对确切模型报告 GDPval-AA v2.1 为 1668 Elo。当前独立 v2.1 排行页未列出该模型，因此保留有原始页面支持的历史记录并标为待复核；没有用搜索摘要中的其他候选分数，也没有把页面更新时间填为评测日期。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前 GDPval-AA v2.1 独立榜单未显示该模型；需确认 1668 是否仍是有效的历史成绩或已被修订/撤下。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis historical Qwen 0902 comparison (Index v4.3.2)",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-6-xhigh-vs-qwen3-8-max"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis 历史对照页对确切模型 Qwen3.8 Max (0902) 报告原始 Humanity’s Last Exam 43% accuracy；该页标注 HLE，不是 HLE-Diamond。该次记录未公布评测日期、推理档位、工具设置或数据集子集，故未补写这些条件。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "未在 OSWorld V2 官方仓库及 2.1 评测指南中找到 qwen3.8-max-0902 的成绩。旧版 Qwen3.8 Max 的 OSWorld 2.0 与 OSWorld-Verified 数值不属于此快照或 v2.1，未沿用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "Qwen earlier Qwen3.8 Max release table",
          "url": "https://qwen.ai/blog?id=qwen3.8"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 release and protocol",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        }
      ],
      "notes": [
        "未找到 0902 快照在 SWE-bench Pro V2 上的成绩。Qwen 早期发布表中的 67.7 未标为 V2 且早于 0902；V2 于 2026-09-22 发布，不能据此反推 0902 使用了 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "Artificial Analysis exact Qwen3.8 Max 0902 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science evaluation and scoring",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science implementation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Vals AI Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Artificial Analysis 对明确标作 Qwen3.8 Max (0902) 的成绩原页显示 12%；只记录公布的整数精度，不采用二手资料的 11.9%。该评测使用 0.1.0 全部 70 项、mini-swe-agent、三次 pass@1 平均、1,000-step 上限及每条 shell 命令 30 秒上限。Vals 的 12.86% 行只标 Qwen 3.8 Max，未确认是 0902，未录入。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源指标 share of tasks passed (pass@1) 与本地定义 task resolution rate 不同；保留来源原始指标，待核实映射。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Alibaba QwenCloud exact Qwen3.8-Max-0902 model page",
          "url": "https://www.qwencloud.com/models/qwen3.8-max-0902"
        },
        {
          "label": "Alibaba Cloud Qwen3.8 Max snapshot and alias update notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        },
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis exact Qwen3.8 Max 0902 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "TOML 保留了两种独立配置：Vals 报告 38.89% accuracy（Mini-SWE-agent，66 项，avg@3，8 小时且无 step/cost 限制）；Artificial Analysis 报告 39%（原页精度，Mini-SWE-agent，66 项，三次 pass@1 平均，500-step 上限）。不合并分数，也不补评测日期。两来源指标分别为 accuracy 与 share of tasks passed (pass@1)，本地定义使用 task resolution rate。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源指标与本地 Terminal-Bench 定义指标 task resolution rate 不同；保留来源原始指标，待核实映射。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T13:46+08:00",
      "checked_sources": [
        {
          "label": "Vals AI exact Qwen 3.8 Max 0902 model profile",
          "url": "https://www.vals.ai/models/alibaba_qwen3.8-max-0902"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals exact-model page reports 59.05% ±1.08 SE. The page shows Alibaba as the default provider, temperature 0.7, default top-p/top-k and max output 128,000; it does not publish a specific evaluation date or reasoning effort. The leaderboard update date was not used as the evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T13:46+08:00",
  "model_id": "alibaba/qwen3.8-max-0902",
  "new_records": 7,
  "overall_status": "待复核"
}

-->
