# GPT-5.4 Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.4-pro
- 模型名称：GPT-5.4 Pro
- 发布日期：2026-03-05
- 最近检查时间：2026-11-05T12:12+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：2
- 收集前已有成绩数量：2
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- GPT-5.4 Pro 的 API 快照和 OpenAI 官方发布资料确认其为独立模型版本；未把基础 GPT-5.4 的 agent 榜单成绩并入。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 live leaderboard JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-Bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/), [Artificial Analysis GPT-5.4 Pro profile](https://artificialanalysis.ai/models/gpt-5-4-pro), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench-Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2.1 evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld V2 official project](https://github.com/xlang-ai/OSWorld-V2), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro), [OpenAI GPT-5.5 comparison table](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T12:12+08:00 |
| chartography | 待核实 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official methodology and harness](https://github.com/surge-ai/chartography), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| humanitys-last-exam | 已存在 | 42.7 (metric=accuracy; effort=xhigh; variant=no tools); 58.7 (metric=accuracy; effort=xhigh; variant=with tools) | [OpenAI GPT-5.4 release and HLE table](https://openai.com/index/introducing-gpt-5-4/), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis GPT-5.4 Pro profile](https://artificialanalysis.ai/models/gpt-5-4-pro), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | 2026-11-05T12:12+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GPT-5.4 Pro profile](https://artificialanalysis.ai/models/gpt-5-4-pro), [GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [GPT-5.5 comparison table](https://openai.com/index/introducing-gpt-5-5/) | 2026-11-05T12:12+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals historical Index V2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T12:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 live leaderboard JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 已检查 DeepSWE v1.1 全量公开 JSON；未见精确 GPT-5.4 Pro 行，未使用 GPT-5.4 基础版成绩。

尚未解决的问题：
- 需确认是否存在未列入当前公开榜单的 GPT-5.4 Pro 结果。

最近核验时间：2026-11-05T12:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-Bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 本地未发现可对应 GPT-5.4 Pro 的 V2 行；官方 V2 动态榜单未能核实精确结果。

尚未解决的问题：
- 需从完整 V2 榜单或原始评测资料确认。

最近核验时间：2026-11-05T12:12+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/)
- [Artificial Analysis GPT-5.4 Pro profile](https://artificialanalysis.ai/models/gpt-5-4-pro)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 本地无目标 V4 记录；当前官方动态榜单未能核实 GPT-5.4 Pro 的精确分数，未沿用基础版成绩。

尚未解决的问题：
- 需核对官方 V4 完整榜单是否含 GPT-5.4 Pro。

最近核验时间：2026-11-05T12:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench-Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 官方 0.1 公告和 Harbor 动态榜单未能核实 GPT-5.4 Pro 精确成绩。

尚未解决的问题：
- 需从完整 0.1 榜单或原始运行记录确认。

最近核验时间：2026-11-05T12:12+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- Zapier 页面只展开部分行，未能确认精确 Pro 变体的 held-out 成绩。

尚未解决的问题：
- 需核对官方榜单完整折叠结果及 Pro 变体。

最近核验时间：2026-11-05T12:12+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2.1 evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld V2 official project](https://github.com/xlang-ai/OSWorld-V2)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)
- [OpenAI GPT-5.5 comparison table](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- GPT-5.5 对照表中 GPT-5.4 Pro 的 OSWorld-Verified 为横线；OSWorld-Verified 本身也不同于 V2.1。未核实到精确 Pro 的 V2.1 结果。

尚未解决的问题：
- 需确认公开 OSWorld V2.1 完整榜单中的 GPT-5.4 Pro 结果。

最近核验时间：2026-11-05T12:12+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official methodology and harness](https://github.com/surge-ai/chartography)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 榜单未找到 GPT-5.4 Pro 的精确行；未将基础 GPT-5.4 的 29.6% 结果并入。

尚未解决的问题：
- 需确认动态榜单是否存在 GPT-5.4 Pro 历史评测。

最近核验时间：2026-11-05T12:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 42.7
- metric: accuracy
- effort: xhigh
- variant: no tools
- source: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 58.7
- metric: accuracy
- effort: xhigh
- variant: with tools
- source: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [OpenAI GPT-5.4 release and HLE table](https://openai.com/index/introducing-gpt-5-4/)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 已有 OpenAI 精确版本成绩：42.7% no tools、58.7% with tools；本轮校正来源并补入 xhigh。来源未公布该成绩的实际评测日期，故删除原来的文章发布日期。

最近核验时间：2026-11-05T12:12+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GPT-5.4 Pro profile](https://artificialanalysis.ai/models/gpt-5-4-pro)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [GPT-5.4 Pro API model documentation](https://developers.openai.com/api/docs/models/gpt-5.4-pro)

研究备注：
- 精确 AA profile 未提供可映射到 V5.0.1 的指数分数；历史 v4.3.2 指数不映射。

尚未解决的问题：
- 需确认 GPT-5.4 Pro 是否有 V5.0.1 结果。

最近核验时间：2026-11-05T12:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GPT-5.4 Pro profile](https://artificialanalysis.ai/models/gpt-5-4-pro)
- [GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [GPT-5.5 comparison table](https://openai.com/index/introducing-gpt-5-5/)

研究备注：
- AA 未核实到 GPT-5.4 Pro 的 GDPval-AA v2.1 Elo；OpenAI 的 82.0% 是 GDPval wins-or-ties，不是 AA Elo。

尚未解决的问题：
- 需取得精确 Pro 配置的 v2.1 Elo 和 source table。

最近核验时间：2026-11-05T12:12+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals historical Index V2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- 当前 V2.2 榜单只展示各实验室最佳模型，没有 GPT-5.4 Pro 行；缺席不足以判定无评测。

尚未解决的问题：
- 需确认是否有精确 GPT-5.4 Pro V2.2 结果。

最近核验时间：2026-11-05T12:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.4 Pro profile",
          "url": "https://artificialanalysis.ai/models/gpt-5-4-pro"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "精确 AA profile 未提供可映射到 V5.0.1 的指数分数；历史 v4.3.2 指数不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 GPT-5.4 Pro 是否有 V5.0.1 结果。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T12:12+08:00",
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
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "Zapier 页面只展开部分行，未能确认精确 Pro 变体的 held-out 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核对官方榜单完整折叠结果及 Pro 变体。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official methodology and harness",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "榜单未找到 GPT-5.4 Pro 的精确行；未将基础 GPT-5.4 的 29.6% 结果并入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认动态榜单是否存在 GPT-5.4 Pro 历史评测。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 live leaderboard JSON",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "已检查 DeepSWE v1.1 全量公开 JSON；未见精确 GPT-5.4 Pro 行，未使用 GPT-5.4 基础版成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认是否存在未列入当前公开榜单的 GPT-5.4 Pro 结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.4 Pro profile",
          "url": "https://artificialanalysis.ai/models/gpt-5-4-pro"
        },
        {
          "label": "GDPval-AA v2.1 evaluation and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "GPT-5.5 comparison table",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "AA 未核实到 GPT-5.4 Pro 的 GDPval-AA v2.1 Elo；OpenAI 的 82.0% 是 GDPval wins-or-ties，不是 AA Elo。"
      ],
      "status": "待核实",
      "unresolved": [
        "需取得精确 Pro 配置的 v2.1 Elo 和 source table。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-5.4 release and HLE table",
          "url": "https://openai.com/index/introducing-gpt-5-4/"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "已有 OpenAI 精确版本成绩：42.7% no tools、58.7% with tools；本轮校正来源并补入 xhigh。来源未公布该成绩的实际评测日期，故删除原来的文章发布日期。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 evaluation guide",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld V2 official project",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        },
        {
          "label": "OpenAI GPT-5.5 comparison table",
          "url": "https://openai.com/index/introducing-gpt-5-5/"
        }
      ],
      "notes": [
        "GPT-5.5 对照表中 GPT-5.4 Pro 的 OSWorld-Verified 为横线；OSWorld-Verified 本身也不同于 V2.1。未核实到精确 Pro 的 V2.1 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认公开 OSWorld V2.1 完整榜单中的 GPT-5.4 Pro 结果。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "SWE-Bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "本地未发现可对应 GPT-5.4 Pro 的 V2 行；官方 V2 动态榜单未能核实精确结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从完整 V2 榜单或原始评测资料确认。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench-Science Harbor leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "官方 0.1 公告和 Harbor 动态榜单未能核实 GPT-5.4 Pro 精确成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从完整 0.1 榜单或原始运行记录确认。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Artificial Analysis GPT-5.4 Pro profile",
          "url": "https://artificialanalysis.ai/models/gpt-5-4-pro"
        },
        {
          "label": "GPT-5.4 Pro API model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-pro"
        }
      ],
      "notes": [
        "本地无目标 V4 记录；当前官方动态榜单未能核实 GPT-5.4 Pro 的精确分数，未沿用基础版成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核对官方 V4 完整榜单是否含 GPT-5.4 Pro。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T12:12+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals historical Index V2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "当前 V2.2 榜单只展示各实验室最佳模型，没有 GPT-5.4 Pro 行；缺席不足以判定无评测。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认是否有精确 GPT-5.4 Pro V2.2 结果。"
      ]
    }
  },
  "existing_records": 2,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T12:12+08:00",
  "model_id": "openai/gpt-5.4-pro",
  "model_notes": [
    "GPT-5.4 Pro 的 API 快照和 OpenAI 官方发布资料确认其为独立模型版本；未把基础 GPT-5.4 的 agent 榜单成绩并入。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
