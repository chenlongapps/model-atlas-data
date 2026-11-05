# Mistral Small 4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/mistral-small-2603
- 模型名称：Mistral Small 4
- 发布日期：2026-03-16
- 最近检查时间：2026-11-05T11:27+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：3
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- 模型是 Mistral Small 4 v26.03。保留 Terminal-Bench Hard 17.4 为独立已有记录；它不是目标 Terminal-Bench 4。GDPval-AA v2.1 的公开分数存在冲突，暂不录入。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/), [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03) | 2026-11-05T11:27+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/), [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03) | 2026-11-05T11:27+08:00 |
| terminal-bench-v4 | 待核实 | — | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.tbench.ai/](https://www.tbench.ai/), [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/), [https://openrouter.ai/mistralai/mistral-small-2603/benchmarks](https://openrouter.ai/mistralai/mistral-small-2603/benchmarks) | 2026-11-05T11:27+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement), [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/) | 2026-11-05T11:27+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/), [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03) | 2026-11-05T11:27+08:00 |
| osworld-v2.1 | 待核实 | — | [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03), [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/) | 2026-11-05T11:27+08:00 |
| chartography | 未找到 | — | [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography), [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03) | 2026-11-05T11:27+08:00 |
| humanitys-last-exam | 已收录 | 10 (metric=accuracy; dataset=Original HLE 2,500-question set; variant=Reasoning); 4 (metric=accuracy; dataset=Original HLE 2,500-question set; variant=Non-reasoning) | [https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex), [https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b](https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [https://lastexam.ai/](https://lastexam.ai/) | 2026-11-05T11:27+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 4 (metric=index score; version=5.0.1; variant=Reasoning) | [https://artificialanalysis.ai/models/mistral-small-4](https://artificialanalysis.ai/models/mistral-small-4) | 2026-11-05T11:27+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa), [https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex) | 2026-11-05T11:27+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.vals.ai/models/mistralai_mistral-small-2603](https://www.vals.ai/models/mistralai_mistral-small-2603), [https://www.vals.ai/benchmarks/vals_index_v1](https://www.vals.ai/benchmarks/vals_index_v1) | 2026-11-05T11:27+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/)
- [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03)

研究备注：
- 官方资料确认目标模型为 Mistral Small 4 v26.03，支持编码；DeepSWE v1.1 榜单当前只部分展示且 JSON 不完整，未确认精确行。

尚未解决的问题：
- 动态榜单不完整，需确认 Mistral Small 4 精确结果。

最近核验时间：2026-11-05T11:27+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/)
- [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03)

研究备注：
- 检查 Scale V2 官方榜单和 Mistral Small 4 发布资料，未确认该精确版本成绩。

尚未解决的问题：
- 当前公开榜单未确认目标行。

最近核验时间：2026-11-05T11:27+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.tbench.ai/](https://www.tbench.ai/)
- [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/)
- [https://openrouter.ai/mistralai/mistral-small-2603/benchmarks](https://openrouter.ai/mistralai/mistral-small-2603/benchmarks)

研究备注：
- 官方版本页确认目标为 Terminal-Bench 4.0；结果页未提供可读精确行。OpenRouter 的 Terminal-Bench Hard 17.4 名称/版本不匹配，不能映射。

尚未解决的问题：
- 需取得可读的 v4 精确结果。

最近核验时间：2026-11-05T11:27+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement)
- [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/)

研究备注：
- 官方 Harbor v0.1 动态榜单本次未加载；未确认 Small 4 精确结果。

尚未解决的问题：
- 动态榜单未加载。

最近核验时间：2026-11-05T11:27+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/)
- [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03)

研究备注：
- 官方资料确认 Small 4 有 Agent / function calling 能力；Zapier 榜单折叠 119 条，无法确认精确模型行。

尚未解决的问题：
- 需检查完整榜单。

最近核验时间：2026-11-05T11:27+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03)
- [https://mistral.ai/news/mistral-small-4/](https://mistral.ai/news/mistral-small-4/)

研究备注：
- Small 4 支持图像输入和 Agent 能力，任务适用；官方 OSWorld 当前页为 2.0，v2.1 发布页未列出该型号成绩，不能断言未测。

尚未解决的问题：
- 尚无精确 v2.1 的公开记录核验。

最近核验时间：2026-11-05T11:27+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- [https://docs.mistral.ai/models/mistral-small-4-0-26-03](https://docs.mistral.ai/models/mistral-small-4-0-26-03)

研究备注：
- Small 4 支持图像输入，任务适用；检查 Surge Chartography 当前榜单快照，未见 Mistral Small 4 精确行。

最近核验时间：2026-11-05T11:27+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 10
- metric: accuracy
- dataset: Original HLE 2,500-question set
- variant: Reasoning
- source: [https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 4
- metric: accuracy
- dataset: Original HLE 2,500-question set
- variant: Non-reasoning
- source: [https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b](https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex)
- [https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b](https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [https://lastexam.ai/](https://lastexam.ai/)

研究备注：
- AA v4.3.2 比较页分别列出 Mistral Small 4 Reasoning 10% 和 Non-reasoning 4%。该指数版本包含原始 HLE；记录为两个独立变体。没有公布的 effort、工具配置或实际评测日不填。

最近核验时间：2026-11-05T11:27+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 4
- metric: index score
- version: 5.0.1
- variant: Reasoning
- source: [https://artificialanalysis.ai/models/mistral-small-4](https://artificialanalysis.ai/models/mistral-small-4)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/mistral-small-4](https://artificialanalysis.ai/models/mistral-small-4)

研究备注：
- 精确 AA 型号页显示 Artificial Analysis Intelligence Index v5.0.1 score 4；页面明确为 Mistral Small 4 (Reasoning)。V5.0.1 是仓库定义 v5.0 的兼容版本；复合指数不替代原始 HLE。

最近核验时间：2026-11-05T11:27+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex)

研究备注：
- AA v2.1 榜单显示 Mistral Small 4 (Reasoning) 370 Elo（CI -22/+22）；另一 AA 比较页显示同名同条件 365 Elo。两页均标 v2.1，公开页面未解释差异，暂不写入任一分数。方法说明为 220 项任务、44 职业/9 行业、Stirrup shell+web、盲测 pairwise Elo。

尚未解决的问题：
- 同一版本和变体存在 370 与 365 Elo 两个公开值，待 AA 说明是否为结果修订或不同运行。

最近核验时间：2026-11-05T11:27+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.vals.ai/models/mistralai_mistral-small-2603](https://www.vals.ai/models/mistralai_mistral-small-2603)
- [https://www.vals.ai/benchmarks/vals_index_v1](https://www.vals.ai/benchmarks/vals_index_v1)

研究备注：
- Small 4 精确 Vals 型号页显示 Accuracy 25.34% / Vals Index，但没有注明 Index 版本；明确的旧 V1 榜单成绩为 29.07%，当前 v2.2 只展示最新/领先模型且未列 Small 4，不能将 25.34 映射到 v2.2。

尚未解决的问题：
- 25.34% 对应的版本与评测日期未披露。

最近核验时间：2026-11-05T11:27+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/mistral-small-4"
        }
      ],
      "notes": [
        "精确 AA 型号页显示 Artificial Analysis Intelligence Index v5.0.1 score 4；页面明确为 Mistral Small 4 (Reasoning)。V5.0.1 是仓库定义 v5.0 的兼容版本；复合指数不替代原始 HLE。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://mistral.ai/news/mistral-small-4/"
        },
        {
          "url": "https://docs.mistral.ai/models/mistral-small-4-0-26-03"
        }
      ],
      "notes": [
        "官方资料确认 Small 4 有 Agent / function calling 能力；Zapier 榜单折叠 119 条，无法确认精确模型行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "url": "https://docs.mistral.ai/models/mistral-small-4-0-26-03"
        }
      ],
      "notes": [
        "Small 4 支持图像输入，任务适用；检查 Surge Chartography 当前榜单快照，未见 Mistral Small 4 精确行。"
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
          "url": "https://mistral.ai/news/mistral-small-4/"
        },
        {
          "url": "https://docs.mistral.ai/models/mistral-small-4-0-26-03"
        }
      ],
      "notes": [
        "官方资料确认目标模型为 Mistral Small 4 v26.03，支持编码；DeepSWE v1.1 榜单当前只部分展示且 JSON 不完整，未确认精确行。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单不完整，需确认 Mistral Small 4 精确结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex"
        }
      ],
      "notes": [
        "AA v2.1 榜单显示 Mistral Small 4 (Reasoning) 370 Elo（CI -22/+22）；另一 AA 比较页显示同名同条件 365 Elo。两页均标 v2.1，公开页面未解释差异，暂不写入任一分数。方法说明为 220 项任务、44 职业/9 行业、Stirrup shell+web、盲测 pairwise Elo。"
      ],
      "status": "冲突",
      "unresolved": [
        "同一版本和变体存在 370 与 365 Elo 两个公开值，待 AA 说明是否为结果修订或不同运行。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-small-4-vs-gpt-5-codex"
        },
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-small-4-non-reasoning-vs-qwen3-5-397b-a17b"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "AA v4.3.2 比较页分别列出 Mistral Small 4 Reasoning 10% 和 Non-reasoning 4%。该指数版本包含原始 HLE；记录为两个独立变体。没有公布的 effort、工具配置或实际评测日不填。"
      ],
      "status": "已收录",
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
          "url": "https://docs.mistral.ai/models/mistral-small-4-0-26-03"
        },
        {
          "url": "https://mistral.ai/news/mistral-small-4/"
        }
      ],
      "notes": [
        "Small 4 支持图像输入和 Agent 能力，任务适用；官方 OSWorld 当前页为 2.0，v2.1 发布页未列出该型号成绩，不能断言未测。"
      ],
      "status": "待核实",
      "unresolved": [
        "尚无精确 v2.1 的公开记录核验。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://mistral.ai/news/mistral-small-4/"
        },
        {
          "url": "https://docs.mistral.ai/models/mistral-small-4-0-26-03"
        }
      ],
      "notes": [
        "检查 Scale V2 官方榜单和 Mistral Small 4 发布资料，未确认该精确版本成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前公开榜单未确认目标行。"
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
          "url": "https://mistral.ai/news/mistral-small-4/"
        }
      ],
      "notes": [
        "官方 Harbor v0.1 动态榜单本次未加载；未确认 Small 4 精确结果。"
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
          "url": "https://mistral.ai/news/mistral-small-4/"
        },
        {
          "url": "https://openrouter.ai/mistralai/mistral-small-2603/benchmarks"
        }
      ],
      "notes": [
        "官方版本页确认目标为 Terminal-Bench 4.0；结果页未提供可读精确行。OpenRouter 的 Terminal-Bench Hard 17.4 名称/版本不匹配，不能映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需取得可读的 v4 精确结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:27+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.vals.ai/models/mistralai_mistral-small-2603"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index_v1"
        }
      ],
      "notes": [
        "Small 4 精确 Vals 型号页显示 Accuracy 25.34% / Vals Index，但没有注明 Index 版本；明确的旧 V1 榜单成绩为 29.07%，当前 v2.2 只展示最新/领先模型且未列 Small 4，不能将 25.34 映射到 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "25.34% 对应的版本与评测日期未披露。"
      ]
    }
  },
  "existing_records": 3,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:27+08:00",
  "model_id": "mistral/mistral-small-2603",
  "model_notes": [
    "模型是 Mistral Small 4 v26.03。保留 Terminal-Bench Hard 17.4 为独立已有记录；它不是目标 Terminal-Bench 4。GDPval-AA v2.1 的公开分数存在冲突，暂不录入。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
