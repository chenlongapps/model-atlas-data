# OmniVoice Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：k2-fsa/omnivoice
- 模型名称：OmniVoice
- 发布日期：2026-03-30
- 最近检查时间：2026-11-05T10:34+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- The exact checkpoint k2-fsa/OmniVoice is documented as a multilingual zero-shot text-to-speech model; text and optional reference audio are inputs, and generated audio is the output.
- This checkpoint exposes speech generation rather than code, text-answer, vision, desktop-action, or general tool-agent behavior; all 11 target benchmarks were assessed as not applicable.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05 |
| swe-bench-pro-v2 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05 |
| terminal-bench-v4 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks) | 2026-11-05 |
| terminal-bench-science-v0.1 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/) | 2026-11-05 |
| automationbench-v1.0.6 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05 |
| osworld-v2.1 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [OSWorld-V2 project](https://osworld-v2.xlang.ai/) | 2026-11-05 |
| chartography | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05 |
| humanitys-last-exam | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05 |
| gdpval-aa-v2.1 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05 |
| vals-index-v2.2 | 不适用 | — | [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 不适用：OmniVoice generates speech audio and has no software-code or terminal-agent output interface.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：the model is a speech-generation checkpoint, not a repository code-editing model.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)

研究备注：
- 不适用：the checkpoint has no text/code completion or terminal-execution interface.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)

研究备注：
- 不适用：speech synthesis does not provide terminal task execution or the testable software outputs required by this benchmark.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 不适用：the model is a TTS generator and has no tool interface for executing cross-application workflows.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)

研究备注：
- 不适用：the model has no desktop screenshot input or GUI-action interface.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 不适用：the checkpoint does not accept chart images or return text answers for visual question answering.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 不适用：the model outputs generated speech rather than the scored text answers required by HLE.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 不适用：the V5 index evaluates general language-model capabilities; OmniVoice is a specialized audio-generation model.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 不适用：speech generation cannot produce the professional work products and agent workflow required by GDPval-AA.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [k2-fsa OmniVoice model card](https://huggingface.co/k2-fsa/OmniVoice)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：the model does not expose a text-agent workflow for the finance, coding, legal, and tax tasks in Vals Index.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "不适用：the V5 index evaluates general language-model capabilities; OmniVoice is a specialized audio-generation model."
      ],
      "status": "不适用"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "不适用：the model is a TTS generator and has no tool interface for executing cross-application workflows."
      ],
      "status": "不适用"
    },
    "chartography": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "不适用：the checkpoint does not accept chart images or return text answers for visual question answering."
      ],
      "status": "不适用"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "不适用：OmniVoice generates speech audio and has no software-code or terminal-agent output interface."
      ],
      "status": "不适用"
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "不适用：speech generation cannot produce the professional work products and agent workflow required by GDPval-AA."
      ],
      "status": "不适用"
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "不适用：the model outputs generated speech rather than the scored text answers required by HLE."
      ],
      "status": "不适用"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "不适用：the model has no desktop screenshot input or GUI-action interface."
      ],
      "status": "不适用"
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "不适用：the model is a speech-generation checkpoint, not a repository code-editing model."
      ],
      "status": "不适用"
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        }
      ],
      "notes": [
        "不适用：speech synthesis does not provide terminal task execution or the testable software outputs required by this benchmark."
      ],
      "status": "不适用"
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "不适用：the checkpoint has no text/code completion or terminal-execution interface."
      ],
      "status": "不适用"
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "k2-fsa OmniVoice model card",
          "url": "https://huggingface.co/k2-fsa/OmniVoice"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：the model does not expose a text-agent workflow for the finance, coding, legal, and tax tasks in Vals Index."
      ],
      "status": "不适用"
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:34+08:00",
  "model_id": "k2-fsa/omnivoice",
  "model_notes": [
    "The exact checkpoint k2-fsa/OmniVoice is documented as a multilingual zero-shot text-to-speech model; text and optional reference audio are inputs, and generated audio is the output.",
    "This checkpoint exposes speech generation rather than code, text-answer, vision, desktop-action, or general tool-agent behavior; all 11 target benchmarks were assessed as not applicable."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
