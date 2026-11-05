# Universal-3.5 Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：assemblyai/universal-3-5-pro
- 模型名称：Universal-3.5 Pro
- 发布日期：2026-06-15
- 最近检查时间：2026-11-05T02:43+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方模型文档确认 universal-3-5-pro 是预录音频转写型号（音频输入、文本输出），不支持目标 Benchmark 所需的编码/工具/图像接口。来源：https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro；https://www.assemblyai.com/docs/api-reference/transcripts/submit
- 发布日期需复核：仓库注释将 Realtime 首发记作 2026-06-15、异步版记作 2026-07-06；当前官方 changelog 页面显示 Realtime 项为 2026-06-23，Async 项为 2026-07-06。保留 TOML 中的 release_date=2026-06-15，不根据不同变体推断或改写。来源：https://www.assemblyai.com/changelog?3b7e7275_page=3

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T02:43+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T02:43+08:00 |
| terminal-bench-v4 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?efforts=all&version=4.0) | 2026-11-05T02:43+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T02:43+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05T02:43+08:00 |
| osworld-v2.1 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T02:43+08:00 |
| chartography | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Chartography benchmark page](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T02:43+08:00 |
| humanitys-last-exam | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-05T02:43+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [AssemblyAI benchmark page](https://www.assemblyai.com/benchmarks) | 2026-11-05T02:43+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T02:43+08:00 |
| vals-index-v2.2 | 不适用 | — | [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro), [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T02:43+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Official docs define universal-3-5-pro as a speech transcription model (audio input, text transcript output), not a coding agent.

最近核验时间：2026-11-05T02:43+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- The official interface transcribes audio and does not produce repository code patches.

最近核验时间：2026-11-05T02:43+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?efforts=all&version=4.0)

研究备注：
- The official interface transcribes audio and does not operate a terminal or execute tool actions.

最近核验时间：2026-11-05T02:43+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- The official interface is speech-to-text, not a scientific terminal or coding agent.

最近核验时间：2026-11-05T02:43+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- The transcription API does not expose the tool-using application workflow actions required by AutomationBench.

最近核验时间：2026-11-05T02:43+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- The documented model accepts audio and returns text; it has no screenshot observation or computer-use action interface.

最近核验时间：2026-11-05T02:43+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Chartography benchmark page](https://surgehq.ai/benchmarks/chartography)

研究备注：
- The documented model accepts audio, not chart images, and performs transcription rather than chart question answering.

最近核验时间：2026-11-05T02:43+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- The model transcribes speech into text; it is not an answer-generating interface for HLE questions.

最近核验时间：2026-11-05T02:43+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [AssemblyAI benchmark page](https://www.assemblyai.com/benchmarks)

研究备注：
- The documented model is a speech recognition/transcription product, not a general-purpose reasoning model assessed by this index.

最近核验时间：2026-11-05T02:43+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The transcription interface does not perform agentic work tasks or create the deliverables evaluated by GDPval-AA.

最近核验时间：2026-11-05T02:43+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [AssemblyAI Universal-3.5 Pro documentation](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro)
- [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The model transcribes speech and does not perform the finance, coding, legal, or tax agent tasks assessed by Vals Index.

最近核验时间：2026-11-05T02:43+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "AssemblyAI benchmark page",
          "url": "https://www.assemblyai.com/benchmarks"
        }
      ],
      "notes": [
        "The documented model is a speech recognition/transcription product, not a general-purpose reasoning model assessed by this index."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "The transcription API does not expose the tool-using application workflow actions required by AutomationBench."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Chartography benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "The documented model accepts audio, not chart images, and performs transcription rather than chart question answering."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Official docs define universal-3-5-pro as a speech transcription model (audio input, text transcript output), not a coding agent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The transcription interface does not perform agentic work tasks or create the deliverables evaluated by GDPval-AA."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Scale HLE leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "The model transcribes speech into text; it is not an answer-generating interface for HLE questions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "OSWorld v2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "The documented model accepts audio and returns text; it has no screenshot observation or computer-use action interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "The official interface transcribes audio and does not produce repository code patches."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "The official interface is speech-to-text, not a scientific terminal or coding agent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        }
      ],
      "notes": [
        "The official interface transcribes audio and does not operate a terminal or execute tool actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:43+08:00",
      "checked_sources": [
        {
          "label": "AssemblyAI Universal-3.5 Pro documentation",
          "url": "https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro"
        },
        {
          "label": "Vals Index v2.2 benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The model transcribes speech and does not perform the finance, coding, legal, or tax agent tasks assessed by Vals Index."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:43+08:00",
  "model_id": "assemblyai/universal-3-5-pro",
  "model_notes": [
    "官方模型文档确认 universal-3-5-pro 是预录音频转写型号（音频输入、文本输出），不支持目标 Benchmark 所需的编码/工具/图像接口。来源：https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro；https://www.assemblyai.com/docs/api-reference/transcripts/submit",
    "发布日期需复核：仓库注释将 Realtime 首发记作 2026-06-15、异步版记作 2026-07-06；当前官方 changelog 页面显示 Realtime 项为 2026-06-23，Async 项为 2026-07-06。保留 TOML 中的 release_date=2026-06-15，不根据不同变体推断或改写。来源：https://www.assemblyai.com/changelog?3b7e7275_page=3"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
