# Sage 1.4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：levanto/levanto-sage-v1.4
- 模型名称：Sage 1.4
- 发布日期：2026-10-04
- 最近检查时间：2026-11-04T04:53+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Sage 1.4 official model page](https://levanto.ai/model) | 2026-11-04T04:53+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [SWE-bench Pro dataset and protocol](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [Sage 1.4 official model page](https://levanto.ai/model) | 2026-11-04T04:53+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 4 announcement](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench run guide](https://www.tbench.ai/run), [Sage 1.4 official model page](https://levanto.ai/model) | 2026-11-04T04:53+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench Science 0.1 announcement](https://www.tbench.ai/news/terminal-bench-science-0-1), [Sage 1.4 official model page](https://levanto.ai/model) | 2026-11-04T04:53+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench), [Sage documentation](https://docs.levanto.ai/) | 2026-11-04T04:53+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld v2.1 official site](https://osworld-v2.xlang.ai/), [Sage documentation](https://docs.levanto.ai/) | 2026-11-04T04:53+08:00 |
| chartography | 不适用 | — | [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography protocol paper](https://arxiv.org/html/2608.10677), [Sage 1.4 official benchmarks](https://levanto.ai/benchmarks) | 2026-11-04T04:53+08:00 |
| humanitys-last-exam | 不适用 | — | [HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam), [Sage 1.4 official model page](https://levanto.ai/model) | 2026-11-04T04:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Levanto Sage benchmarks](https://levanto.ai/benchmarks) | 2026-11-04T04:53+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Sage 1.4 official model page](https://levanto.ai/model) | 2026-11-04T04:53+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 methodology](https://www.vals.ai/benchmarks/vals_index), [Sage 1.4 official benchmarks](https://levanto.ai/benchmarks) | 2026-11-04T04:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Sage 1.4 official model page](https://levanto.ai/model)

研究备注：
- DeepSWE 1.1 通过 coding agent 修改代码仓库并提交 patch，再由 verifier 检查。Sage 1.4 只输出结构化决策，不能生成任意代码补丁。

最近核验时间：2026-11-04T04:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [SWE-bench Pro dataset and protocol](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [Sage 1.4 official model page](https://levanto.ai/model)

研究备注：
- SWE-bench Pro V2 默认全量评测要求 agent 为仓库 issue 生成代码 patch 并通过隐藏测试。Sage 1.4 的 decision-only 输出不适配。

最近核验时间：2026-11-04T04:53+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 4 announcement](https://www.tbench.ai/news/terminal-bench-4-0)
- [Terminal-Bench run guide](https://www.tbench.ai/run)
- [Sage 1.4 official model page](https://levanto.ai/model)

研究备注：
- Terminal-Bench 4 需要 agent 在隔离终端环境执行任务并交付结果。Sage 1.4 无工具调用能力，也不输出命令或代码产物。

最近核验时间：2026-11-04T04:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench Science 0.1 announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Sage 1.4 official model page](https://levanto.ai/model)

研究备注：
- Terminal-Bench Science 0.1 要执行科学工作流并交付分析、模拟、代码或数据工件。Sage 1.4 的结构化决策输出不适配。

最近核验时间：2026-11-04T04:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Sage documentation](https://docs.levanto.ai/)

研究备注：
- AutomationBench 1.0.6 评估多应用工作流的最终环境状态，依赖模拟工具与应用操作。Sage 1.4 输出决策但没有原生工具执行能力；外部 agent 包装器的成绩不能归给单模型。

最近核验时间：2026-11-04T04:53+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld v2.1 official site](https://osworld-v2.xlang.ai/)
- [Sage documentation](https://docs.levanto.ai/)

研究备注：
- OSWorld v2.1 要求长时桌面操作与 GUI action。Sage 可接收图像，但没有原生 GUI 工具，输出也只是结构化决策，无法独立完成协议。

最近核验时间：2026-11-04T04:53+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography protocol paper](https://arxiv.org/html/2608.10677)
- [Sage 1.4 official benchmarks](https://levanto.ai/benchmarks)

研究备注：
- Chartography 要读取图表图像并以自由文本回答。Sage 可接收图像，但只输出固定类型的结构化决策，不能完成自由作答协议。

最近核验时间：2026-11-04T04:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Sage 1.4 official model page](https://levanto.ai/model)

研究备注：
- 原版 HLE 包含 2,500 题，其中多数是 short-answer；Sage 可回答 choice 型问题，但不能输出完整自由文本答案，不能将部分选择题子集成绩当作原版总分。

最近核验时间：2026-11-04T04:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Levanto Sage benchmarks](https://levanto.ai/benchmarks)

研究备注：
- Artificial Analysis Intelligence Index v5 是由九项不同工作流组成的综合指数，包含 agent 工具使用、代码和文件产物。Sage 1.4 的 decision-only/no-tools 接口不适配完整指数；Levanto 自有 Decision Index 分数不是该指数。

最近核验时间：2026-11-04T04:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Sage 1.4 official model page](https://levanto.ai/model)

研究备注：
- GDPval-AA v2.1 使用 shell/web agent 产出文档、幻灯片、图表及表格等工作成果并进行盲评。Sage 1.4 不生成这些文件且没有工具调用。

最近核验时间：2026-11-04T04:53+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 methodology](https://www.vals.ai/benchmarks/vals_index)
- [Sage 1.4 official benchmarks](https://levanto.ai/benchmarks)

研究备注：
- Vals Index v2.2 汇总 finance、coding、legal、tax 等 agent 工作流，包括 Excel/代码/法律与税务工作成果。Sage 1.4 无法独立生成所需产物或调用工具。

最近核验时间：2026-11-04T04:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Levanto Sage benchmarks",
          "url": "https://levanto.ai/benchmarks"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index v5 是由九项不同工作流组成的综合指数，包含 agent 工具使用、代码和文件产物。Sage 1.4 的 decision-only/no-tools 接口不适配完整指数；Levanto 自有 Decision Index 分数不是该指数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Sage documentation",
          "url": "https://docs.levanto.ai/"
        }
      ],
      "notes": [
        "AutomationBench 1.0.6 评估多应用工作流的最终环境状态，依赖模拟工具与应用操作。Sage 1.4 输出决策但没有原生工具执行能力；外部 agent 包装器的成绩不能归给单模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography protocol paper",
          "url": "https://arxiv.org/html/2608.10677"
        },
        {
          "label": "Sage 1.4 official benchmarks",
          "url": "https://levanto.ai/benchmarks"
        }
      ],
      "notes": [
        "Chartography 要读取图表图像并以自由文本回答。Sage 可接收图像，但只输出固定类型的结构化决策，不能完成自由作答协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Sage 1.4 official model page",
          "url": "https://levanto.ai/model"
        }
      ],
      "notes": [
        "DeepSWE 1.1 通过 coding agent 修改代码仓库并提交 patch，再由 verifier 检查。Sage 1.4 只输出结构化决策，不能生成任意代码补丁。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Sage 1.4 official model page",
          "url": "https://levanto.ai/model"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 使用 shell/web agent 产出文档、幻灯片、图表及表格等工作成果并进行盲评。Sage 1.4 不生成这些文件且没有工具调用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "HLE official leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Sage 1.4 official model page",
          "url": "https://levanto.ai/model"
        }
      ],
      "notes": [
        "原版 HLE 包含 2,500 题，其中多数是 short-answer；Sage 可回答 choice 型问题，但不能输出完整自由文本答案，不能将部分选择题子集成绩当作原版总分。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld v2.1 official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Sage documentation",
          "url": "https://docs.levanto.ai/"
        }
      ],
      "notes": [
        "OSWorld v2.1 要求长时桌面操作与 GUI action。Sage 可接收图像，但没有原生 GUI 工具，输出也只是结构化决策，无法独立完成协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro dataset and protocol",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "Sage 1.4 official model page",
          "url": "https://levanto.ai/model"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 默认全量评测要求 agent 为仓库 issue 生成代码 patch 并通过隐藏测试。Sage 1.4 的 decision-only 输出不适配。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Sage 1.4 official model page",
          "url": "https://levanto.ai/model"
        }
      ],
      "notes": [
        "Terminal-Bench Science 0.1 要执行科学工作流并交付分析、模拟、代码或数据工件。Sage 1.4 的结构化决策输出不适配。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Terminal-Bench run guide",
          "url": "https://www.tbench.ai/run"
        },
        {
          "label": "Sage 1.4 official model page",
          "url": "https://levanto.ai/model"
        }
      ],
      "notes": [
        "Terminal-Bench 4 需要 agent 在隔离终端环境执行任务并交付结果。Sage 1.4 无工具调用能力，也不输出命令或代码产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T04:53+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Sage 1.4 official benchmarks",
          "url": "https://levanto.ai/benchmarks"
        }
      ],
      "notes": [
        "Vals Index v2.2 汇总 finance、coding、legal、tax 等 agent 工作流，包括 Excel/代码/法律与税务工作成果。Sage 1.4 无法独立生成所需产物或调用工具。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T04:53+08:00",
  "model_id": "levanto/levanto-sage-v1.4",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
