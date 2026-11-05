# MiniMax-M2.7-highspeed Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：minimax/MiniMax-M2.7-highspeed
- 模型名称：MiniMax-M2.7-highspeed
- 发布日期：2026-03-18
- 最近检查时间：2026-11-05T11:03+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地模型是 2026-03-18 发布的文本输入/输出推理模型，支持工具调用。
- MiniMax 官方称 M2.7-highspeed 与 M2.7 的测试结果相同且速度更快，但没有为本组目标 Benchmark 公布 highspeed 的独立结果与配置；未将基座型号成绩复制过来。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) | 2026-11-05T11:03+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27) | 2026-11-05T11:03+08:00 |
| terminal-bench-v4 | 待核实 | — | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27) | 2026-11-05T11:03+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://snorkel.ai/leaderboard/terminal-bench-science/](https://snorkel.ai/leaderboard/terminal-bench-science/), [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks) | 2026-11-05T11:03+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27) | 2026-11-05T11:03+08:00 |
| osworld-v2.1 | 不适用 | — | [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7), [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T11:03+08:00 |
| chartography | 不适用 | — | [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7), [https://surgehq.ai/benchmarks](https://surgehq.ai/benchmarks) | 2026-11-05T11:03+08:00 |
| humanitys-last-exam | 待核实 | — | [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27), [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T11:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/minimax-m2-7](https://artificialanalysis.ai/models/minimax-m2-7) | 2026-11-05T11:03+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27), [https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know](https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T11:03+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27) | 2026-11-05T11:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)

研究备注：
- 当前公开榜单展示 21/28 个模型；未在可见行中确认 M2.7-highspeed，不能据不完整展示断言未评测。

尚未解决的问题：
- 需检查完整 v1.1 配置中的 exact model ID。

最近核验时间：2026-11-05T11:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)

研究备注：
- 当前动态榜单可见结果未确认 highspeed；官方旧 SWE-Pro 成绩早于 2026-09-22 的 V2 split，且未说明目标版本下的 highspeed 独立配置。

尚未解决的问题：
- 需确认该精确型号是否进入完整 Pro V2 结果。

最近核验时间：2026-11-05T11:03+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)

研究备注：
- Terminal-Bench 4.0 于 2026-08-28 发布；已查材料中的 M2.7 Terminal Bench 2 成绩不属于 V4，也没有 highspeed 的目标版本分数。

尚未解决的问题：
- 需确认 V4 精确型号结果。

最近核验时间：2026-11-05T11:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://snorkel.ai/leaderboard/terminal-bench-science/](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)

研究备注：
- 当前可见榜单未确认 M2.7-highspeed 的 Science v0.1 成绩；没有将基座或其他 Terminal-Bench 版本移用。

尚未解决的问题：
- 需复核完整 Science 榜单。

最近核验时间：2026-11-05T11:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)

研究备注：
- 模型支持工具调用，适用性成立；AutomationBench v1.0.6 当前可见榜单折叠其余 119 项，不能确定精确 highspeed 行。

尚未解决的问题：
- 需检查折叠的剩余模型结果。

最近核验时间：2026-11-05T11:03+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- 模型仅支持文本输入，无法接收桌面截图；未把通用工具能力等同于视觉桌面操作能力。

最近核验时间：2026-11-05T11:03+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
- [https://surgehq.ai/benchmarks](https://surgehq.ai/benchmarks)

研究备注：
- 模型仅支持文本输入，不能读取 Chartography 所需的图表图像。

最近核验时间：2026-11-05T11:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)
- [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 官方说明 M2.7 与 highspeed API 结果相同，但没有将 HLE 的具体样本、推理配置或评测行标为 highspeed；不将 M2.7 报告的 HLE 28.0 复制到此变体。

尚未解决的问题：
- 需要 highspeed 精确型号的 HLE 评测记录或明确测试身份。

最近核验时间：2026-11-05T11:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/minimax-m2-7](https://artificialanalysis.ai/models/minimax-m2-7)

研究备注：
- 未找到 M2.7-highspeed 的独立 AA V5 型号页或结果。M2.7 页面为 V5 N/A；官方的通用结果相同声明不足以证明 highspeed 的 V5 评测结果。

最近核验时间：2026-11-05T11:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)
- [https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know](https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 没有 highspeed 的目标 v2.1 Elo 行。基座资料的 1494/1495 数值不一致且未明确版本；官方“结果相同”说明不足以核实该具体评测身份。

尚未解决的问题：
- 需确认 highspeed 是否以目标 v2.1 配置单独测得分数；基座结果冲突未解。

最近核验时间：2026-11-05T11:03+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)

