# GLM-5V-Turbo Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：zhipuai/glm-5v-turbo
- 模型名称：GLM-5V-Turbo
- 发布日期：2026-04-01
- 最近检查时间：2026-11-05T10:15+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Exact identity is Z.AI GLM-5V-Turbo, released 2026-04-01. Official documentation confirms image/video/text/file input, text output, function calling, and multimodal coding/GUI use; the model is applicable to coding and computer-use benchmarks.
- Z.AI’s technical report reports OSWorld 62.3 without identifying an OSWorld-V2 release or evaluation configuration. OSWorld-V2 v2.1 was released later, on 2026-09-16, so 62.3 is not mapped to the v2.1 target.
- A third-party 17.1% HLE candidate could not be verified on Artificial Analysis’s current exact-model page or source report and was not written.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo) | 2026-11-05T10:15+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo) | 2026-11-05T10:15+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks), [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo) | 2026-11-05T10:15+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks), [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Z.AI GLM-5V-Turbo technical report](https://arxiv.org/html/2604.26752v3) | 2026-11-05T10:15+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo) | 2026-11-05T10:15+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Z.AI GLM-5V-Turbo technical report](https://arxiv.org/html/2604.26752v3), [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo) | 2026-11-05T10:15+08:00 |
| chartography | 未找到 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo) | 2026-11-05T10:15+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis exact GLM-5V-Turbo profile](https://artificialanalysis.ai/models/glm-5v-turbo), [Z.AI GLM-5V-Turbo technical report](https://arxiv.org/html/2604.26752v3), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:15+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact GLM-5V-Turbo profile](https://artificialanalysis.ai/models/glm-5v-turbo), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:15+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis exact GLM-5V-Turbo profile](https://artificialanalysis.ai/models/glm-5v-turbo), [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:15+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T10:15+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo)

研究备注：
- The checked leaderboard data did not provide an exact GLM-5V-Turbo row; the model is coding-capable but no direct score was verified.

尚未解决的问题：
- No exact DeepSWE v1.1 result was verified.

最近核验时间：2026-11-05T10:15+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo)

研究备注：
- The Z.AI model documentation describes coding and agent capabilities but does not report a SWE-bench Pro V2 score. No exact row was verified in the V2 leaderboard.

尚未解决的问题：
- No exact SWE-bench Pro V2 result was verified.

最近核验时间：2026-11-05T10:15+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks)
- [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo)

研究备注：
- No exact Terminal-Bench 4.0 result for GLM-5V-Turbo was found in the reviewed official model materials or version leaderboard.

尚未解决的问题：
- No exact Terminal-Bench 4.0 result was verified.

最近核验时间：2026-11-05T10:15+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks)
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Z.AI GLM-5V-Turbo technical report](https://arxiv.org/html/2604.26752v3)

研究备注：
- The model supports tools and coding, but no exact Terminal-Bench-Science 0.1.0 score was reported in the checked official sources.

尚未解决的问题：
- No exact Terminal-Bench-Science 0.1.0 result was verified.

最近核验时间：2026-11-05T10:15+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo)

研究备注：
- Function calling makes the model applicable. The official leaderboard folds 119 entries, and no exact task_completed_correctly score/configuration for this model was verifiable from the public view.

尚未解决的问题：
- No exact Zapier AutomationBench v1.0.6 result was verified.

