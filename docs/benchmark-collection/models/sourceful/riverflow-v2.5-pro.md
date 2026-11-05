# Riverflow 2.5 Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：sourceful/riverflow-v2.5-pro
- 模型名称：Riverflow 2.5 Pro
- 发布日期：2026-06-05
- 最近检查时间：2026-11-05T04:05+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Sourceful/Replicate 精确型号页确认 Riverflow 2.5 Pro 为图像生成/编辑 API，支持参考图、内部多步规划与候选评分；API 输出是图像，以上内部功能不属于本轮目标 Benchmark 的直接评测结果。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| terminal-bench-v4 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| osworld-v2.1 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| chartography | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| humanitys-last-exam | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |
| vals-index-v2.2 | 不适用 | — | [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro) | 2026-11-05T04:05+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 这是图像生成与编辑 API，不执行代码仓库修复任务。内部多步图像精修与评分不是 DeepSWE 成绩。

最近核验时间：2026-11-05T04:05+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 服务输出图像，不产生 SWE-bench Pro V2 的仓库修复补丁；不适用。

最近核验时间：2026-11-05T04:05+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 服务输出图像，不提供终端操作代理能力；不适用。

最近核验时间：2026-11-05T04:05+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 服务输出图像，不提供在终端中完成科学任务的代理操作能力；不适用。

最近核验时间：2026-11-05T04:05+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 该图像生成/编辑 API 没有外部 SaaS 工具调用接口；内部候选打分不等同于 AutomationBench 工具工作流。

最近核验时间：2026-11-05T04:05+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- API 可用图像作为编辑参考，但输出是图像且不能返回桌面操作动作，不适用 OSWorld。

最近核验时间：2026-11-05T04:05+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- API 输出图像；Chartography 需要根据图表图像返回可评分的文本答案，不适用。

最近核验时间：2026-11-05T04:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 该图像生成/编辑服务不执行通用学术问答任务；内部 thinking 不作为 HLE 成绩。

最近核验时间：2026-11-05T04:05+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 这是专用图像生成服务；图像流程中的 thinking level 不构成通用语言推理指数结果。

最近核验时间：2026-11-05T04:05+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 图像生成端点无法按 GDPval-AA v2.1 交付文档、表格等专业任务成果，不适用。

最近核验时间：2026-11-05T04:05+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Sourceful Riverflow 2.5 Pro model page](https://replicate.com/sourceful/riverflow-v2.5-pro)

研究备注：
- 该模型为图像生成与编辑端点，不适用 Vals Index 的通用 agent/文本工作流程。

最近核验时间：2026-11-05T04:05+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "这是专用图像生成服务；图像流程中的 thinking level 不构成通用语言推理指数结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "该图像生成/编辑 API 没有外部 SaaS 工具调用接口；内部候选打分不等同于 AutomationBench 工具工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "API 输出图像；Chartography 需要根据图表图像返回可评分的文本答案，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "这是图像生成与编辑 API，不执行代码仓库修复任务。内部多步图像精修与评分不是 DeepSWE 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "图像生成端点无法按 GDPval-AA v2.1 交付文档、表格等专业任务成果，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "该图像生成/编辑服务不执行通用学术问答任务；内部 thinking 不作为 HLE 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "API 可用图像作为编辑参考，但输出是图像且不能返回桌面操作动作，不适用 OSWorld。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "服务输出图像，不产生 SWE-bench Pro V2 的仓库修复补丁；不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "服务输出图像，不提供在终端中完成科学任务的代理操作能力；不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "服务输出图像，不提供终端操作代理能力；不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:05+08:00",
      "checked_sources": [
        {
          "label": "Sourceful Riverflow 2.5 Pro model page",
          "url": "https://replicate.com/sourceful/riverflow-v2.5-pro"
        }
      ],
      "notes": [
        "该模型为图像生成与编辑端点，不适用 Vals Index 的通用 agent/文本工作流程。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:05+08:00",
  "model_id": "sourceful/riverflow-v2.5-pro",
  "model_notes": [
    "Sourceful/Replicate 精确型号页确认 Riverflow 2.5 Pro 为图像生成/编辑 API，支持参考图、内部多步规划与候选评分；API 输出是图像，以上内部功能不属于本轮目标 Benchmark 的直接评测结果。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
