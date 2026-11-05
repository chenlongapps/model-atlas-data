# Claude Fable 5 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-fable-5
- 模型名称：Claude Fable 5
- 发布日期：2026-06-09
- 最近检查时间：2026-11-05T03:33+08:00
- 整体处理状态：待复核
- 新增成绩数量：10
- 更新成绩数量：0
- 收集前已有成绩数量：9
- 当前已收录的对应成绩数量：7

## 模型身份与范围说明

- 当前文件对应 Claude Fable 5；没有将 Claude Fable 5.1 或 Claude Mythos 5 的成绩转用。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 70% ± 3% (metric=pass rate; version=1.1; dataset=113 tasks; effort=xhigh; variant=2,260 trials started; 73 did not complete; harness=Pier / mini-swe-agent on Modal) | [DeepSWE v1.1 官方结果](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DeepSWE 官方 README](https://github.com/datacurve-ai/deep-swe) | 2026-11-05T03:33+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Anthropic Claude Fable 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5) | 2026-11-05T03:33+08:00 |
| terminal-bench-v4 | 待核实 | 88.0 (metric=success rate; version=2.1); 44.5% ± 3.8% (metric=resolution rate; version=4.0; dataset=66 tasks; effort=max; harness=Claude Code); 42.0 (metric=accuracy; version=4.0) | [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0), [Anthropic Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-05T03:33+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 21.4 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=3 independent trials per task; harness=Claude Code); 24.7 (metric=accuracy; version=0.1) | [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1), [Anthropic Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Terminal-Bench-Science 官方版本记录](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-05T03:33+08:00 |
| automationbench-v1.0.6 | 待核实 | 17.4 (metric=success rate); 17.1 | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md), [Anthropic 2026-06 Fable 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5), [Anthropic 2026-09 Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-05T03:33+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [Anthropic Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1) | 2026-11-05T03:33+08:00 |
| chartography | 已收录 | 34.8 (metric=accuracy (mean; Pass@1); version=unspecified; dataset=full 100-task released set; effort=Adaptive/Max; variant=10 runs per task; Gemini 3.5 Flash judge; harness=Inspect AI) | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Surge Chartography 官方评测仓库](https://github.com/surge-ai/chartography) | 2026-11-05T03:33+08:00 |
| humanitys-last-exam | 冲突 | 59 (metric=accuracy; variant=no tools); 64.5 (metric=accuracy; variant=with tools); 57.8 (metric=accuracy; variant=no tools); 63.8 (metric=accuracy; variant=with tools) | [Anthropic 2026-06 Fable 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5), [Anthropic 2026-09 Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Scale Humanity’s Last Exam 榜单](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-05T03:33+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Claude Fable 5 页面](https://artificialanalysis.ai/models/claude-fable-5), [Artificial Analysis Intelligence Index 页面](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T03:33+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1932 (metric=Elo); 1618 (CI -16/+16) (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Max; variant=Opus 4.8 Fallback) | [Artificial Analysis GDPval-AA v2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T03:33+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2.1 官方榜单](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-05T03:33+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 70% ± 3%
- metric: pass rate
- version: 1.1
- dataset: 113 tasks
- effort: xhigh
- variant: 2,260 trials started; 73 did not complete
- harness: Pier / mini-swe-agent on Modal
- source: [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSWE v1.1 官方结果](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DeepSWE 官方 README](https://github.com/datacurve-ai/deep-swe)

研究备注：
- 官方榜单列 Claude Fable 5[xhigh] 为 70% ± 3%，共 113 项；2,260 次试验中有 73 次未完成，页面称完成试验的 aggregate pass rate。原始 metric 已按 pass rate 写入，未转换为本地定义的 pass@1。

尚未解决的问题：
- 来源明确写 aggregate pass rate，但本地定义要求 pass@1；统计口径映射尚未核实。

最近核验时间：2026-11-05T03:33+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Anthropic Claude Fable 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)

研究备注：
- Scale V2 Full 榜没有 Claude Fable 5 的精确行；榜上 Fable 5.1 是不同版本。本地 80.3 的未标版本 SWE-Bench Pro 来自 2026-06-09，早于 V2 于 2026-09-22 发布，不能映射为 V2。

最近核验时间：2026-11-05T03:33+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 88.0
- metric: success rate
- version: 2.1
- source: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- date: 2026-06-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 44.5% ± 3.8%
- metric: resolution rate
- version: 4.0
- dataset: 66 tasks
- effort: max
- harness: Claude Code
- source: [https://www.tbench.ai/?version=4.0&efforts=all](https://www.tbench.ai/?version=4.0&efforts=all)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 42.0
- metric: accuracy
- version: 4.0
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 官方说明](https://www.tbench.ai/news/terminal-bench-4-0)
- [Anthropic Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- Terminal-Bench 官方榜报 44.5% ± 3.8%（resolution rate，Fable 5[max]，Claude Code）；Anthropic 自有结果另报 42.0% accuracy，但未给该行 effort 或 harness。两条结果已分别保留。来源评测版本写作 4.0，本地定义为 4.0.0；未填写评测日期。

尚未解决的问题：
- 不同来源的指标、测试配置和版本标记不完全相同，尚不能精确映射或比较。

最近核验时间：2026-11-05T03:33+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 21.4
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: 3 independent trials per task
- harness: Claude Code
- source: [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 24.7
- metric: accuracy
- version: 0.1
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方结果](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Anthropic Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Terminal-Bench-Science 官方版本记录](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- 官方榜报告 21.4% resolution rate：70 项、每项 3 次独立试验、Claude Code。Anthropic 自有图表另报 Fable 5 为 24.7% accuracy，并称与公开榜结果在噪声范围内，但未给自有运行的完整条件；两条结果已分开保留。

尚未解决的问题：
- Anthropic 自有运行缺少 harness、effort 和试验次数；其 accuracy 口径与本地 task resolution rate 定义尚未精确对应。

最近核验时间：2026-11-05T03:33+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 17.4
- metric: success rate
- source: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- date: 2026-06-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 17.1
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)
- [Anthropic 2026-06 Fable 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Anthropic 2026-09 Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- Zapier 榜单标为 1.0.6，但可读取内容只显示前 10 项、其余 119 项折叠。模型文件保留原有 17.4%（2026-06-09 文章未标 benchmark 版本）；Anthropic 2026 年 9 月页面又给出 Fable 5 17.1%，但同样没有写版本或 metric，已另记原始行，不能归到 1.0.6。

尚未解决的问题：
- 无法读取 Zapier 完整榜单；17.4% 与 17.1% 均缺少 AutomationBench 1.0.6 的明确版本标记，17.1% 亦未说明 metric。

最近核验时间：2026-11-05T03:33+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld 2.1 官方公开评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [Anthropic Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1)

研究备注：
- 未找到 Claude Fable 5 的 OSWorld 2.1 成绩。本地 OSWorld-Verified 85% 不是 v2.1；Anthropic 后续页面给的是 OSWorld 2.0 partial/strict 结果，也不是 v2.1。模型具备图像输入，目标适用。

最近核验时间：2026-11-05T03:33+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 34.8
- metric: accuracy (mean; Pass@1)
- version: unspecified
- dataset: full 100-task released set
- effort: Adaptive/Max
- variant: 10 runs per task; Gemini 3.5 Flash judge
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography 官方评测仓库](https://github.com/surge-ai/chartography)

研究备注：
- Surge 官方榜列 Claude Fable 5 (Adaptive/Max)，得分 34.8%。官方 README 说明排行榜使用完整 100 项、每项 10 次运行和 Gemini 3.5 Flash judge；metric 为 accuracy/mean（Pass@1），harness 为 Inspect AI。来源没有提供评测日期或语义版本。

最近核验时间：2026-11-05T03:33+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 59
- metric: accuracy
- variant: no tools
- source: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- date: 2026-06-09
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 64.5
- metric: accuracy
- variant: with tools
- source: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- date: 2026-06-09
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: Humanity's Last Exam
- score: 57.8
- metric: accuracy
- variant: no tools
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 4

- name: Humanity's Last Exam
- score: 63.8
- metric: accuracy
- variant: with tools
- source: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Anthropic 2026-06 Fable 5 发布页](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Anthropic 2026-09 Fable 5.1/5 评测页](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Scale Humanity’s Last Exam 榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- 原有官方行是 59% no tools、64.5% with tools；Anthropic 2026-09 页面同名 Fable 5 又列 57.8% no tools、63.8% with tools。新旧来源均已保留，未覆盖历史记录；新页面没有充分说明 effort、harness 或具体数据集/评测配置，因此不能确认分数差异是否来自更新或配置变化。

尚未解决的问题：
- 同一已知工具条件有不同官方分数；缺少 effort、harness 和评测批次说明，需人工复核是否为结果更新或不同配置。

最近核验时间：2026-11-05T03:33+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Claude Fable 5 页面](https://artificialanalysis.ai/models/claude-fable-5)
- [Artificial Analysis Intelligence Index 页面](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis 的 Fable 5 页面当前显示 Index N/A / No publicly available API；该页展示 v5.0.1，且其组成项 HLE-Diamond 不等于原始 Humanity’s Last Exam。未找到 V5 综合分数。

最近核验时间：2026-11-05T03:33+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1932
- metric: Elo
- source: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- date: 2026-06-09
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1618 (CI -16/+16)
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Max
- variant: Opus 4.8 Fallback
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 官方榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Artificial Analysis v2.1 榜列 Claude Fable 5 (Max, Opus 4.8 Fallback)：1618 Elo，CI -16/+16。该 benchmark 使用 220 项、44 个职业任务，shell 与网页浏览 agentic loop 经盲测成对比较得出 Elo。本地原有 1932 Elo 未标版本，保留不动；新行明确为 v2.1。未把模型发布日期填为评测日期。

最近核验时间：2026-11-05T03:33+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2.1 官方榜单](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- Vals 当前 v2.2 榜单未列 Claude Fable 5；已知 61.39% 是旧 Vals Index v2.1，未转写为 v2.2。

最近核验时间：2026-11-05T03:33+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Claude Fable 5 页面",
          "url": "https://artificialanalysis.ai/models/claude-fable-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index 页面",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis 的 Fable 5 页面当前显示 Index N/A / No publicly available API；该页展示 v5.0.1，且其组成项 HLE-Diamond 不等于原始 Humanity’s Last Exam。未找到 V5 综合分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方变更记录",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        },
        {
          "label": "Anthropic 2026-06 Fable 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        },
        {
          "label": "Anthropic 2026-09 Fable 5.1/5 评测页",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "Zapier 榜单标为 1.0.6，但可读取内容只显示前 10 项、其余 119 项折叠。模型文件保留原有 17.4%（2026-06-09 文章未标 benchmark 版本）；Anthropic 2026 年 9 月页面又给出 Fable 5 17.1%，但同样没有写版本或 metric，已另记原始行，不能归到 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法读取 Zapier 完整榜单；17.4% 与 17.1% 均缺少 AutomationBench 1.0.6 的明确版本标记，17.1% 亦未说明 metric。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography 官方评测仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 官方榜列 Claude Fable 5 (Adaptive/Max)，得分 34.8%。官方 README 说明排行榜使用完整 100 项、每项 10 次运行和 Gemini 3.5 Flash judge；metric 为 accuracy/mean（Pass@1），harness 为 Inspect AI。来源没有提供评测日期或语义版本。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方结果",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DeepSWE 官方 README",
          "url": "https://github.com/datacurve-ai/deep-swe"
        }
      ],
      "notes": [
        "官方榜单列 Claude Fable 5[xhigh] 为 70% ± 3%，共 113 项；2,260 次试验中有 73 次未完成，页面称完成试验的 aggregate pass rate。原始 metric 已按 pass rate 写入，未转换为本地定义的 pass@1。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源明确写 aggregate pass rate，但本地定义要求 pass@1；统计口径映射尚未核实。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Artificial Analysis v2.1 榜列 Claude Fable 5 (Max, Opus 4.8 Fallback)：1618 Elo，CI -16/+16。该 benchmark 使用 220 项、44 个职业任务，shell 与网页浏览 agentic loop 经盲测成对比较得出 Elo。本地原有 1932 Elo 未标版本，保留不动；新行明确为 v2.1。未把模型发布日期填为评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Anthropic 2026-06 Fable 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        },
        {
          "label": "Anthropic 2026-09 Fable 5.1/5 评测页",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Scale Humanity’s Last Exam 榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "原有官方行是 59% no tools、64.5% with tools；Anthropic 2026-09 页面同名 Fable 5 又列 57.8% no tools、63.8% with tools。新旧来源均已保留，未覆盖历史记录；新页面没有充分说明 effort、harness 或具体数据集/评测配置，因此不能确认分数差异是否来自更新或配置变化。"
      ],
      "status": "冲突",
      "unresolved": [
        "同一已知工具条件有不同官方分数；缺少 effort、harness 和评测批次说明，需人工复核是否为结果更新或不同配置。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 2.1 官方公开评测指南",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "Anthropic Fable 5.1/5 评测页",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "未找到 Claude Fable 5 的 OSWorld 2.1 成绩。本地 OSWorld-Verified 85% 不是 v2.1；Anthropic 后续页面给的是 OSWorld 2.0 partial/strict 结果，也不是 v2.1。模型具备图像输入，目标适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Anthropic Claude Fable 5 发布页",
          "url": "https://www.anthropic.com/news/claude-fable-5-mythos-5"
        }
      ],
      "notes": [
        "Scale V2 Full 榜没有 Claude Fable 5 的精确行；榜上 Fable 5.1 是不同版本。本地 80.3 的未标版本 SWE-Bench Pro 来自 2026-06-09，早于 V2 于 2026-09-22 发布，不能映射为 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方结果",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Anthropic Fable 5.1/5 评测页",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Terminal-Bench-Science 官方版本记录",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "官方榜报告 21.4% resolution rate：70 项、每项 3 次独立试验、Claude Code。Anthropic 自有图表另报 Fable 5 为 24.7% accuracy，并称与公开榜结果在噪声范围内，但未给自有运行的完整条件；两条结果已分开保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "Anthropic 自有运行缺少 harness、effort 和试验次数；其 accuracy 口径与本地 task resolution rate 定义尚未精确对应。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方榜单",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Anthropic Fable 5.1/5 评测页",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        }
      ],
      "notes": [
        "Terminal-Bench 官方榜报 44.5% ± 3.8%（resolution rate，Fable 5[max]，Claude Code）；Anthropic 自有结果另报 42.0% accuracy，但未给该行 effort 或 harness。两条结果已分别保留。来源评测版本写作 4.0，本地定义为 4.0.0；未填写评测日期。"
      ],
      "status": "待核实",
      "unresolved": [
        "不同来源的指标、测试配置和版本标记不完全相同，尚不能精确映射或比较。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T03:33+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2.1 官方榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        }
      ],
      "notes": [
        "Vals 当前 v2.2 榜单未列 Claude Fable 5；已知 61.39% 是旧 Vals Index v2.1，未转写为 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 9,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T03:33+08:00",
  "model_id": "anthropic/claude-fable-5",
  "model_notes": [
    "当前文件对应 Claude Fable 5；没有将 Claude Fable 5.1 或 Claude Mythos 5 的成绩转用。"
  ],
  "new_records": 10,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
