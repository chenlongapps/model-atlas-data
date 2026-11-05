# Mistral Large 4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/mistral-large-4
- 模型名称：Mistral Large 4
- 发布日期：2026-10-06
- 最近检查时间：2026-11-04T04:18+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：3

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 61.7 (version=1.1; variant=public preview) | [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/), [DeepSWE v1.1 方法与基准说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DeepSWE 官方排行榜](https://deepswe.datacurve.ai/) | 2026-11-04T04:18+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/), [Scale SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro V2 官方协议](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T04:18+08:00 |
| terminal-bench-v4 | 已收录 | 28.3 (metric=task resolution rate; version=4.0.0; variant=public preview); 27.78 ± 1.82 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=avg@3 (3 runs; pass@1 each); harness=Mini-SWE-agent) | [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/), [Vals Terminal-Bench 4 榜单与方法](https://vals-ai.com/benchmarks/terminal-bench-4) | 2026-11-04T04:18+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science v0.1 发布说明](https://www.tbench.ai/news/terminal-bench-science-0-1), [Artificial Analysis Terminal-Bench Science 评测](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Mistral Large 4 开放权重版模型卡](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | 2026-11-04T04:18+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/), [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T04:18+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 官方网站](https://osworld-v2.xlang.ai/), [OSWorld V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2), [Mistral Large 4 工具调用文档](https://docs.mistral.ai/models/mistral-large-4-0) | 2026-11-04T04:18+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/) | 2026-11-04T04:18+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis Humanity's Last Exam 方法与评测](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis Mistral Large 4 Preview 模型页](https://artificialanalysis.ai/models/mistral-large-4-preview) | 2026-11-04T04:18+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 25 (metric=index score; version=5.0; variant=public preview) | [Artificial Analysis Mistral Large 4 Preview 模型页](https://artificialanalysis.ai/models/mistral-large-4-preview) | 2026-11-04T04:18+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA V2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Mistral Large 4 Preview 模型页](https://artificialanalysis.ai/models/mistral-large-4-preview) | 2026-11-04T04:18+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Mistral Large 4 Preview 模型页](https://www.vals.ai/models/mistralai_mistral-large-4), [Vals Index V2.1 榜单](https://www.vals.ai/benchmarks/vals_index_v2_1), [Vals Index V2.2 榜单](https://www.vals.ai/benchmarks/vals_index), [Mistral Large 4 开放权重版发布说明](https://mistral.ai/news/mistral-large-4-oss/) | 2026-11-04T04:18+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 61.7
- version: 1.1
- variant: public preview
- source: [https://mistral.ai/news/mistral-large-4/](https://mistral.ai/news/mistral-large-4/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/)
- [DeepSWE v1.1 方法与基准说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DeepSWE 官方排行榜](https://deepswe.datacurve.ai/)

研究备注：
- Mistral 公告明确将 61.7% 标为 DeepSWE v1.1 的 Mistral Large 4 Preview 成绩；分数已作为原始记录写入 TOML。Mistral 未说明 metric、harness、effort 或评测日期；官方排行榜没有该行且页面记录的更新早于模型发布。原始记录因此没有填写 metric，当前不映射到本地 pass@1 定义。

尚未解决的问题：
- 需要确认 Mistral 报告的 61.7% 对应本地定义的 pass@1 后，才可补 metric 并计入覆盖率。

最近核验时间：2026-11-04T04:18+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/)
- [Scale SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro V2 官方协议](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- 未找到 Mistral Large 4 Preview 的可核实成绩；Scale 榜单页面的更新早于该模型发布，因此其缺席不能排除之后出现的公开结果。

尚未解决的问题：
- 需复查模型发布后的官方 V2 Full 榜单或 Mistral 原始报告，确认是否存在对应版本成绩。

最近核验时间：2026-11-04T04:18+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 28.3
- metric: task resolution rate
- version: 4.0.0
- variant: public preview
- source: [https://mistral.ai/news/mistral-large-4/](https://mistral.ai/news/mistral-large-4/)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 27.78 ± 1.82
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: avg@3 (3 runs; pass@1 each)
- harness: Mini-SWE-agent
- source: [https://vals-ai.com/benchmarks/terminal-bench-4](https://vals-ai.com/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/)
- [Vals Terminal-Bench 4 榜单与方法](https://vals-ai.com/benchmarks/terminal-bench-4)

研究备注：
- 分开保留两种来源/配置：Mistral 公告报告 Preview 28.3%，但未说明 harness 或评测日期；Vals 榜列 Preview 在 Mini-SWE-agent 下 27.78 ± 1.82，66 tasks，avg@3（三次 pass@1）。两条不合并；来源未给出评测日期，未填 date。

最近核验时间：2026-11-04T04:18+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science v0.1 发布说明](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Artificial Analysis Terminal-Bench Science 评测](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Mistral Large 4 开放权重版模型卡](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)

研究备注：
- 未找到可归属于 2026-10-06 Preview 的成绩。后续开放权重版模型卡上的 4.3 分属于 10 月 29 日改进版本，未移用。

最近核验时间：2026-11-04T04:18+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/)
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- Mistral 公告报告 59.9% / 657 个 workflows，但没有注明 AutomationBench 版本、metric、harness、配置或评测日期；Zapier 当前 V1.0.6 榜未列该模型。

尚未解决的问题：
- 尚不能确认 59.9% 对应本地定义的 AutomationBench v1.0.6 及其 held-out private task set，故没有写入 TOML。

最近核验时间：2026-11-04T04:18+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 官方网站](https://osworld-v2.xlang.ai/)
- [OSWorld V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2)
- [Mistral Large 4 工具调用文档](https://docs.mistral.ai/models/mistral-large-4-0)

研究备注：
- 未找到 Mistral Large 4 Preview 的可核实 OSWorld V2.1 成绩；模型支持工具调用，适用于该类评测。官网当前展示的页面为 V2.0，V2.1 发布说明不能证明已完整核对目标版排行榜。

尚未解决的问题：
- 需要可核实的 OSWorld V2.1 排行榜或精确模型结果。

最近核验时间：2026-11-04T04:18+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Mistral Large 4 Preview 发布说明](https://mistral.ai/news/mistral-large-4/)

研究备注：
- Surge 的 Chartography 榜未列 Mistral Large 4。Mistral 对 ChartQA Pro 的提及是另一评测，未作替代。模型支持图像输入，适用性成立。

最近核验时间：2026-11-04T04:18+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Humanity's Last Exam 方法与评测](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis Mistral Large 4 Preview 模型页](https://artificialanalysis.ai/models/mistral-large-4-preview)

研究备注：
- AA 历史搜索索引曾显示 Preview 为 35%，但当前可访问的官方页面未能复现该条目，未写入 TOML。AA 协议介绍的是原版 HLE 文本题 pass@1；未与 HLE-Diamond 混用。

尚未解决的问题：
- 需要可直接复核的官方结果页，确认 35% 是否确属原版 HLE 的该 Preview 版本。

最近核验时间：2026-11-04T04:18+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 25
- metric: index score
- version: 5.0
- variant: public preview
- source: [https://artificialanalysis.ai/models/mistral-large-4-preview](https://artificialanalysis.ai/models/mistral-large-4-preview)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Mistral Large 4 Preview 模型页](https://artificialanalysis.ai/models/mistral-large-4-preview)

研究备注：
- AA 精确 Preview 模型页显示 Artificial Analysis Intelligence Index V5.0 得分 25；来源未提供 effort 或评测日期，因此未填写。

最近核验时间：2026-11-04T04:18+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA V2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Mistral Large 4 Preview 模型页](https://artificialanalysis.ai/models/mistral-large-4-preview)

研究备注：
- AA 历史搜索索引曾显示该 Preview 为 1434 Elo，但当前官方 GDPval-AA 页面没有该条目且无法复现，未写入 TOML。协议为 GDPval-AA V2.1；未把评测介绍中的任务条件当作该模型的具体执行条件。

尚未解决的问题：
- 需要可直接复核的官方榜单或结果页，确认 1434 Elo 及准确模型版本。

最近核验时间：2026-11-04T04:18+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Mistral Large 4 Preview 模型页](https://www.vals.ai/models/mistralai_mistral-large-4)
- [Vals Index V2.1 榜单](https://www.vals.ai/benchmarks/vals_index_v2_1)
- [Vals Index V2.2 榜单](https://www.vals.ai/benchmarks/vals_index)
- [Mistral Large 4 开放权重版发布说明](https://mistral.ai/news/mistral-large-4-oss/)

研究备注：
- Preview 模型页的 45.09% 未标 Index 版本；V2.1 榜单的 Preview 48.66% 版本不符；V2.2 榜单的 Mistral Large 4 56.53% 属于 10 月 29 日改进权重。均未写入 Preview 的 TOML。

尚未解决的问题：
- 需要能把 V2.2 成绩明确关联到 10 月 6 日 Preview 的来源；当前网页结果不能区分目标检查点。

最近核验时间：2026-11-04T04:18+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Mistral Large 4 Preview 模型页",
          "url": "https://artificialanalysis.ai/models/mistral-large-4-preview"
        }
      ],
      "notes": [
        "AA 精确 Preview 模型页显示 Artificial Analysis Intelligence Index V5.0 得分 25；来源未提供 effort 或评测日期，因此未填写。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Mistral Large 4 Preview 发布说明",
          "url": "https://mistral.ai/news/mistral-large-4/"
        },
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Mistral 公告报告 59.9% / 657 个 workflows，但没有注明 AutomationBench 版本、metric、harness、配置或评测日期；Zapier 当前 V1.0.6 榜未列该模型。"
      ],
      "status": "待核实",
      "unresolved": [
        "尚不能确认 59.9% 对应本地定义的 AutomationBench v1.0.6 及其 held-out private task set，故没有写入 TOML。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Mistral Large 4 Preview 发布说明",
          "url": "https://mistral.ai/news/mistral-large-4/"
        }
      ],
      "notes": [
        "Surge 的 Chartography 榜未列 Mistral Large 4。Mistral 对 ChartQA Pro 的提及是另一评测，未作替代。模型支持图像输入，适用性成立。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Mistral Large 4 Preview 发布说明",
          "url": "https://mistral.ai/news/mistral-large-4/"
        },
        {
          "label": "DeepSWE v1.1 方法与基准说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DeepSWE 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Mistral 公告明确将 61.7% 标为 DeepSWE v1.1 的 Mistral Large 4 Preview 成绩；分数已作为原始记录写入 TOML。Mistral 未说明 metric、harness、effort 或评测日期；官方排行榜没有该行且页面记录的更新早于模型发布。原始记录因此没有填写 metric，当前不映射到本地 pass@1 定义。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要确认 Mistral 报告的 61.7% 对应本地定义的 pass@1 后，才可补 metric 并计入覆盖率。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA V2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Mistral Large 4 Preview 模型页",
          "url": "https://artificialanalysis.ai/models/mistral-large-4-preview"
        }
      ],
      "notes": [
        "AA 历史搜索索引曾显示该 Preview 为 1434 Elo，但当前官方 GDPval-AA 页面没有该条目且无法复现，未写入 TOML。协议为 GDPval-AA V2.1；未把评测介绍中的任务条件当作该模型的具体执行条件。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可直接复核的官方榜单或结果页，确认 1434 Elo 及准确模型版本。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Humanity's Last Exam 方法与评测",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis Mistral Large 4 Preview 模型页",
          "url": "https://artificialanalysis.ai/models/mistral-large-4-preview"
        }
      ],
      "notes": [
        "AA 历史搜索索引曾显示 Preview 为 35%，但当前可访问的官方页面未能复现该条目，未写入 TOML。AA 协议介绍的是原版 HLE 文本题 pass@1；未与 HLE-Diamond 混用。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可直接复核的官方结果页，确认 35% 是否确属原版 HLE 的该 Preview 版本。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 官方网站",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Mistral Large 4 工具调用文档",
          "url": "https://docs.mistral.ai/models/mistral-large-4-0"
        }
      ],
      "notes": [
        "未找到 Mistral Large 4 Preview 的可核实 OSWorld V2.1 成绩；模型支持工具调用，适用于该类评测。官网当前展示的页面为 V2.0，V2.1 发布说明不能证明已完整核对目标版排行榜。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可核实的 OSWorld V2.1 排行榜或精确模型结果。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Mistral Large 4 Preview 发布说明",
          "url": "https://mistral.ai/news/mistral-large-4/"
        },
        {
          "label": "Scale SWE-bench Pro V2 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro V2 官方协议",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "未找到 Mistral Large 4 Preview 的可核实成绩；Scale 榜单页面的更新早于该模型发布，因此其缺席不能排除之后出现的公开结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需复查模型发布后的官方 V2 Full 榜单或 Mistral 原始报告，确认是否存在对应版本成绩。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science v0.1 发布说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 评测",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Mistral Large 4 开放权重版模型卡",
          "url": "https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B"
        }
      ],
      "notes": [
        "未找到可归属于 2026-10-06 Preview 的成绩。后续开放权重版模型卡上的 4.3 分属于 10 月 29 日改进版本，未移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Mistral Large 4 Preview 发布说明",
          "url": "https://mistral.ai/news/mistral-large-4/"
        },
        {
          "label": "Vals Terminal-Bench 4 榜单与方法",
          "url": "https://vals-ai.com/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "分开保留两种来源/配置：Mistral 公告报告 Preview 28.3%，但未说明 harness 或评测日期；Vals 榜列 Preview 在 Mini-SWE-agent 下 27.78 ± 1.82，66 tasks，avg@3（三次 pass@1）。两条不合并；来源未给出评测日期，未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T04:18+08:00",
      "checked_sources": [
        {
          "label": "Vals Mistral Large 4 Preview 模型页",
          "url": "https://www.vals.ai/models/mistralai_mistral-large-4"
        },
        {
          "label": "Vals Index V2.1 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        },
        {
          "label": "Vals Index V2.2 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Mistral Large 4 开放权重版发布说明",
          "url": "https://mistral.ai/news/mistral-large-4-oss/"
        }
      ],
      "notes": [
        "Preview 模型页的 45.09% 未标 Index 版本；V2.1 榜单的 Preview 48.66% 版本不符；V2.2 榜单的 Mistral Large 4 56.53% 属于 10 月 29 日改进权重。均未写入 Preview 的 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要能把 V2.2 成绩明确关联到 10 月 6 日 Preview 的来源；当前网页结果不能区分目标检查点。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T04:18+08:00",
  "model_id": "mistral/mistral-large-4",
  "new_records": 4,
  "overall_status": "待复核"
}

-->
