# GPT-5.5 Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.5-pro
- 模型名称：GPT-5.5 Pro
- 发布日期：2026-04-23
- 最近检查时间：2026-11-05T07:34+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：7
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- OpenAI API 文档确认 GPT-5.5 Pro 快照为 gpt-5.5-pro-2026-04-23，与本地模型文件一致；没有把 base GPT-5.5 的公开分数迁移到 Pro。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | 2026-11-05T07:34+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| terminal-bench-v4 | 待核实 | — | [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science), [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | 2026-11-05T07:34+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | 2026-11-05T07:34+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/), [OSWorld-V2 v2.1 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测代码与方法](https://github.com/surge-ai/chartography), [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | 2026-11-05T07:34+08:00 |
| humanitys-last-exam | 已存在 | 43.1 (metric=accuracy; variant=no tools); 57.2 (metric=accuracy; variant=with tools) | [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/), [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | 2026-11-05T07:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis GPT-5.5 Pro 型号页](https://artificialanalysis.ai/models/gpt-5-5-pro), [Artificial Analysis Intelligence Index V5 说明](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T07:34+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GPT-5.5 Pro 型号页](https://artificialanalysis.ai/models/gpt-5-5-pro), [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T07:34+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index), [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro) | 2026-11-05T07:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro)

研究备注：
- DeepSWE 榜单当前有 GPT-5.5 base 67% (xhigh)，没有 gpt-5.5-pro 行；不将 base 成绩迁移到 Pro。

尚未解决的问题：
- 未找到 GPT-5.5 Pro 的 v1.1 结果。

最近核验时间：2026-11-05T07:34+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 原始发布页对 GPT-5.5 Pro 的 SWE-Bench Pro (Public) 列为 —；Scale Pro V2 动态页当前也未能确认 Pro 记录。

尚未解决的问题：
- 原始发布页无旧版 SWE-Bench Pro 分数，V2 页面未显示该精确型号。

最近核验时间：2026-11-05T07:34+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 首发页对 Pro 的 Terminal-Bench 2.0 列为 —；Vals 与 Artificial Analysis 当前可见 Terminal-Bench 4 页未能确认 Pro v4 结果。

尚未解决的问题：
- 动态/部分榜单不支持据缺席断言无 v4 分数。

最近核验时间：2026-11-05T07:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro)

研究备注：
- Vals 当前可见 Science leaderboard 未显示 GPT-5.5 Pro；未找到可核验的 v0.1.0 结果。

尚未解决的问题：
- 当前页面为动态榜单，无法确认完整型号覆盖。

最近核验时间：2026-11-05T07:34+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro)

研究备注：
- Zapier 1.0.6 页面仅显示前 10 条并折叠其余 119 条，无法完整核实 GPT-5.5 Pro。OpenAI 首发页没有提供 Pro AutomationBench 数值。

尚未解决的问题：
- 榜单折叠结果未能完整检查，不能据可见部分判未找到。

最近核验时间：2026-11-05T07:34+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 v2.1 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- OpenAI 首发页的 Pro OSWorld-Verified 单元格为 —，但该评测并非 OSWorld v2.1；官方资料未给 Pro v2.1 分数。

尚未解决的问题：
- OSWorld-Verified 的缺失不等于 v2.1 已检查无成绩。

最近核验时间：2026-11-05T07:34+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测代码与方法](https://github.com/surge-ai/chartography)
- [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro)

研究备注：
- GPT-5.5 Pro 支持图像输入，适用于 Chartography；Surge 当前可访问榜单列出 GPT-5.5 base (xHigh) 31%，但没有 GPT-5.5 Pro 行。
- 官方评测代码说明该基准评测图表图像并使用 Inspect AI；当前公开榜单未找到 Pro 分数。

最近核验时间：2026-11-05T07:34+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 43.1
- metric: accuracy
- variant: no tools
- source: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)
- date: 2026-04-23
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 57.2
- metric: accuracy
- variant: with tools
- source: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)
- date: 2026-04-23
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro)

研究备注：
- 本地已有两条 OpenAI GPT-5.5 Pro HLE 记录：43.1 accuracy（no tools）和 57.2 accuracy（with tools）；均保留原工具条件。
- API 文档确认快照 gpt-5.5-pro-2026-04-23；未新增或更改 HLE 记录。

