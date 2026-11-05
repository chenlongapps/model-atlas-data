# Voxtral Mini TTS Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/voxtral-mini-tts-2603
- 模型名称：Voxtral Mini TTS
- 发布日期：2026-03-23
- 最近检查时间：2026-11-05T10:45+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Mistral’s official page identifies voxtral-mini-tts-2603 as a March 23, 2026 text-to-speech and voice-cloning model. It accepts text and generates audio; Mistral later deprecated this version on October 31, 2026.
- The model is a specialized TTS generator without code, vision, GUI-action, reasoning, or tool-calling interfaces; no target benchmark result was added.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Voxtral TTS exact model card](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05 |
| swe-bench-pro-v2 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05 |
| terminal-bench-v4 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks) | 2026-11-05 |
| terminal-bench-science-v0.1 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/) | 2026-11-05 |
| automationbench-v1.0.6 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05 |
| osworld-v2.1 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [OSWorld-V2 project](https://osworld-v2.xlang.ai/) | 2026-11-05 |
| chartography | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05 |
| humanitys-last-exam | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05 |
| gdpval-aa-v2.1 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05 |
| vals-index-v2.2 | 不适用 | — | [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Voxtral TTS exact model card](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 不适用：the model generates speech audio rather than code changes or terminal-agent outputs.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：the model has no repository code-editing interface.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)

研究备注：
- 不适用：the model has no code generation or terminal execution interface.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)

研究备注：
- 不适用：speech synthesis does not expose terminal actions for science workflows.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 不适用：the model generates speech from text and has no tool-calling interface to execute workflows.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)

研究备注：
- 不适用：the text-in/audio-out model has no visual screen input or GUI-action interface.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 不适用：the model does not accept images or answer visual chart questions.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 不适用：the model generates speech from text and does not provide the general academic answers evaluated by HLE.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 不适用：the model is a dedicated speech-generation model, not a general reasoning model for the V5 index.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 不适用：the model cannot carry out GDPval-AA agent workflows or create the required professional work products.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Mistral Voxtral TTS model documentation](https://docs.mistral.ai/models/voxtral-tts-26-03)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：the model does not provide the text-agent capability required for finance, coding, legal, and tax tasks.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "不适用：the model is a dedicated speech-generation model, not a general reasoning model for the V5 index."
      ],
      "status": "不适用"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "不适用：the model generates speech from text and has no tool-calling interface to execute workflows."
      ],
      "status": "不适用"
    },
    "chartography": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "不适用：the model does not accept images or answer visual chart questions."
      ],
      "status": "不适用"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Voxtral TTS exact model card",
          "url": "https://huggingface.co/mistralai/Voxtral-4B-TTS-2603"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "不适用：the model generates speech audio rather than code changes or terminal-agent outputs."
      ],
      "status": "不适用"
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "不适用：the model cannot carry out GDPval-AA agent workflows or create the required professional work products."
      ],
      "status": "不适用"
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "不适用：the model generates speech from text and does not provide the general academic answers evaluated by HLE."
      ],
      "status": "不适用"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "不适用：the text-in/audio-out model has no visual screen input or GUI-action interface."
      ],
      "status": "不适用"
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "不适用：the model has no repository code-editing interface."
      ],
      "status": "不适用"
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        }
      ],
      "notes": [
        "不适用：speech synthesis does not expose terminal actions for science workflows."
      ],
      "status": "不适用"
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "不适用：the model has no code generation or terminal execution interface."
      ],
      "status": "不适用"
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mistral Voxtral TTS model documentation",
          "url": "https://docs.mistral.ai/models/voxtral-tts-26-03"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：the model does not provide the text-agent capability required for finance, coding, legal, and tax tasks."
      ],
      "status": "不适用"
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:45+08:00",
  "model_id": "mistral/voxtral-mini-tts-2603",
  "model_notes": [
    "Mistral’s official page identifies voxtral-mini-tts-2603 as a March 23, 2026 text-to-speech and voice-cloning model. It accepts text and generates audio; Mistral later deprecated this version on October 31, 2026.",
    "The model is a specialized TTS generator without code, vision, GUI-action, reasoning, or tool-calling interfaces; no target benchmark result was added."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
