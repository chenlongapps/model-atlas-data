# Schematron V2 Turbo Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inference-net/schematron-v2-turbo
- 模型名称：Schematron V2 Turbo
- 发布日期：2026-04-16
- 最近检查时间：2026-11-05T08:58+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方资料将本型号定位为由 HTML 输入和给定 schema 生成结构化 JSON 的抽取模型，不是通用回答或 agent harness。其 LLM-as-a-judge 抽取质量分数和外部 GPT-5 Nano/Exa SimpleQA pipeline 均不属于本轮 11 项目标成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [deepswe-v1.1 official benchmark page](https://deepswe.datacurve.ai/) | 2026-11-05T08:58+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [swe-bench-pro-v2 official benchmark page](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:58+08:00 |
| terminal-bench-v4 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [terminal-bench-v4 official benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:58+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [terminal-bench-science-v0.1 official benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:58+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [automationbench-v1.0.6 official benchmark page](https://zapier.com/benchmarks) | 2026-11-05T08:58+08:00 |
| osworld-v2.1 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [osworld-v2.1 official benchmark page](https://osworld-v2.xlang.ai/) | 2026-11-05T08:58+08:00 |
| chartography | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [chartography official benchmark page](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T08:58+08:00 |
| humanitys-last-exam | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [humanitys-last-exam official benchmark page](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [artificial-analysis-intelligence-index-v5 official benchmark page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T08:58+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [gdpval-aa-v2.1 official benchmark page](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T08:58+08:00 |
| vals-index-v2.2 | 不适用 | — | [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2), [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron), [vals-index-v2.2 official benchmark page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T08:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [deepswe-v1.1 official benchmark page](https://deepswe.datacurve.ai/)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [swe-bench-pro-v2 official benchmark page](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [terminal-bench-v4 official benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [terminal-bench-science-v0.1 official benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [automationbench-v1.0.6 official benchmark page](https://zapier.com/benchmarks)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [osworld-v2.1 official benchmark page](https://osworld-v2.xlang.ai/)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [chartography official benchmark page](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [humanitys-last-exam official benchmark page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [artificial-analysis-intelligence-index-v5 official benchmark page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [gdpval-aa-v2.1 official benchmark page](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Inference.net Schematron V2 release article](https://inference.net/blog/schematron-v2)
- [Official Schematron model/API documentation](https://docs.inference.net/workhorse-models/schematron)
- [vals-index-v2.2 official benchmark page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。

最近核验时间：2026-11-05T08:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "artificial-analysis-intelligence-index-v5 official benchmark page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "automationbench-v1.0.6 official benchmark page",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "chartography official benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "deepswe-v1.1 official benchmark page",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "gdpval-aa-v2.1 official benchmark page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "humanitys-last-exam official benchmark page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "osworld-v2.1 official benchmark page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "swe-bench-pro-v2 official benchmark page",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "terminal-bench-science-v0.1 official benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "terminal-bench-v4 official benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:58+08:00",
      "checked_sources": [
        {
          "label": "Inference.net Schematron V2 release article",
          "url": "https://inference.net/blog/schematron-v2"
        },
        {
          "label": "Official Schematron model/API documentation",
          "url": "https://docs.inference.net/workhorse-models/schematron"
        },
        {
          "label": "vals-index-v2.2 official benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Schematron V2 Turbo 是 schema-guided HTML→JSON 抽取端点，不执行通用对话、代码/终端代理、GUI、图表问答或专业工作流；其专用抽取评测不是这些目标 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:58+08:00",
  "model_id": "inference-net/schematron-v2-turbo",
  "model_notes": [
    "官方资料将本型号定位为由 HTML 输入和给定 schema 生成结构化 JSON 的抽取模型，不是通用回答或 agent harness。其 LLM-as-a-judge 抽取质量分数和外部 GPT-5 Nano/Exa SimpleQA pipeline 均不属于本轮 11 项目标成绩。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
