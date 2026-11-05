# Inkling Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：thinkingmachines/inkling
- 模型名称：Inkling
- 发布日期：2026-07-15
- 最近检查时间：2026-11-05T00:18+08:00
- 整体处理状态：待复核
- 新增成绩数量：11
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：9

## 模型身份与范围说明

- The official Thinking Machines model card identifies Inkling as the model released on 2026-07-15. Records from different benchmark versions, independent harnesses, and data subsets are kept separate; the official model card’s earlier-checkpoint HLE values were not assigned to the released checkpoint.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 live leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Inkling official release report](https://thinkingmachines.ai/news/introducing-inkling/) | 2026-11-05T00:18+08:00 |
| swe-bench-pro-v2 | 已收录 | 89.88 (metric=task resolution rate; version=2.0.0; dataset=SWE-bench Pro V2 Full public set (642 tasks); effort=xhigh; variant=reported ±2.10; uncapped cost limit; 250-turn limit; harness=mini-swe-agent) | [SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Inkling official model card](https://thinkingmachines.ai/model-card/inkling/) | 2026-11-05T00:18+08:00 |
| terminal-bench-v4 | 已收录 | 1 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (66 tasks); effort=Xhigh; variant=AA independent evaluation; pass@1 averaged over three repeats per task; 500-step cap; harness=mini-swe-agent); 0.51 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (66 tasks); effort=0.99; variant=Vals AI avg@3; pass@1 per run; reported ±0.51; 8-hour task timeout; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-4), [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh), [Artificial Analysis Terminal-Bench methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T00:18+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 0 (metric=task resolution rate; version=0.1.0; dataset=Terminal-Bench-Science 0.1.0 (70 tasks); effort=Xhigh; variant=AA independent evaluation; pass@1 averaged over three repeats per task; harness=mini-swe-agent) | [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh), [Artificial Analysis Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Terminal-Bench-Science official leaderboard](https://terminal-bench-science.ai/) | 2026-11-05T00:18+08:00 |
| automationbench-v1.0.6 | 待核实 | 5 (metric=AutomationBench-AA Score; version=1.0.6; dataset=Private held-out split (657 tasks across six business domains); effort=Xhigh; variant=AA headline score: zero for any guardrail violation, otherwise share of objectives completed; one run per task; 50-turn cap) | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench source repository](https://github.com/zapier/AutomationBench), [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh), [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T00:18+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2.1 public evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld public evaluation page](https://osworld-v2.xlang.ai/) | 2026-11-05T00:18+08:00 |
| chartography | 待核实 | 10 (metric=accuracy (mean; Pass@1); dataset=Chartography full set (100 tasks); effort=High reasoning; variant=Official leaderboard entry; run count not reported; paper says 20 trials per task while current harness README says 10 runs; harness=Inspect AI) | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography methodology paper](https://arxiv.org/abs/2608.10677), [Chartography official harness README](https://github.com/surge-ai/chartography) | 2026-11-05T00:18+08:00 |
| humanitys-last-exam | 已收录 | 32 (metric=accuracy; dataset=HLE text-only subset (2,158 questions); effort=Xhigh; variant=Artificial Analysis independent evaluation; text-only, no tools) | [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Inkling official model card](https://thinkingmachines.ai/model-card/inkling/), [Inkling official release report](https://thinkingmachines.ai/news/introducing-inkling/) | 2026-11-05T00:18+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 12 (metric=index score; version=5.0; dataset=Nine-evaluation composite; effort=Xhigh); 12 (metric=index score; version=5.0.1; dataset=Nine-evaluation composite; effort=Xhigh) | [Artificial Analysis comparison showing Index v5.0](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh), [Artificial Analysis current Inkling page showing Index v5.0.1](https://artificialanalysis.ai/models/inkling), [Artificial Analysis Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T00:18+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1080 (metric=Elo rating; version=2.1; dataset=GDPval public set (220 tasks across 44 occupations); effort=Xhigh; variant=reported interval −22/+22; shell and web browsing; harness=Stirrup) | [GDPval-AA V2.1 dedicated leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis older Inkling comparison row](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh), [GDPval-AA V2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T00:18+08:00 |
| vals-index-v2.2 | 已收录 | 28.96 (metric=performance score; version=2.2; dataset=GDP-weighted finance, coding, legal, and tax evaluations; effort=0.99; variant=reported ±1.12; Inkling via Thinking Machines) | [Vals Index V2.2 leaderboard](https://vals-ai.com/benchmarks/vals_index), [Vals Inkling model page with score, interval, and effort](https://vals-ai.com/models/thinkingmachines_inkling) | 2026-11-05T00:18+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 live leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Inkling official release report](https://thinkingmachines.ai/news/introducing-inkling/)

研究备注：
- The exact Inkling model was not present in the checked official DeepSWE v1.1 leaderboard data; unverified third-party numbers were excluded.

最近核验时间：2026-11-05T00:18+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 89.88
- metric: task resolution rate
- version: 2.0.0
- dataset: SWE-bench Pro V2 Full public set (642 tasks)
- effort: xhigh
- variant: reported ±2.10; uncapped cost limit; 250-turn limit
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Inkling official model card](https://thinkingmachines.ai/model-card/inkling/)

研究备注：
- Scale V2 Full lists Inkling (mini-swe-agent) xhigh at 89.88 with reported ±2.10; it is the 642-task V2 public set with uncapped cost and a 250-turn limit. The leaderboard does not publish a checkpoint hash. No evaluation date was given, so date is omitted.

最近核验时间：2026-11-05T00:18+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 1
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (66 tasks)
- effort: Xhigh
- variant: AA independent evaluation; pass@1 averaged over three repeats per task; 500-step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 0.51
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (66 tasks)
- effort: 0.99
- variant: Vals AI avg@3; pass@1 per run; reported ±0.51; 8-hour task timeout
- harness: Mini-SWE-agent
- source: [https://vals-ai.com/models/thinkingmachines_inkling](https://vals-ai.com/models/thinkingmachines_inkling)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-4)
- [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- [Artificial Analysis Terminal-Bench methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Two independent evaluations are recorded separately: Artificial Analysis reports 1% at Xhigh using mini-swe-agent, pass@1 averaged over three repeats, and a 500-step cap; Vals reports 0.51% ±0.51 at reasoning effort 0.99 using Mini-SWE-agent and avg@3. Vals labels its task-pass percentage Accuracy; the source benchmark checks binary task completion, matching the local task-resolution metric.

最近核验时间：2026-11-05T00:18+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 0
- metric: task resolution rate
- version: 0.1.0
- dataset: Terminal-Bench-Science 0.1.0 (70 tasks)
- effort: Xhigh
- variant: AA independent evaluation; pass@1 averaged over three repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- [Artificial Analysis Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Terminal-Bench-Science official leaderboard](https://terminal-bench-science.ai/)

研究备注：
- Artificial Analysis explicitly reports 0% for Inkling (Xhigh) on the 70-task 0.1.0 release, using mini-swe-agent and pass@1 averaged over three repeats. This is a published zero score, not a missing-result placeholder; it is an independent run rather than an entry on the upstream leaderboard.

最近核验时间：2026-11-05T00:18+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 5
- metric: AutomationBench-AA Score
- version: 1.0.6
- dataset: Private held-out split (657 tasks across six business domains)
- effort: Xhigh
- variant: AA headline score: zero for any guardrail violation, otherwise share of objectives completed; one run per task; 50-turn cap
- source: [https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench source repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis reports AutomationBench-AA score 5% on the exact v1.0.6 private held-out split (657 tasks), with one run per task, a 50-turn cap, and API tools. This objective-completion headline metric differs from Zapier’s task_completed_correctly metric and is retained as a raw, unmapped row; the Zapier full result row is not confirmed.

尚未解决的问题：
- The 5% AutomationBench-AA score is not comparable to the target definition’s task_completed_correctly metric; a precise Zapier primary-metric score for Inkling was not verified.

最近核验时间：2026-11-05T00:18+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2.1 public evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld public evaluation page](https://osworld-v2.xlang.ai/)

研究备注：
- No exact Inkling result for OSWorld V2.1 was found in the checked public sources. Results for OSWorld 1.0 or V2.0 were not transferred; the public verified V2.1 data remains limited.

最近核验时间：2026-11-05T00:18+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 10
- metric: accuracy (mean; Pass@1)
- dataset: Chartography full set (100 tasks)
- effort: High reasoning
- variant: Official leaderboard entry; run count not reported; paper says 20 trials per task while current harness README says 10 runs
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography methodology paper](https://arxiv.org/abs/2608.10677)
- [Chartography official harness README](https://github.com/surge-ai/chartography)

研究备注：
- The official live leaderboard lists Inkling (High reasoning) at 10% on the full 100-task set. The row does not publish a run count or evaluation date. The paper describes 20 trials per task, while the current harness README describes 10 runs. The score is retained with the configuration unresolved.

尚未解决的问题：
- The published trial protocol differs between the paper and current README, and the Inkling leaderboard row does not specify its run count.

最近核验时间：2026-11-05T00:18+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 32
- metric: accuracy
- dataset: HLE text-only subset (2,158 questions)
- effort: Xhigh
- variant: Artificial Analysis independent evaluation; text-only, no tools
- source: [https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Inkling comparison](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Inkling official model card](https://thinkingmachines.ai/model-card/inkling/)
- [Inkling official release report](https://thinkingmachines.ai/news/introducing-inkling/)

研究备注：
- Artificial Analysis reports 32% for Inkling (Xhigh) on HLE’s 2,158-question text-only subset; this is a subset score, not a result on all 2,500 questions or HLE-Diamond. The Inkling model card’s 29.7% text-only and 46.0% with-tools results are not added because the release article identifies those HLE runs as an earlier checkpoint.

最近核验时间：2026-11-05T00:18+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 12
- metric: index score
- version: 5.0
- dataset: Nine-evaluation composite
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 12
- metric: index score
- version: 5.0.1
- dataset: Nine-evaluation composite
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/inkling](https://artificialanalysis.ai/models/inkling)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis comparison showing Index v5.0](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- [Artificial Analysis current Inkling page showing Index v5.0.1](https://artificialanalysis.ai/models/inkling)
- [Artificial Analysis Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The exact v5.0 comparison row reports 12; the current model page reports 12 for v5.0.1. Both versioned rows are preserved separately. The current v5.0.1 definition also contains nine evaluations, but it is not merged into the target v5.0 row.

最近核验时间：2026-11-05T00:18+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1080
- metric: Elo rating
- version: 2.1
- dataset: GDPval public set (220 tasks across 44 occupations)
- effort: Xhigh
- variant: reported interval −22/+22; shell and web browsing
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [GDPval-AA V2.1 dedicated leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis older Inkling comparison row](https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh)
- [GDPval-AA V2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The dedicated current V2.1 leaderboard lists Inkling (Xhigh) at 1080 Elo with interval −22/+22 on 220 tasks; that direct target page is recorded in TOML. An Artificial Analysis comparison page lists 1081 Elo for the same model/effort. The pages do not expose enough run metadata to reconcile the one-point difference, so neither value is silently treated as a correction.

尚未解决的问题：
- Artificial Analysis’s dedicated V2.1 board reports 1080 while its comparison page reports 1081 for Inkling (Xhigh); no dated revision or condition difference resolves the discrepancy.

最近核验时间：2026-11-05T00:18+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 28.96
- metric: performance score
- version: 2.2
- dataset: GDP-weighted finance, coding, legal, and tax evaluations
- effort: 0.99
- variant: reported ±1.12; Inkling via Thinking Machines
- source: [https://vals-ai.com/models/thinkingmachines_inkling](https://vals-ai.com/models/thinkingmachines_inkling)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://vals-ai.com/benchmarks/vals_index)
- [Vals Inkling model page with score, interval, and effort](https://vals-ai.com/models/thinkingmachines_inkling)

研究备注：
- Vals Index V2.2 lists Inkling at 28.96% ±1.12. The model page gives reasoning effort 0.99; the benchmark is a GDP-weighted composite of finance, coding, legal, and tax tasks. The page update date is not treated as the evaluation date.

最近核验时间：2026-11-05T00:18+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison showing Index v5.0",
          "url": "https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh"
        },
        {
          "label": "Artificial Analysis current Inkling page showing Index v5.0.1",
          "url": "https://artificialanalysis.ai/models/inkling"
        },
        {
          "label": "Artificial Analysis Index evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The exact v5.0 comparison row reports 12; the current model page reports 12 for v5.0.1. Both versioned rows are preserved separately. The current v5.0.1 definition also contains nine evaluations, but it is not merged into the target v5.0 row."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench source repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Artificial Analysis Inkling comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis reports AutomationBench-AA score 5% on the exact v1.0.6 private held-out split (657 tasks), with one run per task, a 50-turn cap, and API tools. This objective-completion headline metric differs from Zapier’s task_completed_correctly metric and is retained as a raw, unmapped row; the Zapier full result row is not confirmed."
      ],
      "status": "待核实",
      "unresolved": [
        "The 5% AutomationBench-AA score is not comparable to the target definition’s task_completed_correctly metric; a precise Zapier primary-metric score for Inkling was not verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography methodology paper",
          "url": "https://arxiv.org/abs/2608.10677"
        },
        {
          "label": "Chartography official harness README",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "The official live leaderboard lists Inkling (High reasoning) at 10% on the full 100-task set. The row does not publish a run count or evaluation date. The paper describes 20 trials per task, while the current harness README describes 10 runs. The score is retained with the configuration unresolved."
      ],
      "status": "待核实",
      "unresolved": [
        "The published trial protocol differs between the paper and current README, and the Inkling leaderboard row does not specify its run count."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 live leaderboard data",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "Inkling official release report",
          "url": "https://thinkingmachines.ai/news/introducing-inkling/"
        }
      ],
      "notes": [
        "The exact Inkling model was not present in the checked official DeepSWE v1.1 leaderboard data; unverified third-party numbers were excluded."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA V2.1 dedicated leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis older Inkling comparison row",
          "url": "https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh"
        },
        {
          "label": "GDPval-AA V2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The dedicated current V2.1 leaderboard lists Inkling (Xhigh) at 1080 Elo with interval −22/+22 on 220 tasks; that direct target page is recorded in TOML. An Artificial Analysis comparison page lists 1081 Elo for the same model/effort. The pages do not expose enough run metadata to reconcile the one-point difference, so neither value is silently treated as a correction."
      ],
      "status": "冲突",
      "unresolved": [
        "Artificial Analysis’s dedicated V2.1 board reports 1080 while its comparison page reports 1081 for Inkling (Xhigh); no dated revision or condition difference resolves the discrepancy."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Inkling comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Inkling official model card",
          "url": "https://thinkingmachines.ai/model-card/inkling/"
        },
        {
          "label": "Inkling official release report",
          "url": "https://thinkingmachines.ai/news/introducing-inkling/"
        }
      ],
      "notes": [
        "Artificial Analysis reports 32% for Inkling (Xhigh) on HLE’s 2,158-question text-only subset; this is a subset score, not a result on all 2,500 questions or HLE-Diamond. The Inkling model card’s 29.7% text-only and 46.0% with-tools results are not added because the release article identifies those HLE runs as an earlier checkpoint."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2.1 public evaluation guide",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld public evaluation page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "No exact Inkling result for OSWorld V2.1 was found in the checked public sources. Results for OSWorld 1.0 or V2.0 were not transferred; the public verified V2.1 data remains limited."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Inkling official model card",
          "url": "https://thinkingmachines.ai/model-card/inkling/"
        }
      ],
      "notes": [
        "Scale V2 Full lists Inkling (mini-swe-agent) xhigh at 89.88 with reported ±2.10; it is the 642-task V2 public set with uncapped cost and a 250-turn limit. The leaderboard does not publish a checkpoint hash. No evaluation date was given, so date is omitted."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Inkling comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science official leaderboard",
          "url": "https://terminal-bench-science.ai/"
        }
      ],
      "notes": [
        "Artificial Analysis explicitly reports 0% for Inkling (Xhigh) on the 70-task 0.1.0 release, using mini-swe-agent and pass@1 averaged over three repeats. This is a published zero score, not a missing-result placeholder; it is an independent run rather than an entry on the upstream leaderboard."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard and methodology",
          "url": "https://vals-ai.com/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis Inkling comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/inkling-vs-gpt-5-6-sol-xhigh"
        },
        {
          "label": "Artificial Analysis Terminal-Bench methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Two independent evaluations are recorded separately: Artificial Analysis reports 1% at Xhigh using mini-swe-agent, pass@1 averaged over three repeats, and a 500-step cap; Vals reports 0.51% ±0.51 at reasoning effort 0.99 using Mini-SWE-agent and avg@3. Vals labels its task-pass percentage Accuracy; the source benchmark checks binary task completion, matching the local task-resolution metric."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T00:18+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://vals-ai.com/benchmarks/vals_index"
        },
        {
          "label": "Vals Inkling model page with score, interval, and effort",
          "url": "https://vals-ai.com/models/thinkingmachines_inkling"
        }
      ],
      "notes": [
        "Vals Index V2.2 lists Inkling at 28.96% ±1.12. The model page gives reasoning effort 0.99; the benchmark is a GDP-weighted composite of finance, coding, legal, and tax tasks. The page update date is not treated as the evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T00:18+08:00",
  "model_id": "thinkingmachines/inkling",
  "model_notes": [
    "The official Thinking Machines model card identifies Inkling as the model released on 2026-07-15. Records from different benchmark versions, independent harnesses, and data subsets are kept separate; the official model card’s earlier-checkpoint HLE values were not assigned to the released checkpoint."
  ],
  "new_records": 11,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
