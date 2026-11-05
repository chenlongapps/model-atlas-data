# Gemini 3.1 Flash Live Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.1-flash-live-preview
- 模型名称：Gemini 3.1 Flash Live Preview
- 发布日期：2026-03-26
- 最近检查时间：2026-11-05T10:40+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google’s official model page confirms the exact model ID gemini-3.1-flash-live-preview, multimodal text/image/audio/video inputs, text/audio outputs, thinking, and synchronous function calling. Its Live API requires the client to handle tool responses.
- Artificial Analysis reports scores for other speech-to-speech evaluations for this family; those are outside the 11 target benchmarks and were not mapped into this model file.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench official leaderboard](https://www.tbench.ai/), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| terminal-bench-science-v0.1 | 待核实 | — | [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview), [Gemini Live API tool-use documentation](https://ai.google.dev/gemini-api/docs/live-api/tools) | 2026-11-05 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld-V2 project](https://osworld-v2.xlang.ai/), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview), [Gemini Live API tool-use documentation](https://ai.google.dev/gemini-api/docs/live-api/tools) | 2026-11-05 |
| chartography | 未找到 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| humanitys-last-exam | 待核实 | — | [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Speech-to-Speech evaluations](https://artificialanalysis.ai/speech-to-speech), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- The model can return text and call client-defined tools, but no exact flash-live result was verified in the visible DeepSWE data, whose coverage is incomplete.

尚未解决的问题：
- No exact DeepSWE v1.1 score for this model was verified.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- The model supports synchronous function calling and could be used with an external coding harness. The current public Scale board did not list this exact model; no score was entered.

尚未解决的问题：
- No exact SWE-bench Pro V2 score was verified.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench official leaderboard](https://www.tbench.ai/)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- Function calling could connect this model to an external terminal harness, but no exact Terminal-Bench 4.0 result was exposed in the checked official leaderboard.

尚未解决的问题：
- No exact Terminal-Bench 4.0 score was verified.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- No exact flash-live result was found in the checked public Science leaderboard; model capability does not rule out evaluation through a custom harness.

尚未解决的问题：
- No exact Terminal-Bench Science 0.1.0 score was verified.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)
- [Gemini Live API tool-use documentation](https://ai.google.dev/gemini-api/docs/live-api/tools)

研究备注：
- The model supports synchronous function calling and the task interface is applicable. The official Zapier board folds most rows, so no exact score was verified.

尚未解决的问题：
- No exact AutomationBench v1.0.6 result was verified.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)
- [Gemini Live API tool-use documentation](https://ai.google.dev/gemini-api/docs/live-api/tools)

研究备注：
- The model accepts image/video and supports function calling, so an external computer-use harness is feasible. The v2.1 sources did not expose an exact score; the online project view currently presents v2.0.

尚未解决的问题：
- No exact OSWorld v2.1 result for this model was verified.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- The model accepts images and returns text, so chart reasoning is applicable. The current visible official leaderboard did not list this exact model; Gemini 3.1 Pro is a different model and was not mapped.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- The model accepts text and returns text, but no exact original-HLE score for this model was found in the checked official pages. HLE-Diamond results are not substitutes for the original benchmark.

尚未解决的问题：
- No exact original HLE result was verified.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Speech-to-Speech evaluations](https://artificialanalysis.ai/speech-to-speech)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- No exact V5 index score for this model was verified. The separate Speech-to-Speech Index is not the V5 target.

尚未解决的问题：
- No exact Artificial Analysis Intelligence Index V5 score was verified.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- The model supports function calling, but no exact result under the GDPval-AA v2.1 agent configuration was directly verified.

尚未解决的问题：
- No exact GDPval-AA v2.1 score was verified.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Gemini 3.1 Flash Live model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)

研究备注：
- The model supports dialogue and tool use, but no exact v2.2 score was verified. The current leaderboard only displays the best model from each lab, so absence from its summary is not conclusive.

尚未解决的问题：
- No exact Vals Index v2.2 score was verified.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Speech-to-Speech evaluations",
          "url": "https://artificialanalysis.ai/speech-to-speech"
        },
        {
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "No exact V5 index score for this model was verified. The separate Speech-to-Speech Index is not the V5 target."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Artificial Analysis Intelligence Index V5 score was verified."
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        },
        {
          "label": "Gemini Live API tool-use documentation",
          "url": "https://ai.google.dev/gemini-api/docs/live-api/tools"
        }
      ],
      "notes": [
        "The model supports synchronous function calling and the task interface is applicable. The official Zapier board folds most rows, so no exact score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact AutomationBench v1.0.6 result was verified."
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
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "The model accepts images and returns text, so chart reasoning is applicable. The current visible official leaderboard did not list this exact model; Gemini 3.1 Pro is a different model and was not mapped."
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
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "The model can return text and call client-defined tools, but no exact flash-live result was verified in the visible DeepSWE data, whose coverage is incomplete."
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
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "The model supports function calling, but no exact result under the GDPval-AA v2.1 agent configuration was directly verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact GDPval-AA v2.1 score was verified."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "The model accepts text and returns text, but no exact original-HLE score for this model was found in the checked official pages. HLE-Diamond results are not substitutes for the original benchmark."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact original HLE result was verified."
      ]
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
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        },
        {
          "label": "Gemini Live API tool-use documentation",
          "url": "https://ai.google.dev/gemini-api/docs/live-api/tools"
        }
      ],
      "notes": [
        "The model accepts image/video and supports function calling, so an external computer-use harness is feasible. The v2.1 sources did not expose an exact score; the online project view currently presents v2.0."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact OSWorld v2.1 result for this model was verified."
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
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "The model supports synchronous function calling and could be used with an external coding harness. The current public Scale board did not list this exact model; no score was entered."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 score was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Snorkel Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "No exact flash-live result was found in the checked public Science leaderboard; model capability does not rule out evaluation through a custom harness."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench Science 0.1.0 score was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Terminal-Bench official leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "Function calling could connect this model to an external terminal harness, but no exact Terminal-Bench 4.0 result was exposed in the checked official leaderboard."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench 4.0 score was verified."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Gemini 3.1 Flash Live model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview"
        }
      ],
      "notes": [
        "The model supports dialogue and tool use, but no exact v2.2 score was verified. The current leaderboard only displays the best model from each lab, so absence from its summary is not conclusive."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Vals Index v2.2 score was verified."
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:40+08:00",
  "model_id": "google/gemini-3.1-flash-live-preview",
  "model_notes": [
    "Google’s official model page confirms the exact model ID gemini-3.1-flash-live-preview, multimodal text/image/audio/video inputs, text/audio outputs, thinking, and synchronous function calling. Its Live API requires the client to handle tool responses.",
    "Artificial Analysis reports scores for other speech-to-speech evaluations for this family; those are outside the 11 target benchmarks and were not mapped into this model file."
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
