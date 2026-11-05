# GPT-5.4 mini Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.4-mini
- 模型名称：GPT-5.4 mini
- 发布日期：2026-03-17
- 最近检查时间：2026-11-05T11:16+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：2
- 收集前已有成绩数量：16
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- 核对的是 GPT-5.4 mini 精确型号；已存在的 SWE-Bench Pro 54.4% 和 Terminal-Bench 2.0 60.0% 不映射到 Pro V2 / Terminal-Bench 4。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| terminal-bench-v4 | 待核实 | 60.0 (metric=accuracy; version=2.0; variant=reasoning effort xhigh) | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.tbench.ai/](https://www.tbench.ai/), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.tbench.ai/](https://www.tbench.ai/), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| osworld-v2.1 | 待核实 | — | [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://developers.openai.com/api/docs/models/gpt-5.4-mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| chartography | 未找到 | — | [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| humanitys-last-exam | 已存在 | 41.5 (metric=accuracy; effort=xhigh; variant=with tools); 28.2 (metric=accuracy; effort=xhigh; variant=without tools) | [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:16+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/gpt-5-4-mini](https://artificialanalysis.ai/models/gpt-5-4-mini) | 2026-11-05T11:16+08:00 |
| gdpval-aa-v2.1 | 已收录 | 597 (metric=Elo rating; version=2.1; dataset=GDPval: 220 tasks across 44 occupations and 9 industries; variant=Non-reasoning; harness=Stirrup shell and web browsing; blind pairwise comparisons aggregated as Elo) | [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T11:16+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T11:16+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 检查 DeepSWE v1.1 官方榜单与实时 JSON，未确认 gpt-5-4-mini 的精确行；榜单中出现的 gpt-5-4 是不同 ID。

尚未解决的问题：
- 需核查完整实时榜单并确认 mini 型号是否有独立结果。

最近核验时间：2026-11-05T11:16+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- OpenAI 官方发布表的 SWE-Bench Pro 54.4% 没有声明为 Pro V2；检查 Scale V2 榜单未确认精确 mini 条目。

尚未解决的问题：
- 现有 54.4% 不映射到 Pro V2，待完整榜单核实。

最近核验时间：2026-11-05T11:16+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 60.0
- metric: accuracy
- version: 2.0
- variant: reasoning effort xhigh
- source: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- date: 2026-03-17
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.tbench.ai/](https://www.tbench.ai/)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 现有 Terminal-Bench 2.0 60.0% 不是 v4；检查官方版本页和结果页未确认 GPT-5.4 mini 的 v4 结果。

尚未解决的问题：
- 需要可读取的 Terminal-Bench 4 精确型号结果。

最近核验时间：2026-11-05T11:16+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.tbench.ai/](https://www.tbench.ai/)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 官方版本页确认 Science 0.1；本次官方结果页不可读，未确认该精确型号结果。

尚未解决的问题：
- 结果页不可读，保留待核实。

最近核验时间：2026-11-05T11:16+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 检查 Zapier 官方榜单；可见前 10 行，另有 119 条折叠，无法确认 mini 是否有精确成绩。

尚未解决的问题：
- 需检查完整榜单数据。

最近核验时间：2026-11-05T11:16+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://developers.openai.com/api/docs/models/gpt-5.4-mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 本地有 OSWorld-Verified 72.1%（xhigh），但不是 v2.1；官方 v2 页面当前标 2.0，本次未能确认精确 mini 的 v2.1 成绩。模型支持图像输入和工具。

尚未解决的问题：
- 不能将 OSWorld-Verified 或 OSWorld 2.0 结果移植为 v2.1。

最近核验时间：2026-11-05T11:16+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 检查 Surge Chartography 当前榜单快照；模型具备图像输入，但可见精确成绩仅有 GPT-5.4 full 29.6%，没有 mini 精确行，不跨型号转移。

最近核验时间：2026-11-05T11:16+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 41.5
- metric: accuracy
- effort: xhigh
- variant: with tools
- source: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 28.2
- metric: accuracy
- effort: xhigh
- variant: without tools
- source: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 本地已有两条官方 HLE 结果：41.5% with tools、28.2% without tools。OpenAI 表格标题确认 GPT-5.4 mini 的官方 reasoning effort 为 xhigh，已补入 effort 字段。原表只发布于模型公告日，未给实际评测日期，因此移除两条记录的 date。

最近核验时间：2026-11-05T11:16+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/gpt-5-4-mini](https://artificialanalysis.ai/models/gpt-5-4-mini)

研究备注：
- 精确型号页对应 GPT-5.4 mini (Xhigh)，V5.0.1 显示 N/A / 无公开 API；旧版本指数不映射为 V5。

最近核验时间：2026-11-05T11:16+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 597
- metric: Elo rating
- version: 2.1
- dataset: GDPval: 220 tasks across 44 occupations and 9 industries
- variant: Non-reasoning
- harness: Stirrup shell and web browsing; blind pairwise comparisons aggregated as Elo
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 官方 v2.1 榜单精确列出 GPT-5.4 mini (Non-reasoning)，597 Elo，置信区间 -20/+20。榜单说明采用 220 个 GDPval 任务、44 种职业/9 个行业、Stirrup shell+web agent loop 与盲测 pairwise Elo；Schema 无 CI 字段，故仅在研究备注保留。

最近核验时间：2026-11-05T11:16+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查当前 Vals Index v2.2 页面；榜单显示每个实验室的领先模型和最新/前沿子集，未列 GPT-5.4 mini，缺席不能证明未测。旧版本成绩不映射到 v2.2。

尚未解决的问题：
- 需完整历史数据或精确模型页核实 v2.2。

最近核验时间：2026-11-05T11:16+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/gpt-5-4-mini"
        }
      ],
      "notes": [
        "精确型号页对应 GPT-5.4 mini (Xhigh)，V5.0.1 显示 N/A / 无公开 API；旧版本指数不映射为 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "检查 Zapier 官方榜单；可见前 10 行，另有 119 条折叠，无法确认 mini 是否有精确成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单数据。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "检查 Surge Chartography 当前榜单快照；模型具备图像输入，但可见精确成绩仅有 GPT-5.4 full 29.6%，没有 mini 精确行，不跨型号转移。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "检查 DeepSWE v1.1 官方榜单与实时 JSON，未确认 gpt-5-4-mini 的精确行；榜单中出现的 gpt-5-4 是不同 ID。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查完整实时榜单并确认 mini 型号是否有独立结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "官方 v2.1 榜单精确列出 GPT-5.4 mini (Non-reasoning)，597 Elo，置信区间 -20/+20。榜单说明采用 220 个 GDPval 任务、44 种职业/9 个行业、Stirrup shell+web agent loop 与盲测 pairwise Elo；Schema 无 CI 字段，故仅在研究备注保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "本地已有两条官方 HLE 结果：41.5% with tools、28.2% without tools。OpenAI 表格标题确认 GPT-5.4 mini 的官方 reasoning effort 为 xhigh，已补入 effort 字段。原表只发布于模型公告日，未给实际评测日期，因此移除两条记录的 date。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-mini"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "本地有 OSWorld-Verified 72.1%（xhigh），但不是 v2.1；官方 v2 页面当前标 2.0，本次未能确认精确 mini 的 v2.1 成绩。模型支持图像输入和工具。"
      ],
      "status": "待核实",
      "unresolved": [
        "不能将 OSWorld-Verified 或 OSWorld 2.0 结果移植为 v2.1。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "OpenAI 官方发布表的 SWE-Bench Pro 54.4% 没有声明为 Pro V2；检查 Scale V2 榜单未确认精确 mini 条目。"
      ],
      "status": "待核实",
      "unresolved": [
        "现有 54.4% 不映射到 Pro V2，待完整榜单核实。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://www.tbench.ai/"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "官方版本页确认 Science 0.1；本次官方结果页不可读，未确认该精确型号结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "结果页不可读，保留待核实。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://www.tbench.ai/"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "现有 Terminal-Bench 2.0 60.0% 不是 v4；检查官方版本页和结果页未确认 GPT-5.4 mini 的 v4 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可读取的 Terminal-Bench 4 精确型号结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:16+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "检查当前 Vals Index v2.2 页面；榜单显示每个实验室的领先模型和最新/前沿子集，未列 GPT-5.4 mini，缺席不能证明未测。旧版本成绩不映射到 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "需完整历史数据或精确模型页核实 v2.2。"
      ]
    }
  },
  "existing_records": 16,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:16+08:00",
  "model_id": "openai/gpt-5.4-mini",
  "model_notes": [
    "核对的是 GPT-5.4 mini 精确型号；已存在的 SWE-Bench Pro 54.4% 和 Terminal-Bench 2.0 60.0% 不映射到 Pro V2 / Terminal-Bench 4。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
