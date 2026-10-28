# 首批 DeepSeek-R1 文档成绩摘录

- 来源：[固定 README 修订 0cf78561f1d51c84a21b2190626b21116d5c68bb](https://github.com/deepseek-ai/DeepSeek-R1/blob/0cf78561f1d51c84a21b2190626b21116d5c68bb/README.md#4-evaluation-results)。
- 许可：[同修订 LICENSE](https://github.com/deepseek-ai/DeepSeek-R1/blob/0cf78561f1d51c84a21b2190626b21116d5c68bb/LICENSE)，原文随附于 `MIT.txt`。
- 归属：DeepSeek-AI；Copyright (c) 2023 DeepSeek；论文 https://arxiv.org/abs/2501.12948 。
- 修改：ModelAtlas Data 于 2026-10-28 摘录五项表值、重组为独立 JSON、补充显式目录映射及执行条件摘要。未运行评测，不复制题目、答案、模型输出或权重。

| 规范模型 ID | MMLU-Pro EM (%) | MATH-500 pass@1 (%) |
| --- | --- | --- |
| `deepseek/deepseek-r1` | 84.0 | 97.3 |
| `deepseek/deepseek-v3` | 75.9 | 90.2 |
| `deepseek/deepseek-r1-distill-qwen-32b` | 未采集 | 94.3 |

两个指标各自维护；`mmlu-pro-em` 不覆盖旧待审的 `mmlu-pro` Overall Accuracy。模型身份通过官方权重下载与 Models.dev 的显式 weights 链接核对，不模糊匹配名称，不将初代模型换成后续修订。

已知执行设置通过发布字段 `harness` 随成绩展示，保留原文的“对需要采样的 benchmark”条件限定，不断言每项实际使用相同采样设置。软件版本、数据集修订、工具状态、推理等级与实际评测日期未知。Usage Recommendations 不是逐项实验记录，不能当作已确认配置。

维护者于 2026-10-28 明确批准这五条及其定义、映射和文档摘录分发用于首批试用，未授权提交、推送或部署。MIT 适用于所摘录的仓库文档，不据此声称原始 Benchmark 数据集或 DeepSeek-V3 权重采用 MIT。客户端和站点均保留许可、出处和修改说明；成绩为开发者自报，不声明跨配置可比或能力排名。
