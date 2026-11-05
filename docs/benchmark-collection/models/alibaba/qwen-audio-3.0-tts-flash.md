# Qwen-Audio-3.0-TTS Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen-audio-3.0-tts-flash
- 模型名称：Qwen-Audio-3.0-TTS Flash
- 发布日期：2026-07-14
- 最近检查时间：2026-11-05T01:47+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 发布日期 2026-07-14 依据阿里云 Model Studio lifecycle 中该精确 API ID 的条目；7 月 21 日的社区博客是后续产品介绍。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T01:47+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T01:47+08:00 |
| terminal-bench-v4 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T01:47+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T01:47+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [AutomationBench](https://zapier.com/benchmarks) | 2026-11-05T01:47+08:00 |
| osworld-v2.1 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [OSWorld V2.1 guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T01:47+08:00 |
| chartography | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [Chartography benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T01:47+08:00 |
| humanitys-last-exam | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T01:47+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T01:47+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T01:47+08:00 |
| vals-index-v2.2 | 不适用 | — | [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash), [Vals Index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T01:47+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [AutomationBench](https://zapier.com/benchmarks)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [OSWorld V2.1 guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [Chartography benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [Humanity’s Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Qwen Audio TTS Flash model specification](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash)
- [Vals Index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。

最近核验时间：2026-11-05T01:47+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "AutomationBench",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "DeepSWE v1.1",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "Humanity’s Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "OSWorld V2.1 guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "Terminal-Bench Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T01:47+08:00",
      "checked_sources": [
        {
          "label": "Qwen Audio TTS Flash model specification",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-audio-3-0-tts-flash"
        },
        {
          "label": "Vals Index",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "模型为文本输入、音频输出的 TTS 服务，官方规格不支持 function calling；不能输出这些任务要求的代码、代理操作或文本评测答案。无相应公开分数，按模型能力记为不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T01:47+08:00",
  "model_id": "alibaba/qwen-audio-3.0-tts-flash",
  "model_notes": [
    "发布日期 2026-07-14 依据阿里云 Model Studio lifecycle 中该精确 API ID 的条目；7 月 21 日的社区博客是后续产品介绍。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
