# Laguna M.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：poolside/laguna-m.1
- 模型名称：Laguna M.1
- 发布日期：2026-04-28
- 最近检查时间：2026-11-05T07:03+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Poolside 官方发布页确认 Laguna M.1 于 2026-04-28 发布。官方技术报告列有 SWE-Bench Pro 52.6 和 Terminal-Bench 2.0 41.0；5 月更新又列 Terminal-Bench 2.0 45.8。它们不属于本任务的 Pro V2/TBench 4，未迁移。
- 官方模型卡确认本模型为文本输入/输出；Chartography 需要图表图像理解，故不适用。OSWorld 支持 a11y-tree，故未因无图像输入标为不适用。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE official leaderboard](https://deepswe.datacurve.ai/), [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf) | 2026-11-05T07:03+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf) | 2026-11-05T07:03+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 official page](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf), [Poolside Laguna long-context update](https://poolside.ai/blog/long-context-update-laguna-xs-2-and-m-1) | 2026-11-05T07:03+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science 0.1 official page](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf) | 2026-11-05T07:03+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [Poolside Laguna M.1 model card](https://huggingface.co/poolside/Laguna-M.1) | 2026-11-05T07:03+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2.1 official release materials](https://github.com/xlang-ai/OSWorld-V2/releases), [Poolside Laguna M.1 model card](https://huggingface.co/poolside/Laguna-M.1) | 2026-11-05T07:03+08:00 |
| chartography | 不适用 | — | [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography), [Poolside Laguna M.1 model card](https://huggingface.co/poolside/Laguna-M.1) | 2026-11-05T07:03+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis HLE page](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf) | 2026-11-05T07:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Index V5 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf) | 2026-11-05T07:03+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [GDPval-AA v2.1 official leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf) | 2026-11-05T07:03+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index), [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1) | 2026-11-05T07:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)
- [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)

研究备注：
- DeepSWE 仅展示 21/28 models、57/70 configs；Poolside 官方报告未列该目标项。

尚未解决的问题：
- 需检查未显示的 DeepSWE 配置是否包括此精确模型。

最近核验时间：2026-11-05T07:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)

研究备注：
- Poolside 报告给 SWE-Bench Pro（M.1 52.6、XS.2 46.3），未标 V2；当前可见 Scale V2 榜无精确型号，旧版分数不映射。

尚未解决的问题：
- 需核验完整 V2 榜及版本。

最近核验时间：2026-11-05T07:03+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 official page](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)
- [Poolside Laguna long-context update](https://poolside.ai/blog/long-context-update-laguna-xs-2-and-m-1)

研究备注：
- Poolside 发布报告列 Terminal-Bench 2.0（M.1 41.0、XS.2 35.7）；M.1 后续 TB 2.0 更新为 45.8。这些均非 v4；AA 当前只显示 28/240 models。

尚未解决的问题：
- 需核验完整 AA v4 榜单。

最近核验时间：2026-11-05T07:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official page](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)

研究备注：
- Poolside 报告未列 Terminal-Bench Science；AA 当前只显示 28/120 models。

尚未解决的问题：
- 需检查完整榜单。

最近核验时间：2026-11-05T07:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Poolside Laguna M.1 model card](https://huggingface.co/poolside/Laguna-M.1)

研究备注：
- Zapier 当前公开前 10 条并折叠另 119 条，不能据可见内容确认精确型号。

尚未解决的问题：
- 需核查折叠榜单。

最近核验时间：2026-11-05T07:03+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 official release materials](https://github.com/xlang-ai/OSWorld-V2/releases)
- [Poolside Laguna M.1 model card](https://huggingface.co/poolside/Laguna-M.1)

研究备注：
- OSWorld V2 是动态榜单，当前可读内容无法确认精确型号。Poolside 模型为文本输入，但 OSWorld 可用 a11y-tree 配置，故仍可能适用。

尚未解决的问题：
- 需核实完整行和评测配置。

最近核验时间：2026-11-05T07:03+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography)
- [Poolside Laguna M.1 model card](https://huggingface.co/poolside/Laguna-M.1)

研究备注：
- Poolside M.1/XS.2 仅支持文本输入/输出；Chartography 依赖图表图像的视觉理解。

最近核验时间：2026-11-05T07:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis HLE page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)

研究备注：
- Poolside 报告未列 HLE；AA HLE 页面只展示 677 个模型中的 27 个，榜单缺席不足以认定未测。

尚未解决的问题：
- 需查完整榜单或其他精确来源。

最近核验时间：2026-11-05T07:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Index V5 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)