研究备注：
- 当前 v2.2 页面只展示各实验室最佳模型，未见 highspeed；官方结果相同声明未给出其 Vals v2.2 独立成绩。

尚未解决的问题：
- 未确认 highspeed 在 Vals Index v2.2 下的精确结果。

最近核验时间：2026-11-05T11:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/minimax-m2-7"
        }
      ],
      "notes": [
        "未找到 M2.7-highspeed 的独立 AA V5 型号页或结果。M2.7 页面为 V5 N/A；官方的通用结果相同声明不足以证明 highspeed 的 V5 评测结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://www.minimax.io/models/text/m27"
        }
      ],
      "notes": [
        "模型支持工具调用，适用性成立；AutomationBench v1.0.6 当前可见榜单折叠其余 119 项，不能确定精确 highspeed 行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查折叠的剩余模型结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M2.7"
        },
        {
          "url": "https://surgehq.ai/benchmarks"
        }
      ],
      "notes": [
        "模型仅支持文本输入，不能读取 Chartography 所需的图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        }
      ],
      "notes": [
        "当前公开榜单展示 21/28 个模型；未在可见行中确认 M2.7-highspeed，不能据不完整展示断言未评测。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整 v1.1 配置中的 exact model ID。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://www.minimax.io/models/text/m27"
        },
        {
          "url": "https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "没有 highspeed 的目标 v2.1 Elo 行。基座资料的 1494/1495 数值不一致且未明确版本；官方“结果相同”说明不足以核实该具体评测身份。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 highspeed 是否以目标 v2.1 配置单独测得分数；基座结果冲突未解。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://www.minimax.io/models/text/m27"
        },
        {
          "url": "https://arxiv.org/html/2605.26494"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "官方说明 M2.7 与 highspeed API 结果相同，但没有将 HLE 的具体样本、推理配置或评测行标为 highspeed；不将 M2.7 报告的 HLE 28.0 复制到此变体。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要 highspeed 精确型号的 HLE 评测记录或明确测试身份。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M2.7"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "模型仅支持文本输入，无法接收桌面截图；未把通用工具能力等同于视觉桌面操作能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://www.minimax.io/models/text/m27"
        }
      ],
      "notes": [
        "当前动态榜单可见结果未确认 highspeed；官方旧 SWE-Pro 成绩早于 2026-09-22 的 V2 split，且未说明目标版本下的 highspeed 独立配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认该精确型号是否进入完整 Pro V2 结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "当前可见榜单未确认 M2.7-highspeed 的 Science v0.1 成绩；没有将基座或其他 Terminal-Bench 版本移用。"
      ],
      "status": "待核实",
      "unresolved": [
        "需复核完整 Science 榜单。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://www.minimax.io/models/text/m27"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 于 2026-08-28 发布；已查材料中的 M2.7 Terminal Bench 2 成绩不属于 V4，也没有 highspeed 的目标版本分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 V4 精确型号结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:03+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.minimax.io/models/text/m27"
        }
      ],
      "notes": [
        "当前 v2.2 页面只展示各实验室最佳模型，未见 highspeed；官方结果相同声明未给出其 Vals v2.2 独立成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认 highspeed 在 Vals Index v2.2 下的精确结果。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:03+08:00",
  "model_id": "minimax/MiniMax-M2.7-highspeed",
  "model_notes": [
    "本地模型是 2026-03-18 发布的文本输入/输出推理模型，支持工具调用。",
    "MiniMax 官方称 M2.7-highspeed 与 M2.7 的测试结果相同且速度更快，但没有为本组目标 Benchmark 公布 highspeed 的独立结果与配置；未将基座型号成绩复制过来。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
