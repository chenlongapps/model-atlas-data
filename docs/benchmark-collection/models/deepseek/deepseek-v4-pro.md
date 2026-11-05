# DeepSeek V4 Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4-pro
- 模型名称：DeepSeek V4 Pro
- 发布日期：2026-04-24
- 最近检查时间：2026-11-05T07:18+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：26
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 模型文件是 2026-04-24 的 DeepSeek V4 Pro Preview；DeepSeek API 于 2026-08 更新为 GA 版本，同名模型 ID 不代表同一权重快照。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 排行榜](https://deepswe.datacurve.ai/), [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| terminal-bench-v4 | 待核实 | 64.7 (metric=pass@1; version=2.1; variant=high; harness=Claude Code); 67.9 (metric=accuracy; version=2.0; variant=preview checkpoint; max effort) | [Terminal-Bench 4.0 Vals 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science Vals 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench 1.0.6 官方榜单](https://zapier.com/benchmarks), [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/), [OSWorld-V2 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| chartography | 不适用 | — | [Chartography 官方基准说明与榜单](https://surgehq.ai/benchmarks/chartography), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| humanitys-last-exam | 待核实 | 37.7 (metric=pass@1; variant=preview checkpoint; max effort; without tools); 48.2 (metric=pass@1; variant=preview checkpoint; max effort; with tools) | [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro), [Humanity’s Last Exam 原始论文](https://arxiv.org/abs/2501.14249) | 2026-11-05T07:18+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis DeepSeek V4 发布分析](https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro), [Artificial Analysis DeepSeek V4 Pro 0424 模型页](https://artificialanalysis.ai/models/deepseek-v4-pro-0424) | 2026-11-05T07:18+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1554 (metric=Elo; variant=preview checkpoint; max effort); 1166 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations and 9 major industries; effort=Max; harness=Stirrup) | [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348), [Artificial Analysis DeepSeek V4 发布分析](https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash), [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:18+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 排行榜](https://deepswe.datacurve.ai/)
- [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- 榜单显示 deepseek-v4-flash[max] 53%±4% 或 deepseek-v4-pro[max] 63%±6%，v1.1、113 项任务、mini-swe-agent；榜单标注于 2026-09-22 更新，但没有评测日期或 checkpoint 标识。
- DeepSeek API 在 2026-07/08 后分别将同名 Flash/Pro API 更新为重训/GA 版本，榜单未区分 4 月 Preview 与后续版本；未把成绩回填到 4 月模型。

尚未解决的问题：
- 无法确认榜单通用 API ID 对应本地 2026-04 Preview 的准确权重快照。

最近核验时间：2026-11-05T07:18+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Scale 页面定义 SWE-bench Pro V2 为 642 tasks、11 repos，并说明评测协议于 2026-09-22 更新；当前公开列表未能确认此精确 Preview 型号。
- 本地已有 SWE-Bench Pro 55.4 resolved（未注明 V2）和 hard-aa 数据集的 18 pass@1；均不等同于 SWE-Bench Pro V2。

尚未解决的问题：
- 公开动态榜单未能排除隐藏 Full/Hard 子榜中存在记录；模型对应版本和 Pro V2 结果仍需核实。

最近核验时间：2026-11-05T07:18+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 64.7
- metric: pass@1
- version: 2.1
- variant: high
- harness: Claude Code
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 67.9
- metric: accuracy
- version: 2.0
- variant: preview checkpoint; max effort
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 Vals 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Vals 当前版区分 DeepSeek V4 Flash 0731、V4 Pro 0813 与旧版条目；Flash 0731 的 18.69% 不是本地 Flash Preview 成绩。
- Vals 有一条标题为 DeepSeek V4、路径 slug 为 deepseek-v4-pro 的 11.11% 候选（66-task Terminal-Bench 4.0、Mini-SWE-agent）；页面发布日期显示 Apr 23，且标题未写 Pro，无法确认与本地 Apr 24 Pro Preview 是否同一对象，未录入。
- 本地已有 Terminal-Bench 2.0（Flash 56.9%）或 2.0/2.1（Pro 67.9%/64.7%）记录，均不是目标 4.0。

尚未解决的问题：
- DeepSeek V4 Pro 11.11% Vals 候选的模型标题、发布日期与本地 Preview 记录存在身份歧义。

最近核验时间：2026-11-05T07:18+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science Vals 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- 当前 Vals 榜单列出 Flash 0731 和 Pro 0813 各 4.29%，不是本地 4 月 Preview；基准为 upstream v0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1。
- Artificial Analysis 页面只展示部分模型，未能据此确认本地 Preview 无成绩。

尚未解决的问题：
- 未找到标明本地 2026-04 Preview 的 Terminal-Bench-Science 0.1.0 结果。

最近核验时间：2026-11-05T07:18+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench 1.0.6 官方榜单](https://zapier.com/benchmarks)
- [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Zapier 页面标明 AutomationBench 1.0.6，当前直接显示前 10 条并提供 See 119 more；页面显示区无法完整检查全部条目。
- DeepSeek 后续 V4 Flash 0731 的 Automation Bench (Public) 25.1 与本地预览版不符；Pro GA 的 31.8 也不是本地 Preview，均未移用。

尚未解决的问题：
- 公开榜单折叠记录未能完整逐项核对，无法确认此精确版本是否有记录。

最近核验时间：2026-11-05T07:18+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- 动态榜单未能确认此精确 Preview 版本的 OSWorld 2.1 结果；不能因当前页面未见型号而判定未找到。
- 模型可通过工具交互，但尚无可核实的对应 OSWorld 2.1 成绩。

尚未解决的问题：
- 动态榜单没有可稳定引用的该精确版本行。

最近核验时间：2026-11-05T07:18+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Chartography 官方基准说明与榜单](https://surgehq.ai/benchmarks/chartography)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- 本地模型文件及官方模型卡均将 DeepSeek V4 Flash/Pro 标为文本输入/输出；Chartography 评测专业图表视觉理解，故对文本版不适用。
- 0423 文件所指独立快照身份未获官方确认；在现有模型信息下按文本模型标为不适用，不迁移任何其他版本结果。

最近核验时间：2026-11-05T07:18+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 37.7
- metric: pass@1
- variant: preview checkpoint; max effort; without tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 48.2
- metric: pass@1
- variant: preview checkpoint; max effort; with tools
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Humanity’s Last Exam 原始论文](https://arxiv.org/abs/2501.14249)

研究备注：
- 本地文件已有 HLE 原始成绩：Flash 34.8 Pass@1（Max，无工具）和 45.1 Pass@1（Max，with tools）；Pro 37.7 和 48.2，分别为无工具/with tools。报告未给评测日期或明确题目数。
- 本地定义指标为 accuracy，原始资料写 Pass@1；报告标注 Human Last Exam 并引 Phan et al. 2025，但未明确是否为定义指定的原始 2,500 题集合。原始记录保留，暂不改指标或将其计入定义映射。

尚未解决的问题：
- 成绩来源已确认，但原始题集范围及 Pass@1 与本地 accuracy 定义的映射尚待确认。

最近核验时间：2026-11-05T07:18+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis DeepSeek V4 发布分析](https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Artificial Analysis DeepSeek V4 Pro 0424 模型页](https://artificialanalysis.ai/models/deepseek-v4-pro-0424)

研究备注：
- 2026-04-24 发布分析中的旧 Intelligence Index 分数是 Pro 52、Flash 47，未标注 v5；不能按当前 v5.0.1 处理。V5 使用 HLE-Diamond，不能以 HLE 原始分数代替。
- Pro 0424 精确模型页在 Intelligence Index v5.0.1 摘要处显示 N/A/Unknown；未发现该精确版本可录入的 Index 分数。

最近核验时间：2026-11-05T07:18+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1554
- metric: Elo
- variant: preview checkpoint; max effort
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1166
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations and 9 major industries
- effort: Max
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348)
- [Artificial Analysis DeepSeek V4 发布分析](https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash)
- [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- DeepSeek V4 技术报告列出 GDPval-AA Max：Flash 1395 Elo，Pro 1554 Elo；AA 2026-04-24 发布分析对 Flash 列 1388 Elo，未说明 v2.1。
- AA 当前 v2.1 榜单有精确 DeepSeek V4 Pro 0424 (Max) 1166 Elo，95% CI −17/+17；另有 Pro 0424 (High) 1160。已在模型 TOML 新增 Max 的版本化 v2.1 行，并保留旧报告的无版本 1554 行。
- AA 当前 v2.1 榜单中的 Pro 0424 Max 1166 与技术报告中无版本的 Max 1554 不一致；两者版本/测试口径尚无法解释，均保留并标记冲突。
- deepseek-pro-card

尚未解决的问题：
- Max 旧报告成绩与 AA v2.1 版本化结果不一致，暂不择值；旧无版本成绩保留。

最近核验时间：2026-11-05T07:18+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Vals Index v2.2 当前页面只展示 latest/top/frontier 子集，列出的 DeepSeek 项是 V4 Pro 0813 等后续版本；未出现本地 0424 或 0423 记录。
- 榜单为部分展示，不能据缺席断言未找到成绩。

尚未解决的问题：
- 页面未能确认本地精确快照，也未完整列出全部候选模型。

最近核验时间：2026-11-05T07:18+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis DeepSeek V4 发布分析",
          "url": "https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        },
        {
          "label": "Artificial Analysis DeepSeek V4 Pro 0424 模型页",
          "url": "https://artificialanalysis.ai/models/deepseek-v4-pro-0424"
        }
      ],
      "notes": [
        "2026-04-24 发布分析中的旧 Intelligence Index 分数是 Pro 52、Flash 47，未标注 v5；不能按当前 v5.0.1 处理。V5 使用 HLE-Diamond，不能以 HLE 原始分数代替。",
        "Pro 0424 精确模型页在 Intelligence Index v5.0.1 摘要处显示 N/A/Unknown；未发现该精确版本可录入的 Index 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench 1.0.6 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "DeepSeek API 更新记录",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Zapier 页面标明 AutomationBench 1.0.6，当前直接显示前 10 条并提供 See 119 more；页面显示区无法完整检查全部条目。",
        "DeepSeek 后续 V4 Flash 0731 的 Automation Bench (Public) 25.1 与本地预览版不符；Pro GA 的 31.8 也不是本地 Preview，均未移用。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开榜单折叠记录未能完整逐项核对，无法确认此精确版本是否有记录。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "Chartography 官方基准说明与榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "本地模型文件及官方模型卡均将 DeepSeek V4 Flash/Pro 标为文本输入/输出；Chartography 评测专业图表视觉理解，故对文本版不适用。",
        "0423 文件所指独立快照身份未获官方确认；在现有模型信息下按文本模型标为不适用，不迁移任何其他版本结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 排行榜",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSeek API 更新记录",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "榜单显示 deepseek-v4-flash[max] 53%±4% 或 deepseek-v4-pro[max] 63%±6%，v1.1、113 项任务、mini-swe-agent；榜单标注于 2026-09-22 更新，但没有评测日期或 checkpoint 标识。",
        "DeepSeek API 在 2026-07/08 后分别将同名 Flash/Pro API 更新为重训/GA 版本，榜单未区分 4 月 Preview 与后续版本；未把成绩回填到 4 月模型。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法确认榜单通用 API ID 对应本地 2026-04 Preview 的准确权重快照。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 技术报告",
          "url": "https://arxiv.org/html/2606.19348"
        },
        {
          "label": "Artificial Analysis DeepSeek V4 发布分析",
          "url": "https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash"
        },
        {
          "label": "GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "DeepSeek V4 技术报告列出 GDPval-AA Max：Flash 1395 Elo，Pro 1554 Elo；AA 2026-04-24 发布分析对 Flash 列 1388 Elo，未说明 v2.1。",
        "AA 当前 v2.1 榜单有精确 DeepSeek V4 Pro 0424 (Max) 1166 Elo，95% CI −17/+17；另有 Pro 0424 (High) 1160。已在模型 TOML 新增 Max 的版本化 v2.1 行，并保留旧报告的无版本 1554 行。",
        "AA 当前 v2.1 榜单中的 Pro 0424 Max 1166 与技术报告中无版本的 Max 1554 不一致；两者版本/测试口径尚无法解释，均保留并标记冲突。",
        "deepseek-pro-card"
      ],
      "status": "冲突",
      "unresolved": [
        "Max 旧报告成绩与 AA v2.1 版本化结果不一致，暂不择值；旧无版本成绩保留。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 技术报告",
          "url": "https://arxiv.org/html/2606.19348"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        },
        {
          "label": "Humanity’s Last Exam 原始论文",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "本地文件已有 HLE 原始成绩：Flash 34.8 Pass@1（Max，无工具）和 45.1 Pass@1（Max，with tools）；Pro 37.7 和 48.2，分别为无工具/with tools。报告未给评测日期或明确题目数。",
        "本地定义指标为 accuracy，原始资料写 Pass@1；报告标注 Human Last Exam 并引 Phan et al. 2025，但未明确是否为定义指定的原始 2,500 题集合。原始记录保留，暂不改指标或将其计入定义映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "成绩来源已确认，但原始题集范围及 Pass@1 与本地 accuracy 定义的映射尚待确认。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 发布记录",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "动态榜单未能确认此精确 Preview 版本的 OSWorld 2.1 结果；不能因当前页面未见型号而判定未找到。",
        "模型可通过工具交互，但尚无可核实的对应 OSWorld 2.1 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单没有可稳定引用的该精确版本行。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Scale 页面定义 SWE-bench Pro V2 为 642 tasks、11 repos，并说明评测协议于 2026-09-22 更新；当前公开列表未能确认此精确 Preview 型号。",
        "本地已有 SWE-Bench Pro 55.4 resolved（未注明 V2）和 hard-aa 数据集的 18 pass@1；均不等同于 SWE-Bench Pro V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开动态榜单未能排除隐藏 Full/Hard 子榜中存在记录；模型对应版本和 Pro V2 结果仍需核实。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science Vals 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "当前 Vals 榜单列出 Flash 0731 和 Pro 0813 各 4.29%，不是本地 4 月 Preview；基准为 upstream v0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1。",
        "Artificial Analysis 页面只展示部分模型，未能据此确认本地 Preview 无成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到标明本地 2026-04 Preview 的 Terminal-Bench-Science 0.1.0 结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 Vals 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Vals 当前版区分 DeepSeek V4 Flash 0731、V4 Pro 0813 与旧版条目；Flash 0731 的 18.69% 不是本地 Flash Preview 成绩。",
        "Vals 有一条标题为 DeepSeek V4、路径 slug 为 deepseek-v4-pro 的 11.11% 候选（66-task Terminal-Bench 4.0、Mini-SWE-agent）；页面发布日期显示 Apr 23，且标题未写 Pro，无法确认与本地 Apr 24 Pro Preview 是否同一对象，未录入。",
        "本地已有 Terminal-Bench 2.0（Flash 56.9%）或 2.0/2.1（Pro 67.9%/64.7%）记录，均不是目标 4.0。"
      ],
      "status": "待核实",
      "unresolved": [
        "DeepSeek V4 Pro 11.11% Vals 候选的模型标题、发布日期与本地 Preview 记录存在身份歧义。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:18+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Vals Index v2.2 当前页面只展示 latest/top/frontier 子集，列出的 DeepSeek 项是 V4 Pro 0813 等后续版本；未出现本地 0424 或 0423 记录。",
        "榜单为部分展示，不能据缺席断言未找到成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "页面未能确认本地精确快照，也未完整列出全部候选模型。"
      ]
    }
  },
  "existing_records": 26,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:18+08:00",
  "model_id": "deepseek/deepseek-v4-pro",
  "model_notes": [
    "模型文件是 2026-04-24 的 DeepSeek V4 Pro Preview；DeepSeek API 于 2026-08 更新为 GA 版本，同名模型 ID 不代表同一权重快照。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
