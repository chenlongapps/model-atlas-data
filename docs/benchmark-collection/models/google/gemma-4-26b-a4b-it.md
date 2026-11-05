# Gemma 4 26B A4B IT Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemma-4-26b-a4b-it
- 模型名称：Gemma 4 26B A4B IT
- 发布日期：2026-03-31
- 最近检查时间：2026-11-05T10:19+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- Exact model is Gemma 4 26B A4B IT, released 2026-03-31. Google’s model card labels its benchmark table as instruction-tuned results and lists HLE no tools and HLE with search separately for Gemma 4 26B A4B.
- Google’s model card does not specify the HLE question count, dataset revision, evaluation date, or harness for these two results. No version/date or undisclosed testing conditions were added.
- Artificial Analysis AutomationBench-AA 2% is not mapped to the target AutomationBench score: AA uses a distinct objective-completion/guardrail metric even though its held-out tasks derive from dataset v1.0.6.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks), [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis direct comparison for Gemma 4 26B A4B](https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemma-4-26b-a4b) | 2026-11-05T10:19+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| chartography | 未找到 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| humanitys-last-exam | 已收录 | 8.7 (metric=accuracy; variant=instruction-tuned; HLE no tools); 17.2 (metric=accuracy; variant=instruction-tuned; HLE with search) | [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05T10:19+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact Gemma 4 26B A4B profile](https://artificialanalysis.ai/models/gemma-4-26b-a4b), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis current direct comparison](https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemma-4-26b-a4b) | 2026-11-05T10:19+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis exact Gemma 4 26B A4B profile](https://artificialanalysis.ai/models/gemma-4-26b-a4b) | 2026-11-05T10:19+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index), [Vals AI model directory](https://www.vals.ai/models) | 2026-11-05T10:19+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The exact model was not directly verified in the visible leaderboard/JSON data, whose coverage is incomplete. The official card does not report this benchmark.

尚未解决的问题：
- No exact DeepSWE v1.1 score for Gemma 4 26B A4B IT was verified.

最近核验时间：2026-11-05T10:19+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The official Gemma card does not report SWE-bench Pro V2; the dynamic Scale page did not expose a directly verifiable row for this exact model.

尚未解决的问题：
- No exact SWE-bench Pro V2 result was verified.

最近核验时间：2026-11-05T10:19+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The model card lists other coding and tool-use benchmarks but no Terminal-Bench 4.0 result; the official leaderboard view did not expose a verifiable row for this model.

尚未解决的问题：
- No exact Terminal-Bench 4.0 result was verified.

最近核验时间：2026-11-05T10:19+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks)
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The checked public leaderboard and Google model card did not provide an exact 0.1.0 result for this model.

尚未解决的问题：
- No exact Terminal-Bench Science 0.1.0 result was verified.

最近核验时间：2026-11-05T10:19+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis direct comparison for Gemma 4 26B A4B](https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemma-4-26b-a4b)

研究备注：
- AA reports AutomationBench-AA 2% for this exact model using a held-out v1.0.6-derived task split, but its headline objective-completion/guardrail metric differs from Zapier’s task_completed_correctly metric. Zapier’s folded leaderboard does not expose an exact row; the AA value is not mapped as the target score.

尚未解决的问题：
- No exact Zapier AutomationBench v1.0.6 task_completed_correctly result was verified.

最近核验时间：2026-11-05T10:19+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The model supports image input and screen/UI understanding, so OSWorld is applicable. The reviewed v2.1 release sources did not expose an exact Gemma 4 26B A4B score.

尚未解决的问题：
- No exact OSWorld v2.1 result was verified.

最近核验时间：2026-11-05T10:19+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- Google confirms chart comprehension capability, so this model is applicable. The current public Chartography leaderboard view did not list the exact Gemma 4 26B A4B model.

