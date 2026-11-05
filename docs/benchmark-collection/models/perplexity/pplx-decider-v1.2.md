# pplx-decider-v1.2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：perplexity/pplx-decider-v1.2
- 模型名称：pplx-decider-v1.2
- 发布日期：2026-10-15
- 最近检查时间：2026-11-04T02:42+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T02:42+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Scale SWE-bench Pro V2 Full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:42+08:00 |
| terminal-bench-v4 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Vals AI Terminal-Bench 4 methodology](https://www.vals-ai.com/benchmarks/terminal-bench-4) | 2026-11-04T02:42+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Terminal-Bench Science repository](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T02:42+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Perplexity Decisions API quickstart](https://docs.perplexity.ai/docs/decisions/quickstart), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T02:42+08:00 |
| osworld-v2.1 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 official page](https://osworld-v2.xlang.ai/) | 2026-11-04T02:42+08:00 |
| chartography | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Chartography original paper](https://arxiv.org/html/2608.10677v1), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T02:42+08:00 |
| humanitys-last-exam | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [HLE official repository](https://github.com/centerforaisafety/hle), [HLE official site](https://lastexam.ai/) | 2026-11-04T02:42+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Artificial Analysis Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T02:42+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T02:42+08:00 |
| vals-index-v2.2 | 不适用 | — | [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals AI methodology](https://www.vals.ai/methodology) | 2026-11-04T02:42+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE requires an agent to solve repository tasks, generate code and submit a patch for verification. This model only returns typed decision outputs, not a code change.

最近核验时间：2026-11-04T02:42+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Scale SWE-bench Pro V2 Full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 evaluates long-horizon software engineering tasks using submitted code diffs and test results. A choice/probability/score readout cannot produce the required patch.

最近核验时间：2026-11-04T02:42+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Vals AI Terminal-Bench 4 methodology](https://www.vals-ai.com/benchmarks/terminal-bench-4)

研究备注：
- Terminal-Bench requires an agent to operate a sandboxed terminal and produce a verifier-passing result. The model has no free-form code output or tool-call capability.

最近核验时间：2026-11-04T02:42+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Terminal-Bench Science repository](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- Terminal-Bench Science requires terminal-based scientific workflows, tool actions and verifiable artifacts. Structured decision outputs cannot perform the protocol.

最近核验时间：2026-11-04T02:42+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Perplexity Decisions API quickstart](https://docs.perplexity.ai/docs/decisions/quickstart)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- AutomationBench requires multi-step workflows across business applications with tool execution and final environment-state verification. The model cannot execute actions or call tools.

最近核验时间：2026-11-04T02:42+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 official page](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld v2.1 evaluates multi-step desktop/GUI use. Image input does not supply the missing GUI action/tool output; the model cannot perform the computer-use tasks.

最近核验时间：2026-11-04T02:42+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Chartography original paper](https://arxiv.org/html/2608.10677v1)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Standard Chartography takes a chart image and question, then scores a free-form text answer. This model can receive images but only emits typed decision values; changing the task to closed-set choices would alter the protocol.

最近核验时间：2026-11-04T02:42+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [HLE official repository](https://github.com/centerforaisafety/hle)
- [HLE official site](https://lastexam.ai/)

研究备注：
- The target is the original full HLE set, mixing multiple-choice and short-answer questions. The model cannot generate arbitrary short-answer text, so it cannot follow the full protocol even though it can answer some closed-choice items.

最近核验时间：2026-11-04T02:42+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Artificial Analysis Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA Intelligence Index v5 aggregates nine different evaluations, including work-product creation, coding and terminal agent tasks. The model has no free-text output or tool use. Its Decision Index and Vision Decision Index are separate evaluations, not this benchmark.

最近核验时间：2026-11-04T02:42+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 requires agentic shell/web use and professional work-product generation such as documents and spreadsheets. This decision model has no tools or text/file generation.

最近核验时间：2026-11-04T02:42+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [pplx-decider-v1.2 model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI methodology](https://www.vals.ai/methodology)

研究备注：
- Vals Index aggregates finance, coding, legal and tax workflows, including spreadsheet modeling, terminal use, code migration and legal research. The model cannot produce deliverables or take tool actions.

最近核验时间：2026-11-04T02:42+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
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
        "AA Intelligence Index v5 aggregates nine different evaluations, including work-product creation, coding and terminal agent tasks. The model has no free-text output or tool use. Its Decision Index and Vision Decision Index are separate evaluations, not this benchmark."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "Perplexity Decisions API quickstart",
          "url": "https://docs.perplexity.ai/docs/decisions/quickstart"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench requires multi-step workflows across business applications with tool execution and final environment-state verification. The model cannot execute actions or call tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
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
        "Standard Chartography takes a chart image and question, then scores a free-form text answer. This model can receive images but only emits typed decision values; changing the task to closed-set choices would alter the protocol."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE requires an agent to solve repository tasks, generate code and submit a patch for verification. This model only returns typed decision outputs, not a code change."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 requires agentic shell/web use and professional work-product generation such as documents and spreadsheets. This decision model has no tools or text/file generation."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
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
        "The target is the original full HLE set, mixing multiple-choice and short-answer questions. The model cannot generate arbitrary short-answer text, so it cannot follow the full protocol even though it can answer some closed-choice items."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 official page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "OSWorld v2.1 evaluates multi-step desktop/GUI use. Image input does not supply the missing GUI action/tool output; the model cannot perform the computer-use tasks."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "Scale SWE-bench Pro V2 Full",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 evaluates long-horizon software engineering tasks using submitted code diffs and test results. A choice/probability/score readout cannot produce the required patch."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
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
        "Terminal-Bench Science requires terminal-based scientific workflows, tool actions and verifiable artifacts. Structured decision outputs cannot perform the protocol."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "Vals AI Terminal-Bench 4 methodology",
          "url": "https://www.vals-ai.com/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Terminal-Bench requires an agent to operate a sandboxed terminal and produce a verifier-passing result. The model has no free-form code output or tool-call capability."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:42+08:00",
      "checked_sources": [
        {
          "label": "pplx-decider-v1.2 model card",
          "url": "https://huggingface.co/perplexity-ai/pplx-decider-v1.2"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI methodology",
          "url": "https://www.vals.ai/methodology"
        }
      ],
      "notes": [
        "Vals Index aggregates finance, coding, legal and tax workflows, including spreadsheet modeling, terminal use, code migration and legal research. The model cannot produce deliverables or take tool actions."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:42+08:00",
  "model_id": "perplexity/pplx-decider-v1.2",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
