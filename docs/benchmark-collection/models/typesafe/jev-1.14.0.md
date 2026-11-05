# Jev 1.14 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：typesafe/jev-1.14.0
- 模型名称：Jev 1.14
- 发布日期：2026-10-14
- 最近检查时间：2026-11-04T02:44+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T02:44+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [TypeSafe model page](https://docs.typesafe.ai/models), [Scale SWE-bench Pro V2 Full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:44+08:00 |
| terminal-bench-v4 | 不适用 | — | [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [Vals AI Terminal-Bench 4 methodology](https://www.vals-ai.com/benchmarks/terminal-bench-4) | 2026-11-04T02:44+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Terminal-Bench Science repository](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T02:44+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T02:44+08:00 |
| osworld-v2.1 | 不适用 | — | [TypeSafe image input documentation](https://docs.typesafe.ai/images), [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T02:44+08:00 |
| chartography | 不适用 | — | [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14), [Chartography original paper](https://arxiv.org/html/2608.10677v1), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T02:44+08:00 |
| humanitys-last-exam | 不适用 | — | [TypeSafe model page](https://docs.typesafe.ai/models), [HLE official repository](https://github.com/centerforaisafety/hle), [HLE official site](https://lastexam.ai/) | 2026-11-04T02:44+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [TypeSafe Jev model page](https://docs.typesafe.ai/models), [Artificial Analysis Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T02:44+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [TypeSafe System One API](https://docs.typesafe.ai/api/system-one), [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T02:44+08:00 |
| vals-index-v2.2 | 不适用 | — | [TypeSafe Jev model page](https://docs.typesafe.ai/models), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals AI methodology](https://www.vals.ai/methodology), [Vals Jev 1.14 profile](https://www.vals.ai/models/decision_jev-1.14) | 2026-11-04T02:44+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE requires an agent to generate and submit code patches in repository tasks. Jev only returns typed decisions and cannot create a patch or invoke tools.

最近核验时间：2026-11-04T02:44+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model page](https://docs.typesafe.ai/models)
- [Scale SWE-bench Pro V2 Full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 scores patches submitted for long-horizon code changes and checked in clean environments. Jev does not output code diffs or call tools.

最近核验时间：2026-11-04T02:44+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [Vals AI Terminal-Bench 4 methodology](https://www.vals-ai.com/benchmarks/terminal-bench-4)

研究备注：
- Terminal-Bench 4 requires a harness to operate a sandbox shell and submit a task result for verification. Jev has neither free-form code output nor tool execution.

最近核验时间：2026-11-04T02:44+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Terminal-Bench Science repository](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Terminal-Bench Science consists of verified research workflows in a terminal; the agent must execute commands and produce tested artifacts. Jev cannot do this.

最近核验时间：2026-11-04T02:44+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- AutomationBench requires end-to-end business workflows across applications using tools and actions. Jev returns typed decision values and cannot execute the workflow.

最近核验时间：2026-11-04T02:44+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe image input documentation](https://docs.typesafe.ai/images)
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld requires long-horizon desktop/GUI actions. Jev 1.14 can take images and return a structured box answer, but its API has no desktop action/tool output to operate the environment.

最近核验时间：2026-11-04T02:44+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe Jev 1.14 release](https://typesafe.ai/blog/jev-1-14)
- [Chartography original paper](https://arxiv.org/html/2608.10677v1)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Standard Chartography requires a chart image and question, followed by a free-form text answer. Jev can accept images, but its typed decision/box output cannot produce the answer required by the standard protocol.

最近核验时间：2026-11-04T02:44+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe model page](https://docs.typesafe.ai/models)
- [HLE official repository](https://github.com/centerforaisafety/hle)
- [HLE official site](https://lastexam.ai/)

研究备注：
- The target is the original full HLE set, with both multiple-choice and short-answer questions. Jev cannot generate arbitrary short-answer text, so it cannot follow the complete benchmark protocol even though it can answer some closed-choice items.

最近核验时间：2026-11-04T02:44+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe Jev model page](https://docs.typesafe.ai/models)
- [Artificial Analysis Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA Intelligence Index V5 aggregates nine distinct evaluations, including work-product, coding and tool-based agent tasks. Jev has no free-text output or tool execution. AA Decision Index (57) is a different benchmark and is not mapped here.

最近核验时间：2026-11-04T02:44+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe System One API](https://docs.typesafe.ai/api/system-one)
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 requires tool-based professional work with generated documents and other deliverables. Jev does not generate natural-language work products or invoke tools.

最近核验时间：2026-11-04T02:44+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [TypeSafe Jev model page](https://docs.typesafe.ai/models)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI methodology](https://www.vals.ai/methodology)
- [Vals Jev 1.14 profile](https://www.vals.ai/models/decision_jev-1.14)

研究备注：
- Vals Index aggregates finance, coding, legal and tax workflows, including files, terminal tasks and multi-step agent work. Jev cannot execute those workflows or create deliverables. Vals model profile ClaimBench is a different benchmark, not the Vals Index.

最近核验时间：2026-11-04T02:44+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe Jev model page",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "Artificial Analysis Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA Intelligence Index V5 aggregates nine distinct evaluations, including work-product, coding and tool-based agent tasks. Jev has no free-text output or tool execution. AA Decision Index (57) is a different benchmark and is not mapped here."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench requires end-to-end business workflows across applications using tools and actions. Jev returns typed decision values and cannot execute the workflow."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "Chartography original paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Standard Chartography requires a chart image and question, followed by a free-form text answer. Jev can accept images, but its typed decision/box output cannot produce the answer required by the standard protocol."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE requires an agent to generate and submit code patches in repository tasks. Jev only returns typed decisions and cannot create a patch or invoke tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 requires tool-based professional work with generated documents and other deliverables. Jev does not generate natural-language work products or invoke tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model page",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "HLE official repository",
          "url": "https://github.com/centerforaisafety/hle"
        },
        {
          "label": "HLE official site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "The target is the original full HLE set, with both multiple-choice and short-answer questions. Jev cannot generate arbitrary short-answer text, so it cannot follow the complete benchmark protocol even though it can answer some closed-choice items."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe image input documentation",
          "url": "https://docs.typesafe.ai/images"
        },
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld requires long-horizon desktop/GUI actions. Jev 1.14 can take images and return a structured box answer, but its API has no desktop action/tool output to operate the environment."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe model page",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "Scale SWE-bench Pro V2 Full",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 scores patches submitted for long-horizon code changes and checked in clean environments. Jev does not output code diffs or call tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe System One API",
          "url": "https://docs.typesafe.ai/api/system-one"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench Science repository",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "Terminal-Bench Science consists of verified research workflows in a terminal; the agent must execute commands and produce tested artifacts. Jev cannot do this."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe Jev 1.14 release",
          "url": "https://typesafe.ai/blog/jev-1-14"
        },
        {
          "label": "Vals AI Terminal-Bench 4 methodology",
          "url": "https://www.vals-ai.com/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Terminal-Bench 4 requires a harness to operate a sandbox shell and submit a task result for verification. Jev has neither free-form code output nor tool execution."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:44+08:00",
      "checked_sources": [
        {
          "label": "TypeSafe Jev model page",
          "url": "https://docs.typesafe.ai/models"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI methodology",
          "url": "https://www.vals.ai/methodology"
        },
        {
          "label": "Vals Jev 1.14 profile",
          "url": "https://www.vals.ai/models/decision_jev-1.14"
        }
      ],
      "notes": [
        "Vals Index aggregates finance, coding, legal and tax workflows, including files, terminal tasks and multi-step agent work. Jev cannot execute those workflows or create deliverables. Vals model profile ClaimBench is a different benchmark, not the Vals Index."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:44+08:00",
  "model_id": "typesafe/jev-1.14.0",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
