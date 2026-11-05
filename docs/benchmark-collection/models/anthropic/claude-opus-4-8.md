# Claude Opus 4.8 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-opus-4-8
- 模型名称：Claude Opus 4.8
- 发布日期：2026-05-28
- 最近检查时间：2026-11-05T05:14+08:00
- 整体处理状态：待复核
- 新增成绩数量：5
- 更新成绩数量：2
- 收集前已有成绩数量：7
- 当前已收录的对应成绩数量：6

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 59% ± 2% (metric=pass rate; version=1.1; dataset=113 tasks; effort=max; variant=leaderboard uncertainty display; interval semantics not specified; harness=mini-swe-agent) | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T05:14+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro dataset/version information](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [Anthropic Opus 4.8 release page](https://www.anthropic.com/news/claude-opus-4-8) | 2026-11-05T05:14+08:00 |
| terminal-bench-v4 | 已收录 | 74.6 (metric=success rate; version=2.1; harness=Terminus-2); 23.6% ± 3.6% (metric=task resolution rate; version=4.0.0; dataset=66 tasks; effort=max; variant=95% confidence interval; harness=Claude Code); 22% (rounded display) (metric=task resolution rate; version=4.0.0; dataset=66 tasks; effort=max; variant=pass@1 averaged across three repeats; 500-step limit; rounded integer display; harness=mini-swe-agent) | [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?filters=%7B%22sets%22:%7B%22agent_display%22:%5B%22Claude+Code%22%5D%7D%7D), [Artificial Analysis Opus 4.8 comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:14+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 10.5 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=three independent trials per task; harness=Claude Code) | [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T05:14+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Artificial Analysis Opus 4.8 comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7) | 2026-11-05T05:14+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld official results](https://osworld-v2.xlang.ai/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [Claude Opus 4.8 System Card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) | 2026-11-05T05:14+08:00 |
| chartography | 已收录 | 15.9 (metric=accuracy (mean; Pass@1); dataset=full task set; effort=Adaptive/Max; variant=10 runs per task; Gemini 3.5 Flash judge) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official evaluation repository](https://github.com/surge-ai/chartography) | 2026-11-05T05:14+08:00 |
| humanitys-last-exam | 已存在 | 49.8 (metric=accuracy; variant=no tools); 57.9 (metric=accuracy; variant=with tools) | [Claude Opus 4.8 System Card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) | 2026-11-05T05:14+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Opus 4.8 comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T05:14+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [AA Opus 4.8 comparison vs Opus 4.6](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-6), [AA Opus 4.8 comparison vs o3](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-o3), [AA Opus 4.8 comparison vs GPT-5.1](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-gpt-5-1), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Claude Opus 4.8 System Card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) | 2026-11-05T05:14+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T05:14+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 59% ± 2%
- metric: pass rate
- version: 1.1
- dataset: 113 tasks
- effort: max
- variant: leaderboard uncertainty display; interval semantics not specified
- harness: mini-swe-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 官方 v1.1 榜单给出 Opus 4.8 [max] 59%±2%、113 tasks、mini-swe-agent；页面称 aggregate/pass rates，但未标明 pass@1。已记录原始结果，暂不按本地 pass@1 定义映射。

尚未解决的问题：
- 来源评分术语与本地定义 pass@1 不完全一致，需确认聚合方式。

最近核验时间：2026-11-05T05:14+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro dataset/version information](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [Anthropic Opus 4.8 release page](https://www.anthropic.com/news/claude-opus-4-8)

研究备注：
- 未找到明确标注 SWE-bench Pro V2 的 Opus 4.8 结果；已有 69.2 是未标 V2 的早期 Pro 分数，不迁移。

最近核验时间：2026-11-05T05:14+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 74.6
- metric: success rate
- version: 2.1
- harness: Terminus-2
- source: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)
- date: 2026-05-28
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 23.6% ± 3.6%
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- effort: max
- variant: 95% confidence interval
- harness: Claude Code
- source: [https://www.tbench.ai/?filters=%7B%22sets%22:%7B%22agent_display%22:%5B%22Claude+Code%22%5D%7D%7D](https://www.tbench.ai/?filters=%7B%22sets%22:%7B%22agent_display%22:%5B%22Claude+Code%22%5D%7D%7D)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 22% (rounded display)
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- effort: max
- variant: pass@1 averaged across three repeats; 500-step limit; rounded integer display
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/?filters=%7B%22sets%22:%7B%22agent_display%22:%5B%22Claude+Code%22%5D%7D%7D)
- [Artificial Analysis Opus 4.8 comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 保留两种独立设置：官方 Claude Code 榜 23.6%±3.6%；AA 独立 mini-swe-agent 榜 22% 四舍五入，配置分别记录。

最近核验时间：2026-11-05T05:14+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 10.5
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: three independent trials per task
- harness: Claude Code
- source: [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Terminal-Bench-Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 官方 v0.1 结果为 10.5%，Claude Code；全 70 项任务，每题 3 次独立试验。

最近核验时间：2026-11-05T05:14+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Artificial Analysis Opus 4.8 comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7)

研究备注：
- 模型适用于工具型工作流。Zapier 榜只显示前 10 项，另有 119 项折叠；AA 的 AutomationBench-AA 46% 是另一评测，不能映射为本地 1.0.6。

尚未解决的问题：
- Zapier 完整榜单当前不可见。

最近核验时间：2026-11-05T05:14+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld official results](https://osworld-v2.xlang.ai/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [Claude Opus 4.8 System Card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf)

研究备注：
- System Card 的 OSWorld-Verified 83.4% 不是 v2.1；官方站给出 v2.0 配置结果，但未确认 Opus 4.8 的 v2.1 专属成绩。

尚未解决的问题：
- 现有版本及动态榜单不足以确认 v2.1。

最近核验时间：2026-11-05T05:14+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 15.9
- metric: accuracy (mean; Pass@1)
- dataset: full task set
- effort: Adaptive/Max
- variant: 10 runs per task; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official evaluation repository](https://github.com/surge-ai/chartography)

研究备注：
- 官方榜单列出 Claude Opus 4.8 (Adaptive/Max) 15.9%；方法为 mean Pass@1、完整任务集、每题 10 次运行及 Gemini 3.5 Flash judge；未公布版本或评测日期。

最近核验时间：2026-11-05T05:14+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 49.8
- metric: accuracy
- variant: no tools
- source: [https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 57.9
- metric: accuracy
- variant: with tools
- source: [https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Claude Opus 4.8 System Card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf)

研究备注：
- System Card 确认已有 49.8 accuracy (no tools) 与 57.9 accuracy (with tools)；更新来源并删除 2026-06-09，因为它是 Fable/Mythos 公告日，非已确认评测日。

最近核验时间：2026-11-05T05:14+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Opus 4.8 comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前 AA v5.0.1 页面未给出 Opus 4.8 Index 分数；旧 v4.3.2 的 42 不迁移至 V5。

最近核验时间：2026-11-05T05:14+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [AA Opus 4.8 comparison vs Opus 4.6](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-6)
- [AA Opus 4.8 comparison vs o3](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-o3)
- [AA Opus 4.8 comparison vs GPT-5.1](https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-gpt-5-1)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Claude Opus 4.8 System Card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf)

研究备注：
- AA 不同比较页对 Opus 4.8 显示 1453 与 1454 Elo；当前 leaderboard 没有精确型号行。System Card 的 1890 未标 v2.1，暂不写入单一结果。

尚未解决的问题：
- 两处公开值相差 1 Elo，尚无法判定为显示/更新差异或评测冲突。

最近核验时间：2026-11-05T05:14+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 v2.2 榜单未列 Opus 4.8；旧 v2.1 55.10% 不迁移至 v2.2。

最近核验时间：2026-11-05T05:14+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Opus 4.8 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前 AA v5.0.1 页面未给出 Opus 4.8 Index 分数；旧 v4.3.2 的 42 不迁移至 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis Opus 4.8 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7"
        }
      ],
      "notes": [
        "模型适用于工具型工作流。Zapier 榜只显示前 10 项，另有 119 项折叠；AA 的 AutomationBench-AA 46% 是另一评测，不能映射为本地 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 完整榜单当前不可见。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "官方榜单列出 Claude Opus 4.8 (Adaptive/Max) 15.9%；方法为 mean Pass@1、完整任务集、每题 10 次运行及 Gemini 3.5 Flash judge；未公布版本或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "官方 v1.1 榜单给出 Opus 4.8 [max] 59%±2%、113 tasks、mini-swe-agent；页面称 aggregate/pass rates，但未标明 pass@1。已记录原始结果，暂不按本地 pass@1 定义映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源评分术语与本地定义 pass@1 不完全一致，需确认聚合方式。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "AA Opus 4.8 comparison vs Opus 4.6",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-6"
        },
        {
          "label": "AA Opus 4.8 comparison vs o3",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-o3"
        },
        {
          "label": "AA Opus 4.8 comparison vs GPT-5.1",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-gpt-5-1"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Claude Opus 4.8 System Card",
          "url": "https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf"
        }
      ],
      "notes": [
        "AA 不同比较页对 Opus 4.8 显示 1453 与 1454 Elo；当前 leaderboard 没有精确型号行。System Card 的 1890 未标 v2.1，暂不写入单一结果。"
      ],
      "status": "冲突",
      "unresolved": [
        "两处公开值相差 1 Elo，尚无法判定为显示/更新差异或评测冲突。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Claude Opus 4.8 System Card",
          "url": "https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf"
        }
      ],
      "notes": [
        "System Card 确认已有 49.8 accuracy (no tools) 与 57.9 accuracy (with tools)；更新来源并删除 2026-06-09，因为它是 Fable/Mythos 公告日，非已确认评测日。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "OSWorld official results",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Claude Opus 4.8 System Card",
          "url": "https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf"
        }
      ],
      "notes": [
        "System Card 的 OSWorld-Verified 83.4% 不是 v2.1；官方站给出 v2.0 配置结果，但未确认 Opus 4.8 的 v2.1 专属成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "现有版本及动态榜单不足以确认 v2.1。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro dataset/version information",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "Anthropic Opus 4.8 release page",
          "url": "https://www.anthropic.com/news/claude-opus-4-8"
        }
      ],
      "notes": [
        "未找到明确标注 SWE-bench Pro V2 的 Opus 4.8 结果；已有 69.2 是未标 V2 的早期 Pro 分数，不迁移。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "官方 v0.1 结果为 10.5%，Claude Code；全 70 项任务，每题 3 次独立试验。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/?filters=%7B%22sets%22:%7B%22agent_display%22:%5B%22Claude+Code%22%5D%7D%7D"
        },
        {
          "label": "Artificial Analysis Opus 4.8 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/claude-opus-4-8-vs-claude-opus-4-7"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "保留两种独立设置：官方 Claude Code 榜 23.6%±3.6%；AA 独立 mini-swe-agent 榜 22% 四舍五入，配置分别记录。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T05:14+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 v2.2 榜单未列 Opus 4.8；旧 v2.1 55.10% 不迁移至 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 7,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T05:14+08:00",
  "model_id": "anthropic/claude-opus-4-8",
  "new_records": 5,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
