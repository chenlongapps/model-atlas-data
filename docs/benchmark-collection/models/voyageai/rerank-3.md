# rerank-3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：voyageai/rerank-3
- 模型名称：rerank-3
- 发布日期：2026-09-30
- 最近检查时间：2026-11-04T05:39+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [deepswe-v1.1 官方协议/榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [swe-bench-pro-v2 官方协议/榜单](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| terminal-bench-v4 | 不适用 | — | [terminal-bench-v4 官方协议/榜单](https://www.tbench.ai/run), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [terminal-bench-science-v0.1 官方协议/榜单](https://www.tbench.ai/news/terminal-bench-science-0-1), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [automationbench-v1.0.6 官方协议/榜单](https://zapier.com/benchmarks), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| osworld-v2.1 | 不适用 | — | [osworld-v2.1 官方协议/榜单](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| chartography | 不适用 | — | [chartography 官方协议/榜单](https://surgehq.ai/benchmarks/chartography), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| humanitys-last-exam | 不适用 | — | [humanitys-last-exam 官方协议/榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [artificial-analysis-intelligence-index-v5 官方协议/榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [gdpval-aa-v2.1 官方协议/榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |
| vals-index-v2.2 | 不适用 | — | [vals-index-v2.2 官方协议/榜单](https://www.vals.ai/benchmarks/vals_index), [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker), [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/) | 2026-11-04T05:39+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [deepswe-v1.1 官方协议/榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- DeepSWE 1.1 要求软件工程代理修改代码并由隔离环境验证补丁；rerank-3 仅重排查询与候选文档，单独不能提交代码补丁。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [swe-bench-pro-v2 官方协议/榜单](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- SWE-bench Pro V2 评估代理生成并在环境中验证的代码补丁；rerank-3 不生成补丁。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [terminal-bench-v4 官方协议/榜单](https://www.tbench.ai/run)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- Terminal-Bench 通过沙箱终端中的代理完成任务并运行验证；rerank-3 不执行终端命令。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [terminal-bench-science-v0.1 官方协议/榜单](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- Terminal-Bench Science 要求代理执行科研工作流并产出可验证的代码、分析或数据；rerank-3 只输出相关性排序。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [automationbench-v1.0.6 官方协议/榜单](https://zapier.com/benchmarks)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- AutomationBench 评估代理使用工具完成工作流后的环境状态；rerank-3 可作为外部代理的检索组件，但组合系统成绩不能归属给 reranker。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [osworld-v2.1 官方协议/榜单](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- OSWorld 2.1 要求计算机使用代理观察桌面并执行 GUI 操作；rerank-3 只接收文本查询和候选文档，不输出 GUI 操作。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [chartography 官方协议/榜单](https://surgehq.ai/benchmarks/chartography)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- Chartography 要求读取图表图像并产出自由文本回答；rerank-3 输入为文本查询和候选文本，不接受图像也不生成回答。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [humanitys-last-exam 官方协议/榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- 原版 HLE 是问答基准；rerank-3 的 API 返回候选文档相关性分数和排序，不按基准协议生成答案。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [artificial-analysis-intelligence-index-v5 官方协议/榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- AA Intelligence Index V5 是涵盖知识工作、编码、科学和通用能力的多项模型/代理评测综合指数；rerank-3 只返回相关性分数，不能完成这些评测任务。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [gdpval-aa-v2.1 官方协议/榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- GDPval-AA 评估专业工作任务和交付成果，配套方法需要代理工作流；rerank-3 本身只重排文本候选，外层代理成绩不能归属给它。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [vals-index-v2.2 官方协议/榜单](https://www.vals.ai/benchmarks/vals_index)
- [Voyage Reranker API 文档](https://docs.voyageai.com/docs/reranker)
- [Voyage rerank-3 官方发布说明](https://blog.voyageai.com/2026/09/30/rerank-3/)

研究备注：
- Vals Index v2.2 汇总代理在金融、编码、法律和税务等任务的表现；rerank-3 本身无法执行这些工作流。未发现可归属于该型号的直接成绩。

最近核验时间：2026-11-04T05:39+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "artificial-analysis-intelligence-index-v5 官方协议/榜单",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "AA Intelligence Index V5 是涵盖知识工作、编码、科学和通用能力的多项模型/代理评测综合指数；rerank-3 只返回相关性分数，不能完成这些评测任务。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "automationbench-v1.0.6 官方协议/榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "AutomationBench 评估代理使用工具完成工作流后的环境状态；rerank-3 可作为外部代理的检索组件，但组合系统成绩不能归属给 reranker。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "chartography 官方协议/榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "Chartography 要求读取图表图像并产出自由文本回答；rerank-3 输入为文本查询和候选文本，不接受图像也不生成回答。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "deepswe-v1.1 官方协议/榜单",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "DeepSWE 1.1 要求软件工程代理修改代码并由隔离环境验证补丁；rerank-3 仅重排查询与候选文档，单独不能提交代码补丁。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "gdpval-aa-v2.1 官方协议/榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "GDPval-AA 评估专业工作任务和交付成果，配套方法需要代理工作流；rerank-3 本身只重排文本候选，外层代理成绩不能归属给它。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "humanitys-last-exam 官方协议/榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "原版 HLE 是问答基准；rerank-3 的 API 返回候选文档相关性分数和排序，不按基准协议生成答案。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "osworld-v2.1 官方协议/榜单",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "OSWorld 2.1 要求计算机使用代理观察桌面并执行 GUI 操作；rerank-3 只接收文本查询和候选文档，不输出 GUI 操作。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "swe-bench-pro-v2 官方协议/榜单",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评估代理生成并在环境中验证的代码补丁；rerank-3 不生成补丁。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "terminal-bench-science-v0.1 官方协议/榜单",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要求代理执行科研工作流并产出可验证的代码、分析或数据；rerank-3 只输出相关性排序。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "terminal-bench-v4 官方协议/榜单",
          "url": "https://www.tbench.ai/run"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "Terminal-Bench 通过沙箱终端中的代理完成任务并运行验证；rerank-3 不执行终端命令。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:39+08:00",
      "checked_sources": [
        {
          "label": "vals-index-v2.2 官方协议/榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Voyage Reranker API 文档",
          "url": "https://docs.voyageai.com/docs/reranker"
        },
        {
          "label": "Voyage rerank-3 官方发布说明",
          "url": "https://blog.voyageai.com/2026/09/30/rerank-3/"
        }
      ],
      "notes": [
        "Vals Index v2.2 汇总代理在金融、编码、法律和税务等任务的表现；rerank-3 本身无法执行这些工作流。未发现可归属于该型号的直接成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:39+08:00",
  "model_id": "voyageai/rerank-3",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
