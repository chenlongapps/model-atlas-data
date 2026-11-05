# Kimi K3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：moonshotai/kimi-k3
- 模型名称：Kimi K3
- 发布日期：2026-07-16
- 最近检查时间：2026-11-04T23:53+08:00
- 整体处理状态：待复核
- 新增成绩数量：9
- 更新成绩数量：1
- 收集前已有成绩数量：13
- 当前已收录的对应成绩数量：10

## 模型身份与范围说明

- Kimi K3 是 2026-07-16 发布的通用多模态推理与 agent 模型；本轮对 11 项都完成版本/来源核验。
- 新增 9 条可核实记录：SWE-bench Pro V2、Terminal-Bench 4、Terminal-Bench-Science、Chartography、HLE 两种工具条件、Vals Index v2.2，以及 DeepSWE mini-SWE-agent 的两份来源结果；将原有 DeepSWE 指标字段修正为 v1.1 定义的 pass@1。
- DeepSWE mini-SWE-agent 结果 67.3 与当前官方榜显示 69% ± 5 尚有运行/检查点时间差；保留两个来源值并标记冲突，没有按最高值覆盖。
- GDPval-AA v2.1 尚无 Kimi K3 成绩；旧 v2 的 TOML 记录 1668 Elo 与技术报告 1686 Elo 暂不合并或覆盖。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 67.5 (metric=pass@1; version=1.1; variant=max effort; harness=Kimi Code); 67.3 (metric=pass@1; version=1.1; effort=max; harness=mini-SWE-agent); 69 (metric=pass@1; version=1.1; effort=max; harness=mini-swe-agent) | [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653), [Kimi K3 official launch article](https://www.kimi.com/en/blog/kimi-k3), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T23:53+08:00 |
| swe-bench-pro-v2 | 已收录 | 97.7 (metric=task resolution rate; version=2.0.0; dataset=V2 public set (642 tasks); effort=max; harness=mini-swe-agent) | [Scale AI SWE-bench Pro V2 leaderboard and methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:53+08:00 |
| terminal-bench-v4 | 已收录 | 88.3 (metric=accuracy; version=2.1; variant=max effort; harness=Kimi Code); 17.17 (metric=task resolution rate; version=4.0.0; effort=max; variant=avg@3; pass@1 per run; mean of three runs; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://vals.ai/benchmarks/terminal-bench-4), [Vals AI Kimi K3 model page and run settings](https://www.vals.ai/models/kimi_kimi-k3), [Terminal-Bench 4.0 release and version notes](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T23:53+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 1.43 (metric=task resolution rate; version=0.1.0; effort=max; variant=pass@1 single run; infrastructure/provider errors retried; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench-Science leaderboard and methodology](https://vals.ai/benchmarks/terminal-bench-science), [Vals AI Kimi K3 model page and run settings](https://www.vals.ai/models/kimi_kimi-k3), [Terminal-Bench-Science 0.1 official release](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T23:53+08:00 |
| automationbench-v1.0.6 | 待核实 | 30.8 (metric=success rate; dataset=600-task public subset; variant=max effort) | [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653), [Zapier AutomationBench leaderboard and methodology](https://zapier.com/benchmarks) | 2026-11-04T23:53+08:00 |
| osworld-v2.1 | 未找到 | — | [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653), [OSWorld-V2 repository and v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-04T23:53+08:00 |
| chartography | 已收录 | 26.6 (metric=accuracy (mean; Pass@1); dataset=100-task Chartography set; effort=Max reasoning; variant=20 trials per task; no tools; harness=Inspect AI) | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and evaluation protocol](https://arxiv.org/abs/2608.10677) | 2026-11-04T23:53+08:00 |
| humanitys-last-exam | 已收录 | 43.5 (metric=accuracy; dataset=HLE-Full; effort=max; variant=without tools); 56.0 (metric=accuracy; dataset=HLE-Full; effort=max; variant=with general tools) | [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653), [Humanity’s Last Exam paper and original benchmark definition](https://arxiv.org/abs/2501.14249) | 2026-11-04T23:53+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Kimi K3 model page](https://artificialanalysis.ai/models/kimi-k3), [Artificial Analysis Intelligence Index v5.0.1 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653) | 2026-11-04T23:53+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1668 (metric=Elo; version=v2; variant=max effort) | [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653), [Kimi K3 official launch article](https://www.kimi.com/en/blog/kimi-k3) | 2026-11-04T23:53+08:00 |
| vals-index-v2.2 | 已收录 | 52.95 (metric=performance score; version=2.2; effort=max) | [Vals AI Kimi K3 model page and run settings](https://www.vals.ai/models/kimi_kimi-k3), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T23:53+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 67.5
- metric: pass@1
- version: 1.1
- variant: max effort
- harness: Kimi Code
- source: [https://www.kimi.com/blog/kimi-k3](https://www.kimi.com/blog/kimi-k3)
- date: 2026-07-16
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 67.3
- metric: pass@1
- version: 1.1
- effort: max
- harness: mini-SWE-agent
- source: [https://www.kimi.com/en/blog/kimi-k3](https://www.kimi.com/en/blog/kimi-k3)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: DeepSWE
- score: 69
- metric: pass@1
- version: 1.1
- effort: max
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653)
- [Kimi K3 official launch article](https://www.kimi.com/en/blog/kimi-k3)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Kimi K3 技术报告记录 Kimi Code harness 的 67.5（max）；Kimi 发布文还引用当时 DeepSWE 榜的 mini-SWE-agent 67.3。当前 DeepSWE 榜同一 Kimi K3[max] / mini-swe-agent 条目显示 69% ± 5。三个结果条件中 Kimi Code 与 mini-SWE-agent 不同；两个 mini-SWE-agent 公布值不一致，且当前条目没有可确认的评测日期/检查点差异。保留两个 mini-SWE-agent 发布值，不选择较高者。
- 67.5 的现有 TOML metric 已按 DeepSWE v1.1 官方定义更正为 pass@1；67.3 和当前榜显示的 69 均按各自来源条件单独记录。

尚未解决的问题：
- mini-SWE-agent 的 67.3 与当前榜 69% ± 5 的运行/检查点时间差尚无法核实；数据 Schema 也没有置信区间字段。

最近核验时间：2026-11-04T23:53+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 97.7
- metric: task resolution rate
- version: 2.0.0
- dataset: V2 public set (642 tasks)
- effort: max
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard and methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Scale V2 Full 公共榜列出 Kimi-K3（mini-swe-agent，max）97.70 ± 0.90；V2 默认公开划分为 642 题。TOML 保留榜面值 97.7，置信区间留在此研究备注；页面未给该条具体评测日期，未填 date。

最近核验时间：2026-11-04T23:53+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 88.3
- metric: accuracy
- version: 2.1
- variant: max effort
- harness: Kimi Code
- source: [https://www.kimi.com/blog/kimi-k3](https://www.kimi.com/blog/kimi-k3)
- date: 2026-07-16
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 17.17
- metric: task resolution rate
- version: 4.0.0
- effort: max
- variant: avg@3; pass@1 per run; mean of three runs
- harness: Mini-SWE-agent
- source: [https://vals.ai/benchmarks/terminal-bench-4](https://vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 leaderboard and methodology](https://vals.ai/benchmarks/terminal-bench-4)
- [Vals AI Kimi K3 model page and run settings](https://www.vals.ai/models/kimi_kimi-k3)
- [Terminal-Bench 4.0 release and version notes](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Vals AI 的独立评测列出 Kimi K3 / Mini-SWE-agent 17.17%；榜单标为 Terminal-Bench 4.0。其方法为 66 个全新任务，每模型完整运行三次、每次每题 pass@1，报告三次运行均值。来源图表标签为 Accuracy；由于其方法明确按通过全部 verifier 的任务比例计分，TOML 使用本地定义的 task resolution rate。未把 Kimi 官方 Terminal-Bench 2.1 的 88.3 映射到 v4。

最近核验时间：2026-11-04T23:53+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 1.43
- metric: task resolution rate
- version: 0.1.0
- effort: max
- variant: pass@1 single run; infrastructure/provider errors retried
- harness: Mini-SWE-agent
- source: [https://vals.ai/benchmarks/terminal-bench-science](https://vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench-Science leaderboard and methodology](https://vals.ai/benchmarks/terminal-bench-science)
- [Vals AI Kimi K3 model page and run settings](https://www.vals.ai/models/kimi_kimi-k3)
- [Terminal-Bench-Science 0.1 official release](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Vals AI 的独立评测列出 Kimi K3 / Mini-SWE-agent 1.43%；方法明确使用上游 v0.1.0 的 70 题、每模型单次 pass@1 运行，无部分分。数据页对错误或中断任务有基础设施重试说明。来源标记为 Accuracy；报告的是通过任务比例，TOML 使用本地定义的 task resolution rate。

最近核验时间：2026-11-04T23:53+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 30.8
- metric: success rate
- dataset: 600-task public subset
- variant: max effort
- source: [https://www.kimi.com/blog/kimi-k3](https://www.kimi.com/blog/kimi-k3)
- date: 2026-07-16
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653)
- [Zapier AutomationBench leaderboard and methodology](https://zapier.com/benchmarks)

研究备注：
- 现有 TOML 的 30.8 来自 Kimi 官方报告，但明确使用 600-task public subset；仓库所定义的 AutomationBench 1.0.6 官方榜使用单独 held-out/private task set，公开子集分数不等价，因此没有映射或替换该原始记录。

尚未解决的问题：
- 未找到 Kimi K3 在 AutomationBench 1.0.6 held-out/private task set 上的精确成绩。

最近核验时间：2026-11-04T23:53+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653)
- [OSWorld-V2 repository and v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Kimi K3 技术报告列出 OSWorld 2.0 58.3，但目标定义为 osworld-v2.1；两版任务不能互相映射。未找到 Kimi K3 的 v2.1 成绩。

最近核验时间：2026-11-04T23:53+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 26.6
- metric: accuracy (mean; Pass@1)
- dataset: 100-task Chartography set
- effort: Max reasoning
- variant: 20 trials per task; no tools
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and evaluation protocol](https://arxiv.org/abs/2608.10677)

研究备注：
- Surge 当前官方榜列出 Kimi K3（Max reasoning）26.6%。论文定义为 100 题、mean Pass@1，每题 20 次试验、Inspect AI harness、no tools；未公布此 Kimi 行的独立评测日期，未填 date。

最近核验时间：2026-11-04T23:53+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 43.5
- metric: accuracy
- dataset: HLE-Full
- effort: max
- variant: without tools
- source: [https://arxiv.org/pdf/2607.24653](https://arxiv.org/pdf/2607.24653)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 56.0
- metric: accuracy
- dataset: HLE-Full
- effort: max
- variant: with general tools
- source: [https://arxiv.org/pdf/2607.24653](https://arxiv.org/pdf/2607.24653)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653)
- [Humanity’s Last Exam paper and original benchmark definition](https://arxiv.org/abs/2501.14249)

研究备注：
- Kimi K3 技术报告列出 HLE-Full 43.5（without tools）及 56.0（with general tools）；评测使用 max effort。两种工具条件分别写入 TOML。该来源未提供通用 agent harness 细节，故没有填 harness；版本未指定，未推测版本号。

最近核验时间：2026-11-04T23:53+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Kimi K3 model page](https://artificialanalysis.ai/models/kimi-k3)
- [Artificial Analysis Intelligence Index v5.0.1 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653)

研究备注：
- Kimi K3 的 Artificial Analysis 页面当前对 Index v5.0.1 显示 N/A；技术报告记载的是旧 Intelligence Index v4.1 57.1，不映射到 v5。未找到精确 v5 成绩。

最近核验时间：2026-11-04T23:53+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1668
- metric: Elo
- version: v2
- variant: max effort
- source: [https://www.kimi.com/blog/kimi-k3](https://www.kimi.com/blog/kimi-k3)
- date: 2026-07-16
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Kimi K3 technical report (arXiv)](https://arxiv.org/pdf/2607.24653)
- [Kimi K3 official launch article](https://www.kimi.com/en/blog/kimi-k3)

研究备注：
- 目标为 GDPval-AA v2.1，当前 AA 榜未列 Kimi K3。模型 TOML 中已有的 1668 Elo 属于旧 v2；Kimi 技术报告又列 v2 为 1686（截至 2026-07-23），两份旧版报告数值不同。没有将任一 v2 值映射到 v2.1，也未自动覆盖现有历史行。

尚未解决的问题：
- 旧 v2 的 1668 与 1686 Elo 记录差异尚未解释；确认 v2.1 的 Kimi K3 成绩前需保留版本边界。

最近核验时间：2026-11-04T23:53+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 52.95
- metric: performance score
- version: 2.2
- effort: max
- source: [https://vals.ai/models/kimi_kimi-k3](https://vals.ai/models/kimi_kimi-k3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Kimi K3 model page and run settings](https://www.vals.ai/models/kimi_kimi-k3)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Kimi K3 页面当前列出 52.95% ± 1.00，reasoning effort 为 max；Vals Index 总榜明确版本 2.2。TOML 保留 52.95，置信区间记于研究备注。页面的历史更新还列出 2026-07-16 的 57.81%，但未标为当前 v2.2 结果，未重复收录。未见明确的本次评测日期，未填 date。

最近核验时间：2026-11-04T23:53+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Kimi K3 model page",
          "url": "https://artificialanalysis.ai/models/kimi-k3"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Kimi K3 technical report (arXiv)",
          "url": "https://arxiv.org/pdf/2607.24653"
        }
      ],
      "notes": [
        "Kimi K3 的 Artificial Analysis 页面当前对 Index v5.0.1 显示 N/A；技术报告记载的是旧 Intelligence Index v4.1 57.1，不映射到 v5。未找到精确 v5 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Kimi K3 technical report (arXiv)",
          "url": "https://arxiv.org/pdf/2607.24653"
        },
        {
          "label": "Zapier AutomationBench leaderboard and methodology",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "现有 TOML 的 30.8 来自 Kimi 官方报告，但明确使用 600-task public subset；仓库所定义的 AutomationBench 1.0.6 官方榜使用单独 held-out/private task set，公开子集分数不等价，因此没有映射或替换该原始记录。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到 Kimi K3 在 AutomationBench 1.0.6 held-out/private task set 上的精确成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper and evaluation protocol",
          "url": "https://arxiv.org/abs/2608.10677"
        }
      ],
      "notes": [
        "Surge 当前官方榜列出 Kimi K3（Max reasoning）26.6%。论文定义为 100 题、mean Pass@1，每题 20 次试验、Inspect AI harness、no tools；未公布此 Kimi 行的独立评测日期，未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Kimi K3 technical report (arXiv)",
          "url": "https://arxiv.org/pdf/2607.24653"
        },
        {
          "label": "Kimi K3 official launch article",
          "url": "https://www.kimi.com/en/blog/kimi-k3"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Kimi K3 技术报告记录 Kimi Code harness 的 67.5（max）；Kimi 发布文还引用当时 DeepSWE 榜的 mini-SWE-agent 67.3。当前 DeepSWE 榜同一 Kimi K3[max] / mini-swe-agent 条目显示 69% ± 5。三个结果条件中 Kimi Code 与 mini-SWE-agent 不同；两个 mini-SWE-agent 公布值不一致，且当前条目没有可确认的评测日期/检查点差异。保留两个 mini-SWE-agent 发布值，不选择较高者。",
        "67.5 的现有 TOML metric 已按 DeepSWE v1.1 官方定义更正为 pass@1；67.3 和当前榜显示的 69 均按各自来源条件单独记录。"
      ],
      "status": "冲突",
      "unresolved": [
        "mini-SWE-agent 的 67.3 与当前榜 69% ± 5 的运行/检查点时间差尚无法核实；数据 Schema 也没有置信区间字段。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Kimi K3 technical report (arXiv)",
          "url": "https://arxiv.org/pdf/2607.24653"
        },
        {
          "label": "Kimi K3 official launch article",
          "url": "https://www.kimi.com/en/blog/kimi-k3"
        }
      ],
      "notes": [
        "目标为 GDPval-AA v2.1，当前 AA 榜未列 Kimi K3。模型 TOML 中已有的 1668 Elo 属于旧 v2；Kimi 技术报告又列 v2 为 1686（截至 2026-07-23），两份旧版报告数值不同。没有将任一 v2 值映射到 v2.1，也未自动覆盖现有历史行。"
      ],
      "status": "待核实",
      "unresolved": [
        "旧 v2 的 1668 与 1686 Elo 记录差异尚未解释；确认 v2.1 的 Kimi K3 成绩前需保留版本边界。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Kimi K3 technical report (arXiv)",
          "url": "https://arxiv.org/pdf/2607.24653"
        },
        {
          "label": "Humanity’s Last Exam paper and original benchmark definition",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "Kimi K3 技术报告列出 HLE-Full 43.5（without tools）及 56.0（with general tools）；评测使用 max effort。两种工具条件分别写入 TOML。该来源未提供通用 agent harness 细节，故没有填 harness；版本未指定，未推测版本号。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Kimi K3 technical report (arXiv)",
          "url": "https://arxiv.org/pdf/2607.24653"
        },
        {
          "label": "OSWorld-V2 repository and v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Kimi K3 技术报告列出 OSWorld 2.0 58.3，但目标定义为 osworld-v2.1；两版任务不能互相映射。未找到 Kimi K3 的 v2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Scale V2 Full 公共榜列出 Kimi-K3（mini-swe-agent，max）97.70 ± 0.90；V2 默认公开划分为 642 题。TOML 保留榜面值 97.7，置信区间留在此研究备注；页面未给该条具体评测日期，未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard and methodology",
          "url": "https://vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Vals AI Kimi K3 model page and run settings",
          "url": "https://www.vals.ai/models/kimi_kimi-k3"
        },
        {
          "label": "Terminal-Bench-Science 0.1 official release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Vals AI 的独立评测列出 Kimi K3 / Mini-SWE-agent 1.43%；方法明确使用上游 v0.1.0 的 70 题、每模型单次 pass@1 运行，无部分分。数据页对错误或中断任务有基础设施重试说明。来源标记为 Accuracy；报告的是通过任务比例，TOML 使用本地定义的 task resolution rate。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard and methodology",
          "url": "https://vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals AI Kimi K3 model page and run settings",
          "url": "https://www.vals.ai/models/kimi_kimi-k3"
        },
        {
          "label": "Terminal-Bench 4.0 release and version notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Vals AI 的独立评测列出 Kimi K3 / Mini-SWE-agent 17.17%；榜单标为 Terminal-Bench 4.0。其方法为 66 个全新任务，每模型完整运行三次、每次每题 pass@1，报告三次运行均值。来源图表标签为 Accuracy；由于其方法明确按通过全部 verifier 的任务比例计分，TOML 使用本地定义的 task resolution rate。未把 Kimi 官方 Terminal-Bench 2.1 的 88.3 映射到 v4。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:53+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Kimi K3 model page and run settings",
          "url": "https://www.vals.ai/models/kimi_kimi-k3"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Kimi K3 页面当前列出 52.95% ± 1.00，reasoning effort 为 max；Vals Index 总榜明确版本 2.2。TOML 保留 52.95，置信区间记于研究备注。页面的历史更新还列出 2026-07-16 的 57.81%，但未标为当前 v2.2 结果，未重复收录。未见明确的本次评测日期，未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 13,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:53+08:00",
  "model_id": "moonshotai/kimi-k3",
  "model_notes": [
    "Kimi K3 是 2026-07-16 发布的通用多模态推理与 agent 模型；本轮对 11 项都完成版本/来源核验。",
    "新增 9 条可核实记录：SWE-bench Pro V2、Terminal-Bench 4、Terminal-Bench-Science、Chartography、HLE 两种工具条件、Vals Index v2.2，以及 DeepSWE mini-SWE-agent 的两份来源结果；将原有 DeepSWE 指标字段修正为 v1.1 定义的 pass@1。",
    "DeepSWE mini-SWE-agent 结果 67.3 与当前官方榜显示 69% ± 5 尚有运行/检查点时间差；保留两个来源值并标记冲突，没有按最高值覆盖。",
    "GDPval-AA v2.1 尚无 Kimi K3 成绩；旧 v2 的 TOML 记录 1668 Elo 与技术报告 1686 Elo 暂不合并或覆盖。"
  ],
  "new_records": 9,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
