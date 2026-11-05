# Claude Mythos 5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-mythos-5
- 模型名称：Claude Mythos 5
- 发布日期：2026-06-09
- 最近检查时间：2026-11-05T03:36+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Anthropic 将 Fable 5 与 Mythos 5 描述为同一基础模型的不同安全配置；本任务按独立模型 ID 核对，不迁移 Fable 5 成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 官方结果](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5) | 2026-11-05T03:36+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5) | 2026-11-05T03:36+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T03:36+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1), [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5) | 2026-11-05T03:36+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [AutomationBench 官方 README](https://github.com/zapier/AutomationBench), [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md) | 2026-11-05T03:36+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5) | 2026-11-05T03:36+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方评测仓库](https://github.com/surge-ai/chartography) | 2026-11-05T03:36+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5) | 2026-11-05T03:36+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models), [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T03:36+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Anthropic 2026-09 Fable 5.1 / Mythos 5.1 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-05T03:36+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T03:36+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 官方结果](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)

研究备注：
- DeepSWE v1.1 官方结果显示 21/28 个模型配置；可读取的榜单片段有 Fable 5 而没有 Mythos 5，不能据此断定完整榜单没有 Mythos 5。Fable 5 的分数不转给 Mythos。

尚未解决的问题：
- 公开页面显示的模型配置不完整，无法确认精确 Mythos 5 行。

最近核验时间：2026-11-05T03:36+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)

研究备注：
- Scale SWE-bench Pro V2 Full 榜未列出 Claude Mythos 5 的精确型号行；Fable 5 或 Fable 5.1 的结果均未转用。

最近核验时间：2026-11-05T03:36+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 未能从 Terminal-Bench 4.0 官方动态榜单稳定读取 Claude Mythos 5 的具体记录；未把 Fable 5 分数转用。

尚未解决的问题：
- 官方动态榜单无法稳定读取完整行，不能确认 Mythos 5 是否有公开结果。

最近核验时间：2026-11-05T03:36+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)

研究备注：
- Terminal-Bench-Science 0.1 官方结果列出 Fable 5 和其他模型，但没有 Mythos 5；不把不同安全配置下的 Fable 5 结果转用。

最近核验时间：2026-11-05T03:36+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方 README](https://github.com/zapier/AutomationBench)
- [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)

研究备注：
- Zapier 官方榜单标注版本 1.0.6，但页面只显示前 10 项，其余 119 项折叠；无法确认完整列表是否有 Mythos 5。未找到能精确归属到 Mythos 5 的分数。

尚未解决的问题：
- 官方榜单剩余条目折叠，无法确认完整模型列表。

最近核验时间：2026-11-05T03:36+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)

研究备注：
- Mythos 5 具备图像能力，OSWorld 适用；本轮未找到其精确 v2.1 成绩，不能用 Fable 5 的 OSWorld 2.0 结果替代。

尚未解决的问题：
- 未能从已检查的官方资料确认完整 v2.1 模型结果。

最近核验时间：2026-11-05T03:36+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography 官方评测仓库](https://github.com/surge-ai/chartography)

研究备注：
- Surge 当前 Chartography 官方榜单没有 Claude Mythos 5 的公开行；该模型具备图像输入，目标适用。

最近核验时间：2026-11-05T03:36+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Anthropic Claude Fable 5 / Mythos 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)

研究备注：
- Scale 当前 HLE 榜单未找到 Claude Mythos 5 精确行；Fable 5 的 HLE 成绩不转用。

最近核验时间：2026-11-05T03:36+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis 当前公开模型榜单和 V5 指数页未找到 Mythos 5 的 V5 综合分数；不借用 Fable 5 分数。

最近核验时间：2026-11-05T03:36+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Anthropic 2026-09 Fable 5.1 / Mythos 5.1 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- Artificial Analysis GDPval-AA v2.1 榜单未列 Claude Mythos 5 的 Elo 行；Anthropic 的 Fable 5 或 v2 结果不属于此型号和目标版本。

最近核验时间：2026-11-05T03:36+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前公开 v2.2 榜单未见 Claude Mythos 5 的精确型号行；未将 Fable 5 的分数转用。

最近核验时间：2026-11-05T03:36+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 模型榜单",
          "url": "https://artificialanalysis.ai/leaderboards/models"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis 当前公开模型榜单和 V5 指数页未找到 Mythos 5 的 V5 综合分数；不借用 Fable 5 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方 README",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "AutomationBench 官方变更记录",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        }
      ],
      "notes": [
        "Zapier 官方榜单标注版本 1.0.6，但页面只显示前 10 项，其余 119 项折叠；无法确认完整列表是否有 Mythos 5。未找到能精确归属到 Mythos 5 的分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单剩余条目折叠，无法确认完整模型列表。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography 官方评测仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 当前 Chartography 官方榜单没有 Claude Mythos 5 的公开行；该模型具备图像输入，目标适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方结果",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Anthropic Claude Fable 5 / Mythos 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        }
      ],
      "notes": [
        "DeepSWE v1.1 官方结果显示 21/28 个模型配置；可读取的榜单片段有 Fable 5 而没有 Mythos 5，不能据此断定完整榜单没有 Mythos 5。Fable 5 的分数不转给 Mythos。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开页面显示的模型配置不完整，无法确认精确 Mythos 5 行。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Anthropic 2026-09 Fable 5.1 / Mythos 5.1 评测页",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "Artificial Analysis GDPval-AA v2.1 榜单未列 Claude Mythos 5 的 Elo 行；Anthropic 的 Fable 5 或 v2 结果不属于此型号和目标版本。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Scale Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Anthropic Claude Fable 5 / Mythos 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        }
      ],
      "notes": [
        "Scale 当前 HLE 榜单未找到 Claude Mythos 5 精确行；Fable 5 的 HLE 成绩不转用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 2.1 官方公开评测指南",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "Anthropic Claude Fable 5 / Mythos 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        }
      ],
      "notes": [
        "Mythos 5 具备图像能力，OSWorld 适用；本轮未找到其精确 v2.1 成绩，不能用 Fable 5 的 OSWorld 2.0 结果替代。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能从已检查的官方资料确认完整 v2.1 模型结果。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Anthropic Claude Fable 5 / Mythos 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        }
      ],
      "notes": [
        "Scale SWE-bench Pro V2 Full 榜未列出 Claude Mythos 5 的精确型号行；Fable 5 或 Fable 5.1 的结果均未转用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方结果",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Anthropic Claude Fable 5 / Mythos 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 0.1 官方结果列出 Fable 5 和其他模型，但没有 Mythos 5；不把不同安全配置下的 Fable 5 结果转用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方榜单",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "未能从 Terminal-Bench 4.0 官方动态榜单稳定读取 Claude Mythos 5 的具体记录；未把 Fable 5 分数转用。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态榜单无法稳定读取完整行，不能确认 Mythos 5 是否有公开结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:36+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前公开 v2.2 榜单未见 Claude Mythos 5 的精确型号行；未将 Fable 5 的分数转用。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:36+08:00",
  "model_id": "anthropic/claude-mythos-5",
  "model_notes": [
    "Anthropic 将 Fable 5 与 Mythos 5 描述为同一基础模型的不同安全配置；本任务按独立模型 ID 核对，不迁移 Fable 5 成绩。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
