# Step 3.5 Flash 2603 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：stepfun/step-3.5-flash-2603
- 模型名称：Step 3.5 Flash 2603
- 发布日期：2026-04-02
- 最近检查时间：2026-11-05T10:07+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：3
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- Exact local model identity: Step 3.5 Flash 2603, text input/output, tool and reasoning support. The local file contains three pre-existing results from a generic Step 3.5 Flash OpenRouter benchmark endpoint; they were preserved and not treated as exact 2603 results for this collection.
- Artificial Analysis reports 24% on its original Humanity’s Last Exam evaluation. Its methodology identifies 2,158 text-only questions from the May 2025 2,500-question set; the source does not publish an evaluation date, so no date was added.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | 2026-11-05T10:07+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Step 3.5 Flash official release notes](https://static.stepfun.com/blog/step-3.5-flash/), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro V2 release details](https://labs.scale.com/blog/swe-bench-pro-v2) | 2026-11-05T10:07+08:00 |
| terminal-bench-v4 | 待核实 | — | [Step 3.5 Flash official release notes](https://static.stepfun.com/blog/step-3-5-flash/), [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks) | 2026-11-05T10:07+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks), [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Step 3.5 Flash official release notes](https://static.stepfun.com/blog/step-3-5-flash/) | 2026-11-05T10:07+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench), [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | 2026-11-05T10:07+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | 2026-11-05T10:07+08:00 |
| chartography | 不适用 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | 2026-11-05T10:07+08:00 |
| humanitys-last-exam | 已收录 | 24% (metric=accuracy; dataset=2,158 text-only questions from the original HLE dataset (Artificial Analysis evaluation); variant=pass@1; GPT-5.6 Luna (medium) equality checker) | [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:07+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Step 3.5 Flash 2603 profile](https://artificialanalysis.ai/models/step-3-5-flash), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:07+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash), [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:07+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index), [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | 2026-11-05T10:07+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash)

研究备注：
- The live leaderboard and its published JSON did not provide a directly verified row for the exact 2603 snapshot; visible coverage is incomplete.

尚未解决的问题：
- No exact DeepSWE v1.1 score for Step 3.5 Flash 2603 was verified.

最近核验时间：2026-11-05T10:07+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Step 3.5 Flash official release notes](https://static.stepfun.com/blog/step-3.5-flash/)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro V2 release details](https://labs.scale.com/blog/swe-bench-pro-v2)

研究备注：
- Step material reports a SWE-bench Pro result without identifying it as the 642-task V2 configuration or tying it to the exact 2603 snapshot.

尚未解决的问题：
- No exact SWE-bench Pro V2 result for this snapshot was verified.

最近核验时间：2026-11-05T10:07+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Step 3.5 Flash official release notes](https://static.stepfun.com/blog/step-3-5-flash/)
- [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks)

研究备注：
- Step materials list Terminal-Bench 2.0 and 2.1 results; those do not establish a Terminal-Bench 4.0 score for the exact 2603 snapshot.

尚未解决的问题：
- No exact Terminal-Bench 4.0 result was verified.

最近核验时间：2026-11-05T10:07+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks)
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Step 3.5 Flash official release notes](https://static.stepfun.com/blog/step-3-5-flash/)

研究备注：
- The public leaderboard view did not expose a directly verifiable result for this exact model snapshot.

尚未解决的问题：
- No exact Terminal-Bench-Science 0.1.0 result was verified.

最近核验时间：2026-11-05T10:07+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash)

研究备注：
- The model supports tool use and is applicable. The official leaderboard folds 119 entries, so the visible list cannot establish absence of an exact result.

尚未解决的问题：
- No exact AutomationBench v1.0.6 score or configuration was verified.

最近核验时间：2026-11-05T10:07+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash)

研究备注：
- The model accepts text only and cannot consume the screenshot/image input required for standard OSWorld computer-use tasks.

最近核验时间：2026-11-05T10:07+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash)

研究备注：
- Chartography requires visual chart input; this text-only model cannot receive chart images.

最近核验时间：2026-11-05T10:07+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 24%
- metric: accuracy
- dataset: 2,158 text-only questions from the original HLE dataset (Artificial Analysis evaluation)
- variant: pass@1; GPT-5.6 Luna (medium) equality checker
- source: [https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The direct comparison gives 24% for Step 3.5 Flash 2603. Artificial Analysis documents its original HLE subset as 2,158 text-only questions and distinguishes it from HLE-Diamond. The source does not publish an evaluation date.

最近核验时间：2026-11-05T10:07+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Step 3.5 Flash 2603 profile](https://artificialanalysis.ai/models/step-3-5-flash)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The exact model profile currently reports Index N/A. A 17* estimate visible on an older comparison is explicitly part of v4.3.2 and cannot be transferred to V5.0.1.

最近核验时间：2026-11-05T10:07+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash)
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The exact comparison page has no GDPval-AA v2.1 value for this model; no score was inferred from the blank cell.

