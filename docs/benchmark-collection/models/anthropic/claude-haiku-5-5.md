# Claude Haiku 5.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-haiku-5-5
- 模型名称：Claude Haiku 5.5
- 发布日期：2026-10-07
- 最近检查时间：2026-11-04T03:52+08:00
- 整体处理状态：待复核
- 新增成绩数量：15
- 收集前已有成绩数量：8
- 当前已收录的对应成绩数量：16

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DataCurve DeepSWE leaderboard](https://deepswe.datacurve.ai/), [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5) | 2026-11-04T03:52+08:00 |
| swe-bench-pro-v2 | 已收录 | 87.23 ± 2.36 (metric=task resolution rate; version=2.0.0; dataset=V2 Full; 642 tasks across 11 repositories; effort=high; harness=mini-swe-agent) | [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T03:52+08:00 |
| terminal-bench-v4 | 已收录 | 39.2 (metric=score; version=4.0); 36.36 ± 2.31 (metric=task resolution rate; version=4.0.0; harness=Mini-SWE-agent) | [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5), [Vals AI Terminal-Bench 4 leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-4) | 2026-11-04T03:52+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 10.00 ± 3.61 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=single pass@1 run per model; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench-Science leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-science), [Terminal-Bench Science 0.1 official release](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T03:52+08:00 |
| automationbench-v1.0.6 | 已收录 | 6.1 (metric=task_completed_correctly; version=1.0.6; dataset=657 tasks per effort; effort=Low; variant=strict scoring; default fallbacks enabled with no fallback calls; 50-step cap); 8.5 (metric=task_completed_correctly; version=1.0.6; dataset=657 tasks per effort; effort=Medium; variant=strict scoring; default fallbacks enabled with no fallback calls; 50-step cap); 10.5 (metric=task_completed_correctly; version=1.0.6; dataset=657 tasks per effort; effort=High; variant=strict scoring; default fallbacks enabled with no fallback calls; 50-step cap); 9.9 (metric=task_completed_correctly; version=1.0.6; dataset=657 tasks per effort; effort=XHigh; variant=strict scoring; default fallbacks enabled with no fallback calls; 50-step cap); 12.0 (metric=task_completed_correctly; version=1.0.6; dataset=657 tasks per effort; effort=Max; variant=strict scoring; default fallbacks enabled with no fallback calls; 50-step cap) | [Zapier Claude Haiku 5.5 AutomationBench report](https://zapier.com/benchmarks/claude-haiku5_5-report), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T03:52+08:00 |
| osworld-v2.1 | 待核实 | 72.4 (metric=partial score; version=2.1; variant=offline subset) | [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5), [OSWorld official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T03:52+08:00 |
| chartography | 待核实 | 46.4 (metric=score; variant=no tools) | [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5), [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and protocol](https://arxiv.org/html/2608.10677v1) | 2026-11-04T03:52+08:00 |
| humanitys-last-exam | 待核实 | 45.9 (metric=score; variant=no tools); 57.4 (metric=score; variant=with tools) | [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5), [Scale AI HLE leaderboard and version notice](https://labs.scale.com/leaderboard/humanitys_last_exam), [Original HLE paper](https://arxiv.org/abs/2501.14249) | 2026-11-04T03:52+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 36 (metric=index score; version=5.0; effort=Max); 34 (metric=index score; version=5.0; effort=Xhigh); 30 (metric=index score; version=5.0; effort=High); 25 (metric=index score; version=5.0; effort=Medium); 19 (metric=index score; version=5.0; effort=Low) | [Artificial Analysis Claude Haiku 5.5 release page](https://artificialanalysis.ai/models/releases/claude-haiku-5-5) | 2026-11-04T03:52+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1620 (metric=Elo rating; version=2.1); 1283 (-20/+20) (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Medium; harness=Stirrup shell+web) | [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5), [Artificial Analysis GDPval-AA leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T03:52+08:00 |
| vals-index-v2.2 | 已收录 | 58.73 ± 1.28 (metric=performance score; version=2.2; effort=Max) | [Vals AI Claude Haiku 5.5 model profile](https://www.vals.ai/models/anthropic_claude-haiku-5-5), [Vals Index benchmark definition](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T03:52+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DataCurve DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5)

研究备注：
- 未找到 Claude Haiku 5.5 的公开 DeepSWE v1.1 成绩。DataCurve 榜单快照的更新时间早于模型发布日期，因此该结果仅表示当前可核验资料中未找到。

最近核验时间：2026-11-04T03:52+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 87.23 ± 2.36
- metric: task resolution rate
- version: 2.0.0
- dataset: V2 Full; 642 tasks across 11 repositories
- effort: high
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 新增 V2 Full 成绩 87.23 ± 2.36 Resolve Rate，mini-swe-agent，high effort；来源说明为 642 tasks / 11 repositories。未公布评测日期。

最近核验时间：2026-11-04T03:52+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 39.2
- metric: score
- version: 4.0
- source: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 36.36 ± 2.31
- metric: task resolution rate
- version: 4.0.0
- harness: Mini-SWE-agent
- source: [https://vals-ai.com/benchmarks/terminal-bench-4](https://vals-ai.com/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5)
- [Vals AI Terminal-Bench 4 leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-4)

研究备注：
- 保留 Anthropic 公布的 39.2（来源未给出 harness、effort 或评测日），另收录 Vals AI Mini-SWE-agent 的 36.36 ± 2.31。Vals 说明每项任务严格 pass/fail，三次独立运行取均值、单次 pass@1；两条记录来自不同来源和运行配置，不合并。

最近核验时间：2026-11-04T03:52+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 10.00 ± 3.61
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: single pass@1 run per model
- harness: Mini-SWE-agent
- source: [https://vals-ai.com/benchmarks/terminal-bench-science](https://vals-ai.com/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench-Science leaderboard and methodology](https://vals-ai.com/benchmarks/terminal-bench-science)
- [Terminal-Bench Science 0.1 official release](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 新增 Vals AI 的 10.00 ± 3.61。上游 v0.1.0 共 70 项任务；Vals 的 harness 为 Mini-SWE-agent，单次 pass@1，所有任务严格判定通过/失败。无评测日期或 effort。

最近核验时间：2026-11-04T03:52+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 6.1
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 tasks per effort
- effort: Low
- variant: strict scoring; default fallbacks enabled with no fallback calls; 50-step cap
- source: [https://zapier.com/benchmarks/claude-haiku5_5-report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- date: 2026-10-05
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 8.5
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 tasks per effort
- effort: Medium
- variant: strict scoring; default fallbacks enabled with no fallback calls; 50-step cap
- source: [https://zapier.com/benchmarks/claude-haiku5_5-report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- date: 2026-10-05
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 10.5
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 tasks per effort
- effort: High
- variant: strict scoring; default fallbacks enabled with no fallback calls; 50-step cap
- source: [https://zapier.com/benchmarks/claude-haiku5_5-report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- date: 2026-10-05
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: AutomationBench
- score: 9.9
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 tasks per effort
- effort: XHigh
- variant: strict scoring; default fallbacks enabled with no fallback calls; 50-step cap
- source: [https://zapier.com/benchmarks/claude-haiku5_5-report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- date: 2026-10-05
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: AutomationBench
- score: 12.0
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 tasks per effort
- effort: Max
- variant: strict scoring; default fallbacks enabled with no fallback calls; 50-step cap
- source: [https://zapier.com/benchmarks/claude-haiku5_5-report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- date: 2026-10-05
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier Claude Haiku 5.5 AutomationBench report](https://zapier.com/benchmarks/claude-haiku5_5-report)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- 新增 Low 6.1%、Medium 8.5%、High 10.5%、XHigh 9.9%、Max 12.0%；每个 effort 657 项，严格 task_completed_correctly。报告给出的 run date 为 2026-10-05，API 模式、50-step 上限；默认 fallback 开启但未实际调用 fallback 模型。

最近核验时间：2026-11-04T03:52+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 72.4
- metric: partial score
- version: 2.1
- variant: offline subset
- source: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5)
- [OSWorld official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 保留 Anthropic 的 72.4% Offline subset 原始成绩；该页面未给出评测日期、effort 或 harness。TOML 原有 partial score 标记不是仓库定义的 binary task completion rate，未转成 binary 分数或计入精确映射覆盖。

尚未解决的问题：
- Anthropic 页面仅称 Offline subset，未直接说明 partial reward；具体指标与 OSWorld 2.1 binary completion 定义的对应关系仍需核实。

最近核验时间：2026-11-04T03:52+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 46.4
- metric: score
- variant: no tools
- source: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5)
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and protocol](https://arxiv.org/html/2608.10677v1)

研究备注：
- 保留 Anthropic 发布的 46.4% no tools。官方榜单当前未列出该模型；发布页没有说明是否采用官方 mean Pass@1 协议、harness 或评测日期，故未强行映射本地 accuracy (mean; Pass@1) 定义。

尚未解决的问题：
- Anthropic 报告的 score 是否使用官方 Chartography mean Pass@1 协议和相同测试配置尚未确认。

最近核验时间：2026-11-04T03:52+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 45.9
- metric: score
- variant: no tools
- source: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 57.4
- metric: score
- variant: with tools
- source: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5)
- [Scale AI HLE leaderboard and version notice](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Original HLE paper](https://arxiv.org/abs/2501.14249)

研究备注：
- 保留 Anthropic 原始公布的 no tools 45.9 和 with tools 57.4，不把 2026-10-07 发布日作为评测日期。Scale 页面将 2026-09-17 起的榜单标记为 HLE-Rolling；其 Haiku 5.5 结果不能映射为本地原始 2,500 题 HLE。

尚未解决的问题：
- Anthropic 未说明两条分数所用题集是原始 HLE 还是 HLE-Rolling，且未给出 harness、effort 或测试日期；暂不能映射到本地 original HLE accuracy 定义。

最近核验时间：2026-11-04T03:52+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 36
- metric: index score
- version: 5.0
- effort: Max
- source: [https://artificialanalysis.ai/models/releases/claude-haiku-5-5](https://artificialanalysis.ai/models/releases/claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Artificial Analysis Intelligence Index
- score: 34
- metric: index score
- version: 5.0
- effort: Xhigh
- source: [https://artificialanalysis.ai/models/releases/claude-haiku-5-5](https://artificialanalysis.ai/models/releases/claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Artificial Analysis Intelligence Index
- score: 30
- metric: index score
- version: 5.0
- effort: High
- source: [https://artificialanalysis.ai/models/releases/claude-haiku-5-5](https://artificialanalysis.ai/models/releases/claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Artificial Analysis Intelligence Index
- score: 25
- metric: index score
- version: 5.0
- effort: Medium
- source: [https://artificialanalysis.ai/models/releases/claude-haiku-5-5](https://artificialanalysis.ai/models/releases/claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 5

- name: Artificial Analysis Intelligence Index
- score: 19
- metric: index score
- version: 5.0
- effort: Low
- source: [https://artificialanalysis.ai/models/releases/claude-haiku-5-5](https://artificialanalysis.ai/models/releases/claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Claude Haiku 5.5 release page](https://artificialanalysis.ai/models/releases/claude-haiku-5-5)

研究备注：
- 新增官方明确标为 V5.0 的全部五档分数：Max 36、Xhigh 34、High 30、Medium 25、Low 19。没有公布评测日期。

最近核验时间：2026-11-04T03:52+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1620
- metric: Elo rating
- version: 2.1
- source: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1283 (-20/+20)
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Medium
- harness: Stirrup shell+web
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic release page](https://www.anthropic.com/claude-haiku-5-5)
- [Artificial Analysis GDPval-AA leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 将已有 Anthropic 1620 行指标规范为本地定义 Elo rating；AA 方法说明为 220 tasks / 44 occupations，通过 Stirrup shell+web 测试并进行 Elo 配对比较。AA 另列 Medium effort 1283 (-20/+20)，作为不同 effort 的独立记录。Anthropic 的 1620 没有注明 effort，页面也未给出评测日期。

最近核验时间：2026-11-04T03:52+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 58.73 ± 1.28
- metric: performance score
- version: 2.2
- effort: Max
- source: [https://www.vals.ai/models/anthropic_claude-haiku-5-5](https://www.vals.ai/models/anthropic_claude-haiku-5-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Claude Haiku 5.5 model profile](https://www.vals.ai/models/anthropic_claude-haiku-5-5)
- [Vals Index benchmark definition](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 新增 58.73 ± 1.28，profile 显示 Vals Index、accuracy 与区间；该模型评测配置标明 Compute Effort: max。未使用旧页面历史值 54.31，也未填页面更新日为评测日。

最近核验时间：2026-11-04T03:52+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Claude Haiku 5.5 release page",
          "url": "https://artificialanalysis.ai/models/releases/claude-haiku-5-5"
        }
      ],
      "notes": [
        "新增官方明确标为 V5.0 的全部五档分数：Max 36、Xhigh 34、High 30、Medium 25、Low 19。没有公布评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Zapier Claude Haiku 5.5 AutomationBench report",
          "url": "https://zapier.com/benchmarks/claude-haiku5_5-report"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "新增 Low 6.1%、Medium 8.5%、High 10.5%、XHigh 9.9%、Max 12.0%；每个 effort 657 项，严格 task_completed_correctly。报告给出的 run date 为 2026-10-05，API 模式、50-step 上限；默认 fallback 开启但未实际调用 fallback 模型。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Anthropic release page",
          "url": "https://www.anthropic.com/claude-haiku-5-5"
        },
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper and protocol",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "保留 Anthropic 发布的 46.4% no tools。官方榜单当前未列出该模型；发布页没有说明是否采用官方 mean Pass@1 协议、harness 或评测日期，故未强行映射本地 accuracy (mean; Pass@1) 定义。"
      ],
      "status": "待核实",
      "unresolved": [
        "Anthropic 报告的 score 是否使用官方 Chartography mean Pass@1 协议和相同测试配置尚未确认。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "DataCurve DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Anthropic release page",
          "url": "https://www.anthropic.com/claude-haiku-5-5"
        }
      ],
      "notes": [
        "未找到 Claude Haiku 5.5 的公开 DeepSWE v1.1 成绩。DataCurve 榜单快照的更新时间早于模型发布日期，因此该结果仅表示当前可核验资料中未找到。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Anthropic release page",
          "url": "https://www.anthropic.com/claude-haiku-5-5"
        },
        {
          "label": "Artificial Analysis GDPval-AA leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "将已有 Anthropic 1620 行指标规范为本地定义 Elo rating；AA 方法说明为 220 tasks / 44 occupations，通过 Stirrup shell+web 测试并进行 Elo 配对比较。AA 另列 Medium effort 1283 (-20/+20)，作为不同 effort 的独立记录。Anthropic 的 1620 没有注明 effort，页面也未给出评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Anthropic release page",
          "url": "https://www.anthropic.com/claude-haiku-5-5"
        },
        {
          "label": "Scale AI HLE leaderboard and version notice",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Original HLE paper",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "保留 Anthropic 原始公布的 no tools 45.9 和 with tools 57.4，不把 2026-10-07 发布日作为评测日期。Scale 页面将 2026-09-17 起的榜单标记为 HLE-Rolling；其 Haiku 5.5 结果不能映射为本地原始 2,500 题 HLE。"
      ],
      "status": "待核实",
      "unresolved": [
        "Anthropic 未说明两条分数所用题集是原始 HLE 还是 HLE-Rolling，且未给出 harness、effort 或测试日期；暂不能映射到本地 original HLE accuracy 定义。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Anthropic release page",
          "url": "https://www.anthropic.com/claude-haiku-5-5"
        },
        {
          "label": "OSWorld official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "保留 Anthropic 的 72.4% Offline subset 原始成绩；该页面未给出评测日期、effort 或 harness。TOML 原有 partial score 标记不是仓库定义的 binary task completion rate，未转成 binary 分数或计入精确映射覆盖。"
      ],
      "status": "待核实",
      "unresolved": [
        "Anthropic 页面仅称 Offline subset，未直接说明 partial reward；具体指标与 OSWorld 2.1 binary completion 定义的对应关系仍需核实。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "新增 V2 Full 成绩 87.23 ± 2.36 Resolve Rate，mini-swe-agent，high effort；来源说明为 642 tasks / 11 repositories。未公布评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard and methodology",
          "url": "https://vals-ai.com/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench Science 0.1 official release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "新增 Vals AI 的 10.00 ± 3.61。上游 v0.1.0 共 70 项任务；Vals 的 harness 为 Mini-SWE-agent，单次 pass@1，所有任务严格判定通过/失败。无评测日期或 effort。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Anthropic release page",
          "url": "https://www.anthropic.com/claude-haiku-5-5"
        },
        {
          "label": "Vals AI Terminal-Bench 4 leaderboard and methodology",
          "url": "https://vals-ai.com/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "保留 Anthropic 公布的 39.2（来源未给出 harness、effort 或评测日），另收录 Vals AI Mini-SWE-agent 的 36.36 ± 2.31。Vals 说明每项任务严格 pass/fail，三次独立运行取均值、单次 pass@1；两条记录来自不同来源和运行配置，不合并。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T03:52+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Claude Haiku 5.5 model profile",
          "url": "https://www.vals.ai/models/anthropic_claude-haiku-5-5"
        },
        {
          "label": "Vals Index benchmark definition",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "新增 58.73 ± 1.28，profile 显示 Vals Index、accuracy 与区间；该模型评测配置标明 Compute Effort: max。未使用旧页面历史值 54.31，也未填页面更新日为评测日。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 8,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T03:52+08:00",
  "model_id": "anthropic/claude-haiku-5-5",
  "new_records": 15,
  "overall_status": "待复核"
}

-->
