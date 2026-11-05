# Gemini Embedding 2 Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-embedding-2-preview
- 模型名称：Gemini Embedding 2 Preview
- 发布日期：2026-03-10
- 最近检查时间：2026-11-05T11:57+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google 官方资料与本地 TOML 均确认该型号将多模态输入编码为 embedding 向量，不输出可评分文本。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T11:57+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T11:57+08:00 |
| terminal-bench-v4 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Terminal-Bench leaderboard](https://www.tbench.ai/leaderboard) | 2026-11-05T11:57+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Terminal-Bench Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-05T11:57+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05T11:57+08:00 |
| osworld-v2.1 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T11:57+08:00 |
| chartography | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T11:57+08:00 |
| humanitys-last-exam | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Artificial Analysis Humanity’s Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T11:57+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T11:57+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T11:57+08:00 |
| vals-index-v2.2 | 不适用 | — | [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/), [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T11:57+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Embedding 输出不能生成代码补丁或运行 coding agent。

最近核验时间：2026-11-05T11:57+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Embedding endpoint 不生成软件工程修复补丁，也不能运行 agent。

最近核验时间：2026-11-05T11:57+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Terminal-Bench leaderboard](https://www.tbench.ai/leaderboard)

研究备注：
- Embedding endpoint 不能执行终端命令或完成交互式任务。

最近核验时间：2026-11-05T11:57+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Terminal-Bench Science Harbor leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- Embedding endpoint 不能执行终端科学研究工作流。

最近核验时间：2026-11-05T11:57+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- Embedding endpoint 不提供生成式工作流执行或工具调用。

最近核验时间：2026-11-05T11:57+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Embedding endpoint 输出向量且不支持工具，不能根据屏幕状态执行桌面操作。

最近核验时间：2026-11-05T11:57+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 虽然模型可接收图像，但输出为 embedding 向量，不能产生图表问答文本答案。

最近核验时间：2026-11-05T11:57+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Artificial Analysis Humanity’s Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Embedding endpoint 不输出可评分的问答答案。

最近核验时间：2026-11-05T11:57+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 这是语言模型综合能力指数；embedding endpoint 不提供可评分的生成式推理输出。

最近核验时间：2026-11-05T11:57+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Embedding endpoint 不能生成文档、表格等 GDPval 工作成果。

最近核验时间：2026-11-05T11:57+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Google Gemini Embedding 2 announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/)
- [Google embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 评估 agentic finance/coding/legal/tax 工作成果；embedding endpoint 不生成此类成果。

最近核验时间：2026-11-05T11:57+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "这是语言模型综合能力指数；embedding endpoint 不提供可评分的生成式推理输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Embedding endpoint 不提供生成式工作流执行或工具调用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "虽然模型可接收图像，但输出为 embedding 向量，不能产生图表问答文本答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Embedding 输出不能生成代码补丁或运行 coding agent。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Embedding endpoint 不能生成文档、表格等 GDPval 工作成果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Artificial Analysis Humanity’s Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Embedding endpoint 不输出可评分的问答答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Embedding endpoint 输出向量且不支持工具，不能根据屏幕状态执行桌面操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Embedding endpoint 不生成软件工程修复补丁，也不能运行 agent。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Terminal-Bench Science Harbor leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "Embedding endpoint 不能执行终端科学研究工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Terminal-Bench leaderboard",
          "url": "https://www.tbench.ai/leaderboard"
        }
      ],
      "notes": [
        "Embedding endpoint 不能执行终端命令或完成交互式任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:57+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini Embedding 2 announcement",
          "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/"
        },
        {
          "label": "Google embeddings documentation",
          "url": "https://ai.google.dev/gemini-api/docs/embeddings"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 评估 agentic finance/coding/legal/tax 工作成果；embedding endpoint 不生成此类成果。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:57+08:00",
  "model_id": "google/gemini-embedding-2-preview",
  "model_notes": [
    "Google 官方资料与本地 TOML 均确认该型号将多模态输入编码为 embedding 向量，不输出可评分文本。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
