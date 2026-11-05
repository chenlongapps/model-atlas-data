# Qwen3.7 Max Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.7-max
- 模型名称：Qwen3.7 Max
- 发布日期：2026-05-21
- 最近检查时间：2026-11-05T05:30+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：9
- 当前已收录的对应成绩数量：4

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 21.6 (version=1.1; dataset=113 tasks; variant=Qwen reports the higher score across Claude Code and mini-SWE-agent; temperature=1.0; top_p=0.95; 256K context; selected harness not specified) | [Qwen3.8 official model card with Qwen3.7-Max comparison](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [DeepSWE v1.1 official benchmark page](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T05:30+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen official result/model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [SWE-bench Pro V2 dataset card](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-05T05:30+08:00 |
| terminal-bench-v4 | 已收录 | 69.7 (metric=success rate; version=2.0; harness=Terminus-2); 2% (rounded display) (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=pass@1 across three repeats; maximum 500 agent steps; rounded integer display; harness=mini-swe-agent) | [Artificial Analysis Qwen3.8/Qwen3.7 comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-7-max), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:30+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T05:30+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Qwen official comparison/model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-05T05:30+08:00 |
| osworld-v2.1 | 不适用 | — | [Alibaba Qwen3.7 Max snapshot/model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-7-max), [OSWorld official results](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T05:30+08:00 |
| chartography | 不适用 | — | [Alibaba Qwen3.7 Max snapshot/model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-7-max), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T05:30+08:00 |
| humanitys-last-exam | 已收录 | 41.4 (metric=accuracy); 53.5 (metric=accuracy; variant=with tools) | [Qwen3.7 official release page](https://qwen.ai/blog?id=qwen3.7&locale=en), [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-11-05T05:30+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.7 Max model page](https://artificialanalysis.ai/models/qwen3-7-max), [Artificial Analysis Index V5 methodology/article](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) | 2026-11-05T05:30+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1128 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; harness=Stirrup) | [Artificial Analysis Qwen3.7 Max comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-max-vs-step-3-5-flash-0202), [Artificial Analysis GDPval-AA method](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:30+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T05:30+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 21.6
- version: 1.1
- dataset: 113 tasks
- variant: Qwen reports the higher score across Claude Code and mini-SWE-agent; temperature=1.0; top_p=0.95; 256K context; selected harness not specified
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen3.8 official model card with Qwen3.7-Max comparison](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [DeepSWE v1.1 official benchmark page](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Official comparison table reports Qwen3.7-Max 21.6 on DeepSWE 1.1. The card says it ran Claude Code and mini-SWE-agent and reports the higher result, but does not identify the selected harness or metric name.

尚未解决的问题：
- Metric and selected harness are unspecified; cannot map to the local pass@1 definition yet.

最近核验时间：2026-11-05T05:30+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen official result/model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [SWE-bench Pro V2 dataset card](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- TOML already has 60.6 for generic SWE-Bench Pro. Official Qwen material calls it SWE-bench Pro/refined benchmark but does not identify version 2.0.0; no V2 row added.

尚未解决的问题：
- Need exact evidence that the existing generic Pro score used dataset version 2.0.0.

最近核验时间：2026-11-05T05:30+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 69.7
- metric: success rate
- version: 2.0
- harness: Terminus-2
- source: [https://qwen.ai/blog?id=qwen3.7](https://qwen.ai/blog?id=qwen3.7)
- date: 2026-05-19
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 2% (rounded display)
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: pass@1 across three repeats; maximum 500 agent steps; rounded integer display
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-7-max](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-7-max)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.8/Qwen3.7 comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-7-max)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA comparison gives Qwen3.7 Max 2% on Terminal-Bench 4.0. The independently tested result uses mini-swe-agent, 66 tasks, pass@1 across three repeats and a 500-step maximum; AA exposes only rounded integer percent.

最近核验时间：2026-11-05T05:30+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Checked the official v0.1 result table; it does not list Qwen3.7 Max.

最近核验时间：2026-11-05T05:30+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen official comparison/model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- Qwen material reports 14.2 Pass@1 on a 600-task public subset. The local v1.0.6 definition refers to the leaderboard held-out private task set; this public subset score is not equivalent. Zapier currently exposes only top rows and folds 119 more. No score row added.

尚未解决的问题：
- No verified score for the exact v1.0.6 private leaderboard.

最近核验时间：2026-11-05T05:30+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Qwen3.7 Max snapshot/model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-7-max)
- [OSWorld official results](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- The 2026-05-20 Qwen3.7-Max snapshot is text-only and cannot receive desktop screenshots; later multimodal snapshots are different conditions and are not transferred.

最近核验时间：2026-11-05T05:30+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Alibaba Qwen3.7 Max snapshot/model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-7-max)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- The 2026-05-20 Qwen3.7-Max snapshot is text-only and cannot ingest chart images. The leaderboard score for Qwen 3.7 Plus is a different model.

最近核验时间：2026-11-05T05:30+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 41.4
- metric: accuracy
- source: [https://qwen.ai/blog?id=qwen3.7](https://qwen.ai/blog?id=qwen3.7)
- date: 2026-05-19
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 53.5
- metric: accuracy
- variant: with tools
- source: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Qwen3.7 official release page](https://qwen.ai/blog?id=qwen3.7&locale=en)
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

研究备注：
- Preserved the existing 41.4 accuracy record. Added the separately labeled HLE w/ tools result, 53.5; no conditions were merged.

最近核验时间：2026-11-05T05:30+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.7 Max model page](https://artificialanalysis.ai/models/qwen3-7-max)
- [Artificial Analysis Index V5 methodology/article](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- The current AA model page has no V5.0.1 score/public API. Its older Intelligence Index value 29 belongs to v4.3.2 and is not mapped to V5.

最近核验时间：2026-11-05T05:30+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1128
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-7-max-vs-step-3-5-flash-0202](https://artificialanalysis.ai/models/comparisons/qwen3-7-max-vs-step-3-5-flash-0202)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.7 Max comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-max-vs-step-3-5-flash-0202)
- [Artificial Analysis GDPval-AA method](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Direct comparison page reports 1128 Elo for GDPval-AA v2.1. Methodology states 220 tasks and Elo from pairwise judging; model-specific effort was not disclosed.

最近核验时间：2026-11-05T05:30+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Current v2.2 leaderboard view does not list Qwen3.7 Max; it lists Qwen3.8 Max (0902), a different model.

最近核验时间：2026-11-05T05:30+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.7 Max model page",
          "url": "https://artificialanalysis.ai/models/qwen3-7-max"
        },
        {
          "label": "Artificial Analysis Index V5 methodology/article",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "The current AA model page has no V5.0.1 score/public API. Its older Intelligence Index value 29 belongs to v4.3.2 and is not mapped to V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Qwen official comparison/model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Qwen material reports 14.2 Pass@1 on a 600-task public subset. The local v1.0.6 definition refers to the leaderboard held-out private task set; this public subset score is not equivalent. Zapier currently exposes only top rows and folds 119 more. No score row added."
      ],
      "status": "待核实",
      "unresolved": [
        "No verified score for the exact v1.0.6 private leaderboard."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Qwen3.7 Max snapshot/model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-7-max"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "The 2026-05-20 Qwen3.7-Max snapshot is text-only and cannot ingest chart images. The leaderboard score for Qwen 3.7 Plus is a different model."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8 official model card with Qwen3.7-Max comparison",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "DeepSWE v1.1 official benchmark page",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Official comparison table reports Qwen3.7-Max 21.6 on DeepSWE 1.1. The card says it ran Claude Code and mini-SWE-agent and reports the higher result, but does not identify the selected harness or metric name."
      ],
      "status": "待核实",
      "unresolved": [
        "Metric and selected harness are unspecified; cannot map to the local pass@1 definition yet."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.7 Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-7-max-vs-step-3-5-flash-0202"
        },
        {
          "label": "Artificial Analysis GDPval-AA method",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Direct comparison page reports 1128 Elo for GDPval-AA v2.1. Methodology states 220 tasks and Elo from pairwise judging; model-specific effort was not disclosed."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.7 official release page",
          "url": "https://qwen.ai/blog?id=qwen3.7&locale=en"
        },
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        }
      ],
      "notes": [
        "Preserved the existing 41.4 accuracy record. Added the separately labeled HLE w/ tools result, 53.5; no conditions were merged."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Qwen3.7 Max snapshot/model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-7-max"
        },
        {
          "label": "OSWorld official results",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "The 2026-05-20 Qwen3.7-Max snapshot is text-only and cannot receive desktop screenshots; later multimodal snapshots are different conditions and are not transferred."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Qwen official result/model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "SWE-bench Pro V2 dataset card",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "TOML already has 60.6 for generic SWE-Bench Pro. Official Qwen material calls it SWE-bench Pro/refined benchmark but does not identify version 2.0.0; no V2 row added."
      ],
      "status": "待核实",
      "unresolved": [
        "Need exact evidence that the existing generic Pro score used dataset version 2.0.0."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Checked the official v0.1 result table; it does not list Qwen3.7 Max."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8/Qwen3.7 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-qwen3-7-max"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA comparison gives Qwen3.7 Max 2% on Terminal-Bench 4.0. The independently tested result uses mini-swe-agent, 66 tasks, pass@1 across three repeats and a 500-step maximum; AA exposes only rounded integer percent."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T05:30+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Current v2.2 leaderboard view does not list Qwen3.7 Max; it lists Qwen3.8 Max (0902), a different model."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 9,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T05:30+08:00",
  "model_id": "alibaba/qwen3.7-max",
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
