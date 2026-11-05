# North Mini Code Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：cohere/north-mini-code-1-0
- 模型名称：North Mini Code
- 发布日期：2026-06-09
- 最近检查时间：2026-11-05T03:38+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- North Mini Code 的官方卡注明 Text only；OSWorld 2.1 与 Chartography 因缺少视觉输入能力判为不适用。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [DeepSWE v1.1 官方结果](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T03:38+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T03:38+08:00 |
| terminal-bench-v4 | 未找到 | — | [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all) | 2026-11-05T03:38+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T03:38+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [AutomationBench 官方 README](https://github.com/zapier/AutomationBench), [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md), [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | 2026-11-05T03:38+08:00 |
| osworld-v2.1 | 不适用 | — | [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T03:38+08:00 |
| chartography | 不适用 | — | [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [Surge Chartography 官方说明](https://github.com/surge-ai/chartography) | 2026-11-05T03:38+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | 2026-11-05T03:38+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 27.6 (metric=index score) | [Artificial Analysis North Mini Code 页面](https://artificialanalysis.ai/models/north-mini-code), [本地成绩所引 Artificial Analysis 文章](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model), [Artificial Analysis Intelligence Index 页面](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T03:38+08:00 |
| gdpval-aa-v2.1 | 待核实 | 14 (metric=win rate) | [Artificial Analysis GDPval-AA v2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [本地行所引 Artificial Analysis 文章](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model) | 2026-11-05T03:38+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index), [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | 2026-11-05T03:38+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
- [DeepSWE v1.1 官方结果](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Cohere 官方模型卡没有列 DeepSWE v1.1 结果；本轮官方榜单可读内容没有 North Mini Code 的精确成绩。其他代码 benchmark 不转用。

最近核验时间：2026-11-05T03:38+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
- [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 本地已有 SWE-Bench Pro 40.2 (resolve rate)，但没有版本字段，且来源文章日期为 2026-06-09；SWE-bench Pro V2 于 2026-09-22 发布，不能把旧行视作 V2。Scale V2 榜未找到 North Mini Code 的 exact row。

尚未解决的问题：
- 本地 40.2 行没有版本，无法确认它是否使用 SWE-bench Pro V2 数据。

最近核验时间：2026-11-05T03:38+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
- [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all)

研究备注：
- 本地 Terminal-Bench 36 属于旧 v2 结果，不能映射到 v4；本轮官方 v4 榜单和 Cohere 模型卡均未提供 North Mini Code v4 分数。

最近核验时间：2026-11-05T03:38+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
- [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Cohere 官方模型卡和 Terminal-Bench-Science 0.1 官方结果页未列 North Mini Code 的该版本成绩。

最近核验时间：2026-11-05T03:38+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方 README](https://github.com/zapier/AutomationBench)
- [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)

研究备注：
- Zapier 当前榜单显示 1.0.6，但可读页面仅展示前 10 项，119 项折叠；无法确认完整榜单中是否存在 North Mini Code。Cohere 模型支持工具调用，但没有找到该版本的精确分数。

尚未解决的问题：
- Zapier 官方榜单其余条目折叠，无法确认完整列表。

最近核验时间：2026-11-05T03:38+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
- [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- Cohere 官方模型卡明确为 Text only；OSWorld 2.1 标准评测需要截图视觉输入，因此该模型不适用于本项。

最近核验时间：2026-11-05T03:38+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
- [Surge Chartography 官方说明](https://github.com/surge-ai/chartography)

研究备注：
- Chartography 评测依赖图表图像输入；Cohere 官方模型卡将 North Mini Code 标为 Text only。

最近核验时间：2026-11-05T03:38+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)

研究备注：
- Scale Humanity’s Last Exam 官方榜单没有 North Mini Code 的原始 HLE 分数；本地模型文件也无 HLE 行。

最近核验时间：2026-11-05T03:38+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 27.6
- metric: index score
- source: [https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model)
- date: 2026-06-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis North Mini Code 页面](https://artificialanalysis.ai/models/north-mini-code)
- [本地成绩所引 Artificial Analysis 文章](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model)
- [Artificial Analysis Intelligence Index 页面](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 本地 27.6 index score 未标 Artificial Analysis Index 版本，不能确认是 V5。Artificial Analysis 当前模型页 V5.0.1 显示 N/A / No publicly available API；未找到可直接确认的 V5 成绩。

尚未解决的问题：
- 本地 27.6 分数没有 Index 版本，无法与 V5 对齐。

最近核验时间：2026-11-05T03:38+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 14
- metric: win rate
- source: [https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model)
- date: 2026-06-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [本地行所引 Artificial Analysis 文章](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model)

研究备注：
- 本地 GDPval-AA 14 的 metric 为 win rate、无版本；GDPval-AA v2.1 定义要求 Elo rating。当前 AA v2.1 榜单未找到 North Mini Code 的 Elo 记录，不把 14% 转为 Elo 或标记成 v2.1。

尚未解决的问题：
- 本地 win rate 行的版本和与 v2.1 的关系未说明，指标也不同于本地定义。

最近核验时间：2026-11-05T03:38+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)
- [Cohere North Mini Code 官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)

研究备注：
- Vals 当前 v2.2 榜单未找到 North Mini Code 的精确记录；本地模型文件没有 Vals Index 行。

最近核验时间：2026-11-05T03:38+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis North Mini Code 页面",
          "url": "https://artificialanalysis.ai/models/north-mini-code"
        },
        {
          "label": "本地成绩所引 Artificial Analysis 文章",
          "url": "https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model"
        },
        {
          "label": "Artificial Analysis Intelligence Index 页面",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "本地 27.6 index score 未标 Artificial Analysis Index 版本，不能确认是 V5。Artificial Analysis 当前模型页 V5.0.1 显示 N/A / No publicly available API；未找到可直接确认的 V5 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地 27.6 分数没有 Index 版本，无法与 V5 对齐。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:38+08:00",
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
        },
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        }
      ],
      "notes": [
        "Zapier 当前榜单显示 1.0.6，但可读页面仅展示前 10 项，119 项折叠；无法确认完整榜单中是否存在 North Mini Code。Cohere 模型支持工具调用，但没有找到该版本的精确分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 官方榜单其余条目折叠，无法确认完整列表。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        },
        {
          "label": "Surge Chartography 官方说明",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography 评测依赖图表图像输入；Cohere 官方模型卡将 North Mini Code 标为 Text only。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        },
        {
          "label": "DeepSWE v1.1 官方结果",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Cohere 官方模型卡没有列 DeepSWE v1.1 结果；本轮官方榜单可读内容没有 North Mini Code 的精确成绩。其他代码 benchmark 不转用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "本地行所引 Artificial Analysis 文章",
          "url": "https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model"
        }
      ],
      "notes": [
        "本地 GDPval-AA 14 的 metric 为 win rate、无版本；GDPval-AA v2.1 定义要求 Elo rating。当前 AA v2.1 榜单未找到 North Mini Code 的 Elo 记录，不把 14% 转为 Elo 或标记成 v2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地 win rate 行的版本和与 v2.1 的关系未说明，指标也不同于本地定义。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Scale Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        }
      ],
      "notes": [
        "Scale Humanity’s Last Exam 官方榜单没有 North Mini Code 的原始 HLE 分数；本地模型文件也无 HLE 行。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        },
        {
          "label": "OSWorld 2.1 官方公开评测指南",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "Cohere 官方模型卡明确为 Text only；OSWorld 2.1 标准评测需要截图视觉输入，因此该模型不适用于本项。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        },
        {
          "label": "Scale SWE-bench Pro V2 Full 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "本地已有 SWE-Bench Pro 40.2 (resolve rate)，但没有版本字段，且来源文章日期为 2026-06-09；SWE-bench Pro V2 于 2026-09-22 发布，不能把旧行视作 V2。Scale V2 榜未找到 North Mini Code 的 exact row。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地 40.2 行没有版本，无法确认它是否使用 SWE-bench Pro V2 数据。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        },
        {
          "label": "Terminal-Bench-Science 0.1 官方结果",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Cohere 官方模型卡和 Terminal-Bench-Science 0.1 官方结果页未列 North Mini Code 的该版本成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        },
        {
          "label": "Terminal-Bench 4.0 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Terminal-Bench 4.0 官方榜单",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        }
      ],
      "notes": [
        "本地 Terminal-Bench 36 属于旧 v2 结果，不能映射到 v4；本轮官方 v4 榜单和 Cohere 模型卡均未提供 North Mini Code v4 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:38+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Cohere North Mini Code 官方模型卡",
          "url": "https://huggingface.co/CohereLabs/North-Mini-Code-1.0"
        }
      ],
      "notes": [
        "Vals 当前 v2.2 榜单未找到 North Mini Code 的精确记录；本地模型文件没有 Vals Index 行。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:38+08:00",
  "model_id": "cohere/north-mini-code-1-0",
  "model_notes": [
    "North Mini Code 的官方卡注明 Text only；OSWorld 2.1 与 Chartography 因缺少视觉输入能力判为不适用。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
