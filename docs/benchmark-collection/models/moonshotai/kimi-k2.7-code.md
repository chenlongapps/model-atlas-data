# Kimi K2.7 Code Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：moonshotai/kimi-k2.7-code
- 模型名称：Kimi K2.7 Code
- 发布日期：2026-06-12
- 最近检查时间：2026-11-05T03:23+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 31.0 (metric=pass@1; version=1.1; dataset=113 tasks; effort=maximum reasoning effort; harness=mini-swe-agent) | [Cross-Benchmark Transfer 论文](https://arxiv.org/abs/2610.00890), [DeepSWE v1.1 官方说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T03:23+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale V2 说明](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T03:23+08:00 |
| terminal-bench-v4 | 待核实 | 0.0 (metric=pass@1; version=4.0; dataset=66 tasks; effort=maximum reasoning effort; harness=mini-swe-agent) | [Cross-Benchmark Transfer 论文](https://arxiv.org/abs/2610.00890), [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T03:23+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T03:23+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [AutomationBench 官方 README](https://github.com/zapier/AutomationBench), [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md) | 2026-11-05T03:23+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T03:23+08:00 |
| chartography | 已收录 | 0.0 (metric=accuracy (mean; Pass@1); version=unspecified; dataset=full 100-task released set; effort=Max reasoning; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方评测仓库](https://github.com/surge-ai/chartography) | 2026-11-05T03:23+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale Humanity’s Last Exam 榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [Artificial Analysis Kimi K2.7 Code 页面](https://artificialanalysis.ai/models/kimi-k2-7-code) | 2026-11-05T03:23+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Kimi K2.7 Code 页面](https://artificialanalysis.ai/models/kimi-k2-7-code) | 2026-11-05T03:23+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T03:23+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Kimi K2.7 Code 模型页](https://www.vals.ai/models/kimi_kimi-k2.7-code), [Vals Index v2.2 官方页](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T03:23+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 31.0
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: maximum reasoning effort
- harness: mini-swe-agent
- source: [https://arxiv.org/abs/2610.00890](https://arxiv.org/abs/2610.00890)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Cross-Benchmark Transfer 论文](https://arxiv.org/abs/2610.00890)
- [DeepSWE v1.1 官方说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Cross-Benchmark Transfer 论文将该模型列为 DeepSWE v1.1 的公开基线：31.0% pass@1、113 项、mini-swe-agent；论文没有提供评测日期。

最近核验时间：2026-11-05T03:23+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale V2 说明](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 核对了 Scale 的 SWE-bench Pro V2 Full 榜单；可见 Kimi K3 项，不是 Kimi K2.7 Code，未找到当前模型的 V2 成绩。

最近核验时间：2026-11-05T03:23+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 0.0
- metric: pass@1
- version: 4.0
- dataset: 66 tasks
- effort: maximum reasoning effort
- harness: mini-swe-agent
- source: [https://arxiv.org/abs/2610.00890](https://arxiv.org/abs/2610.00890)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Cross-Benchmark Transfer 论文](https://arxiv.org/abs/2610.00890)
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Cross-Benchmark Transfer 论文确实报告 Kimi K2.7 Code 在 Terminal-Bench 4 的 0.0% pass@1（66 项，mini-swe-agent）。原始成绩已写入 TOML；本地定义使用 task resolution rate 和版本 4.0.0，论文使用 pass@1 和 Terminal-Bench 4.0，精确映射未确认，因此覆盖率不计入。

尚未解决的问题：
- 原始分数可核实；metric 和 version 与本地定义字段不完全相同，需复核映射。

最近核验时间：2026-11-05T03:23+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 官方结果页列有 Kimi K3 的结果，但没有 Kimi K2.7 Code；未将 Kimi K3 成绩转用。

最近核验时间：2026-11-05T03:23+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方 README](https://github.com/zapier/AutomationBench)
- [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)

研究备注：
- Zapier 当前 1.0.6 榜单只在页面文本中显示前 10 行，其余 119 行折叠；无法据此确认 Kimi K2.7 Code 是否有分数，也不把 Kimi K3 的公开集结果转用。

尚未解决的问题：
- 官方榜单有折叠条目，当前可读页面不足以确认完整模型列表。

最近核验时间：2026-11-05T03:23+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 模型支持图像输入和工具，但没有找到此准确模型在 OSWorld 2.1 环境下的公开结果；此项仍适用，不标记为不适用。

最近核验时间：2026-11-05T03:23+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 0.0
- metric: accuracy (mean; Pass@1)
- version: unspecified
- dataset: full 100-task released set
- effort: Max reasoning
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography 官方评测仓库](https://github.com/surge-ai/chartography)

研究备注：
- Surge 官方榜列出 Kimi K2.7 Code (Max)，得分 0%。官方 README 说明 leaderboard 配置为完整 100 项、每项 10 次运行、Gemini 3.5 Flash judge；排行榜模型标注为 Max reasoning。

最近核验时间：2026-11-05T03:23+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale Humanity’s Last Exam 榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Artificial Analysis Kimi K2.7 Code 页面](https://artificialanalysis.ai/models/kimi-k2-7-code)

研究备注：
- Scale 榜单未列 Kimi K2.7 Code 的 HLE 原始成绩；Artificial Analysis 模型页中的 HLE-Diamond 是不同子项，未作为原始 HLE 记录。

最近核验时间：2026-11-05T03:23+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Kimi K2.7 Code 页面](https://artificialanalysis.ai/models/kimi-k2-7-code)

研究备注：
- Artificial Analysis 当前模型页未提供 Kimi K2.7 Code 的 V5 综合 Index 分数；HLE-Diamond 等组成项不等于综合 Index。

最近核验时间：2026-11-05T03:23+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 核对了 Artificial Analysis GDPval-AA v2.1 榜单，未找到 Kimi K2.7 Code 的精确版本记录；GDP.pdf 不作为 GDPval-AA。

最近核验时间：2026-11-05T03:23+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Kimi K2.7 Code 模型页](https://www.vals.ai/models/kimi_kimi-k2.7-code)
- [Vals Index v2.2 官方页](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 模型页显示 49.99% Accuracy，但没有标出 Vals Index 版本；不能确认它属于 v2.2，未写入 TOML。

尚未解决的问题：
- 49.99% 候选值缺少 Vals Index 版本标记，无法确认是否为 v2.2。

最近核验时间：2026-11-05T03:23+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Kimi K2.7 Code 页面",
          "url": "https://artificialanalysis.ai/models/kimi-k2-7-code"
        }
      ],
      "notes": [
        "Artificial Analysis 当前模型页未提供 Kimi K2.7 Code 的 V5 综合 Index 分数；HLE-Diamond 等组成项不等于综合 Index。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方 README",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "AutomationBench 官方变更记录",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        }
      ],
      "notes": [
        "Zapier 当前 1.0.6 榜单只在页面文本中显示前 10 行，其余 119 行折叠；无法据此确认 Kimi K2.7 Code 是否有分数，也不把 Kimi K3 的公开集结果转用。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单有折叠条目，当前可读页面不足以确认完整模型列表。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography 官方评测仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 官方榜列出 Kimi K2.7 Code (Max)，得分 0%。官方 README 说明 leaderboard 配置为完整 100 项、每项 10 次运行、Gemini 3.5 Flash judge；排行榜模型标注为 Max reasoning。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Cross-Benchmark Transfer 论文",
          "url": "https://arxiv.org/abs/2610.00890"
        },
        {
          "label": "DeepSWE v1.1 官方说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Cross-Benchmark Transfer 论文将该模型列为 DeepSWE v1.1 的公开基线：31.0% pass@1、113 项、mini-swe-agent；论文没有提供评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA 榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "核对了 Artificial Analysis GDPval-AA v2.1 榜单，未找到 Kimi K2.7 Code 的精确版本记录；GDP.pdf 不作为 GDPval-AA。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Scale Humanity’s Last Exam 榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Artificial Analysis Kimi K2.7 Code 页面",
          "url": "https://artificialanalysis.ai/models/kimi-k2-7-code"
        }
      ],
      "notes": [
        "Scale 榜单未列 Kimi K2.7 Code 的 HLE 原始成绩；Artificial Analysis 模型页中的 HLE-Diamond 是不同子项，未作为原始 HLE 记录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 2.1 官方公开评测指南",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "模型支持图像输入和工具，但没有找到此准确模型在 OSWorld 2.1 环境下的公开结果；此项仍适用，不标记为不适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale V2 说明",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "核对了 Scale 的 SWE-bench Pro V2 Full 榜单；可见 Kimi K3 项，不是 Kimi K2.7 Code，未找到当前模型的 V2 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方结果",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "官方结果页列有 Kimi K3 的结果，但没有 Kimi K2.7 Code；未将 Kimi K3 成绩转用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Cross-Benchmark Transfer 论文",
          "url": "https://arxiv.org/abs/2610.00890"
        },
        {
          "label": "Terminal-Bench 4.0 官方榜单",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Cross-Benchmark Transfer 论文确实报告 Kimi K2.7 Code 在 Terminal-Bench 4 的 0.0% pass@1（66 项，mini-swe-agent）。原始成绩已写入 TOML；本地定义使用 task resolution rate 和版本 4.0.0，论文使用 pass@1 和 Terminal-Bench 4.0，精确映射未确认，因此覆盖率不计入。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始分数可核实；metric 和 version 与本地定义字段不完全相同，需复核映射。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:23+08:00",
      "checked_sources": [
        {
          "label": "Vals Kimi K2.7 Code 模型页",
          "url": "https://www.vals.ai/models/kimi_kimi-k2.7-code"
        },
        {
          "label": "Vals Index v2.2 官方页",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 模型页显示 49.99% Accuracy，但没有标出 Vals Index 版本；不能确认它属于 v2.2，未写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "49.99% 候选值缺少 Vals Index 版本标记，无法确认是否为 v2.2。"
      ]
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:23+08:00",
  "model_id": "moonshotai/kimi-k2.7-code",
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
