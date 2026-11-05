# Nemotron 3 Nano Omni 30B A3B Reasoning Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
- 模型名称：Nemotron 3 Nano Omni 30B A3B Reasoning
- 发布日期：2026-04-28
- 最近检查时间：2026-11-05T06:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- NVIDIA 官方卡确认此精确产品名为 Nemotron 3 Nano Omni 30B A3B Reasoning。AA GDPval 榜单列出的结果仅记录为 v2.1 GDPval-AA；NVIDIA 报告中旧版 OSWorld 结果不计入 OSWorld v2.1。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:53+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:53+08:00 |
| terminal-bench-v4 | 待核实 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5) | 2026-11-05T06:53+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4) | 2026-11-05T06:53+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T06:53+08:00 |
| osworld-v2.1 | 未找到 | — | [NVIDIA Nemotron 3 Nano Omni BF16 model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16), [NVIDIA Nemotron 3 Omni technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf), [OSWorld V2 official repository and releases](https://github.com/xlang-ai/OSWorld-V2/releases) | 2026-11-05T06:53+08:00 |
| chartography | 未找到 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:53+08:00 |
| humanitys-last-exam | 未找到 | — | [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard), [NVIDIA Nemotron 3 Omni technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf), [Humanity’s Last Exam official evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Nemotron 3 Nano Omni model page](https://artificialanalysis.ai/models/nemotron-3-nano-omni-30b-a3b), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:53+08:00 |
| gdpval-aa-v2.1 | 已收录 | 237 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 major industries; harness=Stirrup) | [GDPval-AA v2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:53+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 榜单当前仅展示部分模型/配置，未见 Nemotron 精确行。

尚未解决的问题：
- 需检查榜单折叠配置以确认是否有此模型。

最近核验时间：2026-11-05T06:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 当前公开 SWE-bench Pro V2 榜单未见精确模型行。

最近核验时间：2026-11-05T06:53+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Artificial Analysis Mistral Medium 3.5 / Step 5 comparison](https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5)

研究备注：
- AA 当前 Terminal-Bench 4 榜单只显示 28/240 models；未见此 exact checkpoint。

尚未解决的问题：
- 需检查完整 AA 榜单是否有该模型行。

最近核验时间：2026-11-05T06:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison](https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4)

研究备注：
- AA 当前 Science 榜单只显示 28/120 models；未见此 exact checkpoint。

尚未解决的问题：
- 需检查完整 AA 榜单是否有该模型行。

最近核验时间：2026-11-05T06:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- Zapier 当前榜单除可见前 10 条外还有 119 条折叠，无法确认 Nemotron 精确项。

尚未解决的问题：
- 需检查折叠记录。

最近核验时间：2026-11-05T06:53+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni BF16 model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)
- [NVIDIA Nemotron 3 Omni technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf)
- [OSWorld V2 official repository and releases](https://github.com/xlang-ai/OSWorld-V2/releases)

研究备注：
- NVIDIA 技术报告列有旧版 OSWorld 47.4，但没有 OSWorld v2.1 条件；该报告早于 V2.1 发布，故不映射为 v2.1 成绩。

最近核验时间：2026-11-05T06:53+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 当前 Chartography 榜单未见该精确型号；没有映射其他 Nemotron 版本或 ChartQA/CharXiv。

最近核验时间：2026-11-05T06:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [NVIDIA Nemotron 3 Nano Omni model card](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard)
- [NVIDIA Nemotron 3 Omni technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf)
- [Humanity’s Last Exam official evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- NVIDIA 官方报告及当前 HLE 资料未见 Nemotron 3 Nano Omni 30B A3B Reasoning 精确型号的原始 HLE 成绩。

最近核验时间：2026-11-05T06:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Nemotron 3 Nano Omni model page](https://artificialanalysis.ai/models/nemotron-3-nano-omni-30b-a3b)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前精确型号页面显示 Intelligence Index 为 N/A/unknown；没有可写入的 v5 分数。

最近核验时间：2026-11-05T06:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 237
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 major industries
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [GDPval-AA v2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA v2.1 当前榜单直接列出 Nemotron 3 Nano Omni 30B A3B Reasoning：237 Elo，CI −24/+24。榜单 Release Date 列为 Apr 2026，属于模型发布日期，不作为成绩 date。

最近核验时间：2026-11-05T06:53+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 当前榜单未列出该精确型号；相近 Nemotron 模型未作映射。

最近核验时间：2026-11-05T06:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Nemotron 3 Nano Omni model page",
          "url": "https://artificialanalysis.ai/models/nemotron-3-nano-omni-30b-a3b"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前精确型号页面显示 Intelligence Index 为 N/A/unknown；没有可写入的 v5 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Zapier 当前榜单除可见前 10 条外还有 119 条折叠，无法确认 Nemotron 精确项。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查折叠记录。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "当前 Chartography 榜单未见该精确型号；没有映射其他 Nemotron 版本或 ChartQA/CharXiv。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 榜单当前仅展示部分模型/配置，未见 Nemotron 精确行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查榜单折叠配置以确认是否有此模型。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 official leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA v2.1 当前榜单直接列出 Nemotron 3 Nano Omni 30B A3B Reasoning：237 Elo，CI −24/+24。榜单 Release Date 列为 Apr 2026，属于模型发布日期，不作为成绩 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "NVIDIA Nemotron 3 Omni technical report",
          "url": "https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf"
        },
        {
          "label": "Humanity’s Last Exam official evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "NVIDIA 官方报告及当前 HLE 资料未见 Nemotron 3 Nano Omni 30B A3B Reasoning 精确型号的原始 HLE 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni BF16 model card",
          "url": "https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16"
        },
        {
          "label": "NVIDIA Nemotron 3 Omni technical report",
          "url": "https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Omni-report.pdf"
        },
        {
          "label": "OSWorld V2 official repository and releases",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        }
      ],
      "notes": [
        "NVIDIA 技术报告列有旧版 OSWorld 47.4，但没有 OSWorld v2.1 条件；该报告早于 V2.1 发布，故不映射为 v2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "当前公开 SWE-bench Pro V2 榜单未见精确模型行。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "Terminal-Bench Science 0.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Mistral Small 4 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/mistral-medium-3-5-vs-mistral-small-4"
        }
      ],
      "notes": [
        "AA 当前 Science 榜单只显示 28/120 models；未见此 exact checkpoint。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整 AA 榜单是否有该模型行。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Nano Omni model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning/modelcard"
        },
        {
          "label": "Terminal-Bench 4.0 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Artificial Analysis Mistral Medium 3.5 / Step 5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-5-vs-mistral-medium-3-5"
        }
      ],
      "notes": [
        "AA 当前 Terminal-Bench 4 榜单只显示 28/240 models；未见此 exact checkpoint。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整 AA 榜单是否有该模型行。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:53+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 当前榜单未列出该精确型号；相近 Nemotron 模型未作映射。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:53+08:00",
  "model_id": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
  "model_notes": [
    "NVIDIA 官方卡确认此精确产品名为 Nemotron 3 Nano Omni 30B A3B Reasoning。AA GDPval 榜单列出的结果仅记录为 v2.1 GDPval-AA；NVIDIA 报告中旧版 OSWorld 结果不计入 OSWorld v2.1。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
