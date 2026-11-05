# Gemini 3.6 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.6-flash
- 模型名称：Gemini 3.6 Flash
- 发布日期：2026-07-21
- 最近检查时间：2026-11-04T22:47+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：10
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 49.0 (metric=resolve rate; version=1.1; variant=high reasoning) | [Datacurve DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/), [Google Gemini 3.6 evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/) | 2026-11-04T22:47+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/), [Google Gemini 3.6 evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/) | 2026-11-04T22:47+08:00 |
| terminal-bench-v4 | 未找到 | 78.0 (metric=accuracy; version=2.1; harness=Terminus 2) | [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/) | 2026-11-04T22:47+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 4.29 (metric=accuracy; version=0.1.0; dataset=Terminal-Bench Science v0.1.0 (70 tasks); variant=pass@1; single run; harness=Mini-SWE-agent) | [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T22:47+08:00 |
| automationbench-v1.0.6 | 待核实 | 17.0 (dataset=Private set) | [Google Gemini 3.7 model card (Gemini 3.6 result column)](https://deepmind.google/models/model-cards/gemini-3-7-flash/), [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks) | 2026-11-04T22:47+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld 2.0 paper](https://arxiv.org/abs/2606.29537), [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/) | 2026-11-04T22:47+08:00 |
| chartography | 已收录 | 34.0 (metric=accuracy (mean; Pass@1); dataset=SurgeAI Chartography (100 tasks; 20 trials per task); effort=Medium reasoning; variant=no tools; harness=Inspect AI) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T22:47+08:00 |
| humanitys-last-exam | 已收录 | 38.0 (metric=accuracy; dataset=Artificial Analysis May 2025 text-only subset (2,158 questions); effort=high reasoning; variant=no tools; pass@1; harness=Artificial Analysis) | [Artificial Analysis Gemini 3.6 launch evaluation](https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T22:47+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Gemini 3.6 profile](https://artificialanalysis.ai/models/gemini-3-6-flash), [Artificial Analysis Gemini 3.6 launch evaluation](https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time), [Artificial Analysis Intelligence Index V5 announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) | 2026-11-04T22:47+08:00 |
| gdpval-aa-v2.1 | 待核实 | 1421 (metric=Elo; version=v2) | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Google Gemini 3.6 evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/) | 2026-11-04T22:47+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Gemini 3.6 model page](https://vals-ai.com/models/google_gemini-3.6-flash) | 2026-11-04T22:47+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 49.0
- metric: resolve rate
- version: 1.1
- variant: high reasoning
- source: [https://deepmind.google/models/evals-methodology/gemini-3-6-flash/](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/)
- date: 2026-07-21
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Datacurve DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/)
- [Google Gemini 3.6 evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/)

研究备注：
- 现有 TOML 记录保留 Google 7 月来源的 49.0；当前 Datacurve v1.1 页面（更新 2026-09-22）列 Gemini 3.6 Flash [high] 为 47% ±4%，113 tasks。Google 方法说明两项均使用最高推理档位（该模型为 high）并使用 mini-swe-agent；尚无证据确认这是同一轮结果的官方修正。
- 本地定义 metric 为 pass@1，既有记录 metric 为 resolve rate；不把两者静默合并。

尚未解决的问题：
- 需要确认 49.0 与 47% ±4% 是同一实验的官方修订还是不同轮次；同时核实本地 pass@1 与源记录 resolve rate 的映射。

最近核验时间：2026-11-04T22:47+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/)
- [Google Gemini 3.6 evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/)

研究备注：
- 未找到 Gemini 3.6 Flash 的精确 V2 成绩。Google 7 月模型卡已有 58.7% SWE-Bench Pro (Public)，但该结果早于 Scale V2 的 2026-09-22 协议，不能映射到 V2。

最近核验时间：2026-11-04T22:47+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 78.0
- metric: accuracy
- version: 2.1
- harness: Terminus 2
- source: [https://deepmind.google/models/evals-methodology/gemini-3-6-flash/](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/)
- date: 2026-07-21
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/)

研究备注：
- 未找到该模型在 Terminal-Bench 4.0 的公开成绩；Google 模型卡 78.0% 属于 Terminal-Bench 2.1，保留为既有原始记录。Vals 当前表列出 59 个 latest/frontier 模型，未见此模型。

最近核验时间：2026-11-04T22:47+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 4.29
- metric: accuracy
- version: 0.1.0
- dataset: Terminal-Bench Science v0.1.0 (70 tasks)
- variant: pass@1; single run
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Vals Terminal-Bench Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Vals 官方榜单列 Gemini 3.6 Flash 4.29%，Mini-SWE-agent；使用上游 v0.1.0 的 70 tasks，pass@1、单次运行。源 metric 为 accuracy，与本地定义的 task resolution rate 不同，原样保留并待确认映射。

尚未解决的问题：
- 本地定义 metric 为 task resolution rate，Vals 原始标签为 accuracy；保持源标签并待核实精确映射。

最近核验时间：2026-11-04T22:47+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 17.0
- dataset: Private set
- source: [https://deepmind.google/models/model-cards/gemini-3-7-flash/](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Google Gemini 3.7 model card (Gemini 3.6 result column)](https://deepmind.google/models/model-cards/gemini-3-7-flash/)
- [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks)

研究备注：
- Google 3.7 模型卡的 Gemini 3.6 Flash 列报告 17.0%（Private set），未给 metric、AutomationBench 版本或 harness，因此只按来源原样记录并待复核。Zapier 当前 v1.0.6 页面静态文本仅显示前 10 名，无法直接核对该模型的完整排行榜行；未采用第三方副本所列的三档具体分数。

尚未解决的问题：
- Google 模型卡未列 benchmark version/metric/harness，Zapier 完整榜的目标行仍待直接确认。

最近核验时间：2026-11-04T22:47+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld 2.0 paper](https://arxiv.org/abs/2606.29537)
- [Google Gemini 3.6 model card](https://deepmind.google/models/model-cards/gemini-3-6-flash/)

研究备注：
- 未找到 Gemini 3.6 Flash 的 OSWorld v2.1 成绩。Google 的 83.0% 是 OSWorld-Verified；后续 Google 模型卡明确列 OSWorld-2.0 33.8%，均不是目标 v2.1。

最近核验时间：2026-11-04T22:47+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 34.0
- metric: accuracy (mean; Pass@1)
- dataset: SurgeAI Chartography (100 tasks; 20 trials per task)
- effort: Medium reasoning
- variant: no tools
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Surge 官方实时榜单列 Gemini 3.6 Flash (Medium reasoning) 34.0%。论文给出通用配置：100 tasks、每项 20 次试验、mean Pass@1、无工具，使用 Inspect AI；该实时行本身没有评测日期。

最近核验时间：2026-11-04T22:47+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 38.0
- metric: accuracy
- dataset: Artificial Analysis May 2025 text-only subset (2,158 questions)
- effort: high reasoning
- variant: no tools; pass@1
- harness: Artificial Analysis
- source: [https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time](https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Gemini 3.6 launch evaluation](https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis 2026-07-21 发布文章报告 Gemini 3.6 Flash (high reasoning) HLE 38%，并称较上一模型低 3 个百分点。其 HLE 方法使用 May-2025 修订集中的 2,158 道文本题，无工具、pass@1，由 GPT-5.6 Luna (medium) 判分；这不是 HLE-Diamond。

最近核验时间：2026-11-04T22:47+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Gemini 3.6 profile](https://artificialanalysis.ai/models/gemini-3-6-flash)
- [Artificial Analysis Gemini 3.6 launch evaluation](https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time)
- [Artificial Analysis Intelligence Index V5 announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)

研究备注：
- AA 7 月发布文章的 50 分是版本未标明的旧 Index，不是 V5。当前模型资料页标注模型已弃用且 Index 为 N/A，V5 公告/方法页面没有 Gemini 3.6 Flash 的可核实 V5 分数，因此未写入旧版分数。

最近核验时间：2026-11-04T22:47+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1421
- metric: Elo
- version: v2
- source: [https://deepmind.google/models/evals-methodology/gemini-3-6-flash/](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/)
- date: 2026-07-21
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Google Gemini 3.6 evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-6-flash/)

研究备注：
- Google 方法页的 1421 Elo 明确属于 GDPval-AA v2。AA 方法说明 v2.1 改变 Elo 固定锚点和拟合方式；在已查的 v2.1 官方页面中未找到可直接核验的该模型行，暂不复用 v2。

尚未解决的问题：
- 公开 AA 页面未直接呈现该模型的 v2.1 Elo 行；需要原始提交或可读 leaderboard row。

最近核验时间：2026-11-04T22:47+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Gemini 3.6 model page](https://vals-ai.com/models/google_gemini-3.6-flash)

研究备注：
- 当前官方 Vals Index v2.2 页面只展示每个实验室最佳模型及 latest/top/frontier 条目，未列 Gemini 3.6 Flash。Vals 模型页中的早期 Index 数值属于旧版本；不映射为 v2.2。

尚未解决的问题：
- 当前 v2.2 页面未覆盖该历史模型的行，尚不能确认无结果还是仅未展示。

最近核验时间：2026-11-04T22:47+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 3.6 profile",
          "url": "https://artificialanalysis.ai/models/gemini-3-6-flash"
        },
        {
          "label": "Artificial Analysis Gemini 3.6 launch evaluation",
          "url": "https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 announcement",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        }
      ],
      "notes": [
        "AA 7 月发布文章的 50 分是版本未标明的旧 Index，不是 V5。当前模型资料页标注模型已弃用且 Index 为 N/A，V5 公告/方法页面没有 Gemini 3.6 Flash 的可核实 V5 分数，因此未写入旧版分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.7 model card (Gemini 3.6 result column)",
          "url": "https://deepmind.google/models/model-cards/gemini-3-7-flash/"
        },
        {
          "label": "Zapier AutomationBench v1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Google 3.7 模型卡的 Gemini 3.6 Flash 列报告 17.0%（Private set），未给 metric、AutomationBench 版本或 harness，因此只按来源原样记录并待复核。Zapier 当前 v1.0.6 页面静态文本仅显示前 10 名，无法直接核对该模型的完整排行榜行；未采用第三方副本所列的三档具体分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "Google 模型卡未列 benchmark version/metric/harness，Zapier 完整榜的目标行仍待直接确认。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T22:47+08:00",
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
        "Surge 官方实时榜单列 Gemini 3.6 Flash (Medium reasoning) 34.0%。论文给出通用配置：100 tasks、每项 20 次试验、mean Pass@1、无工具，使用 Inspect AI；该实时行本身没有评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Datacurve DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Google Gemini 3.6 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-6-flash/"
        },
        {
          "label": "Google Gemini 3.6 evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-6-flash/"
        }
      ],
      "notes": [
        "现有 TOML 记录保留 Google 7 月来源的 49.0；当前 Datacurve v1.1 页面（更新 2026-09-22）列 Gemini 3.6 Flash [high] 为 47% ±4%，113 tasks。Google 方法说明两项均使用最高推理档位（该模型为 high）并使用 mini-swe-agent；尚无证据确认这是同一轮结果的官方修正。",
        "本地定义 metric 为 pass@1，既有记录 metric 为 resolve rate；不把两者静默合并。"
      ],
      "status": "冲突",
      "unresolved": [
        "需要确认 49.0 与 47% ±4% 是同一实验的官方修订还是不同轮次；同时核实本地 pass@1 与源记录 resolve rate 的映射。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Google Gemini 3.6 evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-6-flash/"
        }
      ],
      "notes": [
        "Google 方法页的 1421 Elo 明确属于 GDPval-AA v2。AA 方法说明 v2.1 改变 Elo 固定锚点和拟合方式；在已查的 v2.1 官方页面中未找到可直接核验的该模型行，暂不复用 v2。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开 AA 页面未直接呈现该模型的 v2.1 Elo 行；需要原始提交或可读 leaderboard row。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Gemini 3.6 launch evaluation",
          "url": "https://artificialanalysis.ai/articles/gemini-3-6-flash-3-5-flash-lite-halving-time"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis 2026-07-21 发布文章报告 Gemini 3.6 Flash (high reasoning) HLE 38%，并称较上一模型低 3 个百分点。其 HLE 方法使用 May-2025 修订集中的 2,158 道文本题，无工具、pass@1，由 GPT-5.6 Luna (medium) 判分；这不是 HLE-Diamond。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T22:47+08:00",
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
          "label": "Google Gemini 3.6 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-6-flash/"
        }
      ],
      "notes": [
        "未找到 Gemini 3.6 Flash 的 OSWorld v2.1 成绩。Google 的 83.0% 是 OSWorld-Verified；后续 Google 模型卡明确列 OSWorld-2.0 33.8%，均不是目标 v2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Google Gemini 3.6 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-6-flash/"
        },
        {
          "label": "Google Gemini 3.6 evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-6-flash/"
        }
      ],
      "notes": [
        "未找到 Gemini 3.6 Flash 的精确 V2 成绩。Google 7 月模型卡已有 58.7% SWE-Bench Pro (Public)，但该结果早于 Scale V2 的 2026-09-22 协议，不能映射到 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Vals 官方榜单列 Gemini 3.6 Flash 4.29%，Mini-SWE-agent；使用上游 v0.1.0 的 70 tasks，pass@1、单次运行。源 metric 为 accuracy，与本地定义的 task resolution rate 不同，原样保留并待确认映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地定义 metric 为 task resolution rate，Vals 原始标签为 accuracy；保持源标签并待核实精确映射。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Google Gemini 3.6 model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-6-flash/"
        }
      ],
      "notes": [
        "未找到该模型在 Terminal-Bench 4.0 的公开成绩；Google 模型卡 78.0% 属于 Terminal-Bench 2.1，保留为既有原始记录。Vals 当前表列出 59 个 latest/frontier 模型，未见此模型。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T22:47+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Gemini 3.6 model page",
          "url": "https://vals-ai.com/models/google_gemini-3.6-flash"
        }
      ],
      "notes": [
        "当前官方 Vals Index v2.2 页面只展示每个实验室最佳模型及 latest/top/frontier 条目，未列 Gemini 3.6 Flash。Vals 模型页中的早期 Index 数值属于旧版本；不映射为 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前 v2.2 页面未覆盖该历史模型的行，尚不能确认无结果还是仅未展示。"
      ]
    }
  },
  "existing_records": 10,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T22:47+08:00",
  "model_id": "google/gemini-3.6-flash",
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
