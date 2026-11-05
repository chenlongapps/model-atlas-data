# Mistral Medium 3.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/mistral-medium-3-5
- 模型名称：Mistral Medium 3.5
- 发布日期：2026-04-28
- 最近检查时间：2026-11-05T06:41+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- 官方模型文档和 changelog 将精确 ID mistral-medium-3-5 的发布日列为 2026-04-28；本地 TOML 原值 2026-04-30 已更正为 2026-04-28。Mistral 法律生命周期页另列 2026-04-29，日期来源差异保留在此。
- 新增四条 AA 直接核实记录：Terminal-Bench 4.0、Terminal-Bench-Science 0.1、原始 HLE 文本子集、Artificial Analysis Intelligence Index v5.0.1。GDPval-AA 两种读数冲突，未写入。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:41+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:41+08:00 |
| terminal-bench-v4 | 已收录 | 0 (metric=task resolution rate; version=4.0; dataset=66 tasks; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AA Mistral Medium 3.5 vs Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5), [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:41+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 0 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AA Mistral Medium 3.5 vs Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4), [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:41+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T06:41+08:00 |
| osworld-v2.1 | 待核实 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:41+08:00 |
| chartography | 未找到 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:41+08:00 |
| humanitys-last-exam | 已收录 | 14 (metric=accuracy; dataset=2,158 text-only questions from the May 2025 HLE revision (2,500 questions total); variant=pass@1; GPT-5.6 Luna (medium) equality checker; harness=Artificial Analysis HLE evaluation) | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AA Mistral Medium 3.5 vs GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1), [Humanity's Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:41+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 5 (metric=index score; version=5.0.1) | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AA Mistral Medium 3.5 model page](https://artificialanalysis.ai/models/mistral-medium-3-5), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:41+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [AA Mistral Medium 3.5 vs Step 5 GDPval comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5), [AA Mistral Medium 3.5 vs GLM-5.1 GDPval comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1), [GDPval-AA v2.1 evaluation methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:41+08:00 |
| vals-index-v2.2 | 未找到 | — | [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:41+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 本地模型 ID 与 Mistral 官方 API ID mistral-medium-3-5 精确匹配；DeepSWE 当前榜单仅展示 21/28 models、57/70 configs，当前视图未见该型号。

尚未解决的问题：
- 需核实榜单未展示配置是否有精确型号成绩。

最近核验时间：2026-11-05T06:41+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查 Scale 当前 V2 公榜未见 Mistral Medium 3.5 精确行；未映射 Mistral Large、其他 Medium 版本或旧版 Pro 结果。

最近核验时间：2026-11-05T06:41+08:00

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
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AA Mistral Medium 3.5 vs Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- AA 比较页将精确型号 Mistral Medium 3.5 列为 Terminal-Bench 4.0 0%。其官方方法为 66 tasks、mini-swe-agent、pass@1 averaged over three repeats；具体评测日期和 effort 未公布。

最近核验时间：2026-11-05T06:41+08:00

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
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AA Mistral Medium 3.5 vs Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4)
- [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 比较页将精确型号列为 Terminal-Bench-Science 0.1 0%。其官方方法为版本 0.1.0、70 tasks、mini-swe-agent、pass@1 averaged over three repeats；具体评测日期和 effort 未公布。

最近核验时间：2026-11-05T06:41+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- Mistral Medium 3.5 支持工具工作流；Zapier 1.0.6 榜单额外 119 条当前折叠，无法确认该型号是否出现。AA 的 AutomationBench-AA 是不同的 AA 配置，不映射。

尚未解决的问题：
- 需核查完整 Zapier 1.0.6 榜单是否有该精确型号及成绩。

最近核验时间：2026-11-05T06:41+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型支持图像输入和工具调用，但当前 OSWorld 动态榜单视图未确认精确型号、版本与测试配置。

尚未解决的问题：
- 需核查 OSWorld 2.1 官方其他数据集/版本视图或验证记录。

最近核验时间：2026-11-05T06:41+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Surge 官方榜单当前未见 Mistral Medium 3.5 精确行；可见的 Mistral Large 3 9% 属于不同模型，不映射。

最近核验时间：2026-11-05T06:41+08:00

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
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AA Mistral Medium 3.5 vs GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1)
- [Humanity's Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 比较页给出精确型号 14% accuracy。该分数使用 2,158 道文本题（2025-05 HLE 2,500 题修订版的文本子集），pass@1，并由 GPT-5.6 Luna (medium) 做 equality check；不是全量 2,500 题得分。未公布 effort 或评测日期。

最近核验时间：2026-11-05T06:41+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 5
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/mistral-medium-3-5](https://artificialanalysis.ai/models/mistral-medium-3-5)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AA Mistral Medium 3.5 model page](https://artificialanalysis.ai/models/mistral-medium-3-5)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 精确型号页报告 Artificial Analysis Intelligence Index 5 分，页面标示版本 v5.0.1；没有报告模型特定 effort 或评测日期。

最近核验时间：2026-11-05T06:41+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [AA Mistral Medium 3.5 vs Step 5 GDPval comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- [AA Mistral Medium 3.5 vs GLM-5.1 GDPval comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1)
- [GDPval-AA v2.1 evaluation methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA GDPval-AA v2.1 同型号结果存在 761 和 769 两个读数：直接打开的两个官方比较页显示 761，而相同页面的搜索索引响应显示 769；未找到修订说明或可确认的评测日期。没有将任一读数写入 TOML。

尚未解决的问题：
- 需核实 AA 是否修订过该 GDPval-AA v2.1 Elo，以及哪个读数对应当前已发布结果。

最近核验时间：2026-11-05T06:41+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Medium 3.5 official model documentation](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 当前页面未列 Mistral Medium 3.5；页面仅展示部分模型，缺席不能证明从未评测。

最近核验时间：2026-11-05T06:41+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AA Mistral Medium 3.5 model page",
          "url": "https://artificialanalysis.ai/models/mistral-medium-3-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 精确型号页报告 Artificial Analysis Intelligence Index 5 分，页面标示版本 v5.0.1；没有报告模型特定 effort 或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Mistral Medium 3.5 支持工具工作流；Zapier 1.0.6 榜单额外 119 条当前折叠，无法确认该型号是否出现。AA 的 AutomationBench-AA 是不同的 AA 配置，不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查完整 Zapier 1.0.6 榜单是否有该精确型号及成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Surge 官方榜单当前未见 Mistral Medium 3.5 精确行；可见的 Mistral Large 3 9% 属于不同模型，不映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "本地模型 ID 与 Mistral 官方 API ID mistral-medium-3-5 精确匹配；DeepSWE 当前榜单仅展示 21/28 models、57/70 configs，当前视图未见该型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实榜单未展示配置是否有精确型号成绩。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AA Mistral Medium 3.5 vs Step 5 GDPval comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        },
        {
          "label": "AA Mistral Medium 3.5 vs GLM-5.1 GDPval comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1"
        },
        {
          "label": "GDPval-AA v2.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA GDPval-AA v2.1 同型号结果存在 761 和 769 两个读数：直接打开的两个官方比较页显示 761，而相同页面的搜索索引响应显示 769；未找到修订说明或可确认的评测日期。没有将任一读数写入 TOML。"
      ],
      "status": "冲突",
      "unresolved": [
        "需核实 AA 是否修订过该 GDPval-AA v2.1 Elo，以及哪个读数对应当前已发布结果。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AA Mistral Medium 3.5 vs GLM-5.1 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1"
        },
        {
          "label": "Humanity's Last Exam evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 比较页给出精确型号 14% accuracy。该分数使用 2,158 道文本题（2025-05 HLE 2,500 题修订版的文本子集），pass@1，并由 GPT-5.6 Luna (medium) 做 equality check；不是全量 2,500 题得分。未公布 effort 或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型支持图像输入和工具调用，但当前 OSWorld 动态榜单视图未确认精确型号、版本与测试配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查 OSWorld 2.1 官方其他数据集/版本视图或验证记录。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查 Scale 当前 V2 公榜未见 Mistral Medium 3.5 精确行；未映射 Mistral Large、其他 Medium 版本或旧版 Pro 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AA Mistral Medium 3.5 vs Mistral Small 4 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4"
        },
        {
          "label": "Terminal-Bench Science 0.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 比较页将精确型号列为 Terminal-Bench-Science 0.1 0%。其官方方法为版本 0.1.0、70 tasks、mini-swe-agent、pass@1 averaged over three repeats；具体评测日期和 effort 未公布。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "AA Mistral Medium 3.5 vs Step 5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        },
        {
          "label": "Terminal-Bench 4.0 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "AA 比较页将精确型号 Mistral Medium 3.5 列为 Terminal-Bench 4.0 0%。其官方方法为 66 tasks、mini-swe-agent、pass@1 averaged over three repeats；具体评测日期和 effort 未公布。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "Mistral Medium 3.5 official model documentation",
          "url": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 当前页面未列 Mistral Medium 3.5；页面仅展示部分模型，缺席不能证明从未评测。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:41+08:00",
  "model_id": "mistral/mistral-medium-3-5",
  "model_notes": [
    "官方模型文档和 changelog 将精确 ID mistral-medium-3-5 的发布日列为 2026-04-28；本地 TOML 原值 2026-04-30 已更正为 2026-04-28。Mistral 法律生命周期页另列 2026-04-29，日期来源差异保留在此。",
    "新增四条 AA 直接核实记录：Terminal-Bench 4.0、Terminal-Bench-Science 0.1、原始 HLE 文本子集、Artificial Analysis Intelligence Index v5.0.1。GDPval-AA 两种读数冲突，未写入。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
