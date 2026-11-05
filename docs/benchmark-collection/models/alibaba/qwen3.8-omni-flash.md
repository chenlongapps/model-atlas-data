# Qwen3.8 Omni Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-omni-flash
- 模型名称：Qwen3.8 Omni Flash
- 发布日期：2026-09-17
- 最近检查时间：2026-11-04T10:05+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 57.8 (metric=pass@1; version=1.1; variant=temperature=1.0; top_p=0.95; context=256K; harness=Claude Code / mini-SWE-agent; highest across both, winning harness undisclosed) | [Qwen technical report, Table 2](https://arxiv.org/html/2609.25611), [DeepSWE v1.1 methodology and task count](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T10:05+08:00 |
| swe-bench-pro-v2 | 待核实 | 63.3 (variant=temperature=1.0; top_p=0.95; context=256K; problematic tasks corrected and re-evaluated on refined benchmark; benchmark version/task count not stated; harness=Claude Code) | [Qwen technical report, Table 2](https://arxiv.org/html/2609.25611), [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T10:05+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench official leaderboard](https://www.tbench.ai/), [Terminal-Bench 4.0 official announcement](https://www.tbench.ai/news/terminal-bench-4-0), [Third-party claim, excluded from data](https://trustthebench.com/benchmarks/terminal-bench) | 2026-11-04T10:05+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science v0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1), [Official Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval), [Qwen technical report](https://arxiv.org/html/2609.25611) | 2026-11-04T10:05+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks), [Qwen technical report](https://arxiv.org/html/2609.25611) | 2026-11-04T10:05+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 official site](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [Qwen technical report PDF](https://arxiv.org/pdf/2609.25611) | 2026-11-04T10:05+08:00 |
| chartography | 未找到 | — | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Qwen technical report PDF](https://arxiv.org/pdf/2609.25611) | 2026-11-04T10:05+08:00 |
| humanitys-last-exam | 已收录 | 36.5 (metric=accuracy; version=unspecified; dataset=HLE; tested item count/subset not reported; variant=GPT-4o judged) | [Qwen technical report, Table 2 and footnote](https://arxiv.org/html/2609.25611), [Original Humanity's Last Exam benchmark](https://lastexam.ai/), [Original HLE paper](https://arxiv.org/abs/2501.14249) | 2026-11-04T10:05+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis model releases](https://artificialanalysis.ai/models/releases), [Qwen technical report](https://arxiv.org/html/2609.25611) | 2026-11-04T10:05+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Qwen technical report](https://arxiv.org/html/2609.25611) | 2026-11-04T10:05+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Qwen technical report](https://arxiv.org/html/2609.25611) | 2026-11-04T10:05+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 57.8
- metric: pass@1
- version: 1.1
- variant: temperature=1.0; top_p=0.95; context=256K
- harness: Claude Code / mini-SWE-agent; highest across both, winning harness undisclosed
- source: [https://arxiv.org/html/2609.25611](https://arxiv.org/html/2609.25611)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Qwen technical report, Table 2](https://arxiv.org/html/2609.25611)
- [DeepSWE v1.1 methodology and task count](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 报告将精确型号 Qwen3.8-Omni-Flash 的 DeepSWE 1.1 结果列为 57.8；按定义的 pass@1 指标映射。报告说明该值是 Claude Code 与 mini-SWE-agent 两种 harness 中的最高值，但未披露本模型的获胜 harness；TOML 如实保留了这个条件。
- DeepSWE 官方 v1.1 页面说明该版本为 113 项任务。报告未公布实际评测日期，故未填写 date。

最近核验时间：2026-11-04T10:05+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 63.3
- variant: temperature=1.0; top_p=0.95; context=256K; problematic tasks corrected and re-evaluated on refined benchmark; benchmark version/task count not stated
- harness: Claude Code
- source: [https://arxiv.org/html/2609.25611](https://arxiv.org/html/2609.25611)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen technical report, Table 2](https://arxiv.org/html/2609.25611)
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 报告列出精确型号分数 63.3，并说明使用 Claude Code、temperature=1.0、top_p=0.95、context=256K，问题修订后在 refined benchmark 上重评。该原始记录已保留在模型 TOML，未填写未披露的 version 或 metric。

尚未解决的问题：
- 报告只写 SWE-bench Pro，没有说明对应 V2 2.0.0 / 642-task 默认集；不能映射为本地 swe-bench-pro-v2 定义。

最近核验时间：2026-11-04T10:05+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench official leaderboard](https://www.tbench.ai/)
- [Terminal-Bench 4.0 official announcement](https://www.tbench.ai/news/terminal-bench-4-0)
- [Third-party claim, excluded from data](https://trustthebench.com/benchmarks/terminal-bench)

研究备注：
- Qwen 技术报告未报告 Terminal-Bench 4。官方排行榜的动态表格未能完整读取。第三方页面的 53.9 标注日期早于本模型发布日期，且指向 TB 2.1；其来源链接失效，因此未采用。

尚未解决的问题：
- 官方动态排行榜仍需人工/后续复核以确认是否有精确型号的 v4 成绩。

最近核验时间：2026-11-04T10:05+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science v0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Official Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval)
- [Qwen technical report](https://arxiv.org/html/2609.25611)

研究备注：
- 官方公告说明 v0.1 有 70 项任务，但未列出 Qwen3.8-Omni-Flash。官方 Harbor leaderboard 页面停留在 Loading leaderboard。

尚未解决的问题：
- 排行榜未加载完整，尚不能确认该型号是否有公开结果。

最近核验时间：2026-11-04T10:05+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks)
- [Qwen technical report](https://arxiv.org/html/2609.25611)

研究备注：
- 官方排行榜显示版本 1.0.6，目前展开前 10 个结果并提示另有 119 项；已显示列表中无精确型号。Qwen 技术报告未提及 AutomationBench。

尚未解决的问题：
- 排行榜其余 119 项未展开，不能将当前页面未显示该型号视为已确认无成绩。

最近核验时间：2026-11-04T10:05+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 official site](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [Qwen technical report PDF](https://arxiv.org/pdf/2609.25611)

研究备注：
- Qwen 技术报告中未找到 OSWorld 结果。先前二手提取中出现的 2.0 数值已再次核对并撤回：官方 PDF 不含 OSWorld、19.4 或 46.7。模型具备图像输入，项目适用。

尚未解决的问题：
- 本地目标为 OSWorld 2.1；官方页面标题为 OSWorld 2.0，未找到该模型的 2.1 成绩。

最近核验时间：2026-11-04T10:05+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Qwen technical report PDF](https://arxiv.org/pdf/2609.25611)

研究备注：
- Surge 官方榜单可见其他 Qwen 型号，但没有 Qwen3.8 Omni Flash 精确条目；Qwen 技术报告未提及 Chartography。模型支持图像输入，因此该项适用。

最近核验时间：2026-11-04T10:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 36.5
- metric: accuracy
- version: unspecified
- dataset: HLE; tested item count/subset not reported
- variant: GPT-4o judged
- source: [https://arxiv.org/html/2609.25611](https://arxiv.org/html/2609.25611)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Qwen technical report, Table 2 and footnote](https://arxiv.org/html/2609.25611)
- [Original Humanity's Last Exam benchmark](https://lastexam.ai/)
- [Original HLE paper](https://arxiv.org/abs/2501.14249)

研究备注：
- 报告列出精确型号 HLE=36.5，并注明由 GPT-4o 判分；引用原始 HLE 论文而非 HLE-Diamond。使用官方 accuracy 指标和 unspecified 版本。报告未给评测子集或题数，故 dataset 只注明原始 HLE 名称和该限制；未将报告日期误填为评测日期。

最近核验时间：2026-11-04T10:05+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis model releases](https://artificialanalysis.ai/models/releases)
- [Qwen technical report](https://arxiv.org/html/2609.25611)

研究备注：
- AA 官方页说明当前指数 v5.0.1 由 9 项评测组成。页面当前仅展示部分模型；技术报告没有给出该指数结果。未使用其他 Qwen 型号成绩。

尚未解决的问题：
- 官方指数页和模型发布目录均为动态/部分列表，未找到精确型号不等于确认无成绩。

最近核验时间：2026-11-04T10:05+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Qwen technical report](https://arxiv.org/html/2609.25611)

研究备注：
- AA 官方页面显示 v2.1 及其 220 项任务、Stirrup shell/web 和盲测 Elo 方法；当前公开结果中没有精确型号。Qwen 技术报告也未提及 GDPval-AA。未移用其他 Qwen 变体的成绩。

最近核验时间：2026-11-04T10:05+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Qwen technical report](https://arxiv.org/html/2609.25611)

研究备注：
- Vals 官方 v2.2 榜单有 Qwen 3.8 Max 0902，但没有 Qwen3.8 Omni Flash。Qwen 报告也未提及 Vals Index；未移用 Max 成绩。

最近核验时间：2026-11-04T10:05+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis model releases",
          "url": "https://artificialanalysis.ai/models/releases"
        },
        {
          "label": "Qwen technical report",
          "url": "https://arxiv.org/html/2609.25611"
        }
      ],
      "notes": [
        "AA 官方页说明当前指数 v5.0.1 由 9 项评测组成。页面当前仅展示部分模型；技术报告没有给出该指数结果。未使用其他 Qwen 型号成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方指数页和模型发布目录均为动态/部分列表，未找到精确型号不等于确认无成绩。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench v1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Qwen technical report",
          "url": "https://arxiv.org/html/2609.25611"
        }
      ],
      "notes": [
        "官方排行榜显示版本 1.0.6，目前展开前 10 个结果并提示另有 119 项；已显示列表中无精确型号。Qwen 技术报告未提及 AutomationBench。"
      ],
      "status": "待核实",
      "unresolved": [
        "排行榜其余 119 项未展开，不能将当前页面未显示该型号视为已确认无成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Qwen technical report PDF",
          "url": "https://arxiv.org/pdf/2609.25611"
        }
      ],
      "notes": [
        "Surge 官方榜单可见其他 Qwen 型号，但没有 Qwen3.8 Omni Flash 精确条目；Qwen 技术报告未提及 Chartography。模型支持图像输入，因此该项适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen technical report, Table 2",
          "url": "https://arxiv.org/html/2609.25611"
        },
        {
          "label": "DeepSWE v1.1 methodology and task count",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "报告将精确型号 Qwen3.8-Omni-Flash 的 DeepSWE 1.1 结果列为 57.8；按定义的 pass@1 指标映射。报告说明该值是 Claude Code 与 mini-SWE-agent 两种 harness 中的最高值，但未披露本模型的获胜 harness；TOML 如实保留了这个条件。",
        "DeepSWE 官方 v1.1 页面说明该版本为 113 项任务。报告未公布实际评测日期，故未填写 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Qwen technical report",
          "url": "https://arxiv.org/html/2609.25611"
        }
      ],
      "notes": [
        "AA 官方页面显示 v2.1 及其 220 项任务、Stirrup shell/web 和盲测 Elo 方法；当前公开结果中没有精确型号。Qwen 技术报告也未提及 GDPval-AA。未移用其他 Qwen 变体的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen technical report, Table 2 and footnote",
          "url": "https://arxiv.org/html/2609.25611"
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
        "报告列出精确型号 HLE=36.5，并注明由 GPT-4o 判分；引用原始 HLE 论文而非 HLE-Diamond。使用官方 accuracy 指标和 unspecified 版本。报告未给评测子集或题数，故 dataset 只注明原始 HLE 名称和该限制；未将报告日期误填为评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Qwen technical report PDF",
          "url": "https://arxiv.org/pdf/2609.25611"
        }
      ],
      "notes": [
        "Qwen 技术报告中未找到 OSWorld 结果。先前二手提取中出现的 2.0 数值已再次核对并撤回：官方 PDF 不含 OSWorld、19.4 或 46.7。模型具备图像输入，项目适用。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地目标为 OSWorld 2.1；官方页面标题为 OSWorld 2.0，未找到该模型的 2.1 成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen technical report, Table 2",
          "url": "https://arxiv.org/html/2609.25611"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "报告列出精确型号分数 63.3，并说明使用 Claude Code、temperature=1.0、top_p=0.95、context=256K，问题修订后在 refined benchmark 上重评。该原始记录已保留在模型 TOML，未填写未披露的 version 或 metric。"
      ],
      "status": "待核实",
      "unresolved": [
        "报告只写 SWE-bench Pro，没有说明对应 V2 2.0.0 / 642-task 默认集；不能映射为本地 swe-bench-pro-v2 定义。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science v0.1 official announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Official Harbor leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval"
        },
        {
          "label": "Qwen technical report",
          "url": "https://arxiv.org/html/2609.25611"
        }
      ],
      "notes": [
        "官方公告说明 v0.1 有 70 项任务，但未列出 Qwen3.8-Omni-Flash。官方 Harbor leaderboard 页面停留在 Loading leaderboard。"
      ],
      "status": "待核实",
      "unresolved": [
        "排行榜未加载完整，尚不能确认该型号是否有公开结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench official leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Terminal-Bench 4.0 official announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Third-party claim, excluded from data",
          "url": "https://trustthebench.com/benchmarks/terminal-bench"
        }
      ],
      "notes": [
        "Qwen 技术报告未报告 Terminal-Bench 4。官方排行榜的动态表格未能完整读取。第三方页面的 53.9 标注日期早于本模型发布日期，且指向 TB 2.1；其来源链接失效，因此未采用。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态排行榜仍需人工/后续复核以确认是否有精确型号的 v4 成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T10:05+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Qwen technical report",
          "url": "https://arxiv.org/html/2609.25611"
        }
      ],
      "notes": [
        "Vals 官方 v2.2 榜单有 Qwen 3.8 Max 0902，但没有 Qwen3.8 Omni Flash。Qwen 报告也未提及 Vals Index；未移用 Max 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T10:05+08:00",
  "model_id": "alibaba/qwen3.8-omni-flash",
  "new_records": 3,
  "overall_status": "待复核"
}

-->
