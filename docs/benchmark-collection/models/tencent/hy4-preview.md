# Hy4 preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：tencent/hy4-preview
- 模型名称：Hy4 preview
- 发布日期：2026-08-28
- 最近检查时间：2026-11-04T13:24+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：4

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview), [Hugging Face community evaluation extraction record](https://huggingface.co/tencent/Hy4-preview/discussions/3), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T13:24+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview), [Hugging Face community evaluation extraction record](https://huggingface.co/tencent/Hy4-preview/discussions/3), [Hugging Face SWE-bench Pro leaderboard result](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=tencent%2FHy4-preview&leaderboard_task_id=SWE_Bench_Pro), [Scale AI official SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T13:24+08:00 |
| terminal-bench-v4 | 待核实 | 8.08 (metric=accuracy; version=4.0.0; dataset=Full (66 tasks); variant=avg@3 (mean of three pass@1 runs); 8-hour task limit; no step or cost limit; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4), [Vals AI Hy4 Preview model results](https://www.vals.ai/models/tencent_hy4-preview) | 2026-11-04T13:24+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 1.43 (metric=accuracy; version=0.1.0; dataset=Full (70 tasks); variant=single pass@1 run; infrastructure/provider errors retried; 8-hour task limit; harness=Terminus 2) | [Vals AI Terminal-Bench Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science), [Vals AI Hy4 Preview model results](https://www.vals.ai/models/tencent_hy4-preview) | 2026-11-04T13:24+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview), [Tencent Hy4 preview release announcement](https://www.tencent.com/tencent-releases-and-opensources-tencent-hy4-preview/), [Zapier AutomationBench official leaderboard and protocol](https://zapier.com/benchmarks), [Secondary transcription of Tencent model-card chart (not used as score source)](https://hy4.site/benchmarks/hy4-benchmarks) | 2026-11-04T13:24+08:00 |
| osworld-v2.1 | 未找到 | — | [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview), [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-04T13:24+08:00 |
| chartography | 已收录 | 1.6 (metric=accuracy (mean; Pass@1); version=unspecified; dataset=100 expert tasks; effort=High reasoning; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge AI Chartography evaluation repository and metric](https://github.com/surge-ai/chartography) | 2026-11-04T13:24+08:00 |
| humanitys-last-exam | 已收录 | 43.4 (metric=accuracy; dataset=Text-only; variant=no tools); 55.4 (metric=accuracy; dataset=Text-only; variant=with tools) | [Tencent Hy4 preview official model card benchmark appendix](https://huggingface.co/tencent/Hy4-preview#benchmark-appendix), [Humanity's Last Exam official benchmark page](https://lastexam.ai/), [Hugging Face auxiliary HLE metadata (validation error; not used as score source)](https://huggingface.co/tencent/Hy4-preview/blob/main/.eval_results/hle.yaml) | 2026-11-04T13:24+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index V5 evaluations](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview) | 2026-11-04T13:24+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Tencent Hy4 preview official model card benchmark appendix](https://huggingface.co/tencent/Hy4-preview#benchmark-appendix), [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T13:24+08:00 |
| vals-index-v2.2 | 已收录 | 53.21 (metric=performance score; version=2.2) | [Vals Index v2.2 official leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index), [Vals AI Hy4 Preview model results](https://www.vals.ai/models/tencent_hy4-preview) | 2026-11-04T13:24+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview)
- [Hugging Face community evaluation extraction record](https://huggingface.co/tencent/Hy4-preview/discussions/3)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- ['Hugging Face community metadata reports a model-card-derived candidate score of 64.3, but neither the model card result nor its dataset metadata confirms DeepSWE v1.1. Datacurve’s official v1.1 leaderboard does not list Hy4 preview. The candidate is not written to TOML until the version is verified.']

尚未解决的问题：
- 候选分数 64.3 来自模型卡提取记录，但无法确认它对应目标 v1.1；未录入 TOML。

最近核验时间：2026-11-04T13:24+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview)
- [Hugging Face community evaluation extraction record](https://huggingface.co/tencent/Hy4-preview/discussions/3)
- [Hugging Face SWE-bench Pro leaderboard result](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=tencent%2FHy4-preview&leaderboard_task_id=SWE_Bench_Pro)
- [Scale AI official SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- ['Hugging Face shows a model-card-derived candidate score of 65.7. Its extraction record dates to 2026-08-28, before Scale published SWE-bench Pro V2 on 2026-09-22, so the score cannot be attributed to V2. The candidate is not written to TOML.']

尚未解决的问题：
- 候选分数 65.7 的模型卡提取记录早于 V2 发布，且没有足够证据证明使用 V2 协议；未录入 TOML。

最近核验时间：2026-11-04T13:24+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 8.08
- metric: accuracy
- version: 4.0.0
- dataset: Full (66 tasks)
- variant: avg@3 (mean of three pass@1 runs); 8-hour task limit; no step or cost limit
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Vals AI Hy4 Preview model results](https://www.vals.ai/models/tencent_hy4-preview)

研究备注：
- ['Vals lists Hy4 Preview at 8.08% on Terminal-Bench 4.0 using Mini-SWE-agent, avg@3 (three pass@1 runs), 66 tasks, and an 8-hour task limit. Vals labels its metric “accuracy”; this source metric is preserved verbatim and does not exactly match the local definition metric “task resolution rate”, so the mapping remains pending review. No evaluation date is stated.']

尚未解决的问题：
- 来源指标为 accuracy，仓库定义指标为 task resolution rate；保留来源原文指标，待核对映射。

最近核验时间：2026-11-04T13:24+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 1.43
- metric: accuracy
- version: 0.1.0
- dataset: Full (70 tasks)
- variant: single pass@1 run; infrastructure/provider errors retried; 8-hour task limit
- harness: Terminus 2
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals AI Terminal-Bench Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Vals AI Hy4 Preview model results](https://www.vals.ai/models/tencent_hy4-preview)

研究备注：
- ['Vals lists Hy4 Preview at 1.43% on version 0.1.0 using Terminus 2; its method page specifies 70 tasks, one pass@1 run per model, infrastructure/provider error retries, and an 8-hour task limit. Vals labels its metric “accuracy”; the raw source metric is preserved and awaits mapping review against the local definition “task resolution rate”. No evaluation date is stated.']

尚未解决的问题：
- 来源指标为 accuracy，仓库定义指标为 task resolution rate；保留来源原文指标，待核对映射。

最近核验时间：2026-11-04T13:24+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview)
- [Tencent Hy4 preview release announcement](https://www.tencent.com/tencent-releases-and-opensources-tencent-hy4-preview/)
- [Zapier AutomationBench official leaderboard and protocol](https://zapier.com/benchmarks)
- [Secondary transcription of Tencent model-card chart (not used as score source)](https://hy4.site/benchmarks/hy4-benchmarks)

研究备注：
- ['A candidate value of 32.1% appears in a secondary transcription of Tencent’s model-card chart, but the chart image could not be independently read and Zapier’s official v1.0.6 leaderboard does not list Hy4. Do not write the transcribed score until the original row and test conditions can be verified.']

尚未解决的问题：
- 候选 32.1% 仅可从二手转录核对；官方模型卡原图的具体行及评测条件未能独立确认。

最近核验时间：2026-11-04T13:24+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview)
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- ['No exact Hy4 preview OSWorld v2.1 result was found in the reviewed official materials. A third-party low-confidence estimate was excluded; OSWorld-Verified and OSWorld 2.0 results were not mapped to v2.1.']

最近核验时间：2026-11-04T13:24+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 1.6
- metric: accuracy (mean; Pass@1)
- version: unspecified
- dataset: 100 expert tasks
- effort: High reasoning
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge AI Chartography evaluation repository and metric](https://github.com/surge-ai/chartography)

研究备注：
- ['Surge’s official leaderboard lists Hy4 Preview (High reasoning) at 1.6%. The task set has 100 expert-written tasks; the official repository describes accuracy/mean Pass@1, Inspect AI, 10 runs per task, and Gemini 3.5 Flash judge. No evaluation date is published.']

最近核验时间：2026-11-04T13:24+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 43.4
- metric: accuracy
- dataset: Text-only
- variant: no tools
- source: [https://huggingface.co/tencent/Hy4-preview](https://huggingface.co/tencent/Hy4-preview)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 55.4
- metric: accuracy
- dataset: Text-only
- variant: with tools
- source: [https://huggingface.co/tencent/Hy4-preview](https://huggingface.co/tencent/Hy4-preview)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Tencent Hy4 preview official model card benchmark appendix](https://huggingface.co/tencent/Hy4-preview#benchmark-appendix)
- [Humanity's Last Exam official benchmark page](https://lastexam.ai/)
- [Hugging Face auxiliary HLE metadata (validation error; not used as score source)](https://huggingface.co/tencent/Hy4-preview/blob/main/.eval_results/hle.yaml)

研究备注：
- ['Tencent’s official model-card benchmark appendix reports text-only HLE accuracy of 43.4% without tools and 55.4% with tools; these are retained as separate configurations. Exact tool setup and evaluation date are not stated. Hugging Face auxiliary HLE metadata currently has a validation error and was not used to establish the scores.']

最近核验时间：2026-11-04T13:24+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5 evaluations](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Tencent Hy4 preview official model card](https://huggingface.co/tencent/Hy4-preview)

研究备注：
- ['The current official Artificial Analysis V5 page and model listings do not show an exact Hy4 preview score. No score is written.']

最近核验时间：2026-11-04T13:24+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy4 preview official model card benchmark appendix](https://huggingface.co/tencent/Hy4-preview#benchmark-appendix)
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- ['Tencent’s model card reports GDPval-AA V2 at Elo 1678, not v2.1. The current AA v2.1 page has no exact Hy4 preview result. The older V2 score is not written as a v2.1 result.']

尚未解决的问题：
- 官方模型卡所列 GDPval-AA V2 1678 分不能证明属于 v2.1；未录入 TOML。

最近核验时间：2026-11-04T13:24+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 53.21
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index v2.2 official leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI Hy4 Preview model results](https://www.vals.ai/models/tencent_hy4-preview)

研究备注：
- ['Vals’ official v2.2 leaderboard lists Hy4 Preview at 53.21% (±1.13 standard error). The page update date is a leaderboard snapshot, not a published evaluation date, so date is omitted.']

最近核验时间：2026-11-04T13:24+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5 evaluations",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Tencent Hy4 preview official model card",
          "url": "https://huggingface.co/tencent/Hy4-preview"
        }
      ],
      "notes": [
        [
          "The current official Artificial Analysis V5 page and model listings do not show an exact Hy4 preview score. No score is written."
        ]
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy4 preview official model card",
          "url": "https://huggingface.co/tencent/Hy4-preview"
        },
        {
          "label": "Tencent Hy4 preview release announcement",
          "url": "https://www.tencent.com/tencent-releases-and-opensources-tencent-hy4-preview/"
        },
        {
          "label": "Zapier AutomationBench official leaderboard and protocol",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Secondary transcription of Tencent model-card chart (not used as score source)",
          "url": "https://hy4.site/benchmarks/hy4-benchmarks"
        }
      ],
      "notes": [
        [
          "A candidate value of 32.1% appears in a secondary transcription of Tencent’s model-card chart, but the chart image could not be independently read and Zapier’s official v1.0.6 leaderboard does not list Hy4. Do not write the transcribed score until the original row and test conditions can be verified."
        ]
      ],
      "status": "待核实",
      "unresolved": [
        "候选 32.1% 仅可从二手转录核对；官方模型卡原图的具体行及评测条件未能独立确认。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge AI Chartography evaluation repository and metric",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        [
          "Surge’s official leaderboard lists Hy4 Preview (High reasoning) at 1.6%. The task set has 100 expert-written tasks; the official repository describes accuracy/mean Pass@1, Inspect AI, 10 runs per task, and Gemini 3.5 Flash judge. No evaluation date is published."
        ]
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy4 preview official model card",
          "url": "https://huggingface.co/tencent/Hy4-preview"
        },
        {
          "label": "Hugging Face community evaluation extraction record",
          "url": "https://huggingface.co/tencent/Hy4-preview/discussions/3"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        [
          "Hugging Face community metadata reports a model-card-derived candidate score of 64.3, but neither the model card result nor its dataset metadata confirms DeepSWE v1.1. Datacurve’s official v1.1 leaderboard does not list Hy4 preview. The candidate is not written to TOML until the version is verified."
        ]
      ],
      "status": "待核实",
      "unresolved": [
        "候选分数 64.3 来自模型卡提取记录，但无法确认它对应目标 v1.1；未录入 TOML。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy4 preview official model card benchmark appendix",
          "url": "https://huggingface.co/tencent/Hy4-preview#benchmark-appendix"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        [
          "Tencent’s model card reports GDPval-AA V2 at Elo 1678, not v2.1. The current AA v2.1 page has no exact Hy4 preview result. The older V2 score is not written as a v2.1 result."
        ]
      ],
      "status": "待核实",
      "unresolved": [
        "官方模型卡所列 GDPval-AA V2 1678 分不能证明属于 v2.1；未录入 TOML。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy4 preview official model card benchmark appendix",
          "url": "https://huggingface.co/tencent/Hy4-preview#benchmark-appendix"
        },
        {
          "label": "Humanity's Last Exam official benchmark page",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "Hugging Face auxiliary HLE metadata (validation error; not used as score source)",
          "url": "https://huggingface.co/tencent/Hy4-preview/blob/main/.eval_results/hle.yaml"
        }
      ],
      "notes": [
        [
          "Tencent’s official model-card benchmark appendix reports text-only HLE accuracy of 43.4% without tools and 55.4% with tools; these are retained as separate configurations. Exact tool setup and evaluation date are not stated. Hugging Face auxiliary HLE metadata currently has a validation error and was not used to establish the scores."
        ]
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy4 preview official model card",
          "url": "https://huggingface.co/tencent/Hy4-preview"
        },
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        [
          "No exact Hy4 preview OSWorld v2.1 result was found in the reviewed official materials. A third-party low-confidence estimate was excluded; OSWorld-Verified and OSWorld 2.0 results were not mapped to v2.1."
        ]
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy4 preview official model card",
          "url": "https://huggingface.co/tencent/Hy4-preview"
        },
        {
          "label": "Hugging Face community evaluation extraction record",
          "url": "https://huggingface.co/tencent/Hy4-preview/discussions/3"
        },
        {
          "label": "Hugging Face SWE-bench Pro leaderboard result",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=tencent%2FHy4-preview&leaderboard_task_id=SWE_Bench_Pro"
        },
        {
          "label": "Scale AI official SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        [
          "Hugging Face shows a model-card-derived candidate score of 65.7. Its extraction record dates to 2026-08-28, before Scale published SWE-bench Pro V2 on 2026-09-22, so the score cannot be attributed to V2. The candidate is not written to TOML."
        ]
      ],
      "status": "待核实",
      "unresolved": [
        "候选分数 65.7 的模型卡提取记录早于 V2 发布，且没有足够证据证明使用 V2 协议；未录入 TOML。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Vals AI Hy4 Preview model results",
          "url": "https://www.vals.ai/models/tencent_hy4-preview"
        }
      ],
      "notes": [
        [
          "Vals lists Hy4 Preview at 1.43% on version 0.1.0 using Terminus 2; its method page specifies 70 tasks, one pass@1 run per model, infrastructure/provider error retries, and an 8-hour task limit. Vals labels its metric “accuracy”; the raw source metric is preserved and awaits mapping review against the local definition “task resolution rate”. No evaluation date is stated."
        ]
      ],
      "status": "待核实",
      "unresolved": [
        "来源指标为 accuracy，仓库定义指标为 task resolution rate；保留来源原文指标，待核对映射。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals AI Hy4 Preview model results",
          "url": "https://www.vals.ai/models/tencent_hy4-preview"
        }
      ],
      "notes": [
        [
          "Vals lists Hy4 Preview at 8.08% on Terminal-Bench 4.0 using Mini-SWE-agent, avg@3 (three pass@1 runs), 66 tasks, and an 8-hour task limit. Vals labels its metric “accuracy”; this source metric is preserved verbatim and does not exactly match the local definition metric “task resolution rate”, so the mapping remains pending review. No evaluation date is stated."
        ]
      ],
      "status": "待核实",
      "unresolved": [
        "来源指标为 accuracy，仓库定义指标为 task resolution rate；保留来源原文指标，待核对映射。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T13:24+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI Hy4 Preview model results",
          "url": "https://www.vals.ai/models/tencent_hy4-preview"
        }
      ],
      "notes": [
        [
          "Vals’ official v2.2 leaderboard lists Hy4 Preview at 53.21% (±1.13 standard error). The page update date is a leaderboard snapshot, not a published evaluation date, so date is omitted."
        ]
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T13:24+08:00",
  "model_id": "tencent/hy4-preview",
  "new_records": 6,
  "overall_status": "待复核"
}

-->
