# Grok Imagine Image 2.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-imagine-image-2.0
- 模型名称：Grok Imagine Image 2.0
- 发布日期：2026-08-07
- 最近检查时间：2026-11-04T19:35+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- xAI 官方模型页确认 grok-imagine-image-2.0 接受文本和图像输入、输出图像，用于图像生成与编辑；模型 TOML 记载 tools.supported=false、reasoning.supported=false。
- 基于上述接口能力，11 项 Benchmark 均要求文本答案、代码/终端任务、工具工作流或综合推理结果，故均记为不适用；未把其他 Grok 对话模型的成绩转录过来。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/) | 2026-11-04T19:35+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T19:35+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0), [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T19:35+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement) | 2026-11-04T19:35+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T19:35+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T19:35+08:00 |
| chartography | 不适用 | — | [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography), [xAI Grok Imagine Image 2.0 官方模型文档](https://docs.x.ai/developers/models/grok-imagine-image-2.0) | 2026-11-04T19:35+08:00 |
| humanitys-last-exam | 不适用 | — | [Scale AI Humanity's Last Exam 官方排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity’s Last Exam 独立评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T19:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index v5 官方发布说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T19:35+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T19:35+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T19:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 评测长程软件工程任务并产出代码改动；该模型是图像生成/编辑模型，官方输出模态为图像，不能提交可评分代码 diff。

最近核验时间：2026-11-04T19:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 评测软件仓库修复并检查代码 diff；该模型输出图像，不提供用于仓库修复的文本/代码输出。

最近核验时间：2026-11-04T19:35+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0)
- [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 评测可运行终端任务的 agent；该模型无工具调用能力且输出图像，不能执行并提交终端任务结果。

最近核验时间：2026-11-04T19:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement)

研究备注：
- 该评测要求 agent 在终端完成科学研究工作流并提交可验证产物；该模型是无工具的图像生成/编辑模型。

最近核验时间：2026-11-04T19:35+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 通过工具执行端到端工作流并检查环境状态；该模型不支持工具调用且输出图像。

最近核验时间：2026-11-04T19:35+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld v2.1 评测长程 GUI/计算机使用 agent；该模型不支持工具调用，不能执行桌面交互。

最近核验时间：2026-11-04T19:35+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography)
- [xAI Grok Imagine Image 2.0 官方模型文档](https://docs.x.ai/developers/models/grok-imagine-image-2.0)

研究备注：
- Chartography 要求模型理解输入图表并给出可评分答案；该模型虽可接收图像，但官方输出模态为图像，不能返回所需的文本答案。

最近核验时间：2026-11-04T19:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Scale AI Humanity's Last Exam 官方排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity’s Last Exam 独立评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 需要可自动评分的选择题或简答答案；该模型仅输出图像，无法提供符合该评分接口的文本回答。

最近核验时间：2026-11-04T19:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5 官方发布说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- Artificial Analysis Intelligence Index v5 是以可评分的知识、编码、科学和 agent 任务组成的综合指数；该图像生成模型没有文本推理/agent 输出接口，指数不适用。

最近核验时间：2026-11-04T19:35+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 通过带 shell 与网页工具的 agent 流程生成文档等工作产物；该模型不支持工具调用且仅输出图像。

最近核验时间：2026-11-04T19:35+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 聚合金融、编码、法律和税务 agent 工作任务；该模型无工具调用和文本推理输出，无法按该指数评测。

最近核验时间：2026-11-04T19:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5 官方发布说明",
          "url": "https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index v5 是以可评分的知识、编码、科学和 agent 任务组成的综合指数；该图像生成模型没有文本推理/agent 输出接口，指数不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方排行榜",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 通过工具执行端到端工作流并检查环境状态；该模型不支持工具调用且输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方说明与排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "xAI Grok Imagine Image 2.0 官方模型文档",
          "url": "https://docs.x.ai/developers/models/grok-imagine-image-2.0"
        }
      ],
      "notes": [
        "Chartography 要求模型理解输入图表并给出可评分答案；该模型虽可接收图像，但官方输出模态为图像，不能返回所需的文本答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 评测长程软件工程任务并产出代码改动；该模型是图像生成/编辑模型，官方输出模态为图像，不能提交可评分代码 diff。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 通过带 shell 与网页工具的 agent 流程生成文档等工作产物；该模型不支持工具调用且仅输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Scale AI Humanity's Last Exam 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam 独立评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 需要可自动评分的选择题或简答答案；该模型仅输出图像，无法提供符合该评分接口的文本回答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方仓库及 v2.1 说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "OSWorld v2.1 评测长程 GUI/计算机使用 agent；该模型不支持工具调用，不能执行桌面交互。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-Bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评测软件仓库修复并检查代码 diff；该模型输出图像，不提供用于仓库修复的文本/代码输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "该评测要求 agent 在终端完成科学研究工作流并提交可验证产物；该模型是无工具的图像生成/编辑模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方排行榜",
          "url": "https://www.tbench.ai/?version=4.0"
        },
        {
          "label": "Terminal-Bench 4.0 版本说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 评测可运行终端任务的 agent；该模型无工具调用能力且输出图像，不能执行并提交终端任务结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:35+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方排行榜与方法说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 聚合金融、编码、法律和税务 agent 工作任务；该模型无工具调用和文本推理输出，无法按该指数评测。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:35+08:00",
  "model_id": "xai/grok-imagine-image-2.0",
  "model_notes": [
    "xAI 官方模型页确认 grok-imagine-image-2.0 接受文本和图像输入、输出图像，用于图像生成与编辑；模型 TOML 记载 tools.supported=false、reasoning.supported=false。",
    "基于上述接口能力，11 项 Benchmark 均要求文本答案、代码/终端任务、工具工作流或综合推理结果，故均记为不适用；未把其他 Grok 对话模型的成绩转录过来。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
