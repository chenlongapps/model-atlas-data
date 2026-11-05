# Gemini 4 Argon Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-4-argon
- 模型名称：Gemini 4 Argon
- 发布日期：2026-10-13
- 最近检查时间：2026-11-04T02:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：13
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：12

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 77.9 (metric=pass@1; version=1.1; dataset=DeepSWE v1.1 (113 tasks); effort=high; harness=mini-swe-agent) | [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/), [Google evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon) | 2026-11-04T02:58+08:00 |
| swe-bench-pro-v2 | 已收录 | 99.22 (metric=task resolution rate; version=2.0.0; dataset=SWE-bench Pro V2 Full (642 tasks); reported 99.22 ± 0.45%; effort=high; variant=Full; harness=mini-swe-agent) | [Scale AI SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:58+08:00 |
| terminal-bench-v4 | 已收录 | 57.58 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (66 tasks); reported ±2.31 percentage points; effort=high; variant=avg@3; each run pass@1; harness=Mini-SWE-agent); 57.4 (metric=task resolution rate; version=4.0.0; effort=high; variant=Google self-computed; pass@1; repeat count and harness not specified) | [Vals Terminal-Bench 4 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/), [Vals Gemini 4 Argon profile](https://www.vals.ai/models/google_gemini-4-argon) | 2026-11-04T02:58+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 57.6 (metric=task resolution rate; version=0.1.0; effort=high; variant=Google self-computed; pass@1; verifier timeout set to 6×; harness not specified); 53 (metric=task resolution rate; version=0.1.0; dataset=Terminal-Bench-Science v0.1.0 (70 tasks); effort=high; variant=pass@1 averaged over 3 repeats; harness=mini-swe-agent); 44.29 (metric=task resolution rate; version=0.1.0; dataset=Terminal-Bench-Science v0.1.0 (70 tasks); reported ±5.98 percentage points; effort=high; variant=single pass@1 run; infrastructure or provider errors may be retried; harness=Mini-SWE-agent) | [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/), [Artificial Analysis Terminal-Bench-Science comparison](https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-astra-high), [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T02:58+08:00 |
| automationbench-v1.0.6 | 已收录 | 51.29 (metric=task_completed_correctly; version=1.0.6; dataset=Zapier 1.0.6 held-out private task set (600+ tasks; 47 apps); effort=High; harness=Zapier AutomationBench); 50.08 (metric=task_completed_correctly; version=1.0.6; dataset=Zapier 1.0.6 held-out private task set (600+ tasks; 47 apps); effort=Medium; harness=Zapier AutomationBench) | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T02:58+08:00 |
| osworld-v2.1 | 待核实 | — | [Google Gemini performance table](https://deepmind.google/models/gemini/), [Google Gemini 4 Argon evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-carbon), [OSWorld V2 definition](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T02:58+08:00 |
| chartography | 已收录 | 71.6 (metric=accuracy (mean; Pass@1); version=unspecified; effort=High reasoning; variant=without tools) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Google Gemini 4 Argon evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon) | 2026-11-04T02:58+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale AI Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Scale AI Humanity’s Last Exam text-only leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam_text_only), [Humanity’s Last Exam official site](https://lastexam.ai/), [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/) | 2026-11-04T02:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 50 (metric=index score; version=5.0; dataset=Artificial Analysis Intelligence Index V5 composite (9 evaluations); effort=high) | [Artificial Analysis Gemini 4 Argon model page](https://artificialanalysis.ai/models/gemini-4-argon), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T02:58+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA evaluation page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/) | 2026-11-04T02:58+08:00 |
| vals-index-v2.2 | 已收录 | 69.24 (metric=performance score; version=2.2; dataset=Vals Index composite (finance, coding, legal, tax); effort=high) | [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Gemini 4 Argon model profile](https://www.vals.ai/models/google_gemini-4-argon) | 2026-11-04T02:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 已确认成绩 1

- name: DeepSWE
- score: 77.9
- metric: pass@1
- version: 1.1
- dataset: DeepSWE v1.1 (113 tasks)
- effort: high
- harness: mini-swe-agent
- source: [https://deepmind.google/models/model-cards/gemini-4-argon/](https://deepmind.google/models/model-cards/gemini-4-argon/)

已检查的主要资料：
- [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/)
- [Google evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon)

研究备注：
- Google reports 77.9% on DeepSWE v1.1; methodology describes self-computation with mini-swe-agent, pass@1 and highest thinking settings.

最近核验时间：2026-11-04T02:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 已确认成绩 1

- name: SWE-bench Pro
- score: 99.22
- metric: task resolution rate
- version: 2.0.0
- dataset: SWE-bench Pro V2 Full (642 tasks); reported 99.22 ± 0.45%
- effort: high
- variant: Full
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Recorded V2 Full (642 tasks), high effort and mini-swe-agent; retained the reported ±0.45 uncertainty in dataset text.

最近核验时间：2026-11-04T02:58+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 57.58
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (66 tasks); reported ±2.31 percentage points
- effort: high
- variant: avg@3; each run pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)

#### 已确认成绩 2

- name: Terminal-Bench
- score: 57.4
- metric: task resolution rate
- version: 4.0.0
- effort: high
- variant: Google self-computed; pass@1; repeat count and harness not specified
- source: [https://deepmind.google/models/model-cards/gemini-4-argon/](https://deepmind.google/models/model-cards/gemini-4-argon/)

已检查的主要资料：
- [Vals Terminal-Bench 4 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/)
- [Vals Gemini 4 Argon profile](https://www.vals.ai/models/google_gemini-4-argon)

研究备注：
- Kept the Vals avg@3 result and Google self-computed pass@1 result separate because harness/repetition conditions differ or are unspecified.

最近核验时间：2026-11-04T02:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 57.6
- metric: task resolution rate
- version: 0.1.0
- effort: high
- variant: Google self-computed; pass@1; verifier timeout set to 6×; harness not specified
- source: [https://deepmind.google/models/model-cards/gemini-4-argon/](https://deepmind.google/models/model-cards/gemini-4-argon/)

#### 已确认成绩 2

- name: Terminal-Bench-Science
- score: 53
- metric: task resolution rate
- version: 0.1.0
- dataset: Terminal-Bench-Science v0.1.0 (70 tasks)
- effort: high
- variant: pass@1 averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-astra-high](https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-astra-high)

#### 已确认成绩 3

- name: Terminal-Bench-Science
- score: 44.29
- metric: task resolution rate
- version: 0.1.0
- dataset: Terminal-Bench-Science v0.1.0 (70 tasks); reported ±5.98 percentage points
- effort: high
- variant: single pass@1 run; infrastructure or provider errors may be retried
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)

已检查的主要资料：
- [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/)
- [Artificial Analysis Terminal-Bench-Science comparison](https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-astra-high)
- [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Stored three source-reported configurations separately: Google self-computed pass@1 with 6× verifier timeout, Artificial Analysis pass@1 averaged over 3 repeats, and Vals single pass@1 run.

最近核验时间：2026-11-04T02:58+08:00

### AutomationBench (automationbench-v1.0.6)

#### 已确认成绩 1

- name: AutomationBench
- score: 51.29
- metric: task_completed_correctly
- version: 1.0.6
- dataset: Zapier 1.0.6 held-out private task set (600+ tasks; 47 apps)
- effort: High
- harness: Zapier AutomationBench
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

#### 已确认成绩 2

- name: AutomationBench
- score: 50.08
- metric: task_completed_correctly
- version: 1.0.6
- dataset: Zapier 1.0.6 held-out private task set (600+ tasks; 47 apps)
- effort: Medium
- harness: Zapier AutomationBench
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- Recorded official high and medium effort rows separately from the held-out private task set.

最近核验时间：2026-11-04T02:58+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini performance table](https://deepmind.google/models/gemini/)
- [Google Gemini 4 Argon evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-carbon)
- [OSWorld V2 definition](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- Google reports the Argon OSWorld-2.1 offline-subset partial score and maximum across three single-attempt runs. The source result is preserved with metric "partial score".

尚未解决的问题：
- The repository definition tracks binary task completion rate; the reported partial score is a different metric and cannot be mapped without conflation.

最近核验时间：2026-11-04T02:58+08:00

### Chartography (chartography)

#### 已确认成绩 1

- name: Chartography
- score: 71.6
- metric: accuracy (mean; Pass@1)
- version: unspecified
- effort: High reasoning
- variant: without tools
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Google Gemini 4 Argon evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon)

研究备注：
- The official leaderboard reports 71.6% for Gemini 4 Argon High reasoning; Google methodology says the result is without tools. No source-stated semantic benchmark version or evaluation date was found.

最近核验时间：2026-11-04T02:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Scale AI Humanity’s Last Exam text-only leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam_text_only)
- [Humanity’s Last Exam official site](https://lastexam.ai/)
- [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/)

研究备注：
- Checked the original HLE leaderboard, its text-only leaderboard, the official HLE site, and Google’s model card/methodology. No exact Argon result was listed.

最近核验时间：2026-11-04T02:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 50
- metric: index score
- version: 5.0
- dataset: Artificial Analysis Intelligence Index V5 composite (9 evaluations)
- effort: high
- source: [https://artificialanalysis.ai/models/gemini-4-argon](https://artificialanalysis.ai/models/gemini-4-argon)

已检查的主要资料：
- [Artificial Analysis Gemini 4 Argon model page](https://artificialanalysis.ai/models/gemini-4-argon)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current model page reports V5.0 score 50 for Gemini 4 Argon (High); did not substitute the older Index version.

最近核验时间：2026-11-04T02:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Google Gemini 4 Argon model card](https://deepmind.google/models/model-cards/gemini-4-argon/)

研究备注：
- The current public evaluation table view did not expose a Gemini 4 Argon row; no score was copied from uncorroborated cached search text.

尚未解决的问题：
- Could not verify whether a result exists outside the currently visible public table; no score recorded.

最近核验时间：2026-11-04T02:58+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 69.24
- metric: performance score
- version: 2.2
- dataset: Vals Index composite (finance, coding, legal, tax)
- effort: high
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Gemini 4 Argon model profile](https://www.vals.ai/models/google_gemini-4-argon)

研究备注：
- Recorded the exact V2.2 row score 69.24; excluded a prior-version snapshot and did not treat leaderboard update time as evaluation date.

最近核验时间：2026-11-04T02:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 4 Argon model page",
          "url": "https://artificialanalysis.ai/models/gemini-4-argon"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current model page reports V5.0 score 50 for Gemini 4 Argon (High); did not substitute the older Index version."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Recorded official high and medium effort rows separately from the held-out private task set."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Google Gemini 4 Argon evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-4-argon"
        }
      ],
      "notes": [
        "The official leaderboard reports 71.6% for Gemini 4 Argon High reasoning; Google methodology says the result is without tools. No source-stated semantic benchmark version or evaluation date was found."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 4 Argon model card",
          "url": "https://deepmind.google/models/model-cards/gemini-4-argon/"
        },
        {
          "label": "Google evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-4-argon"
        }
      ],
      "notes": [
        "Google reports 77.9% on DeepSWE v1.1; methodology describes self-computation with mini-swe-agent, pass@1 and highest thinking settings."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Google Gemini 4 Argon model card",
          "url": "https://deepmind.google/models/model-cards/gemini-4-argon/"
        }
      ],
      "notes": [
        "The current public evaluation table view did not expose a Gemini 4 Argon row; no score was copied from uncorroborated cached search text."
      ],
      "status": "待核实",
      "unresolved": [
        "Could not verify whether a result exists outside the currently visible public table; no score recorded."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Scale AI Humanity’s Last Exam leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Scale AI Humanity’s Last Exam text-only leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam_text_only"
        },
        {
          "label": "Humanity’s Last Exam official site",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "Google Gemini 4 Argon model card",
          "url": "https://deepmind.google/models/model-cards/gemini-4-argon/"
        }
      ],
      "notes": [
        "Checked the original HLE leaderboard, its text-only leaderboard, the official HLE site, and Google’s model card/methodology. No exact Argon result was listed."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini performance table",
          "url": "https://deepmind.google/models/gemini/"
        },
        {
          "label": "Google Gemini 4 Argon evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-4-carbon"
        },
        {
          "label": "OSWorld V2 definition",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "Google reports the Argon OSWorld-2.1 offline-subset partial score and maximum across three single-attempt runs. The source result is preserved with metric \"partial score\"."
      ],
      "status": "待核实",
      "unresolved": [
        "The repository definition tracks binary task completion rate; the reported partial score is a different metric and cannot be mapped without conflation."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Recorded V2 Full (642 tasks), high effort and mini-swe-agent; retained the reported ±0.45 uncertainty in dataset text."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 4 Argon model card",
          "url": "https://deepmind.google/models/model-cards/gemini-4-argon/"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-astra-high"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Stored three source-reported configurations separately: Google self-computed pass@1 with 6× verifier timeout, Artificial Analysis pass@1 averaged over 3 repeats, and Vals single pass@1 run."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Google Gemini 4 Argon model card",
          "url": "https://deepmind.google/models/model-cards/gemini-4-argon/"
        },
        {
          "label": "Vals Gemini 4 Argon profile",
          "url": "https://www.vals.ai/models/google_gemini-4-argon"
        }
      ],
      "notes": [
        "Kept the Vals avg@3 result and Google self-computed pass@1 result separate because harness/repetition conditions differ or are unspecified."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Gemini 4 Argon model profile",
          "url": "https://www.vals.ai/models/google_gemini-4-argon"
        }
      ],
      "notes": [
        "Recorded the exact V2.2 row score 69.24; excluded a prior-version snapshot and did not treat leaderboard update time as evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:58+08:00",
  "model_id": "google/gemini-4-argon",
  "new_records": 13,
  "overall_status": "待复核"
}

-->
