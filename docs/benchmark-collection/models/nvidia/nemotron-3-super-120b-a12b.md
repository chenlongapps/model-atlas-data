# Nemotron 3 Super 120B A12B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3-super-120b-a12b
- 模型名称：Nemotron 3 Super 120B A12B
- 发布日期：2026-03-11
- 最近检查时间：2026-11-05T11:45+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- Nemotron 3 Super 与 Nemotron 3.5 Super VL 是不同型号；未移用后者的 Vals 成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/), [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 2026-11-05T11:45+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale AI SWE-bench Pro dataset](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/), [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 2026-11-05T11:45+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench versions](https://www.tbench.ai/benchmarks), [Terminal-Bench leaderboard](https://www.tbench.ai/), [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/), [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 2026-11-05T11:45+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science announcement](https://www.terminal-bench-science.ai/announcement), [Terminal-Bench Science implementation](https://github.com/harbor-framework/terminal-bench-science), [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/), [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 2026-11-05T11:45+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench), [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/), [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 2026-11-05T11:45+08:00 |
| osworld-v2.1 | 不适用 | — | [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T11:45+08:00 |
| chartography | 不适用 | — | [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16), [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T11:45+08:00 |
| humanitys-last-exam | 已收录 | 18.26 (metric=accuracy; variant=no tools); 22.82 (metric=accuracy; variant=with tools) | [NVIDIA Nemotron 3 Super Technical Report, Table 5 p.30](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf) | 2026-11-05T11:45+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T11:45+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [AA comparison: Nemotron 3 Super vs Gemini 3 Flash](https://artificialanalysis.ai/models/comparisons/nvidia-nemotron-3-super-120b-a12b-vs-gemini-3-flash), [AA comparison: Nemotron 3 Super vs Mistral Small 3.2](https://artificialanalysis.ai/models/comparisons/nvidia-nemotron-3-super-120b-a12b-vs-mistral-small-3-2) | 2026-11-05T11:45+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T11:45+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/)
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)

研究备注：
- 未能从当前动态榜单视图确认精确型号的目标版本成绩。

尚未解决的问题：
- 动态或部分加载榜单中尚不能确认精确型号行。

最近核验时间：2026-11-05T11:45+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale AI SWE-bench Pro dataset](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/)
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)

研究备注：
- 未确认目标精确榜单成绩；模型资料中的 SWE-Bench Verified、Terminal Bench Hard、Terminal Bench Core 2.0 不是本任务定义的版本。

尚未解决的问题：
- 动态或部分加载榜单中尚不能确认精确型号行。

最近核验时间：2026-11-05T11:45+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench versions](https://www.tbench.ai/benchmarks)
- [Terminal-Bench leaderboard](https://www.tbench.ai/)
- [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/)
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)

研究备注：
- 未确认目标精确榜单成绩；模型资料中的 SWE-Bench Verified、Terminal Bench Hard、Terminal Bench Core 2.0 不是本任务定义的版本。

尚未解决的问题：
- 动态或部分加载榜单中尚不能确认精确型号行。

最近核验时间：2026-11-05T11:45+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science announcement](https://www.terminal-bench-science.ai/announcement)
- [Terminal-Bench Science implementation](https://github.com/harbor-framework/terminal-bench-science)
- [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/)
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)

研究备注：
- 未能从当前动态榜单视图确认精确型号的目标版本成绩。

尚未解决的问题：
- 动态或部分加载榜单中尚不能确认精确型号行。

最近核验时间：2026-11-05T11:45+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/)
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)

研究备注：
- 模型支持 agent / workflow 工具调用；Zapier 榜单的折叠条目无法确认精确成绩。

尚未解决的问题：
- 无法确认 Nemotron 3 Super 是否有官方 held-out 成绩。

最近核验时间：2026-11-05T11:45+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- 官方模型卡列出的输入为文本；OSWorld v2.1 要求读取桌面 GUI 画面。

