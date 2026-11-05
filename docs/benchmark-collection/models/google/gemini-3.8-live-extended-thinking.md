# Gemini 3.8 Live Extended Thinking Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.8-live-extended-thinking
- 模型名称：Gemini 3.8 Live Extended Thinking
- 发布日期：2026-09-15
- 最近检查时间：2026-11-04T11:02+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方结果页](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking) | 2026-11-04T11:02+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking) | 2026-11-04T11:02+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 官方动态榜单](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 发布说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T11:02+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 官方结果公告](https://www.tbench.ai/news/terminal-bench-science-0-1), [Terminal-Bench-Science 当前官方榜单](https://www.terminal-bench-science.ai/), [Google Gemini 3.8 Live Extended Thinking 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/) | 2026-11-04T11:02+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench), [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking) | 2026-11-04T11:02+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld v2.1 官方评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld 官方榜单](https://osworld-v2.xlang.ai/), [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking) | 2026-11-04T11:02+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Google Gemini 3.8 Live Extended Thinking 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/) | 2026-11-04T11:02+08:00 |
| humanitys-last-exam | 未找到 | — | [Artificial Analysis HLE 定义与榜单](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Google Gemini 3.8 Audio 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/), [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/) | 2026-11-04T11:02+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis 模型页](https://artificialanalysis.ai/models), [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/) | 2026-11-04T11:02+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 方法与榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/) | 2026-11-04T11:02+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking) | 2026-11-04T11:02+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方结果页](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking)

研究备注：
- 官方 DeepSWE 页面列出 Gemini 3.8 Flash，但未列 gemini-3.8-live-extended-thinking。Extended Thinking 支持外部异步 function calling，因此不因语音接口判为不适用；未迁移 Flash 成绩。

最近核验时间：2026-11-04T11:02+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking)

研究备注：
- Scale V2 榜单列出 Gemini 3.8 Flash (mini-swe-agent, high)，未列 Gemini 3.8 Live Extended Thinking；V2 为 642 任务锁定协议。没有复用 Flash 结果。

最近核验时间：2026-11-04T11:02+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 官方动态榜单](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 发布说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 官方 V4 动态榜单直接打开后只呈现表头，未暴露可核对的数据行；发布说明确认 `terminal-bench@4.0.0` 与 resolution-rate 指标，但没有该型号的结果行。

尚未解决的问题：
- 需从可完整读取的官方动态榜单或其他原始资料核验该型号是否有 V4 成绩。

最近核验时间：2026-11-04T11:02+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方结果公告](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Terminal-Bench-Science 当前官方榜单](https://www.terminal-bench-science.ai/)
- [Google Gemini 3.8 Live Extended Thinking 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)

研究备注：
- 官方 0.1 结果公告列出九个被测模型，未列 Gemini 3.8 Live Extended Thinking。当前动态榜单只加载导航和控件，没有结果行；未把普通 Live 或 Gemini Flash 成绩迁移。

尚未解决的问题：
- 无法确认官方发布表之后的动态榜单是否新增该型号。

最近核验时间：2026-11-04T11:02+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)
- [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking)

研究备注：
- Zapier 榜单确认版本 1.0.6，但页面仅展开前 10 项，其余 119 项折叠。可见部分未找到 exact model；该模型支持异步 function calling，但没有核实到 Zapier 榜单代理配置中的结果。

尚未解决的问题：
- 无法核对折叠的 119 项，不能据此断言全榜无此型号。

最近核验时间：2026-11-04T11:02+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld v2.1 官方评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld 官方榜单](https://osworld-v2.xlang.ai/)
- [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking)

研究备注：
- 官方指南确认存在 osworld-v2.1 任务发布；官方榜单页面显示 OSWorld 2.0 标题，但当前抓取只有表头，没有可核对的模型成绩行。未把其他 OSWorld 版本结果视作 v2.1。

尚未解决的问题：
- 榜单数据行不可读取，目标型号在 v2.1 的成绩尚未核验。

最近核验时间：2026-11-04T11:02+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Google Gemini 3.8 Live Extended Thinking 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)

研究备注：
- Surge 官方榜单列出 Gemini 3.8 Flash 等型号，但没有 Gemini 3.8 Live Extended Thinking。该型号支持图像输入和文本输出，适用于图表理解，因此不判为不适用；没有可收录的 exact-model 成绩。

最近核验时间：2026-11-04T11:02+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis HLE 定义与榜单](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Google Gemini 3.8 Audio 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)
- [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/)

研究备注：
- 没有找到该准确型号的原始 HLE 成绩。Google Live 评测方法只列 ServiceNow EVA、AA speech-to-speech 与 τ³-Banking；原始 HLE 为 2,500 道多模态题，不与 HLE-Diamond 混淆。

