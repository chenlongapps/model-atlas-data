# Seed Audio 1.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：bytedance-seed/seed-audio-1.0
- 模型名称：Seed Audio 1.0
- 发布日期：2026-07-20
- 最近检查时间：2026-11-04T23:19+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- ByteDance Seed 官方资料确认 Seed Audio 1.0 于 2026-07-20 发布，是文本提示到场景音频生成模型；本地能力标记为工具和推理均不支持。目标 11 项面向代码/终端 agent、桌面操作、图表视觉、学术问答或职业工作产出，均与此模型的输入输出和用途不匹配。
- 按明显不适用模型规则记录所有 11 项为不适用；未借用 Seed2.1、SeedRealtime 或其他 Seed 型号的成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [DeepSWE v1.1 benchmark](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T23:19+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [SWE-bench Pro V2 benchmark](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:19+08:00 |
| terminal-bench-v4 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Terminal-Bench 4.0 methodology](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T23:19+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Terminal-Bench-Science 0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T23:19+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [AutomationBench leaderboard and methodology](https://zapier.com/benchmarks) | 2026-11-04T23:19+08:00 |
| osworld-v2.1 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-04T23:19+08:00 |
| chartography | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T23:19+08:00 |
| humanitys-last-exam | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T23:19+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Artificial Analysis model overview](https://artificialanalysis.ai/models) | 2026-11-04T23:19+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T23:19+08:00 |
| vals-index-v2.2 | 不适用 | — | [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model), [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T23:19+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [DeepSWE v1.1 benchmark](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Seed Audio 1.0 输入文本并生成音频；DeepSWE 要求 coding agent 提交并验证软件补丁。该音频生成型号不适用于此项。

最近核验时间：2026-11-04T23:19+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [SWE-bench Pro V2 benchmark](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 评测 agent 在真实代码库解决软件问题；Seed Audio 1.0 生成音频，不执行代码任务。

最近核验时间：2026-11-04T23:19+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Terminal-Bench 4.0 methodology](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 要求 agent 在沙盒终端完成任务；Seed Audio 1.0 不支持工具调用且输出音频，不适用。

最近核验时间：2026-11-04T23:19+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Terminal-Bench-Science 0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench-Science 评测终端科学研究工作流并验证分析、模拟等任务产物；Seed Audio 1.0 是文本到音频生成模型，不适用。

最近核验时间：2026-11-04T23:19+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [AutomationBench leaderboard and methodology](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 要求 agent 使用业务应用工具完成工作流；Seed Audio 1.0 的工具能力标记为不支持，也没有公开业务流程执行配置，不适用。

最近核验时间：2026-11-04T23:19+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- OSWorld v2.1 评测 agent 操作桌面环境完成长流程；Seed Audio 1.0 不支持工具操作，且输出音频，不适用。

最近核验时间：2026-11-04T23:19+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 评估图表视觉理解；Seed Audio 1.0 仅接收文本并生成音频，没有图像输入能力，不适用。

最近核验时间：2026-11-04T23:19+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 是需要回答学术问题的知识与推理基准；Seed Audio 1.0 的官方评测面向音频生成，输出音频而非用于该基准的文本答案，不适用。

最近核验时间：2026-11-04T23:19+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Artificial Analysis model overview](https://artificialanalysis.ai/models)

研究备注：
- Artificial Analysis Intelligence Index 是通用模型综合指数，不是音频生成评测；Seed Audio 1.0 专用于音频创作，未找到可归属的 Index V5 成绩，不适用。

最近核验时间：2026-11-04T23:19+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 评测 agent 完成职业任务并产出文档等成果；Seed Audio 1.0 不提供文本/办公产物或工具执行能力，不适用。

最近核验时间：2026-11-04T23:19+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [ByteDance Seed Audio 1.0 release](https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model)
- [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 衡量金融、编程、法律和税务等 agent 任务；Seed Audio 1.0 是音频生成模型，与该指数任务类型不匹配，不适用。

最近核验时间：2026-11-04T23:19+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Artificial Analysis model overview",
          "url": "https://artificialanalysis.ai/models"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index 是通用模型综合指数，不是音频生成评测；Seed Audio 1.0 专用于音频创作，未找到可归属的 Index V5 成绩，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "AutomationBench leaderboard and methodology",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 要求 agent 使用业务应用工具完成工作流；Seed Audio 1.0 的工具能力标记为不支持，也没有公开业务流程执行配置，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Surge Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 评估图表视觉理解；Seed Audio 1.0 仅接收文本并生成音频，没有图像输入能力，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "DeepSWE v1.1 benchmark",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Seed Audio 1.0 输入文本并生成音频；DeepSWE 要求 coding agent 提交并验证软件补丁。该音频生成型号不适用于此项。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 评测 agent 完成职业任务并产出文档等成果；Seed Audio 1.0 不提供文本/办公产物或工具执行能力，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 是需要回答学术问题的知识与推理基准；Seed Audio 1.0 的官方评测面向音频生成，输出音频而非用于该基准的文本答案，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "OSWorld v2.1 评测 agent 操作桌面环境完成长流程；Seed Audio 1.0 不支持工具操作，且输出音频，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "SWE-bench Pro V2 benchmark",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评测 agent 在真实代码库解决软件问题；Seed Audio 1.0 生成音频，不执行代码任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Terminal-Bench-Science 0.1 release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 评测终端科学研究工作流并验证分析、模拟等任务产物；Seed Audio 1.0 是文本到音频生成模型，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Terminal-Bench 4.0 methodology",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 要求 agent 在沙盒终端完成任务；Seed Audio 1.0 不支持工具调用且输出音频，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:19+08:00",
      "checked_sources": [
        {
          "label": "ByteDance Seed Audio 1.0 release",
          "url": "https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model"
        },
        {
          "label": "Vals Index v2.2",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 衡量金融、编程、法律和税务等 agent 任务；Seed Audio 1.0 是音频生成模型，与该指数任务类型不匹配，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:19+08:00",
  "model_id": "bytedance-seed/seed-audio-1.0",
  "model_notes": [
    "ByteDance Seed 官方资料确认 Seed Audio 1.0 于 2026-07-20 发布，是文本提示到场景音频生成模型；本地能力标记为工具和推理均不支持。目标 11 项面向代码/终端 agent、桌面操作、图表视觉、学术问答或职业工作产出，均与此模型的输入输出和用途不匹配。",
    "按明显不适用模型规则记录所有 11 项为不适用；未借用 Seed2.1、SeedRealtime 或其他 Seed 型号的成绩。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
