# Wan3.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/wan3.0-video
- 模型名称：Wan3.0
- 发布日期：2026-08-06
- 最近检查时间：2026-11-04T19:37+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 阿里云 Model Studio 官方资料将 wan3.0-video 列为视频生成模型，发布日为 2026-08-06，支持文本/图像/视频等参考输入并生成最多 30 秒视频；模型 TOML 明确输出为 video/mp4，且 tools/reasoning 均不支持。
- 依照各项 Benchmark 对代码补丁、终端/GUI/工具执行或可评分文本答案的要求，11 项均不适用于此模型；未把其他 Wan 或 Alibaba 对话模型的成绩归到 Wan3.0。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/) | 2026-11-04T19:37+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T19:37+08:00 |
| terminal-bench-v4 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0), [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T19:37+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement) | 2026-11-04T19:37+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T19:37+08:00 |
| osworld-v2.1 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T19:37+08:00 |
| chartography | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T19:37+08:00 |
| humanitys-last-exam | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Scale AI Humanity's Last Exam 官方排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity’s Last Exam 独立评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T19:37+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Artificial Analysis Intelligence Index v5 官方发布说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T19:37+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T19:37+08:00 |
| vals-index-v2.2 | 不适用 | — | [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide), [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T19:37+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 测量长程软件工程任务，需要产出代码改动；Wan3.0 是视频生成模型，输出 video/mp4。

最近核验时间：2026-11-04T19:37+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 评测代码仓库修复并检查代码补丁；Wan3.0 的视频输出不符合可评分的代码 diff。

最近核验时间：2026-11-04T19:37+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0)
- [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 要求 agent 执行终端任务；Wan3.0 不支持工具调用或推理，输出视频。

最近核验时间：2026-11-04T19:37+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement)

研究备注：
- 该项评测要求 agent 在终端执行科学研究工作流并提交可验证产物；Wan3.0 是无工具的视频生成模型。

最近核验时间：2026-11-04T19:37+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 通过工具执行端到端工作流并检查环境状态；Wan3.0 不支持工具调用，且输出为视频。

最近核验时间：2026-11-04T19:37+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld v2.1 评测长程 GUI/计算机使用 agent；Wan3.0 不支持工具调用，不能执行桌面操作。

最近核验时间：2026-11-04T19:37+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 评测图表理解并需要可评分的答案；Wan3.0 输出 video/mp4，不能提供所需回答。

最近核验时间：2026-11-04T19:37+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Scale AI Humanity's Last Exam 官方排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity’s Last Exam 独立评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 需要可自动评分的选择题或简答答案；Wan3.0 仅输出视频，不适合该文本应答评测。

最近核验时间：2026-11-04T19:37+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Artificial Analysis Intelligence Index v5 官方发布说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- AA Intelligence Index v5 综合知识、编码、科学与 agent 任务；Wan3.0 是视频生成模型，不提供文本推理或 agent 输出。

最近核验时间：2026-11-04T19:37+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 使用 shell 和网页工具完成工作任务并产出文档等结果；Wan3.0 不支持工具调用，输出为视频。

最近核验时间：2026-11-04T19:37+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [阿里云 Model Studio Wan3.0 官方指南](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide)
- [阿里云 Model Studio 发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 聚合金融、编码、法律和税务 agent 工作任务；Wan3.0 不支持文本推理与工具执行。

最近核验时间：2026-11-04T19:37+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5 官方发布说明",
          "url": "https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "AA Intelligence Index v5 综合知识、编码、科学与 agent 任务；Wan3.0 是视频生成模型，不提供文本推理或 agent 输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
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
        "AutomationBench 通过工具执行端到端工作流并检查环境状态；Wan3.0 不支持工具调用，且输出为视频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Surge Chartography 官方说明与排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 评测图表理解并需要可评分的答案；Wan3.0 输出 video/mp4，不能提供所需回答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 测量长程软件工程任务，需要产出代码改动；Wan3.0 是视频生成模型，输出 video/mp4。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 使用 shell 和网页工具完成工作任务并产出文档等结果；Wan3.0 不支持工具调用，输出为视频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
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
        "HLE 需要可自动评分的选择题或简答答案；Wan3.0 仅输出视频，不适合该文本应答评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
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
        "OSWorld v2.1 评测长程 GUI/计算机使用 agent；Wan3.0 不支持工具调用，不能执行桌面操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Scale AI SWE-Bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评测代码仓库修复并检查代码补丁；Wan3.0 的视频输出不符合可评分的代码 diff。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Terminal-Bench-Science 0.1 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "该项评测要求 agent 在终端执行科学研究工作流并提交可验证产物；Wan3.0 是无工具的视频生成模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
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
        "Terminal-Bench 4.0 要求 agent 执行终端任务；Wan3.0 不支持工具调用或推理，输出视频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:37+08:00",
      "checked_sources": [
        {
          "label": "阿里云 Model Studio Wan3.0 官方指南",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/wan3-video-generation-guide"
        },
        {
          "label": "阿里云 Model Studio 发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Vals Index v2.2 官方排行榜与方法说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 聚合金融、编码、法律和税务 agent 工作任务；Wan3.0 不支持文本推理与工具执行。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:37+08:00",
  "model_id": "alibaba/wan3.0-video",
  "model_notes": [
    "阿里云 Model Studio 官方资料将 wan3.0-video 列为视频生成模型，发布日为 2026-08-06，支持文本/图像/视频等参考输入并生成最多 30 秒视频；模型 TOML 明确输出为 video/mp4，且 tools/reasoning 均不支持。",
    "依照各项 Benchmark 对代码补丁、终端/GUI/工具执行或可评分文本答案的要求，11 项均不适用于此模型；未把其他 Wan 或 Alibaba 对话模型的成绩归到 Wan3.0。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
