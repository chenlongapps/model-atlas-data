# Hy3 preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：tencent/hy3-preview
- 模型名称：Hy3 preview
- 发布日期：2026-04-20
- 最近检查时间：2026-11-05T08:48+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地原有 1 条 SWE-Bench Verified 成绩；目标 Pro V2 等版本未由该行替代。
- Tencent 官方模型卡评测组件显示 cais/hle 30*；由于 metric、子集和星号含义未说明，原值作为未映射记录保留。
- 本地 release_date 为 2026-04-20，模型卡的权重公开日期为 2026-04-23；本轮不据此改动发布日期。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T08:48+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:48+08:00 |
| terminal-bench-v4 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:48+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:48+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench project](https://github.com/zapier/AutomationBench) | 2026-11-05T08:48+08:00 |
| osworld-v2.1 | 不适用 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/) | 2026-11-05T08:48+08:00 |
| chartography | 不适用 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography harness](https://github.com/surge-ai/chartography) | 2026-11-05T08:48+08:00 |
| humanitys-last-exam | 待核实 | 30* (dataset=cais/hle) | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [Humanity's Last Exam dataset](https://huggingface.co/datasets/cais/hle), [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:48+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact-model profile](https://artificialanalysis.ai/models/hy3-preview), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T08:48+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [GDPval-AA V2.1 leaderboard and definition](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T08:48+08:00 |
| vals-index-v2.2 | 待核实 | — | [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview), [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T08:48+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Official preview materials do not list an exact DeepSWE v1.1 score; the public leaderboard view is partial.

尚未解决的问题：
- Official preview materials do not list an exact DeepSWE v1.1 score; the public leaderboard view is partial.

最近核验时间：2026-11-05T08:48+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- The model card contains older or differently named coding results, not a directly confirmed SWE-bench Pro V2 score.

尚未解决的问题：
- The model card contains older or differently named coding results, not a directly confirmed SWE-bench Pro V2 score.

最近核验时间：2026-11-05T08:48+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- The model card reports Terminal-Bench 2.0 = 54.4 without full metric/harness details; this is not version 4.0.

尚未解决的问题：
- The model card reports Terminal-Bench 2.0 = 54.4 without full metric/harness details; this is not version 4.0.

最近核验时间：2026-11-05T08:48+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- No exact Hy3-preview Terminal-Bench Science v0.1 result was verified.

尚未解决的问题：
- No exact Hy3-preview Terminal-Bench Science v0.1 result was verified.

最近核验时间：2026-11-05T08:48+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench project](https://github.com/zapier/AutomationBench)

研究备注：
- The text model supports agent workflows, but Zapier leaderboard shows only a partial set of entries; no exact score was verified.

尚未解决的问题：
- The text model supports agent workflows, but Zapier leaderboard shows only a partial set of entries; no exact score was verified.

最近核验时间：2026-11-05T08:48+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/)

研究备注：
- The exact Hy3-preview model card lists text input only. The standard OSWorld desktop interaction tasks require visual observation.

最近核验时间：2026-11-05T08:48+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography harness](https://github.com/surge-ai/chartography)

研究备注：
- Hy3-preview is text-only, while Chartography passes chart images inline. The Surge row labelled “Hy3 (High reasoning)” does not identify this preview version and the same UUID has 1.2% and 0.5% visible entries; neither is mapped.

最近核验时间：2026-11-05T08:48+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 30*
- dataset: cais/hle
- source: [https://huggingface.co/tencent/Hy3-preview](https://huggingface.co/tencent/Hy3-preview)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [Humanity's Last Exam dataset](https://huggingface.co/datasets/cais/hle)
- [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HF evaluation widget on the exact Hy3-preview model card shows `cais/hle` and `30*`. The card does not explain the metric, subset, conditions, or asterisk; the raw value is retained without metric and is not counted as a mapping.

尚未解决的问题：
- HF evaluation widget on the exact Hy3-preview model card shows `cais/hle` and `30*`. The card does not explain the metric, subset, conditions, or asterisk; the raw value is retained without metric and is not counted as a mapping.

最近核验时间：2026-11-05T08:48+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact-model profile](https://artificialanalysis.ai/models/hy3-preview)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The current exact-model profile shows Index N/A; its current Index section is V5.0.1. No public V5 score was found.

最近核验时间：2026-11-05T08:48+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [GDPval-AA V2.1 leaderboard and definition](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- No Hy3-preview row was verified on the current V2.1 page. The dynamic page may omit older models, so status remains pending.

尚未解决的问题：
- No Hy3-preview row was verified on the current V2.1 page. The dynamic page may omit older models, so status remains pending.

最近核验时间：2026-11-05T08:48+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3-preview official Hugging Face model card](https://huggingface.co/tencent/Hy3-preview)
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Current V2.2 page displays selected latest/top/frontier models; absence of Hy3-preview is not conclusive.

尚未解决的问题：
- Current V2.2 page displays selected latest/top/frontier models; absence of Hy3-preview is not conclusive.

最近核验时间：2026-11-05T08:48+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model profile",
          "url": "https://artificialanalysis.ai/models/hy3-preview"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The current exact-model profile shows Index N/A; its current Index section is V5.0.1. No public V5 score was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench project",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "The text model supports agent workflows, but Zapier leaderboard shows only a partial set of entries; no exact score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "The text model supports agent workflows, but Zapier leaderboard shows only a partial set of entries; no exact score was verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography harness",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Hy3-preview is text-only, while Chartography passes chart images inline. The Surge row labelled “Hy3 (High reasoning)” does not identify this preview version and the same UUID has 1.2% and 0.5% visible entries; neither is mapped."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Official preview materials do not list an exact DeepSWE v1.1 score; the public leaderboard view is partial."
      ],
      "status": "待核实",
      "unresolved": [
        "Official preview materials do not list an exact DeepSWE v1.1 score; the public leaderboard view is partial."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "GDPval-AA V2.1 leaderboard and definition",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "No Hy3-preview row was verified on the current V2.1 page. The dynamic page may omit older models, so status remains pending."
      ],
      "status": "待核实",
      "unresolved": [
        "No Hy3-preview row was verified on the current V2.1 page. The dynamic page may omit older models, so status remains pending."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "Humanity's Last Exam dataset",
          "url": "https://huggingface.co/datasets/cais/hle"
        },
        {
          "label": "Humanity's Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HF evaluation widget on the exact Hy3-preview model card shows `cais/hle` and `30*`. The card does not explain the metric, subset, conditions, or asterisk; the raw value is retained without metric and is not counted as a mapping."
      ],
      "status": "待核实",
      "unresolved": [
        "HF evaluation widget on the exact Hy3-preview model card shows `cais/hle` and `30*`. The card does not explain the metric, subset, conditions, or asterisk; the raw value is retained without metric and is not counted as a mapping."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "OSWorld V2.1 benchmark",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "The exact Hy3-preview model card lists text input only. The standard OSWorld desktop interaction tasks require visual observation."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "The model card contains older or differently named coding results, not a directly confirmed SWE-bench Pro V2 score."
      ],
      "status": "待核实",
      "unresolved": [
        "The model card contains older or differently named coding results, not a directly confirmed SWE-bench Pro V2 score."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "Terminal-Bench Science benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "No exact Hy3-preview Terminal-Bench Science v0.1 result was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Hy3-preview Terminal-Bench Science v0.1 result was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "Terminal-Bench 4.0 benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "The model card reports Terminal-Bench 2.0 = 54.4 without full metric/harness details; this is not version 4.0."
      ],
      "status": "待核实",
      "unresolved": [
        "The model card reports Terminal-Bench 2.0 = 54.4 without full metric/harness details; this is not version 4.0."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:48+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3-preview official Hugging Face model card",
          "url": "https://huggingface.co/tencent/Hy3-preview"
        },
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Current V2.2 page displays selected latest/top/frontier models; absence of Hy3-preview is not conclusive."
      ],
      "status": "待核实",
      "unresolved": [
        "Current V2.2 page displays selected latest/top/frontier models; absence of Hy3-preview is not conclusive."
      ]
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:48+08:00",
  "model_id": "tencent/hy3-preview",
  "model_notes": [
    "本地原有 1 条 SWE-Bench Verified 成绩；目标 Pro V2 等版本未由该行替代。",
    "Tencent 官方模型卡评测组件显示 cais/hle 30*；由于 metric、子集和星号含义未说明，原值作为未映射记录保留。",
    "本地 release_date 为 2026-04-20，模型卡的权重公开日期为 2026-04-23；本轮不据此改动发布日期。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
