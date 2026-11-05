# Gemini 3.7 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.7-flash
- 模型名称：Gemini 3.7 Flash
- 发布日期：2026-08-13
- 最近检查时间：2026-11-04T17:57+08:00
- 整体处理状态：待复核
- 新增成绩数量：5
- 更新成绩数量：8
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：5

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 65.3 (metric=pass@1; version=1.1; effort=high; variant=self-computed; LiteLLM 1.96; high thinking; harness=mini-swe-agent); 65 (metric=pass@1; version=1.1; dataset=113 tasks; effort=medium; variant=official v1.1 leaderboard; uncertainty ±3 percentage points) | [DeepMind 模型卡与评测方法](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T17:48+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [Scale AI SWE-bench Pro V2 排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T17:48+08:00 |
| terminal-bench-v4 | 待核实 | 85.8 (metric=accuracy; version=2.1); 12.12 (metric=accuracy; version=4.0; dataset=66 tasks; variant=avg@3; each run pass@1; 3 runs; ±1 standard error; harness=Mini-SWE-agent) | [Vals Terminal-Bench 4.0 排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T17:48+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 7.14 (metric=accuracy; version=0.1.0; dataset=70 tasks; variant=single-run pass@1; infrastructure/provider errors retried; harness=Mini-SWE-agent) | [Vals Terminal-Bench-Science 排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T17:48+08:00 |
| automationbench-v1.0.6 | 已存在 | 30.4 (metric=task_completed_correctly; version=1.0.6; dataset=private set; effort=High) | [Zapier AutomationBench 1.0.6 对比报告](https://zapier.com/benchmarks/claude-haiku5_5-report), [Zapier 官方排行榜](https://zapier.com/benchmarks), [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash) | 2026-11-04T17:57+08:00 |
| osworld-v2.1 | 未找到 | — | [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash), [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T17:48+08:00 |
| chartography | 已收录 | 40.4 (metric=accuracy (mean; Pass@1); dataset=100-task full task set; 10 runs per task; Gemini 3.5 Flash judge; effort=High reasoning; harness=Inspect AI) | [Surge 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方 README](https://github.com/surge-ai/chartography) | 2026-11-04T17:48+08:00 |
| humanitys-last-exam | 已收录 | 48 (metric=accuracy; dataset=2,158 text-only questions from the original HLE set; effort=high) | [Artificial Analysis 官方模型对比页](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash), [Artificial Analysis HLE 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis HLE 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T17:48+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis 模型页](https://artificialanalysis.ai/models/gemini-3-7-flash), [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/) | 2026-11-04T17:48+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis 对比页（1371）](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash), [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gemini-3-7-flash-vs-gpt-5-6-terra-non-reasoning), [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gemini-3-7-flash), [Artificial Analysis GDPval-AA 评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T17:57+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2.1 历史排行榜](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-04T17:48+08:00 |

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
- [DeepMind 模型卡与评测方法](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 模型卡的 65.3% 是 Gemini 3.7 Flash high thinking 的自测结果（mini-swe-agent、LiteLLM 1.96）；DeepSWE v1.1 公开榜另列 medium 配置 65% ±3。两条配置分别记录。

最近核验时间：2026-11-04T17:48+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [Scale AI SWE-bench Pro V2 排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 已检查模型卡和 Scale V2 公共排行榜，未找到 Gemini 3.7 Flash 的准确版本成绩；未将 Gemini 3.8 Flash 的成绩映射过来。

最近核验时间：2026-11-04T17:48+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 85.8
- metric: accuracy
- version: 2.1
- source: [https://deepmind.google/models/model-cards/gemini-3-7-flash/](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

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
- [Vals Terminal-Bench 4.0 排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Vals 列出 12.12% accuracy，版本 4.0、66 tasks、Mini-SWE-agent、avg@3（三次各 pass@1，±1 SE）。源成绩已记录；本地定义为版本 4.0.0 和 task resolution rate，映射暂不确定。

尚未解决的问题：
- 来源版本 4.0 与本地 4.0.0 的对应关系及 accuracy 到 task resolution rate 的映射尚未确认。

最近核验时间：2026-11-04T17:48+08:00

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
- [Vals Terminal-Bench-Science 排行榜及方法](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Vals 列出 7.14% accuracy，版本 0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1；基础设施或供应商错误会重试。源成绩已记录；本地指标为 task resolution rate。

尚未解决的问题：
- 来源 accuracy 与本地 task resolution rate 的映射尚未确认。

最近核验时间：2026-11-04T17:48+08:00

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
- Zapier 2026-10 官方报告列出 Gemini 3.7 Flash High 30.4%，比较项为 AutomationBench 1.0.6 的最佳已发布结果；报告给出的指标为 task_completed_correctly。私有测试集。未公布该 Gemini 结果的具体运行日期或专属 harness。

最近核验时间：2026-11-04T17:57+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [DeepMind 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-7-flash)
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- DeepMind 仅公布 OSWorld 2.0 的 47.9% partial score，使用三次运行的最佳结果；它既不是 2.1 版本，也不是本地定义的 binary task completion rate，因此未映射。未找到 Gemini 3.7 Flash 的 2.1 成绩。

最近核验时间：2026-11-04T17:48+08:00

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
- 官方榜列出 Gemini 3.7 Flash (High reasoning) 40.4%。README 说明完整 100 项任务、每任务 10 次运行、Gemini 3.5 Flash 作 judge，汇总指标为 accuracy/mean (Pass@1)；harness 为 Inspect AI。未公布本条结果的具体日期或语义版本。

最近核验时间：2026-11-04T17:48+08:00

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
- [Artificial Analysis 官方模型对比页](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash)
- [Artificial Analysis HLE 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis HLE 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 报 Gemini 3.7 Flash (high) 48%；其 HLE 方法使用原始 HLE 的 2,158 道文本题并按 pass@1 评分。DeepMind 的 HLE-Verified 53.6% 是不同数据集，未映射。

最近核验时间：2026-11-04T17:48+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 模型页](https://artificialanalysis.ai/models/gemini-3-7-flash)
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [DeepMind 模型卡](https://deepmind.google/models/model-cards/gemini-3-7-flash/)

研究备注：
- 当前模型页对 Gemini 3.7 Flash 的 Intelligence Index 显示 N/A。模型卡中的 56 分没有标注目标版本，旧版 v4.3 页面中的 39 分也不是 v5，均未映射为 v5 成绩。

最近核验时间：2026-11-04T17:48+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis 对比页（1371）](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-gemini-3-7-flash)
- [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gemini-3-7-flash-vs-gpt-5-6-terra-non-reasoning)
- [Artificial Analysis 对比页（1392）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gemini-3-7-flash)
- [Artificial Analysis GDPval-AA 评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 官方对比页分别列出同一 Gemini 3.7 Flash high 变体 1371 和 1392 Elo。模型页显示该模型已弃用、重测频率降低；页面没有可确认这些分数新旧顺序的评测日期，因此不选取一个数值写入。
- 官方目标定义对应 v2.1、220 tasks、Stirrup；这些条件不足以解决不同快照的分数冲突。

尚未解决的问题：
- 官方对比页给出 1371 与 1392 Elo，且没有可确认的评测日期或最新快照标记；需要后续复核再决定是否记录。

最近核验时间：2026-11-04T17:57+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2.1 历史排行榜](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- 当前 v2.2 排行榜未列 Gemini 3.7 Flash。v2.1 历史页的 51.27% 属于旧版本，没有映射到 v2.2。

最近核验时间：2026-11-04T17:48+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T17:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 模型页",
          "url": "https://artificialanalysis.ai/models/gemini-3-7-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        }
      ],
      "notes": [
        "当前模型页对 Gemini 3.7 Flash 的 Intelligence Index 显示 N/A。模型卡中的 56 分没有标注目标版本，旧版 v4.3 页面中的 39 分也不是 v5，均未映射为 v5 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T17:57+08:00",
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
        "Zapier 2026-10 官方报告列出 Gemini 3.7 Flash High 30.4%，比较项为 AutomationBench 1.0.6 的最佳已发布结果；报告给出的指标为 task_completed_correctly。私有测试集。未公布该 Gemini 结果的具体运行日期或专属 harness。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T17:48+08:00",
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
        "官方榜列出 Gemini 3.7 Flash (High reasoning) 40.4%。README 说明完整 100 项任务、每任务 10 次运行、Gemini 3.5 Flash 作 judge，汇总指标为 accuracy/mean (Pass@1)；harness 为 Inspect AI。未公布本条结果的具体日期或语义版本。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T17:48+08:00",
      "checked_sources": [
        {
          "label": "DeepMind 模型卡与评测方法",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "模型卡的 65.3% 是 Gemini 3.7 Flash high thinking 的自测结果（mini-swe-agent、LiteLLM 1.96）；DeepSWE v1.1 公开榜另列 medium 配置 65% ±3。两条配置分别记录。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T17:57+08:00",
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
        "官方对比页分别列出同一 Gemini 3.7 Flash high 变体 1371 和 1392 Elo。模型页显示该模型已弃用、重测频率降低；页面没有可确认这些分数新旧顺序的评测日期，因此不选取一个数值写入。",
        "官方目标定义对应 v2.1、220 tasks、Stirrup；这些条件不足以解决不同快照的分数冲突。"
      ],
      "status": "冲突",
      "unresolved": [
        "官方对比页给出 1371 与 1392 Elo，且没有可确认的评测日期或最新快照标记；需要后续复核再决定是否记录。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T17:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 官方模型对比页",
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
        "Artificial Analysis 报 Gemini 3.7 Flash (high) 48%；其 HLE 方法使用原始 HLE 的 2,158 道文本题并按 pass@1 评分。DeepMind 的 HLE-Verified 53.6% 是不同数据集，未映射。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T17:48+08:00",
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
        "DeepMind 仅公布 OSWorld 2.0 的 47.9% partial score，使用三次运行的最佳结果；它既不是 2.1 版本，也不是本地定义的 binary task completion rate，因此未映射。未找到 Gemini 3.7 Flash 的 2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T17:48+08:00",
      "checked_sources": [
        {
          "label": "DeepMind 模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "已检查模型卡和 Scale V2 公共排行榜，未找到 Gemini 3.7 Flash 的准确版本成绩；未将 Gemini 3.8 Flash 的成绩映射过来。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T17:48+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science 排行榜及方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Vals 列出 7.14% accuracy，版本 0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1；基础设施或供应商错误会重试。源成绩已记录；本地指标为 task resolution rate。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源 accuracy 与本地 task resolution rate 的映射尚未确认。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T17:48+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 排行榜及方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Vals 列出 12.12% accuracy，版本 4.0、66 tasks、Mini-SWE-agent、avg@3（三次各 pass@1，±1 SE）。源成绩已记录；本地定义为版本 4.0.0 和 task resolution rate，映射暂不确定。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源版本 4.0 与本地 4.0.0 的对应关系及 accuracy 到 task resolution rate 的映射尚未确认。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T17:48+08:00",
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
        "当前 v2.2 排行榜未列 Gemini 3.7 Flash。v2.1 历史页的 51.27% 属于旧版本，没有映射到 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T17:57+08:00",
  "model_id": "google/gemini-3.7-flash",
  "new_records": 5,
  "overall_status": "待复核",
  "updated_records": 8
}

-->
