# Qwen3.8 Max Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-max
- 模型名称：Qwen3.8 Max
- 发布日期：2026-08-03
- 最近检查时间：2026-11-04T20:45+08:00
- 整体处理状态：待复核
- 新增成绩数量：5
- 更新成绩数量：1
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：6

## 模型身份与范围说明

- Qwen 官方模型卡的 Benchmark Results 表明确区分 Qwen3.8-Max 与独立的 Qwen3.8-2.4T-A95B 权重，并说明 Max 是带额外功能的官方版本；仅将表中 Qwen3.8-Max 列关联到本模型。
- 当前 API 别名曾迁移到 Qwen3.8 Max 0902；本轮不把 0902 或无法固定快照的别名结果并入 2026-08-03 首发模型。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 56.6 (metric=pass@1; version=1.1; dataset=113 tasks; variant=temperature=1.0; top_p=0.95; context=256K; harness=Claude Code) | [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Qwen 模型卡提交历史](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/commits/main), [Qwen3.8 Max API 版本文档](https://help.aliyun.com/zh/model-studio/qwen3-8-max) | 2026-11-04T20:45+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Scale AI SWE-Bench Pro V2 leaderboard and release notes](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-Bench Pro evaluation method](https://github.com/scaleapi/SWE-bench_Pro-os) | 2026-11-04T20:45+08:00 |
| terminal-bench-v4 | 冲突 | 86.6 (metric=avg@10; version=2.1; variant=5h timeout; harness=Claude Code); 19 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=three repeats; per-task pass@1; averaged result; harness=mini-swe-agent); 34.34 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=single run; per-task pass@1; infrastructure/provider errors retried; 8h task limit; harness=mini-swe-agent) | [Artificial Analysis Qwen3.8 Max comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803), [Artificial Analysis Terminal-Bench 4.0 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Vals AI Qwen 3.8 Max model leaderboard](https://www.vals.ai/models/alibaba_qwen3.8-max), [Vals AI Terminal-Bench 4.0 leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-4), [Terminal-Bench 4.0 official release and method](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T20:45+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 12.86 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; upstream v0.1.0; variant=single run; pass@1; infrastructure/provider errors retried; 8h task limit; harness=mini-swe-agent) | [Vals AI Qwen 3.8 Max model leaderboard](https://www.vals.ai/models/alibaba_qwen3.8-max), [Vals AI Terminal-Bench-Science leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-science), [Terminal-Bench-Science v0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T20:45+08:00 |
| automationbench-v1.0.6 | 待核实 | 27.3 (metric=pass@1; dataset=600 public tasks) | [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository and changelog](https://github.com/zapier/AutomationBench), [AutomationBench 1.0.6 changelog](https://raw.githubusercontent.com/zapier/AutomationBench/main/CHANGELOG.md) | 2026-11-04T20:45+08:00 |
| osworld-v2.1 | 未找到 | — | [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [OSWorld-V2 v2.1 official release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T20:45+08:00 |
| chartography | 已收录 | 29.1 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=xHigh; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge AI Chartography evaluation code and method](https://github.com/surge-ai/chartography), [Surge AI Qwen 3.8 Max results article](https://surgehq.ai/blog/qwen-3-8-max-scores-58-7-on-the-tuesday-work-index) | 2026-11-04T20:45+08:00 |
| humanitys-last-exam | 待核实 | 56.2 (metric=score; variant=with tools); 43.6 (metric=score; variant=without tools) | [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [QwenCloud Qwen3.8 Max release and score table](https://www.qwencloud.com/news/qwen-3-8-max), [Scale AI finalized HLE leaderboard and metric](https://labs.scale.com/leaderboard/humanitys_last_exam), [Humanity’s Last Exam official dataset site](https://lastexam.ai/) | 2026-11-04T20:45+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.8 Max (0803) profile](https://artificialanalysis.ai/models/qwen3-8-max-0803), [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Qwen3.8 Max 0803 comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803), [Artificial Analysis Qwen3.8 Max (0902) profile](https://artificialanalysis.ai/models/qwen3-8-max) | 2026-11-04T20:45+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1604 (metric=Elo rating; version=2.1; dataset=220 tasks; harness=Stirrup) | [Artificial Analysis Qwen3.8 Max comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803), [Artificial Analysis GDPval-AA v2.1 method](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa), [Artificial Analysis GDPval-AA v2.1 benchmark](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T20:45+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2), [Vals AI Qwen 3.8 Max model profile](https://www.vals.ai/models/alibaba_qwen3.8-max), [QwenCloud 0902 endpoint migration notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade) | 2026-11-04T20:45+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 56.6
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- variant: temperature=1.0; top_p=0.95; context=256K
- harness: Claude Code
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Qwen 模型卡提交历史](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/commits/main)
- [Qwen3.8 Max API 版本文档](https://help.aliyun.com/zh/model-studio/qwen3-8-max)

研究备注：
- Qwen 官方卡的 Qwen3.8-Max 列报告 56.6，版本为 DeepSWE 1.1；脚注说明测试了 Claude Code 与 mini-SWE-agent，并称该模型在 Claude Code 下表现最佳。该卡 2026-08-11 已存在，早于 0902 快照。DeepSWE 官方方法将该百分比分数作为单次任务通过率；本记录沿用仓库定义的 pass@1 指标并保留 Claude Code harness。
- Datacurve 2026-09-22 的 leaderboard 另列 qwen3.8-max[xhigh] 57%±3；Qwen endpoint 后来切换到 0902，但榜单未固定快照。该观测不映射到本模型，也不覆盖首发卡中的 56.6。

最近核验时间：2026-11-04T20:45+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Scale AI SWE-Bench Pro V2 leaderboard and release notes](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-Bench Pro evaluation method](https://github.com/scaleapi/SWE-bench_Pro-os)

研究备注：
- 本地 Qwen 卡中的 SWE-bench Pro 67.7 使用 Qwen 修订任务集，但没有标注 SWE-Bench Pro V2.0.0。Scale 于 2026-09-22 发布的 V2.0.0 公共集为 642 题，和旧版 731 题不同；官方 V2 榜单未找到 Qwen3.8-Max 的精确条目。保留旧记录，不映射到 V2。

尚未解决的问题：
- 已有的 67.7 未注明目标 V2.0.0 版本或对应 public/held-out 子集，无法确认与本 Benchmark 定义相同。

最近核验时间：2026-11-04T20:45+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 86.6
- metric: avg@10
- version: 2.1
- variant: 5h timeout
- harness: Claude Code
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 19
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: three repeats; per-task pass@1; averaged result
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 34.34
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: single run; per-task pass@1; infrastructure/provider errors retried; 8h task limit
- harness: mini-swe-agent
- source: [https://www.vals.ai/models/alibaba_qwen3.8-max](https://www.vals.ai/models/alibaba_qwen3.8-max)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.8 Max comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803)
- [Artificial Analysis Terminal-Bench 4.0 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Vals AI Qwen 3.8 Max model leaderboard](https://www.vals.ai/models/alibaba_qwen3.8-max)
- [Vals AI Terminal-Bench 4.0 leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Terminal-Bench 4.0 official release and method](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 首发 Qwen3.8 Max 的源记录中保留两条独立结果：Artificial Analysis 报 19%，其方法使用 66 项任务、mini-SWE-agent、每题 pass@1 并运行三次；Vals AI 报 34.34%，方法为 66 项任务、mini-SWE-agent、每模型单次 pass@1 运行，基础设施或供应商错误会重试，每项任务最长 8 小时。两来源的运行条件不同，因此没有择高或合并。
- 本地原有 86.6 是 Terminal-Bench 2.1（Claude Code、avg@10、5 小时上限），不能映射到 v4。

尚未解决的问题：
- AA 的 19% 与 Vals 的 34.34% 相差较大；来源给出的重试和重复次数不同，但不足以解释差值。保留为分开的已核实运行配置，待将来取得可比运行标识后复查。

最近核验时间：2026-11-04T20:45+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 12.86
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks; upstream v0.1.0
- variant: single run; pass@1; infrastructure/provider errors retried; 8h task limit
- harness: mini-swe-agent
- source: [https://www.vals.ai/models/alibaba_qwen3.8-max](https://www.vals.ai/models/alibaba_qwen3.8-max)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Qwen 3.8 Max model leaderboard](https://www.vals.ai/models/alibaba_qwen3.8-max)
- [Vals AI Terminal-Bench-Science leaderboard and method](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Terminal-Bench-Science v0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Vals model page identifies Qwen 3.8 Max with release date 2026-08-03 and reports 12.86% on Terminal-Bench-Science. Vals methodology specifies upstream v0.1.0, 70 tasks, mini-SWE-agent, single pass@1 run per model, with retries only for infrastructure/provider errors and an 8-hour task limit. The page update date is not a model evaluation date and was not written to the TOML date field.
- The 11.9% Artificial Analysis entry belongs to Qwen3.8 Max (0902), not this model.

最近核验时间：2026-11-04T20:45+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 27.3
- metric: pass@1
- dataset: 600 public tasks
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository and changelog](https://github.com/zapier/AutomationBench)
- [AutomationBench 1.0.6 changelog](https://raw.githubusercontent.com/zapier/AutomationBench/main/CHANGELOG.md)

研究备注：
- 本地 Qwen 卡报告 AutomationBench 27.3 pass@1、600 个公开任务；未给出 v1.0.6、effort、harness 或评测日期。Zapier v1.0.6 的官方排行榜使用独立 held-out private task set，版本更新也调整任务。不能把公开集分数当作 v1.0.6 官方榜结果。

尚未解决的问题：
- 已存在的 27.3 是 600-task public subset，但目标定义是 v1.0.6 held-out private leaderboard；来源未给版本及其与目标任务集的对应关系。

最近核验时间：2026-11-04T20:45+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [OSWorld-V2 v2.1 official release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 未找到 Qwen3.8 Max 的 OSWorld v2.1 精确成绩。Qwen 官方卡列有 OSWorld 2.0 binary/partial 和 OSWorld-Verified 分数，但版本与评测定义不同，不映射到 v2.1。

最近核验时间：2026-11-04T20:45+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 29.1
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: xHigh
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge AI Chartography evaluation code and method](https://github.com/surge-ai/chartography)
- [Surge AI Qwen 3.8 Max results article](https://surgehq.ai/blog/qwen-3-8-max-scores-58-7-on-the-tuesday-work-index)

研究备注：
- Surge AI 官方榜单和其 Qwen 3.8 Max 分析文章都报告 29.1%，effort 为 xHigh。Chartography 仓库将 leaderboard 指标定义为 accuracy/mean (Pass@1)，完整集合为 100 tasks，Inspect AI harness，每题 10 runs，Gemini 3.5 Flash judge。来源没有成绩评测日期，因此未填 date。

最近核验时间：2026-11-04T20:45+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 56.2
- metric: score
- variant: with tools
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 43.6
- metric: score
- variant: without tools
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen 官方 Qwen3.8-Max benchmark card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [QwenCloud Qwen3.8 Max release and score table](https://www.qwencloud.com/news/qwen-3-8-max)
- [Scale AI finalized HLE leaderboard and metric](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Humanity’s Last Exam official dataset site](https://lastexam.ai/)

研究备注：
- 本地 TOML 保留 Qwen 官方卡 Qwen3.8-Max 列中的 HLE 56.2（with tools）和 43.6（without tools）。目标定义对应原始 finalized HLE；官方定义使用 accuracy，但 Qwen 卡未说明它采用哪个 HLE 数据集版本/子集，也仅把值标为 score。当前两条记录因此未映射到目标定义，暂不改指标、版本或数据集字段。

尚未解决的问题：
- 需确认两条 Qwen 卡成绩使用原始 2,500 题 HLE，而非其他 HLE 变体/子集；来源也未明确 metric accuracy。

最近核验时间：2026-11-04T20:45+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.8 Max (0803) profile](https://artificialanalysis.ai/models/qwen3-8-max-0803)
- [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Qwen3.8 Max 0803 comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803)
- [Artificial Analysis Qwen3.8 Max (0902) profile](https://artificialanalysis.ai/models/qwen3-8-max)

研究备注：
- 未找到首发 Qwen3.8 Max 的 v5.0.1 综合指数成绩；其 v5 页面显示 N/A。该模型旧 profile 中的 40 属于 v4.3.2，不能映射到 v5。34 分属于 0902 新快照，也不用于首发版。

最近核验时间：2026-11-04T20:45+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1604
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.8 Max comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803)
- [Artificial Analysis GDPval-AA v2.1 method](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)
- [Artificial Analysis GDPval-AA v2.1 benchmark](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Artificial Analysis 对 exact Qwen3.8 Max 列出 1604 Elo，并明确标注 GDPval-AA v2.1。官方方法使用 OpenAI GDPval 的 220 个任务和 Stirrup agent harness；未披露该结果的 reasoning effort、variant 或评测日期，因此相应字段保持省略。

最近核验时间：2026-11-04T20:45+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)
- [Vals AI Qwen 3.8 Max model profile](https://www.vals.ai/models/alibaba_qwen3.8-max)
- [QwenCloud 0902 endpoint migration notice](https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade)

研究备注：
- Vals Index v2.2 榜列出的 59.05% 对应 Qwen3.8 Max 0902；原版 Max 在旧 Vals Index v2 有 51.84%。原版模型页另显示未标指数版本/日期的 55.30%，不能确认它属于 v2.2，未写入。Qwen 官方迁移公告也确认 qwen3.8-max endpoint 后续切换到 0902。

尚未解决的问题：
- 未找到带有 v2.2 版本标识且固定为首发 2026-08-03 Qwen3.8 Max 的成绩；模型页 55.30% 没有说明指数版本。

最近核验时间：2026-11-04T20:45+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8 Max (0803) profile",
          "url": "https://artificialanalysis.ai/models/qwen3-8-max-0803"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Qwen3.8 Max 0803 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803"
        },
        {
          "label": "Artificial Analysis Qwen3.8 Max (0902) profile",
          "url": "https://artificialanalysis.ai/models/qwen3-8-max"
        }
      ],
      "notes": [
        "未找到首发 Qwen3.8 Max 的 v5.0.1 综合指数成绩；其 v5 页面显示 N/A。该模型旧 profile 中的 40 属于 v4.3.2，不能映射到 v5。34 分属于 0902 新快照，也不用于首发版。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.8-Max benchmark card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository and changelog",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "AutomationBench 1.0.6 changelog",
          "url": "https://raw.githubusercontent.com/zapier/AutomationBench/main/CHANGELOG.md"
        }
      ],
      "notes": [
        "本地 Qwen 卡报告 AutomationBench 27.3 pass@1、600 个公开任务；未给出 v1.0.6、effort、harness 或评测日期。Zapier v1.0.6 的官方排行榜使用独立 held-out private task set，版本更新也调整任务。不能把公开集分数当作 v1.0.6 官方榜结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "已存在的 27.3 是 600-task public subset，但目标定义是 v1.0.6 held-out private leaderboard；来源未给版本及其与目标任务集的对应关系。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge AI Chartography evaluation code and method",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Surge AI Qwen 3.8 Max results article",
          "url": "https://surgehq.ai/blog/qwen-3-8-max-scores-58-7-on-the-tuesday-work-index"
        }
      ],
      "notes": [
        "Surge AI 官方榜单和其 Qwen 3.8 Max 分析文章都报告 29.1%，effort 为 xHigh。Chartography 仓库将 leaderboard 指标定义为 accuracy/mean (Pass@1)，完整集合为 100 tasks，Inspect AI harness，每题 10 runs，Gemini 3.5 Flash judge。来源没有成绩评测日期，因此未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.8-Max benchmark card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Qwen 模型卡提交历史",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/commits/main"
        },
        {
          "label": "Qwen3.8 Max API 版本文档",
          "url": "https://help.aliyun.com/zh/model-studio/qwen3-8-max"
        }
      ],
      "notes": [
        "Qwen 官方卡的 Qwen3.8-Max 列报告 56.6，版本为 DeepSWE 1.1；脚注说明测试了 Claude Code 与 mini-SWE-agent，并称该模型在 Claude Code 下表现最佳。该卡 2026-08-11 已存在，早于 0902 快照。DeepSWE 官方方法将该百分比分数作为单次任务通过率；本记录沿用仓库定义的 pass@1 指标并保留 Claude Code harness。",
        "Datacurve 2026-09-22 的 leaderboard 另列 qwen3.8-max[xhigh] 57%±3；Qwen endpoint 后来切换到 0902，但榜单未固定快照。该观测不映射到本模型，也不覆盖首发卡中的 56.6。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8 Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-qwen3-8-max-0803"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 method",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 benchmark",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Artificial Analysis 对 exact Qwen3.8 Max 列出 1604 Elo，并明确标注 GDPval-AA v2.1。官方方法使用 OpenAI GDPval 的 220 个任务和 Stirrup agent harness；未披露该结果的 reasoning effort、variant 或评测日期，因此相应字段保持省略。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.8-Max benchmark card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "QwenCloud Qwen3.8 Max release and score table",
          "url": "https://www.qwencloud.com/news/qwen-3-8-max"
        },
        {
          "label": "Scale AI finalized HLE leaderboard and metric",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Humanity’s Last Exam official dataset site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "本地 TOML 保留 Qwen 官方卡 Qwen3.8-Max 列中的 HLE 56.2（with tools）和 43.6（without tools）。目标定义对应原始 finalized HLE；官方定义使用 accuracy，但 Qwen 卡未说明它采用哪个 HLE 数据集版本/子集，也仅把值标为 score。当前两条记录因此未映射到目标定义，暂不改指标、版本或数据集字段。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认两条 Qwen 卡成绩使用原始 2,500 题 HLE，而非其他 HLE 变体/子集；来源也未明确 metric accuracy。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.8-Max benchmark card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "OSWorld-V2 v2.1 official release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "未找到 Qwen3.8 Max 的 OSWorld v2.1 精确成绩。Qwen 官方卡列有 OSWorld 2.0 binary/partial 和 OSWorld-Verified 分数，但版本与评测定义不同，不映射到 v2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.8-Max benchmark card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Scale AI SWE-Bench Pro V2 leaderboard and release notes",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-Bench Pro evaluation method",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os"
        }
      ],
      "notes": [
        "本地 Qwen 卡中的 SWE-bench Pro 67.7 使用 Qwen 修订任务集，但没有标注 SWE-Bench Pro V2.0.0。Scale 于 2026-09-22 发布的 V2.0.0 公共集为 642 题，和旧版 731 题不同；官方 V2 榜单未找到 Qwen3.8-Max 的精确条目。保留旧记录，不映射到 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "已有的 67.7 未注明目标 V2.0.0 版本或对应 public/held-out 子集，无法确认与本 Benchmark 定义相同。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Qwen 3.8 Max model leaderboard",
          "url": "https://www.vals.ai/models/alibaba_qwen3.8-max"
        },
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science v0.1 official announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Vals model page identifies Qwen 3.8 Max with release date 2026-08-03 and reports 12.86% on Terminal-Bench-Science. Vals methodology specifies upstream v0.1.0, 70 tasks, mini-SWE-agent, single pass@1 run per model, with retries only for infrastructure/provider errors and an 8-hour task limit. The page update date is not a model evaluation date and was not written to the TOML date field.",
        "The 11.9% Artificial Analysis entry belongs to Qwen3.8 Max (0902), not this model."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8 Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-8-max-0803"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 method",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Vals AI Qwen 3.8 Max model leaderboard",
          "url": "https://www.vals.ai/models/alibaba_qwen3.8-max"
        },
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Terminal-Bench 4.0 official release and method",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "首发 Qwen3.8 Max 的源记录中保留两条独立结果：Artificial Analysis 报 19%，其方法使用 66 项任务、mini-SWE-agent、每题 pass@1 并运行三次；Vals AI 报 34.34%，方法为 66 项任务、mini-SWE-agent、每模型单次 pass@1 运行，基础设施或供应商错误会重试，每项任务最长 8 小时。两来源的运行条件不同，因此没有择高或合并。",
        "本地原有 86.6 是 Terminal-Bench 2.1（Claude Code、avg@10、5 小时上限），不能映射到 v4。"
      ],
      "status": "冲突",
      "unresolved": [
        "AA 的 19% 与 Vals 的 34.34% 相差较大；来源给出的重试和重复次数不同，但不足以解释差值。保留为分开的已核实运行配置，待将来取得可比运行标识后复查。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T20:45+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        },
        {
          "label": "Vals AI Qwen 3.8 Max model profile",
          "url": "https://www.vals.ai/models/alibaba_qwen3.8-max"
        },
        {
          "label": "QwenCloud 0902 endpoint migration notice",
          "url": "https://docs.qwencloud.com/changelog/model-updates/qwen3.8-max-upgrade"
        }
      ],
      "notes": [
        "Vals Index v2.2 榜列出的 59.05% 对应 Qwen3.8 Max 0902；原版 Max 在旧 Vals Index v2 有 51.84%。原版模型页另显示未标指数版本/日期的 55.30%，不能确认它属于 v2.2，未写入。Qwen 官方迁移公告也确认 qwen3.8-max endpoint 后续切换到 0902。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到带有 v2.2 版本标识且固定为首发 2026-08-03 Qwen3.8 Max 的成绩；模型页 55.30% 没有说明指数版本。"
      ]
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T20:45+08:00",
  "model_id": "alibaba/qwen3.8-max",
  "model_notes": [
    "Qwen 官方模型卡的 Benchmark Results 表明确区分 Qwen3.8-Max 与独立的 Qwen3.8-2.4T-A95B 权重，并说明 Max 是带额外功能的官方版本；仅将表中 Qwen3.8-Max 列关联到本模型。",
    "当前 API 别名曾迁移到 Qwen3.8 Max 0902；本轮不把 0902 或无法固定快照的别名结果并入 2026-08-03 首发模型。"
  ],
  "new_records": 5,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
