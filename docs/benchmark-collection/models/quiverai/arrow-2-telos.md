# Arrow 2 Telos Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：quiverai/arrow-2-telos
- 模型名称：Arrow 2 Telos
- 发布日期：2026-09-16
- 最近检查时间：2026-11-04T10:35+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [DeepSWE v1.1 官方方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [SWE-bench Pro V2 官方榜单与协议](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| terminal-bench-v4 | 不适用 | — | [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench 官方运行说明](https://www.tbench.ai/run), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Terminal-Bench Science 官方方法](https://www.tbench.ai/news/terminal-bench-science-0-1), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos), [Quiver OpenResponses API](https://docs.quiver.ai/api-reference/openresponses/create-open-response) | 2026-11-04T10:35+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 官方页面](https://osworld-v2.xlang.ai/), [OSWorld V2 官方项目](https://github.com/xlang-ai/OSWorld-V2), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| chartography | 待核实 | — | [Surge Chartography 榜单与方法](https://surgehq.ai/benchmarks/chartography), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos), [Quiver Image-to-SVG API](https://docs.quiver.ai/api-reference/vectorize-svg/vectorize-svg) | 2026-11-04T10:35+08:00 |
| humanitys-last-exam | 不适用 | — | [Artificial Analysis HLE 官方方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |
| vals-index-v2.2 | 不适用 | — | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index), [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos) | 2026-11-04T10:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [DeepSWE v1.1 官方方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- DeepSWE v1.1 评测 coding agent 修复软件并提交补丁；Telos 官方接口定位为复杂 SVG 生成与编辑，输出模态为 SVG，没有公开的通用代码仓库修复流程或该项评测结果。

最近核验时间：2026-11-04T10:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单与协议](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- SWE-bench Pro V2 要求在真实代码库中解决问题并提交代码 diff；Telos 的公开模型/API 文档列出的专门输出和操作是 SVG，未记录代码补丁流程或精确成绩。

最近核验时间：2026-11-04T10:35+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0)
- [Terminal-Bench 官方运行说明](https://www.tbench.ai/run)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- Terminal-Bench 4 在 Harbor 终端环境运行 agent；Telos 官方资料记录 SVG 生成、向量化、编辑和动画，没有文档化的终端工作流。

最近核验时间：2026-11-04T10:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Terminal-Bench Science 官方方法](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- Terminal-Bench Science 需要 agent 在终端执行科学研究任务并通过任务产物/测试评分；Telos 官方公开能力集中于复杂 SVG 创作，没有科研终端执行流程。

最近核验时间：2026-11-04T10:35+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)
- [Quiver OpenResponses API](https://docs.quiver.ai/api-reference/openresponses/create-open-response)

研究备注：
- Zapier 榜单标注 AutomationBench 1.0.6，但当前页面只展开前 10 项，另有折叠条目；没有找到可核验的 Arrow 2 Telos 成绩。模型 Responses 操作是否对实际测试可用取决于 supported_operations。

尚未解决的问题：
- 需检查完整榜单记录，并确认该准确型号、版本与测试条件；页面中未显示不构成完整榜单没有成绩的证明。

最近核验时间：2026-11-04T10:35+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 官方页面](https://osworld-v2.xlang.ai/)
- [OSWorld V2 官方项目](https://github.com/xlang-ai/OSWorld-V2)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- OSWorld 官方网页标题显示 OSWorld 2.0，与本地定义 v2.1 不一致；没有找到 Arrow 2 Telos 的精确成绩。模型支持图像输入及条件式 Responses 操作，但官方资料未确认其桌面交互能力。

尚未解决的问题：
- 需确认 v2.1 对应的正式测试版本以及 Telos 是否曾在匹配的 computer-use harness 中测试。

最近核验时间：2026-11-04T10:35+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge Chartography 榜单与方法](https://surgehq.ai/benchmarks/chartography)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)
- [Quiver Image-to-SVG API](https://docs.quiver.ai/api-reference/vectorize-svg/vectorize-svg)

研究备注：
- Surge 榜单检索未找到 Arrow 2 Telos。模型图像接口明确用于 image-to-SVG；这本身不证明它能够回答专业图表问题。

尚未解决的问题：
- 需确认 Telos 是否能在 Chartography 协议下输出可评分的图表理解答案；当前资料没有精确测试记录。

最近核验时间：2026-11-04T10:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis HLE 官方方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- HLE 以多选或短答的学术答案评分；Telos 官方文档把输出模态列为 SVG，并将用途定位为复杂矢量创作，没有该项通用问答评测证据。

最近核验时间：2026-11-04T10:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- 该综合指数汇总通识、知识工作、科学、编码等多种语言模型评测；Telos 是官方文档所述的 SVG 专用模型，未发现其参与 V5 的公开成绩。

最近核验时间：2026-11-04T10:35+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- GDPval-AA v2.1 的整体协议要求 shell/web agent 完成专业任务并产生多种工作成果；Telos 只公开为 SVG 创作/编辑模型，可能适合个别图表产物，但不能据此形成完整基准成绩。

最近核验时间：2026-11-04T10:35+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)
- [Arrow 2 Telos 官方模型文档](https://docs.quiver.ai/developers/models/arrow-2-telos)

研究备注：
- Vals Index 2.2 汇总 finance、coding、legal、tax 的 agentic 任务；Telos 的公开用途为 SVG 创作，不适合代表该跨领域综合评测成绩。

最近核验时间：2026-11-04T10:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "该综合指数汇总通识、知识工作、科学、编码等多种语言模型评测；Telos 是官方文档所述的 SVG 专用模型，未发现其参与 V5 的公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        },
        {
          "label": "Quiver OpenResponses API",
          "url": "https://docs.quiver.ai/api-reference/openresponses/create-open-response"
        }
      ],
      "notes": [
        "Zapier 榜单标注 AutomationBench 1.0.6，但当前页面只展开前 10 项，另有折叠条目；没有找到可核验的 Arrow 2 Telos 成绩。模型 Responses 操作是否对实际测试可用取决于 supported_operations。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单记录，并确认该准确型号、版本与测试条件；页面中未显示不构成完整榜单没有成绩的证明。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 榜单与方法",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        },
        {
          "label": "Quiver Image-to-SVG API",
          "url": "https://docs.quiver.ai/api-reference/vectorize-svg/vectorize-svg"
        }
      ],
      "notes": [
        "Surge 榜单检索未找到 Arrow 2 Telos。模型图像接口明确用于 image-to-SVG；这本身不证明它能够回答专业图表问题。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 Telos 是否能在 Chartography 协议下输出可评分的图表理解答案；当前资料没有精确测试记录。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方方法",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "DeepSWE v1.1 评测 coding agent 修复软件并提交补丁；Telos 官方接口定位为复杂 SVG 生成与编辑，输出模态为 SVG，没有公开的通用代码仓库修复流程或该项评测结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 的整体协议要求 shell/web agent 完成专业任务并产生多种工作成果；Telos 只公开为 SVG 创作/编辑模型，可能适合个别图表产物，但不能据此形成完整基准成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE 官方方法",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "HLE 以多选或短答的学术答案评分；Telos 官方文档把输出模态列为 SVG，并将用途定位为复杂矢量创作，没有该项通用问答评测证据。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 官方页面",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 官方项目",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "OSWorld 官方网页标题显示 OSWorld 2.0，与本地定义 v2.1 不一致；没有找到 Arrow 2 Telos 的精确成绩。模型支持图像输入及条件式 Responses 操作，但官方资料未确认其桌面交互能力。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 v2.1 对应的正式测试版本以及 Telos 是否曾在匹配的 computer-use harness 中测试。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单与协议",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求在真实代码库中解决问题并提交代码 diff；Telos 的公开模型/API 文档列出的专门输出和操作是 SVG，未记录代码补丁流程或精确成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 官方方法",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "Terminal-Bench Science 需要 agent 在终端执行科学研究任务并通过任务产物/测试评分；Telos 官方公开能力集中于复杂 SVG 创作，没有科研终端执行流程。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方方法",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Terminal-Bench 官方运行说明",
          "url": "https://www.tbench.ai/run"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "Terminal-Bench 4 在 Harbor 终端环境运行 agent；Telos 官方资料记录 SVG 生成、向量化、编辑和动画，没有文档化的终端工作流。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T10:35+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Arrow 2 Telos 官方模型文档",
          "url": "https://docs.quiver.ai/developers/models/arrow-2-telos"
        }
      ],
      "notes": [
        "Vals Index 2.2 汇总 finance、coding、legal、tax 的 agentic 任务；Telos 的公开用途为 SVG 创作，不适合代表该跨领域综合评测成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T10:35+08:00",
  "model_id": "quiverai/arrow-2-telos",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
