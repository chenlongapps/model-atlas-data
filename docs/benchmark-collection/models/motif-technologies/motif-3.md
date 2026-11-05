# Motif 3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：motif-technologies/motif-3
- 模型名称：Motif 3
- 发布日期：2026-08-07
- 最近检查时间：2026-11-04T19:22+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- Motif 3 官方模型卡确认模型为 BF16、文本输入/输出；技术报告的统一评测采样设置为 temperature=1.0、top_p=0.95、最大序列长度 262,144。
- 报告中的 GDPval-AA v2 和 Terminal-Bench 2.1 分数不是本轮目标版本，未跨版本映射。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3), [Motif 3 technical report](https://arxiv.org/html/2608.09119v1) | 2026-11-04T19:22+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3), [Motif 3 technical report](https://arxiv.org/html/2608.09119v1) | 2026-11-04T19:22+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [Artificial Analysis Motif 3 model profile](https://artificialanalysis.ai/models/motif-3), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3), [Motif 3 technical report](https://arxiv.org/html/2608.09119v1) | 2026-11-04T19:22+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals AI Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3), [Motif 3 technical report](https://arxiv.org/html/2608.09119v1) | 2026-11-04T19:22+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3) | 2026-11-04T19:22+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 project](https://osworld-v2.xlang.ai/), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3) | 2026-11-04T19:22+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography benchmark](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3) | 2026-11-04T19:22+08:00 |
| humanitys-last-exam | 已收录 | 37.0 (metric=accuracy; variant=temperature=1.0; top_p=0.95; max sequence length=262144) | [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3), [Motif 3 technical report](https://arxiv.org/html/2608.09119v1), [Artificial Analysis original HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T19:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Motif 3 model profile](https://artificialanalysis.ai/models/motif-3), [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T19:22+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3), [Motif 3 technical report](https://arxiv.org/html/2608.09119v1) | 2026-11-04T19:22+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3) | 2026-11-04T19:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)
- [Motif 3 technical report](https://arxiv.org/html/2608.09119v1)

研究备注：
- 已检查官方 v1.1 榜单、Motif 3 模型卡和技术报告；未见该模型成绩。

最近核验时间：2026-11-04T19:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)
- [Motif 3 technical report](https://arxiv.org/html/2608.09119v1)

研究备注：
- Scale 官方 V2 榜单未见 Motif 3。模型卡和报告中的 SWE-bench Verified 76.2 是另一评测，未映射至 Pro V2。

最近核验时间：2026-11-04T19:22+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [Artificial Analysis Motif 3 model profile](https://artificialanalysis.ai/models/motif-3)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)
- [Motif 3 technical report](https://arxiv.org/html/2608.09119v1)

研究备注：
- Motif 模型卡和技术报告只列 Terminal-Bench 2.1（74.9），不映射至 v4。Terminal-Bench v4 官方榜单当前读取时没有可确认的数据行；Artificial Analysis 当前模型页没有提供可用于映射的 v4 分数。

尚未解决的问题：
- 官方 v4 榜单当前没有可读的成绩行，无法判定公开榜单是否列出 Motif 3。

最近核验时间：2026-11-04T19:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)
- [Motif 3 technical report](https://arxiv.org/html/2608.09119v1)

研究备注：
- Vals AI 官方榜单未列 Motif 3；模型卡与技术报告也未报告此项成绩。

最近核验时间：2026-11-04T19:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)

研究备注：
- Zapier 官方榜单标注 v1.0.6，仅显示前 10 项并折叠 119 项；未在可见条目中发现 Motif 3。

尚未解决的问题：
- 无法检查榜单隐藏的 119 项，不能确定是否包含 Motif 3。

最近核验时间：2026-11-04T19:22+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)

研究备注：
- 官方模型卡标注此模型仅支持 text input；OSWorld v2.1 是需根据桌面截图进行 GUI 操作的评测。

最近核验时间：2026-11-04T19:22+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography benchmark](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)

研究备注：
- 官方模型卡标注此模型仅支持 text input；Chartography 要求读取图表图像。

最近核验时间：2026-11-04T19:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 37.0
- metric: accuracy
- variant: temperature=1.0; top_p=0.95; max sequence length=262144
- source: [https://huggingface.co/Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)
- [Motif 3 technical report](https://arxiv.org/html/2608.09119v1)
- [Artificial Analysis original HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 官方 Motif 模型卡及技术报告均列出 HLE 37.0。模型卡说明该表的成绩来自对应 benchmark leaderboards，统一采样参数为 temperature=1.0、top_p=0.95、最大序列长度 262,144。来源没有给出该结果的评测日期、harness 或具体 HLE 子集，因此未填这些字段。AA 的通用 HLE 方法使用 text-only 2,158 题及 pass@1，但 Motif 报告没有确认该结果采用了这一确切配置。

最近核验时间：2026-11-04T19:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Motif 3 model profile](https://artificialanalysis.ai/models/motif-3)
- [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 当前 Motif 3 页面显示指数 N/A。旧版 v4.3.2 页面中的 34* 明确为估算分数，且不是本地 V5 目标；未发现可核实的 v5.0 成绩。

最近核验时间：2026-11-04T19:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)
- [Motif 3 technical report](https://arxiv.org/html/2608.09119v1)

研究备注：
- Motif 官方报告列出 GDPval-AA v2 成绩 38.7；它不是目标 v2.1 Elo 指标。已检查 GDPval-AA v2.1 官方评测与方法资料，未发现 Motif 3 的 v2.1 分数。

最近核验时间：2026-11-04T19:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Motif 3 model card](https://huggingface.co/Motif-Technologies/Motif-3)

研究备注：
- Vals AI 官方 v2.2 榜单未列出 Motif 3；未找到该模型的 Vals Index v2.2 成绩。

最近核验时间：2026-11-04T19:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Motif 3 model profile",
          "url": "https://artificialanalysis.ai/models/motif-3"
        },
        {
          "label": "Artificial Analysis Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 当前 Motif 3 页面显示指数 N/A。旧版 v4.3.2 页面中的 34* 明确为估算分数，且不是本地 V5 目标；未发现可核实的 v5.0 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        }
      ],
      "notes": [
        "Zapier 官方榜单标注 v1.0.6，仅显示前 10 项并折叠 119 项；未在可见条目中发现 Motif 3。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法检查榜单隐藏的 119 项，不能确定是否包含 Motif 3。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        }
      ],
      "notes": [
        "官方模型卡标注此模型仅支持 text input；Chartography 要求读取图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        },
        {
          "label": "Motif 3 technical report",
          "url": "https://arxiv.org/html/2608.09119v1"
        }
      ],
      "notes": [
        "已检查官方 v1.1 榜单、Motif 3 模型卡和技术报告；未见该模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        },
        {
          "label": "Motif 3 technical report",
          "url": "https://arxiv.org/html/2608.09119v1"
        }
      ],
      "notes": [
        "Motif 官方报告列出 GDPval-AA v2 成绩 38.7；它不是目标 v2.1 Elo 指标。已检查 GDPval-AA v2.1 官方评测与方法资料，未发现 Motif 3 的 v2.1 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        },
        {
          "label": "Motif 3 technical report",
          "url": "https://arxiv.org/html/2608.09119v1"
        },
        {
          "label": "Artificial Analysis original HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "官方 Motif 模型卡及技术报告均列出 HLE 37.0。模型卡说明该表的成绩来自对应 benchmark leaderboards，统一采样参数为 temperature=1.0、top_p=0.95、最大序列长度 262,144。来源没有给出该结果的评测日期、harness 或具体 HLE 子集，因此未填这些字段。AA 的通用 HLE 方法使用 text-only 2,158 题及 pass@1，但 Motif 报告没有确认该结果采用了这一确切配置。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        }
      ],
      "notes": [
        "官方模型卡标注此模型仅支持 text input；OSWorld v2.1 是需根据桌面截图进行 GUI 操作的评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        },
        {
          "label": "Motif 3 technical report",
          "url": "https://arxiv.org/html/2608.09119v1"
        }
      ],
      "notes": [
        "Scale 官方 V2 榜单未见 Motif 3。模型卡和报告中的 SWE-bench Verified 76.2 是另一评测，未映射至 Pro V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        },
        {
          "label": "Motif 3 technical report",
          "url": "https://arxiv.org/html/2608.09119v1"
        }
      ],
      "notes": [
        "Vals AI 官方榜单未列 Motif 3；模型卡与技术报告也未报告此项成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
        },
        {
          "label": "Artificial Analysis Motif 3 model profile",
          "url": "https://artificialanalysis.ai/models/motif-3"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        },
        {
          "label": "Motif 3 technical report",
          "url": "https://arxiv.org/html/2608.09119v1"
        }
      ],
      "notes": [
        "Motif 模型卡和技术报告只列 Terminal-Bench 2.1（74.9），不映射至 v4。Terminal-Bench v4 官方榜单当前读取时没有可确认的数据行；Artificial Analysis 当前模型页没有提供可用于映射的 v4 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 v4 榜单当前没有可读的成绩行，无法判定公开榜单是否列出 Motif 3。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:22+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Motif 3 model card",
          "url": "https://huggingface.co/Motif-Technologies/Motif-3"
        }
      ],
      "notes": [
        "Vals AI 官方 v2.2 榜单未列出 Motif 3；未找到该模型的 Vals Index v2.2 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:22+08:00",
  "model_id": "motif-technologies/motif-3",
  "model_notes": [
    "Motif 3 官方模型卡确认模型为 BF16、文本输入/输出；技术报告的统一评测采样设置为 temperature=1.0、top_p=0.95、最大序列长度 262,144。",
    "报告中的 GDPval-AA v2 和 Terminal-Bench 2.1 分数不是本轮目标版本，未跨版本映射。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
