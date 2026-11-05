# Grok 4.20 (Reasoning) Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-4.20-0309-reasoning
- 模型名称：Grok 4.20 (Reasoning)
- 发布日期：2026-03-09
- 最近检查时间：2026-11-05T11:57+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 与后续 `Grok 4.20 0309 v2` 分开核查；未将后续 v2 的成绩并入。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE live leaderboard JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench versions](https://www.tbench.ai/benchmarks), [Terminal-Bench leaderboard](https://www.tbench.ai/leaderboard), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science announcement](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld official project](https://osworld-v2.xlang.ai/), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| chartography | 待核实 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography repository](https://github.com/surge-ai/chartography), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| humanitys-last-exam | 已收录 | 32 (metric=accuracy; dataset=Original HLE set (2,500 questions)) | [AA comparison: Grok 4.20 0309 Reasoning vs Grok 4](https://artificialanalysis.ai/models/comparisons/grok-4-20-0309-vs-grok-4), [Artificial Analysis Humanity’s Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Grok 4.20 0309 Reasoning profile](https://artificialanalysis.ai/models/grok-4-20-0309), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis Grok 4.20 0309 Reasoning profile](https://artificialanalysis.ai/models/grok-4-20-0309), [AA comparison: GPT-5.5 vs Grok 4.20 0309 Reasoning](https://artificialanalysis.ai/models/comparisons/gpt-5-5-non-reasoning-vs-grok-4-20-0309), [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index V2 historical page](https://www.vals.ai/benchmarks/vals_index_v2), [Vals Grok 4.20 Reasoning model profile](https://www.vals.ai/models/grok_grok-4.20-0309-reasoning), [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning) | 2026-11-05T11:57+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE live leaderboard JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- 当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。

尚未解决的问题：
- 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。

最近核验时间：2026-11-05T11:57+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- 当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。

尚未解决的问题：
- 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。

最近核验时间：2026-11-05T11:57+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench versions](https://www.tbench.ai/benchmarks)
- [Terminal-Bench leaderboard](https://www.tbench.ai/leaderboard)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- 当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。

尚未解决的问题：
- 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。

最近核验时间：2026-11-05T11:57+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science announcement](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- 当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。

尚未解决的问题：
- 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。

最近核验时间：2026-11-05T11:57+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- Zapier v1.0.6 页面只展开部分行，其余条目折叠；本次无法确认精确变体。

尚未解决的问题：
- 需确认完整 held-out 官方榜单中的精确模型行。

最近核验时间：2026-11-05T11:57+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld official project](https://osworld-v2.xlang.ai/)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- 型号支持图像输入与函数调用，适用 OSWorld；未确认精确 0309 变体的 v2.1 分数。

尚未解决的问题：
- 当前动态榜单未能确认精确模型行。

最近核验时间：2026-11-05T11:57+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography repository](https://github.com/surge-ai/chartography)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- 型号支持图像输入和文本输出；Surge 榜单当前可检索行未见该精确变体。

尚未解决的问题：
- 动态榜单未显示完整历史，缺席不足以判定未找到。

最近核验时间：2026-11-05T11:57+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 32
- metric: accuracy
- dataset: Original HLE set (2,500 questions)
- source: [https://artificialanalysis.ai/models/comparisons/grok-4-20-0309-vs-grok-4](https://artificialanalysis.ai/models/comparisons/grok-4-20-0309-vs-grok-4)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [AA comparison: Grok 4.20 0309 Reasoning vs Grok 4](https://artificialanalysis.ai/models/comparisons/grok-4-20-0309-vs-grok-4)
- [Artificial Analysis Humanity’s Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- AA 原始比较表将精确型号列为 Grok 4.20 0309 (Reasoning)，HLE accuracy 32%；HLE 来源说明原始集合共 2,500 题。未公布 slice、工具条件、effort、harness 或评测日期，未填写这些字段。

最近核验时间：2026-11-05T11:57+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Grok 4.20 0309 Reasoning profile](https://artificialanalysis.ai/models/grok-4-20-0309)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- AA 精确模型页当前显示 Index N/A；可见历史指数属于 v4.3.2（reasoning 25* / non-reasoning 15* 估值），不能映射到 V5.0.1。

尚未解决的问题：
- 需确认精确模型是否有 V5.0.1 结果；V5 采用 HLE-Diamond，和原始 HLE 不同。

最近核验时间：2026-11-05T11:57+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Grok 4.20 0309 Reasoning profile](https://artificialanalysis.ai/models/grok-4-20-0309)
- [AA comparison: GPT-5.5 vs Grok 4.20 0309 Reasoning](https://artificialanalysis.ai/models/comparisons/gpt-5-5-non-reasoning-vs-grok-4-20-0309)
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- AA 页面列出 GDPval-AA v2.1 evaluation，但精确模型成绩单元为空；空白不足以证明没有成绩，未迁移其它版本或型号结果。

尚未解决的问题：
- 尚未取得该精确模型在 GDPval-AA v2.1 上可核实的分数。

最近核验时间：2026-11-05T11:57+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index V2 historical page](https://www.vals.ai/benchmarks/vals_index_v2)
- [Vals Grok 4.20 Reasoning model profile](https://www.vals.ai/models/grok_grok-4.20-0309-reasoning)
- [xAI Grok 4.20 0309 Reasoning model documentation](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning)

研究备注：
- Vals v2.2 当前榜单每家实验室只展示最佳型号（SpaceXAI 为 Grok 4.7）；可见的 Grok 4.20 历史值属于旧 V2 或条件无法对应的模型页，不能映射到 v2.2。

尚未解决的问题：
- 需取得与本地精确变体及 Vals Index v2.2 完全对应的结果。

最近核验时间：2026-11-05T11:57+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.20 0309 Reasoning profile",
          "url": "https://artificialanalysis.ai/models/grok-4-20-0309"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "AA 精确模型页当前显示 Index N/A；可见历史指数属于 v4.3.2（reasoning 25* / non-reasoning 15* 估值），不能映射到 V5.0.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认精确模型是否有 V5.0.1 结果；V5 采用 HLE-Diamond，和原始 HLE 不同。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "Zapier v1.0.6 页面只展开部分行，其余条目折叠；本次无法确认精确变体。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认完整 held-out 官方榜单中的精确模型行。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "型号支持图像输入和文本输出；Surge 榜单当前可检索行未见该精确变体。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单未显示完整历史，缺席不足以判定未找到。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE live leaderboard JSON",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.20 0309 Reasoning profile",
          "url": "https://artificialanalysis.ai/models/grok-4-20-0309"
        },
        {
          "label": "AA comparison: GPT-5.5 vs Grok 4.20 0309 Reasoning",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-5-non-reasoning-vs-grok-4-20-0309"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "AA 页面列出 GDPval-AA v2.1 evaluation，但精确模型成绩单元为空；空白不足以证明没有成绩，未迁移其它版本或型号结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "尚未取得该精确模型在 GDPval-AA v2.1 上可核实的分数。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "AA comparison: Grok 4.20 0309 Reasoning vs Grok 4",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-20-0309-vs-grok-4"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "AA 原始比较表将精确型号列为 Grok 4.20 0309 (Reasoning)，HLE accuracy 32%；HLE 来源说明原始集合共 2,500 题。未公布 slice、工具条件、effort、harness 或评测日期，未填写这些字段。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "OSWorld official project",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "型号支持图像输入与函数调用，适用 OSWorld；未确认精确 0309 变体的 v2.1 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前动态榜单未能确认精确模型行。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench Science Harbor leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Terminal-Bench leaderboard",
          "url": "https://www.tbench.ai/leaderboard"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "当前公开榜单视图未能确认本地精确 0309 变体的目标版本成绩；Grok 4.6 与后续 0309 v2 均不是该精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index V2 historical page",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        },
        {
          "label": "Vals Grok 4.20 Reasoning model profile",
          "url": "https://www.vals.ai/models/grok_grok-4.20-0309-reasoning"
        },
        {
          "label": "xAI Grok 4.20 0309 Reasoning model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.20-0309-reasoning"
        }
      ],
      "notes": [
        "Vals v2.2 当前榜单每家实验室只展示最佳型号（SpaceXAI 为 Grok 4.7）；可见的 Grok 4.20 历史值属于旧 V2 或条件无法对应的模型页，不能映射到 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "需取得与本地精确变体及 Vals Index v2.2 完全对应的结果。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:57+08:00",
  "model_id": "xai/grok-4.20-0309-reasoning",
  "model_notes": [
    "与后续 `Grok 4.20 0309 v2` 分开核查；未将后续 v2 的成绩并入。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
