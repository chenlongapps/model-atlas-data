# Gemini Flash Latest Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-flash-latest
- 模型名称：Gemini Flash Latest
- 发布日期：2026-08-13
- 最近检查时间：2026-11-04T18:00+08:00
- 整体处理状态：待复核
- 新增成绩数量：7
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：5

## 模型身份与范围说明

- 该模型条目由模型 TOML 注释固定为 2026-08-13 的 gemini-3.7-flash 快照。Google 官方资料确认 Gemini 3.7 Flash 在该日发布；Google 后续说明该旧 API endpoint 已自动路由到 3.8。本记录只对应此处的 3.7 历史快照，不表示当前动态别名仍指向 3.7。来源：[Google 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)、[Google API 文档](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash)。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 65.3 (metric=pass@1; version=1.1; effort=high; variant=self-computed; LiteLLM 1.96; high thinking; harness=mini-swe-agent); 65 (metric=pass@1; version=1.1; dataset=113 tasks; effort=medium; variant=official v1.1 leaderboard; uncertainty ±3 percentage points) | [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash), [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T18:00+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T18:00+08:00 |
| terminal-bench-v4 | 待核实 | 12.12 (metric=accuracy; version=4.0; dataset=66 tasks; variant=avg@3; each run pass@1; 3 runs; ±1 standard error; harness=Mini-SWE-agent) | [Vals Terminal-Bench 4.0 官方排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-4), [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/) | 2026-11-04T18:00+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 7.14 (metric=accuracy; version=0.1.0; dataset=70 tasks; variant=single-run pass@1; infrastructure/provider errors retried; harness=Mini-SWE-agent) | [Vals Terminal-Bench-Science 官方排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-science), [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/) | 2026-11-04T18:00+08:00 |
| automationbench-v1.0.6 | 已收录 | 30.4 (metric=task_completed_correctly; version=1.0.6; dataset=private set; effort=High) | [Zapier AutomationBench 1.0.6 对比报告](https://zapier.com/benchmarks/claude-haiku5_5-report), [Zapier 官方排行榜](https://zapier.com/benchmarks), [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash) | 2026-11-04T18:00+08:00 |
| osworld-v2.1 | 未找到 | — | [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash), [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T18:00+08:00 |
| chartography | 已收录 | 40.4 (metric=accuracy (mean; Pass@1); dataset=100-task full task set; 10 runs per task; Gemini 3.5 Flash judge; effort=High reasoning; harness=Inspect AI) | [Surge 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方 README](https://github.com/surge-ai/chartography) | 2026-11-04T18:00+08:00 |
| humanitys-last-exam | 已收录 | 48 (metric=accuracy; dataset=2,158 text-only questions from the original HLE set; effort=high) | [Artificial Analysis 模型对比页](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash), [Artificial Analysis HLE 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis HLE 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T18:00+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis 模型页](https://artificialanalysis.ai/models/gemini-3-7-flash), [Artificial Analysis Intelligence Index V5 评测页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/) | 2026-11-04T18:00+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis 对比页（1371）](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash), [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gemini-3-7-flash-vs-gpt-5-6-terra-non-reasoning), [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gemini-3-7-flash), [Artificial Analysis GDPval-AA 评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T18:00+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2.1 历史排行榜](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-04T18:00+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 65.3
- metric: pass@1
- version: 1.1
- effort: high
- variant: self-computed; LiteLLM 1.96; high thinking
- harness: mini-swe-agent
- source: [https://deepmind.google/models/model-cards/gemini-3-7-flash/](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 65
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: medium
- variant: official v1.1 leaderboard; uncertainty ±3 percentage points
- source: [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash)
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Gemini 3.7 Flash high-thinking 自测分 65.3%（mini-swe-agent、LiteLLM 1.96）；Datacurve 官方榜另列 medium 配置 65% ±3，113 tasks。两种 effort 分别记录。无明确评测日。

最近核验时间：2026-11-04T18:00+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 未找到 Gemini 3.7 Flash 的 V2 成绩；Scale 当前榜上的 Gemini 3.8 Flash 不属于这个 2026-08-13 的 3.7 快照，未作映射。

最近核验时间：2026-11-04T18:00+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 12.12
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- variant: avg@3; each run pass@1; 3 runs; ±1 standard error
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench 4.0 官方排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)

研究备注：
- Vals 列出 12.12% accuracy，版本 4.0、66 tasks、Mini-SWE-agent，avg@3（三次各 pass@1，±1 SE）。源成绩已记录；本地定义版本是 4.0.0 且指标为 task resolution rate。

尚未解决的问题：
- 来源版本 4.0 与本地 4.0.0 的对应关系及 accuracy 到 task resolution rate 的映射尚未确认。

最近核验时间：2026-11-04T18:00+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 7.14
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- variant: single-run pass@1; infrastructure/provider errors retried
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench-Science 官方排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-science)
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)

研究备注：
- Vals 列出 7.14% accuracy，版本 0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1；只对基础设施或供应商错误重试。源成绩已记录；本地指标为 task resolution rate。

尚未解决的问题：
- 来源 accuracy 与本地 task resolution rate 的映射尚未确认。

最近核验时间：2026-11-04T18:00+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 30.4
- metric: task_completed_correctly
- version: 1.0.6
- dataset: private set
- effort: High
- source: [https://zapier.com/benchmarks/claude-haiku5_5-report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 对比报告](https://zapier.com/benchmarks/claude-haiku5_5-report)
- [Zapier 官方排行榜](https://zapier.com/benchmarks)
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash)

研究备注：
- Zapier 官方报告将 Gemini 3.7 Flash High 列为 AutomationBench 1.0.6 最佳已发布结果 30.4%，并明确指标 task_completed_correctly。DeepMind 模型卡另注明 private set。未公布该 Gemini 结果的具体运行日期或专属 harness。

最近核验时间：2026-11-04T18:00+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash)
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- DeepMind 只公布 OSWorld 2.0 的 47.9% partial score；OSWorld V2.1 后续发布，且本地定义要求 binary task completion rate，因此不能映射。未找到 Gemini 3.7 Flash 的 V2.1 成绩。

最近核验时间：2026-11-04T18:00+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 40.4
- metric: accuracy (mean; Pass@1)
- dataset: 100-task full task set; 10 runs per task; Gemini 3.5 Flash judge
- effort: High reasoning
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge 官方排行榜](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography 官方 README](https://github.com/surge-ai/chartography)

研究备注：
- 排行榜列出 Gemini 3.7 Flash (High reasoning) 40.4%。README 说明完整 100-task set、每 task 10 runs、Gemini 3.5 Flash judge、Inspect AI harness；指标 accuracy/mean (Pass@1)。没有明确语义版本或评测日期。

最近核验时间：2026-11-04T18:00+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 48
- metric: accuracy
- dataset: 2,158 text-only questions from the original HLE set
- effort: high
- source: [https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis 模型对比页](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash)
- [Artificial Analysis HLE 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis HLE 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 报 Gemini 3.7 Flash (high) 48%；评分采用 pass@1，数据集为原始 HLE 的 2,158 道文本题。DeepMind HLE-Verified 53.6% 是不同数据集，不作映射。没有确认的评测日期。

最近核验时间：2026-11-04T18:00+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 模型页](https://artificialanalysis.ai/models/gemini-3-7-flash)
- [Artificial Analysis Intelligence Index V5 评测页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)

研究备注：
- Artificial Analysis 模型页当前对 Gemini 3.7 Flash 显示 Intelligence Index N/A。模型卡中的 56 分没有版本标注，旧版页面中的 39 分属于 V4.3.2，不能映射到本地 V5 定义。

最近核验时间：2026-11-04T18:00+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis 对比页（1371）](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash)
- [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gemini-3-7-flash-vs-gpt-5-6-terra-non-reasoning)
- [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gemini-3-7-flash)
- [Artificial Analysis GDPval-AA 评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 同一 Gemini 3.7 Flash High 的官方对比页分别显示 1371 和 1392 Elo；Artificial Analysis 页面显示该模型已弃用且重测频率较低，未提供可判定这些快照先后的评测日期，因此不选单一分数。官方定义为 v2.1、220 tasks、Stirrup。

尚未解决的问题：
- 1371 与 1392 Elo 分别来自官方不同页面；无可确认的评测日期或最新快照标记。

最近核验时间：2026-11-04T18:00+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2.1 历史排行榜](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- 官方 v2.2 排行榜未列 Gemini 3.7 Flash；v2.1 历史页的 51.27% 属于旧版本，未映射到 v2.2。

最近核验时间：2026-11-04T18:00+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 模型页",
          "url": "https://artificialanalysis.ai/models/gemini-3-7-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 评测页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        }
      ],
      "notes": [
        "Artificial Analysis 模型页当前对 Gemini 3.7 Flash 显示 Intelligence Index N/A。模型卡中的 56 分没有版本标注，旧版页面中的 39 分属于 V4.3.2，不能映射到本地 V5 定义。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 对比报告",
          "url": "https://zapier.com/benchmarks/claude-haiku5_5-report"
        },
        {
          "label": "Zapier 官方排行榜",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "DeepMind 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-7-flash"
        }
      ],
      "notes": [
        "Zapier 官方报告将 Gemini 3.7 Flash High 列为 AutomationBench 1.0.6 最佳已发布结果 30.4%，并明确指标 task_completed_correctly。DeepMind 模型卡另注明 private set。未公布该 Gemini 结果的具体运行日期或专属 harness。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Surge 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography 官方 README",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "排行榜列出 Gemini 3.7 Flash (High reasoning) 40.4%。README 说明完整 100-task set、每 task 10 runs、Gemini 3.5 Flash judge、Inspect AI harness；指标 accuracy/mean (Pass@1)。没有明确语义版本或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "DeepMind 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-7-flash"
        },
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Gemini 3.7 Flash high-thinking 自测分 65.3%（mini-swe-agent、LiteLLM 1.96）；Datacurve 官方榜另列 medium 配置 65% ±3，113 tasks。两种 effort 分别记录。无明确评测日。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 对比页（1371）",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash"
        },
        {
          "label": "Artificial Analysis 对比页（1392）",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-7-flash-vs-gpt-5-6-terra-non-reasoning"
        },
        {
          "label": "Artificial Analysis 对比页（1392）",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gemini-3-7-flash"
        },
        {
          "label": "Artificial Analysis GDPval-AA 评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis 评测方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "同一 Gemini 3.7 Flash High 的官方对比页分别显示 1371 和 1392 Elo；Artificial Analysis 页面显示该模型已弃用且重测频率较低，未提供可判定这些快照先后的评测日期，因此不选单一分数。官方定义为 v2.1、220 tasks、Stirrup。"
      ],
      "status": "冲突",
      "unresolved": [
        "1371 与 1392 Elo 分别来自官方不同页面；无可确认的评测日期或最新快照标记。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 模型对比页",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash"
        },
        {
          "label": "Artificial Analysis HLE 评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis HLE 方法说明",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 报 Gemini 3.7 Flash (high) 48%；评分采用 pass@1，数据集为原始 HLE 的 2,158 道文本题。DeepMind HLE-Verified 53.6% 是不同数据集，不作映射。没有确认的评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "DeepMind 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-7-flash"
        },
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "DeepMind 只公布 OSWorld 2.0 的 47.9% partial score；OSWorld V2.1 后续发布，且本地定义要求 binary task completion rate，因此不能映射。未找到 Gemini 3.7 Flash 的 V2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "未找到 Gemini 3.7 Flash 的 V2 成绩；Scale 当前榜上的 Gemini 3.8 Flash 不属于这个 2026-08-13 的 3.7 快照，未作映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science 官方排行榜及方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        }
      ],
      "notes": [
        "Vals 列出 7.14% accuracy，版本 0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1；只对基础设施或供应商错误重试。源成绩已记录；本地指标为 task resolution rate。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源 accuracy 与本地 task resolution rate 的映射尚未确认。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 官方排行榜及方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        }
      ],
      "notes": [
        "Vals 列出 12.12% accuracy，版本 4.0、66 tasks、Mini-SWE-agent，avg@3（三次各 pass@1，±1 SE）。源成绩已记录；本地定义版本是 4.0.0 且指标为 task resolution rate。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源版本 4.0 与本地 4.0.0 的对应关系及 accuracy 到 task resolution rate 的映射尚未确认。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T18:00+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方排行榜",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2.1 历史排行榜",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        }
      ],
      "notes": [
        "官方 v2.2 排行榜未列 Gemini 3.7 Flash；v2.1 历史页的 51.27% 属于旧版本，未映射到 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T18:00+08:00",
  "model_id": "google/gemini-flash-latest",
  "model_notes": [
    "该模型条目由模型 TOML 注释固定为 2026-08-13 的 gemini-3.7-flash 快照。Google 官方资料确认 Gemini 3.7 Flash 在该日发布；Google 后续说明该旧 API endpoint 已自动路由到 3.8。本记录只对应此处的 3.7 历史快照，不表示当前动态别名仍指向 3.7。来源：[Google 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)、[Google API 文档](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash)。"
  ],
  "new_records": 7,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
