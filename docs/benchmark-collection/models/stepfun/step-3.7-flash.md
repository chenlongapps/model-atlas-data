# Step 3.7 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：stepfun/step-3.7-flash
- 模型名称：Step 3.7 Flash
- 发布日期：2026-05-29
- 最近检查时间：2026-11-05T05:14+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：11
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T05:14+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Step 3.7 Flash published evaluation artifact](https://huggingface.co/stepfun-ai/Step-3.7-Flash/blob/031fea7380bbe94d91fefadc043af05dc385d1d5/.eval_results/swe_bench_pro.yaml), [SWE-bench Pro dataset/version information](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-05T05:14+08:00 |
| terminal-bench-v4 | 待核实 | 59.6 (metric=success rate; version=2.1) | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/), [StepFun release page](https://static.stepfun.com/blog/step-3.7-flash/), [Artificial Analysis Step 3.7 Flash page](https://artificialanalysis.ai/models/step-3-7-flash) | 2026-11-05T05:14+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T05:14+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05T05:14+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld official results](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T05:14+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official evaluation repository](https://github.com/surge-ai/chartography) | 2026-11-05T05:14+08:00 |
| humanitys-last-exam | 已存在 | 47.2 (metric=accuracy; variant=with tools) | [StepFun release page](https://static.stepfun.com/blog/step-3.7-flash/) | 2026-11-05T05:14+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Step 3.7 Flash comparison](https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:14+08:00 |
| gdpval-aa-v2.1 | 已收录 | 856 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; harness=Stirrup) | [Artificial Analysis Step 3.7 Flash comparison](https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:14+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T05:14+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 当前 v1.1 榜单只显示 21/28 个模型，未见 Step 3.7 Flash；不能据此确认没有成绩。

尚未解决的问题：
- 公开榜单并非完整模型列表。

最近核验时间：2026-11-05T05:14+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Step 3.7 Flash published evaluation artifact](https://huggingface.co/stepfun-ai/Step-3.7-Flash/blob/031fea7380bbe94d91fefadc043af05dc385d1d5/.eval_results/swe_bench_pro.yaml)
- [SWE-bench Pro dataset/version information](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- 已有未标版本的 SWE-Bench Pro 56.3；来源工件日期为 2026-05-23，早于 Pro V2 2.0.0 发布，不能映射为 V2。

尚未解决的问题：
- 需找到明确标注 Pro V2 的该型号成绩。

最近核验时间：2026-11-05T05:14+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 59.6
- metric: success rate
- version: 2.1
- source: [https://static.stepfun.com/blog/step-3.7-flash/](https://static.stepfun.com/blog/step-3.7-flash/)
- date: 2026-05-29
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/)
- [StepFun release page](https://static.stepfun.com/blog/step-3.7-flash/)
- [Artificial Analysis Step 3.7 Flash page](https://artificialanalysis.ai/models/step-3-7-flash)

研究备注：
- 已有 59.6 明确属于 Terminal-Bench 2.1，不迁移至 4.0；公开表未能确认 Step 3.7 Flash 的 v4 成绩。Step 官方发布页当前写 2.1 为 59.5，与旧记录 59.6 不同，未据此覆盖。

尚未解决的问题：
- 需有该型号 v4 的完整、可核验排行榜行。

最近核验时间：2026-11-05T05:14+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 检查 v0.1 官方结果表，未列 Step 3.7 Flash。

最近核验时间：2026-11-05T05:14+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 模型支持工具调用，适用；榜单只公开前 10 项，另有 119 项折叠，无法确认完整列表。

尚未解决的问题：
- 完整排行榜内容当前不可见。

最近核验时间：2026-11-05T05:14+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld official results](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 官方资料确认模型具备视觉工具及 GUI 操作能力，适用；官方结果页为动态内容，未核实 v2.1 精确成绩。Android Daily 61.87% 不是 OSWorld。

尚未解决的问题：
- 动态榜单未能确认该型号 v2.1 结果。

最近核验时间：2026-11-05T05:14+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official evaluation repository](https://github.com/surge-ai/chartography)

研究备注：
- 检查 Surge AI 官方榜和评测仓库，未列 Step 3.7 Flash；Gemini 3.7 Flash 是不同型号。

最近核验时间：2026-11-05T05:14+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 47.2
- metric: accuracy
- variant: with tools
- source: [https://static.stepfun.com/blog/step-3.7-flash/](https://static.stepfun.com/blog/step-3.7-flash/)
- date: 2026-05-29
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [StepFun release page](https://static.stepfun.com/blog/step-3.7-flash/)

研究备注：
- 已有 47.2 accuracy、with tools 记录，StepFun 官方发布页支持该成绩，予以保留。AA 的 21% 未披露对应工具配置，不合并。

最近核验时间：2026-11-05T05:14+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Step 3.7 Flash comparison](https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前页面无该型号 V5 成绩；历史 19* 是 v4.3.2 估计值，不迁移至 V5。

最近核验时间：2026-11-05T05:14+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 856
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202](https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis Step 3.7 Flash comparison](https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 直接比较页给出 v2.1 856 Elo；方法页说明此版本共 220 项任务。评测日期和模型 effort 未披露。

最近核验时间：2026-11-05T05:14+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 检查 v2.2 官方榜单，未列 Step 3.7 Flash；不迁移其他版本或相近型号成绩。

最近核验时间：2026-11-05T05:14+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Step 3.7 Flash comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前页面无该型号 V5 成绩；历史 19* 是 v4.3.2 估计值，不迁移至 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "模型支持工具调用，适用；榜单只公开前 10 项，另有 119 项折叠，无法确认完整列表。"
      ],
      "status": "待核实",
      "unresolved": [
        "完整排行榜内容当前不可见。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "检查 Surge AI 官方榜和评测仓库，未列 Step 3.7 Flash；Gemini 3.7 Flash 是不同型号。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T05:14+08:00",
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
        "当前 v1.1 榜单只显示 21/28 个模型，未见 Step 3.7 Flash；不能据此确认没有成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开榜单并非完整模型列表。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Step 3.7 Flash comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/step-3-7-flash-vs-step-3-5-flash-0202"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 直接比较页给出 v2.1 856 Elo；方法页说明此版本共 220 项任务。评测日期和模型 effort 未披露。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "StepFun release page",
          "url": "https://static.stepfun.com/blog/step-3.7-flash/"
        }
      ],
      "notes": [
        "已有 47.2 accuracy、with tools 记录，StepFun 官方发布页支持该成绩，予以保留。AA 的 21% 未披露对应工具配置，不合并。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "OSWorld official results",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "官方资料确认模型具备视觉工具及 GUI 操作能力，适用；官方结果页为动态内容，未核实 v2.1 精确成绩。Android Daily 61.87% 不是 OSWorld。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单未能确认该型号 v2.1 结果。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Step 3.7 Flash published evaluation artifact",
          "url": "https://huggingface.co/stepfun-ai/Step-3.7-Flash/blob/031fea7380bbe94d91fefadc043af05dc385d1d5/.eval_results/swe_bench_pro.yaml"
        },
        {
          "label": "SWE-bench Pro dataset/version information",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "已有未标版本的 SWE-Bench Pro 56.3；来源工件日期为 2026-05-23，早于 Pro V2 2.0.0 发布，不能映射为 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "需找到明确标注 Pro V2 的该型号成绩。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "检查 v0.1 官方结果表，未列 Step 3.7 Flash。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "StepFun release page",
          "url": "https://static.stepfun.com/blog/step-3.7-flash/"
        },
        {
          "label": "Artificial Analysis Step 3.7 Flash page",
          "url": "https://artificialanalysis.ai/models/step-3-7-flash"
        }
      ],
      "notes": [
        "已有 59.6 明确属于 Terminal-Bench 2.1，不迁移至 4.0；公开表未能确认 Step 3.7 Flash 的 v4 成绩。Step 官方发布页当前写 2.1 为 59.5，与旧记录 59.6 不同，未据此覆盖。"
      ],
      "status": "待核实",
      "unresolved": [
        "需有该型号 v4 的完整、可核验排行榜行。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "检查 v2.2 官方榜单，未列 Step 3.7 Flash；不迁移其他版本或相近型号成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 11,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T05:14+08:00",
  "model_id": "stepfun/step-3.7-flash",
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
