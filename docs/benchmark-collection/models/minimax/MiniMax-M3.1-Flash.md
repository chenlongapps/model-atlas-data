# MiniMax-M3.1-Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：minimax/MiniMax-M3.1-Flash
- 模型名称：MiniMax-M3.1-Flash
- 发布日期：2026-10-19
- 最近检查时间：2026-11-04T02:10+08:00
- 整体处理状态：待复核
- 新增成绩数量：8
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：8

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 73.7 (metric=pass@1; version=1.1; dataset=v1.1 (113 tasks); variant=512K context; harness=mini-SWE-agent 2.4.5) | [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash), [DeepSWE v1.1 官方榜单](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=MiniMaxAI/MiniMax-M3.1-Flash&leaderboard_task_id=deep_swe) | 2026-11-04T02:10+08:00 |
| swe-bench-pro-v2 | 已收录 | 96.57 (metric=task resolution rate; version=2.0.0; dataset=Full public V2 split (642 tasks); effort=xhigh; variant=Scale leaderboard alias: Minimax M3p1 Flash; reported ±1.16; harness=mini-swe-agent) | [Scale AI SWE-bench Pro V2 Full 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:10+08:00 |
| terminal-bench-v4 | 已收录 | 38.1 (metric=task resolution rate; version=4.0.0; dataset=terminal-bench/terminal-bench@4.0.0 (66 tasks); harness=Codex 0.149.1) | [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash), [Harbor Terminal-Bench 4 官方结果](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=MiniMaxAI/MiniMax-M3.1-Flash&leaderboard_task_id=terminalbench_4) | 2026-11-04T02:10+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 3.3 (metric=task resolution rate; version=0.1.0; dataset=harborframework/terminal-bench-science; terminalbenchscience_0_1 (70 tasks); variant=pass@1 averaged over three repeats; harness=mini-swe-agent) | [模型卡精确评测记录](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/blob/main/.eval_results/terminal-bench-science.yaml), [Artificial Analysis Terminal-Bench Science 方法页](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T02:10+08:00 |
| automationbench-v1.0.6 | 已收录 | 62.8 (metric=task_completed_correctly; version=1.0.6; dataset=600 publicly released tasks) | [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash), [Zapier AutomationBench 官方仓库与指标说明](https://github.com/zapier/AutomationBench) | 2026-11-04T02:10+08:00 |
| osworld-v2.1 | 未找到 | — | [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash), [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T02:10+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测仓库](https://github.com/surge-ai/chartography), [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | 2026-11-04T02:10+08:00 |
| humanitys-last-exam | 已收录 | 43.4 (metric=accuracy; version=unspecified; dataset=Text-only subset (2,158 questions); variant=without tools) | [MiniMax 官方模型卡及 HLE 评测注释](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash), [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T02:10+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 29 (metric=index score; version=5.0) | [Artificial Analysis MiniMax-M3.1-Flash 模型页](https://artificialanalysis.ai/models/minimax-m3-1-flash), [Artificial Analysis Intelligence Index V5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T02:10+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 当前评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis MiniMax 与 Step 5 比较页](https://artificialanalysis.ai/models/comparisons/minimax-m3-1-flash-vs-step-5), [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | 2026-11-04T02:10+08:00 |
| vals-index-v2.2 | 已收录 | 53.78 (metric=performance score; version=2.2; effort=max; variant=Official MiniMax API; temperature=1; top_p=0.95; max output=262,144 tokens) | [Vals AI MiniMax-M3.1-Flash 模型页](https://www.vals.ai/models/minimax_MiniMax-M3.1-flash), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T02:10+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 已确认成绩 1

- name: DeepSWE
- score: 73.7
- metric: pass@1
- version: 1.1
- dataset: v1.1 (113 tasks)
- variant: 512K context
- harness: mini-SWE-agent 2.4.5
- source: [https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

已检查的主要资料：
- [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- [DeepSWE v1.1 官方榜单](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=MiniMaxAI/MiniMax-M3.1-Flash&leaderboard_task_id=deep_swe)

研究备注：
- 73.7 is explicitly for the official MiniMax-M3.1-Flash checkpoint; the card specifies mini-SWE-agent 2.4.5 and 512K context. The leaderboard shows DeepSWE v1.1 with 113 tasks.

最近核验时间：2026-11-04T02:10+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 已确认成绩 1

- name: SWE-bench Pro
- score: 96.57
- metric: task resolution rate
- version: 2.0.0
- dataset: Full public V2 split (642 tasks)
- effort: xhigh
- variant: Scale leaderboard alias: Minimax M3p1 Flash; reported ±1.16
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 Full 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Scale Full board lists “Minimax M3p1 Flash (mini-swe-agent) xhigh” at 96.57±1.16 on the V2 full public split of 642 tasks. The board alias is retained in variant; the separate HARD tab score is excluded.

最近核验时间：2026-11-04T02:10+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 38.1
- metric: task resolution rate
- version: 4.0.0
- dataset: terminal-bench/terminal-bench@4.0.0 (66 tasks)
- harness: Codex 0.149.1
- source: [https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

已检查的主要资料：
- [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- [Harbor Terminal-Bench 4 官方结果](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=MiniMaxAI/MiniMax-M3.1-Flash&leaderboard_task_id=terminalbench_4)

研究备注：
- The Harbor result is keyed to MiniMaxAI/MiniMax-M3.1-Flash and reports 38.1; the model card specifies Codex 0.149.1. The result set contains 66 tasks.

最近核验时间：2026-11-04T02:10+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 3.3
- metric: task resolution rate
- version: 0.1.0
- dataset: harborframework/terminal-bench-science; terminalbenchscience_0_1 (70 tasks)
- variant: pass@1 averaged over three repeats
- harness: mini-swe-agent
- source: [https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/blob/main/.eval_results/terminal-bench-science.yaml](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/blob/main/.eval_results/terminal-bench-science.yaml)

已检查的主要资料：
- [模型卡精确评测记录](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/blob/main/.eval_results/terminal-bench-science.yaml)
- [Artificial Analysis Terminal-Bench Science 方法页](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- The model card sidecar records 3.3 for task_id terminalbenchscience_0_1 and attributes the evaluation to Artificial Analysis. AA documents mini-swe-agent, pass@1 averaged over three repeats, and 70 tasks.

最近核验时间：2026-11-04T02:10+08:00

### AutomationBench (automationbench-v1.0.6)

#### 已确认成绩 1

- name: AutomationBench
- score: 62.8
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 600 publicly released tasks
- source: [https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

已检查的主要资料：
- [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- [Zapier AutomationBench 官方仓库与指标说明](https://github.com/zapier/AutomationBench)

研究备注：
- The official model card reports 62.8 for Automation-Bench v1.0.6 on 600 publicly released tasks. This public set is distinct from Zapier’s private held-out official leaderboard; no harness or evaluation date was stated.

最近核验时间：2026-11-04T02:10+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- [OSWorld-V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- The model card reports 61.7 for OSWorld 2.0 (0808 Full release), not the separately defined OSWorld v2.1; that 2.0 result was not transferred. No exact v2.1 score was found in the checked model card or official project materials.

最近核验时间：2026-11-04T02:10+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测仓库](https://github.com/surge-ai/chartography)
- [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

研究备注：
- The model supports image input and text output, so the benchmark is applicable. The official Surge leaderboard and repository showed no MiniMax-M3.1-Flash result; CharXiv RQ 82.5 is a different benchmark.

最近核验时间：2026-11-04T02:10+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 已确认成绩 1

- name: Humanity's Last Exam
- score: 43.4
- metric: accuracy
- version: unspecified
- dataset: Text-only subset (2,158 questions)
- variant: without tools
- source: [https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

已检查的主要资料：
- [MiniMax 官方模型卡及 HLE 评测注释](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- The official model card reports 43.4 for HLE without tools on a text-only subset of 2,158 questions. It is retained as a dataset variant of original HLE; HLE-Diamond and other subsets are not substituted.

最近核验时间：2026-11-04T02:10+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 29
- metric: index score
- version: 5.0
- source: [https://artificialanalysis.ai/models/minimax-m3-1-flash](https://artificialanalysis.ai/models/minimax-m3-1-flash)

已检查的主要资料：
- [Artificial Analysis MiniMax-M3.1-Flash 模型页](https://artificialanalysis.ai/models/minimax-m3-1-flash)
- [Artificial Analysis Intelligence Index V5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The current Artificial Analysis model page identifies MiniMax-M3.1-Flash and score 29 on the current Intelligence Index; the current index definition is v5.0. Older v4.x values were excluded.

最近核验时间：2026-11-04T02:10+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 当前评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis MiniMax 与 Step 5 比较页](https://artificialanalysis.ai/models/comparisons/minimax-m3-1-flash-vs-step-5)
- [MiniMax 官方模型卡](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

研究备注：
- The current official GDPval-AA v2.1 page was checked but did not expose a verifiable row for this exact model. A 1466 Elo candidate seen in an older comparison-page snapshot could not be confirmed on the current page. The model card’s GDP.pdf AA 20.8 is a different evaluation.

尚未解决的问题：
- Recheck if the current official AA leaderboard exposes a MiniMax-M3.1-Flash row or a stable, directly viewable result; do not use the stale 1466 candidate without primary-source confirmation.

最近核验时间：2026-11-04T02:10+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 53.78
- metric: performance score
- version: 2.2
- effort: max
- variant: Official MiniMax API; temperature=1; top_p=0.95; max output=262,144 tokens
- source: [https://www.vals.ai/models/minimax_MiniMax-M3.1-flash](https://www.vals.ai/models/minimax_MiniMax-M3.1-flash)
- date: 2026-10-20

已检查的主要资料：
- [Vals AI MiniMax-M3.1-Flash 模型页](https://www.vals.ai/models/minimax_MiniMax-M3.1-flash)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals reports 53.78% ±1.07 for Vals Index v2.2, and the Oct 20, 2026 update explicitly says this model was evaluated on that index. The evaluation update gives max output 262k, while the current generic settings panel says 524,288; the documented evaluation-specific 262,144 is retained. ±1.07 is preserved in this note because the benchmark schema has no uncertainty field.

最近核验时间：2026-11-04T02:10+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniMax-M3.1-Flash 模型页",
          "url": "https://artificialanalysis.ai/models/minimax-m3-1-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The current Artificial Analysis model page identifies MiniMax-M3.1-Flash and score 29 on the current Intelligence Index; the current index definition is v5.0. Older v4.x values were excluded."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "MiniMax 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        },
        {
          "label": "Zapier AutomationBench 官方仓库与指标说明",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "The official model card reports 62.8 for Automation-Bench v1.0.6 on 600 publicly released tasks. This public set is distinct from Zapier’s private held-out official leaderboard; no harness or evaluation date was stated."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测仓库",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "MiniMax 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        }
      ],
      "notes": [
        "The model supports image input and text output, so the benchmark is applicable. The official Surge leaderboard and repository showed no MiniMax-M3.1-Flash result; CharXiv RQ 82.5 is a different benchmark."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "MiniMax 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        },
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe?eval_result=MiniMaxAI/MiniMax-M3.1-Flash&leaderboard_task_id=deep_swe"
        }
      ],
      "notes": [
        "73.7 is explicitly for the official MiniMax-M3.1-Flash checkpoint; the card specifies mini-SWE-agent 2.4.5 and 512K context. The leaderboard shows DeepSWE v1.1 with 113 tasks."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 当前评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis MiniMax 与 Step 5 比较页",
          "url": "https://artificialanalysis.ai/models/comparisons/minimax-m3-1-flash-vs-step-5"
        },
        {
          "label": "MiniMax 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        }
      ],
      "notes": [
        "The current official GDPval-AA v2.1 page was checked but did not expose a verifiable row for this exact model. A 1466 Elo candidate seen in an older comparison-page snapshot could not be confirmed on the current page. The model card’s GDP.pdf AA 20.8 is a different evaluation."
      ],
      "status": "待核实",
      "unresolved": [
        "Recheck if the current official AA leaderboard exposes a MiniMax-M3.1-Flash row or a stable, directly viewable result; do not use the stale 1466 candidate without primary-source confirmation."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "MiniMax 官方模型卡及 HLE 评测注释",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        },
        {
          "label": "Scale AI Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "The official model card reports 43.4 for HLE without tools on a text-only subset of 2,158 questions. It is retained as a dataset variant of original HLE; HLE-Diamond and other subsets are not substituted."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "MiniMax 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        },
        {
          "label": "OSWorld-V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "The model card reports 61.7 for OSWorld 2.0 (0808 Full release), not the separately defined OSWorld v2.1; that 2.0 result was not transferred. No exact v2.1 score was found in the checked model card or official project materials."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 Full 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Scale Full board lists “Minimax M3p1 Flash (mini-swe-agent) xhigh” at 96.57±1.16 on the V2 full public split of 642 tasks. The board alias is retained in variant; the separate HARD tab score is excluded."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "模型卡精确评测记录",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/blob/main/.eval_results/terminal-bench-science.yaml"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 方法页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "The model card sidecar records 3.3 for task_id terminalbenchscience_0_1 and attributes the evaluation to Artificial Analysis. AA documents mini-swe-agent, pass@1 averaged over three repeats, and 70 tasks."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "MiniMax 官方模型卡",
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash"
        },
        {
          "label": "Harbor Terminal-Bench 4 官方结果",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=MiniMaxAI/MiniMax-M3.1-Flash&leaderboard_task_id=terminalbench_4"
        }
      ],
      "notes": [
        "The Harbor result is keyed to MiniMaxAI/MiniMax-M3.1-Flash and reports 38.1; the model card specifies Codex 0.149.1. The result set contains 66 tasks."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:10+08:00",
      "checked_sources": [
        {
          "label": "Vals AI MiniMax-M3.1-Flash 模型页",
          "url": "https://www.vals.ai/models/minimax_MiniMax-M3.1-flash"
        },
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals reports 53.78% ±1.07 for Vals Index v2.2, and the Oct 20, 2026 update explicitly says this model was evaluated on that index. The evaluation update gives max output 262k, while the current generic settings panel says 524,288; the documented evaluation-specific 262,144 is retained. ±1.07 is preserved in this note because the benchmark schema has no uncertainty field."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:10+08:00",
  "model_id": "minimax/MiniMax-M3.1-Flash",
  "new_records": 8,
  "overall_status": "待复核"
}

-->
