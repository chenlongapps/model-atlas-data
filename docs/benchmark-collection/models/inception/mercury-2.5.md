# Mercury 2.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inception/mercury-2.5
- 模型名称：Mercury 2.5
- 发布日期：2026-09-08
- 最近检查时间：2026-11-04T12:23+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Mercury 2.5 release article](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5) | 2026-11-04T12:23+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Mercury 2.5 release article](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5) | 2026-11-04T12:23+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 official evaluation method](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4), [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5) | 2026-11-04T12:23+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official leaderboard](https://www.terminal-bench-science.ai/), [Terminal-Bench Science evaluation page](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5) | 2026-11-04T12:23+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Artificial Analysis AutomationBench-AA method](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis AutomationBench-AA evaluation](https://artificialanalysis.ai/evaluations/automationbench-aa/), [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5) | 2026-11-04T12:23+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [Inception model documentation](https://docs.inceptionlabs.ai/get-started/models) | 2026-11-04T12:23+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Inception model documentation](https://docs.inceptionlabs.ai/get-started/models) | 2026-11-04T12:23+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5), [Unverified HLE text-only aggregation](https://atlas.kevinhu.io/benchmarks/hle-text-only) | 2026-11-04T12:23+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Mercury 2.5 profile](https://artificialanalysis.ai/models/mercury-2-5), [Artificial Analysis Intelligence Index V5 evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T12:23+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Mercury 2.5 profile](https://artificialanalysis.ai/models/mercury-2-5), [Unverified third-party Mercury 2.5 aggregation](https://www.publicai.io/model-index/m/mercury-2-5) | 2026-11-04T12:23+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2 earlier version](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-04T12:23+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Mercury 2.5 release article](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)

研究备注：
- 官方榜单标注 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 Mercury 2.5；无法确定完整结果中是否存在精确条目。未找到可核实的成绩、指标及 harness。

尚未解决的问题：
- 官方榜单标注 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 Mercury 2.5；无法确定完整结果中是否存在精确条目。未找到可核实的成绩、指标及 harness。

最近核验时间：2026-11-04T12:23+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Mercury 2.5 release article](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)

研究备注：
- Scale AI V2 榜单当前公开结果中未见 Mercury 2.5，也未找到可归属该模型的准确分数与运行条件。Inception 发布页未报告此项成绩。

最近核验时间：2026-11-04T12:23+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 official evaluation method](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4)
- [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5)

研究备注：
- 官方榜单无法从页面文本读取模型行。Artificial Analysis 方法页说明该评测使用 66 项任务和 mini-swe-agent，但没有可核实的 Mercury 2.5 单项分数。

尚未解决的问题：
- 官方榜单无法从页面文本读取模型行。Artificial Analysis 方法页说明该评测使用 66 项任务和 mini-swe-agent，但没有可核实的 Mercury 2.5 单项分数。

