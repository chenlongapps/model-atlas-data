# DeepSeek V4.1 Flash 1017 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4.1-flash-1017
- 模型名称：DeepSeek V4.1 Flash 1017
- 发布日期：2026-10-17
- 最近检查时间：2026-11-04T02:16+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：12

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 77.0 (metric=pass@1; version=1.1; dataset=DeepSWE v1.1 (113 tasks); harness=Mini-SWE-V2) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [DeepSWE 官方榜单精确模型结果](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=deepseek-ai/DeepSeek-V4.1-Flash-1017&leaderboard_task_id=deep_swe), [DeepSWE v1.1 方法页](https://deepswe.datacurve.ai/) | 2026-11-04T02:16+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 Full 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | 2026-11-04T02:16+08:00 |
| terminal-bench-v4 | 已存在 | 42.3 (metric=task resolution rate; version=4.0.0; harness=Claude Code) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [Harbor Terminal-Bench 4 官方精确结果](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=deepseek-ai/DeepSeek-V4.1-Flash-1017&leaderboard_task_id=terminalbench_4), [Terminal-Bench 4.0 官方版本与协议](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T02:16+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 12.9 (metric=task resolution rate; version=0.1.0; dataset=harborframework/terminal-bench-science; terminalbenchscience_0_1 (70 tasks); effort=Max; variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [DeepSeek 官方评测结果记录](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/discussions/40), [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [Artificial Analysis Terminal-Bench Science 方法页](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T02:16+08:00 |
| automationbench-v1.0.6 | 已存在 | 60.5 (metric=task_completed_correctly; version=1.0.6) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [DeepSeek 10 月 17 日发布公告](https://api-docs.deepseek.com/updates/), [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库与指标说明](https://github.com/zapier/AutomationBench) | 2026-11-04T02:16+08:00 |
| osworld-v2.1 | 待核实 | — | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [DeepSeek 10 月 17 日发布公告](https://api-docs.deepseek.com/updates/), [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 官方项目页](https://osworld-v2.xlang.ai/), [Kimi K3.1 Pro 官方比较图及评测说明](https://www.kimi.com/en/blog/kimi-k3-1-pro), [DataLearner OSWorld 2.1 二手榜单](https://www.datalearner.com/benchmarks/osworld-2-1), [AIEvals DeepSeek V4.1 Flash 1017 二手模型页](https://aievals.app/models/deepseek-v4-1-flash-1017) | 2026-11-04T02:16+08:00 |
| chartography | 已存在 | 83.0 (metric=accuracy (mean; Pass@1); version=unspecified; variant=with tools) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测仓库与 scorer](https://github.com/surge-ai/chartography) | 2026-11-04T02:16+08:00 |
| humanitys-last-exam | 已存在 | 42.6 (metric=accuracy; version=unspecified; dataset=full set; variant=without tools); 44.0 (metric=accuracy; version=unspecified; dataset=text-only subset; variant=without tools) | [DeepSeek 官方模型卡及 HLE 条件说明](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [Scale AI Humanity’s Last Exam 官方页面](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T02:16+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 32 (metric=index score; version=5.0; effort=Max); 29 (metric=index score; version=5.0; effort=High); 19 (metric=index score; version=5.0; variant=Non-reasoning) | [Artificial Analysis DeepSeek V4.1 Flash 1017 发布页](https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017), [Artificial Analysis Intelligence Index V5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T02:16+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1746 (metric=Elo rating; version=2.1; dataset=220 GDPval tasks; effort=Max; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T02:16+08:00 |
| vals-index-v2.2 | 已收录 | 61.26 (metric=performance score; version=2.2) | [Vals AI DeepSeek V4.1 Flash 1017 模型页](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T02:16+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 已确认成绩 1

- name: DeepSWE
- score: 77.0
- metric: pass@1
- version: 1.1
- dataset: DeepSWE v1.1 (113 tasks)
- harness: Mini-SWE-V2
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [DeepSWE 官方榜单精确模型结果](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=deepseek-ai/DeepSeek-V4.1-Flash-1017&leaderboard_task_id=deep_swe)
- [DeepSWE v1.1 方法页](https://deepswe.datacurve.ai/)

研究备注：
- The official model card and exact-model DeepSWE leaderboard entry both report 77.0 for the 1017 checkpoint. Existing record retains the model-card harness name Mini-SWE-V2; the leaderboard describes its general run stack as Pier/mini-swe-agent, so that wording difference is noted without replacing the source-specific field.

尚未解决的问题：
- DeepSeek calls the harness Mini-SWE-V2, while the leaderboard page describes Pier/mini-swe-agent generically; no source establishes whether those labels refer to the identical setup.

最近核验时间：2026-11-04T02:16+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 Full 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

研究备注：
- Checked the Scale V2 Full public leaderboard and the official DeepSeek model card; neither contains a SWE-bench Pro V2 result for this exact model. The HARD tab is a separate dataset and no score was inferred.

最近核验时间：2026-11-04T02:16+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 42.3
- metric: task resolution rate
- version: 4.0.0
- harness: Claude Code
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [Harbor Terminal-Bench 4 官方精确结果](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=deepseek-ai/DeepSeek-V4.1-Flash-1017&leaderboard_task_id=terminalbench_4)
- [Terminal-Bench 4.0 官方版本与协议](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The exact Harbor result and DeepSeek model card report 42.3 with Claude Code. The model card abbreviates the release as 4.0; Harbor identifies the dataset artifact as terminal-bench@4.0.0, matching the repository definition. The record version was aligned to that documented artifact version and the canonical task-resolution metric was added.

最近核验时间：2026-11-04T02:16+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 12.9
- metric: task resolution rate
- version: 0.1.0
- dataset: harborframework/terminal-bench-science; terminalbenchscience_0_1 (70 tasks)
- effort: Max
- variant: pass@1 averaged over three repeats
- harness: mini-swe-agent
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/discussions/40](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/discussions/40)

已检查的主要资料：
- [DeepSeek 官方评测结果记录](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/discussions/40)
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [Artificial Analysis Terminal-Bench Science 方法页](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- DeepSeek official evaluation results list 12.9 for Terminal-Bench-Science 0.1; the HF evaluation record associates the result with the (Max) model variant and Artificial Analysis. AA confirms 0.1.0, 70 tasks, mini-swe-agent, and pass@1 averaged over three repeats. The recorded metric follows the local task-resolution definition.

最近核验时间：2026-11-04T02:16+08:00

### AutomationBench (automationbench-v1.0.6)

#### 已确认成绩 1

- name: AutomationBench
- score: 60.5
- metric: task_completed_correctly
- version: 1.0.6
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [DeepSeek 10 月 17 日发布公告](https://api-docs.deepseek.com/updates/)
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库与指标说明](https://github.com/zapier/AutomationBench)

研究备注：
- The exact 1017 model card and release announcement report 60.5 for Automation-Bench v1.0.6. The canonical task_completed_correctly metric comes from Zapier’s benchmark definition. The result source does not identify public versus held-out tasks, harness, or effort, so those conditions are omitted; the score is not assigned to either task set.

最近核验时间：2026-11-04T02:16+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [DeepSeek 10 月 17 日发布公告](https://api-docs.deepseek.com/updates/)
- [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 官方项目页](https://osworld-v2.xlang.ai/)
- [Kimi K3.1 Pro 官方比较图及评测说明](https://www.kimi.com/en/blog/kimi-k3-1-pro)
- [DataLearner OSWorld 2.1 二手榜单](https://www.datalearner.com/benchmarks/osworld-2-1)
- [AIEvals DeepSeek V4.1 Flash 1017 二手模型页](https://aievals.app/models/deepseek-v4-1-flash-1017)

研究备注：
- DeepSeek official card and release note do not list OSWorld. Kimi’s official comparison blog confirms an OSWorld V2.1 evaluation using the Kimi Agent harness and its chart includes DeepSeek V4.1 Flash 1017, but the chart value is not extractable from the text. Secondary tables report 69.3 as Partial score with Max + tools; this is not the local binary task completion rate and was not written to TOML.

尚未解决的问题：
- Need a directly verifiable primary-source score and confirmation of the exact metric/configuration. Do not treat the secondary 69.3 Partial score as binary task completion rate.

最近核验时间：2026-11-04T02:16+08:00

### Chartography (chartography)

#### 已确认成绩 1

- name: Chartography
- score: 83.0
- metric: accuracy (mean; Pass@1)
- version: unspecified
- variant: with tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测仓库与 scorer](https://github.com/surge-ai/chartography)

研究备注：
- The official DeepSeek model card reports 83.0 for Chartography with tools for the exact 1017 checkpoint; the existing variant is retained. The benchmark’s official scorer supplies the canonical accuracy (mean; Pass@1) metric and its materials specify no semantic version. Surge’s separate V4.1 Flash (Max reasoning) listing is not the 1017 with-tools record and is not treated as a conflict.

最近核验时间：2026-11-04T02:16+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 已确认成绩 1

- name: Humanity's Last Exam
- score: 42.6
- metric: accuracy
- version: unspecified
- dataset: full set
- variant: without tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

#### 已确认成绩 2

- name: Humanity's Last Exam
- score: 44.0
- metric: accuracy
- version: unspecified
- dataset: text-only subset
- variant: without tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

已检查的主要资料：
- [DeepSeek 官方模型卡及 HLE 条件说明](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [Scale AI Humanity’s Last Exam 官方页面](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- The official model card reports 42.6 without tools and 44.0 for the text-only subset, marked by a dagger; both corresponding local records are preserved. The local HLE definition identifies the original set as version unspecified and uses accuracy. The source does not report effort, harness, or an evaluation date.

最近核验时间：2026-11-04T02:16+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 32
- metric: index score
- version: 5.0
- effort: Max
- source: [https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017](https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017)

#### 已确认成绩 2

- name: Artificial Analysis Intelligence Index
- score: 29
- metric: index score
- version: 5.0
- effort: High
- source: [https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017](https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017)

#### 已确认成绩 3

- name: Artificial Analysis Intelligence Index
- score: 19
- metric: index score
- version: 5.0
- variant: Non-reasoning
- source: [https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017](https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017)

已检查的主要资料：
- [Artificial Analysis DeepSeek V4.1 Flash 1017 发布页](https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017)
- [Artificial Analysis Intelligence Index V5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis lists three distinct scores for this release on Intelligence Index v5.0: Max 32, High 29, and Non-reasoning 19. All three are preserved as separate records; the composite includes nine component evaluations, including HLE-Diamond rather than the original HLE. No evaluation date or harness was stated.

最近核验时间：2026-11-04T02:16+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 已确认成绩 1

- name: GDPval-AA
- score: 1746
- metric: Elo rating
- version: 2.1
- dataset: 220 GDPval tasks
- effort: Max
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The official AA leaderboard lists DeepSeek V4.1 Flash 1017 (Max) at 1746 Elo with confidence interval -21/+21. The page describes 220 GDPval tasks and a Stirrup shell/web agent loop. The table’s Oct 2026 release column is the model release month, not an evaluation date. The schema has no confidence-interval field, so the interval remains in this note.

最近核验时间：2026-11-04T02:16+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 61.26
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017)

已检查的主要资料：
- [Vals AI DeepSeek V4.1 Flash 1017 模型页](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals reports Accuracy 61.26% ±1.05 and rank 10/32 for this exact model. The current Index page identifies v2.2. The model profile lists DeepSeek, temperature 1, top_p 1, max output 384,000, and effort max, but Vals cautions that individual benchmark settings can differ; these are not asserted as the exact aggregate run configuration. The board update date is not an evaluation date. The schema has no uncertainty field, so ±1.05 remains in this note.

最近核验时间：2026-11-04T02:16+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis DeepSeek V4.1 Flash 1017 发布页",
          "url": "https://artificialanalysis.ai/models/releases/deepseek-v4-1-flash-1017"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis lists three distinct scores for this release on Intelligence Index v5.0: Max 32, High 29, and Non-reasoning 19. All three are preserved as separate records; the composite includes nine component evaluations, including HLE-Diamond rather than the original HLE. No evaluation date or harness was stated."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "DeepSeek 10 月 17 日发布公告",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库与指标说明",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "The exact 1017 model card and release announcement report 60.5 for Automation-Bench v1.0.6. The canonical task_completed_correctly metric comes from Zapier’s benchmark definition. The result source does not identify public versus held-out tasks, harness, or effort, so those conditions are omitted; the score is not assigned to either task set."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测仓库与 scorer",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "The official DeepSeek model card reports 83.0 for Chartography with tools for the exact 1017 checkpoint; the existing variant is retained. The benchmark’s official scorer supplies the canonical accuracy (mean; Pass@1) metric and its materials specify no semantic version. Surge’s separate V4.1 Flash (Max reasoning) listing is not the 1017 with-tools record and is not treated as a conflict."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "DeepSWE 官方榜单精确模型结果",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe?eval_result=deepseek-ai/DeepSeek-V4.1-Flash-1017&leaderboard_task_id=deep_swe"
        },
        {
          "label": "DeepSWE v1.1 方法页",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "The official model card and exact-model DeepSWE leaderboard entry both report 77.0 for the 1017 checkpoint. Existing record retains the model-card harness name Mini-SWE-V2; the leaderboard describes its general run stack as Pier/mini-swe-agent, so that wording difference is noted without replacing the source-specific field."
      ],
      "status": "已存在",
      "unresolved": [
        "DeepSeek calls the harness Mini-SWE-V2, while the leaderboard page describes Pier/mini-swe-agent generically; no source establishes whether those labels refer to the identical setup."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The official AA leaderboard lists DeepSeek V4.1 Flash 1017 (Max) at 1746 Elo with confidence interval -21/+21. The page describes 220 GDPval tasks and a Stirrup shell/web agent loop. The table’s Oct 2026 release column is the model release month, not an evaluation date. The schema has no confidence-interval field, so the interval remains in this note."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡及 HLE 条件说明",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "Scale AI Humanity’s Last Exam 官方页面",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "The official model card reports 42.6 without tools and 44.0 for the text-only subset, marked by a dagger; both corresponding local records are preserved. The local HLE definition identifies the original set as version unspecified and uses accuracy. The source does not report effort, harness, or an evaluation date."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "DeepSeek 10 月 17 日发布公告",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "OSWorld-V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Kimi K3.1 Pro 官方比较图及评测说明",
          "url": "https://www.kimi.com/en/blog/kimi-k3-1-pro"
        },
        {
          "label": "DataLearner OSWorld 2.1 二手榜单",
          "url": "https://www.datalearner.com/benchmarks/osworld-2-1"
        },
        {
          "label": "AIEvals DeepSeek V4.1 Flash 1017 二手模型页",
          "url": "https://aievals.app/models/deepseek-v4-1-flash-1017"
        }
      ],
      "notes": [
        "DeepSeek official card and release note do not list OSWorld. Kimi’s official comparison blog confirms an OSWorld V2.1 evaluation using the Kimi Agent harness and its chart includes DeepSeek V4.1 Flash 1017, but the chart value is not extractable from the text. Secondary tables report 69.3 as Partial score with Max + tools; this is not the local binary task completion rate and was not written to TOML."
      ],
      "status": "待核实",
      "unresolved": [
        "Need a directly verifiable primary-source score and confirmation of the exact metric/configuration. Do not treat the secondary 69.3 Partial score as binary task completion rate."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 Full 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        }
      ],
      "notes": [
        "Checked the Scale V2 Full public leaderboard and the official DeepSeek model card; neither contains a SWE-bench Pro V2 result for this exact model. The HARD tab is a separate dataset and no score was inferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方评测结果记录",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/discussions/40"
        },
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 方法页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "DeepSeek official evaluation results list 12.9 for Terminal-Bench-Science 0.1; the HF evaluation record associates the result with the (Max) model variant and Artificial Analysis. AA confirms 0.1.0, 70 tasks, mini-swe-agent, and pass@1 averaged over three repeats. The recorded metric follows the local task-resolution definition."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
        },
        {
          "label": "Harbor Terminal-Bench 4 官方精确结果",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=deepseek-ai/DeepSeek-V4.1-Flash-1017&leaderboard_task_id=terminalbench_4"
        },
        {
          "label": "Terminal-Bench 4.0 官方版本与协议",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The exact Harbor result and DeepSeek model card report 42.3 with Claude Code. The model card abbreviates the release as 4.0; Harbor identifies the dataset artifact as terminal-bench@4.0.0, matching the repository definition. The record version was aligned to that documented artifact version and the canonical task-resolution metric was added."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:16+08:00",
      "checked_sources": [
        {
          "label": "Vals AI DeepSeek V4.1 Flash 1017 模型页",
          "url": "https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017"
        },
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals reports Accuracy 61.26% ±1.05 and rank 10/32 for this exact model. The current Index page identifies v2.2. The model profile lists DeepSeek, temperature 1, top_p 1, max output 384,000, and effort max, but Vals cautions that individual benchmark settings can differ; these are not asserted as the exact aggregate run configuration. The board update date is not an evaluation date. The schema has no uncertainty field, so ±1.05 remains in this note."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:16+08:00",
  "model_id": "deepseek/deepseek-v4.1-flash-1017",
  "new_records": 6,
  "overall_status": "待复核"
}

-->
