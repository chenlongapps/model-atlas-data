# Nemotron 3 Content Safety Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3-content-safety
- 模型名称：Nemotron 3 Content Safety
- 发布日期：2026-03-16
- 最近检查时间：2026-11-05T11:33+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- NVIDIA 官方卡将该型号识别为 Nemotron 3 Content Safety v1.1，2026-03-16 发布；模型卡支持文本及可选图像并输出安全标签。仓库 TOML 目前仅标文本输入，存在模态元数据差异；本次不因该差异改写模型能力字段。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) | 2026-11-05T11:33+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T11:33+08:00 |
| terminal-bench-v4 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.tbench.ai/](https://www.tbench.ai/) | 2026-11-05T11:33+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard), [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement) | 2026-11-05T11:33+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://zapier.com/benchmarks](https://zapier.com/benchmarks) | 2026-11-05T11:33+08:00 |
| osworld-v2.1 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T11:33+08:00 |
| chartography | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T11:33+08:00 |
| humanitys-last-exam | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://lastexam.ai/](https://lastexam.ai/) | 2026-11-05T11:33+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T11:33+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T11:33+08:00 |
| vals-index-v2.2 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety), [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T11:33+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)

研究备注：
- NVIDIA 将该型号定义为内容安全分类器，输出安全判定，不是代码生成/仓库修复 Agent。

最近核验时间：2026-11-05T11:33+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 模型用于内容安全审核与标签判定，不执行软件工程修复任务。

最近核验时间：2026-11-05T11:33+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.tbench.ai/](https://www.tbench.ai/)

研究备注：
- 内容安全分类器不提供终端交互或命令行问题求解能力。

最近核验时间：2026-11-05T11:33+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)
- [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement)

研究备注：
- 内容安全分类器不执行科学研究工作流或终端任务。

最近核验时间：2026-11-05T11:33+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

研究备注：
- 官方模型用途是安全筛查；无工具调用或跨应用业务工作流能力说明。

最近核验时间：2026-11-05T11:33+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- 模型卡虽有可选图像输入，但输出是安全标签，未声明桌面观察/操作能力。

最近核验时间：2026-11-05T11:33+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型卡虽支持图像输入，但任务是内容安全分类，不提供图表视觉推理结果。

最近核验时间：2026-11-05T11:33+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://lastexam.ai/](https://lastexam.ai/)

研究备注：
- 模型目标输出为安全/不安全标签，而不是原始 HLE 学术问题答案；未找到与该安全分类器相符的 HLE 评测任务。

最近核验时间：2026-11-05T11:33+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA V5 是知识工作、编码、科学与通识的综合指数；内容安全分类器不属于该通用评测对象。

最近核验时间：2026-11-05T11:33+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求通过 shell/web 工作流交付专业文档、幻灯片等成果；安全标签输出不匹配。

最近核验时间：2026-11-05T11:33+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety)
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 衡量财务、编码、法律和税务代理工作；安全分类用途不匹配。

最近核验时间：2026-11-05T11:33+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA V5 是知识工作、编码、科学与通识的综合指数；内容安全分类器不属于该通用评测对象。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "官方模型用途是安全筛查；无工具调用或跨应用业务工作流能力说明。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型卡虽支持图像输入，但任务是内容安全分类，不提供图表视觉推理结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        }
      ],
      "notes": [
        "NVIDIA 将该型号定义为内容安全分类器，输出安全判定，不是代码生成/仓库修复 Agent。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求通过 shell/web 工作流交付专业文档、幻灯片等成果；安全标签输出不匹配。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "模型目标输出为安全/不安全标签，而不是原始 HLE 学术问题答案；未找到与该安全分类器相符的 HLE 评测任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "模型卡虽有可选图像输入，但输出是安全标签，未声明桌面观察/操作能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "模型用于内容安全审核与标签判定，不执行软件工程修复任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        },
        {
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "内容安全分类器不执行科学研究工作流或终端任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://www.tbench.ai/"
        }
      ],
      "notes": [
        "内容安全分类器不提供终端交互或命令行问题求解能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:33+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-3-Content-Safety"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 衡量财务、编码、法律和税务代理工作；安全分类用途不匹配。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:33+08:00",
  "model_id": "nvidia/nemotron-3-content-safety",
  "model_notes": [
    "NVIDIA 官方卡将该型号识别为 Nemotron 3 Content Safety v1.1，2026-03-16 发布；模型卡支持文本及可选图像并输出安全标签。仓库 TOML 目前仅标文本输入，存在模态元数据差异；本次不因该差异改写模型能力字段。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
