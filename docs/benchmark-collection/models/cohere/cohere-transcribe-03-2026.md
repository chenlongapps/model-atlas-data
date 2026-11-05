# Cohere Transcribe Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：cohere/cohere-transcribe-03-2026
- 模型名称：Cohere Transcribe
- 发布日期：2026-03-26
- 最近检查时间：2026-11-05T10:38+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Cohere’s official model documentation identifies the exact model name cohere-transcribe-03-2026 as a 2B automatic speech recognition model with audio input and text transcription output across 14 languages.
- The model exposes speech transcription, not code generation, general question answering, visual understanding, GUI actions, or tool-agent behavior; no target benchmark result was added.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Cohere Transcribe exact model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05 |
| swe-bench-pro-v2 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Cohere Transcribe exact model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05 |
| terminal-bench-v4 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks) | 2026-11-05 |
| terminal-bench-science-v0.1 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/) | 2026-11-05 |
| automationbench-v1.0.6 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05 |
| osworld-v2.1 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [OSWorld-V2 project](https://osworld-v2.xlang.ai/) | 2026-11-05 |
| chartography | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05 |
| humanitys-last-exam | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis speech-to-text benchmark](https://artificialanalysis.ai/speech-to-text/non-streaming/) | 2026-11-05 |
| gdpval-aa-v2.1 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05 |
| vals-index-v2.2 | 不适用 | — | [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Cohere Transcribe exact model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 不适用：the checkpoint is dedicated ASR and does not generate code changes or terminal-agent outputs.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Cohere Transcribe exact model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：the model transcribes audio into text and does not edit source-code repositories.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)

研究备注：
- 不适用：the ASR interface does not provide code generation or terminal task execution.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)

研究备注：
- 不适用：the model has no terminal-action interface for the science workflows.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 不适用：the ASR model has no tool-calling capability to execute cross-application workflows.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)

研究备注：
- 不适用：the model accepts audio only and has no screenshot input or GUI-action interface.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 不适用：the model accepts audio rather than chart images and does not expose visual question answering.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 不适用：transcription output is not the general academic question-answering capability evaluated by HLE.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis speech-to-text benchmark](https://artificialanalysis.ai/speech-to-text/non-streaming/)

研究备注：
- 不适用：Cohere Transcribe is a dedicated ASR model rather than a general model for the V5 knowledge-work, coding, science, and general evaluations.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 不适用：the model’s transcription function does not complete GDPval-AA agent tasks or produce the requested professional work products.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：the ASR model does not provide the general tool-agent behavior required for finance, coding, legal, and tax tasks.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis speech-to-text benchmark",
          "url": "https://artificialanalysis.ai/speech-to-text/non-streaming/"
        }
      ],
      "notes": [
        "不适用：Cohere Transcribe is a dedicated ASR model rather than a general model for the V5 knowledge-work, coding, science, and general evaluations."
      ],
      "status": "不适用"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "不适用：the ASR model has no tool-calling capability to execute cross-application workflows."
      ],
      "status": "不适用"
    },
    "chartography": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "不适用：the model accepts audio rather than chart images and does not expose visual question answering."
      ],
      "status": "不适用"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Cohere Transcribe exact model card",
          "url": "https://huggingface.co/CohereLabs/cohere-transcribe-03-2026"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "不适用：the checkpoint is dedicated ASR and does not generate code changes or terminal-agent outputs."
      ],
      "status": "不适用"
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "不适用：the model’s transcription function does not complete GDPval-AA agent tasks or produce the requested professional work products."
      ],
      "status": "不适用"
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "不适用：transcription output is not the general academic question-answering capability evaluated by HLE."
      ],
      "status": "不适用"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "不适用：the model accepts audio only and has no screenshot input or GUI-action interface."
      ],
      "status": "不适用"
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Cohere Transcribe exact model card",
          "url": "https://huggingface.co/CohereLabs/cohere-transcribe-03-2026"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "不适用：the model transcribes audio into text and does not edit source-code repositories."
      ],
      "status": "不适用"
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        }
      ],
      "notes": [
        "不适用：the model has no terminal-action interface for the science workflows."
      ],
      "status": "不适用"
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "不适用：the ASR interface does not provide code generation or terminal task execution."
      ],
      "status": "不适用"
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Cohere Transcribe documentation",
          "url": "https://docs.cohere.com/docs/transcribe"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：the ASR model does not provide the general tool-agent behavior required for finance, coding, legal, and tax tasks."
      ],
      "status": "不适用"
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:38+08:00",
  "model_id": "cohere/cohere-transcribe-03-2026",
  "model_notes": [
    "Cohere’s official model documentation identifies the exact model name cohere-transcribe-03-2026 as a 2B automatic speech recognition model with audio input and text transcription output across 14 languages.",
    "The model exposes speech transcription, not code generation, general question answering, visual understanding, GUI actions, or tool-agent behavior; no target benchmark result was added."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
