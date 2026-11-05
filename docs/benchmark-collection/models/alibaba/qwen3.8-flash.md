# Qwen3.8 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-flash
- 模型名称：Qwen3.8 Flash
- 发布日期：2026-08-26
- 最近检查时间：2026-11-04T15:37+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 58.7 (metric=score; version=1.1) | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [DeepSWE v1.1 methodology and board](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T15:37+08:00 |
| swe-bench-pro-v2 | 待核实 | 62.5 (metric=score) | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [Scale SWE-bench Pro V2 methodology and leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T15:37+08:00 |
| terminal-bench-v4 | 未找到 | — | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0), [Artificial Analysis Terminal-Bench 4.0 evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T15:37+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [Terminal-Bench-Science official release](https://www.tbench.ai/news/terminal-bench-science-0-1), [Artificial Analysis Terminal-Bench-Science evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T15:37+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [Zapier AutomationBench board](https://zapier.com/benchmarks), [Artificial Analysis model page](https://artificialanalysis.ai/models/qwen3-8-flash) | 2026-11-04T15:37+08:00 |
| osworld-v2.1 | 未找到 | — | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [OSWorld V2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [OSWorld V2 official releases](https://github.com/xlang-ai/OSWorld-V2/releases) | 2026-11-04T15:37+08:00 |
| chartography | 待核实 | 17.4 (metric=accuracy/mean; dataset=100 tasks; effort=xHigh reasoning; variant=10 runs per task; Gemini 3.5 Flash judge) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official benchmark repository](https://github.com/surge-ai/chartography), [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model) | 2026-11-04T15:37+08:00 |
| humanitys-last-exam | 待核实 | — | [Model Menu Qwen3.8 Flash result page](https://modelmenu.dev/models/qwen3.8-flash), [Model Menu HLE variant notes](https://modelmenu.dev/benchmarks/humanitys-last-exam), [Humanity’s Last Exam official benchmark](https://lastexam.ai/) | 2026-11-04T15:37+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.8-Flash model page](https://artificialanalysis.ai/models/qwen3-8-flash), [Artificial Analysis Intelligence Index V5 article](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T15:37+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [AIIQ GDPval-AA v2.1 results page](https://www.aiiq.org/benchmarks/gdpval-aa-v2/), [Artificial Analysis GDPval-AA official page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Qwen3.8-Flash model page](https://artificialanalysis.ai/models/qwen3-8-flash) | 2026-11-04T15:37+08:00 |
| vals-index-v2.2 | 未找到 | — | [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model), [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T15:37+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 58.7
- metric: score
- version: 1.1
- source: [https://docs.qwencloud.com/developer-guides/getting-started/latest-model](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [DeepSWE v1.1 methodology and board](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- QwenCloud maps API model ID qwen3.8-flash to a provider-reported DeepSWE 1.1 score of 58.7. It does not report the metric, harness, dataset, or evaluation date.
- The raw source metric is retained as score; the local definition requires pass@1, so exact mapping remains pending.

尚未解决的问题：
- Confirm the provider-reported score metric before mapping to pass@1.

最近核验时间：2026-11-04T15:37+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 62.5
- metric: score
- source: [https://docs.qwencloud.com/developer-guides/getting-started/latest-model](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [Scale SWE-bench Pro V2 methodology and leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- QwenCloud reports a generic SWE-bench Pro score of 62.5 for qwen3.8-flash, but gives no benchmark version, dataset, metric, or harness.
- Scale V2 is a distinct 642-task locked protocol. No source ties the provider-reported result to V2, so the raw Pro score is preserved without a version and is not mapped to V2.

尚未解决的问题：
- Confirm whether the 62.5 result used SWE-bench Pro V2 (2.0.0); no exact V2 attribution was found.

最近核验时间：2026-11-04T15:37+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0)
- [Artificial Analysis Terminal-Bench 4.0 evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- No exact-model Terminal-Bench 4.0 result was found. Qwen3.8 Max and Qwen3.8-Flash-Next results belong to other model IDs and were not transferred.

最近核验时间：2026-11-04T15:37+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [Terminal-Bench-Science official release](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Artificial Analysis Terminal-Bench-Science evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- No exact-model result was found on the checked public board or in QwenCloud’s reported evaluation summary.

最近核验时间：2026-11-04T15:37+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [Zapier AutomationBench board](https://zapier.com/benchmarks)
- [Artificial Analysis model page](https://artificialanalysis.ai/models/qwen3-8-flash)

研究备注：
- No Qwen3.8-Flash result was confirmed on Zapier’s v1.0.6 board. Artificial Analysis AutomationBench-AA is a different benchmark and metric; its score was not transferred.

最近核验时间：2026-11-04T15:37+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [OSWorld V2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [OSWorld V2 official releases](https://github.com/xlang-ai/OSWorld-V2/releases)

研究备注：
- No exact-model OSWorld 2.1 score was found. OSWorld 2.0 and other Qwen model results were not transferred.

最近核验时间：2026-11-04T15:37+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 17.4
- metric: accuracy/mean
- dataset: 100 tasks
- effort: xHigh reasoning
- variant: 10 runs per task; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official benchmark repository](https://github.com/surge-ai/chartography)
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)

研究备注：
- Added the exact Qwen 3.8 Flash leaderboard result of 17.4%. The source reports xHigh reasoning; the benchmark repository defines the raw scorer as accuracy/mean (Pass@1) and documents the 100-task set. The row details 10 runs per task and a Gemini 3.5 Flash judge.
- The source metric accuracy/mean differs textually from the local definition accuracy (mean; Pass@1); raw label is preserved. Harness is not separately stated for this result row.

尚未解决的问题：
- Review metric-label mapping to the local accuracy (mean; Pass@1) definition.

最近核验时间：2026-11-04T15:37+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Model Menu Qwen3.8 Flash result page](https://modelmenu.dev/models/qwen3.8-flash)
- [Model Menu HLE variant notes](https://modelmenu.dev/benchmarks/humanitys-last-exam)
- [Humanity’s Last Exam official benchmark](https://lastexam.ai/)

研究备注：
- A secondary page attributes 38% to Qwen3.8 Flash and Artificial Analysis. The reported HLE evaluation is a 2,158-question subset, while the repository definition uses the original 2,500-question HLE set; no score was added.

尚未解决的问题：
- Confirm whether a score on the original 2,500-question HLE set exists; do not substitute the 2,158-question subset.

最近核验时间：2026-11-04T15:37+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.8-Flash model page](https://artificialanalysis.ai/models/qwen3-8-flash)
- [Artificial Analysis Intelligence Index V5 article](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- The 39.8 score in secondary result pages belongs to Intelligence Index v4.3.2, not v5. The current AA page reports v5.0.1 and no compatible score for this model; N/A is not written as zero.

最近核验时间：2026-11-04T15:37+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [AIIQ GDPval-AA v2.1 results page](https://www.aiiq.org/benchmarks/gdpval-aa-v2/)
- [Artificial Analysis GDPval-AA official page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Qwen3.8-Flash model page](https://artificialanalysis.ai/models/qwen3-8-flash)

研究备注：
- AIIQ lists a 56.3% normalized score attributed to an AA v4.3.2 configuration; this is not the raw Elo required by the repository. The current official AA board did not confirm an exact-model v2.1 result, so no score was added.

尚未解决的问题：
- Find a source for the original GDPval-AA v2.1 Elo and exact tested configuration; do not record a normalized third-party score as Elo.

最近核验时间：2026-11-04T15:37+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [QwenCloud official Qwen3.8-Flash model page](https://docs.qwencloud.com/developer-guides/getting-started/latest-model)
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The current Vals v2.2 board lists Qwen3.8 Max 0902, not Qwen3.8 Flash. No exact-model v2.2 result was found and no Max result was transferred.

最近核验时间：2026-11-04T15:37+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8-Flash model page",
          "url": "https://artificialanalysis.ai/models/qwen3-8-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 article",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "The 39.8 score in secondary result pages belongs to Intelligence Index v4.3.2, not v5. The current AA page reports v5.0.1 and no compatible score for this model; N/A is not written as zero."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "Zapier AutomationBench board",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis model page",
          "url": "https://artificialanalysis.ai/models/qwen3-8-flash"
        }
      ],
      "notes": [
        "No Qwen3.8-Flash result was confirmed on Zapier’s v1.0.6 board. Artificial Analysis AutomationBench-AA is a different benchmark and metric; its score was not transferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official benchmark repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        }
      ],
      "notes": [
        "Added the exact Qwen 3.8 Flash leaderboard result of 17.4%. The source reports xHigh reasoning; the benchmark repository defines the raw scorer as accuracy/mean (Pass@1) and documents the 100-task set. The row details 10 runs per task and a Gemini 3.5 Flash judge.",
        "The source metric accuracy/mean differs textually from the local definition accuracy (mean; Pass@1); raw label is preserved. Harness is not separately stated for this result row."
      ],
      "status": "待核实",
      "unresolved": [
        "Review metric-label mapping to the local accuracy (mean; Pass@1) definition."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "DeepSWE v1.1 methodology and board",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "QwenCloud maps API model ID qwen3.8-flash to a provider-reported DeepSWE 1.1 score of 58.7. It does not report the metric, harness, dataset, or evaluation date.",
        "The raw source metric is retained as score; the local definition requires pass@1, so exact mapping remains pending."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm the provider-reported score metric before mapping to pass@1."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "AIIQ GDPval-AA v2.1 results page",
          "url": "https://www.aiiq.org/benchmarks/gdpval-aa-v2/"
        },
        {
          "label": "Artificial Analysis GDPval-AA official page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Qwen3.8-Flash model page",
          "url": "https://artificialanalysis.ai/models/qwen3-8-flash"
        }
      ],
      "notes": [
        "AIIQ lists a 56.3% normalized score attributed to an AA v4.3.2 configuration; this is not the raw Elo required by the repository. The current official AA board did not confirm an exact-model v2.1 result, so no score was added."
      ],
      "status": "待核实",
      "unresolved": [
        "Find a source for the original GDPval-AA v2.1 Elo and exact tested configuration; do not record a normalized third-party score as Elo."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "Model Menu Qwen3.8 Flash result page",
          "url": "https://modelmenu.dev/models/qwen3.8-flash"
        },
        {
          "label": "Model Menu HLE variant notes",
          "url": "https://modelmenu.dev/benchmarks/humanitys-last-exam"
        },
        {
          "label": "Humanity’s Last Exam official benchmark",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "A secondary page attributes 38% to Qwen3.8 Flash and Artificial Analysis. The reported HLE evaluation is a 2,158-question subset, while the repository definition uses the original 2,500-question HLE set; no score was added."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm whether a score on the original 2,500-question HLE set exists; do not substitute the 2,158-question subset."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "OSWorld V2.1 release record",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "OSWorld V2 official releases",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        }
      ],
      "notes": [
        "No exact-model OSWorld 2.1 score was found. OSWorld 2.0 and other Qwen model results were not transferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "Scale SWE-bench Pro V2 methodology and leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "QwenCloud reports a generic SWE-bench Pro score of 62.5 for qwen3.8-flash, but gives no benchmark version, dataset, metric, or harness.",
        "Scale V2 is a distinct 642-task locked protocol. No source ties the provider-reported result to V2, so the raw Pro score is preserved without a version and is not mapped to V2."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm whether the 62.5 result used SWE-bench Pro V2 (2.0.0); no exact V2 attribution was found."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "Terminal-Bench-Science official release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "No exact-model result was found on the checked public board or in QwenCloud’s reported evaluation summary."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "Terminal-Bench 4.0 official release",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "No exact-model Terminal-Bench 4.0 result was found. Qwen3.8 Max and Qwen3.8-Flash-Next results belong to other model IDs and were not transferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T15:37+08:00",
      "checked_sources": [
        {
          "label": "QwenCloud official Qwen3.8-Flash model page",
          "url": "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
        },
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The current Vals v2.2 board lists Qwen3.8 Max 0902, not Qwen3.8 Flash. No exact-model v2.2 result was found and no Max result was transferred."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T15:37+08:00",
  "model_id": "alibaba/qwen3.8-flash",
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
