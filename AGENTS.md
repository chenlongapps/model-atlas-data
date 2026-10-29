# AGENTS.md — ModelAtlas Data

## 1. 项目概述

ModelAtlas Data 是 [ModelAtlas Android](https://github.com/chenlongapps/model-atlas-android) 的 AI 模型数据仓库。

项目以 [Models.dev](https://github.com/anomalyco/models.dev) 的模型数据格式为基础，使用 TOML 文件维护模型档案，重点收集、整理和验证 Benchmark 评测成绩。

AI Agent 的主要职责是：

- 搜索和核实模型及 Benchmark 公开资料。
- 补充、修正已有模型档案中的评测成绩。
- 根据需要创建新的模型档案和 Benchmark 定义。
- 保持数据结构一致、准确且可追溯。
- 协助验证数据并生成供 Android 使用的 JSON 数据。

**核心原则：准确性优先于完整性，简单性优先于复杂性。**

本项目是数据整理和展示项目，不负责实际运行模型评测。

## 2. 目录结构

目标目录结构：

```text
model-atlas-data/
├── models/                     # 模型档案，主要数据来源
│   ├── deepseek/
│   ├── openai/
│   └── anthropic/
│
├── benchmarks/                 # Benchmark 定义
│
├── dist/                       # 自动生成的 JSON 数据
│
├── scripts/                    # 校验和构建工具
│
├── AGENTS.md
└── README.md
```

上述目录为目标结构，不代表所有目录均已创建。

### 目录职责

**`models/`**

- 一个模型对应一个 TOML 文件。
- 包含模型基本资料、技术参数和 Benchmark 成绩。
- 是模型成绩的唯一人工维护来源。
- 按研发机构和模型标识组织文件。

**`benchmarks/`**

- 一个 Benchmark 定义对应一个 TOML 文件。
- 记录评测名称、版本、类别、指标及评分方向。
- 不重复维护模型成绩。
- 为后续成绩关联和排行榜生成提供依据。

**`dist/`**

- 存放构建生成的 JSON 数据。
- 不允许直接修改生成结果。
- 应通过修改源数据并重新构建来更新。

**`scripts/`**

- 保存数据校验、格式转换及构建脚本。
- 仅在实际需要时增加工具，不应提前创建复杂的处理框架。

## 3. 数据结构规范

### 3.1 模型文件

模型文件尽可能遵循 Models.dev v2 Schema。

参考：

- https://github.com/anomalyco/models.dev/tree/dev/models
- https://github.com/anomalyco/models.dev/blob/dev/packages/core/src/schema-v2.ts

文件路径：

```text
models/<lab>/<model-id>.toml
```

例如：

```text
models/deepseek/deepseek-r1.toml
```

其模型 ID 为：

```text
deepseek/deepseek-r1
```

模型 ID 由文件路径确定，不需要在 TOML 内添加 `id` 字段。

文件应使用：

```toml
schema = 2
```

不得随意修改 Models.dev 原有字段的名称、类型或语义。

如果未来需要扩展 ModelAtlas 专有字段，应先明确设计和兼容策略，不得由 Agent 擅自增加。

### 3.2 模型基础信息

模型基本信息沿用 Models.dev 的字段规范。

例如：

```toml
schema = 2
name = "Example Model"
description = "Example model description"
family = "example"
open_weights = false
release_date = "2026-01-01"

[modalities]
input = ["text"]
output = ["text"]

[capabilities]
tools = { supported = true }
reasoning = { supported = true }
temperature = true
top_p = true
top_k = true

[limit]
context = 128_000
output = 32_000
```

以上内容仅为结构示例，不代表真实模型。

注意：

- 模型资料必须具有可靠依据。
- 不得根据模型名称推测参数。
- 不得根据上下文窗口推算最大输入长度。
- 不得将不同 API 服务商的特定能力视为模型固有能力。
- 缺失的可选字段应直接省略。
- 不得使用虚构值填补缺失信息。

涉及 API 服务商特有的价格、缓存、推理档位等资料时，应注意 Models.dev 对模型与 Provider 数据的区分。

## 4. Benchmark 成绩规范

### 4.1 基本格式

模型 Benchmark 成绩使用 TOML 表数组：

```toml
[[benchmarks]]
name = "Example Benchmark"
score = 75.5
metric = "accuracy"
version = "1.0"
dataset = "full"
variant = "without tools"
harness = "Example Harness"
source = "https://example.com/results"
date = "2026-01-01"
```

这里的值只是格式示例。

Models.dev 已支持的字段包括：

| 字段 | 含义 |
|---|---|
| `name` | Benchmark 名称 |
| `score` | 原始成绩 |
| `metric` | 评分指标 |
| `version` | Benchmark 版本 |
| `dataset` | 测试集或子集 |
| `variant` | 评测配置 |
| `harness` | 执行环境 |
| `source` | 原始来源 URL |
| `date` | 评测日期 |

`name` 和 `score` 为 Models.dev Schema 的必需字段，其余字段按来源提供的信息填写。

正式收录时应尽可能提供可验证的 `source`。

### 4.2 成绩提取规则

Agent 必须遵循：

1. 只收集存在可靠证据的成绩。
2. 优先使用官方模型卡、技术报告和 Benchmark 官方结果。
3. 保留原始成绩的数值精度。
4. 保留原始评测名称和测试条件。
5. 不得根据其他模型成绩推算缺失结果。
6. 不得把没有公布的成绩填写为 `0`。
7. 不得将不同评分指标转换为相同指标。
8. 不得将模型的宣传性描述解释为量化成绩。

对于无法确认的成绩，直接跳过，并在任务总结中说明原因。

### 4.3 不同评测条件

同一模型在同一个 Benchmark 上可能存在多条成绩。

以下情况通常需要分别记录：

- 不同 Benchmark 版本。
- 不同测试数据集或子集。
- 不同推理等级或思考预算。
- 是否允许使用外部工具。
- 不同 Agent Harness。
- 不同评测指标。
- 不同评测来源或实验设置。

例如：

```toml
[[benchmarks]]
name = "Example Benchmark"
score = 45.2
variant = "low reasoning"
source = "https://example.com/low"

[[benchmarks]]
name = "Example Benchmark"
score = 52.8
variant = "high reasoning"
source = "https://example.com/high"
```

两条成绩必须独立保留，不得仅选取最高分。

如果现有 Schema 无法准确描述某个关键评测条件，不要强行写入无关字段。应保留来源并报告需要扩展 Schema 的原因。

### 4.4 禁止随意合并成绩

不得执行以下操作：

- 将不同版本的 Benchmark 成绩放入同一可比排名。
- 将使用工具和未使用工具的结果直接比较。
- 将不同数据子集的成绩视为完全等价。
- 将不同测试环境下的分数强行统一。
- 在来源不明确时假设使用默认评测条件。
- 自动选择某模型的最高分作为其唯一代表成绩。

成绩可以收录，不代表成绩一定具有跨模型可比性。

## 5. Benchmark 定义

Benchmark 定义保存在 `benchmarks/` 目录。

建议格式：

```toml
id = "example-benchmark-v1"
name = "Example Benchmark"
version = "1.0"
category = "coding"

metric = "accuracy"
unit = "percent"
higher_is_better = true
```

这是 ModelAtlas 专有定义格式，不属于 Models.dev 原始模型 Schema。

### 字段要求

- `id`：稳定且唯一。
- `name`：Benchmark 正式名称。
- `version`：明确的评测版本。
- `category`：能力分类。
- `metric`：评分指标。
- `unit`：分数单位。
- `higher_is_better`：评分方向。

需要时可以扩展 `description`、`url` 和 `methodology` 等字段。

### 定义规则

- 不得根据名称自行猜测 Benchmark 版本。
- 不得将版本不同且测试规则不兼容的 Benchmark 视为同一评测。
- 不得把综合指数错误标注为单一能力测试。
- 不得认为所有成绩都是百分比。
- 不得凭经验假设分数越高越好，必须确认指标含义。

模型档案中的成绩保持 Models.dev 兼容格式，由构建脚本将名称、版本和必要的指标信息映射到 Benchmark ID。

不能确认映射关系时，应报告问题，不得猜测。

## 6. 数据来源与许可

所有数据都应具备明确来源。

推荐来源优先级：

1. Benchmark 官方网站及原始排行榜。
2. 模型研发机构官方发布资料。
3. 模型卡和技术报告。
4. 具有明确测试方法的独立评测机构。
5. 可追溯原始结果的其他公开资料。

优先级不是绝对可靠性保证，仍需核实模型身份、评测版本与测试条件。

### 许可证规则

Models.dev 使用 MIT License，复用相关内容时应保留适用的版权和许可声明。

其他第三方评测结果可能有独立的数据许可与再分发限制。

特别注意：

- 公开可访问不等于允许复制和再分发。
- 标注来源不能代替授权。
- 不得绕过付费、访问控制或网站限制获取数据。
- 不得将第三方数据的许可状态默认为 MIT。
- 未确认可再分发的成绩不得自动纳入公开发布数据。

对于 Artificial Analysis 等第三方评测机构，应先确认对应数据的使用范围和许可要求。

## 7. AI Agent 工作流程

### 7.1 收集指定模型的成绩

当任务要求补充某个模型时：

1. 检查对应模型 TOML 是否存在。
2. 读取已有成绩，确定缺失的信息。
3. 搜索模型官方资料及相关 Benchmark。
4. 核实资料是否对应正确模型或版本。
5. 检查成绩是否已经存在。
6. 仅添加新的、可核实的成绩。
7. 保留来源和已知评测条件。
8. 校验修改后的文件。

不得因为收集 Benchmark 而随意修改模型其他字段。

### 7.2 收集指定 Benchmark 的成绩

当任务要求补充某项 Benchmark 时：

1. 读取 Benchmark 定义。
2. 确认评测版本、指标和使用条件。
3. 搜索对应模型的公开成绩。
4. 确认模型身份及测试条件。
5. 将成绩添加到对应模型 TOML 文件。
6. 检查重复、冲突和来源。
7. 验证数据格式。

**即使任务以 Benchmark 为中心，也只维护模型文件中的原始成绩，不手动维护第二份排行榜成绩。**

### 7.3 添加新模型

添加模型时：

1. 优先检查 Models.dev 是否已有对应模型。
2. 确认研发机构和模型的规范 ID。
3. 能够合法复用时，优先采用上游 TOML 结构。
4. 仅在来源充分时补充缺失信息。
5. 不得将不同模型版本合并为一个文件。
6. 不得因为模型名称相似而认定它们相同。

如果 Models.dev 尚未收录，应按照兼容的 v2 Schema 创建模型文件。

## 8. 重复与冲突处理

### 重复检测

新增成绩前，至少检查：

- 模型 ID
- Benchmark 名称
- Benchmark 版本
- 评分指标
- 测试数据集
- 评测变体
- Harness
- 来源及评测日期（如果存在）

不能仅根据 `name` 和 `score` 判断是否重复。

### 冲突处理

如果新来源与现有成绩不一致：

- 先检查是否为不同评测版本或条件。
- 检查是否为模型更新或评测结果修订。
- 不得自动采用较高分数。
- 不得无依据地覆盖原始成绩。
- 无法确认时保留已有数据，并报告冲突。

确认属于同一评测记录的官方修正时，可以更新，但必须说明依据。

## 9. 排行榜生成规则

排行榜为派生数据，不属于人工维护的事实来源。

构建排行榜时：

1. 读取所有模型 TOML。
2. 提取 Benchmark 成绩。
3. 映射到统一 Benchmark 定义。
4. 根据版本、指标、测试条件划分可比组。
5. 排除无法确认可比性的成绩。
6. 按正确评分方向排序。
7. 生成 JSON 数据。

排行榜必须避免：

- 将不同版本混合排序。
- 将不同指标混合排序。
- 自动采用最高分。
- 将缺失成绩视为零分。
- 将本地数据集排名宣称为官方完整排名。

如果已知条件不足以形成可靠的可比组，应保留原始成绩，不生成强制排名。

## 10. 数据校验

每次修改 TOML 后都应进行校验。

至少检查：

- TOML 语法是否有效。
- 模型文件路径是否符合规范。
- `schema` 是否符合当前约定。
- 字段类型是否正确。
- Benchmark 必需字段是否存在。
- 成绩是否重复。
- 来源 URL 是否与所记录结果对应。
- Benchmark 定义映射是否存在且无歧义。

如果仓库已有验证脚本，应优先运行现有脚本。

对于尚未实现的脚本，不得声称已通过验证。

可以使用 Python 3.11+ 的 `tomllib` 进行基础 TOML 解析检查，但语法检查不等于完成来源和数据真实性验证。

## 11. 文件修改原则

### 最小修改

只修改与当前任务直接相关的内容。

禁止：

- 无关字段的大规模重写。
- 随意调整已有文件的结构。
- 为了统一格式而删除有用的来源注释。
- 未经要求批量重命名模型文件。
- 无明确需求时添加新的数据层、数据库或复杂工具。
- 直接修改 `dist/` 下的生成数据。

### 保留历史信息

尽可能保留已有：

- 模型事实与资料来源。
- Benchmark 成绩与条件。
- 有意义的注释。
- 尚未被证实错误的原始记录。

数据修正应尽可能使 Git Diff 清晰、容易审查。

### 上游兼容

不得擅自改变 Models.dev 字段的语义。

如果需要与上游同步：

- 先比较差异。
- 不得覆盖已经验证的本地补充数据。
- 不得在无法确认冲突时自动合并。
- 对 Schema 不兼容情况进行报告。

## 12. 任务完成标准

Agent 每次完成数据收集任务后，应输出简短报告，至少包含：

### 变更摘要

- 新增或修改的模型文件。
- 新增 Benchmark 成绩数量。
- 修改的已有成绩数量。
- 新建的 Benchmark 定义（如有）。

### 数据来源

- 主要来源 URL。
- 需要人工核实的来源。
- 无法确认的数据许可问题。

### 校验结果

- 实际执行的校验。
- 校验是否通过。
- 尚未解决的数据冲突。
- 被跳过的成绩及原因。

### 示例报告

```text
任务：补充 Example Model 的 Benchmark 数据

修改文件：
- models/example/example-model.toml

结果：
- 新增成绩：3 条
- 修正成绩：1 条
- 跳过：2 条（来源不明确）

校验：
- TOML 语法：通过
- Schema 校验：未执行
- 来源核实：4 条已核实

待确认：
- 1 项评测的使用许可
```

Agent 不得将未执行的校验报告为通过。

## 13. 项目设计原则

始终遵循以下优先级：

1. **真实性**：不编造、不推测。
2. **可追溯性**：重要数据必须可以核实来源。
3. **可比性**：不同测试条件不能随意混合排名。
4. **兼容性**：尽可能兼容 Models.dev。
5. **可维护性**：一个模型一个文件，修改范围明确。
6. **简洁性**：避免提前设计不需要的复杂系统。
7. **可扩展性**：允许未来扩展模型信息和评测类型。

当数据完整性与准确性发生冲突时，优先保证准确性。

当架构复杂性与实际需求发生冲突时，优先选择能够满足需求的最简单方案。

**最终目标不是收集最多的 Benchmark 成绩，而是建立一个可靠、可持续维护、适合 ModelAtlas 展示和比较的 AI 模型数据集。**