# Macaron V1 Venti Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mindlab/macaron-v1-venti
- 模型名称：Macaron V1 Venti
- 发布日期：2026-07-21
- 最近检查时间：2026-11-04T23:08+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Mind Lab 官方发布说明将 Venti（GLM-5.2 底座）与 Tall（Qwen3.6 底座）列为两个独立变体；本轮只归属 Venti 的成绩。
- 技术报告和模型卡的 DeepSWE 58.4 是 Venti 结果，但版本未注明，且指标采用最多三次尝试中的最佳值；不将其当作本地目标版本的 pass@1 成绩。
- 官方文档中未细分型号的 Macaron-V1 AutomationBench 31.8 使用公开任务集，既无法确认 Venti 身份，也不同于本地私有留出集定义。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Macaron-V1.1 benchmark table and setup](https://mint-doc.macaron.xin/model-api/macaron-v1/) | 2026-11-04T23:08+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:08+08:00 |
| terminal-bench-v4 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T23:08+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T23:08+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Macaron model documentation](https://mint-doc.macaron.xin/model-api/macaron-v1/), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T23:08+08:00 |
| osworld-v2.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld 2.0 project](https://osworld-v2.xlang.ai/) | 2026-11-04T23:08+08:00 |
| chartography | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T23:08+08:00 |
| humanitys-last-exam | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T23:08+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Artificial Analysis model overview](https://artificialanalysis.ai/models) | 2026-11-04T23:08+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T23:08+08:00 |
| vals-index-v2.2 | 待核实 | — | [Macaron-V1 technical report](https://arxiv.org/html/2608.09819), [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T23:08+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Macaron-V1.1 benchmark table and setup](https://mint-doc.macaron.xin/model-api/macaron-v1/)

研究备注：
- Venti 技术报告及模型卡列出 DeepSWE 58.4；技术报告称使用 Claude Code harness、最多三次尝试并取最佳结果。报告本身没有注明 DeepSWE 版本，指标不是本地定义的 pass@1。后续官方文档的表格将 Macaron-V1 这一列对应 58.4，但没有细分 Venti/Tall；当前 v1.1 榜单也未列 Macaron。因此该候选不能确认为目标版本、精确子型号和目标指标，未写入 TOML。

尚未解决的问题：
- DeepSWE 58.4 的来源报告未标注数据版本；官方后续表格的 Macaron-V1 列未明确 Venti/Tall，且该分数使用 best-of-up-to-3，而本地定义为 pass@1。

最近核验时间：2026-11-04T23:08+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Venti 材料报告的是 SWE-Verified，不是 SWE-bench Pro V2；Scale 的 V2 页面未见 Macaron-V1-Venti。没有把其他 SWE 变体映射到 V2。

最近核验时间：2026-11-04T23:08+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Venti 技术报告和模型卡报告 TerminalBench 2.1 87.6；技术报告指出使用 Claude Code Agent Harness、Harbor、四小时 timeout 和 pass@1。这不是 v4。Vals 当前 v4 榜单未见 Venti。

最近核验时间：2026-11-04T23:08+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Venti 的公开评测资料未报告 Terminal-Bench-Science 0.1；Vals 当前榜单未列该型号。

最近核验时间：2026-11-04T23:08+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Macaron model documentation](https://mint-doc.macaron.xin/model-api/macaron-v1/)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 官方文档报告“Macaron-V1” AutomationBench 31.8，并说明使用 v1.0.6 公开 600 任务集、API 工具集、每任务最多 50 步；但分数未明确绑定 Venti。公开集也不等价于本地定义所指的私有留出集。Zapier 当前官方私有集榜单未见 Venti。未将分数写入 TOML。

尚未解决的问题：
- 31.8 是否属于 Macaron-V1-Venti 未被官方文档明确；公开 600 任务集成绩不能替代本地私有留出集定义。

最近核验时间：2026-11-04T23:08+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld 2.0 project](https://osworld-v2.xlang.ai/)

研究备注：
- Venti 官方技术报告和模型卡未报告 OSWorld v2.1 成绩；OSWorld v2.1 官方发布资料未提供该型号结果。没有使用 OSWorld 2.0、OSWorld-Verified 或其他版本替代。

最近核验时间：2026-11-04T23:08+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Venti 官方公开材料未报告 Chartography 成绩；Surge 当前榜单未见 Macaron-V1-Venti。

最近核验时间：2026-11-04T23:08+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Venti 官方评测材料未列 HLE；Artificial Analysis HLE 评测页当前可见内容未列 Venti。GLM-5.2 基座分数不是 Venti 成绩。

最近核验时间：2026-11-04T23:08+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Artificial Analysis model overview](https://artificialanalysis.ai/models)

研究备注：
- Mind Lab 官方评测资料未报告 Artificial Analysis Intelligence Index V5；Artificial Analysis 当前模型总览未显示 Macaron-V1-Venti。GLM-5.2 基座分数不归属 Venti。

最近核验时间：2026-11-04T23:08+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Venti 官方评测材料未报告 GDPval-AA v2.1；Artificial Analysis 当前可见评测页未列 Venti。GLM-5.2 基座分数不是 Venti 的分数。

最近核验时间：2026-11-04T23:08+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Macaron-V1 technical report](https://arxiv.org/html/2608.09819)
- [Macaron-V1-Venti model card](https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前页面标示 Index v2.2（2026-10-30），并说明榜单展示每实验室最佳模型和最新、顶尖、前沿模型精选范围；页面未列 Venti，但不是完整历史成绩清单。

尚未解决的问题：
- 无法根据当前精选榜单确认 Macaron-V1-Venti 是否曾获 v2.2 成绩。

最近核验时间：2026-11-04T23:08+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Artificial Analysis model overview",
          "url": "https://artificialanalysis.ai/models"
        }
      ],
      "notes": [
        "Mind Lab 官方评测资料未报告 Artificial Analysis Intelligence Index V5；Artificial Analysis 当前模型总览未显示 Macaron-V1-Venti。GLM-5.2 基座分数不归属 Venti。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron model documentation",
          "url": "https://mint-doc.macaron.xin/model-api/macaron-v1/"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "官方文档报告“Macaron-V1” AutomationBench 31.8，并说明使用 v1.0.6 公开 600 任务集、API 工具集、每任务最多 50 步；但分数未明确绑定 Venti。公开集也不等价于本地定义所指的私有留出集。Zapier 当前官方私有集榜单未见 Venti。未将分数写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "31.8 是否属于 Macaron-V1-Venti 未被官方文档明确；公开 600 任务集成绩不能替代本地私有留出集定义。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Venti 官方公开材料未报告 Chartography 成绩；Surge 当前榜单未见 Macaron-V1-Venti。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Macaron-V1.1 benchmark table and setup",
          "url": "https://mint-doc.macaron.xin/model-api/macaron-v1/"
        }
      ],
      "notes": [
        "Venti 技术报告及模型卡列出 DeepSWE 58.4；技术报告称使用 Claude Code harness、最多三次尝试并取最佳结果。报告本身没有注明 DeepSWE 版本，指标不是本地定义的 pass@1。后续官方文档的表格将 Macaron-V1 这一列对应 58.4，但没有细分 Venti/Tall；当前 v1.1 榜单也未列 Macaron。因此该候选不能确认为目标版本、精确子型号和目标指标，未写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "DeepSWE 58.4 的来源报告未标注数据版本；官方后续表格的 Macaron-V1 列未明确 Venti/Tall，且该分数使用 best-of-up-to-3，而本地定义为 pass@1。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Venti 官方评测材料未报告 GDPval-AA v2.1；Artificial Analysis 当前可见评测页未列 Venti。GLM-5.2 基座分数不是 Venti 的分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Venti 官方评测材料未列 HLE；Artificial Analysis HLE 评测页当前可见内容未列 Venti。GLM-5.2 基座分数不是 Venti 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld 2.0 project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "Venti 官方技术报告和模型卡未报告 OSWorld v2.1 成绩；OSWorld v2.1 官方发布资料未提供该型号结果。没有使用 OSWorld 2.0、OSWorld-Verified 或其他版本替代。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Venti 材料报告的是 SWE-Verified，不是 SWE-bench Pro V2；Scale 的 V2 页面未见 Macaron-V1-Venti。没有把其他 SWE 变体映射到 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Venti 的公开评测资料未报告 Terminal-Bench-Science 0.1；Vals 当前榜单未列该型号。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Venti 技术报告和模型卡报告 TerminalBench 2.1 87.6；技术报告指出使用 Claude Code Agent Harness、Harbor、四小时 timeout 和 pass@1。这不是 v4。Vals 当前 v4 榜单未见 Venti。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:08+08:00",
      "checked_sources": [
        {
          "label": "Macaron-V1 technical report",
          "url": "https://arxiv.org/html/2608.09819"
        },
        {
          "label": "Macaron-V1-Venti model card",
          "url": "https://huggingface.co/mindlab-research/Macaron-V1-Venti/blob/main/README.md"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前页面标示 Index v2.2（2026-10-30），并说明榜单展示每实验室最佳模型和最新、顶尖、前沿模型精选范围；页面未列 Venti，但不是完整历史成绩清单。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法根据当前精选榜单确认 Macaron-V1-Venti 是否曾获 v2.2 成绩。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:08+08:00",
  "model_id": "mindlab/macaron-v1-venti",
  "model_notes": [
    "Mind Lab 官方发布说明将 Venti（GLM-5.2 底座）与 Tall（Qwen3.6 底座）列为两个独立变体；本轮只归属 Venti 的成绩。",
    "技术报告和模型卡的 DeepSWE 58.4 是 Venti 结果，但版本未注明，且指标采用最多三次尝试中的最佳值；不将其当作本地目标版本的 pass@1 成绩。",
    "官方文档中未细分型号的 Macaron-V1 AutomationBench 31.8 使用公开任务集，既无法确认 Venti 身份，也不同于本地私有留出集定义。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
