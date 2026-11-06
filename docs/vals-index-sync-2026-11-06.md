# Vals Index 总分同步（2026-11-06）

## 范围与结果

只同步用户指定 JSON 的 `tasks.overall`，版本为 Vals Index **2.2**；不导入另外 8 个分项，不同步不在 JSON 中的其他模型，不修改自动同步脚本。

- 核对 34 个源模型，**同步 32 条，跳过 2 条**。首轮跳过 MiMo 两条，后按用户明确要求补录为带版本限制说明的官方 API 评测记录。
- 新建模型文件 **3 个**；修改已有模型文件 **29 个**。
- 新增成绩 **7 条**：Carbon、Inkling 2 Small、Mistral Large 4 开放权重版本、GPT-6.1 Terra、Hy4、MiMo V2.6 Pro、MiMo V2.6 Flash。
- 更新已有记录 **25 条**：其中 **24 条**将网页舍入值恢复为 JSON 原始数值精度；Kimi K3.1 Pro 的 62.52 不变，补充明确的档位及溯源注释。未重复添加原有成绩。
- 新补成本 **8 条**，均为源 JSON 的 `cost_per_test`，单位 `USD/test`；原有 24 条成本保持不变。
- 新记录或补充明确档位 **14 条**，直接读取 `reasoning_effort` 或 `compute_effort`，不从名称、旧 variant 或空值推断。
- 新增中文模型描述 **3 条**；新增 Benchmark 定义 **0 个**，复用 `benchmarks/vals-index-v2.2.toml`。
- 最终模型总数 **855**，Vals Index v2.2 记录 **34 条**：32 条已同步，加上未改动的 Beam、Nemotron 两条旧记录。MiMo 两条 API 成绩的 variant 明确注明具体 checkpoint 未披露，不能视为已验证的 RL 权重成绩。

## 来源和记录规则

- 原始 JSON：<https://www.vals.ai/_astro/benchmark_view_vals_index.CxyItaos.json>
- 官方榜单与方法：<https://www.vals.ai/benchmarks/vals_index>
- 本次重新读取的 JSON SHA-256：`9440acd92c489f5f417f5b98dccda8dfcb98774e52cd6641e3eb61acec0917d9`。
- 元数据 `updated = "2026-11-05"` 只是源更新时间，**不写为评测日期**。新成绩不新增 date；已有日期原样保留，不声称本次重新确认了这些日期。
- 总分采用官方页面所称的 performance score，按百分制记录；JSON 的字段名 accuracy 不意味着这是单一能力准确率测试。
- 保留原始数值精度，不重新计算加权指数、误差、成本或延迟。标准误 `stderr`、Provider 和非空采样参数写入相应成绩旁的 TOML 注释，不新增 Schema 字段。JSON 的 null 不变成默认值。
- `max_output_tokens` 仅作为本次实验的输出设置保存，**不直接填入模型固有的 limit.output**。
- 旧 source、dataset、variant、harness、date 及已有 effort 字符串保持原样；只有 Inkling 的旧 `vals-ai.com` 来源改为本次直接核实的 `www.vals.ai` 模型页，不假设两个域名等价。
- Haiku 的已有 `effort = "Max"` 保留，不改成 JSON 的 `"max"`；原始 compute_effort 在注释中明确记录。没有批量规范化大小写或迁移 variant。
- Haiku 与 Luna 原先含 `±` 的 score 改为精确数值时，原显示字符串及 JSON 标准误仍保留在注释中。JSON 不保留 TOML 注释，因此这些误差信息不会作为结构化字段分发；这是现有 Schema 的限制。
- overall 的 harness 为 null，不把某个分项的 OpenHands 或 Mini-SWE-agent 当作综合指数的统一 Harness。

## 新模型与身份核实

检查了 Models.dev `dev` 分支的模型目录和 v2 Schema。Carbon、Inkling 2 Small 尚无对应 lab 文件；上游 Mistral Large 4 文件仍是 10 月 6 日 Preview。未修改或导入无关上游数据。

### Gemini 4 Carbon

文件：`models/google/gemini-4-carbon.toml`。

