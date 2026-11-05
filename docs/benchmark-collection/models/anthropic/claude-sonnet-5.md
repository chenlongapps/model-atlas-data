# Claude Sonnet 5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-sonnet-5
- 模型名称：Claude Sonnet 5
- 发布日期：2026-06-30
- 最近检查时间：2026-11-05T02:08+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 更新成绩数量：0
- 收集前已有成绩数量：7
- 当前已收录的对应成绩数量：6

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 54 (metric=pass@1; version=1.1; dataset=113 tasks; effort=max; variant=Reported uncertainty ±4%; harness=mini-swe-agent) | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/) | 2026-11-05T02:08+08:00 |
| swe-bench-pro-v2 | 已收录 | 93.15 (metric=task resolution rate; version=2.0.0; dataset=642 public tasks; effort=xhigh; variant=Reported uncertainty ±1.71 percentage points; uncapped cost; up to 250 turns; harness=Claude Code) | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T02:08+08:00 |
| terminal-bench-v4 | 冲突 | 80.4 (metric=success rate; version=2.1; harness=Terminus-2); 14 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; effort=Max; variant=pass@1; averaged over 3 repeats per task; maximum 500 agent steps; Artificial Analysis run; harness=mini-swe-agent) | [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6), [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:08+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T02:08+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/blog/claude-models/](https://zapier.com/blog/claude-models/), [https://zapier.com/benchmarks](https://zapier.com/benchmarks) | 2026-11-05T02:08+08:00 |
| osworld-v2.1 | 未找到 | — | [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5), [https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T02:08+08:00 |
| chartography | 冲突 | — | [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography), [https://arxiv.org/html/2608.10677](https://arxiv.org/html/2608.10677) | 2026-11-05T02:08+08:00 |
| humanitys-last-exam | 已收录 | 41 (metric=accuracy; dataset=2,158 text-only questions; effort=Max; variant=pass@1; judged by GPT-5.6 Luna (medium)) | [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:08+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/claude-sonnet-5](https://artificialanalysis.ai/models/claude-sonnet-5), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:08+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1221 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Non-reasoning, High; variant=Reported uncertainty −19/+19 Elo; blind pairwise comparisons; harness=Stirrup); 1167 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Medium; variant=Reported uncertainty −18/+18 Elo; blind pairwise comparisons; harness=Stirrup) | [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6), [https://artificialanalysis.ai/de/models/comparisons/step-5-vs-claude-sonnet-5](https://artificialanalysis.ai/de/models/comparisons/step-5-vs-claude-sonnet-5) | 2026-11-05T02:08+08:00 |
| vals-index-v2.2 | 未找到 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.vals.ai/benchmarks/vals_index_v1_2](https://www.vals.ai/benchmarks/vals_index_v1_2), [https://www.vals.ai/models/anthropic_claude-sonnet-5](https://www.vals.ai/models/anthropic_claude-sonnet-5) | 2026-11-05T02:08+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 54
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: max
- variant: Reported uncertainty ±4%
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)

研究备注：
- 官方 v1.1 榜单列 Claude Sonnet 5 [max]：54%±4%；113 tasks，mini-swe-agent。成绩保留主分 54，原报告的不确定范围已记入 variant。

最近核验时间：2026-11-05T02:08+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 93.15
- metric: task resolution rate
- version: 2.0.0
- dataset: 642 public tasks
- effort: xhigh
- variant: Reported uncertainty ±1.71 percentage points; uncapped cost; up to 250 turns
- harness: Claude Code
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- V2 官方榜列 Sonnet 5 (Claude Code) xhigh：93.15%±1.71%；V2 公共集 642 tasks，成本 uncapped，turn limit 250。

最近核验时间：2026-11-05T02:08+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 80.4
- metric: success rate
- version: 2.1
- harness: Terminus-2
- source: [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5)
- date: 2026-06-30
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 14
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- effort: Max
- variant: pass@1; averaged over 3 repeats per task; maximum 500 agent steps; Artificial Analysis run
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6)
- [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 比较页列 Sonnet 5 (Max) 为 14%；其方法页将 TB4 定为 66 tasks、mini-swe-agent、pass@1 每题 3 次重复、最多 500 steps。Anthropic 发布图表另列 10.3%，但未提供可与 AA 条件对齐的 harness/effort 等信息；不增加该行。

尚未解决的问题：
- AA 14% 与 Anthropic 发布图表 10.3% 均指向 Terminal-Bench 4.0，现有公开资料未能对齐两次评测配置或解释差异。

最近核验时间：2026-11-05T02:08+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 已检查官方 0.1 结果页；公开列出的参测结果未包含 Claude Sonnet 5。现有 81.2% 是 OSWorld-Verified，与此项无关。

最近核验时间：2026-11-05T02:08+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/blog/claude-models/](https://zapier.com/blog/claude-models/)
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

研究备注：
- Zapier 模型文章列 Sonnet 5 (Max) pass rate 10.65%、$0.88/task，但没有标明 benchmark 版本；当前榜单为 1.0.6，余下 119 条结果折叠，无法确认该分数对应 1.0.6。

尚未解决的问题：
- 已有 10.65% 的非版本化公开记录，无法可靠映射到 AutomationBench 1.0.6；不写入模型 TOML。

最近核验时间：2026-11-05T02:08+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5)
- [https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- Anthropic 发布资料中的 81.2% 标为 OSWorld-Verified，不是 OSWorld 2.1；官方 v2.1 指南说明截图观察与桌面动作协议，未找到 Sonnet 5 的 v2.1 分数。

最近核验时间：2026-11-05T02:08+08:00

### Chartography (chartography)

- 当前状态：冲突。

已检查的主要资料：
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- [https://arxiv.org/html/2608.10677](https://arxiv.org/html/2608.10677)

研究备注：
- Surge 当前榜列 Claude Sonnet 5 (Adaptive/Max) 16.9%；论文 July 2026 launch snapshot 对同名配置列 16.6%±1.1%。论文记录 100 tasks×20 trials、mean pass@1、无工具、Inspect AI。

尚未解决的问题：
- 实时榜与论文快照对同名 Adaptive/Max 配置给出不同分数，缺少对应 run 日期/修订关系；不选取其中任一分数写入。

最近核验时间：2026-11-05T02:08+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 41
- metric: accuracy
- dataset: 2,158 text-only questions
- effort: Max
- variant: pass@1; judged by GPT-5.6 Luna (medium)
- source: [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 比较页列 Sonnet 5 (Max) 41%。其原始 HLE 方法使用 2,158 道 text-only 题、pass@1，由 GPT-5.6 Luna (medium) 等值判分；此项是原始 HLE，不是 V5 使用的 HLE-Diamond。

最近核验时间：2026-11-05T02:08+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/claude-sonnet-5](https://artificialanalysis.ai/models/claude-sonnet-5)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前模型页未提供 AA Intelligence Index V5 分数；历史比较页的 38 属于 V4.3.2，不能映射到 V5.0.1。

最近核验时间：2026-11-05T02:08+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1221
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Non-reasoning, High
- variant: Reported uncertainty −19/+19 Elo; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1167
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Medium
- variant: Reported uncertainty −18/+18 Elo; blind pairwise comparisons
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6)
- [https://artificialanalysis.ai/de/models/comparisons/step-5-vs-claude-sonnet-5](https://artificialanalysis.ai/de/models/comparisons/step-5-vs-claude-sonnet-5)

研究备注：
- 官方当前榜列 Claude Sonnet 5 Non-reasoning, High：1221 Elo (−19/+19) 和 Medium：1167 Elo (−18/+18)，均为 2026 年 6 月；已分别收录。GDPval-AA v2.1 使用 220 tasks/44 occupations、Stirrup、blind pairwise comparisons。两张 AA Max 比较页分别列 1464 与 1449 Elo；两页都标为 v2.1 且努力档为 Max，尚无可核实的修订/日期差异说明，因此未录入 Max 值。

尚未解决的问题：
- 相同 Max 档的官方比较页分数 1464/1449 冲突；需 AA 明确结果更新或评测批次后再录入。

最近核验时间：2026-11-05T02:08+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.vals.ai/benchmarks/vals_index_v1_2](https://www.vals.ai/benchmarks/vals_index_v1_2)
- [https://www.vals.ai/models/anthropic_claude-sonnet-5](https://www.vals.ai/models/anthropic_claude-sonnet-5)

研究备注：
- 模型历史页中的 68.61% 属 Vals Index v1.2；当前目标为 v2.2，未找到可核实的 v2.2 分数。

最近核验时间：2026-11-05T02:08+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/claude-sonnet-5"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前模型页未提供 AA Intelligence Index V5 分数；历史比较页的 38 属于 V4.3.2，不能映射到 V5.0.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/blog/claude-models/"
        },
        {
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Zapier 模型文章列 Sonnet 5 (Max) pass rate 10.65%、$0.88/task，但没有标明 benchmark 版本；当前榜单为 1.0.6，余下 119 条结果折叠，无法确认该分数对应 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "已有 10.65% 的非版本化公开记录，无法可靠映射到 AutomationBench 1.0.6；不写入模型 TOML。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "url": "https://arxiv.org/html/2608.10677"
        }
      ],
      "notes": [
        "Surge 当前榜列 Claude Sonnet 5 (Adaptive/Max) 16.9%；论文 July 2026 launch snapshot 对同名配置列 16.6%±1.1%。论文记录 100 tasks×20 trials、mean pass@1、无工具、Inspect AI。"
      ],
      "status": "冲突",
      "unresolved": [
        "实时榜与论文快照对同名 Adaptive/Max 配置给出不同分数，缺少对应 run 日期/修订关系；不选取其中任一分数写入。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "官方 v1.1 榜单列 Claude Sonnet 5 [max]：54%±4%；113 tasks，mini-swe-agent。成绩保留主分 54，原报告的不确定范围已记入 variant。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "url": "https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6"
        },
        {
          "url": "https://artificialanalysis.ai/de/models/comparisons/step-5-vs-claude-sonnet-5"
        }
      ],
      "notes": [
        "官方当前榜列 Claude Sonnet 5 Non-reasoning, High：1221 Elo (−19/+19) 和 Medium：1167 Elo (−18/+18)，均为 2026 年 6 月；已分别收录。GDPval-AA v2.1 使用 220 tasks/44 occupations、Stirrup、blind pairwise comparisons。两张 AA Max 比较页分别列 1464 与 1449 Elo；两页都标为 v2.1 且努力档为 Max，尚无可核实的修订/日期差异说明，因此未录入 Max 值。"
      ],
      "status": "冲突",
      "unresolved": [
        "相同 Max 档的官方比较页分数 1464/1449 冲突；需 AA 明确结果更新或评测批次后再录入。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 比较页列 Sonnet 5 (Max) 41%。其原始 HLE 方法使用 2,158 道 text-only 题、pass@1，由 GPT-5.6 Luna (medium) 等值判分；此项是原始 HLE，不是 V5 使用的 HLE-Diamond。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://www.anthropic.com/news/claude-sonnet-5"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "Anthropic 发布资料中的 81.2% 标为 OSWorld-Verified，不是 OSWorld 2.1；官方 v2.1 指南说明截图观察与桌面动作协议，未找到 Sonnet 5 的 v2.1 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "V2 官方榜列 Sonnet 5 (Claude Code) xhigh：93.15%±1.71%；V2 公共集 642 tasks，成本 uncapped，turn limit 250。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "已检查官方 0.1 结果页；公开列出的参测结果未包含 Claude Sonnet 5。现有 81.2% 是 OSWorld-Verified，与此项无关。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-vs-claude-sonnet-4-6"
        },
        {
          "url": "https://www.anthropic.com/news/claude-sonnet-5"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 比较页列 Sonnet 5 (Max) 为 14%；其方法页将 TB4 定为 66 tasks、mini-swe-agent、pass@1 每题 3 次重复、最多 500 steps。Anthropic 发布图表另列 10.3%，但未提供可与 AA 条件对齐的 harness/effort 等信息；不增加该行。"
      ],
      "status": "冲突",
      "unresolved": [
        "AA 14% 与 Anthropic 发布图表 10.3% 均指向 Terminal-Bench 4.0，现有公开资料未能对齐两次评测配置或解释差异。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:08+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index_v1_2"
        },
        {
          "url": "https://www.vals.ai/models/anthropic_claude-sonnet-5"
        }
      ],
      "notes": [
        "模型历史页中的 68.61% 属 Vals Index v1.2；当前目标为 v2.2，未找到可核实的 v2.2 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 7,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:08+08:00",
  "model_id": "anthropic/claude-sonnet-5",
  "new_records": 6,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
