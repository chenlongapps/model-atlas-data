# 开放权重模型参数量核验

核验日期：2026-11-06。范围为当前 `models/` 中 `open_weights = true` 的 **373** 个模型文件，包含聊天、多模态、图像、语音、Embedding、Reranking 和 Decision 模型。

## 当前结果

- **373/373 个模型文件**已有参数信息：345 个提供总量，3 个只提供整模型激活量，25 个仅提供有独立来源的组件参数。完整总量、激活量和组件记录不可混为同一种覆盖；作者的近似架构规格也不能冒充实际检查点精确计数。
- 首轮补入 336 个，后续补入 **37 个**，包括原先的 23 个组件待补项和 14 个来源/版本待确认项。最后一次核实补入 Ornith 31B、2024 年 Ministral 3B、Nemotron 3.5 Super text-only 条目和 ALLaM 2；这四项采用明确披露的架构规格，限制见下文。
- 模型描述、发行日期、能力、权重链接、许可字段及原始 Benchmark 值和文本均未改动。本次新增/修正 Benchmark 成绩 **0/0**，新建 Benchmark 定义 **0**；未改动本地化。
- 参数量的唯一维护位置仍为模型 TOML。本页只记录范围、方法和待核实项，不重复维护参数数值表。

## 来源与统计口径

优先核对官方模型卡、技术资料与文档；必要时使用 Hugging Face 公共 API 对应完整未量化检查点的已发布参数统计、固定 commit 的实际张量描述元数据，或 Artificial Analysis / OpenRouter 中明确对应版本的参数规格。每条数据的具体来源保存在模型文件或组件的 `sources`。

主要入口：

