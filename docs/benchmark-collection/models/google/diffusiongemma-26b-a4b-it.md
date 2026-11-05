# DiffusionGemma 26B A4B IT Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/diffusiongemma-26b-a4b-it
- 模型名称：DiffusionGemma 26B A4B IT
- 发布日期：2026-06-10
- 最近检查时间：2026-11-05T03:44+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- Google 官方发布博客及 Artificial Analysis 页面将 DiffusionGemma 发布日标为 2026-06-10；原 TOML 原日期为 2026-06-09，已按官方发布日修正 release_date，不以此作为成绩日期。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| chartography | 未找到 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography evaluation repository](https://github.com/surge-ai/chartography), [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| humanitys-last-exam | 已收录 | 11.0 (metric=accuracy; variant=no tools); 11.9 (metric=accuracy; variant=with search) | [Google DiffusionGemma official model card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card), [Google Hugging Face model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 2026-11-05T03:44+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis DiffusionGemma profile](https://artificialanalysis.ai/models/diffusiongemma-26b-a4b) | 2026-11-05T03:44+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T03:44+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T03:44+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- 官方模型卡和 DeepSWE 榜单未找到该准确模型版本的成绩。

最近核验时间：2026-11-05T03:44+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- 模型卡及 Scale V2 榜单未找到该准确模型的公开成绩。

最近核验时间：2026-11-05T03:44+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- 未能稳定读取官方 v4 动态榜单，无法确认该模型是否有结果；没有写入未核实分数。

尚未解决的问题：
- 官方动态榜单需复核，当前无法确认完整结果列表。

最近核验时间：2026-11-05T03:44+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- 官方 Science 0.1 结果页及模型卡未列出该型号成绩。

最近核验时间：2026-11-05T03:44+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- 模型卡确认支持 function calling；Zapier 1.0.6 榜单其余 119 个条目折叠，无法确认是否有该型号成绩。

尚未解决的问题：
- Zapier 榜单的折叠条目无法从当前可读页面核验。

最近核验时间：2026-11-05T03:44+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- 官方模型卡确认支持图像输入，评测适用；未找到 OSWorld v2.1 的精确模型结果。

尚未解决的问题：
- 尚未找到可直接确认的官方 v2.1 模型成绩行。

最近核验时间：2026-11-05T03:44+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography evaluation repository](https://github.com/surge-ai/chartography)
- [Google DiffusionGemma model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- Surge 官方榜单及评测仓库未找到 DiffusionGemma 的结果；能力描述不作为 benchmark 成绩。

最近核验时间：2026-11-05T03:44+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 11.0
- metric: accuracy
- variant: no tools
- source: [https://ai.google.dev/gemma/docs/diffusiongemma/model_card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 11.9
- metric: accuracy
- variant: with search
- source: [https://ai.google.dev/gemma/docs/diffusiongemma/model_card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Google DiffusionGemma official model card](https://ai.google.dev/gemma/docs/diffusiongemma/model_card)
- [Google Hugging Face model card](https://huggingface.co/google/diffusiongemma-26B-A4B-it)

研究备注：
- Google 官方模型卡针对 instruction-tuned 模型并使用推荐的 Entropy Bound sampler，报告 HLE no tools 11.0% 和 with search 11.9%；数据集子集、harness 与评测日期未注明。两条条件分别保留在模型 TOML。

最近核验时间：2026-11-05T03:44+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis DiffusionGemma profile](https://artificialanalysis.ai/models/diffusiongemma-26b-a4b)

研究备注：
- Artificial Analysis 模型页显示当前 V5 Index 不可用/无公开 API；原始 HLE 分数不等同于 AA Intelligence Index。

最近核验时间：2026-11-05T03:44+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 官方 v2.1 榜单未找到 DiffusionGemma 的精确型号 Elo 结果。

最近核验时间：2026-11-05T03:44+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前公开 Vals Index v2.2 榜单未找到 DiffusionGemma 的精确型号条目。

最近核验时间：2026-11-05T03:44+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis DiffusionGemma profile",
          "url": "https://artificialanalysis.ai/models/diffusiongemma-26b-a4b"
        }
      ],
      "notes": [
        "Artificial Analysis 模型页显示当前 V5 Index 不可用/无公开 API；原始 HLE 分数不等同于 AA Intelligence Index。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "模型卡确认支持 function calling；Zapier 1.0.6 榜单其余 119 个条目折叠，无法确认是否有该型号成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 榜单的折叠条目无法从当前可读页面核验。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "Surge 官方榜单及评测仓库未找到 DiffusionGemma 的结果；能力描述不作为 benchmark 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "官方模型卡和 DeepSWE 榜单未找到该准确模型版本的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "官方 v2.1 榜单未找到 DiffusionGemma 的精确型号 Elo 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Google DiffusionGemma official model card",
          "url": "https://ai.google.dev/gemma/docs/diffusiongemma/model_card"
        },
        {
          "label": "Google Hugging Face model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "Google 官方模型卡针对 instruction-tuned 模型并使用推荐的 Entropy Bound sampler，报告 HLE no tools 11.0% 和 with search 11.9%；数据集子集、harness 与评测日期未注明。两条条件分别保留在模型 TOML。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "官方模型卡确认支持图像输入，评测适用；未找到 OSWorld v2.1 的精确模型结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "尚未找到可直接确认的官方 v2.1 模型成绩行。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "模型卡及 Scale V2 榜单未找到该准确模型的公开成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "官方 Science 0.1 结果页及模型卡未列出该型号成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Google DiffusionGemma model card",
          "url": "https://huggingface.co/google/diffusiongemma-26B-A4B-it"
        }
      ],
      "notes": [
        "未能稳定读取官方 v4 动态榜单，无法确认该模型是否有结果；没有写入未核实分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态榜单需复核，当前无法确认完整结果列表。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:44+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前公开 Vals Index v2.2 榜单未找到 DiffusionGemma 的精确型号条目。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:44+08:00",
  "model_id": "google/diffusiongemma-26b-a4b-it",
  "model_notes": [
    "Google 官方发布博客及 Artificial Analysis 页面将 DiffusionGemma 发布日标为 2026-06-10；原 TOML 原日期为 2026-06-09，已按官方发布日修正 release_date，不以此作为成绩日期。"
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
