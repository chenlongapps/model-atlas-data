# Mercury Edit 2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inception/mercury-edit-2
- 模型名称：Mercury Edit 2
- 发布日期：2026-03-30
- 最近检查时间：2026-11-05T10:33+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Inception’s model directory identifies mercury-edit-2 as a text-only FIM/NextEdit model for code completion and next-edit suggestions; the official table does not list tool calling.
- The release post describes four different code-editing evaluations (Instinct, FIM, NEP, and an internal next-edit benchmark); none is mapped to the 11 repository targets.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2) | 2026-11-05 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2) | 2026-11-05 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench official leaderboard](https://www.tbench.ai/), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks), [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2) | 2026-11-05 |
| terminal-bench-science-v0.1 | 待核实 | — | [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Terminal-Bench official versions](https://www.tbench.ai/benchmarks), [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2) | 2026-11-05 |
| automationbench-v1.0.6 | 不适用 | — | [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05 |
| osworld-v2.1 | 不适用 | — | [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [OSWorld-V2 project](https://osworld-v2.xlang.ai/) | 2026-11-05 |
| chartography | 不适用 | — | [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05 |
| humanitys-last-exam | 不适用 | — | [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05 |
| gdpval-aa-v2.1 | 不适用 | — | [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2), [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05 |
| vals-index-v2.2 | 不适用 | — | [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2)

研究备注：
- The model generates code edits, so this coding benchmark is applicable. No exact Mercury Edit 2 result was verified; the visible DeepSWE model list is incomplete.

尚未解决的问题：
- No exact DeepSWE v1.1 score was verified.

最近核验时间：2026-11-05

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2)

研究备注：
- The model can generate code edits, but the official model directory and release post do not report SWE-bench Pro V2; no exact leaderboard score was verified.

尚未解决的问题：
- No exact SWE-bench Pro V2 score was verified.

最近核验时间：2026-11-05

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench official leaderboard](https://www.tbench.ai/)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2)

研究备注：
- The official leaderboard view did not expose a verifiable row for this model; the release post reports other coding benchmarks.

尚未解决的问题：
- No exact Terminal-Bench 4.0 score was verified.

最近核验时间：2026-11-05

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Terminal-Bench official versions](https://www.tbench.ai/benchmarks)
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2)

研究备注：
- The public leaderboard view did not expose an exact Mercury Edit 2 result; the model can generate code edits, so it is not marked not-applicable.

尚未解决的问题：
- No exact Terminal-Bench Science 0.1.0 score was verified.

最近核验时间：2026-11-05

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- The model directory exposes only FIM and NextEdit text-edit endpoints and does not list tool calling; this is not the agent interface required to execute Zapier workflows.

最近核验时间：2026-11-05

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)

研究备注：
- The model is text-only and has no documented screenshot input or desktop-action interface.

最近核验时间：2026-11-05

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- The model is text-only and cannot receive chart images for visual question answering.

最近核验时间：2026-11-05

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Mercury Edit 2 is a specialized code next-edit model, not a general academic question-answering interface for HLE.

最近核验时间：2026-11-05

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Artificial Analysis V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The target index is a broad text-based evaluation suite; this model is a specialized code-edit suggestion model and exposes no general chat or tool-agent interface.

最近核验时间：2026-11-05

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mercury Edit 2 release post](https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2)
- [GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Code next-edit predictions do not provide the cross-industry agent workflow and professional work products required by GDPval-AA.

最近核验时间：2026-11-05

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Inception Mercury Edit 2 model directory](https://docs.inceptionlabs.ai/get-started/models)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- This specialized code-edit model does not expose the cross-industry tool-agent workflow required by the Vals Index.

最近核验时间：2026-11-05

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Artificial Analysis V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The target index is a broad text-based evaluation suite; this model is a specialized code-edit suggestion model and exposes no general chat or tool-agent interface."
      ],
      "status": "不适用"
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "The model directory exposes only FIM and NextEdit text-edit endpoints and does not list tool calling; this is not the agent interface required to execute Zapier workflows."
      ],
      "status": "不适用"
    },
    "chartography": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "The model is text-only and cannot receive chart images for visual question answering."
      ],
      "status": "不适用"
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05",
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
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Mercury Edit 2 release post",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2"
        }
      ],
      "notes": [
        "The model generates code edits, so this coding benchmark is applicable. No exact Mercury Edit 2 result was verified; the visible DeepSWE model list is incomplete."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 score was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mercury Edit 2 release post",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2"
        },
        {
          "label": "GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Code next-edit predictions do not provide the cross-industry agent workflow and professional work products required by GDPval-AA."
      ],
      "status": "不适用"
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Mercury Edit 2 release post",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Mercury Edit 2 is a specialized code next-edit model, not a general academic question-answering interface for HLE."
      ],
      "status": "不适用"
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "The model is text-only and has no documented screenshot input or desktop-action interface."
      ],
      "status": "不适用"
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Mercury Edit 2 release post",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2"
        }
      ],
      "notes": [
        "The model can generate code edits, but the official model directory and release post do not report SWE-bench Pro V2; no exact leaderboard score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 score was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Snorkel Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Mercury Edit 2 release post",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2"
        }
      ],
      "notes": [
        "The public leaderboard view did not expose an exact Mercury Edit 2 result; the model can generate code edits, so it is not marked not-applicable."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench Science 0.1.0 score was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Terminal-Bench official leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Terminal-Bench official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Mercury Edit 2 release post",
          "url": "https://www.inceptionlabs.ai/blog/introducing-mercury-edit-2"
        }
      ],
      "notes": [
        "The official leaderboard view did not expose a verifiable row for this model; the release post reports other coding benchmarks."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench 4.0 score was verified."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05",
      "checked_sources": [
        {
          "label": "Inception Mercury Edit 2 model directory",
          "url": "https://docs.inceptionlabs.ai/get-started/models"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "This specialized code-edit model does not expose the cross-industry tool-agent workflow required by the Vals Index."
      ],
      "status": "不适用"
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:33+08:00",
  "model_id": "inception/mercury-edit-2",
  "model_notes": [
    "Inception’s model directory identifies mercury-edit-2 as a text-only FIM/NextEdit model for code completion and next-edit suggestions; the official table does not list tool calling.",
    "The release post describes four different code-editing evaluations (Instinct, FIM, NEP, and an internal next-edit benchmark); none is mapped to the 11 repository targets."
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
