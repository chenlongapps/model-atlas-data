# MiniMax H3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：minimax/MiniMax-H3
- 模型名称：MiniMax H3
- 发布日期：2026-07-31
- 最近检查时间：2026-11-04T21:22+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- MiniMax 官方发布资料和模型卡将 H3 定义为多模态音视频生成模型；支持文字、图像、视频和音频参考输入，官方生成输出为视频和音频。模型源文件同时标记 tools.supported=false、reasoning.supported=false。
- 因此本轮 11 项编码代理、桌面/业务 agent、文本推理和综合能力基准均不适用；没有把 MiniMax M3/M3.1 等其他型号的成绩归给 H3。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [DeepSWE 官方排行榜](https://deepswe.datacurve.ai/) | 2026-11-04T21:22+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Scale AI SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T21:22+08:00 |
| terminal-bench-v4 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Terminal-Bench 官方说明](https://www.tbench.ai/) | 2026-11-04T21:22+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Terminal-Bench-Science 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T21:22+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Zapier AutomationBench 官方页面](https://zapier.com/benchmarks) | 2026-11-04T21:22+08:00 |
| osworld-v2.1 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T21:22+08:00 |
| chartography | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Chartography 官方说明与榜单](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T21:22+08:00 |
| humanitys-last-exam | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Artificial Analysis HLE 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T21:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Artificial Analysis Intelligence Index 官方页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T21:22+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Artificial Analysis GDPval-AA 官方页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T21:22+08:00 |
| vals-index-v2.2 | 不适用 | — | [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3), [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source), [Vals AI Vals Index 2.2 官方页](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [DeepSWE 官方排行榜](https://deepswe.datacurve.ai/)

研究备注：
- 评测对象为长程软件工程代码代理；H3 官方模型变体用于音视频生成。未将榜单上的 MiniMax M3 结果归给 H3。

最近核验时间：2026-11-04T21:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Scale AI SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 该项要求代码代理解决仓库问题；H3 官方定义为音视频生成模型，不适用。

最近核验时间：2026-11-04T21:22+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Terminal-Bench 官方说明](https://www.tbench.ai/)

研究备注：
- 该项评估代理执行终端任务；H3 官方任务为音视频生成，不适用。

最近核验时间：2026-11-04T21:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Terminal-Bench-Science 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 该项评估终端科学工作流；H3 官方任务为音视频生成，不适用。

最近核验时间：2026-11-04T21:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Zapier AutomationBench 官方页面](https://zapier.com/benchmarks)

研究备注：
- 该项要求 agent 在模拟业务应用中操作工具并完成工作流；H3 的模型文件标记 tools 不支持，官方输出为视频和音频，不适用。

最近核验时间：2026-11-04T21:22+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- 该项要求 agent 操作桌面环境；H3 不支持工具，输入媒体用于生成参考，输出仍为视频和音频，不适用。

最近核验时间：2026-11-04T21:22+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Chartography 官方说明与榜单](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 该项要求视觉图表理解并以答案准确率计分；H3 可接收图像，但官方变体输出视频和音频，没有匹配的图表问答输出，不适用。

最近核验时间：2026-11-04T21:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Artificial Analysis HLE 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 该项要求对学术问题生成答案；H3 官方定义的输出类型为视频和音频，没有该文本推理输出，不适用。

最近核验时间：2026-11-04T21:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Artificial Analysis Intelligence Index 官方页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 该指数聚合知识、编码、科学和通识等语言模型评测；H3 官方定义为音视频生成模型，不适用。

最近核验时间：2026-11-04T21:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Artificial Analysis GDPval-AA 官方页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 该项要求 agent 产出专业工作文件；H3 官方定义的输出是视频和音频，不适用。

最近核验时间：2026-11-04T21:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [MiniMax H3 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [MiniMax H3 官方发布页](https://www.minimax.io/news/minimax-h3-open-source)
- [Vals AI Vals Index 2.2 官方页](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 该指数评价金融、编码、法律及税务任务中的 agent；H3 是音视频生成模型，不适用。榜单中的 MiniMax M3.1-Flash 是另一型号。

最近核验时间：2026-11-04T21:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Artificial Analysis Intelligence Index 官方页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "该指数聚合知识、编码、科学和通识等语言模型评测；H3 官方定义为音视频生成模型，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Zapier AutomationBench 官方页面",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "该项要求 agent 在模拟业务应用中操作工具并完成工作流；H3 的模型文件标记 tools 不支持，官方输出为视频和音频，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Chartography 官方说明与榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "该项要求视觉图表理解并以答案准确率计分；H3 可接收图像，但官方变体输出视频和音频，没有匹配的图表问答输出，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "DeepSWE 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "评测对象为长程软件工程代码代理；H3 官方模型变体用于音视频生成。未将榜单上的 MiniMax M3 结果归给 H3。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Artificial Analysis GDPval-AA 官方页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "该项要求 agent 产出专业工作文件；H3 官方定义的输出是视频和音频，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Artificial Analysis HLE 评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "该项要求对学术问题生成答案；H3 官方定义的输出类型为视频和音频，没有该文本推理输出，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "OSWorld V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "该项要求 agent 操作桌面环境；H3 不支持工具，输入媒体用于生成参考，输出仍为视频和音频，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "该项要求代码代理解决仓库问题；H3 官方定义为音视频生成模型，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Terminal-Bench-Science 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "该项评估终端科学工作流；H3 官方任务为音视频生成，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Terminal-Bench 官方说明",
          "url": "https://www.tbench.ai/"
        }
      ],
      "notes": [
        "该项评估代理执行终端任务；H3 官方任务为音视频生成，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:22+08:00",
      "checked_sources": [
        {
          "label": "MiniMax H3 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-H3"
        },
        {
          "label": "MiniMax H3 官方发布页",
          "url": "https://www.minimax.io/news/minimax-h3-open-source"
        },
        {
          "label": "Vals AI Vals Index 2.2 官方页",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "该指数评价金融、编码、法律及税务任务中的 agent；H3 是音视频生成模型，不适用。榜单中的 MiniMax M3.1-Flash 是另一型号。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:22+08:00",
  "model_id": "minimax/MiniMax-H3",
  "model_notes": [
    "MiniMax 官方发布资料和模型卡将 H3 定义为多模态音视频生成模型；支持文字、图像、视频和音频参考输入，官方生成输出为视频和音频。模型源文件同时标记 tools.supported=false、reasoning.supported=false。",
    "因此本轮 11 项编码代理、桌面/业务 agent、文本推理和综合能力基准均不适用；没有把 MiniMax M3/M3.1 等其他型号的成绩归给 H3。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
