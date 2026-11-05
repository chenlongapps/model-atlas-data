# Seedance 2.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：bytedance-seed/seedance-2.5
- 模型名称：Seedance 2.5
- 发布日期：2026-07-31
- 最近检查时间：2026-11-04T21:05+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- ByteDance Seed 官方公告于 2026-07-31 发布 Seedance 2.5，定位为音视频联合生成模型，支持图像、视频和音频参考输入，单次最长生成 30 秒音视频（https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5）。它没有通用推理或 agent 工作流能力，因此 11 项目标均不适用。未将其他 ByteDance 或 Seedance 版本的成绩转归给本模型。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE 官方榜单](https://deepswe.datacurve.ai/) | 2026-11-04T21:05+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro V2 官方仓库](https://github.com/scaleapi/SWE-bench_Pro-os) | 2026-11-04T21:05+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 官方 V4 页面](https://www.tbench.ai/?version=4) | 2026-11-04T21:05+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench-Science 官方榜单](https://www.terminal-bench-science.ai/) | 2026-11-04T21:05+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Zapier AutomationBench 官方榜单与说明](https://zapier.com/benchmarks) | 2026-11-04T21:05+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T21:05+08:00 |
| chartography | 不适用 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方任务说明](https://surgehq.ai/blog/chartography) | 2026-11-04T21:05+08:00 |
| humanitys-last-exam | 不适用 | — | [Scale HLE 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T21:05+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index V5 官方页面](https://artificialanalysis.ai/) | 2026-11-04T21:05+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA V2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T21:05+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals AI Vals Index 2.2 官方榜单与说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:05+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 评测长时程软件工程 agent。Seedance 2.5 是生成音视频的创作模型，不是代码模型。

最近核验时间：2026-11-04T21:05+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro V2 官方仓库](https://github.com/scaleapi/SWE-bench_Pro-os)

研究备注：
- SWE-bench Pro V2 评测 agent 修复代码仓库问题并提交代码补丁的能力；Seedance 2.5 只生成视频与音频。

最近核验时间：2026-11-04T21:05+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 官方 V4 页面](https://www.tbench.ai/?version=4)

研究备注：
- Terminal-Bench 4.0 评测 agent 完成终端任务的能力。Seedance 2.5 不提供终端工具或任务执行接口。

最近核验时间：2026-11-04T21:05+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench-Science 官方榜单](https://www.terminal-bench-science.ai/)

研究备注：
- Terminal-Bench-Science 评测科研 agent 工作流及其分析、代码和数据产物；视频生成模型不适用于该任务。

最近核验时间：2026-11-04T21:05+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单与说明](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 评测 agent 使用工具完成跨应用业务工作流。Seedance 2.5 生成音视频，不提供业务状态操作或工具调用能力。

最近核验时间：2026-11-04T21:05+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld 2.1 评测长程桌面和网页操作 agent；Seedance 2.5 不执行计算机操作。

最近核验时间：2026-11-04T21:05+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方任务说明](https://surgehq.ai/blog/chartography)

研究备注：
- Chartography 要求模型读取专业图表并回答问题。Seedance 2.5 虽可接收图像作为视频生成参考，但其输出是音视频，不是图表问答答案。

最近核验时间：2026-11-04T21:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Scale HLE 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- Humanity’s Last Exam 评测学术知识和推理能力；Seedance 2.5 是创意视频生成模型，不是通用问答模型。

最近核验时间：2026-11-04T21:05+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5 官方页面](https://artificialanalysis.ai/)

研究备注：
- Artificial Analysis Intelligence Index V5 综合评估知识工作、编码、科学工作流及通用知识等模型能力；生成视频模型不适用。

最近核验时间：2026-11-04T21:05+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA V2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 评测模型使用 shell 和网页工具完成专业工作并提交文档、表格等成品；Seedance 2.5 不执行此类 agent 工作流。

最近核验时间：2026-11-04T21:05+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals AI Vals Index 2.2 官方榜单与说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 2.2 汇总金融、编码、法律和税务 agent 任务表现；视频生成模型与该工作评测无关。

最近核验时间：2026-11-04T21:05+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5 官方页面",
          "url": "https://artificialanalysis.ai/"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 综合评估知识工作、编码、科学工作流及通用知识等模型能力；生成视频模型不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单与说明",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 评测 agent 使用工具完成跨应用业务工作流。Seedance 2.5 生成音视频，不提供业务状态操作或工具调用能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方任务说明",
          "url": "https://surgehq.ai/blog/chartography"
        }
      ],
      "notes": [
        "Chartography 要求模型读取专业图表并回答问题。Seedance 2.5 虽可接收图像作为视频生成参考，但其输出是音视频，不是图表问答答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 评测长时程软件工程 agent。Seedance 2.5 是生成音视频的创作模型，不是代码模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA V2.1 官方榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 评测模型使用 shell 和网页工具完成专业工作并提交文档、表格等成品；Seedance 2.5 不执行此类 agent 工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Scale HLE 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "Humanity’s Last Exam 评测学术知识和推理能力；Seedance 2.5 是创意视频生成模型，不是通用问答模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "OSWorld 2.1 评测长程桌面和网页操作 agent；Seedance 2.5 不执行计算机操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro V2 官方仓库",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 评测 agent 修复代码仓库问题并提交代码补丁的能力；Seedance 2.5 只生成视频与音频。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench-Science 官方榜单",
          "url": "https://www.terminal-bench-science.ai/"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 评测科研 agent 工作流及其分析、代码和数据产物；视频生成模型不适用于该任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 官方 V4 页面",
          "url": "https://www.tbench.ai/?version=4"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 评测 agent 完成终端任务的能力。Seedance 2.5 不提供终端工具或任务执行接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:05+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index 2.2 官方榜单与说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 2.2 汇总金融、编码、法律和税务 agent 任务表现；视频生成模型与该工作评测无关。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:05+08:00",
  "model_id": "bytedance-seed/seedance-2.5",
  "model_notes": [
    "ByteDance Seed 官方公告于 2026-07-31 发布 Seedance 2.5，定位为音视频联合生成模型，支持图像、视频和音频参考输入，单次最长生成 30 秒音视频（https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5）。它没有通用推理或 agent 工作流能力，因此 11 项目标均不适用。未将其他 ByteDance 或 Seedance 版本的成绩转归给本模型。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
