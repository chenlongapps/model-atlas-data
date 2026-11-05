# Laguna S 2.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：poolside/laguna-s-2.1
- 模型名称：Laguna S 2.1
- 发布日期：2026-07-21
- 最近检查时间：2026-11-04T23:15+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- Poolside 官方资料确认 Laguna S 2.1 是 118B-A8B 模型，区别于 Laguna XS 2.1 和 Laguna M.1。原有模型描述将它误列为 XS 规格；已据官方规格更正模型英文描述和 zh-CN 本地化。
- DeepSWE 40.4 来自 Poolside 自有 pool harness、max thinking 配置；按官方方法说明保存 pass@1 每题三次尝试汇总条件。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 40.4 (metric=pass@1; version=1.1; effort=max thinking; variant=pass@1 averaged over 3 attempts per task; harness=pool) | [Poolside Laguna S 2.1 release and evaluation methodology](https://poolside.ai/blog/introducing-laguna-s-2-1), [Poolside Laguna S 2.1 model card](https://huggingface.co/poolside/Laguna-S-2.1), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T23:15+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:15+08:00 |
| terminal-bench-v4 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T23:15+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T23:15+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Poolside Laguna S 2.1 model card](https://huggingface.co/poolside/Laguna-S-2.1), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T23:15+08:00 |
| osworld-v2.1 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-04T23:15+08:00 |
| chartography | 不适用 | — | [Poolside Laguna S 2.1 model card](https://huggingface.co/poolside/Laguna-S-2.1), [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T23:15+08:00 |
| humanitys-last-exam | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T23:15+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Artificial Analysis model overview](https://artificialanalysis.ai/models) | 2026-11-04T23:15+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T23:15+08:00 |
| vals-index-v2.2 | 待核实 | — | [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T23:15+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 40.4
- metric: pass@1
- version: 1.1
- effort: max thinking
- variant: pass@1 averaged over 3 attempts per task
- harness: pool
- source: [https://poolside.ai/blog/introducing-laguna-s-2-1](https://poolside.ai/blog/introducing-laguna-s-2-1)
- date: 2026-07-21
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Poolside Laguna S 2.1 release and evaluation methodology](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Poolside Laguna S 2.1 model card](https://huggingface.co/poolside/Laguna-S-2.1)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Poolside 明确报告 Laguna S 2.1 在 DeepSWE v1.1 的 40.4，使用 max thinking 和自有 pool harness；官方说明 pass@1 按每题三次尝试汇总。原始成绩已写入模型 TOML，未假定 Poolside harness 等同于 DeepSWE 榜单的 mini-swe-agent。

最近核验时间：2026-11-04T23:15+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Poolside 在 2026-07-21 发布的旧结果表列 SWE-Bench Pro (Public Dataset) 59.4，但未标为 V2；Scale 记载 V2 在 2026-09-22 发布，使用刷新后的 split 和锁定协议。不能将 59.4 映射为 V2，当前 V2 榜单未见 Laguna S 2.1。

最近核验时间：2026-11-04T23:15+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Poolside 公布的是 Terminal-Bench 2.1 70.2，不是 v4；Vals 当前 Terminal-Bench 4.0 榜单未见 Laguna S 2.1。未将 2.1 成绩转记到 v4。

最近核验时间：2026-11-04T23:15+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Poolside 发布的评测表未包含 Terminal-Bench-Science 0.1；Vals 当前榜单未见 Laguna S 2.1。

最近核验时间：2026-11-04T23:15+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Poolside Laguna S 2.1 model card](https://huggingface.co/poolside/Laguna-S-2.1)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- Poolside 公布的 S 2.1 评测表没有 AutomationBench；Zapier 当前 1.0.6 榜单未列 Laguna S 2.1。

最近核验时间：2026-11-04T23:15+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Poolside 发布材料未列 OSWorld v2.1；OSWorld 官方 v2.1 发布资料未提供 Laguna S 2.1 成绩。

最近核验时间：2026-11-04T23:15+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Poolside Laguna S 2.1 model card](https://huggingface.co/poolside/Laguna-S-2.1)
- [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Laguna S 2.1 的官方模型卡为 text-to-text，模型发布说明称该型号缺乏视觉能力；Chartography 直接评测需要图表视觉理解。未发现包含额外视觉输入或图表转换工具的独立评测配置。

最近核验时间：2026-11-04T23:15+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Poolside 发布评测材料未列 HLE；Artificial Analysis HLE 页面当前可见内容未列 Laguna S 2.1。

最近核验时间：2026-11-04T23:15+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Artificial Analysis model overview](https://artificialanalysis.ai/models)

研究备注：
- Poolside 发布材料未报告 Artificial Analysis Intelligence Index V5；Artificial Analysis 当前模型总览未显示 Laguna S 2.1，也未找到对应的 AA 型号页。

最近核验时间：2026-11-04T23:15+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Poolside 发布评测材料未列 GDPval-AA；Artificial Analysis v2.1 页面当前可见内容未列 Laguna S 2.1。没有可核实的 Elo 或该型号运行配置。

最近核验时间：2026-11-04T23:15+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Poolside Laguna S 2.1 release](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前页面标示 Index v2.2，并展示每个实验室最佳模型及最新、顶尖和前沿模型子集；未列 Laguna S 2.1，但页面不是完整历史成绩清单。Vals 的政治倾向研究不是 Vals Index，不能作为该项分数。

尚未解决的问题：
- 无法根据当前精选榜单确认 Laguna S 2.1 是否曾获得 Vals Index v2.2 成绩。

最近核验时间：2026-11-04T23:15+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Artificial Analysis model overview",
          "url": "https://artificialanalysis.ai/models"
        }
      ],
      "notes": [
        "Poolside 发布材料未报告 Artificial Analysis Intelligence Index V5；Artificial Analysis 当前模型总览未显示 Laguna S 2.1，也未找到对应的 AA 型号页。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Poolside Laguna S 2.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-S-2.1"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Poolside 公布的 S 2.1 评测表没有 AutomationBench；Zapier 当前 1.0.6 榜单未列 Laguna S 2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-S-2.1"
        },
        {
          "label": "Surge Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Laguna S 2.1 的官方模型卡为 text-to-text，模型发布说明称该型号缺乏视觉能力；Chartography 直接评测需要图表视觉理解。未发现包含额外视觉输入或图表转换工具的独立评测配置。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release and evaluation methodology",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Poolside Laguna S 2.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-S-2.1"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Poolside 明确报告 Laguna S 2.1 在 DeepSWE v1.1 的 40.4，使用 max thinking 和自有 pool harness；官方说明 pass@1 按每题三次尝试汇总。原始成绩已写入模型 TOML，未假定 Poolside harness 等同于 DeepSWE 榜单的 mini-swe-agent。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Poolside 发布评测材料未列 GDPval-AA；Artificial Analysis v2.1 页面当前可见内容未列 Laguna S 2.1。没有可核实的 Elo 或该型号运行配置。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Poolside 发布评测材料未列 HLE；Artificial Analysis HLE 页面当前可见内容未列 Laguna S 2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Poolside 发布材料未列 OSWorld v2.1；OSWorld 官方 v2.1 发布资料未提供 Laguna S 2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Poolside 在 2026-07-21 发布的旧结果表列 SWE-Bench Pro (Public Dataset) 59.4，但未标为 V2；Scale 记载 V2 在 2026-09-22 发布，使用刷新后的 split 和锁定协议。不能将 59.4 映射为 V2，当前 V2 榜单未见 Laguna S 2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Poolside 发布的评测表未包含 Terminal-Bench-Science 0.1；Vals 当前榜单未见 Laguna S 2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Poolside 公布的是 Terminal-Bench 2.1 70.2，不是 v4；Vals 当前 Terminal-Bench 4.0 榜单未见 Laguna S 2.1。未将 2.1 成绩转记到 v4。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:15+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna S 2.1 release",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前页面标示 Index v2.2，并展示每个实验室最佳模型及最新、顶尖和前沿模型子集；未列 Laguna S 2.1，但页面不是完整历史成绩清单。Vals 的政治倾向研究不是 Vals Index，不能作为该项分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法根据当前精选榜单确认 Laguna S 2.1 是否曾获得 Vals Index v2.2 成绩。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:15+08:00",
  "model_id": "poolside/laguna-s-2.1",
  "model_notes": [
    "Poolside 官方资料确认 Laguna S 2.1 是 118B-A8B 模型，区别于 Laguna XS 2.1 和 Laguna M.1。原有模型描述将它误列为 XS 规格；已据官方规格更正模型英文描述和 zh-CN 本地化。",
    "DeepSWE 40.4 来自 Poolside 自有 pool harness、max thinking 配置；按官方方法说明保存 pass@1 每题三次尝试汇总条件。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
