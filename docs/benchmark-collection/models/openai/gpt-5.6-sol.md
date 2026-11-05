# GPT-5.6 Sol Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.6-sol
- 模型名称：GPT-5.6 Sol
- 发布日期：2026-07-09
- 最近检查时间：2026-11-05T00:51+08:00
- 整体处理状态：待复核
- 新增成绩数量：9
- 更新成绩数量：0
- 收集前已有成绩数量：12
- 当前已收录的对应成绩数量：9

## 模型身份与范围说明

- 模型身份及 2026-07-09 发布日期与 OpenAI GPT-5.6 发布页一致；本次保留模型文件原有信息。
- 收集前保留 12 条历史成绩；本次新增的原始行均来自独立、可核实的来源和配置，未覆盖历史行。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 72.7 (metric=resolve rate; version=1.1); 73 (metric=pass@1; version=1.1; dataset=113 tasks; effort=max; harness=Pier; mini-swe-agent on Modal) | [DataCurve DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DataCurve official repository](https://github.com/datacurve-ai/deep-swe) | 2026-11-05T00:51+08:00 |
| swe-bench-pro-v2 | 已收录 | 95.5 (metric=task resolution rate; version=2.0.0; dataset=Full; 642 tasks; effort=xhigh; variant=95% CI ±1.40 percentage points; harness=Codex) | [Scale AI official SWE-Bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [ScaleAI official dataset card](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-05T00:51+08:00 |
| terminal-bench-v4 | 已收录 | 88.8 (metric=success rate; version=2.1); 37.3 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; effort=max; variant=95% CI ±3.8 percentage points; harness=Codex) | [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?efforts=all&version=4.0), [Terminal-Bench 4.0 release v4.0.0](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.0.0) | 2026-11-05T00:51+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 22.4 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=3 trials per task; harness=Codex) | [Terminal-Bench-Science 0.1 official results announcement](https://www.tbench.ai/news/terminal-bench-science-0-1), [Terminal-Bench-Science v0.1.0 release](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) | 2026-11-05T00:51+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [OpenAI GPT-5.6 release results](https://openai.com/index/gpt-5-6/), [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench), [Zapier official announcement](https://www.linkedin.com/posts/zapier_%F0%9D%97%A6%F0%9D%97%BC%F0%9D%97%B9-%F0%9D%97%A7%F0%9D%97%B2%F0%9D%97%BF%F0%9D%97%BF%F0%9D%97%AE-%F0%9D%97%AE%F0%9D%97%BB%F0%9D%97%B1-%F0%9D%97%9F%F0%9D%98%82%F0%9D%97%BB%F0%9D%97%AE-just-activity-7481038274497605633-wnLy) | 2026-11-05T00:51+08:00 |
| osworld-v2.1 | 未找到 | 62.6 (metric=success rate; version=2.0) | [OpenAI GPT-5.6 release (reports OSWorld 2.0)](https://openai.com/index/gpt-5-6/), [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T00:51+08:00 |
| chartography | 已收录 | 45.0 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=max reasoning; variant=20 trials per task; no tools; 95% CI ±1.1 percentage points; harness=Inspect AI; judge=Gemini 3.5 Flash); 39.5 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=default; variant=20 trials per task; no tools; 95% CI ±1.2 percentage points; harness=Inspect AI; judge=Gemini 3.5 Flash) | [Chartography original paper and launch leaderboard](https://arxiv.org/abs/2608.10677), [Surge AI current leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T00:51+08:00 |
| humanitys-last-exam | 待核实 | 49 (metric=accuracy; dataset=May 2025 HLE revision; 2,158 text-only questions; effort=Max; variant=pass@1; harness=GPT-5.6 Luna (medium) equality checker) | [Artificial Analysis comparison: GPT-5.6 Sol Max](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T00:51+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | 58.9 (metric=index score; version=4.1; variant=max) | [Artificial Analysis Intelligence Index current official page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [GPT-5.6 Sol official AA model page](https://artificialanalysis.ai/models/releases/gpt-5-6-sol) | 2026-11-05T00:51+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1609 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Max; harness=Stirrup; shell and web browsing); 1250 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Non-reasoning; harness=Stirrup; shell and web browsing) | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis comparison: GPT-5.6 Sol Max](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T00:51+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI official Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T00:51+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 72.7
- metric: resolve rate
- version: 1.1
- source: [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)
- date: 2026-07-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 73
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: max
- harness: Pier; mini-swe-agent on Modal
- source: [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DataCurve DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DataCurve official repository](https://github.com/datacurve-ai/deep-swe)

研究备注：
- 新增 DataCurve leaderboard 的 max / pass@1 73% 记录（页面报告 ±3）；官方仓库说明该榜使用 Pier、mini-swe-agent 和 Modal，数据集为 113 tasks。
- 保留原 OpenAI 发布行（72.7, resolve rate）作为不同来源记录；未重写其指标或合并 harness。DataCurve 的 ±3 统计定义未公开，因此没有录入 TOML。

最近核验时间：2026-11-05T00:51+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 95.5
- metric: task resolution rate
- version: 2.0.0
- dataset: Full; 642 tasks
- effort: xhigh
- variant: 95% CI ±1.40 percentage points
- harness: Codex
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Scale AI official SWE-Bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [ScaleAI official dataset card](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- Scale V2 Full 官方榜确认 Codex / xhigh 得分 95.50（95% CI ±1.40 pp）；Full 是 642 tasks，数据集卡标示版本 2.0.0。与已有无版本 SWE-Bench Pro 行分开保存。

最近核验时间：2026-11-05T00:51+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 88.8
- metric: success rate
- version: 2.1
- source: [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)
- date: 2026-07-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 37.3
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- effort: max
- variant: 95% CI ±3.8 percentage points
- harness: Codex
- source: [https://www.tbench.ai/?efforts=all&version=4.0](https://www.tbench.ai/?efforts=all&version=4.0)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?efforts=all&version=4.0)
- [Terminal-Bench 4.0 release v4.0.0](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.0.0)

研究备注：
- 官方榜确认 Codex / max 配置为 37.3%（95% CI ±3.8 pp）；数据集为 66 tasks。榜单 Release Date 字段是模型发布日期，不作为评测 date 写入。

最近核验时间：2026-11-05T00:51+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 22.4
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: 3 trials per task
- harness: Codex
- source: [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Terminal-Bench-Science 0.1 official results announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Terminal-Bench-Science v0.1.0 release](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)

研究备注：
- 官方公告确认 Codex 得分 22.4%，覆盖 70 tasks、每项 3 trials；未公布 effort 或具体评测日。

最近核验时间：2026-11-05T00:51+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI GPT-5.6 release results](https://openai.com/index/gpt-5-6/)
- [Zapier AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Zapier official announcement](https://www.linkedin.com/posts/zapier_%F0%9D%97%A6%F0%9D%97%BC%F0%9D%97%B9-%F0%9D%97%A7%F0%9D%97%B2%F0%9D%97%BF%F0%9D%97%BF%F0%9D%97%AE-%F0%9D%97%AE%F0%9D%97%BB%F0%9D%97%B1-%F0%9D%97%9F%F0%9D%98%82%F0%9D%97%BB%F0%9D%97%AE-just-activity-7481038274497605633-wnLy)

研究备注：
- 候选 18.1% 出现在 OpenAI 发布材料及 Zapier 官方宣传资料中，但尚未核实它是否对应本地定义的 v1.0.6 private held-out leaderboard、对应指标及完整运行配置。Zapier 文档区分 public task set 与官方 leaderboard 的 held-out private set。

尚未解决的问题：
- 未能确认 18.1% 是否来自 AutomationBench v1.0.6 官方私有留出集及其完整测试条件；不写入模型 TOML。

最近核验时间：2026-11-05T00:51+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 62.6
- metric: success rate
- version: 2.0
- source: [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)
- date: 2026-07-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [OpenAI GPT-5.6 release (reports OSWorld 2.0)](https://openai.com/index/gpt-5-6/)
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 检查了 OpenAI 已公布的 OSWorld 2.0 结果及 OSWorld V2.1 public-evaluation guide；未找到 GPT-5.6 Sol 的 v2.1 公开成绩。已有 2.0 的 62.6% 不属于 v2.1。

最近核验时间：2026-11-05T00:51+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 45.0
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: max reasoning
- variant: 20 trials per task; no tools; 95% CI ±1.1 percentage points
- harness: Inspect AI; judge=Gemini 3.5 Flash
- source: [https://arxiv.org/abs/2608.10677](https://arxiv.org/abs/2608.10677)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Chartography
- score: 39.5
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: default
- variant: 20 trials per task; no tools; 95% CI ±1.2 percentage points
- harness: Inspect AI; judge=Gemini 3.5 Flash
- source: [https://arxiv.org/abs/2608.10677](https://arxiv.org/abs/2608.10677)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Chartography original paper and launch leaderboard](https://arxiv.org/abs/2608.10677)
- [Surge AI current leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 新增 max reasoning 45.0% 与 default 39.5%，均为 mean Pass@1。原论文说明 100 tasks、每项 20 trials、no tools、Inspect AI harness、Gemini 3.5 Flash judge；无语义版本，论文仅给 2026-07 快照月份，故未填 date。95% CI 分别已记入 variant。

最近核验时间：2026-11-05T00:51+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 49
- metric: accuracy
- dataset: May 2025 HLE revision; 2,158 text-only questions
- effort: Max
- variant: pass@1
- harness: GPT-5.6 Luna (medium) equality checker
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis comparison: GPT-5.6 Sol Max](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前可直接复核的 GPT-5.6 Sol Max 原始 HLE 为 49%。AA methodology 确认使用 May 2025 full-HLE revision 的 2,158 道 text-only 题、原始 equality-checker prompt、GPT-5.6 Luna (medium) judge 和 pass@1；未公布评测日期。

尚未解决的问题：
- 此前研究还发现 Xhigh 47%、High 46%、Medium 42% 与 Low 39% 候选，但当前比较页已改用 HLE-Diamond 或不再显示原始 HLE 行；这些候选暂不写入，需确认原始 HLE 条件。

最近核验时间：2026-11-05T00:51+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 58.9
- metric: index score
- version: 4.1
- variant: max
- source: [https://artificialanalysis.ai/articles/gpt-5-6-has-landed](https://artificialanalysis.ai/articles/gpt-5-6-has-landed)
- date: 2026-07-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Intelligence Index current official page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [GPT-5.6 Sol official AA model page](https://artificialanalysis.ai/models/releases/gpt-5-6-sol)

研究备注：
- 官方当前页面为 v5.0.1，组件与 v4.1 不同，且没有 GPT-5.6 Sol 的 v5 成绩。模型 TOML 中已有 v4.1 行保留，但不映射到 v5。

最近核验时间：2026-11-05T00:51+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1609
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Max
- harness: Stirrup; shell and web browsing
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1250
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Non-reasoning
- harness: Stirrup; shell and web browsing
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis comparison: GPT-5.6 Sol Max](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前官方 leaderboard 直接确认 Non-reasoning 1250 Elo；官方比较页直接确认 Max 1609 Elo。新增两条不同 effort 的成绩。方法页确认 220 tasks、44 occupations、Stirrup、shell + web browsing 与 pairwise Elo。

尚未解决的问题：
- 之前研究中 Xhigh 1569 与 High 1504 的候选分数未能在当前直接比较页或当前 leaderboard 复核；未写入 TOML，等待稳定的官方逐配置来源。

最近核验时间：2026-11-05T00:51+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI official Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 v2.2 官榜（2026-10-30）未列 GPT-5.6 Sol。已有 58.01% 属于 v2.1，不迁移到 v2.2。

最近核验时间：2026-11-05T00:51+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index current official page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis methodology and version history",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "GPT-5.6 Sol official AA model page",
          "url": "https://artificialanalysis.ai/models/releases/gpt-5-6-sol"
        }
      ],
      "notes": [
        "官方当前页面为 v5.0.1，组件与 v4.1 不同，且没有 GPT-5.6 Sol 的 v5 成绩。模型 TOML 中已有 v4.1 行保留，但不映射到 v5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-5.6 release results",
          "url": "https://openai.com/index/gpt-5-6/"
        },
        {
          "label": "Zapier AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Zapier official announcement",
          "url": "https://www.linkedin.com/posts/zapier_%F0%9D%97%A6%F0%9D%97%BC%F0%9D%97%B9-%F0%9D%97%A7%F0%9D%97%B2%F0%9D%97%BF%F0%9D%97%BF%F0%9D%97%AE-%F0%9D%97%AE%F0%9D%97%BB%F0%9D%97%B1-%F0%9D%97%9F%F0%9D%98%82%F0%9D%97%BB%F0%9D%97%AE-just-activity-7481038274497605633-wnLy"
        }
      ],
      "notes": [
        "候选 18.1% 出现在 OpenAI 发布材料及 Zapier 官方宣传资料中，但尚未核实它是否对应本地定义的 v1.0.6 private held-out leaderboard、对应指标及完整运行配置。Zapier 文档区分 public task set 与官方 leaderboard 的 held-out private set。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能确认 18.1% 是否来自 AutomationBench v1.0.6 官方私有留出集及其完整测试条件；不写入模型 TOML。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Chartography original paper and launch leaderboard",
          "url": "https://arxiv.org/abs/2608.10677"
        },
        {
          "label": "Surge AI current leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "新增 max reasoning 45.0% 与 default 39.5%，均为 mean Pass@1。原论文说明 100 tasks、每项 20 trials、no tools、Inspect AI harness、Gemini 3.5 Flash judge；无语义版本，论文仅给 2026-07 快照月份，故未填 date。95% CI 分别已记入 variant。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "DataCurve DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DataCurve official repository",
          "url": "https://github.com/datacurve-ai/deep-swe"
        }
      ],
      "notes": [
        "新增 DataCurve leaderboard 的 max / pass@1 73% 记录（页面报告 ±3）；官方仓库说明该榜使用 Pier、mini-swe-agent 和 Modal，数据集为 113 tasks。",
        "保留原 OpenAI 发布行（72.7, resolve rate）作为不同来源记录；未重写其指标或合并 harness。DataCurve 的 ±3 统计定义未公开，因此没有录入 TOML。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis comparison: GPT-5.6 Sol Max",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前官方 leaderboard 直接确认 Non-reasoning 1250 Elo；官方比较页直接确认 Max 1609 Elo。新增两条不同 effort 的成绩。方法页确认 220 tasks、44 occupations、Stirrup、shell + web browsing 与 pairwise Elo。"
      ],
      "status": "待核实",
      "unresolved": [
        "之前研究中 Xhigh 1569 与 High 1504 的候选分数未能在当前直接比较页或当前 leaderboard 复核；未写入 TOML，等待稳定的官方逐配置来源。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison: GPT-5.6 Sol Max",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-sol-xhigh-vs-gpt-5-6-sol"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前可直接复核的 GPT-5.6 Sol Max 原始 HLE 为 49%。AA methodology 确认使用 May 2025 full-HLE revision 的 2,158 道 text-only 题、原始 equality-checker prompt、GPT-5.6 Luna (medium) judge 和 pass@1；未公布评测日期。"
      ],
      "status": "待核实",
      "unresolved": [
        "此前研究还发现 Xhigh 47%、High 46%、Medium 42% 与 Low 39% 候选，但当前比较页已改用 HLE-Diamond 或不再显示原始 HLE 行；这些候选暂不写入，需确认原始 HLE 条件。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-5.6 release (reports OSWorld 2.0)",
          "url": "https://openai.com/index/gpt-5-6/"
        },
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "检查了 OpenAI 已公布的 OSWorld 2.0 结果及 OSWorld V2.1 public-evaluation guide；未找到 GPT-5.6 Sol 的 v2.1 公开成绩。已有 2.0 的 62.6% 不属于 v2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Scale AI official SWE-Bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "ScaleAI official dataset card",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "Scale V2 Full 官方榜确认 Codex / xhigh 得分 95.50（95% CI ±1.40 pp）；Full 是 642 tasks，数据集卡标示版本 2.0.0。与已有无版本 SWE-Bench Pro 行分开保存。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 official results announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Terminal-Bench-Science v0.1.0 release",
          "url": "https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0"
        }
      ],
      "notes": [
        "官方公告确认 Codex 得分 22.4%，覆盖 70 tasks、每项 3 trials；未公布 effort 或具体评测日。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        },
        {
          "label": "Terminal-Bench 4.0 release v4.0.0",
          "url": "https://github.com/harbor-framework/terminal-bench/releases/tag/v4.0.0"
        }
      ],
      "notes": [
        "官方榜确认 Codex / max 配置为 37.3%（95% CI ±3.8 pp）；数据集为 66 tasks。榜单 Release Date 字段是模型发布日期，不作为评测 date 写入。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T00:51+08:00",
      "checked_sources": [
        {
          "label": "Vals AI official Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 v2.2 官榜（2026-10-30）未列 GPT-5.6 Sol。已有 58.01% 属于 v2.1，不迁移到 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 12,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T00:51+08:00",
  "model_id": "openai/gpt-5.6-sol",
  "model_notes": [
    "模型身份及 2026-07-09 发布日期与 OpenAI GPT-5.6 发布页一致；本次保留模型文件原有信息。",
    "收集前保留 12 条历史成绩；本次新增的原始行均来自独立、可核实的来源和配置，未覆盖历史行。"
  ],
  "new_records": 9,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
