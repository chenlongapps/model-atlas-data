---
name: sync-artificial-analysis
description: 更新 ModelAtlas Data 的 AA Intelligence Index 成绩与加权任务成本。用于下载最新数据、对比 AA 快照或导入 artificial-analysis-models TOML；先展示差异，只写入已核实项。
---

# 同步 Artificial Analysis Intelligence Index

只同步**已有模型**的 AA Intelligence Index 成绩及对应成本，不运行评测。预览只输出差异；同步先展示差异，再写入已核实项，无需逐项重复确认。

## 1. 准备

- 路径：本 Skill 目录为 `SKILL_ROOT`，向上三级为 `DATA_ROOT`；确认根目录包含 `AGENTS.md`、`models/`、`benchmarks/`。以 `DATA_ROOT` 为工作目录，不依赖当前目录或硬编码绝对路径。
- 范围：数据操作限于仓库；外部快照只读取用户指定文件，不扫描父目录或兄弟项目。不默认新增模型、Benchmark 定义或辅助工具，不修改基本资料、其他评测、描述、本地化及已有档位表示。
- 阅读：`AGENTS.md`、README 的成绩/成本/构建规范、相关模型和 AA 定义（通常为 `benchmarks/artificial-analysis-intelligence-index-v5.toml`，版本以内容为准）。可参考 `docs/artificial-analysis-sync-2026-11-07.md`，但历史记录不证明当前版本或许可。
- 检查 `git status --short`，保留用户已有改动。

### Python 与依赖

使用 Python 3.11+，记录解释器实际路径为 `PYTHON`，后续所有 Python 命令显式复用该路径，不依赖跨工具调用的环境变量或激活状态。

| 步骤 | 所需依赖清单 |
| --- | --- |
| 下载或下载器测试 | `SKILL_ROOT/scripts/requirements.txt`（`cryptography`、`tomli-w`） |
| 修改模型后的完整测试 | `DATA_ROOT/requirements-sync.txt`（`tomlkit`），写入前准备好 |
| 本地快照解析、校验、构建 | 仅标准库 |

先读取清单并检查环境；满足要求就复用，否则默认自动创建临时虚拟环境，仅安装所需依赖。遵循用户安装限制和工具权限，不修改系统或已有环境，不使用 `sudo`、`--user`、`--break-system-packages`。

以下为下载并运行完整测试的示例。先核实路径；`TEMP_ROOT` 使用运行环境允许的临时目录，未指定则先设为系统临时目录。整段在同一个 shell 调用中执行，失败即退出并报告：

```sh
VENV_DIR="$(mktemp -d "${TEMP_ROOT%/}/modelatlas-aa-XXXXXX")" || exit 1
"$PYTHON" -m venv "$VENV_DIR" || exit 1
PYTHON="$VENV_DIR/bin/python"
"$PYTHON" -m pip install \
  -r "$SKILL_ROOT/scripts/requirements.txt" \
  -r "$DATA_ROOT/requirements-sync.txt" || exit 1
"$PYTHON" -m pip check || exit 1
"$PYTHON" -c "import tomllib, tomli_w, tomlkit; from cryptography.hazmat.primitives.ciphers.aead import AESGCM" || exit 1
printf 'PYTHON=%s\n' "$PYTHON"
```

按实际步骤删减安装参数和导入检查，准备成功后继续任务。下载器或所需清单缺失时，请用户恢复或提供快照，不搜索外部替代代码。结束后仅清理本次创建且不再使用的环境；需复用时报告路径。

## 2. 获取输入

- **指定快照**：使用指定文件，不擅自替换。
- **本地最新**：仅检查 `DATA_ROOT/temp/` 中的文件名、修改时间和内容，报告所选文件；缺失或先后/来源不明时询问用户。
- **在线最新**：先读内置下载器，准备依赖后执行：

  ```sh
  "$PYTHON" "$SKILL_ROOT/scripts/download_artificial_analysis_scores.py" \
    --out "$DATA_ROOT/temp/"
  ```

  使用下载器实际返回的路径，不猜文件名；失败时报告，不用旧快照冒充最新。

下载器负责格式校验并输出路径、SHA-256、配置总数、有效分数数量、成本缺失数和零值数；非法字段或不同主数据集并存时失败，不按记录数量选取。本地或外部快照需解析并补做同样检查和统计：数值有限且非布尔值，成本非负，零分不等于缺失。

新快照在原有 `models` 数组上增补可选 `slug` 和顶层 `[snapshot]`（`format_version = 1`、`downloaded_at`、`page_url`、`manifest_urls`、`cost_unit`）。`slug` 仅保留来源实际字段，不猜 URL；元信息用于下载溯源，不作为成绩身份。旧四字段快照仍可使用；格式版本不是 Index 版本，下载时间、文件修改时间和 `releaseDate` 均不是成绩 `date`。

