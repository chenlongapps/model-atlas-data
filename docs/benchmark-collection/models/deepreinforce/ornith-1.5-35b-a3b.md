# Ornith 1.5 35B A3B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepreinforce/ornith-1.5-35b-a3b
- 模型名称：Ornith 1.5 35B A3B
- 发布日期：2026-08-18
- 最近检查时间：2026-11-04T16:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 22 (variant=mean of 5 runs; temperature=1.0; top_p=0.95; context=256K; harness=Claude Code) | [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/) | 2026-11-04T16:58+08:00 |
| swe-bench-pro-v2 | 待核实 | 59.6 (variant=mean of 5 runs; temperature=1.0; top_p=0.95; context=256K; network disabled; git history removed; harness=OpenHands) | [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), [Scale SWE-bench Pro 官方数据集与榜单](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-04T16:58+08:00 |
| terminal-bench-v4 | 未找到 | — | [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), [Vals Terminal-Bench 4 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-4), [Terminal-Bench 4 官方说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T16:58+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), [Vals Terminal-Bench Science 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench Science 页面](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T16:58+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks) | 2026-11-04T16:58+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2.1 官方发布数据](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | 2026-11-04T16:58+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | 2026-11-04T16:58+08:00 |
| humanitys-last-exam | 已收录 | 25.6 (metric=accuracy; variant=no tools; mean of 5 runs; Claude 4.6 Opus judge); 33.4 (metric=accuracy; variant=with tools; mean of 5 runs; Claude 4.6 Opus judge) | [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B), [Humanity’s Last Exam 官方定义与准确率指标](https://lastexam.ai/) | 2026-11-04T16:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index 官方榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | 2026-11-04T16:58+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | 2026-11-04T16:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index), [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B) | 2026-11-04T16:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 22
- variant: mean of 5 runs; temperature=1.0; top_p=0.95; context=256K
- harness: Claude Code
- source: [https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)

研究备注：
- 官方模型卡给出精确模型分数 22：Claude Code harness、temperature=1.0、top_p=0.95、256K context，五次运行平均；未写 benchmark 版本或 metric。当前官方 v1.1 榜单未列该模型。源分已保留，但不映射为 v1.1 pass@1。

尚未解决的问题：
- 需要确认 22 分对应 DeepSWE v1.1 及其 pass@1 指标。

最近核验时间：2026-11-04T16:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 59.6
- variant: mean of 5 runs; temperature=1.0; top_p=0.95; context=256K; network disabled; git history removed
- harness: OpenHands
- source: [https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [Scale SWE-bench Pro 官方数据集与榜单](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- 官方模型卡给出 SWE-bench Pro 59.6：OpenHands harness、temperature=1.0、top_p=0.95、256K context，五次运行平均；网络关闭、移除 git 历史。卡片未写数据集版本或 metric，Scale 当前 V2 榜单未找到精确模型，故保留原分但不映射到 V2。

尚未解决的问题：
- 需确认 59.6 是否来自 SWE-bench Pro V2 默认 642 项配置，以及其 task resolution rate metric。

最近核验时间：2026-11-04T16:58+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [Vals Terminal-Bench 4 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Terminal-Bench 4 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 模型卡只列 Terminal-Bench 2.1：Terminus-2 为 67.8、Claude Code 为 68.5；Vals v4 榜单未列该模型。2.1 结果不映射到 v4。

最近核验时间：2026-11-04T16:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [Vals Terminal-Bench Science 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench Science 页面](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 模型卡、Vals 榜单及 Artificial Analysis 页面未找到该模型的 Terminal-Bench Science v0.1 成绩。

最近核验时间：2026-11-04T16:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)

研究备注：
- 官方模型卡和 Zapier 官方榜单均未找到 AutomationBench v1.0.6 成绩。第三方页面的 AutomationBench partial credit 58.0 与官方 benchmark/metric 不同，不作为目标成绩收录。

最近核验时间：2026-11-04T16:58+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2.1 官方发布数据](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)

研究备注：
- 官方 v2.1 发布数据和模型卡未找到该模型的成绩。

最近核验时间：2026-11-04T16:58+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography)
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)

研究备注：
- 官方 Chartography 排行榜和模型卡未找到该模型的成绩。

最近核验时间：2026-11-04T16:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 25.6
- metric: accuracy
- variant: no tools; mean of 5 runs; Claude 4.6 Opus judge
- source: [https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 33.4
- metric: accuracy
- variant: with tools; mean of 5 runs; Claude 4.6 Opus judge
- source: [https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- [Humanity’s Last Exam 官方定义与准确率指标](https://lastexam.ai/)

研究备注：
- 模型卡精确列出 no-tools 25.6、with-tools 33.4；所有 Ornith 1.5 成绩均为五次独立运行平均，HLE 使用 Claude 4.6 Opus judge。HLE 官方定义以 accuracy 为指标；模型卡未注明题数、数据集修订或测评日期，故不填这些字段。

最近核验时间：2026-11-04T16:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index 官方榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)

研究备注：
- 官方 V5.0.1 榜单和模型卡未找到该模型的综合指数成绩。

最近核验时间：2026-11-04T16:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)

研究备注：
- 官方 GDPval-AA v2.1 榜单和模型卡未找到该模型成绩。

最近核验时间：2026-11-04T16:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)
- [Ornith 官方模型卡](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)

研究备注：
- Vals Index v2.2 官方榜单未列该模型；未将其他 Ornith 尺寸或家族模型成绩映射过来。

最近核验时间：2026-11-04T16:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index 官方榜单",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        }
      ],
      "notes": [
        "官方 V5.0.1 榜单和模型卡未找到该模型的综合指数成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        },
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "官方模型卡和 Zapier 官方榜单均未找到 AutomationBench v1.0.6 成绩。第三方页面的 AutomationBench partial credit 58.0 与官方 benchmark/metric 不同，不作为目标成绩收录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        }
      ],
      "notes": [
        "官方 Chartography 排行榜和模型卡未找到该模型的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        },
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "官方模型卡给出精确模型分数 22：Claude Code harness、temperature=1.0、top_p=0.95、256K context，五次运行平均；未写 benchmark 版本或 metric。当前官方 v1.1 榜单未列该模型。源分已保留，但不映射为 v1.1 pass@1。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要确认 22 分对应 DeepSWE v1.1 及其 pass@1 指标。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA 官方榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        }
      ],
      "notes": [
        "官方 GDPval-AA v2.1 榜单和模型卡未找到该模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        },
        {
          "label": "Humanity’s Last Exam 官方定义与准确率指标",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "模型卡精确列出 no-tools 25.6、with-tools 33.4；所有 Ornith 1.5 成绩均为五次独立运行平均，HLE 使用 Claude 4.6 Opus judge。HLE 官方定义以 accuracy 为指标；模型卡未注明题数、数据集修订或测评日期，故不填这些字段。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 官方发布数据",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        }
      ],
      "notes": [
        "官方 v2.1 发布数据和模型卡未找到该模型的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        },
        {
          "label": "Scale SWE-bench Pro 官方数据集与榜单",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "官方模型卡给出 SWE-bench Pro 59.6：OpenHands harness、temperature=1.0、top_p=0.95、256K context，五次运行平均；网络关闭、移除 git 历史。卡片未写数据集版本或 metric，Scale 当前 V2 榜单未找到精确模型，故保留原分但不映射到 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 59.6 是否来自 SWE-bench Pro V2 默认 642 项配置，以及其 task resolution rate metric。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        },
        {
          "label": "Vals Terminal-Bench Science 官方榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 页面",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "模型卡、Vals 榜单及 Artificial Analysis 页面未找到该模型的 Terminal-Bench Science v0.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        },
        {
          "label": "Vals Terminal-Bench 4 官方榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Terminal-Bench 4 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "模型卡只列 Terminal-Bench 2.1：Terminus-2 为 67.8、Claude Code 为 68.5；Vals v4 榜单未列该模型。2.1 结果不映射到 v4。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T16:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Ornith 官方模型卡",
          "url": "https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B"
        }
      ],
      "notes": [
        "Vals Index v2.2 官方榜单未列该模型；未将其他 Ornith 尺寸或家族模型成绩映射过来。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T16:58+08:00",
  "model_id": "deepreinforce/ornith-1.5-35b-a3b",
  "new_records": 4,
  "overall_status": "待复核"
}

-->
