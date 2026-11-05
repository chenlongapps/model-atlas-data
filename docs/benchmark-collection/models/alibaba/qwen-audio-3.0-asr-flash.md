# Qwen-Audio-3.0-ASR Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen-audio-3.0-asr-flash
- 模型名称：Qwen-Audio-3.0-ASR Flash
- 发布日期：2026-06
- 最近检查时间：2026-11-05T04:50+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方产品页和语音识别文档将精确型号定义为 audio-to-text ASR：音频输入、文本转写输出；未依据云平台泛用说明推断该型号具备通用工具代理或图像/屏幕交互能力。
- 因此 11 项目标分别按目标任务类型标为不适用；没有把未找到成绩混作不适用，也未写入任何成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T04:50+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T04:50+08:00 |
| terminal-bench-v4 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [Terminal-Bench 4.0 page](https://www.tbench.ai/?version=4.0&efforts=all) | 2026-11-05T04:50+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [Terminal-Bench Science 0.1 page](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T04:50+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05T04:50+08:00 |
| osworld-v2.1 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T04:50+08:00 |
| chartography | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T04:50+08:00 |
| humanitys-last-exam | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [Humanity’s Last Exam site](https://lastexam.ai/) | 2026-11-05T04:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T04:50+08:00 |
| vals-index-v2.2 | 不适用 | — | [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash), [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T04:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- ASR 专用型号不执行软件仓库修复任务。

最近核验时间：2026-11-05T04:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- ASR 专用型号不执行软件仓库修复任务。

最近核验时间：2026-11-05T04:50+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [Terminal-Bench 4.0 page](https://www.tbench.ai/?version=4.0&efforts=all)

研究备注：
- ASR 专用型号不执行终端工作流任务。

最近核验时间：2026-11-05T04:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [Terminal-Bench Science 0.1 page](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- ASR 专用型号不执行终端科学研究工作流。

最近核验时间：2026-11-05T04:50+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- ASR 专用型号没有可核实的通用 SaaS 工具代理能力。

最近核验时间：2026-11-05T04:50+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型不接收屏幕/桌面视觉输入，也不输出 GUI 动作。

最近核验时间：2026-11-05T04:50+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型不接收图表图像输入；其音频转写用途与图表理解不符。

最近核验时间：2026-11-05T04:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [Humanity’s Last Exam site](https://lastexam.ai/)

研究备注：
- 精确型号仅将音频转成文字，不是通用学术问答模型。

最近核验时间：2026-11-05T04:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 专用 ASR 转写模型不覆盖该综合知识、编码、科学和推理能力评测。

最近核验时间：2026-11-05T04:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 专用 ASR 模型不具备职业代理任务所需的文件交付和工具工作流。

最近核验时间：2026-11-05T04:50+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Qwen-Audio-3.0-ASR Flash official model page](https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash)
- [Qwen speech-to-text official guide](https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 专用 ASR 模型不具备 Vals Index 的跨行业 agentic 任务能力。

最近核验时间：2026-11-05T04:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "AA Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "专用 ASR 转写模型不覆盖该综合知识、编码、科学和推理能力评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "ASR 专用型号没有可核实的通用 SaaS 工具代理能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型不接收图表图像输入；其音频转写用途与图表理解不符。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "ASR 专用型号不执行软件仓库修复任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "专用 ASR 模型不具备职业代理任务所需的文件交付和工具工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "Humanity’s Last Exam site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "精确型号仅将音频转成文字，不是通用学术问答模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型不接收屏幕/桌面视觉输入，也不输出 GUI 动作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "ASR 专用型号不执行软件仓库修复任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "Terminal-Bench Science 0.1 page",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "ASR 专用型号不执行终端科学研究工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "Terminal-Bench 4.0 page",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        }
      ],
      "notes": [
        "ASR 专用型号不执行终端工作流任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Qwen-Audio-3.0-ASR Flash official model page",
          "url": "https://www.qwencloud.com/models/qwen-audio-3.0-asr-flash"
        },
        {
          "label": "Qwen speech-to-text official guide",
          "url": "https://docs.qwencloud.com/developer-guides/speech/speech-to-text-models"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "专用 ASR 模型不具备 Vals Index 的跨行业 agentic 任务能力。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:50+08:00",
  "model_id": "alibaba/qwen-audio-3.0-asr-flash",
  "model_notes": [
    "官方产品页和语音识别文档将精确型号定义为 audio-to-text ASR：音频输入、文本转写输出；未依据云平台泛用说明推断该型号具备通用工具代理或图像/屏幕交互能力。",
    "因此 11 项目标分别按目标任务类型标为不适用；没有把未找到成绩混作不适用，也未写入任何成绩。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