最近核验时间：2026-11-05T10:07+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)
- [Step 3.5 Flash official model card](https://huggingface.co/stepfun-ai/Step-3.5-Flash)

研究备注：
- The current V2.2 leaderboard shows Step 5 Preview as the best StepFun model and states that it shows the best model from each lab; absence of Step 3.5 Flash 2603 is not proof it was never measured.

尚未解决的问题：
- No exact Vals Index v2.2 score for Step 3.5 Flash 2603 was verified.

最近核验时间：2026-11-05T10:07+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Step 3.5 Flash 2603 profile",
          "url": "https://artificialanalysis.ai/models/step-3-5-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The exact model profile currently reports Index N/A. A 17* estimate visible on an older comparison is explicitly part of v4.3.2 and cannot be transferred to V5.0.1."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Step 3.5 Flash official model card",
          "url": "https://huggingface.co/stepfun-ai/Step-3.5-Flash"
        }
      ],
      "notes": [
        "The model supports tool use and is applicable. The official leaderboard folds 119 entries, so the visible list cannot establish absence of an exact result."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact AutomationBench v1.0.6 score or configuration was verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography public leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Step 3.5 Flash official model card",
          "url": "https://huggingface.co/stepfun-ai/Step-3.5-Flash"
        }
      ],
      "notes": [
        "Chartography requires visual chart input; this text-only model cannot receive chart images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard data",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "Step 3.5 Flash official model card",
          "url": "https://huggingface.co/stepfun-ai/Step-3.5-Flash"
        }
      ],
      "notes": [
        "The live leaderboard and its published JSON did not provide a directly verified row for the exact 2603 snapshot; visible coverage is incomplete."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 score for Step 3.5 Flash 2603 was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The exact comparison page has no GDPval-AA v2.1 value for this model; no score was inferred from the blank cell."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-step-3-5-flash"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The direct comparison gives 24% for Step 3.5 Flash 2603. Artificial Analysis documents its original HLE subset as 2,158 text-only questions and distinguishes it from HLE-Diamond. The source does not publish an evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Step 3.5 Flash official model card",
          "url": "https://huggingface.co/stepfun-ai/Step-3.5-Flash"
        }
      ],
      "notes": [
        "The model accepts text only and cannot consume the screenshot/image input required for standard OSWorld computer-use tasks."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Step 3.5 Flash official release notes",
          "url": "https://static.stepfun.com/blog/step-3.5-flash/"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro V2 release details",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        }
      ],
      "notes": [
        "Step material reports a SWE-bench Pro result without identifying it as the 642-task V2 configuration or tying it to the exact 2603 snapshot."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 result for this snapshot was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Snorkel Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "label": "Step 3.5 Flash official release notes",
          "url": "https://static.stepfun.com/blog/step-3-5-flash/"
        }
      ],
      "notes": [
        "The public leaderboard view did not expose a directly verifiable result for this exact model snapshot."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench-Science 0.1.0 result was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Step 3.5 Flash official release notes",
          "url": "https://static.stepfun.com/blog/step-3-5-flash/"
        },
        {
          "label": "Terminal-Bench official versions and leaderboard",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "Step materials list Terminal-Bench 2.0 and 2.1 results; those do not establish a Terminal-Bench 4.0 score for the exact 2603 snapshot."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench 4.0 result was verified."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T10:07+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Step 3.5 Flash official model card",
          "url": "https://huggingface.co/stepfun-ai/Step-3.5-Flash"
        }
      ],
      "notes": [
        "The current V2.2 leaderboard shows Step 5 Preview as the best StepFun model and states that it shows the best model from each lab; absence of Step 3.5 Flash 2603 is not proof it was never measured."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Vals Index v2.2 score for Step 3.5 Flash 2603 was verified."
      ]
    }
  },
  "existing_records": 3,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:07+08:00",
  "model_id": "stepfun/step-3.5-flash-2603",
  "model_notes": [
    "Exact local model identity: Step 3.5 Flash 2603, text input/output, tool and reasoning support. The local file contains three pre-existing results from a generic Step 3.5 Flash OpenRouter benchmark endpoint; they were preserved and not treated as exact 2603 results for this collection.",
    "Artificial Analysis reports 24% on its original Humanity’s Last Exam evaluation. Its methodology identifies 2,158 text-only questions from the May 2025 2,500-question set; the source does not publish an evaluation date, so no date was added."
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
