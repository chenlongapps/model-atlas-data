# Grok 4.7 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-4.7
- 模型名称：Grok 4.7
- 发布日期：2026-09-21
- 最近检查时间：2026-11-04T09:40+08:00
- 整体处理状态：待复核
- 新增成绩数量：7
- 收集前已有成绩数量：8
- 当前已收录的对应成绩数量：4

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 71 (metric=score; version=1.1; variant=high effort) | [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7), [DeepSWE 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE v1.1 说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T09:40+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 公榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7) | 2026-11-04T09:40+08:00 |
| terminal-bench-v4 | 待核实 | 37.6 (metric=score; version=4.0; variant=xhigh effort); 26 (metric=pass@1; version=4.0.0; dataset=66 tasks; effort=Xhigh; variant=averaged over 3 repeats; harness=mini-swe-agent) | [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7), [Artificial Analysis Grok 4.7 对照页](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6), [Artificial Analysis Terminal-Bench 4.0 方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T09:40+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 11 (metric=pass@1; version=0.1.0; dataset=70 tasks; effort=Xhigh; variant=averaged over 3 repeats per task; harness=mini-swe-agent) | [Artificial Analysis Grok 4.7 对照页](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6), [Artificial Analysis Terminal-Bench-Science 0.1 方法](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Harbor 官方 Science 运行列表](https://hub.harborframework.com/organizations/terminal-bench-science) | 2026-11-04T09:40+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 榜单](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench), [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7) | 2026-11-04T09:40+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 官方项目页](https://osworld-v2.xlang.ai/), [OSWorld-V2 官方 README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md), [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7) | 2026-11-04T09:40+08:00 |
| chartography | 已收录 | 14.7 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=xHigh; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方仓库与方法](https://github.com/surge-ai/chartography) | 2026-11-04T09:40+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis Humanity's Last Exam 方法与结果页](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis Grok 4.7 模型比较页](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-gpt-5-6-sol-xhigh) | 2026-11-04T09:40+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 35 (metric=index score; version=5.0.1; effort=xhigh) | [Artificial Analysis Grok 4.7 模型页](https://artificialanalysis.ai/models/grok-4-7), [Artificial Analysis Grok 4.7 对照页](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-grok-4-7) | 2026-11-04T09:40+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1718 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=Xhigh; variant=shell and web access; blind pairwise Elo; harness=Stirrup); 1716 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 industries; effort=High; variant=shell and web access; blind pairwise Elo; harness=Stirrup) | [Artificial Analysis GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T09:40+08:00 |
| vals-index-v2.2 | 已收录 | 58.56 (metric=performance score; version=2.2; dataset=GDP-weighted finance, coding, legal, and tax; effort=xhigh) | [Vals Index v2.2 官方基准页](https://www.vals.ai/benchmarks/vals_index), [Vals Grok 4.7 模型页](https://www.vals.ai/models/grok_grok-4.7) | 2026-11-04T09:40+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 71
- metric: score
- version: 1.1
- variant: high effort
- source: [https://x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7)
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- xAI 发布文明确报告 DeepSWE v1.1 为 71.0%，并以脚注标明 high effort；本地已存在对应数值。xAI 未说明该行的 metric、harness、任务集或实际评测日期；官方榜单上的其他模型配置不能移用于该 xAI 结果。
- 本地定义 metric 为 pass@1，而该来源只称 score，故保留原始行但不强制映射。

尚未解决的问题：
- 来源未给出可与本地 pass@1 定义精确核对的指标与测试配置。

最近核验时间：2026-11-04T09:40+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 公榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7)

研究备注：
- 检查了 V2 公榜与 xAI 发布资料，未发现 Grok 4.7 的该版本结果；没有用其他 SWE-bench 版本或近似型号代替。

最近核验时间：2026-11-04T09:40+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 37.6
- metric: score
- version: 4.0
- variant: xhigh effort
- source: [https://x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 26
- metric: pass@1
- version: 4.0.0
- dataset: 66 tasks
- effort: Xhigh
- variant: averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7)
- [Artificial Analysis Grok 4.7 对照页](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6)
- [Artificial Analysis Terminal-Bench 4.0 方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Terminal-Bench 4.0 版本说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- xAI 报告 Terminal-Bench 4.0 为 37.6%（xHigh），未公布 metric、harness 或实际评测日期。Artificial Analysis 独立评测同一模型配置报告 26%（pass@1，66 项任务，mini-swe-agent，三次重复平均）。两条原始结果分开保留；测试配置不同或未完整披露，不据此覆盖或合并。
- 本地定义的版本是 4.0.0、metric 是 task resolution rate；AA 行使用 pass@1，xAI 行只写 score，均无法按定义精确映射。

尚未解决的问题：
- 当前两条记录的来源 metric 与本地定义不完全相同，且 xAI 未公布 harness；需保留原始条件并待定义映射复核。

最近核验时间：2026-11-04T09:40+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 11
- metric: pass@1
- version: 0.1.0
- dataset: 70 tasks
- effort: Xhigh
- variant: averaged over 3 repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Grok 4.7 对照页](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6)
- [Artificial Analysis Terminal-Bench-Science 0.1 方法](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Harbor 官方 Science 运行列表](https://hub.harborframework.com/organizations/terminal-bench-science)

研究备注：
- AA 独立评测表列出 Grok 4.7 Xhigh 为 11%（整数显示）；方法页说明版本 0.1.0、70 项任务、mini-swe-agent、pass@1 三次重复平均，已将原始字段单独收录。Harbor 另列出三个 grok-4.7-v0.1-trial 运行，各覆盖 70/70 项任务，但没有聚合分数，因此未另写成绩。

尚未解决的问题：
- 本地定义 metric 为 task resolution rate，而 AA 明确报告 pass@1；保留原始 metric，不改写为本地指标，等待精确映射确认。

最近核验时间：2026-11-04T09:40+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 榜单](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)
- [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7)

研究备注：
- 榜单标注版本 1.0.6，但当前页面文本只展示前十名并提示另有 119 项；无法完整检查所有行，且 xAI 发布文没有该成绩。未把 Artificial Analysis 的 AutomationBench-AA 结果当作 Zapier AutomationBench v1.0.6。

尚未解决的问题：
- 公开榜单尚有未展开条目，不能据此确认不存在 Grok 4.7 成绩。

最近核验时间：2026-11-04T09:40+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 官方项目页](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 官方 README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)
- [xAI Grok 4.7 发布文](https://x.ai/news/grok-4-7)

研究备注：
- 官方项目页当前显示 OSWorld 2.0；项目 README 提及 2.1 版本，但本次未找到 Grok 4.7 的精确 2.1 成绩。未使用 2.0 或其他 Grok 型号结果替代。

尚未解决的问题：
- v2.1 的完整公开排行榜未能核实，当前公开榜与目标版本不一致。

最近核验时间：2026-11-04T09:40+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 14.7
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: xHigh
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方仓库与方法](https://github.com/surge-ai/chartography)

研究备注：
- 官方榜单列出 Grok 4.7 (xHigh reasoning) 为 14.7%。README 说明完整 100 项任务集、每项 10 次运行、Gemini 3.5 Flash judge，使用 Inspect AI；按原始 Pass@1 mean 对应本地 metric。来源未公布 benchmark 版本或实际评测日期，故省略。

最近核验时间：2026-11-04T09:40+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Humanity's Last Exam 方法与结果页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis Grok 4.7 模型比较页](https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-gpt-5-6-sol-xhigh)

研究备注：
- 当前可查看的 AA 比较页展示 HLE-Diamond，而非本任务的原版 Humanity’s Last Exam；曾出现的 43% 原版 HLE 候选值无法在当前页面直接复核，因此没有写入。AA 原版 HLE 方法页说明其评测子集和 pass@1，但登录页没有通过登录访问。

尚未解决的问题：
- 原版 HLE 结果候选缺少可直接复核的公开行；不使用 HLE-Diamond 或未经确认的历史截图替代。

最近核验时间：2026-11-04T09:40+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 35
- metric: index score
- version: 5.0.1
- effort: xhigh
- source: [https://artificialanalysis.ai/models/grok-4-7](https://artificialanalysis.ai/models/grok-4-7)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Grok 4.7 模型页](https://artificialanalysis.ai/models/grok-4-7)
- [Artificial Analysis Grok 4.7 对照页](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-grok-4-7)

研究备注：
- 当前 AA 模型页显示 Grok 4.7 Xhigh 指数 35，页面说明指数版本为 5.0.1。该原始版本已如实单独写入，未改写成 5.0；本地定义版本为 5.0，故该行不计入精确映射覆盖率。

尚未解决的问题：
- 本地定义版本 5.0 与来源页面版本 5.0.1 不一致，需要决定是否新增/更新定义后才能纳入覆盖率。

最近核验时间：2026-11-04T09:40+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1718
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: Xhigh
- variant: shell and web access; blind pairwise Elo
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1716
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 industries
- effort: High
- variant: shell and web access; blind pairwise Elo
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 官方页面按推理档位分别列出 Xhigh 1718 Elo 与 High 1716 Elo；已分别保存。方法说明 220 项任务、44 种职业、9 个行业，通过 Stirrup 提供 shell/web 工具并以盲测成对比较聚合 Elo。页面没有公布实际评测日期。既有通用 GDPval 1695 与该 v2.1 评测不同，保留原行。

最近核验时间：2026-11-04T09:40+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 58.56
- metric: performance score
- version: 2.2
- dataset: GDP-weighted finance, coding, legal, and tax
- effort: xhigh
- source: [https://www.vals.ai/models/grok_grok-4.7](https://www.vals.ai/models/grok_grok-4.7)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index v2.2 官方基准页](https://www.vals.ai/benchmarks/vals_index)
- [Vals Grok 4.7 模型页](https://www.vals.ai/models/grok_grok-4.7)

研究备注：
- 官方 v2.2 页面列出 Grok 4.7 为 58.56%；模型页标明 xhigh reasoning effort，并显示该分数的误差范围。模型 TOML 保存原始分数、版本及 effort。页面更新日期不作为评测日期写入。

最近核验时间：2026-11-04T09:40+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.7 模型页",
          "url": "https://artificialanalysis.ai/models/grok-4-7"
        },
        {
          "label": "Artificial Analysis Grok 4.7 对照页",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-grok-4-7"
        }
      ],
      "notes": [
        "当前 AA 模型页显示 Grok 4.7 Xhigh 指数 35，页面说明指数版本为 5.0.1。该原始版本已如实单独写入，未改写成 5.0；本地定义版本为 5.0，故该行不计入精确映射覆盖率。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义版本 5.0 与来源页面版本 5.0.1 不一致，需要决定是否新增/更新定义后才能纳入覆盖率。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "xAI Grok 4.7 发布文",
          "url": "https://x.ai/news/grok-4-7"
        }
      ],
      "notes": [
        "榜单标注版本 1.0.6，但当前页面文本只展示前十名并提示另有 119 项；无法完整检查所有行，且 xAI 发布文没有该成绩。未把 Artificial Analysis 的 AutomationBench-AA 结果当作 Zapier AutomationBench v1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开榜单尚有未展开条目，不能据此确认不存在 Grok 4.7 成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方仓库与方法",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "官方榜单列出 Grok 4.7 (xHigh reasoning) 为 14.7%。README 说明完整 100 项任务集、每项 10 次运行、Gemini 3.5 Flash judge，使用 Inspect AI；按原始 Pass@1 mean 对应本地 metric。来源未公布 benchmark 版本或实际评测日期，故省略。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.7 发布文",
          "url": "https://x.ai/news/grok-4-7"
        },
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "xAI 发布文明确报告 DeepSWE v1.1 为 71.0%，并以脚注标明 high effort；本地已存在对应数值。xAI 未说明该行的 metric、harness、任务集或实际评测日期；官方榜单上的其他模型配置不能移用于该 xAI 结果。",
        "本地定义 metric 为 pass@1，而该来源只称 score，故保留原始行但不强制映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源未给出可与本地 pass@1 定义精确核对的指标与测试配置。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "官方页面按推理档位分别列出 Xhigh 1718 Elo 与 High 1716 Elo；已分别保存。方法说明 220 项任务、44 种职业、9 个行业，通过 Stirrup 提供 shell/web 工具并以盲测成对比较聚合 Elo。页面没有公布实际评测日期。既有通用 GDPval 1695 与该 v2.1 评测不同，保留原行。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Humanity's Last Exam 方法与结果页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis Grok 4.7 模型比较页",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-gpt-5-6-sol-xhigh"
        }
      ],
      "notes": [
        "当前可查看的 AA 比较页展示 HLE-Diamond，而非本任务的原版 Humanity’s Last Exam；曾出现的 43% 原版 HLE 候选值无法在当前页面直接复核，因此没有写入。AA 原版 HLE 方法页说明其评测子集和 pass@1，但登录页没有通过登录访问。"
      ],
      "status": "待核实",
      "unresolved": [
        "原版 HLE 结果候选缺少可直接复核的公开行；不使用 HLE-Diamond 或未经确认的历史截图替代。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 官方 README",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        },
        {
          "label": "xAI Grok 4.7 发布文",
          "url": "https://x.ai/news/grok-4-7"
        }
      ],
      "notes": [
        "官方项目页当前显示 OSWorld 2.0；项目 README 提及 2.1 版本，但本次未找到 Grok 4.7 的精确 2.1 成绩。未使用 2.0 或其他 Grok 型号结果替代。"
      ],
      "status": "待核实",
      "unresolved": [
        "v2.1 的完整公开排行榜未能核实，当前公开榜与目标版本不一致。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 公榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "xAI Grok 4.7 发布文",
          "url": "https://x.ai/news/grok-4-7"
        }
      ],
      "notes": [
        "检查了 V2 公榜与 xAI 发布资料，未发现 Grok 4.7 的该版本结果；没有用其他 SWE-bench 版本或近似型号代替。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.7 对照页",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 0.1 方法",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Harbor 官方 Science 运行列表",
          "url": "https://hub.harborframework.com/organizations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 独立评测表列出 Grok 4.7 Xhigh 为 11%（整数显示）；方法页说明版本 0.1.0、70 项任务、mini-swe-agent、pass@1 三次重复平均，已将原始字段单独收录。Harbor 另列出三个 grok-4.7-v0.1-trial 运行，各覆盖 70/70 项任务，但没有聚合分数，因此未另写成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义 metric 为 task resolution rate，而 AA 明确报告 pass@1；保留原始 metric，不改写为本地指标，等待精确映射确认。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.7 发布文",
          "url": "https://x.ai/news/grok-4-7"
        },
        {
          "label": "Artificial Analysis Grok 4.7 对照页",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 方法",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Terminal-Bench 4.0 版本说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "xAI 报告 Terminal-Bench 4.0 为 37.6%（xHigh），未公布 metric、harness 或实际评测日期。Artificial Analysis 独立评测同一模型配置报告 26%（pass@1，66 项任务，mini-swe-agent，三次重复平均）。两条原始结果分开保留；测试配置不同或未完整披露，不据此覆盖或合并。",
        "本地定义的版本是 4.0.0、metric 是 task resolution rate；AA 行使用 pass@1，xAI 行只写 score，均无法按定义精确映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前两条记录的来源 metric 与本地定义不完全相同，且 xAI 未公布 harness；需保留原始条件并待定义映射复核。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T09:40+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方基准页",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Grok 4.7 模型页",
          "url": "https://www.vals.ai/models/grok_grok-4.7"
        }
      ],
      "notes": [
        "官方 v2.2 页面列出 Grok 4.7 为 58.56%；模型页标明 xhigh reasoning effort，并显示该分数的误差范围。模型 TOML 保存原始分数、版本及 effort。页面更新日期不作为评测日期写入。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 8,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T09:40+08:00",
  "model_id": "xai/grok-4.7",
  "new_records": 7,
  "overall_status": "待复核"
}

-->
