# Qwen-Image-3.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen-image-3.0
- 模型名称：Qwen-Image-3.0
- 发布日期：2026-08-05
- 最近检查时间：2026-11-04T19:54+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 阿里云官方资料将 qwen-image-3.0 列为图像生成模型，官方 API 为文字/参考图输入、图像输出；本地 TOML 也列出 image/png 输出并标记 reasoning/tools 不支持。
- 本地 TOML 的 release_date 是 2026-08-05，而阿里云官方发布列表显示 qwen-image-3.0 日期为 2026-08-04。保留仓库字段用于队列排序，不在本次 benchmark 收集中修改发布日期。
- 逐项检查后，11 项均要求文本答案、代码/终端/GUI/工具工作流或综合推理输出，因此均标为不适用；未将 Qwen 对话模型成绩移植。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/) | 2026-11-04T19:54+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T19:54+08:00 |
| terminal-bench-v4 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0), [Artificial Analysis Terminal-Bench 4.0 官方评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T19:54+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement), [Harbor 官方 benchmark 仓库](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T19:54+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T19:54+08:00 |
| osworld-v2.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T19:54+08:00 |
| chartography | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T19:54+08:00 |
| humanitys-last-exam | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Scale AI Humanity's Last Exam 官方排行榜与方法](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity's Last Exam 方法页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T19:54+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Artificial Analysis Intelligence Index v5 官方说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5), [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Image Lab（单独图像评测）](https://artificialanalysis.ai/image/image-lab/) | 2026-11-04T19:54+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Benchmark 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T19:54+08:00 |
| vals-index-v2.2 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference), [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T19:54+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 评测长程软件工程任务，需要代码文本、代码修改及 agent 行为；Qwen-Image-3.0 是图像生成/编辑模型，只输出 PNG 且不支持工具。

最近核验时间：2026-11-04T19:54+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 需要提交代码补丁并运行仓库测试；图像输出模型不能提供可评分代码 diff。

最近核验时间：2026-11-04T19:54+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0)
- [Artificial Analysis Terminal-Bench 4.0 官方评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- Terminal-Bench 4.0 要求 agent 执行终端任务；该模型不支持工具或 reasoning，输出为图像。

最近核验时间：2026-11-04T19:54+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Harbor 官方 benchmark 仓库](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Terminal-Bench-Science 要求 agent 在终端完成科学工作流并产生可验证的研究产物；该模型不能操作终端，且输出 PNG。

最近核验时间：2026-11-04T19:54+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 要求 agent 调用工具完成跨应用工作流并按环境状态评分；该模型不支持工具调用，输出为图像。

最近核验时间：2026-11-04T19:54+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 评测长时程 GUI/计算机使用 agent；模型没有工具调用能力，且无法输出可执行的桌面操作。

最近核验时间：2026-11-04T19:54+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 需要模型理解输入图表并返回可评分的文本答案；该模型接受图像但只输出 PNG，无法给出评测答案。

最近核验时间：2026-11-04T19:54+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Scale AI Humanity's Last Exam 官方排行榜与方法](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity's Last Exam 方法页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 要求返回可自动评分的 final answer 与 confidence；Qwen-Image-3.0 只输出 PNG。图像输入能力不足以替代文本应答输出。

最近核验时间：2026-11-04T19:54+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Artificial Analysis Intelligence Index v5 官方说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)
- [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Image Lab（单独图像评测）](https://artificialanalysis.ai/image/image-lab/)

研究备注：
- AA Intelligence Index v5 聚合知识、编码、科学和 agent 任务；该模型为图像生成/编辑接口，无法完成这些任务需要的文本答案、代码和工具流程。Qwen-Image-3.0 出现在 AA Image Lab 的图像评测不等同于 Intelligence Index v5。

最近核验时间：2026-11-04T19:54+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Benchmark 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- GDPval-AA v2.1 使用 shell 与网页工具执行职业工作任务，并产出文档、幻灯片、图表或表格；该模型无工具调用且仅输出图像。

最近核验时间：2026-11-04T19:54+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0 官方发布列表](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud Qwen-Image-3.0 官方 API 参考](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 聚合金融、编码、法律和税务 agent 任务；该模型不提供文本推理输出或工具执行能力。

最近核验时间：2026-11-04T19:54+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5 官方说明",
          "url": "https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5"
        },
        {
          "label": "Artificial Analysis Intelligence Index 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Image Lab（单独图像评测）",
          "url": "https://artificialanalysis.ai/image/image-lab/"
        }
      ],
      "notes": [
        "AA Intelligence Index v5 聚合知识、编码、科学和 agent 任务；该模型为图像生成/编辑接口，无法完成这些任务需要的文本答案、代码和工具流程。Qwen-Image-3.0 出现在 AA Image Lab 的图像评测不等同于 Intelligence Index v5。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Zapier AutomationBench 官方排行榜",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 要求 agent 调用工具完成跨应用工作流并按环境状态评分；该模型不支持工具调用，输出为图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Surge Chartography 官方说明与排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 需要模型理解输入图表并返回可评分的文本答案；该模型接受图像但只输出 PNG，无法给出评测答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 评测长程软件工程任务，需要代码文本、代码修改及 agent 行为；Qwen-Image-3.0 是图像生成/编辑模型，只输出 PNG 且不支持工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Benchmark 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 使用 shell 与网页工具执行职业工作任务，并产出文档、幻灯片、图表或表格；该模型无工具调用且仅输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Scale AI Humanity's Last Exam 官方排行榜与方法",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam 方法页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 要求返回可自动评分的 final answer 与 confidence；Qwen-Image-3.0 只输出 PNG。图像输入能力不足以替代文本应答输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "OSWorld-V2 官方仓库及 v2.1 说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 评测长时程 GUI/计算机使用 agent；模型没有工具调用能力，且无法输出可执行的桌面操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Scale AI SWE-Bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 需要提交代码补丁并运行仓库测试；图像输出模型不能提供可评分代码 diff。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Terminal-Bench-Science 0.1 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor 官方 benchmark 仓库",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 要求 agent 在终端完成科学工作流并产生可验证的研究产物；该模型不能操作终端，且输出 PNG。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Terminal-Bench 4.0 官方排行榜",
          "url": "https://www.tbench.ai/?version=4.0"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 要求 agent 执行终端任务；该模型不支持工具或 reasoning，输出为图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:54+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方发布列表",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Alibaba Cloud Qwen-Image-3.0 官方 API 参考",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Vals Index v2.2 官方排行榜与方法说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 聚合金融、编码、法律和税务 agent 任务；该模型不提供文本推理输出或工具执行能力。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:54+08:00",
  "model_id": "alibaba/qwen-image-3.0",
  "model_notes": [
    "阿里云官方资料将 qwen-image-3.0 列为图像生成模型，官方 API 为文字/参考图输入、图像输出；本地 TOML 也列出 image/png 输出并标记 reasoning/tools 不支持。",
    "本地 TOML 的 release_date 是 2026-08-05，而阿里云官方发布列表显示 qwen-image-3.0 日期为 2026-08-04。保留仓库字段用于队列排序，不在本次 benchmark 收集中修改发布日期。",
    "逐项检查后，11 项均要求文本答案、代码/终端/GUI/工具工作流或综合推理输出，因此均标为不适用；未将 Qwen 对话模型成绩移植。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
