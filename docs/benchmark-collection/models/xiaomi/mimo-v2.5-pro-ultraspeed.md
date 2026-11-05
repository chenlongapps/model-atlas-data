# MiMo-V2.5-Pro-UltraSpeed Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2.5-pro-ultraspeed
- 模型名称：MiMo-V2.5-Pro-UltraSpeed
- 发布日期：2026-06-08
- 最近检查时间：2026-11-05T03:56+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Xiaomi 2026-06-08 官方公告确认 UltraSpeed 是 MiMo-V2.5-Pro 的 FP4/DFlash/TileRT 推理速度配置；本地没有该变体的目标 Benchmark 成绩。母版成绩不转用。
- 本地 TOML 只列 text 输入；小米关于 V2.5 系列的资料称包含 Pro 的系列支持视觉，但 UltraSpeed API 的图像输入能力未明确，因此 OSWorld 和 Chartography 保持待核实。
- Xiaomi UltraSpeed 公告中的 FP4-vs-FP8 benchmark 图未能读取，可能影响若干目标项的完整核验；已逐项标记需要复核的项目。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Xiaomi MiMo-V2.5 official page](https://mimo.xiaomi.com/mimo-v2-5), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [Xiaomi MiMo-V2.5 inference note](https://mimo.xiaomi.com/zh/blog/mimo-v2-5-inference), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| chartography | 待核实 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography evaluation repository](https://github.com/surge-ai/chartography), [Xiaomi MiMo-V2.5 inference note](https://mimo.xiaomi.com/zh/blog/mimo-v2-5-inference), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| humanitys-last-exam | 待核实 | — | [Scale Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Xiaomi MiMo-V2.5-Pro UltraSpeed profile](https://mimo.mi.com/models/en-US/mimo-v2.5-pro-ultraspeed), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis MiMo-V2.5-Pro profile](https://artificialanalysis.ai/models/mimo-v2-5-pro), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-11-05T03:56+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- DeepSWE 可见榜单中未找到精确 UltraSpeed 行，但页面仅展示 21/28 配置。Xiaomi 公告中的 FP4-vs-FP8 benchmark 图无法读取，暂不能排除图中有相关测量。

尚未解决的问题：
- 官方榜单未显示完整配置，且 Xiaomi 官方图表文本不可读取。

最近核验时间：2026-11-05T03:56+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 未找到 UltraSpeed 的 V2 分数。官方 Xiaomi 图表文本不可读取；基础 MiMo-V2.5-Pro 或其他版本的旧成绩不转用。

尚未解决的问题：
- Xiaomi 官方性能对比图无法读取，尚不能确认是否含对应的 V2 评测结果。

最近核验时间：2026-11-05T03:56+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Xiaomi MiMo-V2.5 official page](https://mimo.xiaomi.com/mimo-v2-5)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 官方 v4 动态榜单抓取为空表，未能确认 UltraSpeed 结果。MiMo-V2.5 页面上的 Terminal-Bench 2.0 56.1 属于不同型号/版本，不映射。

尚未解决的问题：
- 官方动态榜单无法读取；可见的 MiMo-V2.5 Terminal-Bench 2.0 成绩不是 v4。

最近核验时间：2026-11-05T03:56+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 官方 Science 0.1 结果页未列 MiMo UltraSpeed 的精确成绩。

最近核验时间：2026-11-05T03:56+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- Zapier 官方榜单当前显示的 10 项中没有 UltraSpeed，另有 119 项未展开；无法确认完整 1.0.6 列表是否有此 API 型号。

尚未解决的问题：
- 官方排行榜其余 119 行不可见；不把 Pro 母版成绩转给 UltraSpeed。

最近核验时间：2026-11-05T03:56+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [Xiaomi MiMo-V2.5 inference note](https://mimo.xiaomi.com/zh/blog/mimo-v2-5-inference)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 未找到精确 UltraSpeed 公开成绩。小米资料称 V2.5 系列（含 Pro）有视觉能力；UltraSpeed API 公告未明确其图像输入接口，本地 TOML 当前仅列文本输入，故适用性待核实。

尚未解决的问题：
- 需确认 UltraSpeed API 对该具体变体开放图像输入；不可仅凭系列能力判不适用。

最近核验时间：2026-11-05T03:56+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography evaluation repository](https://github.com/surge-ai/chartography)
- [Xiaomi MiMo-V2.5 inference note](https://mimo.xiaomi.com/zh/blog/mimo-v2-5-inference)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- Surge 榜单未找到精确 UltraSpeed 成绩。V2.5 系列资料提及视觉能力，但 UltraSpeed API 的图像输入细节未明确；本地 TOML 仅列文本输入。

尚未解决的问题：
- 需确认 UltraSpeed API 是否接受 Chartography 图表图像；不把 Pro 母版成绩转用。

最近核验时间：2026-11-05T03:56+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Scale Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed profile](https://mimo.mi.com/models/en-US/mimo-v2.5-pro-ultraspeed)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 未找到可读取的 UltraSpeed HLE 原始成绩。Xiaomi 官方 FP4-vs-FP8 benchmark 图无法读取，不能确认是否包含 HLE 测量；不借用基础 MiMo-V2.5-Pro 结果。

尚未解决的问题：
- 官方性能对比图的内容未能读取，待复核是否包含可归属 UltraSpeed 的 HLE 分数。

最近核验时间：2026-11-05T03:56+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis MiMo-V2.5-Pro profile](https://artificialanalysis.ai/models/mimo-v2-5-pro)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 未找到 UltraSpeed 独立的 Artificial Analysis Intelligence Index V5 记录；速度变体与母版结果不自动合并。

最近核验时间：2026-11-05T03:56+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- AA 榜列出 MiMo-V2.5-Pro (Reasoning) 1129 Elo（CI −17/+17），但该条不是 UltraSpeed。Xiaomi 官方 benchmark 图无法读取，尚不能核实 UltraSpeed 独立行。

尚未解决的问题：
- 仅有母版/Reasoning variant 的公开 Elo；需找到 UltraSpeed 精确条目后才能收录。

最近核验时间：2026-11-05T03:56+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Xiaomi MiMo-V2.5-Pro UltraSpeed announcement](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

研究备注：
- 当前公开 Vals v2.2 页未找到 UltraSpeed 精确型号；不从 MiMo-V2.5-Pro 或后续系列迁移成绩。

最近核验时间：2026-11-05T03:56+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiMo-V2.5-Pro profile",
          "url": "https://artificialanalysis.ai/models/mimo-v2-5-pro"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "未找到 UltraSpeed 独立的 Artificial Analysis Intelligence Index V5 记录；速度变体与母版结果不自动合并。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "Zapier 官方榜单当前显示的 10 项中没有 UltraSpeed，另有 119 项未展开；无法确认完整 1.0.6 列表是否有此 API 型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方排行榜其余 119 行不可见；不把 Pro 母版成绩转给 UltraSpeed。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Xiaomi MiMo-V2.5 inference note",
          "url": "https://mimo.xiaomi.com/zh/blog/mimo-v2-5-inference"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "Surge 榜单未找到精确 UltraSpeed 成绩。V2.5 系列资料提及视觉能力，但 UltraSpeed API 的图像输入细节未明确；本地 TOML 仅列文本输入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 UltraSpeed API 是否接受 Chartography 图表图像；不把 Pro 母版成绩转用。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "DeepSWE 可见榜单中未找到精确 UltraSpeed 行，但页面仅展示 21/28 配置。Xiaomi 公告中的 FP4-vs-FP8 benchmark 图无法读取，暂不能排除图中有相关测量。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单未显示完整配置，且 Xiaomi 官方图表文本不可读取。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "AA 榜列出 MiMo-V2.5-Pro (Reasoning) 1129 Elo（CI −17/+17），但该条不是 UltraSpeed。Xiaomi 官方 benchmark 图无法读取，尚不能核实 UltraSpeed 独立行。"
      ],
      "status": "待核实",
      "unresolved": [
        "仅有母版/Reasoning variant 的公开 Elo；需找到 UltraSpeed 精确条目后才能收录。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Scale Humanity’s Last Exam leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed profile",
          "url": "https://mimo.mi.com/models/en-US/mimo-v2.5-pro-ultraspeed"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "未找到可读取的 UltraSpeed HLE 原始成绩。Xiaomi 官方 FP4-vs-FP8 benchmark 图无法读取，不能确认是否包含 HLE 测量；不借用基础 MiMo-V2.5-Pro 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方性能对比图的内容未能读取，待复核是否包含可归属 UltraSpeed 的 HLE 分数。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "OSWorld official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Xiaomi MiMo-V2.5 inference note",
          "url": "https://mimo.xiaomi.com/zh/blog/mimo-v2-5-inference"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "未找到精确 UltraSpeed 公开成绩。小米资料称 V2.5 系列（含 Pro）有视觉能力；UltraSpeed API 公告未明确其图像输入接口，本地 TOML 当前仅列文本输入，故适用性待核实。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 UltraSpeed API 对该具体变体开放图像输入；不可仅凭系列能力判不适用。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "未找到 UltraSpeed 的 V2 分数。官方 Xiaomi 图表文本不可读取；基础 MiMo-V2.5-Pro 或其他版本的旧成绩不转用。"
      ],
      "status": "待核实",
      "unresolved": [
        "Xiaomi 官方性能对比图无法读取，尚不能确认是否含对应的 V2 评测结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "官方 Science 0.1 结果页未列 MiMo UltraSpeed 的精确成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Xiaomi MiMo-V2.5 official page",
          "url": "https://mimo.xiaomi.com/mimo-v2-5"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "官方 v4 动态榜单抓取为空表，未能确认 UltraSpeed 结果。MiMo-V2.5 页面上的 Terminal-Bench 2.0 56.1 属于不同型号/版本，不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态榜单无法读取；可见的 MiMo-V2.5 Terminal-Bench 2.0 成绩不是 v4。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:56+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Xiaomi MiMo-V2.5-Pro UltraSpeed announcement",
          "url": "https://mimo.xiaomi.com/blog/mimo-tilert-1000tps"
        }
      ],
      "notes": [
        "当前公开 Vals v2.2 页未找到 UltraSpeed 精确型号；不从 MiMo-V2.5-Pro 或后续系列迁移成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:56+08:00",
  "model_id": "xiaomi/mimo-v2.5-pro-ultraspeed",
  "model_notes": [
    "Xiaomi 2026-06-08 官方公告确认 UltraSpeed 是 MiMo-V2.5-Pro 的 FP4/DFlash/TileRT 推理速度配置；本地没有该变体的目标 Benchmark 成绩。母版成绩不转用。",
    "本地 TOML 只列 text 输入；小米关于 V2.5 系列的资料称包含 Pro 的系列支持视觉，但 UltraSpeed API 的图像输入能力未明确，因此 OSWorld 和 Chartography 保持待核实。",
    "Xiaomi UltraSpeed 公告中的 FP4-vs-FP8 benchmark 图未能读取，可能影响若干目标项的完整核验；已逐项标记需要复核的项目。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
