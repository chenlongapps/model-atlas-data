# MAI-Image-2.6 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：microsoft/mai-image-2.6
- 模型名称：MAI-Image-2.6
- 发布日期：2026-08-14
- 最近检查时间：2026-11-04T17:08+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T17:08+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-04T17:08+08:00 |
| terminal-bench-v4 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T17:08+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T17:08+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://zapier.com/benchmarks) | 2026-11-04T17:08+08:00 |
| osworld-v2.1 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T17:08+08:00 |
| chartography | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://github.com/surge-ai/chartography) | 2026-11-04T17:08+08:00 |
| humanitys-last-exam | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://lastexam.ai/) | 2026-11-04T17:08+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T17:08+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T17:08+08:00 |
| vals-index-v2.2 | 不适用 | — | [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf), [Benchmark 官方方法或榜单](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T17:08+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE v1.1 evaluates software engineering agents submitting code patches; MAI-Image 2.6 produces images, not code.

最近核验时间：2026-11-04T17:08+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- SWE-bench Pro requires code patches for repository issues and verifier tests; the model outputs images.

最近核验时间：2026-11-04T17:08+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench evaluates agents completing tasks in a sandboxed terminal; this model provides image outputs and no tools.

最近核验时间：2026-11-04T17:08+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Terminal-Bench Science evaluates scientific workflows in a terminal; this image-generation model has no tool support.

最近核验时间：2026-11-04T17:08+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://zapier.com/benchmarks)

研究备注：
- AutomationBench measures business workflow completion via tools and resulting application state; image output is not a supported workflow action.

最近核验时间：2026-11-04T17:08+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld requires desktop-agent actions; MAI-Image generates images and has no tool capability.

最近核验时间：2026-11-04T17:08+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://github.com/surge-ai/chartography)

研究备注：
- Chartography evaluates text answers to professional chart questions; MAI-Image outputs an image rather than a scored answer.

最近核验时间：2026-11-04T17:08+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://lastexam.ai/)

研究备注：
- Original HLE is academic question answering; this model generates images and does not provide answer text.

最近核验时间：2026-11-04T17:08+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The composite index evaluates language, reasoning, coding, scientific, and agent capabilities; the model is a text-to-image and image-editing system.

最近核验时间：2026-11-04T17:08+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires shell/web agent work and professional text deliverables; the model outputs images.

最近核验时间：2026-11-04T17:08+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Microsoft 官方 MAI-Image-2.6 模型卡](https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf)
- [Benchmark 官方方法或榜单](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index aggregates finance, coding, legal, and tax agent task performance; this image generator does not produce relevant text or tool actions.

最近核验时间：2026-11-04T17:08+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The composite index evaluates language, reasoning, coding, scientific, and agent capabilities; the model is a text-to-image and image-editing system."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench measures business workflow completion via tools and resulting application state; image output is not a supported workflow action."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography evaluates text answers to professional chart questions; MAI-Image outputs an image rather than a scored answer."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE v1.1 evaluates software engineering agents submitting code patches; MAI-Image 2.6 produces images, not code."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires shell/web agent work and professional text deliverables; the model outputs images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "Original HLE is academic question answering; this model generates images and does not provide answer text."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld requires desktop-agent actions; MAI-Image generates images and has no tool capability."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "SWE-bench Pro requires code patches for repository issues and verifier tests; the model outputs images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "Terminal-Bench Science evaluates scientific workflows in a terminal; this image-generation model has no tool support."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench evaluates agents completing tasks in a sandboxed terminal; this model provides image outputs and no tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T17:08+08:00",
      "checked_sources": [
        {
          "label": "Microsoft 官方 MAI-Image-2.6 模型卡",
          "url": "https://microsoft.ai/pdf/MAI-Image-2.6-Model-Card.pdf"
        },
        {
          "label": "Benchmark 官方方法或榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index aggregates finance, coding, legal, and tax agent task performance; this image generator does not produce relevant text or tool actions."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T17:08+08:00",
  "model_id": "microsoft/mai-image-2.6",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
