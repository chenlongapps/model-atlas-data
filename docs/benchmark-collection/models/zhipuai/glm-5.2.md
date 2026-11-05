# GLM-5.2 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：zhipuai/glm-5.2
- 模型名称：GLM-5.2
- 发布日期：2026-06-13
- 最近检查时间：2026-11-05T03:06+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：19
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 本轮增加一条 DeepSWE 1.1 原始公开行：44% ± 2%，metric 原文为 pass rate，effort=max，113 tasks，mini-swe-agent。由于本地定义要求 pass@1，而官方材料未能确认 GLM-5.2 每题的采样数/聚合是否等价，原始行保留在 TOML 但不计入 Benchmark 覆盖率。来源：https://deepswe.datacurve.ai/blog/deepswe-v1-1；https://deepswe.datacurve.ai/data/v1.1/trials；https://github.com/datacurve-ai/deep-swe#readme
- GLM-5.2 TOML release_date=2026-06-13；Z.ai 官方发布页日期为 2026-06-16。保留仓库日期，记录差异，不据此改日期或重排队列。来源：https://z.ai/blog/glm-5.2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 46.2 (metric=resolve rate); 44% ± 2% (metric=pass rate; version=1.1; dataset=113 tasks; effort=max; harness=mini-swe-agent) | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DeepSWE per-task trials](https://deepswe.datacurve.ai/data/v1.1/trials), [DeepSWE official README](https://github.com/datacurve-ai/deep-swe#readme) | 2026-11-05T03:06+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Z.ai GLM-5.2 release page](https://z.ai/blog/glm-5.2), [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md) | 2026-11-05T03:06+08:00 |
| terminal-bench-v4 | 待核实 | 82.7 (metric=success rate; version=2.1; harness=Claude Code); 81.0 (metric=success rate; version=2.1; harness=Terminus 2) | [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md) | 2026-11-05T03:06+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1), [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md) | 2026-11-05T03:06+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard v1.0.6](https://zapier.com/benchmarks), [Official AutomationBench repository README](https://github.com/zapier/AutomationBench), [Official AutomationBench changelog](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md), [Zapier leaderboard article](https://zapier.com/blog/ai-models-on-zapier/) | 2026-11-05T03:06+08:00 |
| osworld-v2.1 | 不适用 | — | [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md), [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official site](https://osworld-v2.xlang.ai/) | 2026-11-05T03:06+08:00 |
| chartography | 不适用 | — | [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md), [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T03:06+08:00 |
| humanitys-last-exam | 已存在 | 40.5 (metric=accuracy; dataset=text-only subset); 54.7 (metric=accuracy; dataset=text-only subset; variant=with tools) | [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md), [Official HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-05T03:06+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis GLM-5.2 model page](https://artificialanalysis.ai/models/releases/glm-5-2), [Artificial Analysis historical v4.1 article](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index/), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T03:06+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GLM-5.2 model page](https://artificialanalysis.ai/models/releases/glm-5-2) | 2026-11-05T03:06+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2 historical leaderboard](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T03:06+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 46.2
- metric: resolve rate
- source: [https://z.ai/blog/glm-5.2](https://z.ai/blog/glm-5.2)
- date: 2026-06-16
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 44% ± 2%
- metric: pass rate
- version: 1.1
- dataset: 113 tasks
- effort: max
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DeepSWE per-task trials](https://deepswe.datacurve.ai/data/v1.1/trials)
- [DeepSWE official README](https://github.com/datacurve-ai/deep-swe#readme)

研究备注：
- A new raw TOML row records the official glm-5.2[max] result, 44% ± 2%, max effort, 113 tasks, mini-swe-agent. The official leaderboard calls the metric “pass rate”; its page does not identify the per-task sample count for GLM-5.2. The current local definition requires pass@1, so the raw row is retained but excluded from exact mapping/coverage.

尚未解决的问题：
- Official static materials do not establish that this aggregate pass rate is pass@1 for GLM-5.2; confirm metric equivalence before mapping it to the local definition.

最近核验时间：2026-11-05T03:06+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Z.ai GLM-5.2 release page](https://z.ai/blog/glm-5.2)
- [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md)

研究备注：
- The existing SWE-Bench Pro 62.1 result has no V2 version or V2 conditions. The official V2 board does not show GLM-5.2; the earlier result is not transferred to V2.

最近核验时间：2026-11-05T03:06+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 82.7
- metric: success rate
- version: 2.1
- harness: Claude Code
- source: [https://z.ai/blog/glm-5.2](https://z.ai/blog/glm-5.2)
- date: 2026-06-16
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 81.0
- metric: success rate
- version: 2.1
- harness: Terminus 2
- source: [https://z.ai/blog/glm-5.2](https://z.ai/blog/glm-5.2)
- date: 2026-06-16
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md)

研究备注：
- The existing 2.1 results (81.0 with Terminus 2; 82.7 with Claude Code) are not v4.0. The current official v4 page did not expose readable dynamic rows.

尚未解决的问题：
- Cannot confirm whether a v4.0 GLM-5.2 result exists from the current dynamic board response.

最近核验时间：2026-11-05T03:06+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md)

研究备注：
- The official Science 0.1 table lists GLM-5.3 but not GLM-5.2. No related model result is transferred.

最近核验时间：2026-11-05T03:06+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard v1.0.6](https://zapier.com/benchmarks)
- [Official AutomationBench repository README](https://github.com/zapier/AutomationBench)
- [Official AutomationBench changelog](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)
- [Zapier leaderboard article](https://zapier.com/blog/ai-models-on-zapier/)

研究备注：
- The official board lists GLM-5.2 at rank #90 but does not show its score in readable content. The official repository README reports 26.17% for a 600-task public set at max effort, but that row does not specify evaluation version; the README says the official leaderboard uses a different held-out set.

尚未解决的问题：
- Cannot attribute the 26.17% public-set result to AutomationBench v1.0.6 or its official held-out leaderboard. No score row added.

最近核验时间：2026-11-05T03:06+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md)
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official site](https://osworld-v2.xlang.ai/)

研究备注：
- GLM-5.2 is documented as text-only and has no screenshot/visual input capability required for OSWorld computer-use evaluation.

最近核验时间：2026-11-05T03:06+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md)
- [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography)

研究备注：
- GLM-5.2 is documented as text-only; Chartography requires chart-image input and visual question answering.

最近核验时间：2026-11-05T03:06+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 40.5
- metric: accuracy
- dataset: text-only subset
- source: [https://z.ai/blog/glm-5.2](https://z.ai/blog/glm-5.2)
- date: 2026-06-16
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 54.7
- metric: accuracy
- dataset: text-only subset
- variant: with tools
- source: [https://z.ai/blog/glm-5.2](https://z.ai/blog/glm-5.2)
- date: 2026-06-16
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [GLM-5.2 official model card](https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md)
- [Official HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- Two existing rows are retained: 40.5 accuracy and 54.7 with tools, both on the model card’s text-only HLE subset. They are separate tool configurations and are not HLE-Diamond. The model card also lists sampling settings; no evaluation date is published.

最近核验时间：2026-11-05T03:06+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GLM-5.2 model page](https://artificialanalysis.ai/models/releases/glm-5-2)
- [Artificial Analysis historical v4.1 article](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index/)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current GLM-5.2 page has no V5.0.1 Intelligence Index result. The historical score 51 is for Index v4.1, not V5.0.1; it is not mapped.

最近核验时间：2026-11-05T03:06+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GLM-5.2 model page](https://artificialanalysis.ai/models/releases/glm-5-2)

研究备注：
- The official board does not show a GLM-5.2 Elo score. A sample artifact named GLM-5.2.pdf is not a total evaluation score.

最近核验时间：2026-11-05T03:06+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2 historical leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- The current v2.2 board does not list GLM-5.2. The v2 result 53.12% is a different version and is not mapped.

最近核验时间：2026-11-05T03:06+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GLM-5.2 model page",
          "url": "https://artificialanalysis.ai/models/releases/glm-5-2"
        },
        {
          "label": "Artificial Analysis historical v4.1 article",
          "url": "https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index/"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current GLM-5.2 page has no V5.0.1 Intelligence Index result. The historical score 51 is for Index v4.1, not V5.0.1; it is not mapped."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard v1.0.6",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Official AutomationBench repository README",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Official AutomationBench changelog",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        },
        {
          "label": "Zapier leaderboard article",
          "url": "https://zapier.com/blog/ai-models-on-zapier/"
        }
      ],
      "notes": [
        "The official board lists GLM-5.2 at rank #90 but does not show its score in readable content. The official repository README reports 26.17% for a 600-task public set at max effort, but that row does not specify evaluation version; the README says the official leaderboard uses a different held-out set."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot attribute the 26.17% public-set result to AutomationBench v1.0.6 or its official held-out leaderboard. No score row added."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "GLM-5.2 official model card",
          "url": "https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md"
        },
        {
          "label": "Chartography official benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "GLM-5.2 is documented as text-only; Chartography requires chart-image input and visual question answering."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DeepSWE per-task trials",
          "url": "https://deepswe.datacurve.ai/data/v1.1/trials"
        },
        {
          "label": "DeepSWE official README",
          "url": "https://github.com/datacurve-ai/deep-swe#readme"
        }
      ],
      "notes": [
        "A new raw TOML row records the official glm-5.2[max] result, 44% ± 2%, max effort, 113 tasks, mini-swe-agent. The official leaderboard calls the metric “pass rate”; its page does not identify the per-task sample count for GLM-5.2. The current local definition requires pass@1, so the raw row is retained but excluded from exact mapping/coverage."
      ],
      "status": "待核实",
      "unresolved": [
        "Official static materials do not establish that this aggregate pass rate is pass@1 for GLM-5.2; confirm metric equivalence before mapping it to the local definition."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GLM-5.2 model page",
          "url": "https://artificialanalysis.ai/models/releases/glm-5-2"
        }
      ],
      "notes": [
        "The official board does not show a GLM-5.2 Elo score. A sample artifact named GLM-5.2.pdf is not a total evaluation score."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "GLM-5.2 official model card",
          "url": "https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md"
        },
        {
          "label": "Official HLE leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "Two existing rows are retained: 40.5 accuracy and 54.7 with tools, both on the model card’s text-only HLE subset. They are separate tool configurations and are not HLE-Diamond. The model card also lists sampling settings; no evaluation date is published."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "GLM-5.2 official model card",
          "url": "https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md"
        },
        {
          "label": "OSWorld v2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld official site",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "GLM-5.2 is documented as text-only and has no screenshot/visual input capability required for OSWorld computer-use evaluation."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Z.ai GLM-5.2 release page",
          "url": "https://z.ai/blog/glm-5.2"
        },
        {
          "label": "GLM-5.2 official model card",
          "url": "https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md"
        }
      ],
      "notes": [
        "The existing SWE-Bench Pro 62.1 result has no V2 version or V2 conditions. The official V2 board does not show GLM-5.2; the earlier result is not transferred to V2."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "GLM-5.2 official model card",
          "url": "https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md"
        }
      ],
      "notes": [
        "The official Science 0.1 table lists GLM-5.3 but not GLM-5.2. No related model result is transferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "GLM-5.2 official model card",
          "url": "https://huggingface.co/zai-org/GLM-5.2/blob/f6142f127a14b58dc602592e996cd7d8ff139351/README.md"
        }
      ],
      "notes": [
        "The existing 2.1 results (81.0 with Terminus 2; 82.7 with Claude Code) are not v4.0. The current official v4 page did not expose readable dynamic rows."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot confirm whether a v4.0 GLM-5.2 result exists from the current dynamic board response."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:06+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2 historical leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "The current v2.2 board does not list GLM-5.2. The v2 result 53.12% is a different version and is not mapped."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 19,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:06+08:00",
  "model_id": "zhipuai/glm-5.2",
  "model_notes": [
    "本轮增加一条 DeepSWE 1.1 原始公开行：44% ± 2%，metric 原文为 pass rate，effort=max，113 tasks，mini-swe-agent。由于本地定义要求 pass@1，而官方材料未能确认 GLM-5.2 每题的采样数/聚合是否等价，原始行保留在 TOML 但不计入 Benchmark 覆盖率。来源：https://deepswe.datacurve.ai/blog/deepswe-v1-1；https://deepswe.datacurve.ai/data/v1.1/trials；https://github.com/datacurve-ai/deep-swe#readme",
    "GLM-5.2 TOML release_date=2026-06-13；Z.ai 官方发布页日期为 2026-06-16。保留仓库日期，记录差异，不据此改日期或重排队列。来源：https://z.ai/blog/glm-5.2"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
