# Mercury Decide Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inception/mercury-decide
- 模型名称：Mercury Decide
- 发布日期：2026-09-30
- 最近检查时间：2026-11-04T05:35+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T05:35+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T05:35+08:00 |
| terminal-bench-v4 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [Terminal-Bench run guide](https://www.tbench.ai/run) | 2026-11-04T05:35+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T05:35+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [AutomationBench official protocol/leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T05:35+08:00 |
| osworld-v2.1 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T05:35+08:00 |
| chartography | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and protocol](https://arxiv.org/html/2608.10677) | 2026-11-04T05:35+08:00 |
| humanitys-last-exam | 待核实 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [Scale original HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis HLE-MultiChoice evaluation](https://artificialanalysis.ai/evaluations/hle-multichoice), [Artificial Analysis Decision Index methodology](https://artificialanalysis.ai/methodology/decision-index), [Artificial Analysis Mercury Decide page](https://artificialanalysis.ai/decision-models/mercury-decide) | 2026-11-04T05:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Decision Index methodology](https://artificialanalysis.ai/methodology/decision-index) | 2026-11-04T05:35+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T05:35+08:00 |
| vals-index-v2.2 | 不适用 | — | [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions), [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T05:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 要求提交并验证代码补丁；Mercury Decide 输出受限的结构化决策，不生成代码。

最近核验时间：2026-11-04T05:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- SWE-bench Pro V2 要求 agent 修改代码仓库、生成 diff 并在独立环境验证；Mercury Decide 没有代码输出或工具执行接口。

最近核验时间：2026-11-04T05:35+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [Terminal-Bench run guide](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench 4 通过 Harbor 在沙箱终端运行 agent；Mercury Decide 不支持工具调用或终端任务执行。

最近核验时间：2026-11-04T05:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science 要求 agent 执行科研终端流程并产出可测试工件；Mercury Decide 没有终端/文件操作接口。

最近核验时间：2026-11-04T05:35+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [AutomationBench official protocol/leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 按端到端工具工作流最终状态评分；Mercury Decide 不支持工具调用。由外部控制器使用模型决策得到的成绩属于整个代理系统，不能单独归属该模型。

最近核验时间：2026-11-04T05:35+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld 2.1 要求代理观察 GUI 并执行操作。Mercury Decide 可接收截图并选择预设选项，但没有 GUI 操作或工具调用接口；包装后的系统成绩不能单独归属此模型。

最近核验时间：2026-11-04T05:35+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and protocol](https://arxiv.org/html/2608.10677)

研究备注：
- Chartography 要求根据图表图像生成自由文本答案；Mercury Decide 仅返回预定义类型的结构化决策，不符合文本答案输出协议。

最近核验时间：2026-11-04T05:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [Scale original HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis HLE-MultiChoice evaluation](https://artificialanalysis.ai/evaluations/hle-multichoice)
- [Artificial Analysis Decision Index methodology](https://artificialanalysis.ai/methodology/decision-index)
- [Artificial Analysis Mercury Decide page](https://artificialanalysis.ai/decision-models/mercury-decide)

研究备注：
- 完整 HLE 定义是 2,500 题；Mercury Decide 的 choice 输出可适配 AA 所测的 HLE-MultiChoice 子集（513 道纯文本多选题），但这不是完整 HLE 分数。AA 官方静态页面确认子集与 accuracy 指标，却未展示该模型的精确数值；在核实数值与测试条件前不写入成绩。AA Decision Index 综合分 53 是另一项指标，不能代替 HLE。

尚未解决的问题：
- 需从 Artificial Analysis 官方 HLE-MultiChoice 页面取得 Mercury Decide 的精确 accuracy 与可核实测试条件；当前公开页面文本未显示该数值。

最近核验时间：2026-11-04T05:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Decision Index methodology](https://artificialanalysis.ai/methodology/decision-index)

研究备注：
- Intelligence Index V5 包含 HLE-Diamond、知识工作、编码、终端和科研 agent 任务。Mercury Decide 无自由文本与工具调用能力；其 AA Decision Index 53 属于单独指数，未映射为 Intelligence Index V5。

最近核验时间：2026-11-04T05:35+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA V2.1 要求 agent 使用 shell 和网页浏览，并交付专业工作成果；Mercury Decide 不支持工具调用或自由文本生成。

最近核验时间：2026-11-04T05:35+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Inception Decisions API documentation](https://docs.inceptionlabs.ai/capabilities/decisions)
- [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index V2.2 评测 finance、coding、legal、tax agentic 任务；Mercury Decide 没有工具调用/自由工作产物输出。个别 LegalBench 或其他决策评测结果不是此 Vals Index。

最近核验时间：2026-11-04T05:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Decision Index methodology",
          "url": "https://artificialanalysis.ai/methodology/decision-index"
        }
      ],
      "notes": [
        "Intelligence Index V5 包含 HLE-Diamond、知识工作、编码、终端和科研 agent 任务。Mercury Decide 无自由文本与工具调用能力；其 AA Decision Index 53 属于单独指数，未映射为 Intelligence Index V5。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "AutomationBench official protocol/leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 按端到端工具工作流最终状态评分；Mercury Decide 不支持工具调用。由外部控制器使用模型决策得到的成绩属于整个代理系统，不能单独归属该模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper and protocol",
          "url": "https://arxiv.org/html/2608.10677"
        }
      ],
      "notes": [
        "Chartography 要求根据图表图像生成自由文本答案；Mercury Decide 仅返回预定义类型的结构化决策，不符合文本答案输出协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 要求提交并验证代码补丁；Mercury Decide 输出受限的结构化决策，不生成代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA V2.1 要求 agent 使用 shell 和网页浏览，并交付专业工作成果；Mercury Decide 不支持工具调用或自由文本生成。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "Scale original HLE leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis HLE-MultiChoice evaluation",
          "url": "https://artificialanalysis.ai/evaluations/hle-multichoice"
        },
        {
          "label": "Artificial Analysis Decision Index methodology",
          "url": "https://artificialanalysis.ai/methodology/decision-index"
        },
        {
          "label": "Artificial Analysis Mercury Decide page",
          "url": "https://artificialanalysis.ai/decision-models/mercury-decide"
        }
      ],
      "notes": [
        "完整 HLE 定义是 2,500 题；Mercury Decide 的 choice 输出可适配 AA 所测的 HLE-MultiChoice 子集（513 道纯文本多选题），但这不是完整 HLE 分数。AA 官方静态页面确认子集与 accuracy 指标，却未展示该模型的精确数值；在核实数值与测试条件前不写入成绩。AA Decision Index 综合分 53 是另一项指标，不能代替 HLE。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从 Artificial Analysis 官方 HLE-MultiChoice 页面取得 Mercury Decide 的精确 accuracy 与可核实测试条件；当前公开页面文本未显示该数值。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "OSWorld V2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld 2.1 要求代理观察 GUI 并执行操作。Mercury Decide 可接收截图并选择预设选项，但没有 GUI 操作或工具调用接口；包装后的系统成绩不能单独归属此模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 agent 修改代码仓库、生成 diff 并在独立环境验证；Mercury Decide 没有代码输出或工具执行接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "Terminal-Bench Science 0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要求 agent 执行科研终端流程并产出可测试工件；Mercury Decide 没有终端/文件操作接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "Terminal-Bench run guide",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench 4 通过 Harbor 在沙箱终端运行 agent；Mercury Decide 不支持工具调用或终端任务执行。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:35+08:00",
      "checked_sources": [
        {
          "label": "Inception Decisions API documentation",
          "url": "https://docs.inceptionlabs.ai/capabilities/decisions"
        },
        {
          "label": "Vals Index V2.2 official methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index V2.2 评测 finance、coding、legal、tax agentic 任务；Mercury Decide 没有工具调用/自由工作产物输出。个别 LegalBench 或其他决策评测结果不是此 Vals Index。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:35+08:00",
  "model_id": "inception/mercury-decide",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
