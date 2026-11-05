# Grok 4.6 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xai/grok-4.6
- 模型名称：Grok 4.6
- 发布日期：2026-08-12
- 最近检查时间：2026-11-04T18:46+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：8
- 收集前已有成绩数量：8
- 当前已收录的对应成绩数量：6

## 模型身份与范围说明

- 原有 8 条 xAI 结果的 date 都是公告发布日期 2026-09-21，而非来源明确公布的评测日期；已移除这些 date。DeepSWE 与 Terminal-Bench 的指标/版本字段同步按仓库定义修正。
- xAI 公告中的通用 GDPval 1605 Elo 保持原样，不映射到 GDPval-AA v2.1。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 65.2 (metric=pass@1; version=1.1; dataset=113 tasks; effort=High; variant=high effort); 67.0 (metric=pass@1; version=1.1; dataset=113 tasks; effort=medium; variant=leaderboard reports ±2 percentage points; harness=mini-swe-agent) | [xAI Grok 4.7 announcement; Grok 4.6 High row](https://x.ai/news/grok-4-7), [Official DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T18:46+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale official SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [xAI Grok 4.7 announcement](https://x.ai/news/grok-4-7) | 2026-11-04T18:46+08:00 |
| terminal-bench-v4 | 已存在 | 20.3 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; effort=High; variant=high effort) | [xAI Grok 4.7 announcement; Grok 4.6 High row](https://x.ai/news/grok-4-7), [Terminal-Bench 4.0 official release notes](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T18:46+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 11.43 (metric=task resolution rate; version=0.1.0; dataset=70 tasks across 5 domains; variant=pass@1; single run; infrastructure/provider-error retries only; harness=mini-swe-agent) | [Vals AI Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T18:46+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks) | 2026-11-04T18:46+08:00 |
| osworld-v2.1 | 未找到 | — | [Official OSWorld project site](https://osworld-v2.xlang.ai/), [Official OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T18:46+08:00 |
| chartography | 已收录 | 20.5 (metric=accuracy (mean; Pass@1); version=unspecified; dataset=100 tasks; effort=xHigh; variant=10 runs per task; leaderboard mean; harness=Inspect AI; Gemini 3.5 Flash judge) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Official Chartography repository and leaderboard configuration](https://github.com/surge-ai/chartography) | 2026-11-04T18:46+08:00 |
| humanitys-last-exam | 已收录 | 43 (metric=accuracy; version=unspecified; dataset=2,158 text-only questions (Artificial Analysis subset); effort=High; variant=pass@1) | [Artificial Analysis Grok 4.6 High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T18:46+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Grok 4.6 model page](https://artificialanalysis.ai/models/grok-4-6), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T18:46+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis Grok 4.6 comparison snapshot](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6), [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T18:46+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals AI Grok 4.6 model profile](https://www.vals.ai/models/grok_grok-4.6), [Vals Index v2.1 historical leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-04T18:46+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 65.2
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: High
- variant: high effort
- source: [https://x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 67.0
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: medium
- variant: leaderboard reports ±2 percentage points
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [xAI Grok 4.7 announcement; Grok 4.6 High row](https://x.ai/news/grok-4-7)
- [Official DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- xAI 的比较表直接列出 Grok 4.6 High 为 65.2%；已将原记录映射指标修正为 pass@1，并补入该版本定义对应的 113 tasks 与 High 档位。
- 官方 v1.1 排行榜另列 grok-4.6[medium] 为 67%±2%；原样保留 ±2 报告，不推断其统计含义。排行榜显示 113 tasks，所有模型使用 mini-swe-agent。

最近核验时间：2026-11-04T18:46+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale official SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [xAI Grok 4.7 announcement](https://x.ai/news/grok-4-7)

研究备注：
- 已检查 Scale 官方完整 V2 排行榜和模型发布资料；未找到可核实的 Grok 4.6 精确版本成绩。

最近核验时间：2026-11-04T18:46+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 20.3
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- effort: High
- variant: high effort
- source: [https://x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [xAI Grok 4.7 announcement; Grok 4.6 High row](https://x.ai/news/grok-4-7)
- [Terminal-Bench 4.0 official release notes](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- xAI 比较表列出 Grok 4.6 High 为 20.3%。按仓库 Terminal-Bench 4 定义补正指标为 task resolution rate、版本为 4.0.0，并记录 66 tasks 与 High 档位。
- 来源未披露本次行的 harness，也未给出评测日期；不作推断。

最近核验时间：2026-11-04T18:46+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 11.43
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks across 5 domains
- variant: pass@1; single run; infrastructure/provider-error retries only
- harness: mini-swe-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench-Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Vals AI 榜单列出 Grok 4.6 / Mini-SWE-agent 为 11.43%。来源说明使用上游 v0.1.0 的 70 tasks、pass@1 单次运行；仅基础设施或 provider 错误任务会重试。
- 页面的 Updated 2026-10-25 是榜单更新时间，不是 Grok 4.6 的评测日期，因此未写入 date。

最近核验时间：2026-11-04T18:46+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks)

研究备注：
- 官方 1.0.6 页面显示前 10 行后折叠为 See 119 more；当前可读内容不能确认 Grok 4.6 是否在折叠行中。AutomationBench-AA 是不同评测，不映射。

尚未解决的问题：
- Zapier 榜单折叠的 119 行中是否存在 Grok 4.6 尚无法确认。

最近核验时间：2026-11-04T18:46+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Official OSWorld project site](https://osworld-v2.xlang.ai/)
- [Official OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 已检查官方项目站和 OSWorld-V2 仓库，未找到 Grok 4.6 对应结果。官方项目页当前介绍 OSWorld 2.0；不把其他 OSWorld 版本的成绩映射到 v2.1。

最近核验时间：2026-11-04T18:46+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 20.5
- metric: accuracy (mean; Pass@1)
- version: unspecified
- dataset: 100 tasks
- effort: xHigh
- variant: 10 runs per task; leaderboard mean
- harness: Inspect AI; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Official Chartography repository and leaderboard configuration](https://github.com/surge-ai/chartography)

研究备注：
- Surge AI 官方榜单列出 Grok 4.6 (xHigh reasoning) 为 20.5%。官方仓库说明榜单配置为完整 100-task 集、每题 10 runs、accuracy/mean（Pass@1），由 Gemini 3.5 Flash 作 judge，使用 Inspect AI。
- 来源未说明具体发布日期；未填写 date。

最近核验时间：2026-11-04T18:46+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 43
- metric: accuracy
- version: unspecified
- dataset: 2,158 text-only questions (Artificial Analysis subset)
- effort: High
- variant: pass@1
- source: [https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Grok 4.6 High comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 比较页列出 Grok 4.6 High 为 43%。该评测使用原 HLE 的 2,158 道 text-only 子集（完整 2025 年 5 月修订为 2,500 题），评分为 pass@1；不等同于 HLE-Diamond。
- 来源未给出评测日期，未填写 date。

最近核验时间：2026-11-04T18:46+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Grok 4.6 model page](https://artificialanalysis.ai/models/grok-4-6)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前 Artificial Analysis Grok 4.6 页面显示 Intelligence Index 为 N/A；当前方法版本为 v5.0.1。旧比较页的 44 属于 v4.3.2，不能映射为 V5。

最近核验时间：2026-11-04T18:46+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Grok 4.6 comparison snapshot](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6)
- [Artificial Analysis GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 旧版 Artificial Analysis 比较快照曾列 Grok 4.6 High 为 1622 Elo；当前直接查看的 v2.1 排行榜未能交叉确认该模型行，且比较快照没有评测日期。暂不写入该候选分数，保留待复核。
- 模型 TOML 现有的 xAI 通用 GDPval 1605 Elo 未注明 GDPval-AA v2.1 或同一测试配置，因此保留原记录但不作为此 Benchmark 成绩或冲突值。

尚未解决的问题：
- 当前可访问的 v2.1 榜单无法交叉确认旧比较快照中的 1622 Elo；需找到当前可核验的 Grok 4.6 High 结果或确认旧快照仍适用。

最近核验时间：2026-11-04T18:46+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI Grok 4.6 model profile](https://www.vals.ai/models/grok_grok-4.6)
- [Vals Index v2.1 historical leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- 当前 v2.2 榜单列出 Grok 4.7，不含 Grok 4.6。Vals Grok 4.6 profile 的 54.48% 未标为 v2.2；历史 v2.1 页面结果亦不映射到 v2.2。

最近核验时间：2026-11-04T18:46+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.6 model page",
          "url": "https://artificialanalysis.ai/models/grok-4-6"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前 Artificial Analysis Grok 4.6 页面显示 Intelligence Index 为 N/A；当前方法版本为 v5.0.1。旧比较页的 44 属于 v4.3.2，不能映射为 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "官方 1.0.6 页面显示前 10 行后折叠为 See 119 more；当前可读内容不能确认 Grok 4.6 是否在折叠行中。AutomationBench-AA 是不同评测，不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 榜单折叠的 119 行中是否存在 Grok 4.6 尚无法确认。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Official Chartography repository and leaderboard configuration",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge AI 官方榜单列出 Grok 4.6 (xHigh reasoning) 为 20.5%。官方仓库说明榜单配置为完整 100-task 集、每题 10 runs、accuracy/mean（Pass@1），由 Gemini 3.5 Flash 作 judge，使用 Inspect AI。",
        "来源未说明具体发布日期；未填写 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.7 announcement; Grok 4.6 High row",
          "url": "https://x.ai/news/grok-4-7"
        },
        {
          "label": "Official DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "xAI 的比较表直接列出 Grok 4.6 High 为 65.2%；已将原记录映射指标修正为 pass@1，并补入该版本定义对应的 113 tasks 与 High 档位。",
        "官方 v1.1 排行榜另列 grok-4.6[medium] 为 67%±2%；原样保留 ±2 报告，不推断其统计含义。排行榜显示 113 tasks，所有模型使用 mini-swe-agent。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.6 comparison snapshot",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "旧版 Artificial Analysis 比较快照曾列 Grok 4.6 High 为 1622 Elo；当前直接查看的 v2.1 排行榜未能交叉确认该模型行，且比较快照没有评测日期。暂不写入该候选分数，保留待复核。",
        "模型 TOML 现有的 xAI 通用 GDPval 1605 Elo 未注明 GDPval-AA v2.1 或同一测试配置，因此保留原记录但不作为此 Benchmark 成绩或冲突值。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前可访问的 v2.1 榜单无法交叉确认旧比较快照中的 1622 Elo；需找到当前可核验的 Grok 4.6 High 结果或确认旧快照仍适用。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Grok 4.6 High comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-grok-4-6"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 比较页列出 Grok 4.6 High 为 43%。该评测使用原 HLE 的 2,158 道 text-only 子集（完整 2025 年 5 月修订为 2,500 题），评分为 pass@1；不等同于 HLE-Diamond。",
        "来源未给出评测日期，未填写 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Official OSWorld project site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Official OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "已检查官方项目站和 OSWorld-V2 仓库，未找到 Grok 4.6 对应结果。官方项目页当前介绍 OSWorld 2.0；不把其他 OSWorld 版本的成绩映射到 v2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Scale official SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "xAI Grok 4.7 announcement",
          "url": "https://x.ai/news/grok-4-7"
        }
      ],
      "notes": [
        "已检查 Scale 官方完整 V2 排行榜和模型发布资料；未找到可核实的 Grok 4.6 精确版本成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Vals AI 榜单列出 Grok 4.6 / Mini-SWE-agent 为 11.43%。来源说明使用上游 v0.1.0 的 70 tasks、pass@1 单次运行；仅基础设施或 provider 错误任务会重试。",
        "页面的 Updated 2026-10-25 是榜单更新时间，不是 Grok 4.6 的评测日期，因此未写入 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "xAI Grok 4.7 announcement; Grok 4.6 High row",
          "url": "https://x.ai/news/grok-4-7"
        },
        {
          "label": "Terminal-Bench 4.0 official release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "xAI 比较表列出 Grok 4.6 High 为 20.3%。按仓库 Terminal-Bench 4 定义补正指标为 task resolution rate、版本为 4.0.0，并记录 66 tasks 与 High 档位。",
        "来源未披露本次行的 harness，也未给出评测日期；不作推断。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T18:46+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI Grok 4.6 model profile",
          "url": "https://www.vals.ai/models/grok_grok-4.6"
        },
        {
          "label": "Vals Index v2.1 historical leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        }
      ],
      "notes": [
        "当前 v2.2 榜单列出 Grok 4.7，不含 Grok 4.6。Vals Grok 4.6 profile 的 54.48% 未标为 v2.2；历史 v2.1 页面结果亦不映射到 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 8,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T18:46+08:00",
  "model_id": "xai/grok-4.6",
  "model_notes": [
    "原有 8 条 xAI 结果的 date 都是公告发布日期 2026-09-21，而非来源明确公布的评测日期；已移除这些 date。DeepSWE 与 Terminal-Bench 的指标/版本字段同步按仓库定义修正。",
    "xAI 公告中的通用 GDPval 1605 Elo 保持原样，不映射到 GDPval-AA v2.1。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 8
}

-->