最近核验时间：2026-11-04T12:23+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official leaderboard](https://www.terminal-bench-science.ai/)
- [Terminal-Bench Science evaluation page](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5)

研究备注：
- 官方榜单为动态页面，当前无法读取结果行；Artificial Analysis 页面未提供可确认的 Mercury 2.5 单项结果。

尚未解决的问题：
- 官方榜单为动态页面，当前无法读取结果行；Artificial Analysis 页面未提供可确认的 Mercury 2.5 单项结果。

最近核验时间：2026-11-04T12:23+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Artificial Analysis AutomationBench-AA method](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis AutomationBench-AA evaluation](https://artificialanalysis.ai/evaluations/automationbench-aa/)
- [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5)

研究备注：
- Zapier 官方榜单确认目标版本 1.0.6，但页面只显示前 10 项并注明另有 119 项。第三方列出的 2.4% 对应 Artificial Analysis AutomationBench-AA（私有 657 项、无 guardrail 违规时目标完成率），与本地定义的 Zapier task_completed_correctly 指标不同，不写入目标 Benchmark。

尚未解决的问题：
- Zapier 官方榜单确认目标版本 1.0.6，但页面只显示前 10 项并注明另有 119 项。第三方列出的 2.4% 对应 Artificial Analysis AutomationBench-AA（私有 657 项、无 guardrail 违规时目标完成率），与本地定义的 Zapier task_completed_correctly 指标不同，不写入目标 Benchmark。

最近核验时间：2026-11-04T12:23+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [Inception model documentation](https://docs.inceptionlabs.ai/get-started/models)

研究备注：
- OSWorld v2.1 以截图作观察并要求 GUI 操作；Mercury 2.5 官方模型表仅支持文本输入输出。没有可归属该独立模型的成绩。

最近核验时间：2026-11-04T12:23+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Inception model documentation](https://docs.inceptionlabs.ai/get-started/models)

研究备注：
- Chartography 需要理解图表图像；Mercury 2.5 官方模型表仅列文本输入输出，不适用于该图像 benchmark。

最近核验时间：2026-11-04T12:23+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Mercury 2.5 Artificial Analysis profile](https://artificialanalysis.ai/models/mercury-2-5)
- [Unverified HLE text-only aggregation](https://atlas.kevinhu.io/benchmarks/hle-text-only)

研究备注：
- 第三方页面列出 11.8%，但标注 HLE Text-Only，与本地目标定义的原始 2,500 题多模态集不一致。Artificial Analysis 的 Mercury 2.5 页面及 HLE 评测页未显示完整集对应成绩，未写入候选分数。

尚未解决的问题：
- 第三方页面列出 11.8%，但标注 HLE Text-Only，与本地目标定义的原始 2,500 题多模态集不一致。Artificial Analysis 的 Mercury 2.5 页面及 HLE 评测页未显示完整集对应成绩，未写入候选分数。

最近核验时间：2026-11-04T12:23+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Mercury 2.5 profile](https://artificialanalysis.ai/models/mercury-2-5)
- [Artificial Analysis Intelligence Index V5 evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis Mercury 2.5 profile 当前 Intelligence Index 为 N/A，V5 页面未列该模型。第三方 12.3 未能验证目标版本 V5，故无可记录成绩。

最近核验时间：2026-11-04T12:23+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Mercury 2.5 profile](https://artificialanalysis.ai/models/mercury-2-5)
- [Unverified third-party Mercury 2.5 aggregation](https://www.publicai.io/model-index/m/mercury-2-5)

研究备注：
- Artificial Analysis 官方结果页未显示可核实的 Mercury 2.5 行；第三方提及的 474 未能核实其分数含义与评测条件，因此不写入。

尚未解决的问题：
- Artificial Analysis 官方结果页未显示可核实的 Mercury 2.5 行；第三方提及的 474 未能核实其分数含义与评测条件，因此不写入。

最近核验时间：2026-11-04T12:23+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2 earlier version](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- 官方 v2.2 榜单未显示 Mercury 2.5。较早 Vals Index v2 榜单的 12.95% 不是目标 v2.2 版本，不能转录。

尚未解决的问题：
- 官方 v2.2 榜单未显示 Mercury 2.5。较早 Vals Index v2 榜单的 12.95% 不是目标 v2.2 版本，不能转录。

最近核验时间：2026-11-04T12:23+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Mercury 2.5 profile",
          "url": "https://artificialanalysis.ai/models/mercury-2-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis Mercury 2.5 profile 当前 Intelligence Index 为 N/A，V5 页面未列该模型。第三方 12.3 未能验证目标版本 V5，故无可记录成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA method",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/automationbench-aa/"
        },
        {
          "label": "Mercury 2.5 Artificial Analysis profile",
          "url": "https://artificialanalysis.ai/models/mercury-2-5"
        }
      ],
      "notes": [
        "Zapier 官方榜单确认目标版本 1.0.6，但页面只显示前 10 项并注明另有 119 项。第三方列出的 2.4% 对应 Artificial Analysis AutomationBench-AA（私有 657 项、无 guardrail 违规时目标完成率），与本地定义的 Zapier task_completed_correctly 指标不同，不写入目标 Benchmark。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 官方榜单确认目标版本 1.0.6，但页面只显示前 10 项并注明另有 119 项。第三方列出的 2.4% 对应 Artificial Analysis AutomationBench-AA（私有 657 项、无 guardrail 违规时目标完成率），与本地定义的 Zapier task_completed_correctly 指标不同，不写入目标 Benchmark。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Inception model documentation",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        }
      ],
      "notes": [
        "Chartography 需要理解图表图像；Mercury 2.5 官方模型表仅列文本输入输出，不适用于该图像 benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Mercury 2.5 release article",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-2-5"
        }
      ],
      "notes": [
        "官方榜单标注 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 Mercury 2.5；无法确定完整结果中是否存在精确条目。未找到可核实的成绩、指标及 harness。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单标注 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 Mercury 2.5；无法确定完整结果中是否存在精确条目。未找到可核实的成绩、指标及 harness。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Mercury 2.5 profile",
          "url": "https://artificialanalysis.ai/models/mercury-2-5"
        },
        {
          "label": "Unverified third-party Mercury 2.5 aggregation",
          "url": "https://www.publicai.io/model-index/m/mercury-2-5"
        }
      ],
      "notes": [
        "Artificial Analysis 官方结果页未显示可核实的 Mercury 2.5 行；第三方提及的 474 未能核实其分数含义与评测条件，因此不写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "Artificial Analysis 官方结果页未显示可核实的 Mercury 2.5 行；第三方提及的 474 未能核实其分数含义与评测条件，因此不写入。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Mercury 2.5 Artificial Analysis profile",
          "url": "https://artificialanalysis.ai/models/mercury-2-5"
        },
        {
          "label": "Unverified HLE text-only aggregation",
          "url": "https://atlas.kevinhu.io/benchmarks/hle-text-only"
        }
      ],
      "notes": [
        "第三方页面列出 11.8%，但标注 HLE Text-Only，与本地目标定义的原始 2,500 题多模态集不一致。Artificial Analysis 的 Mercury 2.5 页面及 HLE 评测页未显示完整集对应成绩，未写入候选分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "第三方页面列出 11.8%，但标注 HLE Text-Only，与本地目标定义的原始 2,500 题多模态集不一致。Artificial Analysis 的 Mercury 2.5 页面及 HLE 评测页未显示完整集对应成绩，未写入候选分数。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "Inception model documentation",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        }
      ],
      "notes": [
        "OSWorld v2.1 以截图作观察并要求 GUI 操作；Mercury 2.5 官方模型表仅支持文本输入输出。没有可归属该独立模型的成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Mercury 2.5 release article",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-2-5"
        }
      ],
      "notes": [
        "Scale AI V2 榜单当前公开结果中未见 Mercury 2.5，也未找到可归属该模型的准确分数与运行条件。Inception 发布页未报告此项成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science official leaderboard",
          "url": "https://www.terminal-bench-science.ai/"
        },
        {
          "label": "Terminal-Bench Science evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Mercury 2.5 Artificial Analysis profile",
          "url": "https://artificialanalysis.ai/models/mercury-2-5"
        }
      ],
      "notes": [
        "官方榜单为动态页面，当前无法读取结果行；Artificial Analysis 页面未提供可确认的 Mercury 2.5 单项结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单为动态页面，当前无法读取结果行；Artificial Analysis 页面未提供可确认的 Mercury 2.5 单项结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 official evaluation method",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Mercury 2.5 Artificial Analysis profile",
          "url": "https://artificialanalysis.ai/models/mercury-2-5"
        }
      ],
      "notes": [
        "官方榜单无法从页面文本读取模型行。Artificial Analysis 方法页说明该评测使用 66 项任务和 mini-swe-agent，但没有可核实的 Mercury 2.5 单项分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单无法从页面文本读取模型行。Artificial Analysis 方法页说明该评测使用 66 项任务和 mini-swe-agent，但没有可核实的 Mercury 2.5 单项分数。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T12:23+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2 earlier version",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "官方 v2.2 榜单未显示 Mercury 2.5。较早 Vals Index v2 榜单的 12.95% 不是目标 v2.2 版本，不能转录。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 v2.2 榜单未显示 Mercury 2.5。较早 Vals Index v2 榜单的 12.95% 不是目标 v2.2 版本，不能转录。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T12:23+08:00",
  "model_id": "inception/mercury-2.5",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
