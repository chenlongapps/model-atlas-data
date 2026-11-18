# 评测来源与口径

[文档导航](README.md) · [成绩与成本规范](data-format.md#benchmark-成绩) · [冲突与许可](review-notes.md)

本页汇总既有核验方法，不保证来源网页、资源 URL 或版本始终有效。每次导入仍须确认精确模型、版本、档位及实验条件；动态资源失效时从官方页面重新定位，不猜 URL。以下链接是核验入口，不是自动采集或再分发授权。

## 常用入口与成本字段

| 来源 | 成绩与方法 | 成本口径 |
| --- | --- | --- |
| [DeepSWE](https://deepswe.datacurve.ai/) · [v1.1 方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1) · [JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) | 同一模型、reasoning_effort、Harness 的 `pass_at_1`，不取 pass@4 或推算通过率 | `mean_cost_usd`，已评分尝试的平均 `USD/task`，不是中位数或总费用 |
| [Terminal-Bench 官方榜](https://www.tbench.ai/leaderboard/terminal-bench/4.0) | 原生 Agent、档位和任务配置分别匹配 | `metrics.total_cost_usd`，`USD/evaluation`；保留任务与试验数，不除成每任务 |
| [Vals Terminal-Bench](https://www.vals.ai/benchmarks/terminal-bench-4) · [Science](https://www.vals.ai/benchmarks/terminal-bench-science) · [Index](https://www.vals.ai/benchmarks/vals_index) | 页面所引用 JSON 的 `tasks.overall[model]`，不重复算分类或行业总分 | 同一行 `cost_per_test`，`USD/test`；null 省略，舍入显示不替代原始值 |
| [AA Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) · [方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 精确配置页/对象及适用 Index 版本；不能凭快照文件名确定版本 | Index 用 `intelligenceIndexCostPerTask.cost.total`，`USD/weighted task` |
| [AA 组成评测](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 同一配置对象的独立评测主指标 | `intelligenceIndexEvaluations[].costPerTask`，`USD/task`；不取 `weightedCostPerTask` 或总评测成本 |

原始比例与百分数只在来源、指标及单位已明确时精确换算单位；不从界面整数反推精确值，不转换不同评分指标。AA 成本可能使用当前定价及缓存口径，不自动视为评测日账单；GDP.pdf 的 AA 成本不含裁判、PDF 处理及 OCR。

## 必须分开的评测条件

| 评测 | 已知边界 |
| --- | --- |
| DeepSWE v1.1 | 全集 113 项，逐配置保留已尝试/有效任务、重复次数及错误排除规则，不假定每个模型完成全量。Provider/verifier/network 错误排除，不代表上下文失败或 Agent 超时也排除 |
| Terminal-Bench 4 | Vals 既有核验为 66 项、mini-swe-agent、三次 pass@1 均值、每任务 8 小时、不设步骤/费用上限；AA 与原生 Agent 不同，不互套成本 |
| Terminal-Bench Science | Vals 既有核验为 70 项、单次 pass@1、8 小时，仅基础设施/Provider 错误可重试；AA 为每任务三次 pass@1 均值，不当作同次实验 |
| AutomationBench | [AA](https://artificialanalysis.ai/evaluations/automationbench-aa)是护栏门控的目标完成比例；[Zapier](https://zapier.com/benchmarks)是整任务严格完成率，两者不能互换 |
| 原始 HLE | [Scale](https://labs.scale.com/leaderboard/humanitys_last_exam)最终 2,500 题多模态；[AA](https://artificialanalysis.ai/evaluations/humanitys-last-exam)为其中 2,158 道文本题，不是同一实验 |
| HLE-Diamond | [AA](https://artificialanalysis.ai/evaluations/hle-diamond)定义为 1,000 题（272 图像题）、无工具、pass@1、GPT-5.6 Luna medium 判分；[Scale 实现](https://labs.scale.com/leaderboard/hle-diamond)不并入 AA 专用定义 |
| Chartography | 工具、数据集、重复次数、裁判和 Harness 分别核对；厂商 original / with Python 不自动等于 Surge 榜单配置 |
| CritPt / GDP.pdf / AA-Omniscience | 困难子集不等于全量；AA 与 Surge 实现不混用；Omniscience Net Score 不等于指数贡献，不用它重算 Index |
| Vals Index | 综合 performance score，不是单一能力准确率；overall 的 Harness 为空时，不借用分项 Harness |

以上为既有来源核验结论，不是未来所有运行的默认配置。来源未给出的条件继续留空。

## 回退、误差与修订

- Default Fallback 和无回退结果分别保留，不因模型名或档位相同合并。
- Vals `refusal_fallback.*.js` 中的 `noFallbackScorePct` 是**同次轨迹的事后重评分，不是关闭回退重新运行**。不按回退率自行扣分，不借用原运行的成本或误差；重评分不变时不额外重复添加。
- 标准误、区间和采样设置保留在成绩旁的 TOML 注释中。当前没有结构化误差字段，JSON 不携带这些注释；不能声称下游已获得完整不确定性信息。
- `max_output_tokens` 是实验设置，不直接填模型固有输出上限；页面更新和数据采集时间不作评测日期。
- 同名指标只有核对方法后才能认定等价。例如 Vals Terminal-Bench 的二元验证通过率曾核实为 task resolution rate；不能将所有来源的 `accuracy` 批量改成该指标。
- 来源修订须有依据；舍入差异、精确值不同和实验条件变化不能一律当精度补全。缺少 run ID 或修订说明时，保留已有记录并报告。

## 模型映射

研发机构与 Provider 前缀分开核对；不得将 Baseten 等托管商另建为 NVIDIA 模型的研发机构。已核实的特殊映射包括 Vals 的 `alibaba/qwen3.8-max-internal` → `alibaba/qwen3.8-max-0902`、`meta/muse-wonder` → `meta/muse-wonder-1.0`；这些依据不自动适用于后续部署。

Mistral Large 4 的 10 月 29 日开放权重版继续训练于 Preview 之后，见[官方公告](https://mistral.ai/news/mistral-large-4-oss/)与[模型卡](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)。Vals `mistralai/mistral-large-4-oss` 对应 `mistral/mistral-large-4-1t-a52b`，不并入较早 Preview。滚动别名、速度档和未披露检查点的 API 成绩也不能自动传播到相似模型。
