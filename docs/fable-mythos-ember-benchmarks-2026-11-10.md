# Fable 5.2、Mythos 5.2 与 Muse Ember：AA / Vals 同步

## 范围与结果

检查日期：2026-11-10。只追加模型文件的原始成绩，不修改基本资料、已有成绩或模型描述，不生成跨条件排行榜。

| 模型文件 | AA 新增 | Vals 新增 | 合计 | 新增成本 |
|---|---:|---:|---:|---:|
| `models/anthropic/claude-fable-5-2.toml` | 60 | 25 | 85 | 69 |
| `models/meta/muse-ember-1.0.toml` | 20 | 10 | 30 | 30 |
| `models/anthropic/claude-mythos-5-2.toml` | 0 | 0 | 0 | 0 |

合计新增 **115 条成绩、99 条成本，修正已有成绩 0 条**。按后续要求，Vals 系列在 `benchmarks/` 中只保留已有的 `vals-index-v2.2`；最终新增 **7 个 AA Benchmark 定义及对应中文翻译**。Fable 原有 12 条、Ember 原有 11 条成绩连同注释原样保留；Mythos 文件完全未改动。被移除定义对应的原始成绩仍保留在模型文件中，不再关联定义。

- AA：Fable 的 `low`、`medium`、`high`、`xhigh`、`max` 五档，以及 Ember 的 `xhigh`、`max` 两档。每档包含 Intelligence Index v5.0.1 及九个组成评测的主指标；Fable 另有原始 HLE text-only 和 GDPval-AA v2.1。AA-Omniscience 收录的是来源的 **Net Score**，不是自行计算的指数贡献；指数实际使用其准确率与非幻觉率分量，不用 Net Score 重算指数。
- Vals：Fable 模型页列出的全部 **19 项 overall 总分**，另收录 **6 项回退计失败重评分**；Ember 模型页列出的全部 **10 项 overall 总分**。档位逐行读取为 Fable `compute_effort = "high"`、Ember `reasoning_effort = "max"`，不以发布文的大小写改写原值。
- 未在 AA 当前模型目录、其模型页公开配置目录、Vals 可用模型目录及本轮相关榜单中找到明确归属于 **Mythos 5.2** 的结果。不能用 Fable 代填，也不将旧 Mythos 型号合并。这是本次检查范围内未找到，并非证明所有地方都没有结果。

## 来源与保留口径

主要模型页：

