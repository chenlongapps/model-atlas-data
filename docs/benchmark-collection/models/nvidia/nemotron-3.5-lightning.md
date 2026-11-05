# Nemotron 3.5 Lightning 30B A3B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3.5-lightning
- 模型名称：Nemotron 3.5 Lightning 30B A3B
- 发布日期：2026-08-11
- 最近检查时间：2026-11-04T19:03+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 本记录对应 NVIDIA Nemotron 3.5 Lightning 30B A3B BF16 checkpoint，不与 NVFP4 checkpoint 混用。
- 模型卡标注 text-only 输入；现有 Terminal-Bench 24.58 属于 v2.1，GDPval-AA 832 属于 v2，均不映射至本轮 v4 / v2.1 目标。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE leaderboard](https://deepswe.datacurve.ai/), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16), [NVIDIA NeMo reproducibility notes](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md) | 2026-11-04T19:03+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [NVIDIA NeMo reproducibility notes](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md) | 2026-11-04T19:03+08:00 |
| terminal-bench-v4 | 待核实 | 24.58 (metric=accuracy; version=2.1; variant=BF16; reasoning; harness=NeMo Evaluator) | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16), [NVIDIA NeMo reproducibility notes](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md) | 2026-11-04T19:03+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals AI Terminal-Bench Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld project](https://osworld-v2.xlang.ai/), [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| chartography | 不适用 | — | [Surge AI Chartography benchmark](https://surgehq.ai/benchmarks/chartography), [Chartography repository](https://github.com/surge-ai/chartography), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| humanitys-last-exam | 已存在 | 11.72 (metric=accuracy; dataset=text-only; variant=BF16; reasoning; no tools) | [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis model profile](https://artificialanalysis.ai/models/nemotron-3-5-lightning), [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| gdpval-aa-v2.1 | 待核实 | 832 (metric=Elo; version=2; variant=BF16; reasoning) | [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-lightning-vs-hy3), [Artificial Analysis GDPval methodology](https://artificialanalysis.ai/benchmarks/gdpval), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI Vals Index leaderboard](https://www.vals.ai/benchmarks/vals_index), [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) | 2026-11-04T19:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)
- [NVIDIA NeMo reproducibility notes](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md)

研究备注：
- 已检查官方榜单及 NVIDIA 模型卡、复现说明；未见 Nemotron 3.5 Lightning 的 DeepSWE v1.1 成绩。

最近核验时间：2026-11-04T19:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [NVIDIA NeMo reproducibility notes](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md)

研究备注：
- Scale 完整榜单未见该模型；NVIDIA 复现说明中的 SWE-bench Verified 与 Multilingual 是不同评测，未映射到 Pro V2。

最近核验时间：2026-11-04T19:03+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 24.58
- metric: accuracy
- version: 2.1
- variant: BF16; reasoning
- harness: NeMo Evaluator
- source: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)
- [NVIDIA NeMo reproducibility notes](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md)

研究备注：
- NVIDIA 模型卡的 Terminal-Bench 24.58 明确属于 v2.1，不映射到 v4。官方 v4 榜单当前读取时成绩表行为空。

尚未解决的问题：
- Terminal-Bench 4.0 榜单当前未呈现可核验的数据行；需在榜单可读时复查是否列出该模型。

最近核验时间：2026-11-04T19:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Terminal-Bench Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- Vals AI 官方榜单未见该模型；NVIDIA 模型卡和复现说明未列出该评测。

最近核验时间：2026-11-04T19:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- Zapier 官方榜单标注 v1.0.6，公开页面只显示前 10 项，其余 119 项折叠；官方仓库说明榜单使用私有 held-out 任务集。

尚未解决的问题：
- 无法检查排行榜隐藏的 119 项，不能可靠判定该模型是否在榜单中。