依据 [Vals 模型页](https://www.vals.ai/models/google_gemini-4-carbon) 明示的 Google 身份、名称、发布日期、私有权重状态和输入类型建档。Google 当前[模型目录](https://ai.google.dev/gemini-api/docs/models)只列 Gemini 4 Argon，尝试读取 Carbon 专页返回 404，未核实独立的厂商规格。

因此描述明确标注资料来自 Vals；不复制 Argon 的能力和限制。Vals 的通用文件输入没有具体 MIME 类型，不假定为 PDF；1M 限制未展开为未经证实的精确整数。未填工具能力及采样控制布尔值。

### Inkling 2 Small

文件：`models/thinkingmachines/inkling-2-small.toml`。

一手来源：[发布公告](https://thinkingmachines.ai/news/inkling-2-small/)、[模型卡](https://thinkingmachines.ai/model-card/inkling-2-small/)。厂商明确模型为 594B 总参数、17B 激活参数，接受文本和图像，输出文本，不支持音频；公告明确发布初期权重关闭，预计安全测试后开放。

**采用 `open_weights = false`，不采用 Vals 的 open-weight 标签，不提前设置 Apache-2.0 许可或捏造权重下载链接。** Tinker 的训练和 serverless 上下文限制属于平台条件，不替代模型规格；厂商的 1M 上下文未擅自展开为精确 token 数。

### Mistral Large 4 开放权重版本

文件：`models/mistral/mistral-large-4-1t-a52b.toml`。

一手来源：[10 月 29 日发布公告](https://mistral.ai/news/mistral-large-4-oss/)、[权重模型卡](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)、[API 文档](https://docs.mistral.ai/models/mistral-large-4-0)。官方说明在 Preview 后继续进行 RL 并发布改进模型，因此不写入现有 `models/mistral/mistral-large-4.toml`。

使用厂商明确的权重标识确定新路径；Vals ID `mistralai/mistral-large-4-oss` 映射至此版本，不将托管商或页面路由当作研发机构。模型卡明确 1.05T 总参数、52B 激活参数，并在本地 Vibe 示例中给出 `max_context_length = 1048576`。许可为 **Mistral Ecosystem Open-Weight License**，不是 MIT；Model-as-a-Service 商业使用另有授权条件。

### Schema 兼容边界

三个新文件使用 `schema = 2` 及上游字段名称、类型和 lab 目录结构，不增加顶层 id、Provider 价格或新扩展字段。未知信息不填 false 或零。

但是，严格上游 LabModelV2 要求完整的采样控制等能力字段；Carbon 还缺少可核实的 tools 字段。为遵守准确性要求而保留这些缺失，**不能声称三个新档案已通过完整上游严格 Schema**。仓库基础结构校验允许这些字段暂缺；Carbon 和 Inkling 的空 limit 表表示尚无精确限制，不代表限制为零或无限。严格消费者需要先补齐核实资料或拒绝这些不完整档案。

`effort`、`cost` 和 `cost_unit` 仍为既有 ModelAtlas 扩展；严格上游消费者需显式处理。

## 全部 34 个模型的处理清单

下列路径均相对于 `models/`。

| JSON 模型 | 本地模型文件 | 操作 |
| --- | --- | --- |
| `anthropic/claude-sonnet-5-5` | `anthropic/claude-sonnet-5-5.toml` | 更新已有记录 |
| `google/gemini-4-carbon` | `google/gemini-4-carbon.toml` | 新模型、新成绩 |
| `anthropic/claude-opus-5-5` | `anthropic/claude-opus-5-5.toml` | 更新已有记录 |
| `google/gemini-4-argon` | `google/gemini-4-argon.toml` | 更新已有记录 |
| `meta/muse-wonder-full` | `meta/muse-wonder-full.toml` | 更新已有记录 |
| `openai/gpt-6-astra` | `openai/gpt-6-astra.toml` | 更新已有记录 |
| `meta/muse-wonder` | `meta/muse-wonder-1.0.toml` | 更新已有记录 |
| `openai/gpt-6.1-sol` | `openai/gpt-6.1-sol.toml` | 更新已有记录 |
| `kimi/kimi-k3.1-pro` | `moonshotai/kimi-k3.1-pro.toml` | 补充档位、溯源 |
| `deepseek/deepseek-v4.1-flash-1017` | `deepseek/deepseek-v4.1-flash-1017.toml` | 更新已有记录 |
| `openai/gpt-6.1-terra` | `openai/gpt-6.1-terra.toml` | 新增成绩 |
| `zai/glm-5.3` | `zhipuai/glm-5.3.toml` | 更新已有记录 |
| `tencent/hy4` | `tencent/hy4.toml` | 新增成绩 |
| `alibaba/qwen3.8-max-internal` | `alibaba/qwen3.8-max-0902.toml` | 更新已有记录 |
| `anthropic/claude-haiku-5-5` | `anthropic/claude-haiku-5-5.toml` | 更新已有记录 |
| `grok/grok-4.7` | `xai/grok-4.7.toml` | 更新已有记录 |
| `xiaomi/mimo-v2.6-pro` | `xiaomi/mimo-v2.6-pro.toml` | 补录官方 API 成绩，注明 checkpoint 未披露 |
| `mistralai/mistral-large-4-oss` | `mistral/mistral-large-4-1t-a52b.toml` | 新模型、新成绩 |
| `thinkingmachines/inkling-2-small` | `thinkingmachines/inkling-2-small.toml` | 新模型、新成绩 |
| `google/gemini-3.8-flash` | `google/gemini-3.8-flash.toml` | 更新已有记录 |
| `xiaomi/mimo-v2.6-flash` | `xiaomi/mimo-v2.6-flash.toml` | 补录官方 API 成绩，注明 checkpoint 未披露 |
| `stepfun/step-5-preview` | `stepfun/step-5-preview.toml` | 更新已有记录 |
| `minimax/MiniMax-M3.1-flash` | `minimax/MiniMax-M3.1-Flash.toml` | 更新已有记录，保留本地 ID 大小写 |
| `tencent/hy4-preview` | `tencent/hy4-preview.toml` | 更新已有记录 |
| `deepseek/deepseek-v4-pro-0813` | `deepseek/deepseek-v4-pro-0813.toml` | 更新已有记录 |
| `kimi/kimi-k3` | `moonshotai/kimi-k3.toml` | 更新已有记录 |
| `openai/gpt-6-luna` | `openai/gpt-6-luna.toml` | 更新已有记录 |
| `zai/glm-5.3-flash` | `zhipuai/glm-5.3-flash.toml` | 更新已有记录 |
| `meta/muse-spark-open` | `meta/muse-spark-open.toml` | 更新已有记录 |
| `inception/mercury-3` | `inception/mercury-3.toml` | 更新已有记录 |
| `reflection/Beam-1.0` | `reflection/beam-1.0-501b-a23b.toml` | 跳过，原样保留 |
| `baseten/nemotron-3.5-super-vl-120b-a12b` | `nvidia/nemotron-3.5-super-vl-120b-a12b.toml` | 跳过，原样保留 |
| `thinkingmachines/inkling` | `thinkingmachines/inkling.toml` | 更新精度，补成本并重新核实来源 |
| `thinkingmachines/inkling-small` | `thinkingmachines/inkling-small.toml` | 更新已有记录 |

Qwen 的特殊映射由官方榜单中的模型链接 `alibaba_qwen3.8-max-0902` 及已有相同来源、条件、舍入分数和成本共同核对；没有写入旧 `qwen3.8-max`。Wonder 则核对现有模型档案与 Vals 模型页的身份、发布日期和既有成绩，不匹配 Wonder Full。

## 跳过、冲突和待核实项

1. **MiMo V2.6 Pro / Flash（已按用户要求补录，版本限制仍未解决）**：JSON 分数为 57.813 / 54.826，[Vals 明确通过官方 Xiaomi API 评测](https://www.vals.ai/models/xiaomi_mimo-v2.6-pro)，而本地权重指向 Pro-RL / Flash-RL。已有收集记录指出 API 曾在别名不变的情况下升级至 MOPD；没有取得足以固定 checkpoint 的新证据。按用户明确要求将两条结果记录在相应模型文件中，但通过可进入 JSON 的 variant 明确标注官方 API、checkpoint 未披露、尚未验证为所链接的 RL 权重。保留既有权重链接、模型信息和成绩，不宣称 API 与 RL/MOPD 等价。成本分别为 0.42958 / 0.221007 USD/test，采样参数均为 temperature=1.0、top_p=0.95、max_output_tokens=128000；不补未知 effort、harness 或 date。相关旧问题见 `docs/benchmark-collection/models/xiaomi/`。
2. **Nemotron 3.5 Super VL**：旧值 29.76，JSON 和[当前模型页](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b)为 29.784 / 29.78，不是相同值的舍入。未找到官方修订说明，且未确定评测精度；保留旧记录，不补当前成本或档位。Baseten 是托管商，不新建 Baseten 研发模型。
3. **Beam 1.0**：[Vals 模型页](https://www.vals.ai/models/reflection_Beam-1.0)未把 API 评测精确绑定到本地 `501b-a23b` 权重标识。本次不改写旧 43.42；JSON 的成本为 null，不填零。既有记录保留不意味着精确 checkpoint 已被验证。
4. **GPT-6.1 Terra、Carbon、Mistral OSS 的旧发布更新与当前结果不同**：[Terra](https://www.vals.ai/models/openai_gpt-6.1-terra)旧更新为 60.17，当前 JSON 为 60.536；[Carbon](https://www.vals.ai/models/google_gemini-4-carbon)为 70.36 / 70.45；[Mistral OSS](https://www.vals.ai/models/mistralai_mistral-large-4-oss)为 56.42 / 56.527。此次只新增用户指定当前 JSON 的结果，明确保留差异说明，不声称旧结果有官方更正，也没有把无条件区分的历史数值一并添加成另一运行。后续需要 run ID 或来源修订记录解释。
5. **Hy4 权重状态**：Vals 标 open-weight，本地档案为 false；本次仅补当前评测结果，不据 Vals 修改已有模型基本信息。Vals 模型页说明通过 OpenRouter 访问、成本使用 Tencent 标价，已保留注释。
6. **描述和严格 Schema**：Carbon 的一手模型规格、三个新文件缺失的能力字段仍需核实；不能因基础构建成功就声称上游完整 Schema 兼容。
7. **再分发许可尚未确认**：Vals 公开网页和 JSON 不等同于开放数据授权，Models.dev 的 MIT 许可也不自动覆盖其成绩或成本数据。正式公开再分发前需确认 Vals 的许可或取得授权；模型权重许可与榜单数据许可是两回事。

此前收集报告是当时的历史快照，不批量重写其状态或旧成本统计；本文件记录本次增量事实与仍未解决的问题。

## 首轮实际执行的校验（MiMo 补录前）

- `python3 -B scripts/validate.py`：**867 个 TOML 成功，0 失败**。
- `python3 -B scripts/build.py`：**855 个模型、11 个 Benchmark 定义、1 个语言文件构建成功**。仅原有警告：1,204 条历史成绩未匹配定义、0 条歧义；3 个历史模型描述缺中文翻译。本次未扩大这些数量。
- `python3 -B -m unittest discover -s tests -v`：**104 项通过**。
- `node --test tests/web.test.mjs`：**19 项通过**。
- 独立重新读取 JSON，核对 SHA-256、30 条成绩与成本、原始/新增档位及每条唯一的定义映射；全部一致，新增或补充档位共 14 条。
- 对比 Git HEAD：852 个原有模型的全部基本字段、非 Vals 成绩和已有注释保持不变；4 个跳过文件原样保留；已有 Vals 的其他字段和日期不变，除明确说明的 Inkling 来源修正。
- 本地化核对：原有全部译文、Benchmark 译文不变；新增 3 个键均对应真实新增模型，译文与英文描述逐项核对。
- `dist/models.json` 与全部 855 个模型 TOML 解析值逐个一致，保留字段缺失状态；dist 仅由构建生成，未直接编辑。
- `git diff --check`：无空白错误。

## MiMo 补录后的实际校验

- `python3 -B scripts/validate.py`：867 个 TOML 成功，0 失败。
- `python3 -B scripts/build.py`：855 个模型、11 个定义、1 个语言文件构建成功；仍为原有 1,204 条未匹配、0 条歧义和 3 个描述翻译缺失警告。
- `python3 -B -m unittest discover -s tests -v`：104 项通过。本次数据补录未修改网页代码，未重新运行网页测试；上面的 19 项通过为首轮结果。
- 重新读取源 JSON：32 条同步成绩和成本全部一致；Vals Index v2.2 合计 34 条，其中 Beam、Nemotron 仍为旧记录。
- 对比补录前 Git 暂存区：只改动两个 MiMo 模型文件及本报告；移除新增 Vals 条目后，两个模型的解析内容与补录前完全一致。未修改已有暂存内容的暂存状态。
- 两条新增记录均唯一映射已有定义，不添加未知 effort、harness 或 date；API/checkpoint 限制通过 variant 原样进入构建 JSON。全部 855 个 JSON 模型与 TOML 一致。
- `git diff --check`：无空白错误。只新增成绩，不修改描述或本地化，不新增模型或 Benchmark 定义。

以上不是完整上游严格 Schema 校验，不代表历史成绩真实性已全部重验，也不代表已取得再分发许可。
