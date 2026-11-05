# DeepSeek V4 Pro 0813 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4-pro-0813
- 模型名称：DeepSeek V4 Pro 0813
- 发布日期：2026-08-13
- 最近检查时间：2026-11-04T17:35+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 更新成绩数量：3
- 收集前已有成绩数量：11
- 当前已收录的对应成绩数量：5

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 62.7 (metric=score; effort=max; variant=temperature=1.0; top_p=0.95; harness=DeepSeek Harness minimal mode) | [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T17:35+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Nex N2.5 Pro model card](https://huggingface.co/nex-agi/Nex-N2.5-Pro/blob/main/README.md) | 2026-11-04T17:35+08:00 |
| terminal-bench-v4 | 待核实 | 87.9 (metric=score; version=2.1; variant=max effort; harness=DeepSeek Harness minimal mode); 14.14 (metric=accuracy; version=4.0; dataset=66 tasks; variant=avg@3; each run pass@1; three runs; ±1 standard error; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T17:35+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 4.29 (metric=accuracy; version=0.1.0; dataset=70 tasks; variant=pass@1 single run; retry infrastructure/provider errors only; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T17:35+08:00 |
| automationbench-v1.0.6 | 待核实 | 31.8 (metric=score; dataset=public) | [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813), [Zapier AutomationBench benchmark](https://zapier.com/benchmarks) | 2026-11-04T17:35+08:00 |
| osworld-v2.1 | 未找到 | — | [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813), [OSWorld v2.1 official release JSON](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [OSWorld official project page](https://osworld-v2.xlang.ai/) | 2026-11-04T17:35+08:00 |
| chartography | 待核实 | — | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) | 2026-11-04T17:35+08:00 |
| humanitys-last-exam | 已存在 | 42.7 (metric=accuracy; variant=without tools); 60 (metric=accuracy; variant=with tools) | [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813), [Humanity's Last Exam official site](https://lastexam.ai/) | 2026-11-04T17:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 23 (metric=index score; version=5.0; effort=max); 23 (metric=index score; version=5.0.1; effort=max) | [Artificial Analysis DeepSeek V4 Pro 0813 profile](https://artificialanalysis.ai/models/deepseek-v4-pro), [Artificial Analysis DeepSeek V4 Pro release profile](https://artificialanalysis.ai/models/releases/deepseek-v4-pro) | 2026-11-04T17:35+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1066 (metric=Elo rating; version=2.1; dataset=220 tasks; variant=non-reasoning; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T17:35+08:00 |
| vals-index-v2.2 | 已收录 | 52.97 (metric=performance score; version=2.2) | [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T17:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 62.7
- metric: score
- effort: max
- variant: temperature=1.0; top_p=0.95
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- The exact 0813 model card records DeepSWE 62.7 and specifies DeepSeek Harness minimal mode, max effort, temperature=1.0, and top_p=0.95; it does not state the DeepSWE version or scoring metric for this row.
- The v1.1 leaderboard separately lists deepseek-v4-pro[max] at 63% ±6% over 113 tasks but does not identify the 0813 checkpoint, so that candidate was not attached to this model.

尚未解决的问题：
- Confirm the model-card score’s benchmark version and metric, and whether the leaderboard’s unqualified V4 Pro row is the 0813 checkpoint.

最近核验时间：2026-11-04T17:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Nex N2.5 Pro model card](https://huggingface.co/nex-agi/Nex-N2.5-Pro/blob/main/README.md)

研究备注：
- The current Scale V2 full leaderboard does not list DeepSeek V4 Pro 0813.
- A secondary Nex model card mentions 55.4 for DeepSeek V4 Pro 0813 but does not identify the benchmark version or metric; that result was not written to the model TOML.

尚未解决的问题：
- Verify whether the 55.4 result is SWE-bench Pro V2 and confirm its metric, harness, and test conditions before adding it.

最近核验时间：2026-11-04T17:35+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 87.9
- metric: score
- version: 2.1
- variant: max effort
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 14.14
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- variant: avg@3; each run pass@1; three runs; ±1 standard error
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Vals lists DeepSeek V4 Pro 0813 at 14.14%, with metric accuracy, source version 4.0, 66 tasks, Mini-SWE-agent, and avg@3 (each run is pass@1; three runs; error bars are ±1 standard error).
- Vals reports page/leaderboard update dates, not a model evaluation date; no date was added to the score record.

尚未解决的问题：
- The local definition uses metric task resolution rate and version 4.0.0. The source labels are retained verbatim, so this raw row is not mapped pending definition reconciliation.

最近核验时间：2026-11-04T17:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 4.29
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- variant: pass@1 single run; retry infrastructure/provider errors only
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals AI Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Vals lists DeepSeek V4 Pro 0813 at 4.29%, metric accuracy, version 0.1.0, 70 tasks, Mini-SWE-agent, pass@1 from one run; infrastructure/provider errors may be retried.
- Vals reports page/leaderboard update dates, not a model evaluation date; no date was added to the score record.

尚未解决的问题：
- The local definition calls the metric task resolution rate, while the source calls it accuracy. The original source metric is retained and the row remains unmapped.

最近核验时间：2026-11-04T17:35+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 31.8
- metric: score
- dataset: public
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- [Zapier AutomationBench benchmark](https://zapier.com/benchmarks)

研究备注：
- The exact model card records AutomationBench (Public) 31.8, matching the existing raw TOML row and public dataset label.
- The model card does not state benchmark version or metric. Zapier identifies task_completed_correctly as its official primary metric and distinguishes the private leaderboard from public-set results.

尚未解决的问题：
- Confirm whether this public result is target version 1.0.6 and what scoring metric produced 31.8; it is not treated as the private-set leaderboard result.

最近核验时间：2026-11-04T17:35+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- [OSWorld v2.1 official release JSON](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [OSWorld official project page](https://osworld-v2.xlang.ai/)

研究备注：
- No exact DeepSeek V4 Pro 0813 score was found in the model card or readable OSWorld v2.1 official results. Unverified estimates were excluded.

最近核验时间：2026-11-04T17:35+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)

研究备注：
- Surge shows a DeepSeek V4 Pro (Max) result of 6.9%, but the row does not identify the 0813 checkpoint or provide enough evaluation conditions to attribute it to this exact model. No score was added.

尚未解决的问题：
- Confirm whether the Surge DeepSeek V4 Pro (Max) result used the 0813 checkpoint and establish its evaluation conditions.

最近核验时间：2026-11-04T17:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 42.7
- metric: accuracy
- variant: without tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 60
- metric: accuracy
- variant: with tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepSeek V4 Pro 0813 model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- [Humanity's Last Exam official site](https://lastexam.ai/)

研究备注：
- The exact 0813 model card lists 42.7 without tools and 60.0 with tools. The HLE official scoring metric is accuracy; both existing rows were updated to that metric while preserving scores and tool variants.
- The model card does not provide an evaluation date or explicit HLE task subset for these rows.

最近核验时间：2026-11-04T17:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 23
- metric: index score
- version: 5.0
- effort: max
- source: [https://artificialanalysis.ai/models/deepseek-v4-pro](https://artificialanalysis.ai/models/deepseek-v4-pro)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 23
- metric: index score
- version: 5.0.1
- effort: max
- source: [https://artificialanalysis.ai/models/releases/deepseek-v4-pro](https://artificialanalysis.ai/models/releases/deepseek-v4-pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis DeepSeek V4 Pro 0813 profile](https://artificialanalysis.ai/models/deepseek-v4-pro)
- [Artificial Analysis DeepSeek V4 Pro release profile](https://artificialanalysis.ai/models/releases/deepseek-v4-pro)

研究备注：
- Both Artificial Analysis pages report index score 23 for DeepSeek V4 Pro 0813 (Max). The model-specific profile labels the method v5.0, while the release profile labels it v5.0.1; both raw rows are preserved.

尚未解决的问题：
- The two official pages disagree on the method-version suffix for the same displayed model/score. Confirm the applicable version before closing review.

最近核验时间：2026-11-04T17:35+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1066
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- variant: non-reasoning
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The exact leaderboard row is DeepSeek V4 Pro 0813 (Non-reasoning), 1066 Elo with −22/+22 interval. The benchmark uses 220 tasks and the Stirrup harness.
- The row’s August 2026 field is the model release month, not an evaluation date, so no date was added.

最近核验时间：2026-11-04T17:35+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 52.97
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The exact model row reports a 52.97% performance score on Vals Index version 2.2. The leaderboard date is not an evaluation date, so no date was added.

最近核验时间：2026-11-04T17:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis DeepSeek V4 Pro 0813 profile",
          "url": "https://artificialanalysis.ai/models/deepseek-v4-pro"
        },
        {
          "label": "Artificial Analysis DeepSeek V4 Pro release profile",
          "url": "https://artificialanalysis.ai/models/releases/deepseek-v4-pro"
        }
      ],
      "notes": [
        "Both Artificial Analysis pages report index score 23 for DeepSeek V4 Pro 0813 (Max). The model-specific profile labels the method v5.0, while the release profile labels it v5.0.1; both raw rows are preserved."
      ],
      "status": "待核实",
      "unresolved": [
        "The two official pages disagree on the method-version suffix for the same displayed model/score. Confirm the applicable version before closing review."
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 Pro 0813 model card",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
        },
        {
          "label": "Zapier AutomationBench benchmark",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "The exact model card records AutomationBench (Public) 31.8, matching the existing raw TOML row and public dataset label.",
        "The model card does not state benchmark version or metric. Zapier identifies task_completed_correctly as its official primary metric and distinguishes the private leaderboard from public-set results."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm whether this public result is target version 1.0.6 and what scoring metric produced 31.8; it is not treated as the private-set leaderboard result."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "DeepSeek V4 Pro 0813 model card",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
        }
      ],
      "notes": [
        "Surge shows a DeepSeek V4 Pro (Max) result of 6.9%, but the row does not identify the 0813 checkpoint or provide enough evaluation conditions to attribute it to this exact model. No score was added."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm whether the Surge DeepSeek V4 Pro (Max) result used the 0813 checkpoint and establish its evaluation conditions."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 Pro 0813 model card",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "The exact 0813 model card records DeepSWE 62.7 and specifies DeepSeek Harness minimal mode, max effort, temperature=1.0, and top_p=0.95; it does not state the DeepSWE version or scoring metric for this row.",
        "The v1.1 leaderboard separately lists deepseek-v4-pro[max] at 63% ±6% over 113 tasks but does not identify the 0813 checkpoint, so that candidate was not attached to this model."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm the model-card score’s benchmark version and metric, and whether the leaderboard’s unqualified V4 Pro row is the 0813 checkpoint."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The exact leaderboard row is DeepSeek V4 Pro 0813 (Non-reasoning), 1066 Elo with −22/+22 interval. The benchmark uses 220 tasks and the Stirrup harness.",
        "The row’s August 2026 field is the model release month, not an evaluation date, so no date was added."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 Pro 0813 model card",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
        },
        {
          "label": "Humanity's Last Exam official site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "The exact 0813 model card lists 42.7 without tools and 60.0 with tools. The HLE official scoring metric is accuracy; both existing rows were updated to that metric while preserving scores and tool variants.",
        "The model card does not provide an evaluation date or explicit HLE task subset for these rows."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 Pro 0813 model card",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
        },
        {
          "label": "OSWorld v2.1 official release JSON",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "OSWorld official project page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "No exact DeepSeek V4 Pro 0813 score was found in the model card or readable OSWorld v2.1 official results. Unverified estimates were excluded."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Nex N2.5 Pro model card",
          "url": "https://huggingface.co/nex-agi/Nex-N2.5-Pro/blob/main/README.md"
        }
      ],
      "notes": [
        "The current Scale V2 full leaderboard does not list DeepSeek V4 Pro 0813.",
        "A secondary Nex model card mentions 55.4 for DeepSeek V4 Pro 0813 but does not identify the benchmark version or metric; that result was not written to the model TOML."
      ],
      "status": "待核实",
      "unresolved": [
        "Verify whether the 55.4 result is SWE-bench Pro V2 and confirm its metric, harness, and test conditions before adding it."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Vals lists DeepSeek V4 Pro 0813 at 4.29%, metric accuracy, version 0.1.0, 70 tasks, Mini-SWE-agent, pass@1 from one run; infrastructure/provider errors may be retried.",
        "Vals reports page/leaderboard update dates, not a model evaluation date; no date was added to the score record."
      ],
      "status": "待核实",
      "unresolved": [
        "The local definition calls the metric task resolution rate, while the source calls it accuracy. The original source metric is retained and the row remains unmapped."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Vals lists DeepSeek V4 Pro 0813 at 14.14%, with metric accuracy, source version 4.0, 66 tasks, Mini-SWE-agent, and avg@3 (each run is pass@1; three runs; error bars are ±1 standard error).",
        "Vals reports page/leaderboard update dates, not a model evaluation date; no date was added to the score record."
      ],
      "status": "待核实",
      "unresolved": [
        "The local definition uses metric task resolution rate and version 4.0.0. The source labels are retained verbatim, so this raw row is not mapped pending definition reconciliation."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T17:35+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The exact model row reports a 52.97% performance score on Vals Index version 2.2. The leaderboard date is not an evaluation date, so no date was added."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 11,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T17:35+08:00",
  "model_id": "deepseek/deepseek-v4-pro-0813",
  "new_records": 6,
  "overall_status": "待复核",
  "updated_records": 3
}

-->
