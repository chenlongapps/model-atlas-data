# Ember-1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：fireworks/ember-1
- 模型名称：Ember-1
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T07:52+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 75.2 (metric=score; version=1.1; dataset=113 tasks); 67.0 (metric=score; version=1.1; dataset=113 tasks; variant=avg@3 (three-run mean)) | [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1), [Fireworks DeepSWE v1.1 SII leaderboard](https://fireworks.ai/specialized-intelligence-index/benchmarks/code-generation/deepswe-v1-1), [DataCurve DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T07:52+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1), [Scale SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T07:52+08:00 |
| terminal-bench-v4 | 待核实 | 20.71 ± 3.64 (metric=accuracy; version=4.0; dataset=66 tasks; variant=avg@3 (three full runs; each run pass@1); harness=Mini-SWE-agent) | [Vals Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1), [Terminal-Bench 4.0 official release information](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T07:52+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 5.71 ± 2.79 (metric=accuracy; version=0.1.0; dataset=70 tasks; variant=single-run pass@1; harness=Mini-SWE-agent) | [Vals Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science), [Terminal-Bench-Science v0.1.0 release](https://github.com/harbor-framework/terminal-bench-science/releases), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| chartography | 未找到 | — | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge Chartography official protocol](https://github.com/surge-ai/chartography), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| humanitys-last-exam | 未找到 | — | [Artificial Analysis Humanity’s Last Exam page](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Fireworks model directory](https://artificialanalysis.ai/providers/fireworks), [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1) | 2026-11-04T07:52+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals historical Index v2.1 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1), [Vals Ember-1 model profile](https://www.vals.ai/models/fireworks_ember-1) | 2026-11-04T07:52+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 75.2
- metric: score
- version: 1.1
- dataset: 113 tasks
- source: [https://fireworks.ai/blog/ember-1](https://fireworks.ai/blog/ember-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 67.0
- metric: score
- version: 1.1
- dataset: 113 tasks
- variant: avg@3 (three-run mean)
- source: [https://fireworks.ai/specialized-intelligence-index/benchmarks/code-generation/deepswe-v1-1](https://fireworks.ai/specialized-intelligence-index/benchmarks/code-generation/deepswe-v1-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)
- [Fireworks DeepSWE v1.1 SII leaderboard](https://fireworks.ai/specialized-intelligence-index/benchmarks/code-generation/deepswe-v1-1)
- [DataCurve DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Fireworks release report gives 75.2% on 113 tasks but does not disclose the metric aggregation or run configuration. The Fireworks SII DeepSWE v1.1 board separately gives 67.0% avg@3 (three-run mean). Both identify Ember-1 and the same benchmark version; both records are retained without treating them as comparable. DataCurve board currently has no exact Ember-1 row.

尚未解决的问题：
- Fireworks launch report score 75.2% and SII avg@3 score 67.0% differ; the launch report does not publish enough evaluation details to reconcile them.

最近核验时间：2026-11-04T07:52+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)
- [Scale SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Fireworks reports SWE-bench Verified, not SWE-bench Pro V2. Scale V2 full leaderboard has no exact Ember-1 row; the Verified score is not substituted.

最近核验时间：2026-11-04T07:52+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 20.71 ± 3.64
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- variant: avg@3 (three full runs; each run pass@1)
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench 4.0 leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)
- [Terminal-Bench 4.0 official release information](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Vals reports 20.71% ±3.64 for Ember-1 with Mini-SWE-agent. Its method uses 66 tasks and avg@3 across three complete runs, each scored pass@1. Fireworks launch result 82.0% is Terminal-Bench 2.1 and is excluded. Vals labels its metric accuracy and version 4.0; the local definition requires task resolution rate and stores canonical version 4.0.0, so the score is preserved but not counted as an exact mapped row.

尚未解决的问题：
- Vals source metric is accuracy while the local v4 definition requires task resolution rate; source version label 4.0 also differs from the local canonical string 4.0.0.

最近核验时间：2026-11-04T07:52+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 5.71 ± 2.79
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- variant: single-run pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Terminal-Bench-Science v0.1.0 release](https://github.com/harbor-framework/terminal-bench-science/releases)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- Vals reports 5.71% ±2.79 with Mini-SWE-agent. The method names upstream v0.1.0 and 70 tasks, using a single pass@1 run; only infrastructure/provider errors are retried. Fireworks release report does not provide a Terminal-Bench-Science result. The Vals board labels the metric accuracy, while the local definition requires task resolution rate; the raw metric is preserved and not counted as an exact mapped row.

尚未解决的问题：
- Vals source metric is accuracy while the local v0.1.0 definition requires task resolution rate.

最近核验时间：2026-11-04T07:52+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- Zapier leaderboard and Fireworks report do not show an exact Ember-1 AutomationBench result. No score or run configuration was inferred.

最近核验时间：2026-11-04T07:52+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- Official OSWorld V2 materials and the Fireworks release report contain no exact Ember-1 v2.1 result. The interactive leaderboard did not expose an exact Ember-1 row in its readable content.

最近核验时间：2026-11-04T07:52+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography official protocol](https://github.com/surge-ai/chartography)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- No exact Ember-1 Chartography score was found on the official board or in Fireworks public release material. Image input support alone is not evidence of a benchmark score.

最近核验时间：2026-11-04T07:52+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Humanity’s Last Exam page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- The Artificial Analysis original-HLE board does not list Ember-1; Fireworks release report also contains no HLE result. No score, test configuration, or date was inferred.

最近核验时间：2026-11-04T07:52+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Fireworks model directory](https://artificialanalysis.ai/providers/fireworks)
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- Artificial Analysis Fireworks listings do not include Ember-1. Fireworks Specialized Intelligence Index (SII) is a separate composite and cannot be used as Artificial Analysis Intelligence Index V5.

最近核验时间：2026-11-04T07:52+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Fireworks Ember-1 release report](https://fireworks.ai/blog/ember-1)

研究备注：
- The current GDPval-AA v2.1 leaderboard has no exact Ember-1 row; Fireworks does not report this result.

最近核验时间：2026-11-04T07:52+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals historical Index v2.1 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1)
- [Vals Ember-1 model profile](https://www.vals.ai/models/fireworks_ember-1)

研究备注：
- Vals v2.2 does not list Ember-1. The profile/search identifies a 50.94% result on Vals Index v2.1 only; it is not copied into the v2.2 record. Vals page update dates are not evaluation dates.

最近核验时间：2026-11-04T07:52+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Fireworks model directory",
          "url": "https://artificialanalysis.ai/providers/fireworks"
        },
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "Artificial Analysis Fireworks listings do not include Ember-1. Fireworks Specialized Intelligence Index (SII) is a separate composite and cannot be used as Artificial Analysis Intelligence Index V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "Zapier leaderboard and Fireworks report do not show an exact Ember-1 AutomationBench result. No score or run configuration was inferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography official protocol",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "No exact Ember-1 Chartography score was found on the official board or in Fireworks public release material. Image input support alone is not evidence of a benchmark score."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        },
        {
          "label": "Fireworks DeepSWE v1.1 SII leaderboard",
          "url": "https://fireworks.ai/specialized-intelligence-index/benchmarks/code-generation/deepswe-v1-1"
        },
        {
          "label": "DataCurve DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Fireworks release report gives 75.2% on 113 tasks but does not disclose the metric aggregation or run configuration. The Fireworks SII DeepSWE v1.1 board separately gives 67.0% avg@3 (three-run mean). Both identify Ember-1 and the same benchmark version; both records are retained without treating them as comparable. DataCurve board currently has no exact Ember-1 row."
      ],
      "status": "冲突",
      "unresolved": [
        "Fireworks launch report score 75.2% and SII avg@3 score 67.0% differ; the launch report does not publish enough evaluation details to reconcile them."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "The current GDPval-AA v2.1 leaderboard has no exact Ember-1 row; Fireworks does not report this result."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Humanity’s Last Exam page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "The Artificial Analysis original-HLE board does not list Ember-1; Fireworks release report also contains no HLE result. No score, test configuration, or date was inferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "Official OSWorld V2 materials and the Fireworks release report contain no exact Ember-1 v2.1 result. The interactive leaderboard did not expose an exact Ember-1 row in its readable content."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        },
        {
          "label": "Scale SWE-bench Pro V2 full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Fireworks reports SWE-bench Verified, not SWE-bench Pro V2. Scale V2 full leaderboard has no exact Ember-1 row; the Verified score is not substituted."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science v0.1.0 release",
          "url": "https://github.com/harbor-framework/terminal-bench-science/releases"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        }
      ],
      "notes": [
        "Vals reports 5.71% ±2.79 with Mini-SWE-agent. The method names upstream v0.1.0 and 70 tasks, using a single pass@1 run; only infrastructure/provider errors are retried. Fireworks release report does not provide a Terminal-Bench-Science result. The Vals board labels the metric accuracy, while the local definition requires task resolution rate; the raw metric is preserved and not counted as an exact mapped row."
      ],
      "status": "待核实",
      "unresolved": [
        "Vals source metric is accuracy while the local v0.1.0 definition requires task resolution rate."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Fireworks Ember-1 release report",
          "url": "https://fireworks.ai/blog/ember-1"
        },
        {
          "label": "Terminal-Bench 4.0 official release information",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Vals reports 20.71% ±3.64 for Ember-1 with Mini-SWE-agent. Its method uses 66 tasks and avg@3 across three complete runs, each scored pass@1. Fireworks launch result 82.0% is Terminal-Bench 2.1 and is excluded. Vals labels its metric accuracy and version 4.0; the local definition requires task resolution rate and stores canonical version 4.0.0, so the score is preserved but not counted as an exact mapped row."
      ],
      "status": "待核实",
      "unresolved": [
        "Vals source metric is accuracy while the local v4 definition requires task resolution rate; source version label 4.0 also differs from the local canonical string 4.0.0."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T07:52+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals historical Index v2.1 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        },
        {
          "label": "Vals Ember-1 model profile",
          "url": "https://www.vals.ai/models/fireworks_ember-1"
        }
      ],
      "notes": [
        "Vals v2.2 does not list Ember-1. The profile/search identifies a 50.94% result on Vals Index v2.1 only; it is not copied into the v2.2 record. Vals page update dates are not evaluation dates."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T07:52+08:00",
  "model_id": "fireworks/ember-1",
  "new_records": 4,
  "overall_status": "待复核"
}

-->