最近核验时间：2026-11-05T07:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GPT-5.5 Pro 型号页](https://artificialanalysis.ai/models/gpt-5-5-pro)
- [Artificial Analysis Intelligence Index V5 说明](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis GPT-5.5 Pro 精确型号页指向 Index v5.0.1，当前 Intelligence Index 值为 N/A/Unknown；未找到可收录分数。

最近核验时间：2026-11-05T07:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GPT-5.5 Pro 型号页](https://artificialanalysis.ai/models/gpt-5-5-pro)
- [OpenAI GPT-5.5 官方发布页](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- 当前 GDPval-AA v2.1 榜单/型号页未提供可核实 GPT-5.5 Pro Elo。OpenAI 发布页中的 GDPval wins-or-ties 82.3% 不是 GDPval-AA v2.1。

尚未解决的问题：
- 没有可直接核实的 GPT-5.5 Pro v2.1 Elo。

最近核验时间：2026-11-05T07:34+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index)
- [OpenAI GPT-5.5 Pro API 模型文档](https://developers.openai.com/api/docs/models/gpt-5.5-pro)

研究备注：
- 当前 Vals v2.2 页面未见 GPT-5.5 Pro；页面为部分 latest/top/frontier 展示，无法据缺席判定未评测。

尚未解决的问题：
- 未找到能确认的 v2.2 Pro 结果；当前榜单展示不完整。

最近核验时间：2026-11-05T07:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.5 Pro 型号页",
          "url": "https://artificialanalysis.ai/models/gpt-5-5-pro"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 说明",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis GPT-5.5 Pro 精确型号页指向 Index v5.0.1，当前 Intelligence Index 值为 N/A/Unknown；未找到可收录分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "OpenAI GPT-5.5 Pro API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5-pro"
        }
      ],
      "notes": [
        "Zapier 1.0.6 页面仅显示前 10 条并折叠其余 119 条，无法完整核实 GPT-5.5 Pro。OpenAI 首发页没有提供 Pro AutomationBench 数值。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单折叠结果未能完整检查，不能据可见部分判未找到。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测代码与方法",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "OpenAI GPT-5.5 Pro API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5-pro"
        }
      ],
      "notes": [
        "GPT-5.5 Pro 支持图像输入，适用于 Chartography；Surge 当前可访问榜单列出 GPT-5.5 base (xHigh) 31%，但没有 GPT-5.5 Pro 行。",
        "官方评测代码说明该基准评测图表图像并使用 Inspect AI；当前公开榜单未找到 Pro 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "OpenAI GPT-5.5 Pro API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5-pro"
        }
      ],
      "notes": [
        "DeepSWE 榜单当前有 GPT-5.5 base 67% (xhigh)，没有 gpt-5.5-pro 行；不将 base 成绩迁移到 Pro。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到 GPT-5.5 Pro 的 v1.1 结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GPT-5.5 Pro 型号页",
          "url": "https://artificialanalysis.ai/models/gpt-5-5-pro"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "当前 GDPval-AA v2.1 榜单/型号页未提供可核实 GPT-5.5 Pro Elo。OpenAI 发布页中的 GDPval wins-or-ties 82.3% 不是 GDPval-AA v2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有可直接核实的 GPT-5.5 Pro v2.1 Elo。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        },
        {
          "label": "OpenAI GPT-5.5 Pro API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5-pro"
        }
      ],
      "notes": [
        "本地已有两条 OpenAI GPT-5.5 Pro HLE 记录：43.1 accuracy（no tools）和 57.2 accuracy（with tools）；均保留原工具条件。",
        "API 文档确认快照 gpt-5.5-pro-2026-04-23；未新增或更改 HLE 记录。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 v2.1 发布记录",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 首发页的 Pro OSWorld-Verified 单元格为 —，但该评测并非 OSWorld v2.1；官方资料未给 Pro v2.1 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "OSWorld-Verified 的缺失不等于 v2.1 已检查无成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 原始发布页对 GPT-5.5 Pro 的 SWE-Bench Pro (Public) 列为 —；Scale Pro V2 动态页当前也未能确认 Pro 记录。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始发布页无旧版 SWE-Bench Pro 分数，V2 页面未显示该精确型号。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "OpenAI GPT-5.5 Pro API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5-pro"
        }
      ],
      "notes": [
        "Vals 当前可见 Science leaderboard 未显示 GPT-5.5 Pro；未找到可核验的 v0.1.0 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前页面为动态榜单，无法确认完整型号覆盖。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "OpenAI GPT-5.5 官方发布页",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "OpenAI 首发页对 Pro 的 Terminal-Bench 2.0 列为 —；Vals 与 Artificial Analysis 当前可见 Terminal-Bench 4 页未能确认 Pro v4 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态/部分榜单不支持据缺席断言无 v4 分数。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "OpenAI GPT-5.5 Pro API 模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.5-pro"
        }
      ],
      "notes": [
        "当前 Vals v2.2 页面未见 GPT-5.5 Pro；页面为部分 latest/top/frontier 展示，无法据缺席判定未评测。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到能确认的 v2.2 Pro 结果；当前榜单展示不完整。"
      ]
    }
  },
  "existing_records": 7,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:34+08:00",
  "model_id": "openai/gpt-5.5-pro",
  "model_notes": [
    "OpenAI API 文档确认 GPT-5.5 Pro 快照为 gpt-5.5-pro-2026-04-23，与本地模型文件一致；没有把 base GPT-5.5 的公开分数迁移到 Pro。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
