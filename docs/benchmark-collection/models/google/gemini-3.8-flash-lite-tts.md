# Gemini 3.8 Flash Lite TTS Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.8-flash-lite-tts
- 模型名称：Gemini 3.8 Flash Lite TTS
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T07:55+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [DeepSWE official leaderboard/protocol](https://deepswe.datacurve.ai/) | 2026-11-04T07:55+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Scale SWE-bench Pro V2 leaderboard/protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T07:55+08:00 |
| terminal-bench-v4 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Terminal-Bench 4.0 official specification](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T07:55+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Terminal-Bench-Science official repository](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T07:55+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Zapier AutomationBench official protocol](https://github.com/zapier/AutomationBench) | 2026-11-04T07:55+08:00 |
| osworld-v2.1 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md) | 2026-11-04T07:55+08:00 |
| chartography | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Surge Chartography official protocol](https://github.com/surge-ai/chartography) | 2026-11-04T07:55+08:00 |
| humanitys-last-exam | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Humanity’s Last Exam evaluation description](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T07:55+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T07:55+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [GDPval-AA v2.1 evaluation description](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T07:55+08:00 |
| vals-index-v2.2 | 不适用 | — | [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts), [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation), [Vals Index v2.2 benchmark description](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T07:55+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [DeepSWE official leaderboard/protocol](https://deepswe.datacurve.ai/)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- DeepSWE evaluates coding agents on long-horizon software engineering tasks and requires verifiable code changes.

最近核验时间：2026-11-04T07:55+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Scale SWE-bench Pro V2 leaderboard/protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- SWE-bench Pro V2 requires solving code repository issues and returning patches evaluated against tests.

最近核验时间：2026-11-04T07:55+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Terminal-Bench 4.0 official specification](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- Terminal-Bench 4 evaluates agents executing tasks in a sandboxed terminal.

最近核验时间：2026-11-04T07:55+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Terminal-Bench-Science official repository](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- Terminal-Bench-Science requires an agent to carry out terminal-based research workflows and return test-verifiable artifacts.

最近核验时间：2026-11-04T07:55+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Zapier AutomationBench official protocol](https://github.com/zapier/AutomationBench)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- AutomationBench requires an agent to use tools across simulated business applications and is scored on resulting application state.

最近核验时间：2026-11-04T07:55+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- OSWorld is a computer-use benchmark; this SKU cannot perceive desktop screenshots or issue computer actions.

最近核验时间：2026-11-04T07:55+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Surge Chartography official protocol](https://github.com/surge-ai/chartography)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- Chartography requires reading chart images and submitting text answers; this SKU accepts no image input and emits no text answer.

最近核验时间：2026-11-04T07:55+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Humanity’s Last Exam evaluation description](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- HLE is scored from multiple-choice or short-answer responses; audio-only output cannot be submitted as the target text answer.

最近核验时间：2026-11-04T07:55+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- The composite includes language, coding, terminal, knowledge-work and agent evaluations that require text responses or executable actions.

最近核验时间：2026-11-04T07:55+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [GDPval-AA v2.1 evaluation description](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- GDPval-AA runs an agent harness with shell and browser access and expects deliverables such as documents, slides, diagrams, or spreadsheets.

最近核验时间：2026-11-04T07:55+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini 3.8 Flash-Lite TTS model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts)
- [Google TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Vals Index v2.2 benchmark description](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.
- Vals Index v2.2 aggregates agent work across finance, coding, legal and tax tasks; an audio-only TTS response is not a compatible submission.

最近核验时间：2026-11-04T07:55+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "The composite includes language, coding, terminal, knowledge-work and agent evaluations that require text responses or executable actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Zapier AutomationBench official protocol",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "AutomationBench requires an agent to use tools across simulated business applications and is scored on resulting application state."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Surge Chartography official protocol",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "Chartography requires reading chart images and submitting text answers; this SKU accepts no image input and emits no text answer."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "DeepSWE official leaderboard/protocol",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "DeepSWE evaluates coding agents on long-horizon software engineering tasks and requires verifiable code changes."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "GDPval-AA v2.1 evaluation description",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "GDPval-AA runs an agent harness with shell and browser access and expects deliverables such as documents, slides, diagrams, or spreadsheets."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Humanity’s Last Exam evaluation description",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "HLE is scored from multiple-choice or short-answer responses; audio-only output cannot be submitted as the target text answer."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "OSWorld is a computer-use benchmark; this SKU cannot perceive desktop screenshots or issue computer actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard/protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "SWE-bench Pro V2 requires solving code repository issues and returning patches evaluated against tests."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Terminal-Bench-Science official repository",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "Terminal-Bench-Science requires an agent to carry out terminal-based research workflows and return test-verifiable artifacts."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Terminal-Bench 4.0 official specification",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "Terminal-Bench 4 evaluates agents executing tasks in a sandboxed terminal."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T07:55+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.8 Flash-Lite TTS model documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts"
        },
        {
          "label": "Google TTS documentation",
          "url": "https://ai.google.dev/gemini-api/docs/speech-generation"
        },
        {
          "label": "Vals Index v2.2 benchmark description",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Google identifies gemini-3.8-flash-lite-tts as text-to-speech: it accepts text only and emits audio only; it has no reasoning or tool-calling support. This benchmark requires a text answer, executable agent action, image understanding, or structured work product, so the SKU is not applicable.",
        "Vals Index v2.2 aggregates agent work across finance, coding, legal and tax tasks; an audio-only TTS response is not a compatible submission."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T07:55+08:00",
  "model_id": "google/gemini-3.8-flash-lite-tts",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
