# Gemma 4 12B IT Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemma-4-12b-it
- 模型名称：Gemma 4 12B IT
- 发布日期：2026-06-03
- 最近检查时间：2026-11-05T04:08+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google 官方发布博客标明 Gemma 4 12B 于 2026-06-03 发布；仓库原 release_date 为 2026-06-09。已按官方发布日更正队列日期。
- 官方模型卡称本组结果为 instruction-tuned 模型；HLE no-tools 5.2% 原始分数有来源，但 metric 未被明确写出，待到队列处理时复核映射。
- 已新增官方模型卡中的 HLE no-tools 原始 5.2% 记录；原表 with-search 一栏为缺值，不作 0 处理。metric 未明确披露，因此该行暂不映射本地 accuracy 定义。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it), [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [Google Gemma 4 12B launch post](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) | 2026-11-05T04:08+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench), [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| chartography | 未找到 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography evaluation repository](https://github.com/surge-ai/chartography), [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| humanitys-last-exam | 待核实 | 5.2 (variant=no tools) | [Google Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4), [Google Hugging Face weights](https://huggingface.co/google/gemma-4-12B-it) | 2026-11-05T04:08+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Gemma 4 12B profile](https://artificialanalysis.ai/models/releases/gemma-4-12b) | 2026-11-05T04:08+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T04:08+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T04:08+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [Google Gemma 4 12B launch post](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)

研究备注：
- DeepSWE 页面当前显示 21/28 配置且未见 Gemma 4 12B；可见列表不完整，不能确认完整榜单无结果。

尚未解决的问题：
- DeepSWE 动态榜单未展示全部配置。

最近核验时间：2026-11-05T04:08+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- 模型卡未列 SWE-bench Pro V2；Scale V2 榜单未找到 Gemma 4 12B 精确型号。

最近核验时间：2026-11-05T04:08+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- 未找到 Gemma 4 12B 的 v4 成绩；官方动态榜单抓取为空表，无法确认完整条目。

尚未解决的问题：
- 官方 Terminal-Bench 4 动态榜单当前无法读取完整结果。

最近核验时间：2026-11-05T04:08+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- Science 0.1 官方结果页未列 Gemma 4 12B。

最近核验时间：2026-11-05T04:08+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- 官方模型卡确认原生函数调用；Zapier 1.0.6 页面仅展示前 10 项并折叠另 119 项，未见该型号但无法排除完整榜单中有结果。

尚未解决的问题：
- Zapier 排行榜隐藏 119 个条目。

最近核验时间：2026-11-05T04:08+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- 官方模型卡确认图像输入、屏幕/UI理解与函数调用；OSWorld 官方榜单未找到该型号的 v2.1 成绩。

最近核验时间：2026-11-05T04:08+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography evaluation repository](https://github.com/surge-ai/chartography)
- [Google Gemma 4 model card](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- 模型支持图表理解和图像输入；Surge 榜单未找到 Gemma 4 12B 成绩。

最近核验时间：2026-11-05T04:08+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 5.2
- variant: no tools
- source: [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Google Hugging Face weights](https://huggingface.co/google/gemma-4-12B-it)

研究备注：
- 官方表列出 Gemma 4 12B Unified 的 HLE no tools 5.2%；with search 为缺值。HF 卡将 gemma-4-12B-it 标为 gemma4_unified。表格只给百分比，未明确 metric；暂保留原始 score 和 no-tools 条件，待确认能否映射本地 accuracy 定义。

尚未解决的问题：
- 官方表未显式说明 HLE 分数的 metric；本地定义要求 accuracy，暂不做精确映射。

最近核验时间：2026-11-05T04:08+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Gemma 4 12B profile](https://artificialanalysis.ai/models/releases/gemma-4-12b)

研究备注：
- AA Gemma 4 12B 页面当前 V5 Index 为 N/A / 无公开 API，没有可收录的综合 Index 分数。

最近核验时间：2026-11-05T04:08+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA v2.1 榜单未找到 Gemma 4 12B 的 Elo 成绩。

最近核验时间：2026-11-05T04:08+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前公开 v2.2 页未列出该精确型号；该页面展示最新/前沿模型子集，未出现不证明从未评测。

最近核验时间：2026-11-05T04:08+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemma 4 12B profile",
          "url": "https://artificialanalysis.ai/models/releases/gemma-4-12b"
        }
      ],
      "notes": [
        "AA Gemma 4 12B 页面当前 V5 Index 为 N/A / 无公开 API，没有可收录的综合 Index 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "官方模型卡确认原生函数调用；Zapier 1.0.6 页面仅展示前 10 项并折叠另 119 项，未见该型号但无法排除完整榜单中有结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 排行榜隐藏 119 个条目。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T04:08+08:00",
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
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "模型支持图表理解和图像输入；Surge 榜单未找到 Gemma 4 12B 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Google Gemma 4 12B launch post",
          "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/"
        }
      ],
      "notes": [
        "DeepSWE 页面当前显示 21/28 配置且未见 Gemma 4 12B；可见列表不完整，不能确认完整榜单无结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "DeepSWE 动态榜单未展示全部配置。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA v2.1 榜单未找到 Gemma 4 12B 的 Elo 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Google Gemma 4 model card",
          "url": "https://ai.google.dev/gemma/docs/core/model_card_4"
        },
        {
          "label": "Google Hugging Face weights",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "官方表列出 Gemma 4 12B Unified 的 HLE no tools 5.2%；with search 为缺值。HF 卡将 gemma-4-12B-it 标为 gemma4_unified。表格只给百分比，未明确 metric；暂保留原始 score 和 no-tools 条件，待确认能否映射本地 accuracy 定义。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方表未显式说明 HLE 分数的 metric；本地定义要求 accuracy，暂不做精确映射。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "OSWorld official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "官方模型卡确认图像输入、屏幕/UI理解与函数调用；OSWorld 官方榜单未找到该型号的 v2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "模型卡未列 SWE-bench Pro V2；Scale V2 榜单未找到 Gemma 4 12B 精确型号。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "Science 0.1 官方结果页未列 Gemma 4 12B。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Google Gemma 4 model card",
          "url": "https://huggingface.co/google/gemma-4-12B-it"
        }
      ],
      "notes": [
        "未找到 Gemma 4 12B 的 v4 成绩；官方动态榜单抓取为空表，无法确认完整条目。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 Terminal-Bench 4 动态榜单当前无法读取完整结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:08+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前公开 v2.2 页未列出该精确型号；该页面展示最新/前沿模型子集，未出现不证明从未评测。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:08+08:00",
  "model_id": "google/gemma-4-12b-it",
  "model_notes": [
    "Google 官方发布博客标明 Gemma 4 12B 于 2026-06-03 发布；仓库原 release_date 为 2026-06-09。已按官方发布日更正队列日期。",
    "官方模型卡称本组结果为 instruction-tuned 模型；HLE no-tools 5.2% 原始分数有来源，但 metric 未被明确写出，待到队列处理时复核映射。",
    "已新增官方模型卡中的 HLE no-tools 原始 5.2% 记录；原表 with-search 一栏为缺值，不作 0 处理。metric 未明确披露，因此该行暂不映射本地 accuracy 定义。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
