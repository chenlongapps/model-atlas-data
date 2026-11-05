# Qwen-Image-2.1-Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen-image-2.1-pro
- 模型名称：Qwen-Image-2.1-Pro
- 发布日期：2026-10-02
- 最近检查时间：2026-11-04T05:04+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T05:04+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T05:04+08:00 |
| terminal-bench-v4 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [Terminal-Bench 4.0 announcement](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench run guide](https://www.tbench.ai/run) | 2026-11-04T05:04+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T05:04+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench) | 2026-11-04T05:04+08:00 |
| osworld-v2.1 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld v2.1 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T05:04+08:00 |
| chartography | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography protocol paper](https://arxiv.org/html/2608.10677) | 2026-11-04T05:04+08:00 |
| humanitys-last-exam | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T05:04+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T05:04+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [GDPval-AA V2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T05:04+08:00 |
| vals-index-v2.2 | 不适用 | — | [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro), [Vals Index V2.2 methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T05:04+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 需要输出代码 patch 并由隔离 verifier 检查；Qwen-Image-2.1-Pro 只输出图像。

最近核验时间：2026-11-04T05:04+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- SWE-bench Pro V2 要求 agent 生成 git diff/patch 并通过测试；本模型是图像生成接口，不输出代码。

最近核验时间：2026-11-04T05:04+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [Terminal-Bench 4.0 announcement](https://www.tbench.ai/news/terminal-bench-4-0)
- [Terminal-Bench run guide](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench 4 通过 Harbor 在沙箱运行终端 agent 并验证结果；本模型不提供终端动作或代码输出。

最近核验时间：2026-11-04T05:04+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science 要执行科学工作流并交付可复现检查的代码、分析、模拟或数据产物；本模型只输出图像。

最近核验时间：2026-11-04T05:04+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 要求工具调用完成多应用工作流并按最终环境状态评分；本模型不支持 function calling 且只输出图像。

最近核验时间：2026-11-04T05:04+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld v2.1 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 需要桌面 GUI 动作和文本/结构化操作结果。即便模型能接收图像，它也只输出生成图像，不支持工具调用，不能独立完成该协议。

最近核验时间：2026-11-04T05:04+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography protocol paper](https://arxiv.org/html/2608.10677)

研究备注：
- Chartography 需要接收图表图像并以自由文本回答；本模型虽支持图像输入，但输出是图像而非可评分答案文本。

最近核验时间：2026-11-04T05:04+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- HLE 需要对问题给出可评分的答案文本，题集还包含图像题；本模型只生成图像，不能完成答案输出协议。

最近核验时间：2026-11-04T05:04+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis Intelligence Index V5 汇总通用知识、编码、科学和知识工作等文字/代码任务；图像生成输出不符合完整指数的响应协议。

最近核验时间：2026-11-04T05:04+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [GDPval-AA V2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA V2.1 要求 Stirrup agent loop、shell/web 操作，并交付文档、幻灯片、图表或表格等工作成果；本模型不支持工具且输出仅为图像。

最近核验时间：2026-11-04T05:04+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Model Studio model page](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro)
- [Vals Index V2.2 methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index V2.2 汇总 finance、coding、legal、tax 的 agentic 工作流，包含终端、表格、代码与研究产物；本模型无工具调用且不能输出文本成果。

最近核验时间：2026-11-04T05:04+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 汇总通用知识、编码、科学和知识工作等文字/代码任务；图像生成输出不符合完整指数的响应协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 要求工具调用完成多应用工作流并按最终环境状态评分；本模型不支持 function calling 且只输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography protocol paper",
          "url": "https://arxiv.org/html/2608.10677"
        }
      ],
      "notes": [
        "Chartography 需要接收图表图像并以自由文本回答；本模型虽支持图像输入，但输出是图像而非可评分答案文本。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 需要输出代码 patch 并由隔离 verifier 检查；Qwen-Image-2.1-Pro 只输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "GDPval-AA V2.1 methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA V2.1 要求 Stirrup agent loop、shell/web 操作，并交付文档、幻灯片、图表或表格等工作成果；本模型不支持工具且输出仅为图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "HLE official leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "HLE 需要对问题给出可评分的答案文本，题集还包含图像题；本模型只生成图像，不能完成答案输出协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld v2.1 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 需要桌面 GUI 动作和文本/结构化操作结果。即便模型能接收图像，它也只输出生成图像，不支持工具调用，不能独立完成该协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 agent 生成 git diff/patch 并通过测试；本模型是图像生成接口，不输出代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "Terminal-Bench Science 0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要执行科学工作流并交付可复现检查的代码、分析、模拟或数据产物；本模型只输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "Terminal-Bench 4.0 announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Terminal-Bench run guide",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench 4 通过 Harbor 在沙箱运行终端 agent 并验证结果；本模型不提供终端动作或代码输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:04+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Model Studio model page",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen-image-2-1-pro"
        },
        {
          "label": "Vals Index V2.2 methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index V2.2 汇总 finance、coding、legal、tax 的 agentic 工作流，包含终端、表格、代码与研究产物；本模型无工具调用且不能输出文本成果。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:04+08:00",
  "model_id": "alibaba/qwen-image-2.1-pro",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
