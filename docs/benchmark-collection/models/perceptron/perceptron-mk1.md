# Perceptron Mk1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：perceptron/perceptron-mk1
- 模型名称：Perceptron Mk1
- 发布日期：2026-05-12
- 最近检查时间：2026-11-05T06:15+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地 TOML 无目标 Benchmark 成绩。官方发布资料称模型用于视觉分析、规划和工具使用，但官方 Mk1 API 文档明确不接受 tools、tool_choice 或 parallel_tool_calls；外部 agent 集成不等于 API 原生工具调用。
- AutomationBench 与 OSWorld 的工具适配方式尚待核实，故状态为待核实；没有把未确认的结果写入 TOML。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [DeepSWE 官方榜单](https://deepswe.datacurve.ai/) | 2026-11-05T06:15+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:15+08:00 |
| terminal-bench-v4 | 不适用 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [Terminal-Bench 4 评测定义](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:15+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [Terminal-Bench Science 评测定义](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:15+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench), [AutomationBench 官方榜单](https://zapier.com/benchmarks) | 2026-11-05T06:15+08:00 |
| osworld-v2.1 | 待核实 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:15+08:00 |
| chartography | 未找到 | — | [Perceptron Mk1 发布文章](https://www.perceptron.inc/blog/introducing-perceptron-mk1), [('Perceptron Mk1 Chat Completions API', 'https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions')](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [Chartography 官方任务仓库](https://github.com/surge-ai/chartography), [Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:15+08:00 |
| humanitys-last-exam | 未找到 | — | [Perceptron Mk1 发布文章](https://www.perceptron.inc/blog/introducing-perceptron-mk1), [Humanity's Last Exam 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:15+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Perceptron Mk1 发布文章](https://www.perceptron.inc/blog/introducing-perceptron-mk1), [('Perceptron Mk1 Chat Completions API', 'https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions')](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [Artificial Analysis Intelligence Index 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:15+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [GDPval-AA 评测方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:15+08:00 |
| vals-index-v2.2 | 不适用 | — | [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions), [Vals Index v2.2 及方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:15+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)

研究备注：
- 模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。

最近核验时间：2026-11-05T06:15+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。

最近核验时间：2026-11-05T06:15+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [Terminal-Bench 4 评测定义](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。

最近核验时间：2026-11-05T06:15+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [Terminal-Bench Science 评测定义](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。

最近核验时间：2026-11-05T06:15+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)
- [AutomationBench 官方榜单](https://zapier.com/benchmarks)

研究备注：
- 官方 API 不接受原生工具调用；尚未确认是否存在将 Mk1 文本输出转换为环境工具动作的适配 harness。官方榜单折叠了未展示条目，无法据可见行判定未参评。

尚未解决的问题：
- 需要核实是否有公开、可复现的 Mk1 适配 harness，以及折叠榜单中是否有精确型号成绩。

最近核验时间：2026-11-05T06:15+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型可读图像并输出文本，但官方 API 不提供原生工具调用；尚未确认是否有适用于 Mk1 的桌面动作适配 harness或可核实评测结果。

尚未解决的问题：
- 需要核实是否有公开 Mk1 桌面动作 harness及 OSWorld 2.1 精确结果。

最近核验时间：2026-11-05T06:15+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perceptron Mk1 发布文章](https://www.perceptron.inc/blog/introducing-perceptron-mk1)
- [('Perceptron Mk1 Chat Completions API', 'https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions')](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [Chartography 官方任务仓库](https://github.com/surge-ai/chartography)
- [Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Mk1 的图像输入、文本输出与图表问答形式匹配；检查 Perceptron 发布资料和 Chartography 官方榜单，未发现精确型号或可核实成绩。

最近核验时间：2026-11-05T06:15+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perceptron Mk1 发布文章](https://www.perceptron.inc/blog/introducing-perceptron-mk1)
- [Humanity's Last Exam 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Mk1 支持图像输入和文本回答，任务模态匹配；发布资料未给出 HLE 成绩，检查的官方 HLE 结果页未发现精确型号记录。

最近核验时间：2026-11-05T06:15+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perceptron Mk1 发布文章](https://www.perceptron.inc/blog/introducing-perceptron-mk1)
- [('Perceptron Mk1 Chat Completions API', 'https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions')](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [Artificial Analysis Intelligence Index 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Mk1 的图像输入和文本输出使其可能适用于含视觉项目的指数评测；检查 AA 指数方法/结果资料未发现 Mk1 的精确 v5 结果。

最近核验时间：2026-11-05T06:15+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [GDPval-AA 评测方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 官方 GDPval-AA v2.1 配置使用 Stirrup agentic loop、shell/web 工具并要求文件成果；Mk1 API 不支持原生工具调用，本地没有可验证兼容 harness或成绩。

最近核验时间：2026-11-05T06:15+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Perceptron Mk1 Chat Completions API](https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions)
- [Vals Index v2.2 及方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 是涵盖金融、编码、法律、税务等 agentic 能力的复合指数；Mk1 API 不支持工具调用，无法按该指数完整配置参测。

最近核验时间：2026-11-05T06:15+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 发布文章",
          "url": "https://www.perceptron.inc/blog/introducing-perceptron-mk1"
        },
        {
          "label": [
            "Perceptron Mk1 Chat Completions API",
            "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
          ],
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "Artificial Analysis Intelligence Index 方法说明",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Mk1 的图像输入和文本输出使其可能适用于含视觉项目的指数评测；检查 AA 指数方法/结果资料未发现 Mk1 的精确 v5 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "官方 API 不接受原生工具调用；尚未确认是否存在将 Mk1 文本输出转换为环境工具动作的适配 harness。官方榜单折叠了未展示条目，无法据可见行判定未参评。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要核实是否有公开、可复现的 Mk1 适配 harness，以及折叠榜单中是否有精确型号成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 发布文章",
          "url": "https://www.perceptron.inc/blog/introducing-perceptron-mk1"
        },
        {
          "label": [
            "Perceptron Mk1 Chat Completions API",
            "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
          ],
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "Chartography 官方任务仓库",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Mk1 的图像输入、文本输出与图表问答形式匹配；检查 Perceptron 发布资料和 Chartography 官方榜单，未发现精确型号或可核实成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "GDPval-AA 评测方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "官方 GDPval-AA v2.1 配置使用 Stirrup agentic loop、shell/web 工具并要求文件成果；Mk1 API 不支持原生工具调用，本地没有可验证兼容 harness或成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 发布文章",
          "url": "https://www.perceptron.inc/blog/introducing-perceptron-mk1"
        },
        {
          "label": "Humanity's Last Exam 评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Mk1 支持图像输入和文本回答，任务模态匹配；发布资料未给出 HLE 成绩，检查的官方 HLE 结果页未发现精确型号记录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型可读图像并输出文本，但官方 API 不提供原生工具调用；尚未确认是否有适用于 Mk1 的桌面动作适配 harness或可核实评测结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要核实是否有公开 Mk1 桌面动作 harness及 OSWorld 2.1 精确结果。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "Terminal-Bench Science 评测定义",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "Terminal-Bench 4 评测定义",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "模型 API 官方文档明确不接受 tools、tool_choice 或 parallel_tool_calls；该项依赖代码/终端 agent 工作流。没有可确认的原生适用评测配置或成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Perceptron Mk1 Chat Completions API",
          "url": "https://docs.perceptron.inc/perceptron-mk1/api-reference/endpoint/chat-completions"
        },
        {
          "label": "Vals Index v2.2 及方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 是涵盖金融、编码、法律、税务等 agentic 能力的复合指数；Mk1 API 不支持工具调用，无法按该指数完整配置参测。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:15+08:00",
  "model_id": "perceptron/perceptron-mk1",
  "model_notes": [
    "本地 TOML 无目标 Benchmark 成绩。官方发布资料称模型用于视觉分析、规划和工具使用，但官方 Mk1 API 文档明确不接受 tools、tool_choice 或 parallel_tool_calls；外部 agent 集成不等于 API 原生工具调用。",
    "AutomationBench 与 OSWorld 的工具适配方式尚待核实，故状态为待核实；没有把未确认的结果写入 TOML。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
