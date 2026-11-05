# Drex 1.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nace-ai/drex-v1.5
- 模型名称：Drex 1.5
- 发布日期：2026-09-28
- 最近检查时间：2026-11-04T06:59+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T06:59+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T06:59+08:00 |
| terminal-bench-v4 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Terminal-Bench run protocol](https://www.tbench.ai/run) | 2026-11-04T06:59+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Terminal-Bench Science description](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T06:59+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Zapier AutomationBench methodology](https://github.com/zapier/AutomationBench) | 2026-11-04T06:59+08:00 |
| osworld-v2.1 | 待核实 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 official release repository](https://github.com/xlang-ai/OSWorld-V2), [Nace.AI Drex Max launch benchmark table](https://www.nace.ai/blog/introducing-drex-max) | 2026-11-04T06:59+08:00 |
| chartography | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Chartography methodology](https://github.com/surge-ai/chartography) | 2026-11-04T06:59+08:00 |
| humanitys-last-exam | 待核实 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Humanity’s Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Nace.AI Drex Max launch benchmark table](https://www.nace.ai/blog/introducing-drex-max), [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5) | 2026-11-04T06:59+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Drex 1.5 Decision Index page](https://artificialanalysis.ai/decision-models/drex-v1-5) | 2026-11-04T06:59+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T06:59+08:00 |
| vals-index-v2.2 | 不适用 | — | [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5), [Vals Index methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T06:59+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- The official model card says Drex v1.5 returns typed decision probabilities and generates no text. DeepSWE requires a standalone software-engineering agent to edit a repository and submit a verifiable patch.

最近核验时间：2026-11-04T06:59+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro requires a code patch for a repository issue and test verification. Drex v1.5 alone does not generate patches.

最近核验时间：2026-11-04T06:59+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Terminal-Bench run protocol](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench requires a CLI agent in a sandbox. Drex v1.5 returns probabilities but has no terminal/tool interface; a wrapper with another code model would be a different system.

最近核验时间：2026-11-04T06:59+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Terminal-Bench Science description](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science requires an agent to perform research workflows and produce verifiable artifacts; Drex v1.5 alone cannot generate those artifacts.

最近核验时间：2026-11-04T06:59+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Zapier AutomationBench methodology](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench requires cross-application workflows and tool calls. Drex v1.5 alone only returns typed probabilities; an external agent result cannot be attributed to it.

最近核验时间：2026-11-04T06:59+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 official release repository](https://github.com/xlang-ai/OSWorld-V2)
- [Nace.AI Drex Max launch benchmark table](https://www.nace.ai/blog/introducing-drex-max)

研究备注：
- Nace’s Oct 19 table lists Drex v1.5 at OSWorld-V2 (automation) = 0.640, but does not state the benchmark release, metric, or harness. The OSWorld repository identifies osworld-v2.1 as the active recommended release; unable to confirm this row uses v2.1 binary completion.

尚未解决的问题：
- Nace’s OSWorld-V2 0.640 row does not disclose release v2.1, metric, or harness; cannot map it to binary task completion rate.

最近核验时间：2026-11-04T06:59+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Chartography methodology](https://github.com/surge-ai/chartography)

研究备注：
- Chartography needs chart-image input and answer generation. Drex v1.5 is text/JSON input and typed probability output, so it cannot run the target protocol.

最近核验时间：2026-11-04T06:59+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Humanity’s Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Nace.AI Drex Max launch benchmark table](https://www.nace.ai/blog/introducing-drex-max)
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)

研究备注：
- Nace’s Oct 19 table reports HLE = 11.4 for Drex v1.5, but gives no metric, dataset subset, or test configuration. The source does not establish that this is the repository target’s original 2,500-question HLE result.

尚未解决的问题：
- Nace’s HLE 11.4 row does not specify metric, dataset subset, or conditions; cannot confirm it is the original 2,500-question HLE target.

最近核验时间：2026-11-04T06:59+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Drex 1.5 Decision Index page](https://artificialanalysis.ai/decision-models/drex-v1-5)

研究备注：
- No Intelligence Index V5 score was found. Artificial Analysis lists Drex under its separate Decision Index; those scores are not Intelligence Index V5 and are not mapped here.

最近核验时间：2026-11-04T06:59+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires an agent to use shell/web tools and produce professional files. Drex v1.5 does not generate text or support tools.

最近核验时间：2026-11-04T06:59+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Nace.AI Drex v1.5 model card](https://huggingface.co/nace-ai/drex-v1.5)
- [Vals Index methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index measures finance, coding, legal, and tax agent work products; Drex v1.5 is a decision component rather than a standalone task-execution model.

最近核验时间：2026-11-04T06:59+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Drex 1.5 Decision Index page",
          "url": "https://artificialanalysis.ai/decision-models/drex-v1-5"
        }
      ],
      "notes": [
        "No Intelligence Index V5 score was found. Artificial Analysis lists Drex under its separate Decision Index; those scores are not Intelligence Index V5 and are not mapped here."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Zapier AutomationBench methodology",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench requires cross-application workflows and tool calls. Drex v1.5 alone only returns typed probabilities; an external agent result cannot be attributed to it."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Chartography methodology",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography needs chart-image input and answer generation. Drex v1.5 is text/JSON input and typed probability output, so it cannot run the target protocol."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "The official model card says Drex v1.5 returns typed decision probabilities and generates no text. DeepSWE requires a standalone software-engineering agent to edit a repository and submit a verifiable patch."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires an agent to use shell/web tools and produce professional files. Drex v1.5 does not generate text or support tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Humanity’s Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Nace.AI Drex Max launch benchmark table",
          "url": "https://www.nace.ai/blog/introducing-drex-max"
        },
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        }
      ],
      "notes": [
        "Nace’s Oct 19 table reports HLE = 11.4 for Drex v1.5, but gives no metric, dataset subset, or test configuration. The source does not establish that this is the repository target’s original 2,500-question HLE result."
      ],
      "status": "待核实",
      "unresolved": [
        "Nace’s HLE 11.4 row does not specify metric, dataset subset, or conditions; cannot confirm it is the original 2,500-question HLE target."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 official release repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Nace.AI Drex Max launch benchmark table",
          "url": "https://www.nace.ai/blog/introducing-drex-max"
        }
      ],
      "notes": [
        "Nace’s Oct 19 table lists Drex v1.5 at OSWorld-V2 (automation) = 0.640, but does not state the benchmark release, metric, or harness. The OSWorld repository identifies osworld-v2.1 as the active recommended release; unable to confirm this row uses v2.1 binary completion."
      ],
      "status": "待核实",
      "unresolved": [
        "Nace’s OSWorld-V2 0.640 row does not disclose release v2.1, metric, or harness; cannot map it to binary task completion rate."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro requires a code patch for a repository issue and test verification. Drex v1.5 alone does not generate patches."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Terminal-Bench Science description",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science requires an agent to perform research workflows and produce verifiable artifacts; Drex v1.5 alone cannot generate those artifacts."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Terminal-Bench run protocol",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench requires a CLI agent in a sandbox. Drex v1.5 returns probabilities but has no terminal/tool interface; a wrapper with another code model would be a different system."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T06:59+08:00",
      "checked_sources": [
        {
          "label": "Nace.AI Drex v1.5 model card",
          "url": "https://huggingface.co/nace-ai/drex-v1.5"
        },
        {
          "label": "Vals Index methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index measures finance, coding, legal, and tax agent work products; Drex v1.5 is a decision component rather than a standalone task-execution model."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T06:59+08:00",
  "model_id": "nace-ai/drex-v1.5",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
