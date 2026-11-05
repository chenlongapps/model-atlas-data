# Nemotron 3.5 Super 120B A12B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3.5-super-120b-a12b
- 模型名称：Nemotron 3.5 Super 120B A12B
- 发布日期：2026-10-15
- 最近检查时间：2026-11-04T02:34+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:34+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [NVIDIA Nemotron 3.5 evaluation report](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/docs/nemotron/super35/evaluate.md), [Surge post-training results](https://surgehq.ai/post-training) | 2026-11-04T02:34+08:00 |
| terminal-bench-v4 | 未找到 | — | [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [Vals AI Terminal-Bench 4 leaderboard](https://www.vals-ai.com/benchmarks/terminal-bench-4), [Artificial Analysis comparison for Super-VL](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-astra-high), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:34+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [Artificial Analysis comparison for Super-VL](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-astra-high), [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T02:34+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Surge post-training results](https://surgehq.ai/post-training), [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:34+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/), [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:34+08:00 |
| chartography | 待核实 | — | [Chartography paper](https://arxiv.org/html/2608.10677v1), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge post-training results](https://surgehq.ai/post-training), [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models) | 2026-11-04T02:34+08:00 |
| humanitys-last-exam | 不适用 | — | [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [NVIDIA HLE evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Super-VL model page](https://artificialanalysis.ai/models/nemotron-3-5-super-vl), [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models), [NVIDIA model release/evaluation page](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/) | 2026-11-04T02:34+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [NVIDIA Nemotron 3.5 evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html), [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models) | 2026-11-04T02:34+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Super-VL model page](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b), [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models) | 2026-11-04T02:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- Perplexity 官方 Agent API 对应的精确 ID 是 perplexity/nemotron-3.5-super-120b-a12b，输入仅文本；DeepSWE 官方榜没有该条目。NVIDIA 模型卡列出的 24.65/18.2 是 Nemotron 3.5 Super VL BF16/NVFP4 的 offline 结果，未证实与 Perplexity API 权重相同，且没有足够的 v1.1/harness/effort 证明，不写入。
- 已查资料未公布目标 API 版的评测日期、effort、harness 或分数。

最近核验时间：2026-11-04T02:34+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [NVIDIA Nemotron 3.5 evaluation report](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/docs/nemotron/super35/evaluate.md)
- [Surge post-training results](https://surgehq.ai/post-training)

研究备注：
- Scale SWE-bench Pro V2 Full 榜未找到目标 Perplexity API 模型。NVIDIA 51.78 来自不同公开 checkpoint/731-task 测试，与 v2 默认 642-task 数据集不匹配；Surge 86.9→92.1 是其数据再训练的 derivative，也不是目标 API 版，均不写入。

最近核验时间：2026-11-04T02:34+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [Vals AI Terminal-Bench 4 leaderboard](https://www.vals-ai.com/benchmarks/terminal-bench-4)
- [Artificial Analysis comparison for Super-VL](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-astra-high)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- Vals 和 AA 榜单可见成绩对应 Nemotron 3.5 Super VL；NVIDIA 卡列出的 1/1.5 是 Super-VL BF16/NVFP4 offline 结果。均不能移用到 Perplexity text-only API ID，官方榜未找到该精确 API 变体。

最近核验时间：2026-11-04T02:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [Artificial Analysis comparison for Super-VL](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-astra-high)
- [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 比较页的 0% 对应 Nemotron 3.5 Super VL，不是目标 Perplexity API 模型。官方页未找到精确 text-only API ID 成绩，不写入 0。

最近核验时间：2026-11-04T02:34+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Surge post-training results](https://surgehq.ai/post-training)
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- Zapier 官方榜显示 v1.0.6，但可读文本只展开 top 10，另有 119 条未展开；当前可见结果没有目标 API 模型。
- Surge post-training 页面给模糊名称 “Nemotron 3.5 Super” 的 AutomationBench 14.8%→27.5%，未明确精确 checkpoint、benchmark 版本与完整运行配置；不可归入目标 API。NVIDIA Super-VL 卡的 AutomationBench-AA 是不同评测项，也不映射。

尚未解决的问题：
- Zapier 榜单仍有 119 条未展开；Surge 所列 Nemotron 3.5 Super 变体身份和配置不充分。

最近核验时间：2026-11-04T02:34+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/)
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- OSWorld-V2 官方仓库与 leaderboard 未找到目标 Perplexity API 变体的 v2.1 成绩。NVIDIA Super-VL 卡上的 OSWorld-Verified 51.14 是不同型号与版本，不映射到本项。

最近核验时间：2026-11-04T02:34+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Chartography paper](https://arxiv.org/html/2608.10677v1)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge post-training results](https://surgehq.ai/post-training)
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)

研究备注：
- Chartography 原始协议需要将图表图像和问题输入模型，并直接文本作答；Perplexity 目标 API 的公开能力仅支持文本输入。Surge post-training 页面另有模糊名称 “Nemotron 3.5 Super” 的 with-tools 39.4%→50.6%，没有精确 checkpoint、benchmark 配置及日期，暂不能归属。

尚未解决的问题：
- 标准图像输入的 Chartography 与目标 text-only API 不兼容；Surge with-tools 的相关结果是否属于目标 API 及是否属于目标配置仍待核实。

最近核验时间：2026-11-04T02:34+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [NVIDIA HLE evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- 本地目标模型对应 Perplexity text-only API；Benchmark 定义是原始 2,500 题完整集合，含多模态题。text-only API 无法完成该完整输入协议。NVIDIA Super-VL 的 HLE full/text-only 分数不属于目标 API，且 HLE text-only subset 不是本定义的完整集合。

最近核验时间：2026-11-04T02:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Super-VL model page](https://artificialanalysis.ai/models/nemotron-3-5-super-vl)
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)
- [NVIDIA model release/evaluation page](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/)

研究备注：
- AA 的 Nemotron 3.5 官方模型页列的是 Nemotron 3.5 Super VL，Index V5.0=14；Perplexity text-only API 与其 checkpoint 对应关系未公开，故不移用。AA 没有找到目标 API ID 独立模型页或可验证成绩。

最近核验时间：2026-11-04T02:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [NVIDIA Nemotron 3.5 evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html)
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)

研究备注：
- AA 的 GDPval-AA v2.1 leaderboard 未列目标 Perplexity API 模型。NVIDIA Super 3.5 的 1211.20 是自报 GDPval-AA v2、不同公开 Super/Super-VL checkpoint；不能映射为 v2.1 或此 API 版。

最近核验时间：2026-11-04T02:34+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Super-VL model page](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b)
- [Perplexity Agent API models](https://docs.perplexity.ai/docs/agent-api/models)

研究备注：
- Vals v2.2 榜单中的 29.76% 对应 Nemotron 3.5 Super VL（Baseten provider），并非目标 Perplexity text-only API ID；未找到该 API 变体独立成绩。

最近核验时间：2026-11-04T02:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Super-VL model page",
          "url": "https://artificialanalysis.ai/models/nemotron-3-5-super-vl"
        },
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "NVIDIA model release/evaluation page",
          "url": "https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/"
        }
      ],
      "notes": [
        "AA 的 Nemotron 3.5 官方模型页列的是 Nemotron 3.5 Super VL，Index V5.0=14；Perplexity text-only API 与其 checkpoint 对应关系未公开，故不移用。AA 没有找到目标 API ID 独立模型页或可验证成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Surge post-training results",
          "url": "https://surgehq.ai/post-training"
        },
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "Zapier 官方榜显示 v1.0.6，但可读文本只展开 top 10，另有 119 条未展开；当前可见结果没有目标 API 模型。",
        "Surge post-training 页面给模糊名称 “Nemotron 3.5 Super” 的 AutomationBench 14.8%→27.5%，未明确精确 checkpoint、benchmark 版本与完整运行配置；不可归入目标 API。NVIDIA Super-VL 卡的 AutomationBench-AA 是不同评测项，也不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier 榜单仍有 119 条未展开；Surge 所列 Nemotron 3.5 Super 变体身份和配置不充分。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge post-training results",
          "url": "https://surgehq.ai/post-training"
        },
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        }
      ],
      "notes": [
        "Chartography 原始协议需要将图表图像和问题输入模型，并直接文本作答；Perplexity 目标 API 的公开能力仅支持文本输入。Surge post-training 页面另有模糊名称 “Nemotron 3.5 Super” 的 with-tools 39.4%→50.6%，没有精确 checkpoint、benchmark 配置及日期，暂不能归属。"
      ],
      "status": "待核实",
      "unresolved": [
        "标准图像输入的 Chartography 与目标 text-only API 不兼容；Surge with-tools 的相关结果是否属于目标 API 及是否属于目标配置仍待核实。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "Perplexity 官方 Agent API 对应的精确 ID 是 perplexity/nemotron-3.5-super-120b-a12b，输入仅文本；DeepSWE 官方榜没有该条目。NVIDIA 模型卡列出的 24.65/18.2 是 Nemotron 3.5 Super VL BF16/NVFP4 的 offline 结果，未证实与 Perplexity API 权重相同，且没有足够的 v1.1/harness/effort 证明，不写入。",
        "已查资料未公布目标 API 版的评测日期、effort、harness 或分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "NVIDIA Nemotron 3.5 evaluation methodology",
          "url": "https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html"
        },
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        }
      ],
      "notes": [
        "AA 的 GDPval-AA v2.1 leaderboard 未列目标 Perplexity API 模型。NVIDIA Super 3.5 的 1211.20 是自报 GDPval-AA v2、不同公开 Super/Super-VL checkpoint；不能映射为 v2.1 或此 API 版。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "NVIDIA HLE evaluation methodology",
          "url": "https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "本地目标模型对应 Perplexity text-only API；Benchmark 定义是原始 2,500 题完整集合，含多模态题。text-only API 无法完成该完整输入协议。NVIDIA Super-VL 的 HLE full/text-only 分数不属于目标 API，且 HLE text-only subset 不是本定义的完整集合。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "OSWorld-V2 官方仓库与 leaderboard 未找到目标 Perplexity API 变体的 v2.1 成绩。NVIDIA Super-VL 卡上的 OSWorld-Verified 51.14 是不同型号与版本，不映射到本项。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "NVIDIA Nemotron 3.5 evaluation report",
          "url": "https://github.com/NVIDIA-NeMo/Nemotron/blob/main/docs/nemotron/super35/evaluate.md"
        },
        {
          "label": "Surge post-training results",
          "url": "https://surgehq.ai/post-training"
        }
      ],
      "notes": [
        "Scale SWE-bench Pro V2 Full 榜未找到目标 Perplexity API 模型。NVIDIA 51.78 来自不同公开 checkpoint/731-task 测试，与 v2 默认 642-task 数据集不匹配；Surge 86.9→92.1 是其数据再训练的 derivative，也不是目标 API 版，均不写入。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "Artificial Analysis comparison for Super-VL",
          "url": "https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-astra-high"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 比较页的 0% 对应 Nemotron 3.5 Super VL，不是目标 Perplexity API 模型。官方页未找到精确 text-only API ID 成绩，不写入 0。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        },
        {
          "label": "Vals AI Terminal-Bench 4 leaderboard",
          "url": "https://www.vals-ai.com/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis comparison for Super-VL",
          "url": "https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-astra-high"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "Vals 和 AA 榜单可见成绩对应 Nemotron 3.5 Super VL；NVIDIA 卡列出的 1/1.5 是 Super-VL BF16/NVFP4 offline 结果。均不能移用到 Perplexity text-only API ID，官方榜未找到该精确 API 变体。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Super-VL model page",
          "url": "https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b"
        },
        {
          "label": "Perplexity Agent API models",
          "url": "https://docs.perplexity.ai/docs/agent-api/models"
        }
      ],
      "notes": [
        "Vals v2.2 榜单中的 29.76% 对应 Nemotron 3.5 Super VL（Baseten provider），并非目标 Perplexity text-only API ID；未找到该 API 变体独立成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:34+08:00",
  "model_id": "nvidia/nemotron-3.5-super-120b-a12b",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
