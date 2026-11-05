# Step 5 Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：stepfun/step-5-preview
- 模型名称：Step 5 Preview
- 发布日期：2026-09-16
- 最近检查时间：2026-11-04T10:47+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：6

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 67.7 (metric=pass@1; version=1.1; effort=High; variant=temperature=1.0; top_p=0.95; harness=SWE-agent) | [StepFun HF 模型卡及评测说明](https://huggingface.co/stepfun-ai/Step-5-Preview), [DeepSWE v1.1 方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T10:47+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-04T10:47+08:00 |
| terminal-bench-v4 | 待核实 | 33.3 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks); 31.82 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; variant=avg@3; three full runs, each run scored pass@1; reported ±2.62 percentage points; harness=Mini-SWE-agent) | [Harbor Terminal-Bench 4 官方 HF 榜单](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=stepfun-ai/Step-5-Preview&leaderboard_task_id=terminalbench_4), [Vals Terminal-Bench 4 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Vals Step 5 Preview 型号页](https://www.vals.ai/models/stepfun_step-5-preview) | 2026-11-04T10:47+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 2.4 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; effort=High; variant=pass@1 averaged over three repeats; reported to one decimal place; harness=mini-swe-agent); 2.86 (metric=task resolution rate; version=0.1.0; dataset=all 70 tasks; variant=single run; pass@1; reported ±2.01 percentage points; harness=Mini-SWE-agent) | [StepFun HF 模型卡评测结果及说明](https://huggingface.co/stepfun-ai/Step-5-Preview), [HF 评测结果记录（引述 Artificial Analysis）](https://huggingface.co/stepfun-ai/Step-5-Preview/discussions/10), [Artificial Analysis Terminal-Bench-Science 0.1 方法](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T10:47+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench), [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-11-04T10:47+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 官方页面](https://osworld-v2.xlang.ai/), [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2), [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-11-04T10:47+08:00 |
| chartography | 待核实 | — | [Surge Chartography 榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 方法仓库](https://github.com/surge-ai/chartography), [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-11-04T10:47+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis HLE 评测定义](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-11-04T10:47+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Step 5 Preview 型号页](https://artificialanalysis.ai/models/step-5), [Artificial Analysis Intelligence Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-11-04T10:47+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis GDPval-AA v2.1 方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [StepFun HF 模型卡与评测说明](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-11-04T10:47+08:00 |
| vals-index-v2.2 | 已收录 | 54.76 (metric=performance score; version=2.2; variant=reported ±1.16 percentage points) | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Vals Step 5 Preview 型号页](https://www.vals.ai/models/stepfun_step-5-preview) | 2026-11-04T10:47+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 67.7
- metric: pass@1
- version: 1.1
- effort: High
- variant: temperature=1.0; top_p=0.95
- harness: SWE-agent
- source: [https://huggingface.co/stepfun-ai/Step-5-Preview](https://huggingface.co/stepfun-ai/Step-5-Preview)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [StepFun HF 模型卡及评测说明](https://huggingface.co/stepfun-ai/Step-5-Preview)
- [DeepSWE v1.1 方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 官方模型卡的 Evaluation results 行列出 DeepSWE 67.7*；评测说明确认 High reasoning、SWE-agent、temperature=1.0、top_p=0.95。TOML 保留数值 67.7，来源显示的星号含义未在可读取说明中解释。

尚未解决的问题：
- 官方模型卡成绩后的星号没有可读取的释义；不影响来源中 67.7 这一数值的读取。

最近核验时间：2026-11-04T10:47+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查了 Scale 官方 V2 榜单及协议页面，未找到 Step 5 Preview 的准确型号记录。

最近核验时间：2026-11-04T10:47+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 33.3
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- source: [https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=stepfun-ai/Step-5-Preview&leaderboard_task_id=terminalbench_4](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=stepfun-ai/Step-5-Preview&leaderboard_task_id=terminalbench_4)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 31.82
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- variant: avg@3; three full runs, each run scored pass@1; reported ±2.62 percentage points
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Harbor Terminal-Bench 4 官方 HF 榜单](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=stepfun-ai/Step-5-Preview&leaderboard_task_id=terminalbench_4)
- [Vals Terminal-Bench 4 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Vals Step 5 Preview 型号页](https://www.vals.ai/models/stepfun_step-5-preview)

研究备注：
- Harbor 官方排行榜的 Step-5-Preview 行为 33.3，测试集显示 66 项任务；该行没有公布 harness 或其他测试设置。Vals 同一准确型号页列出 31.82% ±2.62，Terminal-Bench 4.0 方法页说明 Mini-SWE-agent、avg@3（3 次完整运行，每次 pass@1）。两条来源记录分别保留。

尚未解决的问题：
- 33.3 行未公布 harness/运行次数，无法判定它与 Vals 31.82 avg@3 结果的差异是否来自测试条件。

最近核验时间：2026-11-04T10:47+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 2.4
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- effort: High
- variant: pass@1 averaged over three repeats; reported to one decimal place
- harness: mini-swe-agent
- source: [https://huggingface.co/stepfun-ai/Step-5-Preview/discussions/10](https://huggingface.co/stepfun-ai/Step-5-Preview/discussions/10)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 2.86
- metric: task resolution rate
- version: 0.1.0
- dataset: all 70 tasks
- variant: single run; pass@1; reported ±2.01 percentage points
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [StepFun HF 模型卡评测结果及说明](https://huggingface.co/stepfun-ai/Step-5-Preview)
- [HF 评测结果记录（引述 Artificial Analysis）](https://huggingface.co/stepfun-ai/Step-5-Preview/discussions/10)
- [Artificial Analysis Terminal-Bench-Science 0.1 方法](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- StepFun HF 评测结果记录列出 2.4，注明来自 Artificial Analysis；模型卡评测说明称表列成绩使用 High reasoning。Artificial Analysis 方法页确认 0.1.0、70 项任务、mini-swe-agent、pass@1 三次重复平均。Vals 另列该模型 2.86% ±2.01，其方法为单次运行；TOML 分别保留两条不同实验记录。

最近核验时间：2026-11-04T10:47+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)
- [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview)

研究备注：
- Zapier 榜单标注版本 1.0.6，但当前可读页面仅展开前 10 名，并说明另有 119 条记录。StepFun 模型卡中的评测表以图片呈现，无法从公开文本确认目标型号的对应结果。

尚未解决的问题：
- 榜单其余折叠记录及模型卡图片中的成绩无法核验，不能据此判定为未找到。

最近核验时间：2026-11-04T10:47+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 官方页面](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)
- [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview)

研究备注：
- 已检查的 OSWorld 官方材料标称 OSWorld 2.0，未找到 Step 5 Preview 对应行；本地目标为 OSWorld v2.1，因此没有迁移其他版本成绩。

尚未解决的问题：
- 未核实到本地目标版本 v2.1 的准确型号成绩。

最近核验时间：2026-11-04T10:47+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography 榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 方法仓库](https://github.com/surge-ai/chartography)
- [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview)

研究备注：
- 已检查 Surge 官方榜单与方法资料，未直接检索到 Step 5 Preview 行。模型卡确认该模型可分析图表；模型卡评测结果表为图片，无法读出是否包含 Chartography 成绩，因此不判为不适用或未找到。

尚未解决的问题：
- StepFun 官方评测图表无法文本核验；没有可确认的 Chartography 分数或条件。

最近核验时间：2026-11-04T10:47+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis HLE 评测定义](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview)

研究备注：
- StepFun 官方表格候选显示原始 HLE 46.5（High），但未能确认是否覆盖完整的 2,500 题集合。HLE w/tools 59.4 是 text-only 子集，不与原始 HLE 合并。

尚未解决的问题：
- 46.5 的数据集覆盖范围和完整测试条件无法核验，因此未写入 TOML。

最近核验时间：2026-11-04T10:47+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Step 5 Preview 型号页](https://artificialanalysis.ai/models/step-5)
- [Artificial Analysis Intelligence Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [StepFun HF 模型卡](https://huggingface.co/stepfun-ai/Step-5-Preview)

研究备注：
- AA 当前型号页显示 29 分，页面明确标注索引版本 v5.0.1；仓库目标定义为 v5.0。StepFun 表中出现的 44 未标版本。未将二者记入 v5.0。

尚未解决的问题：
- 尚无与本地定义 v5.0 精确匹配且版本明确的成绩。

最近核验时间：2026-11-04T10:47+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [StepFun HF 模型卡与评测说明](https://huggingface.co/stepfun-ai/Step-5-Preview)

研究备注：
- 官方模型卡说明 GDPval-AA v2.1 成绩基于 Artificial Analysis 截至 2026-09-20 的结果；该日期是数据截止时间而非已确认的运行日期。模型卡评测表以图片呈现，未能直接核验 Step 5 Preview 的精确 Elo 值和条件。

尚未解决的问题：
- 未将研究中出现的 1566 候选值写入 TOML，因为无法从可读取的官方原始榜单或模型卡文本直接复核准确型号行。

最近核验时间：2026-11-04T10:47+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 54.76
- metric: performance score
- version: 2.2
- variant: reported ±1.16 percentage points
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Vals Step 5 Preview 型号页](https://www.vals.ai/models/stepfun_step-5-preview)

研究备注：
- Vals 官方型号页列出 Step 5 Preview 54.76% ±1.16；Vals Index 方法页标明版本 2.2，并将该表述为 performance score。没有把榜单更新日当作成绩日期；未公布实际评测日期，TOML date 留空。

最近核验时间：2026-11-04T10:47+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Step 5 Preview 型号页",
          "url": "https://artificialanalysis.ai/models/step-5"
        },
        {
          "label": "Artificial Analysis Intelligence Index 定义",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "StepFun HF 模型卡",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        }
      ],
      "notes": [
        "AA 当前型号页显示 29 分，页面明确标注索引版本 v5.0.1；仓库目标定义为 v5.0。StepFun 表中出现的 44 未标版本。未将二者记入 v5.0。"
      ],
      "status": "待核实",
      "unresolved": [
        "尚无与本地定义 v5.0 精确匹配且版本明确的成绩。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "StepFun HF 模型卡",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        }
      ],
      "notes": [
        "Zapier 榜单标注版本 1.0.6，但当前可读页面仅展开前 10 名，并说明另有 119 条记录。StepFun 模型卡中的评测表以图片呈现，无法从公开文本确认目标型号的对应结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "榜单其余折叠记录及模型卡图片中的成绩无法核验，不能据此判定为未找到。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 方法仓库",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "StepFun HF 模型卡",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        }
      ],
      "notes": [
        "已检查 Surge 官方榜单与方法资料，未直接检索到 Step 5 Preview 行。模型卡确认该模型可分析图表；模型卡评测结果表为图片，无法读出是否包含 Chartography 成绩，因此不判为不适用或未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "StepFun 官方评测图表无法文本核验；没有可确认的 Chartography 分数或条件。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "StepFun HF 模型卡及评测说明",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        },
        {
          "label": "DeepSWE v1.1 方法",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "官方模型卡的 Evaluation results 行列出 DeepSWE 67.7*；评测说明确认 High reasoning、SWE-agent、temperature=1.0、top_p=0.95。TOML 保留数值 67.7，来源显示的星号含义未在可读取说明中解释。"
      ],
      "status": "已收录",
      "unresolved": [
        "官方模型卡成绩后的星号没有可读取的释义；不影响来源中 67.7 这一数值的读取。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "StepFun HF 模型卡与评测说明",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        }
      ],
      "notes": [
        "官方模型卡说明 GDPval-AA v2.1 成绩基于 Artificial Analysis 截至 2026-09-20 的结果；该日期是数据截止时间而非已确认的运行日期。模型卡评测表以图片呈现，未能直接核验 Step 5 Preview 的精确 Elo 值和条件。"
      ],
      "status": "待核实",
      "unresolved": [
        "未将研究中出现的 1566 候选值写入 TOML，因为无法从可读取的官方原始榜单或模型卡文本直接复核准确型号行。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE 评测定义",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "StepFun HF 模型卡",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        }
      ],
      "notes": [
        "StepFun 官方表格候选显示原始 HLE 46.5（High），但未能确认是否覆盖完整的 2,500 题集合。HLE w/tools 59.4 是 text-only 子集，不与原始 HLE 合并。"
      ],
      "status": "待核实",
      "unresolved": [
        "46.5 的数据集覆盖范围和完整测试条件无法核验，因此未写入 TOML。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 官方页面",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "StepFun HF 模型卡",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        }
      ],
      "notes": [
        "已检查的 OSWorld 官方材料标称 OSWorld 2.0，未找到 Step 5 Preview 对应行；本地目标为 OSWorld v2.1，因此没有迁移其他版本成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "未核实到本地目标版本 v2.1 的准确型号成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查了 Scale 官方 V2 榜单及协议页面，未找到 Step 5 Preview 的准确型号记录。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "StepFun HF 模型卡评测结果及说明",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview"
        },
        {
          "label": "HF 评测结果记录（引述 Artificial Analysis）",
          "url": "https://huggingface.co/stepfun-ai/Step-5-Preview/discussions/10"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 0.1 方法",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Vals Terminal-Bench-Science 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "StepFun HF 评测结果记录列出 2.4，注明来自 Artificial Analysis；模型卡评测说明称表列成绩使用 High reasoning。Artificial Analysis 方法页确认 0.1.0、70 项任务、mini-swe-agent、pass@1 三次重复平均。Vals 另列该模型 2.86% ±2.01，其方法为单次运行；TOML 分别保留两条不同实验记录。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Harbor Terminal-Bench 4 官方 HF 榜单",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=stepfun-ai/Step-5-Preview&leaderboard_task_id=terminalbench_4"
        },
        {
          "label": "Vals Terminal-Bench 4 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals Step 5 Preview 型号页",
          "url": "https://www.vals.ai/models/stepfun_step-5-preview"
        }
      ],
      "notes": [
        "Harbor 官方排行榜的 Step-5-Preview 行为 33.3，测试集显示 66 项任务；该行没有公布 harness 或其他测试设置。Vals 同一准确型号页列出 31.82% ±2.62，Terminal-Bench 4.0 方法页说明 Mini-SWE-agent、avg@3（3 次完整运行，每次 pass@1）。两条来源记录分别保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "33.3 行未公布 harness/运行次数，无法判定它与 Vals 31.82 avg@3 结果的差异是否来自测试条件。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T10:47+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Step 5 Preview 型号页",
          "url": "https://www.vals.ai/models/stepfun_step-5-preview"
        }
      ],
      "notes": [
        "Vals 官方型号页列出 Step 5 Preview 54.76% ±1.16；Vals Index 方法页标明版本 2.2，并将该表述为 performance score。没有把榜单更新日当作成绩日期；未公布实际评测日期，TOML date 留空。"
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T10:47+08:00",
  "model_id": "stepfun/step-5-preview",
  "new_records": 6,
  "overall_status": "待复核"
}

-->
