# Claude Sonnet 5.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-sonnet-5-5
- 模型名称：Claude Sonnet 5.5
- 发布日期：2026-09-28
- 最近检查时间：2026-11-04T06:44+08:00
- 整体处理状态：待复核
- 新增成绩数量：17
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：15

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Datacurve DeepSWE 榜单](https://deepswe.datacurve.ai/), [Anthropic Sonnet 5.5 System Card](https://www.anthropic.com/claude-sonnet-5-5-system-card) | 2026-11-04T06:44+08:00 |
| swe-bench-pro-v2 | 已收录 | 95.79 ± 1.30 (metric=task resolution rate; version=2.0.0; dataset=V2 Full; 642 tasks across 11 repositories; effort=xhigh; harness=mini-swe-agent) | [Scale AI SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T06:44+08:00 |
| terminal-bench-v4 | 已收录 | 70.6 (metric=task resolution rate; version=4.0.0); 64.14 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=avg@3 (three runs, each pass@1); harness=mini-swe-agent) | [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5), [Vals AI Terminal-Bench 4 榜单](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T06:44+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 47.14 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=pass@1; single run; harness=mini-swe-agent) | [Vals AI Terminal-Bench-Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T06:44+08:00 |
| automationbench-v1.0.6 | 已收录 | 18.6 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Between tools; variant=strict scoring; Anthropic default fallbacks; harness=Zapier API; 50-step cap); 18.3 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Low; variant=strict scoring; Anthropic default fallbacks; harness=Zapier API; 50-step cap); 23.3 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Medium; variant=strict scoring; Anthropic default fallbacks; harness=Zapier API; 50-step cap); 29.4 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=High; variant=strict scoring; Anthropic default fallbacks; harness=Zapier API; 50-step cap); 36.8 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=XHigh; variant=strict scoring; Anthropic default fallbacks; harness=Zapier API; 50-step cap); 44.75 (metric=task_completed_correctly; version=1.0.6; dataset=657 held-out evaluation tasks; effort=Max; variant=strict scoring; Anthropic default fallbacks; harness=Zapier API; 50-step cap) | [Zapier Sonnet 5.5 评测报告](https://zapier.com/benchmarks/claude-sonnet5_5-report), [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks) | 2026-11-04T06:44+08:00 |
| osworld-v2.1 | 冲突 | 80.1 (metric=partial score; version=2.1) | [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5), [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T06:44+08:00 |
| chartography | 已收录 | 61.6 (metric=accuracy (mean; Pass@1); variant=no tools) | [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5), [Surge AI Chartography 榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 方法与代码仓库](https://github.com/surge-ai/chartography) | 2026-11-04T06:44+08:00 |
| humanitys-last-exam | 已存在 | 64.5 (metric=accuracy; variant=with tools) | [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5), [Anthropic Sonnet 5.5 System Card](https://www.anthropic.com/claude-sonnet-5-5-system-card) | 2026-11-04T06:44+08:00 |
| artificial-analysis-intelligence-index-v5 | 冲突 | 55 (metric=index score; version=5.0.1; effort=Max; variant=Default Fallback); 50 (metric=index score; version=5.0.1; effort=Xhigh; variant=Default Fallback); 42 (metric=index score; version=5.0.1; effort=High; variant=Default Fallback); 31 (metric=index score; version=5.0.1; effort=Medium; variant=Default Fallback); 26 (metric=index score; version=5.0.1; effort=Low; variant=Default Fallback) | [Artificial Analysis Claude Sonnet 5.5 模型页](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/), [Artificial Analysis Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T06:44+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1844 (metric=Elo rating; version=2.1; variant=pre-release Claude Platform deployment; Anthropic reports a structured-output issue); 1838 (metric=Elo rating; version=2.1; effort=Max; variant=Default Fallback) | [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5), [Artificial Analysis GDPval-AA v2.1 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T06:44+08:00 |
| vals-index-v2.2 | 已收录 | 70.85 (metric=performance score; version=2.2; effort=max) | [Vals AI Claude Sonnet 5.5 模型页](https://www.vals.ai/models/anthropic_claude-sonnet-5-5), [Vals Index v2.2 榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T06:44+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Datacurve DeepSWE 榜单](https://deepswe.datacurve.ai/)
- [Anthropic Sonnet 5.5 System Card](https://www.anthropic.com/claude-sonnet-5-5-system-card)

研究备注：
- Datacurve 当前公开榜单更新早于模型发布日期，不能据此判断该模型没有成绩。System Card 文件本次未能读取；第三方转述的分数未用于写入。

尚未解决的问题：
- 需要直接核对 Anthropic System Card 中 DeepSWE v1.1 的成绩及测试条件。

最近核验时间：2026-11-04T06:44+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 95.79 ± 1.30
- metric: task resolution rate
- version: 2.0.0
- dataset: V2 Full; 642 tasks across 11 repositories
- effort: xhigh
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 准确模型行：95.79 ± 1.30；V2 Full（642 tasks / 11 repositories），xhigh，mini-swe-agent。未把 HARD 子集混入；来源未给该行评测日期。

最近核验时间：2026-11-04T06:44+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 70.6
- metric: task resolution rate
- version: 4.0.0
- source: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 64.14
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: avg@3 (three runs, each pass@1)
- harness: mini-swe-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5)
- [Vals AI Terminal-Bench 4 榜单](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Anthropic 报告 70.6%，本地保留该来源结果；其 effort、harness 和实际评测日未公布。Vals 的 64.14% 是另一独立运行：mini-swe-agent、66 tasks、avg@3（三次 pass@1），没有替换 Anthropic 成绩。

最近核验时间：2026-11-04T06:44+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 47.14
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: pass@1; single run
- harness: mini-swe-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench-Science 榜单](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Vals 行为 47.14%；v0.1.0，70 tasks，mini-swe-agent，pass@1 单次运行。该行未公布 effort 或评测日期。

最近核验时间：2026-11-04T06:44+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 18.6
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Between tools
- variant: strict scoring; Anthropic default fallbacks
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- date: 2026-09-25
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 18.3
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Low
- variant: strict scoring; Anthropic default fallbacks
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- date: 2026-09-25
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 23.3
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Medium
- variant: strict scoring; Anthropic default fallbacks
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- date: 2026-09-25
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: AutomationBench
- score: 29.4
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: High
- variant: strict scoring; Anthropic default fallbacks
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- date: 2026-09-25
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: AutomationBench
- score: 36.8
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: XHigh
- variant: strict scoring; Anthropic default fallbacks
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks/claude-sonnet5_5-report](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- date: 2026-09-25
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 6

- name: AutomationBench
- score: 44.75
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 held-out evaluation tasks
- effort: Max
- variant: strict scoring; Anthropic default fallbacks
- harness: Zapier API; 50-step cap
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- date: 2026-09-25
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier Sonnet 5.5 评测报告](https://zapier.com/benchmarks/claude-sonnet5_5-report)
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)

研究备注：
- 收录 Between tools、Low、Medium、High、XHigh、Max 六档。每档 657 个 held-out tasks，strict task_completed_correctly；API 50-step cap；启用 Anthropic default fallbacks。报告注明一次 fallback 介入但任务失败。Max 使用官方榜单精度 44.75%，与报告中的一位小数展示一致。评测日期为报告明确的 2026-09-25。

最近核验时间：2026-11-04T06:44+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 80.1
- metric: partial score
- version: 2.1
- source: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5)
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 官方发布页报告 80.1% partial score；仓库定义要求 binary task completion rate，partial credit 不得混作二元完成率。保留源记录，但该行不计入本项精确成绩覆盖。来源没有公开评测日期。

尚未解决的问题：
- 本次未找到该模型 OSWorld v2.1 的 binary task completion rate。

最近核验时间：2026-11-04T06:44+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 61.6
- metric: accuracy (mean; Pass@1)
- variant: no tools
- source: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5)
- [Surge AI Chartography 榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 方法与代码仓库](https://github.com/surge-ai/chartography)

研究备注：
- Anthropic 发布页报告 61.6% no tools；本地方法定义将 accuracy/mean 作为 Pass@1。当前可见榜单没有 Sonnet 5.5 行；发布页未提供 epoch、harness 或实际评测日期。

最近核验时间：2026-11-04T06:44+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 64.5
- metric: accuracy
- variant: with tools
- source: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5)
- [Anthropic Sonnet 5.5 System Card](https://www.anthropic.com/claude-sonnet-5-5-system-card)

研究备注：
- 模型文件已有 64.5% with tools 的官方记录；当前发布表没有标为 HLE-Diamond。按原始 HLE 定义保存；来源未公布题集子集、effort 或评测日期，故未填 date。System Card 本次未能读取。

最近核验时间：2026-11-04T06:44+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 55
- metric: index score
- version: 5.0.1
- effort: Max
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 50
- metric: index score
- version: 5.0.1
- effort: Xhigh
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 42
- metric: index score
- version: 5.0.1
- effort: High
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Artificial Analysis Intelligence Index
- score: 31
- metric: index score
- version: 5.0.1
- effort: Medium
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 5

- name: Artificial Analysis Intelligence Index
- score: 26
- metric: index score
- version: 5.0.1
- effort: Low
- variant: Default Fallback
- source: [https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Claude Sonnet 5.5 模型页](https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/)
- [Artificial Analysis Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前模型页报告 Max/Xhigh/High/Medium/Low = 55/50/42/31/26，均为 Default Fallback；该页及方法标注 Index v5.0.1。已原样记录为 v5.0.1，不映射成本地定义 v5.0 的成绩。

尚未解决的问题：
- 仓库目标定义为 v5.0；当前可核实的 Sonnet 5.5 行为 v5.0.1，需确认是否存在可映射的 v5.0 同版结果。

最近核验时间：2026-11-04T06:44+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1844
- metric: Elo rating
- version: 2.1
- variant: pre-release Claude Platform deployment; Anthropic reports a structured-output issue
- source: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1838
- metric: Elo rating
- version: 2.1
- effort: Max
- variant: Default Fallback
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Sonnet 5.5 发布页](https://www.anthropic.com/claude-sonnet-5-5)
- [Artificial Analysis GDPval-AA v2.1 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 保留发布表的 1844 Elo：Anthropic 明确说明这次 AA 评测使用有结构化输出问题的预发布 Claude Platform 部署。另收录当前 AA 榜单的 1838 Elo（Max、Default Fallback）。两行运行/部署条件不同，未取最高值或合并。来源未公布实际评测日期。

最近核验时间：2026-11-04T06:44+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 70.85
- metric: performance score
- version: 2.2
- effort: max
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Claude Sonnet 5.5 模型页](https://www.vals.ai/models/anthropic_claude-sonnet-5-5)
- [Vals Index v2.2 榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 报告 70.85%；模型页显示 max compute effort。榜单更新日不是模型实际评测日，未填 date。

最近核验时间：2026-11-04T06:44+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Claude Sonnet 5.5 模型页",
          "url": "https://artificialanalysis.ai/models/releases/claude-sonnet-5-5/"
        },
        {
          "label": "Artificial Analysis Index 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前模型页报告 Max/Xhigh/High/Medium/Low = 55/50/42/31/26，均为 Default Fallback；该页及方法标注 Index v5.0.1。已原样记录为 v5.0.1，不映射成本地定义 v5.0 的成绩。"
      ],
      "status": "冲突",
      "unresolved": [
        "仓库目标定义为 v5.0；当前可核实的 Sonnet 5.5 行为 v5.0.1，需确认是否存在可映射的 v5.0 同版结果。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Zapier Sonnet 5.5 评测报告",
          "url": "https://zapier.com/benchmarks/claude-sonnet5_5-report"
        },
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "收录 Between tools、Low、Medium、High、XHigh、Max 六档。每档 657 个 held-out tasks，strict task_completed_correctly；API 50-step cap；启用 Anthropic default fallbacks。报告注明一次 fallback 介入但任务失败。Max 使用官方榜单精度 44.75%，与报告中的一位小数展示一致。评测日期为报告明确的 2026-09-25。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Sonnet 5.5 发布页",
          "url": "https://www.anthropic.com/claude-sonnet-5-5"
        },
        {
          "label": "Surge AI Chartography 榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 方法与代码仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Anthropic 发布页报告 61.6% no tools；本地方法定义将 accuracy/mean 作为 Pass@1。当前可见榜单没有 Sonnet 5.5 行；发布页未提供 epoch、harness 或实际评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Datacurve DeepSWE 榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Anthropic Sonnet 5.5 System Card",
          "url": "https://www.anthropic.com/claude-sonnet-5-5-system-card"
        }
      ],
      "notes": [
        "Datacurve 当前公开榜单更新早于模型发布日期，不能据此判断该模型没有成绩。System Card 文件本次未能读取；第三方转述的分数未用于写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要直接核对 Anthropic System Card 中 DeepSWE v1.1 的成绩及测试条件。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Sonnet 5.5 发布页",
          "url": "https://www.anthropic.com/claude-sonnet-5-5"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 榜单",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis 评测方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "保留发布表的 1844 Elo：Anthropic 明确说明这次 AA 评测使用有结构化输出问题的预发布 Claude Platform 部署。另收录当前 AA 榜单的 1838 Elo（Max、Default Fallback）。两行运行/部署条件不同，未取最高值或合并。来源未公布实际评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Sonnet 5.5 发布页",
          "url": "https://www.anthropic.com/claude-sonnet-5-5"
        },
        {
          "label": "Anthropic Sonnet 5.5 System Card",
          "url": "https://www.anthropic.com/claude-sonnet-5-5-system-card"
        }
      ],
      "notes": [
        "模型文件已有 64.5% with tools 的官方记录；当前发布表没有标为 HLE-Diamond。按原始 HLE 定义保存；来源未公布题集子集、effort 或评测日期，故未填 date。System Card 本次未能读取。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Sonnet 5.5 发布页",
          "url": "https://www.anthropic.com/claude-sonnet-5-5"
        },
        {
          "label": "OSWorld-V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "官方发布页报告 80.1% partial score；仓库定义要求 binary task completion rate，partial credit 不得混作二元完成率。保留源记录，但该行不计入本项精确成绩覆盖。来源没有公开评测日期。"
      ],
      "status": "冲突",
      "unresolved": [
        "本次未找到该模型 OSWorld v2.1 的 binary task completion rate。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 Full 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "准确模型行：95.79 ± 1.30；V2 Full（642 tasks / 11 repositories），xhigh，mini-swe-agent。未把 HARD 子集混入；来源未给该行评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Vals 行为 47.14%；v0.1.0，70 tasks，mini-swe-agent，pass@1 单次运行。该行未公布 effort 或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Sonnet 5.5 发布页",
          "url": "https://www.anthropic.com/claude-sonnet-5-5"
        },
        {
          "label": "Vals AI Terminal-Bench 4 榜单",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Anthropic 报告 70.6%，本地保留该来源结果；其 effort、harness 和实际评测日未公布。Vals 的 64.14% 是另一独立运行：mini-swe-agent、66 tasks、avg@3（三次 pass@1），没有替换 Anthropic 成绩。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T06:44+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Claude Sonnet 5.5 模型页",
          "url": "https://www.vals.ai/models/anthropic_claude-sonnet-5-5"
        },
        {
          "label": "Vals Index v2.2 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 报告 70.85%；模型页显示 max compute effort。榜单更新日不是模型实际评测日，未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T06:44+08:00",
  "model_id": "anthropic/claude-sonnet-5-5",
  "new_records": 17,
  "overall_status": "待复核"
}

-->
