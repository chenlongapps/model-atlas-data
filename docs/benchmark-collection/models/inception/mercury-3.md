# Mercury 3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inception/mercury-3
- 模型名称：Mercury 3
- 发布日期：2026-10-16
- 最近检查时间：2026-11-04T02:21+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 Full 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| terminal-bench-v4 | 已收录 | 3.03 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (66 tasks), Vals AI evaluation; variant=avg@3; mean of 3 full pass@1 runs; 8-hour agent time limit per task; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 官方榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Vals AI Mercury 3 模型页](https://www.vals.ai/models/inception_mercury-3), [Terminal-Bench 4.0 官方定义](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T02:21+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Artificial Analysis Terminal-Bench Science 0.1 方法页](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Vals AI Mercury 3 模型页](https://www.vals.ai/models/inception_mercury-3), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库与方法](https://github.com/zapier/AutomationBench), [Inception Mercury 3 API 文档](https://docs.inceptionlabs.ai/get-started/models), [Inception Mercury 3 FAQ](https://docs.inceptionlabs.ai/resources/faq), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 官方项目页](https://osworld-v2.xlang.ai/), [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2), [Inception Mercury 3 API 文档](https://docs.inceptionlabs.ai/get-started/models), [Inception Mercury 3 FAQ](https://docs.inceptionlabs.ai/resources/faq), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测仓库与方法](https://github.com/surge-ai/chartography), [Inception Mercury 3 API 文档](https://docs.inceptionlabs.ai/get-started/models), [Inception Mercury 3 FAQ](https://docs.inceptionlabs.ai/resources/faq), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity’s Last Exam 页面](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis 模型目录](https://artificialanalysis.ai/models), [Artificial Analysis Intelligence Index V5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3) | 2026-11-04T02:21+08:00 |
| vals-index-v2.2 | 已收录 | 43.66 (metric=performance score; version=2.2) | [Vals AI Mercury 3 模型页](https://www.vals.ai/models/inception_mercury-3), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T02:21+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- 已检查 Datacurve 官方 v1.1 榜单与 Inception 发布文正文，未找到 Mercury 3 的可核实 DeepSWE 成绩。Datacurve 榜单最后可见更新为 2026-09-22，早于 Mercury 3 官方公开发布；Inception 发布文另含一张图像版 benchmark 图，当前可读文本无法识别图中项目和值，因此本结论仅限可读资料。

最近核验时间：2026-11-04T02:21+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 Full 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- 已检查 Scale 官方 V2 Full 榜单和 Inception 发布文正文，未找到 Mercury 3 的可引用成绩。Scale 页面标注更新于 2026-09-22，早于模型官方公开发布；未使用估算站点分数。Inception 发布文另含当前无法读取的图像版 benchmark 图，因此本结论仅限可读资料。

最近核验时间：2026-11-04T02:21+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 3.03
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (66 tasks), Vals AI evaluation
- variant: avg@3; mean of 3 full pass@1 runs; 8-hour agent time limit per task
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 官方榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Vals AI Mercury 3 模型页](https://www.vals.ai/models/inception_mercury-3)
- [Terminal-Bench 4.0 官方定义](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Vals AI 官方榜单列出 Mercury 3：3.03%，Mini-SWE-agent harness。方法页说明版本 4.0 的完整 66 项任务每模型运行三次，每次 pass@1，公布 avg@3 均值；本记录保留为该独立 Vals 执行配置。Vals 页面版本写 4.0，映射到本仓库定义的 4.0.0。页面的 2026-10-29 是更新日期，不是已确认的评测日期；模型页标注 high 也不能确认是本项运行档位，因此均未写入。

最近核验时间：2026-11-04T02:21+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Terminal-Bench Science 0.1 方法页](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Vals AI Mercury 3 模型页](https://www.vals.ai/models/inception_mercury-3)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- 已检查 Artificial Analysis 的 Terminal-Bench Science 0.1 方法页、Vals Mercury 3 模型页和 Inception 发布文正文，未找到 Mercury 3 对应分数。AA 可读页说明该 benchmark 的版本和方法，但动态结果区没有可读的该模型行；Inception 发布文另含当前无法读取的图像版 benchmark 图。

最近核验时间：2026-11-04T02:21+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库与方法](https://github.com/zapier/AutomationBench)
- [Inception Mercury 3 API 文档](https://docs.inceptionlabs.ai/get-started/models)
- [Inception Mercury 3 FAQ](https://docs.inceptionlabs.ai/resources/faq)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- Mercury 3 支持 tool calling，故不能仅凭文本输入判为不适用。Zapier 官方榜单可见前十项及“See 119 more”，当前文本无法核验折叠列表中是否有 Mercury 3；官方发布文正文也没有可核实的 AutomationBench 分数。其 benchmark 图像未能从页面文本读取。

尚未解决的问题：
- 需要核实 Zapier 官方榜单折叠项，或找到 Mercury 3 的原始 AutomationBench 评测结果及数据集条件。

最近核验时间：2026-11-04T02:21+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 官方项目页](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2)
- [Inception Mercury 3 API 文档](https://docs.inceptionlabs.ai/get-started/models)
- [Inception Mercury 3 FAQ](https://docs.inceptionlabs.ai/resources/faq)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- OSWorld 官方动态榜单的当前文本快照未显示可核验的 Mercury 3 行；Inception 文档确认模型原生文本输入并支持 tools，但外部 OCR/GUI wrapper 可能改变路径，不能据此直接判不适用。没有找到可核实分数。

尚未解决的问题：
- 官方动态榜单内容未能读取；若存在 wrapper 结果，需确认精确版本、指标和运行配置。

最近核验时间：2026-11-04T02:21+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测仓库与方法](https://github.com/surge-ai/chartography)
- [Inception Mercury 3 API 文档](https://docs.inceptionlabs.ai/get-started/models)
- [Inception Mercury 3 FAQ](https://docs.inceptionlabs.ai/resources/faq)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- Surge 官方榜单和方法仓库可读内容中未找到 Mercury 3 成绩。Mercury 3 原生只接受文本输入，不能直接处理标准图表图像；目前没有该模型使用 OCR/图表转写 wrapper 的来源。Inception 发布文另含无法从页面文本读取的图像版 benchmark 图。

最近核验时间：2026-11-04T02:21+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity’s Last Exam 页面](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- 已检查 Scale 原始 HLE 榜单、Artificial Analysis HLE 页面及 Inception 发布文正文，未找到 Mercury 3 的原始 2,500 题 HLE 成绩；未用 Vals HLAB-Vals-1.1 或其他 HLE 子集替代。官方发布文图像版 benchmark 图当前无法读取。

最近核验时间：2026-11-04T02:21+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 模型目录](https://artificialanalysis.ai/models)
- [Artificial Analysis Intelligence Index V5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- Artificial Analysis 当前模型目录和 V5 Index 页面未找到 Mercury 3 对应模型行或分数；Inception 发布文正文未给出该项数值。发布文另含图像版 benchmark 图，当前无法从可读文本核对其内容。

最近核验时间：2026-11-04T02:21+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Inception Mercury 3 官方发布文](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

研究备注：
- Artificial Analysis 当前 GDPval-AA v2.1 榜单可读内容及 Inception 发布文正文中未找到 Mercury 3 的精确模型行或分数。没有将其他模型或近似名称成绩移用；发布文中的图像版 benchmark 图当前无法读取。

最近核验时间：2026-11-04T02:21+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 43.66
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/models/inception_mercury-3](https://www.vals.ai/models/inception_mercury-3)

已检查的主要资料：
- [Vals AI Mercury 3 模型页](https://www.vals.ai/models/inception_mercury-3)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals AI Mercury 3 模型页和 Vals Index 官方榜单报告 43.66% Accuracy，误差范围 ±1.23，排名 28/32；当前 Index 定义为 v2.2。±1.23 保留在此备注，因为模型数据字段没有误差范围字段。模型页的 high effort 和默认 API 设置注明可能因 benchmark 不同而变化，不能确认是该 Index 运行的精确条件，故未写入。Vals 页面更新日期不是评测日期。

最近核验时间：2026-11-04T02:21+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 模型目录",
          "url": "https://artificialanalysis.ai/models"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "Artificial Analysis 当前模型目录和 V5 Index 页面未找到 Mercury 3 对应模型行或分数；Inception 发布文正文未给出该项数值。发布文另含图像版 benchmark 图，当前无法从可读文本核对其内容。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库与方法",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Inception Mercury 3 API 文档",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Inception Mercury 3 FAQ",
          "url": "https://docs.inceptionlabs.ai/resources/faq"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "Mercury 3 支持 tool calling，故不能仅凭文本输入判为不适用。Zapier 官方榜单可见前十项及“See 119 more”，当前文本无法核验折叠列表中是否有 Mercury 3；官方发布文正文也没有可核实的 AutomationBench 分数。其 benchmark 图像未能从页面文本读取。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要核实 Zapier 官方榜单折叠项，或找到 Mercury 3 的原始 AutomationBench 评测结果及数据集条件。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测仓库与方法",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Inception Mercury 3 API 文档",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Inception Mercury 3 FAQ",
          "url": "https://docs.inceptionlabs.ai/resources/faq"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "Surge 官方榜单和方法仓库可读内容中未找到 Mercury 3 成绩。Mercury 3 原生只接受文本输入，不能直接处理标准图表图像；目前没有该模型使用 OCR/图表转写 wrapper 的来源。Inception 发布文另含无法从页面文本读取的图像版 benchmark 图。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "已检查 Datacurve 官方 v1.1 榜单与 Inception 发布文正文，未找到 Mercury 3 的可核实 DeepSWE 成绩。Datacurve 榜单最后可见更新为 2026-09-22，早于 Mercury 3 官方公开发布；Inception 发布文另含一张图像版 benchmark 图，当前可读文本无法识别图中项目和值，因此本结论仅限可读资料。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "Artificial Analysis 当前 GDPval-AA v2.1 榜单可读内容及 Inception 发布文正文中未找到 Mercury 3 的精确模型行或分数。没有将其他模型或近似名称成绩移用；发布文中的图像版 benchmark 图当前无法读取。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Scale AI Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam 页面",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "已检查 Scale 原始 HLE 榜单、Artificial Analysis HLE 页面及 Inception 发布文正文，未找到 Mercury 3 的原始 2,500 题 HLE 成绩；未用 Vals HLAB-Vals-1.1 或其他 HLE 子集替代。官方发布文图像版 benchmark 图当前无法读取。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Inception Mercury 3 API 文档",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Inception Mercury 3 FAQ",
          "url": "https://docs.inceptionlabs.ai/resources/faq"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "OSWorld 官方动态榜单的当前文本快照未显示可核验的 Mercury 3 行；Inception 文档确认模型原生文本输入并支持 tools，但外部 OCR/GUI wrapper 可能改变路径，不能据此直接判不适用。没有找到可核实分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态榜单内容未能读取；若存在 wrapper 结果，需确认精确版本、指标和运行配置。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 Full 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "已检查 Scale 官方 V2 Full 榜单和 Inception 发布文正文，未找到 Mercury 3 的可引用成绩。Scale 页面标注更新于 2026-09-22，早于模型官方公开发布；未使用估算站点分数。Inception 发布文另含当前无法读取的图像版 benchmark 图，因此本结论仅限可读资料。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Terminal-Bench Science 0.1 方法页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Vals AI Mercury 3 模型页",
          "url": "https://www.vals.ai/models/inception_mercury-3"
        },
        {
          "label": "Inception Mercury 3 官方发布文",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis 的 Terminal-Bench Science 0.1 方法页、Vals Mercury 3 模型页和 Inception 发布文正文，未找到 Mercury 3 对应分数。AA 可读页说明该 benchmark 的版本和方法，但动态结果区没有可读的该模型行；Inception 发布文另含当前无法读取的图像版 benchmark 图。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals AI Mercury 3 模型页",
          "url": "https://www.vals.ai/models/inception_mercury-3"
        },
        {
          "label": "Terminal-Bench 4.0 官方定义",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Vals AI 官方榜单列出 Mercury 3：3.03%，Mini-SWE-agent harness。方法页说明版本 4.0 的完整 66 项任务每模型运行三次，每次 pass@1，公布 avg@3 均值；本记录保留为该独立 Vals 执行配置。Vals 页面版本写 4.0，映射到本仓库定义的 4.0.0。页面的 2026-10-29 是更新日期，不是已确认的评测日期；模型页标注 high 也不能确认是本项运行档位，因此均未写入。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:21+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Mercury 3 模型页",
          "url": "https://www.vals.ai/models/inception_mercury-3"
        },
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals AI Mercury 3 模型页和 Vals Index 官方榜单报告 43.66% Accuracy，误差范围 ±1.23，排名 28/32；当前 Index 定义为 v2.2。±1.23 保留在此备注，因为模型数据字段没有误差范围字段。模型页的 high effort 和默认 API 设置注明可能因 benchmark 不同而变化，不能确认是该 Index 运行的精确条件，故未写入。Vals 页面更新日期不是评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:21+08:00",
  "model_id": "inception/mercury-3",
  "new_records": 2,
  "overall_status": "待复核"
}

-->
