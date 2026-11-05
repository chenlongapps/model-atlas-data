# Grok Voice 3.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-voice-3.0
- 模型名称：Grok Voice 3.0
- 发布日期：2026-10-14
- 最近检查时间：2026-11-04T02:48+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 method and results](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T02:48+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale Labs SWE-bench Pro V2 full leaderboard and methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:48+08:00 |
| terminal-bench-v4 | 未找到 | — | [Vals AI Terminal-Bench 4 leaderboard and methodology](https://www.vals-ai.com/benchmarks/terminal-bench-4) | 2026-11-04T02:48+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Artificial Analysis Terminal-Bench-Science evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Terminal-Bench-Science project](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T02:48+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier Benchmarks](https://zapier.com/benchmarks), [xAI Realtime speech-to-speech and tools documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech) | 2026-11-04T02:48+08:00 |
| osworld-v2.1 | 不适用 | — | [Grok Voice 3.0 model documentation](https://docs.x.ai/developers/models/grok-voice-3.0), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T02:48+08:00 |
| chartography | 不适用 | — | [Chartography original paper](https://arxiv.org/html/2608.10677v1), [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Grok Voice 3.0 model documentation](https://docs.x.ai/developers/models/grok-voice-3.0) | 2026-11-04T02:48+08:00 |
| humanitys-last-exam | 待核实 | — | [Humanity’s Last Exam official site](https://lastexam.ai/), [HLE official repository](https://github.com/centerforaisafety/hle), [xAI Realtime API documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech), [xAI Grok Voice 3 release announcement](https://x.ai/news/grok-voice-3) | 2026-11-04T02:48+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [xAI Grok Voice 3 announcement](https://x.ai/news/grok-voice-3) | 2026-11-04T02:48+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [xAI Realtime API documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech) | 2026-11-04T02:48+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index V2.2](https://www.vals.ai/benchmarks/vals_index), [xAI Realtime API documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech) | 2026-11-04T02:48+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 method and results](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 已核对 Grok Voice 3.0 精确名称未列出；榜单可见的是 Grok 4.6，不能移用其他模型版本的成绩。

最近核验时间：2026-11-04T02:48+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale Labs SWE-bench Pro V2 full leaderboard and methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 已核对 V2 榜单中没有 Grok Voice 3.0 或 Grok 精确匹配。该页面说明 V2 使用 642 个任务及锁定的 endpoint 评测协议。

最近核验时间：2026-11-04T02:48+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Terminal-Bench 4 leaderboard and methodology](https://www.vals-ai.com/benchmarks/terminal-bench-4)

研究备注：
- 页面未列出 Grok Voice 3.0，存在其他 Grok 版本。协议使用 mini-swe-agent、bash 工具和终端 sandbox，未将其他版本分数转用。

最近核验时间：2026-11-04T02:48+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Terminal-Bench-Science evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Terminal-Bench-Science project](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- 官方评测页面说明该套件包含 70 个终端研究工作流，采用 mini-swe-agent，并报告 pass@1 三次均值。页面动态图表只暴露部分模型文本，无法从可读页面确认 Grok Voice 3.0 是否在完整数据中。

尚未解决的问题：
- 需在公开可读的完整模型数据中复核 Grok Voice 3.0；没有写入分数。

最近核验时间：2026-11-04T02:48+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier Benchmarks](https://zapier.com/benchmarks)
- [xAI Realtime speech-to-speech and tools documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech)

研究备注：
- Zapier AutomationBench 1.0.6 评测 47 种工具的端到端工作流；Grok Voice 3.0 Realtime API 支持文本输入和函数工具调用。榜单文本含 See 119 more 折叠结果，未能验证完整名单。

尚未解决的问题：
- 完整公开榜单中是否包含 Grok Voice 3.0 尚未核实；通过适配器参评及其成绩均没有证据。

最近核验时间：2026-11-04T02:48+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Grok Voice 3.0 model documentation](https://docs.x.ai/developers/models/grok-voice-3.0)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld-V2.1 的标准计算机使用协议以屏幕截图作为观察。Grok Voice 3.0 的标准输入为文本和音频，官方接口资料未提供任意截图输入，无法遵循该基准观察协议。

最近核验时间：2026-11-04T02:48+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Chartography original paper](https://arxiv.org/html/2608.10677v1)
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Grok Voice 3.0 model documentation](https://docs.x.ai/developers/models/grok-voice-3.0)

研究备注：
- 原始协议要求接收图表图像及问题并输出自由文本答案，且不使用工具。Grok Voice 3.0 标准接口不支持图像输入；榜单中的其他 Grok 版本不适用于此模型。

最近核验时间：2026-11-04T02:48+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Humanity’s Last Exam official site](https://lastexam.ai/)
- [HLE official repository](https://github.com/centerforaisafety/hle)
- [xAI Realtime API documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech)
- [xAI Grok Voice 3 release announcement](https://x.ai/news/grok-voice-3)

研究备注：
- 原始 HLE 是 2,500 题，含选择题和短答；模型 Realtime API 支持文本输入及文本输出，因此形式上可回答。未找到该准确模型的原始 HLE 成绩；xAI 公告列出的语音专项成绩属于其他基准。官方提交看板需要登录，未尝试绕过访问控制。

尚未解决的问题：
- 无法在不登录的官方提交看板中核实是否有该模型条目；未将 HLE-Diamond 或其他 Grok 版本结果代入。

最近核验时间：2026-11-04T02:48+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [xAI Grok Voice 3 announcement](https://x.ai/news/grok-voice-3)

研究备注：
- AA V5 页面未找到 Grok Voice 3.0 条目；方法说明语音输入单独评测。xAI 公布的 AA Speech-to-Speech Index 86.9 属于另一评测，不作为 V5 成绩。

最近核验时间：2026-11-04T02:48+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [xAI Realtime API documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech)

研究备注：
- 官方页面未找到 Grok Voice 3.0 精确条目。GDPval-AA 使用 shell 和网页浏览 agent loop，并要求文档、幻灯片、图表及表格等工作产物；Realtime API 的文本和工具能力没有证明其符合该标准 harness，未借用 Grok 4.7 或 v2 成绩。

最近核验时间：2026-11-04T02:48+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index V2.2](https://www.vals.ai/benchmarks/vals_index)
- [xAI Realtime API documentation](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech)

研究备注：
- 官方 V2.2 页面未找到 Grok Voice 3.0 精确条目；榜单中的 Grok 4.7 不是同一模型。该 Index 包含 Excel 建模、终端编程和端到端应用工作等 agent 任务，Realtime 语音接口是否符合标准 harness 未证实。

最近核验时间：2026-11-04T02:48+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis intelligence benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "xAI Grok Voice 3 announcement",
          "url": "https://x.ai/news/grok-voice-3"
        }
      ],
      "notes": [
        "AA V5 页面未找到 Grok Voice 3.0 条目；方法说明语音输入单独评测。xAI 公布的 AA Speech-to-Speech Index 86.9 属于另一评测，不作为 V5 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Zapier Benchmarks",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "xAI Realtime speech-to-speech and tools documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech"
        }
      ],
      "notes": [
        "Zapier AutomationBench 1.0.6 评测 47 种工具的端到端工作流；Grok Voice 3.0 Realtime API 支持文本输入和函数工具调用。榜单文本含 See 119 more 折叠结果，未能验证完整名单。"
      ],
      "status": "待核实",
      "unresolved": [
        "完整公开榜单中是否包含 Grok Voice 3.0 尚未核实；通过适配器参评及其成绩均没有证据。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Chartography original paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Grok Voice 3.0 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-voice-3.0"
        }
      ],
      "notes": [
        "原始协议要求接收图表图像及问题并输出自由文本答案，且不使用工具。Grok Voice 3.0 标准接口不支持图像输入；榜单中的其他 Grok 版本不适用于此模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 method and results",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "已核对 Grok Voice 3.0 精确名称未列出；榜单可见的是 Grok 4.6，不能移用其他模型版本的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "xAI Realtime API documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech"
        }
      ],
      "notes": [
        "官方页面未找到 Grok Voice 3.0 精确条目。GDPval-AA 使用 shell 和网页浏览 agent loop，并要求文档、幻灯片、图表及表格等工作产物；Realtime API 的文本和工具能力没有证明其符合该标准 harness，未借用 Grok 4.7 或 v2 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Humanity’s Last Exam official site",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "HLE official repository",
          "url": "https://github.com/centerforaisafety/hle"
        },
        {
          "label": "xAI Realtime API documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech"
        },
        {
          "label": "xAI Grok Voice 3 release announcement",
          "url": "https://x.ai/news/grok-voice-3"
        }
      ],
      "notes": [
        "原始 HLE 是 2,500 题，含选择题和短答；模型 Realtime API 支持文本输入及文本输出，因此形式上可回答。未找到该准确模型的原始 HLE 成绩；xAI 公告列出的语音专项成绩属于其他基准。官方提交看板需要登录，未尝试绕过访问控制。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法在不登录的官方提交看板中核实是否有该模型条目；未将 HLE-Diamond 或其他 Grok 版本结果代入。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Grok Voice 3.0 model documentation",
          "url": "https://docs.x.ai/developers/models/grok-voice-3.0"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld-V2.1 的标准计算机使用协议以屏幕截图作为观察。Grok Voice 3.0 的标准输入为文本和音频，官方接口资料未提供任意截图输入，无法遵循该基准观察协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Scale Labs SWE-bench Pro V2 full leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "已核对 V2 榜单中没有 Grok Voice 3.0 或 Grok 精确匹配。该页面说明 V2 使用 642 个任务及锁定的 endpoint 评测协议。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Terminal-Bench-Science evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science project",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "官方评测页面说明该套件包含 70 个终端研究工作流，采用 mini-swe-agent，并报告 pass@1 三次均值。页面动态图表只暴露部分模型文本，无法从可读页面确认 Grok Voice 3.0 是否在完整数据中。"
      ],
      "status": "待核实",
      "unresolved": [
        "需在公开可读的完整模型数据中复核 Grok Voice 3.0；没有写入分数。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4 leaderboard and methodology",
          "url": "https://www.vals-ai.com/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "页面未列出 Grok Voice 3.0，存在其他 Grok 版本。协议使用 mini-swe-agent、bash 工具和终端 sandbox，未将其他版本分数转用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:48+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "xAI Realtime API documentation",
          "url": "https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech"
        }
      ],
      "notes": [
        "官方 V2.2 页面未找到 Grok Voice 3.0 精确条目；榜单中的 Grok 4.7 不是同一模型。该 Index 包含 Excel 建模、终端编程和端到端应用工作等 agent 任务，Realtime 语音接口是否符合标准 harness 未证实。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:48+08:00",
  "model_id": "xai/grok-voice-3.0",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
