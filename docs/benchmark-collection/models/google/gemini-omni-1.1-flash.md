# Gemini Omni 1.1 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-omni-1.1-flash
- 模型名称：Gemini Omni 1.1 Flash
- 发布日期：2026-08-27
- 最近检查时间：2026-11-04T15:26+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T15:26+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T15:26+08:00 |
| terminal-bench-v4 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T15:26+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T15:26+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Zapier AutomationBench](https://zapier.com/benchmarks) | 2026-11-04T15:26+08:00 |
| osworld-v2.1 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Google Gemini Omni API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [OSWorld V2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T15:26+08:00 |
| chartography | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Surge AI Chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T15:26+08:00 |
| humanitys-last-exam | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Humanity’s Last Exam official page](https://lastexam.ai/) | 2026-11-04T15:26+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T15:26+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T15:26+08:00 |
| vals-index-v2.2 | 不适用 | — | [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/), [Vals AI Index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T15:26+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE evaluates long-horizon software-engineering agents. This exact model is documented for video generation/editing and outputs video; it has no coding-agent tool interface.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 requires an agent to produce a code patch and pass repository tests. This exact model outputs video and does not support tool calling.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench requires an agent to work in a terminal. The model TOML marks tools unsupported, and the official model card documents video output.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench-Science requires terminal-based scientific workflows and verifiable code/data outputs; this model is a video generator/editor with no tool interface.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Zapier AutomationBench](https://zapier.com/benchmarks)

研究备注：
- Zapier AutomationBench evaluates agents completing multi-step SaaS workflows. This exact model outputs video and has no supported tool interface.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Google Gemini Omni API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [OSWorld V2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- OSWorld requires long-horizon interaction with desktop applications. This exact model outputs video and does not support tool calling.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Surge AI Chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography requires visual chart interpretation followed by an answer scored for accuracy. The model accepts visual input but outputs video, so the required answer format is unsupported.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Humanity’s Last Exam official page](https://lastexam.ai/)

研究备注：
- HLE requires textual answers to academic questions. The official model card documents video output rather than answer text for this exact model.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- The Intelligence Index aggregates language-model reasoning, knowledge, coding, and agentic evaluations. The exact model is a video generation/editing model with video output; it is not an applicable language-model configuration.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires agentic professional-work deliverables such as documents, slides, diagrams, and spreadsheets. This exact model outputs video and does not support tool calling.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)
- [Vals AI Index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index aggregates agent performance in finance, coding, legal, and tax tasks. This exact model is a video output model without a supported tool interface.
- No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred.

最近核验时间：2026-11-04T15:26+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "The Intelligence Index aggregates language-model reasoning, knowledge, coding, and agentic evaluations. The exact model is a video generation/editing model with video output; it is not an applicable language-model configuration.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Zapier AutomationBench",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Zapier AutomationBench evaluates agents completing multi-step SaaS workflows. This exact model outputs video and has no supported tool interface.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Surge AI Chartography",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography requires visual chart interpretation followed by an answer scored for accuracy. The model accepts visual input but outputs video, so the required answer format is unsupported.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE evaluates long-horizon software-engineering agents. This exact model is documented for video generation/editing and outputs video; it has no coding-agent tool interface.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires agentic professional-work deliverables such as documents, slides, diagrams, and spreadsheets. This exact model outputs video and does not support tool calling.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Humanity’s Last Exam official page",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "HLE requires textual answers to academic questions. The official model card documents video output rather than answer text for this exact model.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Google Gemini Omni API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "label": "OSWorld V2.1 release record",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "OSWorld requires long-horizon interaction with desktop applications. This exact model outputs video and does not support tool calling.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires an agent to produce a code patch and pass repository tests. This exact model outputs video and does not support tool calling.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Terminal-Bench-Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench-Science requires terminal-based scientific workflows and verifiable code/data outputs; this model is a video generator/editor with no tool interface.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench requires an agent to work in a terminal. The model TOML marks tools unsupported, and the official model card documents video output.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T15:26+08:00",
      "checked_sources": [
        {
          "label": "Google DeepMind model card",
          "url": "https://deepmind.google/models/model-cards/gemini-omni-flash/"
        },
        {
          "label": "Vals AI Index",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index aggregates agent performance in finance, coding, legal, and tax tasks. This exact model is a video output model without a supported tool interface.",
        "No compatible exact-model result was recorded; scores from other Gemini model IDs were not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T15:26+08:00",
  "model_id": "google/gemini-omni-1.1-flash",
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