最近核验时间：2026-11-04T11:02+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis 模型页](https://artificialanalysis.ai/models)
- [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/)

研究备注：
- 没有找到 Gemini 3.8 Live Extended Thinking 的 Index 成绩。AA 当前定义页标为 v5.0.1，并包含 HLE-Diamond；Google Live 评测 PDF 中的 AA 结果类别是 speech-to-speech，不是 Intelligence Index。

最近核验时间：2026-11-04T11:02+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 方法与榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/)

研究备注：
- AA v2.1 可读榜单摘录没有显示该型号。Google Live 评测 PDF 所列项目没有 GDPval-AA；未迁移 Gemini Flash 的 Elo 成绩。

最近核验时间：2026-11-04T11:02+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Google Gemini 3.8 Live Extended Thinking 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking)

研究备注：
- Vals Index v2.2 当前可读榜单包含 Gemini 3.8 Flash，但未列 Gemini 3.8 Live Extended Thinking；未迁移 Flash 结果。

最近核验时间：2026-11-04T11:02+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index 定义",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis 模型页",
          "url": "https://artificialanalysis.ai/models"
        },
        {
          "label": "Google Gemini 3.8 Live 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-live/"
        }
      ],
      "notes": [
        "没有找到 Gemini 3.8 Live Extended Thinking 的 Index 成绩。AA 当前定义页标为 v5.0.1，并包含 HLE-Diamond；Google Live 评测 PDF 中的 AA 结果类别是 speech-to-speech，不是 Intelligence Index。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking"
        }
      ],
      "notes": [
        "Zapier 榜单确认版本 1.0.6，但页面仅展开前 10 项，其余 119 项折叠。可见部分未找到 exact model；该模型支持异步 function calling，但没有核实到 Zapier 榜单代理配置中的结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法核对折叠的 119 项，不能据此断言全榜无此型号。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-8-audio/"
        }
      ],
      "notes": [
        "Surge 官方榜单列出 Gemini 3.8 Flash 等型号，但没有 Gemini 3.8 Live Extended Thinking。该型号支持图像输入和文本输出，适用于图表理解，因此不判为不适用；没有可收录的 exact-model 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方结果页",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking"
        }
      ],
      "notes": [
        "官方 DeepSWE 页面列出 Gemini 3.8 Flash，但未列 gemini-3.8-live-extended-thinking。Extended Thinking 支持外部异步 function calling，因此不因语音接口判为不适用；未迁移 Flash 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 方法与榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Google Gemini 3.8 Live 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-live/"
        }
      ],
      "notes": [
        "AA v2.1 可读榜单摘录没有显示该型号。Google Live 评测 PDF 所列项目没有 GDPval-AA；未迁移 Gemini Flash 的 Elo 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE 定义与榜单",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Google Gemini 3.8 Audio 官方模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-8-audio/"
        },
        {
          "label": "Google Gemini 3.8 Live 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-live/"
        }
      ],
      "notes": [
        "没有找到该准确型号的原始 HLE 成绩。Google Live 评测方法只列 ServiceNow EVA、AA speech-to-speech 与 τ³-Banking；原始 HLE 为 2,500 道多模态题，不与 HLE-Diamond 混淆。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 官方评测指南",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking"
        }
      ],
      "notes": [
        "官方指南确认存在 osworld-v2.1 任务发布；官方榜单页面显示 OSWorld 2.0 标题，但当前抓取只有表头，没有可核对的模型成绩行。未把其他 OSWorld 版本结果视作 v2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单数据行不可读取，目标型号在 v2.1 的成绩尚未核验。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking"
        }
      ],
      "notes": [
        "Scale V2 榜单列出 Gemini 3.8 Flash (mini-swe-agent, high)，未列 Gemini 3.8 Live Extended Thinking；V2 为 642 任务锁定协议。没有复用 Flash 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方结果公告",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Terminal-Bench-Science 当前官方榜单",
          "url": "https://www.terminal-bench-science.ai/"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-8-audio/"
        }
      ],
      "notes": [
        "官方 0.1 结果公告列出九个被测模型，未列 Gemini 3.8 Live Extended Thinking。当前动态榜单只加载导航和控件，没有结果行；未把普通 Live 或 Gemini Flash 成绩迁移。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法确认官方发布表之后的动态榜单是否新增该型号。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 官方动态榜单",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 发布说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "官方 V4 动态榜单直接打开后只呈现表头，未暴露可核对的数据行；发布说明确认 `terminal-bench@4.0.0` 与 resolution-rate 指标，但没有该型号的结果行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需从可完整读取的官方动态榜单或其他原始资料核验该型号是否有 V4 成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T11:02+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Google Gemini 3.8 Live Extended Thinking 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live-extended-thinking"
        }
      ],
      "notes": [
        "Vals Index v2.2 当前可读榜单包含 Gemini 3.8 Flash，但未列 Gemini 3.8 Live Extended Thinking；未迁移 Flash 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T11:02+08:00",
  "model_id": "google/gemini-3.8-live-extended-thinking",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
