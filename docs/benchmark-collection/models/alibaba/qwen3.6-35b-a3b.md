# Qwen3.6 35B-A3B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.6-35b-a3b
- 模型名称：Qwen3.6 35B-A3B
- 发布日期：2026-04-17
- 最近检查时间：2026-11-05T08:49+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 本地已有 1 条 SWE-Bench Verified 成绩，不属于目标 Pro V2。
- 新增 Qwen 官方 HLE 原始分数 21.4；来源未标 metric、subset 或测试条件，故原样保留且不计覆盖率。
- 新增 GDPval-AA V2.1 Reasoning 与 Non-reasoning 两个独立 Elo 结果；来源显示 899 ± 18 与 854 ± 24，未把模型 release month 当作评测日期。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T08:49+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [Qwen3.6-35B-A3B release post](https://qwen.ai/blog?id=qwen3.6-27b), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:49+08:00 |
| terminal-bench-v4 | 待核实 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:49+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:49+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench project](https://github.com/zapier/AutomationBench) | 2026-11-05T08:49+08:00 |
| osworld-v2.1 | 待核实 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/), [OSWorld V2.1 release notes](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T08:49+08:00 |
| chartography | 未找到 | — | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T08:49+08:00 |
| humanitys-last-exam | 待核实 | 21.4 | [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md), [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:49+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact-model profile (current Index V5.0.1 section)](https://artificialanalysis.ai/models/qwen3-6-35b-a3b), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T08:49+08:00 |
| gdpval-aa-v2.1 | 已收录 | 899 ± 18 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; variant=Reasoning; harness=Stirrup agent loop; shell and web browsing); 854 ± 24 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; variant=Non-reasoning; harness=Stirrup agent loop; shell and web browsing) | [GDPval-AA V2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T08:49+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T08:49+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- No exact model score for DeepSWE v1.1 was verified; the public leaderboard view is partial.

尚未解决的问题：
- No exact model score for DeepSWE v1.1 was verified; the public leaderboard view is partial.

最近核验时间：2026-11-05T08:49+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [Qwen3.6-35B-A3B release post](https://qwen.ai/blog?id=qwen3.6-27b)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Official model materials mention unversioned SWE-bench Pro, which predates/does not identify the V2 refresh; it is not mapped to Pro V2.

尚未解决的问题：
- Official model materials mention unversioned SWE-bench Pro, which predates/does not identify the V2 refresh; it is not mapped to Pro V2.

最近核验时间：2026-11-05T08:49+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Official model materials mention Terminal-Bench 2.0; it is not target version 4.0.

尚未解决的问题：
- Official model materials mention Terminal-Bench 2.0; it is not target version 4.0.

最近核验时间：2026-11-05T08:49+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- No exact Terminal-Bench Science v0.1 score was verified.

尚未解决的问题：
- No exact Terminal-Bench Science v0.1 score was verified.

最近核验时间：2026-11-05T08:49+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench project](https://github.com/zapier/AutomationBench)

研究备注：
- Model supports tools and has a relevant task type; the visible official leaderboard subset does not establish this exact model’s score.

尚未解决的问题：
- Model supports tools and has a relevant task type; the visible official leaderboard subset does not establish this exact model’s score.

最近核验时间：2026-11-05T08:49+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 release notes](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- The model accepts images and supports agentic use, so the benchmark is applicable; the current OSWorld page did not provide a readable exact-model score.

尚未解决的问题：
- The model accepts images and supports agentic use, so the benchmark is applicable; the current OSWorld page did not provide a readable exact-model score.

最近核验时间：2026-11-05T08:49+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- The model accepts images and can answer chart questions. The current visible leaderboard includes other Qwen versions but no Qwen3.6-35B-A3B row; recorded as not found in this public snapshot.

最近核验时间：2026-11-05T08:49+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 21.4
- source: [https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen3.6-35B-A3B official Hugging Face model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md)
- [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Qwen official model-card table lists the exact Qwen3.6-35B-A3B column and HLE score 21.4. The table does not specify metric, subset, test condition, or evaluation date; retain the raw row without filling those fields and keep mapping under review.

尚未解决的问题：
- Qwen official model-card table lists the exact Qwen3.6-35B-A3B column and HLE score 21.4. The table does not specify metric, subset, test condition, or evaluation date; retain the raw row without filling those fields and keep mapping under review.

最近核验时间：2026-11-05T08:49+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact-model profile (current Index V5.0.1 section)](https://artificialanalysis.ai/models/qwen3-6-35b-a3b)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The exact-model profile shows Index N/A while the current index section specifies V5.0.1. No public V5 score was found.

最近核验时间：2026-11-05T08:49+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 899 ± 18
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- variant: Reasoning
- harness: Stirrup agent loop; shell and web browsing
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 854 ± 24
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- variant: Non-reasoning
- harness: Stirrup agent loop; shell and web browsing
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [GDPval-AA V2.1 official leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The current V2.1 leaderboard directly lists Qwen3.6 35B A3B Reasoning at Elo 899 ± 18 and Non-reasoning at 854 ± 24. Both are retained separately; April 2026 shown on the model row is release month, not evaluation date.

最近核验时间：2026-11-05T08:49+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The current V2.2 leaderboard does not show this exact model; its selection of latest/top/frontier models is not exhaustive, so status remains pending.

尚未解决的问题：
- The current V2.2 leaderboard does not show this exact model; its selection of latest/top/frontier models is not exhaustive, so status remains pending.

最近核验时间：2026-11-05T08:49+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model profile (current Index V5.0.1 section)",
          "url": "https://artificialanalysis.ai/models/qwen3-6-35b-a3b"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The exact-model profile shows Index N/A while the current index section specifies V5.0.1. No public V5 score was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
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
        "Model supports tools and has a relevant task type; the visible official leaderboard subset does not establish this exact model’s score."
      ],
      "status": "待核实",
      "unresolved": [
        "Model supports tools and has a relevant task type; the visible official leaderboard subset does not establish this exact model’s score."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "The model accepts images and can answer chart questions. The current visible leaderboard includes other Qwen versions but no Qwen3.6-35B-A3B row; recorded as not found in this public snapshot."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "No exact model score for DeepSWE v1.1 was verified; the public leaderboard view is partial."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact model score for DeepSWE v1.1 was verified; the public leaderboard view is partial."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA V2.1 official leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The current V2.1 leaderboard directly lists Qwen3.6 35B A3B Reasoning at Elo 899 ± 18 and Non-reasoning at 854 ± 24. Both are retained separately; April 2026 shown on the model row is release month, not evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "Humanity's Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Qwen official model-card table lists the exact Qwen3.6-35B-A3B column and HLE score 21.4. The table does not specify metric, subset, test condition, or evaluation date; retain the raw row without filling those fields and keep mapping under review."
      ],
      "status": "待核实",
      "unresolved": [
        "Qwen official model-card table lists the exact Qwen3.6-35B-A3B column and HLE score 21.4. The table does not specify metric, subset, test condition, or evaluation date; retain the raw row without filling those fields and keep mapping under review."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "OSWorld V2.1 benchmark",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 release notes",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "The model accepts images and supports agentic use, so the benchmark is applicable; the current OSWorld page did not provide a readable exact-model score."
      ],
      "status": "待核实",
      "unresolved": [
        "The model accepts images and supports agentic use, so the benchmark is applicable; the current OSWorld page did not provide a readable exact-model score."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "Qwen3.6-35B-A3B release post",
          "url": "https://qwen.ai/blog?id=qwen3.6-27b"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Official model materials mention unversioned SWE-bench Pro, which predates/does not identify the V2 refresh; it is not mapped to Pro V2."
      ],
      "status": "待核实",
      "unresolved": [
        "Official model materials mention unversioned SWE-bench Pro, which predates/does not identify the V2 refresh; it is not mapped to Pro V2."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "Terminal-Bench Science benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "No exact Terminal-Bench Science v0.1 score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench Science v0.1 score was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.6-35B-A3B official Hugging Face model card",
          "url": "https://huggingface.co/Qwen/Qwen3.6-35B-A3B/raw/main/README.md"
        },
        {
          "label": "Terminal-Bench 4.0 benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Official model materials mention Terminal-Bench 2.0; it is not target version 4.0."
      ],
      "status": "待核实",
      "unresolved": [
        "Official model materials mention Terminal-Bench 2.0; it is not target version 4.0."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:49+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The current V2.2 leaderboard does not show this exact model; its selection of latest/top/frontier models is not exhaustive, so status remains pending."
      ],
      "status": "待核实",
      "unresolved": [
        "The current V2.2 leaderboard does not show this exact model; its selection of latest/top/frontier models is not exhaustive, so status remains pending."
      ]
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:49+08:00",
  "model_id": "alibaba/qwen3.6-35b-a3b",
  "model_notes": [
    "本地已有 1 条 SWE-Bench Verified 成绩，不属于目标 Pro V2。",
    "新增 Qwen 官方 HLE 原始分数 21.4；来源未标 metric、subset 或测试条件，故原样保留且不计覆盖率。",
    "新增 GDPval-AA V2.1 Reasoning 与 Non-reasoning 两个独立 Elo 结果；来源显示 899 ± 18 与 854 ± 24，未把模型 release month 当作评测日期。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
