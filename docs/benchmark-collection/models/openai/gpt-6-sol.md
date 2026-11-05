# GPT-6 Sol Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-6-sol
- 模型名称：GPT-6 Sol
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T08:34+08:00
- 整体处理状态：待复核
- 新增成绩数量：10
- 收集前已有成绩数量：4
- 当前已收录的对应成绩数量：6

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 68.8 (metric=score; version=1.1; dataset=113 tasks; effort=max) | [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T08:34+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/) | 2026-11-04T08:34+08:00 |
| terminal-bench-v4 | 冲突 | 34.34 (metric=accuracy; version=4.0; effort=max); 44.44 (metric=accuracy; version=4.0; dataset=66 tasks; effort=max; variant=avg@3 across three runs; each run pass@1; reported ±3.54; harness=Mini-SWE-agent) | [Vals GPT-6 Sol profile](https://www.vals.ai/models/openai_gpt-6-sol), [Vals Terminal-Bench 4 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T08:34+08:00 |
| terminal-bench-science-v0.1 | 冲突 | 31.43 (metric=accuracy; effort=max); 30.0 (metric=accuracy; version=0.1.0; dataset=70 tasks; effort=max; variant=single-run pass@1; reported ±5.52; harness=Mini-SWE-agent) | [Vals GPT-6 Sol profile](https://www.vals.ai/models/openai_gpt-6-sol), [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Terminal-Bench-Science v0.1 release report](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T08:34+08:00 |
| automationbench-v1.0.6 | 已收录 | 33.2 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=xhigh; variant=API mode; up to 50 steps per task); 21.2 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=low; variant=API mode; up to 50 steps per task); 26.9 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=medium; variant=API mode; up to 50 steps per task); 31.2 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=high; variant=API mode; up to 50 steps per task); 32.0 (metric=task_completed_correctly; version=1.0.6; dataset=held-out private evaluation set; effort=max; variant=API mode; up to 50 steps per task) | [Zapier GPT-6 Sol effort results](https://zapier.com/benchmarks/claude-sonnet5_5-report), [Zapier AutomationBench official metric and leaderboard methodology](https://zapier.com/benchmarks), [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/) | 2026-11-04T08:34+08:00 |
| osworld-v2.1 | 未找到 | 60.5 (metric=partial reward; version=2.0; dataset=offline v2026.08.08; effort=xhigh) | [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/), [OSWorld V2 official version history](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md), [OSWorld V2 official project](https://osworld-v2.xlang.ai/) | 2026-11-04T08:34+08:00 |
| chartography | 已收录 | 53.6 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=max; variant=Source metric accuracy/mean; 10 runs per task; Gemini 3.5 Flash judge; Max reasoning; harness=Inspect AI) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official methods and harness](https://github.com/surge-ai/chartography) | 2026-11-04T08:34+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis Humanity's Last Exam page and scoring method](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis current GPT-6 Sol model profile](https://artificialanalysis.ai/models/gpt-6-sol), [HLE-Diamond official release](https://lastexam.ai/blog/hle-diamond) | 2026-11-04T08:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 44 (metric=index score; version=5.0.1; effort=max) | [Artificial Analysis GPT-6 Sol model profile](https://artificialanalysis.ai/models/gpt-6-sol), [Artificial Analysis GPT-6 Sol release page](https://artificialanalysis.ai/models/releases/gpt-6-sol), [Artificial Analysis Intelligence Index page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T08:34+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa), [Artificial Analysis GPT-6 Sol and Luna analysis](https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier) | 2026-11-04T08:34+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index), [Vals GPT-6 Sol model profile](https://www.vals.ai/models/openai_gpt-6-sol), [Vals Index v2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-04T08:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 68.8
- metric: score
- version: 1.1
- dataset: 113 tasks
- effort: max
- source: [https://openai.com/index/introducing-gpt-6-sol-and-luna/](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- OpenAI directly reports GPT-6 Sol at max effort with score 68.8 on DeepSWE v1.1; the existing model/version/score match. Added the official 113-task dataset description and moved max into the effort field.
- OpenAI labels the value only as score; the cited run does not state that it used pass@1, which is the local definition metric. The release date is not an evaluation date and was removed from the row.

尚未解决的问题：
- The source does not establish the run metric as pass@1, so this row remains outside exact local-definition coverage.

最近核验时间：2026-11-04T08:34+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

研究备注：
- Checked the Scale V2 full leaderboard for the exact GPT-6 Sol model and the OpenAI release report; neither publishes a GPT-6 Sol SWE-bench Pro V2 result. No other SWE-bench version was transferred.

最近核验时间：2026-11-04T08:34+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 34.34
- metric: accuracy
- version: 4.0
- effort: max
- source: [https://www.vals.ai/models/openai_gpt-6-sol](https://www.vals.ai/models/openai_gpt-6-sol)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 44.44
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- effort: max
- variant: avg@3 across three runs; each run pass@1; reported ±3.54
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals GPT-6 Sol profile](https://www.vals.ai/models/openai_gpt-6-sol)
- [Vals Terminal-Bench 4 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- The current Vals board/profile reports 44.44% ±3.54 for GPT-6 Sol, max, Mini-SWE-agent; the board describes 66 tasks and avg@3 across three pass@1 runs. The same Vals profile's Sep 22 release update reports 34.34% for Terminal-Bench 4.0 at max effort without enough run conditions to reconcile the difference. Both source-backed values were retained as separate TOML rows; neither was selected as the single definitive score.
- Vals reports accuracy while the local definition metric is task resolution rate; exact metric mapping remains for review.

尚未解决的问题：
- The Vals profile's historical 34.34% and current 44.44% results have no disclosed run/configuration difference that explains the discrepancy.
- The source metric is accuracy; local mapping uses task resolution rate.

最近核验时间：2026-11-04T08:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 31.43
- metric: accuracy
- effort: max
- source: [https://www.vals.ai/models/openai_gpt-6-sol](https://www.vals.ai/models/openai_gpt-6-sol)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 30.0
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- effort: max
- variant: single-run pass@1; reported ±5.52
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals GPT-6 Sol profile](https://www.vals.ai/models/openai_gpt-6-sol)
- [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Terminal-Bench-Science v0.1 release report](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- The current Vals board/profile reports 30.00% ±5.52 for GPT-6 Sol, max, Mini-SWE-agent, on the upstream v0.1.0 70-task set with single-run pass@1. The profile's Sep 22 update reports 31.43% but does not expose conditions sufficient to explain the difference; both results are retained separately in the model TOML.
- Vals reports accuracy while the local definition metric is task resolution rate; exact metric mapping remains for review.

尚未解决的问题：
- The historical 31.43% and current 30.00% results have no disclosed run/configuration difference that explains the discrepancy.
- The historical row's exact benchmark version and test configuration are not specified; the source metric is accuracy while local mapping uses task resolution rate.

最近核验时间：2026-11-04T08:34+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 33.2
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: xhigh
- variant: API mode; up to 50 steps per task
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 21.2
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: low
- variant: API mode; up to 50 steps per task
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 26.9
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: medium
- variant: API mode; up to 50 steps per task
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: AutomationBench
- score: 31.2
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: high
- variant: API mode; up to 50 steps per task
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: AutomationBench
- score: 32.0
- metric: task_completed_correctly
- version: 1.0.6
- dataset: held-out private evaluation set
- effort: max
- variant: API mode; up to 50 steps per task
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier GPT-6 Sol effort results](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- [Zapier AutomationBench official metric and leaderboard methodology](https://zapier.com/benchmarks)
- [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

研究备注：
- Zapier's official comparison table lists GPT-6 Sol at 21.2 low, 26.9 medium, 31.2 high, 33.2 xhigh, and 32.0 max, all on AutomationBench 1.0.6. The OpenAI xhigh result independently matches 33.2.
- The benchmark page defines task_completed_correctly as the strict headline metric and describes leaderboard scores as held-out private task results, API mode, with up to 50 steps per task. No per-model evaluation date or exact task count is published.

最近核验时间：2026-11-04T08:34+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 60.5
- metric: partial reward
- version: 2.0
- dataset: offline v2026.08.08
- effort: xhigh
- source: [https://openai.com/index/introducing-gpt-6-sol-and-luna/](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [OpenAI GPT-6 Sol and Luna release report](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [OSWorld V2 official version history](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)
- [OSWorld V2 official project](https://osworld-v2.xlang.ai/)

研究备注：
- The existing GPT-6 Sol score is explicitly OSWorld 2.0 offline partial reward on v2026.08.08, not v2.1; it remains unchanged except the unsupported release-date value was removed. The official v2.1 materials checked did not publish an exact GPT-6 Sol v2.1 result.

最近核验时间：2026-11-04T08:34+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 53.6
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: max
- variant: Source metric accuracy/mean; 10 runs per task; Gemini 3.5 Flash judge; Max reasoning
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official methods and harness](https://github.com/surge-ai/chartography)

研究备注：
- Surge's leaderboard reports GPT-6 Sol (Max reasoning) at 53.6%. The official README defines accuracy/mean as Pass@1, uses the full 100-task set, ten runs per task and Gemini 3.5 Flash judge, and identifies Inspect AI as the harness. The TOML uses the repository's canonical metric wording, which is semantically equivalent to the source label accuracy/mean.
- The source does not give a semantic version or evaluation date; neither was added.

最近核验时间：2026-11-04T08:34+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Humanity's Last Exam page and scoring method](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis current GPT-6 Sol model profile](https://artificialanalysis.ai/models/gpt-6-sol)
- [HLE-Diamond official release](https://lastexam.ai/blog/hle-diamond)

研究备注：
- Artificial Analysis documents the original HLE text-only evaluation and pass@1 scoring, but current model/profile materials surfaced HLE-Diamond values rather than a directly verifiable GPT-6 Sol result on the original HLE set. HLE-Diamond was not transferred to the original HLE benchmark.

尚未解决的问题：
- A directly accessible source row for GPT-6 Sol on the original Humanity's Last Exam set has not been verified.

最近核验时间：2026-11-04T08:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 44
- metric: index score
- version: 5.0.1
- effort: max
- source: [https://artificialanalysis.ai/models/gpt-6-sol](https://artificialanalysis.ai/models/gpt-6-sol)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GPT-6 Sol model profile](https://artificialanalysis.ai/models/gpt-6-sol)
- [Artificial Analysis GPT-6 Sol release page](https://artificialanalysis.ai/models/releases/gpt-6-sol)
- [Artificial Analysis Intelligence Index page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- The current official GPT-6 Sol Max profile and model release page report an Intelligence Index score of 44 and identify the active index as v5.0.1. The raw result is recorded with exact source version and max effort; no evaluation date is stated.
- The repository's local Benchmark definition currently names version 5.0, while the direct source labels the evaluated index v5.0.1. The row therefore needs version-definition reconciliation before it counts toward exact mapped coverage.

尚未解决的问题：
- Source version 5.0.1 does not exactly match the local definition version 5.0; do not silently rewrite either version.

最近核验时间：2026-11-04T08:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)
- [Artificial Analysis GPT-6 Sol and Luna analysis](https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier)

研究备注：
- The official page documents GDPval-AA v2.1 as 220 tasks with shell/web access through Stirrup and Elo scoring. The GPT-6 Sol article confirms a max-effort result but gives only a relative comparison; the current public leaderboard does not expose a directly verifiable GPT-6 Sol row. No absolute score was written.

尚未解决的问题：
- A directly accessible official absolute Elo result for GPT-6 Sol on GDPval-AA v2.1 is still needed.

最近核验时间：2026-11-04T08:34+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)
- [Vals GPT-6 Sol model profile](https://www.vals.ai/models/openai_gpt-6-sol)
- [Vals Index v2 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- The official v2.2 leaderboard was checked; it does not list GPT-6 Sol among the visible current results. The GPT-6 Sol profile displays an overall 52.71% accuracy without naming the Vals Index version, while the profile's explicit Sep 22 result is 62.57% on Vals Index v2. These values cannot safely be attributed to v2.2.

尚未解决的问题：
- The profile's 52.71% score has no explicit version label and cannot be reconciled with the v2.2 leaderboard; no v2.2 result was added.

最近核验时间：2026-11-04T08:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-6 Sol model profile",
          "url": "https://artificialanalysis.ai/models/gpt-6-sol"
        },
        {
          "label": "Artificial Analysis GPT-6 Sol release page",
          "url": "https://artificialanalysis.ai/models/releases/gpt-6-sol"
        },
        {
          "label": "Artificial Analysis Intelligence Index page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "The current official GPT-6 Sol Max profile and model release page report an Intelligence Index score of 44 and identify the active index as v5.0.1. The raw result is recorded with exact source version and max effort; no evaluation date is stated.",
        "The repository's local Benchmark definition currently names version 5.0, while the direct source labels the evaluated index v5.0.1. The row therefore needs version-definition reconciliation before it counts toward exact mapped coverage."
      ],
      "status": "待核实",
      "unresolved": [
        "Source version 5.0.1 does not exactly match the local definition version 5.0; do not silently rewrite either version."
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier GPT-6 Sol effort results",
          "url": "https://zapier.com/benchmarks/claude-sonnet5_5-report"
        },
        {
          "label": "Zapier AutomationBench official metric and leaderboard methodology",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "OpenAI GPT-6 Sol and Luna release report",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        }
      ],
      "notes": [
        "Zapier's official comparison table lists GPT-6 Sol at 21.2 low, 26.9 medium, 31.2 high, 33.2 xhigh, and 32.0 max, all on AutomationBench 1.0.6. The OpenAI xhigh result independently matches 33.2.",
        "The benchmark page defines task_completed_correctly as the strict headline metric and describes leaderboard scores as held-out private task results, API mode, with up to 50 steps per task. No per-model evaluation date or exact task count is published."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official methods and harness",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge's leaderboard reports GPT-6 Sol (Max reasoning) at 53.6%. The official README defines accuracy/mean as Pass@1, uses the full 100-task set, ten runs per task and Gemini 3.5 Flash judge, and identifies Inspect AI as the harness. The TOML uses the repository's canonical metric wording, which is semantically equivalent to the source label accuracy/mean.",
        "The source does not give a semantic version or evaluation date; neither was added."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Sol and Luna release report",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "OpenAI directly reports GPT-6 Sol at max effort with score 68.8 on DeepSWE v1.1; the existing model/version/score match. Added the official 113-task dataset description and moved max into the effort field.",
        "OpenAI labels the value only as score; the cited run does not state that it used pass@1, which is the local definition metric. The release date is not an evaluation date and was removed from the row."
      ],
      "status": "待核实",
      "unresolved": [
        "The source does not establish the run metric as pass@1, so this row remains outside exact local-definition coverage."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        },
        {
          "label": "Artificial Analysis GPT-6 Sol and Luna analysis",
          "url": "https://artificialanalysis.ai/articles/gpt-6-sol-and-luna-push-the-cost-efficiency-frontier"
        }
      ],
      "notes": [
        "The official page documents GDPval-AA v2.1 as 220 tasks with shell/web access through Stirrup and Elo scoring. The GPT-6 Sol article confirms a max-effort result but gives only a relative comparison; the current public leaderboard does not expose a directly verifiable GPT-6 Sol row. No absolute score was written."
      ],
      "status": "待核实",
      "unresolved": [
        "A directly accessible official absolute Elo result for GPT-6 Sol on GDPval-AA v2.1 is still needed."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Humanity's Last Exam page and scoring method",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis current GPT-6 Sol model profile",
          "url": "https://artificialanalysis.ai/models/gpt-6-sol"
        },
        {
          "label": "HLE-Diamond official release",
          "url": "https://lastexam.ai/blog/hle-diamond"
        }
      ],
      "notes": [
        "Artificial Analysis documents the original HLE text-only evaluation and pass@1 scoring, but current model/profile materials surfaced HLE-Diamond values rather than a directly verifiable GPT-6 Sol result on the original HLE set. HLE-Diamond was not transferred to the original HLE benchmark."
      ],
      "status": "待核实",
      "unresolved": [
        "A directly accessible source row for GPT-6 Sol on the original Humanity's Last Exam set has not been verified."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Sol and Luna release report",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        },
        {
          "label": "OSWorld V2 official version history",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        },
        {
          "label": "OSWorld V2 official project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "The existing GPT-6 Sol score is explicitly OSWorld 2.0 offline partial reward on v2026.08.08, not v2.1; it remains unchanged except the unsupported release-date value was removed. The official v2.1 materials checked did not publish an exact GPT-6 Sol v2.1 result."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "OpenAI GPT-6 Sol and Luna release report",
          "url": "https://openai.com/index/introducing-gpt-6-sol-and-luna/"
        }
      ],
      "notes": [
        "Checked the Scale V2 full leaderboard for the exact GPT-6 Sol model and the OpenAI release report; neither publishes a GPT-6 Sol SWE-bench Pro V2 result. No other SWE-bench version was transferred."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Vals GPT-6 Sol profile",
          "url": "https://www.vals.ai/models/openai_gpt-6-sol"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench-Science v0.1 release report",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "The current Vals board/profile reports 30.00% ±5.52 for GPT-6 Sol, max, Mini-SWE-agent, on the upstream v0.1.0 70-task set with single-run pass@1. The profile's Sep 22 update reports 31.43% but does not expose conditions sufficient to explain the difference; both results are retained separately in the model TOML.",
        "Vals reports accuracy while the local definition metric is task resolution rate; exact metric mapping remains for review."
      ],
      "status": "冲突",
      "unresolved": [
        "The historical 31.43% and current 30.00% results have no disclosed run/configuration difference that explains the discrepancy.",
        "The historical row's exact benchmark version and test configuration are not specified; the source metric is accuracy while local mapping uses task resolution rate."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Vals GPT-6 Sol profile",
          "url": "https://www.vals.ai/models/openai_gpt-6-sol"
        },
        {
          "label": "Vals Terminal-Bench 4 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "The current Vals board/profile reports 44.44% ±3.54 for GPT-6 Sol, max, Mini-SWE-agent; the board describes 66 tasks and avg@3 across three pass@1 runs. The same Vals profile's Sep 22 release update reports 34.34% for Terminal-Bench 4.0 at max effort without enough run conditions to reconcile the difference. Both source-backed values were retained as separate TOML rows; neither was selected as the single definitive score.",
        "Vals reports accuracy while the local definition metric is task resolution rate; exact metric mapping remains for review."
      ],
      "status": "冲突",
      "unresolved": [
        "The Vals profile's historical 34.34% and current 44.44% results have no disclosed run/configuration difference that explains the discrepancy.",
        "The source metric is accuracy; local mapping uses task resolution rate."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T08:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals GPT-6 Sol model profile",
          "url": "https://www.vals.ai/models/openai_gpt-6-sol"
        },
        {
          "label": "Vals Index v2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "The official v2.2 leaderboard was checked; it does not list GPT-6 Sol among the visible current results. The GPT-6 Sol profile displays an overall 52.71% accuracy without naming the Vals Index version, while the profile's explicit Sep 22 result is 62.57% on Vals Index v2. These values cannot safely be attributed to v2.2."
      ],
      "status": "待核实",
      "unresolved": [
        "The profile's 52.71% score has no explicit version label and cannot be reconciled with the v2.2 leaderboard; no v2.2 result was added."
      ]
    }
  },
  "existing_records": 4,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T08:34+08:00",
  "model_id": "openai/gpt-6-sol",
  "new_records": 10,
  "overall_status": "待复核"
}

-->
