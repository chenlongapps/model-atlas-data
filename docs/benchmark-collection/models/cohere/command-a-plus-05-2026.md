# Command A Plus Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：cohere/command-a-plus-05-2026
- 模型名称：Command A Plus
- 发布日期：2026-05-20
- 最近检查时间：2026-11-05T05:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- 模型身份为 Cohere Command A Plus（API ID command-a-plus-05-2026），发布日期 2026-05-20。
- GDPval-AA v2.1 存在 514/522 Elo 差异，保留冲突状态且未新增该成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T05:58+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T05:58+08:00 |
| terminal-bench-v4 | 已收录 | 1 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=pass@1 averaged over 3 repeats; harness=mini-swe-agent) | [AA Command A+ comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus), [AA Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T05:58+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 0 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=pass@1 averaged over 3 repeats; harness=mini-swe-agent) | [AA Command A+ comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus), [AA Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T05:58+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench) | 2026-11-05T05:58+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2 project page](https://osworld-v2.xlang.ai/) | 2026-11-05T05:58+08:00 |
| chartography | 未找到 | — | [Surge Chartography](https://surgehq.ai/benchmarks/chartography), [Chartography repository](https://github.com/surge-ai/chartography) | 2026-11-05T05:58+08:00 |
| humanitys-last-exam | 已收录 | 12 (metric=accuracy; dataset=May 2025 revision; 2,158 text-only questions; variant=pass@1) | [AA Command A+ comparison](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-claude-sonnet-4-6-adaptive), [AA HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 6 (metric=index score; version=5.0.1) | [AA Command A+ model page](https://artificialanalysis.ai/models/command-a-plus), [AA comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus) | 2026-11-05T05:58+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [AA comparison showing 514](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gemini-3-5-flash-medium), [AA comparison showing 522](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gpt-5), [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T05:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 当前 v1.1 榜单显示 21/28 个模型，未见 Command A+。

尚未解决的问题：
- 公开可见列表不完整，无法确认未展示条目是否包含该型号。

最近核验时间：2026-11-05T05:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查了 2026-09-22 发布的 V2 榜单，未找到 Command A+ 精确型号结果。

尚未解决的问题：
- 当前公开榜单展示的型号集合不完整，无法据缺少条目判定未评测。

最近核验时间：2026-11-05T05:58+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 1
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: pass@1 averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [AA Command A+ comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus)
- [AA Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- AA 对比页报告 1%；方法为 66 项任务、mini-swe-agent、pass@1，每任务三次重复平均。

最近核验时间：2026-11-05T05:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 0
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: pass@1 averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [AA Command A+ comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus)
- [AA Terminal-Bench-Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 对比页报告 0%；方法为 70 项任务、mini-swe-agent、pass@1，每任务三次重复平均。

最近核验时间：2026-11-05T05:58+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)

研究备注：
- Command A+ 有工具调用与图像输入能力，可能适用；官方榜单其余型号折叠。

尚未解决的问题：
- 无法查看完整官方榜单以确认目标型号是否已测。

最近核验时间：2026-11-05T05:58+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2 project page](https://osworld-v2.xlang.ai/)

研究备注：
- Command A+ 支持图像和工具；未找到精确型号与 OSWorld 2.1 对应的原始分数。

尚未解决的问题：
- 官方动态页面未能完整确认目标型号是否存在。

最近核验时间：2026-11-05T05:58+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography](https://surgehq.ai/benchmarks/chartography)
- [Chartography repository](https://github.com/surge-ai/chartography)

研究备注：
- 模型支持图像输入；检查 Surge 官方榜单和项目资料，未发现 Command A+ 精确型号分数。

最近核验时间：2026-11-05T05:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 12
- metric: accuracy
- dataset: May 2025 revision; 2,158 text-only questions
- variant: pass@1
- source: [https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-claude-sonnet-4-6-adaptive](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-claude-sonnet-4-6-adaptive)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [AA Command A+ comparison](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-claude-sonnet-4-6-adaptive)
- [AA HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 报告 12% accuracy；使用 May 2025 revision 中 2,158 道 text-only 题目，pass@1。

最近核验时间：2026-11-05T05:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 6
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/command-a-plus](https://artificialanalysis.ai/models/command-a-plus)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [AA Command A+ model page](https://artificialanalysis.ai/models/command-a-plus)
- [AA comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus)

研究备注：
- 当前 Artificial Analysis Intelligence Index v5.0.1 分数为 6；不采用旧版指数分数。

最近核验时间：2026-11-05T05:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [AA comparison showing 514](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gemini-3-5-flash-medium)
- [AA comparison showing 522](https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gpt-5)
- [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 页面分别显示 514 与 522 Elo，均标为 GDPval-AA v2.1；该版覆盖 220 项任务并以 Elo 评定。

尚未解决的问题：
- 公开页面数值不一致，无法判定评测日期或修订关系；未写入单一分数。

最近核验时间：2026-11-05T05:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查 2026-10-30 更新的官方榜单，未发现 Command A+ 精确型号。

最近核验时间：2026-11-05T05:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA Command A+ model page",
          "url": "https://artificialanalysis.ai/models/command-a-plus"
        },
        {
          "label": "AA comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus"
        }
      ],
      "notes": [
        "当前 Artificial Analysis Intelligence Index v5.0.1 分数为 6；不采用旧版指数分数。"
      ],
      "status": "已收录",
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
        "Command A+ 有工具调用与图像输入能力，可能适用；官方榜单其余型号折叠。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法查看完整官方榜单以确认目标型号是否已测。"
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
          "label": "Chartography repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "模型支持图像输入；检查 Surge 官方榜单和项目资料，未发现 Command A+ 精确型号分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "当前 v1.1 榜单显示 21/28 个模型，未见 Command A+。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开可见列表不完整，无法确认未展示条目是否包含该型号。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA comparison showing 514",
          "url": "https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gemini-3-5-flash-medium"
        },
        {
          "label": "AA comparison showing 522",
          "url": "https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-gpt-5"
        },
        {
          "label": "AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 页面分别显示 514 与 522 Elo，均标为 GDPval-AA v2.1；该版覆盖 220 项任务并以 Elo 评定。"
      ],
      "status": "冲突",
      "unresolved": [
        "公开页面数值不一致，无法判定评测日期或修订关系；未写入单一分数。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA Command A+ comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/command-a-plus-vs-claude-sonnet-4-6-adaptive"
        },
        {
          "label": "AA HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 报告 12% accuracy；使用 May 2025 revision 中 2,158 道 text-only 题目，pass@1。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
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
        "Command A+ 支持图像和工具；未找到精确型号与 OSWorld 2.1 对应的原始分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态页面未能完整确认目标型号是否存在。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查了 2026-09-22 发布的 V2 榜单，未找到 Command A+ 精确型号结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前公开榜单展示的型号集合不完整，无法据缺少条目判定未评测。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA Command A+ comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus"
        },
        {
          "label": "AA Terminal-Bench-Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 对比页报告 0%；方法为 70 项任务、mini-swe-agent、pass@1，每任务三次重复平均。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T05:58+08:00",
      "checked_sources": [
        {
          "label": "AA Command A+ comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-command-a-plus"
        },
        {
          "label": "AA Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "AA 对比页报告 1%；方法为 66 项任务、mini-swe-agent、pass@1，每任务三次重复平均。"
      ],
      "status": "已收录",
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
        "检查 2026-10-30 更新的官方榜单，未发现 Command A+ 精确型号。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T05:58+08:00",
  "model_id": "cohere/command-a-plus-05-2026",
  "model_notes": [
    "模型身份为 Cohere Command A Plus（API ID command-a-plus-05-2026），发布日期 2026-05-20。",
    "GDPval-AA v2.1 存在 514/522 Elo 差异，保留冲突状态且未新增该成绩。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
