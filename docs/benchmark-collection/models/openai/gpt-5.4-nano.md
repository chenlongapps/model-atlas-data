# GPT-5.4 nano Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.4-nano
- 模型名称：GPT-5.4 nano
- 发布日期：2026-03-17
- 最近检查时间：2026-11-05T11:27+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：2
- 收集前已有成绩数量：16
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 精确目标为 GPT-5.4 nano；本地 SWE-Bench Pro 52.4% 和 Terminal-Bench 2.0 46.3% 不是 Pro V2 / Terminal-Bench 4，不作映射。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| terminal-bench-v4 | 待核实 | 46.3 (metric=accuracy; version=2.0; variant=reasoning effort xhigh) | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.tbench.ai/](https://www.tbench.ai/), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| osworld-v2.1 | 待核实 | — | [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://developers.openai.com/api/docs/models/gpt-5.4-nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| chartography | 未找到 | — | [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography), [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/) | 2026-11-05T11:27+08:00 |
| humanitys-last-exam | 已存在 | 37.7 (metric=accuracy; effort=xhigh; variant=with tools); 24.3 (metric=accuracy; effort=xhigh; variant=without tools) | [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/), [https://lastexam.ai/](https://lastexam.ai/) | 2026-11-05T11:27+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/gpt-5-4-nano](https://artificialanalysis.ai/models/gpt-5-4-nano) | 2026-11-05T11:27+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa), [https://artificialanalysis.ai/models/gpt-5-4-nano](https://artificialanalysis.ai/models/gpt-5-4-nano) | 2026-11-05T11:27+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.vals.ai/models/openai_gpt-5.4-nano-2026-03-17](https://www.vals.ai/models/openai_gpt-5.4-nano-2026-03-17), [https://www.vals.ai/benchmarks/vals_index_v1_1](https://www.vals.ai/benchmarks/vals_index_v1_1), [https://www.vals.ai/benchmarks/vals_index_v2](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T11:27+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 官方 v1.1 榜单当前只显示 21/28 个模型且实时 JSON 记录不完整；未确认 `gpt-5-4-nano` 精确行。榜单中的 `gpt-5-4` 是不同模型 ID。

尚未解决的问题：
- 动态榜单数据不全，尚不能排除未展示的精确成绩。

最近核验时间：2026-11-05T11:27+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 检查 Scale SWE-Bench Pro V2 榜单；本地已有 SWE-Bench Pro 52.4% 属 Public 旧版本，OpenAI 原文未标 V2，不能映射。

尚未解决的问题：
- 当前公开榜单未确认 nano 的 v2 成绩；本地旧版成绩不能替代。

最近核验时间：2026-11-05T11:27+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 46.3
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
- 本地 46.3% 明确对应 Terminal-Bench 2.0；官方版本页确认 v4，但结果页没有可读的 nano 精确结果。

尚未解决的问题：
- 需要官方 v4 结果页的精确模型行。

最近核验时间：2026-11-05T11:27+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 检查 0.1 公告及 Harbor 官方榜单；Harbor 动态榜单停在 Loading，未确认精确结果。

尚未解决的问题：
- 动态榜单未加载。

最近核验时间：2026-11-05T11:27+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- GPT-5.4 nano 支持 tools/function calling；Zapier v1.0.6 榜单仅显示前 10 条，另有 119 条折叠，无法确认精确行。

尚未解决的问题：
- 需检查完整榜单数据。

最近核验时间：2026-11-05T11:27+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://developers.openai.com/api/docs/models/gpt-5.4-nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- 本地 39.0% 是 OSWorld-Verified，不是 OSWorld v2.1。nano 支持图像和函数调用，但官方 API 卡注明内置 Computer-use tool 不支持；外部 harness 是否构成目标版本结果尚未确认。

尚未解决的问题：
- 不能把 OSWorld-Verified 39.0% 当作 v2.1。

最近核验时间：2026-11-05T11:27+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)

研究备注：
- nano 支持图像输入；检查 Surge Chartography 当前公开榜单快照，未见 GPT-5.4 nano 精确行。

最近核验时间：2026-11-05T11:27+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 37.7
- metric: accuracy
- effort: xhigh
- variant: with tools
- source: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 24.3
- metric: accuracy
- effort: xhigh
- variant: without tools
- source: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano/](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)
- [https://lastexam.ai/](https://lastexam.ai/)

研究备注：
- 本地已有 37.7% with tools 和 24.3% without tools；OpenAI 原表确认为 GPT-5.4 nano xhigh。更新为 effort=xhigh；删除仅代表公告发布日期的 date（原文未给实际评测日期）。结果属于原始 HLE，不是 HLE-Diamond。

最近核验时间：2026-11-05T11:27+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/gpt-5-4-nano](https://artificialanalysis.ai/models/gpt-5-4-nano)

研究备注：
- 精确 AA 型号页的 Intelligence Index 明确显示 N/A；页面将当前指数版本标为 V5.0.1，未给 nano 可用分数。

最近核验时间：2026-11-05T11:27+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [https://artificialanalysis.ai/models/gpt-5-4-nano](https://artificialanalysis.ai/models/gpt-5-4-nano)

研究备注：
- 检查 AA GDPval-AA v2.1 榜单及 nano 精确型号页，未找到 GPT-5.4 nano 的公开精确行；不把 GPT-5.4 mini 成绩移用。

最近核验时间：2026-11-05T11:27+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.vals.ai/models/openai_gpt-5.4-nano-2026-03-17](https://www.vals.ai/models/openai_gpt-5.4-nano-2026-03-17)
- [https://www.vals.ai/benchmarks/vals_index_v1_1](https://www.vals.ai/benchmarks/vals_index_v1_1)
- [https://www.vals.ai/benchmarks/vals_index_v2](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- Vals nano 型号页显示 51.16%，但未标 Index 版本；历史 v1.1 为 46.46%、v2.0 为 33.00%，当前 v2.2 榜单只展示每家最佳模型且未列 nano，无法确认 51.16 属于 v2.2。

尚未解决的问题：
- 版本和该动态型号页当前分数的对应关系不明。

最近核验时间：2026-11-05T11:27+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/gpt-5-4-nano"
        }
      ],
      "notes": [
        "精确 AA 型号页的 Intelligence Index 明确显示 N/A；页面将当前指数版本标为 V5.0.1，未给 nano 可用分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "GPT-5.4 nano 支持 tools/function calling；Zapier v1.0.6 榜单仅显示前 10 条，另有 119 条折叠，无法确认精确行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单数据。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "nano 支持图像输入；检查 Surge Chartography 当前公开榜单快照，未见 GPT-5.4 nano 精确行。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:27+08:00",
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
        "官方 v1.1 榜单当前只显示 21/28 个模型且实时 JSON 记录不完整；未确认 `gpt-5-4-nano` 精确行。榜单中的 `gpt-5-4` 是不同模型 ID。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单数据不全，尚不能排除未展示的精确成绩。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "url": "https://artificialanalysis.ai/models/gpt-5-4-nano"
        }
      ],
      "notes": [
        "检查 AA GDPval-AA v2.1 榜单及 nano 精确型号页，未找到 GPT-5.4 nano 的公开精确行；不把 GPT-5.4 mini 成绩移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        },
        {
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "本地已有 37.7% with tools 和 24.3% without tools；OpenAI 原表确认为 GPT-5.4 nano xhigh。更新为 effort=xhigh；删除仅代表公告发布日期的 date（原文未给实际评测日期）。结果属于原始 HLE，不是 HLE-Diamond。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://developers.openai.com/api/docs/models/gpt-5.4-nano"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "本地 39.0% 是 OSWorld-Verified，不是 OSWorld v2.1。nano 支持图像和函数调用，但官方 API 卡注明内置 Computer-use tool 不支持；外部 harness 是否构成目标版本结果尚未确认。"
      ],
      "status": "待核实",
      "unresolved": [
        "不能把 OSWorld-Verified 39.0% 当作 v2.1。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "检查 Scale SWE-Bench Pro V2 榜单；本地已有 SWE-Bench Pro 52.4% 属 Public 旧版本，OpenAI 原文未标 V2，不能映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前公开榜单未确认 nano 的 v2 成绩；本地旧版成绩不能替代。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "url": "https://openai.com/index/introducing-gpt-5-4-mini-and-nano/"
        }
      ],
      "notes": [
        "检查 0.1 公告及 Harbor 官方榜单；Harbor 动态榜单停在 Loading，未确认精确结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单未加载。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:27+08:00",
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
        "本地 46.3% 明确对应 Terminal-Bench 2.0；官方版本页确认 v4，但结果页没有可读的 nano 精确结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要官方 v4 结果页的精确模型行。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.vals.ai/models/openai_gpt-5.4-nano-2026-03-17"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index_v1_1"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "Vals nano 型号页显示 51.16%，但未标 Index 版本；历史 v1.1 为 46.46%、v2.0 为 33.00%，当前 v2.2 榜单只展示每家最佳模型且未列 nano，无法确认 51.16 属于 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "版本和该动态型号页当前分数的对应关系不明。"
      ]
    }
  },
  "existing_records": 16,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:27+08:00",
  "model_id": "openai/gpt-5.4-nano",
  "model_notes": [
    "精确目标为 GPT-5.4 nano；本地 SWE-Bench Pro 52.4% 和 Terminal-Bench 2.0 46.3% 不是 Pro V2 / Terminal-Bench 4，不作映射。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
