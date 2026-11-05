# d3-flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：vllm-sr/d3-flash
- 模型名称：d3-flash
- 发布日期：2026-10-10
- 最近检查时间：2026-11-04T03:22+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T03:22+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Scale AI SWE-bench Pro V2 leaderboard and protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T03:22+08:00 |
| terminal-bench-v4 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Terminal-Bench 4.0 protocol](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T03:22+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Terminal-Bench Science v0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T03:22+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks) | 2026-11-04T03:22+08:00 |
| osworld-v2.1 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T03:22+08:00 |
| chartography | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Chartography official paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T03:22+08:00 |
| humanitys-last-exam | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Scale original Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Humanity’s Last Exam official paper](https://arxiv.org/html/2501.14249v12) | 2026-11-04T03:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis model directory](https://artificialanalysis.ai/models) | 2026-11-04T03:22+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Artificial Analysis GDPval-AA v2.1 protocol](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T03:22+08:00 |
| vals-index-v2.2 | 不适用 | — | [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash), [Vals Index V2.2 methodology and leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T03:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- The d3-flash card describes a decision-only output interface with choice, yes/no, or score answers and no free-form text. DeepSWE v1.1 evaluates code changes submitted as patches, so the standard protocol is not compatible. The card has no DeepSWE result.

最近核验时间：2026-11-04T03:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Scale AI SWE-bench Pro V2 leaderboard and protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 requires an agent-produced repository diff for clean-image re-evaluation. d3-flash cannot produce a code diff through its standard typed-decision interface. No target result is published on the card.

最近核验时间：2026-11-04T03:22+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Terminal-Bench 4.0 protocol](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4 evaluates terminal agents. The d3-flash card exposes no tool or terminal-action output; its Jev and Perception results are different benchmarks and were not reused.

最近核验时间：2026-11-04T03:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Terminal-Bench Science v0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science requires terminal workflows and testable research artifacts. d3-flash only emits typed decision values; no result for this target appears on its card.

最近核验时间：2026-11-04T03:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks)

研究备注：
- AutomationBench runs agents through end-to-end workflows using real tools and scores final application state. d3-flash has no tool-use interface and does not generate workflow text.

最近核验时间：2026-11-04T03:22+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 requires computer-use agents to execute GUI actions. d3-flash can receive images but only returns structured decisions, not clicks, typing, or key actions.

最近核验时间：2026-11-04T03:22+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Chartography official paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Chartography requires chart-image interpretation followed by free-form text answers. Image input alone is insufficient because d3-flash only returns typed decision outputs.

最近核验时间：2026-11-04T03:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Scale original Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Humanity’s Last Exam official paper](https://arxiv.org/html/2501.14249v12)

研究备注：
- The original 2,500-question HLE contains a mix of multiple-choice and exact-string answers (the official paper reports 24% multiple choice and 76% exact-match strings). A decision-only output cannot complete the standard full-set protocol; a multiple-choice-only subset would be a different dataset configuration. The Scale board does not list d3-flash.

最近核验时间：2026-11-04T03:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis model directory](https://artificialanalysis.ai/models)

研究备注：
- V5.0 is a composite across knowledge work, coding, science, and general knowledge, including tasks requiring text or work-product outputs. The decision-only d3-flash interface is incompatible with the composite protocol. Its Jev Decision Index is a separate benchmark. The AA model directory does not show d3-flash.

最近核验时间：2026-11-04T03:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Artificial Analysis GDPval-AA v2.1 protocol](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 requires an agent loop with shell and web access and outputs such as documents, slides, diagrams, and spreadsheets. d3-flash has no tool or work-product output interface.

最近核验时间：2026-11-04T03:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [vLLM-SR d3-flash official model card](https://huggingface.co/vllm-sr/d3-flash)
- [Vals Index V2.2 methodology and leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index evaluates agentic finance, coding, legal, and tax work. d3-flash has no tool/action interface or text/artifact output needed for these task protocols. The Vals leaderboard does not list d3-flash.

最近核验时间：2026-11-04T03:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis model directory",
          "url": "https://artificialanalysis.ai/models"
        }
      ],
      "notes": [
        "V5.0 is a composite across knowledge work, coding, science, and general knowledge, including tasks requiring text or work-product outputs. The decision-only d3-flash interface is incompatible with the composite protocol. Its Jev Decision Index is a separate benchmark. The AA model directory does not show d3-flash."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Zapier AutomationBench leaderboard and protocol",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench runs agents through end-to-end workflows using real tools and scores final application state. d3-flash has no tool-use interface and does not generate workflow text."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Chartography official paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "Chartography requires chart-image interpretation followed by free-form text answers. Image input alone is insufficient because d3-flash only returns typed decision outputs."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "DeepSWE v1.1",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "The d3-flash card describes a decision-only output interface with choice, yes/no, or score answers and no free-form text. DeepSWE v1.1 evaluates code changes submitted as patches, so the standard protocol is not compatible. The card has no DeepSWE result."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 protocol",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 requires an agent loop with shell and web access and outputs such as documents, slides, diagrams, and spreadsheets. d3-flash has no tool or work-product output interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Scale original Humanity’s Last Exam leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Humanity’s Last Exam official paper",
          "url": "https://arxiv.org/html/2501.14249v12"
        }
      ],
      "notes": [
        "The original 2,500-question HLE contains a mix of multiple-choice and exact-string answers (the official paper reports 24% multiple choice and 76% exact-match strings). A decision-only output cannot complete the standard full-set protocol; a multiple-choice-only subset would be a different dataset configuration. The Scale board does not list d3-flash."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 requires computer-use agents to execute GUI actions. d3-flash can receive images but only returns structured decisions, not clicks, typing, or key actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard and protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires an agent-produced repository diff for clean-image re-evaluation. d3-flash cannot produce a code diff through its standard typed-decision interface. No target result is published on the card."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Terminal-Bench Science v0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science requires terminal workflows and testable research artifacts. d3-flash only emits typed decision values; no result for this target appears on its card."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Terminal-Bench 4.0 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4 evaluates terminal agents. The d3-flash card exposes no tool or terminal-action output; its Jev and Perception results are different benchmarks and were not reused."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T03:22+08:00",
      "checked_sources": [
        {
          "label": "vLLM-SR d3-flash official model card",
          "url": "https://huggingface.co/vllm-sr/d3-flash"
        },
        {
          "label": "Vals Index V2.2 methodology and leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index evaluates agentic finance, coding, legal, and tax work. d3-flash has no tool/action interface or text/artifact output needed for these task protocols. The Vals leaderboard does not list d3-flash."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T03:22+08:00",
  "model_id": "vllm-sr/d3-flash",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
