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