# Models.dev 同步异常核验（2026-11-17）

对比提交：`a50e5491e509229af85d44fa17ce3ab51762f6a0`。范围为同步摘要中的 8 个描述冲突及 5 个跳过项；未批量同步其他模型。

## 修改与保留

已有模型修改文件：

- `models/meta/muse-ember-1.0.toml`
- `models/moonshotai/kimi-k3.1-pro.toml`
- `models/runway/aleph-2.toml`
- `models/runway/gen-4.5.toml`
- `models/google/gemini-4-carbon.toml`
- `models/thinkingmachines/inkling-2-small.toml`
- `models/minimax/MiniMax-M3.1-Flash.toml`

- 更新 Muse Ember、Kimi K3.1 Pro、Aleph 2、Gen-4.5 的英文描述及中文翻译。
- Laguna S 2.1 保留本地描述：上游误称 XS，官方模型卡确认是 S（118B 总量，约 8B 激活）；三款 Hy-MT2 保留翻译模型描述，未采用上游的编程/智能体推理描述。
- Gemini 4 Carbon 改用官方资料描述，补充音频/PDF 输入、工具、采样控制和准确上下文。保留首次公告日期 2026-10-28；2026-11-10 是扩大开放日期，不将两者无说明替换。未核实知识截止时间，未补充；输出受 API 执行模式约束：普通同步生成 65,536，long decode 可达到共享 1,048,576 窗口扣除输入后的长度，暂不写成模型固有的无条件输出上限。输入使用已核实的通用模态，不照搬各 Provider 的 MIME 清单。
- Inkling 2 Small 更新开放权重、Apache-2.0、11 月 12 日更新日期、两种官方权重链接，补充官方完整模型 594B/17B 参数及配置中的 1,048,576 上下文。未采用上游未经核实的 `family = "ling"`、最大输出 131,072 或全套采样能力布尔值；不把评测温度、Provider 请求设置当成全部模型固有能力。
- MiniMax-M3.1-Flash 补充官方权重链接，更新已经过时的“尚未发布权重”注释；保留已有参数量和全部成绩。
- 新增 `models/huawei/openpangu-2.0-flash.toml`、`models/huawei/openpangu-2.0-pro.toml` 及中文描述，复用上游机构和 ID。分别补充官方近似参数量 92B/6B、505B/18B，配置中的 524,288 上下文及采样能力。未核实的发行日期、知识截止和最大输出省略，未从 Hub 仓库创建时间推断发行日期。

原有模型的成绩值、文本、注释和条件均不变。新增成绩 **8** 条、修正 **0** 条，新建 Benchmark 定义 **0** 个。openPangu 每款保留上游四项 thinking 成绩：AIME 2026、SWE-bench Verified、LiveCodeBench V6、GPQA-Diamond。已逐条对照官方表格的 Thinking 列，保留 `Avg@16` / `Avg@3` / `Avg@4` 原指标；不推断独立版本、Harness、评测日期、成本或默认条件。8 条均未精确映射现有定义，保留原始成绩并由构建报告警告，不能混入其他指标的排名。

## 同步脚本

- 本地已有模型可保留未知的 capability 项或发行日期缺失状态；已有字段类型错误仍拒绝。上游候选及合并结果继续执行完整导入检查，不填默认值、不降低新模型的导入门槛。
- 编辑器新增 `[[weights]]` 等表时，会在被保护的成绩占位表后添加分隔空行。恢复原始成绩时只移除该占位表生成的分隔空行，仍按原规则逐字节核对成绩文本，未改成忽略尾部空白。
- 增加补齐缺失字段、拒绝错误类型、完整上游校验、成绩尾部空白/注释及暂存区保护的回归测试。
- 对末尾没有换行、追加新表会与最后一行粘连的情况，继续安全跳过，不为通过同步而修改成绩文本；另有回归测试确认不会写入目标文件。

自动同步仍按明确上游值更新基本信息，不提供永久人工字段锁定。未来运行可能再次覆盖本次保留的日期、补入未独立核实的输出等字段；本次没有擅自新增同步例外机制。已有中文翻译继续保护 Laguna S / Hy-MT2 描述。

## 主要来源

| 用途 | 来源 |
| --- | --- |
| Ember 描述 | https://research.meta.ai/blog/muse-ember |
| Kimi 描述 | https://www.kimi.com/en/blog/kimi-k3-1-pro |
| Laguna 身份 | https://huggingface.co/poolside/Laguna-S-2.1 |
| Hy-MT2 系列定位 | https://huggingface.co/tencent/Hy-MT2-1.8B |
| Runway 描述 | https://runway.com/product/aleph-2 、https://runway.com/research/introducing-runway-gen-4.5 |
| Carbon 首次公告 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ |
| Carbon 能力、上下文和 API 条件 | https://ai.google.dev/gemini-api/docs/models/gemini-4-carbon 、https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-carbon |
| Inkling 发布与权重开放日期 | https://thinkingmachines.ai/news/inkling-2-small/ |
| Inkling 参数及许可 | https://huggingface.co/thinkingmachines/Inkling-2-Small/blob/2ad1157016e1aac77b6ff1b770e7c05229403134/README.md |
| Inkling 准确上下文 | https://huggingface.co/thinkingmachines/Inkling-2-Small/blob/2ad1157016e1aac77b6ff1b770e7c05229403134/config.json |
| MiniMax 权重 | https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash |
| Flash 参数、成绩 | https://huggingface.co/openpangu/openPangu-2.0-Flash/blob/5b78fc70a06dd27c5c4c5e918c46c49531d357b4/README.md |
| Pro 参数、成绩 | https://huggingface.co/openpangu/openPangu-2.0-Pro/blob/4a18c03499972a726512788562c5960f213c43e8/README.md |

openPangu 上述固定版本的 `config.json` 和 `generation_config.json` 分别核实上下文与采样控制。权重采用 **OpenPangu Model License Agreement Version 2.0**（同版本 `LICENSE`）：包含欧盟境内访问、下载、运行等使用限制，以及再分发/产品归属声明要求。开放权重不等于无条件许可，不标记成 Apache/MIT。仅维护资料，不在本仓库下载或再分发模型权重。

## 实际校验

- `python3 -m unittest discover -s tests -q`：141 项通过。
- `python3 scripts/validate.py`：955 个 TOML 全部通过语法检查。
- `python3 scripts/build.py`：943 个模型、11 个定义、1 个语言文件构建成功；未匹配成绩 1,390 条、歧义 0 条，包含本次新增的 8 条未映射成绩，无缺失翻译警告。
- 对 7 个已修改的已有模型，逐一比较 Git HEAD 和工作区的解析后成绩，以及 `benchmark_bytes` 保护的成绩文本，全部相同。
- 对原始 HEAD 版本的 Gemini、Inkling、MiniMax，使用固定上游候选执行内存更新，原来三处跳过均不再报错，成绩文本不变；未执行全仓写入同步。
- 对新增 8 条成绩，逐条解析固定官方 README 表格，确认 Thinking 列的数值、指标及来源 revision 一致；基础构建检查同时覆盖路径、schema、字段类型、重复成绩和来源 URL 格式。
- 本地化仅更新 6 个受影响描述、增加 2 个新模型描述；其他模型及 Benchmark 本地化未变，源模型键引用通过构建检查。
- `git diff --check` 通过。未执行完整上游 Schema 校验、权重运行测试或所有历史成绩的重新来源核验。
