# Jev Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：typesafe/jev-latest
- 模型名称：Jev
- 发布日期：2026-09-15
- 最近检查时间：2026-11-04T11:12+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [DeepSWE v1.1 official method](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:12+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [Scale SWE-bench Pro V2 official protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T11:12+08:00 |
| terminal-bench-v4 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [Terminal-Bench 4 official board](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 release and method](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T11:12+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [Terminal-Bench-Science 0.1 official method](https://www.tbench.ai/news/terminal-bench-science-0-1), [Artificial Analysis TBS method](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T11:12+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [Zapier AutomationBench leaderboard and task summary](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T11:12+08:00 |
| osworld-v2.1 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [OSWorld v2.1 official evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld leaderboard](https://osworld-v2.xlang.ai/) | 2026-11-04T11:12+08:00 |
| chartography | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [Chartography official task specification](https://github.com/surge-ai/chartography), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T11:12+08:00 |
| humanitys-last-exam | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [Original HLE definition and leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [HLE official repository](https://github.com/centerforaisafety/hle), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:12+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [Artificial Analysis Intelligence Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Jev 1.14 Decision Index profile](https://artificialanalysis.ai/decision-models/jev-1-14), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T11:12+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T11:12+08:00 |
| vals-index-v2.2 | 不适用 | — | [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index), [Vals Jev 1.14 profile](https://www.vals.ai/models/decision_jev-1.14), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [DeepSWE v1.1 official method](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. DeepSWE requires a coding agent to modify a repository, submit a patch and run verification. Jev returns typed decisions/boxes and cannot generate a patch or invoke tools.

最近核验时间：2026-11-04T11:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [Scale SWE-bench Pro V2 official protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. SWE-bench Pro V2 requires software agents to produce an issue-fixing diff and have it checked in a clean environment. Jev cannot generate code diffs or call tools.

最近核验时间：2026-11-04T11:12+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [Terminal-Bench 4 official board](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 release and method](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Terminal-Bench 4 requires an agent to run commands in a terminal environment and submit verifiable task outputs. Jev has no free-form command/code output or tool execution interface.

最近核验时间：2026-11-04T11:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [Terminal-Bench-Science 0.1 official method](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Artificial Analysis TBS method](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Terminal-Bench-Science requires terminal-based research workflows and generated/verified artifacts such as analyses, simulations, proofs or code. Jev cannot execute commands or create those artifacts.

最近核验时间：2026-11-04T11:12+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [Zapier AutomationBench leaderboard and task summary](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. AutomationBench requires end-to-end business workflows across apps using 47 tools and is graded by final application state. Jev returns typed values and cannot invoke tools or execute the workflow. The visible leaderboard omits 119 collapsed rows, so N/A is based on interface incompatibility, not on an inference from missing rows.

最近核验时间：2026-11-04T11:12+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [OSWorld v2.1 official evaluation guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld leaderboard](https://osworld-v2.xlang.ai/)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. OSWorld requires long-horizon desktop/GUI actions. Jev 1.14 can return a structured box answer, but its API has no desktop action/tool output for operating the environment; an external action adapter would be a separate evaluated system.

最近核验时间：2026-11-04T11:12+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [Chartography official task specification](https://github.com/surge-ai/chartography)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Chartography requires a chart image and answer text that is compared to the reference by a judge. Jev can accept images experimentally but its typed decision/box outputs cannot provide free-form chart readings or explanations.

最近核验时间：2026-11-04T11:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [Original HLE definition and leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [HLE official repository](https://github.com/centerforaisafety/hle)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. The target is the full 2,500-question original HLE set with both multiple-choice and short-answer items. Jev 1.14 lacks free-text output, so it cannot complete the full protocol. No exact Jev 1.14 full-HLE score was found; Jev 1.13’s HLE-MultiChoice subset result is a different dataset and version.

最近核验时间：2026-11-04T11:12+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [Artificial Analysis Intelligence Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Jev 1.14 Decision Index profile](https://artificialanalysis.ai/decision-models/jev-1-14)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. The Intelligence Index V5 composite includes coding, science and work-product evaluations that require free-form output and tool-based agents, which Jev cannot provide. The Jev 1.14 Decision Index score is a separate index and is not mapped to Intelligence Index V5.

最近核验时间：2026-11-04T11:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. GDPval-AA requires shell/web agent execution and professional work products such as documents, slides, diagrams and spreadsheets. Jev cannot call tools or generate those outputs.

最近核验时间：2026-11-04T11:12+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model catalog and alias mapping](https://docs.typesafe.ai/models)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)
- [Vals Jev 1.14 profile](https://www.vals.ai/models/decision_jev-1.14)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)

研究备注：
- At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Vals Index is an agentic composite across finance, coding, legal and tax, with terminal work and professional artifacts. Jev cannot generate those artifacts or execute tools. The Jev 1.14 Vals model profile lists ClaimBench, not Vals Index; no score is mapped.

最近核验时间：2026-11-04T11:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Jev 1.14 Decision Index profile",
          "url": "https://artificialanalysis.ai/decision-models/jev-1-14"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. The Intelligence Index V5 composite includes coding, science and work-product evaluations that require free-form output and tool-based agents, which Jev cannot provide. The Jev 1.14 Decision Index score is a separate index and is not mapped to Intelligence Index V5."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "Zapier AutomationBench leaderboard and task summary",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. AutomationBench requires end-to-end business workflows across apps using 47 tools and is graded by final application state. Jev returns typed values and cannot invoke tools or execute the workflow. The visible leaderboard omits 119 collapsed rows, so N/A is based on interface incompatibility, not on an inference from missing rows."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "Chartography official task specification",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Chartography requires a chart image and answer text that is compared to the reference by a judge. Jev can accept images experimentally but its typed decision/box outputs cannot provide free-form chart readings or explanations."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "DeepSWE v1.1 official method",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. DeepSWE requires a coding agent to modify a repository, submit a patch and run verification. Jev returns typed decisions/boxes and cannot generate a patch or invoke tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. GDPval-AA requires shell/web agent execution and professional work products such as documents, slides, diagrams and spreadsheets. Jev cannot call tools or generate those outputs."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "Original HLE definition and leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "HLE official repository",
          "url": "https://github.com/centerforaisafety/hle"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. The target is the full 2,500-question original HLE set with both multiple-choice and short-answer items. Jev 1.14 lacks free-text output, so it cannot complete the full protocol. No exact Jev 1.14 full-HLE score was found; Jev 1.13’s HLE-MultiChoice subset result is a different dataset and version."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "OSWorld v2.1 official evaluation guide",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. OSWorld requires long-horizon desktop/GUI actions. Jev 1.14 can return a structured box answer, but its API has no desktop action/tool output for operating the environment; an external action adapter would be a separate evaluated system."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "Scale SWE-bench Pro V2 official protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. SWE-bench Pro V2 requires software agents to produce an issue-fixing diff and have it checked in a clean environment. Jev cannot generate code diffs or call tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "Terminal-Bench-Science 0.1 official method",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Artificial Analysis TBS method",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Terminal-Bench-Science requires terminal-based research workflows and generated/verified artifacts such as analyses, simulations, proofs or code. Jev cannot execute commands or create those artifacts."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "Terminal-Bench 4 official board",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 release and method",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Terminal-Bench 4 requires an agent to run commands in a terminal environment and submit verifiable task outputs. Jev has no free-form command/code output or tool execution interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T11:12+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model catalog and alias mapping",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Jev 1.14 profile",
          "url": "https://www.vals.ai/models/decision_jev-1.14"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "At check time 2026-11-04, the TypeSafe model catalog mapped `jev-latest` to Jev 1.14.0 (`jev-1.14.0`); findings below apply to that resolved version, not the older Jev 1.13.0. Vals Index is an agentic composite across finance, coding, legal and tax, with terminal work and professional artifacts. Jev cannot generate those artifacts or execute tools. The Jev 1.14 Vals model profile lists ClaimBench, not Vals Index; no score is mapped."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T11:12+08:00",
  "model_id": "typesafe/jev-latest",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
