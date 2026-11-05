# Inkling Small Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：thinkingmachines/inkling-small
- 模型名称：Inkling Small
- 发布日期：2026-07-30
- 最近检查时间：2026-11-04T21:39+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- 准确型号依据 Thinking Machines 2026-07-30 的 Inkling-Small 正式发布和对应模型卡；只采用正式发布成绩，不并入更早 preview checkpoint 的分数。
- 本轮新增六条原始成绩：Terminal-Bench 4.0、Chartography、两种 HLE 配置、Artificial Analysis Intelligence Index v5.0.1、Vals Index 2.2。Terminal-Bench 指标和 AA Index 版本与本地定义不一致，保留来源原指标/版本并待复核。
- 不把官方发布的 SWE-bench Pro Public、Terminal-Bench 2.1 或 GDPval-AA v2 成绩映射到目标中的不同版本。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/) | 2026-11-04T21:39+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/) | 2026-11-04T21:39+08:00 |
| terminal-bench-v4 | 待核实 | 0.0 (metric=accuracy; version=4.0.0; dataset=66 tasks; variant=avg@3; per-run pass@1; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 官方榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T21:39+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals AI Terminal-Bench-Science 官方榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T21:39+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/) | 2026-11-04T21:39+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/), [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T21:39+08:00 |
| chartography | 已收录 | 9.1 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=xHigh reasoning; variant=10 runs per task; harness=Inspect AI) | [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方方法与配置](https://github.com/surge-ai/chartography) | 2026-11-04T21:39+08:00 |
| humanitys-last-exam | 已收录 | 31.6 (metric=accuracy; dataset=2,158 text-only questions; effort=0.99; variant=text-only; no tools); 47.8 (metric=accuracy; effort=0.99; variant=with tools) | [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/), [Artificial Analysis HLE 官方评测页与方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T21:39+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 13 (metric=index score; version=5.0.1) | [Artificial Analysis Inkling Small 型号页](https://artificialanalysis.ai/models/inkling-small/), [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/) | 2026-11-04T21:39+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/) | 2026-11-04T21:39+08:00 |
| vals-index-v2.2 | 已收录 | 27.59 (metric=performance score; version=2.2) | [Vals AI Vals Index 2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:39+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/)

研究备注：
- DeepSWE 官方榜单未列出 Inkling Small。发布文中的 SWE-bench Pro public 和 Terminal-Bench 2.1 均非 DeepSWE v1.1。

最近核验时间：2026-11-04T21:39+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/)

研究备注：
- V2 官方榜单未列出 Inkling Small。发布文中的 55.9% 是 SWE-bench Pro Public，发表于 V2 发布之前且未证明属于 V2，未映射到 V2。

最近核验时间：2026-11-04T21:39+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 0.0
- metric: accuracy
- version: 4.0.0
- dataset: 66 tasks
- variant: avg@3; per-run pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 官方榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 官方榜单确有 Inkling Small (Mini-SWE-agent) 的 0.00% 结果；这是实际测得的零分，不是缺失值。记录版本 4.0.0、66 tasks、avg@3（各轮 pass@1）。来源指标标签为 Accuracy，本地目标定义要求 task resolution rate；原始行已保留但不计入精确映射覆盖率。
- 模型详情页显示默认 effort 0.99，但未证实该设置专属于此评测，因此省略 effort。

尚未解决的问题：
- 需核实官方榜单的 Accuracy 是否能按本地定义映射为 task resolution rate；在确认前保留原指标。

最近核验时间：2026-11-04T21:39+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Terminal-Bench-Science 官方榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- 官方榜单未找到 Inkling Small 的准确型号成绩。

最近核验时间：2026-11-04T21:39+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/)

研究备注：
- Zapier 官方榜单未列出 Inkling Small；官方发布中的 Terminal-Bench 2.1 不是 AutomationBench。

最近核验时间：2026-11-04T21:39+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/)
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 所查 OSWorld V2 官方项目页和仓库未找到 Inkling Small 的准确型号结果。

