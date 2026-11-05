# Gemini Flash-Lite Latest Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-flash-lite-latest
- 模型名称：Gemini Flash-Lite Latest
- 发布日期：2026-07-21
- 最近检查时间：2026-11-04T22:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Datacurve DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| terminal-bench-v4 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| osworld-v2.1 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| chartography | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T22:53+08:00 |
| humanitys-last-exam | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T22:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Artificial Analysis Gemini 3.5 Flash-Lite profile](https://artificialanalysis.ai/models/gemini-3-5-flash-lite), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T22:53+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:53+08:00 |
| vals-index-v2.2 | 待核实 | — | [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T22:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Datacurve DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- No leaderboard row explicitly names `gemini-flash-lite-latest`; the visible Gemini 3.5 Flash [high] row is a different model.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- The 54.2% in the concrete Gemini 3.5 Flash-Lite model card is July SWE-Bench Pro (Public) without a V2 label. It is not an exact alias or V2 score.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- The concrete Gemini 3.5 Flash-Lite 54.0% model-card result is Terminal-Bench 2.1, not V4; no exact alias V4 row was found.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- No exact alias result was found on the Vals Science leaderboard; no score from concrete Gemini models was transferred.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- Zapier has public rows for concrete Gemini 3.5 Flash-Lite effort settings, but the available source does not state those evaluations used the mutable alias. No alias-specific score is written.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- Google reports OSWorld-Verified for the concrete Gemini 3.5 Flash-Lite; that is not OSWorld v2.1 and does not identify an alias evaluation.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- Surge lists a concrete Gemini 3.5 Flash-Lite result, but not the mutable alias; no score was transferred.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- No original source explicitly attributes an HLE run to this alias. Concrete-model or secondary scores cannot establish the alias version.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Artificial Analysis Gemini 3.5 Flash-Lite profile](https://artificialanalysis.ai/models/gemini-3-5-flash-lite)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- The Artificial Analysis score 12 / v5.0.1 belongs to the concrete Gemini 3.5 Flash-Lite profile. It is not evidence for a run using this alias.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Gemini 3.5 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- The concrete model-card result 1140 Elo is GDPval-AA v2, not v2.1, and does not identify the alias evaluation.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Google model/version documentation](https://ai.google.dev/gemini-api/docs/models)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.
- The Vals v2.2 page does not list the alias; concrete-model scores from older Vals versions do not establish an alias result.

尚未解决的问题：
- 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。

最近核验时间：2026-11-04T22:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Artificial Analysis Gemini 3.5 Flash-Lite profile",
          "url": "https://artificialanalysis.ai/models/gemini-3-5-flash-lite"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "The Artificial Analysis score 12 / v5.0.1 belongs to the concrete Gemini 3.5 Flash-Lite profile. It is not evidence for a run using this alias."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "Zapier has public rows for concrete Gemini 3.5 Flash-Lite effort settings, but the available source does not state those evaluations used the mutable alias. No alias-specific score is written."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "Surge lists a concrete Gemini 3.5 Flash-Lite result, but not the mutable alias; no score was transferred."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Datacurve DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "No leaderboard row explicitly names `gemini-flash-lite-latest`; the visible Gemini 3.5 Flash [high] row is a different model."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "The concrete model-card result 1140 Elo is GDPval-AA v2, not v2.1, and does not identify the alias evaluation."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Artificial Analysis HLE evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "No original source explicitly attributes an HLE run to this alias. Concrete-model or secondary scores cannot establish the alias version."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "Google reports OSWorld-Verified for the concrete Gemini 3.5 Flash-Lite; that is not OSWorld v2.1 and does not identify an alias evaluation."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "The 54.2% in the concrete Gemini 3.5 Flash-Lite model card is July SWE-Bench Pro (Public) without a V2 label. It is not an exact alias or V2 score."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Vals Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "No exact alias result was found on the Vals Science leaderboard; no score from concrete Gemini models was transferred."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Gemini 3.5 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "The concrete Gemini 3.5 Flash-Lite 54.0% model-card result is Terminal-Bench 2.1, not V4; no exact alias V4 row was found."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T22:53+08:00",
      "checked_sources": [
        {
          "label": "Google model/version documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias.",
        "The Vals v2.2 page does not list the alias; concrete-model scores from older Vals versions do not establish an alias result."
      ],
      "status": "待核实",
      "unresolved": [
        "需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T22:53+08:00",
  "model_id": "google/gemini-flash-lite-latest",
  "model_notes": [
    "Google defines `gemini-flash-lite-latest` as a mutable latest alias that may hot-swap; official docs do not provide its historical concrete model ID for benchmark runs. The local TOML comment says it tracks `gemini-3.5-flash-lite`, but that comment alone does not identify the model version used in a source evaluation. Scores explicitly reported for Gemini 3.5 Flash-Lite were therefore not assigned to this alias."
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
