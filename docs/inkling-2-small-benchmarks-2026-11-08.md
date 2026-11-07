# Inkling 2 Small Benchmark 核验（2026-11-08）

## 范围与变更

- 模型：`thinkingmachines/inkling-2-small`，对应 2026-11-05 正式发布的 Inkling 2 Small；不并入 Inkling、Inkling Small 或 Fledge-Alpha 早期检查点。
- 本轮优先核对仓库既有的 11 项评测范围，不是官方模型卡全部评测的完整导入。
- 唯一成绩维护位置：`models/thinkingmachines/inkling-2-small.toml`。新增 11 条，共 14 条；未修改原有 3 条成绩的分数、成本或实验条件，修复其中 2 条 Vals 成绩的来源链接。
- 新增 `benchmarks/automationbench-aa-v1.0.6.toml` 及 `i18n/zh-CN.toml` 对应翻译；模型基本信息和描述未改。

## 主要来源与判定

- [官方发布](https://thinkingmachines.ai/news/inkling-2-small/)与[模型卡](https://thinkingmachines.ai/model-card/inkling-2-small/)：采用 DeepSWE v1.1、SWE-bench Pro V2 Hard / Full、Chartography original / with Python 共 5 条。发布文声明 effort `0.99`（xhigh）、temperature 1.0、最大轨迹预算 1M tokens；记录为发布方披露的快照条件，不冒充重新运行或独立确认的逐行配置。来源未提供的 Harness、重复次数及评测日期省略。
- [Artificial Analysis 模型页](https://artificialanalysis.ai/models/inkling-2-small)及[评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)：页面内嵌公开数据的 `slug = "inkling-2-small"`、名称和发布日期均匹配。新增 Terminal-Bench 4.0、Terminal-Bench-Science 0.1.0、AutomationBench-AA 1.0.6、原始 HLE text-only 和 GDPval-AA 2.1 共 5 条；复核已有 Intelligence Index v5.0.1 原值不变。分数从原始比例精确换算为百分数，不从界面整数反推。
- AA 的本轮 Terminal-Bench、Science、AutomationBench-AA 成本直接取同一模型的 `intelligenceIndexEvaluations[].costPerTask`，单位 `USD/task`；不使用按指数权重加权的 `weightedCostPerTask`，不从 token 单价推算。既有指数的 `USD/weighted task` 保持不变。AA 未披露该模型行的 effort，不套用发布方的 `0.99`。
- [Vals Science 页面](https://www.vals.ai/benchmarks/terminal-bench-science)和[原始 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_science.KYAu-wfB.json)：新增 1 条整体成绩及 `USD/test` 成本，记录原始精度、effort、Harness、70 tasks、单次 pass@1、仅基础设施或 Provider 错误可重试、8 小时任务限制。没有导入五个领域分项。
- Vals Science 是单次评测，AA Science 是每任务三次 pass@1 的均值，不能当作同一记录冲突，也不以高分覆盖低分。Terminal-Bench 4.0 同样保留 AA 与 Vals 的不同配置及成本口径。
- [AutomationBench-AA 方法](https://artificialanalysis.ai/evaluations/automationbench-aa)确认其主指标是护栏约束下的目标完成比例，违反护栏则该任务为零分；不是 [Zapier 官方榜单](https://zapier.com/benchmarks)的 `task_completed_correctly`。因此使用独立定义，不修改旧定义、不迁移其他模型的既有记录。
- 既有 Vals Index 的 `CxyItaos` JSON 已返回 404；当前 [Index JSON](https://www.vals.ai/_astro/benchmark_view_vals_index.Bndh1wJE.json)和 [Terminal-Bench JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.CfJg38mV.json)均核对到同一模型的原分数、成本和采样设置。`source` 改为稳定评测页，`cost_source` 指向当前原始 JSON；旧资源标识保留于注释中。

## 跳过、限制与许可

- [DeepSWE 当前榜单](https://deepswe.datacurve.ai/)未见该型号；已有明确型号的发布方成绩可以收录，但不据通用榜单方法补造该行 Harness 或成本。
- [Scale Full 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)与 Hard 榜单存在名称为 `Inkling Small 2`、版本字段为空的条目，精度高于发布方快照。本轮未仅凭相似名称及舍入分数认定为同一检查点，故采用明确写明 Inkling 2 Small 的模型卡原始精度，不额外导入这些行。需取得稳定模型 ID 或明确别名依据后再核实；未将 `confidenceInterval_upper = 0` 当作已确认的零不确定性。
- [Surge Chartography 榜单](https://surgehq.ai/benchmarks/chartography)未列出 Inkling 2 Small；不能将旧 Inkling / Inkling Small 的成绩或通用运行次数赋给新型号。发布方的 original 和 with Python 分开保留，其他具体工具配置未知。
- HLE 使用 AA 明确披露的 2,158 题 text-only 评测；模型卡中另列 HLE-Diamond，不将后者映射到原始 HLE 定义。
- 未取得 Zapier 严格任务完成率的该型号可靠成绩。[OSWorld 项目页](https://osworld-v2.xlang.ai/)和[仓库](https://github.com/xlang-ai/OSWorld-V2)也未取得该型号且属于 `osworld-v2.1` 的可核实结果；两者均不填零。这不是对所有潜在公开结果的穷尽性证明。
- 其他官方表格评测（包括其他 AA 指数组件、Terminal-Bench 2.1、安全、视觉、金融评测等）未在本轮扩展；不把缺少定义或尚未逐项核实的结果混入既有定义。
- [AA 网站条款](https://artificialanalysis.ai/terms-of-use)第 2.1、2.2、3.3 节对使用、复制、再分发及自动采集设有限制；未取得适用于本仓库分发用途的单独授权。停止继续采集 AA，发布或商用前需人工确认授权，不能因为网页公开或保留来源就声称可自由再分发。Vals 页面标示 All rights reserved，亦未确认独立的数据再分发许可。本轮没有提交、推送或发布。
- [Thinking Machines 模型卡](https://thinkingmachines.ai/model-card/inkling-2-small/)仍列 Tinker Terms of Use，发布文仅计划后续开放权重；不把计划中的 Apache-2.0 权重许可当作已生效许可或评测数据许可，保留现有 `open_weights = false`。

## 实际校验

- `python3 scripts/validate.py`：868 个 TOML 全部通过。
- `python3 scripts/build.py`：成功生成 855 个模型、12 个评测定义、1 个语言文件；全库仍有 1,184 条既有未匹配成绩、0 条歧义、3 项模型描述缺译警告，本轮未批量修复无关记录。
- `python3 -m unittest discover -s tests -v`：112 项全部通过。
- 定向检查：目标模型 14 条成绩均唯一匹配定义；与 Git 原版比较确认仅追加 11 条成绩并修复 2 条来源，已有分数、成本、条件和模型基本信息未变。
- 用 `Decimal` 比较 TOML 数字字面量与本轮已读取的 AA / Vals 原始值：百分数换算、非加权每任务成本、GDPval Elo 及 Vals Science 设置一致。额外确认生成 JSON 与构建采用的标准数字类型解析结果一致。
- 上述校验不证明数据再分发许可已获授权，也不是完整 Models.dev Schema 校验；不同来源或条件的成绩未生成可比性排名。
