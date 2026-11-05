# MiniCPM5-1B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openbmb/minicpm5-1b
- 模型名称：MiniCPM5-1B
- 发布日期：2026-05-19
- 最近检查时间：2026-11-05T05:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 模型身份为 OpenBMB MiniCPM5-1B，发布日期 2026-05-19；模型卡将输入和输出均标为文本。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B) | 2026-11-05T05:58+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B) | 2026-11-05T05:58+08:00 |
| terminal-bench-v4 | 未找到 | — | [AA MiniCPM5-1B page](https://artificialanalysis.ai/models/minicpm5-1b), [AA Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T05:58+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [AA MiniCPM5-1B comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-luna-vs-minicpm5-1b), [AA Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T05:58+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier leaderboard](https://zapier.com/benchmarks), [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B) | 2026-11-05T05:58+08:00 |
| osworld-v2.1 | 不适用 | — | [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T05:58+08:00 |
| chartography | 不适用 | — | [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B), [Surge Chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T05:58+08:00 |
| humanitys-last-exam | 未找到 | — | [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B), [AA HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [AA MiniCPM5-1B page](https://artificialanalysis.ai/models/minicpm5-1b), [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B), [AA GDPval methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T05:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)

研究备注：
- 当前 v1.1 榜单显示 21/28 个模型，未见 MiniCPM5-1B；模型卡无该分数。

尚未解决的问题：
- 榜单可见列表不完整，无法确认未展示型号是否已评测。

最近核验时间：2026-11-05T05:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)

研究备注：
- Scale V2 当前展示结果未列 MiniCPM5-1B；模型卡无目标分数。

尚未解决的问题：
- 未能确认是否存在未公开或未展示结果。

最近核验时间：2026-11-05T05:58+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [AA MiniCPM5-1B page](https://artificialanalysis.ai/models/minicpm5-1b)
- [AA Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 未找到 MiniCPM5-1B 的 Terminal-Bench 4.0 公开分数。

最近核验时间：2026-11-05T05:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [AA MiniCPM5-1B comparison](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-luna-vs-minicpm5-1b)
- [AA Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 比较资料对 MiniCPM5-1B 及其 non-reasoning 变体显示无目标分数。

最近核验时间：2026-11-05T05:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier leaderboard](https://zapier.com/benchmarks)
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)

研究备注：
- 该模型支持工具调用；官方榜单部分结果折叠，未能查看完整型号列表。

尚未解决的问题：
- 无法确认该型号是否位于未展开结果中。

最近核验时间：2026-11-05T05:58+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型卡将输入/输出定义为文本；模型不具备处理桌面画面的视觉输入模态。

最近核验时间：2026-11-05T05:58+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)
- [Surge Chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型只接收文本，不能输入 Chartography 所需的图表图像。

最近核验时间：2026-11-05T05:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)
- [AA HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 官方模型资料与 AA 公开资料中未找到该精确型号 HLE 成绩。

最近核验时间：2026-11-05T05:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [AA MiniCPM5-1B page](https://artificialanalysis.ai/models/minicpm5-1b)
- [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前精确型号资料没有提供可录入的 V5 Index 分数；不使用旧版或估算分数。

最近核验时间：2026-11-05T05:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [MiniCPM5-1B model card](https://huggingface.co/openbmb/MiniCPM5-1B)
- [AA GDPval methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 未找到该精确型号的 GDPval-AA v2.1 公开 Elo 成绩。

最近核验时间：2026-11-05T05:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查官方 V2.2 榜单，未发现 MiniCPM5-1B 精确型号。

最近核验时间：2026-11-05T05:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA MiniCPM5-1B page",
          "url": "https://artificialanalysis.ai/models/minicpm5-1b"
        },
        {
          "label": "AA Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前精确型号资料没有提供可录入的 V5 Index 分数；不使用旧版或估算分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Zapier leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        }
      ],
      "notes": [
        "该模型支持工具调用；官方榜单部分结果折叠，未能查看完整型号列表。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法确认该型号是否位于未展开结果中。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        },
        {
          "label": "Surge Chartography",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型只接收文本，不能输入 Chartography 所需的图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        }
      ],
      "notes": [
        "当前 v1.1 榜单显示 21/28 个模型，未见 MiniCPM5-1B；模型卡无该分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单可见列表不完整，无法确认未展示型号是否已评测。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        },
        {
          "label": "AA GDPval methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "未找到该精确型号的 GDPval-AA v2.1 公开 Elo 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        },
        {
          "label": "AA HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "官方模型资料与 AA 公开资料中未找到该精确型号 HLE 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型卡将输入/输出定义为文本；模型不具备处理桌面画面的视觉输入模态。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "MiniCPM5-1B model card",
          "url": "https://huggingface.co/openbmb/MiniCPM5-1B"
        }
      ],
      "notes": [
        "Scale V2 当前展示结果未列 MiniCPM5-1B；模型卡无目标分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能确认是否存在未公开或未展示结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA MiniCPM5-1B comparison",
          "url": "https://artificialanalysis.ai/models/releases/comparisons/gpt-6-luna-vs-minicpm5-1b"
        },
        {
          "label": "AA Terminal-Bench-Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 比较资料对 MiniCPM5-1B 及其 non-reasoning 变体显示无目标分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA MiniCPM5-1B page",
          "url": "https://artificialanalysis.ai/models/minicpm5-1b"
        },
        {
          "label": "AA Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "未找到 MiniCPM5-1B 的 Terminal-Bench 4.0 公开分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "检查官方 V2.2 榜单，未发现 MiniCPM5-1B 精确型号。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T05:58+08:00",
  "model_id": "openbmb/minicpm5-1b",
  "model_notes": [
    "模型身份为 OpenBMB MiniCPM5-1B，发布日期 2026-05-19；模型卡将输入和输出均标为文本。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