- [Models.dev v2 Schema](https://github.com/anomalyco/models.dev/blob/dev/packages/core/src/schema-v2.ts)：确认可复用 `metadata`，不新增上游顶层字段。
- [DeepSeek-R1 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-R1)、[GPT-OSS-120B 官方模型卡](https://huggingface.co/openai/gpt-oss-120b)：直接披露总量及激活量。
- [Mistral 官方文档](https://docs.mistral.ai/models.md)、[BGE-M3 官方文档](https://bge-model.com/bge/bge_m3.html)、[Whisper 官方模型表](https://github.com/openai/whisper/blob/main/README.md)。
- [Hugging Face 公共模型 API 示例](https://huggingface.co/api/models/meta-llama/Llama-3.1-70B-Instruct)：读取已发布的 `safetensors.parameters` / `safetensors.total`，不是根据模型名、字节数或层数推算。
- [Artificial Analysis MiniMax M2.5 参数规格](https://artificialanalysis.ai/models/minimax-m2-5)、[DeepSeek V3.2 参数规格](https://artificialanalysis.ai/models/deepseek-v3-2)。
- [OpenRouter 公共模型目录](https://openrouter.ai/api/v1/models)：核对版本规格和 `hugging_face_id` 映射，不把 Provider 能力或价格并入模型基本信息。
- [DeepSeek 官方价格表的 2026-02-04 存档](https://web.archive.org/web/20260204135805id_/https://api-docs.deepseek.com/quick_start/pricing/)：明确将 `deepseek-chat` / `deepseek-reasoner` 映射到 V3.2 的非思考/思考模式；结合[官方发行公告](https://api-docs.deepseek.com/news/news251201)，只用于本地记录的历史版本，不保证当前浮动服务仍对应相同模型。
- [Artificial Analysis DeepSeek V4 Pro 页面](https://artificialanalysis.ai/models/deepseek-v4-pro)：本次读取时标题明确为 “DeepSeek V4 Pro 0813 (Max)”，而非较早的 Preview 版本。

### 保留差异，不强制统一

- 官方架构总量、名义规模、包含 Embedding 的完整权重统计，以及带辅助预测模块的发行包，可能不是同一口径。采用哪一项及已知范围写入 `notes`，不能把这些数值混成精确的跨模型排名。
- Hub 统计须核对检查点身份、完整性、浮点数据类型和数字自洽性。仅换算明确发布的数值；整数位置索引等非参数张量排除。量化打包统计、自相矛盾的总量、组件或适配器子集不作为完整总量。
- Ornith 1.0 9B 和 35B 的 Hub 统计存在冲突，但[官方公告](https://deep-reinforce.com/ornith_1_0.html)正文另外明确写出参数规模，故使用作者的近似规格，并在模型 `notes` 中说明没有采用错误的 Hub 统计。
- 模型卡直接披露的近似值保留其精度；不能用组件估算值相加来制造完整总量。官方 BF16 版本可用于其明确关联的同一 FP8 版本，不能把另一个 Base、Instruct、Thinking 或更新版本随意替代。
- 独立可选草稿模型、单独存放的辅助适配器、同一模型的不同文件格式不重复相加。必须核实目标检查点本身是否完整，不能将必需的视觉编码器、决策头等遗漏。
- 推理阶段不同的激活量明确注明。DeepSeek V4.1 只填已核实的激活量及阶段说明，不把官方明确称为 backbone 的数字当作完整总量。
- 浮动别名及速度档位仅在本地已有明确检查点或可靠版本映射时补充，`notes` 标明适用目标，不保证未来别名部署仍相同。已有日期与目标权重年代不一致的字段原样保留，例如 `mistral/mistral-large-latest`；这些历史基本信息仍需人工复核，不能据日期自行换成另一个模型版本。

### 独立张量元数据核验

本轮核验固定 commit 的 54 个 safetensors 文件头，以及 47 个 PyTorch ZIP 检查点的 `data.pkl` 描述。没有下载完整权重文件、创建真实张量或运行模型。PyTorch 和个别 safetensors 核验使用有界文件前缀，可能包含少量相邻权重字节；只有描述元数据被解释和计数，不能表述为完全没有传输任何权重字节。

复核步骤：

1. 从 `sources` 的 `/blob/<commit>/...` 取得固定仓库版本，读取索引的 `weight_map`，确认目标组件、文件集合和张量名称，不混入另一格式或检查点。
2. safetensors 的前 8 字节是 little-endian JSON 头部长度。只请求有界 HTTP Range、检查状态及 `Content-Range`，解析 JSON 的 `dtype`、`shape`、名称。逐张量计算 `math.prod(shape)`；按 dtype 和组件分别记录，检查权重/偏置及其他可训练参数，排除已确认的索引缓冲区。未量化组件可以在同一仓库的其他部分量化时单独核验，不能据其推算量化部分的参数。
3. 分片的和只用于恢复**同一检查点/组件**的权重数，不是把不同组件相加填父表。必须检查张量名集合与索引严格相等、没有缺片或重复、统计范围不漏掉必需模块。
4. PyTorch ZIP 从有界前缀定位未压缩的 `data.pkl`，不使用不受限的 pickle 或 `torch.load`。本次受限解析器只允许 `collections.OrderedDict`、三个惰性的 Float/Half/BFloat16 Storage 标签和返回描述字典的 `_rebuild_tensor_v2` 替身；持久化 storage 引用仅保存为描述，不加载任何 storage。拒绝其他全局对象及未解释的共享张量，核对所有分片索引后，统计实际 weight/bias 描述的 `shape`。本次四个 PyTorch 检查点的全部条目均为 weight/bias，没有额外缓冲区或重复张量。
5. 固定版本、范围、排除项和数值口径写入模型 `notes`。无法安全解释的元数据应跳过，不能为提高覆盖率放宽解析器或估算值。

示例：对下面已核验的 **单个 U-Net 文件头**复算，结果应为 `{"F16": 2567463684}`。这不是完整 SDXL 模型总量。示例只显示 dtype 元素数；对其他模型还须执行上面列出的名称、缓冲区及分片完整性检查。

```python
import json, math, urllib.request

url = ("https://huggingface.co/ByteDance/SDXL-Lightning/resolve/"
       "c9a24f48e1c025556787b0c58dd67a091ece2e44/"
       "sdxl_lightning_4step_unet.safetensors?download=true")
request = urllib.request.Request(url, headers={"Range": "bytes=0-262143"})
with urllib.request.urlopen(request, timeout=40) as response:
    assert response.status == 206
    assert response.headers.get("Content-Range", "").startswith("bytes 0-")
    prefix = response.read(262144)
size = int.from_bytes(prefix[:8], "little")
assert 2 <= size <= len(prefix) - 8  # Reject truncated/unbounded metadata.
header = json.loads(prefix[8:8+size])
counts = {}
for name, tensor in header.items():
    if name != "__metadata__":
        assert name.endswith(("weight", "bias")) and tensor["dtype"] == "F16"
        counts["F16"] = counts.get("F16", 0) + math.prod(tensor["shape"])
print(json.dumps(counts))
```

解决的 API 冲突：

- **AutoGLM Phone Multilingual**：五个固定分片的 BF16 weight/bias 实测总数相同地支持完整多模态检查点统计，而不是 API 异常小的 `total`。没有从另一个 GLM 名称复制参数量。
- **MiMo V2.5 ASR**：七个固定分片实测 F32 weight/bias；配置明确 `tie_word_embeddings = false`，没有将 API 差异假定成共享参数。官方要求另行下载 Audio Tokenizer，所以这里只收录 ASR **组件**，不填完整管线总量。
- **MythoMax、ReMM、Euryale v2.2、Nemotron Mini**：分别核对 13、3、30、1 个 PyTorch 检查点文件的所有描述元数据，未依据模型名称、文件体积或另一基础模型推算。历史排行榜的近似规模仅作辅助线索，不替代实际检查点计数。

## 已补入的组件记录

兼容字段方案见 [README 的组件参数量说明](../README.md#组件参数量及兼容策略)：`components` 为可选、不嵌套的数组，每项有唯一非空名称、至少一个数值及独立来源。父表总量不会取首项或组件之和，旧记录无需迁移；JSON 原样保留数组及字段缺失。

本轮 25 个仅有组件参数的模型包括原先的 23 个待补项，以及新解决的 DeepSeek Vision Exp 和 MiMo ASR。范围如下，具体数值和固定来源仍只维护在模型 TOML：

| 模型组 | 已收录范围及限制 |
| --- | --- |
| Qwen Image 2.1 / Turbo | 官方视觉生成组件规格，未包括文字编码器等。 |
| 七个 FLUX 模型 | 官方 rectified-flow / image transformer 规格，不将其当作包含编码器的完整管线。 |
| FIBO、Krea 2 Turbo、MiniMax H3 | 各自官方 DiT / diffusion transformer / Omni-Transformer 规格，完整编码与生成管线总量缺失。 |
| SDXL-Lightning | 四种步数 U-Net 分别实测；是互斥的替代检查点，不能相加或默选步数。 |
| Clef / Clef Flash | 全部骨干分片与独立 joint head 分别核验，未相加填父表。 |
| OmniVoice | 语音生成检查点与 Audio Tokenizer 分别核验；排除八个 I64 codebook offsets。 |
| DreamShaper 8 LCM / SDXL Base | 实测 U-Net，不重复累计单文件/组件格式，也未补造编码器大小。 |
| Macaron V1 Tall | 作者披露的四个 LoRA 专家分别记录，不采用名义骨干加 LoRA 的发行 footprint 作完整总量。 |
| Pixtral 12B / GLM Image | 官方明确披露的 decoder / vision 或 autoregressive / diffusion 组件独立记录，不自行汇总。 |
| 两个 pplx-decider | 全部主检查点分片与独立 readout 分别核验，不将骨干统计当完整总量。 |
| DeepSeek V4 Flash Vision Exp | 实测全部未量化 `vision.*` 和 `aligner.*` 张量，并与完整索引核对；不推算量化语言部分和 DSpark 总量。 |
| MiMo V2.5 ASR | 实测 ASR 检查点，不包括另行下载的 Audio Tokenizer。 |

## 最后四项的来源与限制

这些条目已补入**有来源的参数规格**，但不因此宣称其权重公开状态、服务内部文件或精确序列化参数量已获得核实。模型原有 `open_weights` 标记、权重链接和描述未修改，也没有通过排除模型改变覆盖分母。

| 模型 ID | 新证据及收录范围 |
| --- | --- |
| `deepreinforce/ornith-1.0-31b` | [2026-06-25 官方 README 的固定版本](https://github.com/ornith-ai/Ornith-1/blob/d196d60faa9ee1b1daa811e8b552b4ee203b1272/README.md)在正文独立列出模型规模/架构 “9B-Dense, 31B-Dense, 35B-MoE, and 397B-MoE”，与[发行公告](https://ornith.ai/ornith_1_0.html)对应。收录作者近似架构规格，不是解析本地名称，不照搬 Gemma/Qwen 的精确权重数。此前因没有公开检查点而完全留空过于严格：明确的作者规格可与精确检查点计数分开记录。不过官方 serving 表仍只列 9B、35B、397B，本次仍未找到可访问的 31B 权重；不得据此声称其公开权重已验证。 |
| `mistral/ministral-3b` | [OpenRouter 的精确模型页](https://openrouter.ai/mistralai/ministral-3b)正文明确写出 “3B parameter model”，并标注 2024 年 10 月发行；[Mistral 官方文档](https://docs.mistral.ai/models/ministral-3b-24-1.md)确认 `ministral-3b-2410` 及其不同的 2025 替代版本。仅收录前者已披露的近似参数规格，不借用后者的检查点计数。2024 版本权重公开状态与许可仍需另行核实。 |
| `nvidia/nemotron-3.5-super-120b-a12b` | [NVIDIA 官方 Nemotron 页面](https://developer.nvidia.com/nemotron)在介绍正文中明确称 “Nemotron 3.5 Super” 的 MoE 架构有 120B 参数、每 token 激活 12B；[Perplexity 模型文档](https://docs.perplexity.ai/docs/agent-api/models.md)将精确服务 ID 对应到同名模型并说明仅接受文本。收录已披露的命名模型架构规格，不推断服务内部是否移除视觉组件、不减去编码器参数，也不声称存在另一个已核实的裁剪版检查点。 |
| `sdaia/allam-2-7b` | [Groq 对精确 `allam-2-7b` ID 的模型卡](https://console.groq.com/docs/model/allam-2-7b)在 Model Architecture 段落明确写出 “autoregressive transformer with 7 billion parameters”。收录该声明，而不是从名称填数或改用 ALLaM-7B-Instruct-preview。本地原权重链接仍未核实，参数来源本身不证明该链接可访问。 |

## 校验与后续

已执行 TOML 语法检查、完整 Python 测试、JSON 构建，以及对 Git 基线的独立比较：模型的新增内容仅为参数 metadata，其他解析字段及原始 Benchmark 文本保持一致。另对 API 来源数值与本次获取的公共响应进行比对；这些检查不替代未来来源修订的重新核验。

本次实际结果：

```text
开放权重参数信息覆盖：373/373；没有参数信息的模型：0
提供总量：345；提供激活量：121（两者可同时存在）；仅有组件：25
TOML 语法：867 成功，0 失败
Python 单元测试：112 通过
Web 单元测试：19 通过
JSON 构建：855 模型、11 个 Benchmark 定义、1 个语言文件
JSON 与源 TOML：855 个模型全部一致
Git 基线：373 个模型仅新增参数 metadata，其他原始字节和 Benchmark 未变
API 数值与已获取公共响应比对：完整模型 121 项、组件 4 项
固定张量元数据：54 个 safetensors 文件头、47 个 PyTorch 描述集合
最后四项规格与已保存来源正文：4 项对应
git diff --check：通过
```

构建仍有原先的警告：1184 条成绩未匹配 Benchmark 定义、3 个模型描述缺少中文翻译；本次没有修改这些无关内容。

仍需区分的限制：

1. 373/373 指每个当前标记为开放权重的模型都有至少一个有来源的数值，不等于全部有精确完整总量，也不等于全部公开权重链接及服务内部检查点均已验证。最后四项的来源限制必须与数值一起保留；未发现需要用户提供凭据或手动操作才能取得参数规格的阻碍。
2. 25 个组件条目虽有参数信息，完整总量仍未知。若后续补齐完整总量，须有独立来源；不得把组件求和作为回退，也不能将名义发行 footprint 改称完整总量。
3. 模型权重许可仍以官方模型资料为准。本次只记录事实数值和来源，没有下载完整权重或再分发权重；原有许可声明保持不变。`microsoft/wizardlm-2-8x22b` 的来源仍是原文件已引用的第三方重传，不能据本次参数核验声称其权重出处及再分发许可已获得独立验证。