最近核验时间：2026-11-04T21:39+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 9.1
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: xHigh reasoning
- variant: 10 runs per task
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方方法与配置](https://github.com/surge-ai/chartography)

研究备注：
- 榜单列出 Inkling Small (xHigh reasoning) 9.1%。方法为 100 tasks、每项 10 runs、Inspect AI harness、Gemini 3.5 Flash judge；指标为 accuracy (mean; Pass@1)。无该行评测日期或语义版本，故省略。

最近核验时间：2026-11-04T21:39+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 31.6
- metric: accuracy
- dataset: 2,158 text-only questions
- effort: 0.99
- variant: text-only; no tools
- source: [https://thinkingmachines.ai/news/inkling-small/](https://thinkingmachines.ai/news/inkling-small/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 47.8
- metric: accuracy
- effort: 0.99
- variant: with tools
- source: [https://thinkingmachines.ai/news/inkling-small/](https://thinkingmachines.ai/news/inkling-small/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/)
- [Artificial Analysis HLE 官方评测页与方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 正式发布成绩为 HLE text-only 31.6% 和 HLE with tools 47.8%，分别保留为独立配置；发布文说明所有评测 effort=0.99、temperature=1.0。AA 说明其可比文本子集为 2,158 道题，故仅在 text-only 行记录该 dataset。
- 更早 Inkling-Small preview 表中 29.6% / 46.6% 是预览模型成绩，未与正式发布的 31.6% / 47.8% 合并。

最近核验时间：2026-11-04T21:39+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 13
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/inkling-small/](https://artificialanalysis.ai/models/inkling-small/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Inkling Small 型号页](https://artificialanalysis.ai/models/inkling-small/)
- [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/)

研究备注：
- Artificial Analysis 当前型号页显示 Intelligence Index 得分 13，并注明当前版本 v5.0.1；模型源 TOML 保留原始版本 5.0.1。发布文中的 AA Index v4.1 40.0 不属于本目标，未迁移。

尚未解决的问题：
- 本地定义版本为 5.0，当前官方型号页版本为 5.0.1；需确认是否更新本地定义或保持版本分开，当前不计入 V5.0 精确覆盖率。

最近核验时间：2026-11-04T21:39+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Thinking Machines Inkling Small 官方发布](https://thinkingmachines.ai/news/inkling-small/)

研究备注：
- 官方发布列出 GDPval-AA v2 = 1269 Elo，属于不同版本；AA v2.1 官方评测页未找到 Inkling Small。未将 v2 分数映射到 v2.1。

最近核验时间：2026-11-04T21:39+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 27.59
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Vals Index 2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 官方 v2.2 榜单列出 Inkling Small 27.59%；指标 performance score。来源未给该模型行的 effort、harness 或评测日期，故省略。

最近核验时间：2026-11-04T21:39+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Inkling Small 型号页",
          "url": "https://artificialanalysis.ai/models/inkling-small/"
        },
        {
          "label": "Thinking Machines Inkling Small 官方发布",
          "url": "https://thinkingmachines.ai/news/inkling-small/"
        }
      ],
      "notes": [
        "Artificial Analysis 当前型号页显示 Intelligence Index 得分 13，并注明当前版本 v5.0.1；模型源 TOML 保留原始版本 5.0.1。发布文中的 AA Index v4.1 40.0 不属于本目标，未迁移。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义版本为 5.0，当前官方型号页版本为 5.0.1；需确认是否更新本地定义或保持版本分开，当前不计入 V5.0 精确覆盖率。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Thinking Machines Inkling Small 官方发布",
          "url": "https://thinkingmachines.ai/news/inkling-small/"
        }
      ],
      "notes": [
        "Zapier 官方榜单未列出 Inkling Small；官方发布中的 Terminal-Bench 2.1 不是 AutomationBench。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方方法与配置",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "榜单列出 Inkling Small (xHigh reasoning) 9.1%。方法为 100 tasks、每项 10 runs、Inspect AI harness、Gemini 3.5 Flash judge；指标为 accuracy (mean; Pass@1)。无该行评测日期或语义版本，故省略。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Thinking Machines Inkling Small 官方发布",
          "url": "https://thinkingmachines.ai/news/inkling-small/"
        }
      ],
      "notes": [
        "DeepSWE 官方榜单未列出 Inkling Small。发布文中的 SWE-bench Pro public 和 Terminal-Bench 2.1 均非 DeepSWE v1.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Thinking Machines Inkling Small 官方发布",
          "url": "https://thinkingmachines.ai/news/inkling-small/"
        }
      ],
      "notes": [
        "官方发布列出 GDPval-AA v2 = 1269 Elo，属于不同版本；AA v2.1 官方评测页未找到 Inkling Small。未将 v2 分数映射到 v2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Thinking Machines Inkling Small 官方发布",
          "url": "https://thinkingmachines.ai/news/inkling-small/"
        },
        {
          "label": "Artificial Analysis HLE 官方评测页与方法",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "正式发布成绩为 HLE text-only 31.6% 和 HLE with tools 47.8%，分别保留为独立配置；发布文说明所有评测 effort=0.99、temperature=1.0。AA 说明其可比文本子集为 2,158 道题，故仅在 text-only 行记录该 dataset。",
        "更早 Inkling-Small preview 表中 29.6% / 46.6% 是预览模型成绩，未与正式发布的 31.6% / 47.8% 合并。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "所查 OSWorld V2 官方项目页和仓库未找到 Inkling Small 的准确型号结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Thinking Machines Inkling Small 官方发布",
          "url": "https://thinkingmachines.ai/news/inkling-small/"
        }
      ],
      "notes": [
        "V2 官方榜单未列出 Inkling Small。发布文中的 55.9% 是 SWE-bench Pro Public，发表于 V2 发布之前且未证明属于 V2，未映射到 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "官方榜单未找到 Inkling Small 的准确型号成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "官方榜单确有 Inkling Small (Mini-SWE-agent) 的 0.00% 结果；这是实际测得的零分，不是缺失值。记录版本 4.0.0、66 tasks、avg@3（各轮 pass@1）。来源指标标签为 Accuracy，本地目标定义要求 task resolution rate；原始行已保留但不计入精确映射覆盖率。",
        "模型详情页显示默认 effort 0.99，但未证实该设置专属于此评测，因此省略 effort。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实官方榜单的 Accuracy 是否能按本地定义映射为 task resolution rate；在确认前保留原指标。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:39+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index 2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "官方 v2.2 榜单列出 Inkling Small 27.59%；指标 performance score。来源未给该模型行的 effort、harness 或评测日期，故省略。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:39+08:00",
  "model_id": "thinkingmachines/inkling-small",
  "model_notes": [
    "准确型号依据 Thinking Machines 2026-07-30 的 Inkling-Small 正式发布和对应模型卡；只采用正式发布成绩，不并入更早 preview checkpoint 的分数。",
    "本轮新增六条原始成绩：Terminal-Bench 4.0、Chartography、两种 HLE 配置、Artificial Analysis Intelligence Index v5.0.1、Vals Index 2.2。Terminal-Bench 指标和 AA Index 版本与本地定义不一致，保留来源原指标/版本并待复核。",
    "不把官方发布的 SWE-bench Pro Public、Terminal-Bench 2.1 或 GDPval-AA v2 成绩映射到目标中的不同版本。"
  ],
  "new_records": 6,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
