# Rune 26B-A4B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：surogate/rune-26b-a4b
- 模型名称：Rune 26B-A4B
- 发布日期：2026-09-21
- 最近检查时间：2026-11-04T09:16+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [DeepSWE benchmark protocol](https://huggingface.co/datasets/datacurve/deep-swe) | 2026-11-04T09:16+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [SWE-bench Pro V2 official board](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T09:16+08:00 |
| terminal-bench-v4 | 不适用 | — | [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune), [Terminal-Bench 4.0 version and protocol](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T09:16+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune), [Terminal-Bench Science official protocol](https://www.terminal-bench-science.ai/announcement) | 2026-11-04T09:16+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune), [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks) | 2026-11-04T09:16+08:00 |
| osworld-v2.1 | 不适用 | — | [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune), [OSWorld-V2 official README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md) | 2026-11-04T09:16+08:00 |
| chartography | 不适用 | — | [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune), [Rune model card and Surogate vision notes](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [Surge Chartography leaderboard and protocol](https://github.com/surge-ai/chartography) | 2026-11-04T09:16+08:00 |
| humanitys-last-exam | 不适用 | — | [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [Humanity’s Last Exam original paper and dataset protocol](https://arxiv.org/abs/2501.14249) | 2026-11-04T09:16+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T09:16+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [GDPval-AA v2.1 official evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T09:16+08:00 |
| vals-index-v2.2 | 不适用 | — | [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T09:16+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [DeepSWE benchmark protocol](https://huggingface.co/datasets/datacurve/deep-swe)

研究备注：
- 不适用：DeepSWE 需要编码代理提交可运行的软件修改；Rune 的托管接口只返回结构化决策概率，不能生成代码补丁。

最近核验时间：2026-11-04T09:16+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [SWE-bench Pro V2 official board](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：SWE-bench Pro V2 按代码补丁解决软件问题评分；Rune 的决策输出接口不能生成补丁。

最近核验时间：2026-11-04T09:16+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune)
- [Terminal-Bench 4.0 version and protocol](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 不适用：Terminal-Bench 4.0 要求代理在终端环境中执行任务；托管接口不能生成终端命令或调用工具。

最近核验时间：2026-11-04T09:16+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune)
- [Terminal-Bench Science official protocol](https://www.terminal-bench-science.ai/announcement)

研究备注：
- 不适用：Terminal-Bench Science 需要科学工作流、代码执行和结果文件；Rune 无工具调用且不生成可提交的工作产物。

最近核验时间：2026-11-04T09:16+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune)
- [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks)

研究备注：
- 不适用：AutomationBench 评测跨应用工具工作流及其最终状态；Rune 仅返回 typed decision，不支持 function calling。

最近核验时间：2026-11-04T09:16+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune)
- [OSWorld-V2 official README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)

研究备注：
- 不适用：OSWorld v2.1 需要桌面环境中的视觉观察与动作执行；本地记录的 Fireworks 接口是 text-only 且无 function calling。HF 权重在 Surogate vision serving 下的视觉能力不代表该托管接口。

最近核验时间：2026-11-04T09:16+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Fireworks Rune serving interface](https://fireworks.ai/models/fireworks/rune)
- [Rune model card and Surogate vision notes](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [Surge Chartography leaderboard and protocol](https://github.com/surge-ai/chartography)

研究备注：
- 不适用：Chartography 要输入图表图像并返回可与答案比较的数值/文字答案。Rune 托管接口不接收图像且只输出 decision 概率，不符合该接口；HF 卡在 Surogate --vision 下的权重能力不适用于 Fireworks endpoint。

最近核验时间：2026-11-04T09:16+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [Humanity’s Last Exam original paper and dataset protocol](https://arxiv.org/abs/2501.14249)

研究备注：
- 不适用：原始 HLE 包含 multiple-choice 与 short-answer 题；Rune 可表达 choices，但不能生成多数 exact-match 短答案，无法得到全套 HLE 有效成绩。Decision Index 或部分选择题结果不能映射为 HLE。

最近核验时间：2026-11-04T09:16+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 不适用：AA Index V5 是包含知识工作、编码、科学与工具类评测的综合指数；decision-only 输出和无工具接口无法完成该整项综合评测。Rune 的 Decision Index 分数是另一项指数，不能移用。

最近核验时间：2026-11-04T09:16+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [GDPval-AA v2.1 official evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 不适用：GDPval-AA v2.1 需要使用 shell 与网页工具完成工作任务并产出办公交付物；Rune 不能调用工具或生成这些文件。

最近核验时间：2026-11-04T09:16+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Rune model card](https://huggingface.co/surogate/rune-26b-a4b-GGUF)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：Vals Index 评估财务、编码、法律和税务领域的 agentic 工作；Rune 的 typed decision 输出和无工具接口不能执行这些任务。

最近核验时间：2026-11-04T09:16+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Rune model card",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "不适用：AA Index V5 是包含知识工作、编码、科学与工具类评测的综合指数；decision-only 输出和无工具接口无法完成该整项综合评测。Rune 的 Decision Index 分数是另一项指数，不能移用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Rune serving interface",
          "url": "https://fireworks.ai/models/fireworks/rune"
        },
        {
          "label": "Zapier AutomationBench leaderboard and protocol",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "不适用：AutomationBench 评测跨应用工具工作流及其最终状态；Rune 仅返回 typed decision，不支持 function calling。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Rune serving interface",
          "url": "https://fireworks.ai/models/fireworks/rune"
        },
        {
          "label": "Rune model card and Surogate vision notes",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "Surge Chartography leaderboard and protocol",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "不适用：Chartography 要输入图表图像并返回可与答案比较的数值/文字答案。Rune 托管接口不接收图像且只输出 decision 概率，不符合该接口；HF 卡在 Surogate --vision 下的权重能力不适用于 Fireworks endpoint。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Rune model card",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "DeepSWE benchmark protocol",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe"
        }
      ],
      "notes": [
        "不适用：DeepSWE 需要编码代理提交可运行的软件修改；Rune 的托管接口只返回结构化决策概率，不能生成代码补丁。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Rune model card",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "GDPval-AA v2.1 official evaluation and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "不适用：GDPval-AA v2.1 需要使用 shell 与网页工具完成工作任务并产出办公交付物；Rune 不能调用工具或生成这些文件。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Rune model card",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "Humanity’s Last Exam original paper and dataset protocol",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "不适用：原始 HLE 包含 multiple-choice 与 short-answer 题；Rune 可表达 choices，但不能生成多数 exact-match 短答案，无法得到全套 HLE 有效成绩。Decision Index 或部分选择题结果不能映射为 HLE。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Rune serving interface",
          "url": "https://fireworks.ai/models/fireworks/rune"
        },
        {
          "label": "OSWorld-V2 official README",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        }
      ],
      "notes": [
        "不适用：OSWorld v2.1 需要桌面环境中的视觉观察与动作执行；本地记录的 Fireworks 接口是 text-only 且无 function calling。HF 权重在 Surogate vision serving 下的视觉能力不代表该托管接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Rune model card",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "SWE-bench Pro V2 official board",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "不适用：SWE-bench Pro V2 按代码补丁解决软件问题评分；Rune 的决策输出接口不能生成补丁。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Rune serving interface",
          "url": "https://fireworks.ai/models/fireworks/rune"
        },
        {
          "label": "Terminal-Bench Science official protocol",
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "不适用：Terminal-Bench Science 需要科学工作流、代码执行和结果文件；Rune 无工具调用且不生成可提交的工作产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Rune serving interface",
          "url": "https://fireworks.ai/models/fireworks/rune"
        },
        {
          "label": "Terminal-Bench 4.0 version and protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "不适用：Terminal-Bench 4.0 要求代理在终端环境中执行任务；托管接口不能生成终端命令或调用工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T09:16+08:00",
      "checked_sources": [
        {
          "label": "Rune model card",
          "url": "https://huggingface.co/surogate/rune-26b-a4b-GGUF"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：Vals Index 评估财务、编码、法律和税务领域的 agentic 工作；Rune 的 typed decision 输出和无工具接口不能执行这些任务。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T09:16+08:00",
  "model_id": "surogate/rune-26b-a4b",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
