# Fugu Ultra Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：sakana/fugu-ultra
- 模型名称：Fugu Ultra
- 发布日期：2026-06-15
- 最近检查时间：2026-11-05T02:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：12
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方 Fugu Ultra API 目录目前将通用别名 fugu-ultra 指向 v2.0，同时仍列出 v1.0 和 v1.1；本地模型文件未固定版本，release_date=2026-06-15 也不足以确定 API pin。来源：https://console.sakana.ai/models
- Sakana technical report 对 Fugu-Ultra 的 HLE 50.0 及其他历史分数没有标注 API ID；Fugu Ultra v2 的 Chartography 宣传数值嵌在不可读取的图像中。均不据此猜测版本或测试条件。来源：https://arxiv.org/html/2606.21228v2；https://sakana.ai/fugu-max-release/

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 leaderboard and methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Sakana Fugu Ultra v2 announcement](https://sakana.ai/fugu-max-release/), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:58+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:58+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:58+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:58+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Sakana Fugu Ultra v2 announcement](https://sakana.ai/fugu-max-release/), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:58+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official site](https://osworld-v2.xlang.ai/), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:58+08:00 |
| chartography | 待核实 | — | [Sakana Fugu product page and embedded comparison](https://sakana.ai/fugu/), [Sakana model catalog and version IDs](https://console.sakana.ai/models), [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T02:58+08:00 |
| humanitys-last-exam | 待核实 | — | [Sakana Fugu technical report v2](https://arxiv.org/html/2606.21228v2), [Official HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam), [Sakana model catalog and version IDs](https://console.sakana.ai/models) | 2026-11-05T02:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:58+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard and methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Sakana Fugu Ultra v2 announcement](https://sakana.ai/fugu-max-release/)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- Sakana announces a Fugu Ultra v2.0 “DeepSWE” score of 74.3, but the announcement omits the DeepSWE version, metric, harness, and task conditions. The current v1.1 leaderboard does not show Fugu Ultra.

尚未解决的问题：
- Cannot verify that the 74.3 result is DeepSWE v1.1; no row added.

最近核验时间：2026-11-05T02:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The existing TOML row “SWE Bench Pro” 73.7 has no V2 version or V2 conditions. Sakana’s report names the earlier SWE Bench Pro evaluation; it does not report V2. The official V2 board does not list Fugu Ultra.

最近核验时间：2026-11-05T02:58+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The existing Terminal Bench 2.1 result (82.1) is not v4.0. The current official v4 page did not expose readable dynamic rows.

尚未解决的问题：
- Cannot confirm whether an exact Fugu Ultra v4.0 result exists from the current dynamic board response.

最近核验时间：2026-11-05T02:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The official Science 0.1 result table does not list Fugu Ultra; Sakana’s technical report does not include this benchmark.

最近核验时间：2026-11-05T02:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Sakana Fugu Ultra v2 announcement](https://sakana.ai/fugu-max-release/)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The v1.0.6 board shows the top 10 and a collapsed 116 additional entries. Sakana’s AutomationBench statement is for Fugu Max, not Fugu Ultra.

尚未解决的问题：
- The complete leaderboard is not visible, so absence of Fugu Ultra cannot be confirmed.

最近核验时间：2026-11-05T02:58+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official site](https://osworld-v2.xlang.ai/)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- Fugu Ultra accepts image inputs and supports tools, so the benchmark is not marked inapplicable. The official v2.1 materials checked do not list an Ultra result.

最近核验时间：2026-11-05T02:58+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Sakana Fugu product page and embedded comparison](https://sakana.ai/fugu/)
- [Sakana model catalog and version IDs](https://console.sakana.ai/models)
- [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Sakana states that Fugu Ultra v2.0 performs best or joint-best on Chartography, but the score is in an image that could not be read directly. The local TOML does not pin an API version; current alias fugu-ultra defaults to v2.0 while v1.0 remains separately available.

尚未解决的问题：
- No numeric score or exact effort/harness/test setup was recoverable, and the local model version is not pinned; no score added.

最近核验时间：2026-11-05T02:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Sakana Fugu technical report v2](https://arxiv.org/html/2606.21228v2)
- [Official HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Sakana model catalog and version IDs](https://console.sakana.ai/models)

研究备注：
- The existing TOML row is HLE 50.0. Report Table 1 also gives 50.0 for Fugu-Ultra; Appendix A describes the full 2,500-sample set including multimodal samples, without tools. The HLE method defines accuracy; however, the report does not identify a pinned Fugu Ultra API revision.

尚未解决的问题：
- Official API docs currently map fugu-ultra to v2.0 and also list v1.0/v1.1. The paper does not name a specific API ID, so the existing result cannot be assigned confidently to the current alias or a frozen release version.

最近核验时间：2026-11-05T02:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- No Fugu Ultra result is listed for AA Intelligence Index V5. HLE-Diamond within AA V5 is separate from original HLE.

最近核验时间：2026-11-05T02:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The current official GDPval-AA v2.1 board does not list a Fugu Ultra Elo result. Sakana’s Fugu report does not contain this evaluation.

最近核验时间：2026-11-05T02:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The current official Vals Index v2.2 listing does not show Fugu Ultra.

最近核验时间：2026-11-05T02:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "No Fugu Ultra result is listed for AA Intelligence Index V5. HLE-Diamond within AA V5 is separate from original HLE."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Sakana Fugu Ultra v2 announcement",
          "url": "https://sakana.ai/fugu-max-release/"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The v1.0.6 board shows the top 10 and a collapsed 116 additional entries. Sakana’s AutomationBench statement is for Fugu Max, not Fugu Ultra."
      ],
      "status": "待核实",
      "unresolved": [
        "The complete leaderboard is not visible, so absence of Fugu Ultra cannot be confirmed."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Sakana Fugu product page and embedded comparison",
          "url": "https://sakana.ai/fugu/"
        },
        {
          "label": "Sakana model catalog and version IDs",
          "url": "https://console.sakana.ai/models"
        },
        {
          "label": "Chartography official benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Sakana states that Fugu Ultra v2.0 performs best or joint-best on Chartography, but the score is in an image that could not be read directly. The local TOML does not pin an API version; current alias fugu-ultra defaults to v2.0 while v1.0 remains separately available."
      ],
      "status": "待核实",
      "unresolved": [
        "No numeric score or exact effort/harness/test setup was recoverable, and the local model version is not pinned; no score added."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard and methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Sakana Fugu Ultra v2 announcement",
          "url": "https://sakana.ai/fugu-max-release/"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "Sakana announces a Fugu Ultra v2.0 “DeepSWE” score of 74.3, but the announcement omits the DeepSWE version, metric, harness, and task conditions. The current v1.1 leaderboard does not show Fugu Ultra."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot verify that the 74.3 result is DeepSWE v1.1; no row added."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The current official GDPval-AA v2.1 board does not list a Fugu Ultra Elo result. Sakana’s Fugu report does not contain this evaluation."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Sakana Fugu technical report v2",
          "url": "https://arxiv.org/html/2606.21228v2"
        },
        {
          "label": "Official HLE leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Sakana model catalog and version IDs",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The existing TOML row is HLE 50.0. Report Table 1 also gives 50.0 for Fugu-Ultra; Appendix A describes the full 2,500-sample set including multimodal samples, without tools. The HLE method defines accuracy; however, the report does not identify a pinned Fugu Ultra API revision."
      ],
      "status": "待核实",
      "unresolved": [
        "Official API docs currently map fugu-ultra to v2.0 and also list v1.0/v1.1. The paper does not name a specific API ID, so the existing result cannot be assigned confidently to the current alias or a frozen release version."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "Fugu Ultra accepts image inputs and supports tools, so the benchmark is not marked inapplicable. The official v2.1 materials checked do not list an Ultra result."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The existing TOML row “SWE Bench Pro” 73.7 has no V2 version or V2 conditions. Sakana’s report names the earlier SWE Bench Pro evaluation; it does not report V2. The official V2 board does not list Fugu Ultra."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The official Science 0.1 result table does not list Fugu Ultra; Sakana’s technical report does not include this benchmark."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The existing Terminal Bench 2.1 result (82.1) is not v4.0. The current official v4 page did not expose readable dynamic rows."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot confirm whether an exact Fugu Ultra v4.0 result exists from the current dynamic board response."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The current official Vals Index v2.2 listing does not show Fugu Ultra."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 12,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:58+08:00",
  "model_id": "sakana/fugu-ultra",
  "model_notes": [
    "官方 Fugu Ultra API 目录目前将通用别名 fugu-ultra 指向 v2.0，同时仍列出 v1.0 和 v1.1；本地模型文件未固定版本，release_date=2026-06-15 也不足以确定 API pin。来源：https://console.sakana.ai/models",
    "Sakana technical report 对 Fugu-Ultra 的 HLE 50.0 及其他历史分数没有标注 API ID；Fugu Ultra v2 的 Chartography 宣传数值嵌在不可读取的图像中。均不据此猜测版本或测试条件。来源：https://arxiv.org/html/2606.21228v2；https://sakana.ai/fugu-max-release/"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
