# Clef Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：cloudflare/clef-flash
- 模型名称：Clef Flash
- 发布日期：2026-10-01
- 最近检查时间：2026-11-04T05:14+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T05:14+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T05:14+08:00 |
| terminal-bench-v4 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [Terminal-Bench run guide](https://www.tbench.ai/run) | 2026-11-04T05:14+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T05:14+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [AutomationBench official page](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T05:14+08:00 |
| osworld-v2.1 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T05:14+08:00 |
| chartography | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and protocol](https://arxiv.org/html/2608.10677) | 2026-11-04T05:14+08:00 |
| humanitys-last-exam | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [Scale HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Decision Index page for Clef-Flash](https://artificialanalysis.ai/decision-models/clef-flash) | 2026-11-04T05:14+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Decision Index page for Clef-Flash](https://artificialanalysis.ai/decision-models/clef-flash) | 2026-11-04T05:14+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T05:14+08:00 |
| vals-index-v2.2 | 不适用 | — | [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash), [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T05:14+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 要求模型提交代码补丁并由隔离 verifier 执行检查；Clef-Flash 只返回 schema 约束的选项概率，不生成代码。

最近核验时间：2026-11-04T05:14+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- SWE-bench Pro V2 要求 agent 修改仓库、提交 diff 并在独立环境验证；Clef-Flash 不输出代码且无工具执行能力。

最近核验时间：2026-11-04T05:14+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [Terminal-Bench run guide](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench 4 通过 Harbor 在沙箱终端中运行 agent 并评估任务完成；Clef-Flash 不能执行 shell 或生成终端工作产物。

最近核验时间：2026-11-04T05:14+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science 要求 agent 执行科研终端流程并产出可测试工件；Clef-Flash 不输出代码/文件，也不执行工具。

最近核验时间：2026-11-04T05:14+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [AutomationBench official page](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 评估 agent 使用工具完成端到端工作流并达到目标环境状态；Clef-Flash 不支持工具调用。未找到该准确变体的目标成绩。

最近核验时间：2026-11-04T05:14+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld V2.1 要求计算机使用 agent 观察界面并执行 GUI 操作；Clef-Flash 虽接收图像但不能生成界面操作或调用工具。

最近核验时间：2026-11-04T05:14+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and protocol](https://arxiv.org/html/2608.10677)

研究备注：
- Chartography 标准协议要求根据图表图像生成自由文本答案；Clef-Flash 只输出 schema 约束的选择概率，不符合该输出要求；官方榜单未找到该精确变体。

最近核验时间：2026-11-04T05:14+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [Scale HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Decision Index page for Clef-Flash](https://artificialanalysis.ai/decision-models/clef-flash)

研究备注：
- Scale 完整 HLE 有 2,500 道公开题，约 24% 为多选，整体评估最终答案与信心；Clef-Flash 不能对完整集合中的自由作答题输出答案文本。AA Decision Index 的 HLE-MultiChoice 子项和 Decision Index 46 分均不是完整 HLE 成绩，未映射。

最近核验时间：2026-11-04T05:14+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Decision Index page for Clef-Flash](https://artificialanalysis.ai/decision-models/clef-flash)

研究备注：
- Intelligence Index V5 汇总知识工作、编码、科学和通识任务；Clef-Flash 的结构化选择输出不能完成开放式答案或工作成果。官方 Decision Index 46 是另一套指标，未映射到 Intelligence Index V5。

最近核验时间：2026-11-04T05:14+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA V2.1 要求 agent 使用工具并交付文档、幻灯片、图表、表格等工作成果；Clef-Flash 无工具调用且不生成自由文本/这些产物。

最近核验时间：2026-11-04T05:14+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Cloudflare Clef-Flash model card](https://huggingface.co/Cloudflare/clef-flash)
- [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index V2.2 汇总 finance、coding、legal、tax 的 agentic 任务表现；Clef-Flash 无工具且不生成自由文本或工作产物，不能完成该协议。

最近核验时间：2026-11-04T05:14+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Decision Index page for Clef-Flash",
          "url": "https://artificialanalysis.ai/decision-models/clef-flash"
        }
      ],
      "notes": [
        "Intelligence Index V5 汇总知识工作、编码、科学和通识任务；Clef-Flash 的结构化选择输出不能完成开放式答案或工作成果。官方 Decision Index 46 是另一套指标，未映射到 Intelligence Index V5。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
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
        "AutomationBench 评估 agent 使用工具完成端到端工作流并达到目标环境状态；Clef-Flash 不支持工具调用。未找到该准确变体的目标成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
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
        "Chartography 标准协议要求根据图表图像生成自由文本答案；Clef-Flash 只输出 schema 约束的选择概率，不符合该输出要求；官方榜单未找到该精确变体。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 要求模型提交代码补丁并由隔离 verifier 执行检查；Clef-Flash 只返回 schema 约束的选项概率，不生成代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA V2.1 要求 agent 使用工具并交付文档、幻灯片、图表、表格等工作成果；Clef-Flash 无工具调用且不生成自由文本/这些产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "Scale HLE official leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Decision Index page for Clef-Flash",
          "url": "https://artificialanalysis.ai/decision-models/clef-flash"
        }
      ],
      "notes": [
        "Scale 完整 HLE 有 2,500 道公开题，约 24% 为多选，整体评估最终答案与信心；Clef-Flash 不能对完整集合中的自由作答题输出答案文本。AA Decision Index 的 HLE-MultiChoice 子项和 Decision Index 46 分均不是完整 HLE 成绩，未映射。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
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
        "OSWorld V2.1 要求计算机使用 agent 观察界面并执行 GUI 操作；Clef-Flash 虽接收图像但不能生成界面操作或调用工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 agent 修改仓库、提交 diff 并在独立环境验证；Clef-Flash 不输出代码且无工具执行能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "Terminal-Bench Science 0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要求 agent 执行科研终端流程并产出可测试工件；Clef-Flash 不输出代码/文件，也不执行工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "Terminal-Bench run guide",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench 4 通过 Harbor 在沙箱终端中运行 agent 并评估任务完成；Clef-Flash 不能执行 shell 或生成终端工作产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:14+08:00",
      "checked_sources": [
        {
          "label": "Cloudflare Clef-Flash model card",
          "url": "https://huggingface.co/Cloudflare/clef-flash"
        },
        {
          "label": "Vals Index V2.2 official methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index V2.2 汇总 finance、coding、legal、tax 的 agentic 任务表现；Clef-Flash 无工具且不生成自由文本或工作产物，不能完成该协议。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:14+08:00",
  "model_id": "cloudflare/clef-flash",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
