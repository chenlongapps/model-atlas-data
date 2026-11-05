# MiMo-V2.6-Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2.6-pro
- 模型名称：MiMo-V2.6-Pro
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T09:11+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 收集前已有成绩数量：17
- 当前已收录的对应成绩数量：5

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 71.9 (metric=score; version=1.1; variant=MiMo-V2.6 Pro comparison column) | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [DataCurve DeepSWE leaderboard row for exact Pro-RL checkpoint](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=XiaomiMiMo/MiMo-V2.6-Pro-RL&leaderboard_task_id=deep_swe), [Xiaomi MiMo-V2.6 launch report](https://mimo.mi.com/docs/en-US/news/latest/v2-6) | 2026-11-04T09:11+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Xiaomi MiMo-V2.6 launch report](https://mimo.mi.com/docs/en-US/news/latest/v2-6) | 2026-11-04T09:11+08:00 |
| terminal-bench-v4 | 已收录 | 34.9 (metric=task resolution rate; version=4.0.0; variant=MiMo-V2.6 Pro comparison column); 89.9 (metric=score; version=2.1; variant=MiMo-V2.6 Pro comparison column) | [Harbor Terminal-Bench 4 result for exact Pro-RL checkpoint](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=XiaomiMiMo/MiMo-V2.6-Pro-RL&leaderboard_task_id=terminalbench_4), [Terminal-Bench 4.0 version and method](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T09:11+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [Terminal-Bench Science announcement](https://www.terminal-bench-science.ai/announcement), [Harbor Terminal-Bench Science leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-04T09:11+08:00 |
| automationbench-v1.0.6 | 已收录 | 53.1 (metric=task_completed_correctly; version=1.0.6; variant=MiMo-V2.6 Pro comparison column) | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [Zapier AutomationBench leaderboard and metric definition](https://zapier.com/benchmarks) | 2026-11-04T09:11+08:00 |
| osworld-v2.1 | 未找到 | — | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [OSWorld-V2 official README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md) | 2026-11-04T09:11+08:00 |
| chartography | 未找到 | — | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography methodology](https://github.com/surge-ai/chartography) | 2026-11-04T09:11+08:00 |
| humanitys-last-exam | 已收录 | 49 (metric=accuracy; dataset=2,158 text-only questions from the original 2,500-item HLE set) | [Artificial Analysis Pro vs GPT-6 Astra comparison](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T09:11+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 30 (metric=index score; version=5.0.1) | [Artificial Analysis MiMo-V2.6-Pro profile](https://artificialanalysis.ai/models/mimo-v2-6-pro), [Artificial Analysis Intelligence Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T09:11+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1673 (metric=Elo rating; version=2.1; variant=MiMo-V2.6 Pro comparison column); 1691 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; harness=Stirrup) | [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [Artificial Analysis Pro vs GPT-6 Astra comparison](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T09:11+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals MiMo V2.6 Pro model page and test settings](https://www.vals.ai/models/xiaomi_mimo-v2.6-pro), [Xiaomi MOPD checkpoint and API update note](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition) | 2026-11-04T09:11+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 71.9
- metric: score
- version: 1.1
- variant: MiMo-V2.6 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [DataCurve DeepSWE leaderboard row for exact Pro-RL checkpoint](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=XiaomiMiMo/MiMo-V2.6-Pro-RL&leaderboard_task_id=deep_swe)
- [Xiaomi MiMo-V2.6 launch report](https://mimo.mi.com/docs/en-US/news/latest/v2-6)

研究备注：
- The Pro-RL card and exact DataCurve row report 71.9 for DeepSWE v1.1; Xiaomi’s launch report separately says approximately 72.6. The reports do not explain whether this reflects a checkpoint or evaluation-condition change. Preserve 71.9 and flag the difference; do not substitute the higher value.

尚未解决的问题：
- The Pro-RL card and exact DataCurve row report 71.9 for DeepSWE v1.1; Xiaomi’s launch report separately says approximately 72.6. The reports do not explain whether this reflects a checkpoint or evaluation-condition change. Preserve 71.9 and flag the difference; do not substitute the higher value.

最近核验时间：2026-11-04T09:11+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Xiaomi MiMo-V2.6 launch report](https://mimo.mi.com/docs/en-US/news/latest/v2-6)

研究备注：
- No exact Pro-RL result was found in these sources; scores from SWE-bench Verified or another Pro version were not reused.

最近核验时间：2026-11-04T09:11+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 34.9
- metric: task resolution rate
- version: 4.0.0
- variant: MiMo-V2.6 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 89.9
- metric: score
- version: 2.1
- variant: MiMo-V2.6 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Harbor Terminal-Bench 4 result for exact Pro-RL checkpoint](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=XiaomiMiMo/MiMo-V2.6-Pro-RL&leaderboard_task_id=terminalbench_4)
- [Terminal-Bench 4.0 version and method](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The exact Pro-RL checkpoint is listed at 34.9. Official Hub identifies dataset terminal-bench/terminal-bench@4.0.0 with 66 test tasks; the benchmark metric is task resolution rate. Effort and the run-specific harness were not disclosed.

最近核验时间：2026-11-04T09:11+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [Terminal-Bench Science announcement](https://www.terminal-bench-science.ai/announcement)
- [Harbor Terminal-Bench Science leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- No exact Pro-RL result was found in the model card or announcement. The Harbor leaderboard is dynamically rendered and the current rows were not extractable, so absence cannot be fully confirmed.

尚未解决的问题：
- No exact Pro-RL result was found in the model card or announcement. The Harbor leaderboard is dynamically rendered and the current rows were not extractable, so absence cannot be fully confirmed.

最近核验时间：2026-11-04T09:11+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 53.1
- metric: task_completed_correctly
- version: 1.0.6
- variant: MiMo-V2.6 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [Zapier AutomationBench leaderboard and metric definition](https://zapier.com/benchmarks)

研究备注：
- The Pro-RL table reports 53.1 for AutomationBench v1.0.6. The stored metric follows the benchmark’s documented task_completed_correctly rate; the Xiaomi table does not specify dataset split, effort, harness, or evaluation date.

最近核验时间：2026-11-04T09:11+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [OSWorld-V2 official README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)

研究备注：
- The model card’s 82.0 is OSWorld-Verified, not OSWorld v2.1. No exact v2.1 result was found; the existing OSWorld-Verified row is preserved without remapping.

最近核验时间：2026-11-04T09:11+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography methodology](https://github.com/surge-ai/chartography)

研究备注：
- Pro supports image input and the benchmark is applicable. No exact MiMo Pro result was found on the official Surge page.

最近核验时间：2026-11-04T09:11+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 49
- metric: accuracy
- dataset: 2,158 text-only questions from the original 2,500-item HLE set
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Pro vs GPT-6 Astra comparison](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis reports 49% for the original HLE. Its method uses 2,158 text-only questions from the original 2,500-item dataset and reports pass@1 accuracy; the source page does not disclose an evaluation date or checkpoint revision. The existing Agents’ Last Exam 31.6 row is a different benchmark and was not reused.

最近核验时间：2026-11-04T09:11+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 30
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/mimo-v2-6-pro](https://artificialanalysis.ai/models/mimo-v2-6-pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis MiMo-V2.6-Pro profile](https://artificialanalysis.ai/models/mimo-v2-6-pro)
- [Artificial Analysis Intelligence Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The current profile reports 30 for the V5 Index and labels the live revision v5.0.1. The TOML preserves that version, while the local benchmark definition is 5.0, so the row does not map to coverage until the version definition is reconciled. The profile identifies Pro as an open-weight model but does not disclose the precise checkpoint revision used.

尚未解决的问题：
- The current profile reports 30 for the V5 Index and labels the live revision v5.0.1. The TOML preserves that version, while the local benchmark definition is 5.0, so the row does not map to coverage until the version definition is reconciled. The profile identifies Pro as an open-weight model but does not disclose the precise checkpoint revision used.

最近核验时间：2026-11-04T09:11+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1673
- metric: Elo rating
- version: 2.1
- variant: MiMo-V2.6 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1691
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [MiMo-V2.6-Pro-RL official model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [Artificial Analysis Pro vs GPT-6 Astra comparison](https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The Xiaomi Pro-RL card reports 1673 Elo, while Artificial Analysis comparison/search records include 1691 and an older page showed 1686. These are retained as separate source rows where available; no disclosed test-condition or checkpoint detail resolves the difference. Do not choose a maximum. AA methodology describes GDPval-AA v2.1 as 220 tasks across 44 occupations using Stirrup.

尚未解决的问题：
- The Xiaomi Pro-RL card reports 1673 Elo, while Artificial Analysis comparison/search records include 1691 and an older page showed 1686. These are retained as separate source rows where available; no disclosed test-condition or checkpoint detail resolves the difference. Do not choose a maximum. AA methodology describes GDPval-AA v2.1 as 220 tasks across 44 occupations using Stirrup.

最近核验时间：2026-11-04T09:11+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals MiMo V2.6 Pro model page and test settings](https://www.vals.ai/models/xiaomi_mimo-v2.6-pro)
- [Xiaomi MOPD checkpoint and API update note](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)

研究备注：
- Vals reports 57.81% through the Xiaomi provider/API with temperature 1 and top_p 0.95, but does not disclose the exact checkpoint revision. Xiaomi states that the API alias was updated to MOPD while retaining its name; this TOML entry points to the Pro-RL weights, so no API score is copied pending exact variant confirmation.

尚未解决的问题：
- Vals reports 57.81% through the Xiaomi provider/API with temperature 1 and top_p 0.95, but does not disclose the exact checkpoint revision. Xiaomi states that the API alias was updated to MOPD while retaining its name; this TOML entry points to the Pro-RL weights, so no API score is copied pending exact variant confirmation.

最近核验时间：2026-11-04T09:11+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiMo-V2.6-Pro profile",
          "url": "https://artificialanalysis.ai/models/mimo-v2-6-pro"
        },
        {
          "label": "Artificial Analysis Intelligence Index evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The current profile reports 30 for the V5 Index and labels the live revision v5.0.1. The TOML preserves that version, while the local benchmark definition is 5.0, so the row does not map to coverage until the version definition is reconciled. The profile identifies Pro as an open-weight model but does not disclose the precise checkpoint revision used."
      ],
      "status": "待核实",
      "unresolved": [
        "The current profile reports 30 for the V5 Index and labels the live revision v5.0.1. The TOML preserves that version, while the local benchmark definition is 5.0, so the row does not map to coverage until the version definition is reconciled. The profile identifies Pro as an open-weight model but does not disclose the precise checkpoint revision used."
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
        },
        {
          "label": "Zapier AutomationBench leaderboard and metric definition",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "The Pro-RL table reports 53.1 for AutomationBench v1.0.6. The stored metric follows the benchmark’s documented task_completed_correctly rate; the Xiaomi table does not specify dataset split, effort, harness, or evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
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
        "Pro supports image input and the benchmark is applicable. No exact MiMo Pro result was found on the official Surge page."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
        },
        {
          "label": "DataCurve DeepSWE leaderboard row for exact Pro-RL checkpoint",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe?eval_result=XiaomiMiMo/MiMo-V2.6-Pro-RL&leaderboard_task_id=deep_swe"
        },
        {
          "label": "Xiaomi MiMo-V2.6 launch report",
          "url": "https://mimo.mi.com/docs/en-US/news/latest/v2-6"
        }
      ],
      "notes": [
        "The Pro-RL card and exact DataCurve row report 71.9 for DeepSWE v1.1; Xiaomi’s launch report separately says approximately 72.6. The reports do not explain whether this reflects a checkpoint or evaluation-condition change. Preserve 71.9 and flag the difference; do not substitute the higher value."
      ],
      "status": "冲突",
      "unresolved": [
        "The Pro-RL card and exact DataCurve row report 71.9 for DeepSWE v1.1; Xiaomi’s launch report separately says approximately 72.6. The reports do not explain whether this reflects a checkpoint or evaluation-condition change. Preserve 71.9 and flag the difference; do not substitute the higher value."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
        },
        {
          "label": "Artificial Analysis Pro vs GPT-6 Astra comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The Xiaomi Pro-RL card reports 1673 Elo, while Artificial Analysis comparison/search records include 1691 and an older page showed 1686. These are retained as separate source rows where available; no disclosed test-condition or checkpoint detail resolves the difference. Do not choose a maximum. AA methodology describes GDPval-AA v2.1 as 220 tasks across 44 occupations using Stirrup."
      ],
      "status": "冲突",
      "unresolved": [
        "The Xiaomi Pro-RL card reports 1673 Elo, while Artificial Analysis comparison/search records include 1691 and an older page showed 1686. These are retained as separate source rows where available; no disclosed test-condition or checkpoint detail resolves the difference. Do not choose a maximum. AA methodology describes GDPval-AA v2.1 as 220 tasks across 44 occupations using Stirrup."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Pro vs GPT-6 Astra comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-6-pro-vs-gpt-6-astra"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis reports 49% for the original HLE. Its method uses 2,158 text-only questions from the original 2,500-item dataset and reports pass@1 accuracy; the source page does not disclose an evaluation date or checkpoint revision. The existing Agents’ Last Exam 31.6 row is a different benchmark and was not reused."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
        },
        {
          "label": "OSWorld-V2 official README",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        }
      ],
      "notes": [
        "The model card’s 82.0 is OSWorld-Verified, not OSWorld v2.1. No exact v2.1 result was found; the existing OSWorld-Verified row is preserved without remapping."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
        },
        {
          "label": "SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Xiaomi MiMo-V2.6 launch report",
          "url": "https://mimo.mi.com/docs/en-US/news/latest/v2-6"
        }
      ],
      "notes": [
        "No exact Pro-RL result was found in these sources; scores from SWE-bench Verified or another Pro version were not reused."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.6-Pro-RL official model card",
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
        },
        {
          "label": "Terminal-Bench Science announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor Terminal-Bench Science leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "No exact Pro-RL result was found in the model card or announcement. The Harbor leaderboard is dynamically rendered and the current rows were not extractable, so absence cannot be fully confirmed."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Pro-RL result was found in the model card or announcement. The Harbor leaderboard is dynamically rendered and the current rows were not extractable, so absence cannot be fully confirmed."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "Harbor Terminal-Bench 4 result for exact Pro-RL checkpoint",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=XiaomiMiMo/MiMo-V2.6-Pro-RL&leaderboard_task_id=terminalbench_4"
        },
        {
          "label": "Terminal-Bench 4.0 version and method",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The exact Pro-RL checkpoint is listed at 34.9. Official Hub identifies dataset terminal-bench/terminal-bench@4.0.0 with 66 test tasks; the benchmark metric is task resolution rate. Effort and the run-specific harness were not disclosed."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T09:11+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals MiMo V2.6 Pro model page and test settings",
          "url": "https://www.vals.ai/models/xiaomi_mimo-v2.6-pro"
        },
        {
          "label": "Xiaomi MOPD checkpoint and API update note",
          "url": "https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition"
        }
      ],
      "notes": [
        "Vals reports 57.81% through the Xiaomi provider/API with temperature 1 and top_p 0.95, but does not disclose the exact checkpoint revision. Xiaomi states that the API alias was updated to MOPD while retaining its name; this TOML entry points to the Pro-RL weights, so no API score is copied pending exact variant confirmation."
      ],
      "status": "待核实",
      "unresolved": [
        "Vals reports 57.81% through the Xiaomi provider/API with temperature 1 and top_p 0.95, but does not disclose the exact checkpoint revision. Xiaomi states that the API alias was updated to MOPD while retaining its name; this TOML entry points to the Pro-RL weights, so no API score is copied pending exact variant confirmation."
      ]
    }
  },
  "existing_records": 17,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T09:11+08:00",
  "model_id": "xiaomi/mimo-v2.6-pro",
  "new_records": 3,
  "overall_status": "待复核"
}

-->
