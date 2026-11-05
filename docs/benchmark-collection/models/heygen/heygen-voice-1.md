# HeyGen Voice Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：heygen/heygen-voice-1
- 模型名称：HeyGen Voice
- 发布日期：2026-10-13
- 最近检查时间：2026-11-04T03:03+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T03:03+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [SWE-bench Pro V2 leaderboard and protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-04T03:03+08:00 |
| terminal-bench-v4 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Terminal-Bench 4 announcement](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T03:03+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Terminal-Bench Science v0.1 announcement](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T03:03+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks) | 2026-11-04T03:03+08:00 |
| osworld-v2.1 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T03:03+08:00 |
| chartography | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Chartography paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T03:03+08:00 |
| humanitys-last-exam | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Scale AI HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Humanity’s Last Exam official site](https://lastexam.ai/) | 2026-11-04T03:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis model overview](https://artificialanalysis.ai/models/) | 2026-11-04T03:03+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T03:03+08:00 |
| vals-index-v2.2 | 不适用 | — | [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1), [Vals Index V2.2 methodology and leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T03:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- The model is a text-to-speech/speech-to-speech voice model that returns audio; DeepSWE requires a code patch that can be verified in a repository environment.

最近核验时间：2026-11-04T03:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [SWE-bench Pro V2 leaderboard and protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- The model returns audio and has no coding agent interface; SWE-bench Pro V2 evaluates repository code patches against tests.

最近核验时间：2026-11-04T03:03+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Terminal-Bench 4 announcement](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The model has no terminal or tool interface; Terminal-Bench 4 evaluates agents executing terminal tasks.

最近核验时间：2026-11-04T03:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Terminal-Bench Science v0.1 announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- The model returns generated speech and does not execute the scientific terminal workflows or produce the verified artifacts required by this benchmark.

最近核验时间：2026-11-04T03:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks)

研究备注：
- AutomationBench requires tool-mediated cross-application workflows evaluated by their resulting application state; this speech model has no such action interface.

最近核验时间：2026-11-04T03:03+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld requires an agent to observe and operate a desktop environment; the model accepts text and emits audio and has no GUI action interface.

最近核验时间：2026-11-04T03:03+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Chartography paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Chartography requires chart-image understanding and free-form text answers; the documented model API emits audio and is not a chart-question-answering interface.

最近核验时间：2026-11-04T03:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Scale AI HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Humanity’s Last Exam official site](https://lastexam.ai/)

研究备注：
- The original HLE evaluates academic question answering; the model emits speech audio rather than a text answer and exposes no reasoning capability.

最近核验时间：2026-11-04T03:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis model overview](https://artificialanalysis.ai/models/)

研究备注：
- The V5 suite is a primarily text-based language-model evaluation; the target is an audio-generation model, not a text reasoning or agent model.

最近核验时间：2026-11-04T03:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA uses an agent workflow to produce professional work artifacts; this API accepts text and returns speech audio without the needed tools or artifact output.

最近核验时间：2026-11-04T03:03+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Voice 1 official model page](https://www.heygen.com/models/heygen-voice-1)
- [Vals Index V2.2 methodology and leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index measures agentic finance, coding, legal, and tax work; a speech-generation endpoint cannot perform or submit the evaluated professional tasks.

最近核验时间：2026-11-04T03:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis model overview",
          "url": "https://artificialanalysis.ai/models/"
        }
      ],
      "notes": [
        "The V5 suite is a primarily text-based language-model evaluation; the target is an audio-generation model, not a text reasoning or agent model."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Zapier AutomationBench leaderboard and protocol",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench requires tool-mediated cross-application workflows evaluated by their resulting application state; this speech model has no such action interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "Chartography requires chart-image understanding and free-form text answers; the documented model API emits audio and is not a chart-question-answering interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "The model is a text-to-speech/speech-to-speech voice model that returns audio; DeepSWE requires a code patch that can be verified in a repository environment."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA uses an agent workflow to produce professional work artifacts; this API accepts text and returns speech audio without the needed tools or artifact output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Scale AI HLE leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Humanity’s Last Exam official site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "The original HLE evaluates academic question answering; the model emits speech audio rather than a text answer and exposes no reasoning capability."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld requires an agent to observe and operate a desktop environment; the model accepts text and emits audio and has no GUI action interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard and protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "The model returns audio and has no coding agent interface; SWE-bench Pro V2 evaluates repository code patches against tests."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Terminal-Bench Science v0.1 announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "The model returns generated speech and does not execute the scientific terminal workflows or produce the verified artifacts required by this benchmark."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Terminal-Bench 4 announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The model has no terminal or tool interface; Terminal-Bench 4 evaluates agents executing terminal tasks."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T03:03+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Voice 1 official model page",
          "url": "https://www.heygen.com/models/heygen-voice-1"
        },
        {
          "label": "Vals Index V2.2 methodology and leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index measures agentic finance, coding, legal, and tax work; a speech-generation endpoint cannot perform or submit the evaluated professional tasks."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T03:03+08:00",
  "model_id": "heygen/heygen-voice-1",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
