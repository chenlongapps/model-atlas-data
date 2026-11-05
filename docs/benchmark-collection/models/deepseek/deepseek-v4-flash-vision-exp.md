# DeepSeek V4 Flash Vision Exp Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4-flash-vision-exp
- 模型名称：DeepSeek V4 Flash Vision Exp
- 发布日期：2026-08-21
- 最近检查时间：2026-11-04T16:46+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 收集前已有成绩数量：11
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 59.3 (metric=score; variant=max effort; harness=DeepSeek Harness minimal mode) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp), [DeepSWE v1.1 官方榜单与方法](https://deepswe.datacurve.ai/) | 2026-11-04T16:46+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp), [Scale SWE-bench Pro 数据集](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [Scale SWE-bench Pro V2 排行榜](https://scale.com/leaderboard/swe_bench_pro) | 2026-11-04T16:46+08:00 |
| terminal-bench-v4 | 未找到 | 83.9 (metric=score; version=2.1; variant=max effort; harness=DeepSeek Harness minimal mode) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp), [Vals Terminal-Bench 4 榜单](https://www.vals.ai/benchmarks/terminal-bench-4), [Terminal-Bench 4 官方页面](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T16:46+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp), [Vals Terminal-Bench Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench Science 评测](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T16:46+08:00 |
| automationbench-v1.0.6 | 待核实 | 25.7 (metric=score; dataset=public; variant=max effort; harness=DeepSeek Harness minimal mode) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp), [Zapier AutomationBench 榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T16:46+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2.1 官方发布结果](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | 2026-11-04T16:46+08:00 |
| chartography | 冲突 | 64.3 (metric=score); 11.2 (metric=accuracy (mean; Pass@1); dataset=Chartography full task set; effort=Max reasoning; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp), [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测代码和排行榜配置](https://github.com/surge-ai/chartography) | 2026-11-04T16:46+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale 原版 Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | 2026-11-04T16:46+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis 精确模型页面](https://artificialanalysis.ai/models/deepseek-v4-flash-vision), [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T16:46+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1554 (metric=Elo rating; version=2.1; dataset=GDPval (220 tasks); effort=Max; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence Index 与评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T16:46+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index), [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | 2026-11-04T16:46+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 59.3
- metric: score
- variant: max effort
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- [DeepSWE v1.1 官方榜单与方法](https://deepswe.datacurve.ai/)

研究备注：
- 官方模型卡列 DeepSWE 59.3，但未注明 benchmark 版本或指标；v1.1 榜单未找到该精确模型。保留原 TOML 记录，不将其推定为 v1.1 pass@1。

尚未解决的问题：
- 需要来源明确 DeepSWE 59.3 的版本与评分指标，才能映射到 v1.1。

最近核验时间：2026-11-04T16:46+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- [Scale SWE-bench Pro 数据集](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [Scale SWE-bench Pro V2 排行榜](https://scale.com/leaderboard/swe_bench_pro)

研究备注：
- 模型卡和 Scale V2 榜单均未找到该模型的 SWE-bench Pro V2 成绩。

最近核验时间：2026-11-04T16:46+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 83.9
- metric: score
- version: 2.1
- variant: max effort
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- [Vals Terminal-Bench 4 榜单](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Terminal-Bench 4 官方页面](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 现有 83.9 分明确标注为 Terminal-Bench 2.1；Vals v4 榜单未列该模型。未把 2.1 成绩映射到 v4。

最近核验时间：2026-11-04T16:46+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- [Vals Terminal-Bench Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench Science 评测](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 模型卡及已检查的 Vals、Artificial Analysis 榜单未找到 Terminal-Bench Science v0.1 成绩。

最近核验时间：2026-11-04T16:46+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 25.7
- metric: score
- dataset: public
- variant: max effort
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- [Zapier AutomationBench 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- 官方模型卡列 AutomationBench (Public) 25.7，并说明文字 Agent 评测使用 DeepSeek Harness minimal mode、max effort、temperature 1.0、top_p 0.95；未注明该分数对应 v1.0.6 或 task_completed_correctly。Zapier 官方榜单的 private task set 与 public 结果不可等同。保留原记录，不补写版本或指标。

尚未解决的问题：
- 需要确认 public 25.7 的评测版本和 metric 是否与本地 v1.0.6 定义相同。

最近核验时间：2026-11-04T16:46+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2.1 官方发布结果](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)

研究备注：
- 官方 v2.1 release JSON 未找到 DeepSeek V4 Flash Vision Exp 的成绩；模型支持图像输入和工具调用，因此记为已检查未找到，而非不适用。

最近核验时间：2026-11-04T16:46+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 64.3
- metric: score
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Chartography
- score: 11.2
- metric: accuracy (mean; Pass@1)
- dataset: Chartography full task set
- effort: Max reasoning
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测代码和排行榜配置](https://github.com/surge-ai/chartography)

研究备注：
- DeepSeek 官方模型卡列 64.3，但未说明 metric 或测试条件。Surge 官方榜单以名称 V4 Flash Vision (experimental) (Max reasoning) 列 11.2%；名称与模型匹配，但榜单未列 checkpoint/backend。Chartography 仓库将 accuracy/mean 定义为 Pass@1，并说明榜单配置为完整任务集、每项 10 次运行、Gemini 3.5 Flash judge，支持 reasoning effort。两个结果均保留；未选择较高值。

尚未解决的问题：
- 官方模型卡 64.3 与 Surge 11.2 的测试配置差异未说明，不能判断是否是相同评测条件或同一结果的修订。

最近核验时间：2026-11-04T16:46+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale 原版 Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)

研究备注：
- 原版 HLE 官方榜单未列该模型。未将 HLE-Rolling 或 HLE-Diamond 子集成绩映射为本项原版 HLE。

最近核验时间：2026-11-04T16:46+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 精确模型页面](https://artificialanalysis.ai/models/deepseek-v4-flash-vision)
- [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 精确模型页面的 Artificial Analysis Intelligence Index 显示 N/A，无综合指数成绩。页面介绍当前方法版本 v5.0.1，而本地定义为 v5.0；该方法信息不是模型成绩。

最近核验时间：2026-11-04T16:46+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1554
- metric: Elo rating
- version: 2.1
- dataset: GDPval (220 tasks)
- effort: Max
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence Index 与评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 官方 v2.1 榜单精确列出 DeepSeek V4 Flash Vision (Max)：1554 Elo，置信区间 -17/+17。评测使用 Stirrup，基于 GDPval 220 项任务；Max 记为 effort。表内 Aug 2026 为模型发布月份，不作为 benchmark date。

最近核验时间：2026-11-04T16:46+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)
- [DeepSeek 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)

研究备注：
- Vals v2.2 官方榜单未列该模型；页面上的 DeepSeek V4.1 Flash 1017 等为不同模型版本，未映射。

最近核验时间：2026-11-04T16:46+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 精确模型页面",
          "url": "https://artificialanalysis.ai/models/deepseek-v4-flash-vision"
        },
        {
          "label": "Artificial Analysis Intelligence Index 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "精确模型页面的 Artificial Analysis Intelligence Index 显示 N/A，无综合指数成绩。页面介绍当前方法版本 v5.0.1，而本地定义为 v5.0；该方法信息不是模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        },
        {
          "label": "Zapier AutomationBench 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "官方模型卡列 AutomationBench (Public) 25.7，并说明文字 Agent 评测使用 DeepSeek Harness minimal mode、max effort、temperature 1.0、top_p 0.95；未注明该分数对应 v1.0.6 或 task_completed_correctly。Zapier 官方榜单的 private task set 与 public 结果不可等同。保留原记录，不补写版本或指标。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要确认 public 25.7 的评测版本和 metric 是否与本地 v1.0.6 定义相同。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        },
        {
          "label": "Surge Chartography 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测代码和排行榜配置",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "DeepSeek 官方模型卡列 64.3，但未说明 metric 或测试条件。Surge 官方榜单以名称 V4 Flash Vision (experimental) (Max reasoning) 列 11.2%；名称与模型匹配，但榜单未列 checkpoint/backend。Chartography 仓库将 accuracy/mean 定义为 Pass@1，并说明榜单配置为完整任务集、每项 10 次运行、Gemini 3.5 Flash judge，支持 reasoning effort。两个结果均保留；未选择较高值。"
      ],
      "status": "冲突",
      "unresolved": [
        "官方模型卡 64.3 与 Surge 11.2 的测试配置差异未说明，不能判断是否是相同评测条件或同一结果的修订。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        },
        {
          "label": "DeepSWE v1.1 官方榜单与方法",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "官方模型卡列 DeepSWE 59.3，但未注明 benchmark 版本或指标；v1.1 榜单未找到该精确模型。保留原 TOML 记录，不将其推定为 v1.1 pass@1。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要来源明确 DeepSWE 59.3 的版本与评分指标，才能映射到 v1.1。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Intelligence Index 与评测方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "官方 v2.1 榜单精确列出 DeepSeek V4 Flash Vision (Max)：1554 Elo，置信区间 -17/+17。评测使用 Stirrup，基于 GDPval 220 项任务；Max 记为 effort。表内 Aug 2026 为模型发布月份，不作为 benchmark date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "Scale 原版 Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        }
      ],
      "notes": [
        "原版 HLE 官方榜单未列该模型。未将 HLE-Rolling 或 HLE-Diamond 子集成绩映射为本项原版 HLE。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 官方发布结果",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        }
      ],
      "notes": [
        "官方 v2.1 release JSON 未找到 DeepSeek V4 Flash Vision Exp 的成绩；模型支持图像输入和工具调用，因此记为已检查未找到，而非不适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        },
        {
          "label": "Scale SWE-bench Pro 数据集",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "Scale SWE-bench Pro V2 排行榜",
          "url": "https://scale.com/leaderboard/swe_bench_pro"
        }
      ],
      "notes": [
        "模型卡和 Scale V2 榜单均未找到该模型的 SWE-bench Pro V2 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        },
        {
          "label": "Vals Terminal-Bench Science 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 评测",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "模型卡及已检查的 Vals、Artificial Analysis 榜单未找到 Terminal-Bench Science v0.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        },
        {
          "label": "Vals Terminal-Bench 4 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Terminal-Bench 4 官方页面",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "现有 83.9 分明确标注为 Terminal-Bench 2.1；Vals v4 榜单未列该模型。未把 2.1 成绩映射到 v4。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T16:46+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "DeepSeek 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp"
        }
      ],
      "notes": [
        "Vals v2.2 官方榜单未列该模型；页面上的 DeepSeek V4.1 Flash 1017 等为不同模型版本，未映射。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 11,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T16:46+08:00",
  "model_id": "deepseek/deepseek-v4-flash-vision-exp",
  "new_records": 2,
  "overall_status": "待复核"
}

-->
