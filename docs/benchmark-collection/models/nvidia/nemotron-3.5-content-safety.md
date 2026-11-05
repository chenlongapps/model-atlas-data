# Nemotron 3.5 Content Safety Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3.5-content-safety
- 模型名称：Nemotron 3.5 Content Safety
- 发布日期：2026-06-02
- 最近检查时间：2026-11-05T04:35+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- NVIDIA 官方卡将精确型号限定为多模态内容安全审核器，输出 safety labels；目标 11 项均不适用。发布日期按渠道存在差异：Hugging Face/NGC 为 2026-03-16，Build.NVIDIA 为 2026-06-02；保留仓库当前 release_date=2026-06-02，不更改排序。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T04:35+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Scale SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T04:35+08:00 |
| terminal-bench-v4 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all) | 2026-11-05T04:35+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T04:35+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T04:35+08:00 |
| osworld-v2.1 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T04:35+08:00 |
| chartography | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T04:35+08:00 |
| humanitys-last-exam | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Humanity's Last Exam official site](https://lastexam.ai/) | 2026-11-05T04:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Artificial Analysis Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:35+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T04:35+08:00 |
| vals-index-v2.2 | 不适用 | — | [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard), [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T04:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- NVIDIA 定义该精确型号为安全审核器，输出安全标签，不是软件工程代理。

最近核验时间：2026-11-05T04:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Scale SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 该模型用途是输入/回答安全分类，不执行代码仓库修复任务。

最近核验时间：2026-11-05T04:35+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)

研究备注：
- 该安全分类模型不提供终端代理任务能力。

最近核验时间：2026-11-05T04:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 该精确型号是安全标签分类器，不执行科学终端工作流。

最近核验时间：2026-11-05T04:35+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- 模型卡将其限定为安全审核模型，本地 `tools.supported=false`，不执行跨应用流程。

最近核验时间：2026-11-05T04:35+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 虽然模型接收图像，但用途是识别内容安全标签，没有桌面 GUI 操作工具。

最近核验时间：2026-11-05T04:35+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型虽可接收图像并输出文本，但官方定义的输出是安全分类标签，不是图表理解答案。

最近核验时间：2026-11-05T04:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Humanity's Last Exam official site](https://lastexam.ai/)

研究备注：
- 专用安全分类输出不适用于 HLE 学术问答。

最近核验时间：2026-11-05T04:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Artificial Analysis Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 专用内容安全分类模型的标签结果不构成通用语言模型 Index 分数。

最近核验时间：2026-11-05T04:35+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求专业工作产物与 agent 工具执行；该模型只输出内容安全标签。

最近核验时间：2026-11-05T04:35+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [NVIDIA Nemotron 3.5 Content Safety official model card](https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard)
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 衡量跨行业 agent 任务；该模型是安全审核分类器。

最近核验时间：2026-11-05T04:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Artificial Analysis Index v5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "专用内容安全分类模型的标签结果不构成通用语言模型 Index 分数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "模型卡将其限定为安全审核模型，本地 `tools.supported=false`，不执行跨应用流程。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型虽可接收图像并输出文本，但官方定义的输出是安全分类标签，不是图表理解答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "NVIDIA 定义该精确型号为安全审核器，输出安全标签，不是软件工程代理。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "GDPval-AA v2.1 official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求专业工作产物与 agent 工具执行；该模型只输出内容安全标签。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Humanity's Last Exam official site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "专用安全分类输出不适用于 HLE 学术问答。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "虽然模型接收图像，但用途是识别内容安全标签，没有桌面 GUI 操作工具。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Scale SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "该模型用途是输入/回答安全分类，不执行代码仓库修复任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "该精确型号是安全标签分类器，不执行科学终端工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        }
      ],
      "notes": [
        "该安全分类模型不提供终端代理任务能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:35+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Nemotron 3.5 Content Safety official model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard"
        },
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 衡量跨行业 agent 任务；该模型是安全审核分类器。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:35+08:00",
  "model_id": "nvidia/nemotron-3.5-content-safety",
  "model_notes": [
    "NVIDIA 官方卡将精确型号限定为多模态内容安全审核器，输出 safety labels；目标 11 项均不适用。发布日期按渠道存在差异：Hugging Face/NGC 为 2026-03-16，Build.NVIDIA 为 2026-06-02；保留仓库当前 release_date=2026-06-02，不更改排序。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
