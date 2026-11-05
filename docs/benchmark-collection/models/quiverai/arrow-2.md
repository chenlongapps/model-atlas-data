# Arrow 2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：quiverai/arrow-2
- 模型名称：Arrow 2
- 发布日期：2026-09-16
- 最近检查时间：2026-11-04T10:27+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE 官方方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [SWE-bench Pro V2 数据集](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 4 官方说明](https://www.tbench.ai/news/terminal-bench-4-0), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench Science 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 榜单](https://zapier.com/benchmarks), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2), [Arrow 2 OpenResponses 文档](https://docs.quiver.ai/api-reference/openresponses/create-open-response) | 2026-11-04T10:27+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 官方项目](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 官方站点](https://osworld-v2.xlang.ai/), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| chartography | 待核实 | — | [Surge Chartography 榜单与任务说明](https://surgehq.ai/benchmarks/chartography), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2), [Quiver 图像转 SVG 接口](https://docs.quiver.ai/api-reference/vectorize-svg/vectorize-svg) | 2026-11-04T10:27+08:00 |
| humanitys-last-exam | 不适用 | — | [Artificial Analysis HLE 任务说明](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA v2.1 方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2) | 2026-11-04T10:27+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE 官方方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- DeepSWE v1.1 评测 coding agent 完成长程软件工程任务并提交补丁；Arrow 2 官方接口面向 SVG 生成、向量化、编辑和动画，输出模态为 SVG，没有通用代码仓库修复与补丁执行接口。

最近核验时间：2026-11-04T10:27+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [SWE-bench Pro V2 数据集](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- SWE-bench Pro V2 要求在真实代码库中解决软件工程问题并提交代码补丁；Arrow 2 官方记录的输出为 SVG，资料未显示代码编辑、测试执行或补丁提交流程。

最近核验时间：2026-11-04T10:27+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 4 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- Terminal-Bench 4 评测 agent 在终端环境执行任务；Arrow 2 是 SVG 专用模型，官方文档没有声明终端执行能力。

最近核验时间：2026-11-04T10:27+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench Science 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- Terminal-Bench Science 评测在终端中完成科学计算与研究工作流；Arrow 2 的官方能力限于 SVG 内容生成与编辑，资料未显示终端或科学计算执行接口。

最近核验时间：2026-11-04T10:27+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 榜单](https://zapier.com/benchmarks)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)
- [Arrow 2 OpenResponses 文档](https://docs.quiver.ai/api-reference/openresponses/create-open-response)

研究备注：
- 未找到 Arrow 2 可核实的精确版本成绩。公开榜单展示部分条目并折叠其余项目，未在可见列表中出现不等于完整榜单没有该模型。

尚未解决的问题：
- 需进一步确认 AutomationBench v1.0.6 完整记录及 Arrow 2 是否曾以该准确模型版本参与测试；当前证据不足以判为未找到或不适用。

最近核验时间：2026-11-04T10:27+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 官方项目](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 官方站点](https://osworld-v2.xlang.ai/)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- 未找到 Arrow 2 可核实的精确版本成绩。OSWorld 官方站点显示 OSWorld 2.0，和本地定义的 v2.1 版本不一致；Arrow 2 文档列出图像输入，但未确认屏幕理解和桌面交互能力。

尚未解决的问题：
- 需确认本地 v2.1 对应的官方评测版本以及 Arrow 2 是否符合该测试的 computer-use 接口要求。

最近核验时间：2026-11-04T10:27+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography 榜单与任务说明](https://surgehq.ai/benchmarks/chartography)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)
- [Quiver 图像转 SVG 接口](https://docs.quiver.ai/api-reference/vectorize-svg/vectorize-svg)

研究备注：
- 未找到 Arrow 2 可核实的精确成绩。Chartography 评测专业图表阅读与多步图形推理；Arrow 2 可接收图像，但官方明确的图像任务是 image-to-SVG，输出模态为 SVG。

尚未解决的问题：
- 现有资料不足以确定该模型能否在 Chartography 协议下返回可评分的图表推理答案，故保留待核实。

最近核验时间：2026-11-04T10:27+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis HLE 任务说明](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- HLE 是有明确答案的多学科学术问答评测；Arrow 2 官方输出模态为 SVG，不能按其公布接口提交问答答案。

最近核验时间：2026-11-04T10:27+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- Artificial Analysis Intelligence Index 汇总通用知识、推理、编码等能力；Arrow 2 官方资料将其定位为 SVG 专用生成模型，输出 SVG，不能据此参加并形成该通用语言模型综合指数成绩。

最近核验时间：2026-11-04T10:27+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- GDPval-AA v2.1 要求模型通过 agentic harness 使用 shell 和网页工具，并产出文档、幻灯片、图表、表格等职业成果；Arrow 2 的公开接口定位和输出模态是 SVG，不能执行完整基准任务协议。

最近核验时间：2026-11-04T10:27+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Arrow 2 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2)

研究备注：
- Vals Index v2.2 汇总 finance、coding、legal、tax 等领域的 agentic 任务；Arrow 2 的公开接口是 SVG 专用生成与编辑，不能完成该综合评测协议。

最近核验时间：2026-11-04T10:27+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index 汇总通用知识、推理、编码等能力；Arrow 2 官方资料将其定位为 SVG 专用生成模型，输出 SVG，不能据此参加并形成该通用语言模型综合指数成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        },
        {
          "label": "Arrow 2 OpenResponses 文档",
          "url": "https://docs.quiver.ai/api-reference/openresponses/create-open-response"
        }
      ],
      "notes": [
        "未找到 Arrow 2 可核实的精确版本成绩。公开榜单展示部分条目并折叠其余项目，未在可见列表中出现不等于完整榜单没有该模型。"
      ],
      "status": "待核实",
      "unresolved": [
        "需进一步确认 AutomationBench v1.0.6 完整记录及 Arrow 2 是否曾以该准确模型版本参与测试；当前证据不足以判为未找到或不适用。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 榜单与任务说明",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        },
        {
          "label": "Quiver 图像转 SVG 接口",
          "url": "https://docs.quiver.ai/api-reference/vectorize-svg/vectorize-svg"
        }
      ],
      "notes": [
        "未找到 Arrow 2 可核实的精确成绩。Chartography 评测专业图表阅读与多步图形推理；Arrow 2 可接收图像，但官方明确的图像任务是 image-to-SVG，输出模态为 SVG。"
      ],
      "status": "待核实",
      "unresolved": [
        "现有资料不足以确定该模型能否在 Chartography 协议下返回可评分的图表推理答案，故保留待核实。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方方法",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "DeepSWE v1.1 评测 coding agent 完成长程软件工程任务并提交补丁；Arrow 2 官方接口面向 SVG 生成、向量化、编辑和动画，输出模态为 SVG，没有通用代码仓库修复与补丁执行接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 要求模型通过 agentic harness 使用 shell 和网页工具，并产出文档、幻灯片、图表、表格等职业成果；Arrow 2 的公开接口定位和输出模态是 SVG，不能执行完整基准任务协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE 任务说明",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "HLE 是有明确答案的多学科学术问答评测；Arrow 2 官方输出模态为 SVG，不能按其公布接口提交问答答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方项目",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld 官方站点",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "未找到 Arrow 2 可核实的精确版本成绩。OSWorld 官方站点显示 OSWorld 2.0，和本地定义的 v2.1 版本不一致；Arrow 2 文档列出图像输入，但未确认屏幕理解和桌面交互能力。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认本地 v2.1 对应的官方评测版本以及 Arrow 2 是否符合该测试的 computer-use 接口要求。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 数据集",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求在真实代码库中解决软件工程问题并提交代码补丁；Arrow 2 官方记录的输出为 SVG，资料未显示代码编辑、测试执行或补丁提交流程。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "Terminal-Bench Science 评测在终端中完成科学计算与研究工作流；Arrow 2 的官方能力限于 SVG 内容生成与编辑，资料未显示终端或科学计算执行接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "Terminal-Bench 4 评测 agent 在终端环境执行任务；Arrow 2 是 SVG 专用模型，官方文档没有声明终端执行能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T10:27+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Arrow 2 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2"
        }
      ],
      "notes": [
        "Vals Index v2.2 汇总 finance、coding、legal、tax 等领域的 agentic 任务；Arrow 2 的公开接口是 SVG 专用生成与编辑，不能完成该综合评测协议。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T10:27+08:00",
  "model_id": "quiverai/arrow-2",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
