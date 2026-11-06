# Benchmark 成本补齐（2026-11-06）

## 结果与范围

仅为已有成绩补充成本；不新增、修正或删除成绩，不改推理档位、实验条件、原有来源、日期或模型基本信息。新增 Benchmark 定义 0 个；描述未变化，无需修改本地化。

| 目标版本 | 原有成绩 | 补充成本 | 保持缺失 |
| --- | ---: | ---: | ---: |
| DeepSWE 1.1 | 82 | 17 | 65 |
| Terminal-Bench 4.0 / 4.0.0 | 112 | 58 | 54 |
| Vals Index 2.2 | 27 | 24 | 3 |
| Artificial Analysis Intelligence Index 5.0.1 | 104 | 92 | 12 |
| 合计 | 325 | 191 | 134 |

修改 62 个 `models/<lab>/<model>.toml` 文件，清单见下方。`cost`、`cost_unit`、可选 `cost_source` 是 ModelAtlas 扩展，校验和兼容规则见 [README](../README.md#benchmark-成绩的成本)。成本元数据不参与成绩身份判重，不会把同一成绩的不同成本视为两个实验。旧记录的缺失状态不变。

## 来源与口径

### DeepSWE：17 条，`USD/task`

- [官方榜](https://deepswe.datacurve.ai/)、[v1.1 方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1)、[原始 JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)。
- 读取同一 `model`、`reasoning_effort`、`harness` 配置的 `mean_cost_usd`：对已评分尝试取平均，来源排除 provider/verifier/network 错误。不用中位数、不除以任务数、不从单价重算。
- 核对 pass@1 原始值或该配置的官方舍入显示，并与首页内嵌配置数据交叉核验成本。没有把厂商独立报告的同名评测当作 Datacurve 实验，也没有把无日期的 DeepSeek 名称或 `gemini-flash-latest` 当作具体 checkpoint。
- GPT-6 Astra 的官方 `cost_basis` 明确采用当前输入、缓存读写和输出定价，无单独 compute-unit fee；该口径原文保留在相应 TOML 注释中，不代表实际评测日账单。

### Terminal-Bench 4：58 条，按来源分别保存

- 12 条来自 [Terminal-Bench 官方榜](https://www.tbench.ai/leaderboard/terminal-bench/4.0)：读取内嵌 `metrics.total_cost_usd`，单位 `USD/evaluation`。匹配模型、原生 Agent、档位及成绩显示；对应行均报告 `n_trials = 330`，全任务集为 66 个任务，已在注释中保留。没有换算为每任务费用。
- 27 条来自 [Vals Terminal-Bench 4](https://www.vals.ai/benchmarks/terminal-bench-4) 及其公开引用的 [原始 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.g-vQx4Dh.json)：读取 `tasks.overall[model].cost_per_test`，单位 `USD/test`。
- 19 条来自用户提供的 AA 快照：读取对应模型的 `intelligenceIndexEvaluations` 中 `slug = "terminalbench-4-0"` 的 `costPerTask`，单位 `USD/task`。不是 `intelligenceIndexCostPerTask.evaluations[].weightedCostPerTask`，后者只是 Index 的加权贡献，不能充当独立评测成本。
- 三方实验的成本不互相套用。AA 对应同文件已有精确 Index 记录所锚定的 checkpoint，再核对来源配置、档位和 Terminal-Bench 成绩；无法唯一确定则跳过。舍入的成绩不被改写为新分数。

### Vals Index：24 条，`USD/test`

- [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index) 及页面公开引用的 [原始 JSON](https://www.vals.ai/_astro/benchmark_view_vals_index.CxyItaos.json)。
- 使用 `tasks.overall[model].cost_per_test`，保留完整数值精度，不使用已舍入的表格美元显示。核对版本、模型 ID、精确值或原有舍入成绩、已注明档位、Provider 及输出限制等条件。
- Vals 的机构 ID 与本仓库不同，例如 `kimi` / `moonshotai`、`zai` / `zhipuai`；`meta/muse-wonder` 对应已有的 `meta/muse-wonder-1.0` 记录。Vals 页面将 Qwen 0902 链接至 `alibaba_qwen3.8-max-0902`，原始 JSON 的内部键为 `alibaba/qwen3.8-max-internal`；不据此将旧 Qwen3.8 Max 版本合并。
- 页面数据的 `updated = "2026-11-05"` 是来源更新时间，不写入成绩的评测日期。

### AA Index：92 条，`USD/weighted task`

- 用户提供 `artificial-analysis-models-2026-11-05.json`，共 725 个模型配置；106 个有 Index 成绩，98 个有成本。该文件未复制进仓库。
- 读取 `intelligenceIndexCostPerTask.cost.total`，不使用 `intelligenceIndexCost.total`。口径为 [AA 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) 的按 Index 权重加权的每任务成本；不是 API 每百万 token 单价，也不是总评测费用。
- 使用原有官方模型页/比较页/发布页对应的模型配置与精确 Index 分数联合核对，保留已有档位的原始大小写及 fallback 等条件。成本独立来源需要定位具体配置时填写官方模型页 `cost_source`。
- 文件无顶层版本或采集时间元数据；文件名日期不当作实际评测日期。5.0.1 的适用性由已有记录、对应来源与九项评测构成核对；不把该快照成本套到旧版 Index 或 Astra Fast 模式。

### 采集内容的 SHA-256

哈希用于识别本次核对的内容，不证明来源的再分发许可。网页/静态资源日后可能更新；快照没有提交到仓库。

| 内容 | SHA-256 |
| --- | --- |
| 用户 AA JSON | `ea49b968039dcf1bb91e706136ac41525078a7ebf45d06b17b7737dc051522c2` |
| DeepSWE 原始 JSON | `a7c15d66288fd249c020b9931c017b92d1a3b90e480b3ff34974b752bd030019` |
| DeepSWE 首页 | `4ad6365bf7625f9fe176a5c6c709855ecaa74d3c829dadfb407546d0aefcfae2` |
| Terminal-Bench 官方榜 HTML | `4627bf67ded7174911eb5956bfbb5d54c4a0dfb25be01487a05b5af3aa945f84` |
| Vals Index 原始 JSON | `9440acd92c489f5f417f5b98dccda8dfcb98774e52cd6641e3eb61acec0917d9` |
| Vals Terminal-Bench 原始 JSON | `5ba784b71ce48173da02c365ac5c2f7bc09a99c5c489af560d08dd2639a63100` |

## 跳过与未解决问题

以下记录均保持原样，不补默认值，不因成本缺失删掉成绩。

- **94 条没有核实到同一实验的成本**：DeepSWE 61 条、Terminal-Bench 32 条、Vals Index 1 条。主要为厂商/第三方发布、不同 Harness 或来源不能确认；没有将其与官方榜同名模型拼接。Vals 的 Inkling Index 旧记录来源为未核实的 `vals-ai.com`，不假定等同于当前官方页面。
- **18 条 AA Terminal-Bench 配置或成绩无法唯一对应**：Qwen3.7 Max、Qwen3.8 2.4T A95B、Qwen3.8 Flash Next、旧 Qwen3.8 Max、Opus 4.8、Sonnet 5、Trinity Large Thinking、Ling 3.0 Flash Fin、Ling 3.1 Flash、LongCat 2.0、Muse Spark 1.2、Muse Spark 1.3 Xhigh、Mistral Medium 2604、Kimi K3.1 Pro、Hy3、Solar Mini4、GLM 5.1、GLM 5.3。快照不必涵盖每个已有记录的配置；没有从同模型其他档位移用成本。
- **6 条 AA Index 无精确配置/分数匹配**：Qwen3.8 Max 0902 的旧舍入记录、Gemini 3.1 Flash-Lite Preview 的旧舍入记录、Gemini 3.5 Flash-Lite 的旧舍入记录、Mistral Medium 2604、Mistral Medium 3.5 的旧舍入记录、GPT-6 Astra Fast。已有精确记录可匹配时仅补精确记录，不自动合并旧记录。
- **5 条 AA Index 无成本**：Gemini 3.8 Flash Low、Gemma 4 31B、Wonder High、Wonder Full Max、Tencent Hy4。另有 Command A+ 的 Index 与 Terminal-Bench 成本为零，无法确认真实零费用还是定价/用量缺失，两条均跳过。
- **4 条 checkpoint 身份未确认**：DeepSWE 的 DeepSeek V4 Flash 0731、`gemini-flash-latest`；Vals Terminal-Bench 的 `gemini-flash-latest`；Vals Index 的 Beam 1.0。Beam 在公开表格中也未提供成本。
- **DeepSWE 两条成本冲突**：GPT-5.6 Sol max 的原始 JSON 为 `8.386436346666667`，首页内嵌为 `6.455954682467823`；GPT-5.6 Luna max 分别为 `3.028116810267857` 和 `0.6056233620535714`。同一生成时间下两种来源内容不同，未找到足够依据确认重定价修订，暂不选择任一值。全量源配置还存在其他成本差异，但不向未匹配的本地实验传播。
- **Vals 三条条件/成绩不一致**：旧 Qwen3.8 Max Terminal-Bench 记录注明 single run，当前方法为 avg@3；旧 GPT-6 Sol Terminal-Bench 模型页记录为 34.34，当前为 44.444；Nemotron 3.5 Super VL Index 记录为 29.76，当前为 29.784。保留原记录，未改成绩、未强行添加当前成本。

### 定义映射与许可

- 仓库原有 1,204 条成绩未匹配 Benchmark 定义，歧义 0 条。本次未改变数量；其中补成本的 29 条原有记录仍未匹配（Terminal-Bench 24 条、DeepSWE 5 条），原因包括原有指标名称如 `accuracy`、`resolution rate`、`pass rate` 与定义不同。只报告，不为使映射通过而改指标、改版本或声明未经论证的指标等价关系；这些记录仍保留原始成绩，不强制排名。
- 原有中文模型描述缺少 3 项，未扩大或修复该问题；本次没有描述变化。
- **成本数据的再分发许可仍需人工确认。** Models.dev 的 MIT 许可不自动适用于这些第三方评测数据。AA 的 [网站条款](https://artificialanalysis.ai/terms-of-use)（标注修订于 2026-09-15）第 2.1、2.2、3.3 节包含个人非商业使用、复制/再分发及自动采集限制；用户提供文件不等于已取得公开再分发授权。此次 AA 数值仅从用户文件读取，未批量抓取 AA 模型页；正式对外发布前应确认许可或取得授权。Vals、Datacurve 及 Terminal-Bench 榜单成本数据的单独再分发授权本次亦未确认，不将任务集或代码开源许可视为榜单数据许可。

## 修改的模型文件（62）

所有路径均位于 `models/`：

```text
alibaba/qwen3.8-27b.toml
alibaba/qwen3.8-max-0902.toml
anthropic/claude-fable-5-1.toml
anthropic/claude-fable-5.toml
anthropic/claude-haiku-4-5.toml
anthropic/claude-haiku-5-5.toml
anthropic/claude-opus-4-8.toml
anthropic/claude-opus-5-5.toml
anthropic/claude-opus-5.toml
anthropic/claude-sonnet-5-5.toml
anthropic/claude-sonnet-5.toml
deepseek/deepseek-v4-flash-0731.toml
deepseek/deepseek-v4-pro-0813.toml
deepseek/deepseek-v4.1-flash-1017.toml
fireworks/ember-1.toml
google/gemini-3.1-flash-lite-preview.toml
google/gemini-3.5-flash-lite.toml
google/gemini-3.5-flash.toml
google/gemini-3.7-flash.toml
google/gemini-3.8-flash.toml
google/gemini-4-argon.toml
ibm/granite-4.2-8b.toml
inception/mercury-3.toml
meta/muse-glimmer-30b.toml
meta/muse-spark-1.3.toml
meta/muse-spark-open.toml
meta/muse-wonder-1.0.toml
meta/muse-wonder-full.toml
minimax/MiniMax-M3.1-Flash.toml
minimax/MiniMax-M3.toml
mistral/mistral-large-4.toml
mistral/mistral-medium-3-5.toml
mistral/mistral-small-2603.toml
moonshotai/kimi-k3.1-pro.toml
moonshotai/kimi-k3.toml
nvidia/nemotron-3-ultra-550b-a55b.toml
nvidia/nemotron-3.5-lightning.toml
nvidia/nemotron-3.5-super-vl-120b-a12b.toml
openai/gpt-5.4.toml
openai/gpt-5.5.toml
openai/gpt-5.6-luna.toml
openai/gpt-5.6-sol.toml
openai/gpt-5.6-terra.toml
openai/gpt-6-astra.toml
openai/gpt-6-luna.toml
openai/gpt-6-sol.toml
openai/gpt-6.1-sol.toml
openai/gpt-6.1-terra.toml
reflection/beam-1.0-501b-a23b.toml
stepfun/step-5-preview.toml
tencent/hy4-preview.toml
thinkingmachines/inkling-small.toml
thinkingmachines/inkling.toml
xai/grok-4.5.toml
xai/grok-4.6.toml
xai/grok-4.7.toml
xiaomi/mimo-v2.5-pro.toml
xiaomi/mimo-v2.6-flash.toml
xiaomi/mimo-v2.6-pro.toml
zhipuai/glm-5.2.toml
zhipuai/glm-5.3-flash.toml
zhipuai/glm-5.3.toml
```

## 实际校验

- `python3 -B scripts/validate.py`：864 个 TOML 成功，0 失败。
- `python3 -B scripts/build.py`：852 个模型、11 个定义、1 个语言文件构建成功；仅上述原有警告。`dist/` 为脚本生成，未直接编辑。
- `python3 -B -m unittest discover -s tests -v`：104 项通过，覆盖成本非负有限数值、成对字段、来源 URL、缺失状态、不同单位与精度的 JSON 保留、成本不能掩盖成绩重复/冲突、已有成绩及成本的同步保护。
- `node --test tests/web.test.mjs`：19 项通过，未修改网页功能。
- 逐条比较解析后的 TOML 与原始数据候选：191 条成本、单位和来源一致；134 条跳过记录原样保留。对比 Git 基线，全部模型基本字段、原有成绩数值与条件、注释及原有文本未改动，仅增加成本字段及必要的成本口径注释。
- 独立重新读取原始来源快照验证：191/191 条成本与实际来源字段一致；生成的 `dist/models.json` 与 852 个模型的 TOML 解析值逐个一致。单位分布为 `USD/weighted task` 92 条、`USD/task` 36 条、`USD/test` 51 条、`USD/evaluation` 12 条。
- `git diff --check`：无空白错误。

上述校验不代表已取得数据再分发许可，也不是完整上游 Schema 或所有历史成绩的来源真实性验证。
