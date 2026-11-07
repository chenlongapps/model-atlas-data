# ModelAtlas Data

ModelAtlas Data 是 [ModelAtlas Android](https://github.com/chenlongapps/model-atlas-android) 的 AI 模型数据仓库，专注于收集、整理和维护 AI 模型的 Benchmark 评测成绩，并逐步扩展模型相关信息。

项目以 [Models.dev](https://github.com/anomalyco/models.dev) 的模型数据结构为基础，采用 **TOML** 维护模型档案，通过人工制定规范与 AI Agent 辅助收集数据，最终生成适合应用使用的 JSON 数据集。

## 项目目标

- **模型档案**：以模型为中心组织数据，每个模型对应一个独立的 TOML 文件。
- **Benchmark 收集**：整理模型在不同评测项目、版本及测试条件下的成绩。
- **AI 辅助维护**：通过 AI Agent 搜索公开资料、提取成绩并补充模型档案。
- **Benchmark 排名**：以评测项目为中心汇总成绩，生成满足可比性要求的排行榜。
- **数据分发**：将 TOML 源数据转换为 JSON，供 ModelAtlas Android 使用。
- **可追溯性**：保留成绩来源及评测条件，便于核实和后续维护。

## 模型参数量

参数量使用上游允许的 `metadata` 扩展点，不新增顶层字段、不改变 `schema = 2`：

```toml
[metadata.modelatlas.parameters]
total_billion = 671
active_billion = 37
sources = ["https://github.com/deepseek-ai/DeepSeek-R1"]
```

- `total_billion`：完整模型总参数量；`active_billion`：来源明确披露的每 token 激活参数量。单位均为十亿（B），必须为有限正数；二者同时存在时必须口径一致，激活量不超过总量。没有完整模型数值时可以仅提供下述组件记录。
- `sources`：支持数值及统计口径的非空 HTTP(S) URL 数组，不重复；`notes`：可选非空字符串，说明近似精度、统计范围或其他关键限制。
- 只采用与该模型版本对应的模型卡、论文、官方技术资料等可靠依据；不从名称、文件体积、量化位宽或专家数推算。350M 可以仅换算单位记为 `0.35`，不补造数值精度。
- 未知值省略，不填零；稠密模型不自动补激活量。多模态模型仅披露语言骨干或生成主干时，不冒充完整模型总量；不同组件、有效参数量与每 token 激活量也不混用。近似值须在 `notes` 中注明。
- 模型卡未披露完整总量时，可核对对应未量化完整检查点的 Hugging Face 公共 API `safetensors.parameters` / `safetensors.total`，仅换算已发布的数值，并在 `notes` 明示为 Hub 权重统计。须检查版本、完整性、数据类型及统计自洽性；不将量化打包后的元素数、仅骨干或仅适配器的统计当作完整总量，不汇总不同格式、检查点或组件。整数位置索引等非参数张量不计入参数量；API 统计互相矛盾时，不直接采用任意一项。
- 可独立核验固定 commit 的实际张量描述元数据，按真实浮点权重形状逐项计数，并检查全部分片与索引一一对应；这不是从层数、名称、字节数或量化位宽估算。`notes` 必须说明为独立检查点计数及范围，`sources` 指向固定版本的文件或分片索引。仅明确核实的组件也可采用此方法，但仍只能写入组件。PyTorch ZIP 仅用受限、惰性的描述解析器，不运行任意 pickle 对象、不调用不受限的 `torch.load`；无法安全解析、存在未解释的共享存储、缓冲区或分片缺失时跳过并报告。复核方法及 API 冲突处理见[核验报告](docs/model-parameters.md)。
- 官方架构统计、名义规模和序列化权重统计可能采用不同口径；保留来源精度和已知条件，不强制统一或据此生成参数量排名。独立发布的可选草稿模型、适配器或其他格式不与目标检查点相加。推理阶段不同的激活量须在 `notes` 中说明，不能将预填充和解码混为一个无条件数值。
- 此表整体可省略，旧记录保持有效；存在此表时，须提供至少一个有来源的完整模型数值或组件数值，不允许只用说明文字凑覆盖率。开放权重范围以源文件的 `open_weights = true` 为准，不因参数量缺失而改动该标记，也不替未确认版本填值。
- 这是 ModelAtlas 的 metadata 语义约定，不是上游标准参数字段；上游 Schema 接受 JSON metadata，本仓库的构建和同步额外校验上述约定。JSON 原样保留数值及字段缺失状态；上游未提供的本地 metadata 在同步时保留，若上游明确提供同路径字段，仍按基本信息同步规则处理，不作永久锁定。
- 本次来源核验与未补全项见 [`docs/model-parameters.md`](docs/model-parameters.md)。参数量不影响模型描述，未修改描述时无需调整本地化。

### 组件参数量及兼容策略

`components` 是参数表的可选表数组，每项记录一个明确命名、范围已核实的组件。每项 `name` 为来源中的非空组件名称（同一模型内不可重复），`total_billion` / `active_billion` 至少一个，正数及单位规则与完整模型相同；每项必须有自己的 `sources`，可选 `notes` 说明口径。组件不允许嵌套。不自动将组件相加、从整模型数值倒推出组件大小，或将未知部分视为零；组件可能重叠，也可能只是整条管线的一部分。只有组件记录时，父表不必重复 `sources`，但不能补出父表总量。

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

这是增量 metadata 扩展：原有完整总量、激活量及缺失状态的语义不变，旧记录无需迁移。只读取父表数值的旧消费者仍会得到“完整总量未知”，不得以首个组件或组件之和作为回退。支持组件的新消费者应单独展示组件名称、数值及范围，不与整模型总量混排。JSON 构建原样保留数组顺序和来源；自动同步在上游未明确提供该路径时保留本地组件数组。严格的 ModelAtlas 消费者需显式支持新字段；Models.dev 的通用 JSON metadata 扩展点无需改变。

## Benchmark 成绩的推理档位

模型文件的 `[[benchmarks]]` 支持 ModelAtlas 扩展字段 `effort`：

```toml
[[benchmarks]]
name = "Example Bench"
score = 42.1
effort = "xhigh"
variant = "without tools"
```

- `effort` 是可选非空字符串，原样保留来源中的官方档位名称和大小写，不限制枚举；例如 `"xhigh"`、`"Adaptive/Max"` 都可使用。
- 来源未说明档位时省略，不设置默认值、不根据模型名推断。`variant` 继续保存其他评测条件。
- 没有 `effort` 的旧记录仍然有效；不会自动解析或迁移旧 `variant`。构建 JSON 和自动同步均保留原值及缺失状态。
- 判重包含 `effort`：不同档位或未注明档位分别保留，缺失不等于 `"default"`。条件相同而分数相同或不同均报告重复或冲突，不自动选择高分。定义映射仍只按名称、版本和指标进行。
- 此字段是本仓库扩展，不代表 Models.dev 的严格 Schema 已支持；向严格遵循上游 Schema 的消费者传递数据时，需先显式处理（如移除）此扩展字段。

## Benchmark 成绩的成本

`[[benchmarks]]` 支持 ModelAtlas 扩展字段 `cost`、`cost_unit` 和 `cost_source`：

```toml
[[benchmarks]]
name = "Example Bench"
score = 42.1
cost = 1.25
cost_unit = "USD/task"
source = "https://example.com/results"
```

- `cost` 为有限非负数，必须与非空字符串 `cost_unit` 成对提供；缺失不填零。只有来源明确报告真实零成本时才记录 `0`，不能将四舍五入为 `$0.00` 或无定价的占位零当作真实零。
- 单位包含币种及计费口径，保留来源含义，如 `USD/task`（平均每任务）、`USD/test`（来源的 Cost / Test）、`USD/weighted task`（按评测权重加权的每任务成本）、`USD/evaluation`（整次评测总成本）。不换算币种、不根据 API 单价或任务数推算；总成本须保留任务数和重复次数等已知条件或注释。
- 成本属于该条评测结果，不是模型固有属性或 Provider token 单价。必须核对模型版本、档位、Harness、数据集及实验设置；相同模型在不同来源的成绩不能互相套用成本。重定价及缓存等已知口径应保留在注释中。
- `cost_source` 为可选 HTTP(S) URL，用于成本的独立来源；省略时由 `source` 提供依据。提供成本时至少须有一个有效来源，成本来源与成绩来源不同不能据此忽略实验条件差异。
- 旧记录保持兼容；构建原样保留数值、单位、来源和缺失状态。成本及其单位、溯源不参与成绩身份判重，不能用不同成本掩盖重复或冲突的成绩。
- 这些字段与 `effort` 一样不是上游严格 Models.dev Schema 的字段；对接严格上游消费者时须显式处理（如移除）。自动同步不覆盖已有成绩及其成本。

## 数据校验

需要 Python 3.11+，无需安装第三方依赖。在仓库根目录运行：

```sh
python3 scripts/validate.py
```

脚本递归检查 `models/`、`benchmarks/`、`i18n/` 中的 `.toml` 文件，报告所有解析错误及其位置，并汇总成功和失败数量。从其他目录运行时，使用脚本的绝对路径即可。

全部通过返回退出码 `0`；存在语法、编码、读取错误或未找到任何 TOML 文件时返回 `1`。此脚本仅检查 TOML 语法，不校验 Schema、字段类型、成绩重复、来源真实性或本地化对应关系。

运行脚本测试：

```sh
python3 -m pip install -r requirements-sync.txt
python3 -m unittest discover -s tests -v
```

## JSON 构建

同样使用 Python 3.11+，无需第三方依赖：

```sh
python3 scripts/build.py
```

默认读取脚本所在仓库的源数据并生成以下文件（`dist/` 不提交 Git）：

```text
dist/
  models.json         # { "<lab>/<model-id>": { ...模型字段... } }
  benchmarks.json     # { "<benchmark-id>": { ...定义字段... } }
  i18n/
    zh-CN.json        # 保留 model.descriptions / benchmark.description 表结构
```

- 不增加顶层 `version`、内嵌翻译、派生 `results` 或排行榜。模型保留 `schema`，Benchmark 的 `id` 作为对象键，不在定义内部重复。
- 保留其余源字段（包括未知但可转换为 JSON 的字段）、成绩条件、来源、数组顺序和缺失状态；不补默认值、不合并成绩、不选择最高分。JSON 不保留 TOML 注释或数字的书写形式，如 `42.10` 可能输出为 `42.1`，不会主动取整或重评分。
- 检查 TOML、模型路径、`schema = 2`、主要字段类型、成绩的 `name`/`score`、重复或冲突记录、已有来源 URL 的格式、Benchmark 定义必填字段及唯一 ID、本地化表结构与键引用。未知本地化 ID、无效类型等错误使构建失败，返回 `1`。
- 成绩与定义按名称、显式版本和指标精确匹配。未匹配或存在歧义的数量、缺失的来源或现有语言中的描述翻译仅作为警告报告，构建仍返回 `0`；不推断版本、指标或默认条件，不丢弃原始成绩。没有任何有效模型时失败；`benchmarks/`、`i18n/` 可以暂缺。
- 使用 UTF-8、稳定键排序和末尾换行，相同源数据生成相同内容。拒绝 NaN、Infinity 及不能直接转换为 JSON 的 TOML 日期/时间值；日期字段应使用源格式要求的字符串。
- 全部校验、序列化和临时文件写入成功后才逐文件原子替换产物；这不是整个目录的事务，替换阶段的 I/O 故障可能留下部分更新，应修复后重跑。不会清空输出目录或删除无关文件；若存在已无对应源文件的 `i18n/*.json`，需先手动移走旧产物。

这些检查不等于完整 Models.dev Schema 校验，也不会联网核验来源内容、评测真实性或翻译语义。修改后的测试仍使用上面的 `unittest` 命令运行。

支持从其他目录运行，以及指定源仓库和输出目录；显式传入的相对路径相对于当前工作目录：

```sh
python3 /path/to/model-atlas-data/scripts/build.py --root /path/to/model-atlas-data --output /path/to/output
```

## Web Explorer 与 GitHub Pages 数据发布

Web Explorer 是数据集的轻量静态浏览入口，默认地址为 <https://chenlongapps.github.io/model-atlas-data/>（需先成功部署）。界面参考 Models.dev，Models 和 Benchmarks 分别提供搜索、筛选、表格排序、详情与双向导航；顶部搜索支持 `Ctrl+K` / `⌘K`。界面支持简体中文和英文，可在顶部切换并在浏览器允许时记住选择；首次使用浏览器语言，不支持时回退英文。中文描述优先使用现有翻译，缺失时回退原文；英文显示原文，原始数据未必均为英文。成绩逐条保留原始条件及来源，不提供未经可比性验证的排名。评测详情按定义的 `higher_is_better` 将成绩由好到差展示（评分方向未知时保留原顺序），`effort` 单独成列，未注明时显示 `—`；此展示顺序不代表不同测试条件下的成绩可比较。关联只采用名称、显式版本和指标的精确唯一匹配，未匹配的成绩仍在模型详情中显示。

网站直接读取同一发布目录的 JSON，不修改数据或 Android 所用结构。`.github/workflows/pages.yml` 复用上述测试、校验和构建命令，通过官方 Pages Actions 同时发布网页和 JSON；不提交 `dist/`。发布包包含本次构建的 JSON、`manifest.json`、网页资源和上游许可声明 `LICENSE.models-dev`；使用全新的临时输出目录，避免发布历史产物或仓库中的其他文件。网页资源不加入 manifest，也不影响 `data_version`。

Benchmark 详情页的交互式散点图采用通栏画布、弱水平网格和按研发机构固定配色的散点，支持按评测成本或模型发布日期观察原始分数分布。机构图例位于图下：点击后仅展示该机构的模型，并自动标注全部可见模型及原始档位；再次点击当前机构或“显示所有机构”恢复全部。机构选择仍遵守当前成本口径、档位及条件筛选，不混合缺少坐标的记录。档位和相同条件组收在“筛选”中；搜索只突出显示模型。一个点对应一条成绩，重合坐标可查看全部记录，前沿点及聚焦机构时分别标注重合点中的不同模型名称及档位，不以“+N”代替前沿模型名；悬停或键盘聚焦显示悬浮详情卡，点击或 Enter 固定，方向键切换数据点，Escape 或关闭按钮清除选择。总览模式完整标注前沿模型，并优先标注搜索命中和选中点；前沿与机构聚焦标注不使用总览的标注数量上限，必要时增加绘图区高度。标注避让并按需加引导线，不移动数据坐标；过长名称可截断，完整记录仍可查看。筛选只影响图表，不删改下方原始成绩表。无成本时默认使用模型 `release_date`，不是成绩日期。

- 成本轴要求精确一致的 `cost_unit`，不同币种、每任务、每测试、加权每任务和整次评测不混合、不换算；缺失值不填零。图表坐标和详情使用原始精度，不采用表格舍入值。字符串成绩（例如带置信区间或舍入说明的原文）不自动解析成数值，只在原始成绩表展示，并计入图表缺少有效坐标的数量。
- 成本默认使用对数刻度，可切换为线性；当前展示记录中存在真实零成本时自动回退线性并明确提示，不删零、不以任意极小值代替。对数仅影响屏幕映射，不改原始数值、支配关系或前沿成员。货币刻度保留小数精度，轴标题仍显示完整成本口径。发布日期使用线性时间轴。
- 成本模式的象限和帕累托前沿默认开启，可手动关闭；不满足各自绘制条件时禁用。象限以当前展示记录的成本和分数中位数划分，浅绿表示相对低成本、强成绩，浅灰表示相对高成本、弱成绩；强弱方向遵循 `higher_is_better`，不是官方阈值。分界值在图下标明，带 `≈` 的简写可悬停查看完整数值；底色边界按未舍入的中位数定位。
- 帕累托前沿只在有来源依据的可比组内显示，不将字段相同、条件缺失或来源同域名视为可比证据。总览自动识别符合协议且至少含两个模型的组，分别计算和绘制前沿，不因混入其他条件记录而整体禁用，也不跨组判断支配关系或连线；多组使用不同虚线样式，图下列出各组及未参与前沿的记录数，点击组图例可单独查看。目前仅支持 [DeepSWE 1.1 官方协议](https://deepswe.datacurve.ai/blog/deepswe-v1-1) 下明确注明相同档位、`mini-swe-agent`、113 个任务、4 次完整运行且全部 452 次尝试均评分的精确条件组；还要求成绩来源和所有其他条件相同，不纳入部分尝试、不同文本条件或未知扩展条件。依据与成本口径见[收集报告](docs/benchmark-costs-2026-11-06.md)。其余记录保留分布图，没有可用组时明确显示原因；后续协议须单独核实后显式支持，不自动推断。
- 虚线折线仅连接各组内的非支配观测点，不平滑，不代表插值模型、官方完整前沿或统计显著优势；同成本同分数的记录均保留并分别标注名称。前沿仅有一个坐标时显示外圈标记及模型名，不虚构线段。搜索只突出显示，不重算前沿；机构或条件筛选会重算。发布日期模式不展示成本象限或前沿。数据与可比性说明默认折叠，可随时展开。
- 卡片底部显示样本量、被筛除或缺少坐标的记录数及来源；时间仅采用 manifest 的数据包生成时间，没有该字段时标明不可用，不冒充评测更新时间。图表不改变原有数据的来源或再分发许可限制。

本地预览（Python 3.11+，无需第三方依赖）：

```sh
python3 scripts/preview.py
```

浏览 <http://127.0.0.1:8000/>，按 `Ctrl+C` 停止。可用 `--port 端口号` 指定端口，`--port 0` 自动选择可用端口。脚本构建当前源数据并在临时目录中提供网页和数据，退出时清理；仅监听本机，不生成 manifest，因此页面显示发布信息不可用。如需生成完整 manifest，使用下方发布包命令，源数据相关文件须先提交。网页测试使用 Node.js（20+）：

```sh
node --test tests/web.test.mjs
```

首次启用：

1. 在仓库 **Settings → Pages → Build and deployment → Source** 中选择 **GitHub Actions**。
2. 确认 **Settings → Environments → github-pages** 的部署规则允许默认分支；如需审批，需批准部署后才会发布。
3. 在 **Actions → Deploy data to GitHub Pages → Run workflow** 中选择默认分支并运行。部署成功后可从该次运行的 `github-pages` 环境链接查看站点地址。

此仓库默认地址下的数据端点为（如配置自定义域名，以部署输出地址为准）：

```text
https://chenlongapps.github.io/model-atlas-data/models.json
https://chenlongapps.github.io/model-atlas-data/benchmarks.json
https://chenlongapps.github.io/model-atlas-data/i18n/zh-CN.json
https://chenlongapps.github.io/model-atlas-data/manifest.json
https://chenlongapps.github.io/model-atlas-data/LICENSE.models-dev
```

`manifest.json` 描述本次发布包：

- `schema_version`：manifest 格式版本，当前为整数 `1`。
- `git_commit`：构建时实际检出的完整 Git 提交 ID，不一定是触发工作流的提交。
- `published_at`：UTC 时间，格式为 `YYYY-MM-DDTHH:MM:SSZ`；表示生成发布包的时间，而非部署完成时间。
- `files`：以相对于 manifest 的路径为键，列出 `models.json`、`benchmarks.json`、所有构建的 `i18n/*.json` 和 `LICENSE.models-dev`；每项包含文件实际字节的 `sha256`（小写十六进制）和 `size`（字节数）。manifest 不包含自身。
- `data_version`：`sha256:` 加上 `files` 对象规范化后的 SHA-256 摘要。规范化使用 UTF-8 编码 JSON、按键排序、不转义非 ASCII 字符、无多余空格（Python 的 `json.dumps(files, ensure_ascii=False, sort_keys=True, separators=(",", ":"))`），不添加换行。同一文件清单和内容得到相同版本；Git 提交或生成时间变化不影响版本。

本地生成完整发布包（须先提交相关源码，且输出目录应为全新目录）：

```sh
python3 scripts/build.py --output /path/to/release
cp LICENSE.models-dev /path/to/release/LICENSE.models-dev
python3 scripts/manifest.py --output /path/to/release
cp -R web/. /path/to/release/
```

manifest 脚本支持 `--root` 指定 Git 仓库，`--output` 默认为 `<root>/dist`；相对路径相对于当前工作目录。它拒绝相关模型、定义、本地化、构建脚本、manifest 脚本或许可文件存在未提交更改，检查输出 JSON 清单和许可文件，并先完成校验再原子替换 manifest。脚本不会自行重建或证明已有 JSON 确实由当前提交生成，因此应紧接构建步骤执行；Pages 工作流使用干净检出和全新输出目录。校验值用于检测文件是否一致，不提供签名或来源真实性保证。

自动发布规则：

- `main` 分支的模型、Benchmark 定义、本地化、网页资源、构建、manifest 或校验脚本、测试、上游许可及 Pages 工作流变更时触发。若将默认分支从 `main` 改名，需同步修改工作流中的 `push.branches`。
- `Sync new Models.dev models` 工作流成功完成后触发，即使没有新增模型也会重建。同步使用 `GITHUB_TOKEN` 推送，不会触发普通 `push` 工作流，因此单独使用 `workflow_run` 衔接；更改同步工作流的 `name` 时也须更新此引用。
- 支持手动触发，但只允许默认分支部署；同步完成事件还须来自本仓库的默认分支。各入口均检出默认分支的最新代码，不下载或执行同步运行的产物；排队期间有新提交时，实际构建版本可能晚于触发版本，以 checkout 日志为准。
- 发布串行执行，不取消进行中的发布。测试、校验或构建失败时不部署，保留此前已发布的数据。构建仅有仓库读取权限，部署任务单独授予 `pages: write` 和 `id-token: write`，无需个人访问令牌。

失败时先查看 Actions 中失败步骤：数据或测试失败时修正源文件后重试；Pages 配置、权限或环境审批失败时检查上述仓库设置。现有构建警告仍不阻止发布，不代表成绩来源和翻译已通过人工核验。该工作流只服务发布，不替代面向 PR 的通用 CI。

## 自动同步模型

`.github/workflows/sync-models.yml` 每小时第 17 分钟运行，也可在 GitHub Actions 手动触发。它从 [Models.dev 的 `dev` 分支](https://github.com/anomalyco/models.dev/tree/dev/models) 拉取研发机构级 `models/` 数据，并直接提交本仓库默认分支；不创建 PR。需要允许 `GITHUB_TOKEN` 写入仓库，且默认分支保护规则允许机器人推送；推送被拒绝或分支并发更新时任务失败，不强推或自动变基。

- 新模型完整导入：原样新增本地不存在的 `models/<lab>/<model-id>.toml`，包括上游 `benchmarks`。首次运行也会补齐上游已有但本地缺少的模型。
- 已有模型仅对比、更新基本信息；上游成绩不参与更新和成绩校验，本地 `benchmarks` 的值、字段缺失状态、原始精度、格式及区块注释保持不变。没有本地成绩的已有模型也不会自动补入上游成绩。
- 基本信息以上游明确提供的值为准：已有字段不同则更新，缺少的字段则补充，不再依赖旧上游版本或把历史漏同步视为本地冲突。字典逐字段合并，数组作为完整字段比较；上游缺失的字段、本地独有补充及上游已删除的模型均保留，不自动判断别名。已有翻译的描述仍按下面的保护规则处理。
- 不同步 Provider 数据，不修改 `benchmarks/`、`i18n/`、`dist/`；目前暂不补充翻译。上游重命名会被视为新路径，旧路径继续保留，不自动判断模型别名。
- 已有模型的描述若存在本地化条目，则保留旧描述并报告待人工同步翻译；其他无冲突的基本信息仍可更新。新增模型的翻译继续后续人工补齐。
- 新模型检查 TOML、路径、Schema 版本、主要字段类型、成绩必填字段、重复及冲突记录、来源 URL，以及 Benchmark 定义映射。映射必须精确匹配名称、显式版本和指标，不推断默认条件；不兼容的整个模型跳过，并在运行摘要中报告。未知字段也跳过，等待人工审查兼容性。
- 这些是保守的导入检查，不等同于完整 Models.dev Schema 校验，也不会联网核验每项成绩的原始来源或自动生成 Benchmark 定义、排行榜。
- 已有模型更新前检查本地、上游及合并后的基本字段，不重新校验或规范化已有成绩。使用 `tomlkit` 保留本地注释和格式，并复查仅预期字段变化、成绩文本未变；无法安全编辑时跳过并报告。
- 提交前检查暂存区：只允许报告中的新增模型和基本信息更新，逐一检查内容哈希；更新模型还须匹配更新前哈希，并独立确认成绩值和文本未变。禁止删除、重命名或额外文件。有新增或更新才提交；摘要记录更新字段和需要人工处理的翻译描述，提交信息记录上游 commit SHA。工作流名称保持不变以兼容 Pages 的 `workflow_run`。
- 上游仓库使用 MIT 许可，声明保留于 [`LICENSE.models-dev`](LICENSE.models-dev)。许可文本变化时停止同步，等待人工审查；模型权重本身的许可仍以对应模型资料为准。

本地预览（Python 3.11+；同步及其测试需要 `requirements-sync.txt` 中的依赖，校验、构建和网页预览仍仅使用标准库。需要自行准备上游 Git checkout，报告建议写到仓库外）：

```sh
python3 -m pip install -r requirements-sync.txt
python3 scripts/sync_models.py sync --upstream /path/to/models.dev --report /path/to/sync-report.json --dry-run
```

预览同时显示新增模型和已有模型的基本信息更新，不需要准备旧上游基线。确认差异后移除 `--dry-run` 才会写入；已有成绩始终不变。
