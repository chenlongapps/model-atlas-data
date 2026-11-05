# Nemotron VoiceChat Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-voicechat
- 模型名称：Nemotron VoiceChat
- 发布日期：2026-03-16
- 最近检查时间：2026-11-05T11:33+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- NVIDIA 官方卡识别为 Nemotron 3 VoiceChat v1.0（12B），输入文本提示/音频，输出文本/音频/转写；本地 TOML 的视觉模型描述及 tools=true 未由该卡确认。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) | 2026-11-05T11:33+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T11:33+08:00 |
| terminal-bench-v4 | 待核实 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.tbench.ai/](https://www.tbench.ai/) | 2026-11-05T11:33+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement) | 2026-11-05T11:33+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://zapier.com/benchmarks](https://zapier.com/benchmarks) | 2026-11-05T11:33+08:00 |
| osworld-v2.1 | 不适用 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T11:33+08:00 |
| chartography | 不适用 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T11:33+08:00 |
| humanitys-last-exam | 不适用 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://lastexam.ai/](https://lastexam.ai/) | 2026-11-05T11:33+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T11:33+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T11:33+08:00 |
| vals-index-v2.2 | 不适用 | — | [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard), [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T11:33+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)

研究备注：
- NVIDIA v1.0 VoiceChat 是语音对话模型；仓库 TOML 仍标示 tools=true，但官方模型卡未明确确认该精确 API 可调用外部工具。榜单动态数据不完整，未确认成绩。

尚未解决的问题：
- 工具接口差异未解决，且未确认 DeepSWE v1.1 精确结果。

最近核验时间：2026-11-05T11:33+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 检查 Scale Pro V2 榜单和 NVIDIA VoiceChat 模型卡；没有核实该精确型号的目标分数。

尚未解决的问题：
- 本地工具能力与官方卡未能一致核实。

最近核验时间：2026-11-05T11:33+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.tbench.ai/](https://www.tbench.ai/)

研究备注：
- 官方模型卡将该版本定位为语音助手，未给出 TB4 结果；结果页当前不可读取。

尚未解决的问题：
- 工具执行能力及精确 TB4 结果均待核实。

最近核验时间：2026-11-05T11:33+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement)

研究备注：
- NVIDIA 模型卡未给出 Science 0.1 成绩；Harbor 动态榜单本次未加载。

尚未解决的问题：
- 工具执行能力及榜单结果待核实。

最近核验时间：2026-11-05T11:33+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

研究备注：
- NVIDIA v1.0 模型卡定位为语音对话，未列 function/tool calling API；仓库模型 TOML 标示 tools=true，因此不据未列举直接判不适用。Zapier 榜单折叠其余条目，未确认精确成绩。

尚未解决的问题：
- 需核实 tools=true 对应的精确模型 API 能力及完整榜单行。

最近核验时间：2026-11-05T11:33+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- 官方模型卡输入为文本提示/用户语音，不含屏幕图像输入或桌面操作接口，无法完成 OSWorld GUI 任务。

最近核验时间：2026-11-05T11:33+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 官方模型卡没有图像输入；语音对话模型不适用于图表图像理解。

最近核验时间：2026-11-05T11:33+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://lastexam.ai/](https://lastexam.ai/)

研究备注：
- 官方模型卡是语音对话模型，接受文本/音频且输出文本/音频；HLE 原始测试含多模态学术题，模型无图像输入，不能覆盖目标测试集。

最近核验时间：2026-11-05T11:33+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA V5 是知识工作、编码、科学与通识综合评测，不是语音识别/合成/对话测试；VoiceChat 官方用途为全双工语音交互。

最近核验时间：2026-11-05T11:33+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 需要 shell/web agent loop 及专业工作成果；官方 VoiceChat 模型卡定位为语音助手，没有声明此类工作流。

最近核验时间：2026-11-05T11:33+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard](https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard)
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 针对财务、编码、法律和税务代理工作；官方 VoiceChat 模型卡定位为语音交互，不是该类工作产品基准。

最近核验时间：2026-11-05T11:33+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA V5 是知识工作、编码、科学与通识综合评测，不是语音识别/合成/对话测试；VoiceChat 官方用途为全双工语音交互。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "NVIDIA v1.0 模型卡定位为语音对话，未列 function/tool calling API；仓库模型 TOML 标示 tools=true，因此不据未列举直接判不适用。Zapier 榜单折叠其余条目，未确认精确成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实 tools=true 对应的精确模型 API 能力及完整榜单行。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "官方模型卡没有图像输入；语音对话模型不适用于图表图像理解。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        }
      ],
      "notes": [
        "NVIDIA v1.0 VoiceChat 是语音对话模型；仓库 TOML 仍标示 tools=true，但官方模型卡未明确确认该精确 API 可调用外部工具。榜单动态数据不完整，未确认成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "工具接口差异未解决，且未确认 DeepSWE v1.1 精确结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 需要 shell/web agent loop 及专业工作成果；官方 VoiceChat 模型卡定位为语音助手，没有声明此类工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "官方模型卡是语音对话模型，接受文本/音频且输出文本/音频；HLE 原始测试含多模态学术题，模型无图像输入，不能覆盖目标测试集。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "官方模型卡输入为文本提示/用户语音，不含屏幕图像输入或桌面操作接口，无法完成 OSWorld GUI 任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "检查 Scale Pro V2 榜单和 NVIDIA VoiceChat 模型卡；没有核实该精确型号的目标分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地工具能力与官方卡未能一致核实。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "NVIDIA 模型卡未给出 Science 0.1 成绩；Harbor 动态榜单本次未加载。"
      ],
      "status": "待核实",
      "unresolved": [
        "工具执行能力及榜单结果待核实。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://www.tbench.ai/"
        }
      ],
      "notes": [
        "官方模型卡将该版本定位为语音助手，未给出 TB4 结果；结果页当前不可读取。"
      ],
      "status": "待核实",
      "unresolved": [
        "工具执行能力及精确 TB4 结果均待核实。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 针对财务、编码、法律和税务代理工作；官方 VoiceChat 模型卡定位为语音交互，不是该类工作产品基准。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:33+08:00",
  "model_id": "nvidia/nemotron-voicechat",
  "model_notes": [
    "NVIDIA 官方卡识别为 Nemotron 3 VoiceChat v1.0（12B），输入文本提示/音频，输出文本/音频/转写；本地 TOML 的视觉模型描述及 tools=true 未由该卡确认。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
