# AGENTS.md — ModelAtlas Data

ModelAtlas Data 是 [ModelAtlas Android](https://github.com/chenlongapps/model-atlas-android) 的 AI 模型数据仓库，基于 [Models.dev](https://github.com/anomalyco/models.dev) 格式维护资料和 Benchmark 成绩，不运行评测。

**准确性优先于完整性，简单性优先于复杂性。** 资料须有可靠依据；未知的可选字段省略，不编造、不猜测。仅修改与任务相关的内容，保留有效的来源、条件和注释。

## 目录

- `models/<lab>/<model-id>.toml`：一个模型一个文件，成绩的唯一人工维护来源。
- `benchmarks/`：Benchmark 定义，一个评测一个 TOML，不重复维护成绩。
- `benchmark-results/`：构建生成并随仓库提交的成绩汇总。按 Benchmark ID 写 TOML，未能唯一匹配定义的成绩按原评测名称写入 `uncategorized/`，全部从模型源文件派生。
- `i18n/`：按语言维护模型和 Benchmark 描述。
- `dist/`：生成的 JSON；不得直接修改，应修改源数据后重新构建。
- `scripts/`：校验和构建工具；只在实际需要时添加工具。

部分目录或工具可能尚不存在，不要假设它们已经创建。

## 工作流程

1. 检查已有模型、成绩及相关 Benchmark 定义，确认身份和版本。
2. 核实来源、成绩、评测条件和许可，检查重复与冲突。
3. 修改源文件；不要无故重写结构、批量重命名或新增数据库等复杂工具。
4. **同步 Benchmark 成绩汇总。** 新增、修改或删除模型成绩时，先更新 `models/<lab>/<model-id>.toml` 中的 `[[benchmarks]]`，再运行 `python3 scripts/build.py` 重新生成 `benchmark-results/`，并用 `python3 scripts/validate.py --check-results` 检查汇总与源数据是否一致。将受影响的汇总 TOML 纳入同一次变更（包括 `uncategorized/`）；不要手工编辑汇总。若无法重建或校验，须报告原因及尚未同步的范围。
5. 按下文处理本地化、上游同步、校验和报告。

## 模型数据

- 新增前检查 Models.dev，确认研发机构和规范 ID；合法复用时优先采用上游结构。不同版本不得合并，名称相似不代表同一模型。
- 尽可能遵循 [Models.dev v2 Schema](https://github.com/anomalyco/models.dev/blob/dev/packages/core/src/schema-v2.ts)，参考[上游模型文件](https://github.com/anomalyco/models.dev/tree/dev/models)。使用 `schema = 2`，ID 由路径确定，例如 `models/deepseek/deepseek-r1.toml` 对应 `deepseek/deepseek-r1`，无需额外的 `id`。
- 不擅自修改上游字段的名称、类型或语义；新增 ModelAtlas 专有字段前须明确设计和兼容策略。
- 区分模型固有属性与 Provider 特有的能力、价格、缓存和推理档位；不得根据上下文窗口推算最大输入长度。

### 参数量

使用 `[metadata.modelatlas.parameters]`，详见 [README 参数量规范](README.md#模型参数量)及[组件兼容策略](README.md#组件参数量及兼容策略)。

- `total_billion`（完整模型总量）和 `active_billion`（每 token 激活量）单位为 B，须为有限正数；有数值时 `sources` 须为非空 HTTP(S) URL 数组，可选 `notes`。
- 可选 `components` 表数组单独记录组件：`name` 非空且唯一，至少一个上述数值字段及独立 `sources`，可选 `notes`，不得嵌套。参数表至少包含一项可核实的完整模型或组件数值。
- 不从名称推断参数，不将组件或有效参数量冒充完整总量或激活量，不汇总组件填入父表。
- 人工或 AI 辅助新增、更新 `open_weights = true` 的模型时，主动查阅对应版本的官方模型卡、论文或技术资料，尽可能补齐完整模型的总量和激活量，不要只更新标记和下载链接。两项分别核实并附来源；无法核实的字段省略并报告，不填零、不猜测，也不默认二者相等。示例见 [Kimi K3.1 Pro](models/moonshotai/kimi-k3.1-pro.toml)，其数值仅适用于该模型。

## Benchmark 成绩

成绩保存在模型文件的 `[[benchmarks]]` 表数组中，`name`、`score` 必填；按来源填写 `metric`、`version`、`dataset`、`effort`、`variant`、`harness`、`source` 和 `date`，尽可能提供可验证的来源 URL。

- **原始成绩：** 保留数值精度、评测名称和已知条件；不得推算成绩、将缺失值填为 `0`、将不同评分指标转换为相同指标或将宣传描述当作量化结果。
- **评测条件：** 不同版本、数据集、指标、推理预算、工具使用、Harness、来源或实验设置的成绩分别保留，不只选最高分；未说明的条件不假定默认值。
- **无法核实或表达：** 无法核实的成绩跳过并说明原因；Schema 无法准确表达关键条件时，不塞入无关字段，保留来源并报告限制。
- **判重：** 检查模型 ID、名称、版本、指标、数据集、`effort`、变体、Harness、来源和日期，不能只凭名称和分数判重。`effort` 按原字符串参与判重，缺失不等于任何显式档位（包括 `"default"`）；相同条件下的重复或冲突均须报告。
- **冲突：** 检查评测条件、模型更新和结果修订；不得无依据地覆盖或自动采用高分。无法确认时保留已有记录并报告；确认是同一记录的官方修正时可更新并说明依据。

### 推理档位与成本

- `effort` 是可选非空字符串，原样记录来源中的官方推理档位名称和大小写，不限制枚举；未说明则省略，不设置默认值。`variant` 继续记录工具使用、重复次数等其他条件；不自动解析或迁移旧 `variant`。
- `cost`（有限非负数）和 `cost_unit`（包含币种及口径的非空字符串）必须成对提供。可选 `cost_source` 为独立的 HTTP(S) 成本来源，否则使用 `source`；详见 [README 成本规范](README.md#benchmark-成绩的成本)。
- 只补充同一模型版本、档位、Harness、来源和实验条件下的已核实成本；不推算、不将缺失或显示舍入值填零，不混用每任务、加权每任务、每测试和整次评测总成本。成本及其溯源字段不参与成绩身份判重。
- `effort`、`cost`、`cost_unit` 和 `cost_source` 是 ModelAtlas 扩展，不代表严格的上游 Schema 已支持，对接严格上游消费者时须显式处理。旧记录保持兼容，JSON 构建原样保留字段及缺失状态；自动同步保留已有成绩和成本。

## Benchmark 定义与排行榜

- **仅用户明确要求或确认后才能新增定义。** 优先复用已有定义；缺少定义时仍可保留已核实的原始成绩并报告未映射情况，不为消除构建警告或补齐分项创建定义。
- `benchmarks/` 是 ModelAtlas 专有定义，不是 Models.dev 模型 Schema。须包含稳定唯一的 `id`、正式 `name`、`version`、`category`、`metric`、`unit` 和 `higher_is_better`，需要时补充描述、来源和方法。
- 不猜测版本、指标、单位或评分方向，不将综合指数标为单一能力测试；规则不兼容的版本分别定义。构建按名称、版本和必要的指标信息映射成绩；不明确时报告。
- 排行榜是派生数据：按版本、指标和测试条件划分可比组，排除可比性无法确认的成绩，再按正确方向排序。不混合不兼容的版本、数据集、工具或环境，不自动选最高分、不将缺失成绩视为零，不将本地排名称为官方完整排名。条件不足时保留原始成绩，不强制排名。
- 汇总同时生成 `benchmark-results/` TOML 和 `dist/benchmark-results.json`。每条结果使用 `model_id` 关联模型，`result` 保留整条原始记录。每个已定义评测按 `higher_is_better` 排列数值成绩，同分按模型 ID 排序，字符串分数置后。顺序用于展示，可比性仍需按实验条件判断。`uncategorized/` 沿用原有顺序。修改模型或定义源文件后重建并提交生成的 TOML。详见[成绩汇总规范](docs/data-format.md#benchmark-成绩汇总)。

## 国际化

`i18n/<语言>.toml` 的 `[model.descriptions]` 以模型 ID（`<lab>/<model-id>`）为键，`[benchmark.description]` 以 Benchmark 定义的 `id` 为键。

新增、修改、重命名或删除模型及 Benchmark 定义时，同步新增、更新、迁移或删除受影响的本地化条目；新增有描述的模型或定义时，为已有语言文件补充翻译。翻译须符合源数据及已核实事实，不编造或遗漏关键条件；无法准确翻译时报告。仅修改成绩等不影响描述的内容时无需改动本地化。Models.dev 自动同步的例外见下节。

## 上游同步

- 同步前比较差异；无法确认的冲突或 Schema 不兼容须报告，不得自动合并。除下述规则外，不覆盖已验证的本地补充。
- Models.dev 自动同步可导入基本字段合法的新模型，并仅保留校验通过且能唯一匹配现有定义的 Benchmark 成绩。无法映射或不合法的成绩逐条跳过并报告，不猜测版本或指标，不创建定义；不改动已有模型的 Benchmark。已有模型的基本字段跟随上游当前明确提供的值，不依赖旧上游基线；上游缺失的字段、本地独有补充和已有成绩保留。
- 新模型保留上游原文描述，按 Index-Translate → deep-translator（Google）→ Argos Translate 顺序尝试简体中文翻译，不覆盖已有本地化条目。全部失败仍导入原文并报告，后续人工补齐，不自动补翻已有模型。
- 已有模型的描述若存在本地化条目，自动同步须保留旧描述并报告，待人工同步翻译后再更新。其他新增和修改仍遵循上述国际化规则。
- Models.dev 自动同步工作流先核对暂存的模型和翻译，再重新生成、校验并暂存汇总 TOML，和本次源文件变化一起提交。

## 校验与报告

每次修改 TOML 后优先运行仓库已有校验脚本，至少检查语法、模型路径、`schema`、字段类型、Benchmark 必填字段、重复成绩、来源与结果是否对应，以及定义映射是否存在且无歧义。修改本地化 TOML 时还须检查键与源数据的对应关系，以及翻译与描述的一致性。

```sh
python3 scripts/validate.py  # TOML 语法
python3 scripts/build.py     # 结构、映射和 TOML / JSON 构建
python3 scripts/validate.py --check-results  # 检查生成的 TOML 是否与源数据一致
```

也可使用 Python 3.11+ 的 `tomllib` 做基础解析；语法检查不等于 Schema、来源或真实性验证。具体检查范围见 [README](README.md#数据校验)。

数据收集任务完成后简短报告：修改的模型文件、新增和修正的成绩数量、新建的 Benchmark 定义、主要来源 URL、实际执行的校验及结果，以及跳过的成绩、未解决的冲突、需人工核实的来源和许可问题。不得声称未执行的校验已通过。
