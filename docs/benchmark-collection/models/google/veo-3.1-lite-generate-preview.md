# Veo 3.1 Lite Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/veo-3.1-lite-generate-preview
- 模型名称：Veo 3.1 Lite Preview
- 发布日期：2026-03-31
- 最近检查时间：2026-11-05T10:32+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google’s exact model card identifies veo-3.1-lite-generate-preview as a video-generation model: text/image input, video-with-audio output. The card records that the preview API shut down on 2026-10-22; benchmark applicability is assessed from the model’s documented interface.
- No benchmark result was added because all 11 target benchmark task interfaces are not applicable to this video-generation model.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05 |
| swe-bench-pro-v2 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05 |
| terminal-bench-v4 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks) | 2026-11-05 |
| terminal-bench-science-v0.1 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Terminal-Bench Science official leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/) | 2026-11-05 |
| automationbench-v1.0.6 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05 |
| osworld-v2.1 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [OSWorld-V2 project](https://osworld-v2.xlang.ai/) | 2026-11-05 |
| chartography | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05 |
| humanitys-last-exam | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05 |
| gdpval-aa-v2.1 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05 |
| vals-index-v2.2 | 不适用 | — | [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 不适用：the model generates video rather than code changes or terminal-agent outputs required for software issue resolution.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：the model’s documented output is video with audio, not repository code edits.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)

研究备注：
- 不适用：the model has no text/code generation or terminal execution interface for these tasks.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Terminal-Bench Science official leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)

研究备注：
- 不适用：the model outputs video with audio and has no documented terminal-science task interface.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 不适用：the model has no documented tool-calling interface to search and execute cross-app workflows.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)

研究备注：
- 不适用：the model accepts images but generates video; it has no documented desktop-action or GUI-control interface.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 不适用：the model has no text-answer output for chart question answering; its documented output is video with audio.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 不适用：the model is a video-generation API, not a text-answer model for scored academic questions.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 不适用：this dedicated video-generation model does not expose the general language-model evaluation interface required by the text-based V5 index.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 不适用：video generation cannot provide GDPval’s requested documents, slides, diagrams, spreadsheets, or agent-workflow output.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Google Veo 3.1 Lite model card](https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：the model has no documented text-agent interface to complete finance, coding, legal, and tax tasks.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "不适用：this dedicated video-generation model does not expose the general language-model evaluation interface required by the text-based V5 index."
      ],
      "status": "不适用"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "不适用：the model has no documented tool-calling interface to search and execute cross-app workflows."
      ],
      "status": "不适用"
    },
    "chartography": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "不适用：the model has no text-answer output for chart question answering; its documented output is video with audio."
      ],
      "status": "不适用"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "不适用：the model generates video rather than code changes or terminal-agent outputs required for software issue resolution."
      ],
      "status": "不适用"
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "不适用：video generation cannot provide GDPval’s requested documents, slides, diagrams, spreadsheets, or agent-workflow output."
      ],
      "status": "不适用"
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "不适用：the model is a video-generation API, not a text-answer model for scored academic questions."
      ],
      "status": "不适用"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "不适用：the model accepts images but generates video; it has no documented desktop-action or GUI-control interface."
      ],
      "status": "不适用"
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "不适用：the model’s documented output is video with audio, not repository code edits."
      ],
      "status": "不适用"
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Terminal-Bench Science official leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        }
      ],
      "notes": [
        "不适用：the model outputs video with audio and has no documented terminal-science task interface."
      ],
      "status": "不适用"
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "不适用：the model has no text/code generation or terminal execution interface for these tasks."
      ],
      "status": "不适用"
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Veo 3.1 Lite model card",
          "url": "https://aistudio.google.com/docs/models/veo-3.1-lite-generate-preview"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：the model has no documented text-agent interface to complete finance, coding, legal, and tax tasks."
      ],
      "status": "不适用"
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:32+08:00",
  "model_id": "google/veo-3.1-lite-generate-preview",
  "model_notes": [
    "Google’s exact model card identifies veo-3.1-lite-generate-preview as a video-generation model: text/image input, video-with-audio output. The card records that the preview API shut down on 2026-10-22; benchmark applicability is assessed from the model’s documented interface.",
    "No benchmark result was added because all 11 target benchmark task interfaces are not applicable to this video-generation model."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
