# MiMo-V2.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2.5
- 模型名称：MiMo-V2.5
- 发布日期：2026-04-22
- 最近检查时间：2026-11-05T08:19+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：1
- 收集前已有成绩数量：12
- 当前已收录的对应成绩数量：1

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 12.39 (metric=task success rate; version=1.1; dataset=113 tasks; 3 samples per task; variant=MiMo-V2.5 w/ Vanilla; 512K context; temperature 1.0; top_p 0.95) | [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256) | 2026-11-05T08:12+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5), [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256), [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:12+08:00 |
| terminal-bench-v4 | 待核实 | 65.8 (metric=score; version=2.0) | [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5), [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:12+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science), [https://github.com/harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-05T08:12+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://github.com/zapier/AutomationBench](https://github.com/zapier/AutomationBench), [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5) | 2026-11-05T08:12+08:00 |
| osworld-v2.1 | 待核实 | — | [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5) | 2026-11-05T08:12+08:00 |
| chartography | 待核实 | — | [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography), [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5) | 2026-11-05T08:12+08:00 |
| humanitys-last-exam | 待核实 | 27 (metric=pass@1; dataset=Artificial Analysis text-only subset; 2,158 questions; variant=MiMo-V2.5 (Artificial Analysis legacy HLE evaluation)) | [https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T08:19+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/mimo-v2-5-0424](https://artificialanalysis.ai/models/mimo-v2-5-0424), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T08:12+08:00 |
| gdpval-aa-v2.1 | 待核实 | 996 (metric=Elo rating; version=2.1; dataset=220 tasks; variant=MiMo-V2.5 (Artificial Analysis comparison); harness=Stirrup) | [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T08:19+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.vals.ai/models/xiaomi_mimo-v2.5](https://www.vals.ai/models/xiaomi_mimo-v2.5) | 2026-11-05T08:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 12.39
- metric: task success rate
- version: 1.1
- dataset: 113 tasks; 3 samples per task
- variant: MiMo-V2.5 w/ Vanilla; 512K context; temperature 1.0; top_p 0.95
- source: [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256)

研究备注：
- 小米作者论文报告 MiMo-V2.5 w/ Vanilla 为 12.39 task success rate；113 个任务、每任务 3 个样本、512K context、temperature 1.0、top_p 0.95。该原始指标不是本仓定义的 pass@1，先保留原始行但不计目标覆盖。

尚未解决的问题：
- 论文未将这一聚合 task success rate 明确写成 pass@1；harness 和评测日期未说明。

最近核验时间：2026-11-05T08:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)
- [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256)
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 模型卡已有未注明版本的 56.1；小米作者论文另报 731-task SWE-bench Pro Vanilla 为 50.11。两者均不能映射到使用 642 题的 V2。

尚未解决的问题：
- 未核实到精确 SWE-bench Pro V2 结果；动态榜单可见条目有限，不能据缺席断言未找到。

最近核验时间：2026-11-05T08:12+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 65.8
- metric: score
- version: 2.0
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)
- [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 本地模型卡成绩为 Terminal-Bench 2.0 的 65.8，不映射到目标 4.0；当前 Vals 榜单可见集合未确认精确 MiMo-V2.5 行。

尚未解决的问题：
- 未核实到版本 4.0 的精确成绩；动态榜单未显示不能证明没有成绩。

最近核验时间：2026-11-05T08:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- [https://github.com/harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- 核对了目标版本的公开页面；当前可见模型集合未提供精确 MiMo-V2.5 成绩。

尚未解决的问题：
- 榜单是动态/有限显示，不能据缺席断言未找到。

最近核验时间：2026-11-05T08:12+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://github.com/zapier/AutomationBench](https://github.com/zapier/AutomationBench)
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)

研究备注：
- 模型支持工具和多模态输入，能力上适用；官方排行榜当前只显示部分条目，不能确认精确型号成绩。

尚未解决的问题：
- 未取得可读且能核实精确型号的官方结果行。

最近核验时间：2026-11-05T08:12+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)

研究备注：
- 模型具备图像理解及 agent 能力；公开 OSWorld 页面当前可见内容未确认精确版本成绩。

尚未解决的问题：
- 动态结果页未列出精确型号；缺席不能作为未找到结论。

最近核验时间：2026-11-05T08:12+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)

研究备注：
- MiMo-V2.5 接受图像并输出文本，能力上适用；Surge 榜单的可读动态结果未确认精确型号行。

尚未解决的问题：
- 未获得可核实的精确成绩。

最近核验时间：2026-11-05T08:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 27
- metric: pass@1
- dataset: Artificial Analysis text-only subset; 2,158 questions
- variant: MiMo-V2.5 (Artificial Analysis legacy HLE evaluation)
- source: [https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 比较页报告 27%；AA 旧 HLE 方法是原始 HLE 的 2,158 道 text-only 子集，指标 pass@1。该结果是明确的子集条件，不等于完整 2,500 题多模态设置。

尚未解决的问题：
- 该记录 metric=pass@1，与本地完整 HLE 定义 metric=accuracy 不同，因此原始分数保留但不计 HLE 覆盖。

最近核验时间：2026-11-05T08:19+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/mimo-v2-5-0424](https://artificialanalysis.ai/models/mimo-v2-5-0424)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前 AA 精确型号页显示 Intelligence Index 为 N/A；历史 V4.x 分数不映射为 V5。

最近核验时间：2026-11-05T08:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 996
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- variant: MiMo-V2.5 (Artificial Analysis comparison)
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA 历史/缓存比较页曾列 base Elo 996；该比较页当前已动态更新，不再显示该行。原始记录保留并待复核，当前不可称为可见排行榜成绩。

尚未解决的问题：
- 缺少当前可见或可归档快照来独立复核 996 及其运行条件；未填写评测日期。

最近核验时间：2026-11-05T08:19+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.vals.ai/models/xiaomi_mimo-v2.5](https://www.vals.ai/models/xiaomi_mimo-v2.5)

研究备注：
- 当前 v2.2 榜单只显示有限的最新/frontier 模型；模型页概览及旧 v2.0 成绩未能确认是 v2.2 指数结果。

尚未解决的问题：
- 没有可核验的精确 v2.2 数值；动态页面缺席不作为未找到。

最近核验时间：2026-11-05T08:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/mimo-v2-5-0424"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前 AA 精确型号页显示 Intelligence Index 为 N/A；历史 V4.x 分数不映射为 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5"
        }
      ],
      "notes": [
        "模型支持工具和多模态输入，能力上适用；官方排行榜当前只显示部分条目，不能确认精确型号成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "未取得可读且能核实精确型号的官方结果行。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5"
        }
      ],
      "notes": [
        "MiMo-V2.5 接受图像并输出文本，能力上适用；Surge 榜单的可读动态结果未确认精确型号行。"
      ],
      "status": "待核实",
      "unresolved": [
        "未获得可核实的精确成绩。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://arxiv.org/html/2610.40256"
        }
      ],
      "notes": [
        "小米作者论文报告 MiMo-V2.5 w/ Vanilla 为 12.39 task success rate；113 个任务、每任务 3 个样本、512K context、temperature 1.0、top_p 0.95。该原始指标不是本仓定义的 pass@1，先保留原始行但不计目标覆盖。"
      ],
      "status": "待核实",
      "unresolved": [
        "论文未将这一聚合 task success rate 明确写成 pass@1；harness 和评测日期未说明。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:19+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA 历史/缓存比较页曾列 base Elo 996；该比较页当前已动态更新，不再显示该行。原始记录保留并待复核，当前不可称为可见排行榜成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "缺少当前可见或可归档快照来独立复核 996 及其运行条件；未填写评测日期。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:19+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/claude-sonnet-4-6-adaptive-vs-mimo-v2-5-0424"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 比较页报告 27%；AA 旧 HLE 方法是原始 HLE 的 2,158 道 text-only 子集，指标 pass@1。该结果是明确的子集条件，不等于完整 2,500 题多模态设置。"
      ],
      "status": "待核实",
      "unresolved": [
        "该记录 metric=pass@1，与本地完整 HLE 定义 metric=accuracy 不同，因此原始分数保留但不计 HLE 覆盖。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5"
        }
      ],
      "notes": [
        "模型具备图像理解及 agent 能力；公开 OSWorld 页面当前可见内容未确认精确版本成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态结果页未列出精确型号；缺席不能作为未找到结论。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5"
        },
        {
          "url": "https://arxiv.org/html/2610.40256"
        },
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "模型卡已有未注明版本的 56.1；小米作者论文另报 731-task SWE-bench Pro Vanilla 为 50.11。两者均不能映射到使用 642 题的 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "未核实到精确 SWE-bench Pro V2 结果；动态榜单可见条目有限，不能据缺席断言未找到。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "核对了目标版本的公开页面；当前可见模型集合未提供精确 MiMo-V2.5 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单是动态/有限显示，不能据缺席断言未找到。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5"
        },
        {
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "本地模型卡成绩为 Terminal-Bench 2.0 的 65.8，不映射到目标 4.0；当前 Vals 榜单可见集合未确认精确 MiMo-V2.5 行。"
      ],
      "status": "待核实",
      "unresolved": [
        "未核实到版本 4.0 的精确成绩；动态榜单未显示不能证明没有成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:12+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.vals.ai/models/xiaomi_mimo-v2.5"
        }
      ],
      "notes": [
        "当前 v2.2 榜单只显示有限的最新/frontier 模型；模型页概览及旧 v2.0 成绩未能确认是 v2.2 指数结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有可核验的精确 v2.2 数值；动态页面缺席不作为未找到。"
      ]
    }
  },
  "existing_records": 12,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:19+08:00",
  "model_id": "xiaomi/mimo-v2.5",
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
