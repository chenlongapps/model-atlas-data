# Clef Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：cloudflare/clef
- 模型名称：Clef
- 发布日期：2026-10-01
- 最近检查时间：2026-11-04T05:12+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T05:12+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T05:12+08:00 |
| terminal-bench-v4 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [Terminal-Bench 4.0 protocol](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T05:12+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T05:12+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [AutomationBench official page](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T05:12+08:00 |
| osworld-v2.1 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-04T05:12+08:00 |
| chartography | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and protocol](https://arxiv.org/html/2608.10677) | 2026-11-04T05:12+08:00 |
| humanitys-last-exam | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [Scale HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Decision Index page for Clef](https://artificialanalysis.ai/decision-models/clef) | 2026-11-04T05:12+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Decision Index page for Clef](https://artificialanalysis.ai/decision-models/clef) | 2026-11-04T05:12+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T05:12+08:00 |
| vals-index-v2.2 | 不适用 | — | [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef), [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T05:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 要求模型提交代码补丁并由隔离 verifier 执行检查；Clef 只返回 schema 约束的选项概率，不生成代码。

最近核验时间：2026-11-04T05:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- SWE-bench Pro V2 要求 agent 修改仓库、提交 diff 并在独立环境验证；Clef 不输出代码且无工具执行能力。

最近核验时间：2026-11-04T05:12+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [Terminal-Bench 4.0 protocol](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4 通过 Harbor 运行终端 agent 并评估任务完成；Clef 不能执行 shell 或生成终端工作产物。

最近核验时间：2026-11-04T05:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science 要求 agent 执行科研终端流程并产出可测试工件；Clef 不输出代码/文件，也不执行工具。

最近核验时间：2026-11-04T05:12+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [AutomationBench official page](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 评估模型使用多项工具完成端到端工作流并达到目标环境状态；Clef 没有工具调用或工作流执行能力。未找到可核实的 Clef 精确版本成绩。

最近核验时间：2026-11-04T05:12+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- OSWorld V2.1 要求代理观察桌面界面并执行 GUI 操作；Clef 可读图像但不能生成 GUI 操作或调用工具。未找到可核实的 Clef 精确版本成绩。

最近核验时间：2026-11-04T05:12+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and protocol](https://arxiv.org/html/2608.10677)

研究备注：
- Chartography 要求模型根据图表图像生成自由文本答案；Clef 虽接收图像，但只输出预定义类型的决策概率，不能按原协议给出答案文本。官方榜单未找到 Clef 条目。

最近核验时间：2026-11-04T05:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [Scale HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Decision Index page for Clef](https://artificialanalysis.ai/decision-models/clef)

研究备注：
- Scale 完整 HLE 对 2,500 道公开题报告总体 accuracy，题目约 24% 为多选并要求最终答案与信心；Clef 只能输出 schema 约束选择概率，不能回答完整集合中的自由作答题。AA Decision Index 中的 HLE-MultiChoice 及其 Decision Index 49 分不等同完整 HLE 成绩，未写入。

最近核验时间：2026-11-04T05:12+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Decision Index page for Clef](https://artificialanalysis.ai/decision-models/clef)

研究备注：
- Intelligence Index V5 是知识工作、编码、科学和通识任务的复合评估；Clef 的固定选项概率输出不能完成开放式回答或工作成果。公开 Clef 页面显示的是不同的 Decision Index，不是本项 Intelligence Index V5，未作映射。

最近核验时间：2026-11-04T05:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA V2.1 要求完成并交付文档、幻灯片、图表、表格等工作成果；Clef 只能给 schema 约束的选项/评分概率，不能生成这些产物。

最近核验时间：2026-11-04T05:12+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef model card](https://huggingface.co/Cloudflare/clef)
- [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index V2.2 汇总 finance、coding、legal、tax 的 agentic 任务表现；Clef 无工具且不生成开放文本或工作产物，无法按该协议完成评测。

最近核验时间：2026-11-04T05:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Decision Index page for Clef",
          "url": "https://artificialanalysis.ai/decision-models/clef"
        }
      ],
      "notes": [
        "Intelligence Index V5 是知识工作、编码、科学和通识任务的复合评估；Clef 的固定选项概率输出不能完成开放式回答或工作成果。公开 Clef 页面显示的是不同的 Decision Index，不是本项 Intelligence Index V5，未作映射。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "AutomationBench official page",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 评估模型使用多项工具完成端到端工作流并达到目标环境状态；Clef 没有工具调用或工作流执行能力。未找到可核实的 Clef 精确版本成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper and protocol",
          "url": "https://arxiv.org/html/2608.10677"
        }
      ],
      "notes": [
        "Chartography 要求模型根据图表图像生成自由文本答案；Clef 虽接收图像，但只输出预定义类型的决策概率，不能按原协议给出答案文本。官方榜单未找到 Clef 条目。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 要求模型提交代码补丁并由隔离 verifier 执行检查；Clef 只返回 schema 约束的选项概率，不生成代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA V2.1 要求完成并交付文档、幻灯片、图表、表格等工作成果；Clef 只能给 schema 约束的选项/评分概率，不能生成这些产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "Scale HLE official leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Decision Index page for Clef",
          "url": "https://artificialanalysis.ai/decision-models/clef"
        }
      ],
      "notes": [
        "Scale 完整 HLE 对 2,500 道公开题报告总体 accuracy，题目约 24% 为多选并要求最终答案与信心；Clef 只能输出 schema 约束选择概率，不能回答完整集合中的自由作答题。AA Decision Index 中的 HLE-MultiChoice 及其 Decision Index 49 分不等同完整 HLE 成绩，未写入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "OSWorld V2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "OSWorld V2.1 要求代理观察桌面界面并执行 GUI 操作；Clef 可读图像但不能生成 GUI 操作或调用工具。未找到可核实的 Clef 精确版本成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 agent 修改仓库、提交 diff 并在独立环境验证；Clef 不输出代码且无工具执行能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "Terminal-Bench Science 0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要求 agent 执行科研终端流程并产出可测试工件；Clef 不输出代码/文件，也不执行工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "Terminal-Bench 4.0 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4 通过 Harbor 运行终端 agent 并评估任务完成；Clef 不能执行 shell 或生成终端工作产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:12+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef model card",
          "url": "https://huggingface.co/Cloudflare/clef"
        },
        {
          "label": "Vals Index V2.2 official methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index V2.2 汇总 finance、coding、legal、tax 的 agentic 任务表现；Clef 无工具且不生成开放文本或工作产物，无法按该协议完成评测。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:12+08:00",
  "model_id": "cloudflare/clef",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