## 3. 对比与核验

**快照提供候选数值及可用的配置线索，不能独立证明精确模型版本、档位或 Index 版本；新增的下载溯源也不能替代官方配置页核验。**

先扫描本地 AA 成绩及 `source`，结合历史线索批量对比；只深入核验新增、变化和歧义项。写入前列出本地路径、AA 配置/来源、原值、新值及依据：

| 情况 | 处理 |
| --- | --- |
| 已匹配且数值不变 | 跳过，不重写 |
| 已核实的新配置或不同实验条件 | 分别新增，不只取最高分 |
| 同一配置分数变化 | 仅在确认官方修订后更新，否则保留本地并报告冲突 |
| 同一配置缺成本或成本变化 | 按下节单独核验后补充/更新 |
| 来源缺值或条目消失 | 不清空、不删除本地数据 |
| 无本地模型、映射歧义、条件或版本不明 | 跳过并说明原因 |

核验要求：

- 查 AA 官方模型页，必要时查页面原始数据，确认配置标识（如实际 `slug`）、精确模型版本、档位和来源。名称相似、日期接近、分数相同均不足以匹配；不猜 URL，不为补字段擅改下载器，不混合日期后缀、Preview、正式版或检查点。
- `effort` 仅用来源明确披露的原字符串；不从名称猜测、不借用其他评测、不改大小写、不将缺失当默认值，不迁移已有 `variant`。
- 结合 AA 方法页与 Index 定义核实快照适用版本；不将当前版本套给旧快照，不合并 5.0、5.0.1 等版本。已核实版本缺少本地定义时可保留原始成绩并报告未映射，不为消除警告新建或改写定义。
- 按模型 ID、评测名称、版本、指标、数据集、`effort`、`variant`、`harness`、`source`、`date` 及其他关键条件判重，成本不参与身份判重。缺失条件不证明条件相同；不能另加一条冲突成绩来规避判重。

核验入口：[模型](https://artificialanalysis.ai/models) · [Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) · [方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

### 成本口径

- 只取 `intelligenceIndexCostPerTask.cost.total`（简化快照的 `cost`），单位为 `USD/weighted task`。不以 token 单价、总评测费用、`intelligenceIndexCost.total` 或分项 `costPerTask` 替代，不推算或换算。
- 仅附到同一模型版本、档位、来源和已核实条件的成绩。`cost`、`cost_unit` 成对写入；独立来源用 `cost_source`，否则沿用成绩 `source`。
- 拒绝负数、非有限值和布尔值。原始零值或页面 `$0.00` 不证明真实免费；未经核实则省略成本，保留已有有效值。
- 更新已核实的当前观测成本时，在附近注释记录旧值、快照日期和依据；不认定旧值错误，不当作评测当天账单，不推断重定价原因。

## 4. 写入

- 仅编辑已确认模型文件的相关 `[[benchmarks]]`；保留注释、顺序、精度、缺失状态及无关内容，不整文件重新序列化。
- 填写有依据的 `name`、`score`、`metric`、`version`、`source` 和条件，未知可选字段省略。保留原始精度；网页舍入值不能替代精确值，也不能单独证明数值变化。
- `dist/` 仅通过构建脚本生成。未要求时不提交、推送或发布。
- 公开再分发前核查 AA 条款和许可；可下载或用户提供不等于获授权，Models.dev 许可不覆盖 AA 数据。许可不明则报告。

## 5. 校验与报告

修改模型后，在 `DATA_ROOT` 运行：

```sh
"$PYTHON" scripts/validate.py || exit 1
"$PYTHON" -m unittest discover -s tests -v || exit 1
"$PYTHON" scripts/build.py || exit 1
git diff --check || exit 1
```

- 对比修改前后解析值：仅计划项变化，分数和成本与已核实输入一致；检查重复、冲突、定义映射，区分历史警告与新增警告。
- `validate.py` 仅检查 TOML 语法；构建和测试不替代来源真实性、完整上游 Schema 或许可核验。依赖或检查失败如实报告，不声称通过。
- 无模型数据变化时无需构建或重写，报告实际检查即可。
- 最终简报：输入摘要、修改路径、新增/修正成绩数、补充/更新成本数、主要来源、校验结果、跳过项、冲突和许可限制。仅在用户要求时另存报告。

维护下载器时另跑离线测试（无需访问 AA，也不更新模型）：

```sh
"$PYTHON" -m unittest discover -s "$SKILL_ROOT/tests" -v
```

## 调用示例

- “使用 sync-artificial-analysis，下载并同步最新 AA Index。”
- “使用 sync-artificial-analysis，对比指定快照，只预览差异，不修改模型。”
- “使用 sync-artificial-analysis，同步本地最新快照，冲突保留并报告。”