最近核验时间：2026-11-05T10:15+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Z.AI GLM-5V-Turbo technical report](https://arxiv.org/html/2604.26752v3)
- [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo)

研究备注：
- Z.AI reports 62.3 on OSWorld for the exact model, but the report does not specify OSWorld-V2 or v2.1. The v2.1 release is dated 2026-09-16, after the report version dated 2026-05-12; the result cannot be assumed to use the target release.

尚未解决的问题：
- The OSWorld release/configuration for the 62.3 result is unknown; no v2.1 score was verified.

最近核验时间：2026-11-05T10:15+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Z.AI GLM-5V-Turbo official documentation](https://docs.z.ai/guides/vlm/glm-5v-turbo)

研究备注：
- The model is chart-capable and applicable. The current public leaderboard view contains other Z.AI models but no exact GLM-5V-Turbo result.

最近核验时间：2026-11-05T10:15+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis exact GLM-5V-Turbo profile](https://artificialanalysis.ai/models/glm-5v-turbo)
- [Z.AI GLM-5V-Turbo technical report](https://arxiv.org/html/2604.26752v3)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current exact-model profile has no visible original HLE score and the technical report does not report HLE. A third-party 17.1% candidate could not be verified against the official page/API, so no score was written.

尚未解决的问题：
- Verify whether the unconfirmed third-party 17.1% HLE candidate corresponds to this exact model and protocol.

最近核验时间：2026-11-05T10:15+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact GLM-5V-Turbo profile](https://artificialanalysis.ai/models/glm-5v-turbo)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current exact-model profile reports Index N/A for V5; an older v4 composite estimate is not transferable to V5.

最近核验时间：2026-11-05T10:15+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis exact GLM-5V-Turbo profile](https://artificialanalysis.ai/models/glm-5v-turbo)
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current profile and reviewed official report do not expose an exact GDPval-AA v2.1 result; the public results page lists only a subset of models.

尚未解决的问题：
- No exact GDPval-AA v2.1 result was verified.

最近核验时间：2026-11-05T10:15+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The current V2.2 leaderboard shows GLM 5.3 as the best Z.AI model and states that it shows the best model from each lab; this does not establish whether GLM-5V-Turbo was evaluated.

尚未解决的问题：
- No exact Vals Index v2.2 result was verified.

最近核验时间：2026-11-05T10:15+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact GLM-5V-Turbo profile",
          "url": "https://artificialanalysis.ai/models/glm-5v-turbo"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current exact-model profile reports Index N/A for V5; an older v4 composite estimate is not transferable to V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Z.AI GLM-5V-Turbo official documentation",
          "url": "https://docs.z.ai/guides/vlm/glm-5v-turbo"
        }
      ],
      "notes": [
        "Function calling makes the model applicable. The official leaderboard folds 119 entries, and no exact task_completed_correctly score/configuration for this model was verifiable from the public view."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Zapier AutomationBench v1.0.6 result was verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T10:15+08:00",
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
          "label": "Z.AI GLM-5V-Turbo official documentation",
          "url": "https://docs.z.ai/guides/vlm/glm-5v-turbo"
        }
      ],
      "notes": [
        "The model is chart-capable and applicable. The current public leaderboard view contains other Z.AI models but no exact GLM-5V-Turbo result."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T10:15+08:00",
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
          "label": "Z.AI GLM-5V-Turbo official documentation",
          "url": "https://docs.z.ai/guides/vlm/glm-5v-turbo"
        }
      ],
      "notes": [
        "The checked leaderboard data did not provide an exact GLM-5V-Turbo row; the model is coding-capable but no direct score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 result was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact GLM-5V-Turbo profile",
          "url": "https://artificialanalysis.ai/models/glm-5v-turbo"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current profile and reviewed official report do not expose an exact GDPval-AA v2.1 result; the public results page lists only a subset of models."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact GDPval-AA v2.1 result was verified."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact GLM-5V-Turbo profile",
          "url": "https://artificialanalysis.ai/models/glm-5v-turbo"
        },
        {
          "label": "Z.AI GLM-5V-Turbo technical report",
          "url": "https://arxiv.org/html/2604.26752v3"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current exact-model profile has no visible original HLE score and the technical report does not report HLE. A third-party 17.1% candidate could not be verified against the official page/API, so no score was written."
      ],
      "status": "待核实",
      "unresolved": [
        "Verify whether the unconfirmed third-party 17.1% HLE candidate corresponds to this exact model and protocol."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Z.AI GLM-5V-Turbo technical report",
          "url": "https://arxiv.org/html/2604.26752v3"
        },
        {
          "label": "Z.AI GLM-5V-Turbo official documentation",
          "url": "https://docs.z.ai/guides/vlm/glm-5v-turbo"
        }
      ],
      "notes": [
        "Z.AI reports 62.3 on OSWorld for the exact model, but the report does not specify OSWorld-V2 or v2.1. The v2.1 release is dated 2026-09-16, after the report version dated 2026-05-12; the result cannot be assumed to use the target release."
      ],
      "status": "待核实",
      "unresolved": [
        "The OSWorld release/configuration for the 62.3 result is unknown; no v2.1 score was verified."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Z.AI GLM-5V-Turbo official documentation",
          "url": "https://docs.z.ai/guides/vlm/glm-5v-turbo"
        }
      ],
      "notes": [
        "The Z.AI model documentation describes coding and agent capabilities but does not report a SWE-bench Pro V2 score. No exact row was verified in the V2 leaderboard."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 result was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T10:15+08:00",
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
          "label": "Z.AI GLM-5V-Turbo technical report",
          "url": "https://arxiv.org/html/2604.26752v3"
        }
      ],
      "notes": [
        "The model supports tools and coding, but no exact Terminal-Bench-Science 0.1.0 score was reported in the checked official sources."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench-Science 0.1.0 result was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench official versions and leaderboard",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Z.AI GLM-5V-Turbo official documentation",
          "url": "https://docs.z.ai/guides/vlm/glm-5v-turbo"
        }
      ],
      "notes": [
        "No exact Terminal-Bench 4.0 result for GLM-5V-Turbo was found in the reviewed official model materials or version leaderboard."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench 4.0 result was verified."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T10:15+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The current V2.2 leaderboard shows GLM 5.3 as the best Z.AI model and states that it shows the best model from each lab; this does not establish whether GLM-5V-Turbo was evaluated."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Vals Index v2.2 result was verified."
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:15+08:00",
  "model_id": "zhipuai/glm-5v-turbo",
  "model_notes": [
    "Exact identity is Z.AI GLM-5V-Turbo, released 2026-04-01. Official documentation confirms image/video/text/file input, text output, function calling, and multimodal coding/GUI use; the model is applicable to coding and computer-use benchmarks.",
    "Z.AI’s technical report reports OSWorld 62.3 without identifying an OSWorld-V2 release or evaluation configuration. OSWorld-V2 v2.1 was released later, on 2026-09-16, so 62.3 is not mapped to the v2.1 target.",
    "A third-party 17.1% HLE candidate could not be verified on Artificial Analysis’s current exact-model page or source report and was not written."
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
