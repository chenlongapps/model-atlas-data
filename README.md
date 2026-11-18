# ModelAtlas Data

[ModelAtlas Android](https://github.com/chenlongapps/model-atlas-android) 的 AI 模型数据仓库，基于 [Models.dev](https://github.com/anomalyco/models.dev) 格式维护模型资料和已公开的 Benchmark 成绩，**不运行评测**。

以 TOML 为源数据，构建 JSON 供应用使用；保留成绩来源与实验条件，不把不同版本或配置混成排名。

**[在线浏览](https://chenlongapps.github.io/model-atlas-data/) · [文档导航](docs/README.md) · [维护规则](AGENTS.md)**

## 快速开始

需要 Python 3.11+，以下命令无需第三方依赖：

```sh
python3 scripts/validate.py  # TOML 语法检查
python3 scripts/build.py     # 结构检查并生成 dist/ JSON
python3 scripts/preview.py   # 本地网页预览
```

预览地址：<http://127.0.0.1:8000/>，`Ctrl+C` 停止。测试、输出目录及检查范围见[开发与校验](docs/development.md)。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `models/<lab>/<model-id>.toml` | 一个模型一个文件，包含该模型的原始成绩 |
| `benchmarks/` | 评测定义，不重复维护成绩 |
| `i18n/` | 模型和评测描述的翻译 |
| `scripts/`、`tests/` | 校验、构建、同步及测试 |
| `web/` | Web Explorer 静态网页 |
| `dist/` | 生成的 JSON，不直接修改、不提交 Git |

## 数据使用

发布站点提供下列端点，前缀为 `https://chenlongapps.github.io/model-atlas-data/`：

| 端点 | 内容 |
| --- | --- |
| [models.json](https://chenlongapps.github.io/model-atlas-data/models.json) | 模型 ID → 档案及逐条成绩 |
| [benchmarks.json](https://chenlongapps.github.io/model-atlas-data/benchmarks.json) | 评测 ID → 定义 |
| [i18n/zh-CN.json](https://chenlongapps.github.io/model-atlas-data/i18n/zh-CN.json) | 简体中文描述 |
| [manifest.json](https://chenlongapps.github.io/model-atlas-data/manifest.json) | 数据版本、Git 提交、发布包生成时间及文件哈希 |
| [llms.txt](https://chenlongapps.github.io/model-atlas-data/llms.txt) | 面向 AI 的数据导航 |

- 缺失值表示未知，不是零或默认配置；不同模型版本、指标、数据集、档位及 Harness 不自动可比。
- 按名称、版本和指标关联定义，兼容版本及 `unspecified` 例外见[映射规则](docs/data-format.md#benchmark-定义与展示)；未映射成绩仍在模型数据中保留。网页排序和前沿不代表经核实的排行榜。
- 构建检查不证明来源真实性或许可。Models.dev 的 [MIT 声明](LICENSE.models-dev)不覆盖第三方评测数据及模型权重，分发前须核对[许可与待核实事项](docs/review-notes.md)。

## 维护数据

修改前阅读 [AGENTS.md](AGENTS.md)，具体格式见[数据规范](docs/data-format.md)。准确性优先：未知项省略，保留有效来源、原始精度及条件；新增 Benchmark 定义须先获用户确认。

### 模型参数量

使用 `metadata.modelatlas.parameters`，分别记录完整总量和每 token 激活量，单位 B；不从名称推断。见[字段规范](docs/data-format.md#模型参数量)与[核验方法](docs/model-parameters.md)。

### 组件参数量及兼容策略

`components` 独立记录有来源的组件，不求和填完整总量；旧消费者不能回退到组件之和。见[组件规范](docs/data-format.md#组件参数量及兼容策略)。

### Benchmark 成绩的推理档位

`effort` 原样保留来源档位与大小写，缺失不等于默认值；其他条件保留在 `variant` 等字段。见[档位规范](docs/data-format.md#推理档位)。

### Benchmark 成绩的成本

`cost` 与 `cost_unit` 成对提供，可用 `cost_source` 单独溯源；不同计费口径不混用。它们与 `effort` 是 ModelAtlas 扩展，严格上游消费者须显式处理。见[成本规范](docs/data-format.md#benchmark-成绩的成本)。

### 数据校验

每次修改 TOML 后运行语法检查及构建，并按改动运行测试；还须人工核对来源与条件。见[检查范围与测试命令](docs/development.md)。

## 更多文档

- [网页、图表与 GitHub Pages 发布](docs/publishing.md)
- [Models.dev 自动同步与翻译](docs/models-dev-sync.md)
- [评测来源、成本字段与实验口径](docs/benchmark-sources.md)

自动同步每小时检查上游，新模型完整导入，已有模型只更新基本信息、不改已有成绩；有翻译的描述保留待人工核验。历史执行报告不再单独维护，仍有影响的限制集中在[待核实事项](docs/review-notes.md)。
