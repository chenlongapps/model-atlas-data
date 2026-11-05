# Lyria 3 Pro Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/lyria-3-pro-preview
- 模型名称：Lyria 3 Pro Preview
- 发布日期：2026-03-25
- 最近检查时间：2026-11-05T10:44+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google Cloud’s official Lyria page confirms the exact `lyria-3-pro-preview` model ID, full-song music generation, text/image input, and a 2026-03-25 release date. The Gemini API model page is titled “Lyria 3 Pro” but its Model code row mistakenly says `lyria-3-clip-preview`; the separate IDs on the Google Cloud page resolve the local model identity.
- The model is a specialized music generator, not a text/code agent; no target benchmark result was added.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05 |
| swe-bench-pro-v2 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05 |
| terminal-bench-v4 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks) | 2026-11-05 |
| terminal-bench-science-v0.1 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/) | 2026-11-05 |
| automationbench-v1.0.6 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05 |
| osworld-v2.1 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [OSWorld-V2 project](https://osworld-v2.xlang.ai/) | 2026-11-05 |
| chartography | 不适用 | — | [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3), [Google music-generation guide](https://ai.google.dev/gemini-api/docs/music-generation), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05 |
| humanitys-last-exam | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Google music-generation guide](https://ai.google.dev/gemini-api/docs/music-generation), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05 |
| gdpval-aa-v2.1 | 不适用 | — | [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview), [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05 |
| vals-index-v2.2 | 不适用 | — | [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 不适用：the model generates full songs rather than code edits or terminal-agent outputs.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：the model has no repository code-editing interface.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)

研究备注：
- 不适用：music generation does not provide code execution or terminal actions.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)

研究备注：
- 不适用：the model has no terminal task interface for the science workflows.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 不适用：the official model page states function calling is not supported.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)

研究备注：
- 不适用：the model is a music generator without function calling or GUI action support.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)
- [Google music-generation guide](https://ai.google.dev/gemini-api/docs/music-generation)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 不适用：although image prompts are accepted, the documented task is image-to-music generation, not chart interpretation or visual question answering.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Google music-generation guide](https://ai.google.dev/gemini-api/docs/music-generation)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 不适用：the model produces music and lyrics rather than general academic answers.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 不适用：this specialized music model does not provide the general knowledge-work, coding, science, and reasoning interface evaluated by V5.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Lyria 3 Pro model page](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview)
- [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 不适用：the model cannot complete GDPval-AA agent tasks or provide the required professional work products.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Google Cloud Lyria model IDs and versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：the model does not provide finance, coding, legal, or tax task-agent behavior.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "不适用：this specialized music model does not provide the general knowledge-work, coding, science, and reasoning interface evaluated by V5."
      ],
      "status": "不适用"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "不适用：the official model page states function calling is not supported."
      ],
      "status": "不适用"
    },
    "chartography": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Cloud Lyria model IDs and versions",
          "url": "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3"
        },
        {
          "label": "Google music-generation guide",
          "url": "https://ai.google.dev/gemini-api/docs/music-generation"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "不适用：although image prompts are accepted, the documented task is image-to-music generation, not chart interpretation or visual question answering."
      ],
      "status": "不适用"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Google Cloud Lyria model IDs and versions",
          "url": "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "不适用：the model generates full songs rather than code edits or terminal-agent outputs."
      ],
      "status": "不适用"
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "不适用：the model cannot complete GDPval-AA agent tasks or provide the required professional work products."
      ],
      "status": "不适用"
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Google music-generation guide",
          "url": "https://ai.google.dev/gemini-api/docs/music-generation"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "不适用：the model produces music and lyrics rather than general academic answers."
      ],
      "status": "不适用"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "不适用：the model is a music generator without function calling or GUI action support."
      ],
      "status": "不适用"
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Google Cloud Lyria model IDs and versions",
          "url": "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3"
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
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        }
      ],
      "notes": [
        "不适用：the model has no terminal task interface for the science workflows."
      ],
      "status": "不适用"
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Lyria 3 Pro model page",
          "url": "https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "不适用：music generation does not provide code execution or terminal actions."
      ],
      "status": "不适用"
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Google Cloud Lyria model IDs and versions",
          "url": "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：the model does not provide finance, coding, legal, or tax task-agent behavior."
      ],
      "status": "不适用"
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:44+08:00",
  "model_id": "google/lyria-3-pro-preview",
  "model_notes": [
    "Google Cloud’s official Lyria page confirms the exact `lyria-3-pro-preview` model ID, full-song music generation, text/image input, and a 2026-03-25 release date. The Gemini API model page is titled “Lyria 3 Pro” but its Model code row mistakenly says `lyria-3-clip-preview`; the separate IDs on the Google Cloud page resolve the local model identity.",
    "The model is a specialized music generator, not a text/code agent; no target benchmark result was added."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
