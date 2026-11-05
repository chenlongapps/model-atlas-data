# Gemini 3.5 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.5-flash
- 模型名称：Gemini 3.5 Flash
- 发布日期：2026-05-19
- 最近检查时间：2026-11-05T05:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：10
- 收集前已有成绩数量：10
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 模型身份为 Google Gemini 3.5 Flash，发布日期 2026-05-19。
- 将 10 条既有成绩的来源链接改为版本固定模型卡；移除 10 个等同发布日的 date 字段，因为 Google 仅说明结果截至 2026 年 5 月，没有逐项评测日期。
- 保留 SWE-Bench Pro、Terminal-Bench 2.1、OSWorld-Verified 与 GDPval-AA 原始记录，不将其自动映射到目标版本。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 36%±4% (metric=pass@1; version=1.1; dataset=113 tasks; effort=high; harness=mini-swe-agent) | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T05:58+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/), [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T05:58+08:00 |
| terminal-bench-v4 | 未找到 | 76.2 (metric=success rate; version=2.1; harness=Terminus-2) | [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/), [AA Gemini 3.5 page](https://artificialanalysis.ai/models/gemini-3-5-flash), [AA TB4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T05:58+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [AA Gemini 3.5 page](https://artificialanalysis.ai/models/gemini-3-5-flash), [AA TB-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T05:58+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench) | 2026-11-05T05:58+08:00 |
| osworld-v2.1 | 待核实 | — | [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2 project page](https://osworld-v2.xlang.ai/) | 2026-11-05T05:58+08:00 |
| chartography | 未找到 | — | [Surge Chartography](https://surgehq.ai/benchmarks/chartography), [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/) | 2026-11-05T05:58+08:00 |
| humanitys-last-exam | 已存在 | 40.2 (metric=accuracy; dataset=full set, text + MM) | [Google Gemini 3.5 version-specific model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/) | 2026-11-05T05:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [AA Gemini 3.5 page](https://artificialanalysis.ai/models/gemini-3-5-flash), [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1656 (metric=Elo) | [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/), [AA Gemini 3.5 comparison](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gemini-3-5-flash), [AA GDPval methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T05:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 36%±4%
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: high
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 官方榜单精确列出 gemini-3.5-flash[high]：36%±4%，113 tasks；使用 mini-swe-agent。

最近核验时间：2026-11-05T05:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Google 模型卡的 55.1% 属于 SWE-Bench Pro Public、single attempt；早于 V2 发布，不能映射。

尚未解决的问题：
- 未找到 Gemini 3.5 Flash 精确 V2 结果；Scale 榜单未显示该型号。

最近核验时间：2026-11-05T05:58+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 76.2
- metric: success rate
- version: 2.1
- harness: Terminus-2
- source: [https://deepmind.google/models/model-cards/gemini-3-5-flash/](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- [AA Gemini 3.5 page](https://artificialanalysis.ai/models/gemini-3-5-flash)
- [AA TB4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- Google 已报告的 76.2% 属于 Terminal-Bench 2.1；未找到该模型 v4.0 分数。

最近核验时间：2026-11-05T05:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [AA Gemini 3.5 page](https://artificialanalysis.ai/models/gemini-3-5-flash)
- [AA TB-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 未找到 Gemini 3.5 Flash 对应 Terminal-Bench-Science 0.1 的公开分数。

最近核验时间：2026-11-05T05:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)

研究备注：
- 模型卡确认其工具和 agent 能力；官方榜单部分结果折叠，未能查看完整型号列表。

尚未解决的问题：
- 无法确认该型号是否位于未展开的结果中。

最近核验时间：2026-11-05T05:58+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2 project page](https://osworld-v2.xlang.ai/)

研究备注：
- Google 报告的 OSWorld-Verified 78.4% 未标为 OSWorld 2.1，不能映射到目标版本。

尚未解决的问题：
- 未找到精确 OSWorld 2.1 原始结果；动态榜单无法完整核对目标型号。

最近核验时间：2026-11-05T05:58+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography](https://surgehq.ai/benchmarks/chartography)
- [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)

研究备注：
- 模型支持图像输入；未发现 Gemini 3.5 Flash 精确型号结果。Gemini 3.5 Flash-Lite 是不同型号。

最近核验时间：2026-11-05T05:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 40.2
- metric: accuracy
- dataset: full set, text + MM
- source: [https://deepmind.google/models/model-cards/gemini-3-5-flash/](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Google Gemini 3.5 version-specific model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)

研究备注：
- 源 TOML 已有 40.2% accuracy，数据集为 full set, text + MM，版本固定模型卡确认该成绩。

最近核验时间：2026-11-05T05:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [AA Gemini 3.5 page](https://artificialanalysis.ai/models/gemini-3-5-flash)
- [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 未找到该精确型号可映射到 V5 的公开 Index 分数；High 配置不能自动映射至未指定 effort 的记录。

最近核验时间：2026-11-05T05:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1656
- metric: Elo
- source: [https://deepmind.google/models/model-cards/gemini-3-5-flash/](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google Gemini 3.5 model card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- [AA Gemini 3.5 comparison](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gemini-3-5-flash)
- [AA GDPval methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 保留已有 GDPval-AA 1656 Elo；Google 未标 v2.1。AA 页面另报 High 配置 1201/1202 Elo，与现有项的 effort 不同。

尚未解决的问题：
- 无法确认 1656 的目标版本；AA High 的 1 Elo 差异与 effort 配置未解决。

最近核验时间：2026-11-05T05:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查 2026-10-30 更新的官方 V2.2 榜单，未发现 Gemini 3.5 Flash 精确型号。

最近核验时间：2026-11-05T05:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA Gemini 3.5 page",
          "url": "https://artificialanalysis.ai/models/gemini-3-5-flash"
        },
        {
          "label": "AA Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "未找到该精确型号可映射到 V5 的公开 Index 分数；High 配置不能自动映射至未指定 effort 的记录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Zapier leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "模型卡确认其工具和 agent 能力；官方榜单部分结果折叠，未能查看完整型号列表。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法确认该型号是否位于未展开的结果中。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Google Gemini 3.5 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash/"
        }
      ],
      "notes": [
        "模型支持图像输入；未发现 Gemini 3.5 Flash 精确型号结果。Gemini 3.5 Flash-Lite 是不同型号。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "官方榜单精确列出 gemini-3.5-flash[high]：36%±4%，113 tasks；使用 mini-swe-agent。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash/"
        },
        {
          "label": "AA Gemini 3.5 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gemini-3-5-flash"
        },
        {
          "label": "AA GDPval methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "保留已有 GDPval-AA 1656 Elo；Google 未标 v2.1。AA 页面另报 High 配置 1201/1202 Elo，与现有项的 effort 不同。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法确认 1656 的目标版本；AA High 的 1 Elo 差异与 effort 配置未解决。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 version-specific model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash/"
        }
      ],
      "notes": [
        "源 TOML 已有 40.2% accuracy，数据集为 full set, text + MM，版本固定模型卡确认该成绩。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2 project page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "Google 报告的 OSWorld-Verified 78.4% 未标为 OSWorld 2.1，不能映射到目标版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到精确 OSWorld 2.1 原始结果；动态榜单无法完整核对目标型号。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash/"
        },
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Google 模型卡的 55.1% 属于 SWE-Bench Pro Public、single attempt；早于 V2 发布，不能映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到 Gemini 3.5 Flash 精确 V2 结果；Scale 榜单未显示该型号。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA Gemini 3.5 page",
          "url": "https://artificialanalysis.ai/models/gemini-3-5-flash"
        },
        {
          "label": "AA TB-Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "未找到 Gemini 3.5 Flash 对应 Terminal-Bench-Science 0.1 的公开分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.5 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash/"
        },
        {
          "label": "AA Gemini 3.5 page",
          "url": "https://artificialanalysis.ai/models/gemini-3-5-flash"
        },
        {
          "label": "AA TB4 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "Google 已报告的 76.2% 属于 Terminal-Bench 2.1；未找到该模型 v4.0 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "检查 2026-10-30 更新的官方 V2.2 榜单，未发现 Gemini 3.5 Flash 精确型号。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 10,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T05:58+08:00",
  "model_id": "google/gemini-3.5-flash",
  "model_notes": [
    "模型身份为 Google Gemini 3.5 Flash，发布日期 2026-05-19。",
    "将 10 条既有成绩的来源链接改为版本固定模型卡；移除 10 个等同发布日的 date 字段，因为 Google 仅说明结果截至 2026 年 5 月，没有逐项评测日期。",
    "保留 SWE-Bench Pro、Terminal-Bench 2.1、OSWorld-Verified 与 GDPval-AA 原始记录，不将其自动映射到目标版本。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 10
}

-->
