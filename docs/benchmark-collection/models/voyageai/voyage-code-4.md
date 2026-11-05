# voyage-code-4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：voyageai/voyage-code-4
- 模型名称：voyage-code-4
- 发布日期：2026-08-13
- 最近检查时间：2026-11-04T18:07+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Voyage AI 将 voyage-code-4 定义为代码检索 embedding 模型：文本输入、向量输出，供 coding agent 做检索使用。以下“不适用”只表示这 11 项目标测试要求生成答案或执行独立 agent 任务，不表示分数为 0。来源：[Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)、[Voyage embeddings 文档](https://docs.voyageai.com/docs/embeddings)。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [DeepSWE v1.1 评测说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T18:07+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T18:07+08:00 |
| terminal-bench-v4 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [Vals Terminal-Bench 4.0 官方说明](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T18:07+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [Vals Terminal-Bench Science 官方说明](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T18:07+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Voyage embeddings 官方文档](https://docs.voyageai.com/docs/embeddings), [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks) | 2026-11-04T18:07+08:00 |
| osworld-v2.1 | 不适用 | — | [Voyage embeddings 官方文档](https://docs.voyageai.com/docs/embeddings), [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T18:07+08:00 |
| chartography | 不适用 | — | [Voyage embeddings 官方文档](https://docs.voyageai.com/docs/embeddings), [Surge Chartography 官方说明](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T18:07+08:00 |
| humanitys-last-exam | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [Humanity’s Last Exam 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T18:07+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [Artificial Analysis Intelligence Index V5 官方页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T18:07+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T18:07+08:00 |
| vals-index-v2.2 | 不适用 | — | [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/), [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T18:07+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [DeepSWE v1.1 评测说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE requires a coding agent to submit a patch that passes task tests; voyage-code-4 returns embeddings and cannot independently modify repositories.

最近核验时间：2026-11-04T18:07+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 requires an agent to solve repository-level software engineering tasks; voyage-code-4 is a retrieval embedding used by host agents, not the code-generating agent.

最近核验时间：2026-11-04T18:07+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [Vals Terminal-Bench 4.0 官方说明](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Terminal-Bench 4 requires an agent to operate in a terminal sandbox and deliver a verified artifact; the embedding model does not execute tools or generate the task result.

最近核验时间：2026-11-04T18:07+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [Vals Terminal-Bench Science 官方说明](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Terminal-Bench Science requires terminal-based scientific workflows and verified outputs; a text-to-embedding model cannot independently execute those tasks.

最近核验时间：2026-11-04T18:07+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Voyage embeddings 官方文档](https://docs.voyageai.com/docs/embeddings)
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)

研究备注：
- AutomationBench evaluates end-to-end workflows across simulated business applications; voyage-code-4 has no independent text-generation or tool-execution output for those workflows.

最近核验时间：2026-11-04T18:07+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Voyage embeddings 官方文档](https://docs.voyageai.com/docs/embeddings)
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld evaluates agents operating a desktop environment; voyage-code-4 only accepts text and returns vectors, with no computer-use actions.

最近核验时间：2026-11-04T18:07+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Voyage embeddings 官方文档](https://docs.voyageai.com/docs/embeddings)
- [Surge Chartography 官方说明](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography evaluates visual interpretation and reasoning over chart images; voyage-code-4 only accepts text and returns embeddings.

最近核验时间：2026-11-04T18:07+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [Humanity’s Last Exam 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Humanity’s Last Exam requires standalone generated answers to closed-ended academic questions; voyage-code-4 outputs vectors rather than answers.

最近核验时间：2026-11-04T18:07+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [Artificial Analysis Intelligence Index V5 官方页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis Intelligence Index V5 aggregates nine reasoning, coding, science, and knowledge-work evaluations that require model-generated task results; code retrieval embeddings do not provide those outputs.

最近核验时间：2026-11-04T18:07+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires an agent to complete professional tasks and produce work artifacts; a retrieval embedding cannot independently create those deliverables.

最近核验时间：2026-11-04T18:07+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)
- [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index aggregates finance, coding, legal, and tax agent-task performance; voyage-code-4 is a code retrieval embedding rather than an independently acting/generating agent.

最近核验时间：2026-11-04T18:07+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 官方页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 aggregates nine reasoning, coding, science, and knowledge-work evaluations that require model-generated task results; code retrieval embeddings do not provide those outputs."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage embeddings 官方文档",
          "url": "https://docs.voyageai.com/docs/embeddings"
        },
        {
          "label": "Zapier AutomationBench 官方排行榜",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench evaluates end-to-end workflows across simulated business applications; voyage-code-4 has no independent text-generation or tool-execution output for those workflows."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage embeddings 官方文档",
          "url": "https://docs.voyageai.com/docs/embeddings"
        },
        {
          "label": "Surge Chartography 官方说明",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography evaluates visual interpretation and reasoning over chart images; voyage-code-4 only accepts text and returns embeddings."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "DeepSWE v1.1 评测说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE requires a coding agent to submit a patch that passes task tests; voyage-code-4 returns embeddings and cannot independently modify repositories."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "GDPval-AA 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires an agent to complete professional tasks and produce work artifacts; a retrieval embedding cannot independently create those deliverables."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "Humanity’s Last Exam 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Humanity’s Last Exam requires standalone generated answers to closed-ended academic questions; voyage-code-4 outputs vectors rather than answers."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage embeddings 官方文档",
          "url": "https://docs.voyageai.com/docs/embeddings"
        },
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld evaluates agents operating a desktop environment; voyage-code-4 only accepts text and returns vectors, with no computer-use actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires an agent to solve repository-level software engineering tasks; voyage-code-4 is a retrieval embedding used by host agents, not the code-generating agent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "Vals Terminal-Bench Science 官方说明",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Terminal-Bench Science requires terminal-based scientific workflows and verified outputs; a text-to-embedding model cannot independently execute those tasks."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "Vals Terminal-Bench 4.0 官方说明",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Terminal-Bench 4 requires an agent to operate in a terminal sandbox and deliver a verified artifact; the embedding model does not execute tools or generate the task result."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T18:07+08:00",
      "checked_sources": [
        {
          "label": "Voyage Code 4 发布说明",
          "url": "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
        },
        {
          "label": "Vals Index v2.2 官方排行榜",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index aggregates finance, coding, legal, and tax agent-task performance; voyage-code-4 is a code retrieval embedding rather than an independently acting/generating agent."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T18:07+08:00",
  "model_id": "voyageai/voyage-code-4",
  "model_notes": [
    "Voyage AI 将 voyage-code-4 定义为代码检索 embedding 模型：文本输入、向量输出，供 coding agent 做检索使用。以下“不适用”只表示这 11 项目标测试要求生成答案或执行独立 agent 任务，不表示分数为 0。来源：[Voyage Code 4 发布说明](https://blog.voyageai.com/2026/08/13/voyage-code-4/)、[Voyage embeddings 文档](https://docs.voyageai.com/docs/embeddings)。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
