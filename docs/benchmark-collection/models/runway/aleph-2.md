# Aleph 2.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：runway/aleph-2
- 模型名称：Aleph 2.0
- 发布日期：2026-06
- 最近检查时间：2026-11-05T04:50+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Runway 官方 API 变更记录确认 aleph2 是视频编辑 API：输入既有视频、文字提示和可选关键帧，输出编辑后视频。此精确型号不是通用文本/代码代理，也不是 GUI 控制模型。
- 11 项目标按其 benchmark 的代码、桌面代理、图表理解、知识推理或职业任务类型核验后均不适用；本轮未写入成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T04:50+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T04:50+08:00 |
| terminal-bench-v4 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [Terminal-Bench 4.0 page](https://www.tbench.ai/?version=4.0&efforts=all) | 2026-11-05T04:50+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [Terminal-Bench Science 0.1 page](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T04:50+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05T04:50+08:00 |
| osworld-v2.1 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T04:50+08:00 |
| chartography | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T04:50+08:00 |
| humanitys-last-exam | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [Humanity’s Last Exam site](https://lastexam.ai/) | 2026-11-05T04:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T04:50+08:00 |
| vals-index-v2.2 | 不适用 | — | [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/), [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T04:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 视频编辑 API 不执行软件仓库修复任务。

最近核验时间：2026-11-05T04:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 视频编辑 API 不执行软件仓库修复任务。

最近核验时间：2026-11-05T04:50+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [Terminal-Bench 4.0 page](https://www.tbench.ai/?version=4.0&efforts=all)

研究备注：
- 视频编辑 API 不执行终端工作流任务。

最近核验时间：2026-11-05T04:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [Terminal-Bench Science 0.1 page](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 视频编辑 API 不执行终端科学研究工作流。

最近核验时间：2026-11-05T04:50+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 该型号用于视频编辑，没有可核实的通用 SaaS 工具代理能力。

最近核验时间：2026-11-05T04:50+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 视频输入/视频输出编辑能力不等同于屏幕观察与 GUI 动作控制。

最近核验时间：2026-11-05T04:50+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 视频编辑任务不满足图表静态图像理解与问答的输入输出要求。

最近核验时间：2026-11-05T04:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [Humanity’s Last Exam site](https://lastexam.ai/)

研究备注：
- 视频编辑 API 不是通用学术问答模型。

最近核验时间：2026-11-05T04:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 视频编辑 API 不适用于通用知识、编码、科学和推理综合评测。

最近核验时间：2026-11-05T04:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 视频编辑能力不满足职业代理任务的文件交付和工具工作流要求。

最近核验时间：2026-11-05T04:50+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway input format documentation](https://docs.dev.runwayml.com/assets/inputs/)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 视频编辑 API 不具备 Vals Index 的跨行业 agentic 工作任务能力。

最近核验时间：2026-11-05T04:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "AA Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "视频编辑 API 不适用于通用知识、编码、科学和推理综合评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "该型号用于视频编辑，没有可核实的通用 SaaS 工具代理能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "视频编辑任务不满足图表静态图像理解与问答的输入输出要求。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "视频编辑 API 不执行软件仓库修复任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "视频编辑能力不满足职业代理任务的文件交付和工具工作流要求。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "Humanity’s Last Exam site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "视频编辑 API 不是通用学术问答模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "视频输入/视频输出编辑能力不等同于屏幕观察与 GUI 动作控制。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "视频编辑 API 不执行软件仓库修复任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "Terminal-Bench Science 0.1 page",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "视频编辑 API 不执行终端科学研究工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "Terminal-Bench 4.0 page",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        }
      ],
      "notes": [
        "视频编辑 API 不执行终端工作流任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Runway API changelog",
          "url": "https://docs.dev.runwayml.com/api-details/api_changelog/"
        },
        {
          "label": "Runway input format documentation",
          "url": "https://docs.dev.runwayml.com/assets/inputs/"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "视频编辑 API 不具备 Vals Index 的跨行业 agentic 工作任务能力。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:50+08:00",
  "model_id": "runway/aleph-2",
  "model_notes": [
    "Runway 官方 API 变更记录确认 aleph2 是视频编辑 API：输入既有视频、文字提示和可选关键帧，输出编辑后视频。此精确型号不是通用文本/代码代理，也不是 GUI 控制模型。",
    "11 项目标按其 benchmark 的代码、桌面代理、图表理解、知识推理或职业任务类型核验后均不适用；本轮未写入成绩。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
