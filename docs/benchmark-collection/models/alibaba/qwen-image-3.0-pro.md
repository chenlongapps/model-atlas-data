# Qwen-Image-3.0-Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen-image-3.0-pro
- 模型名称：Qwen-Image-3.0-Pro
- 发布日期：2026-08-05
- 最近检查时间：2026-11-04T20:00+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地 TOML 与阿里云官方 qwen-image-3.0-pro 型号对应；输入支持文本和图像，输出为 PNG，不支持工具调用或 reasoning。
- 本地 release_date 为 2026-08-05；阿里云发布列表列出 qwen-image-3.0-pro 于 2026-07-20 在 International 发布、2026-08-06 在 Global 发布。保留仓库日期用于队列排序，不据此推测或修改发布日期。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/), [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T20:00+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Scale AI SWE-Bench Pro V2 官方排行榜与方法](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T20:00+08:00 |
| terminal-bench-v4 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 官方方法说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T20:00+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Terminal-Bench-Science 官方公告与方法](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench-Science 官方仓库](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T20:00+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Zapier AutomationBench 官方排行榜与方法](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T20:00+08:00 |
| osworld-v2.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld v2.1 官方发布清单](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T20:00+08:00 |
| chartography | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Chartography 官方任务与评分说明](https://github.com/surge-ai/chartography), [Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T20:00+08:00 |
| humanitys-last-exam | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Scale AI Humanity’s Last Exam 官方榜单与方法](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T20:00+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Artificial Analysis Intelligence Index V5 官方评测](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Qwen-Image-3.0-Pro 图像模型页（非 Intelligence Index）](https://artificialanalysis.ai/image/models/qwen-image-3-0-pro) | 2026-11-04T20:00+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Artificial Analysis GDPval-AA v2.1 官方评测与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T20:00+08:00 |
| vals-index-v2.2 | 不适用 | — | [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro), [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T20:00+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE v1.1 要求模型以编码 Agent 方式解决长程软件工程任务并提供可验证的代码产物；该型号输出 PNG，不支持工具调用。

最近核验时间：2026-11-04T20:00+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Scale AI SWE-Bench Pro V2 官方排行榜与方法](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 要求 Agent 修改代码仓库并提交可验证补丁；图像输出无法提供代码 diff。

最近核验时间：2026-11-04T20:00+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 官方方法说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 要求 Agent 在沙箱终端完成任务；该型号不支持工具调用且仅输出图像。官方榜单未提供可读的该型号成绩。

最近核验时间：2026-11-04T20:00+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Terminal-Bench-Science 官方公告与方法](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench-Science 官方仓库](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Terminal-Bench-Science 0.1 要求 Agent 执行终端科学工作流并产出可验证的分析、计算或研究结果；该型号无法执行终端工作流。

最近核验时间：2026-11-04T20:00+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Zapier AutomationBench 官方排行榜与方法](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 1.0.6 要求 Agent 调用工具完成跨应用工作流并按环境状态评分；该型号不支持工具调用且输出 PNG。

最近核验时间：2026-11-04T20:00+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld v2.1 官方发布清单](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- OSWorld v2.1 要求电脑使用 Agent 在桌面环境执行 GUI 操作；该型号不支持工具调用，无法输出可执行电脑操作。

最近核验时间：2026-11-04T20:00+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Chartography 官方任务与评分说明](https://github.com/surge-ai/chartography)
- [Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 要求读取图表并返回可评分答案；该型号虽可接收图像，但只输出 PNG，无法提交答案。榜单中的 Qwen 对话型号不等于本模型。

最近核验时间：2026-11-04T20:00+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Scale AI Humanity’s Last Exam 官方榜单与方法](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- Humanity’s Last Exam 要求返回可评分的最终文字答案和置信度；该型号只输出图像，无法按该格式作答。

最近核验时间：2026-11-04T20:00+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Artificial Analysis Intelligence Index V5 官方评测](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Qwen-Image-3.0-Pro 图像模型页（非 Intelligence Index）](https://artificialanalysis.ai/image/models/qwen-image-3-0-pro)

研究备注：
- Artificial Analysis Intelligence Index V5 汇总知识、编码、科学与 Agent 等文字/工具任务；该型号的 PNG 输出与该指数不匹配。Artificial Analysis 对该型号的图像专项评测属于另一评测，不映射至此。

最近核验时间：2026-11-04T20:00+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Artificial Analysis GDPval-AA v2.1 官方评测与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 使用 shell 与网页代理完成职业工作任务，并要求文档、幻灯片、图表或表格等工作产物；该型号不支持工具调用且只输出图像。

最近核验时间：2026-11-04T20:00+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud Qwen-Image-3.0-Pro 模型说明](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro)
- [Alibaba Cloud Qwen 图像生成和编辑 API](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 汇总金融、编码、法律和税务 Agent 任务；该型号不能提供相应的文本推理、代码或工具执行结果。

最近核验时间：2026-11-04T20:00+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 官方评测",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Qwen-Image-3.0-Pro 图像模型页（非 Intelligence Index）",
          "url": "https://artificialanalysis.ai/image/models/qwen-image-3-0-pro"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 汇总知识、编码、科学与 Agent 等文字/工具任务；该型号的 PNG 输出与该指数不匹配。Artificial Analysis 对该型号的图像专项评测属于另一评测，不映射至此。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Zapier AutomationBench 官方排行榜与方法",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 1.0.6 要求 Agent 调用工具完成跨应用工作流并按环境状态评分；该型号不支持工具调用且输出 PNG。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Chartography 官方任务与评分说明",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Chartography 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 要求读取图表并返回可评分答案；该型号虽可接收图像，但只输出 PNG，无法提交答案。榜单中的 Qwen 对话型号不等于本模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 方法说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE v1.1 要求模型以编码 Agent 方式解决长程软件工程任务并提供可验证的代码产物；该型号输出 PNG，不支持工具调用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 使用 shell 与网页代理完成职业工作任务，并要求文档、幻灯片、图表或表格等工作产物；该型号不支持工具调用且只输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Scale AI Humanity’s Last Exam 官方榜单与方法",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "Humanity’s Last Exam 要求返回可评分的最终文字答案和置信度；该型号只输出图像，无法按该格式作答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "OSWorld-V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld v2.1 官方发布清单",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "OSWorld v2.1 要求电脑使用 Agent 在桌面环境执行 GUI 操作；该型号不支持工具调用，无法输出可执行电脑操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Scale AI SWE-Bench Pro V2 官方排行榜与方法",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 Agent 修改代码仓库并提交可验证补丁；图像输出无法提供代码 diff。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Terminal-Bench-Science 官方公告与方法",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench-Science 官方仓库",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 0.1 要求 Agent 执行终端科学工作流并产出可验证的分析、计算或研究结果；该型号无法执行终端工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Terminal-Bench 4.0 官方排行榜",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 官方方法说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 要求 Agent 在沙箱终端完成任务；该型号不支持工具调用且仅输出图像。官方榜单未提供可读的该型号成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T20:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud Qwen-Image-3.0-Pro 模型说明",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0-pro"
        },
        {
          "label": "Alibaba Cloud Qwen 图像生成和编辑 API",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference"
        },
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 汇总金融、编码、法律和税务 Agent 任务；该型号不能提供相应的文本推理、代码或工具执行结果。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T20:00+08:00",
  "model_id": "alibaba/qwen-image-3.0-pro",
  "model_notes": [
    "本地 TOML 与阿里云官方 qwen-image-3.0-pro 型号对应；输入支持文本和图像，输出为 PNG，不支持工具调用或 reasoning。",
    "本地 release_date 为 2026-08-05；阿里云发布列表列出 qwen-image-3.0-pro 于 2026-07-20 在 International 发布、2026-08-06 在 Global 发布。保留仓库日期用于队列排序，不据此推测或修改发布日期。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
