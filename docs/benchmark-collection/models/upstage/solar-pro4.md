# Solar Pro 4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：upstage/solar-pro4
- 模型名称：Solar Pro 4
- 发布日期：2026-08-06
- 最近检查时间：2026-11-04T19:48+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- Upstage 官方资料确认 Solar Pro 4 是文本输入/输出的 reasoning 与 agent 模型，支持工具调用；本地模型身份与其官方名称和 2026-08-06 发布日一致。
- 只将 Artificial Analysis 官方直接比较页公开的原版 HLE 29% 写入；其他型号或版本不移植。Terminal-Bench 4.0 官方 AA 页面存在 1%/0% 不一致，保留为冲突待复核。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/), [Upstage Solar Pro 4 官方发布文章](https://www.upstage.ai/blog/en/solar-pro-4) | 2026-11-04T19:48+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Upstage Solar Pro 4 官方发布文章](https://www.upstage.ai/blog/en/solar-pro-4) | 2026-11-04T19:48+08:00 |
| terminal-bench-v4 | 冲突 | — | [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0), [Artificial Analysis Terminal-Bench 4.0 官方评测方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [AA 官方历史比较页（Index v4.3.2）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4), [AA 官方当前比较页（Index v5.0.1）](https://artificialanalysis.ai/models/comparisons/solar-pro4-vs-gpt-5-6-sol) | 2026-11-04T19:48+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement), [Harbor 官方 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [Artificial Analysis Terminal-Bench-Science 官方评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T19:48+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库与公开结果](https://github.com/zapier/AutomationBench) | 2026-11-04T19:48+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2), [Upstage Solar Pro 4 API 文档](https://console.upstage.ai/api/chat) | 2026-11-04T19:48+08:00 |
| chartography | 不适用 | — | [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography), [Artificial Analysis Solar Pro 4 模型资料](https://artificialanalysis.ai/models/solar-pro4) | 2026-11-04T19:48+08:00 |
| humanitys-last-exam | 已收录 | 29 (metric=accuracy) | [Artificial Analysis 官方模型比较页（HLE 结果）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4), [Scale AI Humanity's Last Exam 官方方法与排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity's Last Exam 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T19:48+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Solar Pro 4 当前模型页](https://artificialanalysis.ai/models/solar-pro4), [Artificial Analysis Intelligence Index v5 官方说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T19:48+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis 官方比较页（v2.1 结果栏）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4), [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Upstage Solar Pro 4 官方发布文章（仅 GDPval-AA v2）](https://www.upstage.ai/blog/en/solar-pro-4) | 2026-11-04T19:48+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T19:48+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)
- [Upstage Solar Pro 4 官方发布文章](https://www.upstage.ai/blog/en/solar-pro-4)

研究备注：
- 已检查 DeepSWE v1.1 官方榜单，未见 Solar Pro 4 精确条目。Upstage 官方文章公布的 Terminal-Bench v2.1 与 SWE-Bench Verified 成绩不是本项目要求的版本。

最近核验时间：2026-11-04T19:48+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Upstage Solar Pro 4 官方发布文章](https://www.upstage.ai/blog/en/solar-pro-4)

研究备注：
- 已检查 Scale V2 Full 榜单，但浏览器可读结果未呈现完整模型行；Upstage 公布的 SWE-Bench Verified 结果不是 SWE-bench Pro V2。

尚未解决的问题：
- 官方 V2 Full 榜单完整结果行在当前可读页面中不可见；需复查能完整呈现条目的官方结果页。

最近核验时间：2026-11-04T19:48+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：冲突。

已检查的主要资料：
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0)
- [Artificial Analysis Terminal-Bench 4.0 官方评测方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [AA 官方历史比较页（Index v4.3.2）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4)
- [AA 官方当前比较页（Index v5.0.1）](https://artificialanalysis.ai/models/comparisons/solar-pro4-vs-gpt-5-6-sol)

研究备注：
- 两个 Artificial Analysis 官方比较页对 Solar Pro 4 的 Terminal-Bench 4.0 显示值不同：Index v4.3.2 历史页为 1%，较新的 Index v5.0.1 比较页为 0%。页面未说明两次测试的配置、模型快照或分数修订原因；未将任何一值写入模型 TOML。Upstage 官方发布的 57 分是 Terminal-Bench v2.1，不能用于解决 v4 冲突。

尚未解决的问题：
- 官方 AA 历史页为 1%，较新的官方比较页为 0%；缺少测试日期、模型快照或修订说明，需复核后才能确定是否为同条件冲突。

最近核验时间：2026-11-04T19:48+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Harbor 官方 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [Artificial Analysis Terminal-Bench-Science 官方评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 官方公告和 AA 方法页确认目标为 Terminal-Bench-Science 0.1；Harbor 榜单在本次浏览时仍显示加载中。AA 历史比较表的 Solar Pro 4 对应单元格未提供读数，尚无可核实的模型成绩。

尚未解决的问题：
- Harbor 官方 leaderboard 未加载出结果，当前无法核实完整榜单。

最近核验时间：2026-11-04T19:48+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库与公开结果](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 官方榜单标为 1.0.6，只显示前 10 行并折叠其余 119 行；可见内容未见 Solar Pro 4，无法据此确认完整榜单。未将 Artificial Analysis 的 AutomationBench-AA 变体等同于此项。

尚未解决的问题：
- Zapier 官方网页折叠 119 行，尚未核对完整榜单中的 Solar Pro 4 条目。

最近核验时间：2026-11-04T19:48+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 官方仓库及 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2)
- [Upstage Solar Pro 4 API 文档](https://console.upstage.ai/api/chat)

研究备注：
- OSWorld v2.1 要求计算机使用 agent 处理 GUI；Solar Pro 4 的官方模型资料列为文本输入/输出，不支持输入屏幕图像，故本项不适用。

最近核验时间：2026-11-04T19:48+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography 官方说明与排行榜](https://surgehq.ai/benchmarks/chartography)
- [Artificial Analysis Solar Pro 4 模型资料](https://artificialanalysis.ai/models/solar-pro4)

研究备注：
- Chartography 需要输入图表图像并给出可评分的文本理解答案；官方模型资料显示 Solar Pro 4 仅接受文本输入，故本项不适用。

最近核验时间：2026-11-04T19:48+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 29
- metric: accuracy
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis 官方模型比较页（HLE 结果）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4)
- [Scale AI Humanity's Last Exam 官方方法与排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity's Last Exam 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis 官方比较页的 Solar Pro 4 行显示 Humanity’s Last Exam 29%；记录原始显示精度为 29，指标为 accuracy。比较页的 v4.3.2 综合 Index 标注为 estimated；该标记针对综合 Index，不是 HLE 行。页面未公布此行的具体日期、推理档位、harness 或题目子集，未补填这些条件。

最近核验时间：2026-11-04T19:48+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Solar Pro 4 当前模型页](https://artificialanalysis.ai/models/solar-pro4)
- [Artificial Analysis Intelligence Index v5 官方说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- Artificial Analysis 当前 Solar Pro 4 模型页对 Intelligence Index 显示 N/A；v5 说明确认当前指数版本为 5.0.1。历史 v4.3.2 比较页的估算综合分不属于目标 v5，也未转录。

最近核验时间：2026-11-04T19:48+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 官方比较页（v2.1 结果栏）](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4)
- [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Upstage Solar Pro 4 官方发布文章（仅 GDPval-AA v2）](https://www.upstage.ai/blog/en/solar-pro-4)

研究备注：
- AA 官方历史比较页中 Solar Pro 4 的 GDPval-AA v2.1 单元格为空；Upstage 发布页给出的是 GDPval-AA v2 38.8%，版本和指标都不匹配，不能转录。

最近核验时间：2026-11-04T19:48+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 官方页确认当前版本为 2.2，但可读榜单仅展示 19 个 latest/top/frontier 模型；列表没有 Solar Pro 4，因非完整结果集而不能据此确认全榜不存在。

尚未解决的问题：
- Vals 官方页面只呈现部分最新/头部模型；尚未找到能核对 Solar Pro 4 的完整 v2.2 结果集。

最近核验时间：2026-11-04T19:48+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Solar Pro 4 当前模型页",
          "url": "https://artificialanalysis.ai/models/solar-pro4"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5 官方说明",
          "url": "https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "Artificial Analysis 当前 Solar Pro 4 模型页对 Intelligence Index 显示 N/A；v5 说明确认当前指数版本为 5.0.1。历史 v4.3.2 比较页的估算综合分不属于目标 v5，也未转录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方排行榜",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库与公开结果",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Zapier 官方榜单标为 1.0.6，只显示前 10 行并折叠其余 119 行；可见内容未见 Solar Pro 4，无法据此确认完整榜单。未将 Artificial Analysis 的 AutomationBench-AA 变体等同于此项。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 官方网页折叠 119 行，尚未核对完整榜单中的 Solar Pro 4 条目。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方说明与排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Artificial Analysis Solar Pro 4 模型资料",
          "url": "https://artificialanalysis.ai/models/solar-pro4"
        }
      ],
      "notes": [
        "Chartography 需要输入图表图像并给出可评分的文本理解答案；官方模型资料显示 Solar Pro 4 仅接受文本输入，故本项不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Upstage Solar Pro 4 官方发布文章",
          "url": "https://www.upstage.ai/blog/en/solar-pro-4"
        }
      ],
      "notes": [
        "已检查 DeepSWE v1.1 官方榜单，未见 Solar Pro 4 精确条目。Upstage 官方文章公布的 Terminal-Bench v2.1 与 SWE-Bench Verified 成绩不是本项目要求的版本。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 官方比较页（v2.1 结果栏）",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Upstage Solar Pro 4 官方发布文章（仅 GDPval-AA v2）",
          "url": "https://www.upstage.ai/blog/en/solar-pro-4"
        }
      ],
      "notes": [
        "AA 官方历史比较页中 Solar Pro 4 的 GDPval-AA v2.1 单元格为空；Upstage 发布页给出的是 GDPval-AA v2 38.8%，版本和指标都不匹配，不能转录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 官方模型比较页（HLE 结果）",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4"
        },
        {
          "label": "Scale AI Humanity's Last Exam 官方方法与排行榜",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam 评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis 官方比较页的 Solar Pro 4 行显示 Humanity’s Last Exam 29%；记录原始显示精度为 29，指标为 accuracy。比较页的 v4.3.2 综合 Index 标注为 estimated；该标记针对综合 Index，不是 HLE 行。页面未公布此行的具体日期、推理档位、harness 或题目子集，未补填这些条件。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方仓库及 v2.1 说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Upstage Solar Pro 4 API 文档",
          "url": "https://console.upstage.ai/api/chat"
        }
      ],
      "notes": [
        "OSWorld v2.1 要求计算机使用 agent 处理 GUI；Solar Pro 4 的官方模型资料列为文本输入/输出，不支持输入屏幕图像，故本项不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-Bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Upstage Solar Pro 4 官方发布文章",
          "url": "https://www.upstage.ai/blog/en/solar-pro-4"
        }
      ],
      "notes": [
        "已检查 Scale V2 Full 榜单，但浏览器可读结果未呈现完整模型行；Upstage 公布的 SWE-Bench Verified 结果不是 SWE-bench Pro V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 V2 Full 榜单完整结果行在当前可读页面中不可见；需复查能完整呈现条目的官方结果页。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor 官方 leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "官方公告和 AA 方法页确认目标为 Terminal-Bench-Science 0.1；Harbor 榜单在本次浏览时仍显示加载中。AA 历史比较表的 Solar Pro 4 对应单元格未提供读数，尚无可核实的模型成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "Harbor 官方 leaderboard 未加载出结果，当前无法核实完整榜单。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方排行榜",
          "url": "https://www.tbench.ai/?version=4.0"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 官方评测方法",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "AA 官方历史比较页（Index v4.3.2）",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-solarpro4"
        },
        {
          "label": "AA 官方当前比较页（Index v5.0.1）",
          "url": "https://artificialanalysis.ai/models/comparisons/solar-pro4-vs-gpt-5-6-sol"
        }
      ],
      "notes": [
        "两个 Artificial Analysis 官方比较页对 Solar Pro 4 的 Terminal-Bench 4.0 显示值不同：Index v4.3.2 历史页为 1%，较新的 Index v5.0.1 比较页为 0%。页面未说明两次测试的配置、模型快照或分数修订原因；未将任何一值写入模型 TOML。Upstage 官方发布的 57 分是 Terminal-Bench v2.1，不能用于解决 v4 冲突。"
      ],
      "status": "冲突",
      "unresolved": [
        "官方 AA 历史页为 1%，较新的官方比较页为 0%；缺少测试日期、模型快照或修订说明，需复核后才能确定是否为同条件冲突。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:48+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方排行榜与方法说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 官方页确认当前版本为 2.2，但可读榜单仅展示 19 个 latest/top/frontier 模型；列表没有 Solar Pro 4，因非完整结果集而不能据此确认全榜不存在。"
      ],
      "status": "待核实",
      "unresolved": [
        "Vals 官方页面只呈现部分最新/头部模型；尚未找到能核对 Solar Pro 4 的完整 v2.2 结果集。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:48+08:00",
  "model_id": "upstage/solar-pro4",
  "model_notes": [
    "Upstage 官方资料确认 Solar Pro 4 是文本输入/输出的 reasoning 与 agent 模型，支持工具调用；本地模型身份与其官方名称和 2026-08-06 发布日一致。",
    "只将 Artificial Analysis 官方直接比较页公开的原版 HLE 29% 写入；其他型号或版本不移植。Terminal-Bench 4.0 官方 AA 页面存在 1%/0% 不一致，保留为冲突待复核。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
