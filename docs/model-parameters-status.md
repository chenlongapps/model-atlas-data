# 开放权重模型参数量收集与同步状态

[文档导航](README.md) · [字段与组件规范](data-format.md#模型参数量) · [核验方法](model-parameters.md) · [待核实事项](review-notes.md)

本页是 `open_weights = true` 模型参数量收集的长期进度台账，记录字段覆盖、收集状态和同步状态，不复制参数数值。数值、来源及详细限制以 `models/<lab>/<model-id>.toml` 的 `[metadata.modelatlas.parameters]` 为准。

## 统计口径

- 扫描 `models/` 下全部 TOML，只统计 `open_weights = true` 的模型；模型 ID 直接使用文件路径，不另起名称。
- 按 `release_date` 倒序排列，同日按模型 ID 升序；日期缺失的模型排在最后。
- `total_billion` 是完整模型总参数量，也是收集完成的核心口径；`active_billion` 只在来源明确披露时记录，不默认等于总参数量，也不因缺失把模型判为未完成。
- `components` 是可选补充信息，记录独立组件或管线范围，不求和填入完整总量，不影响整体完成状态。
- 字段列中的 `✅` 表示 TOML 已有该字段，`—` 表示缺失；缺失不代表 `0`，也不代表可以用其它字段推算。

### 收集状态

| 状态 | 含义 |
| --- | --- |
| ✅ 已收集 | `total_billion` 已记录；激活量是否单列不改变该状态 |
| ⚠️ 待核实 | 尚无完整总量，只记录了 `active_billion`；总量或来源仍需核实 |
| ❌ 待收集 | 尚无任何参数量记录，需要从头收集 |
| 🔒 官方未披露 | 只有组件等局部数值，已确认无法从官方来源核实完整总量 |
| ➖ 不适用 | 人工确认该模型或字段不需要按此口径收集 |

### 同步状态

| 状态 | 含义 |
| --- | --- |
| 待写入 | 参数已核实但尚未写入模型 TOML（仅人工标记） |
| 已入库 | 参数字段已存在于模型 TOML |
| 已构建 | 通过 `--dist` 指定的 `models.json` 中对应参数与 TOML 一致（脚本检查） |
| 已发布 | 人工确认发布包包含该参数；不能仅因网页可访问就标记 |
| 未核验 | 尚未核对构建或发布；无参数时默认使用 |

**字段存在不代表来源已经核实，已入库不代表已发布。** 构建成功只说明结构与序列化通过，不证明模型卡、论文或权重仓库支持该数值。

### 核验日期与备注

最近核验日期只在人工确认后写入备注，格式为 `核验 YYYY-MM-DD`。不从文件修改时间、模型发布日期、构建时间或本次扫描时间推断核验日期。备注中的 `来源 N` 是该参数表（含组件）去重后的来源 URL 数，详细口径仍看 TOML 的 `sources` 与 `notes`。

> 下面的统计和清单由脚本生成，不要直接编辑；人工结论写入后文的记录块或特殊情况说明，避免下次生成时被覆盖。

<!-- parameters-status:begin -->

## 总体进度

> 自动统计当前 `models/` 目录：扫描 987 个模型 TOML，其中 421 个 `open_weights = true`。数值及来源以各模型 TOML 为准，本页不复制参数值。

| 指标 | 数值 | 说明 |
| --- | ---: | --- |
| 开放权重模型总数 | 421 | 当前追踪范围 |
| 已完成模型数 | 388 | ✅ 已收集；`total_billion` 已记录 |
| 部分完成模型数 | 2 | ⚠️ 待核实；缺完整总量，仅记录激活量 |
| 待收集模型数 | 2 | ❌ 待收集；尚无任何参数量记录 |
| 无法获取参数的模型数 | 29 | 🔒 官方未披露；仅组件等，完整总量未披露 |
| 不适用模型数 | 0 | ➖ 不适用；人工确认无需收集 |
| 总参数量覆盖率 | 92.2% | `total_billion` 存在：388 / 421 |
| 激活参数量覆盖率 | 32.1% | `active_billion` 存在：135 / 421 |
| 总量已收集但激活量缺失 | 255 | 已计入 ✅；不推定等于总参数量，按独立覆盖率统计 |
| 组件参数量记录数 | 7.4% | `components` 非空：31 / 421；可选字段，不计入完成率 |
| 整体收集完成率 | 92.2% | `✅ 已收集 / 总数` |
| 已确定率 | 99.0% | `(✅ 已收集 + 🔒 官方未披露 + ➖ 不适用) / 总数`，表示无需继续收集 |
| 待处理率 | 1.0% | `(⚠️ 待核实 + ❌ 待收集) / 总数` |

收集完成以 `total_billion` 为核心口径；`active_billion` 只在来源披露时记录，不推定等于总参数量，也不因缺失单独判为模型未完成。已收集总量但未单列激活量的模型仍计入 ✅，激活量缺口由单独的覆盖率反映，避免把稠密模型或来源未单列激活量的模型误判为未完成。

同步状态分布：待写入 0，已入库 419，已构建 0，已发布 0，未核验 2。

## 模型收集清单

按 `release_date` 倒序；同日按模型 ID 升序。字段列中的 `✅` 表示 TOML 已有该字段，`—` 表示缺失，不代表 `0`，也不代表字段之间可以互相推算。

| 模型 ID | 总参数量 | 激活参数量 | 组件参数量 | 收集状态 | 同步状态 | 备注 |
| --- | :---: | :---: | :---: | --- | --- | --- |
| `baseten/bison-1` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；官方 31B；Hub 分 dtype 合计因 tied embeddings 重复计数偏大，采用索引去重总量；来源 1；未单列激活量；TOML 备注 |
| `baseten/groundhog-1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；官方 26B，约 4B 激活；同为 Gemma 4 系 tied embeddings 检查点；来源 1；TOML 备注 |
| `thinkingmachines/inkling-2-mini` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `tencent/hy4-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `minimax/MiniMax-H3-Image` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 核验 2026-11-25；仅记录 33.1B diffusion transformer；完整管线总量未披露；仅组件 1 项；来源 1；TOML 备注 |
| `minimax/MiniMax-H3-Image-Highspeed` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 核验 2026-11-25；与 MiniMax-H3-Image 共用检查点；仅记录 33.1B diffusion transformer；仅组件 1 项；来源 1；TOML 备注 |
| `butler/cicero` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `thinkingmachines/inkling-2-small` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `ricursiveai/ripple-65b-preview` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `tencent/hy4` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；官方 770B 骨干 + ViT/DFly2；完整检查点 774.43B，激活为 49B 文本 + 1.23B 视觉；来源 2；TOML 备注 |
| `sarvam/sarvam-prism` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；FP8 固定发布：骨干与 decision head 合计 105.02B，官方未单列激活量；来源 3；未单列激活量；TOML 备注 |
| `mistral/mistral-large-4-1t-a52b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `baseten/joey-1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `turion/turion-extract-alpha` | — | — | — | ❌ 待收集 | 未核验 | 核验 2026-11-25；LoRA adapter 加提取头，官方未披露合并后完整总量；尚无参数记录 |
| `turion/turion-jev-31b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；官方 31B；采用固定检查点索引的去重总量；来源 1；未单列激活量；TOML 备注 |
| `moonshotai/kimi-k3.1-pro` | ✅ | ✅ | ✅ | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `recursive/flint` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepreinforce/ornith-1.5-122b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；官方 122B；Hub BF16 为 125.09B，差异未解释，保留官方口径；来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-3.5-embed-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baseten/elephant-1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `baseten/mammoth-1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `minimax/MiniMax-M3.1-Flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `nvidia/nemotron-3.5-embed-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `deepseek/deepseek-v4.1-flash-1017` | — | ✅ | ✅ | ⚠️ 待核实 | 已入库 | 仅激活量；来源 3；TOML 备注 |
| `black-forest-labs/flux-3-image-klein` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `meta/muse-spark-open` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-3.5-super-120b-a12b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 核验 2026-11-06；架构规格不证明服务移除了视觉组件，不自行扣除编码器参数；来源 2；TOML 备注 |
| `nvidia/nemotron-3.5-super-vl-120b-a12b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `perplexity/pplx-decider-flash-v1.2` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 3；TOML 备注 |
| `perplexity/pplx-decider-v1.2` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 3；TOML 备注 |
| `respan/span-02` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `swiss-ai/apertus-v1.5-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；仓库 gated 且模型卡不可读；采用完整 BF16 仓库统计 8.90B，含视觉与音频 tokenizer；来源 1；未单列激活量；TOML 备注 |
| `vllm-sr/d3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `vllm-sr/d3-flash` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `vllm-sr/d3-mini` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen-image-2.1-turbo` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `lightonai/lightonocr-3-0.8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `phocinae/phocinae-largha-150m-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `openbmb/minicpm-v-4.7-35b-a3b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/embeddinggemma-2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nace-ai/drex-v2.0` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `openbmb/minicpm-v-4.7-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-large-4` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `reflection/beam-1.0-501b-a23b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `aleph-alpha/kolibri-1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `pixilabai/blink-v0.3-26b-a4b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `cloudflare/clef` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 3；TOML 备注 |
| `cloudflare/clef-flash` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 3；TOML 备注 |
| `inclusionai/ling-3.1-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `nace-ai/drex-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `jaredpalmer/kev-4b` | — | — | — | ❌ 待收集 | 未核验 | 核验 2026-11-25；LoRA adapter 加指针头，官方未披露合并后完整总量；尚无参数记录 |
| `xiaomi/mimo-v2.6-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `xiaomi/mimo-v2.6-pro` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `xiaomi/mimo-v2.6-pro-ultraspeed` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `surogate/rune-26b-a4b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `stepfun/step-5-preview` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen-image-2.1` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `deepseek/deepseek-v4.1-flash` | — | ✅ | — | ⚠️ 待核实 | 已入库 | 仅激活量；来源 1；TOML 备注 |
| `inclusionai/ling-3.0-flash-vl` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `cohere/north-small-translate-1-0` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `openbmb/minicpm5-2b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `tencent/hy4-preview` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3.8-flash-next` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `inclusionai/ling-3.0-flash-fin` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `zhipuai/glm-5.3-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `ibm/granite-4.2-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `apodex/apodex-1.1-mini` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `bria/fibo-generate-1.5` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `deepseek/deepseek-v4-flash-vision-exp` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 2；TOML 备注 |
| `deepreinforce/ornith-1.5-35b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `alibaba/qwen3.8-27b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `zhipuai/glm-5.3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `deepseek/deepseek-v4-pro-0813` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `alibaba/qwen3.8-2.4t-a95b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `nvidia/nemotron-3.5-lightning` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `meta/muse-glimmer-30b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `inclusionai/ling-3.0-tiny` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `motif-technologies/motif-3` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `deepseek/deepseek-v4-flash-0731` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `huawei/openpangu-2.0-pro` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `minimax/MiniMax-H3` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `thinkingmachines/inkling-small` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `swiss-ai/apertus-v1.5-70b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；仓库 gated 且模型卡不可读；采用完整 BF16 仓库统计 72.01B，含视觉与音频 tokenizer；来源 1；未单列激活量；TOML 备注 |
| `inclusionai/ling-3.0-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `mindlab/macaron-v1-tall` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 4 项；来源 1；TOML 备注 |
| `mindlab/macaron-v1-venti` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `poolside/laguna-s-2.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `moonshotai/kimi-k3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-3-embed-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-3-embed-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `thinkingmachines/inkling` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `cohere/cohere-transcribe-arabic-07-2026` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `tencent/hy3` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `prism-ml/ternary-bonsai-27b` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 核验 2026-11-25；仅记录语言权重与视觉塔组件；完整总量未披露，量化打包计数不展开；仅组件 2 项；来源 1；TOML 备注 |
| `poolside/laguna-xs-2.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `huawei/openpangu-2.0-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `meituan/longcat-2.0` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepreinforce/ornith-1.0-35b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-06；Hub 统计冲突，采用作者披露的近似规格；来源 1；未单列激活量；TOML 备注 |
| `deepreinforce/ornith-1.0-397b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `deepreinforce/ornith-1.0-9b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-06；Hub 统计冲突，采用作者披露的近似规格；来源 1；未单列激活量；TOML 备注 |
| `liquid/lfm2.5-embedding-350m` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `zhipuai/glm-5.2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `moonshotai/kimi-k2.7-code` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `moonshotai/kimi-k2.7-code-highspeed` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `cohere/north-mini-code-1-0` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `google/diffusiongemma-26b-a4b-it` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 核验 2026-11-25；官方 25.2B 加约 0.55B 视觉编码器；固定 BF16 检查点 25.82B，激活 3.8B；来源 2；TOML 备注 |
| `google/gemma-4-12b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `xiaomi/mimo-v2.5-pro-ultraspeed` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `krea/krea-2-medium-turbo` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `nex-agi/nex-n2-pro` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-3.5-content-safety` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `minimax/MiniMax-M3` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `stepfun/step-3.7-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `tencent/hy-mt2-1.8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `tencent/hy-mt2-30b-a3b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `tencent/hy-mt2-7b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/command-a-plus-05-2026` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `openbmb/minicpm5-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-medium-2604` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `mistral/mistral-medium-3-5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-medium-latest` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `poolside/laguna-m.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `poolside/laguna-xs.2` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `deepseek/deepseek-v4-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `deepseek/deepseek-v4-pro` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepseek/deepseek-v4-flash-0423` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepseek/deepseek-v4-pro-0423` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `xiaomi/mimo-v2.5-asr` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 2；TOML 备注 |
| `alibaba/qwen3.6-27b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `xiaomi/mimo-v2.5` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `xiaomi/mimo-v2.5-pro` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `moonshotai/kimi-k2.6` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `tencent/hy3-preview` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `alibaba/qwen3.6-35b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `resemble-ai/chatterbox-nano` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `zhipuai/glm-5.1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-4-26b-a4b-it` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `google/gemma-4-31b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-4-E2B-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-4-E4B-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `stepfun/step-3.5-flash-2603` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `arcee-ai/trinity-large-thinking` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `k2-fsa/omnivoice` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 2；TOML 备注 |
| `cohere/cohere-transcribe-03-2026` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `mistral/voxtral-mini-tts-2603` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-cascade-2-30b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `minimax/MiniMax-M2.7` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `minimax/MiniMax-M2.7-highspeed` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `mistral/mistral-small-2603` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `mistral/mistral-small-latest` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `nvidia/nemotron-3-content-safety` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `nvidia/nemotron-voicechat` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `rekaai/reka-edge` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3.5-0.8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3.5-2b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3.5-4b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `fish-audio/s2-pro` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3.5-9b-base` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `perplexity/pplx-embed-context-v1-0.6b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `perplexity/pplx-embed-context-v1-4b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `perplexity/pplx-embed-v1-0.6b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `perplexity/pplx-embed-v1-4b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3.5-35b-a3b-base` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `liquid/lfm2-24b-a2b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `alibaba/qwen3.5-122b-a10b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3.5-27b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3.5-35b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3.5-9b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `trendyol/asure-12b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sarvam/sarvam-105b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `sarvam/sarvam-30b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/tiny-aya-earth` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/tiny-aya-fire` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/tiny-aya-global` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/tiny-aya-water` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3.5-397b-a17b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `minimax/MiniMax-M2.5-highspeed` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `minimax/MiniMax-M2.5` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `zhipuai/glm-5` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `mistral/voxtral-mini-transcribe-realtime-2602` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-coder-next` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `stepfun/step-3.5-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `arcee-ai/trinity-large-preview` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepseek/deepseek-ocr-2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `moonshotai/kimi-k2.5` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `nvidia/nemotron-content-safety-reasoning-4b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `zhipuai/glm-4.7-flash` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `zhipuai/glm-4.7-flashx` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `lightonai/lightonocr-2-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `black-forest-labs/flux-2-klein-4b` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `black-forest-labs/flux-2-klein-9b` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `zhipuai/glm-image` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 1；TOML 备注 |
| `ai21/jamba-mini` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3-asr-0.6b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-asr-1.7b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `minimax/MiniMax-M2.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `zhipuai/glm-4.7` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/llama-nemotron-embed-vl-1b-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/llama-nemotron-rerank-vl-1b-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `xiaomi/mimo-v2-flash` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `zhipuai/autoglm-phone-9b-multilingual` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/devstral-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/devstral-small-2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `zhipuai/glm-4.6v` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `zhipuai/glm-4.6v-flash` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `essentialai/rnj-1-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/devstral-medium-latest` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/ministral-14b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/ministral-14b-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/ministral-3-14b-instruct-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/ministral-3-3b-instruct-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/ministral-3-8b-instruct-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/ministral-3b-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/ministral-8b-2512` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/mistral-large-2512` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `arcee-ai/trinity-mini` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `arcee-ai/trinity-nano-preview` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepseek/deepseek-chat` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 3；TOML 备注 |
| `deepseek/deepseek-reasoner` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 3；TOML 备注 |
| `deepseek/deepseek-v3.2` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `black-forest-labs/flux-2-dev` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `moonshotai/kimi-k2-thinking` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `moonshotai/kimi-k2-thinking-turbo` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `openai/gpt-oss-safeguard-120b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `openai/gpt-oss-safeguard-20b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `nvidia/llama-3.1-nemotron-safety-guard-8b-v3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `nvidia/nemotron-nano-12b-v2-vl` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `minimax/MiniMax-M2` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `allenai/olmocr-2-7b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `nvidia/llama-nemotron-embed-1b-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `paddlepaddle/paddleocr-vl` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-vl-30b-a3b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `ibm/granite-4-h-micro` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `ibm/granite-4-h-small` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `zhipuai/glm-4.6` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `thedrummer/cydonia-24b-v4.1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `aisingapore/gemma-sea-lion-v4-27b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-vl-235b-a22b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-vl-235b-a22b-thinking` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-omni-30b-a3b-thinking` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/magistral-small-2509` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `opendatalab/mineru2.5-2509-1.2b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `moonshotai/kimi-k2-0905` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `google/embeddinggemma-300m` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `swiss-ai/apertus-70b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `swiss-ai/apertus-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-next-80b-a3b-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3-next-80b-a3b-thinking` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `cohere/command-a-translate-08-2025` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `nousresearch/hermes-4-405b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/command-a-reasoning-08-2025` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `deepseek/deepseek-chat-v3.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `deepseek/deepseek-v3.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `bytedance-seed/seed-oss-36b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen-image` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 核验 2026-11-25；仅记录 visual transformer、文本编码器与 VAE 组件；完整管线总量未披露；仅组件 3 项；来源 4；TOML 备注 |
| `nvidia/nemotron-nano-9b-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baichuan/baichuan-m2-32b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `zhipuai/glm-4.5v` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `openai/gpt-oss-120b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `openai/gpt-oss-20b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `nvidia/parakeet-tdt-0.6b-v3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-coder-30b-a3b-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `cohere/command-a-vision-07-2025` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-30b-a3b-instruct-2507` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `zhipuai/glm-4.5` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `zhipuai/glm-4.5-air` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3-235b-a22b-thinking-2507` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-coder-480b-a35b-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3-235b-a22b-instruct-2507` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `mistral/voxtral-mini-3b-2507` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/voxtral-small-24b-2507` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/voxtral-small-latest` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `moonshotai/kimi-k2` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `moonshotai/kimi-k2-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `mistral/devstral-small-2507` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cognitivecomputations/dolphin-mistral-24b-venice-edition` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `ai21/jamba-large` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `baidu/ernie-4.5-21b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `baidu/ernie-4.5-300b-a47b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `baidu/ernie-4.5-vl-424b-a47b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `google/gemma-3n-e2b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-3n-e4b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-small-2506` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-small-3.2-24b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `minimax/minimax-m1-80k` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `mistral/magistral-small-2506` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-embedding-0.6b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-embedding-4b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-embedding-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-reranker-0.6b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen3-reranker-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `black-forest-labs/flux-1-kontext-dev` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `deepseek/deepseek-r1-0528-qwen3-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `deepseek/deepseek-r1-0528` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `sarvam/sarvam-m` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `meta/llama-guard-4-12b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `meta/llama-prompt-guard-2-22m` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-prompt-guard-2-86m` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen3-235b-a22b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3-30b-a3b` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `alibaba/qwen3-32b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `nvidia/llama-3.1-nemotron-70b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `pfnet/plamo-embedding-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/llama-3.1-nemotron-ultra-253b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `meta/llama-4-maverick-17b-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1；TOML 备注 |
| `meta/llama-4-scout-17b-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `deepseek/deepseek-chat-v3-0324` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `deepseek/deepseek-v3-0324` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `nvidia/llama-3.3-nemotron-super-49b-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-small-3-1-24b-instruct-2503` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `mistral/mistral-small-3.1-24b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/command-a` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/command-a-03-2025` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `google/gemma-3-12b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-3-27b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-3-4b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `rekaai/reka-flash-3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `thedrummer/skyfall-36b-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwq-32b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/c4ai-aya-vision-32b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/c4ai-aya-vision-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `canopylabs/orpheus-3b-0.1-ft` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sesame/csm-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/command-r7b-arabic-02-2025` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `microsoft/phi-4-mini` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `microsoft/phi-4-multimodal-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `aion-labs/aion-rp-llama-3.1-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-small-24b-instruct-2501` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen2-5-vl-72b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sdaia/allam-2-7b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-06；Groq 精确 ID 模型卡支持 7B 规格；本地权重链接仍待核实；来源 1；未单列激活量；TOML 备注 |
| `deepseek/deepseek-r1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `deepseek/deepseek-r1-distill-qwen-32b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `deepseek/deepseek-v3` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `sao10k/l3.3-euryale-70b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/command-r7b-12-2024` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.3-70b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `hexgrad/kokoro-82m` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `mistral/mistral-large-2411` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen2.5-coder-0.5b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `alibaba/qwen2.5-coder-32b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `thedrummer/unslopnemo-12b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `mistral/mistral-large-latest` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 核验 2026-11-06；别名对应检查点与历史基本信息年代仍需复核；来源 1；TOML 备注 |
| `mistral/pixtral-large-latest` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `cohere/c4ai-aya-expanse-32b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/c4ai-aya-expanse-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `anthracite-org/magnum-v4-72b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/ministral-8b-instruct-2410` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `openai/whisper-large-v3-turbo` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.2-11b-vision-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.2-1b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.2-1b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.2-3b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.2-3b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.2-90b-vision-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `alibaba/qwen2.5-7b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `mistral/pixtral-12b` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 2 项；来源 1；TOML 备注 |
| `cohere/command-r-08-2024` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `cohere/command-r-plus-08-2024` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `sao10k/l3.1-euryale-70b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nvidia/nemotron-mini-4b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nousresearch/hermes-3-llama-3.1-70b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nousresearch/hermes-3-llama-3.1-405b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `abacusai/dracarys-llama-3.1-70b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sao10k/l3-lunaris-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `black-forest-labs/flux-1-dev` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `black-forest-labs/flux-1-schnell` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `google/gemma-2-2b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baai/bge-en-icl` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baai/bge-multilingual-gemma2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-large-2407` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `meta/llama-3.1-70b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-3.1-8b-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `meta/llama-guard-3-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-nemo` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `google/gemma-2-27b-it` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/codestral-22b-v0.1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/codestral-latest` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mistral-7b-instruct-v0.3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nousresearch/hermes-2-pro-llama-3-8b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 2；未单列激活量；TOML 备注 |
| `alibaba/gte-large-en-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mistral/mixtral-8x22b-instruct` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 1 |
| `microsoft/wizardlm-2-8x22b` | ✅ | — | — | ✅ 已收集 | 已入库 | 核验 2026-11-06；参数计数来自第三方重传检查点，不代表原始出处或再分发许可；来源 1；未单列激活量；TOML 备注 |
| `baai/bge-reranker-v2-m3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `mixedbread/mxbai-embed-large-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `bytedance-seed/stable-diffusion-xl-lightning` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 4 项；来源 5；TOML 备注 |
| `nomic-ai/nomic-embed-text-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `intfloat/multilingual-e5-large-instruct` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `nomic-ai/nomic-embed-text-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baai/bge-m3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `upstage/solar-10.7b-instruct-v1.0` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量 |
| `mistral/mixtral-8x7b-instruct-v0.1` | ✅ | ✅ | — | ✅ 已收集 | 已入库 | 来源 2；TOML 备注 |
| `lykon/dreamshaper-8-lcm` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `whereisai/uae-large-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `openai/whisper-large-v3` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baai/bge-base-en-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baai/bge-large-en-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `baai/bge-small-en-v1.5` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `gryphe/mythomax-l2-13b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `stabilityai/stable-diffusion-xl-base-1.0` | — | — | ✅ | 🔒 官方未披露 | 已入库 | 仅组件 1 项；来源 1；TOML 备注 |
| `undi95/remm-slerp-l2-13b` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `thenlper/gte-base` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `thenlper/gte-large` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `intfloat/multilingual-e5-large` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `intfloat/e5-base-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `intfloat/e5-large-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `openai/whisper-tiny` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `shibing624/text2vec-base-chinese` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/all-minilm-l12-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/all-minilm-l6-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/all-mpnet-base-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/multi-qa-mpnet-base-dot-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/clip-vit-b-32` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/clip-vit-b-32-multilingual-v1` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |
| `sentence-transformers/paraphrase-minilm-l6-v2` | ✅ | — | — | ✅ 已收集 | 已入库 | 来源 1；未单列激活量；TOML 备注 |

<!-- parameters-status:end -->

## 特殊情况与处理结论

以下清单是 2026-11-25 建立台账时的快照，并包含同日补充的 `alibaba/qwen-image`、`minimax/MiniMax-H3-Image`、`minimax/MiniMax-H3-Image-Highspeed`、`prism-ml/ternary-bonsai-27b`；结论来自现有模型 TOML 和专题核验记录。后续新增或状态变化以自动生成的表为准；自动扫描不应覆盖这里的判断，也不应为了覆盖率重复收集或把组件相加。

### 仅公开组件参数量

当前有 29 个模型只记录了 `components`，没有可核实的完整 `total_billion`，状态为 🔒：

- 视觉生成与图像管线：`alibaba/qwen-image`、`alibaba/qwen-image-2.1`、`alibaba/qwen-image-2.1-turbo`、`black-forest-labs/flux-1-dev`、`black-forest-labs/flux-1-kontext-dev`、`black-forest-labs/flux-1-schnell`、`black-forest-labs/flux-2-dev`、`black-forest-labs/flux-2-klein-4b`、`black-forest-labs/flux-2-klein-9b`、`black-forest-labs/flux-3-image-klein`、`bria/fibo-generate-1.5`、`bytedance-seed/stable-diffusion-xl-lightning`、`krea/krea-2-medium-turbo`、`lykon/dreamshaper-8-lcm`、`minimax/MiniMax-H3-Image`、`minimax/MiniMax-H3-Image-Highspeed`、`stabilityai/stable-diffusion-xl-base-1.0`、`zhipuai/glm-image`、`minimax/MiniMax-H3`。
- 语音、ASR 与 decider：`k2-fsa/omnivoice`、`xiaomi/mimo-v2.5-asr`、`cloudflare/clef`、`cloudflare/clef-flash`、`perplexity/pplx-decider-v1.2`、`perplexity/pplx-decider-flash-v1.2`。
- 多模态与 LoRA 发行包：`deepseek/deepseek-v4-flash-vision-exp`、`mindlab/macaron-v1-tall`、`mistral/pixtral-12b`、`prism-ml/ternary-bonsai-27b`。

这些组件可能重叠，也可能只是完整管线的一部分。补总量前必须找到官方完整总量，或按固定检查点核对全部必需组件与张量；不得直接把组件数值相加，也不得把未知部分当作零。

### 仅公开激活量

`deepseek/deepseek-v4.1-flash` 和 `deepseek/deepseek-v4.1-flash-1017` 都没有完整总量，状态为 ⚠️。前者只有 `active_billion`；后者另将官方 552B backbone 记为组件。552B 不含 Engram 与视觉模块，不能当作完整模型总量。`google/diffusiongemma-26b-a4b-it` 已按官方 25.2B 加约 0.55B 视觉编码器与固定 BF16 检查点核对，补为 25.82B。

### 参数规格不证明权重状态

以下模型有参数规格，但来源不足以证明当前权重可访问、版本准确或许可有效；它们仍按仓库现有 `open_weights` 标记纳入统计，不因参数数值获得额外授权：

- `nvidia/nemotron-3.5-super-120b-a12b`：NVIDIA 架构规格和 Perplexity 的精确 ID 映射不能证明服务移除了视觉组件；不自行扣除编码器参数。
- `sdaia/allam-2-7b`：Groq 精确 ID 模型卡支持 7B 规格；本地 Hugging Face 权重链接仍待核实。
- `microsoft/wizardlm-2-8x22b`：参数计数来自第三方重传检查点，不构成原始权重出处或再分发许可认证。
- `mistral/mistral-large-latest`：别名对应检查点与历史基本信息年代仍需复核，不据日期自行替换模型。

### 来源冲突与版本

- `deepreinforce/ornith-1.0-9b`、`deepreinforce/ornith-1.0-35b`：Hub 统计存在冲突，采用作者正文明确披露的近似规格，并在 TOML `notes` 保留口径；不采用 Hub 的异常统计。
- `baseten/bison-1`、`baseten/groundhog-1`、`turion/turion-jev-31b`：Gemma 4 系 tied embeddings 在 Hub 分 dtype 合计中重复计数，采用官方规模与索引去重总量，并在 `notes` 说明。
- `tencent/hy4`、`tencent/hy4-flash`：官方规格表分别列出骨干、Engram、ViT 与 DFly2；完整检查点统计与官方组件口径分开保留。
- `deepreinforce/ornith-1.5-122b`：官方 122B，Hub BF16 检查点 125.09B，差异未解释，保留官方口径。
- `swiss-ai/apertus-v1.5-8b`、`swiss-ai/apertus-v1.5-70b`：仓库 gated 且模型卡不可读，采用完整 BF16 仓库统计，包含视觉与音频 tokenizer。
- `zhipuai/autoglm-phone-9b-multilingual`：采用固定 commit 五个 BF16 分片的权重/偏置计数，不采用异常偏小的 Hub total。
- `xiaomi/mimo-v2.5-asr`：ASR 检查点需要另行下载 Audio Tokenizer，当前只记录 ASR 组件，不补管线总量。
- 其他仍未解决的许可、评测条件和版本冲突见[待核实事项](review-notes.md)；参数核验方法及更多组件范围见[参数量核验](model-parameters.md)。

## 维护方式

本节的人工记录块由人工维护，生成脚本只读取、不覆盖。`notes` 会显示在上表备注列，`status` 和 `sync` 覆盖自动判断；没有列出的模型使用自动判断。只在自动判断不足时添加条目，例如已核实但尚未写入、已确认不适用或需要记录核验日期。模型被移除或不再标记 `open_weights = true` 时，应同时删除其人工记录条目；脚本会拒绝引用未追踪模型的记录，以免静默丢失人工结论。

<!-- parameters-status:manual:begin -->
```toml
# 仅在自动判断不足时添加。id 必须是当前 open_weights 模型的路径 ID。
# status 可选值：✅ 已收集、⚠️ 待核实、❌ 待收集、🔒 官方未披露、➖ 不适用。
# sync 可选值：待写入、已入库、已构建、已发布、未核验。

[[model]]
id = "nvidia/nemotron-3.5-super-120b-a12b"
verified = "2026-11-06"
notes = "架构规格不证明服务移除了视觉组件，不自行扣除编码器参数。"

[[model]]
id = "sdaia/allam-2-7b"
verified = "2026-11-06"
notes = "Groq 精确 ID 模型卡支持 7B 规格；本地权重链接仍待核实。"

[[model]]
id = "microsoft/wizardlm-2-8x22b"
verified = "2026-11-06"
notes = "参数计数来自第三方重传检查点，不代表原始出处或再分发许可。"

[[model]]
id = "mistral/mistral-large-latest"
verified = "2026-11-06"
notes = "别名对应检查点与历史基本信息年代仍需复核。"

[[model]]
id = "deepreinforce/ornith-1.0-9b"
verified = "2026-11-06"
notes = "Hub 统计冲突，采用作者披露的近似规格。"

[[model]]
id = "deepreinforce/ornith-1.0-35b"
verified = "2026-11-06"
notes = "Hub 统计冲突，采用作者披露的近似规格。"

[[model]]
id = "baseten/bison-1"
verified = "2026-11-25"
notes = "官方 31B；Hub 分 dtype 合计因 tied embeddings 重复计数偏大，采用索引去重总量。"

[[model]]
id = "baseten/groundhog-1"
verified = "2026-11-25"
notes = "官方 26B，约 4B 激活；同为 Gemma 4 系 tied embeddings 检查点。"

[[model]]
id = "turion/turion-jev-31b"
verified = "2026-11-25"
notes = "官方 31B；采用固定检查点索引的去重总量。"

[[model]]
id = "tencent/hy4"
verified = "2026-11-25"
notes = "官方 770B 骨干 + ViT/DFly2；完整检查点 774.43B，激活为 49B 文本 + 1.23B 视觉。"

[[model]]
id = "sarvam/sarvam-prism"
verified = "2026-11-25"
notes = "FP8 固定发布：骨干与 decision head 合计 105.02B，官方未单列激活量。"

[[model]]
id = "google/diffusiongemma-26b-a4b-it"
verified = "2026-11-25"
notes = "官方 25.2B 加约 0.55B 视觉编码器；固定 BF16 检查点 25.82B，激活 3.8B。"

[[model]]
id = "deepreinforce/ornith-1.5-122b"
verified = "2026-11-25"
notes = "官方 122B；Hub BF16 为 125.09B，差异未解释，保留官方口径。"

[[model]]
id = "swiss-ai/apertus-v1.5-8b"
verified = "2026-11-25"
notes = "仓库 gated 且模型卡不可读；采用完整 BF16 仓库统计 8.90B，含视觉与音频 tokenizer。"

[[model]]
id = "swiss-ai/apertus-v1.5-70b"
verified = "2026-11-25"
notes = "仓库 gated 且模型卡不可读；采用完整 BF16 仓库统计 72.01B，含视觉与音频 tokenizer。"

[[model]]
id = "alibaba/qwen-image"
verified = "2026-11-25"
notes = "仅记录 visual transformer、文本编码器与 VAE 组件；完整管线总量未披露。"

[[model]]
id = "minimax/MiniMax-H3-Image"
verified = "2026-11-25"
notes = "仅记录 33.1B diffusion transformer；完整管线总量未披露。"

[[model]]
id = "minimax/MiniMax-H3-Image-Highspeed"
verified = "2026-11-25"
notes = "与 MiniMax-H3-Image 共用检查点；仅记录 33.1B diffusion transformer。"

[[model]]
id = "prism-ml/ternary-bonsai-27b"
verified = "2026-11-25"
notes = "仅记录语言权重与视觉塔组件；完整总量未披露，量化打包计数不展开。"

[[model]]
id = "turion/turion-extract-alpha"
verified = "2026-11-25"
notes = "LoRA adapter 加提取头，官方未披露合并后完整总量。"

[[model]]
id = "jaredpalmer/kev-4b"
verified = "2026-11-25"
notes = "LoRA adapter 加指针头，官方未披露合并后完整总量。"
```
<!-- parameters-status:manual:end -->

## 自动更新

```sh
python3 scripts/parameters_status.py          # 按当前 TOML 更新统计和清单
python3 scripts/parameters_status.py --check  # 只检查文档是否与源数据一致
python3 scripts/parameters_status.py --dist dist/models.json  # 额外核对已构建状态
```

脚本只替换 `parameters-status:begin` 与 `parameters-status:end` 之间的内容；人工记录块和本页其余说明不会被覆盖。需要核对构建产物时使用 `--dist dist/models.json`，脚本会用其中的参数与 TOML 对比，匹配时把同步状态标为“已构建”；默认不读取未提交的 `dist/`，以免文档随本地构建状态漂移。`--check` 应与生成时使用相同参数；若文档是用 `--dist` 生成的，复核时也传入同一路径。发布状态仍需人工核对 manifest 或发布包后写入人工记录块。

新增开放权重模型后应运行脚本纳入清单。参数数值或来源发生变化时，先改模型 TOML，再运行脚本；不要把数值抄进本页。