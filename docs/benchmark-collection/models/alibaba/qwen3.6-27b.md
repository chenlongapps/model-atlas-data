# Qwen3.6 27B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.6-27b
- 模型名称：Qwen3.6 27B
- 发布日期：2026-04-22
- 最近检查时间：2026-11-05T07:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- Alibaba 官方 Model Studio 资料确认 qwen3.6-27b 于 2026-04-22 发布；Qwen 模型卡对应 Qwen/Qwen3.6-27B，支持文本、图像、视频输入与文本输出，并提供工具调用配置。已有 SWE-Bench Verified 77.2 原始行保留；它不属于本轮 11 项成绩。
- 新增两条目标成绩：HLE 24.0 与 GDPval-AA v2.1 969 Elo。GDPval-AA 的非推理模式作为 variant 单独记录；没有用榜单的模型发布日期填 Benchmark date。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T07:53+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Scale SWE-Bench Pro V2 官方榜单与方法](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T07:53+08:00 |
| terminal-bench-v4 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Vals Terminal-Bench 4 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T07:53+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Vals Terminal-Bench Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science), [Terminal-Bench Science v0.1.0 发布说明](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) | 2026-11-05T07:53+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Zapier AutomationBench 1.0.6 官方榜单](https://zapier.com/benchmarks) | 2026-11-05T07:53+08:00 |
| osworld-v2.1 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [OSWorld 官方榜单](https://osworld-v2.xlang.ai/), [OSWorld V2.1 发布说明](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T07:53+08:00 |
| chartography | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测仓库](https://github.com/surge-ai/chartography) | 2026-11-05T07:53+08:00 |
| humanitys-last-exam | 已收录 | 24.0 (metric=accuracy) | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Humanity's Last Exam 官方主页与定量结果](https://lastexam.ai/) | 2026-11-05T07:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.6 27B 型号页](https://artificialanalysis.ai/models/qwen3-6-27b/), [Artificial Analysis Intelligence Index V5.0.1 方法页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T07:53+08:00 |
| gdpval-aa-v2.1 | 已收录 | 969 (metric=Elo rating; version=2.1; dataset=220 tasks; variant=Non-reasoning; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T07:53+08:00 |
| vals-index-v2.2 | 待核实 | — | [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B), [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T07:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Qwen 官方模型卡没有目标项成绩；DeepSWE 当前视图标示 21/28 个模型，未见精确 Qwen3.6-27B 行。动态榜单不完整，不能据缺席判为未找到。

尚未解决的问题：
- 未确认该精确模型是否在完整榜单的其他配置或折叠项中有结果。

最近核验时间：2026-11-05T07:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Scale SWE-Bench Pro V2 官方榜单与方法](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Qwen 官方模型卡报告 SWE-bench Pro 53.5，但未标为 V2，且注明对公共任务集有修订；不映射为本地 2.0.0/642-task V2。Scale V2 当前榜单未见精确型号，页面视图不能证明完整。

尚未解决的问题：
- 没有确认 Qwen 53.5 对应的任务集是否为 V2 默认 642 项，故不写入目标成绩。

最近核验时间：2026-11-05T07:53+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Vals Terminal-Bench 4 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Qwen 官方模型卡的 59.3 标为 Terminal-Bench 2.0，使用 Harbor/Terminus-2、3 小时超时并取 5 次运行平均；这不是 4.0。Vals 当前显示 latest/top/frontier 子集且未见精确型号。

尚未解决的问题：
- 未确认完整 Terminal-Bench 4 榜单中是否存在精确型号结果。

最近核验时间：2026-11-05T07:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Vals Terminal-Bench Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Terminal-Bench Science v0.1.0 发布说明](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)

研究备注：
- 未找到 Qwen3.6-27B 的精确 v0.1.0 成绩；Vals 当前榜单只展示部分模型，缺席不足以判为未找到。

尚未解决的问题：
- 未确认完整榜单中是否存在精确型号结果。

最近核验时间：2026-11-05T07:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Zapier AutomationBench 1.0.6 官方榜单](https://zapier.com/benchmarks)

研究备注：
- 模型支持工具调用，任务适用；Zapier 榜单显示 10 条，另有 119 条结果折叠，无法确认精确型号是否在未展开项中。未将其他 AutomationBench 版本成绩迁入。

尚未解决的问题：
- 当前可见榜单不完整，未能确认精确型号的 1.0.6 成绩。

最近核验时间：2026-11-05T07:53+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [OSWorld 官方榜单](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 发布说明](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Qwen 支持视觉输入和工具调用；当前官方页面展示 OSWorld 2.0，未核实到 2.1 精确结果。没有把其他 OSWorld 版本或 OSWorld-Verified 分数映射到 v2.1。

尚未解决的问题：
- 未找到可确认的 OSWorld v2.1 精确结果；当前官方榜单标为 2.0。

最近核验时间：2026-11-05T07:53+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测仓库](https://github.com/surge-ai/chartography)

研究备注：
- 模型支持图像输入并输出文本，适用于图表问答；当前 Surge 榜单未见精确 Qwen3.6-27B 行，但页面为动态公开视图，不能据此判为未找到。

尚未解决的问题：
- 未确认动态榜单中是否有未显示的精确型号结果。

最近核验时间：2026-11-05T07:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 24.0
- metric: accuracy
- source: [https://huggingface.co/Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Humanity's Last Exam 官方主页与定量结果](https://lastexam.ai/)

研究备注：
- Qwen 官方模型卡列 HLE 24.0。HLE 官方资料将标准 HLE 定义为 2,500 题并以 accuracy (%) 报分；模型卡发布时间早于 HLE-Diamond 发布，故按标准 HLE 原始项目记录。来源没有说明具体评测日期或其他测试条件，这些字段不填写。

最近核验时间：2026-11-05T07:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.6 27B 型号页](https://artificialanalysis.ai/models/qwen3-6-27b/)
- [Artificial Analysis Intelligence Index V5.0.1 方法页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 当前 AA 型号页指向 Index V5.0.1，但综合值为 N/A/Unknown；旧页面中的 22 分属于 Index V4.3，不符合 V5 定义。

最近核验时间：2026-11-05T07:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 969
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- variant: Non-reasoning
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA v2.1 榜单精确列出 Qwen3.6 27B (Non-reasoning)：969 Elo，CI −21/+21。方法页说明该版本使用 220 项任务、经 Stirrup agentic harness 提供 shell 和网页浏览。榜单中的 Apr 2026 是模型发布日期月份，不是评测日期，因此未填 date。

最近核验时间：2026-11-05T07:53+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方 Qwen3.6-27B 模型卡](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 Vals Index v2.2 页只展示部分 latest/top/frontier 模型，未见 Qwen3.6-27B；缺席不足以证明没有成绩。旧版 Vals Index 结果不迁入 v2.2。

尚未解决的问题：
- 没有确认的 v2.2 精确结果；需完整榜单或原始评测报告核实。

最近核验时间：2026-11-05T07:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.6 27B 型号页",
          "url": "https://artificialanalysis.ai/models/qwen3-6-27b/"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0.1 方法页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "当前 AA 型号页指向 Index V5.0.1，但综合值为 N/A/Unknown；旧页面中的 22 分属于 Index V4.3，不符合 V5 定义。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Zapier AutomationBench 1.0.6 官方榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "模型支持工具调用，任务适用；Zapier 榜单显示 10 条，另有 119 条结果折叠，无法确认精确型号是否在未展开项中。未将其他 AutomationBench 版本成绩迁入。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前可见榜单不完整，未能确认精确型号的 1.0.6 成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "模型支持图像输入并输出文本，适用于图表问答；当前 Surge 榜单未见精确 Qwen3.6-27B 行，但页面为动态公开视图，不能据此判为未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认动态榜单中是否有未显示的精确型号结果。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 方法说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Qwen 官方模型卡没有目标项成绩；DeepSWE 当前视图标示 21/28 个模型，未见精确 Qwen3.6-27B 行。动态榜单不完整，不能据缺席判为未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认该精确模型是否在完整榜单的其他配置或折叠项中有结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA v2.1 榜单精确列出 Qwen3.6 27B (Non-reasoning)：969 Elo，CI −21/+21。方法页说明该版本使用 220 项任务、经 Stirrup agentic harness 提供 shell 和网页浏览。榜单中的 Apr 2026 是模型发布日期月份，不是评测日期，因此未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Humanity's Last Exam 官方主页与定量结果",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "Qwen 官方模型卡列 HLE 24.0。HLE 官方资料将标准 HLE 定义为 2,500 题并以 accuracy (%) 报分；模型卡发布时间早于 HLE-Diamond 发布，故按标准 HLE 原始项目记录。来源没有说明具体评测日期或其他测试条件，这些字段不填写。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "OSWorld 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 发布说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Qwen 支持视觉输入和工具调用；当前官方页面展示 OSWorld 2.0，未核实到 2.1 精确结果。没有把其他 OSWorld 版本或 OSWorld-Verified 分数映射到 v2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到可确认的 OSWorld v2.1 精确结果；当前官方榜单标为 2.0。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Scale SWE-Bench Pro V2 官方榜单与方法",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Qwen 官方模型卡报告 SWE-bench Pro 53.5，但未标为 V2，且注明对公共任务集有修订；不映射为本地 2.0.0/642-task V2。Scale V2 当前榜单未见精确型号，页面视图不能证明完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有确认 Qwen 53.5 对应的任务集是否为 V2 默认 642 项，故不写入目标成绩。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Vals Terminal-Bench Science 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench Science v0.1.0 发布说明",
          "url": "https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0"
        }
      ],
      "notes": [
        "未找到 Qwen3.6-27B 的精确 v0.1.0 成绩；Vals 当前榜单只展示部分模型，缺席不足以判为未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认完整榜单中是否存在精确型号结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Vals Terminal-Bench 4 官方榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Qwen 官方模型卡的 59.3 标为 Terminal-Bench 2.0，使用 Harbor/Terminus-2、3 小时超时并取 5 次运行平均；这不是 4.0。Vals 当前显示 latest/top/frontier 子集且未见精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认完整 Terminal-Bench 4 榜单中是否存在精确型号结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:53+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方 Qwen3.6-27B 模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.6-27B"
        },
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 Vals Index v2.2 页只展示部分 latest/top/frontier 模型，未见 Qwen3.6-27B；缺席不足以证明没有成绩。旧版 Vals Index 结果不迁入 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有确认的 v2.2 精确结果；需完整榜单或原始评测报告核实。"
      ]
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:53+08:00",
  "model_id": "alibaba/qwen3.6-27b",
  "model_notes": [
    "Alibaba 官方 Model Studio 资料确认 qwen3.6-27b 于 2026-04-22 发布；Qwen 模型卡对应 Qwen/Qwen3.6-27B，支持文本、图像、视频输入与文本输出，并提供工具调用配置。已有 SWE-Bench Verified 77.2 原始行保留；它不属于本轮 11 项成绩。",
    "新增两条目标成绩：HLE 24.0 与 GDPval-AA v2.1 969 Elo。GDPval-AA 的非推理模式作为 variant 单独记录；没有用榜单的模型发布日期填 Benchmark date。"
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
