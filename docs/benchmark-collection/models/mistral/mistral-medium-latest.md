# Mistral Medium (latest) Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/mistral-medium-latest
- 模型名称：Mistral Medium (latest)
- 发布日期：2026-04-29
- 最近检查时间：2026-11-05T06:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Mistral 本地模型注释及官方 Vibe 文档均将 mistral-medium-latest 指向 Medium 3.5；官方生命周期政策说明 -latest 是可变 alias。没有把固定 Medium 3.5 的成绩迁移到此可变 alias。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:53+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:53+08:00 |
| terminal-bench-v4 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5), [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:53+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4), [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:53+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T06:53+08:00 |
| osworld-v2.1 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository and releases](https://github.com/xlang-ai/OSWorld-V2/releases) | 2026-11-05T06:53+08:00 |
| chartography | 未找到 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:53+08:00 |
| humanitys-last-exam | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1), [Humanity’s Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Artificial Analysis Mistral Medium 3.5 model page](https://artificialanalysis.ai/models/mistral-medium-3-5), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:53+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5), [GDPval-AA v2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:53+08:00 |
| vals-index-v2.2 | 未找到 | — | [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration), [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Mistral 官方将 mistral-medium-latest 用作 Medium 3.5 alias，但生命周期政策说明 -latest 是可变 alias；DeepSWE 榜面也未完整展示。

尚未解决的问题：
- 需固定评测时间点所指向的模型版本，并检查未显示榜单配置。

最近核验时间：2026-11-05T06:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 当前公开 V2 榜单未见精确 alias 行；未将固定版 SWE-Bench Verified 结果映射到 Pro V2。

最近核验时间：2026-11-05T06:53+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- AA 页面有固定 Mistral Medium 3.5 的成绩，但没有证据证明 alias 在评测时指向该固定 checkpoint。

尚未解决的问题：
- 需核实 AA 评测时 mistral-medium-latest 的目标 checkpoint。

最近核验时间：2026-11-05T06:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4)
- [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 页面有固定 Mistral Medium 3.5 的成绩，但没有证据证明 alias 在评测时指向该固定 checkpoint。

尚未解决的问题：
- 需核实评测时 alias 的目标 checkpoint。

最近核验时间：2026-11-05T06:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- Zapier 榜单隐藏 119 条记录，且 alias 会更新；未能确定 exact alias 的评测行或版本。

尚未解决的问题：
- 需检查折叠榜单并核验评测时 alias 指向。

最近核验时间：2026-11-05T06:53+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository and releases](https://github.com/xlang-ai/OSWorld-V2/releases)

研究备注：
- 动态榜单当前无法确认 alias 的完整名称和固定版本。

尚未解决的问题：
- 需锁定评测时 alias 目标并检查完整 OSWorld V2.1 榜单。

最近核验时间：2026-11-05T06:53+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 当前公开榜单未列出精确 alias；没有将同名基础型号的结果迁移到可变 alias。

最近核验时间：2026-11-05T06:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1)
- [Humanity’s Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Mistral Medium 3.5 固定型号有 14% 子集结果，但无法确认 alias 在评测时解析为该 checkpoint。

尚未解决的问题：
- 需核实评测时 alias 的目标 checkpoint。

最近核验时间：2026-11-05T06:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Artificial Analysis Mistral Medium 3.5 model page](https://artificialanalysis.ai/models/mistral-medium-3-5)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 对固定版 Mistral Medium 3.5 有 Index 5，但当前材料无法将该固定版结果归属到评测时可变 alias。

尚未解决的问题：
- 需核实 AA 评测记录使用的模型 ID/checkpoint。

最近核验时间：2026-11-05T06:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)
- [GDPval-AA v2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 固定版 Medium 3.5 页面存在 761/769 不同读数；此外无法锁定 alias 的评测 checkpoint。

尚未解决的问题：
- 需确认 alias 指向及 GDPval 官方读数差异。

最近核验时间：2026-11-05T06:53+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mistral Vibe model configuration](https://docs.mistral.ai/vibe/code/cli/configuration)
- [Mistral model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前官方 Vals Index v2.2 页面未列出精确 alias；未从固定版搬移成绩。

最近核验时间：2026-11-05T06:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 model page",
          "url": "https://artificialanalysis.ai/models/mistral-medium-3-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 对固定版 Mistral Medium 3.5 有 Index 5，但当前材料无法将该固定版结果归属到评测时可变 alias。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实 AA 评测记录使用的模型 ID/checkpoint。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Zapier 榜单隐藏 119 条记录，且 alias 会更新；未能确定 exact alias 的评测行或版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查折叠榜单并核验评测时 alias 指向。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "当前公开榜单未列出精确 alias；没有将同名基础型号的结果迁移到可变 alias。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Mistral 官方将 mistral-medium-latest 用作 Medium 3.5 alias，但生命周期政策说明 -latest 是可变 alias；DeepSWE 榜面也未完整展示。"
      ],
      "status": "待核实",
      "unresolved": [
        "需固定评测时间点所指向的模型版本，并检查未显示榜单配置。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Step 5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        },
        {
          "label": "GDPval-AA v2.1 official leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "固定版 Medium 3.5 页面存在 761/769 不同读数；此外无法锁定 alias 的评测 checkpoint。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 alias 指向及 GDPval 官方读数差异。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / GLM-5.1 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-glm-5-1"
        },
        {
          "label": "Humanity’s Last Exam evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Mistral Medium 3.5 固定型号有 14% 子集结果，但无法确认 alias 在评测时解析为该 checkpoint。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实评测时 alias 的目标 checkpoint。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository and releases",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        }
      ],
      "notes": [
        "动态榜单当前无法确认 alias 的完整名称和固定版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "需锁定评测时 alias 目标并检查完整 OSWorld V2.1 榜单。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "当前公开 V2 榜单未见精确 alias 行；未将固定版 SWE-Bench Verified 结果映射到 Pro V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4"
        },
        {
          "label": "Terminal-Bench Science 0.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 页面有固定 Mistral Medium 3.5 的成绩，但没有证据证明 alias 在评测时指向该固定 checkpoint。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实评测时 alias 的目标 checkpoint。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Step 5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        },
        {
          "label": "Terminal-Bench 4.0 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "AA 页面有固定 Mistral Medium 3.5 的成绩，但没有证据证明 alias 在评测时指向该固定 checkpoint。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实 AA 评测时 mistral-medium-latest 的目标 checkpoint。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Mistral Vibe model configuration",
          "url": "https://docs.mistral.ai/vibe/code/cli/configuration"
        },
        {
          "label": "Mistral model lifecycle policy",
          "url": "https://docs.mistral.ai/inference/model-lifecycle"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前官方 Vals Index v2.2 页面未列出精确 alias；未从固定版搬移成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:53+08:00",
  "model_id": "mistral/mistral-medium-latest",
  "model_notes": [
    "Mistral 本地模型注释及官方 Vibe 文档均将 mistral-medium-latest 指向 Medium 3.5；官方生命周期政策说明 -latest 是可变 alias。没有把固定 Medium 3.5 的成绩迁移到此可变 alias。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
