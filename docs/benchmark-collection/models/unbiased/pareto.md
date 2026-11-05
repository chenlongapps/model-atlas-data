# Pareto Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：unbiased/pareto
- 模型名称：Pareto
- 发布日期：2026-09-17
- 最近检查时间：2026-11-04T10:17+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 70.0 (metric=score (%); version=1.1; dataset=30-task slice; not the full 113-task v1.1 set; variant=Pareto 26.9; preliminary Unbiased run); 69.9 (metric=score (%); version=1.1; dataset=task denominator not reported; variant=Pareto 26.10 preview; preliminary October 1 run) | [Unbiased official model card](https://unbiased.ai/model-card/), [Unbiased Pareto 26.10 preview announcement](https://unbiased.ai/blog/pareto-26-10-preview/), [DeepSWE v1.1 official leaderboard and method](https://deepswe.datacurve.ai/), [Unbiased release alias changelog](https://unbiased.ai/changelog/) | 2026-11-04T10:17+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Unbiased Pareto 26.9 / 26.10 published score tables](https://unbiased.ai/model-card/), [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/), [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T10:17+08:00 |
| terminal-bench-v4 | 已收录 | 50.8 (metric=task resolution rate; version=4.0.0; variant=Pareto 26.10 preview; preliminary October 1 run) | [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/), [Unbiased release alias changelog](https://unbiased.ai/changelog/), [Terminal-Bench 4.0 official specification](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T10:17+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Unbiased official model card](https://unbiased.ai/model-card/), [Terminal-Bench Science v0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1), [Official Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval) | 2026-11-04T10:17+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench v1.0.6 official leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Unbiased official model card](https://unbiased.ai/model-card/) | 2026-11-04T10:17+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld official site](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [Unbiased official model card](https://unbiased.ai/model-card/) | 2026-11-04T10:17+08:00 |
| chartography | 未找到 | — | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Unbiased official model card](https://unbiased.ai/model-card/), [Chartography paper](https://arxiv.org/abs/2608.10677) | 2026-11-04T10:17+08:00 |
| humanitys-last-exam | 已收录 | 49.9 (metric=accuracy; version=unspecified; dataset=HLE text-only; item count not reported; variant=Pareto 26.10 preview; preliminary October 1 run) | [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/), [Unbiased official model card](https://unbiased.ai/model-card/), [Original Humanity's Last Exam benchmark](https://lastexam.ai/), [Original HLE paper](https://arxiv.org/abs/2501.14249) | 2026-11-04T10:17+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Intelligence Index v5.0.1 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis model listing](https://artificialanalysis.ai/models/), [Unbiased official model card](https://unbiased.ai/model-card/) | 2026-11-04T10:17+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Unbiased official model card](https://unbiased.ai/model-card/), [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/) | 2026-11-04T10:17+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Unbiased official model card](https://unbiased.ai/model-card/) | 2026-11-04T10:17+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 70.0
- metric: score (%)
- version: 1.1
- dataset: 30-task slice; not the full 113-task v1.1 set
- variant: Pareto 26.9; preliminary Unbiased run
- source: [https://unbiased.ai/model-card/](https://unbiased.ai/model-card/)
- date: 2026-09-20
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 69.9
- metric: score (%)
- version: 1.1
- dataset: task denominator not reported
- variant: Pareto 26.10 preview; preliminary October 1 run
- source: [https://unbiased.ai/blog/pareto-26-10-preview/](https://unbiased.ai/blog/pareto-26-10-preview/)
- date: 2026-10-01
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Unbiased official model card](https://unbiased.ai/model-card/)
- [Unbiased Pareto 26.10 preview announcement](https://unbiased.ai/blog/pareto-26-10-preview/)
- [DeepSWE v1.1 official leaderboard and method](https://deepswe.datacurve.ai/)
- [Unbiased release alias changelog](https://unbiased.ai/changelog/)

研究备注：
- Unbiased 直接列出 Pareto 26.9 = 70.0%（2026-09-20）与 Pareto 26.10 preview = 69.9%（2026-10-01）；两行已在 TOML 中分别保存，没有挑选最高分或合并条件。官方说明 26.9 使用 30-task slice，不是完整 113-task v1.1 集；26.10 分母仍待确认。
- 官方变更日志说明当前 `pareto` API alias 于 10 月 15 日切到 26.10，26.9 仍可固定调用。TOML 的模型发布日期是 9 月 17 日，因此行内 variant 保留各自版本，避免把两版混写。来源只将分数标为 score (%) / percent correct，没有明确写本地定义使用的 pass@1；harness 和 effort 未披露。

尚未解决的问题：
- 本地定义要求 pass@1；官方分数表未明确该 metric，且 26.9 是 30-task slice、26.10 denominator 未确认。两条原始分数已保留，但定义映射待复核。

最近核验时间：2026-11-04T10:17+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Unbiased Pareto 26.9 / 26.10 published score tables](https://unbiased.ai/model-card/)
- [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/)
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 已检查 Pareto 两个版本公布的 benchmark 清单和 Scale V2 页面；没有找到 Pareto 的 SWE-bench Pro V2 精确成绩。没有从其他 SWE-bench Pro 版本或底层模型推断分数。

最近核验时间：2026-11-04T10:17+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 50.8
- metric: task resolution rate
- version: 4.0.0
- variant: Pareto 26.10 preview; preliminary October 1 run
- source: [https://unbiased.ai/blog/pareto-26-10-preview/](https://unbiased.ai/blog/pareto-26-10-preview/)
- date: 2026-10-01
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/)
- [Unbiased release alias changelog](https://unbiased.ai/changelog/)
- [Terminal-Bench 4.0 official specification](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Unbiased 报告 Pareto 26.10 preview 于 2026-10-01 的 Terminal-Bench 4.0 成绩为 50.8%，并说明为 preliminary run；该行以版本与变体单独记录。报告未说明 harness、effort 或其他测试条件。日期记录为来源明确给出的实际 run date，不是发布日期。

最近核验时间：2026-11-04T10:17+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Unbiased official model card](https://unbiased.ai/model-card/)
- [Terminal-Bench Science v0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Official Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval)

研究备注：
- Pareto 26.9 与 26.10 官方成绩清单未列出 Terminal-Bench-Science 结果。官方 Harbor leaderboard 页面未加载完整。

尚未解决的问题：
- 动态 leaderboard 未加载，尚不能确认是否存在精确 Pareto 版本成绩。

最近核验时间：2026-11-04T10:17+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench v1.0.6 official leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Unbiased official model card](https://unbiased.ai/model-card/)

研究备注：
- Zapier 官方页明确显示版本 1.0.6，但只展开前 10 条并提示另有 119 条；已展示内容没有 Pareto。Unbiased 两版公开成绩表未列 AutomationBench。模型本身支持 tool calling，故该项适用。

尚未解决的问题：
- 榜单其余 119 条当前未展开，无法据此断言完整排行榜中没有 Pareto。

最近核验时间：2026-11-04T10:17+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld official site](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [Unbiased official model card](https://unbiased.ai/model-card/)

研究备注：
- 已检查的官方 OSWorld 页面和仓库使用 OSWorld 2.0 标题；未找到 Pareto 精确结果。

尚未解决的问题：
- 本地目标定义是 OSWorld v2.1；没有可确认的 v2.1 成绩，不能将 v2.0 或 partial reward 结果映射到该定义。

最近核验时间：2026-11-04T10:17+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Unbiased official model card](https://unbiased.ai/model-card/)
- [Chartography paper](https://arxiv.org/abs/2608.10677)

研究备注：
- Surge 官方榜单没有 Pareto 精确条目，Unbiased 公布的 benchmark 表也未列 Chartography。Pareto 接受图像输入，测试适用；不使用其他基础模型成绩。

最近核验时间：2026-11-04T10:17+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 49.9
- metric: accuracy
- version: unspecified
- dataset: HLE text-only; item count not reported
- variant: Pareto 26.10 preview; preliminary October 1 run
- source: [https://unbiased.ai/blog/pareto-26-10-preview/](https://unbiased.ai/blog/pareto-26-10-preview/)
- date: 2026-10-01
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/)
- [Unbiased official model card](https://unbiased.ai/model-card/)
- [Original Humanity's Last Exam benchmark](https://lastexam.ai/)
- [Original HLE paper](https://arxiv.org/abs/2501.14249)

研究备注：
- Unbiased 报告 Pareto 26.10 preview 于 2026-10-01 的 HLE text-only 成绩为 49.9%，并说明 score 为 percent correct；已作为独立数据集条件记录。题目数量、effort、tool setting 与 harness 未披露，因此不声称覆盖完整 2,500 题。该项是 HLE，不是 HLE-Diamond。

最近核验时间：2026-11-04T10:17+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5.0.1 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis model listing](https://artificialanalysis.ai/models/)
- [Unbiased official model card](https://unbiased.ai/model-card/)

研究备注：
- AA v5 官方页面当前展示部分模型；目前没有精确 Pareto 条目。Unbiased 的 Pareto 公开结果表没有列 AA Index 分数。未使用 Pareto 组成模型或其他测试的结果推算指数。

尚未解决的问题：
- AA 页面仅显示部分模型，当前未命中精确型号不足以确认公开榜单中完全没有结果。

最近核验时间：2026-11-04T10:17+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Unbiased official model card](https://unbiased.ai/model-card/)
- [Unbiased Pareto 26.10 launch notes](https://unbiased.ai/blog/pareto-26-10-preview/)

研究备注：
- AA 当前页面返回的 leaderboard 是部分结果，未出现 Pareto；Unbiased 26.9 与 26.10 公布清单都未列 GDPval-AA。未移用底层模型分数。

尚未解决的问题：
- AA leaderboard 为动态部分列表，需后续复核是否存在未显示的精确型号结果。

最近核验时间：2026-11-04T10:17+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Unbiased official model card](https://unbiased.ai/model-card/)

研究备注：
- Vals v2.2 榜单当前显示的模型中没有 Pareto，Unbiased 公布成绩清单也未列 Vals Index。未移用任何组成模型成绩。

最近核验时间：2026-11-04T10:17+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1 page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis model listing",
          "url": "https://artificialanalysis.ai/models/"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        }
      ],
      "notes": [
        "AA v5 官方页面当前展示部分模型；目前没有精确 Pareto 条目。Unbiased 的 Pareto 公开结果表没有列 AA Index 分数。未使用 Pareto 组成模型或其他测试的结果推算指数。"
      ],
      "status": "待核实",
      "unresolved": [
        "AA 页面仅显示部分模型，当前未命中精确型号不足以确认公开榜单中完全没有结果。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench v1.0.6 official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        }
      ],
      "notes": [
        "Zapier 官方页明确显示版本 1.0.6，但只展开前 10 条并提示另有 119 条；已展示内容没有 Pareto。Unbiased 两版公开成绩表未列 AutomationBench。模型本身支持 tool calling，故该项适用。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单其余 119 条当前未展开，无法据此断言完整排行榜中没有 Pareto。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/abs/2608.10677"
        }
      ],
      "notes": [
        "Surge 官方榜单没有 Pareto 精确条目，Unbiased 公布的 benchmark 表也未列 Chartography。Pareto 接受图像输入，测试适用；不使用其他基础模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        },
        {
          "label": "Unbiased Pareto 26.10 preview announcement",
          "url": "https://unbiased.ai/blog/pareto-26-10-preview/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard and method",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Unbiased release alias changelog",
          "url": "https://unbiased.ai/changelog/"
        }
      ],
      "notes": [
        "Unbiased 直接列出 Pareto 26.9 = 70.0%（2026-09-20）与 Pareto 26.10 preview = 69.9%（2026-10-01）；两行已在 TOML 中分别保存，没有挑选最高分或合并条件。官方说明 26.9 使用 30-task slice，不是完整 113-task v1.1 集；26.10 分母仍待确认。",
        "官方变更日志说明当前 `pareto` API alias 于 10 月 15 日切到 26.10，26.9 仍可固定调用。TOML 的模型发布日期是 9 月 17 日，因此行内 variant 保留各自版本，避免把两版混写。来源只将分数标为 score (%) / percent correct，没有明确写本地定义使用的 pass@1；harness 和 effort 未披露。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义要求 pass@1；官方分数表未明确该 metric，且 26.9 是 30-task slice、26.10 denominator 未确认。两条原始分数已保留，但定义映射待复核。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        },
        {
          "label": "Unbiased Pareto 26.10 launch notes",
          "url": "https://unbiased.ai/blog/pareto-26-10-preview/"
        }
      ],
      "notes": [
        "AA 当前页面返回的 leaderboard 是部分结果，未出现 Pareto；Unbiased 26.9 与 26.10 公布清单都未列 GDPval-AA。未移用底层模型分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "AA leaderboard 为动态部分列表，需后续复核是否存在未显示的精确型号结果。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Unbiased Pareto 26.10 launch notes",
          "url": "https://unbiased.ai/blog/pareto-26-10-preview/"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        },
        {
          "label": "Original Humanity's Last Exam benchmark",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "Original HLE paper",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "Unbiased 报告 Pareto 26.10 preview 于 2026-10-01 的 HLE text-only 成绩为 49.9%，并说明 score 为 percent correct；已作为独立数据集条件记录。题目数量、effort、tool setting 与 harness 未披露，因此不声称覆盖完整 2,500 题。该项是 HLE，不是 HLE-Diamond。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "OSWorld official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        }
      ],
      "notes": [
        "已检查的官方 OSWorld 页面和仓库使用 OSWorld 2.0 标题；未找到 Pareto 精确结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地目标定义是 OSWorld v2.1；没有可确认的 v2.1 成绩，不能将 v2.0 或 partial reward 结果映射到该定义。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Unbiased Pareto 26.9 / 26.10 published score tables",
          "url": "https://unbiased.ai/model-card/"
        },
        {
          "label": "Unbiased Pareto 26.10 launch notes",
          "url": "https://unbiased.ai/blog/pareto-26-10-preview/"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "已检查 Pareto 两个版本公布的 benchmark 清单和 Scale V2 页面；没有找到 Pareto 的 SWE-bench Pro V2 精确成绩。没有从其他 SWE-bench Pro 版本或底层模型推断分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        },
        {
          "label": "Terminal-Bench Science v0.1 official announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Official Harbor leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval"
        }
      ],
      "notes": [
        "Pareto 26.9 与 26.10 官方成绩清单未列出 Terminal-Bench-Science 结果。官方 Harbor leaderboard 页面未加载完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态 leaderboard 未加载，尚不能确认是否存在精确 Pareto 版本成绩。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Unbiased Pareto 26.10 launch notes",
          "url": "https://unbiased.ai/blog/pareto-26-10-preview/"
        },
        {
          "label": "Unbiased release alias changelog",
          "url": "https://unbiased.ai/changelog/"
        },
        {
          "label": "Terminal-Bench 4.0 official specification",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Unbiased 报告 Pareto 26.10 preview 于 2026-10-01 的 Terminal-Bench 4.0 成绩为 50.8%，并说明为 preliminary run；该行以版本与变体单独记录。报告未说明 harness、effort 或其他测试条件。日期记录为来源明确给出的实际 run date，不是发布日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T10:17+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Unbiased official model card",
          "url": "https://unbiased.ai/model-card/"
        }
      ],
      "notes": [
        "Vals v2.2 榜单当前显示的模型中没有 Pareto，Unbiased 公布成绩清单也未列 Vals Index。未移用任何组成模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T10:17+08:00",
  "model_id": "unbiased/pareto",
  "new_records": 4,
  "overall_status": "待复核"
}

-->
