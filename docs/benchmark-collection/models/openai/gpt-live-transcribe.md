# GPT-Live-Transcribe Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-live-transcribe
- 模型名称：GPT-Live-Transcribe
- 发布日期：2026-07-28
- 最近检查时间：2026-11-04T21:43+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- OpenAI 官方文档确认 gpt-live-transcribe 是实时语音转文字端点，只接收音频并输出转写文本；不支持图像、视频或函数调用。模型文件也标记 tools.supported=false、reasoning.supported=false。
- 11 项目标均要求代码/终端代理、GUI/视觉理解、通用学术推理或专业工作生成，均不适用于该专用转录端点；没有把其他 GPT 型号成绩映射给它。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [DeepSWE v1.1 官方说明](https://deepswe.datacurve.ai/) | 2026-11-04T21:43+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Scale AI SWE-bench Pro V2 官方方法](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T21:43+08:00 |
| terminal-bench-v4 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Terminal-Bench 官方说明](https://www.tbench.ai/) | 2026-11-04T21:43+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Terminal-Bench-Science 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T21:43+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Zapier AutomationBench 官方方法](https://zapier.com/benchmarks) | 2026-11-04T21:43+08:00 |
| osworld-v2.1 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T21:43+08:00 |
| chartography | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Surge AI Chartography 官方说明](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T21:43+08:00 |
| humanitys-last-exam | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Artificial Analysis HLE 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T21:43+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Artificial Analysis Intelligence Index 官方页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T21:43+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T21:43+08:00 |
| vals-index-v2.2 | 不适用 | — | [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe), [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription), [Vals AI Vals Index 2.2 官方说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:43+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [DeepSWE v1.1 官方说明](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 评测长程代码代理；本端点只输入音频并输出转写文本，不执行代码代理任务。

最近核验时间：2026-11-04T21:43+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Scale AI SWE-bench Pro V2 官方方法](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 该评测要求代码代理提交并验证代码补丁；本端点不生成通用代码补丁，也不支持函数调用。

最近核验时间：2026-11-04T21:43+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Terminal-Bench 官方说明](https://www.tbench.ai/)

研究备注：
- 该评测要求代理在沙箱终端完成任务；本端点不支持工具调用，仅作实时语音转写。

最近核验时间：2026-11-04T21:43+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Terminal-Bench-Science 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 该评测要求代理执行科学终端工作流并产出可验证结果；本端点不具备此能力。

最近核验时间：2026-11-04T21:43+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Zapier AutomationBench 官方方法](https://zapier.com/benchmarks)

研究备注：
- 该评测要求 agent 在模拟业务应用中完成跨应用工作流；该端点不支持函数调用或通用任务推理。

最近核验时间：2026-11-04T21:43+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- 该评测要求 agent 理解桌面画面并执行 GUI 操作；本端点不支持图像输入或函数调用。

最近核验时间：2026-11-04T21:43+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Surge AI Chartography 官方说明](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 该评测要求读取图表图像并进行视觉推理；本端点不支持图像输入。

最近核验时间：2026-11-04T21:43+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Artificial Analysis HLE 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 要求回答学术问题；本端点的文本输出仅为音频转写结果，不是通用问答。

最近核验时间：2026-11-04T21:43+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Artificial Analysis Intelligence Index 官方页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 该综合指数覆盖知识工作、编码、科学和通识能力；本端点用途限于实时语音转写。

最近核验时间：2026-11-04T21:43+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求 agent 完成专业工作并产出交付物；本端点不支持函数调用或通用生成。

最近核验时间：2026-11-04T21:43+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [OpenAI GPT-Live-Transcribe 官方模型文档](https://developers.openai.com/api/docs/models/gpt-live-transcribe)
- [OpenAI Realtime 转录指南](https://developers.openai.com/api/docs/guides/realtime-transcription)
- [Vals AI Vals Index 2.2 官方说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 该指数衡量金融、编码、法律和税务任务中的 agent 能力，与专用转录端点不匹配。

最近核验时间：2026-11-04T21:43+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Artificial Analysis Intelligence Index 官方页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "该综合指数覆盖知识工作、编码、科学和通识能力；本端点用途限于实时语音转写。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Zapier AutomationBench 官方方法",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "该评测要求 agent 在模拟业务应用中完成跨应用工作流；该端点不支持函数调用或通用任务推理。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Surge AI Chartography 官方说明",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "该评测要求读取图表图像并进行视觉推理；本端点不支持图像输入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "DeepSWE v1.1 官方说明",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 评测长程代码代理；本端点只输入音频并输出转写文本，不执行代码代理任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Artificial Analysis GDPval-AA 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求 agent 完成专业工作并产出交付物；本端点不支持函数调用或通用生成。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Artificial Analysis HLE 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 要求回答学术问题；本端点的文本输出仅为音频转写结果，不是通用问答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "OSWorld V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "该评测要求 agent 理解桌面画面并执行 GUI 操作；本端点不支持图像输入或函数调用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方方法",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "该评测要求代码代理提交并验证代码补丁；本端点不生成通用代码补丁，也不支持函数调用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Terminal-Bench-Science 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "该评测要求代理执行科学终端工作流并产出可验证结果；本端点不具备此能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Terminal-Bench 官方说明",
          "url": "https://www.tbench.ai/"
        }
      ],
      "notes": [
        "该评测要求代理在沙箱终端完成任务；本端点不支持工具调用，仅作实时语音转写。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:43+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Live-Transcribe 官方模型文档",
          "url": "https://developers.openai.com/api/docs/models/gpt-live-transcribe"
        },
        {
          "label": "OpenAI Realtime 转录指南",
          "url": "https://developers.openai.com/api/docs/guides/realtime-transcription"
        },
        {
          "label": "Vals AI Vals Index 2.2 官方说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "该指数衡量金融、编码、法律和税务任务中的 agent 能力，与专用转录端点不匹配。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:43+08:00",
  "model_id": "openai/gpt-live-transcribe",
  "model_notes": [
    "OpenAI 官方文档确认 gpt-live-transcribe 是实时语音转文字端点，只接收音频并输出转写文本；不支持图像、视频或函数调用。模型文件也标记 tools.supported=false、reasoning.supported=false。",
    "11 项目标均要求代码/终端代理、GUI/视觉理解、通用学术推理或专业工作生成，均不适用于该专用转录端点；没有把其他 GPT 型号成绩映射给它。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
