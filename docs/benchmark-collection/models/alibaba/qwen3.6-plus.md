# Qwen3.6 Plus Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.6-plus
- 模型名称：Qwen3.6 Plus
- 发布日期：2026-04-02
- 最近检查时间：2026-11-05T10:00+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- Alibaba’s official model documentation identifies the snapshot qwen3.6-plus-2026-04-02; this is the exact hosted Qwen3.6 Plus model in the local TOML.
- The HLE row is Artificial Analysis’s 28% accuracy result on 2,158 text-only questions from the original HLE set. It is retained with the subset identified and should not be compared as if it covered all 2,500 questions.
- No evaluation publication date was verified for the added HLE score; no benchmark date was added.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus) | 2026-11-05T10:00+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Alibaba Qwen3.6 Plus official release and benchmark notes](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603005), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T10:00+08:00 |
| terminal-bench-v4 | 待核实 | — | [Alibaba Qwen3.6 Plus official release and benchmark notes](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603005), [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks) | 2026-11-05T10:00+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks), [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/) | 2026-11-05T10:00+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench), [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus) | 2026-11-05T10:00+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Current OSWorld-V2 leaderboard page](https://osworld-v2.xlang.ai/), [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus) | 2026-11-05T10:00+08:00 |
| chartography | 未找到 | — | [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository](https://github.com/surge-ai/chartography), [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus) | 2026-11-05T10:00+08:00 |
| humanitys-last-exam | 已收录 | 28% (metric=accuracy; dataset=2,158 text-only questions from the original HLE dataset (Artificial Analysis evaluation)) | [Artificial Analysis Qwen3.6 Plus direct comparison](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:00+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis current Qwen3.6 Plus profile](https://artificialanalysis.ai/models/qwen3-6-plus), [Artificial Analysis Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:00+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis comparison reporting Qwen3.6 Plus at 990 Elo](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview), [Artificial Analysis comparison page checked for the 989 Elo value](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-step-3-5-flash-0202), [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T10:00+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals AI current Qwen3.6 Plus model profile](https://www.vals.ai/models/alibaba_qwen3.6-plus), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T10:00+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 official leaderboard data](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus)

研究备注：
- The official live leaderboard and its JSON did not provide a directly verified row for the exact qwen3.6-plus-2026-04-02 snapshot. The current data covers only a subset of models/configurations, so absence is not proof of no score.

尚未解决的问题：
- No exact DeepSWE v1.1 score for this snapshot was verified.

最近核验时间：2026-11-05T10:00+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Alibaba Qwen3.6 Plus official release and benchmark notes](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603005)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Alibaba reports a refined SWE-Bench Pro evaluation, without identifying it as the target V2 suite. The release notes do not establish that the reported result uses the 642-task V2 dataset.
- The Scale V2 leaderboard was checked for the exact snapshot; no directly verified result row was obtained.

尚未解决的问题：
- No exact Qwen3.6 Plus score on SWE-bench Pro V2 was verified.

最近核验时间：2026-11-05T10:00+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Alibaba Qwen3.6 Plus official release and benchmark notes](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603005)
- [Terminal-Bench official versions and leaderboard](https://www.tbench.ai/benchmarks)

研究备注：
- Alibaba’s report specifies Terminal-Bench 2.0, Harbor/Terminus-2, a three-hour limit, and an average over five runs. This is not Terminal-Bench 4.0.
- The official v4.0 benchmark page was checked; no exact Qwen3.6 Plus v4 score was verified.

尚未解决的问题：
- Only a Terminal-Bench 2.0 result is reported in the release material; no v4 score was verified.

最近核验时间：2026-11-05T10:00+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science official versions](https://www.tbench.ai/benchmarks)
- [Snorkel Terminal-Bench Science leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)

研究备注：
- The target benchmark was released after the exact Qwen3.6 Plus snapshot. The current leaderboard is dynamic and does not expose a complete result set, so absence from its visible material is not conclusive.

尚未解决的问题：
- No exact score was verified; the public leaderboard is dynamic and incomplete.

最近核验时间：2026-11-05T10:00+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus)

研究备注：
- The exact model supports function calling and is applicable. The official v1.0.6 leaderboard folds 119 results after the visible top ten; the exact model row could not be confirmed.

尚未解决的问题：
- A folded leaderboard prevents confirming whether this exact model has a public result.

最近核验时间：2026-11-05T10:00+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Current OSWorld-V2 leaderboard page](https://osworld-v2.xlang.ai/)
- [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus)

研究备注：
- The model accepts image/video inputs, returns text, and supports function calling, so OSWorld is applicable. The v2.1 release notes and current page checked did not provide a score for the exact snapshot; the current project page is labeled v2.0.

尚未解决的问题：
- No exact OSWorld 2.1 score was verified.

最近核验时间：2026-11-05T10:00+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography public leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository](https://github.com/surge-ai/chartography)
- [Qwen3.6 Plus official model documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus)

研究备注：
- The model is multimodal and applicable. The current visible leaderboard snapshot lists other Qwen versions (including Qwen 3.5 Plus and Qwen 3.7 Plus) but not the exact Qwen3.6 Plus snapshot; no adjacent-version score was reused.

最近核验时间：2026-11-05T10:00+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 28%
- metric: accuracy
- dataset: 2,158 text-only questions from the original HLE dataset (Artificial Analysis evaluation)
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.6 Plus direct comparison](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis directly reports 28% for the exact Qwen3.6 Plus model. Its methodology uses 2,158 text-only questions from the original full HLE dataset and pass@1 scoring; the dataset subset is recorded in the TOML.
- This result is not the full 2,500-question multimodal set, so it is not directly comparable with full-set scores.

尚未解决的问题：
- Only the 2,158-question text-only subset was evaluated in this result; full 2,500-question performance is not established.

最近核验时间：2026-11-05T10:00+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis current Qwen3.6 Plus profile](https://artificialanalysis.ai/models/qwen3-6-plus)
- [Artificial Analysis Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current exact-model profile displays N/A for the Intelligence Index. A legacy estimated index score (27*) is not an Intelligence Index V5 result.

最近核验时间：2026-11-05T10:00+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis comparison reporting Qwen3.6 Plus at 990 Elo](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview)
- [Artificial Analysis comparison page checked for the 989 Elo value](https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-step-3-5-flash-0202)
- [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Research found 990 and 989 Elo values for the exact model on Artificial Analysis comparison-page snapshots. The values are not accompanied by evaluation dates or conditions that explain the difference; no value was chosen or written.
- GDPval-AA v2.1 is a separate result from the older GDPval-AA v2 score of 1066; that v2 value is not treated as a v2.1 result.

尚未解决的问题：
- The 989 vs 990 Elo difference remains unresolved; a direct, dated leaderboard entry is needed before writing a score.

最近核验时间：2026-11-05T10:00+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals AI current Qwen3.6 Plus model profile](https://www.vals.ai/models/alibaba_qwen3.6-plus)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The model profile reports a Vals Index aggregate of 52.13%, but does not specify the index version. The current v2.2 leaderboard shows latest/top/frontier models and does not include this model; absence there is not proof the model was not evaluated.

尚未解决的问题：
- Version mapping for the profile’s 52.13% remains unverified; no v2.2 score was added.

最近核验时间：2026-11-05T10:00+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis current Qwen3.6 Plus profile",
          "url": "https://artificialanalysis.ai/models/qwen3-6-plus"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current exact-model profile displays N/A for the Intelligence Index. A legacy estimated index score (27*) is not an Intelligence Index V5 result."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Qwen3.6 Plus official model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus"
        }
      ],
      "notes": [
        "The exact model supports function calling and is applicable. The official v1.0.6 leaderboard folds 119 results after the visible top ten; the exact model row could not be confirmed."
      ],
      "status": "待核实",
      "unresolved": [
        "A folded leaderboard prevents confirming whether this exact model has a public result."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T10:00+08:00",
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
          "label": "Qwen3.6 Plus official model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus"
        }
      ],
      "notes": [
        "The model is multimodal and applicable. The current visible leaderboard snapshot lists other Qwen versions (including Qwen 3.5 Plus and Qwen 3.7 Plus) but not the exact Qwen3.6 Plus snapshot; no adjacent-version score was reused."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T10:00+08:00",
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
          "label": "Qwen3.6 Plus official model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus"
        }
      ],
      "notes": [
        "The official live leaderboard and its JSON did not provide a directly verified row for the exact qwen3.6-plus-2026-04-02 snapshot. The current data covers only a subset of models/configurations, so absence is not proof of no score."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact DeepSWE v1.1 score for this snapshot was verified."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison reporting Qwen3.6 Plus at 990 Elo",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis comparison page checked for the 989 Elo value",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-step-3-5-flash-0202"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Research found 990 and 989 Elo values for the exact model on Artificial Analysis comparison-page snapshots. The values are not accompanied by evaluation dates or conditions that explain the difference; no value was chosen or written.",
        "GDPval-AA v2.1 is a separate result from the older GDPval-AA v2 score of 1066; that v2 value is not treated as a v2.1 result."
      ],
      "status": "冲突",
      "unresolved": [
        "The 989 vs 990 Elo difference remains unresolved; a direct, dated leaderboard entry is needed before writing a score."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.6 Plus direct comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-6-plus-vs-gemini-3-1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis directly reports 28% for the exact Qwen3.6 Plus model. Its methodology uses 2,158 text-only questions from the original full HLE dataset and pass@1 scoring; the dataset subset is recorded in the TOML.",
        "This result is not the full 2,500-question multimodal set, so it is not directly comparable with full-set scores."
      ],
      "status": "已收录",
      "unresolved": [
        "Only the 2,158-question text-only subset was evaluated in this result; full 2,500-question performance is not established."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Current OSWorld-V2 leaderboard page",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Qwen3.6 Plus official model documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-plus"
        }
      ],
      "notes": [
        "The model accepts image/video inputs, returns text, and supports function calling, so OSWorld is applicable. The v2.1 release notes and current page checked did not provide a score for the exact snapshot; the current project page is labeled v2.0."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact OSWorld 2.1 score was verified."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Qwen3.6 Plus official release and benchmark notes",
          "url": "https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603005"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Alibaba reports a refined SWE-Bench Pro evaluation, without identifying it as the target V2 suite. The release notes do not establish that the reported result uses the 642-task V2 dataset.",
        "The Scale V2 leaderboard was checked for the exact snapshot; no directly verified result row was obtained."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Qwen3.6 Plus score on SWE-bench Pro V2 was verified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science official versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Snorkel Terminal-Bench Science leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        }
      ],
      "notes": [
        "The target benchmark was released after the exact Qwen3.6 Plus snapshot. The current leaderboard is dynamic and does not expose a complete result set, so absence from its visible material is not conclusive."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact score was verified; the public leaderboard is dynamic and incomplete."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Qwen3.6 Plus official release and benchmark notes",
          "url": "https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-6-plus-to-accelerate-agentic-ai-deployment-for-enterprises-and-alibaba%E2%80%99s-ai-applications_603005"
        },
        {
          "label": "Terminal-Bench official versions and leaderboard",
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "Alibaba’s report specifies Terminal-Bench 2.0, Harbor/Terminus-2, a three-hour limit, and an average over five runs. This is not Terminal-Bench 4.0.",
        "The official v4.0 benchmark page was checked; no exact Qwen3.6 Plus v4 score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "Only a Terminal-Bench 2.0 result is reported in the release material; no v4 score was verified."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T10:00+08:00",
      "checked_sources": [
        {
          "label": "Vals AI current Qwen3.6 Plus model profile",
          "url": "https://www.vals.ai/models/alibaba_qwen3.6-plus"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The model profile reports a Vals Index aggregate of 52.13%, but does not specify the index version. The current v2.2 leaderboard shows latest/top/frontier models and does not include this model; absence there is not proof the model was not evaluated."
      ],
      "status": "待核实",
      "unresolved": [
        "Version mapping for the profile’s 52.13% remains unverified; no v2.2 score was added."
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:00+08:00",
  "model_id": "alibaba/qwen3.6-plus",
  "model_notes": [
    "Alibaba’s official model documentation identifies the snapshot qwen3.6-plus-2026-04-02; this is the exact hosted Qwen3.6 Plus model in the local TOML.",
    "The HLE row is Artificial Analysis’s 28% accuracy result on 2,158 text-only questions from the original HLE set. It is retained with the subset identified and should not be compared as if it covered all 2,500 questions.",
    "No evaluation publication date was verified for the added HLE score; no benchmark date was added."
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
