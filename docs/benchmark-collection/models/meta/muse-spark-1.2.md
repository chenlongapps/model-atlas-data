# Muse Spark 1.2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-spark-1.2
- 模型名称：Muse Spark 1.2
- 发布日期：2026-08-05
- 最近检查时间：2026-11-04T20:17+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：14
- 当前已收录的对应成绩数量：5

## 模型身份与范围说明

- Meta 于 2026-08-05 发布 Muse Code 与 Muse Spark 1.2；本地 release_date 与 Meta 官方发布页一致。模型接受文本、图像、视频和音频输入，输出文本，并支持 reasoning/tools。
- 本轮只新增目标 11 项 Benchmark 中已核实的 Chartography、Terminal-Bench 4.0 和 GDPval-AA v2.1 成绩；旧版成绩与未解决冲突均按原始配置分别记录或说明。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 55.0 (metric=pass@1; version=1.1; variant=xhigh effort; harness=mini-swe-agent); 59.3 (metric=pass@1; version=1.1; variant=xhigh effort; harness=Muse Code) | [Meta Muse Spark 1.2 官方发布页](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2), [Meta Muse Spark 1.2 DeepSWE 方法](https://research.meta.ai/static/muse-spark-1-2-methodology), [Datacurve DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/), [Meta Muse Spark 1.3 方法（对照 1.2 xhigh）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology) | 2026-11-04T20:17+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Meta Muse Spark 1.2 官方方法](https://research.meta.ai/static/muse-spark-1-2-methodology) | 2026-11-04T20:17+08:00 |
| terminal-bench-v4 | 已收录 | 82.9 (metric=pass@1; version=2.1; variant=xhigh effort; harness=Muse Code); 7 (metric=task resolution rate; version=4.0.0; effort=Xhigh; variant=pass@1; three repeats per task; harness=mini-swe-agent) | [Artificial Analysis Muse Spark 1.3 vs 1.2 官方对比页](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2), [Artificial Analysis Terminal-Bench 4.0 官方评测与方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench 4.0 官方发布说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T20:17+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Artificial Analysis Muse Spark 1.3 vs 1.2 官方对比页](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2), [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement), [Harbor Terminal-Bench-Science v0.1 官方排行榜](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-04T20:17+08:00 |
| automationbench-v1.0.6 | 待核实 | 38.2 (metric=pass@1; dataset=public v3 task set; variant=xhigh effort) | [Meta Muse Spark 1.3 方法（public v3 task set）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology), [Zapier AutomationBench 1.0.6 官方排行榜与方法](https://zapier.com/benchmarks), [Zapier AutomationBench 官方 1.0.6 changelog](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T20:17+08:00 |
| osworld-v2.1 | 未找到 | 47.6 (metric=mean partial score; version=2.0; dataset=06.24; variant=xhigh effort; harness=Meta internal evaluation framework); 17.9 (metric=binary completion rate; version=2.0; dataset=06.24; variant=xhigh effort; harness=Meta internal evaluation framework) | [Meta Muse Spark 1.3 方法（Muse Spark 1.2 的 OSWorld 2.0 条件）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology), [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld v2.1 官方发布页](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-04T20:17+08:00 |
| chartography | 已收录 | 32.1 (metric=accuracy (mean; Pass@1); dataset=100-task full Chartography set; effort=xHigh; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方评测方法与 Inspect AI harness](https://github.com/surge-ai/chartography) | 2026-11-04T20:17+08:00 |
| humanitys-last-exam | 冲突 | — | [Artificial Analysis Muse Spark 1.2 (Xhigh) 官方对比页](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4), [Artificial Analysis Muse Spark 1.2 官方分析（2026-08-05）](https://artificialanalysis.ai/articles/muse-spark-1-2), [Artificial Analysis Muse Spark 1.3 官方分析（2026-09-02）](https://artificialanalysis.ai/articles/muse-spark-1-3/), [Artificial Analysis HLE 数据集与方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T20:17+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Muse Spark 1.2 官方模型页（v5.0.1 无分数）](https://artificialanalysis.ai/models/muse-spark-1-2), [Artificial Analysis Intelligence Index v5.0.1 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Muse Spark 1.2/Xhigh 官方对比页（标注 v4.3.2）](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4), [Artificial Analysis Intelligence Index v5 公告](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T20:17+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1615 (metric=Elo; version=2; variant=xhigh effort; harness=Stirrup); 1474 (metric=Elo rating; version=2.1; dataset=220 tasks; effort=Xhigh; harness=Stirrup) | [Artificial Analysis Muse Spark 1.2 (Xhigh) 与 GDPval-AA v2.1 官方对比](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4), [Artificial Analysis GDPval-AA v2.1 排行榜与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Meta Muse Spark 1.3 方法（历史 GDPval-AA v2 结果）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology), [Artificial Analysis Muse Spark 1.2 分析（历史 GDPval-AA v2 结果）](https://artificialanalysis.ai/articles/muse-spark-1-2) | 2026-11-04T20:17+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 官方排行榜与版本更新](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2.1 官方排行榜（Muse Spark 1.2 旧版结果）](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-04T20:17+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 55.0
- metric: pass@1
- version: 1.1
- variant: xhigh effort
- harness: mini-swe-agent
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- date: 2026-09-02
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 59.3
- metric: pass@1
- version: 1.1
- variant: xhigh effort
- harness: Muse Code
- source: [https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)
- date: 2026-08-05
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Meta Muse Spark 1.2 官方发布页](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)
- [Meta Muse Spark 1.2 DeepSWE 方法](https://research.meta.ai/static/muse-spark-1-2-methodology)
- [Datacurve DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)
- [Meta Muse Spark 1.3 方法（对照 1.2 xhigh）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)

研究备注：
- TOML 中保留两条精确 Muse Spark 1.2 / DeepSWE v1.1 成绩：59.3 pass@1（Muse Code）和 55.0 pass@1（mini-swe-agent）。评测 harness 不同，作为不同配置分别保留；本次没有改动。

最近核验时间：2026-11-04T20:17+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Meta Muse Spark 1.2 官方方法](https://research.meta.ai/static/muse-spark-1-2-methodology)

研究备注：
- Scale AI V2 官方榜单未找到 Muse Spark 1.2；Meta 1.2 / 1.3 已查方法资料列出的编码评测也未见 SWE-bench Pro V2。模型具备编码能力，因此该项适用，但没有可核实成绩。

最近核验时间：2026-11-04T20:17+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 82.9
- metric: pass@1
- version: 2.1
- variant: xhigh effort
- harness: Muse Code
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- date: 2026-09-02
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 7
- metric: task resolution rate
- version: 4.0.0
- effort: Xhigh
- variant: pass@1; three repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.3 vs 1.2 官方对比页](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2)
- [Artificial Analysis Terminal-Bench 4.0 官方评测与方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Terminal-Bench 4.0 官方发布说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 新增 7% task resolution rate，版本 4.0.0，Xhigh，mini-swe-agent，pass@1（三次重复）；Artificial Analysis 方法页说明该版本共 66 项任务。原有 82.9 分属于 Terminal-Bench 2.1，未复用。

最近核验时间：2026-11-04T20:17+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.3 vs 1.2 官方对比页](https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2)
- [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Harbor Terminal-Bench-Science v0.1 官方排行榜](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- AA 的 Muse Spark 1.3/1.2 对比页没有 Muse Spark 1.2 的 Terminal-Bench-Science 0.1 分数；Harbor 官方 v0.1 排行榜未能从公开页面文本中确认该型号结果。没有写入分数。

尚未解决的问题：
- 需要继续核对 Harbor 官方 v0.1 排行榜是否有 Muse Spark 1.2 的精确成绩。

最近核验时间：2026-11-04T20:17+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 38.2
- metric: pass@1
- dataset: public v3 task set
- variant: xhigh effort
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- date: 2026-09-02
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Meta Muse Spark 1.3 方法（public v3 task set）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)
- [Zapier AutomationBench 1.0.6 官方排行榜与方法](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方 1.0.6 changelog](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- 已有 TOML 记录 38.2 pass@1，dataset 为 public v3 task set；Meta 方法确认该结果用公开任务集。Zapier 1.0.6 官方排行榜使用 held-out private set，且官方说明公开任务集成绩不能视为同一配置，因此保留原记录但不把它映射为本项 v1.0.6 成绩。

尚未解决的问题：
- Meta 的 public v3 与 Zapier v1.0.6 的版本对应关系及公开结果所用 harness 尚未确认；不得以现有 38.2 替代 v1.0.6 官方私有集成绩。

最近核验时间：2026-11-04T20:17+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 47.6
- metric: mean partial score
- version: 2.0
- dataset: 06.24
- variant: xhigh effort
- harness: Meta internal evaluation framework
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- date: 2026-09-02
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: OSWorld
- score: 17.9
- metric: binary completion rate
- version: 2.0
- dataset: 06.24
- variant: xhigh effort
- harness: Meta internal evaluation framework
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- date: 2026-09-02
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Meta Muse Spark 1.3 方法（Muse Spark 1.2 的 OSWorld 2.0 条件）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)
- [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld v2.1 官方发布页](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- 本地两条 OSWorld 成绩均明确属于 v2.0、dataset 06.24（47.6 mean partial score；17.9 binary completion rate）。Meta 方法说明 Muse Spark 1.2 使用 OSWorld 2.0/06.24；目标 v2.1 于 2026-09-16 发布，故旧版两条记录未映射到 v2.1，也未删除。

最近核验时间：2026-11-04T20:17+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 32.1
- metric: accuracy (mean; Pass@1)
- dataset: 100-task full Chartography set
- effort: xHigh
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography 官方评测方法与 Inspect AI harness](https://github.com/surge-ai/chartography)

研究备注：
- 新增 32.1%，Muse Spark 1.2 xHigh。Surge 官方说明该评测为 100 题，排行榜配置每题 10 次运行并使用 Gemini 3.5 Flash judge；官方任务 harness 基于 Inspect AI。未公布该分数的评测日期，因此未填写 date。

最近核验时间：2026-11-04T20:17+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.2 (Xhigh) 官方对比页](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4)
- [Artificial Analysis Muse Spark 1.2 官方分析（2026-08-05）](https://artificialanalysis.ai/articles/muse-spark-1-2)
- [Artificial Analysis Muse Spark 1.3 官方分析（2026-09-02）](https://artificialanalysis.ai/articles/muse-spark-1-3/)
- [Artificial Analysis HLE 数据集与方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 的 Muse Spark 1.2 (Xhigh) 对比页报 45%，2026-08-05 模型分析文章报 44%；2026-09-02 分析又把 1.2 记作 45%。未说明这些结果间的测试条件或修订，故没有把任一分数写入 TOML。AA 的 HLE 方法使用原始 2,500 题中的 2,158 道 text-only 题，也不同于仓库定义的完整 2,500 题配置。

尚未解决的问题：
- 公开来源对同一 Muse Spark 1.2 HLE 结果报 44% 和 45%，无条件/修订说明；另需区分 AA 的 2,158 text-only 子集与完整 HLE 2,500 题。

最近核验时间：2026-11-04T20:17+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.2 官方模型页（v5.0.1 无分数）](https://artificialanalysis.ai/models/muse-spark-1-2)
- [Artificial Analysis Intelligence Index v5.0.1 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Muse Spark 1.2/Xhigh 官方对比页（标注 v4.3.2）](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4)
- [Artificial Analysis Intelligence Index v5 公告](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- AA 当前 Muse Spark 1.2 官方模型页的 Intelligence Index v5.0.1 为 N/A；对比页所示 40 属于 v4.3.2，旧文章的 54 也不是 v5 的成绩，均未映射。

最近核验时间：2026-11-04T20:17+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1615
- metric: Elo
- version: 2
- variant: xhigh effort
- harness: Stirrup
- source: [https://research.meta.ai/blog/introducing-muse-spark-1-3](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- date: 2026-09-02
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1474
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- effort: Xhigh
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.2 (Xhigh) 与 GDPval-AA v2.1 官方对比](https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4)
- [Artificial Analysis GDPval-AA v2.1 排行榜与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Meta Muse Spark 1.3 方法（历史 GDPval-AA v2 结果）](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology)
- [Artificial Analysis Muse Spark 1.2 分析（历史 GDPval-AA v2 结果）](https://artificialanalysis.ai/articles/muse-spark-1-2)

研究备注：
- 新增 1474 Elo rating，精确版本 v2.1、Xhigh、Stirrup、220 tasks；该分数来自 AA 精确型号对比页。原有 1615 Elo 条目明确属于 GDPval-AA v2，保持原样。另有 AA 2026-08-05 文章将 v2 记为 1631；与 Meta 2026-09-02 的 1615 存在未解释差异。v2.1 1474 是独立明确版本结果，没有由 v2 分数换算。

尚未解决的问题：
- GDPval-AA v2 的 1615（Meta 2026-09-02）与 1631（AA 2026-08-05）差异无已公布条件或修订解释；目标 v2.1 的 1474 已独立收录，不能由 v2 推导。

最近核验时间：2026-11-04T20:17+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 官方排行榜与版本更新](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2.1 官方排行榜（Muse Spark 1.2 旧版结果）](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- Vals v2.2 当前官方榜单显示最新/前沿结果，未列出 Muse Spark 1.2；官方 v2.1 页面有 49.29%，但 v2.2 于 2026-10-19 更新多个组成评测，不能沿用旧值。没有写入 v2.2 成绩。

尚未解决的问题：
- 当前公开 v2.2 页面没有 Muse Spark 1.2 精确成绩；需确认该版本是否曾完成评测。

最近核验时间：2026-11-04T20:17+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.2 官方模型页（v5.0.1 无分数）",
          "url": "https://artificialanalysis.ai/models/muse-spark-1-2"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Muse Spark 1.2/Xhigh 官方对比页（标注 v4.3.2）",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5 公告",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "AA 当前 Muse Spark 1.2 官方模型页的 Intelligence Index v5.0.1 为 N/A；对比页所示 40 属于 v4.3.2，旧文章的 54 也不是 v5 的成绩，均未映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.3 方法（public v3 task set）",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        },
        {
          "label": "Zapier AutomationBench 1.0.6 官方排行榜与方法",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方 1.0.6 changelog",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "已有 TOML 记录 38.2 pass@1，dataset 为 public v3 task set；Meta 方法确认该结果用公开任务集。Zapier 1.0.6 官方排行榜使用 held-out private set，且官方说明公开任务集成绩不能视为同一配置，因此保留原记录但不把它映射为本项 v1.0.6 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "Meta 的 public v3 与 Zapier v1.0.6 的版本对应关系及公开结果所用 harness 尚未确认；不得以现有 38.2 替代 v1.0.6 官方私有集成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography 官方评测方法与 Inspect AI harness",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "新增 32.1%，Muse Spark 1.2 xHigh。Surge 官方说明该评测为 100 题，排行榜配置每题 10 次运行并使用 Gemini 3.5 Flash judge；官方任务 harness 基于 Inspect AI。未公布该分数的评测日期，因此未填写 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.2 官方发布页",
          "url": "https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2"
        },
        {
          "label": "Meta Muse Spark 1.2 DeepSWE 方法",
          "url": "https://research.meta.ai/static/muse-spark-1-2-methodology"
        },
        {
          "label": "Datacurve DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Meta Muse Spark 1.3 方法（对照 1.2 xhigh）",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        }
      ],
      "notes": [
        "TOML 中保留两条精确 Muse Spark 1.2 / DeepSWE v1.1 成绩：59.3 pass@1（Muse Code）和 55.0 pass@1（mini-swe-agent）。评测 harness 不同，作为不同配置分别保留；本次没有改动。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.2 (Xhigh) 与 GDPval-AA v2.1 官方对比",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 排行榜与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Meta Muse Spark 1.3 方法（历史 GDPval-AA v2 结果）",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        },
        {
          "label": "Artificial Analysis Muse Spark 1.2 分析（历史 GDPval-AA v2 结果）",
          "url": "https://artificialanalysis.ai/articles/muse-spark-1-2"
        }
      ],
      "notes": [
        "新增 1474 Elo rating，精确版本 v2.1、Xhigh、Stirrup、220 tasks；该分数来自 AA 精确型号对比页。原有 1615 Elo 条目明确属于 GDPval-AA v2，保持原样。另有 AA 2026-08-05 文章将 v2 记为 1631；与 Meta 2026-09-02 的 1615 存在未解释差异。v2.1 1474 是独立明确版本结果，没有由 v2 分数换算。"
      ],
      "status": "冲突",
      "unresolved": [
        "GDPval-AA v2 的 1615（Meta 2026-09-02）与 1631（AA 2026-08-05）差异无已公布条件或修订解释；目标 v2.1 的 1474 已独立收录，不能由 v2 推导。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.2 (Xhigh) 官方对比页",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-2-vs-gpt-5-4"
        },
        {
          "label": "Artificial Analysis Muse Spark 1.2 官方分析（2026-08-05）",
          "url": "https://artificialanalysis.ai/articles/muse-spark-1-2"
        },
        {
          "label": "Artificial Analysis Muse Spark 1.3 官方分析（2026-09-02）",
          "url": "https://artificialanalysis.ai/articles/muse-spark-1-3/"
        },
        {
          "label": "Artificial Analysis HLE 数据集与方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 的 Muse Spark 1.2 (Xhigh) 对比页报 45%，2026-08-05 模型分析文章报 44%；2026-09-02 分析又把 1.2 记作 45%。未说明这些结果间的测试条件或修订，故没有把任一分数写入 TOML。AA 的 HLE 方法使用原始 2,500 题中的 2,158 道 text-only 题，也不同于仓库定义的完整 2,500 题配置。"
      ],
      "status": "冲突",
      "unresolved": [
        "公开来源对同一 Muse Spark 1.2 HLE 结果报 44% 和 45%，无条件/修订说明；另需区分 AA 的 2,158 text-only 子集与完整 HLE 2,500 题。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.3 方法（Muse Spark 1.2 的 OSWorld 2.0 条件）",
          "url": "https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology"
        },
        {
          "label": "OSWorld-V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld v2.1 官方发布页",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "本地两条 OSWorld 成绩均明确属于 v2.0、dataset 06.24（47.6 mean partial score；17.9 binary completion rate）。Meta 方法说明 Muse Spark 1.2 使用 OSWorld 2.0/06.24；目标 v2.1 于 2026-09-16 发布，故旧版两条记录未映射到 v2.1，也未删除。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Meta Muse Spark 1.2 官方方法",
          "url": "https://research.meta.ai/static/muse-spark-1-2-methodology"
        }
      ],
      "notes": [
        "Scale AI V2 官方榜单未找到 Muse Spark 1.2；Meta 1.2 / 1.3 已查方法资料列出的编码评测也未见 SWE-bench Pro V2。模型具备编码能力，因此该项适用，但没有可核实成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.3 vs 1.2 官方对比页",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2"
        },
        {
          "label": "Terminal-Bench-Science 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor Terminal-Bench-Science v0.1 官方排行榜",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "AA 的 Muse Spark 1.3/1.2 对比页没有 Muse Spark 1.2 的 Terminal-Bench-Science 0.1 分数；Harbor 官方 v0.1 排行榜未能从公开页面文本中确认该型号结果。没有写入分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要继续核对 Harbor 官方 v0.1 排行榜是否有 Muse Spark 1.2 的精确成绩。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.3 vs 1.2 官方对比页",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-muse-spark-1-2"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 官方评测与方法",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Terminal-Bench 4.0 官方发布说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "新增 7% task resolution rate，版本 4.0.0，Xhigh，mini-swe-agent，pass@1（三次重复）；Artificial Analysis 方法页说明该版本共 66 项任务。原有 82.9 分属于 Terminal-Bench 2.1，未复用。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T20:17+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方排行榜与版本更新",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2.1 官方排行榜（Muse Spark 1.2 旧版结果）",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        }
      ],
      "notes": [
        "Vals v2.2 当前官方榜单显示最新/前沿结果，未列出 Muse Spark 1.2；官方 v2.1 页面有 49.29%，但 v2.2 于 2026-10-19 更新多个组成评测，不能沿用旧值。没有写入 v2.2 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前公开 v2.2 页面没有 Muse Spark 1.2 精确成绩；需确认该版本是否曾完成评测。"
      ]
    }
  },
  "existing_records": 14,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T20:17+08:00",
  "model_id": "meta/muse-spark-1.2",
  "model_notes": [
    "Meta 于 2026-08-05 发布 Muse Code 与 Muse Spark 1.2；本地 release_date 与 Meta 官方发布页一致。模型接受文本、图像、视频和音频输入，输出文本，并支持 reasoning/tools。",
    "本轮只新增目标 11 项 Benchmark 中已核实的 Chartography、Terminal-Bench 4.0 和 GDPval-AA v2.1 成绩；旧版成绩与未解决冲突均按原始配置分别记录或说明。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