最近核验时间：2026-11-05T10:19+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 8.7
- metric: accuracy
- variant: instruction-tuned; HLE no tools
- source: [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 17.2
- metric: accuracy
- variant: instruction-tuned; HLE with search
- source: [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The official Benchmark Results table identifies instruction-tuned model values: HLE no tools 8.7% and HLE with search 17.2% for Gemma 4 26B A4B. These are retained as separate variants. The card does not state question count, revision, harness, or evaluation date.

最近核验时间：2026-11-05T10:19+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact Gemma 4 26B A4B profile](https://artificialanalysis.ai/models/gemma-4-26b-a4b)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis current direct comparison](https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemma-4-26b-a4b)

研究备注：
- The exact profile currently shows Index N/A. The comparison reports HLE-Diamond without a value; HLE-Diamond is distinct from the original HLE rows in the Google model card. No V5 index score was found.

最近核验时间：2026-11-05T10:19+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis exact Gemma 4 26B A4B profile](https://artificialanalysis.ai/models/gemma-4-26b-a4b)

研究备注：
- AA’s v2.1 evaluation page confirms the standalone 220-task evaluation, but no exact Gemma 4 26B A4B Elo was directly visible in the opened model/comparison pages. A search-index candidate was not treated as verified.

尚未解决的问题：
- No exact GDPval-AA v2.1 score was directly verified.

最近核验时间：2026-11-05T10:19+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI model directory](https://www.vals.ai/models)

研究备注：
- The V2.2 page shows the best model from each lab and does not list this exact model. No exact v2.2 model page/result was verified, so absence is not treated as proof of no score.

尚未解决的问题：
- No exact Vals Index v2.2 result was verified.

最近核验时间：2026-11-05T10:19+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact Gemma 4 26B A4B profile",
          "url": "https://artificialanalysis.ai/models/gemma-4-26b-a4b"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis current direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemma-4-26b-a4b"
        }
      ],
      "notes": [
        "The exact profile currently shows Index N/A. The comparison reports HLE-Diamond without a value; HLE-Diamond is distinct from the original HLE rows in the Google model card. No V5 index score was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis direct comparison for Gemma 4 26B A4B",
          "url": "https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemma-4-26b-a4b"
        }
      ],
      "notes": [
        "AA reports AutomationBench-AA 2% for this exact model using a held-out v1.0.6-derived task split, but its headline objective-completion/guardrail metric differs from Zapier’s task_completed_correctly metric. Zapier’s folded leaderboard does not expose an exact row; the AA value is not mapped as the target score."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Zapier AutomationBench v1.0.6 task_completed_correctly result was verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography public leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "Google confirms chart comprehension capability, so this model is applicable. The current public Chartography leaderboard view did not list the exact Gemma 4 26B A4B model."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard data",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The exact model was not directly verified in the visible leaderboard/JSON data, whose coverage is incomplete. The official card does not report this benchmark."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 score for Gemma 4 26B A4B IT was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis exact Gemma 4 26B A4B profile",
          "url": "https://artificialanalysis.ai/models/gemma-4-26b-a4b"
        }
      ],
      "notes": [
        "AA’s v2.1 evaluation page confirms the standalone 220-task evaluation, but no exact Gemma 4 26B A4B Elo was directly visible in the opened model/comparison pages. A search-index candidate was not treated as verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact GDPval-AA v2.1 score was directly verified."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The official Benchmark Results table identifies instruction-tuned model values: HLE no tools 8.7% and HLE with search 17.2% for Gemma 4 26B A4B. These are retained as separate variants. The card does not state question count, revision, harness, or evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The model supports image input and screen/UI understanding, so OSWorld is applicable. The reviewed v2.1 release sources did not expose an exact Gemma 4 26B A4B score."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact OSWorld v2.1 result was verified."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The official Gemma card does not report SWE-bench Pro V2; the dynamic Scale page did not expose a directly verifiable row for this exact model."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 result was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Snorkel Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The checked public leaderboard and Google model card did not provide an exact 0.1.0 result for this model."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench Science 0.1.0 result was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench official versions and leaderboard",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The model card lists other coding and tool-use benchmarks but no Terminal-Bench 4.0 result; the official leaderboard view did not expose a verifiable row for this model."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench 4.0 result was verified."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T10:19+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI model directory",
          "url": "https://www.vals.ai/models"
        }
      ],
      "notes": [
        "The V2.2 page shows the best model from each lab and does not list this exact model. No exact v2.2 model page/result was verified, so absence is not treated as proof of no score."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Vals Index v2.2 result was verified."
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:19+08:00",
  "model_id": "google/gemma-4-26b-a4b-it",
  "model_notes": [
    "Exact model is Gemma 4 26B A4B IT, released 2026-03-31. Google’s model card labels its benchmark table as instruction-tuned results and lists HLE no tools and HLE with search separately for Gemma 4 26B A4B.",
    "Google’s model card does not specify the HLE question count, dataset revision, evaluation date, or harness for these two results. No version/date or undisclosed testing conditions were added.",
    "Artificial Analysis AutomationBench-AA 2% is not mapped to the target AutomationBench score: AA uses a distinct objective-completion/guardrail metric even though its held-out tasks derive from dataset v1.0.6."
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
