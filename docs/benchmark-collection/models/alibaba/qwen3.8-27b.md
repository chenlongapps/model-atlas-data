# Qwen3.8 27B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-27b
- 模型名称：Qwen3.8 27B
- 发布日期：2026-08-14
- 最近检查时间：2026-11-04T17:05+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：30
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 42.2 (metric=score; version=1.1; harness=Claude Code) | [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B), [DeepSWE v1.1 官方 leaderboard 与方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T17:05+08:00 |
| swe-bench-pro-v2 | 已存在 | 61.7 (metric=task resolution rate; version=2.0.0; dataset=default (V2, 642 tasks); variant=temperature=1.0; top_p=0.95; context=256K; harness=Claude Code) | [Qwen 官方模型卡与评测条件](https://huggingface.co/Qwen/Qwen3.8-27B), [Scale 官方 SWE-bench Pro leaderboard](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [Scale 官方 V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T17:05+08:00 |
| terminal-bench-v4 | 未找到 | 73 (metric=score; version=2.1; harness=Terminus) | [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B), [Vals Terminal-Bench 4 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-4), [Terminal-Bench 4 官方说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T17:05+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B), [Vals Terminal-Bench Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench Science 页面](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T17:05+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B), [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks) | 2026-11-04T17:05+08:00 |
| osworld-v2.1 | 待核实 | — | [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B), [OSWorld V2.1 官方发布数据](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T17:05+08:00 |
| chartography | 未找到 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-11-04T17:05+08:00 |
| humanitys-last-exam | 待核实 | 30.8 (metric=accuracy; variant=without tools; GPT-4o judge) | [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B), [Humanity’s Last Exam 官方定义与准确率指标](https://lastexam.ai/) | 2026-11-04T17:05+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index 官方榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-11-04T17:05+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-11-04T17:05+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index), [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-11-04T17:05+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 42.2
- metric: score
- version: 1.1
- harness: Claude Code
- source: [https://huggingface.co/Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [DeepSWE v1.1 官方 leaderboard 与方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Qwen 官方卡确认 DeepSWE v1.1 分数 42.2，Claude Code harness、temperature=1.0、top_p=0.95、256K context。原记录的 metric=score 未与本地定义 pass@1 对齐；DeepSWE 官方页使用 pass rate，但未证实 Qwen 此次评测等同于 pass@1。保留原成绩和版本，不补猜指标。

尚未解决的问题：
- Qwen 卡片未明确该结果的评分 metric；需确认是否为 pass@1。

最近核验时间：2026-11-04T17:05+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 61.7
- metric: task resolution rate
- version: 2.0.0
- dataset: default (V2, 642 tasks)
- variant: temperature=1.0; top_p=0.95; context=256K
- harness: Claude Code
- source: [https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Qwen 官方模型卡与评测条件](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Scale 官方 SWE-bench Pro leaderboard](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [Scale 官方 V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- 已有分数 61.7 在 Scale 官方榜单中以精确模型 Qwen/Qwen3.8-27B 列出。Scale 文档确认默认配置为 V2、642 项、版本 2.0.0；Qwen 卡注明 Claude Code harness、temperature=1.0、top_p=0.95、256K context。已在 TOML 补齐版本、目标 metric 名称、default 数据集与条件；原分数未变。

最近核验时间：2026-11-04T17:05+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 73
- metric: score
- version: 2.1
- harness: Terminus
- source: [https://huggingface.co/Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Vals Terminal-Bench 4 官方榜单](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Terminal-Bench 4 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Qwen 卡只列 Terminal-Bench 2.1 的 73.0（Terminus）；Vals v4 榜单中的 Qwen 3.8 Max 不是 Qwen3.8-27B 权重。没有把 2.1 分数映射到 v4。

最近核验时间：2026-11-04T17:05+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Vals Terminal-Bench Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench Science 页面](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 模型卡和已查官方榜单未找到 Qwen3.8-27B 的 Terminal-Bench Science v0.1 结果。

最近核验时间：2026-11-04T17:05+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)

研究备注：
- 官方模型卡和 Zapier v1.0.6 榜单均未列该模型的结果。

最近核验时间：2026-11-04T17:05+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [OSWorld V2.1 官方发布数据](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- 模型卡列 OSWorld-Verified 84.3，但未说明其版本为 OSWorld 2.1；官方 v2.1 发布数据未列该模型。保留现有 OSWorld-Verified 原始行，不映射至 2.1。

尚未解决的问题：
- 需确认 OSWorld-Verified 84.3 使用的具体 release/version 和评测条件。

最近核验时间：2026-11-04T17:05+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)

研究备注：
- Surge 榜单未列 Qwen3.8-27B；Qwen 3.8 Max 的 29.1% 是不同产品/模型版本，未映射。

最近核验时间：2026-11-04T17:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 30.8
- metric: accuracy
- variant: without tools; GPT-4o judge
- source: [https://huggingface.co/Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Humanity’s Last Exam 官方定义与准确率指标](https://lastexam.ai/)

研究备注：
- 原有 30.8 分的 metric 已据 HLE 官方定义修正为 accuracy；模型卡说明由 GPT-4o 判分，但未明示工具设置或数据集变体。原 TOML 的 without tools 变体暂保留为历史记录，不视为已核验。

尚未解决的问题：
- 模型卡未确认 without-tools 条件，也未说明结果对应原始 HLE、HLE-Rolling 还是其它数据子集。

最近核验时间：2026-11-04T17:05+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index 官方榜单](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)

研究备注：
- AA 官方 V5.0.1 榜单和模型卡未找到 Qwen3.8-27B 的综合指数结果。

最近核验时间：2026-11-04T17:05+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA 官方榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)

研究备注：
- AA GDPval-AA v2.1 榜单和 Qwen 官方模型卡均未找到该模型结果。

最近核验时间：2026-11-04T17:05+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)
- [Qwen 官方模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)

研究备注：
- Vals v2.2 榜单未列 Qwen3.8-27B；榜单中的 Qwen 3.8 Max 不同于此开源权重。

最近核验时间：2026-11-04T17:05+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index 官方榜单",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        }
      ],
      "notes": [
        "AA 官方 V5.0.1 榜单和模型卡未找到 Qwen3.8-27B 的综合指数结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "官方模型卡和 Zapier v1.0.6 榜单均未列该模型的结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        }
      ],
      "notes": [
        "Surge 榜单未列 Qwen3.8-27B；Qwen 3.8 Max 的 29.1% 是不同产品/模型版本，未映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "DeepSWE v1.1 官方 leaderboard 与方法",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Qwen 官方卡确认 DeepSWE v1.1 分数 42.2，Claude Code harness、temperature=1.0、top_p=0.95、256K context。原记录的 metric=score 未与本地定义 pass@1 对齐；DeepSWE 官方页使用 pass rate，但未证实 Qwen 此次评测等同于 pass@1。保留原成绩和版本，不补猜指标。"
      ],
      "status": "待核实",
      "unresolved": [
        "Qwen 卡片未明确该结果的评分 metric；需确认是否为 pass@1。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA 官方榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        }
      ],
      "notes": [
        "AA GDPval-AA v2.1 榜单和 Qwen 官方模型卡均未找到该模型结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "Humanity’s Last Exam 官方定义与准确率指标",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "原有 30.8 分的 metric 已据 HLE 官方定义修正为 accuracy；模型卡说明由 GPT-4o 判分，但未明示工具设置或数据集变体。原 TOML 的 without tools 变体暂保留为历史记录，不视为已核验。"
      ],
      "status": "待核实",
      "unresolved": [
        "模型卡未确认 without-tools 条件，也未说明结果对应原始 HLE、HLE-Rolling 还是其它数据子集。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "OSWorld V2.1 官方发布数据",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "模型卡列 OSWorld-Verified 84.3，但未说明其版本为 OSWorld 2.1；官方 v2.1 发布数据未列该模型。保留现有 OSWorld-Verified 原始行，不映射至 2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 OSWorld-Verified 84.3 使用的具体 release/version 和评测条件。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡与评测条件",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "Scale 官方 SWE-bench Pro leaderboard",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "Scale 官方 V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "已有分数 61.7 在 Scale 官方榜单中以精确模型 Qwen/Qwen3.8-27B 列出。Scale 文档确认默认配置为 V2、642 项、版本 2.0.0；Qwen 卡注明 Claude Code harness、temperature=1.0、top_p=0.95、256K context。已在 TOML 补齐版本、目标 metric 名称、default 数据集与条件；原分数未变。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "Vals Terminal-Bench Science 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 页面",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "模型卡和已查官方榜单未找到 Qwen3.8-27B 的 Terminal-Bench Science v0.1 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        },
        {
          "label": "Vals Terminal-Bench 4 官方榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Terminal-Bench 4 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Qwen 卡只列 Terminal-Bench 2.1 的 73.0（Terminus）；Vals v4 榜单中的 Qwen 3.8 Max 不是 Qwen3.8-27B 权重。没有把 2.1 分数映射到 v4。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T17:05+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Qwen 官方模型卡",
          "url": "https://huggingface.co/Qwen/Qwen3.8-27B"
        }
      ],
      "notes": [
        "Vals v2.2 榜单未列 Qwen3.8-27B；榜单中的 Qwen 3.8 Max 不同于此开源权重。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 30,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T17:05+08:00",
  "model_id": "alibaba/qwen3.8-27b",
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
