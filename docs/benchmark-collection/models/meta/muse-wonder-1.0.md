# Muse Wonder Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-wonder-1.0
- 模型名称：Muse Wonder
- 发布日期：2026-10-12
- 最近检查时间：2026-11-04T03:11+08:00
- 整体处理状态：待复核
- 新增成绩数量：7
- 收集前已有成绩数量：13
- 当前已收录的对应成绩数量：9

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 78.8 (metric=pass@1; version=1.1; variant=max effort) | [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card), [DataCurve DeepSWE leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T03:11+08:00 |
| swe-bench-pro-v2 | 已收录 | 96.73 (metric=task resolution rate; version=2.0.0; dataset=SWE-bench Pro V2 Full (642 tasks); reported 96.73 ± 1.12%; effort=xhigh; variant=Full; harness=mini-swe-agent) | [Scale AI SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T03:11+08:00 |
| terminal-bench-v4 | 已收录 | 49.49 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (66 tasks); reported ±2.20 percentage points; effort=max; variant=Vals AI independent run; source labels score accuracy; avg@3 (each run pass@1); harness=Mini-SWE-agent) | [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Vals Muse Wonder model profile](https://www.vals.ai/models/meta_muse-wonder), [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card), [Artificial Analysis Terminal-Bench 4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T03:11+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 26 (metric=task resolution rate; version=0.1.0; dataset=Terminal-Bench Science v0.1.0 (70 tasks); effort=max; variant=Artificial Analysis run; source labels score accuracy; pass@1 averaged over 3 repeats; score displayed as an integer percent; harness=mini-swe-agent); 22.86 (metric=task resolution rate; version=0.1.0; dataset=Terminal-Bench Science v0.1.0 (70 tasks); reported ±5.05 percentage points; effort=max; variant=Vals AI run; source labels score accuracy; single pass@1; harness=Mini-SWE-agent) | [Artificial Analysis Muse Wonder comparison](https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-gpt-6-astra), [Artificial Analysis Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Vals Muse Wonder model profile](https://www.vals.ai/models/meta_muse-wonder) | 2026-11-04T03:11+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card), [Artificial Analysis AutomationBench-AA evaluation](https://artificialanalysis.ai/evaluations/automationbench-aa), [Artificial Analysis evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T03:11+08:00 |
| osworld-v2.1 | 已存在 | 34.3 (metric=binary task completion rate; version=osworld-v2.1; variant=max effort; source labels this binary completion rate) | [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T03:11+08:00 |
| chartography | 未找到 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and protocol](https://arxiv.org/html/2608.10677v1), [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card) | 2026-11-04T03:11+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale original Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Scale HLE-Diamond leaderboard](https://labs.scale.com/leaderboard/hle-diamond), [Humanity’s Last Exam official site](https://lastexam.ai/), [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card) | 2026-11-04T03:11+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 43 (metric=index score; version=5.0; dataset=Artificial Analysis Intelligence Index V5 composite (9 evaluations); effort=max) | [Artificial Analysis Muse Wonder model page](https://artificialanalysis.ai/models/muse-wonder), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card) | 2026-11-04T03:11+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1770 (metric=Elo rating; version=2.1; dataset=GDPval-AA v2.1 (220 tasks; 44 occupations; 9 industries); effort=Max; harness=Stirrup agent loop (shell and web browsing)) | [Artificial Analysis GDPval-AA v2.1 leaderboard and protocol](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa), [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card) | 2026-11-04T03:11+08:00 |
| vals-index-v2.2 | 已收录 | 64.88 (metric=performance score; version=2.2; dataset=Vals Index composite (finance, coding, legal, tax); effort=max; variant=model profile reports ±1.07) | [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Muse Wonder model profile](https://www.vals.ai/models/meta_muse-wonder) | 2026-11-04T03:11+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 已确认成绩 1

- name: DeepSWE
- score: 78.8
- metric: pass@1
- version: 1.1
- variant: max effort
- source: [https://research.meta.ai/static/muse-wonder-model-card](https://research.meta.ai/static/muse-wonder-model-card)

已检查的主要资料：
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)
- [DataCurve DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Kept the existing 78.8 pass@1 result for exact Muse Wonder 1.0 / DeepSWE v1.1. Meta attributes this result to DataCurve and describes the 113-task benchmark; the current public DataCurve table did not expose a Wonder row for independent row-level re-verification. Removed the model-release date from this result because no evaluation date is stated.

最近核验时间：2026-11-04T03:11+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 已确认成绩 1

- name: SWE-bench Pro
- score: 96.73
- metric: task resolution rate
- version: 2.0.0
- dataset: SWE-bench Pro V2 Full (642 tasks); reported 96.73 ± 1.12%
- effort: xhigh
- variant: Full
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Added the exact Muse Wonder 1.0 V2 Full result: 96.73 ± 1.12%, mini-swe-agent, xhigh. The V2 Full set has 642 tasks; this is not the HARD subset. The leaderboard update date is not an evaluation date.

最近核验时间：2026-11-04T03:11+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 49.49
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (66 tasks); reported ±2.20 percentage points
- effort: max
- variant: Vals AI independent run; source labels score accuracy; avg@3 (each run pass@1)
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/models/meta_muse-wonder](https://www.vals.ai/models/meta_muse-wonder)

已检查的主要资料：
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Vals Muse Wonder model profile](https://www.vals.ai/models/meta_muse-wonder)
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)
- [Artificial Analysis Terminal-Bench 4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- Added the separate Vals Wonder run (49.49 ± 2.20%, avg@3, Mini-SWE-agent) with the repository canonical task-resolution metric. Preserved the pre-existing 52.0 Artificial Analysis row as a distinct reported-accuracy variant; no evaluation date is published for either.

最近核验时间：2026-11-04T03:11+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 26
- metric: task resolution rate
- version: 0.1.0
- dataset: Terminal-Bench Science v0.1.0 (70 tasks)
- effort: max
- variant: Artificial Analysis run; source labels score accuracy; pass@1 averaged over 3 repeats; score displayed as an integer percent
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-gpt-6-astra](https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-gpt-6-astra)

#### 已确认成绩 2

- name: Terminal-Bench-Science
- score: 22.86
- metric: task resolution rate
- version: 0.1.0
- dataset: Terminal-Bench Science v0.1.0 (70 tasks); reported ±5.05 percentage points
- effort: max
- variant: Vals AI run; source labels score accuracy; single pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/models/meta_muse-wonder](https://www.vals.ai/models/meta_muse-wonder)

已检查的主要资料：
- [Artificial Analysis Muse Wonder comparison](https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-gpt-6-astra)
- [Artificial Analysis Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Vals Muse Wonder model profile](https://www.vals.ai/models/meta_muse-wonder)

研究备注：
- Added two distinct v0.1.0 results: Artificial Analysis reports 26% (displayed as an integer, pass@1 averaged over three repeats); Vals reports 22.86 ± 5.05% (single pass@1 run). Both use Mini-SWE-agent. The repository metric is task resolution rate; sources display accuracy. No evaluation dates are stated.

最近核验时间：2026-11-04T03:11+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)
- [Artificial Analysis AutomationBench-AA evaluation](https://artificialanalysis.ai/evaluations/automationbench-aa)
- [Artificial Analysis evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- The model file already contains a 39.1 strict pass@1 Artificial Analysis AutomationBench-AA result. AA documents a 657-task held-out v1.0.6-derived dataset, but its AA protocol/metric differs from the Zapier-hosted leaderboard target; the current Zapier table did not expose a Muse Wonder result. The existing row is retained and now identifies the AA dataset version.

尚未解决的问题：
- Cannot verify an exact Zapier 1.0.6 task_completed_correctly score or establish that the existing AA strict-pass metric is identical to the benchmark definition.

最近核验时间：2026-11-04T03:11+08:00

### OSWorld (osworld-v2.1)

#### 已确认成绩 1

- name: OSWorld
- score: 34.3
- metric: binary task completion rate
- version: osworld-v2.1
- variant: max effort; source labels this binary completion rate
- source: [https://research.meta.ai/static/muse-wonder-model-card](https://research.meta.ai/static/muse-wonder-model-card)

已检查的主要资料：
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- The existing 34.3 strict binary completion result is the benchmark definition’s binary task-completion measure; its metric wording and version were aligned to the local canonical definition using the exact V2.1 source description. The separate 72.6 mean partial-reward result remains unchanged as a different metric. Removed release-date values from both records because the source does not publish evaluation dates.

最近核验时间：2026-11-04T03:11+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and protocol](https://arxiv.org/html/2608.10677v1)
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)

研究备注：
- Checked the Chartography section of the official leaderboard and the model card; neither reports Muse Wonder. Other Muse Wonder rows on the Surge page belong to separate DAYJOB benchmarks and were not reused. The model is compatible with the chart-image/text-answer protocol, so this is a no-result finding rather than not-applicable.

最近核验时间：2026-11-04T03:11+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale original Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Scale HLE-Diamond leaderboard](https://labs.scale.com/leaderboard/hle-diamond)
- [Humanity’s Last Exam official site](https://lastexam.ai/)
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)

研究备注：
- No Muse Wonder score was found for the original finalized 2,500-question HLE. Scale’s 37.30% Muse Wonder result is HLE-Diamond, a separate 1,000-question refined subset, and was not recorded as original HLE.

最近核验时间：2026-11-04T03:11+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 43
- metric: index score
- version: 5.0
- dataset: Artificial Analysis Intelligence Index V5 composite (9 evaluations)
- effort: max
- source: [https://artificialanalysis.ai/models/muse-wonder](https://artificialanalysis.ai/models/muse-wonder)

已检查的主要资料：
- [Artificial Analysis Muse Wonder model page](https://artificialanalysis.ai/models/muse-wonder)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)

研究备注：
- Added current Artificial Analysis Intelligence Index V5.0 score 43 for Muse Wonder (max). Preserved the existing score 52 as V4.3; it is a different composite version. V5 contains HLE-Diamond, not the original HLE. No evaluation date was stated.

最近核验时间：2026-11-04T03:11+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 已确认成绩 1

- name: GDPval-AA
- score: 1770
- metric: Elo rating
- version: 2.1
- dataset: GDPval-AA v2.1 (220 tasks; 44 occupations; 9 industries)
- effort: Max
- harness: Stirrup agent loop (shell and web browsing)
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and protocol](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)
- [Meta Muse Wonder model card](https://research.meta.ai/static/muse-wonder-model-card)

研究备注：
- Added Muse Wonder (Max) score 1770 Elo, distinct from Muse Wonder Full (Max) at 1857. The evaluation uses the 220-task / 44-occupation GDPval-AA v2.1 dataset and a Stirrup shell/web agent loop. No evaluation date was stated.

最近核验时间：2026-11-04T03:11+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 64.88
- metric: performance score
- version: 2.2
- dataset: Vals Index composite (finance, coding, legal, tax)
- effort: max
- variant: model profile reports ±1.07
- source: [https://www.vals.ai/models/meta_muse-wonder](https://www.vals.ai/models/meta_muse-wonder)

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Muse Wonder model profile](https://www.vals.ai/models/meta_muse-wonder)

研究备注：
- Added the exact Wonder composite score 64.88% (profile reports ±1.07; reasoning effort max). Preserved existing Finance Agent v2 as a distinct component result, not the Vals Index. Wonder Full is a different model with a different score. The leaderboard update date is not an evaluation date.

最近核验时间：2026-11-04T03:11+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Wonder model page",
          "url": "https://artificialanalysis.ai/models/muse-wonder"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        }
      ],
      "notes": [
        "Added current Artificial Analysis Intelligence Index V5.0 score 43 for Muse Wonder (max). Preserved the existing score 52 as V4.3; it is a different composite version. V5 contains HLE-Diamond, not the original HLE. No evaluation date was stated."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/automationbench-aa"
        },
        {
          "label": "Artificial Analysis evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "The model file already contains a 39.1 strict pass@1 Artificial Analysis AutomationBench-AA result. AA documents a 657-task held-out v1.0.6-derived dataset, but its AA protocol/metric differs from the Zapier-hosted leaderboard target; the current Zapier table did not expose a Muse Wonder result. The existing row is retained and now identifies the AA dataset version."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot verify an exact Zapier 1.0.6 task_completed_correctly score or establish that the existing AA strict-pass metric is identical to the benchmark definition."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper and protocol",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        }
      ],
      "notes": [
        "Checked the Chartography section of the official leaderboard and the model card; neither reports Muse Wonder. Other Muse Wonder rows on the Surge page belong to separate DAYJOB benchmarks and were not reused. The model is compatible with the chart-image/text-answer protocol, so this is a no-result finding rather than not-applicable."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        },
        {
          "label": "DataCurve DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Kept the existing 78.8 pass@1 result for exact Muse Wonder 1.0 / DeepSWE v1.1. Meta attributes this result to DataCurve and describes the 113-task benchmark; the current public DataCurve table did not expose a Wonder row for independent row-level re-verification. Removed the model-release date from this result because no evaluation date is stated."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and protocol",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        },
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        }
      ],
      "notes": [
        "Added Muse Wonder (Max) score 1770 Elo, distinct from Muse Wonder Full (Max) at 1857. The evaluation uses the 220-task / 44-occupation GDPval-AA v2.1 dataset and a Stirrup shell/web agent loop. No evaluation date was stated."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Scale original Humanity’s Last Exam leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Scale HLE-Diamond leaderboard",
          "url": "https://labs.scale.com/leaderboard/hle-diamond"
        },
        {
          "label": "Humanity’s Last Exam official site",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        }
      ],
      "notes": [
        "No Muse Wonder score was found for the original finalized 2,500-question HLE. Scale’s 37.30% Muse Wonder result is HLE-Diamond, a separate 1,000-question refined subset, and was not recorded as original HLE."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "The existing 34.3 strict binary completion result is the benchmark definition’s binary task-completion measure; its metric wording and version were aligned to the local canonical definition using the exact V2.1 source description. The separate 72.6 mean partial-reward result remains unchanged as a different metric. Removed release-date values from both records because the source does not publish evaluation dates."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Added the exact Muse Wonder 1.0 V2 Full result: 96.73 ± 1.12%, mini-swe-agent, xhigh. The V2 Full set has 642 tasks; this is not the HARD subset. The leaderboard update date is not an evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Wonder comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-gpt-6-astra"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Vals Muse Wonder model profile",
          "url": "https://www.vals.ai/models/meta_muse-wonder"
        }
      ],
      "notes": [
        "Added two distinct v0.1.0 results: Artificial Analysis reports 26% (displayed as an integer, pass@1 averaged over three repeats); Vals reports 22.86 ± 5.05% (single pass@1 run). Both use Mini-SWE-agent. The repository metric is task resolution rate; sources display accuracy. No evaluation dates are stated."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals Muse Wonder model profile",
          "url": "https://www.vals.ai/models/meta_muse-wonder"
        },
        {
          "label": "Meta Muse Wonder model card",
          "url": "https://research.meta.ai/static/muse-wonder-model-card"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "Added the separate Vals Wonder run (49.49 ± 2.20%, avg@3, Mini-SWE-agent) with the repository canonical task-resolution metric. Preserved the pre-existing 52.0 Artificial Analysis row as a distinct reported-accuracy variant; no evaluation date is published for either."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T03:11+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Muse Wonder model profile",
          "url": "https://www.vals.ai/models/meta_muse-wonder"
        }
      ],
      "notes": [
        "Added the exact Wonder composite score 64.88% (profile reports ±1.07; reasoning effort max). Preserved existing Finance Agent v2 as a distinct component result, not the Vals Index. Wonder Full is a different model with a different score. The leaderboard update date is not an evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 13,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T03:11+08:00",
  "model_id": "meta/muse-wonder-1.0",
  "new_records": 7,
  "overall_status": "待复核"
}

-->
