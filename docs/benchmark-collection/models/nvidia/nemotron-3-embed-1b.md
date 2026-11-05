# Nemotron 3 Embed 1B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3-embed-1b
- 模型名称：Nemotron 3 Embed 1B
- 发布日期：2026-07-16
- 最近检查时间：2026-11-05T00:10+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- NVIDIA documents Nemotron 3 Embed 1B as a text embedding model with embedding-vector output; the source TOML likewise has type=embedding and tools.supported=false. All 11 targets require generated answers, coding work, or agent actions, so they are out of scope for this model.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T00:10+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T00:10+08:00 |
| terminal-bench-v4 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [Terminal-Bench 4.0 methodology](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T00:10+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T00:10+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [AutomationBench repository](https://github.com/zapier/AutomationBench) | 2026-11-05T00:10+08:00 |
| osworld-v2.1 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T00:10+08:00 |
| chartography | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [Chartography official page](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T00:10+08:00 |
| humanitys-last-exam | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T00:10+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T00:10+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T00:10+08:00 |
| vals-index-v2.2 | 不适用 | — | [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard), [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), [Vals Index](https://vals.ai/benchmarks/vals_index) | 2026-11-05T00:10+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- The benchmark requires a coding agent to produce a software patch; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- The benchmark requires a software-engineering agent to produce and verify code patches; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [Terminal-Bench 4.0 methodology](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The benchmark requires an agent to execute terminal tasks; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- The benchmark requires an agent to complete scientific terminal workflows; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)

研究备注：
- The benchmark requires an agent to use API tools and complete workflows; this model emits embeddings and has tools.supported=false. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- The benchmark requires GUI interaction and environment actions; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [Chartography official page](https://surgehq.ai/benchmarks/chartography)

研究备注：
- The benchmark requires visual chart interpretation and answer generation; this model accepts text and emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- The benchmark requires answers to academic questions; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The composite index evaluates language-model knowledge work, coding, science, and general answers; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The benchmark requires an agent to produce professional work products; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA official model card](https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard)
- [NVIDIA Hugging Face model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [Vals Index](https://vals.ai/benchmarks/vals_index)

研究备注：
- The composite index measures agent work across finance, coding, legal, and tax tasks; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists.

最近核验时间：2026-11-05T00:10+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The composite index evaluates language-model knowledge work, coding, science, and general answers; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "The benchmark requires an agent to use API tools and complete workflows; this model emits embeddings and has tools.supported=false. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "Chartography official page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "The benchmark requires visual chart interpretation and answer generation; this model accepts text and emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "The benchmark requires a coding agent to produce a software patch; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The benchmark requires an agent to produce professional work products; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "Humanity's Last Exam",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "The benchmark requires answers to academic questions; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "The benchmark requires GUI interaction and environment actions; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "The benchmark requires a software-engineering agent to produce and verify code patches; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "Terminal-Bench-Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "The benchmark requires an agent to complete scientific terminal workflows; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "Terminal-Bench 4.0 methodology",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The benchmark requires an agent to execute terminal tasks; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T00:10+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard"
        },
        {
          "label": "NVIDIA Hugging Face model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16"
        },
        {
          "label": "Vals Index",
          "url": "https://vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The composite index measures agent work across finance, coding, legal, and tax tasks; this model emits embeddings only. This is a task-scope decision based on model type, not a claim that no public result exists."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T00:10+08:00",
  "model_id": "nvidia/nemotron-3-embed-1b",
  "model_notes": [
    "NVIDIA documents Nemotron 3 Embed 1B as a text embedding model with embedding-vector output; the source TOML likewise has type=embedding and tools.supported=false. All 11 targets require generated answers, coding work, or agent actions, so they are out of scope for this model."
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
