# Artificial Analysis 导出同步（2026-11-07）

## 输入与口径

- 用户文件：`/Users/chenlong/Downloads/artificial-analysis-models-2026-11-07-2.toml`，未复制进仓库。
- SHA-256：`527c24db5528be9da7efbfad863be0f948c86559feda6b4175aa5de4da593aec`。
- 共 726 个配置，109 个有 `intelligenceIndex`，102 个有 `cost`（其中 3 个为零）。617 个无成绩配置不补零、不删除或覆盖本地数据。
- 当前官方 [Index 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) 确认为 5.0.1、九项评测。成本是 `USD/weighted task`，不是 token 单价或评测总成本；新增记录及成本变化对应的官方页面已核对。
- 文件名日期仅用于识别快照，不写入成绩 `date`，也不覆盖模型发布日期。未迁移已有 `effort`/`variant`、改写描述或合并历史成绩。

## 修改的模型文件（7）

| 文件 | 修改 |
| --- | --- |
| `models/thinkingmachines/inkling-2-small.toml` | 新增 Index 5.0.1 成绩及成本 |
| `models/google/gemini-4-carbon.toml` | 新增 Medium、High、Low 三条 Index 5.0.1 成绩及各自成本 |
| `models/cohere/north-mini-code-1-0.toml` | 新增 Index 5.0.1 成绩；保留旧版未注明版本的 27.6，不写入无法确认的零成本 |
| `models/tencent/hy4.toml` | 为已有精确成绩补充成本 |
| `models/meta/muse-wonder-1.0.toml` | 为已有 High 成绩补充成本 |
| `models/mistral/mistral-large-4.toml` | 更新 Medium、High 的当前观测成本，不改成绩 |
| `models/nvidia/nemotron-3.5-super-vl-120b-a12b.toml` | 更新当前观测成本，不改成绩 |

合计新增 **5 条成绩、6 条成本**（4 条随新成绩写入，2 条补充已有成绩），更新 **3 条成本**；没有修正任何已有分数，没有新建模型或 Benchmark 定义，无描述变化，因此未修改本地化。

三条成本变化已在对应官方配置页核对，旧值保留在 TOML 注释中。这是当前观测值更新，不宣称历史快照错误，也未推断重定价原因：

| 配置 | 旧成本 | 当前成本（USD/weighted task） |
| --- | --- | --- |
| Mistral Large 4 Medium | 1.4119376739255958 | 1.4120973060945472 |
| Mistral Large 4 High | 2.061496607384404 | 2.0617306268126856 |
| Nemotron 3.5 Super VL | 0.5382257339551116 | 0.5196327287868884 |

## 主要来源

- [Inkling 2 Small](https://artificialanalysis.ai/models/inkling-2-small)
- Gemini 4 Carbon：[Medium](https://artificialanalysis.ai/models/gemini-4-carbon-medium)、[High](https://artificialanalysis.ai/models/gemini-4-carbon)、[Low](https://artificialanalysis.ai/models/gemini-4-carbon-low)
- [North Mini Code 当前指数](https://artificialanalysis.ai/models/north-mini-code)；另查阅 [官方模型卡](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)，确认已有完整模型 30B 总量、3B 激活量和 Apache-2.0 许可，参数表无需修改。
- [Tencent Hy4](https://artificialanalysis.ai/models/tencent-hy4)、[Muse Wonder High](https://artificialanalysis.ai/models/muse-wonder-high)
- Mistral Large 4：[Medium](https://artificialanalysis.ai/models/mistral-large-4-medium)、[High](https://artificialanalysis.ai/models/mistral-large-4)
- [Nemotron 3.5 Super VL](https://artificialanalysis.ai/models/nemotron-3-5-super-vl)

## 跳过与限制

- **6 条有成绩配置未导入**：Nanbeige4.3-33B、K2 Horizon 375B A23B、Granite 4.2 3B、K-EXAONE 2.0、NVIDIA Nemotron 3 Nano 4B 尚无本地对应档案；导出仅含名称、日期及评测数值，不足以建立规范模型资料。Ling 3.1 Flash 1019 不能确认等同于现有 `inclusionai/ling-3.1-flash`，未将日期后缀版本合并。
- **3 个零成本未采纳**：K2 Horizon、Command A+、North Mini Code；未确认是真实零费用而非缺失定价占位，不能将网页显示 `$0.00` 当作充分证据。
- 同步后用户文件中 **103/109** 条分数在本地有对应的 5.0.1 精确记录；其中 98 条正成本一致。其余 6 条如上跳过。93 条已有配置不需要修改。
- AA 数据再分发许可仍需人工确认。[网站条款](https://artificialanalysis.ai/terms-of-use) 的既有审查与限制见 [`benchmark-costs-2026-11-06.md`](benchmark-costs-2026-11-06.md#定义映射与许可)；用户提供文件不等于获得公开再分发授权，Models.dev 的 MIT 许可也不适用于 AA 评测数据。

## 实际执行的校验

- `python3 scripts/validate.py`：867 个 TOML 全部通过语法解析。
- `python3 scripts/build.py`：855 个模型、11 个定义、1 个语言文件构建成功；包含主要字段类型、路径、Schema 标记、重复/冲突、来源 URL 与定义映射检查，不等于完整上游 Schema 或全部来源真实性校验。
- `python3 -m unittest discover -s tests -v`：112 项测试全部通过。
- `git diff --check`：通过。
- 独立解析与 `HEAD` 比较：7 个模型的基本资料和全部已有成绩分数、条件、来源不变，仅预期成本字段变化；5 条新成绩、5 条已有成绩的成本修改与输入精确数值一致。全部 855 个生成 JSON 模型与 TOML 解析值一致。
- 在内存中恢复修改前模型并比较引用检查结果：构建警告与修改前完全一致，已有 1,184 条成绩未映射定义、歧义 0 条，中文描述缺少 3 项；本次没有新增警告。
