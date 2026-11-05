# LongCat-2.0 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meituan/longcat-2.0
- 模型名称：LongCat-2.0
- 发布日期：2026-06-30
- 最近检查时间：2026-11-05T02:16+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：7
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0) | 2026-11-05T02:16+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0) | 2026-11-05T02:16+08:00 |
| terminal-bench-v4 | 已收录 | 70.8 (metric=success rate; version=2.1); 0 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=pass@1; averaged over 3 repeats per task; maximum 500 agent steps; Artificial Analysis run; harness=mini-swe-agent) | [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:16+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1), [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0) | 2026-11-05T02:16+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://longcat.chat/blog/longcat-2-5-preview](https://longcat.chat/blog/longcat-2-5-preview), [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0) | 2026-11-05T02:16+08:00 |
| osworld-v2.1 | 不适用 | — | [https://artificialanalysis.ai/models/longcat-2-0](https://artificialanalysis.ai/models/longcat-2-0), [https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T02:16+08:00 |
| chartography | 不适用 | — | [https://artificialanalysis.ai/models/longcat-2-0](https://artificialanalysis.ai/models/longcat-2-0), [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T02:16+08:00 |
| humanitys-last-exam | 已收录 | 34 (metric=accuracy; dataset=2,158 text-only questions; variant=pass@1; judged by GPT-5.6 Luna (medium)) | [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:16+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/longcat-2-0](https://artificialanalysis.ai/models/longcat-2-0), [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T02:16+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0), [https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-longcat-2-0), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:16+08:00 |
| vals-index-v2.2 | 未找到 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T02:16+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0)

研究备注：
- 已检查 Datacurve 当前 v1.1 榜单及 LongCat 官方评测表；未找到精确型号的 DeepSWE v1.1 成绩。

最近核验时间：2026-11-05T02:16+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0)

研究备注：
- 官方模型卡的 SWE-bench Pro 59.5 未注明版本；Scale 当前 V2 榜单未列 LongCat-2.0，不能把旧未标版本成绩当作 V2。

最近核验时间：2026-11-05T02:16+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 70.8
- metric: success rate
- version: 2.1
- source: [https://github.com/meituan-longcat/longcat-2.0](https://github.com/meituan-longcat/longcat-2.0)
- date: 2026-06-30
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 0
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: pass@1; averaged over 3 repeats per task; maximum 500 agent steps; Artificial Analysis run
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 比较页列 LongCat 2.0 Terminal-Bench 4.0 为 0%；其方法页说明使用 66 tasks、mini-swe-agent、pass@1 每题 3 次重复、最多 500 steps。该 0% 是明确发布分数，不是缺失值。模型卡另列的 70.8 属 Terminal-Bench 2.1，保留且不映射到 v4。

最近核验时间：2026-11-05T02:16+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0)

研究备注：
- 官方 0.1 结果页与 LongCat 模型卡均未给出该型号的 Terminal-Bench Science 0.1 成绩。

最近核验时间：2026-11-05T02:16+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://longcat.chat/blog/longcat-2-5-preview](https://longcat.chat/blog/longcat-2-5-preview)
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://github.com/meituan-longcat/LongCat-2.0](https://github.com/meituan-longcat/LongCat-2.0)

研究备注：
- LongCat 官方 2.5 博文似乎引用 AutomationBench v1.0.6 对比，但直接页无可读结果；Zapier 当前榜单只展示前 10 条，其余 119 条折叠。未确认 LongCat-2.0 是否有准确 v1.0.6 成绩。

尚未解决的问题：
- 公开榜单未能完整检查，且博客结果无法直接读取；不记录猜测分数。

最近核验时间：2026-11-05T02:16+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://artificialanalysis.ai/models/longcat-2-0](https://artificialanalysis.ai/models/longcat-2-0)
- [https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- LongCat 2.0 为文本输入/文本输出模型；OSWorld v2.1 的公开协议使用桌面截图观察与 GUI 动作，未找到无需视觉输入的原生评测配置。

最近核验时间：2026-11-05T02:16+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://artificialanalysis.ai/models/longcat-2-0](https://artificialanalysis.ai/models/longcat-2-0)
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- LongCat 2.0 为文本输入模型，不支持直接读取 Chartography 图表图像；官方榜单亦未检出该型号。

最近核验时间：2026-11-05T02:16+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 34
- metric: accuracy
- dataset: 2,158 text-only questions
- variant: pass@1; judged by GPT-5.6 Luna (medium)
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 比较页列 LongCat 2.0 原始 HLE 为 34%；方法采用 2,158 道 text-only 题、pass@1，并由 GPT-5.6 Luna (medium) 等值判分。该项不是 HLE-Diamond，来源未注明 effort。

最近核验时间：2026-11-05T02:16+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/longcat-2-0](https://artificialanalysis.ai/models/longcat-2-0)
- [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 当前 LongCat 模型页的 V5.0.1 指数为 N/A；比较页中的 19 分明确属于历史 Index V4.3.2，不能映射到 V5.

最近核验时间：2026-11-05T02:16+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0)
- [https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-longcat-2-0](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-longcat-2-0)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 两张 Artificial Analysis 比较页均列 GDPval-AA v2.1，但同为 LongCat 2.0 的 Elo 分别为 870 和 856。AA 方法页说明 v2.1 分数校准发生过版本调整，但页面没有足够批次/时间信息解释这两个值；不擅自选择或同时写入。

尚未解决的问题：
- 官方比较页面对相同模型与 GDPval-AA v2.1 给出 870/856 的未解释差异。

最近核验时间：2026-11-05T02:16+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 已检查当前 Vals Index v2.2 榜单，未找到 LongCat 2.0 的精确成绩。

最近核验时间：2026-11-05T02:16+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/longcat-2-0"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "当前 LongCat 模型页的 V5.0.1 指数为 N/A；比较页中的 19 分明确属于历史 Index V4.3.2，不能映射到 V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://longcat.chat/blog/longcat-2-5-preview"
        },
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://github.com/meituan-longcat/LongCat-2.0"
        }
      ],
      "notes": [
        "LongCat 官方 2.5 博文似乎引用 AutomationBench v1.0.6 对比，但直接页无可读结果；Zapier 当前榜单只展示前 10 条，其余 119 条折叠。未确认 LongCat-2.0 是否有准确 v1.0.6 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开榜单未能完整检查，且博客结果无法直接读取；不记录猜测分数。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/longcat-2-0"
        },
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "LongCat 2.0 为文本输入模型，不支持直接读取 Chartography 图表图像；官方榜单亦未检出该型号。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://github.com/meituan-longcat/LongCat-2.0"
        }
      ],
      "notes": [
        "已检查 Datacurve 当前 v1.1 榜单及 LongCat 官方评测表；未找到精确型号的 DeepSWE v1.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0"
        },
        {
          "url": "https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-longcat-2-0"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "两张 Artificial Analysis 比较页均列 GDPval-AA v2.1，但同为 LongCat 2.0 的 Elo 分别为 870 和 856。AA 方法页说明 v2.1 分数校准发生过版本调整，但页面没有足够批次/时间信息解释这两个值；不擅自选择或同时写入。"
      ],
      "status": "冲突",
      "unresolved": [
        "官方比较页面对相同模型与 GDPval-AA v2.1 给出 870/856 的未解释差异。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 比较页列 LongCat 2.0 原始 HLE 为 34%；方法采用 2,158 道 text-only 题、pass@1，并由 GPT-5.6 Luna (medium) 等值判分。该项不是 HLE-Diamond，来源未注明 effort。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/longcat-2-0"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "LongCat 2.0 为文本输入/文本输出模型；OSWorld v2.1 的公开协议使用桌面截图观察与 GUI 动作，未找到无需视觉输入的原生评测配置。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://github.com/meituan-longcat/LongCat-2.0"
        }
      ],
      "notes": [
        "官方模型卡的 SWE-bench Pro 59.5 未注明版本；Scale 当前 V2 榜单未列 LongCat-2.0，不能把旧未标版本成绩当作 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "url": "https://github.com/meituan-longcat/LongCat-2.0"
        }
      ],
      "notes": [
        "官方 0.1 结果页与 LongCat 模型卡均未给出该型号的 Terminal-Bench Science 0.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-low-vs-longcat-2-0"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 比较页列 LongCat 2.0 Terminal-Bench 4.0 为 0%；其方法页说明使用 66 tasks、mini-swe-agent、pass@1 每题 3 次重复、最多 500 steps。该 0% 是明确发布分数，不是缺失值。模型卡另列的 70.8 属 Terminal-Bench 2.1，保留且不映射到 v4。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:16+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "已检查当前 Vals Index v2.2 榜单，未找到 LongCat 2.0 的精确成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 7,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:16+08:00",
  "model_id": "meituan/longcat-2.0",
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
