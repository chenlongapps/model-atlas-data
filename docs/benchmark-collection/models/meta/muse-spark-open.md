# Muse Spark Open Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-spark-open
- 模型名称：Muse Spark Open
- 发布日期：2026-10-15
- 最近检查时间：2026-11-04T02:30+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 收集前已有成绩数量：20
- 当前已收录的对应成绩数量：8

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已存在 | 60 (metric=pass@1; version=1.1; effort=xhigh; harness=Muse Code) | [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B), [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T02:30+08:00 |
| swe-bench-pro-v2 | 已收录 | 95.02 (metric=task resolution rate; version=2.0.0; dataset=V2 Full/default split, 642 tasks; reported 95.02 ± 1.43; effort=xhigh; harness=mini-swe-agent) | [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:30+08:00 |
| terminal-bench-v4 | 冲突 | 6.57 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0, 66 tasks (Vals AI evaluation); variant=Vals AI run; reported ±0.51; harness=Mini-SWE-agent); 8 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (Artificial Analysis evaluation); effort=xhigh; variant=Artificial Analysis run; displayed rounded to integer percent; harness=mini-swe-agent) | [Vals AI Terminal-Bench 4.0 leaderboard](https://www.vals-ai.com/benchmarks/terminal-bench-4), [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high), [Artificial Analysis Terminal-Bench 4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T02:30+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 2 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; effort=xhigh; variant=pass@1 averaged over 3 repeats; source displays rounded integer percent; harness=mini-swe-agent) | [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high), [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T02:30+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B), [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) | 2026-11-04T02:30+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/), [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology), [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) | 2026-11-04T02:30+08:00 |
| chartography | 未找到 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper](https://arxiv.org/html/2608.10677v1), [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) | 2026-11-04T02:30+08:00 |
| humanitys-last-exam | 待核实 | 61.0 (metric=accuracy; version=unspecified; variant=xhigh effort, with tools) | [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B), [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) | 2026-11-04T02:30+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 25 (metric=index score; version=5.0; effort=xhigh) | [Artificial Analysis Muse Spark Open model page](https://artificialanalysis.ai/models/muse-spark-open), [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high), [Artificial Analysis Index V5 announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5), [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) | 2026-11-04T02:30+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) | 2026-11-04T02:30+08:00 |
| vals-index-v2.2 | 已收录 | 48.57 (metric=performance score; version=2.2) | [Vals AI Muse Spark Open model page](https://www.vals.ai/models/meta_muse-spark-open), [Vals Index leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T02:30+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 已确认成绩 1

- name: DeepSWE
- score: 60
- metric: pass@1
- version: 1.1
- effort: xhigh
- harness: Muse Code
- source: [https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)

已检查的主要资料：
- [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 模型卡列 DeepSWE 1.1 Preferred harness = 60；Meta 方法报告确认该结果来自 Artificial Analysis，使用 Muse Code harness，xhigh 配置。现有 TOML 已据此补齐 pass@1、effort=xhigh 与 harness=Muse Code。
- 模型卡/报告没有给出这次评测的执行日期；原先与发布日期相同的 date 已移除。

最近核验时间：2026-11-04T02:30+08:00

### SWE-bench Pro (swe-bench-pro-v2)

#### 已确认成绩 1

- name: SWE-bench Pro
- score: 95.02
- metric: task resolution rate
- version: 2.0.0
- dataset: V2 Full/default split, 642 tasks; reported 95.02 ± 1.43
- effort: xhigh
- harness: mini-swe-agent
- source: [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Scale V2 Full 行列 Muse Spark Open (mini-swe-agent) xhigh，95.02 ± 1.43；V2 Full/default 是 642-task split。记录报告的中心值 95.02，误差范围保存在 dataset 字段中。
- 榜单页面更新时间不是评测执行日期；没有填 date。

最近核验时间：2026-11-04T02:30+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 6.57
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0, 66 tasks (Vals AI evaluation)
- variant: Vals AI run; reported ±0.51
- harness: Mini-SWE-agent
- source: [https://www.vals-ai.com/benchmarks/terminal-bench-4](https://www.vals-ai.com/benchmarks/terminal-bench-4)

#### 已确认成绩 2

- name: Terminal-Bench
- score: 8
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (Artificial Analysis evaluation)
- effort: xhigh
- variant: Artificial Analysis run; displayed rounded to integer percent
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high)

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 leaderboard](https://www.vals-ai.com/benchmarks/terminal-bench-4)
- [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high)
- [Artificial Analysis Terminal-Bench 4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- Vals AI 列分数 6.57% ± 0.51，Mini-SWE-agent；AA 对比页列 8%，精度只到整数，并标注模型为 Xhigh。两处都指向 Terminal-Bench 4.0/mini-swe-agent，但没有证据证明 provider、effort 和运行设置一致，因此分别保留两条记录，不平均、不择高。
- Vals 模型页提醒不同 benchmark 可能使用不同 provider/参数，不能将其全局默认 xhigh 断定为 TB4 评测设置。
- 页面更新时间不是评测执行日期；没有填 date。

尚未解决的问题：
- 需要由维护者确认两条独立 evaluator 结果是否作为不同配置并列保留；AA 仅公布四舍五入整数值。

最近核验时间：2026-11-04T02:30+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 2
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- effort: xhigh
- variant: pass@1 averaged over 3 repeats; source displays rounded integer percent
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high)

已检查的主要资料：
- [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high)
- [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 对比页列 Muse Spark Open (Xhigh) 为 2%；这是来源发布的整数百分比，不补造小数。AA 方法页给出 v0.1.0、70 tasks、Mini-SWE-agent、pass@1 三次重复平均。
- 该结果页没有给出评测执行日期；没有填 date。

最近核验时间：2026-11-04T02:30+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology)

研究备注：
- Zapier 官方榜显示版本 1.0.6，但可读页面文本只展开 top 10 并提示另外 119 条未展开；当前可见项目没有 Muse Spark Open。
- Meta 方法中的 AutomationBench-AA 是 Intelligence Index 子项，不等同于独立 AutomationBench 1.0.6；不能移作本项成绩。

尚未解决的问题：
- 官方榜仍有 119 条未展开，当前可读内容不足以确认完整榜单是否包含该模型。

最近核验时间：2026-11-04T02:30+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology)
- [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)

研究备注：
- Meta 模型卡的 OSWorld-Verified 80.4 是不同评测配置：方法报告描述 361 tasks、GUI-only、无 shell、最多 200 steps、4 次运行的 mean per-task reward；不等同于 OSWorld v2.1 定义的 binary task completion rate。
- 核对 OSWorld-V2 官方仓库和排行榜未找到 Muse Spark Open 的 v2.1 成绩；保留模型文件中的 OSWorld-Verified 行，不映射到本项。

最近核验时间：2026-11-04T02:30+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper](https://arxiv.org/html/2608.10677v1)
- [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)

研究备注：
- Surge 官方榜列出 Muse Spark 1.2（32.1%）和 1.3（27.6%），未列 Muse Spark Open；不可跨 checkpoint 移用成绩。
- Chartography 需要图像加问题、直接文本作答。Muse Spark Open 支持图像输入、文本输出，因此该项适用；本轮未找到该准确模型版本的公开成绩。

最近核验时间：2026-11-04T02:30+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 已确认成绩 1

- name: Humanity's Last Exam
- score: 61.0
- metric: accuracy
- version: unspecified
- variant: xhigh effort, with tools
- source: [https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)

已检查的主要资料：
- [Meta model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology)

研究备注：
- Meta 卡将 61.0 明确列为原始 HLE (with tools)，并把 HLE-Diamond (no tools) 26.1 单列；保留 61.0，不混入 HLE-Diamond。条件为 xhigh、with tools；Meta 方法提及 bash 与 browser。
- 现有 TOML 的 date 与模型发布日期一致，来源没有说明 benchmark 执行日期，已移除 date。

尚未解决的问题：
- Meta 方法没有明确该 with-tools 评测使用 benchmark 定义中的完整 2,500-question 原始集合，题集范围待核实。

最近核验时间：2026-11-04T02:30+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 25
- metric: index score
- version: 5.0
- effort: xhigh
- source: [https://artificialanalysis.ai/models/muse-spark-open](https://artificialanalysis.ai/models/muse-spark-open)

已检查的主要资料：
- [Artificial Analysis Muse Spark Open model page](https://artificialanalysis.ai/models/muse-spark-open)
- [Artificial Analysis model comparison](https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high)
- [Artificial Analysis Index V5 announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology)

研究备注：
- AA 官方 Muse Spark Open (Xhigh) 页面列 V5.0 Intelligence Index = 25。已新增 version=5.0 的 25 分成绩。
- Meta 报告中既有 39 分属于 AA v4.3；原行保留并补 version=4.3。该报告从 AA 取数日期不是评测执行日，删除与发布日期相同的旧 date。

最近核验时间：2026-11-04T02:30+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology)

研究备注：
- Meta 卡上的 GDPval-AA 1401 是 version 2 / Elo，Meta 方法报告说明其来自旧版 GDPval-AA v2；不是定义要求的 v2.1。原成绩行保留，但不映射为 v2.1。
- 核对 AA GDPval-AA v2.1 页面未见 Muse Spark Open；页面上的其他 Meta 模型不作为该模型的成绩。

最近核验时间：2026-11-04T02:30+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 48.57
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/models/meta_muse-spark-open](https://www.vals.ai/models/meta_muse-spark-open)

已检查的主要资料：
- [Vals AI Muse Spark Open model page](https://www.vals.ai/models/meta_muse-spark-open)
- [Vals Index leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals AI Muse Spark Open 模型专页列 Vals Index 48.57% ± 1.09，收录中心值 48.57。该模型页提示不同 benchmark 可采用不同 provider/参数，因此没有将全局默认值填入本项。
- Vals Index 榜页更新日是页面快照时间，不等于该模型的 benchmark 执行日期；没有填 date。

最近核验时间：2026-11-04T02:30+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Spark Open model page",
          "url": "https://artificialanalysis.ai/models/muse-spark-open"
        },
        {
          "label": "Artificial Analysis model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high"
        },
        {
          "label": "Artificial Analysis Index V5 announcement",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-spark-open-evaluation-methodology"
        }
      ],
      "notes": [
        "AA 官方 Muse Spark Open (Xhigh) 页面列 V5.0 Intelligence Index = 25。已新增 version=5.0 的 25 分成绩。",
        "Meta 报告中既有 39 分属于 AA v4.3；原行保留并补 version=4.3。该报告从 AA 取数日期不是评测执行日，删除与发布日期相同的旧 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Meta model card",
          "url": "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-spark-open-evaluation-methodology"
        }
      ],
      "notes": [
        "Zapier 官方榜显示版本 1.0.6，但可读页面文本只展开 top 10 并提示另外 119 条未展开；当前可见项目没有 Muse Spark Open。",
        "Meta 方法中的 AutomationBench-AA 是 Intelligence Index 子项，不等同于独立 AutomationBench 1.0.6；不能移作本项成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜仍有 119 条未展开，当前可读内容不足以确认完整榜单是否包含该模型。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "Meta model card",
          "url": "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B"
        }
      ],
      "notes": [
        "Surge 官方榜列出 Muse Spark 1.2（32.1%）和 1.3（27.6%），未列 Muse Spark Open；不可跨 checkpoint 移用成绩。",
        "Chartography 需要图像加问题、直接文本作答。Muse Spark Open 支持图像输入、文本输出，因此该项适用；本轮未找到该准确模型版本的公开成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Meta model card",
          "url": "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-spark-open-evaluation-methodology"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "模型卡列 DeepSWE 1.1 Preferred harness = 60；Meta 方法报告确认该结果来自 Artificial Analysis，使用 Muse Code harness，xhigh 配置。现有 TOML 已据此补齐 pass@1、effort=xhigh 与 harness=Muse Code。",
        "模型卡/报告没有给出这次评测的执行日期；原先与发布日期相同的 date 已移除。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-spark-open-evaluation-methodology"
        }
      ],
      "notes": [
        "Meta 卡上的 GDPval-AA 1401 是 version 2 / Elo，Meta 方法报告说明其来自旧版 GDPval-AA v2；不是定义要求的 v2.1。原成绩行保留，但不映射为 v2.1。",
        "核对 AA GDPval-AA v2.1 页面未见 Muse Spark Open；页面上的其他 Meta 模型不作为该模型的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Meta model card",
          "url": "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-spark-open-evaluation-methodology"
        }
      ],
      "notes": [
        "Meta 卡将 61.0 明确列为原始 HLE (with tools)，并把 HLE-Diamond (no tools) 26.1 单列；保留 61.0，不混入 HLE-Diamond。条件为 xhigh、with tools；Meta 方法提及 bash 与 browser。",
        "现有 TOML 的 date 与模型发布日期一致，来源没有说明 benchmark 执行日期，已移除 date。"
      ],
      "status": "待核实",
      "unresolved": [
        "Meta 方法没有明确该 with-tools 评测使用 benchmark 定义中的完整 2,500-question 原始集合，题集范围待核实。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-spark-open-evaluation-methodology"
        },
        {
          "label": "Meta model card",
          "url": "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B"
        }
      ],
      "notes": [
        "Meta 模型卡的 OSWorld-Verified 80.4 是不同评测配置：方法报告描述 361 tasks、GUI-only、无 shell、最多 200 steps、4 次运行的 mean per-task reward；不等同于 OSWorld v2.1 定义的 binary task completion rate。",
        "核对 OSWorld-V2 官方仓库和排行榜未找到 Muse Spark Open 的 v2.1 成绩；保留模型文件中的 OSWorld-Verified 行，不映射到本项。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Scale V2 Full 行列 Muse Spark Open (mini-swe-agent) xhigh，95.02 ± 1.43；V2 Full/default 是 642-task split。记录报告的中心值 95.02，误差范围保存在 dataset 字段中。",
        "榜单页面更新时间不是评测执行日期；没有填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 对比页列 Muse Spark Open (Xhigh) 为 2%；这是来源发布的整数百分比，不补造小数。AA 方法页给出 v0.1.0、70 tasks、Mini-SWE-agent、pass@1 三次重复平均。",
        "该结果页没有给出评测执行日期；没有填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals-ai.com/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-spark-open-vs-gpt-6-1-sol-high"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "Vals AI 列分数 6.57% ± 0.51，Mini-SWE-agent；AA 对比页列 8%，精度只到整数，并标注模型为 Xhigh。两处都指向 Terminal-Bench 4.0/mini-swe-agent，但没有证据证明 provider、effort 和运行设置一致，因此分别保留两条记录，不平均、不择高。",
        "Vals 模型页提醒不同 benchmark 可能使用不同 provider/参数，不能将其全局默认 xhigh 断定为 TB4 评测设置。",
        "页面更新时间不是评测执行日期；没有填 date。"
      ],
      "status": "冲突",
      "unresolved": [
        "需要由维护者确认两条独立 evaluator 结果是否作为不同配置并列保留；AA 仅公布四舍五入整数值。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:30+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Muse Spark Open model page",
          "url": "https://www.vals.ai/models/meta_muse-spark-open"
        },
        {
          "label": "Vals Index leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals AI Muse Spark Open 模型专页列 Vals Index 48.57% ± 1.09，收录中心值 48.57。该模型页提示不同 benchmark 可采用不同 provider/参数，因此没有将全局默认值填入本项。",
        "Vals Index 榜页更新日是页面快照时间，不等于该模型的 benchmark 执行日期；没有填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 20,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:30+08:00",
  "model_id": "meta/muse-spark-open",
  "new_records": 6,
  "overall_status": "待复核"
}

-->
