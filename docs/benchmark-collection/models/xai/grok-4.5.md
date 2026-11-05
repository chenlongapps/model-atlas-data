# Grok 4.5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-4.5
- 模型名称：Grok 4.5
- 发布日期：2026-07-16
- 最近检查时间：2026-11-05T01:13+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- xAI 官方发布页注明 Grok 4.5 于 2026-07-16 发布；据此将模型 TOML 的 release_date 从 2026-07-08 更正为 2026-07-16，并按新日期重新排序队列：https://x.ai/news/grok-4-5。
- TOML 中原有的 6 条成绩保留；本轮新增 4 条。可精确映射到当前 11 项定义的成绩共 4 条。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 62.0 (metric=resolve rate; version=1.0); 53 (metric=resolve rate; version=1.1; harness=mini-swe-agent) | [xAI 官方发布页](https://x.ai/news/grok-4-5), [DataCurve DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DataCurve changelog](https://deepswe.datacurve.ai/changelog) | 2026-11-05T01:13+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [xAI Grok 4.5 announcement](https://x.ai/news/grok-4-5) | 2026-11-05T01:13+08:00 |
| terminal-bench-v4 | 已收录 | 83.3 (metric=success rate; version=2.1); 12.4 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; effort=High; variant=95% CI: 9.8%–15.0%; harness=Grok Build) | [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?efforts=all&version=4.0), [ModelCap archive transcribing the official board row](https://modelcap.ai/benchmarks/terminal-bench-4), [Harbor raw evaluation row](https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4/leaderboards/4-0-0/rows/0eed5a0d-96b6-491b-aeb7-cd5e4700c2d7) | 2026-11-05T01:13+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus) | 2026-11-05T01:13+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench), [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus) | 2026-11-05T01:13+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/) | 2026-11-05T01:13+08:00 |
| chartography | 已收录 | 17.3 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=default; variant=20 trials per task; no tools; 95% CI ±1.1 percentage points; frozen launch snapshot July 2026; harness=Inspect AI; judge=Gemini 3.5 Flash); 16.7 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=high reasoning; variant=20 trials per task; no tools; 95% CI ±1.1 percentage points; frozen launch snapshot July 2026; harness=Inspect AI; judge=Gemini 3.5 Flash) | [Chartography paper (frozen July 2026 results)](https://arxiv.org/html/2608.10677), [Surge Chartography live leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography dataset](https://huggingface.co/datasets/surgeai/chartography), [Chartography harness](https://github.com/surge-ai/chartography) | 2026-11-05T01:13+08:00 |
| humanitys-last-exam | 已收录 | 42.7 (metric=accuracy; dataset=May 2025; text-only; 2,158 questions; effort=high; variant=no tools; pass@1; reasoning=true; harness=Artificial Analysis) | [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [ModelCap archived Grok 4.5 benchmark row](https://modelcap.ai/model/x-ai-grok-4-5) | 2026-11-05T01:13+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Grok 4.5 model page](https://artificialanalysis.ai/models/grok-4-5), [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus), [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T01:13+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Grok comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus), [Secondary leaderboard snapshot](https://bubblenews.today/benchmarks/gdpval-aa/) | 2026-11-05T01:13+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index official benchmark page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T01:13+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 62.0
- metric: resolve rate
- version: 1.0
- source: [https://x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)
- date: 2026-07-08
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 53
- metric: resolve rate
- version: 1.1
- harness: mini-swe-agent
- source: [https://x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)
- date: 2026-07-08
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [xAI 官方发布页](https://x.ai/news/grok-4-5)
- [DataCurve DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DataCurve changelog](https://deepswe.datacurve.ai/changelog)

研究备注：
- 模型 TOML 已有 DeepSWE v1.1、53%、resolve rate、mini-swe-agent 记录；另有 62.0% 是 v1.0，不属于本项。DataCurve v1.1 页面说明 113 个任务。
- 当前本地定义的 metric 为 pass@1，而旧记录写 resolve rate；xAI 公告发布日期为 2026-07-16，旧记录 date=2026-07-08，DataCurve changelog 显示结果于 7 月 16 日加入。保留成绩原样，待确认定义映射和 date 字段含义。

尚未解决的问题：
- 现有 53% 记录的 metric 与本地定义不一致，且记录日期早于 xAI 官方发布公告；未擅自改写历史记录。

最近核验时间：2026-11-05T01:13+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [xAI Grok 4.5 announcement](https://x.ai/news/grok-4-5)

研究备注：
- 未找到可归属 SWE-bench Pro V2 (2.0.0) 的 Grok 4.5 成绩。模型 TOML 中未标版本的 64.7% 是 xAI 的 SWE Bench Pro 旧记录，不能映射到 V2。

最近核验时间：2026-11-05T01:13+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 83.3
- metric: success rate
- version: 2.1
- source: [https://x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)
- date: 2026-07-08
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 12.4
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- effort: High
- variant: 95% CI: 9.8%–15.0%
- harness: Grok Build
- source: [https://www.tbench.ai/?efforts=all&version=4.0](https://www.tbench.ai/?efforts=all&version=4.0)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?efforts=all&version=4.0)
- [ModelCap archive transcribing the official board row](https://modelcap.ai/benchmarks/terminal-bench-4)
- [Harbor raw evaluation row](https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4/leaderboards/4-0-0/rows/0eed5a0d-96b6-491b-aeb7-cd5e4700c2d7)

研究备注：
- 官方榜单归档列出 Grok 4.5 / Grok Build / High，12.4%，95% CI 9.8%–15.0%；Harbor 原始行确认 Terminal-Bench 4.0.0、330/330 trials、16 errors、avg reward 0.13。12.4% 取自榜单归档，不由 avg reward 推算。数据集为 66 tasks。

最近核验时间：2026-11-05T01:13+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus)

研究备注：
- 官方 0.1 结果资料未列 Grok 4.5；资料中出现的 Grok 4.6 结果不适用于本模型。未复用其他版本或模型成绩。

最近核验时间：2026-11-05T01:13+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus)

研究备注：
- Zapier 页面当前可见 10 行并折叠 119 行，不能据此断言完整排行榜没有 Grok 4.5。Artificial Analysis 的 AutomationBench-AA 58% 是不同评测，未映射到 AutomationBench 1.0.6。

尚未解决的问题：
- 没有找到能够直接核实 Grok 4.5 在私有 held-out v1.0.6 任务集上的成绩、effort、harness 或评测日期。

最近核验时间：2026-11-05T01:13+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/)

研究备注：
- 未找到可验证的 OSWorld 2.1 Grok 4.5 公开成绩；保留 OSWorld 2.0 或其他版本为不同评测。

最近核验时间：2026-11-05T01:13+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 17.3
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: default
- variant: 20 trials per task; no tools; 95% CI ±1.1 percentage points; frozen launch snapshot July 2026
- harness: Inspect AI; judge=Gemini 3.5 Flash
- source: [https://arxiv.org/abs/2608.10677](https://arxiv.org/abs/2608.10677)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Chartography
- score: 16.7
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: high reasoning
- variant: 20 trials per task; no tools; 95% CI ±1.1 percentage points; frozen launch snapshot July 2026
- harness: Inspect AI; judge=Gemini 3.5 Flash
- source: [https://arxiv.org/abs/2608.10677](https://arxiv.org/abs/2608.10677)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Chartography paper (frozen July 2026 results)](https://arxiv.org/html/2608.10677)
- [Surge Chartography live leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography dataset](https://huggingface.co/datasets/surgeai/chartography)
- [Chartography harness](https://github.com/surge-ai/chartography)

研究备注：
- 论文 Table 3 直接列出 Grok 4.5 default 17.3 ±1.1% 和 high reasoning 16.7 ±1.1%；每项 100 tasks × 20 trials，mean pass@1，无工具，Inspect AI，Gemini 3.5 Flash judge。当前 Surge 榜单将 high 显示为整数 17%，与论文精度相符，未作为冲突。

最近核验时间：2026-11-05T01:13+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 42.7
- metric: accuracy
- dataset: May 2025; text-only; 2,158 questions
- effort: high
- variant: no tools; pass@1; reasoning=true
- harness: Artificial Analysis
- source: [https://modelcap.ai/model/x-ai-grok-4-5](https://modelcap.ai/model/x-ai-grok-4-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [ModelCap archived Grok 4.5 benchmark row](https://modelcap.ai/model/x-ai-grok-4-5)

研究备注：
- ModelCap 归档的 Artificial Analysis 结果为 42.7% accuracy，配置注明 Grok 4.5 (high)、May 2025 HLE、2,158 道 text-only questions、no tools、pass@1、reasoning=true；其发布日期列为 2026-09-05。精确值来自归档行，当前 AA 页面未检索到相同文本行。

最近核验时间：2026-11-05T01:13+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Grok 4.5 model page](https://artificialanalysis.ai/models/grok-4-5)
- [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus)
- [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前 Grok 4.5 模型页显示 Intelligence Index N/A；比较页的 v5.0.1 综合指数值为空。ModelCap 归档的 39.1 属于旧 v4.3，不能填入 V5。

最近核验时间：2026-11-05T01:13+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Grok comparison](https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus)
- [Secondary leaderboard snapshot](https://bubblenews.today/benchmarks/gdpval-aa/)

研究备注：
- 当前 AA v2.1 排行榜列出 Grok 4.7，但没有 Grok 4.5；早期索引/第三方快照出现 1381 与 1389 两个候选 Elo，未能从当前原始榜单复核。

尚未解决的问题：
- 1381 与 1389 的来源快照及测试配置尚未对齐；不选择其一，不写入成绩。

最近核验时间：2026-11-05T01:13+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index official benchmark page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 Vals Index v2.2 资料中未找到 Grok 4.5 对应结果；较新榜单出现的 Grok 4.7 不属于本模型，也未复用旧版成绩。

最近核验时间：2026-11-05T01:13+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.5 model page",
          "url": "https://artificialanalysis.ai/models/grok-4-5"
        },
        {
          "label": "Artificial Analysis comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus"
        },
        {
          "label": "Artificial Analysis Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前 Grok 4.5 模型页显示 Intelligence Index N/A；比较页的 v5.0.1 综合指数值为空。ModelCap 归档的 39.1 属于旧 v4.3，不能填入 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Artificial Analysis comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus"
        }
      ],
      "notes": [
        "Zapier 页面当前可见 10 行并折叠 119 行，不能据此断言完整排行榜没有 Grok 4.5。Artificial Analysis 的 AutomationBench-AA 58% 是不同评测，未映射到 AutomationBench 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有找到能够直接核实 Grok 4.5 在私有 held-out v1.0.6 任务集上的成绩、effort、harness 或评测日期。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Chartography paper (frozen July 2026 results)",
          "url": "https://arxiv.org/html/2608.10677"
        },
        {
          "label": "Surge Chartography live leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography dataset",
          "url": "https://huggingface.co/datasets/surgeai/chartography"
        },
        {
          "label": "Chartography harness",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "论文 Table 3 直接列出 Grok 4.5 default 17.3 ±1.1% 和 high reasoning 16.7 ±1.1%；每项 100 tasks × 20 trials，mean pass@1，无工具，Inspect AI，Gemini 3.5 Flash judge。当前 Surge 榜单将 high 显示为整数 17%，与论文精度相符，未作为冲突。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "xAI 官方发布页",
          "url": "https://x.ai/news/grok-4-5"
        },
        {
          "label": "DataCurve DeepSWE v1.1",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DataCurve changelog",
          "url": "https://deepswe.datacurve.ai/changelog"
        }
      ],
      "notes": [
        "模型 TOML 已有 DeepSWE v1.1、53%、resolve rate、mini-swe-agent 记录；另有 62.0% 是 v1.0，不属于本项。DataCurve v1.1 页面说明 113 个任务。",
        "当前本地定义的 metric 为 pass@1，而旧记录写 resolve rate；xAI 公告发布日期为 2026-07-16，旧记录 date=2026-07-08，DataCurve changelog 显示结果于 7 月 16 日加入。保留成绩原样，待确认定义映射和 date 字段含义。"
      ],
      "status": "待核实",
      "unresolved": [
        "现有 53% 记录的 metric 与本地定义不一致，且记录日期早于 xAI 官方发布公告；未擅自改写历史记录。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Grok comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus"
        },
        {
          "label": "Secondary leaderboard snapshot",
          "url": "https://bubblenews.today/benchmarks/gdpval-aa/"
        }
      ],
      "notes": [
        "当前 AA v2.1 排行榜列出 Grok 4.7，但没有 Grok 4.5；早期索引/第三方快照出现 1381 与 1389 两个候选 Elo，未能从当前原始榜单复核。"
      ],
      "status": "冲突",
      "unresolved": [
        "1381 与 1389 的来源快照及测试配置尚未对齐；不选择其一，不写入成绩。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "ModelCap archived Grok 4.5 benchmark row",
          "url": "https://modelcap.ai/model/x-ai-grok-4-5"
        }
      ],
      "notes": [
        "ModelCap 归档的 Artificial Analysis 结果为 42.7% accuracy，配置注明 Grok 4.5 (high)、May 2025 HLE、2,158 道 text-only questions、no tools、pass@1、reasoning=true；其发布日期列为 2026-09-05。精确值来自归档行，当前 AA 页面未检索到相同文本行。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld 2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld-V2 leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "未找到可验证的 OSWorld 2.1 Grok 4.5 公开成绩；保留 OSWorld 2.0 或其他版本为不同评测。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "xAI Grok 4.5 announcement",
          "url": "https://x.ai/news/grok-4-5"
        }
      ],
      "notes": [
        "未找到可归属 SWE-bench Pro V2 (2.0.0) 的 Grok 4.5 成绩。模型 TOML 中未标版本的 64.7% 是 xAI 的 SWE Bench Pro 旧记录，不能映射到 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Artificial Analysis comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-command-a-plus"
        }
      ],
      "notes": [
        "官方 0.1 结果资料未列 Grok 4.5；资料中出现的 Grok 4.6 结果不适用于本模型。未复用其他版本或模型成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        },
        {
          "label": "ModelCap archive transcribing the official board row",
          "url": "https://modelcap.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Harbor raw evaluation row",
          "url": "https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4/leaderboards/4-0-0/rows/0eed5a0d-96b6-491b-aeb7-cd5e4700c2d7"
        }
      ],
      "notes": [
        "官方榜单归档列出 Grok 4.5 / Grok Build / High，12.4%，95% CI 9.8%–15.0%；Harbor 原始行确认 Terminal-Bench 4.0.0、330/330 trials、16 errors、avg reward 0.13。12.4% 取自榜单归档，不由 avg reward 推算。数据集为 66 tasks。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T01:13+08:00",
      "checked_sources": [
        {
          "label": "Vals Index official benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 Vals Index v2.2 资料中未找到 Grok 4.5 对应结果；较新榜单出现的 Grok 4.7 不属于本模型，也未复用旧版成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T01:13+08:00",
  "model_id": "xai/grok-4.5",
  "model_notes": [
    "xAI 官方发布页注明 Grok 4.5 于 2026-07-16 发布；据此将模型 TOML 的 release_date 从 2026-07-08 更正为 2026-07-16，并按新日期重新排序队列：https://x.ai/news/grok-4-5。",
    "TOML 中原有的 6 条成绩保留；本轮新增 4 条。可精确映射到当前 11 项定义的成绩共 4 条。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
