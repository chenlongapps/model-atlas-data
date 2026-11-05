# Gemini 3.8 Live Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.8-live
- 模型名称：Gemini 3.8 Live
- 发布日期：2026-09-15
- 最近检查时间：2026-11-04T10:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方结果页](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live) | 2026-11-04T10:58+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live) | 2026-11-04T10:58+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 官方动态榜单](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 发布说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T10:58+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 官方结果公告](https://www.tbench.ai/news/terminal-bench-science-0-1), [Terminal-Bench-Science 当前官方榜单](https://www.terminal-bench-science.ai/), [Google Gemini 3.8 Live 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/) | 2026-11-04T10:58+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench), [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live) | 2026-11-04T10:58+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld v2.1 官方评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld 官方榜单](https://osworld-v2.xlang.ai/), [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live) | 2026-11-04T10:58+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Google Gemini 3.8 Live 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/) | 2026-11-04T10:58+08:00 |
| humanitys-last-exam | 未找到 | — | [Artificial Analysis HLE 评测定义与榜单](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Google Gemini 3.8 Audio 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/), [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/) | 2026-11-04T10:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis 模型搜索/型号页](https://artificialanalysis.ai/models), [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/) | 2026-11-04T10:58+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 方法与榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/) | 2026-11-04T10:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live) | 2026-11-04T10:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方结果页](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live)

研究备注：
- 官方 DeepSWE 页面列出 Gemini 3.8 Flash，但未列 Gemini 3.8 Live。Live 支持 function calling，因此没有仅按语音用途判断不适用；没有把 Flash 结果迁移到 Live。

最近核验时间：2026-11-04T10:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live)

研究备注：
- Scale V2 榜单列出 Gemini 3.8 Flash (mini-swe-agent, high)，未列 Gemini 3.8 Live。V2 为 642 任务协议；未复用 Flash 成绩。

最近核验时间：2026-11-04T10:58+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 官方动态榜单](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 发布说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 官方 V4 动态榜单在本次直接打开后只呈现表头，未暴露可核对的数据行；发布说明确认版本 4.0.0 与 resolution-rate 指标，但未列出 Gemini 3.8 Live。因动态榜单抽取不完整，不将缺少数据行视为未找到。

尚未解决的问题：
- 需要从可完整读取的官方动态榜单或其他原始来源核验 Gemini 3.8 Live 是否有 V4 成绩。

最近核验时间：2026-11-04T10:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方结果公告](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Terminal-Bench-Science 当前官方榜单](https://www.terminal-bench-science.ai/)
- [Google Gemini 3.8 Live 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)

研究备注：
- 官方 0.1 结果公告所列九个模型中没有 Gemini 3.8 Live。当前动态 leaderboard 只返回页面框架，无法检查后来是否新增结果；不将其他 Gemini 型号或 Live Extended Thinking 成绩迁移。

尚未解决的问题：
- 当前官方榜单结果行不可读取，无法判断公告之后是否新增 Gemini 3.8 Live。

最近核验时间：2026-11-04T10:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)
- [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live)

研究备注：
- 榜单标注 AutomationBench 1.0.6，但页面只展开前 10 项，并另有 119 项折叠记录；可见区域未找到 Gemini 3.8 Live。该型号支持 function calling，不因实时语音属性直接判定不适用。

尚未解决的问题：
- 折叠榜单其余记录不可见，不能断言全榜不存在 Gemini 3.8 Live。

最近核验时间：2026-11-04T10:58+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld v2.1 官方评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld 官方榜单](https://osworld-v2.xlang.ai/)
- [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live)

研究备注：
- 官方指南确认存在 osworld-v2.1 任务发布。官方排行榜显示 OSWorld 2.0 标题，但当前抓取仅返回表头，没有可核对的 Live 行；没有用其他 OSWorld 版本替代。

尚未解决的问题：
- 官方榜单数据行当前不可完整读取，目标型号与 v2.1 的成绩仍待核验。

最近核验时间：2026-11-04T10:58+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Google Gemini 3.8 Live 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)

研究备注：
- Surge 官方榜单中可见 Gemini 3.8 Flash 等型号，但未见 Gemini 3.8 Live。Live 支持图像输入且输出文本，故不判为不适用；未移用 Flash 结果。

最近核验时间：2026-11-04T10:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis HLE 评测定义与榜单](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Google Gemini 3.8 Audio 官方模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)
- [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/)

研究备注：
- AA 原始 HLE 页面没有可见的 Gemini 3.8 Live 成绩行。Google Live 评测方法列出 ServiceNow EVA、AA speech-to-speech 与 τ³-Banking，没有列 HLE；未使用 Gemini Flash 或 Live Extended Thinking 成绩。

