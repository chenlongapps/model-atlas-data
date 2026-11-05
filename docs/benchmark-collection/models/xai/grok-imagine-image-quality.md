# Grok Imagine Image Quality Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-imagine-image-quality
- 模型名称：Grok Imagine Image Quality
- 发布日期：2026-04-03
- 最近检查时间：2026-11-05T09:54+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- The repository model is the historical dated alias grok-imagine-image-quality-20260403. xAI retired the generic slug on 2026-11-02 and now routes it to grok-imagine-image-2.0 at low quality; that redirected endpoint is a different model version.
- The xAI Image Arena Quality Elo is not one of the 11 target benchmarks. No target benchmark score row existed in the TOML, and none was added.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T09:54+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T09:54+08:00 |
| terminal-bench-v4 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T09:54+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Terminal-Bench Science v0.1.0](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) | 2026-11-05T09:54+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-05T09:54+08:00 |
| osworld-v2.1 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T09:54+08:00 |
| chartography | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Chartography benchmark repository](https://github.com/surge-ai/chartography) | 2026-11-05T09:54+08:00 |
| humanitys-last-exam | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Humanity’s Last Exam](https://lastexam.ai/) | 2026-11-05T09:54+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Artificial Analysis Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:54+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:54+08:00 |
| vals-index-v2.2 | 不适用 | — | [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation), [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2), [Vals Index v2.2 methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T09:54+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- The model generates or edits images and does not provide coding-agent text or repository-patch output.

最近核验时间：2026-11-05T09:54+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 measures code-repository repair; this endpoint returns images rather than code changes.

最近核验时间：2026-11-05T09:54+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The image-generation endpoint has no terminal execution interface.

最近核验时间：2026-11-05T09:54+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Terminal-Bench Science v0.1.0](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)

研究备注：
- The benchmark requires scientific task execution in a terminal; this model generates or edits images.

最近核验时间：2026-11-05T09:54+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench requires an agent to execute workflows using tools; the image endpoint has no function-calling capability.

最近核验时间：2026-11-05T09:54+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Although the endpoint accepts image input, it generates images and does not operate a desktop or return action-control output.

最近核验时间：2026-11-05T09:54+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Chartography benchmark repository](https://github.com/surge-ai/chartography)

研究备注：
- The endpoint is an image generation/editing model and returns images; Chartography requires chart-question-answering responses.

最近核验时间：2026-11-05T09:54+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Humanity’s Last Exam](https://lastexam.ai/)

研究备注：
- The endpoint returns images rather than answers to academic questions.

最近核验时间：2026-11-05T09:54+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Artificial Analysis Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The index evaluates language-model reasoning, agentic tasks, coding, and science; this endpoint only generates or edits images.

最近核验时间：2026-11-05T09:54+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- GDPval-AA requires agentic professional work with file outputs; this endpoint returns generated images.

最近核验时间：2026-11-05T09:54+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [xAI model documentation](https://docs.x.ai/developers/model-capabilities/images/generation)
- [xAI retirement and redirect notice (effective Nov 2, 2026)](https://docs.x.ai/developers/migration/imagine-image-quality-nov-2)
- [Vals Index v2.2 methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index measures finance, coding, legal, and tax agent tasks; this image-generation endpoint does not produce those work outputs.

最近核验时间：2026-11-05T09:54+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The index evaluates language-model reasoning, agentic tasks, coding, and science; this endpoint only generates or edits images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench requires an agent to execute workflows using tools; the image endpoint has no function-calling capability."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Chartography benchmark repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "The endpoint is an image generation/editing model and returns images; Chartography requires chart-question-answering responses."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "DeepSWE v1.1",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "The model generates or edits images and does not provide coding-agent text or repository-patch output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "GDPval-AA requires agentic professional work with file outputs; this endpoint returns generated images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Humanity’s Last Exam",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "The endpoint returns images rather than answers to academic questions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Although the endpoint accepts image input, it generates images and does not operate a desktop or return action-control output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 measures code-repository repair; this endpoint returns images rather than code changes."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Terminal-Bench Science v0.1.0",
          "url": "https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0"
        }
      ],
      "notes": [
        "The benchmark requires scientific task execution in a terminal; this model generates or edits images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The image-generation endpoint has no terminal execution interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T09:54+08:00",
      "checked_sources": [
        {
          "label": "xAI model documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/images/generation"
        },
        {
          "label": "xAI retirement and redirect notice (effective Nov 2, 2026)",
          "url": "https://docs.x.ai/developers/migration/imagine-image-quality-nov-2"
        },
        {
          "label": "Vals Index v2.2 methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index measures finance, coding, legal, and tax agent tasks; this image-generation endpoint does not produce those work outputs."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T09:54+08:00",
  "model_id": "xai/grok-imagine-image-quality",
  "model_notes": [
    "The repository model is the historical dated alias grok-imagine-image-quality-20260403. xAI retired the generic slug on 2026-11-02 and now routes it to grok-imagine-image-2.0 at low quality; that redirected endpoint is a different model version.",
    "The xAI Image Arena Quality Elo is not one of the 11 target benchmarks. No target benchmark score row existed in the TOML, and none was added."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
