# DeepSeek V4.1 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4.1-flash
- 模型名称：DeepSeek V4.1 Flash
- 发布日期：2026-09-10
- 最近检查时间：2026-11-04T11:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 收集前已有成绩数量：34
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 74.2 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=mini-swe-agent); 69.8 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=Claude Code); 65.6 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=Codex); 65.5 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=OpenCode); 66.2 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=Pi); 72.6 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=DeepSeek Harness minimal mode); 70.5 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=DeepSeek Harness standard mode); 67.6 (metric=resolved; version=1.1; variant=reasoning_effort=100; harness=DeepSeek Harness PTC mode) | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [DeepSWE v1.1 official leaderboard and protocol](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DeepSWE official result dataset](https://huggingface.co/datasets/datacurve/deep-swe) | 2026-11-04T11:58+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Scale official SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-04T11:58+08:00 |
| terminal-bench-v4 | 待核实 | 90.6 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=DeepSeek Harness minimal mode); 30.0 (metric=pass@1; version=3.0; variant=reasoning_effort=100; harness=DeepSeek Harness minimal mode); 31.2 (metric=pass@1; version=4.0; variant=reasoning_effort=100; harness=DeepSeek Harness minimal mode); 88.0 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=Claude Code); 84.1 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=Codex); 85.0 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=OpenCode); 86.1 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=Pi); 90.3 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=mini-swe-agent); 85.8 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=DeepSeek Harness standard mode); 85.8 (metric=pass@1; version=2.1; variant=reasoning_effort=100; harness=DeepSeek Harness PTC mode) | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Terminal-Bench 4 official current leaderboard](https://www.tbench.ai/?version=4), [Terminal-Bench 4 official release and protocol](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T11:58+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Terminal-Bench Science 0.1 official announcement and initial results](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench Science official live leaderboard](https://www.terminal-bench-science.ai/) | 2026-11-04T11:58+08:00 |
| automationbench-v1.0.6 | 待核实 | 54.8 (metric=pass@1; variant=reasoning_effort=100) | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Zapier official AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier official AutomationBench repository and methodology](https://github.com/zapier/AutomationBench) | 2026-11-04T11:58+08:00 |
| osworld-v2.1 | 待核实 | — | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [OSWorld v2.1 official public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official interactive leaderboard](https://osworld-v2.xlang.ai/) | 2026-11-04T11:58+08:00 |
| chartography | 已收录 | 78.9 (metric=pass@1; variant=reasoning_effort=100; with tools; harness=Claude Code); 11.6 (metric=accuracy (mean; Pass@1); dataset=100 tasks; 10 runs per task; effort=Max reasoning; harness=Inspect AI; Gemini 3.5 Flash judge) | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Surge official Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official evaluation repository and leaderboard configuration](https://github.com/surge-ai/chartography) | 2026-11-04T11:58+08:00 |
| humanitys-last-exam | 待核实 | 36.8 (metric=pass@1; dataset=full set; variant=reasoning_effort=100); 39.1 (metric=pass@1; dataset=text-only subset; variant=reasoning_effort=100); 63.9 (metric=pass@1; variant=reasoning_effort=100; with tools) | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Artificial Analysis official Humanity's Last Exam evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T11:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Artificial Analysis official Intelligence Index v5 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis exact-model profile](https://artificialanalysis.ai/models/deepseek-v4-1-flash) | 2026-11-04T11:58+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1600 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Max; variant=Artificial Analysis leaderboard anchor; harness=Stirrup shell and web agent loop) | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Artificial Analysis official GDPval-AA v2.1 evaluation and leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis exact-model profile](https://artificialanalysis.ai/models/deepseek-v4-1-flash) | 2026-11-04T11:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), [DeepSeek official API update log](https://api-docs.deepseek.com/updates/), [Vals official Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T11:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 74.2
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: mini-swe-agent
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 69.8
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: Claude Code
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: DeepSWE
- score: 65.6
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: Codex
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: DeepSWE
- score: 65.5
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: OpenCode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: DeepSWE
- score: 66.2
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: Pi
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 6

- name: DeepSWE
- score: 72.6
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 7

- name: DeepSWE
- score: 70.5
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: DeepSeek Harness standard mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 8

- name: DeepSWE
- score: 67.6
- metric: resolved
- version: 1.1
- variant: reasoning_effort=100
- harness: DeepSeek Harness PTC mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [DeepSWE v1.1 official leaderboard and protocol](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DeepSWE official result dataset](https://huggingface.co/datasets/datacurve/deep-swe)

研究备注：
- The source TOML contains eight exact V4.1 Flash results (74.2, 69.8, 65.6, 65.5, 66.2, 72.6, 70.5, 67.6), all confirmed against the official DeepSeek card with version 1.1, reasoning_effort=100, and separately named harnesses.
- The source metric is 'resolved', while the local DeepSWE definition uses 'pass@1'. Preserve the source metric; these rows do not map to the local definition's exact metric and are not counted as mapped coverage. The later V4.1-Flash-1017 result is a different checkpoint.

尚未解决的问题：
- The local definition's pass@1 metric and the official card's resolved metric need an explicit mapping decision; no source metric was rewritten.

最近核验时间：2026-11-04T11:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Scale official SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- The official V2 leaderboard was checked and does not list this exact checkpoint. The model card's SEC-Bench Pro result is a different benchmark and was not mapped.

最近核验时间：2026-11-04T11:58+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 90.6
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 30.0
- metric: pass@1
- version: 3.0
- variant: reasoning_effort=100
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 31.2
- metric: pass@1
- version: 4.0
- variant: reasoning_effort=100
- harness: DeepSeek Harness minimal mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 88.0
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: Claude Code
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Terminal-Bench
- score: 84.1
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: Codex
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 6

- name: Terminal-Bench
- score: 85.0
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: OpenCode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 7

- name: Terminal-Bench
- score: 86.1
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: Pi
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 8

- name: Terminal-Bench
- score: 90.3
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: mini-swe-agent
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 9

- name: Terminal-Bench
- score: 85.8
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: DeepSeek Harness standard mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 10

- name: Terminal-Bench
- score: 85.8
- metric: pass@1
- version: 2.1
- variant: reasoning_effort=100
- harness: DeepSeek Harness PTC mode
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Terminal-Bench 4 official current leaderboard](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4 official release and protocol](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- The source TOML contains 31.2, pass@1, version 4.0, reasoning_effort=100, DeepSeek Harness minimal mode; the official DeepSeek card confirms these values and conditions for V4.1 Flash.
- The repository definition specifies version 4.0.0 and metric 'task resolution rate'; the source reports version 4.0 and pass@1. Preserve the original source fields and leave this row unmapped pending an explicit equivalence decision. The live leaderboard's rows could not be inspected.

尚未解决的问题：
- The source row's 4.0/pass@1 fields do not exactly match the local definition's 4.0.0/task resolution rate.

最近核验时间：2026-11-04T11:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Terminal-Bench Science 0.1 official announcement and initial results](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench Science official live leaderboard](https://www.terminal-bench-science.ai/)

研究备注：
- No source TOML or DeepSeek model-card result is present for this benchmark. The initial results predate the 2026-09-10 release; current live leaderboard rows could not be read, so a post-release result cannot be ruled out.

尚未解决的问题：
- The current leaderboard's model rows remain unavailable for exact V4.1 Flash verification.

最近核验时间：2026-11-04T11:58+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 54.8
- metric: pass@1
- variant: reasoning_effort=100
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Zapier official AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier official AutomationBench repository and methodology](https://github.com/zapier/AutomationBench)

研究备注：
- The source TOML's exact V4.1 Flash row is 54.8, pass@1, reasoning_effort=100; the DeepSeek card and official update log confirm it and say the official scaffold was used with temperature=1.0 and top_p=0.95.
- The result source does not state benchmark version or dataset. The local target is v1.0.6 and defines task_completed_correctly on a held-out private set, so the row is not mapped to this exact definition. Zapier's current page shows only part of the list.

尚未解决的问题：
- The score's AutomationBench version, task set, and metric equivalence to the v1.0.6 held-out leaderboard are unverified.

最近核验时间：2026-11-04T11:58+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [OSWorld v2.1 official public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official interactive leaderboard](https://osworld-v2.xlang.ai/)

研究备注：
- No OSWorld row appears in the source TOML, DeepSeek model card, or official release log. The v2.1 guideline was checked; the interactive current leaderboard's complete model rows were not available in page extraction.

尚未解决的问题：
- An exact V4.1 Flash v2.1 result cannot be verified from the current interactive leaderboard.

最近核验时间：2026-11-04T11:58+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 78.9
- metric: pass@1
- variant: reasoning_effort=100; with tools
- harness: Claude Code
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Chartography
- score: 11.6
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks; 10 runs per task
- effort: Max reasoning
- harness: Inspect AI; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Surge official Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official evaluation repository and leaderboard configuration](https://github.com/surge-ai/chartography)

研究备注：
- Added the official Surge leaderboard entry for DeepSeek V4.1 Flash (Max reasoning): 11.6%. The official repository defines the leaderboard's accuracy/mean (Pass@1) metric and configuration as the complete 100-task set, ten runs per task, Inspect AI harness, and Gemini 3.5 Flash judge.
- The existing official DeepSeek card row is a separate 78.9 Pass@1 result explicitly marked with tools (Claude Code harness, max effort, 512k context). Both records are retained separately; the current Surge row does not publish a model-specific tool setting. The existing 78.9 source row retains its original metric label and is not counted as an exact local-definition mapping.

最近核验时间：2026-11-04T11:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 36.8
- metric: pass@1
- dataset: full set
- variant: reasoning_effort=100
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 39.1
- metric: pass@1
- dataset: text-only subset
- variant: reasoning_effort=100
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Humanity's Last Exam
- score: 63.9
- metric: pass@1
- variant: reasoning_effort=100; with tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Artificial Analysis official Humanity's Last Exam evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Three existing source rows are confirmed against the official DeepSeek card: 36.8 HLE Pass@1, 39.1† text-only subset, and 63.9 HLE with tools. The HLE page defines the target as the original 2,500-question multimodal set; the source does not specify the exact version or full dataset scope for the with-tools row.
- The model card uses metric 'pass@1' while the local definition uses 'accuracy'. Existing source values and variants were preserved; no duplicate rows were added.

尚未解决的问题：
- The source metric label and local accuracy metric do not exactly map; the with-tools row's dataset scope and harness are not stated.

最近核验时间：2026-11-04T11:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Artificial Analysis official Intelligence Index v5 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis exact-model profile](https://artificialanalysis.ai/models/deepseek-v4-1-flash)

研究备注：
- The exact-model profile currently shows no Intelligence Index result. The current Index is v5.0.1 and no exact V4.1 Flash result was found; component scores such as HLE-Diamond or GDP.pdf are not the full Index.

最近核验时间：2026-11-04T11:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1600
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Max
- variant: Artificial Analysis leaderboard anchor
- harness: Stirrup shell and web agent loop
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Artificial Analysis official GDPval-AA v2.1 evaluation and leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis exact-model profile](https://artificialanalysis.ai/models/deepseek-v4-1-flash)

研究备注：
- Added the official leaderboard anchor for DeepSeek V4.1 Flash (Max) at 1600 Elo. The page defines GDPval-AA v2.1 as 220 tasks across 44 occupations and 9 industries, using Stirrup with shell and web access and blinded pairwise comparisons. The model card ties max effort to reasoning_effort=100.
- No source gives the evaluation date; the release date and leaderboard page update date were not copied into the record.

最近核验时间：2026-11-04T11:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSeek V4.1 Flash official model card and evaluation table](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [DeepSeek official API update log](https://api-docs.deepseek.com/updates/)
- [Vals official Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The current v2.2 leaderboard lists DeepSeek V4.1 Flash 1017, not this September V4.1 Flash checkpoint. The later 1017 score was not transferred.

最近核验时间：2026-11-04T11:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Artificial Analysis official Intelligence Index v5 page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis exact-model profile",
          "url": "https://artificialanalysis.ai/models/deepseek-v4-1-flash"
        }
      ],
      "notes": [
        "The exact-model profile currently shows no Intelligence Index result. The current Index is v5.0.1 and no exact V4.1 Flash result was found; component scores such as HLE-Diamond or GDP.pdf are not the full Index."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Zapier official AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier official AutomationBench repository and methodology",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "The source TOML's exact V4.1 Flash row is 54.8, pass@1, reasoning_effort=100; the DeepSeek card and official update log confirm it and say the official scaffold was used with temperature=1.0 and top_p=0.95.",
        "The result source does not state benchmark version or dataset. The local target is v1.0.6 and defines task_completed_correctly on a held-out private set, so the row is not mapped to this exact definition. Zapier's current page shows only part of the list."
      ],
      "status": "待核实",
      "unresolved": [
        "The score's AutomationBench version, task set, and metric equivalence to the v1.0.6 held-out leaderboard are unverified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Surge official Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official evaluation repository and leaderboard configuration",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Added the official Surge leaderboard entry for DeepSeek V4.1 Flash (Max reasoning): 11.6%. The official repository defines the leaderboard's accuracy/mean (Pass@1) metric and configuration as the complete 100-task set, ten runs per task, Inspect AI harness, and Gemini 3.5 Flash judge.",
        "The existing official DeepSeek card row is a separate 78.9 Pass@1 result explicitly marked with tools (Claude Code harness, max effort, 512k context). Both records are retained separately; the current Surge row does not publish a model-specific tool setting. The existing 78.9 source row retains its original metric label and is not counted as an exact local-definition mapping."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard and protocol",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DeepSWE official result dataset",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe"
        }
      ],
      "notes": [
        "The source TOML contains eight exact V4.1 Flash results (74.2, 69.8, 65.6, 65.5, 66.2, 72.6, 70.5, 67.6), all confirmed against the official DeepSeek card with version 1.1, reasoning_effort=100, and separately named harnesses.",
        "The source metric is 'resolved', while the local DeepSWE definition uses 'pass@1'. Preserve the source metric; these rows do not map to the local definition's exact metric and are not counted as mapped coverage. The later V4.1-Flash-1017 result is a different checkpoint."
      ],
      "status": "待核实",
      "unresolved": [
        "The local definition's pass@1 metric and the official card's resolved metric need an explicit mapping decision; no source metric was rewritten."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Artificial Analysis official GDPval-AA v2.1 evaluation and leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis exact-model profile",
          "url": "https://artificialanalysis.ai/models/deepseek-v4-1-flash"
        }
      ],
      "notes": [
        "Added the official leaderboard anchor for DeepSeek V4.1 Flash (Max) at 1600 Elo. The page defines GDPval-AA v2.1 as 220 tasks across 44 occupations and 9 industries, using Stirrup with shell and web access and blinded pairwise comparisons. The model card ties max effort to reasoning_effort=100.",
        "No source gives the evaluation date; the release date and leaderboard page update date were not copied into the record."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Artificial Analysis official Humanity's Last Exam evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Three existing source rows are confirmed against the official DeepSeek card: 36.8 HLE Pass@1, 39.1† text-only subset, and 63.9 HLE with tools. The HLE page defines the target as the original 2,500-question multimodal set; the source does not specify the exact version or full dataset scope for the with-tools row.",
        "The model card uses metric 'pass@1' while the local definition uses 'accuracy'. Existing source values and variants were preserved; no duplicate rows were added."
      ],
      "status": "待核实",
      "unresolved": [
        "The source metric label and local accuracy metric do not exactly map; the with-tools row's dataset scope and harness are not stated."
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "OSWorld v2.1 official public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld official interactive leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "No OSWorld row appears in the source TOML, DeepSeek model card, or official release log. The v2.1 guideline was checked; the interactive current leaderboard's complete model rows were not available in page extraction."
      ],
      "status": "待核实",
      "unresolved": [
        "An exact V4.1 Flash v2.1 result cannot be verified from the current interactive leaderboard."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Scale official SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "The official V2 leaderboard was checked and does not list this exact checkpoint. The model card's SEC-Bench Pro result is a different benchmark and was not mapped."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Terminal-Bench Science 0.1 official announcement and initial results",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench Science official live leaderboard",
          "url": "https://www.terminal-bench-science.ai/"
        }
      ],
      "notes": [
        "No source TOML or DeepSeek model-card result is present for this benchmark. The initial results predate the 2026-09-10 release; current live leaderboard rows could not be read, so a post-release result cannot be ruled out."
      ],
      "status": "待核实",
      "unresolved": [
        "The current leaderboard's model rows remain unavailable for exact V4.1 Flash verification."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Terminal-Bench 4 official current leaderboard",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4 official release and protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "The source TOML contains 31.2, pass@1, version 4.0, reasoning_effort=100, DeepSeek Harness minimal mode; the official DeepSeek card confirms these values and conditions for V4.1 Flash.",
        "The repository definition specifies version 4.0.0 and metric 'task resolution rate'; the source reports version 4.0 and pass@1. Preserve the original source fields and leave this row unmapped pending an explicit equivalence decision. The live leaderboard's rows could not be inspected."
      ],
      "status": "待核实",
      "unresolved": [
        "The source row's 4.0/pass@1 fields do not exactly match the local definition's 4.0.0/task resolution rate."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T11:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4.1 Flash official model card and evaluation table",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
        },
        {
          "label": "DeepSeek official API update log",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Vals official Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The current v2.2 leaderboard lists DeepSeek V4.1 Flash 1017, not this September V4.1 Flash checkpoint. The later 1017 score was not transferred."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 34,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T11:58+08:00",
  "model_id": "deepseek/deepseek-v4.1-flash",
  "new_records": 2,
  "overall_status": "待复核"
}

-->
