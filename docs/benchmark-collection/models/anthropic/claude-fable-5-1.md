# Claude Fable 5.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-fable-5-1
- 模型名称：Claude Fable 5.1
- 发布日期：2026-09-01
- 最近检查时间：2026-11-04T14:50+08:00
- 整体处理状态：待复核
- 新增成绩数量：25
- 收集前已有成绩数量：9
- 当前已收录的对应成绩数量：14

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 67.4 (metric=pass@1; version=1.1; dataset=113 long-horizon coding tasks; effort=max; variant=adaptive thinking; average over 5 trials; default sampling settings) | [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [DeepSWE v1.1 methodology and leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T14:50+08:00 |
| swe-bench-pro-v2 | 待核实 | 99.10 ± 0.50 (metric=resolve rate; version=V2; dataset=Full public split: 642 tasks across 11 repositories; effort=high; harness=Claude Code) | [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2) | 2026-11-04T14:50+08:00 |
| terminal-bench-v4 | 待核实 | 55.8 (metric=accuracy; version=4.0; dataset=66 tasks; effort=max; variant=production safeguards with fallback; harness=Claude Code --bare); 57.9 ± 3.8 (metric=resolution rate; version=4.0; dataset=66 tasks; effort=max; variant=95% confidence interval; harness=Claude Code); 57.9 ± 3.4 (metric=resolution rate; version=4.0; dataset=66 tasks; effort=xhigh; variant=95% confidence interval; harness=Claude Code); 54.5 ± 3.4 (metric=resolution rate; version=4.0; dataset=66 tasks; effort=high; variant=95% confidence interval; harness=Claude Code); 53.9 ± 3.4 (metric=resolution rate; version=4.0; dataset=66 tasks; effort=medium; variant=95% confidence interval; harness=Claude Code); 43.3 ± 3.6 (metric=resolution rate; version=4.0; dataset=66 tasks; effort=low; variant=95% confidence interval; harness=Claude Code); 58.08 ± 3.31 (metric=accuracy; version=4.0; dataset=66 tasks; effort=max; variant=avg@3; per-task pass@1; harness=Mini-SWE-agent) | [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Vals AI Terminal-Bench 4.0 results](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T14:50+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 52.6 (metric=accuracy; version=0.1; dataset=70 tasks; effort=max; variant=production safeguards with fallback; harness=Claude Code --bare); 40.00 ± 5.90 (metric=accuracy; version=0.1.0; dataset=70 tasks; effort=max; variant=single pass@1; harness=Mini-SWE-agent) | [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [Terminal-Bench Science v0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1), [Vals AI Terminal-Bench Science results](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T14:50+08:00 |
| automationbench-v1.0.6 | 待核实 | 31.4 (metric=task_completed_correctly; version=1.0.6; dataset=657 private held-out tasks; variant=with Opus 5 fallback on about 260 of 657 tasks; fallback completions count toward score); 22.37 (metric=task_completed_correctly; version=1.0.6; dataset=657 private held-out tasks; effort=Max; variant=no fallback; API mode; 50-step cap) | [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks), [AutomationBench scoring definition](https://github.com/zapier/AutomationBench), [Fireworks AutomationBench results](https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench), [LLMLeaderBoard AutomationBench results](https://llmleaderboard.com/benchmarks/automationbench), [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-04T14:50+08:00 |
| osworld-v2.1 | 冲突 | 77.9 (metric=partial score; version=2.0; dataset=August 2026 task release; variant=production safeguards; interventions score zero; no fallback); 41.7 (metric=strict success rate; version=2.0; dataset=August 2026 task release; variant=production safeguards; interventions score zero; no fallback) | [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [OSWorld 2.1 XLANG release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [AIB OSWorld 2.1 leaderboard](https://www.aib.vote/en/benchmarks/osworld-2-1) | 2026-11-04T14:50+08:00 |
| chartography | 待核实 | 46.2 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=Adaptive/Max; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI); 42.6 (metric=accuracy; dataset=100 tasks; effort=max; variant=without tools; adaptive thinking; mean of 5 runs; Sonnet 4.6 judge); 86.2 (metric=accuracy; dataset=100 tasks; effort=max; variant=with tools (container and image crop); adaptive thinking; mean of 5 runs; Sonnet 4.6 judge); 44.8 (metric=accuracy; dataset=100 tasks; effort=max; variant=without tools; adaptive thinking; mean of 5 runs; Gemini 3.5 Flash judge); 88.4 (metric=accuracy; dataset=100 tasks; effort=max; variant=with tools; adaptive thinking; mean of 5 runs; Gemini 3.5 Flash judge) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge Chartography README and methodology](https://github.com/surge-ai/chartography/blob/main/README.md), [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [Anthropic Opus 5.5 system card](https://www.anthropic.com/claude-opus-5-5-system-card) | 2026-11-04T14:50+08:00 |
| humanitys-last-exam | 已收录 | 60.9 (metric=accuracy; variant=without tools; production safeguards with fallback); 65 (metric=accuracy; variant=with tools; production safeguards with fallback); 59.1 (metric=accuracy; dataset=2,158 text-only questions from the original HLE set; effort=Max; variant=Default Fallback; Pass@1; GPT-5.6 Luna medium judge); 58.7 (metric=accuracy; dataset=2,158 text-only questions from the original HLE set; effort=Xhigh; variant=Default Fallback; Pass@1; GPT-5.6 Luna medium judge) | [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Artificial Analysis HLE leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T14:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 49 (metric=index score; version=5.0; effort=Max; variant=Default Fallback); 49 (metric=index score; version=5.0.1; effort=Max; variant=Default Fallback); 50 (metric=index score; version=5.0.1; effort=Xhigh; variant=Default Fallback) | [Artificial Analysis Fable 5.1 model record](https://artificialanalysis.ai/models/claude-fable-5-1?trk=article-ssr-frontend-pulse_little-text-block), [Artificial Analysis Fable 5.1 Xhigh comparison](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-xhigh-vs-claude-fable-5-1), [Artificial Analysis methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T14:50+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1853 (metric=Elo; version=2; variant=production safeguards with fallback); 1763 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Max; variant=Default Fallback; 95% CI -19/+19; harness=Stirrup); 1740 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Xhigh; variant=Default Fallback; 95% CI -19/+19; harness=Stirrup); 1644 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=High; variant=Default Fallback; 95% CI -18/+18; harness=Stirrup); 1554 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Medium; variant=Default Fallback; 95% CI -18/+18; harness=Stirrup); 1477 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Low; variant=Default Fallback; 95% CI -18/+18; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa), [Anthropic Fable 5.1 release results, GDPval-AA v2](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-04T14:50+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals AI Claude Fable 5.1 model profile](https://www.vals.ai/models/anthropic_claude-fable-5-1) | 2026-11-04T14:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 67.4
- metric: pass@1
- version: 1.1
- dataset: 113 long-horizon coding tasks
- effort: max
- variant: adaptive thinking; average over 5 trials; default sampling settings
- source: [https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [DeepSWE v1.1 methodology and leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 系统卡将 67.4% 归于 Claude Fable 5.1；采用 113 项任务、max effort、五次试验均值。官方榜单上的 Claude Fable 5 是不同模型，未用于本记录。来源未给出这项评测的发布日期，因此没有写入 date。

最近核验时间：2026-11-04T14:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 99.10 ± 0.50
- metric: resolve rate
- version: V2
- dataset: Full public split: 642 tasks across 11 repositories
- effort: high
- harness: Claude Code
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2)

研究备注：
- Scale 榜单列 Fable 5.1（Claude Code, high）99.10 ± 0.50；对应 Full public split 的 642 项任务。系统卡中的 81.2% 属于不同版本，未写入。

尚未解决的问题：
- 来源原文使用版本 V2 和指标 resolve rate；仓库定义是版本 2.0.0、task resolution rate。为保留源字段，TOML 未把版本或指标改写成定义值，因此该条仍待定义映射复核。

最近核验时间：2026-11-04T14:50+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 55.8
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- effort: max
- variant: production safeguards with fallback
- harness: Claude Code --bare
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 57.9 ± 3.8
- metric: resolution rate
- version: 4.0
- dataset: 66 tasks
- effort: max
- variant: 95% confidence interval
- harness: Claude Code
- source: [https://www.tbench.ai/?version=4.0&efforts=all](https://www.tbench.ai/?version=4.0&efforts=all)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 57.9 ± 3.4
- metric: resolution rate
- version: 4.0
- dataset: 66 tasks
- effort: xhigh
- variant: 95% confidence interval
- harness: Claude Code
- source: [https://www.tbench.ai/?version=4.0&efforts=all](https://www.tbench.ai/?version=4.0&efforts=all)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 54.5 ± 3.4
- metric: resolution rate
- version: 4.0
- dataset: 66 tasks
- effort: high
- variant: 95% confidence interval
- harness: Claude Code
- source: [https://www.tbench.ai/?version=4.0&efforts=all](https://www.tbench.ai/?version=4.0&efforts=all)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Terminal-Bench
- score: 53.9 ± 3.4
- metric: resolution rate
- version: 4.0
- dataset: 66 tasks
- effort: medium
- variant: 95% confidence interval
- harness: Claude Code
- source: [https://www.tbench.ai/?version=4.0&efforts=all](https://www.tbench.ai/?version=4.0&efforts=all)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 6

- name: Terminal-Bench
- score: 43.3 ± 3.6
- metric: resolution rate
- version: 4.0
- dataset: 66 tasks
- effort: low
- variant: 95% confidence interval
- harness: Claude Code
- source: [https://www.tbench.ai/?version=4.0&efforts=all](https://www.tbench.ai/?version=4.0&efforts=all)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 7

- name: Terminal-Bench
- score: 58.08 ± 3.31
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- effort: max
- variant: avg@3; per-task pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Vals AI Terminal-Bench 4.0 results](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 保留 Anthropic 的 55.8%（Claude Code --bare, max, 15 次/任务）、官方榜单的五个 effort 行，以及 Vals AI 的 Mini-SWE-agent 58.08 ± 3.31；各 harness 和采样配置分开存放。官方排行榜页可浏览，但网页文本提取没有显示结果行，行值由研究代理直接核验。

尚未解决的问题：
- 原始来源分别使用 accuracy / resolution rate 和版本 4.0；本地定义要求 task resolution rate、版本 4.0.0。保持来源标签后，相关行未精确映射，需复核定义兼容性。

最近核验时间：2026-11-04T14:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 52.6
- metric: accuracy
- version: 0.1
- dataset: 70 tasks
- effort: max
- variant: production safeguards with fallback
- harness: Claude Code --bare
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 40.00 ± 5.90
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- effort: max
- variant: single pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [Terminal-Bench Science v0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Vals AI Terminal-Bench Science results](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- 保留 Anthropic 52.6% 和 Vals AI Mini-SWE-agent 40.00 ± 5.90 两个不同配置；官方榜单列出的 Fable 5 不是 Fable 5.1。

尚未解决的问题：
- Anthropic 与 Vals 来源使用 accuracy，版本分别显示 0.1 或 0.1.0；本地定义要求 task resolution rate、版本 0.1.0。未将源指标改写成本地标签，映射需复核。

最近核验时间：2026-11-04T14:50+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 31.4
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 private held-out tasks
- variant: with Opus 5 fallback on about 260 of 657 tasks; fallback completions count toward score
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 22.37
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 private held-out tasks
- effort: Max
- variant: no fallback; API mode; 50-step cap
- source: [https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench](https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks)
- [AutomationBench scoring definition](https://github.com/zapier/AutomationBench)
- [Fireworks AutomationBench results](https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench)
- [LLMLeaderBoard AutomationBench results](https://llmleaderboard.com/benchmarks/automationbench)
- [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- Zapier 官方列出的 31.4% 是启用 Opus 5 fallback 的组合结果，约 260/657 项由 Opus 5 完成。另有两个独立榜单镜像给出纯 Fable 5.1 Max 22.37%，并报告 API 模式和 50 步上限；两者分开保留。

尚未解决的问题：
- Zapier 官方页可核实 fallback 组合分数，但没有找到纯 Fable 5.1 的对应官方排行榜行；22.37% 目前仅有独立镜像交叉核对，待官方来源确认。

最近核验时间：2026-11-04T14:50+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 77.9
- metric: partial score
- version: 2.0
- dataset: August 2026 task release
- variant: production safeguards; interventions score zero; no fallback
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: OSWorld
- score: 41.7
- metric: strict success rate
- version: 2.0
- dataset: August 2026 task release
- variant: production safeguards; interventions score zero; no fallback
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [OSWorld 2.1 XLANG release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [AIB OSWorld 2.1 leaderboard](https://www.aib.vote/en/benchmarks/osworld-2-1)

研究备注：
- TOML 中现有 77.9 partial / 41.7 strict 明确属于 OSWorld 2.0，保留但不计为 v2.1。没有把后续材料中有版本分歧的 80.7 partial 写入。

尚未解决的问题：
- Anthropic 后续发布材料把 80.7 partial 标为 OSWorld 2.1；System Card 对同一 80.7 partial / 42.8 strict run 则标为 OSWorld 2.0，并称使用 2026-09-10 任务文件。官方 v2.1 于 2026-09-16 发布，AIB 当前 v2.1 榜单也未列 Fable。版本无法确认，且本地定义仅接受 binary task completion rate。

最近核验时间：2026-11-04T14:50+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 46.2
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: Adaptive/Max
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Chartography
- score: 42.6
- metric: accuracy
- dataset: 100 tasks
- effort: max
- variant: without tools; adaptive thinking; mean of 5 runs; Sonnet 4.6 judge
- source: [https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Chartography
- score: 86.2
- metric: accuracy
- dataset: 100 tasks
- effort: max
- variant: with tools (container and image crop); adaptive thinking; mean of 5 runs; Sonnet 4.6 judge
- source: [https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Chartography
- score: 44.8
- metric: accuracy
- dataset: 100 tasks
- effort: max
- variant: without tools; adaptive thinking; mean of 5 runs; Gemini 3.5 Flash judge
- source: [https://www.anthropic.com/claude-opus-5-5-system-card](https://www.anthropic.com/claude-opus-5-5-system-card)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Chartography
- score: 88.4
- metric: accuracy
- dataset: 100 tasks
- effort: max
- variant: with tools; adaptive thinking; mean of 5 runs; Gemini 3.5 Flash judge
- source: [https://www.anthropic.com/claude-opus-5-5-system-card](https://www.anthropic.com/claude-opus-5-5-system-card)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography README and methodology](https://github.com/surge-ai/chartography/blob/main/README.md)
- [Anthropic Fable 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [Anthropic Opus 5.5 system card](https://www.anthropic.com/claude-opus-5-5-system-card)

研究备注：
- Surge 榜单列 Fable 5.1 Adaptive/Max 46.2，并给出 100 项测试、10 次运行、Inspect AI 和 Gemini 3.5 Flash judge。Anthropic 另报告 42.6/86.2（Sonnet 4.6 judge）及 44.8/88.4（Gemini 3.5 Flash judge），无工具和有工具结果分别保留。

尚未解决的问题：
- Surge 行与本地 metric 精确匹配；Anthropic 系统卡四条原始指标标为 accuracy，而本地定义要求 accuracy (mean; Pass@1)。未把这些来源标签强行规范化，四条记录的定义映射待复核。

最近核验时间：2026-11-04T14:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 60.9
- metric: accuracy
- variant: without tools; production safeguards with fallback
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 65
- metric: accuracy
- variant: with tools; production safeguards with fallback
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Humanity's Last Exam
- score: 59.1
- metric: accuracy
- dataset: 2,158 text-only questions from the original HLE set
- effort: Max
- variant: Default Fallback; Pass@1; GPT-5.6 Luna medium judge
- source: [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Humanity's Last Exam
- score: 58.7
- metric: accuracy
- dataset: 2,158 text-only questions from the original HLE set
- effort: Xhigh
- variant: Default Fallback; Pass@1; GPT-5.6 Luna medium judge
- source: [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Fable 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Artificial Analysis HLE leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Anthropic 的 60.9% without tools 与 65% with tools 是原版 HLE 结果，metric 为 accuracy。Artificial Analysis 另列 Max 59.1% 和 Xhigh 58.7%，使用原 HLE 中 2,158 道 text-only 题、Pass@1、Default Fallback 和 GPT-5.6 Luna medium judge；这些子集分数不覆盖 Anthropic 结果。

最近核验时间：2026-11-04T14:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 49
- metric: index score
- version: 5.0
- effort: Max
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-fable-5-1?trk=article-ssr-frontend-pulse_little-text-block](https://artificialanalysis.ai/models/claude-fable-5-1?trk=article-ssr-frontend-pulse_little-text-block)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 49
- metric: index score
- version: 5.0.1
- effort: Max
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/claude-fable-5-1](https://artificialanalysis.ai/models/claude-fable-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 50
- metric: index score
- version: 5.0.1
- effort: Xhigh
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-xhigh-vs-claude-fable-5-1](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-xhigh-vs-claude-fable-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Fable 5.1 model record](https://artificialanalysis.ai/models/claude-fable-5-1?trk=article-ssr-frontend-pulse_little-text-block)
- [Artificial Analysis Fable 5.1 Xhigh comparison](https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-xhigh-vs-claude-fable-5-1)
- [Artificial Analysis methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- V5.0 的 Max 49 精确对应仓库定义。另将当前 V5.0.1 的 Max 49 与 Xhigh 50 分开记录，没有混入 V5.0 覆盖统计。

最近核验时间：2026-11-04T14:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1853
- metric: Elo
- version: 2
- variant: production safeguards with fallback
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1763
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Max
- variant: Default Fallback; 95% CI -19/+19
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: GDPval-AA
- score: 1740
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Xhigh
- variant: Default Fallback; 95% CI -19/+19
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: GDPval-AA
- score: 1644
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: High
- variant: Default Fallback; 95% CI -18/+18
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: GDPval-AA
- score: 1554
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Medium
- variant: Default Fallback; 95% CI -18/+18
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: GDPval-AA
- score: 1477
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Low
- variant: Default Fallback; 95% CI -18/+18
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)
- [Anthropic Fable 5.1 release results, GDPval-AA v2](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- 当前官方 v2.1 榜单列出 Max 1763、Xhigh 1740、High 1644、Medium 1554、Low 1477 Elo，保留各行置信区间和 Default Fallback 条件。Anthropic 的 1853 属于 v2，继续作为独立既有记录。

尚未解决的问题：
- 曾见到的 Artificial Analysis 旧缓存快照中，Max、High、Medium、Low 比当前官方榜单各高 1 Elo（Xhigh 相同）。本次记录当前直接可见的官方值，但没有评测日期可用于判断这是榜单修订还是抓取版本差异。

最近核验时间：2026-11-04T14:50+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI Claude Fable 5.1 model profile](https://www.vals.ai/models/anthropic_claude-fable-5-1)

研究备注：
- 检查当前 v2.2 榜单和 Fable 5.1 模型页，未发现该模型的 v2.2 成绩。历史 v2/v2.1 记录未移作 v2.2。

最近核验时间：2026-11-04T14:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Fable 5.1 model record",
          "url": "https://artificialanalysis.ai/models/claude-fable-5-1?trk=article-ssr-frontend-pulse_little-text-block"
        },
        {
          "label": "Artificial Analysis Fable 5.1 Xhigh comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-xhigh-vs-claude-fable-5-1"
        },
        {
          "label": "Artificial Analysis methodology and version history",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "V5.0 的 Max 49 精确对应仓库定义。另将当前 V5.0.1 的 Max 49 与 Xhigh 50 分开记录，没有混入 V5.0 覆盖统计。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench v1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench scoring definition",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Fireworks AutomationBench results",
          "url": "https://fireworks.ai/specialized-intelligence-index/benchmarks/workflow-automation/automationbench"
        },
        {
          "label": "LLMLeaderBoard AutomationBench results",
          "url": "https://llmleaderboard.com/benchmarks/automationbench"
        },
        {
          "label": "Anthropic Fable 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "Zapier 官方列出的 31.4% 是启用 Opus 5 fallback 的组合结果，约 260/657 项由 Opus 5 完成。另有两个独立榜单镜像给出纯 Fable 5.1 Max 22.37%，并报告 API 模式和 50 步上限；两者分开保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 官方页可核实 fallback 组合分数，但没有找到纯 Fable 5.1 的对应官方排行榜行；22.37% 目前仅有独立镜像交叉核对，待官方来源确认。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography README and methodology",
          "url": "https://github.com/surge-ai/chartography/blob/main/README.md"
        },
        {
          "label": "Anthropic Fable 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "Anthropic Opus 5.5 system card",
          "url": "https://www.anthropic.com/claude-opus-5-5-system-card"
        }
      ],
      "notes": [
        "Surge 榜单列 Fable 5.1 Adaptive/Max 46.2，并给出 100 项测试、10 次运行、Inspect AI 和 Gemini 3.5 Flash judge。Anthropic 另报告 42.6/86.2（Sonnet 4.6 judge）及 44.8/88.4（Gemini 3.5 Flash judge），无工具和有工具结果分别保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "Surge 行与本地 metric 精确匹配；Anthropic 系统卡四条原始指标标为 accuracy，而本地定义要求 accuracy (mean; Pass@1)。未把这些来源标签强行规范化，四条记录的定义映射待复核。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "DeepSWE v1.1 methodology and leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "系统卡将 67.4% 归于 Claude Fable 5.1；采用 113 项任务、max effort、五次试验均值。官方榜单上的 Claude Fable 5 是不同模型，未用于本记录。来源未给出这项评测的发布日期，因此没有写入 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T14:50+08:00",
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
          "label": "Anthropic Fable 5.1 release results, GDPval-AA v2",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "当前官方 v2.1 榜单列出 Max 1763、Xhigh 1740、High 1644、Medium 1554、Low 1477 Elo，保留各行置信区间和 Default Fallback 条件。Anthropic 的 1853 属于 v2，继续作为独立既有记录。"
      ],
      "status": "待核实",
      "unresolved": [
        "曾见到的 Artificial Analysis 旧缓存快照中，Max、High、Medium、Low 比当前官方榜单各高 1 Elo（Xhigh 相同）。本次记录当前直接可见的官方值，但没有评测日期可用于判断这是榜单修订还是抓取版本差异。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Artificial Analysis HLE leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis intelligence benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Anthropic 的 60.9% without tools 与 65% with tools 是原版 HLE 结果，metric 为 accuracy。Artificial Analysis 另列 Max 59.1% 和 Xhigh 58.7%，使用原 HLE 中 2,158 道 text-only 题、Pass@1、Default Fallback 和 GPT-5.6 Luna medium judge；这些子集分数不覆盖 Anthropic 结果。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Fable 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "OSWorld 2.1 XLANG release manifest",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "AIB OSWorld 2.1 leaderboard",
          "url": "https://www.aib.vote/en/benchmarks/osworld-2-1"
        }
      ],
      "notes": [
        "TOML 中现有 77.9 partial / 41.7 strict 明确属于 OSWorld 2.0，保留但不计为 v2.1。没有把后续材料中有版本分歧的 80.7 partial 写入。"
      ],
      "status": "冲突",
      "unresolved": [
        "Anthropic 后续发布材料把 80.7 partial 标为 OSWorld 2.1；System Card 对同一 80.7 partial / 42.8 strict run 则标为 OSWorld 2.0，并称使用 2026-09-10 任务文件。官方 v2.1 于 2026-09-16 发布，AIB 当前 v2.1 榜单也未列 Fable。版本无法确认，且本地定义仅接受 binary task completion rate。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale V2 release and protocol",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        }
      ],
      "notes": [
        "Scale 榜单列 Fable 5.1（Claude Code, high）99.10 ± 0.50；对应 Full public split 的 642 项任务。系统卡中的 81.2% 属于不同版本，未写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源原文使用版本 V2 和指标 resolve rate；仓库定义是版本 2.0.0、task resolution rate。为保留源字段，TOML 未把版本或指标改写成定义值，因此该条仍待定义映射复核。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Fable 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "Terminal-Bench Science v0.1 release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Vals AI Terminal-Bench Science results",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "保留 Anthropic 52.6% 和 Vals AI Mini-SWE-agent 40.00 ± 5.90 两个不同配置；官方榜单列出的 Fable 5 不是 Fable 5.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "Anthropic 与 Vals 来源使用 accuracy，版本分别显示 0.1 或 0.1.0；本地定义要求 task resolution rate、版本 0.1.0。未将源指标改写成本地标签，映射需复核。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Fable 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Vals AI Terminal-Bench 4.0 results",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "保留 Anthropic 的 55.8%（Claude Code --bare, max, 15 次/任务）、官方榜单的五个 effort 行，以及 Vals AI 的 Mini-SWE-agent 58.08 ± 3.31；各 harness 和采样配置分开存放。官方排行榜页可浏览，但网页文本提取没有显示结果行，行值由研究代理直接核验。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始来源分别使用 accuracy / resolution rate 和版本 4.0；本地定义要求 task resolution rate、版本 4.0.0。保持来源标签后，相关行未精确映射，需复核定义兼容性。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T14:50+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI Claude Fable 5.1 model profile",
          "url": "https://www.vals.ai/models/anthropic_claude-fable-5-1"
        }
      ],
      "notes": [
        "检查当前 v2.2 榜单和 Fable 5.1 模型页，未发现该模型的 v2.2 成绩。历史 v2/v2.1 记录未移作 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 9,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T14:50+08:00",
  "model_id": "anthropic/claude-fable-5-1",
  "new_records": 25,
  "overall_status": "待复核"
}

-->
