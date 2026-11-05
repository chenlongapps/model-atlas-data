# Krea 2 Large Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：krea/krea-2-large
- 模型名称：Krea 2 Large
- 发布日期：2026-05-12
- 最近检查时间：2026-11-05T06:15+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地 TOML 无目标 Benchmark 成绩；官方 Krea 2 Large API 变体输出图像，故 11 项目标均不适用。没有将 Krea 2 的其他图像生成评测映射到这 11 项 Benchmark。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE 官方榜单](https://deepswe.datacurve.ai/) | 2026-11-05T06:15+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:15+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 4 评测定义](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:15+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench Science 评测定义](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:15+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [AutomationBench 官方榜单](https://zapier.com/benchmarks) | 2026-11-05T06:15+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:15+08:00 |
| chartography | 不适用 | — | [Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:15+08:00 |
| humanitys-last-exam | 不适用 | — | [Humanity's Last Exam 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:15+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:15+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [GDPval-AA 评测方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:15+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 及方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:15+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)

研究备注：
- 官方 Krea 2 Large 接口是图像生成模型，不能执行长程软件工程代理任务；没有适用成绩。

最近核验时间：2026-11-05T06:15+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 官方 Krea 2 Large 接口输出图像，不具备代码仓库修改代理流程所需的输出能力。

最近核验时间：2026-11-05T06:15+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 4 评测定义](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- 官方 Krea 2 Large 接口输出图像，不能在终端环境执行并验证任务。

最近核验时间：2026-11-05T06:15+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench Science 评测定义](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- 官方 Krea 2 Large 接口输出图像，不能在终端环境执行科学任务并提交可验证结果。

最近核验时间：2026-11-05T06:15+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [AutomationBench 官方榜单](https://zapier.com/benchmarks)

研究备注：
- 图像生成接口不能调用模拟 SaaS 工具并改变业务环境状态。

最近核验时间：2026-11-05T06:15+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 图像生成结果不是桌面操作 agent 的动作或可执行操作指令。

最近核验时间：2026-11-05T06:15+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 该接口生成图像而非针对图表问题输出可评分文本答案。

最近核验时间：2026-11-05T06:15+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Humanity's Last Exam 评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 该接口输出生成图像，不提供 HLE 所需的可评分答案文本。

最近核验时间：2026-11-05T06:15+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 该项是语言模型综合能力指数；Krea 2 Large 是图像生成接口，不是该指数适用的文本回答模型。

最近核验时间：2026-11-05T06:15+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [GDPval-AA 评测方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 该接口生成图像，不具备 GDPval-AA agentic 工作流所需的工具操作和文件成果能力。

最近核验时间：2026-11-05T06:15+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 及方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 该接口生成图像，不执行 Vals Index 的金融、编码、法律和税务 agentic 任务。

最近核验时间：2026-11-05T06:15+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index 方法说明",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "该项是语言模型综合能力指数；Krea 2 Large 是图像生成接口，不是该指数适用的文本回答模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "图像生成接口不能调用模拟 SaaS 工具并改变业务环境状态。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "该接口生成图像而非针对图表问题输出可评分文本答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "官方 Krea 2 Large 接口是图像生成模型，不能执行长程软件工程代理任务；没有适用成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA 评测方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "该接口生成图像，不具备 GDPval-AA agentic 工作流所需的工具操作和文件成果能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Humanity's Last Exam 评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "该接口输出生成图像，不提供 HLE 所需的可评分答案文本。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "图像生成结果不是桌面操作 agent 的动作或可执行操作指令。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "官方 Krea 2 Large 接口输出图像，不具备代码仓库修改代理流程所需的输出能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 评测定义",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "官方 Krea 2 Large 接口输出图像，不能在终端环境执行科学任务并提交可验证结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 评测定义",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "官方 Krea 2 Large 接口输出图像，不能在终端环境执行并验证任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:15+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 及方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "该接口生成图像，不执行 Vals Index 的金融、编码、法律和税务 agentic 任务。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:15+08:00",
  "model_id": "krea/krea-2-large",
  "model_notes": [
    "本地 TOML 无目标 Benchmark 成绩；官方 Krea 2 Large API 变体输出图像，故 11 项目标均不适用。没有将 Krea 2 的其他图像生成评测映射到这 11 项 Benchmark。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
