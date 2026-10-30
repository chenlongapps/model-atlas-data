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

## 数据校验

需要 Python 3.11+，无需安装第三方依赖。在仓库根目录运行：

```sh
python3 scripts/validate.py
```

脚本递归检查 `models/`、`benchmarks/`、`i18n/` 中的 `.toml` 文件，报告所有解析错误及其位置，并汇总成功和失败数量。从其他目录运行时，使用脚本的绝对路径即可。

全部通过返回退出码 `0`；存在语法、编码、读取错误或未找到任何 TOML 文件时返回 `1`。此脚本仅检查 TOML 语法，不校验 Schema、字段类型、成绩重复、来源真实性或本地化对应关系。

运行脚本测试：

```sh
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

## 自动同步新增模型

`.github/workflows/sync-models.yml` 每小时第 17 分钟运行，也可在 GitHub Actions 手动触发。它从 [Models.dev 的 `dev` 分支](https://github.com/anomalyco/models.dev/tree/dev/models) 拉取研发机构级 `models/` 数据，并直接提交本仓库默认分支；不创建 PR。需要允许 `GITHUB_TOKEN` 写入仓库，且默认分支保护规则允许机器人推送；推送被拒绝或分支并发更新时任务失败，不强推或自动变基。

- 只原样新增本地不存在的 `models/<lab>/<model-id>.toml`。已有路径完全跳过，包括本地补充的成绩和注释；上游修改、删除不会同步。首次运行也会补齐上游已有但本地缺少的模型。
- 不同步 Provider 数据，不修改 `benchmarks/`、`i18n/`、`dist/`；目前暂不补充翻译。上游重命名会被视为新路径，旧路径继续保留，不自动判断模型别名。
- 新模型检查 TOML、路径、Schema 版本、主要字段类型、成绩必填字段、重复及冲突记录、来源 URL，以及 Benchmark 定义映射。映射必须精确匹配名称、显式版本和指标，不推断默认条件；不兼容的整个模型跳过，并在运行摘要中报告。未知字段也跳过，等待人工审查兼容性。
- 这些是保守的导入检查，不等同于完整 Models.dev Schema 校验，也不会联网核验每项成绩的原始来源或自动生成 Benchmark 定义、排行榜。
- 提交前检查暂存区：只能包含本次新增模型，内容哈希须与同步报告一致，禁止修改、删除或额外文件。有新增才提交；摘要和提交信息记录上游 commit SHA。
- 上游仓库使用 MIT 许可，声明保留于 [`LICENSE.models-dev`](LICENSE.models-dev)。许可文本变化时停止同步，等待人工审查；模型权重本身的许可仍以对应模型资料为准。

本地预览（需要自行准备上游 Git checkout；报告建议写到仓库外）：

```sh
python3 scripts/sync_models.py sync --upstream /path/to/models.dev --report /path/to/sync-report.json --dry-run
```
