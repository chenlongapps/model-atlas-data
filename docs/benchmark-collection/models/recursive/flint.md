# Flint Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：recursive/flint
- 模型名称：Flint
- 发布日期：2026-10-21
- 最近检查时间：2026-11-04T01:57+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE 官方 v1.1 榜单](https://deepswe.datacurve.ai/), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint) | 2026-11-04T01:57+08:00 |
| swe-bench-pro-v2 | 已收录 | 89.7 (metric=task resolution rate; version=2.0.0; variant=Average pass@1 over at least 5 attempts; no internet access; timeout up to 5 hours; temperature 1.0; top-p 0.95; top-k 20; harness=mini-swe-agent) | [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint), [Scale AI SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T01:57+08:00 |
| terminal-bench-v4 | 未找到 | — | [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint), [Terminal-Bench 4.0 榜单](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [Terminal-Bench 官方发布页](https://github.com/harbor-framework/terminal-bench/releases) | 2026-11-04T01:57+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint), [Terminal-Bench-Science v0.1 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval) | 2026-11-04T01:57+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint) | 2026-11-04T01:57+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 官方网站](https://osworld-v2.xlang.ai/), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint) | 2026-11-04T01:57+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方任务仓库](https://github.com/surge-ai/chartography), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint) | 2026-11-04T01:57+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint) | 2026-11-04T01:57+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index v5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Intelligence Index v5.0 发布说明](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5), [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models) | 2026-11-04T01:57+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint) | 2026-11-04T01:57+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index), [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint), [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint) | 2026-11-04T01:57+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE 官方 v1.1 榜单](https://deepswe.datacurve.ai/)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)

研究备注：
- 已查官方 v1.1 榜单及 Flint 官方发布资料，未找到该精确模型的可核实分数。榜单显示 113 个任务、更新时间 2026-09-22，早于 Flint 发布；因此仅记录当前资料中未找到，不推断发布后绝无成绩。

最近核验时间：2026-11-04T01:57+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 已确认成绩 1

- name: SWE-bench Pro
- score: 89.7
- metric: task resolution rate
- version: 2.0.0
- variant: Average pass@1 over at least 5 attempts; no internet access; timeout up to 5 hours; temperature 1.0; top-p 0.95; top-k 20
- harness: mini-swe-agent
- source: [https://huggingface.co/RecursiveSI/flint](https://huggingface.co/RecursiveSI/flint)

已检查的主要资料：
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)
- [Scale AI SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Recursive 官方模型卡报告 89.7%；写明 agentic 成绩为至少 5 次尝试的平均 pass@1，使用 mini-swe-agent、无网络，最长 5 小时超时；统一采样为 temperature 1.0、top-p 0.95、top-k 20。数据子集、checkpoint 精度和评测日期未说明，故省略。
- Scale 公共 V2 榜单更新时间早于 Flint 发布且未列出 Flint；这不是同一已公开配置的对照分数，不构成成绩冲突。

最近核验时间：2026-11-04T01:57+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)
- [Terminal-Bench 4.0 榜单](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [Terminal-Bench 官方发布页](https://github.com/harbor-framework/terminal-bench/releases)

研究备注：
- Flint 官方模型卡只报告 Terminal-Bench 2.1 的 54.9%；此版本与本任务定义的 4.0 不同，未迁移该分数。查过的 4.0 官方页面当前榜格为空。

最近核验时间：2026-11-04T01:57+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)
- [Terminal-Bench-Science v0.1 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval)

研究备注：
- Flint 模型卡和发布说明没有报告此项成绩。官方 Harbor leaderboard 路由可打开但内容动态加载，文本检查只显示加载中，无法确认完整模型列表；没有可核实候选分数。

尚未解决的问题：
- 官方 leaderboard 的动态结果未能从页面文本读取；后续可复查可交互榜单或源数据。

最近核验时间：2026-11-04T01:57+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)

研究备注：
- Zapier 官方榜单显示版本 1.0.6，但页面展开前 10 项并将其余 119 项折叠，无法核实 Flint 是否在完整列表中。模型发布资料也未报告 AutomationBench 分数。未把 Artificial Analysis 的 AutomationBench-AA 分数当作 Zapier 指标。

尚未解决的问题：
- 官方网页不能从当前可读表格确认折叠条目；没有找到可核实分数。

最近核验时间：2026-11-04T01:57+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 官方网站](https://osworld-v2.xlang.ai/)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)

研究备注：
- 查官方 OSWorld-V2 仓库、项目站点和 Flint 官方发布资料，均未找到 Flint 的 v2.1 成绩或 leaderboard 条目。没有推断或记录通用 benchmark 配置为 Flint 实测条件。

最近核验时间：2026-11-04T01:57+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方任务仓库](https://github.com/surge-ai/chartography)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)

研究备注：
- Chartography 标准任务将图表图片与专家问题配对；Flint 官方卡明确输入/输出均为文本，不能在标准图像输入设置下参加该评测。没有把自定义外部视觉工具配置推定为 Flint 的成绩。

最近核验时间：2026-11-04T01:57+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)

研究备注：
- 查 Flint 官方发布资料和 Scale HLE 榜单，未找到该精确模型的原始 HLE 成绩。Scale 页面当前版本更新时间为 2026-09-17，早于 Flint 发布；页面未列 Flint 只作为当前榜单状态，不据此断言发布后不存在成绩。

最近核验时间：2026-11-04T01:57+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Intelligence Index v5.0 发布说明](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)

研究备注：
- 查 AA Index v5.0 评测页、v5 发布说明及 AA 模型主榜，未找到 Flint 条目或模型专属分数。没有把 HLE-Diamond 等子评测映射成原始 HLE。

最近核验时间：2026-11-04T01:57+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)

研究备注：
- 查 AA GDPval-AA v2.1 评测页、AA 模型榜单和 Flint 官方资料，未找到 Flint 专属 Elo。220 项任务、Stirrup shell/web loop 等是基准通用描述，不作为 Flint 实测条件。

最近核验时间：2026-11-04T01:57+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)
- [Recursive Flint 模型卡](https://huggingface.co/RecursiveSI/flint)
- [Recursive Flint 发布说明](https://recursive.com/updates/introducing-recursive-flint)

研究备注：
- 查 Vals Index v2.2 官方榜单及 Flint 官方资料，未找到 Flint 成绩或模型页。官方榜单注明 v2.2，更新于 2026-10-30。

最近核验时间：2026-11-04T01:57+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5.0",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5.0 发布说明",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        },
        {
          "label": "Artificial Analysis 模型榜单",
          "url": "https://artificialanalysis.ai/leaderboards/models"
        }
      ],
      "notes": [
        "查 AA Index v5.0 评测页、v5 发布说明及 AA 模型主榜，未找到 Flint 条目或模型专属分数。没有把 HLE-Diamond 等子评测映射成原始 HLE。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        }
      ],
      "notes": [
        "Zapier 官方榜单显示版本 1.0.6，但页面展开前 10 项并将其余 119 项折叠，无法核实 Flint 是否在完整列表中。模型发布资料也未报告 AutomationBench 分数。未把 Artificial Analysis 的 AutomationBench-AA 分数当作 Zapier 指标。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方网页不能从当前可读表格确认折叠条目；没有找到可核实分数。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方任务仓库",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        }
      ],
      "notes": [
        "Chartography 标准任务将图表图片与专家问题配对；Flint 官方卡明确输入/输出均为文本，不能在标准图像输入设置下参加该评测。没有把自定义外部视觉工具配置推定为 Flint 的成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方 v1.1 榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        }
      ],
      "notes": [
        "已查官方 v1.1 榜单及 Flint 官方发布资料，未找到该精确模型的可核实分数。榜单显示 113 个任务、更新时间 2026-09-22，早于 Flint 发布；因此仅记录当前资料中未找到，不推断发布后绝无成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis 模型榜单",
          "url": "https://artificialanalysis.ai/leaderboards/models"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        }
      ],
      "notes": [
        "查 AA GDPval-AA v2.1 评测页、AA 模型榜单和 Flint 官方资料，未找到 Flint 专属 Elo。220 项任务、Stirrup shell/web loop 等是基准通用描述，不作为 Flint 实测条件。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Scale AI Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        }
      ],
      "notes": [
        "查 Flint 官方发布资料和 Scale HLE 榜单，未找到该精确模型的原始 HLE 成绩。Scale 页面当前版本更新时间为 2026-09-17，早于 Flint 发布；页面未列 Flint 只作为当前榜单状态，不据此断言发布后不存在成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 官方网站",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        }
      ],
      "notes": [
        "查官方 OSWorld-V2 仓库、项目站点和 Flint 官方发布资料，均未找到 Flint 的 v2.1 成绩或 leaderboard 条目。没有推断或记录通用 benchmark 配置为 Flint 实测条件。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Recursive 官方模型卡报告 89.7%；写明 agentic 成绩为至少 5 次尝试的平均 pass@1，使用 mini-swe-agent、无网络，最长 5 小时超时；统一采样为 temperature 1.0、top-p 0.95、top-k 20。数据子集、checkpoint 精度和评测日期未说明，故省略。",
        "Scale 公共 V2 榜单更新时间早于 Flint 发布且未列出 Flint；这不是同一已公开配置的对照分数，不构成成绩冲突。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        },
        {
          "label": "Terminal-Bench-Science v0.1 leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval"
        }
      ],
      "notes": [
        "Flint 模型卡和发布说明没有报告此项成绩。官方 Harbor leaderboard 路由可打开但内容动态加载，文本检查只显示加载中，无法确认完整模型列表；没有可核实候选分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 leaderboard 的动态结果未能从页面文本读取；后续可复查可交互榜单或源数据。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        },
        {
          "label": "Terminal-Bench 4.0 榜单",
          "url": "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
        },
        {
          "label": "Terminal-Bench 官方发布页",
          "url": "https://github.com/harbor-framework/terminal-bench/releases"
        }
      ],
      "notes": [
        "Flint 官方模型卡只报告 Terminal-Bench 2.1 的 54.9%；此版本与本任务定义的 4.0 不同，未迁移该分数。查过的 4.0 官方页面当前榜格为空。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T01:57+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Recursive Flint 模型卡",
          "url": "https://huggingface.co/RecursiveSI/flint"
        },
        {
          "label": "Recursive Flint 发布说明",
          "url": "https://recursive.com/updates/introducing-recursive-flint"
        }
      ],
      "notes": [
        "查 Vals Index v2.2 官方榜单及 Flint 官方资料，未找到 Flint 成绩或模型页。官方榜单注明 v2.2，更新于 2026-10-30。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T01:57+08:00",
  "model_id": "recursive/flint",
  "new_records": 1,
  "overall_status": "待复核"
}

-->
