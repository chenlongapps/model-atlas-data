# MiMo-V2.5-Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2.5-pro
- 模型名称：MiMo-V2.5-Pro
- 发布日期：2026-04-22
- 最近检查时间：2026-11-05T08:19+08:00
- 整体处理状态：待复核
- 新增成绩数量：8
- 更新成绩数量：1
- 收集前已有成绩数量：18
- 当前已收录的对应成绩数量：7

## 模型身份与范围说明

- 本地 release_date 为 2026-04-22；小米 Model Release log 列 2026-04-23，独立产品发布页列 April 27th。两页的发布时间语境不同；本轮没有足够依据统一定义，保留仓库日期并记录差异。参见 https://mimo.mi.com/docs/en-US/updates/model 与 https://mimo.xiaomi.com/mimo-v2-5-pro。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 19 (metric=score; version=1.1; variant=MiMo-V2.5 Pro comparison column) | [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T08:14+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://mimo.xiaomi.com/mimo-v2-5-pro/](https://mimo.xiaomi.com/mimo-v2-5-pro/), [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro), [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256) | 2026-11-05T08:14+08:00 |
| terminal-bench-v4 | 冲突 | 1.5 (metric=score; version=4.0; variant=MiMo-V2.5 Pro comparison column); 65.2 (metric=score; version=2.1; variant=MiMo-V2.5 Pro comparison column); 0.51 (metric=accuracy; version=4.0; dataset=66 tasks; 3 runs per task (avg@3); variant=Vals AI; pass@1; temperature 1; top_p 0.95; top_k default; max output 128,000; harness=Mini-SWE-agent) | [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [https://www.vals.ai/models/xiaomi_mimo-v2.5-pro](https://www.vals.ai/models/xiaomi_mimo-v2.5-pro), [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:14+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science), [https://github.com/harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science), [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL) | 2026-11-05T08:14+08:00 |
| automationbench-v1.0.6 | 待核实 | 16 (metric=score; version=1.0.6; variant=MiMo-V2.5 Pro comparison column) | [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://github.com/zapier/AutomationBench](https://github.com/zapier/AutomationBench) | 2026-11-05T08:14+08:00 |
| osworld-v2.1 | 待核实 | — | [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro) | 2026-11-05T08:14+08:00 |
| chartography | 不适用 | — | [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro), [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T08:14+08:00 |
| humanitys-last-exam | 待核实 | 48 (metric=accuracy; variant=MiMo-V2.5-Pro-FP8); 47 (metric=accuracy; variant=MiMo-V2.5-Pro-MXFP4); 34 (metric=accuracy; variant=MiMo-V2.5-Pro-FP8; without tool); 33 (metric=accuracy; variant=MiMo-V2.5-Pro-MXFP4; without tool); 36 (metric=pass@1; dataset=Artificial Analysis text-only subset; 2,158 questions; variant=MiMo-V2.5-Pro (Reasoning; Artificial Analysis legacy HLE evaluation)) | [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash), [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T08:19+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/mimo-v2-5-pro](https://artificialanalysis.ai/models/mimo-v2-5-pro), [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T08:14+08:00 |
| gdpval-aa-v2.1 | 冲突 | 1107 (metric=Elo rating; version=2.1; variant=MiMo-V2.5 Pro comparison column); 1121 (metric=Elo rating; version=2.1; dataset=220 tasks; variant=MiMo-V2.5-Pro (Reasoning; Artificial Analysis comparison); harness=Stirrup); 1129 (metric=Elo rating; version=2.1; dataset=220 tasks; variant=MiMo-V2.5-Pro (Reasoning; current Artificial Analysis leaderboard); harness=Stirrup) | [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T08:19+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.vals.ai/models/xiaomi_mimo-v2.5-pro](https://www.vals.ai/models/xiaomi_mimo-v2.5-pro) | 2026-11-05T08:14+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 19
- metric: score
- version: 1.1
- variant: MiMo-V2.5 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 本地已有 MiMo-V2.5 Pro 对比列 19.0、版本 1.1；Datacurve 2026-06-15 快照另显示 19% ±2，harness 为 mini-swe-agent。模型卡没有说明 metric、数据集、推理档位或评测日期；本地 metric=score 未匹配本仓 pass@1 定义。

尚未解决的问题：
- 原始分数可确认，但缺少足够证据把本地 score 标签更正成 pass@1，并且 Datacurve 区间无法由当前记录表达。

最近核验时间：2026-11-05T08:14+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://mimo.xiaomi.com/mimo-v2-5-pro/](https://mimo.xiaomi.com/mimo-v2-5-pro/)
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [https://arxiv.org/html/2610.40256](https://arxiv.org/html/2610.40256)

研究备注：
- 本地 57.2 未标版本；模型发布来源早于 Scale 于 2026-09-22 更新的 V2。旧版 731-task Pro 结果不映射到 V2 默认 642-task 配置。

尚未解决的问题：
- 未核实到精确 SWE-bench Pro V2 成绩；Scale 动态榜单缺少可确认条目，不据此断言未找到。

最近核验时间：2026-11-05T08:14+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 1.5
- metric: score
- version: 4.0
- variant: MiMo-V2.5 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 65.2
- metric: score
- version: 2.1
- variant: MiMo-V2.5 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 0.51
- metric: accuracy
- version: 4.0
- dataset: 66 tasks; 3 runs per task (avg@3)
- variant: Vals AI; pass@1; temperature 1; top_p 0.95; top_k default; max output 128,000
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/models/xiaomi_mimo-v2.5-pro](https://www.vals.ai/models/xiaomi_mimo-v2.5-pro)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [https://www.vals.ai/models/xiaomi_mimo-v2.5-pro](https://www.vals.ai/models/xiaomi_mimo-v2.5-pro)
- [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 小米对比表给 MiMo-V2.5 Pro 记 1.5（本地原始行 metric=score）；Vals 精确型号页给 0.51% ±0.51，Harness Mini-SWE-agent，66 tasks、avg@3/pass@1，provider Xiaomi，temperature 1、top_p 0.95、top_k default、max output 128K。两个来源的运行配置不能对齐；两行均保留。

尚未解决的问题：
- 小米来源未公开 1.5 的 Harness、采样次数和完整配置；无法判定与 Vals 的 0.51 是配置差异还是记录冲突。

最近核验时间：2026-11-05T08:14+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- [https://github.com/harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science)
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)

研究备注：
- 核对了当前官方目标榜单与方法页面；没有找到足以确认该型号 0.1 结果的固定行。

尚未解决的问题：
- 动态榜单显示范围有限，不能据缺席断言未找到。

最近核验时间：2026-11-05T08:14+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 16
- metric: score
- version: 1.0.6
- variant: MiMo-V2.5 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://github.com/zapier/AutomationBench](https://github.com/zapier/AutomationBench)

研究备注：
- 官方 Xiaomi 对比表精确列出 MiMo-V2.5 Pro 16.0 / v1.0.6，本地已有该值；来源未给 task_completed_correctly metric 的明示标签、dataset、harness 或评测日期，因此保留 raw score 并待复核映射。

尚未解决的问题：
- 本地 metric=score，与本仓 task_completed_correctly 不一致；缺失评测条件不能补猜。

最近核验时间：2026-11-05T08:14+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)

研究备注：
- 模型支持工具调用，但公开 OSWorld 结果页未确认精确 2.1 成绩；OSWorld-Verified 的缺失项不视作 OSWorld 2.1。

尚未解决的问题：
- 未取得该版本可核实结果；动态榜单缺席不足以判未找到。

最近核验时间：2026-11-05T08:14+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 该型号官方模型卡和本地 TOML 输入为 text，输出 text；没有图像输入，不能完成 Chartography 图表视觉阅读任务。

最近核验时间：2026-11-05T08:14+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 48
- metric: accuracy
- variant: MiMo-V2.5-Pro-FP8
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 47
- metric: accuracy
- variant: MiMo-V2.5-Pro-MXFP4
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 3

- name: Humanity's Last Exam
- score: 34
- metric: accuracy
- variant: MiMo-V2.5-Pro-FP8; without tool
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 4

- name: Humanity's Last Exam
- score: 33
- metric: accuracy
- variant: MiMo-V2.5-Pro-MXFP4; without tool
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 5

- name: Humanity's Last Exam
- score: 36
- metric: pass@1
- dataset: Artificial Analysis text-only subset; 2,158 questions
- variant: MiMo-V2.5-Pro (Reasoning; Artificial Analysis legacy HLE evaluation)
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash)
- [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA legacy HLE 比较页的 36 使用原始 HLE 2,158 道 text-only 子集、pass@1；小米 FP4-DFlash 卡另列 FP8 48、MXFP4 47 及无工具 34/33。不同来源的量化、工具条件和数据配置分别保留。

尚未解决的问题：
- AA 页面是旧版 HLE 评测上下文；小米卡没有提供完整 HLE 子集、工具及评测设置，不能作同配置冲突判断。

最近核验时间：2026-11-05T08:19+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/mimo-v2-5-pro](https://artificialanalysis.ai/models/mimo-v2-5-pro)
- [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前精确型号页显示 Intelligence Index 为 N/A；旧版 V4.3.2 的 26 分不是 V5 结果。

最近核验时间：2026-11-05T08:14+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1107
- metric: Elo rating
- version: 2.1
- variant: MiMo-V2.5 Pro comparison column
- source: [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: GDPval-AA
- score: 1121
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- variant: MiMo-V2.5-Pro (Reasoning; Artificial Analysis comparison)
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 3

- name: GDPval-AA
- score: 1129
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks
- variant: MiMo-V2.5-Pro (Reasoning; current Artificial Analysis leaderboard)
- harness: Stirrup
- source: [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424](https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 保留小米比较表 1107、AA 历史比较内容 1121、当前 AA v2.1 leaderboard 1129 ±17。当前可直接复核的是 1129；1121 来自现已更新的动态比较页，已无当前可见行。

尚未解决的问题：
- 三个来源未给出可对齐的运行快照/评测日期；需查找 1121 的历史页面快照，再判断 1107、1121 与 1129 是修订还是配置差异。

最近核验时间：2026-11-05T08:19+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.vals.ai/models/xiaomi_mimo-v2.5-pro](https://www.vals.ai/models/xiaomi_mimo-v2.5-pro)

研究备注：
- 当前 v2.2 榜单展示有限的最新/frontier 集合；模型页可见旧版 Vals Index 数值未明确标为 v2.2。旧 v2.0/v2.1 不映射。

尚未解决的问题：
- 没有核实到精确型号 v2.2 指数值；榜单缺席不作为未找到。

最近核验时间：2026-11-05T08:14+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/mimo-v2-5-pro"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前精确型号页显示 Intelligence Index 为 N/A；旧版 V4.3.2 的 26 分不是 V5 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "官方 Xiaomi 对比表精确列出 MiMo-V2.5 Pro 16.0 / v1.0.6，本地已有该值；来源未给 task_completed_correctly metric 的明示标签、dataset、harness 或评测日期，因此保留 raw score 并待复核映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地 metric=score，与本仓 task_completed_correctly 不一致；缺失评测条件不能补猜。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro"
        },
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "该型号官方模型卡和本地 TOML 输入为 text，输出 text；没有图像输入，不能完成 Chartography 图表视觉阅读任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "url": "https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "本地已有 MiMo-V2.5 Pro 对比列 19.0、版本 1.1；Datacurve 2026-06-15 快照另显示 19% ±2，harness 为 mini-swe-agent。模型卡没有说明 metric、数据集、推理档位或评测日期；本地 metric=score 未匹配本仓 pass@1 定义。"
      ],
      "status": "待核实",
      "unresolved": [
        "原始分数可确认，但缺少足够证据把本地 score 标签更正成 pass@1，并且 Datacurve 区间无法由当前记录表达。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:19+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-mimo-v2-5-0424"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "保留小米比较表 1107、AA 历史比较内容 1121、当前 AA v2.1 leaderboard 1129 ±17。当前可直接复核的是 1129；1121 来自现已更新的动态比较页，已无当前可见行。"
      ],
      "status": "冲突",
      "unresolved": [
        "三个来源未给出可对齐的运行快照/评测日期；需查找 1121 的历史页面快照，再判断 1107、1121 与 1129 是修订还是配置差异。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:19+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash"
        },
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-5-pro-vs-gpt-5-codex"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA legacy HLE 比较页的 36 使用原始 HLE 2,158 道 text-only 子集、pass@1；小米 FP4-DFlash 卡另列 FP8 48、MXFP4 47 及无工具 34/33。不同来源的量化、工具条件和数据配置分别保留。"
      ],
      "status": "待核实",
      "unresolved": [
        "AA 页面是旧版 HLE 评测上下文；小米卡没有提供完整 HLE 子集、工具及评测设置，不能作同配置冲突判断。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro"
        }
      ],
      "notes": [
        "模型支持工具调用，但公开 OSWorld 结果页未确认精确 2.1 成绩；OSWorld-Verified 的缺失项不视作 OSWorld 2.1。"
      ],
      "status": "待核实",
      "unresolved": [
        "未取得该版本可核实结果；动态榜单缺席不足以判未找到。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-5-pro/"
        },
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro"
        },
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "url": "https://arxiv.org/html/2610.40256"
        }
      ],
      "notes": [
        "本地 57.2 未标版本；模型发布来源早于 Scale 于 2026-09-22 更新的 V2。旧版 731-task Pro 结果不映射到 V2 默认 642-task 配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "未核实到精确 SWE-bench Pro V2 成绩；Scale 动态榜单缺少可确认条目，不据此断言未找到。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        },
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        }
      ],
      "notes": [
        "核对了当前官方目标榜单与方法页面；没有找到足以确认该型号 0.1 结果的固定行。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态榜单显示范围有限，不能据缺席断言未找到。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
        },
        {
          "url": "https://www.vals.ai/models/xiaomi_mimo-v2.5-pro"
        },
        {
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "小米对比表给 MiMo-V2.5 Pro 记 1.5（本地原始行 metric=score）；Vals 精确型号页给 0.51% ±0.51，Harness Mini-SWE-agent，66 tasks、avg@3/pass@1，provider Xiaomi，temperature 1、top_p 0.95、top_k default、max output 128K。两个来源的运行配置不能对齐；两行均保留。"
      ],
      "status": "冲突",
      "unresolved": [
        "小米来源未公开 1.5 的 Harness、采样次数和完整配置；无法判定与 Vals 的 0.51 是配置差异还是记录冲突。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:14+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.vals.ai/models/xiaomi_mimo-v2.5-pro"
        }
      ],
      "notes": [
        "当前 v2.2 榜单展示有限的最新/frontier 集合；模型页可见旧版 Vals Index 数值未明确标为 v2.2。旧 v2.0/v2.1 不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有核实到精确型号 v2.2 指数值；榜单缺席不作为未找到。"
      ]
    }
  },
  "existing_records": 18,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:19+08:00",
  "model_id": "xiaomi/mimo-v2.5-pro",
  "model_notes": [
    "本地 release_date 为 2026-04-22；小米 Model Release log 列 2026-04-23，独立产品发布页列 April 27th。两页的发布时间语境不同；本轮没有足够依据统一定义，保留仓库日期并记录差异。参见 https://mimo.mi.com/docs/en-US/updates/model 与 https://mimo.xiaomi.com/mimo-v2-5-pro。"
  ],
  "new_records": 8,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
