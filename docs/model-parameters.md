# 参数量核验方法

[文档导航](README.md) · [字段与组件规范](data-format.md#模型参数量) · [收集状态](model-parameters-status.md) · [待核实事项](review-notes.md)

参数数值及独立来源只维护在模型 TOML。本页保留核验方法和统计边界，不维护覆盖率或参数排名。下列案例来自 2026-11-06 核验，不代表来源和权重状态已持续复核。

## 来源选择

优先使用对应版本的官方模型卡、论文及技术文档。必要时核对完整未量化检查点的 Hugging Face 公共 API，或固定 commit 的实际张量描述元数据；第三方规格需能可靠对应版本。

常用入口：[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)、[GPT-OSS-120B](https://huggingface.co/openai/gpt-oss-120b)、[Mistral](https://docs.mistral.ai/models.md)、[BGE-M3](https://bge-model.com/bge/bge_m3.html)、[Whisper](https://github.com/openai/whisper/blob/main/README.md)、[Hub API 示例](https://huggingface.co/api/models/meta-llama/Llama-3.1-70B-Instruct)、[OpenRouter 目录](https://openrouter.ai/api/v1/models)。具体数值仍以各模型的 `sources`、`notes` 为准。

### 不同口径不强行统一

- 官方架构/名义规模、包含 Embedding 的完整权重数及带辅助预测模块的发行包可能不同；保留来源精度与范围。
- Hub 的 `safetensors.parameters` / `safetensors.total` 必须核对检查点身份、完整性、浮点类型与统计自洽性。整数索引不是模型参数，量化打包元素数不能直接当参数量；API 冲突时不能任选一项。
- 模型卡的近似规格可单独采用并注明，但不借用相近 Base、Instruct、Thinking 或更新版本。BF16 规格仅可用于明确关联的同一 FP8 版本。
- 不相加独立可选草稿模型、辅助适配器或同一模型的不同格式；也不能遗漏目标检查点必需的编码器或决策头。
- 预填充与解码激活量分别说明。DeepSeek V4.1 的 backbone 规格不能冒充完整总量。
- 浮动别名及速度档位仅在有可靠版本映射时补充，不能保证未来部署不变。例如 [DeepSeek 2026-02-04 价格表存档](https://web.archive.org/web/20260204135805id_/https://api-docs.deepseek.com/quick_start/pricing/)与[发行公告](https://api-docs.deepseek.com/news/news251201)支持当时 chat/reasoner → V3.2 映射，不证明当前服务仍相同。
- 第三方页面标题也可能随版本变动；历史核验时 [AA DeepSeek V4 Pro](https://artificialanalysis.ai/models/deepseek-v4-pro)对应 0813 Max，不能套给较早 Preview。

## 固定检查点的张量元数据核验

只核对真实权重的描述与形状，不从层数、名称、字节数或量化位宽估算，不运行模型。

1. 从 `sources` 的固定 commit 文件/索引确定目标范围，读取 `weight_map`，确认文件集合和张量名称，不混入其他格式、组件或检查点。
2. safetensors：前 8 字节为 little-endian JSON 头长度。用有界 HTTP Range，检查响应状态、`Content-Range` 和头部完整性，读取 `dtype`、`shape`、名称；按真实浮点权重的 `math.prod(shape)` 逐项计数，检查权重、偏置及其他可训练参数，排除已确认的索引缓冲区。
3. 分片求和仅用于恢复**同一检查点或组件**的数值，不是组件求和填父表。张量名须与索引严格一致，无缺片、重复或遗漏必需模块。独立核实的未量化组件可单记，但不推算量化部分。
4. PyTorch ZIP：只用受限、惰性的 `data.pkl` 描述解析器，不运行任意 pickle 对象、不使用不受限的 `torch.load`。既有核验只允许 `collections.OrderedDict`、Float/Half/BFloat16 Storage 标签和返回描述字典的 `_rebuild_tensor_v2` 替身；storage 引用只作描述，不加载真实张量。其他全局对象、未解释的共享存储/张量或缓冲区应拒绝，不能默认为独立权重。
5. 核对全部分片，记录固定版本、范围、排除项与统计口径到 `notes`。无法安全解释或存在未解决矛盾时跳过并报告，不为覆盖率放宽检查。

有界前缀可能包含少量相邻权重字节，不能声称完全未传输权重字节；也不等于下载了完整权重。历史复算示例及执行记录可从 [Git 中的原核验报告](https://github.com/chenlongapps/model-atlas-data/blob/0f218c077a8d290d7de6618026928555d7fec336/docs/model-parameters.md)查阅。

### 处理过的统计冲突

| 案例 | 处理依据与边界 |
| --- | --- |
| AutoGLM Phone Multilingual | 五个固定 BF16 分片的 weight/bias 计数支持完整多模态检查点，不采用异常偏小的 Hub total |
| MiMo V2.5 ASR | 七个 F32 分片且 `tie_word_embeddings = false`；另需 Audio Tokenizer，因此只记录 ASR 组件，不补管线总量 |
| MythoMax、ReMM、Euryale v2.2、Nemotron Mini | 核对全部 PyTorch 描述及索引，不按名称或基础模型规模推算 |
| Ornith 1.0 9B / 35B | Hub 统计冲突，改用[作者正文明确披露的近似规格](https://deep-reinforce.com/ornith_1_0.html)，在 notes 说明口径 |
| Bison-1 / Groundhog-1 / Turion Jev 31B | Gemma 4 系 tied embeddings 在两个分片合计中重复计数；采用固定索引去重后的总量，并按官方 31B/26B 口径记录 |
| Hy4 / Hy4 Flash | 官方表分别列出语言骨干、Engram、ViT 与 DFly2；完整检查点统计与官方组件口径分开保留，不自行把组件相加当总量 |
| DiffusionGemma 26B A4B | 卡面 25.2B 加约 0.55B 视觉编码器；固定 BF16 检查点 25.82B，差异按视觉编码器解释 |

## 组件范围

以下已核验范围不能当作完整模型总量；详细数值及固定文件来源仍在模型 TOML：

| 模型组 | 仅已核实的范围 |
| --- | --- |
| Qwen Image 2.1 / Turbo、FLUX 系列 | 视觉生成组件或 rectified-flow/image transformer，不含完整编码管线 |
| FIBO、Krea 2 Turbo、MiniMax H3 | 官方 DiT / diffusion / Omni-Transformer 规格 |
| SDXL-Lightning | 不同步数的 U-Net 是互斥检查点，不能相加或默选步数 |
| DreamShaper 8 LCM / SDXL Base | 实测 U-Net，不累加单文件/组件格式，不补造编码器规模 |
| Clef / Clef Flash、pplx-decider | 骨干与独立 joint/readout head 分别核验，不相加填父表 |
| OmniVoice | 语音生成检查点与 Audio Tokenizer 分别核验，排除 I64 codebook offsets |
| Macaron V1 Tall | 四个 LoRA 专家分别记录，不把名义骨干加 LoRA footprint 当完整总量 |
| Pixtral 12B / GLM Image | 官方 decoder/vision 或 autoregressive/diffusion 组件，不自行汇总 |
| DeepSeek V4 Flash Vision Exp | 全部未量化 `vision.*`、`aligner.*` 与索引核对，不推算量化语言部分及 DSpark 总量 |
| MiMo V2.5 ASR | ASR 检查点，不含另行下载的 Audio Tokenizer |
| Qwen-Image、MiniMax H3 Image、Ternary Bonsai 27B | 视觉生成或语言组件分别核验，完整管线总量未合并；Ternary Bonsai 的量化打包计数不展开 |

## 参数规格不证明权重状态

以下来源可支持命名模型的参数规格，但不证明权重公开、服务内部文件或精确序列化计数：

| 模型 | 依据与仍需保留的限制 |
| --- | --- |
| `deepreinforce/ornith-1.0-31b` | [固定官方 README](https://github.com/ornith-ai/Ornith-1/blob/d196d60faa9ee1b1daa811e8b552b4ee203b1272/README.md)与[发行公告](https://ornith.ai/ornith_1_0.html)披露近似架构规格；核验时未找到可访问的 31B 权重，不能据此验证 `open_weights` |
| `mistral/ministral-3b` | [OpenRouter 精确版本页](https://openrouter.ai/mistralai/ministral-3b)与[官方文档](https://docs.mistral.ai/models/ministral-3b-24-1.md)对应 2024 版，不借用 2025 替代版计数；权重公开及许可待核实 |
| `nvidia/nemotron-3.5-super-120b-a12b` | [NVIDIA 架构规格](https://developer.nvidia.com/nemotron)及[Perplexity 文本服务映射](https://docs.perplexity.ai/docs/agent-api/models.md)；不推断服务移除了视觉组件，不自行扣除编码器参数 |
| `sdaia/allam-2-7b` | [Groq 精确 ID 模型卡](https://console.groq.com/docs/model/allam-2-7b)正文披露规模；不改用 ALLaM-7B-Instruct-preview，本地权重链接仍待核实 |

历史基本信息与目标权重年代不一致的条目（如 `mistral/mistral-large-latest`）仍需复核，不据日期自行换模型。`microsoft/wizardlm-2-8x22b` 的第三方重传来源也不因参数计数获得出处或再分发许可认证。模型权重许可始终以对应官方资料为准。
