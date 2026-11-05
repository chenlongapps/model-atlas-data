# Qwen3.6 Max Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.6-max-preview
- 模型名称：Qwen3.6 Max Preview
- 发布日期：2026-04-20
- 最近检查时间：2026-11-05T08:46+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方文章日期为 2026-04-18，而本地 release_date 为 2026-04-20；日期口径不同，本轮未擅自改动模型发布日期。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T08:35+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:35+08:00 |
| terminal-bench-v4 | 待核实 | — | [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview), [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:35+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview), [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:35+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Alibaba Cloud exact-model documentation](https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max), [AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench project](https://github.com/zapier/AutomationBench) | 2026-11-05T08:35+08:00 |
| osworld-v2.1 | 不适用 | — | [Alibaba Cloud exact-model documentation](https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max), [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/) | 2026-11-05T08:35+08:00 |
| chartography | 不适用 | — | [Alibaba Cloud exact-model documentation](https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max), [Chartography benchmark](https://surgehq.ai/benchmarks/chartography), [Chartography project](https://github.com/surge-ai/chartography) | 2026-11-05T08:35+08:00 |
| humanitys-last-exam | 待核实 | — | [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview), [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact-model profile (current Intelligence Index V5.0.1 section)](https://artificialanalysis.ai/models/qwen3-6-max), [Artificial Analysis older comparison (Index v4.1.1 / GDPval-AA v2)](https://artificialanalysis.ai/models/comparisons/qwen3-6-max-vs-qwen3-max), [Artificial Analysis Intelligence Index definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T08:46+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis older comparison (GDPval-AA v2)](https://artificialanalysis.ai/models/comparisons/qwen3-6-max-vs-qwen3-max), [GDPval-AA V2.1 definition](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T08:35+08:00 |
| vals-index-v2.2 | 待核实 | — | [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview), [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T08:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 检查了官方发布文和 DeepSWE 当前榜单，但未能从可见资料确认该型号的 DeepSWE v1.1 精确成绩。榜单公开视图只显示部分模型，不能将缺席视作未找到。

尚未解决的问题：
- 检查了官方发布文和 DeepSWE 当前榜单，但未能从可见资料确认该型号的 DeepSWE v1.1 精确成绩。榜单公开视图只显示部分模型，不能将缺席视作未找到。

最近核验时间：2026-11-05T08:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Qwen 发布文提及 SWE-bench Pro，但未标 V2；该发布文早于 2026-09-22 的 Pro V2 刷新版。目标版本与分数尚不能确认。

尚未解决的问题：
- Qwen 发布文提及 SWE-bench Pro，但未标 V2；该发布文早于 2026-09-22 的 Pro V2 刷新版。目标版本与分数尚不能确认。

最近核验时间：2026-11-05T08:35+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview)
- [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Qwen 发布文提及 Terminal-Bench 2.0 与相对提升，没有目标绝对分数；版本 2.0 不能映射为 4.0。

尚未解决的问题：
- Qwen 发布文提及 Terminal-Bench 2.0 与相对提升，没有目标绝对分数；版本 2.0 不能映射为 4.0。

最近核验时间：2026-11-05T08:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview)
- [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- 已检查官方发布资料和 Terminal-Bench Science 基准页，未核实该精确型号的 v0.1 成绩；动态页面未列出不构成未找到。

尚未解决的问题：
- 已检查官方发布资料和 Terminal-Bench Science 基准页，未核实该精确型号的 v0.1 成绩；动态页面未列出不构成未找到。

最近核验时间：2026-11-05T08:35+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Alibaba Cloud exact-model documentation](https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max)
- [AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench project](https://github.com/zapier/AutomationBench)

研究备注：
- 精确型号文档确认支持 function calling，任务类型适用；未确认该模型的 AutomationBench 1.0.6 成绩。榜单只展示部分条目，缺席不能判未找到。

尚未解决的问题：
- 精确型号文档确认支持 function calling，任务类型适用；未确认该模型的 AutomationBench 1.0.6 成绩。榜单只展示部分条目，缺席不能判未找到。

最近核验时间：2026-11-05T08:35+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud exact-model documentation](https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max)
- [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/)

研究备注：
- 阿里云精确型号文档说明该 Preview 仅支持文本输入/输出；OSWorld 桌面任务需要观察屏幕图像，不能以纯文本接口完成标准任务。

最近核验时间：2026-11-05T08:35+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Cloud exact-model documentation](https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max)
- [Chartography benchmark](https://surgehq.ai/benchmarks/chartography)
- [Chartography project](https://github.com/surge-ai/chartography)

研究备注：
- 阿里云精确型号文档说明该 Preview 不接收图像；Chartography 任务要求解读图表图像。

最近核验时间：2026-11-05T08:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview)
- [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 官方发布页正文没有列出可读的 HLE 目标成绩；成绩图在文本视图中不可读取，未从不可读图像推定数值。

尚未解决的问题：
- 官方发布页正文没有列出可读的 HLE 目标成绩；成绩图在文本视图中不可读取，未从不可读图像推定数值。

最近核验时间：2026-11-05T08:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact-model profile (current Intelligence Index V5.0.1 section)](https://artificialanalysis.ai/models/qwen3-6-max)
- [Artificial Analysis older comparison (Index v4.1.1 / GDPval-AA v2)](https://artificialanalysis.ai/models/comparisons/qwen3-6-max-vs-qwen3-max)
- [Artificial Analysis Intelligence Index definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA 精确型号页当前将 Artificial Analysis Intelligence Index 显示为 N/A，并在同页说明当前索引为 V5.0.1。旧比较页的 Index 为 v4.1.1，不能映射；截至本次检查未找到该型号公开的 V5 分数。

最近核验时间：2026-11-05T08:46+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis older comparison (GDPval-AA v2)](https://artificialanalysis.ai/models/comparisons/qwen3-6-max-vs-qwen3-max)
- [GDPval-AA V2.1 definition](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 旧 AA 比较页列的是 GDPval-AA v2，不是 v2.1；当前官方页面可见内容不足以确认该型号的 v2.1 分数。

尚未解决的问题：
- 旧 AA 比较页列的是 GDPval-AA v2，不是 v2.1；当前官方页面可见内容不足以确认该型号的 v2.1 分数。

最近核验时间：2026-11-05T08:35+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6 Max Preview official release post](https://qwen.ai/blog?id=qwen3.6-max-preview)
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前 V2.2 榜单显示最新、top 和 frontier 模型；未显示该型号不能据此断言未找到。

尚未解决的问题：
- Vals 当前 V2.2 榜单显示最新、top 和 frontier 模型；未显示该型号不能据此断言未找到。

最近核验时间：2026-11-05T08:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model profile (current Intelligence Index V5.0.1 section)",
          "url": "https://artificialanalysis.ai/models/qwen3-6-max"
        },
        {
          "label": "Artificial Analysis older comparison (Index v4.1.1 / GDPval-AA v2)",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-6-max-vs-qwen3-max"
        },
        {
          "label": "Artificial Analysis Intelligence Index definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA 精确型号页当前将 Artificial Analysis Intelligence Index 显示为 N/A，并在同页说明当前索引为 V5.0.1。旧比较页的 Index 为 v4.1.1，不能映射；截至本次检查未找到该型号公开的 V5 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud exact-model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max"
        },
        {
          "label": "AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench project",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "精确型号文档确认支持 function calling，任务类型适用；未确认该模型的 AutomationBench 1.0.6 成绩。榜单只展示部分条目，缺席不能判未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "精确型号文档确认支持 function calling，任务类型适用；未确认该模型的 AutomationBench 1.0.6 成绩。榜单只展示部分条目，缺席不能判未找到。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud exact-model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max"
        },
        {
          "label": "Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography project",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "阿里云精确型号文档说明该 Preview 不接收图像；Chartography 任务要求解读图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6 Max Preview official release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-max-preview"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "检查了官方发布文和 DeepSWE 当前榜单，但未能从可见资料确认该型号的 DeepSWE v1.1 精确成绩。榜单公开视图只显示部分模型，不能将缺席视作未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "检查了官方发布文和 DeepSWE 当前榜单，但未能从可见资料确认该型号的 DeepSWE v1.1 精确成绩。榜单公开视图只显示部分模型，不能将缺席视作未找到。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis older comparison (GDPval-AA v2)",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-6-max-vs-qwen3-max"
        },
        {
          "label": "GDPval-AA V2.1 definition",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "旧 AA 比较页列的是 GDPval-AA v2，不是 v2.1；当前官方页面可见内容不足以确认该型号的 v2.1 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "旧 AA 比较页列的是 GDPval-AA v2，不是 v2.1；当前官方页面可见内容不足以确认该型号的 v2.1 分数。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6 Max Preview official release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-max-preview"
        },
        {
          "label": "Humanity's Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "官方发布页正文没有列出可读的 HLE 目标成绩；成绩图在文本视图中不可读取，未从不可读图像推定数值。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方发布页正文没有列出可读的 HLE 目标成绩；成绩图在文本视图中不可读取，未从不可读图像推定数值。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Cloud exact-model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/zh/model-studio/qwen3-6-max"
        },
        {
          "label": "OSWorld V2.1 benchmark",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "阿里云精确型号文档说明该 Preview 仅支持文本输入/输出；OSWorld 桌面任务需要观察屏幕图像，不能以纯文本接口完成标准任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6 Max Preview official release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-max-preview"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Qwen 发布文提及 SWE-bench Pro，但未标 V2；该发布文早于 2026-09-22 的 Pro V2 刷新版。目标版本与分数尚不能确认。"
      ],
      "status": "待核实",
      "unresolved": [
        "Qwen 发布文提及 SWE-bench Pro，但未标 V2；该发布文早于 2026-09-22 的 Pro V2 刷新版。目标版本与分数尚不能确认。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6 Max Preview official release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-max-preview"
        },
        {
          "label": "Terminal-Bench Science benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "已检查官方发布资料和 Terminal-Bench Science 基准页，未核实该精确型号的 v0.1 成绩；动态页面未列出不构成未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "已检查官方发布资料和 Terminal-Bench Science 基准页，未核实该精确型号的 v0.1 成绩；动态页面未列出不构成未找到。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6 Max Preview official release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-max-preview"
        },
        {
          "label": "Terminal-Bench 4.0 benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Qwen 发布文提及 Terminal-Bench 2.0 与相对提升，没有目标绝对分数；版本 2.0 不能映射为 4.0。"
      ],
      "status": "待核实",
      "unresolved": [
        "Qwen 发布文提及 Terminal-Bench 2.0 与相对提升，没有目标绝对分数；版本 2.0 不能映射为 4.0。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:35+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6 Max Preview official release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-max-preview"
        },
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前 V2.2 榜单显示最新、top 和 frontier 模型；未显示该型号不能据此断言未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "Vals 当前 V2.2 榜单显示最新、top 和 frontier 模型；未显示该型号不能据此断言未找到。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:46+08:00",
  "model_id": "alibaba/qwen3.6-max-preview",
  "model_notes": [
    "官方文章日期为 2026-04-18，而本地 release_date 为 2026-04-20；日期口径不同，本轮未擅自改动模型发布日期。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
