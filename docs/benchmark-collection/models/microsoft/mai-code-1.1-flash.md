# MAI-Code-1.1-Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：microsoft/mai-code-1.1-flash
- 模型名称：MAI-Code-1.1-Flash
- 发布日期：2026-08-11
- 最近检查时间：2026-11-04T18:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Microsoft 页面链接的 MAI-Code-1-Flash Model Card 明确是旧版 MAI-Code-1-Flash（1.0，2026-06-02），未将其中 SWE-Bench Pro、Terminal-Bench 2 或 HLE 成绩移用到 1.1。
- Microsoft 1.1 公告只提到 GitHub Copilot CLI 场景下 Terminal-Bench 2.1 的相对改进 22%，未公布 11 项目标 Benchmark 的绝对成绩；公告时间不是成绩评测日期。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [Official DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) | 2026-11-04T18:53+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale official SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/), [Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-04T18:53+08:00 |
| terminal-bench-v4 | 待核实 | — | [Official Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [Terminal-Bench 4.0 official release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/), [Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-04T18:53+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals AI Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) | 2026-11-04T18:53+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks), [Microsoft MAI-Code-1.1-Flash model page](https://microsoft.ai/models/mai-code-1-flash/) | 2026-11-04T18:53+08:00 |
| osworld-v2.1 | 待核实 | — | [Official OSWorld project site](https://osworld-v2.xlang.ai/), [Official OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [Microsoft MAI-Code-1.1-Flash model page](https://microsoft.ai/models/mai-code-1-flash/) | 2026-11-04T18:53+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Official Chartography repository](https://github.com/surge-ai/chartography), [Microsoft MAI-Code-1.1-Flash model page](https://microsoft.ai/models/mai-code-1-flash/) | 2026-11-04T18:53+08:00 |
| humanitys-last-exam | 未找到 | — | [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/), [Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-04T18:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) | 2026-11-04T18:53+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) | 2026-11-04T18:53+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) | 2026-11-04T18:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Official DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)

研究备注：
- 已检查官方 DeepSWE v1.1 榜单和 Microsoft 1.1 公告，未找到 MAI-Code-1.1-Flash 精确版本的公开结果。

