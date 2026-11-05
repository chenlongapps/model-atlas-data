# Granite 4.2 8B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：ibm/granite-4.2-8b
- 模型名称：Granite 4.2 8B
- 发布日期：2026-08-25
- 最近检查时间：2026-11-04T16:29+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE 官方榜单](https://deepswe.datacurve.ai/), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b) | 2026-11-04T16:29+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b), [IBM Granite 4.2 技术文章](https://huggingface.co/blog/ibm-granite/granite-4-2), [Scale SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T16:29+08:00 |
| terminal-bench-v4 | 未找到 | — | [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b), [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Artificial Analysis Terminal-Bench 4.0 方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T16:29+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science 方法](https://artificialanalysis.ai/evaluations/terminal-bench-science), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b) | 2026-11-04T16:29+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Zapier AutomationBench 官方榜单与方法](https://zapier.com/benchmarks), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b), [IBM 官方发布文章](https://research.ibm.com/blog/introducing-granite-4-2) | 2026-11-04T16:29+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2.1 官方发布记录](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b) | 2026-11-04T16:29+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 论文与方法](https://arxiv.org/html/2608.10677v1), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b) | 2026-11-04T16:29+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale HLE 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [IBM Granite 官方模型与评测表](https://www.ibm.com/granite), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b) | 2026-11-04T16:29+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 5 (metric=index score; version=5.0.1) | [Artificial Analysis Granite 4.2 8B 官方模型页](https://artificialanalysis.ai/models/granite-4-2-8b/), [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T16:29+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 官方页面](https://artificialanalysis.ai/evaluations/gdpval-aa), [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b) | 2026-11-04T16:29+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Vals Granite 4.2 8B 官方模型页](https://www.vals.ai/models/ibm_granite-4.2-8b) | 2026-11-04T16:29+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)

研究备注：
- 官方榜单未见 Granite 4.2 8B 或对应别名；未将其他 Granite 型号的结果转给该模型。

最近核验时间：2026-11-04T16:29+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)
- [IBM Granite 4.2 技术文章](https://huggingface.co/blog/ibm-granite/granite-4-2)
- [Scale SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- IBM 发布的 SWE Bench Pro 19.11 未标注任务集版本；模型卡自动评测记录在 V2 于 2026-09-22 发布之前。Scale V2 榜单未找到 Granite 4.2 8B。因此未把 19.11 归入 V2，且未在本目标版本下新增该条。

最近核验时间：2026-11-04T16:29+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)
- [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Artificial Analysis Terminal-Bench 4.0 方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- IBM 模型卡的 Terminal-Bench 20.56 属于版本 2.1，不是目标 v4；Vals 榜单和 AA 方法页未提供 Granite 4.2 8B 的 v4 成绩。

最近核验时间：2026-11-04T16:29+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science 方法](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)

研究备注：
- 未在 Vals 或 Artificial Analysis 公开结果中找到 Granite 4.2 8B。IBM 模型卡里的 SciCode 是不同 Benchmark，未映射到 Terminal-Bench-Science。

最近核验时间：2026-11-04T16:29+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单与方法](https://zapier.com/benchmarks)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)
- [IBM 官方发布文章](https://research.ibm.com/blog/introducing-granite-4-2)

研究备注：
- 公开榜单与 IBM 发布资料未找到该模型的 AutomationBench v1.0.6 成绩。模型支持工具调用，故此项适用。

最近核验时间：2026-11-04T16:29+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2.1 官方发布记录](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)

研究备注：
- 官方 v2.1 发布记录没有 Granite 4.2 8B 或其仓库 ID；未找到可归属到目标版本的公开成绩。

最近核验时间：2026-11-04T16:29+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 论文与方法](https://arxiv.org/html/2608.10677v1)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)

研究备注：
- Chartography 输入图表图像并测量图表视觉理解；模型卡和仓库源文件都将 Granite 4.2 8B 列为仅文本输入，因此不适用。榜单也无该型号结果。

最近核验时间：2026-11-04T16:29+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale HLE 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [IBM Granite 官方模型与评测表](https://www.ibm.com/granite)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)

研究备注：
- Scale HLE 公开榜单未见 Granite 4.2 8B；IBM 官方列出的该型号评测也没有 HLE 成绩。

最近核验时间：2026-11-04T16:29+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 5
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/granite-4-2-8b/](https://artificialanalysis.ai/models/granite-4-2-8b/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Granite 4.2 8B 官方模型页](https://artificialanalysis.ai/models/granite-4-2-8b/)
- [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA 官方模型页将精确模型 Granite 4.2 8B 的 Intelligence Index 记为 5，页面 Index 章节标注 v5.0.1；已按原始版本写入模型 TOML，未填评测日期或未公布条件。

尚未解决的问题：
- 本地定义 version="5.0"，来源明确为 5.0.1；原始结果已保留，精确定义映射待复核，当前覆盖统计不计入。

最近核验时间：2026-11-04T16:29+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方页面](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [IBM 官方模型卡](https://huggingface.co/ibm-granite/granite-4.2-8b)

研究备注：
- 未在官方页面找到该模型的 GDPval-AA v2.1 成绩。IBM 发布的通用 GDPval 分数 1189 不是已确认的 GDPval-AA v2.1，不转记。

最近核验时间：2026-11-04T16:29+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Vals Granite 4.2 8B 官方模型页](https://www.vals.ai/models/ibm_granite-4.2-8b)

研究备注：
- Vals v2.2 榜单直接核对未见 Granite 4.2 8B；精确模型结果页路由不可用，未获得可核实分数。

最近核验时间：2026-11-04T16:29+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Granite 4.2 8B 官方模型页",
          "url": "https://artificialanalysis.ai/models/granite-4-2-8b/"
        },
        {
          "label": "Artificial Analysis Intelligence Index 方法",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA 官方模型页将精确模型 Granite 4.2 8B 的 Intelligence Index 记为 5，页面 Index 章节标注 v5.0.1；已按原始版本写入模型 TOML，未填评测日期或未公布条件。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义 version=\"5.0\"，来源明确为 5.0.1；原始结果已保留，精确定义映射待复核，当前覆盖统计不计入。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单与方法",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        },
        {
          "label": "IBM 官方发布文章",
          "url": "https://research.ibm.com/blog/introducing-granite-4-2"
        }
      ],
      "notes": [
        "公开榜单与 IBM 发布资料未找到该模型的 AutomationBench v1.0.6 成绩。模型支持工具调用，故此项适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 论文与方法",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        }
      ],
      "notes": [
        "Chartography 输入图表图像并测量图表视觉理解；模型卡和仓库源文件都将 Granite 4.2 8B 列为仅文本输入，因此不适用。榜单也无该型号结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        }
      ],
      "notes": [
        "官方榜单未见 Granite 4.2 8B 或对应别名；未将其他 Granite 型号的结果转给该模型。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方页面",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        }
      ],
      "notes": [
        "未在官方页面找到该模型的 GDPval-AA v2.1 成绩。IBM 发布的通用 GDPval 分数 1189 不是已确认的 GDPval-AA v2.1，不转记。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Scale HLE 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "IBM Granite 官方模型与评测表",
          "url": "https://www.ibm.com/granite"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        }
      ],
      "notes": [
        "Scale HLE 公开榜单未见 Granite 4.2 8B；IBM 官方列出的该型号评测也没有 HLE 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 官方发布记录",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "OSWorld V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        }
      ],
      "notes": [
        "官方 v2.1 发布记录没有 Granite 4.2 8B 或其仓库 ID；未找到可归属到目标版本的公开成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        },
        {
          "label": "IBM Granite 4.2 技术文章",
          "url": "https://huggingface.co/blog/ibm-granite/granite-4-2"
        },
        {
          "label": "Scale SWE-bench Pro V2 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "IBM 发布的 SWE Bench Pro 19.11 未标注任务集版本；模型卡自动评测记录在 V2 于 2026-09-22 发布之前。Scale V2 榜单未找到 Granite 4.2 8B。因此未把 19.11 归入 V2，且未在本目标版本下新增该条。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 方法",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        }
      ],
      "notes": [
        "未在 Vals 或 Artificial Analysis 公开结果中找到 Granite 4.2 8B。IBM 模型卡里的 SciCode 是不同 Benchmark，未映射到 Terminal-Bench-Science。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "IBM 官方模型卡",
          "url": "https://huggingface.co/ibm-granite/granite-4.2-8b"
        },
        {
          "label": "Vals Terminal-Bench 4.0 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 方法",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "IBM 模型卡的 Terminal-Bench 20.56 属于版本 2.1，不是目标 v4；Vals 榜单和 AA 方法页未提供 Granite 4.2 8B 的 v4 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T16:29+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Granite 4.2 8B 官方模型页",
          "url": "https://www.vals.ai/models/ibm_granite-4.2-8b"
        }
      ],
      "notes": [
        "Vals v2.2 榜单直接核对未见 Granite 4.2 8B；精确模型结果页路由不可用，未获得可核实分数。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T16:29+08:00",
  "model_id": "ibm/granite-4.2-8b",
  "new_records": 1,
  "overall_status": "待复核"
}

-->
