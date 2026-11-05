# GPT-5.6 Cyber Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.6-cyber
- 模型名称：GPT-5.6 Cyber
- 发布日期：2026-08-07
- 最近检查时间：2026-11-04T19:31+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 模型身份已与 OpenAI 官方资料核对：API changelog 将 gpt-5.6-cyber 与 Daybreak Red 列在 2026-08-07；面向公众的 Daybreak 文章日期为 2026-08-10。保留仓库 release_date=2026-08-07，不在本次收集中改动。
- OpenAI 将 GPT-5.6 Cyber 描述为经网络安全任务专门训练的模型，并与 GPT-5.6 Sol 区分；所有 Sol 榜单成绩均不转录为 Cyber 成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/) | 2026-11-04T19:31+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T19:31+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0), [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T19:31+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement), [Harbor 官方 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-04T19:31+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库与公开结果](https://github.com/zapier/AutomationBench) | 2026-11-04T19:31+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 官方仓库及 v2.1 发布说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T19:31+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方仓库](https://github.com/surge-ai/chartography) | 2026-11-04T19:31+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale AI Humanity's Last Exam 官方排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Humanity's Last Exam 独立评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T19:31+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index v5 官方发布说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T19:31+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T19:31+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T19:31+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)

研究备注：
- 已检查版本选择为 v1.1 的官方榜单（113 tasks）；榜单中可见 GPT-5.6 Sol [max] 73%±3%，没有 GPT-5.6 Cyber 的精确条目。Sol 是不同模型，不转录其成绩。

最近核验时间：2026-11-04T19:31+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-Bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 已检查 Scale 官方 SWE-Bench Pro V2 Full 榜单；可见内容没有 GPT-5.6 Cyber 的精确条目。页面同时说明 V2 为 642-task 新版本；其他 SWE-bench 版本或 GPT-5.6 Sol 结果不转录。

最近核验时间：2026-11-04T19:31+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4.0)
- [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 已检查官方 Terminal-Bench 4.0 页面和版本说明；可读页面中的 leaderboard 表格没有渲染结果行，无法确认完整榜单是否含 GPT-5.6 Cyber。版本说明指出 4.0 更改了任务和运行条件，不能沿用其他版本分数。

尚未解决的问题：
- 官方结果页当前没有渲染可读榜单行；需后续重新核对完整 leaderboard。

最近核验时间：2026-11-04T19:31+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Harbor 官方 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- 官方公告确认 v0.1 含 70 个科学工作流任务。官方公告中的 leaderboard 图像及 Harbor leaderboard 在本次可读页面中未提供可核对的完整模型行，因此不能确认 Cyber 是否有公开结果。

尚未解决的问题：
- 官方 Harbor leaderboard 仍显示加载中，公告 leaderboard 以图片展示；需后续核对完整可读结果。

最近核验时间：2026-11-04T19:31+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库与公开结果](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 官方榜单标明版本 1.0.6，只显示前 10 行并折叠其余 119 行；可见内容没有 GPT-5.6 Cyber。官方仓库公开任务结果列出 GPT-5.6 Sol 45.83% (max)，但这是不同模型；隐藏行尚未核对。

尚未解决的问题：
- 官方网页折叠了其余 119 行；需后续核对隐藏榜单条目或官方原始结果。

最近核验时间：2026-11-04T19:31+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 官方仓库及 v2.1 发布说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- 官方仓库标明 osworld-v2.1 为当前推荐版本；项目页公开内容仍以 OSWorld 2.0 为主，未发现 GPT-5.6 Cyber 的精确 v2.1 结果。不得把 GPT-5.5、GPT-5.6 Sol 或其他 OSWorld 版本结果转录。

最近核验时间：2026-11-04T19:31+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography 官方仓库](https://github.com/surge-ai/chartography)

研究备注：
- 已检查 Surge 官方排行榜；可见 GPT 5.6 Sol (Max reasoning) 45%，没有 GPT-5.6 Cyber 的精确条目。Sol 成绩不转录到 Cyber。

最近核验时间：2026-11-04T19:31+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI Humanity's Last Exam 官方排行榜](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Humanity's Last Exam 独立评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 已检查 Scale 官方排行榜和 Artificial Analysis 独立评测页，均未发现 GPT-5.6 Cyber 的精确公开成绩。未将不同模型或 HLE 子集结果视作该模型在完整 HLE 上的成绩。

最近核验时间：2026-11-04T19:31+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5 官方发布说明](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- 已检查 Artificial Analysis v5 发布说明；未发现 GPT-5.6 Cyber 的 v5 综合指数成绩。v5 使用 HLE-Diamond 并从指数中移除 GDPval-AA v2.1，不能由其他单项成绩推导该综合分。

最近核验时间：2026-11-04T19:31+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 已检查 Artificial Analysis v2.1 榜单与方法说明；榜单包含 GPT-5.6 Sol (Non-reasoning) Elo 1250，但没有 GPT-5.6 Cyber 精确条目。没有转录 Sol 分数。

最近核验时间：2026-11-04T19:31+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方排行榜与方法说明](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 已检查 Vals 官方 Version 2.2 页面及完整可读榜单；没有 GPT-5.6 Cyber 精确条目。页面的综合指数成绩不能用其他单项分数推导。

最近核验时间：2026-11-04T19:31+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5 官方发布说明",
          "url": "https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis v5 发布说明；未发现 GPT-5.6 Cyber 的 v5 综合指数成绩。v5 使用 HLE-Diamond 并从指数中移除 GDPval-AA v2.1，不能由其他单项成绩推导该综合分。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:31+08:00",
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
        "Zapier 官方榜单标明版本 1.0.6，只显示前 10 行并折叠其余 119 行；可见内容没有 GPT-5.6 Cyber。官方仓库公开任务结果列出 GPT-5.6 Sol 45.83% (max)，但这是不同模型；隐藏行尚未核对。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方网页折叠了其余 119 行；需后续核对隐藏榜单条目或官方原始结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography 官方仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "已检查 Surge 官方排行榜；可见 GPT 5.6 Sol (Max reasoning) 45%，没有 GPT-5.6 Cyber 的精确条目。Sol 成绩不转录到 Cyber。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "已检查版本选择为 v1.1 的官方榜单（113 tasks）；榜单中可见 GPT-5.6 Sol [max] 73%±3%，没有 GPT-5.6 Cyber 的精确条目。Sol 是不同模型，不转录其成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis v2.1 榜单与方法说明；榜单包含 GPT-5.6 Sol (Non-reasoning) Elo 1250，但没有 GPT-5.6 Cyber 精确条目。没有转录 Sol 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Scale AI Humanity's Last Exam 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam 独立评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "已检查 Scale 官方排行榜和 Artificial Analysis 独立评测页，均未发现 GPT-5.6 Cyber 的精确公开成绩。未将不同模型或 HLE 子集结果视作该模型在完整 HLE 上的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 官方仓库及 v2.1 发布说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "官方仓库标明 osworld-v2.1 为当前推荐版本；项目页公开内容仍以 OSWorld 2.0 为主，未发现 GPT-5.6 Cyber 的精确 v2.1 结果。不得把 GPT-5.5、GPT-5.6 Sol 或其他 OSWorld 版本结果转录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-Bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "已检查 Scale 官方 SWE-Bench Pro V2 Full 榜单；可见内容没有 GPT-5.6 Cyber 的精确条目。页面同时说明 V2 为 642-task 新版本；其他 SWE-bench 版本或 GPT-5.6 Sol 结果不转录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor 官方 leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "官方公告确认 v0.1 含 70 个科学工作流任务。官方公告中的 leaderboard 图像及 Harbor leaderboard 在本次可读页面中未提供可核对的完整模型行，因此不能确认 Cyber 是否有公开结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 Harbor leaderboard 仍显示加载中，公告 leaderboard 以图片展示；需后续核对完整可读结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方排行榜",
          "url": "https://www.tbench.ai/?version=4.0"
        },
        {
          "label": "Terminal-Bench 4.0 版本说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "已检查官方 Terminal-Bench 4.0 页面和版本说明；可读页面中的 leaderboard 表格没有渲染结果行，无法确认完整榜单是否含 GPT-5.6 Cyber。版本说明指出 4.0 更改了任务和运行条件，不能沿用其他版本分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方结果页当前没有渲染可读榜单行；需后续重新核对完整 leaderboard。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:31+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方排行榜与方法说明",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "已检查 Vals 官方 Version 2.2 页面及完整可读榜单；没有 GPT-5.6 Cyber 精确条目。页面的综合指数成绩不能用其他单项分数推导。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:31+08:00",
  "model_id": "openai/gpt-5.6-cyber",
  "model_notes": [
    "模型身份已与 OpenAI 官方资料核对：API changelog 将 gpt-5.6-cyber 与 Daybreak Red 列在 2026-08-07；面向公众的 Daybreak 文章日期为 2026-08-10。保留仓库 release_date=2026-08-07，不在本次收集中改动。",
    "OpenAI 将 GPT-5.6 Cyber 描述为经网络安全任务专门训练的模型，并与 GPT-5.6 Sol 区分；所有 Sol 榜单成绩均不转录为 Cyber 成绩。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