最近核验时间：2026-11-04T19:03+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld project](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- 此 BF16 checkpoint 的官方模型卡标注 text-only 输入；OSWorld v2.1 需要视觉观察截图，不能由该 checkpoint 直接完成对应评测。

最近核验时间：2026-11-04T19:03+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge AI Chartography benchmark](https://surgehq.ai/benchmarks/chartography)
- [Chartography repository](https://github.com/surge-ai/chartography)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- Chartography 评测图像中的图表理解；该 BF16 checkpoint 的官方模型卡标注 text-only 输入。

最近核验时间：2026-11-04T19:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 11.72
- metric: accuracy
- dataset: text-only
- variant: BF16; reasoning; no tools
- source: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- 现有 TOML 记录与 NVIDIA BF16 模型卡一致：HLE text-only、no tools，accuracy 11.72；来源没有给出评测日期或 HLE 版本。

最近核验时间：2026-11-04T19:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis model profile](https://artificialanalysis.ai/models/nemotron-3-5-lightning)
- [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- Artificial Analysis 模型页显示指数 6、版本 v5.0.1；仓库定义为 v5.0，且来源未说明使用 BF16 还是 NVFP4，因此未写入。发布文章中的 24 对应 NVFP4，旧 v4.3.2 的 13 也不映射。

尚未解决的问题：
- 需确认 AA v5.0.1 与仓库 v5.0 定义的映射关系，以及该分数对应的 checkpoint 精度。

最近核验时间：2026-11-04T19:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 832
- metric: Elo
- version: 2
- variant: BF16; reasoning
- source: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-lightning-vs-hy3)
- [Artificial Analysis GDPval methodology](https://artificialanalysis.ai/benchmarks/gdpval)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- Artificial Analysis 比较页列出 GDPval-AA v2.1 638 Elo，但未标明 BF16/NVFP4 checkpoint。NVIDIA 模型卡的 832 是 GDPval-AA v2，不能映射到 v2.1；638 暂不写入。

尚未解决的问题：
- 需确认 638 Elo 对应的 checkpoint 精度是否为本模型 BF16。

最近核验时间：2026-11-04T19:03+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Vals Index leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [NVIDIA BF16 model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)

研究备注：
- Vals AI v2.2 榜单未列出 Nemotron 3.5 Lightning；榜单上的 Nemotron 3.5 Super VL 是另一个模型。

最近核验时间：2026-11-04T19:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis model profile",
          "url": "https://artificialanalysis.ai/models/nemotron-3-5-lightning"
        },
        {
          "label": "Artificial Analysis Index methodology",
          "url": "https://artificialanalysis.ai/methodology"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "Artificial Analysis 模型页显示指数 6、版本 v5.0.1；仓库定义为 v5.0，且来源未说明使用 BF16 还是 NVFP4，因此未写入。发布文章中的 24 对应 NVFP4，旧 v4.3.2 的 13 也不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 AA v5.0.1 与仓库 v5.0 定义的映射关系，以及该分数对应的 checkpoint 精度。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "Zapier 官方榜单标注 v1.0.6，公开页面只显示前 10 项，其余 119 项折叠；官方仓库说明榜单使用私有 held-out 任务集。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法检查排行榜隐藏的 119 项，不能可靠判定该模型是否在榜单中。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "Chartography 评测图像中的图表理解；该 BF16 checkpoint 的官方模型卡标注 text-only 输入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        },
        {
          "label": "NVIDIA NeMo reproducibility notes",
          "url": "https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md"
        }
      ],
      "notes": [
        "已检查官方榜单及 NVIDIA 模型卡、复现说明；未见 Nemotron 3.5 Lightning 的 DeepSWE v1.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/nemotron-3-5-lightning-vs-hy3"
        },
        {
          "label": "Artificial Analysis GDPval methodology",
          "url": "https://artificialanalysis.ai/benchmarks/gdpval"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "Artificial Analysis 比较页列出 GDPval-AA v2.1 638 Elo，但未标明 BF16/NVFP4 checkpoint。NVIDIA 模型卡的 832 是 GDPval-AA v2，不能映射到 v2.1；638 暂不写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 638 Elo 对应的 checkpoint 精度是否为本模型 BF16。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "现有 TOML 记录与 NVIDIA BF16 模型卡一致：HLE text-only、no tools，accuracy 11.72；来源没有给出评测日期或 HLE 版本。"
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "OSWorld project",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "此 BF16 checkpoint 的官方模型卡标注 text-only 输入；OSWorld v2.1 需要视觉观察截图，不能由该 checkpoint 直接完成对应评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "NVIDIA NeMo reproducibility notes",
          "url": "https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md"
        }
      ],
      "notes": [
        "Scale 完整榜单未见该模型；NVIDIA 复现说明中的 SWE-bench Verified 与 Multilingual 是不同评测，未映射到 Pro V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "Vals AI 官方榜单未见该模型；NVIDIA 模型卡和复现说明未列出该评测。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        },
        {
          "label": "NVIDIA NeMo reproducibility notes",
          "url": "https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/lightning-3.5/reproducibility.md"
        }
      ],
      "notes": [
        "NVIDIA 模型卡的 Terminal-Bench 24.58 明确属于 v2.1，不映射到 v4。官方 v4 榜单当前读取时成绩表行为空。"
      ],
      "status": "待核实",
      "unresolved": [
        "Terminal-Bench 4.0 榜单当前未呈现可核验的数据行；需在榜单可读时复查是否列出该模型。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:03+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "NVIDIA BF16 model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16"
        }
      ],
      "notes": [
        "Vals AI v2.2 榜单未列出 Nemotron 3.5 Lightning；榜单上的 Nemotron 3.5 Super VL 是另一个模型。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:03+08:00",
  "model_id": "nvidia/nemotron-3.5-lightning",
  "model_notes": [
    "本记录对应 NVIDIA Nemotron 3.5 Lightning 30B A3B BF16 checkpoint，不与 NVFP4 checkpoint 混用。",
    "模型卡标注 text-only 输入；现有 Terminal-Bench 24.58 属于 v2.1，GDPval-AA 832 属于 v2，均不映射至本轮 v4 / v2.1 目标。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
