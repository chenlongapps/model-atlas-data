# 数据规范

[文档导航](README.md) · [校验与构建](development.md)

## 目录与模型身份

| 路径 | 内容 |
| --- | --- |
| `models/<lab>/<model-id>.toml` | 一个模型一个文件，成绩的唯一人工维护来源 |
| `benchmarks/*.toml` | Benchmark 定义，不重复维护成绩 |
| `i18n/<语言>.toml` | 模型和评测描述翻译 |
| `dist/` | 构建生成的 JSON，不直接修改、不提交 Git |

模型尽可能遵循 [Models.dev v2 Schema](https://github.com/anomalyco/models.dev/blob/dev/packages/core/src/schema-v2.ts)，使用 `schema = 2`。ID 由路径确定，例如 `models/deepseek/deepseek-r1.toml` 对应 `deepseek/deepseek-r1`，不另加顶层 `id`。

新增前核对上游机构、规范 ID 和确切版本。Preview、正式版、日期后缀及不同检查点不能仅凭名称相近合并。区分模型固有属性与 Provider 能力、价格、缓存和推理配置；不从上下文窗口推算最大输入长度。未知可选字段省略，不填零或默认布尔值。

本仓库的基础检查不是完整上游严格 Schema 校验。已核实资料不足的档案可能缺少上游要求的能力字段；严格消费者应补齐核实资料或拒绝不完整档案，不能把缺失视为 `false`。

## 模型参数量

使用上游允许的 `metadata` 扩展点，不新增顶层字段：

```toml
[metadata.modelatlas.parameters]
total_billion = 671
active_billion = 37
sources = ["https://github.com/deepseek-ai/DeepSeek-R1"]
```

| 字段 | 约定 |
| --- | --- |
| `total_billion` | 完整模型总参数量，单位 B（十亿） |
| `active_billion` | 来源明确披露的每 token 激活参数量，单位 B |
| `sources` | 支持数值及统计口径的非空 HTTP(S) URL 数组，不重复 |
| `notes` | 可选非空字符串，记录近似精度、范围及限制 |

- 数值必须为有限正数；总量和激活量同时存在时，口径一致且激活量不超过总量。未知项省略，稠密模型也不自动令二者相等。
- 只采用对应版本的可靠资料。不从名称、文件体积、量化位宽或专家数推算；350M 可换算为 `0.35`，不补造精度。
- 骨干、有效参数量、每 token 激活量和完整模型总量不能混用。官方名义规模与检查点权重统计可能口径不同，须保留说明，不据此强制生成参数排名。
- 新增或更新 `open_weights = true` 模型时，主动查阅该版本官方资料，分别核实完整总量和激活量；不能只更新标记或权重链接。无法核实的项省略并报告。
- 模型卡未披露总量时，可核对完整未量化检查点的 Hub 已发布统计，或固定 commit 的实际浮点权重张量元数据。必须核对完整性、数据类型、索引及统计自洽性；安全方法见[参数量核验](model-parameters.md)。
- 参数表整体可省略；存在时至少提供一个有来源的完整模型或组件数值，不能只有说明文字。不因参数缺失而修改 `open_weights`。

### 组件参数量及兼容策略

`components` 是可选、不嵌套的表数组。每项有唯一非空 `name`、至少一个参数数值及独立 `sources`，可选 `notes`；数值及单位规则与父表相同。

```toml
[metadata.modelatlas.parameters]
notes = "Only component counts are disclosed; complete total is unknown."

[[metadata.modelatlas.parameters.components]]
name = "Multimodal Decoder"
total_billion = 12
sources = ["https://huggingface.co/mistralai/Pixtral-12B-2409"]

[[metadata.modelatlas.parameters.components]]
name = "Vision Encoder"
total_billion = 0.4
sources = ["https://huggingface.co/mistralai/Pixtral-12B-2409"]
```

组件可能重叠，也可能只是管线的一部分。不求和填父表、不从整模型倒推组件、不把未知部分视为零。仅有组件时，父表无需重复 `sources`，完整总量仍为未知。

这是 ModelAtlas 的 metadata 语义约定，不是上游标准参数字段。旧消费者只读父表数值，不得回退到首个组件或组件之和；新消费者应单独展示组件范围，不与完整总量混排。旧记录无需迁移，JSON 保留数值、数组顺序和缺失状态。

Models.dev 的通用 JSON metadata 扩展点无需改变；严格的 ModelAtlas 消费者需显式支持组件字段。上游未提供的本地 metadata 在同步时保留，但上游明确提供同路径字段时仍按基本信息同步规则处理，不作永久锁定。

## Benchmark 成绩

成绩保存在模型的 `[[benchmarks]]` 表数组中。`name`、`score` 必填；按来源提供 `metric`、`version`、`dataset`、`effort`、`variant`、`harness`、`source` 和 `date`。

```toml
[[benchmarks]]
name = "Example Bench"
score = 42.1
effort = "xhigh"
variant = "without tools"
source = "https://example.com/results"
```

- 保留数值精度、原始指标和已知条件；不推算成绩、不将缺值填零、不以宣传描述代替量化结果。
- 不同模型版本、数据集、指标、推理预算、工具、Harness、来源或实验设置分别保留，不自动选最高分。
- `date` 仅记录已披露的评测日期。发布日期、文件名日期、来源更新时间和检查时间都不能代替它。
- 关键条件无法用 Schema 准确表达时，保留来源并报告限制，不塞入无关字段。TOML 注释不会进入 JSON，不能假定下游已获得注释中的条件或误差说明。
- 判重核对模型 ID、名称、版本、指标、数据集、档位、变体、Harness、来源和日期，不能只看名称与分数。同条件下重复或冲突都要报告；只有确认同一记录的官方修正后才能更新。

### 推理档位

`effort` 是可选非空字符串，原样保留来源的官方名称和大小写，不限制枚举，例如 `"xhigh"`、`"Adaptive/Max"`。

来源未说明则省略，不从模型名推断，也不设置默认档位。`variant` 保存工具使用、重复次数等其他条件；不自动解析或迁移旧 `variant`。

`effort` 参与判重，缺失不等于任何显式档位（包括 `"default"`）。定义映射仍只按名称、版本和指标进行；JSON 与自动同步保留原值及缺失状态。

### Benchmark 成绩的成本

```toml
[[benchmarks]]
name = "Example Bench"
score = 42.1
cost = 1.25
cost_unit = "USD/task"
source = "https://example.com/results"
```

- `cost` 为有限非负数，与非空 `cost_unit` 成对提供。缺失、无定价占位或显示舍入为 `$0.00` 不等于真实零费用；只有明确报告真实零成本才记 `0`。
- 单位须包含币种及口径，如 `USD/task`、`USD/test`、`USD/weighted task`、`USD/evaluation`。不混用、不换算币种、不按 API 单价或任务数推算；总成本保留已知任务数和重复次数。
- 成本属于该条实验结果，不是模型固有属性或 Provider token 单价。核对模型版本、档位、Harness、数据集和实验设置，不从其他来源或配置移用费用。
- 可选 `cost_source` 为独立的 HTTP(S) 成本来源，省略时使用 `source`；提供成本时至少须有一个有效来源。独立成本来源不能替代实验条件核对。
- 重定价、缓存等已知口径保留在注释中。当前观测成本不自动等于评测当日账单；更新时保留旧值及依据，不推断修订原因。
- 成本、单位及成本来源不参与成绩身份判重，不能用不同成本掩盖重复或冲突。JSON 原样保留，自动同步不覆盖已有成绩及成本。

`effort`、`cost`、`cost_unit`、`cost_source` 是 ModelAtlas 扩展，不代表严格上游 Models.dev Schema 已支持；对接严格上游消费者时须显式处理，例如移除这些字段。

## Benchmark 定义与展示

`benchmarks/` 是 ModelAtlas 专有定义，不是 Models.dev 模型 Schema。**仅用户明确要求或确认后新增定义**；未映射的已核实原始成绩仍可保留，不为消除警告创建定义。

定义须包含稳定唯一的 `id`、正式 `name`、`version`、`category`、`metric`、`unit`、`higher_is_better`。不猜版本、单位或评分方向，不将综合指数当作单一能力测试；不兼容版本分别定义。

构建按名称、版本和指标匹配：除定义的 `version` 外，可匹配其显式声明的 `compatible_versions`；`version = "unspecified"` 的定义允许成绩省略版本。其余不推断版本或默认条件，缺少或存在多个匹配时报告。兼容版本只能依据已核实的方法声明，不能为消除警告随意添加；旧覆盖率统计不代表当前映射结果。

排行榜是派生数据，须先确认版本、指标、数据集、工具及环境可比，再按正确方向排序；条件不足时只保留原始成绩，不强制排名。网页排序或数学前沿不是官方完整排名。

### 展示优先级

定义可提供顶层 `popularity`，取有限的 `[0, 1]` 数值，越大越优先。这是人工维护的展示权重，不是官方知名度或模型能力指标。

字段可省略，JSON 保留缺失状态、不填零。Web Explorer 默认按其降序排列评测，同分按名称和 ID、缺失值置后；搜索及分类沿用此顺序，手动表头排序优先。不增加知名度展示列，也不改变模型成绩排序。

## Benchmark 成绩汇总

`models/<lab>/<model-id>.toml` 的 `[[benchmarks]]` 是成绩的维护入口。构建从这些记录和 `benchmarks/` 的定义同时生成两份汇总。

- `benchmark-results/<benchmark-id>.toml` 对应一个定义。未匹配或匹配有歧义的记录按原始 `name` 分文件，放入 `benchmark-results/uncategorized/`。文件名使用简化的名称和原名 SHA-256 的前 16 位十六进制字符，记录内部保留准确名称。
- `dist/benchmark-results.json` 的 `benchmarks` 以定义 ID 为键，`uncategorized` 以原始评测名称为键。每个键的值与相应 TOML 解析后的结构一致。已有模型、定义和本地化 JSON 继续使用原有结构。

已定义评测使用一个 `results` 数组，TOML 表示为 `[[results]]`。数组可为空。每条记录包含 `model_id` 和 `result`，后者逐字段保留源记录，包括字符串分数、扩展字段和缺失状态。

- `higher_is_better = true` 按数值分数降序，否则升序。同分按模型 ID 升序，同模型同分沿用源文件顺序。字符串分数保持原文，放在数值之后，按模型 ID 和源文件顺序排列。
- 该顺序用于展示。比较模型能力时，仍须核对版本、数据集、工具、推理档位、Harness 等实验条件。
- 未分类评测保留空的 `groups` 和原有 `unranked` 数组，按模型 ID 及模型文件中的记录顺序排列。

## 国际化

- `[model.descriptions]` 以模型 ID（`<lab>/<model-id>`）为键。
- `[benchmark.description]` 以 Benchmark 定义 ID 为键。
- 新增、修改、重命名或删除模型及定义时，同步处理受影响的描述翻译；为已有语言文件补齐新增描述，不编造或遗漏关键条件。
- 仅修改成绩等不影响描述的字段，无需改动本地化。仅新增参数量也不要求改译文。
- Models.dev 自动同步的描述保护及新模型翻译例外见[同步说明](models-dev-sync.md)。
