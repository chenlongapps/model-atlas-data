# Gemma 4 31B IT Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemma-4-31b-it
- 模型名称：Gemma 4 31B IT
- 发布日期：2026-03-31
- 最近检查时间：2026-11-05T10:28+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- Google’s official Gemma 4 model card identifies the 31B benchmark rows as instruction-tuned results; the two HLE conditions are preserved separately.
- The model card does not disclose HLE question count, dataset revision, evaluation date, or harness for these rows; no undisclosed conditions were added.
- Vals Index remains pending: the exact Vals model page contains a 61.16% headline and an April 9, 2026 update stating 38.94%, but neither is version-attributed to v2.2; 61.16% is the mean of three other listed benchmark results.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks), [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld-V2 project](https://osworld-v2.xlang.ai/), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| chartography | 未找到 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| humanitys-last-exam | 已收录 | 19.5 (metric=accuracy; variant=instruction-tuned; HLE no tools); 26.5 (metric=accuracy; variant=instruction-tuned; HLE with search) | [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Gemma 4 31B profile](https://artificialanalysis.ai/models/gemma-4-31b), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Gemma 4 31B profile](https://artificialanalysis.ai/models/gemma-4-31b) | 2026-11-05 |
| vals-index-v2.2 | 待核实 | — | [Vals Gemma 4 31B IT model page](https://www.vals.ai/models/google_gemma-4-31b-it), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- No exact Gemma 4 31B IT result was verified in the visible leaderboard data; source coverage is incomplete, so absence is not conclusive.

尚未解决的问题：
- No exact DeepSWE v1.1 score for this model was verified.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The official model card does not report SWE-bench Pro V2; the dynamic Scale board did not expose a directly verifiable row for this exact model.

尚未解决的问题：
- No exact SWE-bench Pro V2 result was verified.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The model card lists other coding and tool-use benchmarks but no Terminal-Bench 4.0 result; the official leaderboard view did not expose a verifiable row for this model.

尚未解决的问题：
- No exact Terminal-Bench 4.0 result was verified.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks)
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The checked public leaderboard and model card did not provide an exact Terminal-Bench Science 0.1.0 result.

尚未解决的问题：
- No exact Terminal-Bench Science 0.1.0 result was verified.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The model supports native function calling, so the benchmark is applicable. The official leaderboard folds most rows; no exact Gemma 4 31B IT task_completed_correctly score was verified.

尚未解决的问题：
- No exact AutomationBench v1.0.6 task_completed_correctly result was verified.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- Gemma 4 31B IT supports image input and screen/UI understanding, so OSWorld is applicable. The reviewed v2.1 sources did not expose an exact score.

尚未解决的问题：
- No exact OSWorld v2.1 result was verified.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- Google confirms chart comprehension capability, so the model is applicable. The current public Chartography leaderboard view did not list this exact model.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 19.5
- metric: accuracy
- variant: instruction-tuned; HLE no tools
- source: [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 26.5
- metric: accuracy
- variant: instruction-tuned; HLE with search
- source: [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Google Gemma 4 official model card](https://ai.google.dev/gemma/docs/core/model_card_4)

研究备注：
- The official Benchmark Results table labels instruction-tuned results and lists HLE no tools at 19.5% and HLE with search at 26.5% for Gemma 4 31B. These variants are separate records.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Gemma 4 31B profile](https://artificialanalysis.ai/models/gemma-4-31b)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current profile shows the Intelligence Index as N/A; no V5 score was found. HLE-Diamond elsewhere on the profile is distinct from the original HLE rows above.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Gemma 4 31B profile](https://artificialanalysis.ai/models/gemma-4-31b)

研究备注：
- The evaluation page confirms a separate v2.1 leaderboard, but no exact Gemma 4 31B IT Elo was directly verified. An unverified search-index candidate was not entered.

尚未解决的问题：
- No exact GDPval-AA v2.1 score was directly verified.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Gemma 4 31B IT model page](https://www.vals.ai/models/google_gemma-4-31b-it)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The exact model page shows a 61.16% headline and its Apr 9 update says 38.94% on Vals Index, but neither labels a v2.2 score. The 61.16 headline equals the mean of MortgageTax 61.37%, SAGE 82.78%, and Terminal-Bench 2.0 39.33%; the 38.94% entry predates v2.2 and cites older component tasks. Neither value was entered. The v2.2 board is dated Nov 4, 2026 and shows only each lab’s best model.

尚未解决的问题：
- No exact Vals Index v2.2 score for Gemma 4 31B IT was verified.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemma 4 31B profile",
          "url": "https://artificialanalysis.ai/models/gemma-4-31b"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current profile shows the Intelligence Index as N/A; no V5 score was found. HLE-Diamond elsewhere on the profile is distinct from the original HLE rows above."
      ],
      "status": "未找到"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
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
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The model supports native function calling, so the benchmark is applicable. The official leaderboard folds most rows; no exact Gemma 4 31B IT task_completed_correctly score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact AutomationBench v1.0.6 task_completed_correctly result was verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05",
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
        "Google confirms chart comprehension capability, so the model is applicable. The current public Chartography leaderboard view did not list this exact model."
      ],
      "status": "未找到"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
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
        "No exact Gemma 4 31B IT result was verified in the visible leaderboard data; source coverage is incomplete, so absence is not conclusive."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 score for this model was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Intelligence Benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Gemma 4 31B profile",
          "url": "https://artificialanalysis.ai/models/gemma-4-31b"
        }
      ],
      "notes": [
        "The evaluation page confirms a separate v2.1 leaderboard, but no exact Gemma 4 31B IT Elo was directly verified. An unverified search-index candidate was not entered."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact GDPval-AA v2.1 score was directly verified."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "The official Benchmark Results table labels instruction-tuned results and lists HLE no tools at 19.5% and HLE with search at 26.5% for Gemma 4 31B. These variants are separate records."
      ],
      "status": "已收录"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Google Gemma 4 official model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        }
      ],
      "notes": [
        "Gemma 4 31B IT supports image input and screen/UI understanding, so OSWorld is applicable. The reviewed v2.1 sources did not expose an exact score."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact OSWorld v2.1 result was verified."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
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
        "The official model card does not report SWE-bench Pro V2; the dynamic Scale board did not expose a directly verifiable row for this exact model."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 result was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
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
        "The checked public leaderboard and model card did not provide an exact Terminal-Bench Science 0.1.0 result."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench Science 0.1.0 result was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
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
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Vals Gemma 4 31B IT model page",
          "url": "https://www.vals.ai/models/google_gemma-4-31b-it"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The exact model page shows a 61.16% headline and its Apr 9 update says 38.94% on Vals Index, but neither labels a v2.2 score. The 61.16 headline equals the mean of MortgageTax 61.37%, SAGE 82.78%, and Terminal-Bench 2.0 39.33%; the 38.94% entry predates v2.2 and cites older component tasks. Neither value was entered. The v2.2 board is dated Nov 4, 2026 and shows only each lab’s best model."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Vals Index v2.2 score for Gemma 4 31B IT was verified."
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:28+08:00",
  "model_id": "google/gemma-4-31b-it",
  "model_notes": [
    "Google’s official Gemma 4 model card identifies the 31B benchmark rows as instruction-tuned results; the two HLE conditions are preserved separately.",
    "The model card does not disclose HLE question count, dataset revision, evaluation date, or harness for these rows; no undisclosed conditions were added.",
    "Vals Index remains pending: the exact Vals model page contains a 61.16% headline and an April 9, 2026 update stating 38.94%, but neither is version-attributed to v2.2; 61.16% is the mean of three other listed benchmark results."
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