研究备注：
- AA Index 当前只公开展示部分模型，未找到精确型号行；HLE-Diamond 是另一评测，不能替代 Index/HLE 分数。

尚未解决的问题：
- 需核验完整 v5.0.1 指数数据。

最近核验时间：2026-11-05T07:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [GDPval-AA v2.1 official leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Poolside Laguna M.1 / XS.2 technical report](https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf)

研究备注：
- AA GDPval 页面只公开展示 308 个模型中的 27 个，未见精确型号。

尚未解决的问题：
- 需核验完整榜单。

最近核验时间：2026-11-05T07:03+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)
- [Poolside Laguna M.1 / XS.2 release post](https://poolside.ai/blog/introducing-laguna-xs2-m1)

研究备注：
- Vals 页面当前只展示 latest/top/frontier 子集，不能据此判断完整数据是否有精确结果。

尚未解决的问题：
- 需检查完整 v2.2 榜单。

最近核验时间：2026-11-05T07:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Index V5 page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        }
      ],
      "notes": [
        "AA Index 当前只公开展示部分模型，未找到精确型号行；HLE-Diamond 是另一评测，不能替代 Index/HLE 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整 v5.0.1 指数数据。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Poolside Laguna M.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-M.1"
        }
      ],
      "notes": [
        "Zapier 当前公开前 10 条并折叠另 119 条，不能据可见内容确认精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查折叠榜单。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Chartography official benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Poolside Laguna M.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-M.1"
        }
      ],
      "notes": [
        "Poolside M.1/XS.2 仅支持文本输入/输出；Chartography 依赖图表图像的视觉理解。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 release post",
          "url": "https://poolside.ai/blog/introducing-laguna-xs2-m1"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        }
      ],
      "notes": [
        "DeepSWE 仅展示 21/28 models、57/70 configs；Poolside 官方报告未列该目标项。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查未显示的 DeepSWE 配置是否包括此精确模型。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 official leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        }
      ],
      "notes": [
        "AA GDPval 页面只公开展示 308 个模型中的 27 个，未见精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整榜单。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        }
      ],
      "notes": [
        "Poolside 报告未列 HLE；AA HLE 页面只展示 677 个模型中的 27 个，榜单缺席不足以认定未测。"
      ],
      "status": "待核实",
      "unresolved": [
        "需查完整榜单或其他精确来源。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 official release materials",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        },
        {
          "label": "Poolside Laguna M.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-M.1"
        }
      ],
      "notes": [
        "OSWorld V2 是动态榜单，当前可读内容无法确认精确型号。Poolside 模型为文本输入，但 OSWorld 可用 a11y-tree 配置，故仍可能适用。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实完整行和评测配置。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 release post",
          "url": "https://poolside.ai/blog/introducing-laguna-xs2-m1"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        }
      ],
      "notes": [
        "Poolside 报告给 SWE-Bench Pro（M.1 52.6、XS.2 46.3），未标 V2；当前可见 Scale V2 榜无精确型号，旧版分数不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整 V2 榜及版本。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official page",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        }
      ],
      "notes": [
        "Poolside 报告未列 Terminal-Bench Science；AA 当前只显示 28/120 models。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official page",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 release post",
          "url": "https://poolside.ai/blog/introducing-laguna-xs2-m1"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 technical report",
          "url": "https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf"
        },
        {
          "label": "Poolside Laguna long-context update",
          "url": "https://poolside.ai/blog/long-context-update-laguna-xs-2-and-m-1"
        }
      ],
      "notes": [
        "Poolside 发布报告列 Terminal-Bench 2.0（M.1 41.0、XS.2 35.7）；M.1 后续 TB 2.0 更新为 45.8。这些均非 v4；AA 当前只显示 28/240 models。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整 AA v4 榜单。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Poolside Laguna M.1 / XS.2 release post",
          "url": "https://poolside.ai/blog/introducing-laguna-xs2-m1"
        }
      ],
      "notes": [
        "Vals 页面当前只展示 latest/top/frontier 子集，不能据此判断完整数据是否有精确结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整 v2.2 榜单。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:03+08:00",
  "model_id": "poolside/laguna-m.1",
  "model_notes": [
    "Poolside 官方发布页确认 Laguna M.1 于 2026-04-28 发布。官方技术报告列有 SWE-Bench Pro 52.6 和 Terminal-Bench 2.0 41.0；5 月更新又列 Terminal-Bench 2.0 45.8。它们不属于本任务的 Pro V2/TBench 4，未迁移。",
    "官方模型卡确认本模型为文本输入/输出；Chartography 需要图表图像理解，故不适用。OSWorld 支持 a11y-tree，故未因无图像输入标为不适用。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
