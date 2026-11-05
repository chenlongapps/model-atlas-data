# GLM-5.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：zhipuai/glm-5.1
- 模型名称：GLM-5.1
- 发布日期：2026-04-07
- 最近检查时间：2026-11-05T09:48+08:00
- 整体处理状态：待复核
- 新增成绩数量：5
- 更新成绩数量：0
- 收集前已有成绩数量：4
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- GLM-5.1 is the exact model name shown on Z.ai’s official Hugging Face model card and Artificial Analysis comparison page.
- Vals AI’s current GLM-5.1 profile shows an aggregate 56.33% but does not identify the Vals Index version; it was not mapped to v2.2.
- The Vals profile lists a release date of April 1, while this model TOML records April 7. The profile date was not used to change the release metadata.

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 18% ±1% (metric=pass@1; version=1.1; dataset=113 tasks; harness=mini-swe-agent) | [Archived official DeepSWE v1.1 leaderboard snapshot](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology and leaderboard description](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T09:48+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Z.ai official GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T09:48+08:00 |
| terminal-bench-v4 | 已收录 | 65.1 (metric=pass@1; version=2.1; harness=Claude Code); 2% (metric=task resolution rate; version=4.0; dataset=Terminal-Bench 4.0 (66 tasks); harness=mini-swe-agent; Artificial Analysis evaluation) | [Artificial Analysis direct GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini), [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:48+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science v0.1.0 release](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0), [Artificial Analysis benchmark methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:48+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench), [Artificial Analysis comparison page (AutomationBench-AA variant)](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini) | 2026-11-05T09:48+08:00 |
| osworld-v2.1 | 不适用 | — | [Z.ai official GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1), [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T09:48+08:00 |
| chartography | 不适用 | — | [Artificial Analysis GLM-5.1 model profile](https://artificialanalysis.ai/models/glm-5-1), [Chartography benchmark repository](https://github.com/surge-ai/chartography) | 2026-11-05T09:48+08:00 |
| humanitys-last-exam | 待核实 | 31.0 (variant=Z.ai model card; HLE without tools); 52.3 (variant=Z.ai model card; HLE with tools) | [Z.ai official GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:48+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis current GLM-5.1 profile](https://artificialanalysis.ai/models/glm-5-1), [Artificial Analysis Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:48+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1103 (metric=Elo rating; version=2.1; dataset=GDPval-AA v2.1 (220 tasks; 44 occupations); variant=Reasoning; harness=Artificial Analysis Stirrup; E2B sandbox with web fetch, web search, code execution, and file output tools) | [Artificial Analysis direct GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini), [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:48+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals AI current GLM-5.1 profile](https://www.vals.ai/models/zai_glm-5.1), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T09:48+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 18% ±1%
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- harness: mini-swe-agent
- source: [https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Archived official DeepSWE v1.1 leaderboard snapshot](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology and leaderboard description](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- The archived leaderboard lists the exact glm-5.1 entry at 18% ±1%; its display is a leaderboard snapshot, not an evaluation date.
- The v1.1 benchmark is 113 tasks and uses pass@1; the leaderboard describes mini-swe-agent. No effort level or run date was confirmed.

最近核验时间：2026-11-05T09:48+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Z.ai official GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- The Z.ai model card reports SWE-Bench Pro 58.4 without a V2 label. The local 19.8 hard-aa row is another evaluation split. Neither maps to the target Pro V2 result.
- The V2 leaderboard defines a distinct 642-task suite; no exact GLM-5.1 V2 score was verified.

尚未解决的问题：
- An exact GLM-5.1 score for the 642-task SWE-bench Pro V2 suite remains unverified.

最近核验时间：2026-11-05T09:48+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 65.1
- metric: pass@1
- version: 2.1
- harness: Claude Code
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 2%
- metric: task resolution rate
- version: 4.0
- dataset: Terminal-Bench 4.0 (66 tasks)
- harness: mini-swe-agent; Artificial Analysis evaluation
- source: [https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis direct GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini)
- [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The comparison page explicitly reports 2% for Terminal-Bench 4.0 for GLM-5.1 (Reasoning). This is separate from the local 65.1 score for version 2.1.
- Artificial Analysis documents 66 tasks, mini-swe-agent, and pass@1 averaged over three repeats; the source row is stored with the repository definition’s task-resolution-rate metric.

最近核验时间：2026-11-05T09:48+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science v0.1.0 release](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)
- [Artificial Analysis benchmark methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Checked the v0.1.0 release materials and the current Artificial Analysis evaluation profile; no exact GLM-5.1 result was found in the material inspected.
- The current AA GLM-5.1 profile has no public Intelligence Index aggregate. Dynamic leaderboard omissions do not establish that no public score exists.

尚未解决的问题：
- No exact score confirmed; the public science leaderboard is dynamic and its visible material may be incomplete.

最近核验时间：2026-11-05T09:48+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis comparison page (AutomationBench-AA variant)](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini)

研究备注：
- Artificial Analysis reports 20% for its AutomationBench-AA variant, which is not enough to establish a score on the target official AutomationBench v1.0.6 setup.
- The official leaderboard folds most rows after the visible top ten, so GLM-5.1 absence from the visible portion cannot be treated as no result.

尚未解决的问题：
- The AA variant’s 20% is not mapped to AutomationBench v1.0.6; the exact official result remains unverified.

最近核验时间：2026-11-05T09:48+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Z.ai official GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1)
- [OSWorld-V2 v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- The model card exposes text input and text output only; OSWorld 2.1 requires visual desktop interaction.

最近核验时间：2026-11-05T09:48+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GLM-5.1 model profile](https://artificialanalysis.ai/models/glm-5-1)
- [Chartography benchmark repository](https://github.com/surge-ai/chartography)

研究备注：
- The exact GLM-5.1 profile supports text input only. It cannot read chart images for the target chart-understanding benchmark.

最近核验时间：2026-11-05T09:48+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 31.0
- variant: Z.ai model card; HLE without tools
- source: [https://huggingface.co/zai-org/GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 52.3
- variant: Z.ai model card; HLE with tools
- source: [https://huggingface.co/zai-org/GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Z.ai official GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The Z.ai model card reports 31.0 for HLE and 52.3 for HLE with tools; both raw values were retained without inventing metric, dataset subset, version, or tool setup details.
- Artificial Analysis separately reports 30% on its 2,158-question text-only HLE evaluation. This does not establish a result for the repository target’s original 2,500-question set and was not added as a target score.

尚未解决的问题：
- The model card does not state scoring metric, exact HLE subset, evaluation conditions, or run date for its two HLE values.

最近核验时间：2026-11-05T09:48+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis current GLM-5.1 profile](https://artificialanalysis.ai/models/glm-5-1)
- [Artificial Analysis Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current exact-model profile displays N/A for the Intelligence Index. The comparison page’s 26 belongs to legacy v4.3.2 and cannot be mapped to V5.

最近核验时间：2026-11-05T09:48+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1103
- metric: Elo rating
- version: 2.1
- dataset: GDPval-AA v2.1 (220 tasks; 44 occupations)
- variant: Reasoning
- harness: Artificial Analysis Stirrup; E2B sandbox with web fetch, web search, code execution, and file output tools
- source: [https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis direct GLM-5.1 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini)
- [Artificial Analysis GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The comparison page explicitly lists GLM-5.1 (Reasoning) at 1103 Elo on GDPval-AA v2.1. No evaluation date is stated.
- Methodology specifies 220 tasks across 44 occupations and the Stirrup harness in an E2B sandbox with web and code/file tools.
- Alternative 1116/1117 values appeared only in unverified cached extracts; they were not found in the direct comparison page and were not used.

最近核验时间：2026-11-05T09:48+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals AI current GLM-5.1 profile](https://www.vals.ai/models/zai_glm-5.1)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The model profile displays 56.33% under Vals Index but does not identify the index version. The current leaderboard is v2.2 and only shows latest, top, and frontier models; absence there is not proof that the profile score is v2.2.

尚未解决的问题：
- Exact version mapping for the profile’s 56.33% remains unverified; no v2.2 score was added.

最近核验时间：2026-11-05T09:48+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis current GLM-5.1 profile",
          "url": "https://artificialanalysis.ai/models/glm-5-1"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current exact-model profile displays N/A for the Intelligence Index. The comparison page’s 26 belongs to legacy v4.3.2 and cannot be mapped to V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T09:48+08:00",
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
          "label": "Artificial Analysis comparison page (AutomationBench-AA variant)",
          "url": "https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini"
        }
      ],
      "notes": [
        "Artificial Analysis reports 20% for its AutomationBench-AA variant, which is not enough to establish a score on the target official AutomationBench v1.0.6 setup.",
        "The official leaderboard folds most rows after the visible top ten, so GLM-5.1 absence from the visible portion cannot be treated as no result."
      ],
      "status": "待核实",
      "unresolved": [
        "The AA variant’s 20% is not mapped to AutomationBench v1.0.6; the exact official result remains unverified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GLM-5.1 model profile",
          "url": "https://artificialanalysis.ai/models/glm-5-1"
        },
        {
          "label": "Chartography benchmark repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "The exact GLM-5.1 profile supports text input only. It cannot read chart images for the target chart-understanding benchmark."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Archived official DeepSWE v1.1 leaderboard snapshot",
          "url": "https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology and leaderboard description",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "The archived leaderboard lists the exact glm-5.1 entry at 18% ±1%; its display is a leaderboard snapshot, not an evaluation date.",
        "The v1.1 benchmark is 113 tasks and uses pass@1; the leaderboard describes mini-swe-agent. No effort level or run date was confirmed."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct GLM-5.1 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The comparison page explicitly lists GLM-5.1 (Reasoning) at 1103 Elo on GDPval-AA v2.1. No evaluation date is stated.",
        "Methodology specifies 220 tasks across 44 occupations and the Stirrup harness in an E2B sandbox with web and code/file tools.",
        "Alternative 1116/1117 values appeared only in unverified cached extracts; they were not found in the direct comparison page and were not used."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Z.ai official GLM-5.1 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.1"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The Z.ai model card reports 31.0 for HLE and 52.3 for HLE with tools; both raw values were retained without inventing metric, dataset subset, version, or tool setup details.",
        "Artificial Analysis separately reports 30% on its 2,158-question text-only HLE evaluation. This does not establish a result for the repository target’s original 2,500-question set and was not added as a target score."
      ],
      "status": "待核实",
      "unresolved": [
        "The model card does not state scoring metric, exact HLE subset, evaluation conditions, or run date for its two HLE values."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Z.ai official GLM-5.1 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.1"
        },
        {
          "label": "OSWorld-V2 v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "The model card exposes text input and text output only; OSWorld 2.1 requires visual desktop interaction."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Z.ai official GLM-5.1 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.1"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "The Z.ai model card reports SWE-Bench Pro 58.4 without a V2 label. The local 19.8 hard-aa row is another evaluation split. Neither maps to the target Pro V2 result.",
        "The V2 leaderboard defines a distinct 642-task suite; no exact GLM-5.1 V2 score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "An exact GLM-5.1 score for the 642-task SWE-bench Pro V2 suite remains unverified."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science v0.1.0 release",
          "url": "https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0"
        },
        {
          "label": "Artificial Analysis benchmark methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Checked the v0.1.0 release materials and the current Artificial Analysis evaluation profile; no exact GLM-5.1 result was found in the material inspected.",
        "The current AA GLM-5.1 profile has no public Intelligence Index aggregate. Dynamic leaderboard omissions do not establish that no public score exists."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact score confirmed; the public science leaderboard is dynamic and its visible material may be incomplete."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis direct GLM-5.1 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/glm-5-1-vs-gpt-5-1-codex-mini"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The comparison page explicitly reports 2% for Terminal-Bench 4.0 for GLM-5.1 (Reasoning). This is separate from the local 65.1 score for version 2.1.",
        "Artificial Analysis documents 66 tasks, mini-swe-agent, and pass@1 averaged over three repeats; the source row is stored with the repository definition’s task-resolution-rate metric."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T09:48+08:00",
      "checked_sources": [
        {
          "label": "Vals AI current GLM-5.1 profile",
          "url": "https://www.vals.ai/models/zai_glm-5.1"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The model profile displays 56.33% under Vals Index but does not identify the index version. The current leaderboard is v2.2 and only shows latest, top, and frontier models; absence there is not proof that the profile score is v2.2."
      ],
      "status": "待核实",
      "unresolved": [
        "Exact version mapping for the profile’s 56.33% remains unverified; no v2.2 score was added."
      ]
    }
  },
  "existing_records": 4,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T09:48+08:00",
  "model_id": "zhipuai/glm-5.1",
  "model_notes": [
    "GLM-5.1 is the exact model name shown on Z.ai’s official Hugging Face model card and Artificial Analysis comparison page.",
    "Vals AI’s current GLM-5.1 profile shows an aggregate 56.33% but does not identify the Vals Index version; it was not mapped to v2.2.",
    "The Vals profile lists a release date of April 1, while this model TOML records April 7. The profile date was not used to change the release metadata."
  ],
  "new_records": 5,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
