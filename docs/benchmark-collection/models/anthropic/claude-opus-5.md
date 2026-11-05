# Claude Opus 5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-opus-5
- 模型名称：Claude Opus 5
- 发布日期：2026-07-24
- 最近检查时间：2026-11-04T21:58+08:00
- 整体处理状态：待复核
- 新增成绩数量：8
- 更新成绩数量：0
- 收集前已有成绩数量：2
- 当前已收录的对应成绩数量：7

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 68.8 (metric=resolve rate; version=1.1); 74.0 (metric=pass@1; version=1.1; dataset=113 tasks; effort=max; variant=reported uncertainty ±4 percentage points; harness=mini-SWE-agent) | [DeepSWE v1.1 official results](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology and announcement](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T21:58+08:00 |
| swe-bench-pro-v2 | 待核实 | 99.4 (metric=Pass@1; version=2.0.0; dataset=642 tasks (638/642; reported uncertainty ±0.40 percentage points); effort=xhigh; harness=Claude Code) | [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale AI SWE-bench Pro V2 methodology](https://labs.scale.com/blog/swe-bench-pro-v2?trk=article-ssr-frontend-pulse_little-text-block) | 2026-11-04T21:58+08:00 |
| terminal-bench-v4 | 待核实 | 53.53 (metric=accuracy; version=4.0.0; dataset=66 tasks; variant=avg@3; each run pass@1; harness=Mini-SWE-agent) | [Vals Terminal-Bench 4 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Terminal-Bench 4.0 official announcement](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T21:58+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 27.14 (metric=accuracy; version=0.1.0; dataset=70 tasks; variant=single run; pass@1; retries for provider infrastructure errors; harness=Mini-SWE-agent) | [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Terminal-Bench Science 0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T21:58+08:00 |
| automationbench-v1.0.6 | 已收录 | 26.0 (metric=success rate; variant=max effort); 26.9 (metric=task_completed_correctly; version=1.0.6; dataset=657 tasks; effort=Max) | [Zapier AutomationBench report (includes Claude Opus 5 comparison)](https://zapier.com/benchmarks/claude-opus5_5-report) | 2026-11-04T21:58+08:00 |
| osworld-v2.1 | 已收录 | 70.6 (metric=success rate; version=2.0); 44.33 (metric=binary task completion rate; version=osworld-v2.1; dataset=108 tasks; effort=Max; variant=batch tool; 500-step budget) | [OSWorld V2 leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2.1 release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T21:58+08:00 |
| chartography | 已收录 | 27.3 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=Adaptive/Max; variant=10 runs per task; harness=Inspect AI) | [Surge AI Chartography results](https://surgehq.ai/benchmarks/chartography), [Chartography benchmark repository](https://github.com/surge-ai/chartography) | 2026-11-04T21:58+08:00 |
| humanitys-last-exam | 冲突 | 56.3 (metric=accuracy; variant=no tools); 64.7 (metric=accuracy; variant=with tools) | [Anthropic Claude Opus 5 system card](https://www.anthropic.com/claude-opus-5-system-card), [Anthropic Claude Fable and Mythos 5.1 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-04T21:58+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Claude Opus 5 profile](https://artificialanalysis.ai/models/claude-opus-5/), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T21:58+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1861 (metric=Elo; version=v2; variant=max effort); 1730 (metric=Elo rating; version=2.1; dataset=220 tasks; effort=Max; harness=Stirrup) | [Artificial Analysis GDPval-AA leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T21:58+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:58+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 68.8
- metric: resolve rate
- version: 1.1
- source: [https://www.anthropic.com/claude-opus-5-system-card](https://www.anthropic.com/claude-opus-5-system-card)
- date: 2026-07-24
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 74.0
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: max
- variant: reported uncertainty ±4 percentage points
- harness: mini-SWE-agent
- source: [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepSWE v1.1 official results](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology and announcement](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 新增的是 DeepSWE v1.1 官方排行榜上的 pass@1（max effort）结果；原有 68.8 resolve rate 记录保留，二者指标不同。

最近核验时间：2026-11-04T21:58+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 源 TOML 成绩记录 1

- name: SWE-bench Pro
- score: 99.4
- metric: Pass@1
- version: 2.0.0
- dataset: 642 tasks (638/642; reported uncertainty ±0.40 percentage points)
- effort: xhigh
- harness: Claude Code
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale AI SWE-bench Pro V2 methodology](https://labs.scale.com/blog/swe-bench-pro-v2?trk=article-ssr-frontend-pulse_little-text-block)

研究备注：
- 官方 V2 默认集排行榜列出 Claude Opus 5 / Claude Code / xhigh：99.40% ±0.40%，638/642。源记录保留排行榜的 Pass@1 标签。
- 模型原有 79.2 resolve rate 来自 Opus 5 发布系统卡，未标为 V2；保留且不映射到 V2。

尚未解决的问题：
- 排行榜指标标签 Pass@1 与本仓库定义的 task resolution rate 不完全一致；覆盖率暂不计入，需核实二者语义映射。

最近核验时间：2026-11-04T21:58+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 53.53
- metric: accuracy
- version: 4.0.0
- dataset: 66 tasks
- variant: avg@3; each run pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench 4 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Terminal-Bench 4.0 official announcement](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Vals 列出 Claude Opus 5 53.53%，版本 4.0，66 项任务，Mini-SWE-agent，avg@3（每次运行 pass@1）。

尚未解决的问题：
- 原始来源指标为 accuracy，本仓库定义为 task resolution rate；保留源标签，暂不计入精确映射覆盖率。

最近核验时间：2026-11-04T21:58+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 27.14
- metric: accuracy
- version: 0.1.0
- dataset: 70 tasks
- variant: single run; pass@1; retries for provider infrastructure errors
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Terminal-Bench Science 0.1 official announcement](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Vals 列出 Claude Opus 5 27.14%，70 项任务，Mini-SWE-agent，单次运行 pass@1；基础设施错误可重试。

尚未解决的问题：
- 原始来源指标为 accuracy，本仓库定义为 task resolution rate；保留源标签，暂不计入精确映射覆盖率。

最近核验时间：2026-11-04T21:58+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 26.0
- metric: success rate
- variant: max effort
- source: [https://www.anthropic.com/claude-opus-5-system-card](https://www.anthropic.com/claude-opus-5-system-card)
- date: 2026-07-24
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 26.9
- metric: task_completed_correctly
- version: 1.0.6
- dataset: 657 tasks
- effort: Max
- source: [https://zapier.com/benchmarks/claude-opus5_5-report](https://zapier.com/benchmarks/claude-opus5_5-report)
- date: 2026-09-17 to 2026-09-18
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench report (includes Claude Opus 5 comparison)](https://zapier.com/benchmarks/claude-opus5_5-report)

研究备注：
- Zapier 2026-09-17 至 2026-09-18 的报告明确列出 Claude Opus 5 Max 26.9%，指标 task_completed_correctly、657 项任务；TOML 另保留发布系统卡中的旧 26.0 行。

最近核验时间：2026-11-04T21:58+08:00

### OSWorld (osworld-v2.1)

#### 源 TOML 成绩记录 1

- name: OSWorld
- score: 70.6
- metric: success rate
- version: 2.0
- source: [https://www.anthropic.com/claude-opus-5-system-card](https://www.anthropic.com/claude-opus-5-system-card)
- date: 2026-07-24
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: OSWorld
- score: 44.33
- metric: binary task completion rate
- version: osworld-v2.1
- dataset: 108 tasks
- effort: Max
- variant: batch tool; 500-step budget
- source: [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [OSWorld V2 leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- V2.1 榜单对应 Claude Opus 5 Max，batch tool，44.33% binary task completion，108 项完整任务，500 步上限；既有 70.6 为 OSWorld 2.0，分别保留。

最近核验时间：2026-11-04T21:58+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 27.3
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: Adaptive/Max
- variant: 10 runs per task
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography results](https://surgehq.ai/benchmarks/chartography)
- [Chartography benchmark repository](https://github.com/surge-ai/chartography)

研究备注：
- Surge 榜单列出 Claude Opus 5 (Adaptive/Max) 27.3%；100 项任务，Pass@1，10 次运行/任务，Inspect AI。

最近核验时间：2026-11-04T21:58+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 56.3
- metric: accuracy
- variant: no tools
- source: [https://www.anthropic.com/claude-opus-5-system-card](https://www.anthropic.com/claude-opus-5-system-card)
- date: 2026-07-24
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 64.7
- metric: accuracy
- variant: with tools
- source: [https://www.anthropic.com/claude-opus-5-system-card](https://www.anthropic.com/claude-opus-5-system-card)
- date: 2026-07-24
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic Claude Opus 5 system card](https://www.anthropic.com/claude-opus-5-system-card)
- [Anthropic Claude Fable and Mythos 5.1 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- 现有 Claude Opus 5 系统卡给出无工具 56.3%、带工具 64.7%；Anthropic 后续 Fable/Mythos 5.1 公告将 Opus 5 的相同配置列为无工具 56.6%、带工具 63.6%。保留系统卡原记录，不覆盖或新增竞争记录。

尚未解决的问题：
- Anthropic 两份官方资料对 Opus 5 相同 HLE 工具配置给出不同成绩，尚未说明评测轮次或设置差异；需要核实。

最近核验时间：2026-11-04T21:58+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Claude Opus 5 profile](https://artificialanalysis.ai/models/claude-opus-5/)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis 的 Claude Opus 5 模型页当前未提供 Intelligence Index V5 成绩；未从资料核验出可加入的分数。

最近核验时间：2026-11-04T21:58+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1861
- metric: Elo
- version: v2
- variant: max effort
- source: [https://www.anthropic.com/claude-opus-5-system-card](https://www.anthropic.com/claude-opus-5-system-card)
- date: 2026-07-24
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1730
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- effort: Max
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Artificial Analysis V2.1 榜单列出 Claude Opus 5 (Max) 1730 Elo ±19，220 项任务，Stirrup harness；原有 1861 是 V2，独立保留。

最近核验时间：2026-11-04T21:58+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前 V2.2 榜单未列 Claude Opus 5；查到的 V2/V2.1 结果不是目标版本，未写入。

最近核验时间：2026-11-04T21:58+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Claude Opus 5 profile",
          "url": "https://artificialanalysis.ai/models/claude-opus-5/"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis 的 Claude Opus 5 模型页当前未提供 Intelligence Index V5 成绩；未从资料核验出可加入的分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench report (includes Claude Opus 5 comparison)",
          "url": "https://zapier.com/benchmarks/claude-opus5_5-report"
        }
      ],
      "notes": [
        "Zapier 2026-09-17 至 2026-09-18 的报告明确列出 Claude Opus 5 Max 26.9%，指标 task_completed_correctly、657 项任务；TOML 另保留发布系统卡中的旧 26.0 行。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography results",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography benchmark repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 榜单列出 Claude Opus 5 (Adaptive/Max) 27.3%；100 项任务，Pass@1，10 次运行/任务，Inspect AI。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official results",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology and announcement",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "新增的是 DeepSWE v1.1 官方排行榜上的 pass@1（max effort）结果；原有 68.8 resolve rate 记录保留，二者指标不同。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Artificial Analysis V2.1 榜单列出 Claude Opus 5 (Max) 1730 Elo ±19，220 项任务，Stirrup harness；原有 1861 是 V2，独立保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Claude Opus 5 system card",
          "url": "https://www.anthropic.com/claude-opus-5-system-card"
        },
        {
          "label": "Anthropic Claude Fable and Mythos 5.1 announcement",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "现有 Claude Opus 5 系统卡给出无工具 56.3%、带工具 64.7%；Anthropic 后续 Fable/Mythos 5.1 公告将 Opus 5 的相同配置列为无工具 56.6%、带工具 63.6%。保留系统卡原记录，不覆盖或新增竞争记录。"
      ],
      "status": "冲突",
      "unresolved": [
        "Anthropic 两份官方资料对 Opus 5 相同 HLE 工具配置给出不同成绩，尚未说明评测轮次或设置差异；需要核实。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 release manifest",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "V2.1 榜单对应 Claude Opus 5 Max，batch tool，44.33% binary task completion，108 项完整任务，500 步上限；既有 70.6 为 OSWorld 2.0，分别保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 methodology",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2?trk=article-ssr-frontend-pulse_little-text-block"
        }
      ],
      "notes": [
        "官方 V2 默认集排行榜列出 Claude Opus 5 / Claude Code / xhigh：99.40% ±0.40%，638/642。源记录保留排行榜的 Pass@1 标签。",
        "模型原有 79.2 resolve rate 来自 Opus 5 发布系统卡，未标为 V2；保留且不映射到 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "排行榜指标标签 Pass@1 与本仓库定义的 task resolution rate 不完全一致；覆盖率暂不计入，需核实二者语义映射。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Terminal-Bench Science 0.1 official announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Vals 列出 Claude Opus 5 27.14%，70 项任务，Mini-SWE-agent，单次运行 pass@1；基础设施错误可重试。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始来源指标为 accuracy，本仓库定义为 task resolution rate；保留源标签，暂不计入精确映射覆盖率。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Terminal-Bench 4.0 official announcement",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Vals 列出 Claude Opus 5 53.53%，版本 4.0，66 项任务，Mini-SWE-agent，avg@3（每次运行 pass@1）。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始来源指标为 accuracy，本仓库定义为 task resolution rate；保留源标签，暂不计入精确映射覆盖率。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:58+08:00",
      "checked_sources": [
        {
          "label": "Vals Index official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前 V2.2 榜单未列 Claude Opus 5；查到的 V2/V2.1 结果不是目标版本，未写入。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 2,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:58+08:00",
  "model_id": "anthropic/claude-opus-5",
  "new_records": 8,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
