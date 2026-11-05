# Aion-3.0-Mini Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：aion-labs/aion-3.0-mini
- 模型名称：Aion-3.0-Mini
- 发布日期：2026-05-14
- 最近检查时间：2026-11-05T06:01+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 模型身份为 Aion-3.0-Mini，发布日期 2026-05-14；官方目录/API 标为文本输入/输出并支持工具调用。
- Chartography 需要图表图像输入，因此对 text->text 的该型号标为不适用；OSWorld 可走 accessibility-tree agent 路径，仍保留待核实状态。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T06:01+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:01+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?efforts=all&version=4.0), [AA Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:01+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science 0.1 announcement](https://www.tbench.ai/news/terminal-bench-science-0-1), [AA Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:01+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench), [Aion model catalog](https://www.aionlabs.ai/docs/models/) | 2026-11-05T06:01+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2 project page](https://osworld-v2.xlang.ai/), [Aion API model catalog](https://api.aionlabs.ai/v1/models) | 2026-11-05T06:01+08:00 |
| chartography | 不适用 | — | [Aion model catalog](https://www.aionlabs.ai/docs/models/), [Chartography official page](https://surgehq.ai/benchmarks/chartography), [Chartography repository](https://github.com/surge-ai/chartography) | 2026-11-05T06:01+08:00 |
| humanitys-last-exam | 未找到 | — | [Aion model catalog](https://www.aionlabs.ai/docs/models/), [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:01+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Aion model catalog](https://www.aionlabs.ai/docs/models/), [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:01+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Aion model catalog](https://www.aionlabs.ai/docs/models/), [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:01+08:00 |
| vals-index-v2.2 | 未找到 | — | [Aion model catalog](https://www.aionlabs.ai/docs/models/), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:01+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 榜单当前可见 21/28 个模型，未见 Aion-3.0-Mini。

尚未解决的问题：
- 榜单仅显示部分模型，无法确认未展示结果中是否含该型号。

最近核验时间：2026-11-05T06:01+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查 V2 官方榜单，未找到 Aion-3.0-Mini 精确型号；公开展示结果不完整。

尚未解决的问题：
- 缺少完整候选清单，无法确认未展示的评测记录。

最近核验时间：2026-11-05T06:01+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?efforts=all&version=4.0)
- [AA Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 官方 TB4 榜单当前没有可读模型结果；未找到 Aion-3.0-Mini 的可核实分数。

尚未解决的问题：
- 动态榜单数据未能读取，不能据此判断是否已有分数。

最近核验时间：2026-11-05T06:01+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science 0.1 announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [AA Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 检查官方发布资料与 AA 方法页，未取得 Aion-3.0-Mini 的具体模型行或分数。

尚未解决的问题：
- 动态结果表未能核实目标型号是否被评测。

最近核验时间：2026-11-05T06:01+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Aion model catalog](https://www.aionlabs.ai/docs/models/)

研究备注：
- Aion-3.0-Mini 支持工具调用，评测类型可能适用；Zapier 榜单其余 119 项折叠。

尚未解决的问题：
- 无法查看完整榜单，目标型号是否出现在折叠部分仍待核实。

最近核验时间：2026-11-05T06:01+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2 project page](https://osworld-v2.xlang.ai/)
- [Aion API model catalog](https://api.aionlabs.ai/v1/models)

研究备注：
- 模型是文本输入/输出但支持工具调用；OSWorld 具备 a11y-tree 观察路径，不能仅凭缺少图像输入判不适用。未找到该精确型号的 V2.1 分数。

尚未解决的问题：
- 尚未找到能确认 Aion-3.0-Mini 与 OSWorld 2.1 对应关系的公开结果。

最近核验时间：2026-11-05T06:01+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Aion model catalog](https://www.aionlabs.ai/docs/models/)
- [Chartography official page](https://surgehq.ai/benchmarks/chartography)
- [Chartography repository](https://github.com/surge-ai/chartography)

研究备注：
- Aion-3.0-Mini 为 text->text，不能接收 Chartography 任务要求的图表图像。

最近核验时间：2026-11-05T06:01+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Aion model catalog](https://www.aionlabs.ai/docs/models/)
- [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 检查 Aion 官方目录与 AA HLE 资料，未找到该精确型号的公开成绩。

最近核验时间：2026-11-05T06:01+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Aion model catalog](https://www.aionlabs.ai/docs/models/)
- [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 未找到 Aion-3.0-Mini 对应 Artificial Analysis Intelligence Index V5 的公开分数。

最近核验时间：2026-11-05T06:01+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Aion model catalog](https://www.aionlabs.ai/docs/models/)
- [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 检查官方 Aion 资料与 AA GDPval-AA v2.1 页面，未找到该精确型号的 Elo 成绩。

最近核验时间：2026-11-05T06:01+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Aion model catalog](https://www.aionlabs.ai/docs/models/)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查当前 V2.2 官方榜单，未发现 Aion-3.0-Mini 精确条目。

最近核验时间：2026-11-05T06:01+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Aion model catalog",
          "url": "https://www.aionlabs.ai/docs/models/"
        },
        {
          "label": "AA Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "未找到 Aion-3.0-Mini 对应 Artificial Analysis Intelligence Index V5 的公开分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Aion model catalog",
          "url": "https://www.aionlabs.ai/docs/models/"
        }
      ],
      "notes": [
        "Aion-3.0-Mini 支持工具调用，评测类型可能适用；Zapier 榜单其余 119 项折叠。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法查看完整榜单，目标型号是否出现在折叠部分仍待核实。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Aion model catalog",
          "url": "https://www.aionlabs.ai/docs/models/"
        },
        {
          "label": "Chartography official page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Aion-3.0-Mini 为 text->text，不能接收 Chartography 任务要求的图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "榜单当前可见 21/28 个模型，未见 Aion-3.0-Mini。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单仅显示部分模型，无法确认未展示结果中是否含该型号。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Aion model catalog",
          "url": "https://www.aionlabs.ai/docs/models/"
        },
        {
          "label": "GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "检查官方 Aion 资料与 AA GDPval-AA v2.1 页面，未找到该精确型号的 Elo 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Aion model catalog",
          "url": "https://www.aionlabs.ai/docs/models/"
        },
        {
          "label": "Artificial Analysis HLE",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "检查 Aion 官方目录与 AA HLE 资料，未找到该精确型号的公开成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2 project page",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Aion API model catalog",
          "url": "https://api.aionlabs.ai/v1/models"
        }
      ],
      "notes": [
        "模型是文本输入/输出但支持工具调用；OSWorld 具备 a11y-tree 观察路径，不能仅凭缺少图像输入判不适用。未找到该精确型号的 V2.1 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "尚未找到能确认 Aion-3.0-Mini 与 OSWorld 2.1 对应关系的公开结果。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查 V2 官方榜单，未找到 Aion-3.0-Mini 精确型号；公开展示结果不完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "缺少完整候选清单，无法确认未展示的评测记录。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "AA Terminal-Bench-Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "检查官方发布资料与 AA 方法页，未取得 Aion-3.0-Mini 的具体模型行或分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态结果表未能核实目标型号是否被评测。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        },
        {
          "label": "AA Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "官方 TB4 榜单当前没有可读模型结果；未找到 Aion-3.0-Mini 的可核实分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单数据未能读取，不能据此判断是否已有分数。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Aion model catalog",
          "url": "https://www.aionlabs.ai/docs/models/"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "检查当前 V2.2 官方榜单，未发现 Aion-3.0-Mini 精确条目。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:01+08:00",
  "model_id": "aion-labs/aion-3.0-mini",
  "model_notes": [
    "模型身份为 Aion-3.0-Mini，发布日期 2026-05-14；官方目录/API 标为文本输入/输出并支持工具调用。",
    "Chartography 需要图表图像输入，因此对 text->text 的该型号标为不适用；OSWorld 可走 accessibility-tree agent 路径，仍保留待核实状态。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
