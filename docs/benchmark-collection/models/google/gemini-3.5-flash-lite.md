# Gemini 3.5 Flash Lite Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.5-flash-lite
- 模型名称：Gemini 3.5 Flash Lite
- 发布日期：2026-07-21
- 最近检查时间：2026-11-04T22:28+08:00
- 整体处理状态：待复核
- 新增成绩数量：5
- 更新成绩数量：0
- 收集前已有成绩数量：9
- 当前已收录的对应成绩数量：4

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:28+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T22:28+08:00 |
| terminal-bench-v4 | 未找到 | 54.0 (metric=accuracy; version=2.1; harness=Terminus 2) | [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/), [Vals Terminal-Bench 4 leaderboard](https://vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T22:28+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals Terminal-Bench Science leaderboard](https://vals.ai/benchmarks/terminal-bench-science), [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:28+08:00 |
| automationbench-v1.0.6 | 已收录 | 0.0 (metric=task_completed_correctly; version=1.0.6; dataset=Held-out private evaluation tasks (600+ tasks); effort=Low; harness=API mode); 3.96 (metric=task_completed_correctly; version=1.0.6; dataset=Held-out private evaluation tasks (600+ tasks); effort=Medium; harness=API mode); 3.35 (metric=task_completed_correctly; version=1.0.6; dataset=Held-out private evaluation tasks (600+ tasks); effort=High; harness=API mode) | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-04T22:28+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 2.0 paper](https://arxiv.org/abs/2606.29537), [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) | 2026-11-04T22:28+08:00 |
| chartography | 已收录 | 10.2 (metric=accuracy (mean; Pass@1); dataset=SurgeAI Chartography (100 tasks; 20 trials per task); effort=Minimal reasoning; variant=no tools; harness=Inspect AI) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T22:28+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Secondary AA HLE snapshot](https://atlas.kevinhu.io/benchmarks/hle-text-only) | 2026-11-04T22:28+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 12 (metric=index score; version=5.0.1) | [Artificial Analysis Gemini 3.5 Flash-Lite profile](https://artificialanalysis.ai/models/gemini-3-5-flash-lite) | 2026-11-04T22:28+08:00 |
| gdpval-aa-v2.1 | 未找到 | 1140 (metric=Elo; version=v2) | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T22:28+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T22:28+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- 未找到 Gemini 3.5 Flash Lite 的精确条目；榜单上的 gemini-3.5-flash[high] 属于 Gemini 3.5 Flash，不是 Flash Lite。

最近核验时间：2026-11-04T22:28+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 模型卡已有 54.2% SWE-Bench Pro (Public)，但未标明 V2；Scale 的 V2 使用 2026-09-22 发布的 V2 协议，因此不把旧记录映射为 V2。

最近核验时间：2026-11-04T22:28+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 54.0
- metric: accuracy
- version: 2.1
- harness: Terminus 2
- source: [https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)
- date: 2026-07-21
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)
- [Vals Terminal-Bench 4 leaderboard](https://vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 模型卡已有 Terminal-Bench 2.1、Terminus 2 的 54.0%；与目标 Terminal-Bench 4 不同。

最近核验时间：2026-11-04T22:28+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Terminal-Bench Science leaderboard](https://vals.ai/benchmarks/terminal-bench-science)
- [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- 已查 Vals 官方榜单和模型卡，未找到该准确模型的 Terminal-Bench Science 0.1 成绩。

最近核验时间：2026-11-04T22:28+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 0.0
- metric: task_completed_correctly
- version: 1.0.6
- dataset: Held-out private evaluation tasks (600+ tasks)
- effort: Low
- harness: API mode
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: AutomationBench
- score: 3.96
- metric: task_completed_correctly
- version: 1.0.6
- dataset: Held-out private evaluation tasks (600+ tasks)
- effort: Medium
- harness: API mode
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 3

- name: AutomationBench
- score: 3.35
- metric: task_completed_correctly
- version: 1.0.6
- dataset: Held-out private evaluation tasks (600+ tasks)
- effort: High
- harness: API mode
- source: [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- Zapier 官方 1.0.6 榜单列出 Low 0.0%、Medium 3.96%、High 3.35%；0.0% 是榜单明确报告的 Low 配置成绩，不是缺失值。榜单说明其使用 600+ held-out private tasks，且成绩在 API mode 下运行。

最近核验时间：2026-11-04T22:28+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 2.0 paper](https://arxiv.org/abs/2606.29537)
- [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)

研究备注：
- 未找到 OSWorld v2.1 的 Gemini 3.5 Flash Lite 成绩；模型卡中的 OSWorld-Verified 74.0% 是不同评测，不映射到该项。

最近核验时间：2026-11-04T22:28+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 10.2
- metric: accuracy (mean; Pass@1)
- dataset: SurgeAI Chartography (100 tasks; 20 trials per task)
- effort: Minimal reasoning
- variant: no tools
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Surge 官方实时榜单列出 Gemini 3.5 Flash-Lite (Minimal reasoning) 10.2%。论文说明 Chartography 为 100 项任务、每项 20 次试验、mean Pass@1，单条评测无工具并使用 Inspect AI；官方资料未给语义版本或此条结果日期。

最近核验时间：2026-11-04T22:28+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis HLE evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Secondary AA HLE snapshot](https://atlas.kevinhu.io/benchmarks/hle-text-only)

研究备注：
- 二手快照报告 18.8% 左右，但 Artificial Analysis 官方排行榜的动态模型行无法从可读页面文本中直接核验；未把二手分数写入 TOML。该 AA 评测注明为 May 2025 文本子集，与 HLE-Diamond 不同。

尚未解决的问题：
- 官方动态排行榜未能直接核对 Gemini 3.5 Flash Lite 的分数行；应在原始排行榜可读时核实二手来源提及的约 18.8% 及其配置。

最近核验时间：2026-11-04T22:28+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 12
- metric: index score
- version: 5.0.1
- source: [https://artificialanalysis.ai/models/gemini-3-5-flash-lite](https://artificialanalysis.ai/models/gemini-3-5-flash-lite)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Gemini 3.5 Flash-Lite profile](https://artificialanalysis.ai/models/gemini-3-5-flash-lite)

研究备注：
- 官方模型页报告 Index score 12，当前指数版本为 5.0.1。已把源版本 5.0.1 原样写入 TOML；本仓库对应定义版本为 5.0，严格版本映射尚待确认，覆盖率暂不计入。

尚未解决的问题：
- 本地定义版本为 5.0，原始资料版本为 5.0.1；确认两者能否按当前定义精确映射后，再将该成绩纳入覆盖率。

最近核验时间：2026-11-04T22:28+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1140
- metric: Elo
- version: v2
- source: [https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)
- date: 2026-07-21
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Google model card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 官方模型卡已有 1140 Elo，但明确是 GDPval-AA v2。AA v2.1 使用不同 Elo 标定，未找到 Gemini 3.5 Flash Lite 的 v2.1 行，不复用 v2 成绩。

最近核验时间：2026-11-04T22:28+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 已查官方 2.2 页面；当前页面显示每个实验室最佳模型及 latest/top/frontier 行，未列 Gemini 3.5 Flash Lite。没有从其他 Vals Index 版本挪用分数。

最近核验时间：2026-11-04T22:28+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 3.5 Flash-Lite profile",
          "url": "https://artificialanalysis.ai/models/gemini-3-5-flash-lite"
        }
      ],
      "notes": [
        "官方模型页报告 Index score 12，当前指数版本为 5.0.1。已把源版本 5.0.1 原样写入 TOML；本仓库对应定义版本为 5.0，严格版本映射尚待确认，覆盖率暂不计入。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义版本为 5.0，原始资料版本为 5.0.1；确认两者能否按当前定义精确映射后，再将该成绩纳入覆盖率。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Zapier 官方 1.0.6 榜单列出 Low 0.0%、Medium 3.96%、High 3.35%；0.0% 是榜单明确报告的 Low 配置成绩，不是缺失值。榜单说明其使用 600+ held-out private tasks，且成绩在 API mode 下运行。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "Surge 官方实时榜单列出 Gemini 3.5 Flash-Lite (Minimal reasoning) 10.2%。论文说明 Chartography 为 100 项任务、每项 20 次试验、mean Pass@1，单条评测无工具并使用 Inspect AI；官方资料未给语义版本或此条结果日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Google model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "未找到 Gemini 3.5 Flash Lite 的精确条目；榜单上的 gemini-3.5-flash[high] 属于 Gemini 3.5 Flash，不是 Flash Lite。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Google model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "官方模型卡已有 1140 Elo，但明确是 GDPval-AA v2。AA v2.1 使用不同 Elo 标定，未找到 Gemini 3.5 Flash Lite 的 v2.1 行，不复用 v2 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Secondary AA HLE snapshot",
          "url": "https://atlas.kevinhu.io/benchmarks/hle-text-only"
        }
      ],
      "notes": [
        "二手快照报告 18.8% 左右，但 Artificial Analysis 官方排行榜的动态模型行无法从可读页面文本中直接核验；未把二手分数写入 TOML。该 AA 评测注明为 May 2025 文本子集，与 HLE-Diamond 不同。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态排行榜未能直接核对 Gemini 3.5 Flash Lite 的分数行；应在原始排行榜可读时核实二手来源提及的约 18.8% 及其配置。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld 2.0 paper",
          "url": "https://arxiv.org/abs/2606.29537"
        },
        {
          "label": "Google model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "未找到 OSWorld v2.1 的 Gemini 3.5 Flash Lite 成绩；模型卡中的 OSWorld-Verified 74.0% 是不同评测，不映射到该项。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Google model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "模型卡已有 54.2% SWE-Bench Pro (Public)，但未标明 V2；Scale 的 V2 使用 2026-09-22 发布的 V2 协议，因此不把旧记录映射为 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench Science leaderboard",
          "url": "https://vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Google model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        }
      ],
      "notes": [
        "已查 Vals 官方榜单和模型卡，未找到该准确模型的 Terminal-Bench Science 0.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Google model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/"
        },
        {
          "label": "Vals Terminal-Bench 4 leaderboard",
          "url": "https://vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "模型卡已有 Terminal-Bench 2.1、Terminus 2 的 54.0%；与目标 Terminal-Bench 4 不同。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T22:28+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "已查官方 2.2 页面；当前页面显示每个实验室最佳模型及 latest/top/frontier 行，未列 Gemini 3.5 Flash Lite。没有从其他 Vals Index 版本挪用分数。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 9,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T22:28+08:00",
  "model_id": "google/gemini-3.5-flash-lite",
  "new_records": 5,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
