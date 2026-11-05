# Claude Opus 5.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-opus-5-5
- 模型名称：Claude Opus 5.5
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T07:44+08:00
- 整体处理状态：待复核
- 新增成绩数量：22
- 收集前已有成绩数量：9
- 当前已收录的对应成绩数量：19

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 74.2 (metric=pass@1; version=1.1; dataset=113 tasks; effort=max; variant=mean of 5 trials) | [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T07:44+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf), [Scale SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T07:44+08:00 |
| terminal-bench-v4 | 已收录 | 66.36 (metric=task resolution rate; version=4.0.0; effort=xhigh; variant=production safeguards with fallback; 5 trials per task (330 runs); harness=Claude Code --bare); 65.15 (metric=accuracy; version=4.0; harness=Mini-SWE-agent) | [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf), [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5), [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T07:44+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 58.7 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; effort=max; variant=production safeguards with fallback; 10 trials per task (700 runs); harness=Claude Code --bare); 47.14 (metric=accuracy; harness=Mini-SWE-agent) | [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf), [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5), [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T07:44+08:00 |
| automationbench-v1.0.6 | 已收录 | 23.3 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Low; variant=without fallbacks; strict all-assertions scoring; refusals included; harness=Zapier API; 50-step cap); 28.6 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Medium; variant=without fallbacks; strict all-assertions scoring; refusals included; harness=Zapier API; 50-step cap); 32.0 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=High; variant=without fallbacks; strict all-assertions scoring; refusals included; harness=Zapier API; 50-step cap); 34.4 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=XHigh; variant=without fallbacks; strict all-assertions scoring; refusals included; harness=Zapier API; 50-step cap); 40.0 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Max; variant=without fallbacks; strict all-assertions scoring; refusals included; harness=Zapier API; 50-step cap); 42.47 (metric=task_completed_correctly; version=1.0.6; effort=Max; variant=Anthropic default fallback routing) | [Zapier Opus 5.5 evaluation report](https://zapier.com/benchmarks/claude-opus5_5-report), [Zapier public leaderboard](https://zapier.com/benchmarks), [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5) | 2026-11-04T07:44+08:00 |
| osworld-v2.1 | 冲突 | 81.8 (metric=partial score; version=2.1; effort=max; variant=production safeguards with fallback) | [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2 official project](https://osworld-v2.xlang.ai/) | 2026-11-04T07:44+08:00 |
| chartography | 待核实 | 89 (metric=score; effort=max; variant=with tools; production safeguards); 66.3 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=Adaptive/Max; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge Chartography evaluation protocol](https://github.com/surge-ai/chartography) | 2026-11-04T07:44+08:00 |
| humanitys-last-exam | 已收录 | 67.7 (metric=score; effort=max; variant=with tools; production safeguards); 61.4 (metric=accuracy; dataset=2,158 text-only questions from the original 2,500-question HLE set; effort=Max; variant=Pass@1; Default Fallback) | [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5), [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T07:44+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 58 (metric=index score; version=5.0; effort=max); 59 (metric=index score; version=5.0.1; effort=Max; variant=Default Fallback); 57 (metric=index score; version=5.0.1; effort=Xhigh; variant=Default Fallback); 52 (metric=index score; version=5.0.1; effort=High; variant=Default Fallback); 48 (metric=index score; version=5.0.1; effort=Medium; variant=Default Fallback); 35 (metric=index score; version=5.0.1; effort=Low; variant=Default Fallback) | [Artificial Analysis Index v5.0 launch report](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5), [Artificial Analysis Index v5.0.1 benchmark page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Opus 5.5 Max profile](https://artificialanalysis.ai/models/claude-opus-5-5), [Artificial Analysis Opus 5.5 Xhigh profile](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh), [Artificial Analysis Opus 5.5 High profile](https://artificialanalysis.ai/models/claude-opus-5-5-high), [Artificial Analysis Opus 5.5 Medium profile](https://artificialanalysis.ai/models/claude-opus-5-5-medium), [Artificial Analysis Opus 5.5 Low profile](https://artificialanalysis.ai/models/claude-opus-5-5-low) | 2026-11-04T07:44+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1846 (metric=Elo rating; version=2.1; effort=max; variant=production safeguards); 1866 (metric=Elo rating; version=2.1; dataset=OpenAI GDPval (220 tasks); effort=Max; variant=Default Fallback; E2B sandbox; blind pairwise comparisons; harness=Stirrup); 1835 (metric=Elo rating; version=2.1; dataset=OpenAI GDPval (220 tasks); effort=Xhigh; variant=Default Fallback; E2B sandbox; blind pairwise comparisons; harness=Stirrup); 1714 (metric=Elo rating; version=2.1; dataset=OpenAI GDPval (220 tasks); effort=High; variant=Default Fallback; E2B sandbox; blind pairwise comparisons; harness=Stirrup); 1593 (metric=Elo rating; version=2.1; dataset=OpenAI GDPval (220 tasks); effort=Medium; variant=Default Fallback; E2B sandbox; blind pairwise comparisons; harness=Stirrup); 1240 (metric=Elo rating; version=2.1; dataset=OpenAI GDPval (220 tasks); effort=Low; variant=Default Fallback; E2B sandbox; blind pairwise comparisons; harness=Stirrup) | [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5), [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T07:44+08:00 |
| vals-index-v2.2 | 已收录 | 70.18 (metric=performance score; version=2.2; dataset=Vals Index composite (finance, coding, legal, tax); effort=max; variant=Anthropic default provider; 2.68% fallback rate) | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Claude Opus 5.5 model profile](https://www.vals.ai/models/anthropic_claude-opus-5-5) | 2026-11-04T07:44+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 74.2
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: max
- variant: mean of 5 trials
- source: [https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- System Card reports 74.2% pass@1 on 113 tasks, averaged across five trials, at max adaptive thinking. DataCurve leaderboard currently has no exact Opus 5.5 row; the System Card is the score source.

最近核验时间：2026-11-04T07:44+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- [Scale SWE-bench Pro V2 full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- The System Card reports 89.9% for SWE-bench Pro but does not identify V2; its cited paper is the 2025 Pro paper. The V2 full leaderboard has no exact Opus 5.5 row, so no V2 score was written.

尚未解决的问题：
- Cannot establish that the System Card 89.9% result used SWE-bench Pro V2 (642-task default configuration).

最近核验时间：2026-11-04T07:44+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 66.36
- metric: task resolution rate
- version: 4.0.0
- effort: xhigh
- variant: production safeguards with fallback; 5 trials per task (330 runs)
- harness: Claude Code --bare
- source: [https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 65.15
- metric: accuracy
- version: 4.0
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- System Card gives the Anthropic run as 66.36%; the launch report rounds it to 66.4%. It used xhigh effort, Claude Code --bare and five trials per task (330 runs), with production safeguards and fallback. Vals separately reports 65.15% with Mini-SWE-agent; retained as a distinct source/configuration. The repository version 4.0.0 is the canonical form of the source-labeled 4.0 release.

最近核验时间：2026-11-04T07:44+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 58.7
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- effort: max
- variant: production safeguards with fallback; 10 trials per task (700 runs)
- harness: Claude Code --bare
- source: [https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 47.14
- metric: accuracy
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)
- [Vals Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- System Card reports 58.7% at max effort with Claude Code --bare, ten trials per task (700 runs), and production safeguards/fallback. Vals separately reports 47.14% with Mini-SWE-agent; its page does not name the benchmark version, so that row has no version field. The repository version 0.1.0 is the canonical form of the source-labeled 0.1 release.

最近核验时间：2026-11-04T07:44+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 23.3
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Low
- variant: without fallbacks; strict all-assertions scoring; refusals included
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-opus5_5-report](https://zapier.com/benchmarks/claude-opus5_5-report)
- date: 2026-09-17 to 2026-09-18
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 28.6
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Medium
- variant: without fallbacks; strict all-assertions scoring; refusals included
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-opus5_5-report](https://zapier.com/benchmarks/claude-opus5_5-report)
- date: 2026-09-17 to 2026-09-18
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 32.0
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: High
- variant: without fallbacks; strict all-assertions scoring; refusals included
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-opus5_5-report](https://zapier.com/benchmarks/claude-opus5_5-report)
- date: 2026-09-17 to 2026-09-18
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: AutomationBench
- score: 34.4
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: XHigh
- variant: without fallbacks; strict all-assertions scoring; refusals included
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-opus5_5-report](https://zapier.com/benchmarks/claude-opus5_5-report)
- date: 2026-09-17 to 2026-09-18
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: AutomationBench
- score: 40.0
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Max
- variant: without fallbacks; strict all-assertions scoring; refusals included
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-opus5_5-report](https://zapier.com/benchmarks/claude-opus5_5-report)
- date: 2026-09-17 to 2026-09-18
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: AutomationBench
- score: 42.47
- metric: task_completed_correctly
- version: 1.0.6
- effort: Max
- variant: Anthropic default fallback routing
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier Opus 5.5 evaluation report](https://zapier.com/benchmarks/claude-opus5_5-report)
- [Zapier public leaderboard](https://zapier.com/benchmarks)
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)

研究备注：
- Zapier explicitly dates its no-fallback run to Sep 17–18, 2026 and reports Low 23.3%, Medium 28.6%, High 32.0%, XHigh 34.4%, and Max 40.0% over 657 tasks per effort; refusals remain in the denominator. The public leaderboard separately reports 42.47% at Max with Anthropic default fallback routing. These are distinct configurations.

最近核验时间：2026-11-04T07:44+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 81.8
- metric: partial score
- version: 2.1
- effort: max
- variant: production safeguards with fallback
- source: [https://www.anthropic.com/claude-opus-5-5](https://www.anthropic.com/claude-opus-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2 official project](https://osworld-v2.xlang.ai/)

研究备注：
- Anthropic identifies the result as OSWorld 2.1 and labels 81.8% as partial. The local v2.1 definition is binary task completion rate; the partial score is kept with its source metric and is not counted as a mapped binary-completion result. No evaluation date is stated.

尚未解决的问题：
- The verified 81.8% uses partial scoring, while the local Benchmark definition requires binary task completion rate.

最近核验时间：2026-11-04T07:44+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 89
- metric: score
- effort: max
- variant: with tools; production safeguards
- source: [https://www.anthropic.com/claude-opus-5-5](https://www.anthropic.com/claude-opus-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Chartography
- score: 66.3
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: Adaptive/Max
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography evaluation protocol](https://github.com/surge-ai/chartography)

研究备注：
- Anthropic reports 89.0% with tools at max effort but does not state dataset, repeats, judge, or harness; this row remains separate and is not normalized to the local metric. Surge reports 66.3% for Opus 5.5 (Adaptive/Max) on the standard 100-task leaderboard, with ten runs per task, Gemini 3.5 Flash judge, and accuracy/mean (Pass@1). Both scores are retained as distinct configurations.

尚未解决的问题：
- The Anthropic 89.0% result lacks enough published protocol details to compare with Surge standard-board 66.3%.

最近核验时间：2026-11-04T07:44+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 67.7
- metric: score
- effort: max
- variant: with tools; production safeguards
- source: [https://www.anthropic.com/claude-opus-5-5](https://www.anthropic.com/claude-opus-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 61.4
- metric: accuracy
- dataset: 2,158 text-only questions from the original 2,500-question HLE set
- effort: Max
- variant: Pass@1; Default Fallback
- source: [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)
- [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Anthropic reports 67.7% with tools; its release report does not state dataset size or evaluation date. Artificial Analysis separately reports 61.4% at Max with Default Fallback, pass@1 on 2,158 text-only questions from the original 2,500-question HLE set. These are distinct configurations.

最近核验时间：2026-11-04T07:44+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 58
- metric: index score
- version: 5.0
- effort: max
- source: [https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 59
- metric: index score
- version: 5.0.1
- effort: Max
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-opus-5-5](https://artificialanalysis.ai/models/claude-opus-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 57
- metric: index score
- version: 5.0.1
- effort: Xhigh
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-opus-5-5-xhigh](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Artificial Analysis Intelligence Index
- score: 52
- metric: index score
- version: 5.0.1
- effort: High
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-opus-5-5-high](https://artificialanalysis.ai/models/claude-opus-5-5-high)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Artificial Analysis Intelligence Index
- score: 48
- metric: index score
- version: 5.0.1
- effort: Medium
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-opus-5-5-medium](https://artificialanalysis.ai/models/claude-opus-5-5-medium)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 6

- name: Artificial Analysis Intelligence Index
- score: 35
- metric: index score
- version: 5.0.1
- effort: Low
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-opus-5-5-low](https://artificialanalysis.ai/models/claude-opus-5-5-low)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Index v5.0 launch report](https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5)
- [Artificial Analysis Index v5.0.1 benchmark page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Opus 5.5 Max profile](https://artificialanalysis.ai/models/claude-opus-5-5)
- [Artificial Analysis Opus 5.5 Xhigh profile](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh)
- [Artificial Analysis Opus 5.5 High profile](https://artificialanalysis.ai/models/claude-opus-5-5-high)
- [Artificial Analysis Opus 5.5 Medium profile](https://artificialanalysis.ai/models/claude-opus-5-5-medium)
- [Artificial Analysis Opus 5.5 Low profile](https://artificialanalysis.ai/models/claude-opus-5-5-low)

研究备注：
- The v5 launch report gives 58 at max for v5.0, matching the repository definition. Current official profiles label the revised suite v5.0.1 and report Max 59, Xhigh 57, High 52, Medium 48, and Low 35, all with Default Fallback; the revision scores are retained under v5.0.1 and are not mapped to the v5.0 definition. Neither page gives an evaluation date.

最近核验时间：2026-11-04T07:44+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1846
- metric: Elo rating
- version: 2.1
- effort: max
- variant: production safeguards
- source: [https://www.anthropic.com/claude-opus-5-5](https://www.anthropic.com/claude-opus-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1866
- metric: Elo rating
- version: 2.1
- dataset: OpenAI GDPval (220 tasks)
- effort: Max
- variant: Default Fallback; E2B sandbox; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: GDPval-AA
- score: 1835
- metric: Elo rating
- version: 2.1
- dataset: OpenAI GDPval (220 tasks)
- effort: Xhigh
- variant: Default Fallback; E2B sandbox; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: GDPval-AA
- score: 1714
- metric: Elo rating
- version: 2.1
- dataset: OpenAI GDPval (220 tasks)
- effort: High
- variant: Default Fallback; E2B sandbox; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: GDPval-AA
- score: 1593
- metric: Elo rating
- version: 2.1
- dataset: OpenAI GDPval (220 tasks)
- effort: Medium
- variant: Default Fallback; E2B sandbox; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: GDPval-AA
- score: 1240
- metric: Elo rating
- version: 2.1
- dataset: OpenAI GDPval (220 tasks)
- effort: Low
- variant: Default Fallback; E2B sandbox; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic launch report](https://www.anthropic.com/claude-opus-5-5)
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Anthropic reports 1846 for GDPval-AA v2.1 at max effort. Artificial Analysis currently lists Max 1866 (Default Fallback), Xhigh 1835, High 1714, Medium 1593, and Low 1240 on 220 tasks via Stirrup. The two Max results differ by 20 Elo; both are preserved because the sources do not explain the discrepancy. No evaluation date is stated.

尚未解决的问题：
- Anthropic launch report and current Artificial Analysis leaderboard report different Max scores for GDPval-AA v2.1 (1846 vs 1866); the reason is not published.

最近核验时间：2026-11-04T07:44+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 70.18
- metric: performance score
- version: 2.2
- dataset: Vals Index composite (finance, coding, legal, tax)
- effort: max
- variant: Anthropic default provider; 2.68% fallback rate
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Claude Opus 5.5 model profile](https://www.vals.ai/models/anthropic_claude-opus-5-5)

研究备注：
- Vals reports 70.18% performance score at max effort, Anthropic as default provider, and 2.68% fallback rate. The composite covers finance, coding, legal, and tax tasks. The page update date is not treated as an evaluation date.

最近核验时间：2026-11-04T07:44+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Index v5.0 launch report",
          "url": "https://artificialanalysis.ai/es/articles/artificial-analysis-intelligence-index-v5"
        },
        {
          "label": "Artificial Analysis Index v5.0.1 benchmark page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Opus 5.5 Max profile",
          "url": "https://artificialanalysis.ai/models/claude-opus-5-5"
        },
        {
          "label": "Artificial Analysis Opus 5.5 Xhigh profile",
          "url": "https://artificialanalysis.ai/models/claude-opus-5-5-xhigh"
        },
        {
          "label": "Artificial Analysis Opus 5.5 High profile",
          "url": "https://artificialanalysis.ai/models/claude-opus-5-5-high"
        },
        {
          "label": "Artificial Analysis Opus 5.5 Medium profile",
          "url": "https://artificialanalysis.ai/models/claude-opus-5-5-medium"
        },
        {
          "label": "Artificial Analysis Opus 5.5 Low profile",
          "url": "https://artificialanalysis.ai/models/claude-opus-5-5-low"
        }
      ],
      "notes": [
        "The v5 launch report gives 58 at max for v5.0, matching the repository definition. Current official profiles label the revised suite v5.0.1 and report Max 59, Xhigh 57, High 52, Medium 48, and Low 35, all with Default Fallback; the revision scores are retained under v5.0.1 and are not mapped to the v5.0 definition. Neither page gives an evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Zapier Opus 5.5 evaluation report",
          "url": "https://zapier.com/benchmarks/claude-opus5_5-report"
        },
        {
          "label": "Zapier public leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        }
      ],
      "notes": [
        "Zapier explicitly dates its no-fallback run to Sep 17–18, 2026 and reports Low 23.3%, Medium 28.6%, High 32.0%, XHigh 34.4%, and Max 40.0% over 657 tasks per effort; refusals remain in the denominator. The public leaderboard separately reports 42.47% at Max with Anthropic default fallback routing. These are distinct configurations."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography evaluation protocol",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Anthropic reports 89.0% with tools at max effort but does not state dataset, repeats, judge, or harness; this row remains separate and is not normalized to the local metric. Surge reports 66.3% for Opus 5.5 (Adaptive/Max) on the standard 100-task leaderboard, with ten runs per task, Gemini 3.5 Flash judge, and accuracy/mean (Pass@1). Both scores are retained as distinct configurations."
      ],
      "status": "待核实",
      "unresolved": [
        "The Anthropic 89.0% result lacks enough published protocol details to compare with Surge standard-board 66.3%."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Opus 5.5 System Card",
          "url": "https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "System Card reports 74.2% pass@1 on 113 tasks, averaged across five trials, at max adaptive thinking. DataCurve leaderboard currently has no exact Opus 5.5 row; the System Card is the score source."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Anthropic reports 1846 for GDPval-AA v2.1 at max effort. Artificial Analysis currently lists Max 1866 (Default Fallback), Xhigh 1835, High 1714, Medium 1593, and Low 1240 on 220 tasks via Stirrup. The two Max results differ by 20 Elo; both are preserved because the sources do not explain the discrepancy. No evaluation date is stated."
      ],
      "status": "冲突",
      "unresolved": [
        "Anthropic launch report and current Artificial Analysis leaderboard report different Max scores for GDPval-AA v2.1 (1846 vs 1866); the reason is not published."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        },
        {
          "label": "Artificial Analysis HLE evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Anthropic reports 67.7% with tools; its release report does not state dataset size or evaluation date. Artificial Analysis separately reports 61.4% at Max with Default Fallback, pass@1 on 2,158 text-only questions from the original 2,500-question HLE set. These are distinct configurations."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2 official project",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "Anthropic identifies the result as OSWorld 2.1 and labels 81.8% as partial. The local v2.1 definition is binary task completion rate; the partial score is kept with its source metric and is not counted as a mapped binary-completion result. No evaluation date is stated."
      ],
      "status": "冲突",
      "unresolved": [
        "The verified 81.8% uses partial scoring, while the local Benchmark definition requires binary task completion rate."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Opus 5.5 System Card",
          "url": "https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf"
        },
        {
          "label": "Scale SWE-bench Pro V2 full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "The System Card reports 89.9% for SWE-bench Pro but does not identify V2; its cited paper is the 2025 Pro paper. The V2 full leaderboard has no exact Opus 5.5 row, so no V2 score was written."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot establish that the System Card 89.9% result used SWE-bench Pro V2 (642-task default configuration)."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Opus 5.5 System Card",
          "url": "https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf"
        },
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        },
        {
          "label": "Vals Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "System Card reports 58.7% at max effort with Claude Code --bare, ten trials per task (700 runs), and production safeguards/fallback. Vals separately reports 47.14% with Mini-SWE-agent; its page does not name the benchmark version, so that row has no version field. The repository version 0.1.0 is the canonical form of the source-labeled 0.1 release."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Opus 5.5 System Card",
          "url": "https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf"
        },
        {
          "label": "Anthropic launch report",
          "url": "https://www.anthropic.com/claude-opus-5-5"
        },
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "System Card gives the Anthropic run as 66.36%; the launch report rounds it to 66.4%. It used xhigh effort, Claude Code --bare and five trials per task (330 runs), with production safeguards and fallback. Vals separately reports 65.15% with Mini-SWE-agent; retained as a distinct source/configuration. The repository version 4.0.0 is the canonical form of the source-labeled 4.0 release."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T07:44+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Claude Opus 5.5 model profile",
          "url": "https://www.vals.ai/models/anthropic_claude-opus-5-5"
        }
      ],
      "notes": [
        "Vals reports 70.18% performance score at max effort, Anthropic as default provider, and 2.68% fallback rate. The composite covers finance, coding, legal, and tax tasks. The page update date is not treated as an evaluation date."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 9,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T07:44+08:00",
  "model_id": "anthropic/claude-opus-5-5",
  "new_records": 22,
  "overall_status": "待复核"
}

-->
