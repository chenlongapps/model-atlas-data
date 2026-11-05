# CoBuddy Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：baidu/cobuddy
- 模型名称：CoBuddy
- 发布日期：2026-05-06
- 最近检查时间：2026-11-05T06:28+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地文件描述为支持工具的代码生成 agent，但本轮未找到百度官方模型卡或 API 页面确认其精确 API ID/版本和 2026-05-06 发布日；百度官方案例文章只确认 CoBuddy 产品和代码生成用途。 benchmark 结果均未核实到可写入分数。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:28+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:28+08:00 |
| terminal-bench-v4 | 待核实 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [Terminal-Bench 4 official evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:28+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [Terminal-Bench Science official evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:28+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T06:28+08:00 |
| osworld-v2.1 | 待核实 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld official runner (a11y_tree support)](https://github.com/xlang-ai/OSWorld-V2/blob/main/scripts/python/run_multienv_claude.py), [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/) | 2026-11-05T06:28+08:00 |
| chartography | 不适用 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [Chartography official task repository](https://github.com/surge-ai/chartography), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:28+08:00 |
| humanitys-last-exam | 未找到 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [Humanity's Last Exam official evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:28+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:28+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy), [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:28+08:00 |
| vals-index-v2.2 | 未找到 | — | [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535), [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:28+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 百度官方资料确认 CoBuddy 用于代码生成和 Agent，但没有精确模型/API 版本的官方榜单项；DeepSWE 当前可读榜单仅显示 21/28 models、57/70 configs。

尚未解决的问题：
- 榜单未展示的配置中是否有本地 baidu/cobuddy 对应型号尚未确认；官方 API ID/具体版本也需补证。

最近核验时间：2026-11-05T06:28+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查 Scale 官方当前 V2 公榜未见精确 CoBuddy 型号；未将其他百度或 ERNIE 型号的成绩映射过来。

最近核验时间：2026-11-05T06:28+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [Terminal-Bench 4 official evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 本地 TOML 标注为支持工具的代码 agent，任务类型可能适用；AA 当前榜面仅显示 28/240 models，未见精确型号且视图不完整。

尚未解决的问题：
- 需核实未展示榜单结果中是否存在精确 CoBuddy 型号及分数。

最近核验时间：2026-11-05T06:28+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [Terminal-Bench Science official evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 本地 TOML 标注支持工具；AA 当前榜面仅显示 28/120 models，未见精确型号且视图不完整。

尚未解决的问题：
- 需核实未展示榜单结果中是否存在精确 CoBuddy 型号及分数。

最近核验时间：2026-11-05T06:28+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- 本地 TOML 标注文本输入/输出及工具支持，工作流可能适用；Zapier 榜单当前只显示前 10 项并折叠 119 条，无法确认是否有精确 CoBuddy 结果。

尚未解决的问题：
- 需要可访问完整榜单或原始评测记录确认成绩。

最近核验时间：2026-11-05T06:28+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld official runner (a11y_tree support)](https://github.com/xlang-ai/OSWorld-V2/blob/main/scripts/python/run_multienv_claude.py)
- [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)

研究备注：
- 本地 TOML 为文本输入/输出且支持工具。OSWorld 官方 runner 支持 a11y_tree 观察配置，因此不能仅凭无图像输入判为不适用；动态官方榜单当前视图未显示精确型号。

尚未解决的问题：
- 需要核查其他榜单版本/数据集视图或维护者验证的原始记录。

最近核验时间：2026-11-05T06:28+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [Chartography official task repository](https://github.com/surge-ai/chartography)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 本地模型只接收文本；Chartography 每项任务都要求模型读取图表图像。不能将其他视觉模型提供的图表描述当作 CoBuddy 自身成绩。

最近核验时间：2026-11-05T06:28+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [Humanity's Last Exam official evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 检查 HLE 官方结果页和可见 CoBuddy 产品资料，未找到精确 CoBuddy 型号的原始 HLE 成绩。

最近核验时间：2026-11-05T06:28+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前 Intelligence Index V5 榜单/方法资料未见精确 CoBuddy 型号；未以其他百度模型结果代替。

最近核验时间：2026-11-05T06:28+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy)
- [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 检查 GDPval-AA v2.1 官方评测页及可见 CoBuddy 资料，未找到精确型号的可核实成绩。

最近核验时间：2026-11-05T06:28+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Baidu CoBuddy code-generation case article](https://cloud.baidu.com/article/8387535)
- [OpenRouter Baidu CoBuddy model directory](https://openrouter.ai/baidu/cobuddy)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 Vals Index v2.2 官方页面未列精确 CoBuddy 型号；缺席不代表确认从未评测。

最近核验时间：2026-11-05T06:28+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "OpenRouter Baidu CoBuddy model directory",
          "url": "https://openrouter.ai/baidu/cobuddy"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前 Intelligence Index V5 榜单/方法资料未见精确 CoBuddy 型号；未以其他百度模型结果代替。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "本地 TOML 标注文本输入/输出及工具支持，工作流可能适用；Zapier 榜单当前只显示前 10 项并折叠 119 条，无法确认是否有精确 CoBuddy 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可访问完整榜单或原始评测记录确认成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "Chartography official task repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "本地模型只接收文本；Chartography 每项任务都要求模型读取图表图像。不能将其他视觉模型提供的图表描述当作 CoBuddy 自身成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "百度官方资料确认 CoBuddy 用于代码生成和 Agent，但没有精确模型/API 版本的官方榜单项；DeepSWE 当前可读榜单仅显示 21/28 models、57/70 configs。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单未展示的配置中是否有本地 baidu/cobuddy 对应型号尚未确认；官方 API ID/具体版本也需补证。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "OpenRouter Baidu CoBuddy model directory",
          "url": "https://openrouter.ai/baidu/cobuddy"
        },
        {
          "label": "GDPval-AA v2.1 official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "检查 GDPval-AA v2.1 官方评测页及可见 CoBuddy 资料，未找到精确型号的可核实成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "Humanity's Last Exam official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "检查 HLE 官方结果页和可见 CoBuddy 产品资料，未找到精确 CoBuddy 型号的原始 HLE 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld official runner (a11y_tree support)",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/scripts/python/run_multienv_claude.py"
        },
        {
          "label": "OpenRouter Baidu CoBuddy model directory",
          "url": "https://openrouter.ai/baidu/cobuddy"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "本地 TOML 为文本输入/输出且支持工具。OSWorld 官方 runner 支持 a11y_tree 观察配置，因此不能仅凭无图像输入判为不适用；动态官方榜单当前视图未显示精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要核查其他榜单版本/数据集视图或维护者验证的原始记录。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查 Scale 官方当前 V2 公榜未见精确 CoBuddy 型号；未将其他百度或 ERNIE 型号的成绩映射过来。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "Terminal-Bench Science official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "本地 TOML 标注支持工具；AA 当前榜面仅显示 28/120 models，未见精确型号且视图不完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实未展示榜单结果中是否存在精确 CoBuddy 型号及分数。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "Terminal-Bench 4 official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "本地 TOML 标注为支持工具的代码 agent，任务类型可能适用；AA 当前榜面仅显示 28/240 models，未见精确型号且视图不完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实未展示榜单结果中是否存在精确 CoBuddy 型号及分数。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:28+08:00",
      "checked_sources": [
        {
          "label": "Baidu CoBuddy code-generation case article",
          "url": "https://cloud.baidu.com/article/8387535"
        },
        {
          "label": "OpenRouter Baidu CoBuddy model directory",
          "url": "https://openrouter.ai/baidu/cobuddy"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 Vals Index v2.2 官方页面未列精确 CoBuddy 型号；缺席不代表确认从未评测。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:28+08:00",
  "model_id": "baidu/cobuddy",
  "model_notes": [
    "本地文件描述为支持工具的代码生成 agent，但本轮未找到百度官方模型卡或 API 页面确认其精确 API ID/版本和 2026-05-06 发布日；百度官方案例文章只确认 CoBuddy 产品和代码生成用途。 benchmark 结果均未核实到可写入分数。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
