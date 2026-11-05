# MAI-Voice-2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：microsoft/mai-voice-2
- 模型名称：MAI-Voice-2
- 发布日期：2026-06-02
- 最近检查时间：2026-11-05T04:25+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Microsoft 官方发布资料确认 MAI-Voice-2 是文字转语音模型；未将后续 MAI-Voice-2.1 型号或其成绩映射到当前精确版本。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T04:25+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Scale SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T04:25+08:00 |
| terminal-bench-v4 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all) | 2026-11-05T04:25+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T04:25+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T04:25+08:00 |
| osworld-v2.1 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T04:25+08:00 |
| chartography | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T04:25+08:00 |
| humanitys-last-exam | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Humanity's Last Exam official site](https://lastexam.ai/) | 2026-11-05T04:25+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Artificial Analysis Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:25+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T04:25+08:00 |
| vals-index-v2.2 | 不适用 | — | [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/), [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T04:25+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 该精确型号是文字转语音模型，不提供代码代理能力。

最近核验时间：2026-11-05T04:25+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Scale SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 软件仓库修复代理评测不适用于文字转语音模型。

最近核验时间：2026-11-05T04:25+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)

研究备注：
- 终端任务要求代码执行能力；该型号将文本转换为语音。

最近核验时间：2026-11-05T04:25+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 科学终端工作流需要代码/终端代理，该型号是 TTS。

最近核验时间：2026-11-05T04:25+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- 该型号没有工具调用或跨应用工作流执行能力。

最近核验时间：2026-11-05T04:25+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 该型号输入文本、输出音频，没有桌面屏幕观察或 GUI 操作能力。

最近核验时间：2026-11-05T04:25+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 该型号不接收图表图像，也不以文本回答图表理解问题。

最近核验时间：2026-11-05T04:25+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Humanity's Last Exam official site](https://lastexam.ai/)

研究备注：
- HLE 需要学术问答文本输出；该型号输出语音音频。

最近核验时间：2026-11-05T04:25+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Artificial Analysis Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA Index 综合评估语言模型能力；文字转语音功能不能映射为该指数分数。

最近核验时间：2026-11-05T04:25+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求使用工具完成专业工作并交付文件；该型号无代理或工具能力。

最近核验时间：2026-11-05T04:25+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Voice-2 official announcement](https://microsoft.ai/news/mai-voice-2/)
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 测量跨行业 agent 表现，不适用于 TTS 语音合成模型。

最近核验时间：2026-11-05T04:25+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Artificial Analysis Index v5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA Index 综合评估语言模型能力；文字转语音功能不能映射为该指数分数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "该型号没有工具调用或跨应用工作流执行能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "该型号不接收图表图像，也不以文本回答图表理解问题。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "该精确型号是文字转语音模型，不提供代码代理能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "GDPval-AA v2.1 official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求使用工具完成专业工作并交付文件；该型号无代理或工具能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Humanity's Last Exam official site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "HLE 需要学术问答文本输出；该型号输出语音音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "该型号输入文本、输出音频，没有桌面屏幕观察或 GUI 操作能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Scale SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "软件仓库修复代理评测不适用于文字转语音模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "科学终端工作流需要代码/终端代理，该型号是 TTS。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        }
      ],
      "notes": [
        "终端任务要求代码执行能力；该型号将文本转换为语音。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:25+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Voice-2 official announcement",
          "url": "https://microsoft.ai/news/mai-voice-2/"
        },
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 测量跨行业 agent 表现，不适用于 TTS 语音合成模型。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:25+08:00",
  "model_id": "microsoft/mai-voice-2",
  "model_notes": [
    "Microsoft 官方发布资料确认 MAI-Voice-2 是文字转语音模型；未将后续 MAI-Voice-2.1 型号或其成绩映射到当前精确版本。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
