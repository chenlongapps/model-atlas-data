# North Small Translate Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：cohere/north-small-translate-1-0
- 模型名称：North Small Translate
- 发布日期：2026-09-09
- 最近检查时间：2026-11-04T12:18+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T12:18+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T12:18+08:00 |
| terminal-bench-v4 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 release](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T12:18+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Terminal-Bench Science official site](https://www.terminal-bench-science.ai/), [Terminal-Bench Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement) | 2026-11-04T12:18+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T12:18+08:00 |
| osworld-v2.1 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T12:18+08:00 |
| chartography | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography) | 2026-11-04T12:18+08:00 |
| humanitys-last-exam | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T12:18+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Artificial Analysis Intelligence Index V5 evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T12:18+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Cohere North Small Translate launch](https://cohere.com/blog/north-small-translate) | 2026-11-04T12:18+08:00 |
| vals-index-v2.2 | 不适用 | — | [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0), [Vals Index v2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T12:18+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 评测长程软件工程 coding agent。该模型专为机器翻译设计，仓库模型定义明确标记不支持 reasoning 或 tools；当前榜单可读文本显示 21/28 项，缺席不能单独证明完整榜单没有记录，但模型本身不适用于该 agent benchmark。

最近核验时间：2026-11-04T12:18+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 要求软件工程任务中的代码修改与验证。North Small Translate 是专用翻译模型，且不支持 reasoning 或 tools，不适用于该 coding-agent 评测。

最近核验时间：2026-11-04T12:18+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 release](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4 要求 agent 执行终端任务并产出结果。该模型专用于机器翻译且不支持 tools 或 reasoning，不适用于该评测；榜单文本视图不足以证明模型是否列在完整列表中。

最近核验时间：2026-11-04T12:18+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Terminal-Bench Science official site](https://www.terminal-bench-science.ai/)
- [Terminal-Bench Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement)

研究备注：
- 该基准要求 agent 执行科学研究工作流并产出可验证工件。模型能力与任务不匹配；初始公告早于模型发布日期，当前页面文本无法读取完整动态结果。

最近核验时间：2026-11-04T12:18+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 评估 agent 使用模拟应用执行跨应用工作流。该模型不支持工具调用；官方榜单只显示部分结果，但不影响基于模型用途和能力判断其不适用于独立 agent 评测。

最近核验时间：2026-11-04T12:18+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 使用屏幕截图观察并要求 GUI 操作；North Small Translate 仅支持 text 输入输出且不支持 tools，无法独立执行该评测。

最近核验时间：2026-11-04T12:18+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)

研究备注：
- Chartography 的任务输入图表图像并要求图表理解；North Small Translate 仅支持 text 输入输出，不适用于该图像评测。

最近核验时间：2026-11-04T12:18+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 是专家级跨领域问答评测，目标是通用知识与推理；North Small Translate 是专用翻译模型且不支持 reasoning，不适用于该评测。

最近核验时间：2026-11-04T12:18+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Artificial Analysis Intelligence Index V5 evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA Intelligence Index V5 汇总通用知识工作、编程、科学与推理任务；North Small Translate 的能力范围仅为机器翻译，官方榜单也未列该模型，因此不适用于该综合指数。

最近核验时间：2026-11-04T12:18+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Cohere North Small Translate launch](https://cohere.com/blog/north-small-translate)

研究备注：
- GDPval-AA 通过 Stirrup agent、shell 和 web 工具评估专业工作产物；North Small Translate 不支持 tools 或 reasoning，Cohere 发布的 WMT26 翻译成绩不属于该 benchmark。

最近核验时间：2026-11-04T12:18+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0)
- [Vals Index v2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 评估多个行业领域的代理工作流；North Small Translate 不支持工具调用或推理，且专用于翻译，不适用于该综合 agent 指数。

最近核验时间：2026-11-04T12:18+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA Intelligence Index V5 汇总通用知识工作、编程、科学与推理任务；North Small Translate 的能力范围仅为机器翻译，官方榜单也未列该模型，因此不适用于该综合指数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 评估 agent 使用模拟应用执行跨应用工作流。该模型不支持工具调用；官方榜单只显示部分结果，但不影响基于模型用途和能力判断其不适用于独立 agent 评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography 的任务输入图表图像并要求图表理解；North Small Translate 仅支持 text 输入输出，不适用于该图像评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 评测长程软件工程 coding agent。该模型专为机器翻译设计，仓库模型定义明确标记不支持 reasoning 或 tools；当前榜单可读文本显示 21/28 项，缺席不能单独证明完整榜单没有记录，但模型本身不适用于该 agent benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Cohere North Small Translate launch",
          "url": "https://cohere.com/blog/north-small-translate"
        }
      ],
      "notes": [
        "GDPval-AA 通过 Stirrup agent、shell 和 web 工具评估专业工作产物；North Small Translate 不支持 tools 或 reasoning，Cohere 发布的 WMT26 翻译成绩不属于该 benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 是专家级跨领域问答评测，目标是通用知识与推理；North Small Translate 是专用翻译模型且不支持 reasoning，不适用于该评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 使用屏幕截图观察并要求 GUI 操作；North Small Translate 仅支持 text 输入输出且不支持 tools，无法独立执行该评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求软件工程任务中的代码修改与验证。North Small Translate 是专用翻译模型，且不支持 reasoning 或 tools，不适用于该 coding-agent 评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Terminal-Bench Science official site",
          "url": "https://www.terminal-bench-science.ai/"
        },
        {
          "label": "Terminal-Bench Science 0.1 announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "该基准要求 agent 执行科学研究工作流并产出可验证工件。模型能力与任务不匹配；初始公告早于模型发布日期，当前页面文本无法读取完整动态结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Terminal-Bench 4 leaderboard",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 release",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4 要求 agent 执行终端任务并产出结果。该模型专用于机器翻译且不支持 tools 或 reasoning，不适用于该评测；榜单文本视图不足以证明模型是否列在完整列表中。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T12:18+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Small Translate documentation",
          "url": "https://docs.cohere.com/docs/north-small-translate-1.0"
        },
        {
          "label": "Vals Index v2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 评估多个行业领域的代理工作流；North Small Translate 不支持工具调用或推理，且专用于翻译，不适用于该综合 agent 指数。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T12:18+08:00",
  "model_id": "cohere/north-small-translate-1-0",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
