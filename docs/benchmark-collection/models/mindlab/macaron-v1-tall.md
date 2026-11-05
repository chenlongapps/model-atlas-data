# Macaron V1 Tall Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mindlab/macaron-v1-tall
- 模型名称：Macaron V1 Tall
- 发布日期：2026-07-21
- 最近检查时间：2026-11-04T23:01+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方技术报告将 Macaron-V1-Tall 定义为基于 Qwen3.6-35B-A3B 的独立型号，并与基于 GLM-5.2 的 Macaron-V1-Venti 区分。本轮只归属 Tall 的结果。
- 技术报告 Tall 表格报告的项目不包括本次 11 项目标；不把 Venti、基座模型或未细分型号的分数移入 Tall。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T23:01+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:01+08:00 |
| terminal-bench-v4 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T23:01+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Terminal-Bench-Science 0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T23:01+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Macaron model documentation](https://mint-doc.macaron.xin/model-api/macaron-v1/), [Macaron-V1 technical report](https://arxiv.org/html/2608.09819) | 2026-11-04T23:01+08:00 |
| osworld-v2.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-04T23:01+08:00 |
| chartography | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T23:01+08:00 |
| humanitys-last-exam | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T23:01+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Artificial Analysis model overview](https://artificialanalysis.ai/models) | 2026-11-04T23:01+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T23:01+08:00 |
| vals-index-v2.2 | 待核实 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T23:01+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 技术报告中的 DeepSWE 58.4 属于 Macaron-V1-Venti，不是 Tall；报告未给它标注为本地定义的 v1.1。DeepSWE v1.1 现行榜单未列 Macaron。

最近核验时间：2026-11-04T23:01+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Tall 的技术报告列出 SWE-Verified，而不是 SWE-bench Pro V2；Scale 的 V2 榜单未见 Macaron-V1-Tall。没有将其他 SWE-bench 变体映射为 V2。

最近核验时间：2026-11-04T23:01+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Tall 的技术报告给出的是 TerminalBench 2.1 成绩 56.2，且说明其使用 Claude Code Agent Harness、四小时 timeout 和 pass@1；这不是 v4。Vals 当前 v4 榜单未见 Tall。

最近核验时间：2026-11-04T23:01+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Terminal-Bench-Science 0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 技术报告的 Tall 结果没有包含 Terminal-Bench-Science；官方 0.1 发布资料未提供 Macaron-V1-Tall 成绩。

最近核验时间：2026-11-04T23:01+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Macaron model documentation](https://mint-doc.macaron.xin/model-api/macaron-v1/)
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)

研究备注：
- 官方文档表格报告未细分型号的“Macaron-V1” AutomationBench 31.8；Tall 技术报告确认 Tall 与 Venti 是不同型号。文档提及公开任务集，而本地定义针对官方榜单私有留出集，因此未把该分数写入 Tall TOML。

尚未解决的问题：
- 官方文档的 Macaron-V1 31.8 是否对应 Tall，以及它是否与本地私有留出集定义等价，均未明确。

最近核验时间：2026-11-04T23:01+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Tall 技术报告没有列出 OSWorld；OSWorld v2.1 官方发布页未提供该型号成绩。没有使用其他 OSWorld 版本替代。

最近核验时间：2026-11-04T23:01+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 技术报告未报告 Tall 的 Chartography 成绩；Surge 当前榜单页面未见 Macaron-V1-Tall。

最近核验时间：2026-11-04T23:01+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 技术报告未报告 Tall 的 HLE 成绩；Artificial Analysis 评测页介绍了 2,500 题 HLE，但当前可见页面未列 Macaron-V1-Tall。

最近核验时间：2026-11-04T23:01+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Artificial Analysis model overview](https://artificialanalysis.ai/models)

研究备注：
- 未找到 Artificial Analysis 的 Macaron-V1-Tall 模型详情页或与 Index V5 对应的结果；当前模型总览页面未显示该型号。

最近核验时间：2026-11-04T23:01+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 技术报告未报告 Tall 的 GDPval-AA 成绩；Artificial Analysis v2.1 评测页当前可见内容未列 Macaron-V1-Tall。

最近核验时间：2026-11-04T23:01+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前页面标示 Index v2.2（2026-10-30），展示每个实验室最佳模型及最新、顶尖和前沿模型子集；未列 Tall，但页面范围并非完整历史成绩清单。

尚未解决的问题：
- 无法根据当前精选榜单确认 Macaron-V1-Tall 是否曾获得该版本成绩。

最近核验时间：2026-11-04T23:01+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Artificial Analysis model overview",
          "url": "https://artificialanalysis.ai/models"
        }
      ],
      "notes": [
        "未找到 Artificial Analysis 的 Macaron-V1-Tall 模型详情页或与 Index V5 对应的结果；当前模型总览页面未显示该型号。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron model documentation",
          "url": "https://mint-doc.macaron.xin/model-api/macaron-v1/"
        },
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        }
      ],
      "notes": [
        "官方文档表格报告未细分型号的“Macaron-V1” AutomationBench 31.8；Tall 技术报告确认 Tall 与 Venti 是不同型号。文档提及公开任务集，而本地定义针对官方榜单私有留出集，因此未把该分数写入 Tall TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方文档的 Macaron-V1 31.8 是否对应 Tall，以及它是否与本地私有留出集定义等价，均未明确。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "技术报告未报告 Tall 的 Chartography 成绩；Surge 当前榜单页面未见 Macaron-V1-Tall。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "技术报告中的 DeepSWE 58.4 属于 Macaron-V1-Venti，不是 Tall；报告未给它标注为本地定义的 v1.1。DeepSWE v1.1 现行榜单未列 Macaron。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "技术报告未报告 Tall 的 GDPval-AA 成绩；Artificial Analysis v2.1 评测页当前可见内容未列 Macaron-V1-Tall。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "技术报告未报告 Tall 的 HLE 成绩；Artificial Analysis 评测页介绍了 2,500 题 HLE，但当前可见页面未列 Macaron-V1-Tall。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Tall 技术报告没有列出 OSWorld；OSWorld v2.1 官方发布页未提供该型号成绩。没有使用其他 OSWorld 版本替代。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Tall 的技术报告列出 SWE-Verified，而不是 SWE-bench Pro V2；Scale 的 V2 榜单未见 Macaron-V1-Tall。没有将其他 SWE-bench 变体映射为 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Terminal-Bench-Science 0.1 release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "技术报告的 Tall 结果没有包含 Terminal-Bench-Science；官方 0.1 发布资料未提供 Macaron-V1-Tall 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Tall 的技术报告给出的是 TerminalBench 2.1 成绩 56.2，且说明其使用 Claude Code Agent Harness、四小时 timeout 和 pass@1；这不是 v4。Vals 当前 v4 榜单未见 Tall。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:01+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前页面标示 Index v2.2（2026-10-30），展示每个实验室最佳模型及最新、顶尖和前沿模型子集；未列 Tall，但页面范围并非完整历史成绩清单。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法根据当前精选榜单确认 Macaron-V1-Tall 是否曾获得该版本成绩。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:01+08:00",
  "model_id": "mindlab/macaron-v1-tall",
  "model_notes": [
    "官方技术报告将 Macaron-V1-Tall 定义为基于 Qwen3.6-35B-A3B 的独立型号，并与基于 GLM-5.2 的 Macaron-V1-Venti 区分。本轮只归属 Tall 的结果。",
    "技术报告 Tall 表格报告的项目不包括本次 11 项目标；不把 Venti、基座模型或未细分型号的分数移入 Tall。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
