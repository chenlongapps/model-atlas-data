# Qwen3.8 Flash Next Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-flash-next
- 模型名称：Qwen3.8 Flash Next
- 发布日期：2026-08-27
- 最近检查时间：2026-11-04T15:20+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 收集前已有成绩数量：27
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 58.7 (metric=score; version=1.1; harness=mini-swe-agent) | [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next), [DeepSWE v1.1 methodology and board](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T15:20+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next), [Scale SWE-bench Pro V2 methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T15:20+08:00 |
| terminal-bench-v4 | 待核实 | 25.25 (metric=pass@1; version=4.0; dataset=66 tasks; variant=mean over 3 repeats per task; 500-step cap; task timeout up to 8 hours; harness=mini-SWE-agent v2.4.6) | [Artificial Analysis Qwen3.8-Flash-Next model page](https://artificialanalysis.ai/models/qwen3-8-flash-next), [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Dated result index linking the AA row](https://unifybench.ai/efforts?model=qwen3.8-flash-next) | 2026-11-04T15:20+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next), [Terminal-Bench-Science official release](https://www.tbench.ai/news/terminal-bench-science-0-1), [Artificial Analysis evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Qwen model effort results checked for the AA source row](https://unifybench.ai/efforts?model=qwen3.8-flash-next) | 2026-11-04T15:20+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Zapier AutomationBench official page](https://zapier.com/benchmarks), [Artificial Analysis model page](https://artificialanalysis.ai/models/qwen3-8-flash-next), [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 2026-11-04T15:20+08:00 |
| osworld-v2.1 | 未找到 | 19.4 (metric=binary completion rate; version=2.0); 52.3 (metric=partial score; version=2.0) | [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2.1 methodology](https://arxiv.org/abs/2606.29537) | 2026-11-04T15:20+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography benchmark](https://surgehq.ai/benchmarks/chartography), [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 2026-11-04T15:20+08:00 |
| humanitys-last-exam | 待核实 | 35.9 (metric=score; variant=GPT-4o judge) | [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next), [Humanity’s Last Exam official benchmark](https://lastexam.ai/), [HLE paper](https://arxiv.org/abs/2501.14249) | 2026-11-04T15:20+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.8-Flash-Next model page](https://artificialanalysis.ai/models/qwen3-8-flash-next), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T15:20+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Dated result index showing the AA-linked observation](https://unifybench.ai/efforts?model=qwen3.8-flash-next), [Artificial Analysis model comparison snapshot](https://artificialanalysis.ai/models/comparisons/qwen3-8-flash-next-vs-step-3-7-flash) | 2026-11-04T15:20+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI Index leaderboard](https://www.vals.ai/benchmarks/vals_index), [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 2026-11-04T15:20+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 58.7
- metric: score
- version: 1.1
- harness: mini-swe-agent
- source: [https://huggingface.co/Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [DeepSWE v1.1 methodology and board](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Qwen reports 58.7 and says it evaluated Claude Code and mini-SWE-agent, reporting the higher result and identifying mini-SWE-agent as the stronger harness for this model.
- The model card does not name the metric; the repository definition requires pass@1, so the raw source metric=score remains unmapped pending confirmation. It does not publish a run date, dataset details, or effort setting.

尚未解决的问题：
- Confirm whether the provider-reported 58.7 is the benchmark definition’s pass@1 metric; do not infer it from the value alone.

最近核验时间：2026-11-04T15:20+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Scale SWE-bench Pro V2 methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- The existing 62.5 is the Qwen card’s SWE-bench Pro result on its refined/corrected task set with Claude Code; the card does not give an official Pro version, task count, or local task-resolution metric.
- Scale released V2 on 2026-09-22 with 642 tasks and a locked protocol, after the Qwen model card was published. Do not map the existing result to V2.

尚未解决的问题：
- No source ties the 62.5 result to SWE-bench Pro V2 (2.0.0); no exact-model score was found on the current V2 board.

最近核验时间：2026-11-04T15:20+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 25.25
- metric: pass@1
- version: 4.0
- dataset: 66 tasks
- variant: mean over 3 repeats per task; 500-step cap; task timeout up to 8 hours
- harness: mini-SWE-agent v2.4.6
- source: [https://artificialanalysis.ai/models/qwen3-8-flash-next](https://artificialanalysis.ai/models/qwen3-8-flash-next)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Qwen3.8-Flash-Next model page](https://artificialanalysis.ai/models/qwen3-8-flash-next)
- [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Dated result index linking the AA row](https://unifybench.ai/efforts?model=qwen3.8-flash-next)

研究备注：
- Added the independently evaluated 25.25% result. The AA method page specifies all 66 tasks, mini-SWE-agent, pass@1 averaged over three repeats. The linked row identifies mini-SWE-agent v2.4.6, a 500-step cap, and an eight-hour task timeout.
- The score source labels the run as reasoning mode but does not report a reasoning-effort budget; no effort value or evaluation date was added. The 2026-10-31 source-collection timestamp is not an evaluation date.
- The source uses version 4.0 and metric pass@1; the local definition expects 4.0.0 and task resolution rate. Preserve source labels and keep the mapping pending.

尚未解决的问题：
- Version and metric do not exactly match the local definition; keep the raw row and exclude it from exact-match coverage until reviewed.

最近核验时间：2026-11-04T15:20+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Terminal-Bench-Science official release](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Artificial Analysis evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Qwen model effort results checked for the AA source row](https://unifybench.ai/efforts?model=qwen3.8-flash-next)

研究备注：
- No exact-model score was found in the Qwen card or checked public evaluation pages. The UnifyBench family-removal value 42.3 (+0.3) is an index sensitivity change, not a Terminal-Bench-Science model score.

最近核验时间：2026-11-04T15:20+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Zapier AutomationBench official page](https://zapier.com/benchmarks)
- [Artificial Analysis model page](https://artificialanalysis.ai/models/qwen3-8-flash-next)
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)

研究备注：
- No exact-model result was found for Zapier AutomationBench v1.0.6. Artificial Analysis AutomationBench-AA is a separate evaluation with a different score definition; its 55.91% must not be mapped to Zapier task_completed_correctly.

最近核验时间：2026-11-04T15:20+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 19.4
- metric: binary completion rate
- version: 2.0
- source: [https://huggingface.co/Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: OSWorld
- score: 52.3
- metric: partial score
- version: 2.0
- source: [https://huggingface.co/Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2.1 methodology](https://arxiv.org/abs/2606.29537)

研究备注：
- The existing 19.4 binary completion and 52.3 partial scores are explicitly for OSWorld 2.0. No Qwen3.8-Flash-Next score for 2.1 was found; the earlier version rows remain unchanged.

最近核验时间：2026-11-04T15:20+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography benchmark](https://surgehq.ai/benchmarks/chartography)
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)

研究备注：
- No score for the exact Flash-Next model was found. Surge lists Qwen 3.8 Flash (xHigh), a distinct production model derived from Flash-Next with additional production features; its result was not transferred.

最近核验时间：2026-11-04T15:20+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 35.9
- metric: score
- variant: GPT-4o judge
- source: [https://huggingface.co/Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Humanity’s Last Exam official benchmark](https://lastexam.ai/)
- [HLE paper](https://arxiv.org/abs/2501.14249)

研究备注：
- The existing 35.9 provider-reported score and GPT-4o judge are confirmed by the Qwen model card. The card does not report the test-set variant or metric name. Removed the unsupported “without tools” condition; tool availability is not specified.

尚未解决的问题：
- Confirm whether the score refers to the original 2,500-question HLE set used by the local definition, rather than a different subset; metric=score remains distinct from the definition’s accuracy.

最近核验时间：2026-11-04T15:20+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.8-Flash-Next model page](https://artificialanalysis.ai/models/qwen3-8-flash-next)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current model page reports no Artificial Analysis Intelligence Index score (N/A; zero of four intelligence units available) and describes its current composite as v5.0.1. No score for the repository’s v5.0 definition was found. N/A is not recorded as zero.

最近核验时间：2026-11-04T15:20+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Dated result index showing the AA-linked observation](https://unifybench.ai/efforts?model=qwen3.8-flash-next)
- [Artificial Analysis model comparison snapshot](https://artificialanalysis.ai/models/comparisons/qwen3-8-flash-next-vs-step-3-7-flash)

研究备注：
- A 2026-10-31 UnifyBench snapshot reports an AA-linked GDPval-AA v2.1 result of 1,635.78 Elo for the exact model; an older AA comparison page rounds it to 1,637. The currently rendered official v2.1 leaderboard does not list Flash-Next (it lists the distinct Qwen3.8 27B model), so no score was added.

尚未解决的问题：
- Resolve the discrepancy between the dated third-party capture/older AA comparison and the current official leaderboard before recording an Elo result.

最近核验时间：2026-11-04T15:20+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Index leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Qwen official model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)

研究备注：
- No Qwen3.8-Flash-Next Vals Index v2.2 result was found. Results for other Qwen3.8 variants, including Max, were not transferred.

最近核验时间：2026-11-04T15:20+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8-Flash-Next model page",
          "url": "https://artificialanalysis.ai/models/qwen3-8-flash-next"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current model page reports no Artificial Analysis Intelligence Index score (N/A; zero of four intelligence units available) and describes its current composite as v5.0.1. No score for the repository’s v5.0 definition was found. N/A is not recorded as zero."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official page",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis model page",
          "url": "https://artificialanalysis.ai/models/qwen3-8-flash-next"
        },
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        }
      ],
      "notes": [
        "No exact-model result was found for Zapier AutomationBench v1.0.6. Artificial Analysis AutomationBench-AA is a separate evaluation with a different score definition; its 55.91% must not be mapped to Zapier task_completed_correctly."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        }
      ],
      "notes": [
        "No score for the exact Flash-Next model was found. Surge lists Qwen 3.8 Flash (xHigh), a distinct production model derived from Flash-Next with additional production features; its result was not transferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        },
        {
          "label": "DeepSWE v1.1 methodology and board",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Qwen reports 58.7 and says it evaluated Claude Code and mini-SWE-agent, reporting the higher result and identifying mini-SWE-agent as the stronger harness for this model.",
        "The model card does not name the metric; the repository definition requires pass@1, so the raw source metric=score remains unmapped pending confirmation. It does not publish a run date, dataset details, or effort setting."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm whether the provider-reported 58.7 is the benchmark definition’s pass@1 metric; do not infer it from the value alone."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Dated result index showing the AA-linked observation",
          "url": "https://unifybench.ai/efforts?model=qwen3.8-flash-next"
        },
        {
          "label": "Artificial Analysis model comparison snapshot",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-flash-next-vs-step-3-7-flash"
        }
      ],
      "notes": [
        "A 2026-10-31 UnifyBench snapshot reports an AA-linked GDPval-AA v2.1 result of 1,635.78 Elo for the exact model; an older AA comparison page rounds it to 1,637. The currently rendered official v2.1 leaderboard does not list Flash-Next (it lists the distinct Qwen3.8 27B model), so no score was added."
      ],
      "status": "待核实",
      "unresolved": [
        "Resolve the discrepancy between the dated third-party capture/older AA comparison and the current official leaderboard before recording an Elo result."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        },
        {
          "label": "Humanity’s Last Exam official benchmark",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "HLE paper",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "The existing 35.9 provider-reported score and GPT-4o judge are confirmed by the Qwen model card. The card does not report the test-set variant or metric name. Removed the unsupported “without tools” condition; tool availability is not specified."
      ],
      "status": "待核实",
      "unresolved": [
        "Confirm whether the score refers to the original 2,500-question HLE set used by the local definition, rather than a different subset; metric=score remains distinct from the definition’s accuracy."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2.1 methodology",
          "url": "https://arxiv.org/abs/2606.29537"
        }
      ],
      "notes": [
        "The existing 19.4 binary completion and 52.3 partial scores are explicitly for OSWorld 2.0. No Qwen3.8-Flash-Next score for 2.1 was found; the earlier version rows remain unchanged."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        },
        {
          "label": "Scale SWE-bench Pro V2 methodology",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "The existing 62.5 is the Qwen card’s SWE-bench Pro result on its refined/corrected task set with Claude Code; the card does not give an official Pro version, task count, or local task-resolution metric.",
        "Scale released V2 on 2026-09-22 with 642 tasks and a locked protocol, after the Qwen model card was published. Do not map the existing result to V2."
      ],
      "status": "待核实",
      "unresolved": [
        "No source ties the 62.5 result to SWE-bench Pro V2 (2.0.0); no exact-model score was found on the current V2 board."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        },
        {
          "label": "Terminal-Bench-Science official release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Artificial Analysis evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Qwen model effort results checked for the AA source row",
          "url": "https://unifybench.ai/efforts?model=qwen3.8-flash-next"
        }
      ],
      "notes": [
        "No exact-model score was found in the Qwen card or checked public evaluation pages. The UnifyBench family-removal value 42.3 (+0.3) is an index sensitivity change, not a Terminal-Bench-Science model score."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8-Flash-Next model page",
          "url": "https://artificialanalysis.ai/models/qwen3-8-flash-next"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Dated result index linking the AA row",
          "url": "https://unifybench.ai/efforts?model=qwen3.8-flash-next"
        }
      ],
      "notes": [
        "Added the independently evaluated 25.25% result. The AA method page specifies all 66 tasks, mini-SWE-agent, pass@1 averaged over three repeats. The linked row identifies mini-SWE-agent v2.4.6, a 500-step cap, and an eight-hour task timeout.",
        "The score source labels the run as reasoning mode but does not report a reasoning-effort budget; no effort value or evaluation date was added. The 2026-10-31 source-collection timestamp is not an evaluation date.",
        "The source uses version 4.0 and metric pass@1; the local definition expects 4.0.0 and task resolution rate. Preserve source labels and keep the mapping pending."
      ],
      "status": "待核实",
      "unresolved": [
        "Version and metric do not exactly match the local definition; keep the raw row and exclude it from exact-match coverage until reviewed."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T15:20+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Index leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Qwen official model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next"
        }
      ],
      "notes": [
        "No Qwen3.8-Flash-Next Vals Index v2.2 result was found. Results for other Qwen3.8 variants, including Max, were not transferred."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 27,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T15:20+08:00",
  "model_id": "alibaba/qwen3.8-flash-next",
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
