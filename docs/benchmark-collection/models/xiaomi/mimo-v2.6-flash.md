# MiMo-V2.6-Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2.6-flash
- 模型名称：MiMo-V2.6-Flash
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T09:02+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 收集前已有成绩数量：16
- 当前已收录的对应成绩数量：4

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 67.9 (metric=score; version=1.1) | [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [DataCurve DeepSWE official leaderboard row](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=XiaomiMiMo/MiMo-V2.6-Flash-RL&leaderboard_task_id=deep_swe), [Xiaomi MiMo-V2.6 release note](https://mimo.mi.com/docs/en-US/news/latest/v2-6) | 2026-11-04T09:02+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T09:02+08:00 |
| terminal-bench-v4 | 已收录 | 28.8 (metric=task resolution rate; version=4.0.0); 87.6 (metric=score; version=2.1) | [Harbor Terminal-Bench 4 result for exact checkpoint](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=XiaomiMiMo/MiMo-V2.6-Flash-RL&leaderboard_task_id=terminalbench_4), [Terminal-Bench 4.0 release and version](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T09:02+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [Terminal-Bench Science official announcement](https://www.terminal-bench-science.ai/announcement), [Harbor Terminal-Bench Science leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-04T09:02+08:00 |
| automationbench-v1.0.6 | 已收录 | 52.3 (metric=task_completed_correctly; version=1.0.6) | [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [Zapier AutomationBench leaderboard and metric](https://zapier.com/benchmarks) | 2026-11-04T09:02+08:00 |
| osworld-v2.1 | 未找到 | — | [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [OSWorld-V2 official repository and v2.1 information](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md), [OSWorld project page](https://osworld-v2.xlang.ai/) | 2026-11-04T09:02+08:00 |
| chartography | 未找到 | — | [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography methodology](https://github.com/surge-ai/chartography) | 2026-11-04T09:02+08:00 |
| humanitys-last-exam | 已收录 | 35 (metric=accuracy; dataset=2,158 text-only questions from the original 2,500-item HLE set) | [Artificial Analysis comparison with Step 5](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T09:02+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 27 (metric=index score; version=5.0.1) | [Artificial Analysis MiMo-V2.6-Flash profile](https://artificialanalysis.ai/models/mimo-v2-6-flash), [Artificial Analysis Intelligence Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T09:02+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1615 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; harness=Stirrup) | [Artificial Analysis comparison with Step 5](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL) | 2026-11-04T09:02+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals MiMo V2.6 Flash profile and settings](https://www.vals.ai/models/xiaomi_mimo-v2.6-flash), [Xiaomi MOPD checkpoint and API update note](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition) | 2026-11-04T09:02+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 67.9
- metric: score
- version: 1.1
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [DataCurve DeepSWE official leaderboard row](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=XiaomiMiMo/MiMo-V2.6-Flash-RL&leaderboard_task_id=deep_swe)
- [Xiaomi MiMo-V2.6 release note](https://mimo.mi.com/docs/en-US/news/latest/v2-6)

研究备注：
- Exact checkpoint leaderboard and model card report 67.9; Xiaomi release note reports approximately 65.7 for DeepSWE v1.1. Published evaluation conditions do not explain the difference, so preserve the existing 67.9 and flag for review.

尚未解决的问题：
- Exact checkpoint leaderboard and model card report 67.9; Xiaomi release note reports approximately 65.7 for DeepSWE v1.1. Published evaluation conditions do not explain the difference, so preserve the existing 67.9 and flag for review.

最近核验时间：2026-11-04T09:02+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- No exact MiMo-V2.6-Flash result was found; results from SWE-bench Verified or other Pro versions were not reused.

最近核验时间：2026-11-04T09:02+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 28.8
- metric: task resolution rate
- version: 4.0.0
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 87.6
- metric: score
- version: 2.1
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Harbor Terminal-Bench 4 result for exact checkpoint](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=XiaomiMiMo/MiMo-V2.6-Flash-RL&leaderboard_task_id=terminalbench_4)
- [Terminal-Bench 4.0 release and version](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The exact Flash-RL checkpoint is listed at 28.8. Official Harbor command identifies dataset version terminal-bench/terminal-bench@4.0.0; the benchmark measures task resolution rate. No per-run harness or effort was disclosed on the result row.

最近核验时间：2026-11-04T09:02+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [Terminal-Bench Science official announcement](https://www.terminal-bench-science.ai/announcement)
- [Harbor Terminal-Bench Science leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- No exact MiMo result was found in the model card or announcement. The official Harbor leaderboard is dynamically rendered and its full rows were not extractable during this check, so absence is not treated as fully confirmed.

尚未解决的问题：
- No exact MiMo result was found in the model card or announcement. The official Harbor leaderboard is dynamically rendered and its full rows were not extractable during this check, so absence is not treated as fully confirmed.

最近核验时间：2026-11-04T09:02+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 52.3
- metric: task_completed_correctly
- version: 1.0.6
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [Zapier AutomationBench leaderboard and metric](https://zapier.com/benchmarks)

研究备注：
- Existing 52.3 and version 1.0.6 match Xiaomi’s exact model card. Metric is recorded as the benchmark’s documented task_completed_correctly rate; effort, harness, dataset split, and evaluation date were not disclosed.

最近核验时间：2026-11-04T09:02+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [OSWorld-V2 official repository and v2.1 information](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)
- [OSWorld project page](https://osworld-v2.xlang.ai/)

研究备注：
- The 80.8 result on the Xiaomi card is OSWorld-Verified, not OSWorld v2.1. No exact v2.1 result was found; the historical OSWorld-Verified row is retained without remapping.

最近核验时间：2026-11-04T09:02+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography methodology](https://github.com/surge-ai/chartography)

研究备注：
- The model supports image input, so the benchmark is applicable. No exact MiMo result was found on the official leaderboard.

最近核验时间：2026-11-04T09:02+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 35
- metric: accuracy
- dataset: 2,158 text-only questions from the original 2,500-item HLE set
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis comparison with Step 5](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis reports 35% accuracy for MiMo-V2.6-Flash. Its documented HLE result uses 2,158 text-only questions from the original 2,500-question set; that subset is stored explicitly. No evaluation date, effort, or checkpoint revision was disclosed on the result page. The existing Agents’ Last Exam 27.6 record is a different benchmark and was not reused.

最近核验时间：2026-11-04T09:02+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 27
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/mimo-v2-6-flash](https://artificialanalysis.ai/models/mimo-v2-6-flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis MiMo-V2.6-Flash profile](https://artificialanalysis.ai/models/mimo-v2-6-flash)
- [Artificial Analysis Intelligence Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The current AA profile reports 27 under v5.0.1, so the source row preserves version 5.0.1. The local benchmark definition is version 5.0; this record does not map to it and is excluded from mapped coverage pending definition/version review. The profile links to the published model weights but does not expose an evaluation checkpoint revision.

尚未解决的问题：
- The current AA profile reports 27 under v5.0.1, so the source row preserves version 5.0.1. The local benchmark definition is version 5.0; this record does not map to it and is excluded from mapped coverage pending definition/version review. The profile links to the published model weights but does not expose an evaluation checkpoint revision.

最近核验时间：2026-11-04T09:02+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1615
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis comparison with Step 5](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Xiaomi MiMo-V2.6-Flash-RL model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)

研究备注：
- Artificial Analysis independently reports 1615 Elo for MiMo-V2.6-Flash on GDPval-AA v2.1. Its method describes 220 tasks across 44 occupations with the Stirrup harness; the Xiaomi model-card table shows no Flash result (“-”). No effort, evaluation date, or checkpoint revision was disclosed.

最近核验时间：2026-11-04T09:02+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals MiMo V2.6 Flash profile and settings](https://www.vals.ai/models/xiaomi_mimo-v2.6-flash)
- [Xiaomi MOPD checkpoint and API update note](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)

研究备注：
- Vals reports 54.83% using the Xiaomi API, but does not identify the exact checkpoint revision. Xiaomi says MOPD checkpoints were released while the API names stayed mimo-v2.6-flash; this TOML entry points specifically to the Flash-RL weights, so the API result is not copied into the score table pending exact variant confirmation.

尚未解决的问题：
- Vals reports 54.83% using the Xiaomi API, but does not identify the exact checkpoint revision. Xiaomi says MOPD checkpoints were released while the API names stayed mimo-v2.6-flash; this TOML entry points specifically to the Flash-RL weights, so the API result is not copied into the score table pending exact variant confirmation.

最近核验时间：2026-11-04T09:02+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiMo-V2.6-Flash profile",
          "url": "https://artificialanalysis.ai/models/mimo-v2-6-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The current AA profile reports 27 under v5.0.1, so the source row preserves version 5.0.1. The local benchmark definition is version 5.0; this record does not map to it and is excluded from mapped coverage pending definition/version review. The profile links to the published model weights but does not expose an evaluation checkpoint revision."
      ],
      "status": "待核实",
      "unresolved": [
        "The current AA profile reports 27 under v5.0.1, so the source row preserves version 5.0.1. The local benchmark definition is version 5.0; this record does not map to it and is excluded from mapped coverage pending definition/version review. The profile links to the published model weights but does not expose an evaluation checkpoint revision."
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "label": "Zapier AutomationBench leaderboard and metric",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Existing 52.3 and version 1.0.6 match Xiaomi’s exact model card. Metric is recorded as the benchmark’s documented task_completed_correctly rate; effort, harness, dataset split, and evaluation date were not disclosed."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography methodology",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "The model supports image input, so the benchmark is applicable. No exact MiMo result was found on the official leaderboard."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "label": "DataCurve DeepSWE official leaderboard row",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe?eval_result=XiaomiMiMo/MiMo-V2.6-Flash-RL&leaderboard_task_id=deep_swe"
        },
        {
          "label": "Xiaomi MiMo-V2.6 release note",
          "url": "https://mimo.mi.com/docs/en-US/news/latest/v2-6"
        }
      ],
      "notes": [
        "Exact checkpoint leaderboard and model card report 67.9; Xiaomi release note reports approximately 65.7 for DeepSWE v1.1. Published evaluation conditions do not explain the difference, so preserve the existing 67.9 and flag for review."
      ],
      "status": "冲突",
      "unresolved": [
        "Exact checkpoint leaderboard and model card report 67.9; Xiaomi release note reports approximately 65.7 for DeepSWE v1.1. Published evaluation conditions do not explain the difference, so preserve the existing 67.9 and flag for review."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison with Step 5",
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        }
      ],
      "notes": [
        "Artificial Analysis independently reports 1615 Elo for MiMo-V2.6-Flash on GDPval-AA v2.1. Its method describes 220 tasks across 44 occupations with the Stirrup harness; the Xiaomi model-card table shows no Flash result (“-”). No effort, evaluation date, or checkpoint revision was disclosed."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison with Step 5",
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-6-flash-vs-step-5"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis reports 35% accuracy for MiMo-V2.6-Flash. Its documented HLE result uses 2,158 text-only questions from the original 2,500-question set; that subset is stored explicitly. No evaluation date, effort, or checkpoint revision was disclosed on the result page. The existing Agents’ Last Exam 27.6 record is a different benchmark and was not reused."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "label": "OSWorld-V2 official repository and v2.1 information",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        },
        {
          "label": "OSWorld project page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "The 80.8 result on the Xiaomi card is OSWorld-Verified, not OSWorld v2.1. No exact v2.1 result was found; the historical OSWorld-Verified row is retained without remapping."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "label": "SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "No exact MiMo-V2.6-Flash result was found; results from SWE-bench Verified or other Pro versions were not reused."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Xiaomi MiMo-V2.6-Flash-RL model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "label": "Terminal-Bench Science official announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor Terminal-Bench Science leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "No exact MiMo result was found in the model card or announcement. The official Harbor leaderboard is dynamically rendered and its full rows were not extractable during this check, so absence is not treated as fully confirmed."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact MiMo result was found in the model card or announcement. The official Harbor leaderboard is dynamically rendered and its full rows were not extractable during this check, so absence is not treated as fully confirmed."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Harbor Terminal-Bench 4 result for exact checkpoint",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=XiaomiMiMo/MiMo-V2.6-Flash-RL&leaderboard_task_id=terminalbench_4"
        },
        {
          "label": "Terminal-Bench 4.0 release and version",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The exact Flash-RL checkpoint is listed at 28.8. Official Harbor command identifies dataset version terminal-bench/terminal-bench@4.0.0; the benchmark measures task resolution rate. No per-run harness or effort was disclosed on the result row."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T09:02+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals MiMo V2.6 Flash profile and settings",
          "url": "https://www.vals.ai/models/xiaomi_mimo-v2.6-flash"
        },
        {
          "label": "Xiaomi MOPD checkpoint and API update note",
          "url": "https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition"
        }
      ],
      "notes": [
        "Vals reports 54.83% using the Xiaomi API, but does not identify the exact checkpoint revision. Xiaomi says MOPD checkpoints were released while the API names stayed mimo-v2.6-flash; this TOML entry points specifically to the Flash-RL weights, so the API result is not copied into the score table pending exact variant confirmation."
      ],
      "status": "待核实",
      "unresolved": [
        "Vals reports 54.83% using the Xiaomi API, but does not identify the exact checkpoint revision. Xiaomi says MOPD checkpoints were released while the API names stayed mimo-v2.6-flash; this TOML entry points specifically to the Flash-RL weights, so the API result is not copied into the score table pending exact variant confirmation."
      ]
    }
  },
  "existing_records": 16,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T09:02+08:00",
  "model_id": "xiaomi/mimo-v2.6-flash",
  "new_records": 3,
  "overall_status": "待复核"
}

-->
