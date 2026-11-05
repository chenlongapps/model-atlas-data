# FIBO Generate 1.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：bria/fibo-generate-1.5
- 模型名称：FIBO Generate 1.5
- 发布日期：2026-08-24
- 最近检查时间：2026-11-04T16:37+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [DeepSWE 官方说明](https://deepswe.datacurve.ai/) | 2026-11-04T16:37+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T16:37+08:00 |
| terminal-bench-v4 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/?version=4.0) | 2026-11-04T16:37+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Artificial Analysis Terminal-Bench-Science 官方方法](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T16:37+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Zapier AutomationBench 官方榜单与方法](https://zapier.com/benchmarks) | 2026-11-04T16:37+08:00 |
| osworld-v2.1 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [OSWorld 官方项目说明](https://osworld-v2.xlang.ai/), [OSWorld V2.1 官方发布记录](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T16:37+08:00 |
| chartography | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 论文与方法](https://arxiv.org/html/2608.10677v1), [BRIA 官方图像生成文档](https://docs.bria.ai/image-generation/generation/image-generate) | 2026-11-04T16:37+08:00 |
| humanitys-last-exam | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Humanity’s Last Exam 官方说明](https://lastexam.ai/) | 2026-11-04T16:37+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Artificial Analysis Intelligence Index V5 官方评测页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T16:37+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T16:37+08:00 |
| vals-index-v2.2 | 不适用 | — | [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T16:37+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [DeepSWE 官方说明](https://deepswe.datacurve.ai/)

研究备注：
- FIBO 1.5 是文本/参考图到图像生成模型；DeepSWE 评测软件工程代码任务并要求代码变更/执行结果，模型没有此类代码工作流能力。

最近核验时间：2026-11-04T16:37+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 要求对真实仓库 issue 执行代码修复；FIBO 1.5 的任务类型是图像生成，输出是图像，与代码修复任务不相符。

最近核验时间：2026-11-04T16:37+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/?version=4.0)

研究备注：
- Terminal-Bench 4 要求在终端沙盒里完成多步任务；FIBO 1.5 生成图像，不支持终端工具或文本产物工作流。

最近核验时间：2026-11-04T16:37+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Artificial Analysis Terminal-Bench-Science 官方方法](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- Terminal-Bench-Science 要求通过终端完成科学研究工作流并产出可验证结果；FIBO 1.5 是图像生成模型，不具备该任务类型的工具操作/文本推理能力。

最近核验时间：2026-11-04T16:37+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Zapier AutomationBench 官方榜单与方法](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 是跨业务应用的端到端工具代理工作流评测；模型标记 tools unsupported，且仅生成图像，不执行应用工作流。

最近核验时间：2026-11-04T16:37+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [OSWorld 官方项目说明](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 官方发布记录](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- OSWorld v2.1 评测桌面计算机使用代理的长流程操作；FIBO 1.5 无工具调用/桌面操作能力，且输出为生成图像，不适用。

最近核验时间：2026-11-04T16:37+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 论文与方法](https://arxiv.org/html/2608.10677v1)
- [BRIA 官方图像生成文档](https://docs.bria.ai/image-generation/generation/image-generate)

研究备注：
- Chartography 需要理解专业图表图像、多步推理并输出文本答案。FIBO 可把文字或参考图用于图像生成，但目标 FIBO 1.5 的输出是生成图像，不是图表问答/推理结果；不可把参考图条件化误作图表理解 benchmark 能力。

最近核验时间：2026-11-04T16:37+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Humanity’s Last Exam 官方说明](https://lastexam.ai/)

研究备注：
- HLE 是学术问答评测，要求生成文本答案并计算准确率；FIBO 1.5 输出图像，不适用。

最近核验时间：2026-11-04T16:37+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Artificial Analysis Intelligence Index V5 官方评测页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA Intelligence Index V5 汇总知识工作、编程、科学和通用问答等语言/agent 任务能力；FIBO 1.5 是图像生成模型，不支持相应文本推理评测。

最近核验时间：2026-11-04T16:37+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求通过 agent 工作流完成职业知识工作并产出文本/数据制品；FIBO 1.5 不支持工具执行或文本答案输出。

最近核验时间：2026-11-04T16:37+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [BRIA 官方模型卡](https://huggingface.co/briaai/Fibo-1.5)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 汇总 finance、coding、legal、tax 等 agent 任务表现；FIBO 1.5 作为图像生成模型不具备此类文本/agent 任务输出能力。

最近核验时间：2026-11-04T16:37+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA Intelligence Index V5 汇总知识工作、编程、科学和通用问答等语言/agent 任务能力；FIBO 1.5 是图像生成模型，不支持相应文本推理评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Zapier AutomationBench 官方榜单与方法",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 是跨业务应用的端到端工具代理工作流评测；模型标记 tools unsupported，且仅生成图像，不执行应用工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 论文与方法",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "BRIA 官方图像生成文档",
          "url": "https://docs.bria.ai/image-generation/generation/image-generate"
        }
      ],
      "notes": [
        "Chartography 需要理解专业图表图像、多步推理并输出文本答案。FIBO 可把文字或参考图用于图像生成，但目标 FIBO 1.5 的输出是生成图像，不是图表问答/推理结果；不可把参考图条件化误作图表理解 benchmark 能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "DeepSWE 官方说明",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "FIBO 1.5 是文本/参考图到图像生成模型；DeepSWE 评测软件工程代码任务并要求代码变更/执行结果，模型没有此类代码工作流能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Artificial Analysis GDPval-AA 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求通过 agent 工作流完成职业知识工作并产出文本/数据制品；FIBO 1.5 不支持工具执行或文本答案输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Humanity’s Last Exam 官方说明",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "HLE 是学术问答评测，要求生成文本答案并计算准确率；FIBO 1.5 输出图像，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "OSWorld 官方项目说明",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 官方发布记录",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "OSWorld v2.1 评测桌面计算机使用代理的长流程操作；FIBO 1.5 无工具调用/桌面操作能力，且输出为生成图像，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Scale SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求对真实仓库 issue 执行代码修复；FIBO 1.5 的任务类型是图像生成，输出是图像，与代码修复任务不相符。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 官方方法",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 要求通过终端完成科学研究工作流并产出可验证结果；FIBO 1.5 是图像生成模型，不具备该任务类型的工具操作/文本推理能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Terminal-Bench 4.0 官方说明",
          "url": "https://www.tbench.ai/?version=4.0"
        }
      ],
      "notes": [
        "Terminal-Bench 4 要求在终端沙盒里完成多步任务；FIBO 1.5 生成图像，不支持终端工具或文本产物工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T16:37+08:00",
      "checked_sources": [
        {
          "label": "BRIA 官方模型卡",
          "url": "https://huggingface.co/briaai/Fibo-1.5"
        },
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 汇总 finance、coding、legal、tax 等 agent 任务表现；FIBO 1.5 作为图像生成模型不具备此类文本/agent 任务输出能力。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T16:37+08:00",
  "model_id": "bria/fibo-generate-1.5",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