- AA Fable：[Max](https://artificialanalysis.ai/models/claude-fable-5-2)、[Low](https://artificialanalysis.ai/models/claude-fable-5-2-low)、[Medium](https://artificialanalysis.ai/models/claude-fable-5-2-medium)、[High](https://artificialanalysis.ai/models/claude-fable-5-2-high)、[Xhigh](https://artificialanalysis.ai/models/claude-fable-5-2-xhigh)。
- AA Ember：[Max](https://artificialanalysis.ai/models/muse-ember)、[Xhigh](https://artificialanalysis.ai/models/muse-ember-xhigh)。
- Vals：[Fable 5.2](https://www.vals.ai/models/anthropic_claude-fable-5-2)、[Muse Ember](https://www.vals.ai/models/meta_muse-ember)。
- [AA 评测方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)、[Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index)、[Vals 当前 Index JSON](https://www.vals.ai/_astro/benchmark_view_vals_index.DeTlTtu4.json)。其余各评测页及对应 JSON 已逐项核对，直接保存在各条记录的 `source` / `cost_source` 中。

AA 数值来自公开模型页内嵌、身份匹配的配置对象，比例只精确换算为百分数，不按界面整数反推。最终定向校验直接以 `Decimal` 解析原始 HTML 中的 JSON 数字，避免先转浮点再核对。Vals 使用每个评测页公开引用的 JSON 的 `tasks.overall[model]`，不重新计算行业权重、误差或平均成绩。

AA Index 成本取 `intelligenceIndexCostPerTask.cost.total`，单位 `USD/weighted task`；组成评测取 `intelligenceIndexEvaluations[].costPerTask`，单位 `USD/task`，不取加权贡献或总费用。AA 成本是来源当前定价、缓存口径下的观测，不声称为评测当日账单。GDP.pdf 成本不含裁判、PDF 处理及 OCR。Vals 成本取同一行 `cost_per_test`，单位 `USD/test`，不借用 API token 单价。

Fable 的 AA 配置均明确为 **Default Fallback**，不冒充无回退评测。Vals 的 Code Migration、Legal Index、Legal Research、ProgramBench、Terminal-Bench 4 和 Vals Index 有不同的回退计失败成绩，分别保留。例如：

| Vals 评测 | 发布成绩 | 回退辅助任务计失败 |
|---|---:|---:|
| Vals Index 2.2 | 71.309 | 69.483 |
| Code Migration 1.1 | 83.265 | 73.02 |
| Vals Legal Index | 69.175 | 69.09 |
| Legal Research Bench | 46.154 | 45.673 |
| ProgramBench | 19 | 18 |
| Terminal-Bench 4.0 | 65.152 | 58.586 |

重评分直接读取页面引用的 `refusal_fallback.*.js` 内 JSON 的 `noFallbackScorePct`，相应资源 URL 保存在重评分记录中；不根据回退率自行扣分。它们是**同次轨迹的事后重评分，不是关闭回退后重新运行**，也不复用原运行成本或误差。Science Index、Terminal-Bench-Science 虽用过回退，但重评分不改变分数，保留一条并注明。SWE-bench Multimodal 未取得该行完整回退账本，不声称无回退。

AA 与 Vals 的 Terminal-Bench 和 Science 运行次数、任务限制与框架配置不同，分别保留；AA 的 AutomationBench 护栏门控目标完成率不冒充 Zapier 的整任务严格完成率。HLE-Diamond 与原始 HLE、CritPt 困难子集与全量数据、GDP.pdf 的 AA 与 Surge 实现均不混用。Ember 发布文的 Index v5.0 = 36 与 AA 当前 v5.0.1 = 36.0212987864912 分别保留，不视为原成绩精度修正。

## 定义与本地化

新增 AA 定义：`aa-briefcase-v1.1`、`aa-omniscience-v1.1`、`automationbench-aa-v1.0.6`、`critpt-v2-hard`、`frontiercode-v2`、`gdp-pdf-aa`、`hle-diamond`。

后续按用户要求移除最初新增的 16 个 Vals 专有定义（包括 `hlab-vals-v1.1`）及其翻译，Vals 系列只保留已有的 `vals-index-v2.2`。通用的 Terminal-Bench / Terminal-Bench-Science 定义不受影响，仍可关联相应 Vals 来源成绩；模型文件中的全部原始成绩、成本、条件及来源不作删改。

Vals 原始成绩的版本直接采用评测视图元数据（包括 `"1"` / `"1.0"`），不是推断出的上游数据集 tag。没有语义化版本依据的 GDP.pdf 与 HLE-Diamond 使用 `unspecified` 定义，成绩不补造版本。`i18n/zh-CN.toml` 最终仅追加 7 项 AA 定义翻译，全部原有模型与评测译文不变。

## 限制与未解决项

- 本轮覆盖 AA 当前指数九个评测的主指标及有明确值的原始 HLE / GDPval，和 Vals 模型页的全部 overall 总分；未扩展 AA 六个行业能力指数、额外旧评测、Elo 子项或 Vals 行业/领域分项，也没有复制任务内容或轨迹。
- 新成绩没有推断评测日期；发布时间、数据 `updated`、检查日期均不当作实验日期。输出 token 上限只是 Vals 行设置，不写成新的模型规格。
- 标准误、GDPval 区间和采样参数保存在 TOML 注释中。现有 Schema 没有结构化误差字段，注释不会进入 JSON；不因此重写为带误差的字符串或新增未设计字段。
- 未核实 Ember 的原始 HLE / GDPval 数值；公开配置对象为缺失值，跳过而非填零。不存在已确认、需要覆盖的同身份旧成绩冲突。
- **再分发许可仍需人工确认。** AA [网站条款](https://artificialanalysis.ai/terms-of-use) 的使用、自动采集、复制与分发限制见既有[许可核查](benchmark-costs-2026-11-06.md#定义映射与许可)。Vals 标示 All rights reserved，未确认单独的数据开放许可。网页公开、保留来源或 Models.dev 的 MIT 许可均不等于取得这两站数据的再分发授权。本轮未提交、推送或发布。
- 原有 `TODO.md`、Mythos 文件及所有旧译文均保留。执行期间出现的独立网页代码与测试改动未由本任务修改或回退。

## 首轮同步的校验（移除 Vals 定义前）

- `python3 scripts/validate.py`：**922 个 TOML，全部通过**。
- `python3 scripts/build.py`：**887 个模型、34 个定义、1 个语言文件**构建成功。当前警告为 1,206 条历史成绩未映射、0 条歧义、32 个历史模型描述缺译；按任务开始时的目标模型及定义/译文恢复基线，未映射原为 1,211 条，本轮没有新增未映射记录或缺译。
- `python3 -m unittest discover -s tests -v`：**112 项通过**。
- `git diff --check`：通过。
- 独立定向核对：**115 条新成绩、99 条成本**逐条与原始公开数据精确一致，档位、成本来源、无评测日期及唯一的定义映射均通过；6 条重评分没有借用成本。
- 对比任务开始前快照：两个更新模型的原始全文仍是当前文件的完整前缀，已有基本字段、成绩与注释不变；Mythos 和 TODO 字节不变；已有翻译逐键不变。新增 23 项定义翻译与源描述核对。
- 生成 JSON 的全部模型、定义及中文本地化与 TOML 解析内容一致。`dist/` 仅由构建生成，未直接编辑。

这些检查不是完整上游严格 Schema 或全部历史成绩真实性认证，也不证明已取得公开分发许可。

## 按要求精简 Vals 定义后的校验

- 删除 16 个 Vals 专有定义及对应中文翻译，只保留 `benchmarks/vals-index-v2.2.toml`；模型文件不变。
- `python3 scripts/validate.py`：906 个 TOML 全部通过。
- `python3 scripts/build.py`：887 个模型、18 个定义、1 个语言文件构建成功。未映射成绩由 1,206 增至 1,234（新增 28 条未映射是删除定义的预期结果，原始成绩仍保留）；歧义仍为 0，历史缺译仍为 32 项。
- 定向检查确认仅这 16 个定义被删除，保留的定义、全部模型及无关网页/测试文件与本次精简前的哈希一致，本地化没有悬空评测键。
- `git diff --check` 通过；JSON 由构建重新生成。本次精简未重新运行单元测试，前述 112 项通过是首轮同步结果。
