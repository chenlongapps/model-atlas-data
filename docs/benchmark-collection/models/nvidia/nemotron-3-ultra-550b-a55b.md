# Nemotron 3 Ultra 550B A55B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3-ultra-550b-a55b
- 模型名称：Nemotron 3 Ultra 550B A55B
- 发布日期：2026-06-04
- 最近检查时间：2026-11-05T04:06+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：11
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- 本地模型为 NVIDIA Nemotron 3 Ultra 550B A55B BF16；官方模型卡确认 2026-06-04 发布。已有 11 条记录保留，目标 HLE 两条已存在。
- 新增 GDPval-AA v2.1 1021 Elo（CI -17/+17），以官方 AA 榜单中 Reasoning 配置和 Stirrup shell/web harness 为准；未把 NVIDIA 的通用 GDPval 46.7 wins-or-ties 记录当成 GDPval-AA。
- 新增 AA Index 12，来源版本 5.0.1；本地目标定义版本 5.0，故该原始记录保留但映射待复核。
- NVIDIA HF 自动评测区另显示 SWE-Bench Verified 71.9，而 TOML 历史行为 70.7；两处评测条件未确认，本轮不覆盖历史行。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |
| terminal-bench-v4 | 待核实 | 56.4 (metric=success rate; version=2.1) | [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1), [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |
| osworld-v2.1 | 不适用 | — | [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16), [OSWorld V2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T04:06+08:00 |
| chartography | 不适用 | — | [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16), [Chartography evaluation repository](https://github.com/surge-ai/chartography) | 2026-11-05T04:06+08:00 |
| humanitys-last-exam | 已存在 | 26.7 (metric=accuracy; variant=no tools); 37.4 (metric=accuracy; variant=with tools) | [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 12 (metric=index score; version=5.0.1) | [Artificial Analysis Nemotron 3 Ultra profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-ultra-550b-a55b) | 2026-11-05T04:06+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1021 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; variant=Reasoning; CI -17/+17; harness=Stirrup agentic loop (shell and web browsing)) | [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T04:06+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 2026-11-05T04:06+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- DeepSWE 榜单可读页面当前仅展示 21/28 配置，未见 Nemotron 3 Ultra；未找到可核实的分数、effort、harness 或评测日期。

尚未解决的问题：
- 榜单可见配置不完整，不能据此确认完整列表无结果。

最近核验时间：2026-11-05T04:06+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- Scale V2 榜单和 NVIDIA 模型卡均未找到 Nemotron 3 Ultra 的 SWE-bench Pro V2 行。NVIDIA 已有 SWE-Bench Verified 是不同 benchmark。

最近核验时间：2026-11-05T04:06+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 56.4
- metric: success rate
- version: 2.1
- source: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- date: 2026-06-04
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- 官方 v4 动态榜单当前模型和分数表为空，无法确认 Nemotron 是否有 v4 行。本地已有 Terminal-Bench 2.1 56.4（success rate），不映射到 v4。

尚未解决的问题：
- 官方 Terminal-Bench 4 动态榜单无法读取完整结果。

最近核验时间：2026-11-05T04:06+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- 官方 Science 0.1 结果页列出的模型中未找到 Nemotron 3 Ultra 的精确成绩。

最近核验时间：2026-11-05T04:06+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- NVIDIA 卡未列 AutomationBench。Zapier 页面标示 1.0.6，但可见前 10 行后仍有 119 行折叠，不能确认完整列表是否含 Nemotron。

尚未解决的问题：
- Zapier 官方排行榜其余 119 行不可见。

最近核验时间：2026-11-05T04:06+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- [OSWorld V2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 官方模型卡将精确 BF16 型号列为文本输入/文本输出；OSWorld 需要图像/屏幕观测，此型号不支持图像输入。

最近核验时间：2026-11-05T04:06+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- [Chartography evaluation repository](https://github.com/surge-ai/chartography)

研究备注：
- 官方模型卡确认此型号只支持文本输入；Chartography 需要读取图表图像。Surge 页上的 Nemotron 记录属于其他榜单区块，不是 Chartography。

最近核验时间：2026-11-05T04:06+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 26.7
- metric: accuracy
- variant: no tools
- source: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- date: 2026-06-04
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 37.4
- metric: accuracy
- variant: with tools
- source: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- date: 2026-06-04
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- 模型卡将其称为 HLE，使用 `cais/hle` 数据集；本地已有 26.7% no tools 与 37.4% with tools 两行，均为 accuracy，分别保留。本轮未改这两条历史成绩。

最近核验时间：2026-11-05T04:06+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 12
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/nvidia-nemotron-3-ultra-550b-a55b](https://artificialanalysis.ai/models/nvidia-nemotron-3-ultra-550b-a55b)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Nemotron 3 Ultra profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-ultra-550b-a55b)

研究备注：
- Artificial Analysis 当前模型页报告 Index score 12、version 5.0.1；原始分数已写入 TOML。仓库定义版本是 5.0，严格版本不匹配，因此不计入精确 V5 覆盖率。

尚未解决的问题：
- 需确认本地定义 5.0 是否应接受官方 V5.0.1；本次保留原版本，不修改 benchmark 定义。

最近核验时间：2026-11-05T04:06+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1021
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- variant: Reasoning; CI -17/+17
- harness: Stirrup agentic loop (shell and web browsing)
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 官方榜单列出 Nemotron 3 Ultra 550B A55B (Reasoning) 1021 Elo，CI −17/+17。该评测为 220 个任务、44 种职业、9 个行业，经 Stirrup agent loop（shell 与网页浏览）进行。对应原始成绩已写入 TOML；未设置来源未报告的评测日期或 effort。

最近核验时间：2026-11-05T04:06+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [NVIDIA Nemotron 3 Ultra BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

研究备注：
- 当前公开 Vals v2.2 榜单未列 Nemotron 3 Ultra 550B A55B；榜中其他 Nemotron 型号和 NVIDIA 卡中的 Vals Financial Agent 1.1 均不是目标记录。

尚未解决的问题：
- 当前 Vals 页为所展示模型列表，未出现不能证明历史上不存在该型号结果。

最近核验时间：2026-11-05T04:06+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Nemotron 3 Ultra profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-ultra-550b-a55b"
        }
      ],
      "notes": [
        "Artificial Analysis 当前模型页报告 Index score 12、version 5.0.1；原始分数已写入 TOML。仓库定义版本是 5.0，严格版本不匹配，因此不计入精确 V5 覆盖率。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认本地定义 5.0 是否应接受官方 V5.0.1；本次保留原版本，不修改 benchmark 定义。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "NVIDIA 卡未列 AutomationBench。Zapier 页面标示 1.0.6，但可见前 10 行后仍有 119 行折叠，不能确认完整列表是否含 Nemotron。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 官方排行榜其余 119 行不可见。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        },
        {
          "label": "Chartography evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "官方模型卡确认此型号只支持文本输入；Chartography 需要读取图表图像。Surge 页上的 Nemotron 记录属于其他榜单区块，不是 Chartography。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "DeepSWE 榜单可读页面当前仅展示 21/28 配置，未见 Nemotron 3 Ultra；未找到可核实的分数、effort、harness 或评测日期。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单可见配置不完整，不能据此确认完整列表无结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "官方榜单列出 Nemotron 3 Ultra 550B A55B (Reasoning) 1021 Elo，CI −17/+17。该评测为 220 个任务、44 种职业、9 个行业，经 Stirrup agent loop（shell 与网页浏览）进行。对应原始成绩已写入 TOML；未设置来源未报告的评测日期或 effort。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "模型卡将其称为 HLE，使用 `cais/hle` 数据集；本地已有 26.7% no tools 与 37.4% with tools 两行，均为 accuracy，分别保留。本轮未改这两条历史成绩。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        },
        {
          "label": "OSWorld V2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "官方模型卡将精确 BF16 型号列为文本输入/文本输出；OSWorld 需要图像/屏幕观测，此型号不支持图像输入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "Scale V2 榜单和 NVIDIA 模型卡均未找到 Nemotron 3 Ultra 的 SWE-bench Pro V2 行。NVIDIA 已有 SWE-Bench Verified 是不同 benchmark。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "官方 Science 0.1 结果页列出的模型中未找到 Nemotron 3 Ultra 的精确成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "官方 v4 动态榜单当前模型和分数表为空，无法确认 Nemotron 是否有 v4 行。本地已有 Terminal-Bench 2.1 56.4（success rate），不映射到 v4。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 Terminal-Bench 4 动态榜单无法读取完整结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:06+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "NVIDIA Nemotron 3 Ultra BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
        }
      ],
      "notes": [
        "当前公开 Vals v2.2 榜单未列 Nemotron 3 Ultra 550B A55B；榜中其他 Nemotron 型号和 NVIDIA 卡中的 Vals Financial Agent 1.1 均不是目标记录。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前 Vals 页为所展示模型列表，未出现不能证明历史上不存在该型号结果。"
      ]
    }
  },
  "existing_records": 11,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:06+08:00",
  "model_id": "nvidia/nemotron-3-ultra-550b-a55b",
  "model_notes": [
    "本地模型为 NVIDIA Nemotron 3 Ultra 550B A55B BF16；官方模型卡确认 2026-06-04 发布。已有 11 条记录保留，目标 HLE 两条已存在。",
    "新增 GDPval-AA v2.1 1021 Elo（CI -17/+17），以官方 AA 榜单中 Reasoning 配置和 Stirrup shell/web harness 为准；未把 NVIDIA 的通用 GDPval 46.7 wins-or-ties 记录当成 GDPval-AA。",
    "新增 AA Index 12，来源版本 5.0.1；本地目标定义版本 5.0，故该原始记录保留但映射待复核。",
    "NVIDIA HF 自动评测区另显示 SWE-Bench Verified 71.9，而 TOML 历史行为 70.7；两处评测条件未确认，本轮不覆盖历史行。"
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
