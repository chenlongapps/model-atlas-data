# GPT-Realtime-2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-realtime-2
- 模型名称：GPT-Realtime-2
- 发布日期：2026-05-07
- 最近检查时间：2026-11-05T06:22+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方模型文档确认模型 ID 为 gpt-realtime-2，支持语音、图像、文本和工具调用；OpenAI 发布记录确认日期为 2026-05-07，与本地 release_date 相符。AA 的语音专项成绩不属于本轮 11 项 Benchmark。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:22+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:22+08:00 |
| terminal-bench-v4 | 待核实 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Terminal-Bench 4 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?efforts=all&version=4.0) | 2026-11-05T06:22+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Terminal-Bench Science evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:22+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-05T06:22+08:00 |
| osworld-v2.1 | 待核实 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:22+08:00 |
| chartography | 未找到 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official task repository](https://github.com/surge-ai/chartography) | 2026-11-05T06:22+08:00 |
| humanitys-last-exam | 未找到 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Humanity's Last Exam official evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:22+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:22+08:00 |
| vals-index-v2.2 | 未找到 | — | [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE 官方可读取榜单仅显示部分型号和配置，当前可见行未列 GPT-Realtime-2；页面不完整，不能据此判定没有成绩。

尚未解决的问题：
- 需核实榜单未展示配置中是否有精确模型结果。

最近核验时间：2026-11-05T06:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查 Scale 官方 V2 榜单未见精确 GPT-Realtime-2 结果。模型支持 function calling，但没有因此推断其参加过该评测。

最近核验时间：2026-11-05T06:22+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Terminal-Bench 4 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?efforts=all&version=4.0)

研究备注：
- AA 可读取的 Terminal-Bench 4 列表只展示部分结果（28/240 models），tbench.ai 可见视图也未见精确型号；不能据此排除隐藏/其他配置成绩。

尚未解决的问题：
- 需核实完整榜单及其他 harness/effort 配置。

最近核验时间：2026-11-05T06:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Terminal-Bench Science evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA Terminal-Bench Science 页面可读取视图只展示部分结果（28/120 models），未见精确型号；可见表不完整。

尚未解决的问题：
- 需核实榜单其余结果中是否有 GPT-Realtime-2。

最近核验时间：2026-11-05T06:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- 模型支持工具调用且任务类型可能适用；Zapier 榜单折叠 119 条，无法确认精确型号是否出现。

尚未解决的问题：
- 需核实官方榜单折叠行中的精确型号和成绩。

最近核验时间：2026-11-05T06:22+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型支持图像输入、文本输出及 function calling；官方榜单带动态筛选，当前可见视图未见精确型号。

尚未解决的问题：
- 需检查其他版本/数据集视图或原始结果数据。

最近核验时间：2026-11-05T06:22+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official task repository](https://github.com/surge-ai/chartography)

研究备注：
- 图像输入和文本输出与图表问答形式相符；检查 Surge 官方榜单未见精确 GPT-Realtime-2 型号或可核实成绩。

最近核验时间：2026-11-05T06:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Humanity's Last Exam official evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 检查 OpenAI 模型资料及 AA 官方 HLE 页面，未发现精确 GPT-Realtime-2 成绩。AA 的语音专属结果不是 HLE。

最近核验时间：2026-11-05T06:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 检查 Artificial Analysis Intelligence Index V5 方法/公开结果页，未发现精确 GPT-Realtime-2 V5 成绩；未将语音专项评测映射为综合指数。

最近核验时间：2026-11-05T06:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 检查 AA GDPval-AA v2.1 方法和公开结果页，未发现精确 GPT-Realtime-2 成绩。

最近核验时间：2026-11-05T06:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-Realtime-2 model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查 Vals Index v2.2 官方当前页面，未发现 GPT-Realtime-2 精确型号。

最近核验时间：2026-11-05T06:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "检查 Artificial Analysis Intelligence Index V5 方法/公开结果页，未发现精确 GPT-Realtime-2 V5 成绩；未将语音专项评测映射为综合指数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "模型支持工具调用且任务类型可能适用；Zapier 榜单折叠 119 条，无法确认精确型号是否出现。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实官方榜单折叠行中的精确型号和成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official task repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "图像输入和文本输出与图表问答形式相符；检查 Surge 官方榜单未见精确 GPT-Realtime-2 型号或可核实成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE 官方可读取榜单仅显示部分型号和配置，当前可见行未列 GPT-Realtime-2；页面不完整，不能据此判定没有成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实榜单未展示配置中是否有精确模型结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "检查 AA GDPval-AA v2.1 方法和公开结果页，未发现精确 GPT-Realtime-2 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Humanity's Last Exam official evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "检查 OpenAI 模型资料及 AA 官方 HLE 页面，未发现精确 GPT-Realtime-2 成绩。AA 的语音专属结果不是 HLE。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型支持图像输入、文本输出及 function calling；官方榜单带动态筛选，当前可见视图未见精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查其他版本/数据集视图或原始结果数据。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查 Scale 官方 V2 榜单未见精确 GPT-Realtime-2 结果。模型支持 function calling，但没有因此推断其参加过该评测。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Terminal-Bench Science evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA Terminal-Bench Science 页面可读取视图只展示部分结果（28/120 models），未见精确型号；可见表不完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实榜单其余结果中是否有 GPT-Realtime-2。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Terminal-Bench 4 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        }
      ],
      "notes": [
        "AA 可读取的 Terminal-Bench 4 列表只展示部分结果（28/240 models），tbench.ai 可见视图也未见精确型号；不能据此排除隐藏/其他配置成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实完整榜单及其他 harness/effort 配置。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-Realtime-2 model documentation",
          "url": "https://developers.openai.com/api/docs/models/gpt-realtime-2"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "检查 Vals Index v2.2 官方当前页面，未发现 GPT-Realtime-2 精确型号。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:22+08:00",
  "model_id": "openai/gpt-realtime-2",
  "model_notes": [
    "官方模型文档确认模型 ID 为 gpt-realtime-2，支持语音、图像、文本和工具调用；OpenAI 发布记录确认日期为 2026-05-07，与本地 release_date 相符。AA 的语音专项成绩不属于本轮 11 项 Benchmark。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