最近核验时间：2026-11-05T11:45+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3 Super model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)
- [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 官方模型卡列出的输入为文本，不支持读取图表图像。

最近核验时间：2026-11-05T11:45+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 18.26
- metric: accuracy
- variant: no tools
- source: [https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 22.82
- metric: accuracy
- variant: with tools
- source: [https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [NVIDIA Nemotron 3 Super Technical Report, Table 5 p.30](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)

研究备注：
- 已写入两条原始 HLE accuracy：18.26（no tools）与 22.82（with tools）。来源未公布评测日期；未填 date。

最近核验时间：2026-11-05T11:45+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Nemotron 3 Super profile](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA 精确模型页当前 Index 显示 N/A；旧比较页中的 v4.3.2 指数不属于目标 v5.0 系列。

最近核验时间：2026-11-05T11:45+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [GDPval-AA v2.1 leaderboard and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [AA comparison: Nemotron 3 Super vs Gemini 3 Flash](https://artificialanalysis.ai/models/comparisons/nvidia-nemotron-3-super-120b-a12b-vs-gemini-3-flash)
- [AA comparison: Nemotron 3 Super vs Mistral Small 3.2](https://artificialanalysis.ai/models/comparisons/nvidia-nemotron-3-super-120b-a12b-vs-mistral-small-3-2)

研究备注：
- 当前 AA leaderboard 为 497 Elo（CI -19/+19）；AA 比较页分别显示 490 与 493 Elo。模型相同且页面未说明更新批次或配置差异，因此没有写入任一候选值。

尚未解决的问题：
- 需核实 AA 页面间读数差异及更新时间/配置；暂不选取一个分数。

最近核验时间：2026-11-05T11:45+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 当前榜单每个实验室只展示最佳模型；NVIDIA 行为 Nemotron 3.5 Super VL。

尚未解决的问题：
- 无法从当前精简榜单判断 Nemotron 3 Super 是否存在独立成绩。

最近核验时间：2026-11-05T11:45+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Nemotron 3 Super profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA 精确模型页当前 Index 显示 N/A；旧比较页中的 v4.3.2 指数不属于目标 v5.0 系列。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:45+08:00",
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
          "label": "Artificial Analysis Nemotron 3 Super profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/"
        },
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        }
      ],
      "notes": [
        "模型支持 agent / workflow 工具调用；Zapier 榜单的折叠条目无法确认精确成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法确认 Nemotron 3 Super 是否有官方 held-out 成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        },
        {
          "label": "Surge Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "官方模型卡列出的输入为文本，不支持读取图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Artificial Analysis Nemotron 3 Super profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/"
        },
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        }
      ],
      "notes": [
        "未能从当前动态榜单视图确认精确型号的目标版本成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态或部分加载榜单中尚不能确认精确型号行。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 leaderboard and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "AA comparison: Nemotron 3 Super vs Gemini 3 Flash",
          "url": "https://artificialanalysis.ai/models/comparisons/nvidia-nemotron-3-super-120b-a12b-vs-gemini-3-flash"
        },
        {
          "label": "AA comparison: Nemotron 3 Super vs Mistral Small 3.2",
          "url": "https://artificialanalysis.ai/models/comparisons/nvidia-nemotron-3-super-120b-a12b-vs-mistral-small-3-2"
        }
      ],
      "notes": [
        "当前 AA leaderboard 为 497 Elo（CI -19/+19）；AA 比较页分别显示 490 与 493 Elo。模型相同且页面未说明更新批次或配置差异，因此没有写入任一候选值。"
      ],
      "status": "冲突",
      "unresolved": [
        "需核实 AA 页面间读数差异及更新时间/配置；暂不选取一个分数。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Super Technical Report, Table 5 p.30",
          "url": "https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf"
        }
      ],
      "notes": [
        "已写入两条原始 HLE accuracy：18.26（no tools）与 22.82（with tools）。来源未公布评测日期；未填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "官方模型卡列出的输入为文本；OSWorld v2.1 要求读取桌面 GUI 画面。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale AI SWE-bench Pro dataset",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "Artificial Analysis Nemotron 3 Super profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/"
        },
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        }
      ],
      "notes": [
        "未确认目标精确榜单成绩；模型资料中的 SWE-Bench Verified、Terminal Bench Hard、Terminal Bench Core 2.0 不是本任务定义的版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态或部分加载榜单中尚不能确认精确型号行。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Terminal-Bench Science implementation",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Nemotron 3 Super profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/"
        },
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        }
      ],
      "notes": [
        "未能从当前动态榜单视图确认精确型号的目标版本成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态或部分加载榜单中尚不能确认精确型号行。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench versions",
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "label": "Terminal-Bench leaderboard",
          "url": "https://www.tbench.ai/"
        },
        {
          "label": "Artificial Analysis Nemotron 3 Super profile",
          "url": "https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/"
        },
        {
          "label": "NVIDIA Nemotron 3 Super model card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
        }
      ],
      "notes": [
        "未确认目标精确榜单成绩；模型资料中的 SWE-Bench Verified、Terminal Bench Hard、Terminal Bench Core 2.0 不是本任务定义的版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态或部分加载榜单中尚不能确认精确型号行。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:45+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 当前榜单每个实验室只展示最佳模型；NVIDIA 行为 Nemotron 3.5 Super VL。"
      ],
      "status": "待核实",
      "unresolved": [
        "无法从当前精简榜单判断 Nemotron 3 Super 是否存在独立成绩。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:45+08:00",
  "model_id": "nvidia/nemotron-3-super-120b-a12b",
  "model_notes": [
    "Nemotron 3 Super 与 Nemotron 3.5 Super VL 是不同型号；未移用后者的 Vals 成绩。"
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
