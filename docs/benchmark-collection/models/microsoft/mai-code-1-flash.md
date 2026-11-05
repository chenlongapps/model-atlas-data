# MAI-Code-1-Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：microsoft/mai-code-1-flash
- 模型名称：MAI-Code-1-Flash
- 发布日期：2026-06-02
- 最近检查时间：2026-11-05T04:22+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：4
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 处理前模型文件已有 4 条 Benchmark 成绩，本轮保留原记录并新增官方模型卡中 HLE 18（Acc）一条。
- 官方模型卡确认 SWE-Bench Pro 51.2 与 Terminal Bench 2 54.8，但均非明确的 SWE-bench Pro V2 / Terminal-Bench 4 成绩；现有相邻版本记录未覆盖或改写。
- HLE 行没有公布修订版或专属工具条件，因此只记录来源明确的准确率和 Academic reasoning, text 数据集说明。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T04:22+08:00 |
| terminal-bench-v4 | 待核实 | 54.8 (metric=success rate; version=2.0) | [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| osworld-v2.1 | 不适用 | — | [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T04:22+08:00 |
| chartography | 不适用 | — | [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official evaluation repository](https://github.com/surge-ai/chartography) | 2026-11-05T04:22+08:00 |
| humanitys-last-exam | 已收录 | 18 (metric=accuracy; dataset=Academic reasoning, text) | [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) | 2026-11-05T04:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 官方榜单目前只显示 21/28 个型号，未显示 MAI-Code-1-Flash；模型卡未列 DeepSWE。

尚未解决的问题：
- 官方榜单不完整，尚不能确认该型号是否有 DeepSWE v1.1 成绩。

最近核验时间：2026-11-05T04:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 官方模型卡列出 SWE-Bench Pro pass rate 51.2%，平均 28.0K tokens，GitHub Copilot 生产 harness；但未注明 V2。模型 TOML 已有同分泛称 SWE-Bench Pro 记录，保留且不映射到 V2。

尚未解决的问题：
- 需要确认此泛称成绩对应的 Pro 数据集版本；不把它作为 SWE-bench Pro V2 结果。

最近核验时间：2026-11-05T04:22+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 54.8
- metric: success rate
- version: 2.0
- source: [https://llm-stats.com/benchmarks/terminal-bench-2](https://llm-stats.com/benchmarks/terminal-bench-2)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 模型卡列出 Terminal Bench 2 pass rate 54.8%，不映射为 Terminal-Bench 4；官方 v4 动态榜单当前无法读取完整结果行。

尚未解决的问题：
- 未能确认 v4 完整榜单中是否有该型号。

最近核验时间：2026-11-05T04:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- Science 0.1 官方结果表列出的型号中没有 MAI-Code-1-Flash；模型卡未列该项目。

最近核验时间：2026-11-05T04:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 模型卡确认该型号用于工具型 agentic coding；Zapier 1.0.6 榜单显示前 10 项并折叠 119 项，无法确认完整名单。

尚未解决的问题：
- 榜单折叠结果中是否有该型号待核实。

最近核验时间：2026-11-05T04:22+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型卡明确输入和输出均为文本，没有 OSWorld 所需的视觉桌面观察输入。

最近核验时间：2026-11-05T04:22+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official evaluation repository](https://github.com/surge-ai/chartography)

研究备注：
- 模型卡明确该精确型号只接收文本输入；Chartography 需要图表图像输入并输出文本答案，不适用。

最近核验时间：2026-11-05T04:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 18
- metric: accuracy
- dataset: Academic reasoning, text
- source: [https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 官方模型卡列出 HLE / Academic reasoning, text，Acc 18，平均 token 使用量 26.3K。卡片未给出 HLE 修订版或该行专属工具条件；未推填。

最近核验时间：2026-11-05T04:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 未找到 MAI-Code-1-Flash 的 Index v5.0.1 综合分；模型卡中其他 coding/reasoning 单项不映射为综合指数。

最近核验时间：2026-11-05T04:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- AA 公开资料未找到该精确型号的 GDPval-AA v2.1 Elo；Microsoft 模型卡未报告该项。

最近核验时间：2026-11-05T04:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Microsoft MAI-Code-1-Flash model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF)

研究备注：
- 当前公开 v2.2 排行榜展示最新/前沿模型子集，未列 MAI-Code-1-Flash；模型卡未报告该项。

最近核验时间：2026-11-05T04:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "未找到 MAI-Code-1-Flash 的 Index v5.0.1 综合分；模型卡中其他 coding/reasoning 单项不映射为综合指数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "模型卡确认该型号用于工具型 agentic coding；Zapier 1.0.6 榜单显示前 10 项并折叠 119 项，无法确认完整名单。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单折叠结果中是否有该型号待核实。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "模型卡明确该精确型号只接收文本输入；Chartography 需要图表图像输入并输出文本答案，不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "官方榜单目前只显示 21/28 个型号，未显示 MAI-Code-1-Flash；模型卡未列 DeepSWE。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单不完整，尚不能确认该型号是否有 DeepSWE v1.1 成绩。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "AA 公开资料未找到该精确型号的 GDPval-AA v2.1 Elo；Microsoft 模型卡未报告该项。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "官方模型卡列出 HLE / Academic reasoning, text，Acc 18，平均 token 使用量 26.3K。卡片未给出 HLE 修订版或该行专属工具条件；未推填。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型卡明确输入和输出均为文本，没有 OSWorld 所需的视觉桌面观察输入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "官方模型卡列出 SWE-Bench Pro pass rate 51.2%，平均 28.0K tokens，GitHub Copilot 生产 harness；但未注明 V2。模型 TOML 已有同分泛称 SWE-Bench Pro 记录，保留且不映射到 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要确认此泛称成绩对应的 Pro 数据集版本；不把它作为 SWE-bench Pro V2 结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "Science 0.1 官方结果表列出的型号中没有 MAI-Code-1-Flash；模型卡未列该项目。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "模型卡列出 Terminal Bench 2 pass rate 54.8%，不映射为 Terminal-Bench 4；官方 v4 动态榜单当前无法读取完整结果行。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能确认 v4 完整榜单中是否有该型号。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:22+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Microsoft MAI-Code-1-Flash model card",
          "url": "https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF"
        }
      ],
      "notes": [
        "当前公开 v2.2 排行榜展示最新/前沿模型子集，未列 MAI-Code-1-Flash；模型卡未报告该项。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 4,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:22+08:00",
  "model_id": "microsoft/mai-code-1-flash",
  "model_notes": [
    "处理前模型文件已有 4 条 Benchmark 成绩，本轮保留原记录并新增官方模型卡中 HLE 18（Acc）一条。",
    "官方模型卡确认 SWE-Bench Pro 51.2 与 Terminal Bench 2 54.8，但均非明确的 SWE-bench Pro V2 / Terminal-Bench 4 成绩；现有相邻版本记录未覆盖或改写。",
    "HLE 行没有公布修订版或专属工具条件，因此只记录来源明确的准确率和 Academic reasoning, text 数据集说明。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
