# MAI-Voice-2-Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：microsoft/mai-voice-2-flash
- 模型名称：MAI-Voice-2-Flash
- 发布日期：2026-07-23
- 最近检查时间：2026-11-04T22:16+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Microsoft 官方发布资料将 MAI-Voice-2-Flash 定位为低延迟语音生成模型；模型 TOML 标明文本输入、音频输出，并且不支持工具或推理能力。
- 微软在早期发布公告中未提供本轮 11 项目标 Benchmark 的成绩；语音延迟和产品指标不是目标 Benchmark。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE official leaderboard](https://deepswe.datacurve.ai/), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Scale AI SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| terminal-bench-v4 | 不适用 | — | [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Zapier AutomationBench leaderboard and methodology](https://zapier.com/benchmarks), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld V2.1 official project](https://osworld-v2.xlang.ai/), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography official description and leaderboard](https://surgehq.ai/benchmarks/chartography), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| humanitys-last-exam | 不适用 | — | [Humanity’s Last Exam official benchmark](https://lastexam.ai/), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) | 2026-11-04T22:16+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- DeepSWE 评估长程软件工程编码代理；该模型执行文本转语音，输出音频而非代码补丁。

最近核验时间：2026-11-04T22:16+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- SWE-bench Pro V2 评估代码库修复代理；该模型不输出文本或代码。

最近核验时间：2026-11-04T22:16+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- Terminal-Bench 4 评估沙箱终端代理；该模型不支持工具调用，输出为音频。

最近核验时间：2026-11-04T22:16+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- Terminal-Bench Science 评估终端科学研究工作流；该模型不支持工具调用且输出音频。

最近核验时间：2026-11-04T22:16+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Zapier AutomationBench leaderboard and methodology](https://zapier.com/benchmarks)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- AutomationBench 评估跨应用工具代理工作流；该模型不支持工具调用且输出音频。

最近核验时间：2026-11-04T22:16+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld V2.1 official project](https://osworld-v2.xlang.ai/)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- OSWorld 评估长流程桌面操作；该模型没有工具调用能力，输出为音频。

最近核验时间：2026-11-04T22:16+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography official description and leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- Chartography 需要图表视觉输入和多步推理答案；该模型只接收文本并输出音频。

最近核验时间：2026-11-04T22:16+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Humanity’s Last Exam official benchmark](https://lastexam.ai/)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- Humanity’s Last Exam 是学术问答与推理评测；该模型以语音生成代替文本回答。

最近核验时间：2026-11-04T22:16+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- Artificial Analysis Intelligence Index V5 汇总语言模型的通识、编码、科学和知识工作评测；语音生成模型不提供文本或推理结果。

最近核验时间：2026-11-04T22:16+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- GDPval-AA 需要通过 shell 和网页浏览完成专业工作产物；该模型不支持工具调用且只输出音频。

最近核验时间：2026-11-04T22:16+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Microsoft MAI-Voice-2-Flash release](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/)

研究备注：
- Vals Index 汇总金融、编码、法律及税务领域的代理任务；这些任务不适用于文本转语音模型。

最近核验时间：2026-11-04T22:16+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 汇总语言模型的通识、编码、科学和知识工作评测；语音生成模型不提供文本或推理结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard and methodology",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "AutomationBench 评估跨应用工具代理工作流；该模型不支持工具调用且输出音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography official description and leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "Chartography 需要图表视觉输入和多步推理答案；该模型只接收文本并输出音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "DeepSWE 评估长程软件工程编码代理；该模型执行文本转语音，输出音频而非代码补丁。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "GDPval-AA 需要通过 shell 和网页浏览完成专业工作产物；该模型不支持工具调用且只输出音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Humanity’s Last Exam official benchmark",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "Humanity’s Last Exam 是学术问答与推理评测；该模型以语音生成代替文本回答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 official project",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "OSWorld 评估长流程桌面操作；该模型没有工具调用能力，输出为音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评估代码库修复代理；该模型不输出文本或代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "Terminal-Bench Science 评估终端科学研究工作流；该模型不支持工具调用且输出音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "Terminal-Bench 4 评估沙箱终端代理；该模型不支持工具调用，输出为音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T22:16+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Microsoft MAI-Voice-2-Flash release",
          "url": "https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/"
        }
      ],
      "notes": [
        "Vals Index 汇总金融、编码、法律及税务领域的代理任务；这些任务不适用于文本转语音模型。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T22:16+08:00",
  "model_id": "microsoft/mai-voice-2-flash",
  "model_notes": [
    "Microsoft 官方发布资料将 MAI-Voice-2-Flash 定位为低延迟语音生成模型；模型 TOML 标明文本输入、音频输出，并且不支持工具或推理能力。",
    "微软在早期发布公告中未提供本轮 11 项目标 Benchmark 的成绩；语音延迟和产品指标不是目标 Benchmark。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
