# Trinity Large Thinking Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：arcee-ai/trinity-large-thinking
- 模型名称：Trinity Large Thinking
- 发布日期：2026-04-01
- 最近检查时间：2026-11-05T10:13+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- Exact identity is Arcee AI Trinity Large Thinking, released on 2026-04-01; it is the text-only Thinking checkpoint, distinct from Trinity Large Preview and TrueBase.
- Artificial Analysis directly reports Humanity’s Last Exam 16%, GDPval-AA v2.1 336 Elo, and Terminal-Bench 4.0 1% for Trinity Large Thinking. No evaluation publication dates were exposed, so no date fields were added.
- Artificial Analysis AutomationBench-AA reports a result on a private 657-task split of Zapier AutomationBench v1.0.6, but its objective-completion/guardrail metric differs from the target definition task_completed_correctly; it is not recorded as the target AutomationBench score.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Arcee Trinity Large Thinking model card](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) | 2026-11-05T10:13+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Arcee Trinity Large Thinking announcement](https://www.arcee.ai/blog/trinity-large-thinking), [Arcee open-source model catalog](https://www.arcee.ai/open-source-catalog), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T10:13+08:00 |
| terminal-bench-v4 | 已收录 | 1% (metric=task resolution rate; version=4.0; dataset=Terminal-Bench 4.0 (66 tasks; average of three repeats per task); harness=mini-swe-agent) | [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive), [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Terminal-Bench official version and leaderboard page](https://www.tbench.ai/benchmarks) | 2026-11-05T10:13+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks), [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Arcee Trinity Large Thinking technical report](https://arxiv.org/html/2602.17004) | 2026-11-05T10:13+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard and official metric](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive) | 2026-11-05T10:13+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Arcee Trinity Large Thinking model card](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) | 2026-11-05T10:13+08:00 |
| chartography | 不适用 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Arcee Trinity Large Thinking model card](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) | 2026-11-05T10:13+08:00 |
| humanitys-last-exam | 已收录 | 16% (metric=accuracy; dataset=2,158 text-only questions from the original HLE dataset (Artificial Analysis evaluation)) | [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:13+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis current Trinity profile](https://artificialanalysis.ai/models/trinity-large-thinking), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive) | 2026-11-05T10:13+08:00 |
| gdpval-aa-v2.1 | 已收录 | 336 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; harness=Stirrup with shell and web tools) | [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive), [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T10:13+08:00 |
| vals-index-v2.2 | 待核实 | — | [Trinity Large Thinking Vals AI model page](https://www.vals.ai/models/arcee-ai_trinity-large-thinking), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T10:13+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Arcee Trinity Large Thinking model card](https://huggingface.co/arcee-ai/Trinity-Large-Thinking)

研究备注：
- The exact Thinking checkpoint was not found in the visible leaderboard/JSON data; the published leaderboard view is incomplete.

尚未解决的问题：
- No exact DeepSWE v1.1 score for Trinity Large Thinking was verified.

最近核验时间：2026-11-05T10:13+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Arcee Trinity Large Thinking announcement](https://www.arcee.ai/blog/trinity-large-thinking)
- [Arcee open-source model catalog](https://www.arcee.ai/open-source-catalog)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Arcee materials report SWE-bench Verified, not SWE-bench Pro V2. No exact Trinity Large Thinking V2 score was verified on the Scale leaderboard.

尚未解决的问题：
- No exact SWE-bench Pro V2 result was verified.

最近核验时间：2026-11-05T10:13+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 1%
- metric: task resolution rate
- version: 4.0
- dataset: Terminal-Bench 4.0 (66 tasks; average of three repeats per task)
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)
- [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Terminal-Bench official version and leaderboard page](https://www.tbench.ai/benchmarks)

研究备注：
- The exact comparison row reports Terminal-Bench 4.0 at 1%. Artificial Analysis states it evaluated all 66 v4.0 tasks using mini-swe-agent, pass@1 averaged over three repeats per task. The source does not publish an evaluation date.

最近核验时间：2026-11-05T10:13+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks)
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Arcee Trinity Large Thinking technical report](https://arxiv.org/html/2602.17004)

研究备注：
- The leaderboard/report sources checked did not provide an exact Terminal-Bench-Science 0.1.0 result for this checkpoint.

尚未解决的问题：
- No exact Terminal-Bench-Science 0.1.0 result was verified.

最近核验时间：2026-11-05T10:13+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard and official metric](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)

研究备注：
- Artificial Analysis reports AutomationBench-AA 1% for this model on a private 657-task held-out split from dataset v1.0.6, but its headline metric credits partial objective completion unless a guardrail is violated; Zapier target metric requires every scored assertion to pass. The exact Zapier leaderboard row remains unverifiable, so the AA-specific value is not mapped as this target score.

尚未解决的问题：
- Verify whether Trinity Large Thinking has a Zapier AutomationBench v1.0.6 task_completed_correctly score.

最近核验时间：2026-11-05T10:13+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Arcee Trinity Large Thinking model card](https://huggingface.co/arcee-ai/Trinity-Large-Thinking)

研究备注：
- The checkpoint accepts text only and cannot consume the screenshots required for standard OSWorld desktop tasks.

最近核验时间：2026-11-05T10:13+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Arcee Trinity Large Thinking model card](https://huggingface.co/arcee-ai/Trinity-Large-Thinking)

研究备注：
- Chartography requires visual chart input; this text-only checkpoint cannot receive chart images.

最近核验时间：2026-11-05T10:13+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 16%
- metric: accuracy
- dataset: 2,158 text-only questions from the original HLE dataset (Artificial Analysis evaluation)
- source: [https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The direct comparison reports 16% for the exact Trinity Large Thinking checkpoint. Artificial Analysis uses 2,158 text-only questions from the original HLE set, scored pass@1 with the original HLE equality-checker prompt and GPT-5.6 Luna (medium). This is not HLE-Diamond; no evaluation date is published.

最近核验时间：2026-11-05T10:13+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis current Trinity profile](https://artificialanalysis.ai/models/trinity-large-thinking)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)

研究备注：
- The exact profile summary is N/A for current Intelligence Index v5.0.1. The 11 shown on the comparison page is part of v4.3.2, which is not the V5 score.

最近核验时间：2026-11-05T10:13+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 336
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- harness: Stirrup with shell and web tools
- source: [https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis direct comparison](https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive)
- [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis GDPval-AA v2.1 page](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The direct comparison reports 336 Elo for Trinity Large Thinking on GDPval-AA v2.1. Methodology specifies 220 tasks, Stirrup with an E2B sandbox and shell/web tools, blind pairwise judging and Elo anchored to DeepSeek V4.1 Flash (max)=1600. No effort setting or evaluation date is published.

最近核验时间：2026-11-05T10:13+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Trinity Large Thinking Vals AI model page](https://www.vals.ai/models/arcee-ai_trinity-large-thinking)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals lists an April 4, 2026 score of 42.6% but does not identify it as V2.2; the current model page only shows Terminal-Bench 2.0. The V2.2 leaderboard shows only each lab’s best model, so omission is not proof that Trinity was not measured.

尚未解决的问题：
- No exact Vals Index v2.2 score was verified.

最近核验时间：2026-11-05T10:13+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis current Trinity profile",
          "url": "https://artificialanalysis.ai/models/trinity-large-thinking"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive"
        }
      ],
      "notes": [
        "The exact profile summary is N/A for current Intelligence Index v5.0.1. The 11 shown on the comparison page is part of v4.3.2, which is not the V5 score."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard and official metric",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive"
        }
      ],
      "notes": [
        "Artificial Analysis reports AutomationBench-AA 1% for this model on a private 657-task held-out split from dataset v1.0.6, but its headline metric credits partial objective completion unless a guardrail is violated; Zapier target metric requires every scored assertion to pass. The exact Zapier leaderboard row remains unverifiable, so the AA-specific value is not mapped as this target score."
      ],
      "status": "待核实",
      "unresolved": [
        "Verify whether Trinity Large Thinking has a Zapier AutomationBench v1.0.6 task_completed_correctly score."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography public leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Arcee Trinity Large Thinking model card",
          "url": "https://huggingface.co/arcee-ai/Trinity-Large-Thinking"
        }
      ],
      "notes": [
        "Chartography requires visual chart input; this text-only checkpoint cannot receive chart images."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard data",
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "label": "Arcee Trinity Large Thinking model card",
          "url": "https://huggingface.co/arcee-ai/Trinity-Large-Thinking"
        }
      ],
      "notes": [
        "The exact Thinking checkpoint was not found in the visible leaderboard/JSON data; the published leaderboard view is incomplete."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 score for Trinity Large Thinking was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The direct comparison reports 336 Elo for Trinity Large Thinking on GDPval-AA v2.1. Methodology specifies 220 tasks, Stirrup with an E2B sandbox and shell/web tools, blind pairwise judging and Elo anchored to DeepSeek V4.1 Flash (max)=1600. No effort setting or evaluation date is published."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The direct comparison reports 16% for the exact Trinity Large Thinking checkpoint. Artificial Analysis uses 2,158 text-only questions from the original HLE set, scored pass@1 with the original HLE equality-checker prompt and GPT-5.6 Luna (medium). This is not HLE-Diamond; no evaluation date is published."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Arcee Trinity Large Thinking model card",
          "url": "https://huggingface.co/arcee-ai/Trinity-Large-Thinking"
        }
      ],
      "notes": [
        "The checkpoint accepts text only and cannot consume the screenshots required for standard OSWorld desktop tasks."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Arcee Trinity Large Thinking announcement",
          "url": "https://www.arcee.ai/blog/trinity-large-thinking"
        },
        {
          "label": "Arcee open-source model catalog",
          "url": "https://www.arcee.ai/open-source-catalog"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Arcee materials report SWE-bench Verified, not SWE-bench Pro V2. No exact Trinity Large Thinking V2 score was verified on the Scale leaderboard."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact SWE-bench Pro V2 result was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Snorkel Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "label": "Arcee Trinity Large Thinking technical report",
          "url": "https://arxiv.org/html/2602.17004"
        }
      ],
      "notes": [
        "The leaderboard/report sources checked did not provide an exact Terminal-Bench-Science 0.1.0 result for this checkpoint."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Terminal-Bench-Science 0.1.0 result was verified."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/trinity-large-thinking-vs-claude-sonnet-4-6-adaptive"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Terminal-Bench official version and leaderboard page",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "The exact comparison row reports Terminal-Bench 4.0 at 1%. Artificial Analysis states it evaluated all 66 v4.0 tasks using mini-swe-agent, pass@1 averaged over three repeats per task. The source does not publish an evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T10:13+08:00",
      "checked_sources": [
        {
          "label": "Trinity Large Thinking Vals AI model page",
          "url": "https://www.vals.ai/models/arcee-ai_trinity-large-thinking"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals lists an April 4, 2026 score of 42.6% but does not identify it as V2.2; the current model page only shows Terminal-Bench 2.0. The V2.2 leaderboard shows only each lab’s best model, so omission is not proof that Trinity was not measured."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Vals Index v2.2 score was verified."
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:13+08:00",
  "model_id": "arcee-ai/trinity-large-thinking",
  "model_notes": [
    "Exact identity is Arcee AI Trinity Large Thinking, released on 2026-04-01; it is the text-only Thinking checkpoint, distinct from Trinity Large Preview and TrueBase.",
    "Artificial Analysis directly reports Humanity’s Last Exam 16%, GDPval-AA v2.1 336 Elo, and Terminal-Bench 4.0 1% for Trinity Large Thinking. No evaluation publication dates were exposed, so no date fields were added.",
    "Artificial Analysis AutomationBench-AA reports a result on a private 657-task split of Zapier AutomationBench v1.0.6, but its objective-completion/guardrail metric differs from the target definition task_completed_correctly; it is not recorded as the target AutomationBench score."
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
