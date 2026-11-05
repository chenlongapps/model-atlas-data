# Beam 1.0 501B A23B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：reflection/beam-1.0-501b-a23b
- 模型名称：Beam 1.0 501B A23B
- 发布日期：2026-10-05
- 最近检查时间：2026-11-04T04:48+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 收集前已有成绩数量：7
- 当前已收录的对应成绩数量：5

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 43.3 (metric=pass@1; version=1.1; dataset=datacurve/deep-swe; variant=BF16) | [HF machine-readable evaluation result](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml), [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/) | 2026-11-04T04:48+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B), [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/) | 2026-11-04T04:48+08:00 |
| terminal-bench-v4 | 已收录 | 80.1 (version=2.1; dataset=harborframework/terminal-bench-2.1; variant=BF16); 3.0 (metric=task resolution rate; version=4.0.0; dataset=harborframework/terminal-bench; variant=pass@1 averaged over 3 repeats; harness=mini-swe-agent) | [HF Terminal-Bench 4 evaluation result](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-4.0.yaml), [Artificial Analysis Terminal-Bench 4 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T04:48+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 0.5 (metric=task resolution rate; version=0.1.0; dataset=harborframework/terminal-bench-science; variant=pass@1 averaged over 3 repeats; harness=mini-swe-agent) | [HF Terminal-Bench Science evaluation result](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-science.yaml), [Artificial Analysis Terminal-Bench Science method](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T04:48+08:00 |
| automationbench-v1.0.6 | 冲突 | 39.3 (dataset=public; variant=BF16) | [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench v1.0.6 changelog](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md), [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/) | 2026-11-04T04:48+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld v2.1 release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [OSWorld v2.1 official site](https://osworld-v2.xlang.ai/), [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B) | 2026-11-04T04:48+08:00 |
| chartography | 待核实 | — | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography protocol paper](https://arxiv.org/html/2608.10677), [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B) | 2026-11-04T04:48+08:00 |
| humanitys-last-exam | 冲突 | 36.0 (metric=accuracy; dataset=cais/hle; variant=BF16; no tools); 51.1 (metric=accuracy; dataset=cais/hle; variant=BF16; with tools) | [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B), [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/), [HLE official leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T04:48+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 18 (metric=index score; version=5.0) | [Artificial Analysis Beam model page](https://artificialanalysis.ai/models/reflection-beam) | 2026-11-04T04:48+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA evaluation and leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T04:48+08:00 |
| vals-index-v2.2 | 已收录 | 43.42 (metric=performance score; version=2.2) | [Vals Index official benchmark page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T04:48+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 43.3
- metric: pass@1
- version: 1.1
- dataset: datacurve/deep-swe
- variant: BF16
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml)
- date: 2026-10-07
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [HF machine-readable evaluation result](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml)
- [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/)

研究备注：
- 保留官方 HF 评测记录中注明的 BF16 DeepSWE 1.1 分数 43.3%；后续 Reflection 文章另报 44.4%，未披露足以确认两者条件一致的信息。

尚未解决的问题：
- Reflection 后续文章报告 44.4%，而 HF 评测记录中的 BF16 成绩为 43.3%；文章没有提供足以核对两者测试配置的信息，保留现有 BF16 成绩，不择高覆盖。

最近核验时间：2026-11-04T04:48+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B)
- [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/)

研究备注：
- 本地目标是默认 642 题的 V2 全量配置。现有 76.5 为 V2-Hard 子集，66.1 为 V1，均不属于目标全量成绩。

尚未解决的问题：
- 后续文章将 V2-Hard 报为 77.2，最终模型卡报 76.5；测试条件不足以解释差异，且都不是 V2 全量结果。

最近核验时间：2026-11-04T04:48+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 80.1
- version: 2.1
- dataset: harborframework/terminal-bench-2.1
- variant: BF16
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml)
- date: 2026-10-07
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 3.0
- metric: task resolution rate
- version: 4.0.0
- dataset: harborframework/terminal-bench
- variant: pass@1 averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-4.0.yaml](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-4.0.yaml)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [HF Terminal-Bench 4 evaluation result](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-4.0.yaml)
- [Artificial Analysis Terminal-Bench 4 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 新增 Beam 1.0 官方成绩：3.0%，v4.0.0，mini-swe-agent，pass@1 三次重复平均。

最近核验时间：2026-11-04T04:48+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 0.5
- metric: task resolution rate
- version: 0.1.0
- dataset: harborframework/terminal-bench-science
- variant: pass@1 averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-science.yaml](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-science.yaml)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [HF Terminal-Bench Science evaluation result](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-science.yaml)
- [Artificial Analysis Terminal-Bench Science method](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 新增 Beam 1.0 官方成绩：0.5%，v0.1.0，mini-swe-agent，pass@1 三次重复平均；方法页说明共 70 项任务。

最近核验时间：2026-11-04T04:48+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 39.3
- dataset: public
- variant: BF16
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B](https://huggingface.co/reflection/Beam-1.0-501B-A23B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench v1.0.6 changelog](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)
- [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/)

研究备注：
- 现有 39.3 明确来自 public split；本地定义对应的是 v1.0.6 的 private held-out 榜单。

尚未解决的问题：
- Reflection 后续文章报 public split 37.0，最终模型卡报 39.3，来源未解释差异。未找到 private split 成绩。

最近核验时间：2026-11-04T04:48+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld v2.1 release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [OSWorld v2.1 official site](https://osworld-v2.xlang.ai/)
- [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B)

研究备注：
- Beam 官方模型卡标注文本输入；OSWorld v2.1 需要从屏幕图像感知。使用视觉前端或 wrapper 得到的结果属于组合 agent。

最近核验时间：2026-11-04T04:48+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography protocol paper](https://arxiv.org/html/2608.10677)
- [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B)

研究备注：
- Surge 官方榜单列有 “Reflection Beam 1.0 (Max)” 1.2%，但未标出精确 checkpoint、图像输入路径或 harness；协议要求模型读取图表图像，而 Beam 是文本输入。

尚未解决的问题：
- 未确认榜单分数对应当前模型文件中的精确 checkpoint 和测试配置，暂不归入模型。

最近核验时间：2026-11-04T04:48+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 36.0
- metric: accuracy
- dataset: cais/hle
- variant: BF16; no tools
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml)
- date: 2026-10-07
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 51.1
- metric: accuracy
- dataset: cais/hle
- variant: BF16; with tools
- source: [https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml](https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml)
- date: 2026-10-07
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Reflection Beam model card](https://huggingface.co/reflection/Beam-1.0-501B-A23B)
- [Reflection Beam introduction and updated results](https://reflection.ai/blog/introducing-beam/)
- [HLE official leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- HF 评测 YAML 记录 cais/hle 数据集、accuracy 和 2026-10-07 评测日期，分别注明无工具 36.0% 和有工具 51.1%。但 HF 页面提示 task_id “hle” 与数据集任务定义不匹配。

尚未解决的问题：
- Reflection 介绍文章另报 36.2%/51.2%，未披露足以核对的测试配置；另外需确认其与本地定义的原始 2,500 题使用完全一致。

最近核验时间：2026-11-04T04:48+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 18
- metric: index score
- version: 5.0
- source: [https://artificialanalysis.ai/models/reflection-beam](https://artificialanalysis.ai/models/reflection-beam)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Beam model page](https://artificialanalysis.ai/models/reflection-beam)

研究备注：
- 新增 Artificial Analysis 官方页面所列 Intelligence Index v5.0 分数 18。该指数包含多个评测，不能替代原始 HLE 成绩。

最近核验时间：2026-11-04T04:48+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation and leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 已检查 Artificial Analysis 当前 v2.1 榜单，未列出 Beam/Reflection。

最近核验时间：2026-11-04T04:48+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 43.42
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index official benchmark page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 新增 Vals 官方页面所列 Beam 1.0 Vals Index v2.2 分数 43.42%，使用仓库定义的 performance score 指标。

尚未解决的问题：
- 页面更新时间 2026-10-30 不是评测日期，因此未填写 date。

最近核验时间：2026-11-04T04:48+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Beam model page",
          "url": "https://artificialanalysis.ai/models/reflection-beam"
        }
      ],
      "notes": [
        "新增 Artificial Analysis 官方页面所列 Intelligence Index v5.0 分数 18。该指数包含多个评测，不能替代原始 HLE 成绩。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Reflection Beam model card",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench v1.0.6 changelog",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        },
        {
          "label": "Reflection Beam introduction and updated results",
          "url": "https://reflection.ai/blog/introducing-beam/"
        }
      ],
      "notes": [
        "现有 39.3 明确来自 public split；本地定义对应的是 v1.0.6 的 private held-out 榜单。"
      ],
      "status": "冲突",
      "unresolved": [
        "Reflection 后续文章报 public split 37.0，最终模型卡报 39.3，来源未解释差异。未找到 private split 成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography protocol paper",
          "url": "https://arxiv.org/html/2608.10677"
        },
        {
          "label": "Reflection Beam model card",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B"
        }
      ],
      "notes": [
        "Surge 官方榜单列有 “Reflection Beam 1.0 (Max)” 1.2%，但未标出精确 checkpoint、图像输入路径或 harness；协议要求模型读取图表图像，而 Beam 是文本输入。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认榜单分数对应当前模型文件中的精确 checkpoint 和测试配置，暂不归入模型。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "HF machine-readable evaluation result",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/Beam-1.0-501B-A23B.yaml"
        },
        {
          "label": "Reflection Beam introduction and updated results",
          "url": "https://reflection.ai/blog/introducing-beam/"
        }
      ],
      "notes": [
        "保留官方 HF 评测记录中注明的 BF16 DeepSWE 1.1 分数 43.3%；后续 Reflection 文章另报 44.4%，未披露足以确认两者条件一致的信息。"
      ],
      "status": "冲突",
      "unresolved": [
        "Reflection 后续文章报告 44.4%，而 HF 评测记录中的 BF16 成绩为 43.3%；文章没有提供足以核对两者测试配置的信息，保留现有 BF16 成绩，不择高覆盖。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation and leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis 当前 v2.1 榜单，未列出 Beam/Reflection。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Reflection Beam model card",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B"
        },
        {
          "label": "Reflection Beam introduction and updated results",
          "url": "https://reflection.ai/blog/introducing-beam/"
        },
        {
          "label": "HLE official leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "HF 评测 YAML 记录 cais/hle 数据集、accuracy 和 2026-10-07 评测日期，分别注明无工具 36.0% 和有工具 51.1%。但 HF 页面提示 task_id “hle” 与数据集任务定义不匹配。"
      ],
      "status": "冲突",
      "unresolved": [
        "Reflection 介绍文章另报 36.2%/51.2%，未披露足以核对的测试配置；另外需确认其与本地定义的原始 2,500 题使用完全一致。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld v2.1 release manifest",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "OSWorld v2.1 official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Reflection Beam model card",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B"
        }
      ],
      "notes": [
        "Beam 官方模型卡标注文本输入；OSWorld v2.1 需要从屏幕图像感知。使用视觉前端或 wrapper 得到的结果属于组合 agent。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Reflection Beam model card",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B"
        },
        {
          "label": "Reflection Beam introduction and updated results",
          "url": "https://reflection.ai/blog/introducing-beam/"
        }
      ],
      "notes": [
        "本地目标是默认 642 题的 V2 全量配置。现有 76.5 为 V2-Hard 子集，66.1 为 V1，均不属于目标全量成绩。"
      ],
      "status": "未找到",
      "unresolved": [
        "后续文章将 V2-Hard 报为 77.2，最终模型卡报 76.5；测试条件不足以解释差异，且都不是 V2 全量结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "HF Terminal-Bench Science evaluation result",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-science.yaml"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science method",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "新增 Beam 1.0 官方成绩：0.5%，v0.1.0，mini-swe-agent，pass@1 三次重复平均；方法页说明共 70 项任务。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "HF Terminal-Bench 4 evaluation result",
          "url": "https://huggingface.co/reflection/Beam-1.0-501B-A23B/blob/main/.eval_results/terminal-bench-4.0.yaml"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4 method",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "新增 Beam 1.0 官方成绩：3.0%，v4.0.0，mini-swe-agent，pass@1 三次重复平均。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T04:48+08:00",
      "checked_sources": [
        {
          "label": "Vals Index official benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "新增 Vals 官方页面所列 Beam 1.0 Vals Index v2.2 分数 43.42%，使用仓库定义的 performance score 指标。"
      ],
      "status": "已收录",
      "unresolved": [
        "页面更新时间 2026-10-30 不是评测日期，因此未填写 date。"
      ]
    }
  },
  "existing_records": 7,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T04:48+08:00",
  "model_id": "reflection/beam-1.0-501b-a23b",
  "new_records": 4,
  "overall_status": "待复核"
}

-->
