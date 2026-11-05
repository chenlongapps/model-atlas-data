# HeyGen Voice Turbo Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：heygen/heygen-voice-1-turbo
- 模型名称：HeyGen Voice Turbo
- 发布日期：2026-10-13
- 最近检查时间：2026-11-04T03:04+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [DeepSWE v1.1 protocol](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T03:04+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [SWE-bench Pro V2 protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-04T03:04+08:00 |
| terminal-bench-v4 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Terminal-Bench 4 protocol](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T03:04+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Terminal-Bench Science v0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T03:04+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Zapier AutomationBench protocol](https://zapier.com/benchmarks) | 2026-11-04T03:04+08:00 |
| osworld-v2.1 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T03:04+08:00 |
| chartography | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Chartography protocol paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T03:04+08:00 |
| humanitys-last-exam | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Scale HLE official leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T03:04+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Artificial Analysis V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T03:04+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Artificial Analysis GDPval-AA evaluation protocol](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T03:04+08:00 |
| vals-index-v2.2 | 不适用 | — | [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1), [Vals Index V2.2 methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T03:04+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [DeepSWE v1.1 protocol](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Turbo is a text-to-speech endpoint that returns audio; DeepSWE requires a verifiable code patch from an engineering agent.

最近核验时间：2026-11-04T03:04+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [SWE-bench Pro V2 protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- SWE-bench Pro V2 requires a code patch tested against a repository; Turbo provides speech generation and no coding/tool interface.

最近核验时间：2026-11-04T03:04+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Terminal-Bench 4 protocol](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The benchmark requires terminal-agent execution, which the audio-generating Turbo API does not expose.

最近核验时间：2026-11-04T03:04+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Terminal-Bench Science v0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- The benchmark requires scientific terminal workflows and verifiable work artifacts; Turbo returns audio and has no terminal interface.

最近核验时间：2026-11-04T03:04+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Zapier AutomationBench protocol](https://zapier.com/benchmarks)

研究备注：
- AutomationBench requires tool-mediated cross-application workflows scored by final app state; Turbo is a speech component, not a workflow agent.

最近核验时间：2026-11-04T03:04+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld requires screenshot-based desktop interaction; Turbo has no image input or desktop-action output.

最近核验时间：2026-11-04T03:04+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Chartography protocol paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Chartography requires chart-image input and free-form text answers; Turbo outputs audio. The HeyGen image-conditioned feature is for speech-scene adaptation, not documented chart QA.

最近核验时间：2026-11-04T03:04+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Scale HLE official leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- The original HLE is a text-answer academic reasoning evaluation; Turbo is audio-output TTS and has no text-answer reasoning interface.

最近核验时间：2026-11-04T03:04+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Artificial Analysis V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The V5 composite is a primarily text-based language-model evaluation suite; Turbo is a speech-generation endpoint.

最近核验时间：2026-11-04T03:04+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Artificial Analysis GDPval-AA evaluation protocol](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires an agent loop and professional text/file artifacts; Turbo only returns audio and has no tools.

最近核验时间：2026-11-04T03:04+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice model family and API page](https://www.heygen.com/models/heygen-voice-1)
- [Vals Index V2.2 methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index evaluates agentic finance, coding, legal, and tax work; Turbo cannot perform or submit those tasks.

最近核验时间：2026-11-04T03:04+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Artificial Analysis V5 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The V5 composite is a primarily text-based language-model evaluation suite; Turbo is a speech-generation endpoint."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Zapier AutomationBench protocol",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench requires tool-mediated cross-application workflows scored by final app state; Turbo is a speech component, not a workflow agent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Chartography protocol paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "Chartography requires chart-image input and free-form text answers; Turbo outputs audio. The HeyGen image-conditioned feature is for speech-scene adaptation, not documented chart QA."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "DeepSWE v1.1 protocol",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Turbo is a text-to-speech endpoint that returns audio; DeepSWE requires a verifiable code patch from an engineering agent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Artificial Analysis GDPval-AA evaluation protocol",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires an agent loop and professional text/file artifacts; Turbo only returns audio and has no tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Scale HLE official leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "The original HLE is a text-answer academic reasoning evaluation; Turbo is audio-output TTS and has no text-answer reasoning interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld requires screenshot-based desktop interaction; Turbo has no image input or desktop-action output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires a code patch tested against a repository; Turbo provides speech generation and no coding/tool interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Terminal-Bench Science v0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "The benchmark requires scientific terminal workflows and verifiable work artifacts; Turbo returns audio and has no terminal interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Terminal-Bench 4 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The benchmark requires terminal-agent execution, which the audio-generating Turbo API does not expose."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T03:04+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice model family and API page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Vals Index V2.2 methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index evaluates agentic finance, coding, legal, and tax work; Turbo cannot perform or submit those tasks."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T03:04+08:00",
  "model_id": "heygen/heygen-voice-1-turbo",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
