# FLUX 3 Image Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：black-forest-labs/flux-3-image
- 模型名称：FLUX 3 Image
- 发布日期：2026-10-01
- 最近检查时间：2026-11-04T05:06+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T05:06+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T05:06+08:00 |
| terminal-bench-v4 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [Terminal-Bench run guide](https://www.tbench.ai/run) | 2026-11-04T05:06+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T05:06+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [AutomationBench official leaderboard/protocol](https://zapier.com/benchmarks) | 2026-11-04T05:06+08:00 |
| osworld-v2.1 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T05:06+08:00 |
| chartography | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [Chartography protocol paper](https://arxiv.org/html/2608.10677), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T05:06+08:00 |
| humanitys-last-exam | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [HLE official leaderboard/methodology](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T05:06+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T05:06+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [GDPval-AA V2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T05:06+08:00 |
| vals-index-v2.2 | 不适用 | — | [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview), [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T05:06+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 要求提交代码 patch 并由隔离 verifier 检查；FLUX 3 Image 生成图像，不输出代码。

最近核验时间：2026-11-04T05:06+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- SWE-bench Pro V2 要求 agent 产出代码 diff/patch 并运行测试；FLUX 3 Image 只生成图像。

最近核验时间：2026-11-04T05:06+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [Terminal-Bench run guide](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench 4 通过 Harbor 在终端沙箱中运行 agent；FLUX 3 Image 没有代码/终端输出接口。

最近核验时间：2026-11-04T05:06+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science 需要执行科研工作流并交付代码、分析、模拟或数据工件；FLUX 3 Image 仅返回图像。

最近核验时间：2026-11-04T05:06+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [AutomationBench official leaderboard/protocol](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 要求使用工具完成端到端应用工作流并按环境最终状态评分；FLUX 3 Image 不支持工具调用且只输出图像。

最近核验时间：2026-11-04T05:06+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 需要桌面截图观察及 GUI 操作。FLUX 3 Image 的图像输入用于参考/编辑，输出仍是图像，不提供桌面 action 接口。

最近核验时间：2026-11-04T05:06+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [Chartography protocol paper](https://arxiv.org/html/2608.10677)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 输入图表图像与问题，要求自由文本回答并按 mean Pass@1 评分；FLUX 3 Image 输出图像而不是答案文本。

最近核验时间：2026-11-04T05:06+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [HLE official leaderboard/methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- HLE 要求为原始题目输出可评分的最终答案；FLUX 3 Image 只返回生成图像。

最近核验时间：2026-11-04T05:06+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis Intelligence Index V5 汇总知识、编码、科学和知识工作任务，需要对应的文本/代码任务结果；FLUX 3 Image 仅生成图像。

最近核验时间：2026-11-04T05:06+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [GDPval-AA V2.1 methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA V2.1 评估 agent 产出文档、幻灯片、图表或表格等工作成果；FLUX 3 Image 不能输出这些文档或表格结构。

最近核验时间：2026-11-04T05:06+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [BFL FLUX 3 Image overview](https://docs.bfl.ml/flux_3/flux3_image_overview)
- [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index V2.2 汇总 finance、coding、legal、tax 的 agent 工作流；FLUX 3 Image 无工具且只输出图像，不能完成文字或代码任务。

最近核验时间：2026-11-04T05:06+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 汇总知识、编码、科学和知识工作任务，需要对应的文本/代码任务结果；FLUX 3 Image 仅生成图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "AutomationBench official leaderboard/protocol",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 要求使用工具完成端到端应用工作流并按环境最终状态评分；FLUX 3 Image 不支持工具调用且只输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "Chartography protocol paper",
          "url": "https://arxiv.org/html/2608.10677"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 输入图表图像与问题，要求自由文本回答并按 mean Pass@1 评分；FLUX 3 Image 输出图像而不是答案文本。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 要求提交代码 patch 并由隔离 verifier 检查；FLUX 3 Image 生成图像，不输出代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "GDPval-AA V2.1 methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA V2.1 评估 agent 产出文档、幻灯片、图表或表格等工作成果；FLUX 3 Image 不能输出这些文档或表格结构。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "HLE official leaderboard/methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "HLE 要求为原始题目输出可评分的最终答案；FLUX 3 Image 只返回生成图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 需要桌面截图观察及 GUI 操作。FLUX 3 Image 的图像输入用于参考/编辑，输出仍是图像，不提供桌面 action 接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 agent 产出代码 diff/patch 并运行测试；FLUX 3 Image 只生成图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "Terminal-Bench Science 0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science 需要执行科研工作流并交付代码、分析、模拟或数据工件；FLUX 3 Image 仅返回图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "Terminal-Bench run guide",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench 4 通过 Harbor 在终端沙箱中运行 agent；FLUX 3 Image 没有代码/终端输出接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:06+08:00",
      "checked_sources": [
        {
          "label": "BFL FLUX 3 Image overview",
          "url": "https://docs.bfl.ml/flux_3/flux3_image_overview"
        },
        {
          "label": "Vals Index V2.2 official methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index V2.2 汇总 finance、coding、legal、tax 的 agent 工作流；FLUX 3 Image 无工具且只输出图像，不能完成文字或代码任务。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:06+08:00",
  "model_id": "black-forest-labs/flux-3-image",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