最近核验时间：2026-11-04T10:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis 模型搜索/型号页](https://artificialanalysis.ai/models)
- [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/)

研究备注：
- 未找到 Gemini 3.8 Live 的 AA Intelligence Index 记录。AA 当前定义页标为 v5.0.1，包含 HLE-Diamond；Google Live 评测 PDF 所列 AA 项目是 speech-to-speech，不是 Intelligence Index。未将 Gemini 3.8 Flash 指数成绩迁移。

最近核验时间：2026-11-04T10:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 方法与榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Google Gemini 3.8 Live 评测方法](https://deepmind.google/models/evals-methodology/gemini-3-8-live/)

研究备注：
- AA v2.1 的可读榜单片段没有显示 Gemini 3.8 Live。Google Live 评测方法列出 ServiceNow EVA、AA speech-to-speech 与 τ³-Banking，没有列 GDPval；没有把 Flash 成绩迁移到 Live。

最近核验时间：2026-11-04T10:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Google Gemini 3.8 Live 官方模型页](https://aistudio.google.com/docs/models/gemini-3.8-live)

研究备注：
- Vals Index v2.2 可读榜单中包含 Gemini 3.8 Flash，但未列 Gemini 3.8 Live。该综合评测跨 finance、coding、legal 和 tax；未移用 Flash 成绩。

最近核验时间：2026-11-04T10:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T10:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index 定义",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis 模型搜索/型号页",
          "url": "https://artificialanalysis.ai/models"
        },
        {
          "label": "Google Gemini 3.8 Live 评测方法",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-8-live/"
        }
      ],
      "notes": [
        "未找到 Gemini 3.8 Live 的 AA Intelligence Index 记录。AA 当前定义页标为 v5.0.1，包含 HLE-Diamond；Google Live 评测 PDF 所列 AA 项目是 speech-to-speech，不是 Intelligence Index。未将 Gemini 3.8 Flash 指数成绩迁移。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T10:58+08:00",
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
          "label": "Google Gemini 3.8 Live 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live"
        }
      ],
      "notes": [
        "榜单标注 AutomationBench 1.0.6，但页面只展开前 10 项，并另有 119 项折叠记录；可见区域未找到 Gemini 3.8 Live。该型号支持 function calling，不因实时语音属性直接判定不适用。"
      ],
      "status": "待核实",
      "unresolved": [
        "折叠榜单其余记录不可见，不能断言全榜不存在 Gemini 3.8 Live。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T10:58+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Google Gemini 3.8 Live 官方模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-8-audio/"
        }
      ],
      "notes": [
        "Surge 官方榜单中可见 Gemini 3.8 Flash 等型号，但未见 Gemini 3.8 Live。Live 支持图像输入且输出文本，故不判为不适用；未移用 Flash 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T10:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方结果页",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Google Gemini 3.8 Live 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live"
        }
      ],
      "notes": [
        "官方 DeepSWE 页面列出 Gemini 3.8 Flash，但未列 Gemini 3.8 Live。Live 支持 function calling，因此没有仅按语音用途判断不适用；没有把 Flash 结果迁移到 Live。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T10:58+08:00",
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
        "AA v2.1 的可读榜单片段没有显示 Gemini 3.8 Live。Google Live 评测方法列出 ServiceNow EVA、AA speech-to-speech 与 τ³-Banking，没有列 GDPval；没有把 Flash 成绩迁移到 Live。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T10:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE 评测定义与榜单",
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
        "AA 原始 HLE 页面没有可见的 Gemini 3.8 Live 成绩行。Google Live 评测方法列出 ServiceNow EVA、AA speech-to-speech 与 τ³-Banking，没有列 HLE；未使用 Gemini Flash 或 Live Extended Thinking 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T10:58+08:00",
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
          "label": "Google Gemini 3.8 Live 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live"
        }
      ],
      "notes": [
        "官方指南确认存在 osworld-v2.1 任务发布。官方排行榜显示 OSWorld 2.0 标题，但当前抓取仅返回表头，没有可核对的 Live 行；没有用其他 OSWorld 版本替代。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单数据行当前不可完整读取，目标型号与 v2.1 的成绩仍待核验。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T10:58+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "Google Gemini 3.8 Live 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live"
        }
      ],
      "notes": [
        "Scale V2 榜单列出 Gemini 3.8 Flash (mini-swe-agent, high)，未列 Gemini 3.8 Live。V2 为 642 任务协议；未复用 Flash 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T10:58+08:00",
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
          "label": "Google Gemini 3.8 Live 官方模型卡",
          "url": "https://deepmind.google/models/model-cards/gemini-3-8-audio/"
        }
      ],
      "notes": [
        "官方 0.1 结果公告所列九个模型中没有 Gemini 3.8 Live。当前动态 leaderboard 只返回页面框架，无法检查后来是否新增结果；不将其他 Gemini 型号或 Live Extended Thinking 成绩迁移。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前官方榜单结果行不可读取，无法判断公告之后是否新增 Gemini 3.8 Live。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T10:58+08:00",
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
        "官方 V4 动态榜单在本次直接打开后只呈现表头，未暴露可核对的数据行；发布说明确认版本 4.0.0 与 resolution-rate 指标，但未列出 Gemini 3.8 Live。因动态榜单抽取不完整，不将缺少数据行视为未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要从可完整读取的官方动态榜单或其他原始来源核验 Gemini 3.8 Live 是否有 V4 成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T10:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Google Gemini 3.8 Live 官方模型页",
          "url": "https://aistudio.google.com/docs/models/gemini-3.8-live"
        }
      ],
      "notes": [
        "Vals Index v2.2 可读榜单中包含 Gemini 3.8 Flash，但未列 Gemini 3.8 Live。该综合评测跨 finance、coding、legal 和 tax；未移用 Flash 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T10:58+08:00",
  "model_id": "google/gemini-3.8-live",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
