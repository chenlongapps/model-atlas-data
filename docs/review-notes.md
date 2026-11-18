# 待核实事项与许可

[文档导航](README.md) · [评测口径](benchmark-sources.md) · [参数核验](model-parameters.md)

本页汇总历史采集报告中仍需注意的限制，不是实时处理队列，也不宣称已重新联网核验。下列日期标识原核验批次；处理前须重新读取模型 TOML、注释和来源，确认后续是否已有修订。不因删除旧报告而将待核实项视为已解决。

## 许可与分发

**网页公开、能够下载、用户提供快照及保留来源，都不等于获得再分发授权。** Models.dev 的 MIT 许可不自动覆盖模型权重或第三方成绩、成本数据。

| 来源 | 仍需处理的风险 |
| --- | --- |
| [Artificial Analysis 条款](https://artificialanalysis.ai/terms-of-use) | 既有审查所读版本（标注 2026-09-15 修订）第 2.1、2.2、3.3 节包含个人非商业使用、复制/再分发及自动采集限制；未确认本仓库分发用途的单独授权。继续采集及发布/商用前应审查现行条款或取得授权 |
| [Vals](https://www.vals.ai/benchmarks/vals_index) | 页面标示 All rights reserved，未确认独立数据开放许可；公开 JSON 不等于开放授权 |
| [Datacurve](https://github.com/datacurve-ai/deep-swe/blob/main/LICENSE) / [Terminal-Bench](https://www.tbench.ai/) | 代码或任务集开源许可不能直接套到网站榜单及成本数据，单独授权待确认 |
| [Scale](https://labs.scale.com/leaderboard/humanitys_last_exam) | 原 HLE / HLE-Diamond 榜单未提供已确认的数值再分发授权，不能从题目或代码许可推定 |

本仓库维护资料，不再分发模型权重。开放权重也不等于无条件许可：

- openPangu 2.0 使用 **OpenPangu Model License Agreement Version 2.0**，包括欧盟境内访问、下载、运行限制及再分发/归属声明要求，不能标成 Apache/MIT。参见固定版本 [Flash](https://huggingface.co/openpangu/openPangu-2.0-Flash/blob/5b78fc70a06dd27c5c4c5e918c46c49531d357b4/LICENSE)、[Pro](https://huggingface.co/openpangu/openPangu-2.0-Pro/blob/4a18c03499972a726512788562c5960f213c43e8/LICENSE)。
- [Mistral Large 4 OSS](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) 使用 Mistral Ecosystem Open-Weight License，Model-as-a-Service 商用另有条件，不是 MIT。
- 参数规格不证明权重链接可访问或许可有效；Ornith 31B、2024 Ministral 3B、ALLaM 2 和 WizardLM 第三方重传等限制见[参数核验](model-parameters.md#参数规格不证明权重状态)。

## 评测冲突与版本身份

以下保留原报告的观测差异，**不是要求新增成绩副本或自动改分数**。具体原始值、条件和来源优先查模型文件及其注释。

| 事项（原核验日期） | 后续要求 |
| --- | --- |
| DeepSWE `deepseek-v4-flash` 身份（2026-11-06） | 无日期后缀的源 JSON 不能可靠绑定 `deepseek-v4-flash-0731` 或早期版本；不复制到任一版本或滚动别名 |
| DeepSWE 成本冲突（2026-11-06） | JSON 与首页内嵌榜单的同配置 mean_cost_usd 不一致，涉及 GPT-5.6 Sol/Luna/Terra 各五档、GLM-5.3 Flash max、DeepSeek V4 Pro max、Gemini 3.6 Flash high；成本保持缺失，双方值在 TOML 注释。需修订或重定价依据，不能任选高/低值 |
| Vals Terminal-Bench 历史结果（2026-11-06） | GPT-6 Sol 旧模型页与当前 overall 值、旧 Qwen3.8 Max single-run 与当前 avg@3 的关系未确认；旧记录不覆盖、不套当前成本 |
| Vals Index Nemotron Super VL / Beam（2026-11-06） | 前者旧值与 JSON 不只是舍入差异，缺官方修订及精度依据；后者 API 未精确绑定 501b-a23b 权重且成本为 null。保留旧记录，不补当前费用 |
| Vals Index MiMo V2.6 Pro / Flash（2026-11-06） | 已按用户确认补录官方 Xiaomi API 成绩，但具体 checkpoint 未披露，不能视作已验证的 RL 权重成绩。API 别名曾升级 MOPD；保留 variant 中的限制，不宣称 RL/MOPD 等价 |
| Vals Index Terra / Carbon / Mistral OSS（2026-11-06） | 旧发布更新与当前 JSON 不同，缺 run ID 或修订记录；不声称是官方更正，也不无条件新增另一运行 |
| AA 原始 HLE（2026-11-11） | Kimi K3.1 Pro、MiMo V2.6 Pro、Gemini 3.8 Flash、Qwen3.8 Max 0902 的来源与本地分数不一致，未确认条件或修订关系，保留本地，不选高分 |
| Inkling 2 Small 的 Scale 条目（2026-11-08） | `Inkling Small 2` 条目缺版本，不能仅凭相似名称及舍入值等同新检查点；需稳定模型 ID 或明确别名依据。Chartography 也不能移用旧 Inkling / Inkling Small 结果 |
| AA 零成本及快照映射（2026-11-06～07） | Command A+、North Mini Code、K2 Horizon 等原始零值未证实真实免费；Ling 3.1 Flash 1019 不等于无后缀版本。仅名称、日期和数值不足以建档或固定配置 |
| Mythos 5.2 / Ember（2026-11-10） | 当时未核实 Mythos 5.2 的 AA/Vals 结果，不能用 Fable 代填；Ember 原始 HLE/GDPval 缺值不补零。这不是对后续所有公开结果的穷尽性结论 |

## 旧队列中的未完成核验

早期逐模型队列含大量“页面不可读”“版本或指标未说明”的事项；不在新文档中重复维护过期状态、计数和成绩表。完整问题及已检查来源保留在 [2026-11-05 总览的“需要关注的问题”](https://github.com/chenlongapps/model-atlas-data/blob/0f218c077a8d290d7de6618026928555d7fec336/docs/benchmark-collection/OVERVIEW.md#需要关注的问题)，可由其中链接进入单模型记录。

后续核验仍须遵守：

- 部分榜单、折叠行、动态内容或无法解析的 PDF 不足以证明没有成绩；需要完整可访问来源，不从图表猜数值。
- OSWorld partial score 与 binary completion 不混用；AutomationBench 的 public/private split、AA 与 Zapier、SWE-bench Pro 的 Full/Hard 与版本分别核对。
- HLE 原始集、文本子集、Rolling、Diamond 不混用；GDPval-AA v2/v2.1 的不同锚点也不转换。
- 厂商、独立评测及 API 结果存在差异时，不择高覆盖。例如 Beam、MiMo、Solar Mini 4、Opus 5.5、Muse Spark Open 等历史差异，须看对应源记录和实验条件，不能只凭分数判断冲突已解决。
- 旧队列的定义映射或覆盖率可能已过时；判断当前映射以构建器和现有定义为准，不照搬旧统计或因此新建定义。

## 模型基本资料与同步风险

2026-11-17 人工核验已解决 Carbon 官方规格来源及 Inkling 开放权重状态的旧缺口，不再保留“只有 Vals 描述”“权重尚未发布”为当前结论：

- Carbon 以[官方模型页](https://ai.google.dev/gemini-api/docs/models/gemini-4-carbon)及[API 条件](https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-carbon)为据。首次公告与扩大开放日期不同；普通同步生成与 long decode 输出约束不同，不填无条件最大输出。知识截止仍未核实。
- Inkling 以[官方发布](https://thinkingmachines.ai/news/inkling-2-small/)及固定版本[模型卡](https://huggingface.co/thinkingmachines/Inkling-2-Small/blob/2ad1157016e1aac77b6ff1b770e7c05229403134/README.md)、[配置](https://huggingface.co/thinkingmachines/Inkling-2-Small/blob/2ad1157016e1aac77b6ff1b770e7c05229403134/config.json)核实权重、许可、参数和上下文；仍不采用未核实的 family、最大输出和全套能力布尔值。
- [Laguna S 2.1](https://huggingface.co/poolside/Laguna-S-2.1) 不是 XS；[Hy-MT2](https://huggingface.co/tencent/Hy-MT2-1.8B) 是翻译模型，不能跟随上游错误描述改成编程/智能体模型。已有译文继续保护描述。
- openPangu 未核实发行日期、知识截止及最大输出，不从 Hub 创建时间猜日期。其 Thinking 列的 Avg@16/3/4 原指标不改成 pass@1；没有对应定义仍保留原始成绩。

自动同步没有永久人工字段锁定，未来上游明确值可能再次改变日期或补入未独立核实的字段；需审阅差异和摘要，而非假定人工核验永远锁定。

## 历史追溯

一次性报告、采集队列及其专用生成器已移除；并未删除模型成绩或重新判定来源许可。原始报告、来源内容哈希、逐模型清单和当次检查结果可从 [清理前的 docs 快照](https://github.com/chenlongapps/model-atlas-data/tree/0f218c077a8d290d7de6618026928555d7fec336/docs)读取。本页保留其限制，不将历史检查通过数当作本次校验结果。
