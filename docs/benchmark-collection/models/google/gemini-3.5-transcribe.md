# Gemini 3.5 Transcribe Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.5-transcribe
- 模型名称：Gemini 3.5 Transcribe
- 发布日期：2026-08-26
- 最近检查时间：2026-11-04T15:41+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [DeepSWE v1.1 benchmark](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T15:41+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T15:41+08:00 |
| terminal-bench-v4 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T15:41+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T15:41+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Zapier AutomationBench](https://zapier.com/benchmarks) | 2026-11-04T15:41+08:00 |
| osworld-v2.1 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [OSWorld V2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T15:41+08:00 |
| chartography | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Surge AI Chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T15:41+08:00 |
| humanitys-last-exam | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Humanity’s Last Exam](https://lastexam.ai/) | 2026-11-04T15:41+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T15:41+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T15:41+08:00 |
| vals-index-v2.2 | 不适用 | — | [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe), [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe), [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T15:41+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [DeepSWE v1.1 benchmark](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE evaluates software-engineering agents. Gemini 3.5 Transcribe accepts audio and returns transcript text; it does not support thinking, function calling, or code execution. This task is outside the model’s declared purpose.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 requires an agent to produce code patches and pass repository tests. This transcription model does not support code execution or function calling.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench evaluates terminal task execution; the exact model is audio transcription and has no code execution or function-calling support.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench-Science requires terminal-based scientific workflows. This model only transcribes audio and has no terminal or code-execution capability.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Zapier AutomationBench](https://zapier.com/benchmarks)

研究备注：
- AutomationBench evaluates tool-using agents that complete cross-application workflows. The exact model does not support function calling and is designed for speech transcription.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [OSWorld V2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- OSWorld requires visual perception and long-horizon desktop interaction. This model accepts audio only and does not provide computer-use tools.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Surge AI Chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography requires chart-image input and visual chart reasoning. This exact model accepts audio only and outputs transcription text.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Humanity’s Last Exam](https://lastexam.ai/)

研究备注：
- HLE measures academic question answering and reasoning. This exact model is documented only for speech-to-text transcription and explicitly does not support thinking.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- AA Intelligence Index V5 combines knowledge, reasoning, coding, scientific and agentic evaluations. This exact model is an audio transcription endpoint without reasoning, function calling, or code execution.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires agentic professional-work tasks and deliverable production via shell and web tools. This exact model accepts audio for transcription and does not support those capabilities.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.5 Transcribe model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe)
- [Google audio transcription guide](https://ai.google.dev/gemini-api/docs/transcribe)
- [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index measures finance, coding, legal, and tax agent performance. The exact model is a transcription endpoint without reasoning or tool calling.
- No compatible exact-model score was recorded; results for other Gemini models were not transferred.

最近核验时间：2026-11-04T15:41+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "AA Intelligence Index V5 combines knowledge, reasoning, coding, scientific and agentic evaluations. This exact model is an audio transcription endpoint without reasoning, function calling, or code execution.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Zapier AutomationBench",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench evaluates tool-using agents that complete cross-application workflows. The exact model does not support function calling and is designed for speech transcription.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Surge AI Chartography",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography requires chart-image input and visual chart reasoning. This exact model accepts audio only and outputs transcription text.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "DeepSWE v1.1 benchmark",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE evaluates software-engineering agents. Gemini 3.5 Transcribe accepts audio and returns transcript text; it does not support thinking, function calling, or code execution. This task is outside the model’s declared purpose.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires agentic professional-work tasks and deliverable production via shell and web tools. This exact model accepts audio for transcription and does not support those capabilities.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Humanity’s Last Exam",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "HLE measures academic question answering and reasoning. This exact model is documented only for speech-to-text transcription and explicitly does not support thinking.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "OSWorld V2.1 release record",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "OSWorld requires visual perception and long-horizon desktop interaction. This model accepts audio only and does not provide computer-use tools.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires an agent to produce code patches and pass repository tests. This transcription model does not support code execution or function calling.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Terminal-Bench-Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench-Science requires terminal-based scientific workflows. This model only transcribes audio and has no terminal or code-execution capability.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench evaluates terminal task execution; the exact model is audio transcription and has no code execution or function-calling support.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T15:41+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 Transcribe model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe"
        },
        {
          "label": "Google audio transcription guide",
          "url": "https://ai.google.dev/gemini-api/docs/transcribe"
        },
        {
          "label": "Vals Index v2.2",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index measures finance, coding, legal, and tax agent performance. The exact model is a transcription endpoint without reasoning or tool calling.",
        "No compatible exact-model score was recorded; results for other Gemini models were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T15:41+08:00",
  "model_id": "google/gemini-3.5-transcribe",
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
