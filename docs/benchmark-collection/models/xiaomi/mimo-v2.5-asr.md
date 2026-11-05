# MiMo-V2.5-ASR Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2.5-asr
- 模型名称：MiMo-V2.5-ASR
- 发布日期：2026-04-23
- 最近检查时间：2026-11-05T07:50+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地 release_date 为 2026-04-23；小米模型博客将 MiMo-V2.5-ASR 列于 2026 年 4 月，官方 API 发布记录另将 API ID mimo-v2.5-asr 标为 2026-06-02。此处保留本地队列日期，并记录 API 上线日期差异；没有把 API 日期当作模型文件发布日期。来源：https://mimo.xiaomi.com/mimo-v2-5-asr；https://mimo.mi.com/docs/en-US/updates/model

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://deepswe.datacurve.ai/) | 2026-11-05T07:50+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T07:50+08:00 |
| terminal-bench-v4 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T07:50+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T07:50+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://zapier.com/benchmarks) | 2026-11-05T07:50+08:00 |
| osworld-v2.1 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://osworld-v2.xlang.ai/) | 2026-11-05T07:50+08:00 |
| chartography | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T07:50+08:00 |
| humanitys-last-exam | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://lastexam.ai/) | 2026-11-05T07:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T07:50+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T07:50+08:00 |
| vals-index-v2.2 | 不适用 | — | [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition), [对应 Benchmark 官方资料](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T07:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://deepswe.datacurve.ai/)

研究备注：
- ASR 专用接口仅接收音频并输出转写文本，不接受代码任务文本，也不提供编码代理执行工具。

最近核验时间：2026-11-05T07:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 音频转写接口不具备在代码仓库中编辑和验证补丁的任务输入/输出能力。

最近核验时间：2026-11-05T07:50+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 模型不支持推理或工具，且输入/输出模态不适用于终端环境任务。

最近核验时间：2026-11-05T07:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- 科学终端工作流需要命令行操作和研究产物；该模型只做音频转写且不支持工具。

最近核验时间：2026-11-05T07:50+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://zapier.com/benchmarks)

研究备注：
- 模型无工具调用能力；音频转写输出不能执行多工具工作流。

最近核验时间：2026-11-05T07:50+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://osworld-v2.xlang.ai/)

研究备注：
- 只接收音频并输出文本，不能处理桌面截图或执行 GUI 操作。

最近核验时间：2026-11-05T07:50+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 不接收图表图像；产品任务是语音识别而非图表问答。

最近核验时间：2026-11-05T07:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://lastexam.ai/)

研究备注：
- HLE 是学术问答；该专用 ASR 接口不接收题目文本/图像并生成问答答案。

最近核验时间：2026-11-05T07:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 该综合指数评测知识工作、编码、科学和通识能力；专用 ASR 端点不具备对应交互形态。

最近核验时间：2026-11-05T07:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 评测要求代理完成职业任务并交付文件；音频转写接口不支持此工作流。

最近核验时间：2026-11-05T07:50+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [MiMo-V2.5-ASR 官方语音识别 API 文档](https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition)
- [对应 Benchmark 官方资料](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 该综合指数聚合金融、编码、法律和税务代理任务；专用 ASR 接口不支持这些工作流。

最近核验时间：2026-11-05T07:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "该综合指数评测知识工作、编码、科学和通识能力；专用 ASR 端点不具备对应交互形态。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "模型无工具调用能力；音频转写输出不能执行多工具工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "不接收图表图像；产品任务是语音识别而非图表问答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "ASR 专用接口仅接收音频并输出转写文本，不接受代码任务文本，也不提供编码代理执行工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "评测要求代理完成职业任务并交付文件；音频转写接口不支持此工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "HLE 是学术问答；该专用 ASR 接口不接收题目文本/图像并生成问答答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "只接收音频并输出文本，不能处理桌面截图或执行 GUI 操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "音频转写接口不具备在代码仓库中编辑和验证补丁的任务输入/输出能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "科学终端工作流需要命令行操作和研究产物；该模型只做音频转写且不支持工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "模型不支持推理或工具，且输入/输出模态不适用于终端环境任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:50+08:00",
      "checked_sources": [
        {
          "label": "MiMo-V2.5-ASR 官方语音识别 API 文档",
          "url": "https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition"
        },
        {
          "label": "对应 Benchmark 官方资料",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "该综合指数聚合金融、编码、法律和税务代理任务；专用 ASR 接口不支持这些工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:50+08:00",
  "model_id": "xiaomi/mimo-v2.5-asr",
  "model_notes": [
    "本地 release_date 为 2026-04-23；小米模型博客将 MiMo-V2.5-ASR 列于 2026 年 4 月，官方 API 发布记录另将 API ID mimo-v2.5-asr 标为 2026-06-02。此处保留本地队列日期，并记录 API 上线日期差异；没有把 API 日期当作模型文件发布日期。来源：https://mimo.xiaomi.com/mimo-v2-5-asr；https://mimo.mi.com/docs/en-US/updates/model"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
