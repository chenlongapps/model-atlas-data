# Ling 3.1 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：inclusionai/ling-3.1-flash
- 模型名称：Ling 3.1 Flash
- 发布日期：2026-09-29
- 最近检查时间：2026-11-04T06:01+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [deepswe-v1.1 官方榜单/方法](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=deep_swe), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [HF 官方评测提交元数据](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files), [DeepSWE 当前官方榜单与协议](https://huggingface.co/datasets/datacurve/deep-swe) | 2026-11-04T06:01+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [swe-bench-pro-v2 官方榜单/方法](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=SWE_Bench_Pro), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [HF 官方评测提交元数据](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files) | 2026-11-04T06:01+08:00 |
| terminal-bench-v4 | 已收录 | 46.03 (metric=task resolution rate; version=4.0.0; dataset=harborframework/terminal-bench; harness=LingCode); 33 (metric=task resolution rate; version=4.0.0; dataset=Artificial Analysis Terminal-Bench 4.0 (66 tasks); harness=mini-swe-agent (pass@1 averaged over three repeats)) | [terminal-bench-v4 官方榜单/方法](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=terminalbench_4), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [Terminal-Bench 4 HF 官方榜单与模型行](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=terminalbench_4), [HF 官方评测提交中的 LingCode 配置](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files), [Artificial Analysis Terminal-Bench 4 官方对照页](https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash), [Artificial Analysis Terminal-Bench 4 方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T06:01+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [terminal-bench-science-v0.1 官方榜单/方法](https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash) | 2026-11-04T06:01+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [automationbench-v1.0.6 官方榜单/方法](https://zapier.com/benchmarks), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [HF 模型卡中的官方评测图](https://cdn-uploads.huggingface.co/production/uploads/678143d4ddb1f1ce16daca8e/VNCYlkUqCCY-QN-_dAmy0.png) | 2026-11-04T06:01+08:00 |
| osworld-v2.1 | 不适用 | — | [osworld-v2.1 官方榜单/方法](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash) | 2026-11-04T06:01+08:00 |
| chartography | 不适用 | — | [chartography 官方榜单/方法](https://surgehq.ai/benchmarks/chartography), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash) | 2026-11-04T06:01+08:00 |
| humanitys-last-exam | 待核实 | — | [humanitys-last-exam 官方榜单/方法](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [HLE 原始 2,500 题方法与榜单](https://labs.scale.com/leaderboard/humanitys_last_exam), [HF 评测提交及 task_id 错误](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files) | 2026-11-04T06:01+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [artificial-analysis-intelligence-index-v5 官方榜单/方法](https://artificialanalysis.ai/models/ling-3-1-flash/), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [Artificial Analysis Index V5 定义与方法](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T06:01+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [gdpval-aa-v2.1 官方榜单/方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash), [Artificial Analysis 比较页候选值 A](https://artificialanalysis.ai/models/comparisons/ling-3-1-flash-vs-gpt-6-astra-high), [Artificial Analysis 比较页候选值 B](https://artificialanalysis.ai/models/comparisons/ling-3-1-flash-vs-glm-5-3-low) | 2026-11-04T06:01+08:00 |
| vals-index-v2.2 | 未找到 | — | [vals-index-v2.2 官方榜单/方法](https://www.vals.ai/benchmarks/vals_index), [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash) | 2026-11-04T06:01+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [deepswe-v1.1 官方榜单/方法](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=deep_swe)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [HF 官方评测提交元数据](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files)
- [DeepSWE 当前官方榜单与协议](https://huggingface.co/datasets/datacurve/deep-swe)

研究备注：
- HF 官方模型评测记录报告 59.7，dataset 为 datacurve/deep-swe，task_id 为 deep_swe，且注明 LingCode；但这条元数据未明确 DeepSWE 1.1 版本和 pass@1 指标，当前公开 113-task 榜单也没有可直接复核的 Ling 3.1 Flash 对应行，因此暂不写入 TOML。

尚未解决的问题：
- HF 模型评测元数据缺少版本与 metric；59.7 是否对应本地 DeepSWE 1.1/pass@1 定义尚未被来源显式确认。

最近核验时间：2026-11-04T06:01+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [swe-bench-pro-v2 官方榜单/方法](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=SWE_Bench_Pro)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [HF 官方评测提交元数据](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files)

研究备注：
- HF 官方评测元数据报告 68.74 并注明 LingCode，精确模型也出现在 ScaleAI 的 SWE-bench Pro 页面；但提交没有记录配置字段，无法排除 hard 子集或其它配置，故暂不写入本地 V2 默认 642-task 定义。

尚未解决的问题：
- 来源元数据没有 config/subset；需要确认 68.74 对应本地定义的 V2 2.0.0 默认 642-task 配置，而非 hard 或其它配置。

最近核验时间：2026-11-04T06:01+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 46.03
- metric: task resolution rate
- version: 4.0.0
- dataset: harborframework/terminal-bench
- harness: LingCode
- source: [https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files)
- 本地 Benchmark 定义映射：精确匹配

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 33
- metric: task resolution rate
- version: 4.0.0
- dataset: Artificial Analysis Terminal-Bench 4.0 (66 tasks)
- harness: mini-swe-agent (pass@1 averaged over three repeats)
- source: [https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash](https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [terminal-bench-v4 官方榜单/方法](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=terminalbench_4)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [Terminal-Bench 4 HF 官方榜单与模型行](https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=terminalbench_4)
- [HF 官方评测提交中的 LingCode 配置](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files)
- [Artificial Analysis Terminal-Bench 4 官方对照页](https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash)
- [Artificial Analysis Terminal-Bench 4 方法](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 已收录两个独立配置：官方 HF 评测记录/榜单的 LingCode 结果 46.03；Artificial Analysis 独立评测 33%，采用 mini-swe-agent、pass@1 并对每任务三次重复取平均。二者版本均为 Terminal-Bench 4.0.0，保留为不同 harness 记录。没有把模型卡提交时间当作评测日期。

最近核验时间：2026-11-04T06:01+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [terminal-bench-science-v0.1 官方榜单/方法](https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)

研究备注：
- 已检查 HF 精确型号评测结果和 Artificial Analysis 当前模型对照页；没有找到该 checkpoint 在 Terminal-Bench-Science 0.1.0 的可核实榜单成绩。AA 当前对照页对该型号未展示成绩；不能把另一型号或相邻 benchmark 的分数移用。

最近核验时间：2026-11-04T06:01+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [automationbench-v1.0.6 官方榜单/方法](https://zapier.com/benchmarks)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [HF 模型卡中的官方评测图](https://cdn-uploads.huggingface.co/production/uploads/678143d4ddb1f1ce16daca8e/VNCYlkUqCCY-QN-_dAmy0.png)

研究备注：
- Ling 3.1 Flash 官方模型卡提及 AutomationBench，但正文没有分数、版本或条件，数值位于模型卡评测图中；本次无法从可读取的原始图表确认数值。二手转录的 public-set 52.50% 未写入；Zapier 明确将 public set 与 private leaderboard 分开。

尚未解决的问题：
- 官方模型卡评测图中的 AutomationBench 数值、版本和配置尚待直接复核；public set 结果不能代替官方 private task leaderboard。

最近核验时间：2026-11-04T06:01+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [osworld-v2.1 官方榜单/方法](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)

研究备注：
- OSWorld 2.1 的计算机使用任务需要桌面视觉观察和多步 GUI 操作；本型号是 text-only，官方资料将视觉能力列在另一型号 Ling 3.0 Flash VL。若加外部视觉模型/控制器，成绩属于组合代理而非本模型自身。

最近核验时间：2026-11-04T06:01+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [chartography 官方榜单/方法](https://surgehq.ai/benchmarks/chartography)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)

研究备注：
- Chartography 要求对专业图表图像进行视觉理解并回答；Ling 3.1 Flash 官方型号输入为文本，不含图像输入，不能按该基准协议独立完成。

最近核验时间：2026-11-04T06:01+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [humanitys-last-exam 官方榜单/方法](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [HLE 原始 2,500 题方法与榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [HF 评测提交及 task_id 错误](https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files)

研究备注：
- HF 官方模型卡评测列表列出 37.44（dataset=cais/hle），但其 HF 评测提交被标记为无效：task_id=hle 不匹配该数据集任务，且未说明 score 的 metric、文本/多模态子集或测试条件。AA 当前页面的 HLE-Diamond 属不同 benchmark；未确认本模型对应原始 2,500 题定义的成绩，因此未写入 TOML。

尚未解决的问题：
- 需要从模型作者或一手评测记录确认 HLE 37.44 的有效 task、metric、数据子集及测试条件；不得将 HLE-Diamond 或旧 AA 指数结果当作原始 HLE。

最近核验时间：2026-11-04T06:01+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [artificial-analysis-intelligence-index-v5 官方榜单/方法](https://artificialanalysis.ai/models/ling-3-1-flash/)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [Artificial Analysis Index V5 定义与方法](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis 当前精确型号页面将 Intelligence Index 标为 N/A/Unknown；当前 V5 对照页也没有该型号的 V5 分数。搜索到的 41 分属于旧版 v4.3.2，后续 Ling-3.1-flash-1019 的 V5 记录又是不同 checkpoint，均未移用。

最近核验时间：2026-11-04T06:01+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [gdpval-aa-v2.1 官方榜单/方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- [Artificial Analysis 比较页候选值 A](https://artificialanalysis.ai/models/comparisons/ling-3-1-flash-vs-gpt-6-astra-high)
- [Artificial Analysis 比较页候选值 B](https://artificialanalysis.ai/models/comparisons/ling-3-1-flash-vs-glm-5-3-low)

研究备注：
- 研究过程中 Artificial Analysis 的不同对照页面/快照出现 1,617 与 1,618 两个 Elo 候选值；当前公开 GDPval-AA v2.1 榜单和对照页未能复现 Ling 3.1 Flash 的对应行。未选择较高值，也未写入 TOML。该评测与 InclusionAI 自报 Elo 1,673 的配置不同，后者未移用。

尚未解决的问题：
- 需确认 AA 的 1,617/1,618 是否不同运行、缓存版本或配置，并取得当前公开的一手榜单行后再写入。

最近核验时间：2026-11-04T06:01+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [vals-index-v2.2 官方榜单/方法](https://www.vals.ai/benchmarks/vals_index)
- [inclusionAI/Ling-3.1-flash 官方模型卡](https://huggingface.co/inclusionAI/Ling-3.1-flash)

研究备注：
- 已检查 Vals Index v2.2 官方榜单；没有找到该准确 checkpoint 的公开成绩。未将 Vals 其它终端/单项基准或模型系列成绩映射为 Vals Index。

最近核验时间：2026-11-04T06:01+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "artificial-analysis-intelligence-index-v5 官方榜单/方法",
          "url": "https://artificialanalysis.ai/models/ling-3-1-flash/"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "Artificial Analysis Index V5 定义与方法",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis 当前精确型号页面将 Intelligence Index 标为 N/A/Unknown；当前 V5 对照页也没有该型号的 V5 分数。搜索到的 41 分属于旧版 v4.3.2，后续 Ling-3.1-flash-1019 的 V5 记录又是不同 checkpoint，均未移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "automationbench-v1.0.6 官方榜单/方法",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "HF 模型卡中的官方评测图",
          "url": "https://cdn-uploads.huggingface.co/production/uploads/678143d4ddb1f1ce16daca8e/VNCYlkUqCCY-QN-_dAmy0.png"
        }
      ],
      "notes": [
        "Ling 3.1 Flash 官方模型卡提及 AutomationBench，但正文没有分数、版本或条件，数值位于模型卡评测图中；本次无法从可读取的原始图表确认数值。二手转录的 public-set 52.50% 未写入；Zapier 明确将 public set 与 private leaderboard 分开。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方模型卡评测图中的 AutomationBench 数值、版本和配置尚待直接复核；public set 结果不能代替官方 private task leaderboard。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "chartography 官方榜单/方法",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        }
      ],
      "notes": [
        "Chartography 要求对专业图表图像进行视觉理解并回答；Ling 3.1 Flash 官方型号输入为文本，不含图像输入，不能按该基准协议独立完成。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "deepswe-v1.1 官方榜单/方法",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=deep_swe"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "HF 官方评测提交元数据",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files"
        },
        {
          "label": "DeepSWE 当前官方榜单与协议",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe"
        }
      ],
      "notes": [
        "HF 官方模型评测记录报告 59.7，dataset 为 datacurve/deep-swe，task_id 为 deep_swe，且注明 LingCode；但这条元数据未明确 DeepSWE 1.1 版本和 pass@1 指标，当前公开 113-task 榜单也没有可直接复核的 Ling 3.1 Flash 对应行，因此暂不写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "HF 模型评测元数据缺少版本与 metric；59.7 是否对应本地 DeepSWE 1.1/pass@1 定义尚未被来源显式确认。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "gdpval-aa-v2.1 官方榜单/方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "Artificial Analysis 比较页候选值 A",
          "url": "https://artificialanalysis.ai/models/comparisons/ling-3-1-flash-vs-gpt-6-astra-high"
        },
        {
          "label": "Artificial Analysis 比较页候选值 B",
          "url": "https://artificialanalysis.ai/models/comparisons/ling-3-1-flash-vs-glm-5-3-low"
        }
      ],
      "notes": [
        "研究过程中 Artificial Analysis 的不同对照页面/快照出现 1,617 与 1,618 两个 Elo 候选值；当前公开 GDPval-AA v2.1 榜单和对照页未能复现 Ling 3.1 Flash 的对应行。未选择较高值，也未写入 TOML。该评测与 InclusionAI 自报 Elo 1,673 的配置不同，后者未移用。"
      ],
      "status": "冲突",
      "unresolved": [
        "需确认 AA 的 1,617/1,618 是否不同运行、缓存版本或配置，并取得当前公开的一手榜单行后再写入。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "humanitys-last-exam 官方榜单/方法",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "HLE 原始 2,500 题方法与榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "HF 评测提交及 task_id 错误",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files"
        }
      ],
      "notes": [
        "HF 官方模型卡评测列表列出 37.44（dataset=cais/hle），但其 HF 评测提交被标记为无效：task_id=hle 不匹配该数据集任务，且未说明 score 的 metric、文本/多模态子集或测试条件。AA 当前页面的 HLE-Diamond 属不同 benchmark；未确认本模型对应原始 2,500 题定义的成绩，因此未写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要从模型作者或一手评测记录确认 HLE 37.44 的有效 task、metric、数据子集及测试条件；不得将 HLE-Diamond 或旧 AA 指数结果当作原始 HLE。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "osworld-v2.1 官方榜单/方法",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        }
      ],
      "notes": [
        "OSWorld 2.1 的计算机使用任务需要桌面视觉观察和多步 GUI 操作；本型号是 text-only，官方资料将视觉能力列在另一型号 Ling 3.0 Flash VL。若加外部视觉模型/控制器，成绩属于组合代理而非本模型自身。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "swe-bench-pro-v2 官方榜单/方法",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=SWE_Bench_Pro"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "HF 官方评测提交元数据",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files"
        }
      ],
      "notes": [
        "HF 官方评测元数据报告 68.74 并注明 LingCode，精确模型也出现在 ScaleAI 的 SWE-bench Pro 页面；但提交没有记录配置字段，无法排除 hard 子集或其它配置，故暂不写入本地 V2 默认 642-task 定义。"
      ],
      "status": "待核实",
      "unresolved": [
        "来源元数据没有 config/subset；需要确认 68.74 对应本地定义的 V2 2.0.0 默认 642-task 配置，而非 hard 或其它配置。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "terminal-bench-science-v0.1 官方榜单/方法",
          "url": "https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        }
      ],
      "notes": [
        "已检查 HF 精确型号评测结果和 Artificial Analysis 当前模型对照页；没有找到该 checkpoint 在 Terminal-Bench-Science 0.1.0 的可核实榜单成绩。AA 当前对照页对该型号未展示成绩；不能把另一型号或相邻 benchmark 的分数移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "terminal-bench-v4 官方榜单/方法",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=terminalbench_4"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        },
        {
          "label": "Terminal-Bench 4 HF 官方榜单与模型行",
          "url": "https://huggingface.co/datasets/harborframework/terminal-bench?eval_result=inclusionAI/Ling-3.1-flash&leaderboard_task_id=terminalbench_4"
        },
        {
          "label": "HF 官方评测提交中的 LingCode 配置",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash/discussions/6/files"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4 官方对照页",
          "url": "https://artificialanalysis.ai/models/comparisons/reflection-beam-vs-ling-3-1-flash"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4 方法",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "已收录两个独立配置：官方 HF 评测记录/榜单的 LingCode 结果 46.03；Artificial Analysis 独立评测 33%，采用 mini-swe-agent、pass@1 并对每任务三次重复取平均。二者版本均为 Terminal-Bench 4.0.0，保留为不同 harness 记录。没有把模型卡提交时间当作评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T06:01+08:00",
      "checked_sources": [
        {
          "label": "vals-index-v2.2 官方榜单/方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "inclusionAI/Ling-3.1-flash 官方模型卡",
          "url": "https://huggingface.co/inclusionAI/Ling-3.1-flash"
        }
      ],
      "notes": [
        "已检查 Vals Index v2.2 官方榜单；没有找到该准确 checkpoint 的公开成绩。未将 Vals 其它终端/单项基准或模型系列成绩映射为 Vals Index。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T06:01+08:00",
  "model_id": "inclusionai/ling-3.1-flash",
  "new_records": 2,
  "overall_status": "待复核"
}

-->
