# MiniCPM5-2B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openbmb/minicpm5-2b
- 模型名称：MiniCPM5-2B
- 发布日期：2026-09-06
- 最近检查时间：2026-11-04T12:36+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T12:36+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T12:36+08:00 |
| terminal-bench-v4 | 待核实 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 release](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T12:36+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Terminal-Bench Science official site](https://www.terminal-bench-science.ai/) | 2026-11-04T12:36+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Artificial Analysis AutomationBench-AA evaluation](https://artificialanalysis.ai/evaluations/automationbench-aa/) | 2026-11-04T12:36+08:00 |
| osworld-v2.1 | 不适用 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-04T12:36+08:00 |
| chartography | 不适用 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography) | 2026-11-04T12:36+08:00 |
| humanitys-last-exam | 已收录 | 8.9 (metric=accuracy; dataset=2,158 text-only questions from the 2,500-question HLE dataset; variant=pass@1; GPT-5.6 Luna (medium) equality checker) | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Artificial Analysis MiniCPM5-2B results](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Humanity's Last Exam official evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T12:36+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis MiniCPM5-2B profile](https://artificialanalysis.ai/models/minicpm5-2b/), [Artificial Analysis Intelligence Index V5 evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis MiniCPM5-2B v4.2 results article](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b) | 2026-11-04T12:36+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis MiniCPM5-2B results](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa) | 2026-11-04T12:36+08:00 |
| vals-index-v2.2 | 待核实 | — | [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index earlier v2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-04T12:36+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 官方榜单注明 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 MiniCPM5-2B；不能据此确认完整榜单中没有发布后结果。

尚未解决的问题：
- 官方榜单注明 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 MiniCPM5-2B；不能据此确认完整榜单中没有发布后结果。

最近核验时间：2026-11-04T12:36+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 模型卡列出 SWE-bench Pro 14.4，但没有注明 V2.0.0、指标或测试条件；Scale V2 榜单没有可核实的对应条目，故不补猜版本或 harness。

尚未解决的问题：
- 模型卡列出 SWE-bench Pro 14.4，但没有注明 V2.0.0、指标或测试条件；Scale V2 榜单没有可核实的对应条目，故不补猜版本或 harness。

最近核验时间：2026-11-04T12:36+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 release](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 模型卡列出 Terminal-Bench v2.1 8.6，不属于目标 v4.0.0；V4 官方结果行当前无法读取，没有可确认的 V4 成绩。

尚未解决的问题：
- 模型卡列出 Terminal-Bench v2.1 8.6，不属于目标 v4.0.0；V4 官方结果行当前无法读取，没有可确认的 V4 成绩。

最近核验时间：2026-11-04T12:36+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Terminal-Bench Science official site](https://www.terminal-bench-science.ai/)

研究备注：
- 模型卡未列该项目；官方动态结果页面无法核验完整结果行，因此不能仅凭当前页面断言未参测。

尚未解决的问题：
- 模型卡未列该项目；官方动态结果页面无法核验完整结果行，因此不能仅凭当前页面断言未参测。

最近核验时间：2026-11-04T12:36+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Artificial Analysis AutomationBench-AA evaluation](https://artificialanalysis.ai/evaluations/automationbench-aa/)

研究备注：
- Zapier 官方榜单确认 1.0.6，但目前页面只呈现部分结果，未见 MiniCPM5-2B。Artificial Analysis AutomationBench-AA 是不同私有测试配置和指标，不符合本地定义的 task_completed_correctly，未转录。

尚未解决的问题：
- Zapier 官方榜单确认 1.0.6，但目前页面只呈现部分结果，未见 MiniCPM5-2B。Artificial Analysis AutomationBench-AA 是不同私有测试配置和指标，不符合本地定义的 task_completed_correctly，未转录。

最近核验时间：2026-11-04T12:36+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- OSWorld v2.1 要求按屏幕截图进行 GUI 操作；MiniCPM5-2B 仅支持文本输入，无法独立处理截图。第三方 OSWorld-Verified 估算不属于目标 v2.1。

最近核验时间：2026-11-04T12:36+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)

研究备注：
- Chartography 要求理解图表图像并生成可评分答案；MiniCPM5-2B 仅支持文本输入，不适用于图像输入任务。

最近核验时间：2026-11-04T12:36+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 8.9
- metric: accuracy
- dataset: 2,158 text-only questions from the 2,500-question HLE dataset
- variant: pass@1; GPT-5.6 Luna (medium) equality checker
- source: [https://huggingface.co/openbmb/MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Artificial Analysis MiniCPM5-2B results](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Humanity's Last Exam official evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 已收录精确成绩 8.9。OpenBMB 最终 BF16 模型卡将其标为来自 Artificial Analysis 的结果；AA 发布文章显示四舍五入后的 9%。AA 方法使用原始 HLE 的 2,158 道文本题、pass@1 和 GPT-5.6 Luna (medium) equality checker，故以 dataset 与 variant 字段保留该配置，不视为全部 2,500 题的成绩。来源未公布评测日期，未填写 date。

最近核验时间：2026-11-04T12:36+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis MiniCPM5-2B profile](https://artificialanalysis.ai/models/minicpm5-2b/)
- [Artificial Analysis Intelligence Index V5 evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis MiniCPM5-2B v4.2 results article](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b)

研究备注：
- 精确模型的 Artificial Analysis 当前 profile 显示 V5 Intelligence Index 为 N/A；官方已发布的 15 分明确属于 v4.2（更早的 23 分属于 v4.1.1），不适用于目标 V5.0。

最近核验时间：2026-11-04T12:36+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis MiniCPM5-2B results](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)

研究备注：
- AA 发布文章报告 831 Elo，但明确为旧版 GDPval-AA v2、人类锚点 1000；目标 v2.1 使用 DeepSeek V4.1 Flash (max)=1600 锚点及 Crowd-BT，无法换算。模型卡的 19.6 也没有足够指标/版本信息。

尚未解决的问题：
- AA 发布文章报告 831 Elo，但明确为旧版 GDPval-AA v2、人类锚点 1000；目标 v2.1 使用 DeepSeek V4.1 Flash (max)=1600 锚点及 Crowd-BT，无法换算。模型卡的 19.6 也没有足够指标/版本信息。

最近核验时间：2026-11-04T12:36+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [OpenBMB MiniCPM5-2B official model card](https://huggingface.co/openbmb/MiniCPM5-2B)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index earlier v2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- Vals 官方 v2.2 榜单显示的是 Best/Frontier 部分模型列表，未见 MiniCPM5-2B，但页面不是完整名单；当前没有可核实的目标版本成绩。

尚未解决的问题：
- Vals 官方 v2.2 榜单显示的是 Best/Frontier 部分模型列表，未见 MiniCPM5-2B，但页面不是完整名单；当前没有可核实的目标版本成绩。

最近核验时间：2026-11-04T12:36+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniCPM5-2B profile",
          "url": "https://artificialanalysis.ai/models/minicpm5-2b/"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis MiniCPM5-2B v4.2 results article",
          "url": "https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b"
        }
      ],
      "notes": [
        "精确模型的 Artificial Analysis 当前 profile 显示 V5 Intelligence Index 为 N/A；官方已发布的 15 分明确属于 v4.2（更早的 23 分属于 v4.1.1），不适用于目标 V5.0。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/automationbench-aa/"
        }
      ],
      "notes": [
        "Zapier 官方榜单确认 1.0.6，但目前页面只呈现部分结果，未见 MiniCPM5-2B。Artificial Analysis AutomationBench-AA 是不同私有测试配置和指标，不符合本地定义的 task_completed_correctly，未转录。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 官方榜单确认 1.0.6，但目前页面只呈现部分结果，未见 MiniCPM5-2B。Artificial Analysis AutomationBench-AA 是不同私有测试配置和指标，不符合本地定义的 task_completed_correctly，未转录。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
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
        "Chartography 要求理解图表图像并生成可评分答案；MiniCPM5-2B 仅支持文本输入，不适用于图像输入任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "官方榜单注明 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 MiniCPM5-2B；不能据此确认完整榜单中没有发布后结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单注明 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 MiniCPM5-2B；不能据此确认完整榜单中没有发布后结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniCPM5-2B results",
          "url": "https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Intelligence Benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        }
      ],
      "notes": [
        "AA 发布文章报告 831 Elo，但明确为旧版 GDPval-AA v2、人类锚点 1000；目标 v2.1 使用 DeepSeek V4.1 Flash (max)=1600 锚点及 Crowd-BT，无法换算。模型卡的 19.6 也没有足够指标/版本信息。"
      ],
      "status": "待核实",
      "unresolved": [
        "AA 发布文章报告 831 Elo，但明确为旧版 GDPval-AA v2、人类锚点 1000；目标 v2.1 使用 DeepSeek V4.1 Flash (max)=1600 锚点及 Crowd-BT，无法换算。模型卡的 19.6 也没有足够指标/版本信息。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "Artificial Analysis MiniCPM5-2B results",
          "url": "https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b"
        },
        {
          "label": "Artificial Analysis Intelligence Benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Humanity's Last Exam official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "已收录精确成绩 8.9。OpenBMB 最终 BF16 模型卡将其标为来自 Artificial Analysis 的结果；AA 发布文章显示四舍五入后的 9%。AA 方法使用原始 HLE 的 2,158 道文本题、pass@1 和 GPT-5.6 Luna (medium) equality checker，故以 dataset 与 variant 字段保留该配置，不视为全部 2,500 题的成绩。来源未公布评测日期，未填写 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "OSWorld v2.1 要求按屏幕截图进行 GUI 操作；MiniCPM5-2B 仅支持文本输入，无法独立处理截图。第三方 OSWorld-Verified 估算不属于目标 v2.1。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "模型卡列出 SWE-bench Pro 14.4，但没有注明 V2.0.0、指标或测试条件；Scale V2 榜单没有可核实的对应条目，故不补猜版本或 harness。"
      ],
      "status": "待核实",
      "unresolved": [
        "模型卡列出 SWE-bench Pro 14.4，但没有注明 V2.0.0、指标或测试条件；Scale V2 榜单没有可核实的对应条目，故不补猜版本或 harness。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "Terminal-Bench Science official site",
          "url": "https://www.terminal-bench-science.ai/"
        }
      ],
      "notes": [
        "模型卡未列该项目；官方动态结果页面无法核验完整结果行，因此不能仅凭当前页面断言未参测。"
      ],
      "status": "待核实",
      "unresolved": [
        "模型卡未列该项目；官方动态结果页面无法核验完整结果行，因此不能仅凭当前页面断言未参测。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 release",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "模型卡列出 Terminal-Bench v2.1 8.6，不属于目标 v4.0.0；V4 官方结果行当前无法读取，没有可确认的 V4 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "模型卡列出 Terminal-Bench v2.1 8.6，不属于目标 v4.0.0；V4 官方结果行当前无法读取，没有可确认的 V4 成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T12:36+08:00",
      "checked_sources": [
        {
          "label": "OpenBMB MiniCPM5-2B official model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-2B"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index earlier v2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "Vals 官方 v2.2 榜单显示的是 Best/Frontier 部分模型列表，未见 MiniCPM5-2B，但页面不是完整名单；当前没有可核实的目标版本成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "Vals 官方 v2.2 榜单显示的是 Best/Frontier 部分模型列表，未见 MiniCPM5-2B，但页面不是完整名单；当前没有可核实的目标版本成绩。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T12:36+08:00",
  "model_id": "openbmb/minicpm5-2b",
  "new_records": 1,
  "overall_status": "待复核"
}

-->
