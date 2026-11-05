# Jev 1.13 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：typesafe/jev-1.13.0
- 模型名称：Jev 1.13
- 发布日期：2026-09-15
- 最近检查时间：2026-11-04T11:07+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE v1.1 官方方法与榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Scale SWE-bench Pro V2 官方榜单与协议](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 4 官方榜单](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 发布说明](https://www.tbench.ai/news/terminal-bench-4-0), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench-Science 0.1 官方定义与结果](https://www.tbench.ai/news/terminal-bench-science-0-1), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Zapier AutomationBench 官方说明与榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld v2.1 官方评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld 官方榜单](https://osworld-v2.xlang.ai/), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| chartography | 不适用 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方方法仓库](https://github.com/surge-ai/chartography), [TypeSafe 图像输入说明](https://docs.typesafe.ai/images.md), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| humanitys-last-exam | 未找到 | — | [Artificial Analysis 原始 HLE 定义与榜单](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Artificial Analysis Decision Index 文章](https://artificialanalysis.ai/articles/artificial-analysis-decision-index), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index V5 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Jev 1.13 Decision Index 页面](https://artificialanalysis.ai/decision-models/jev-1-13), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA v2.1 方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Vals Jev 1.13.0 型号页](https://www.vals.ai/models/decision_jev-1.13.0), [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one) | 2026-11-04T11:07+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE v1.1 官方方法与榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- DeepSWE 要求编码 agent 在仓库中处理任务、提交 patch 并在隔离环境验证。Jev 只返回预定义 typed decision，不生成代码或自由文本，不能以单独模型接口完成基准工作流；没有把榜单上其他型号的成绩移用。

最近核验时间：2026-11-04T11:07+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Scale SWE-bench Pro V2 官方榜单与协议](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- SWE-bench Pro V2 要求 agent 处理 issue、生成代码 diff 并在干净环境重新评分。Jev 不生成文本/code diff，也没有工具调用能力；其他型号的榜单结果不适用于 Jev。

最近核验时间：2026-11-04T11:07+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 4 官方榜单](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 发布说明](https://www.tbench.ai/news/terminal-bench-4-0)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- Terminal-Bench 4 是 Harbor terminal-agent 执行任务并提交可验证结果的基准。Jev 仅输出 typed decisions，不生成命令、代码或其他终端产物，也不支持工具；因此按单独模型接口不适用。

最近核验时间：2026-11-04T11:07+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方定义与结果](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- 该基准要求在终端中完成科学工作流并生成/验证分析、模拟、证明、代码或数据产物。Jev 的 decision-only 输出和无工具接口无法完成这些任务。

最近核验时间：2026-11-04T11:07+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Zapier AutomationBench 官方说明与榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- AutomationBench 是使用 47 项工具完成跨应用工作流的端到端 agent 基准，按最终应用状态断言评分。Jev 本身不支持工具调用，也不生成可直接驱动工具的自由文本。榜单可见前 10 行没有 Jev，隐藏记录不能据此判为全榜未找到；不适用结论来自接口与任务协议不兼容。

最近核验时间：2026-11-04T11:07+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld v2.1 官方评测指南](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld 官方榜单](https://osworld-v2.xlang.ai/)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- OSWorld v2.1 要求 agent 在桌面应用中执行 GUI 操作。Jev 虽可返回有限类型的 decision，但本身不能发出 GUI 动作、坐标或待输入文本，且没有工具调用；增加外部动作适配器的系统分数不能直接作为 Jev 单模型成绩。

最近核验时间：2026-11-04T11:07+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方方法仓库](https://github.com/surge-ai/chartography)
- [TypeSafe 图像输入说明](https://docs.typesafe.ai/images.md)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- Chartography 要求模型根据图表图像和专家问题生成文本答案，再由 judge 与标准答案比较。Jev 图像输入即使开启，也只能返回预定义 decision，无法提交图表读数或解释文本；按单独模型接口不适用。

最近核验时间：2026-11-04T11:07+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis 原始 HLE 定义与榜单](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Artificial Analysis Decision Index 文章](https://artificialanalysis.ai/articles/artificial-analysis-decision-index)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- 原始 HLE 目标是 2,500 道多模态题，含选择题和短答题；未找到 Jev 1.13 的完整原始 HLE 成绩。AA 报道的 21 分对应 HLE-MultiChoice 的 513 题 text-only 子集，不是本地目标定义的全量 HLE，未写入 TOML。Jev 的 typed decision 输出也无法覆盖完整短答格式。

最近核验时间：2026-11-04T11:07+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5 定义](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Jev 1.13 Decision Index 页面](https://artificialanalysis.ai/decision-models/jev-1-13)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- AA Intelligence Index 是涵盖知识工作、coding、science 与 general knowledge 的九项综合评测，Jev 的 typed decision 接口无法完成该 composite 的自由文本和代码工作。AA Decision Index 的 58 分是不同指数，不映射到 Intelligence Index V5。

最近核验时间：2026-11-04T11:07+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- GDPval-AA v2.1 要求模型通过 shell/web agent loop 产出文档、幻灯片、图表和表格等专业工作成果。Jev 不支持工具调用，也不生成这些工作产物；按单独模型接口不适用。

最近核验时间：2026-11-04T11:07+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Vals Jev 1.13.0 型号页](https://www.vals.ai/models/decision_jev-1.13.0)
- [TypeSafe Jev API 输出协议](https://docs.typesafe.ai/api/system-one)

研究备注：
- Vals Index v2.2 是覆盖 finance、coding、legal 和 tax 的 agentic 综合评测，含终端工作与专业成果产出；Jev 仅输出预定义 decision，不生成文档、代码或工具动作。Vals Jev 型号页的 97.65% 是 ClaimBench 成绩，不是 Vals Index，未作映射。

最近核验时间：2026-11-04T11:07+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5 定义",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Jev 1.13 Decision Index 页面",
          "url": "https://artificialanalysis.ai/decision-models/jev-1-13"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "AA Intelligence Index 是涵盖知识工作、coding、science 与 general knowledge 的九项综合评测，Jev 的 typed decision 接口无法完成该 composite 的自由文本和代码工作。AA Decision Index 的 58 分是不同指数，不映射到 Intelligence Index V5。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方说明与榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "AutomationBench 是使用 47 项工具完成跨应用工作流的端到端 agent 基准，按最终应用状态断言评分。Jev 本身不支持工具调用，也不生成可直接驱动工具的自由文本。榜单可见前 10 行没有 Jev，隐藏记录不能据此判为全榜未找到；不适用结论来自接口与任务协议不兼容。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方方法仓库",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "TypeSafe 图像输入说明",
          "url": "https://docs.typesafe.ai/images.md"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "Chartography 要求模型根据图表图像和专家问题生成文本答案，再由 judge 与标准答案比较。Jev 图像输入即使开启，也只能返回预定义 decision，无法提交图表读数或解释文本；按单独模型接口不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方方法与榜单",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "DeepSWE 要求编码 agent 在仓库中处理任务、提交 patch 并在隔离环境验证。Jev 只返回预定义 typed decision，不生成代码或自由文本，不能以单独模型接口完成基准工作流；没有把榜单上其他型号的成绩移用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 要求模型通过 shell/web agent loop 产出文档、幻灯片、图表和表格等专业工作成果。Jev 不支持工具调用，也不生成这些工作产物；按单独模型接口不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 原始 HLE 定义与榜单",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Artificial Analysis Decision Index 文章",
          "url": "https://artificialanalysis.ai/articles/artificial-analysis-decision-index"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "原始 HLE 目标是 2,500 道多模态题，含选择题和短答题；未找到 Jev 1.13 的完整原始 HLE 成绩。AA 报道的 21 分对应 HLE-MultiChoice 的 513 题 text-only 子集，不是本地目标定义的全量 HLE，未写入 TOML。Jev 的 typed decision 输出也无法覆盖完整短答格式。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 官方评测指南",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "OSWorld v2.1 要求 agent 在桌面应用中执行 GUI 操作。Jev 虽可返回有限类型的 decision，但本身不能发出 GUI 动作、坐标或待输入文本，且没有工具调用；增加外部动作适配器的系统分数不能直接作为 Jev 单模型成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 官方榜单与协议",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 agent 处理 issue、生成代码 diff 并在干净环境重新评分。Jev 不生成文本/code diff，也没有工具调用能力；其他型号的榜单结果不适用于 Jev。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方定义与结果",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "该基准要求在终端中完成科学工作流并生成/验证分析、模拟、证明、代码或数据产物。Jev 的 decision-only 输出和无工具接口无法完成这些任务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 官方榜单",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 发布说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "Terminal-Bench 4 是 Harbor terminal-agent 执行任务并提交可验证结果的基准。Jev 仅输出 typed decisions，不生成命令、代码或其他终端产物，也不支持工具；因此按单独模型接口不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T11:07+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Jev 1.13.0 型号页",
          "url": "https://www.vals.ai/models/decision_jev-1.13.0"
        },
        {
          "label": "TypeSafe Jev API 输出协议",
          "url": "https://docs.typesafe.ai/api/system-one"
        }
      ],
      "notes": [
        "Vals Index v2.2 是覆盖 finance、coding、legal 和 tax 的 agentic 综合评测，含终端工作与专业成果产出；Jev 仅输出预定义 decision，不生成文档、代码或工具动作。Vals Jev 型号页的 97.65% 是 ClaimBench 成绩，不是 Vals Index，未作映射。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T11:07+08:00",
  "model_id": "typesafe/jev-1.13.0",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
