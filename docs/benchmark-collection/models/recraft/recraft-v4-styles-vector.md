# Recraft V4 Styles Vector Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：recraft/recraft-v4-styles-vector
- 模型名称：Recraft V4 Styles Vector
- 发布日期：2026-08-26
- 最近检查时间：2026-11-04T16:06+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [DeepSWE 1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T16:06+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T16:06+08:00 |
| terminal-bench-v4 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Terminal-Bench 4.0](https://www.tbench.ai/) | 2026-11-04T16:06+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T16:06+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Zapier AutomationBench](https://zapier.com/benchmarks) | 2026-11-04T16:06+08:00 |
| osworld-v2.1 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [OSWorld V2 project and release record](https://github.com/xlang-ai/OSWorld-V2), [OSWorld v2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T16:06+08:00 |
| chartography | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Surge AI Chartography](https://surgehq.ai/benchmarks/chartography), [Chartography official task and scoring format](https://raw.githubusercontent.com/surge-ai/chartography/main/README.md) | 2026-11-04T16:06+08:00 |
| humanitys-last-exam | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Humanity's Last Exam](https://lastexam.ai/) | 2026-11-04T16:06+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T16:06+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Artificial Analysis GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T16:06+08:00 |
| vals-index-v2.2 | 不适用 | — | [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles), [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles), [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T16:06+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [DeepSWE 1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE evaluates long-horizon software-engineering agents. Recraft V4 Styles Vector accepts a prompt and style references and returns SVG graphics; it does not provide coding-agent output. The leaderboard did not identify this exact variant.

最近核验时间：2026-11-04T16:06+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 evaluates repository-level code patches. Recraft V4 Styles Vector returns SVG graphics rather than code patches. The official V2 leaderboard did not identify this exact variant.

最近核验时间：2026-11-04T16:06+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Terminal-Bench 4.0](https://www.tbench.ai/)

研究备注：
- Terminal-Bench evaluates terminal-agent task execution. Recraft V4 Styles Vector is an SVG image-generation API, not a terminal agent. The official page did not identify this exact variant.

最近核验时间：2026-11-04T16:06+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench-Science requires terminal-based scientific workflows. Recraft V4 Styles Vector returns SVGs and does not provide the measured workflow. The official results page did not identify this exact variant.

最近核验时间：2026-11-04T16:06+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Zapier AutomationBench](https://zapier.com/benchmarks)

研究备注：
- AutomationBench evaluates tool-using agents completing business workflows. Recraft V4 Styles Vector is an image-generation endpoint with no workflow-agent interface. The leaderboard search did not identify Recraft.

最近核验时间：2026-11-04T16:06+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [OSWorld V2 project and release record](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld v2.1 release record](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- OSWorld evaluates desktop-control agents. Recraft V4 Styles Vector generates SVGs and does not expose GUI actions. The project page and v2.1 release record did not identify Recraft.

最近核验时间：2026-11-04T16:06+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Surge AI Chartography](https://surgehq.ai/benchmarks/chartography)
- [Chartography official task and scoring format](https://raw.githubusercontent.com/surge-ai/chartography/main/README.md)

研究备注：
- Chartography pairs chart images with questions and grades answer text. Recraft V4 Styles Vector accepts style-reference images but returns SVG graphics rather than answers. The leaderboard did not identify this exact variant.

最近核验时间：2026-11-04T16:06+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Humanity's Last Exam](https://lastexam.ai/)

研究备注：
- Humanity’s Last Exam measures academic question answering. Recraft V4 Styles Vector returns SVG graphics rather than answers to the questions. The official page did not identify Recraft.

最近核验时间：2026-11-04T16:06+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The Intelligence Index aggregates knowledge, coding, science, and agentic evaluations. Recraft V4 Styles Vector is an SVG-generation model; the vendor’s style-matching evaluation is a separate image-generation task and cannot be mapped to this Index. The official page did not identify Recraft.

最近核验时间：2026-11-04T16:06+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Artificial Analysis GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA evaluates professional work tasks and agent-generated work products. Recraft V4 Styles Vector returns SVG graphics rather than the measured work products. The official page did not identify Recraft.

最近核验时间：2026-11-04T16:06+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4 Styles API documentation (includes Vector variant)](https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles)
- [Recraft V4 Styles release announcement](https://www.recraft.ai/blog/meet-recraft-v4-styles)
- [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index aggregates agent performance in finance, coding, legal, and tax tasks. Recraft V4 Styles Vector is an SVG-generation endpoint, outside those task interfaces. The official page did not identify Recraft.

最近核验时间：2026-11-04T16:06+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The Intelligence Index aggregates knowledge, coding, science, and agentic evaluations. Recraft V4 Styles Vector is an SVG-generation model; the vendor’s style-matching evaluation is a separate image-generation task and cannot be mapped to this Index. The official page did not identify Recraft."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Zapier AutomationBench",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench evaluates tool-using agents completing business workflows. Recraft V4 Styles Vector is an image-generation endpoint with no workflow-agent interface. The leaderboard search did not identify Recraft."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Surge AI Chartography",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official task and scoring format",
          "url": "https://raw.githubusercontent.com/surge-ai/chartography/main/README.md"
        }
      ],
      "notes": [
        "Chartography pairs chart images with questions and grades answer text. Recraft V4 Styles Vector accepts style-reference images but returns SVG graphics rather than answers. The leaderboard did not identify this exact variant."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "DeepSWE 1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE evaluates long-horizon software-engineering agents. Recraft V4 Styles Vector accepts a prompt and style references and returns SVG graphics; it does not provide coding-agent output. The leaderboard did not identify this exact variant."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Artificial Analysis GDPval-AA",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA evaluates professional work tasks and agent-generated work products. Recraft V4 Styles Vector returns SVG graphics rather than the measured work products. The official page did not identify Recraft."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Humanity's Last Exam",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "Humanity’s Last Exam measures academic question answering. Recraft V4 Styles Vector returns SVG graphics rather than answers to the questions. The official page did not identify Recraft."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "OSWorld V2 project and release record",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld v2.1 release record",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "OSWorld evaluates desktop-control agents. Recraft V4 Styles Vector generates SVGs and does not expose GUI actions. The project page and v2.1 release record did not identify Recraft."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 evaluates repository-level code patches. Recraft V4 Styles Vector returns SVG graphics rather than code patches. The official V2 leaderboard did not identify this exact variant."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Terminal-Bench-Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench-Science requires terminal-based scientific workflows. Recraft V4 Styles Vector returns SVGs and does not provide the measured workflow. The official results page did not identify this exact variant."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/"
        }
      ],
      "notes": [
        "Terminal-Bench evaluates terminal-agent task execution. Recraft V4 Styles Vector is an SVG image-generation API, not a terminal agent. The official page did not identify this exact variant."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T16:06+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4 Styles API documentation (includes Vector variant)",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-styles"
        },
        {
          "label": "Recraft V4 Styles release announcement",
          "url": "https://www.recraft.ai/blog/meet-recraft-v4-styles"
        },
        {
          "label": "Vals Index v2.2",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index aggregates agent performance in finance, coding, legal, and tax tasks. Recraft V4 Styles Vector is an SVG-generation endpoint, outside those task interfaces. The official page did not identify Recraft."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T16:06+08:00",
  "model_id": "recraft/recraft-v4-styles-vector",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
