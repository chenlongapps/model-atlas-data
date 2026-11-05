# Ling 3.0 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inclusionai/ling-3.0-flash
- 模型名称：Ling 3.0 Flash
- 发布日期：2026-07-23
- 最近检查时间：2026-11-04T22:07+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE official leaderboard](https://deepswe.datacurve.ai/), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| swe-bench-pro-v2 | 待核实 | 56.6 (dataset=ScaleAI/SWE-bench_Pro; harness=OpenHands) | [Ling 3.0 Flash official SWE-bench Pro evaluation metadata](https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/swe-bench_pro.yaml), [Ling 3.0 Flash official model card and harness notes](https://huggingface.co/inclusionAI/Ling-3.0-flash), [Scale AI SWE-bench Pro V2 leaderboard and release information](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T22:07+08:00 |
| terminal-bench-v4 | 未找到 | — | [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2.1 official release and repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2.1 release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography benchmark and leaderboard](https://surgehq.ai/benchmarks/chartography), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| humanitys-last-exam | 待核实 | 22.7 (dataset=cais/hle) | [Ling 3.0 Flash official HLE evaluation metadata](https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/hle.yaml), [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash), [HLE dataset](https://huggingface.co/datasets/cais/hle) | 2026-11-04T22:07+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Ling 3.0 Flash profile](https://artificialanalysis.ai/models/ling-3-0-flash), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T22:07+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Ling 3.0 Flash official model card and GDPval evaluation conditions](https://huggingface.co/inclusionAI/Ling-3.0-flash) | 2026-11-04T22:07+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index V2 historical leaderboard](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-04T22:07+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- DeepSWE 官方排行榜未列出 Ling 3.0 Flash；模型卡列出的终端代理评测是 Terminal-Bench 2.1，不映射到 DeepSWE。

最近核验时间：2026-11-04T22:07+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 56.6
- dataset: ScaleAI/SWE-bench_Pro
- harness: OpenHands
- source: [https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/swe-bench_pro.yaml](https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/swe-bench_pro.yaml)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Ling 3.0 Flash official SWE-bench Pro evaluation metadata](https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/swe-bench_pro.yaml)
- [Ling 3.0 Flash official model card and harness notes](https://huggingface.co/inclusionAI/Ling-3.0-flash)
- [Scale AI SWE-bench Pro V2 leaderboard and release information](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- InclusionAI 的官方评测元数据给出 SWE-bench Pro 56.6，数据集标识 ScaleAI/SWE-bench_Pro，模型卡说明 SWE-Bench 系列使用 OpenHands。因来源未给出 metric 或 benchmark version，仅以原名、分数、数据集、harness 和 source 入 TOML。
- 该评测文件于 2026-08-06 提交，早于 Scale AI 发布 SWE-bench Pro V2；不能将此成绩认定为 V2。

尚未解决的问题：
- 缺少官方 metric 与 benchmark version；此原始记录不与本地 2.0.0 / task resolution rate 定义精确映射，也不能据此确认 V2 成绩。

最近核验时间：2026-11-04T22:07+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- 官方 V4 榜单未列 Ling 3.0 Flash。模型卡中可见 Terminal-Bench 2.1 的独立成绩和 Terminus 2 条件，不用于 V4。

最近核验时间：2026-11-04T22:07+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- 所查官方 Science 0.1 榜单及模型卡没有该模型的对应成绩。

最近核验时间：2026-11-04T22:07+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- Zapier 官方 1.0.6 榜单未列出 Ling 3.0 Flash；没有找到可核实的对应公开成绩。

最近核验时间：2026-11-04T22:07+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2.1 official release and repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2.1 release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- OSWorld V2.1 官方资料确认 108 项任务及该版本，但所查资料没有 Ling 3.0 Flash 成绩。模型是文本输入；OSWorld 同时提供 accessibility-tree observation，因此不据此判定不适用。

最近核验时间：2026-11-04T22:07+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography benchmark and leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- Chartography 评估专业图表视觉理解；Ling 3.0 Flash 的模型卡与仓库 TOML 都标明仅接受文本输入，没有图像输入能力。

最近核验时间：2026-11-04T22:07+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 22.7
- dataset: cais/hle
- source: [https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/hle.yaml](https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/hle.yaml)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Ling 3.0 Flash official HLE evaluation metadata](https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/hle.yaml)
- [Ling 3.0 Flash official model card](https://huggingface.co/inclusionAI/Ling-3.0-flash)
- [HLE dataset](https://huggingface.co/datasets/cais/hle)

研究备注：
- 官方模型卡列出 HLE 22.7，评测元数据指向 cais/hle。未将 metric、版本、工具条件或日期写入成绩，因为来源未提供。
- Hugging Face 当前将该结果文件标为 YAML task ID 与数据集不匹配；分数保留原始记录，但不参与 HLE 定义的精确映射。

尚未解决的问题：
- 需要确认 22.7 的原始评测配置和指标；Hugging Face 评测元数据当前存在 task ID mismatch。

最近核验时间：2026-11-04T22:07+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Ling 3.0 Flash profile](https://artificialanalysis.ai/models/ling-3-0-flash)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 的 Ling 3.0 Flash 模型页对 Intelligence Index 显示 N/A；没有 V5 指数分数可写入。

最近核验时间：2026-11-04T22:07+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Ling 3.0 Flash official model card and GDPval evaluation conditions](https://huggingface.co/inclusionAI/Ling-3.0-flash)

研究备注：
- 官方模型卡确认曾对 GDPval v2-AA 的 220 项公开任务使用 Stirrup，并给出 250-turn / 5-hour 条件，但可读正文未提供 Ling 的分数。官方 V2.1 榜单页面可读结果中未核验到 Ling 的具体行。

尚未解决的问题：
- 未取得可核实的精确 GDPval-AA v2.1 成绩；不采用社区转述的 1107，也不从不可读图表或搜索摘要推断。

最近核验时间：2026-11-04T22:07+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index V2 historical leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- Vals 官方 V2.2 榜单未列出 Ling 3.0 Flash。其 V2 历史页的结果属于另一版本，未写入。

最近核验时间：2026-11-04T22:07+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Ling 3.0 Flash profile",
          "url": "https://artificialanalysis.ai/models/ling-3-0-flash"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 的 Ling 3.0 Flash 模型页对 Intelligence Index 显示 N/A；没有 V5 指数分数可写入。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "Zapier 官方 1.0.6 榜单未列出 Ling 3.0 Flash；没有找到可核实的对应公开成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography benchmark and leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "Chartography 评估专业图表视觉理解；Ling 3.0 Flash 的模型卡与仓库 TOML 都标明仅接受文本输入，没有图像输入能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "DeepSWE 官方排行榜未列出 Ling 3.0 Flash；模型卡列出的终端代理评测是 Terminal-Bench 2.1，不映射到 DeepSWE。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Ling 3.0 Flash official model card and GDPval evaluation conditions",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "官方模型卡确认曾对 GDPval v2-AA 的 220 项公开任务使用 Stirrup，并给出 250-turn / 5-hour 条件，但可读正文未提供 Ling 的分数。官方 V2.1 榜单页面可读结果中未核验到 Ling 的具体行。"
      ],
      "status": "待核实",
      "unresolved": [
        "未取得可核实的精确 GDPval-AA v2.1 成绩；不采用社区转述的 1107，也不从不可读图表或搜索摘要推断。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Ling 3.0 Flash official HLE evaluation metadata",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/hle.yaml"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        },
        {
          "label": "HLE dataset",
          "url": "https://huggingface.co/datasets/cais/hle"
        }
      ],
      "notes": [
        "官方模型卡列出 HLE 22.7，评测元数据指向 cais/hle。未将 metric、版本、工具条件或日期写入成绩，因为来源未提供。",
        "Hugging Face 当前将该结果文件标为 YAML task ID 与数据集不匹配；分数保留原始记录，但不参与 HLE 定义的精确映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要确认 22.7 的原始评测配置和指标；Hugging Face 评测元数据当前存在 task ID mismatch。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 official release and repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2.1 release manifest",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "OSWorld V2.1 官方资料确认 108 项任务及该版本，但所查资料没有 Ling 3.0 Flash 成绩。模型是文本输入；OSWorld 同时提供 accessibility-tree observation，因此不据此判定不适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Ling 3.0 Flash official SWE-bench Pro evaluation metadata",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash/blob/main/.eval_results/swe-bench_pro.yaml"
        },
        {
          "label": "Ling 3.0 Flash official model card and harness notes",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard and release information",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "InclusionAI 的官方评测元数据给出 SWE-bench Pro 56.6，数据集标识 ScaleAI/SWE-bench_Pro，模型卡说明 SWE-Bench 系列使用 OpenHands。因来源未给出 metric 或 benchmark version，仅以原名、分数、数据集、harness 和 source 入 TOML。",
        "该评测文件于 2026-08-06 提交，早于 Scale AI 发布 SWE-bench Pro V2；不能将此成绩认定为 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "缺少官方 metric 与 benchmark version；此原始记录不与本地 2.0.0 / task resolution rate 定义精确映射，也不能据此确认 V2 成绩。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "所查官方 Science 0.1 榜单及模型卡没有该模型的对应成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Ling 3.0 Flash official model card",
          "url": "https://huggingface.co/inclusionAI/Ling-3.0-flash"
        }
      ],
      "notes": [
        "官方 V4 榜单未列 Ling 3.0 Flash。模型卡中可见 Terminal-Bench 2.1 的独立成绩和 Terminus 2 条件，不用于 V4。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T22:07+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index V2 historical leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "Vals 官方 V2.2 榜单未列出 Ling 3.0 Flash。其 V2 历史页的结果属于另一版本，未写入。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T22:07+08:00",
  "model_id": "inclusionai/ling-3.0-flash",
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
