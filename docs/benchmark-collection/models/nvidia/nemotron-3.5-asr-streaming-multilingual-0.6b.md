# Nemotron 3.5 ASR Streaming Multilingual 0.6B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b
- 模型名称：Nemotron 3.5 ASR Streaming Multilingual 0.6B
- 发布日期：2026-06-04
- 最近检查时间：2026-11-04T21:01+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- NVIDIA 的模型介绍于 2026-06-04 发布，称 Nemotron 3.5 ASR 是 600M 参数的流式多语言语音转文字模型；官方 NVIDIA FAQ 也明确记载其发布日期为 2026-06-04。仓库原日期 `2026-08` 已据此更正为 `2026-06-04`，队列会按新日期重新排序。精确 Hugging Face 模型卡 URL（https://huggingface.co/nvidia/Nemotron-3.5-ASR-Streaming-Multilingual-0.6b）返回 401，未尝试绕过；公开 NVIDIA/HF 介绍页为 https://huggingface.co/blog/nvidia/fine-tuning-nemotron-35-asr。模型 TOML 标注 audio 输入、text 输出且不支持 reasoning/tools。11 项目标均不适用于该 ASR 模型；未复用其他 Nemotron 型号成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE 官方榜单](https://deepswe.datacurve.ai/) | 2026-11-04T21:01+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro V2 官方仓库](https://github.com/scaleapi/SWE-bench_Pro-os) | 2026-11-04T21:01+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 官方 V4 页面](https://www.tbench.ai/?version=4), [Vals AI Terminal-Bench 4.0 榜单](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T21:01+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench-Science 官方榜单](https://www.terminal-bench-science.ai/) | 2026-11-04T21:01+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Zapier AutomationBench 官方榜单与说明](https://zapier.com/benchmarks) | 2026-11-04T21:01+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T21:01+08:00 |
| chartography | 不适用 | — | [Surge Chartography 官方榜单与说明](https://surgehq.ai/benchmarks/chartography), [Chartography 官方代码库](https://github.com/surge-ai/chartography) | 2026-11-04T21:01+08:00 |
| humanitys-last-exam | 不适用 | — | [Scale HLE 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T21:01+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index V5 官方发布说明](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5), [Artificial Analysis 官方榜单](https://artificialanalysis.ai/) | 2026-11-04T21:01+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA V2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T21:01+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals AI Vals Index 2.2 官方榜单与说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:01+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 评测长时程软件工程 agent。本模型是 600M 流式语音转文字模型，不具备代码生成或软件工程能力。

最近核验时间：2026-11-04T21:01+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro V2 官方仓库](https://github.com/scaleapi/SWE-bench_Pro-os)

研究备注：
- SWE-bench Pro V2 评测 agent 修复软件仓库问题并提交代码补丁的能力；ASR 转写模型不适合此任务。

最近核验时间：2026-11-04T21:01+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 官方 V4 页面](https://www.tbench.ai/?version=4)
- [Vals AI Terminal-Bench 4.0 榜单](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Terminal-Bench 4.0 评测 agent 完成终端任务的能力；该模型只执行语音转写，且模型 TOML 标注不支持 tools。

最近核验时间：2026-11-04T21:01+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench-Science 官方榜单](https://www.terminal-bench-science.ai/)

研究备注：
- Terminal-Bench-Science 评测科研工作流 agent；该模型是 ASR 转写模型，不具备科研推理、代码或工具执行能力。

最近核验时间：2026-11-04T21:01+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单与说明](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 评测跨工具完成业务工作流的 agent；该模型不支持 tools，只接收音频并输出转写文本。

最近核验时间：2026-11-04T21:01+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld 2.1 评测桌面与网页计算机操作 agent；语音转写模型没有视觉输入或计算机操作能力。

最近核验时间：2026-11-04T21:01+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography 官方榜单与说明](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方代码库](https://github.com/surge-ai/chartography)

研究备注：
- Chartography 评测专业图表的视觉感知与推理；本模型只接收音频输入，不支持图像输入。

最近核验时间：2026-11-04T21:01+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Scale HLE 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- Humanity’s Last Exam 评测学术知识与推理问题；ASR 模型只将语音转换为文本，不提供通用问题求解能力。

最近核验时间：2026-11-04T21:01+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5 官方发布说明](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)
- [Artificial Analysis 官方榜单](https://artificialanalysis.ai/)

研究备注：
- Artificial Analysis Intelligence Index V5 是通用模型能力综合评测，覆盖知识工作、编码、科学工作流与推理；单项 ASR 模型不适用。

最近核验时间：2026-11-04T21:01+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA V2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 需要模型在 agent 环境中完成跨行业工作任务并生成文档、表格等成品；该模型不执行通用推理或工具工作流。

最近核验时间：2026-11-04T21:01+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals AI Vals Index 2.2 官方榜单与说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 2.2 汇总模型在金融、编码、法律和税务 agent 任务中的表现；ASR 转写模型不适用于该综合评测。榜单中的其他 Nemotron 型号不是本模型。

最近核验时间：2026-11-04T21:01+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5 官方发布说明",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        },
        {
          "label": "Artificial Analysis 官方榜单",
          "url": "https://artificialanalysis.ai/"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 是通用模型能力综合评测，覆盖知识工作、编码、科学工作流与推理；单项 ASR 模型不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单与说明",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 评测跨工具完成业务工作流的 agent；该模型不支持 tools，只接收音频并输出转写文本。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单与说明",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方代码库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography 评测专业图表的视觉感知与推理；本模型只接收音频输入，不支持图像输入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 评测长时程软件工程 agent。本模型是 600M 流式语音转文字模型，不具备代码生成或软件工程能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA V2.1 官方榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 需要模型在 agent 环境中完成跨行业工作任务并生成文档、表格等成品；该模型不执行通用推理或工具工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Scale HLE 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "Humanity’s Last Exam 评测学术知识与推理问题；ASR 模型只将语音转换为文本，不提供通用问题求解能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld 2.1 评测桌面与网页计算机操作 agent；语音转写模型没有视觉输入或计算机操作能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro V2 官方仓库",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评测 agent 修复软件仓库问题并提交代码补丁的能力；ASR 转写模型不适合此任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench-Science 官方榜单",
          "url": "https://www.terminal-bench-science.ai/"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 评测科研工作流 agent；该模型是 ASR 转写模型，不具备科研推理、代码或工具执行能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 官方 V4 页面",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Vals AI Terminal-Bench 4.0 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 评测 agent 完成终端任务的能力；该模型只执行语音转写，且模型 TOML 标注不支持 tools。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:01+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index 2.2 官方榜单与说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 2.2 汇总模型在金融、编码、法律和税务 agent 任务中的表现；ASR 转写模型不适用于该综合评测。榜单中的其他 Nemotron 型号不是本模型。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:01+08:00",
  "model_id": "nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b",
  "model_notes": [
    "NVIDIA 的模型介绍于 2026-06-04 发布，称 Nemotron 3.5 ASR 是 600M 参数的流式多语言语音转文字模型；官方 NVIDIA FAQ 也明确记载其发布日期为 2026-06-04。仓库原日期 `2026-08` 已据此更正为 `2026-06-04`，队列会按新日期重新排序。精确 Hugging Face 模型卡 URL（https://huggingface.co/nvidia/Nemotron-3.5-ASR-Streaming-Multilingual-0.6b）返回 401，未尝试绕过；公开 NVIDIA/HF 介绍页为 https://huggingface.co/blog/nvidia/fine-tuning-nemotron-35-asr。模型 TOML 标注 audio 输入、text 输出且不支持 reasoning/tools。11 项目标均不适用于该 ASR 模型；未复用其他 Nemotron 型号成绩。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