最近核验时间：2026-11-04T18:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale official SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)
- [Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 已检查 Scale 官方 V2 完整榜单和 Microsoft 资料，未找到 MAI-Code-1.1-Flash 的 V2 结果。Microsoft 旧卡中的 SWE-Bench Pro 51.2 属于 MAI-Code-1-Flash（1.0），且未注明 V2，不移用。

最近核验时间：2026-11-04T18:53+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Official Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [Terminal-Bench 4.0 official release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)
- [Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 已检查 Terminal-Bench 4.0 官方榜单和发布说明及 Microsoft 1.1 公告。官方榜单网页读取时没有呈现模型数据行，暂不能确认是否有该模型结果。Microsoft 公告提及的是 Terminal-Bench 2.1 的相对提升，不是 4.0 的绝对分数。

尚未解决的问题：
- 官方 Terminal-Bench 4.0 榜单通过浏览器读取时未呈现数据行；需在排行榜恢复可见后复查 MAI-Code-1.1-Flash。

最近核验时间：2026-11-04T18:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)

研究备注：
- 已检查 Vals AI 官方榜单和 Microsoft 1.1 资料；公开表中未找到 MAI-Code-1.1-Flash 行。

最近核验时间：2026-11-04T18:53+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks)
- [Microsoft MAI-Code-1.1-Flash model page](https://microsoft.ai/models/mai-code-1-flash/)

研究备注：
- Zapier 官方榜单只显示前 10 行并将其余 119 行折叠，当前无法确认折叠数据中是否有 MAI-Code-1.1-Flash。

尚未解决的问题：
- Zapier 榜单折叠的 119 行中是否存在 MAI-Code-1.1-Flash 尚无法确认。

最近核验时间：2026-11-04T18:53+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Official OSWorld project site](https://osworld-v2.xlang.ai/)
- [Official OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [Microsoft MAI-Code-1.1-Flash model page](https://microsoft.ai/models/mai-code-1-flash/)

研究备注：
- 已检查 OSWorld 官方站和 v2 仓库。仓库确认 v2.1 发布，但官方站当前介绍 OSWorld 2.0，交互式榜单未呈现可核对的 MAI-Code 行；暂列待核实而非认定不适用。

尚未解决的问题：
- OSWorld v2.1 官方交互榜单未能显示可核对模型行；需要可读的 v2.1 榜单数据继续核验。

最近核验时间：2026-11-04T18:53+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Official Chartography repository](https://github.com/surge-ai/chartography)
- [Microsoft MAI-Code-1.1-Flash model page](https://microsoft.ai/models/mai-code-1-flash/)

研究备注：
- 已检查 Surge AI 官方榜单和 Chartography 仓库，未找到 MAI-Code-1.1-Flash 成绩。模型支持图像输入，因此该视觉 Benchmark 适用。

最近核验时间：2026-11-04T18:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)
- [Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 已检查 Artificial Analysis HLE 官方页面、方法和 Microsoft 资料，未找到 MAI-Code-1.1-Flash 精确版本行。旧 Microsoft 模型卡中的 HLE 18 属于 MAI-Code-1-Flash（1.0），不可移用。

最近核验时间：2026-11-04T18:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)

研究备注：
- 已检查 Artificial Analysis 当前 v5.0.1 指数榜单和方法，未找到 MAI-Code-1.1-Flash 的综合指数结果。

最近核验时间：2026-11-04T18:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)

研究备注：
- 已检查 Artificial Analysis GDPval-AA v2.1 官方榜单和方法及 Microsoft 公告，未找到 MAI-Code-1.1-Flash 精确版本成绩。

最近核验时间：2026-11-04T18:53+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Microsoft MAI-Code-1.1-Flash announcement](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/)

研究备注：
- 已检查 Vals 官方 v2.2 榜单和 Microsoft 公告，榜单未列出 MAI-Code-1.1-Flash。

最近核验时间：2026-11-04T18:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis 当前 v5.0.1 指数榜单和方法，未找到 MAI-Code-1.1-Flash 的综合指数结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash model page",
          "url": "https://microsoft.ai/models/mai-code-1-flash/"
        }
      ],
      "notes": [
        "Zapier 官方榜单只显示前 10 行并将其余 119 行折叠，当前无法确认折叠数据中是否有 MAI-Code-1.1-Flash。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 榜单折叠的 119 行中是否存在 MAI-Code-1.1-Flash 尚无法确认。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Official Chartography repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash model page",
          "url": "https://microsoft.ai/models/mai-code-1-flash/"
        }
      ],
      "notes": [
        "已检查 Surge AI 官方榜单和 Chartography 仓库，未找到 MAI-Code-1.1-Flash 成绩。模型支持图像输入，因此该视觉 Benchmark 适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Official DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        }
      ],
      "notes": [
        "已检查官方 DeepSWE v1.1 榜单和 Microsoft 1.1 公告，未找到 MAI-Code-1.1-Flash 精确版本的公开结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis GDPval-AA v2.1 官方榜单和方法及 Microsoft 公告，未找到 MAI-Code-1.1-Flash 精确版本成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis HLE 官方页面、方法和 Microsoft 资料，未找到 MAI-Code-1.1-Flash 精确版本行。旧 Microsoft 模型卡中的 HLE 18 属于 MAI-Code-1-Flash（1.0），不可移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Official OSWorld project site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Official OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash model page",
          "url": "https://microsoft.ai/models/mai-code-1-flash/"
        }
      ],
      "notes": [
        "已检查 OSWorld 官方站和 v2 仓库。仓库确认 v2.1 发布，但官方站当前介绍 OSWorld 2.0，交互式榜单未呈现可核对的 MAI-Code 行；暂列待核实而非认定不适用。"
      ],
      "status": "待核实",
      "unresolved": [
        "OSWorld v2.1 官方交互榜单未能显示可核对模型行；需要可读的 v2.1 榜单数据继续核验。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Scale official SWE-bench Pro V2 full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "已检查 Scale 官方 V2 完整榜单和 Microsoft 资料，未找到 MAI-Code-1.1-Flash 的 V2 结果。Microsoft 旧卡中的 SWE-Bench Pro 51.2 属于 MAI-Code-1-Flash（1.0），且未注明 V2，不移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        }
      ],
      "notes": [
        "已检查 Vals AI 官方榜单和 Microsoft 1.1 资料；公开表中未找到 MAI-Code-1.1-Flash 行。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Official Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
        },
        {
          "label": "Terminal-Bench 4.0 official release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash (1.0) model card; excluded as wrong version",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "已检查 Terminal-Bench 4.0 官方榜单和发布说明及 Microsoft 1.1 公告。官方榜单网页读取时没有呈现模型数据行，暂不能确认是否有该模型结果。Microsoft 公告提及的是 Terminal-Bench 2.1 的相对提升，不是 4.0 的绝对分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 Terminal-Bench 4.0 榜单通过浏览器读取时未呈现数据行；需在排行榜恢复可见后复查 MAI-Code-1.1-Flash。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T18:53+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Microsoft MAI-Code-1.1-Flash announcement",
          "url": "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
        }
      ],
      "notes": [
        "已检查 Vals 官方 v2.2 榜单和 Microsoft 公告，榜单未列出 MAI-Code-1.1-Flash。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T18:53+08:00",
  "model_id": "microsoft/mai-code-1.1-flash",
  "model_notes": [
    "Microsoft 页面链接的 MAI-Code-1-Flash Model Card 明确是旧版 MAI-Code-1-Flash（1.0，2026-06-02），未将其中 SWE-Bench Pro、Terminal-Bench 2 或 HLE 成绩移用到 1.1。",
    "Microsoft 1.1 公告只提到 GitHub Copilot CLI 场景下 Terminal-Bench 2.1 的相对改进 22%，未公布 11 项目标 Benchmark 的绝对成绩；公告时间不是成绩评测日期。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
