# Mistral Medium 3.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/mistral-medium-2604
- 模型名称：Mistral Medium 3.5
- 发布日期：2026-04-28
- 最近检查时间：2026-11-05T06:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：2
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- 官方模型卡将本模型对应的产品型号标为 Mistral Medium 3.5、版本 v26.04、API ID mistral-medium-3-5，并列出发布日期 2026-04-28；本地 release_date 已由 2026-04-29 修正。Mistral Legal Center 另列 2026-04-29，日期差异留档。
- AA 成绩来源直接使用 Mistral Medium 3.5 产品名，官方模型卡、v26.04 与本地 Hugging Face 权重链接支持将结果归到该固定型号。GDPval 761/769 读数差异未解决。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:53+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:53+08:00 |
| terminal-bench-v4 | 已收录 | 0 (metric=task resolution rate; version=4.0; dataset=66 tasks; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5), [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:53+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 0 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4), [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:53+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T06:53+08:00 |
| osworld-v2.1 | 待核实 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository and releases](https://github.com/xlang-ai/OSWorld-V2/releases) | 2026-11-05T06:53+08:00 |
| chartography | 未找到 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:53+08:00 |
| humanitys-last-exam | 已收录 | 14 (metric=accuracy; dataset=2,158 text-only questions from the May 2025 HLE revision (2,500 questions total); variant=pass@1; GPT-5.6 Luna (medium) equality checker; harness=Artificial Analysis HLE evaluation) | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1), [Humanity’s Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 5 (metric=index score; version=5.0.1) | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Artificial Analysis Mistral Medium 3.5 model page](https://artificialanalysis.ai/models/mistral-medium-3-5), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:53+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5), [Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1), [GDPval-AA v2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:53+08:00 |
| vals-index-v2.2 | 未找到 | — | [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 榜单当前仅展示 21/28 models、57/70 configs；未显示精确型号，不能据此认定未找到。

尚未解决的问题：
- 需核查榜单未显示的配置中是否有 Mistral Medium 3.5 精确结果。

最近核验时间：2026-11-05T06:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 当前公开 V2 榜单未见精确型号行；本地 SWE-Bench Verified 77.6 不属于 Pro V2。

最近核验时间：2026-11-05T06:53+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 0
- metric: task resolution rate
- version: 4.0
- dataset: 66 tasks
- variant: pass@1 averaged over three repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- AA 比较页直接列出 Mistral Medium 3.5 为 0%；方法为 66 tasks、mini-swe-agent、pass@1 每任务三次重复。

最近核验时间：2026-11-05T06:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 0
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: pass@1 averaged over three repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4)
- [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 比较页直接列出 Mistral Medium 3.5 为 0%；方法为版本 0.1.0、70 tasks、mini-swe-agent、pass@1 每任务三次重复。

最近核验时间：2026-11-05T06:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- Zapier 当前榜单可见前 10 项，另有 119 条折叠；未发现可读的完整型号表。

尚未解决的问题：
- 需检查折叠条目中是否有固定 Mistral Medium 3.5 成绩。

最近核验时间：2026-11-05T06:53+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository and releases](https://github.com/xlang-ai/OSWorld-V2/releases)

研究备注：
- 官方 OSWorld V2 页面当前无法从可读榜单确认该精确型号。

尚未解决的问题：
- 需确认动态榜单完整行和模型评测配置。

最近核验时间：2026-11-05T06:53+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 当前公开 Chartography 榜单未见 Mistral Medium 3.5 精确型号；未映射其他 Mistral 型号。

最近核验时间：2026-11-05T06:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 14
- metric: accuracy
- dataset: 2,158 text-only questions from the May 2025 HLE revision (2,500 questions total)
- variant: pass@1; GPT-5.6 Luna (medium) equality checker
- harness: Artificial Analysis HLE evaluation
- source: [https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1)
- [Humanity’s Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 比较页直接列出 14%；方法资料说明此分数对应 2,158 道 text-only 题、pass@1，使用 GPT-5.6 Luna (medium) equality checker；没有评测日期。

最近核验时间：2026-11-05T06:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 5
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/mistral-medium-3-5](https://artificialanalysis.ai/models/mistral-medium-3-5)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Artificial Analysis Mistral Medium 3.5 model page](https://artificialanalysis.ai/models/mistral-medium-3-5)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前 AA 模型页直接显示分数 5，并在同页标明 Intelligence Index v5.0.1。

最近核验时间：2026-11-05T06:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- [Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1)
- [GDPval-AA v2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA 当前直接比较页显示 761 Elo；此前同一官方页面搜索快照出现 769。为避免择取未解释的不同读数，未新增 GDPval 记录。

尚未解决的问题：
- 需确认 761 与 769 的差异是否为官方修订或评测条件变化。

最近核验时间：2026-11-05T06:53+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Medium 3.5 v26.04 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前官方 Vals Index v2.2 页面未列出 Mistral Medium 3.5。

最近核验时间：2026-11-05T06:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 model page",
          "url": "https://artificialanalysis.ai/models/mistral-medium-3-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前 AA 模型页直接显示分数 5，并在同页标明 Intelligence Index v5.0.1。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Zapier 当前榜单可见前 10 项，另有 119 条折叠；未发现可读的完整型号表。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查折叠条目中是否有固定 Mistral Medium 3.5 成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "当前公开 Chartography 榜单未见 Mistral Medium 3.5 精确型号；未映射其他 Mistral 型号。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 榜单当前仅展示 21/28 models、57/70 configs；未显示精确型号，不能据此认定未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查榜单未显示的配置中是否有 Mistral Medium 3.5 精确结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Step 5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1"
        },
        {
          "label": "GDPval-AA v2.1 official leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA 当前直接比较页显示 761 Elo；此前同一官方页面搜索快照出现 769。为避免择取未解释的不同读数，未新增 GDPval 记录。"
      ],
      "status": "冲突",
      "unresolved": [
        "需确认 761 与 769 的差异是否为官方修订或评测条件变化。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1"
        },
        {
          "label": "Humanity’s Last Exam evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 比较页直接列出 14%；方法资料说明此分数对应 2,158 道 text-only 题、pass@1，使用 GPT-5.6 Luna (medium) equality checker；没有评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository and releases",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        }
      ],
      "notes": [
        "官方 OSWorld V2 页面当前无法从可读榜单确认该精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认动态榜单完整行和模型评测配置。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "当前公开 V2 榜单未见精确型号行；本地 SWE-Bench Verified 77.6 不属于 Pro V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4"
        },
        {
          "label": "Terminal-Bench Science 0.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 比较页直接列出 Mistral Medium 3.5 为 0%；方法为版本 0.1.0、70 tasks、mini-swe-agent、pass@1 每任务三次重复。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Step 5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        },
        {
          "label": "Terminal-Bench 4.0 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "AA 比较页直接列出 Mistral Medium 3.5 为 0%；方法为 66 tasks、mini-swe-agent、pass@1 每任务三次重复。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 v26.04 model card",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前官方 Vals Index v2.2 页面未列出 Mistral Medium 3.5。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 2,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:53+08:00",
  "model_id": "mistral/mistral-medium-2604",
  "model_notes": [
    "官方模型卡将本模型对应的产品型号标为 Mistral Medium 3.5、版本 v26.04、API ID mistral-medium-3-5，并列出发布日期 2026-04-28；本地 release_date 已由 2026-04-29 修正。Mistral Legal Center 另列 2026-04-29，日期差异留档。",
    "AA 成绩来源直接使用 Mistral Medium 3.5 产品名，官方模型卡、v26.04 与本地 Hugging Face 权重链接支持将结果归到该固定型号。GDPval 761/769 读数差异未解决。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
