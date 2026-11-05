# Qwen-Image-2.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen-image-2.1
- 模型名称：Qwen-Image-2.1
- 发布日期：2026-09-14
- 最近检查时间：2026-11-04T11:16+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Qwen Image official repository](https://github.com/QwenLM/Qwen-Image-2.1), [DeepSWE v1.1 official method and leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T11:16+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Scale SWE-bench Pro V2 official protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-04T11:16+08:00 |
| terminal-bench-v4 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Terminal-Bench 4 official release and method](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4) | 2026-11-04T11:16+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Terminal-Bench-Science 0.1 official definition](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T11:16+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Zapier AutomationBench official benchmark page](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T11:16+08:00 |
| osworld-v2.1 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [OSWorld v2.1 official evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official leaderboard](https://osworld-v2.xlang.ai/) | 2026-11-04T11:16+08:00 |
| chartography | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Surge Chartography official task specification](https://github.com/surge-ai/chartography), [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T11:16+08:00 |
| humanitys-last-exam | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Artificial Analysis original HLE definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T11:16+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Artificial Analysis Intelligence Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T11:16+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Artificial Analysis GDPval-AA v2.1 method](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T11:16+08:00 |
| vals-index-v2.2 | 不适用 | — | [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Vals Index v2.2 leaderboard and method](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T11:16+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Qwen Image official repository](https://github.com/QwenLM/Qwen-Image-2.1)
- [DeepSWE v1.1 official method and leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE requires a coding agent to modify a repository, submit a patch and run verification. Qwen-Image-2.1 is a text-to-image/image-editing diffusion model whose inference pipeline returns PNG images, so it cannot provide code patches or execution. Local release_date is 2026-09-14 (HF createdAt); the Qwen repo milestone says 2026-09-20, and neither date is an evaluation date.

最近核验时间：2026-11-04T11:16+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Scale SWE-bench Pro V2 official protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- SWE-bench Pro V2 requires a software engineering agent to produce an issue-fixing diff for evaluation in a clean environment. Qwen-Image-2.1 returns images, not code diffs or text.

最近核验时间：2026-11-04T11:16+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Terminal-Bench 4 official release and method](https://www.tbench.ai/news/terminal-bench-4-0)
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4)

研究备注：
- Terminal-Bench 4 requires an agent to operate a Harbor terminal task and submit verifiable task output. This model has no text, terminal or tool interface; its output is an image.

最近核验时间：2026-11-04T11:16+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Terminal-Bench-Science 0.1 official definition](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench-Science evaluates terminal-based research workflows and verified artifacts such as analysis, simulation, proofs, code and data products. Image generation/editing cannot complete those tasks.

最近核验时间：2026-11-04T11:16+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Zapier AutomationBench official benchmark page](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench requires an agent to execute cross-application workflows using 47 tools and is scored by final application state. Qwen-Image-2.1 only generates or edits images and has no tool/workflow output. The leaderboard folds 119 rows after the first 10; N/A is based on interface incompatibility, not on treating those hidden rows as absent.

最近核验时间：2026-11-04T11:16+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [OSWorld v2.1 official evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official leaderboard](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld v2.1 requires GUI interaction, including desktop actions such as mouse/keyboard input. Qwen-Image-2.1 can take an image as an editing condition but returns a generated image, not GUI actions or text.

最近核验时间：2026-11-04T11:16+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Surge Chartography official task specification](https://github.com/surge-ai/chartography)
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography requires a model to answer expert questions about chart images; its response is compared with a reference answer. Qwen-Image-2.1 outputs images, so it cannot submit chart readings or text explanations.

最近核验时间：2026-11-04T11:16+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Artificial Analysis original HLE definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- The original HLE contains 2,500 multimodal questions with multiple-choice and short-answer answers. Qwen-Image-2.1 returns generated images rather than answer text, so it cannot follow the full benchmark response protocol.

最近核验时间：2026-11-04T11:16+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Artificial Analysis Intelligence Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The Intelligence Index composite spans knowledge work, coding, science and general knowledge, requiring text answers and agent outputs. An image-generation/editing model cannot perform that composite protocol.

最近核验时间：2026-11-04T11:16+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Artificial Analysis GDPval-AA v2.1 method](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires shell/web agent access and professional deliverables such as documents, slides, diagrams and spreadsheets. Qwen-Image-2.1 returns images and cannot execute tools or provide the required work products.

最近核验时间：2026-11-04T11:16+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Image-2.1 official model card](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Vals Index v2.2 leaderboard and method](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index is an agentic composite across finance, coding, legal and tax, including terminal work and professional deliverables. Qwen-Image-2.1 cannot execute these workflows or produce the required text/code artifacts.

最近核验时间：2026-11-04T11:16+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The Intelligence Index composite spans knowledge work, coding, science and general knowledge, requiring text answers and agent outputs. An image-generation/editing model cannot perform that composite protocol."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Zapier AutomationBench official benchmark page",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench requires an agent to execute cross-application workflows using 47 tools and is scored by final application state. Qwen-Image-2.1 only generates or edits images and has no tool/workflow output. The leaderboard folds 119 rows after the first 10; N/A is based on interface incompatibility, not on treating those hidden rows as absent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Surge Chartography official task specification",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography requires a model to answer expert questions about chart images; its response is compared with a reference answer. Qwen-Image-2.1 outputs images, so it cannot submit chart readings or text explanations."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Qwen Image official repository",
          "url": "https://github.com/QwenLM/Qwen-Image-2.1"
        },
        {
          "label": "DeepSWE v1.1 official method and leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE requires a coding agent to modify a repository, submit a patch and run verification. Qwen-Image-2.1 is a text-to-image/image-editing diffusion model whose inference pipeline returns PNG images, so it cannot provide code patches or execution. Local release_date is 2026-09-14 (HF createdAt); the Qwen repo milestone says 2026-09-20, and neither date is an evaluation date."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 method",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires shell/web agent access and professional deliverables such as documents, slides, diagrams and spreadsheets. Qwen-Image-2.1 returns images and cannot execute tools or provide the required work products."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Artificial Analysis original HLE definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "The original HLE contains 2,500 multimodal questions with multiple-choice and short-answer answers. Qwen-Image-2.1 returns generated images rather than answer text, so it cannot follow the full benchmark response protocol."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "OSWorld v2.1 official evaluation guide",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "OSWorld v2.1 requires GUI interaction, including desktop actions such as mouse/keyboard input. Qwen-Image-2.1 can take an image as an editing condition but returns a generated image, not GUI actions or text."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Scale SWE-bench Pro V2 official protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires a software engineering agent to produce an issue-fixing diff for evaluation in a clean environment. Qwen-Image-2.1 returns images, not code diffs or text."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Terminal-Bench-Science 0.1 official definition",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench-Science evaluates terminal-based research workflows and verified artifacts such as analysis, simulation, proofs, code and data products. Image generation/editing cannot complete those tasks."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Terminal-Bench 4 official release and method",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4"
        }
      ],
      "notes": [
        "Terminal-Bench 4 requires an agent to operate a Harbor terminal task and submit verifiable task output. This model has no text, terminal or tool interface; its output is an image."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T11:16+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Image-2.1 official model card",
          "url": "https://huggingface.co/Qwen/Qwen-Image-2.1"
        },
        {
          "label": "Vals Index v2.2 leaderboard and method",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index is an agentic composite across finance, coding, legal and tax, including terminal work and professional deliverables. Qwen-Image-2.1 cannot execute these workflows or produce the required text/code artifacts."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T11:16+08:00",
  "model_id": "alibaba/qwen-image-2.1",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
