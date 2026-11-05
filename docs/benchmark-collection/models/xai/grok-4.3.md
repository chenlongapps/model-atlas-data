# Grok 4.3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-4.3
- 模型名称：Grok 4.3
- 发布日期：2026-04-17
- 最近检查时间：2026-11-05T08:50+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：4
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地原有 AA Intelligence Index 53 / v4.0 与 generic GDPval-AA 1500 Elo 记录保留；不映射到目标 V5/V2.1。GDPval 行 date=2026-04-30 与来源文章发布日期一致，但文章未说明评测日期，该旧字段暂保留并标记复核。
- 新增 Surge Chartography 榜单原始分数 12.9（High reasoning）；排行榜行未标 reducer，因此不填写 metric，映射待复核。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T08:50+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:50+08:00 |
| terminal-bench-v4 | 待核实 | — | [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3), [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:50+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3), [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:50+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench project](https://github.com/zapier/AutomationBench) | 2026-11-05T08:50+08:00 |
| osworld-v2.1 | 待核实 | — | [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3), [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/), [OSWorld V2.1 release notes](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T08:50+08:00 |
| chartography | 待核实 | 12.9 (dataset=Chartography full task set (100 tasks); variant=High reasoning; harness=Inspect AI Chartography harness; leaderboard configuration: 10 runs per task, Gemini 3.5 Flash judge) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Official Chartography benchmark harness and scoring protocol](https://github.com/surge-ai/chartography) | 2026-11-05T08:50+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis Grok 4.3 model profile](https://artificialanalysis.ai/models/grok-4-3), [Artificial Analysis Grok 4.3 release article](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing), [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | 53 (metric=index score; version=4.0) | [Artificial Analysis Grok 4.3 exact-model profile](https://artificialanalysis.ai/models/grok-4-3), [Artificial Analysis Intelligence Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Grok 4.3 release article](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing) | 2026-11-05T08:50+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1500 (metric=Elo) | [GDPval-AA V2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Grok 4.3 release article](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing) | 2026-11-05T08:50+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Grok 4.3 Vals model profile](https://www.vals.ai/models/xai_grok-4-3) | 2026-11-05T08:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- No exact Grok 4.3 DeepSWE v1.1 score was verified; current public leaderboard displays only part of the model/configuration set.

尚未解决的问题：
- No exact Grok 4.3 DeepSWE v1.1 score was verified; current public leaderboard displays only part of the model/configuration set.

最近核验时间：2026-11-05T08:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- No directly verifiable Grok 4.3 SWE-bench Pro V2 score was found. Do not map other Grok versions or unspecified Pro variants.

尚未解决的问题：
- No directly verifiable Grok 4.3 SWE-bench Pro V2 score was found. Do not map other Grok versions or unspecified Pro variants.

最近核验时间：2026-11-05T08:50+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3)
- [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- No directly verifiable Grok 4.3 Terminal-Bench 4 score was found; nearby versions/configurations do not establish v4.0.

尚未解决的问题：
- No directly verifiable Grok 4.3 Terminal-Bench 4 score was found; nearby versions/configurations do not establish v4.0.

最近核验时间：2026-11-05T08:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3)
- [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- No exact Grok 4.3 Terminal-Bench Science v0.1 score was verified.

尚未解决的问题：
- No exact Grok 4.3 Terminal-Bench Science v0.1 score was verified.

最近核验时间：2026-11-05T08:50+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench project](https://github.com/zapier/AutomationBench)

研究备注：
- Exact model supports function calling and the task is applicable. The visible leaderboard subset does not verify a Grok 4.3 score.

尚未解决的问题：
- Exact model supports function calling and the task is applicable. The visible leaderboard subset does not verify a Grok 4.3 score.

最近核验时间：2026-11-05T08:50+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [xAI Grok 4.3 model documentation](https://docs.x.ai/developers/models/grok-4.3)
- [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 release notes](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Exact model supports image input and tools, so the task is applicable; the current OSWorld page did not show a readable exact-model V2.1 row.

尚未解决的问题：
- Exact model supports image input and tools, so the task is applicable; the current OSWorld page did not show a readable exact-model V2.1 row.

最近核验时间：2026-11-05T08:50+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 12.9
- dataset: Chartography full task set (100 tasks)
- variant: High reasoning
- harness: Inspect AI Chartography harness; leaderboard configuration: 10 runs per task, Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Official Chartography benchmark harness and scoring protocol](https://github.com/surge-ai/chartography)

研究备注：
- Surge directly lists Grok 4.3 (High reasoning) at 12.9%. The leaderboard row does not specify which reducer is shown. The official harness reports accuracy/mean and Pass@10 (among other reducers), so the raw score is preserved without metric and is not counted toward mapped coverage. No evaluation date or semantic version is published.

尚未解决的问题：
- Surge directly lists Grok 4.3 (High reasoning) at 12.9%. The leaderboard row does not specify which reducer is shown. The official harness reports accuracy/mean and Pass@10 (among other reducers), so the raw score is preserved without metric and is not counted toward mapped coverage. No evaluation date or semantic version is published.

最近核验时间：2026-11-05T08:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Grok 4.3 model profile](https://artificialanalysis.ai/models/grok-4-3)
- [Artificial Analysis Grok 4.3 release article](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)
- [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Reviewed the exact-model profile, release article and HLE page; no exact Grok 4.3 raw HLE result was verified. HLE-Diamond under AA Index V5 is a different dataset from original HLE.

尚未解决的问题：
- Reviewed the exact-model profile, release article and HLE page; no exact Grok 4.3 raw HLE result was verified. HLE-Diamond under AA Index V5 is a different dataset from original HLE.

最近核验时间：2026-11-05T08:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 53
- metric: index score
- version: 4.0
- source: [https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)
- date: 2026-04-30
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Grok 4.3 exact-model profile](https://artificialanalysis.ai/models/grok-4-3)
- [Artificial Analysis Intelligence Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Grok 4.3 release article](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)

研究备注：
- Current exact-model profile shows Intelligence Index N/A in its current V5.0.1 section. The local score 53 is version 4.0 and is not mapped to V5.

最近核验时间：2026-11-05T08:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1500
- metric: Elo
- source: [https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)
- date: 2026-04-30
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [GDPval-AA V2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Grok 4.3 release article](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)

研究备注：
- Local TOML has a generic GDPval-AA Elo 1500 row from the April release article; it is not version-labeled V2.1. The current V2.1 page has no direct Grok 4.3 row. A search-index candidate was not visible in the opened primary page, so it is not added or treated as a verified conflict. Existing date equals article publication date; the source does not establish that it is the evaluation date, so this legacy field is flagged for later review and retained unchanged.

尚未解决的问题：
- Local TOML has a generic GDPval-AA Elo 1500 row from the April release article; it is not version-labeled V2.1. The current V2.1 page has no direct Grok 4.3 row. A search-index candidate was not visible in the opened primary page, so it is not added or treated as a verified conflict. Existing date equals article publication date; the source does not establish that it is the evaluation date, so this legacy field is flagged for later review and retained unchanged.

最近核验时间：2026-11-05T08:50+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Grok 4.3 Vals model profile](https://www.vals.ai/models/xai_grok-4-3)

研究备注：
- Current V2.2 board displays a selected latest/top/frontier set and does not verify Grok 4.3. Older Vals v2, v1.1, and v1 results are not mapped to V2.2.

尚未解决的问题：
- Current V2.2 board displays a selected latest/top/frontier set and does not verify Grok 4.3. Older Vals v2, v1.1, and v1 results are not mapped to V2.2.

最近核验时间：2026-11-05T08:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.3 exact-model profile",
          "url": "https://artificialanalysis.ai/models/grok-4-3"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Grok 4.3 release article",
          "url": "https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing"
        }
      ],
      "notes": [
        "Current exact-model profile shows Intelligence Index N/A in its current V5.0.1 section. The local score 53 is version 4.0 and is not mapped to V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.3 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.3"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench project",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Exact model supports function calling and the task is applicable. The visible leaderboard subset does not verify a Grok 4.3 score."
      ],
      "status": "待核实",
      "unresolved": [
        "Exact model supports function calling and the task is applicable. The visible leaderboard subset does not verify a Grok 4.3 score."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Official Chartography benchmark harness and scoring protocol",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge directly lists Grok 4.3 (High reasoning) at 12.9%. The leaderboard row does not specify which reducer is shown. The official harness reports accuracy/mean and Pass@10 (among other reducers), so the raw score is preserved without metric and is not counted toward mapped coverage. No evaluation date or semantic version is published."
      ],
      "status": "待核实",
      "unresolved": [
        "Surge directly lists Grok 4.3 (High reasoning) at 12.9%. The leaderboard row does not specify which reducer is shown. The official harness reports accuracy/mean and Pass@10 (among other reducers), so the raw score is preserved without metric and is not counted toward mapped coverage. No evaluation date or semantic version is published."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.3 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.3"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "No exact Grok 4.3 DeepSWE v1.1 score was verified; current public leaderboard displays only part of the model/configuration set."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Grok 4.3 DeepSWE v1.1 score was verified; current public leaderboard displays only part of the model/configuration set."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA V2.1 official leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Grok 4.3 release article",
          "url": "https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing"
        }
      ],
      "notes": [
        "Local TOML has a generic GDPval-AA Elo 1500 row from the April release article; it is not version-labeled V2.1. The current V2.1 page has no direct Grok 4.3 row. A search-index candidate was not visible in the opened primary page, so it is not added or treated as a verified conflict. Existing date equals article publication date; the source does not establish that it is the evaluation date, so this legacy field is flagged for later review and retained unchanged."
      ],
      "status": "待核实",
      "unresolved": [
        "Local TOML has a generic GDPval-AA Elo 1500 row from the April release article; it is not version-labeled V2.1. The current V2.1 page has no direct Grok 4.3 row. A search-index candidate was not visible in the opened primary page, so it is not added or treated as a verified conflict. Existing date equals article publication date; the source does not establish that it is the evaluation date, so this legacy field is flagged for later review and retained unchanged."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.3 model profile",
          "url": "https://artificialanalysis.ai/models/grok-4-3"
        },
        {
          "label": "Artificial Analysis Grok 4.3 release article",
          "url": "https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing"
        },
        {
          "label": "Humanity's Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Reviewed the exact-model profile, release article and HLE page; no exact Grok 4.3 raw HLE result was verified. HLE-Diamond under AA Index V5 is a different dataset from original HLE."
      ],
      "status": "待核实",
      "unresolved": [
        "Reviewed the exact-model profile, release article and HLE page; no exact Grok 4.3 raw HLE result was verified. HLE-Diamond under AA Index V5 is a different dataset from original HLE."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.3 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.3"
        },
        {
          "label": "OSWorld V2.1 benchmark",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 release notes",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Exact model supports image input and tools, so the task is applicable; the current OSWorld page did not show a readable exact-model V2.1 row."
      ],
      "status": "待核实",
      "unresolved": [
        "Exact model supports image input and tools, so the task is applicable; the current OSWorld page did not show a readable exact-model V2.1 row."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.3 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.3"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "No directly verifiable Grok 4.3 SWE-bench Pro V2 score was found. Do not map other Grok versions or unspecified Pro variants."
      ],
      "status": "待核实",
      "unresolved": [
        "No directly verifiable Grok 4.3 SWE-bench Pro V2 score was found. Do not map other Grok versions or unspecified Pro variants."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.3 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.3"
        },
        {
          "label": "Terminal-Bench Science benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "No exact Grok 4.3 Terminal-Bench Science v0.1 score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Grok 4.3 Terminal-Bench Science v0.1 score was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.3 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-4.3"
        },
        {
          "label": "Terminal-Bench 4.0 benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "No directly verifiable Grok 4.3 Terminal-Bench 4 score was found; nearby versions/configurations do not establish v4.0."
      ],
      "status": "待核实",
      "unresolved": [
        "No directly verifiable Grok 4.3 Terminal-Bench 4 score was found; nearby versions/configurations do not establish v4.0."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:50+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Grok 4.3 Vals model profile",
          "url": "https://www.vals.ai/models/xai_grok-4-3"
        }
      ],
      "notes": [
        "Current V2.2 board displays a selected latest/top/frontier set and does not verify Grok 4.3. Older Vals v2, v1.1, and v1 results are not mapped to V2.2."
      ],
      "status": "待核实",
      "unresolved": [
        "Current V2.2 board displays a selected latest/top/frontier set and does not verify Grok 4.3. Older Vals v2, v1.1, and v1 results are not mapped to V2.2."
      ]
    }
  },
  "existing_records": 4,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:50+08:00",
  "model_id": "xai/grok-4.3",
  "model_notes": [
    "本地原有 AA Intelligence Index 53 / v4.0 与 generic GDPval-AA 1500 Elo 记录保留；不映射到目标 V5/V2.1。GDPval 行 date=2026-04-30 与来源文章发布日期一致，但文章未说明评测日期，该旧字段暂保留并标记复核。",
    "新增 Surge Chartography 榜单原始分数 12.9（High reasoning）；排行榜行未标 reducer，因此不填写 metric，映射待复核。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
