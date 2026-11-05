# Muse Spark 1.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-spark-1.1
- 模型名称：Muse Spark 1.1
- 发布日期：2026-07-09
- 最近检查时间：2026-11-05T09:33+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：4
- 收集前已有成绩数量：11
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- 发布日期由 2026-04-08 修正为 2026-07-09：Meta 对 Muse Spark 1.1 的公告及评测报告均标注 2026-07-09；4 月 8 日对应未标版本的 Muse Spark。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 53.3 (metric=pass@1; version=1.1; dataset=113 tasks; effort=xhigh; variant=pass@1 averaged over five attempts; internet disabled; harness=mini-swe-agent internal bash-only fork; 64 GB RAM and storage VM) | [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T09:33+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report), [SWE-bench Pro V2 leaderboard and version details](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T09:33+08:00 |
| terminal-bench-v4 | 待核实 | 80.0 (metric=success rate; version=2.1) | [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T09:33+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report), [Terminal-Bench-Science v0.1 release](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) | 2026-11-05T09:33+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report) | 2026-11-05T09:33+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report) | 2026-11-05T09:33+08:00 |
| chartography | 待核实 | 24.4 (dataset=100 tasks; variant=xHigh reasoning; harness=Inspect AI leaderboard configuration; 10 runs per task; Gemini 3.5 Flash judge) | [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography harness and leaderboard configuration](https://github.com/surge-ai/chartography) | 2026-11-05T09:33+08:00 |
| humanitys-last-exam | 已存在 | 62.1 (metric=accuracy; dataset=full 2,500-question HLE; effort=xhigh; variant=with tools; bash and browser; blocklist huggingface.co, kaggle.com, paperswithcode.com, lmsys.org; harness=Meta Model API; GPT o3-mini judge); 52.2 (metric=accuracy; dataset=full 2,500-question HLE; effort=xhigh; variant=no tools; harness=Meta Model API; GPT o3-mini judge) | [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report), [Humanity's Last Exam](https://lastexam.ai/) | 2026-11-05T09:33+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Muse Spark 1.1 profile](https://artificialanalysis.ai/models/muse-spark-1-1), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T09:33+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1212 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; effort=Xhigh; harness=Artificial Analysis Stirrup; E2B sandbox with shell/code execution and web tools) | [Artificial Analysis Muse Spark 1.1 vs GPT-5.4 comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-1-1-vs-gpt-5-4), [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa) | 2026-11-05T09:33+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals AI Muse Spark 1.1 profile](https://www.vals.ai/models/meta_muse-spark-1.1), [Vals Index 2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T09:33+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 53.3
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: xhigh
- variant: pass@1 averaged over five attempts; internet disabled
- harness: mini-swe-agent internal bash-only fork; 64 GB RAM and storage VM
- source: [https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 模型 TOML 已有 53.3；Meta 报告确认目标为 DeepSWE v1.1、113 项任务、pass@1 五次运行平均、xhigh，使用禁网的 bash-only mini-swe-agent 内部 fork，64 GB RAM+storage VM。已把 metric 从 resolve rate 修正为 pass@1，并补充条件。

最近核验时间：2026-11-05T09:33+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- [SWE-bench Pro V2 leaderboard and version details](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 模型 TOML 已有 61.5 的 SWE-Bench Pro 成绩；Meta 报告说明来源为 Scale leaderboard、731 项任务和 mini-swe-agent。目标 V2 是不同的 642 项任务协议，不能映射。

尚未解决的问题：
- 本地 61.5 对应 731 项旧套件；尚未找到精确 V2 结果。

最近核验时间：2026-11-05T09:33+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 80.0
- metric: success rate
- version: 2.1
- source: [https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 模型 TOML 已有 80.0，但 version=2.1；目标 v4.0 使用不同任务集和配置。没有把旧版分数转填到 v4。

尚未解决的问题：
- 现有 80.0 是 version 2.1；尚未核实 v4.0 成绩。

最近核验时间：2026-11-05T09:33+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- [Terminal-Bench-Science v0.1 release](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)

研究备注：
- Meta 评测报告发表于 Terminal-Bench-Science v0.1 发布前；已查官方发布页，未找到可对应的 Muse Spark 1.1 分数。

尚未解决的问题：
- 当前动态榜单信息不完整，尚不能确认公开成绩是否存在。

最近核验时间：2026-11-05T09:33+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)

研究备注：
- Zapier 当前榜单只显示部分模型，余项折叠；Meta/Artificial Analysis 的 AutomationBench-AA 条目是独立评分实现，不能作为目标官方结果直接映射。

尚未解决的问题：
- 官方榜单折叠的其余模型无法逐项核对；AA 的 AutomationBench-AA 评分口径不同。

最近核验时间：2026-11-05T09:33+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)

研究备注：
- 模型 TOML 已有 OSWorld-Verified 80.8，但它不是 OSWorld 2.1；目标 v2.1 发布页未给出 Muse Spark 1.1 的精确分数。

尚未解决的问题：
- 现有 OSWorld-Verified 结果不是 v2.1；官方 2.1 页面未提供该模型的可读分数行。

最近核验时间：2026-11-05T09:33+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 24.4
- dataset: 100 tasks
- variant: xHigh reasoning
- harness: Inspect AI leaderboard configuration; 10 runs per task; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography harness and leaderboard configuration](https://github.com/surge-ai/chartography)

研究备注：
- Surge 当前榜单直接列 Muse Spark 1.1 (xHigh reasoning) 24.4%。原始分数已保留在模型 TOML；榜单行未标明 reducer，故不填写 metric 且状态待核实。官方仓库说明 leaderboard 使用 Inspect AI、每项任务 10 次运行和 Gemini 3.5 Flash judge。

尚未解决的问题：
- 榜单没有说明 24.4 对应 accuracy/mean、pass_at_10 还是其他 reducer；不能匹配本地 metric 定义。

最近核验时间：2026-11-05T09:33+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 62.1
- metric: accuracy
- dataset: full 2,500-question HLE
- effort: xhigh
- variant: with tools; bash and browser; blocklist huggingface.co, kaggle.com, paperswithcode.com, lmsys.org
- harness: Meta Model API; GPT o3-mini judge
- source: [https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 52.2
- metric: accuracy
- dataset: full 2,500-question HLE
- effort: xhigh
- variant: no tools
- harness: Meta Model API; GPT o3-mini judge
- source: [https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Meta Muse Spark 1.1 evaluation report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report)
- [Humanity's Last Exam](https://lastexam.ai/)

研究备注：
- 模型 TOML 已有 62.1 with tools；Meta 评测报告 Figure 44 还列无工具 52.2。两条均为 full 2,500-question HLE、accuracy、xhigh，judge 为 GPT o3-mini；with-tool 条件用 bash/browser 并配置站点 blocklist。报告日期是发布日，不作为评测日期。

最近核验时间：2026-11-05T09:33+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.1 profile](https://artificialanalysis.ai/models/muse-spark-1-1)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 的精确 Muse Spark 1.1 profile 当前将 Intelligence Index 显示为 N/A；不把旧 V4.x 分数或 HLE-Diamond 映射为 V5。

最近核验时间：2026-11-05T09:33+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1212
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- effort: Xhigh
- harness: Artificial Analysis Stirrup; E2B sandbox with shell/code execution and web tools
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-1-1-vs-gpt-5-4](https://artificialanalysis.ai/models/comparisons/muse-spark-1-1-vs-gpt-5-4)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis Muse Spark 1.1 vs GPT-5.4 comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-1-1-vs-gpt-5-4)
- [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)

研究备注：
- 已加入 Artificial Analysis 对比页直接列出的 1212 Elo；该页标明 GDPval-AA v2.1、Muse Spark 1.1 (Xhigh)。方法页说明 220 任务、Stirrup/E2B 与工具配置。来源未公布评测日期，date 省略。

最近核验时间：2026-11-05T09:33+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals AI Muse Spark 1.1 profile](https://www.vals.ai/models/meta_muse-spark-1.1)
- [Vals Index 2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Muse Spark 1.1 profile 当前显示 63.18%，但 profile 未显式标注 Index v2.2；当前 v2.2 leaderboard 只列 latest/top/frontier 模型且没有该行，暂不映射为确定的 v2.2 成绩。

尚未解决的问题：
- 63.18% profile 分数没有显式版本标签；需确认它属于 Vals Index 2.2。

最近核验时间：2026-11-05T09:33+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.1 profile",
          "url": "https://artificialanalysis.ai/models/muse-spark-1-1"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 的精确 Muse Spark 1.1 profile 当前将 Intelligence Index 显示为 N/A；不把旧 V4.x 分数或 HLE-Diamond 映射为 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        }
      ],
      "notes": [
        "Zapier 当前榜单只显示部分模型，余项折叠；Meta/Artificial Analysis 的 AutomationBench-AA 条目是独立评分实现，不能作为目标官方结果直接映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单折叠的其余模型无法逐项核对；AA 的 AutomationBench-AA 评分口径不同。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography harness and leaderboard configuration",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 当前榜单直接列 Muse Spark 1.1 (xHigh reasoning) 24.4%。原始分数已保留在模型 TOML；榜单行未标明 reducer，故不填写 metric 且状态待核实。官方仓库说明 leaderboard 使用 Inspect AI、每项任务 10 次运行和 Gemini 3.5 Flash judge。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单没有说明 24.4 对应 accuracy/mean、pass_at_10 还是其他 reducer；不能匹配本地 metric 定义。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "模型 TOML 已有 53.3；Meta 报告确认目标为 DeepSWE v1.1、113 项任务、pass@1 五次运行平均、xhigh，使用禁网的 bash-only mini-swe-agent 内部 fork，64 GB RAM+storage VM。已把 metric 从 resolve rate 修正为 pass@1，并补充条件。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark 1.1 vs GPT-5.4 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-1-1-vs-gpt-5-4"
        },
        {
          "label": "GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        }
      ],
      "notes": [
        "已加入 Artificial Analysis 对比页直接列出的 1212 Elo；该页标明 GDPval-AA v2.1、Muse Spark 1.1 (Xhigh)。方法页说明 220 任务、Stirrup/E2B 与工具配置。来源未公布评测日期，date 省略。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        },
        {
          "label": "Humanity's Last Exam",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "模型 TOML 已有 62.1 with tools；Meta 评测报告 Figure 44 还列无工具 52.2。两条均为 full 2,500-question HLE、accuracy、xhigh，judge 为 GPT o3-mini；with-tool 条件用 bash/browser 并配置站点 blocklist。报告日期是发布日，不作为评测日期。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        }
      ],
      "notes": [
        "模型 TOML 已有 OSWorld-Verified 80.8，但它不是 OSWorld 2.1；目标 v2.1 发布页未给出 Muse Spark 1.1 的精确分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "现有 OSWorld-Verified 结果不是 v2.1；官方 2.1 页面未提供该模型的可读分数行。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard and version details",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "模型 TOML 已有 61.5 的 SWE-Bench Pro 成绩；Meta 报告说明来源为 Scale leaderboard、731 项任务和 mini-swe-agent。目标 V2 是不同的 642 项任务协议，不能映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地 61.5 对应 731 项旧套件；尚未找到精确 V2 结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        },
        {
          "label": "Terminal-Bench-Science v0.1 release",
          "url": "https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0"
        }
      ],
      "notes": [
        "Meta 评测报告发表于 Terminal-Bench-Science v0.1 发布前；已查官方发布页，未找到可对应的 Muse Spark 1.1 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前动态榜单信息不完整，尚不能确认公开成绩是否存在。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Spark 1.1 evaluation report",
          "url": "https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report"
        },
        {
          "label": "Terminal-Bench 4.0 release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "模型 TOML 已有 80.0，但 version=2.1；目标 v4.0 使用不同任务集和配置。没有把旧版分数转填到 v4。"
      ],
      "status": "待核实",
      "unresolved": [
        "现有 80.0 是 version 2.1；尚未核实 v4.0 成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T09:33+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Muse Spark 1.1 profile",
          "url": "https://www.vals.ai/models/meta_muse-spark-1.1"
        },
        {
          "label": "Vals Index 2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Muse Spark 1.1 profile 当前显示 63.18%，但 profile 未显式标注 Index v2.2；当前 v2.2 leaderboard 只列 latest/top/frontier 模型且没有该行，暂不映射为确定的 v2.2 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "63.18% profile 分数没有显式版本标签；需确认它属于 Vals Index 2.2。"
      ]
    }
  },
  "existing_records": 11,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T09:33+08:00",
  "model_id": "meta/muse-spark-1.1",
  "model_notes": [
    "发布日期由 2026-04-08 修正为 2026-07-09：Meta 对 Muse Spark 1.1 的公告及评测报告均标注 2026-07-09；4 月 8 日对应未标版本的 Muse Spark。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 4
}

-->
