# Hy Image 3.5 Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：tencent/hy-image-v3.5-preview
- 模型名称：Hy Image 3.5 Preview
- 发布日期：2026-09-22
- 最近检查时间：2026-11-04T08:39+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DeepSWE 官方榜单](https://deepswe.datacurve.ai/) | 2026-11-04T08:39+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Scale SWE-bench Pro V2 官方仓库](https://github.com/scaleapi/SWE-bench_Pro-os), [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T08:39+08:00 |
| terminal-bench-v4 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Terminal-Bench 4.0 官方发布说明](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench Harbor 官方仓库](https://github.com/harbor-framework/terminal-bench) | 2026-11-04T08:39+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Terminal-Bench Science 官方发布说明](https://www.tbench.ai/news/terminal-bench-science-0-1), [Terminal-Bench Science 官方仓库](https://github.com/harbor-framework/terminal-bench-science) | 2026-11-04T08:39+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Zapier AutomationBench 官方说明](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T08:39+08:00 |
| osworld-v2.1 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [OSWorld V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md), [OSWorld V2 官方项目](https://osworld-v2.xlang.ai/) | 2026-11-04T08:39+08:00 |
| chartography | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方任务与评分仓库](https://github.com/surge-ai/chartography) | 2026-11-04T08:39+08:00 |
| humanitys-last-exam | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Humanity’s Last Exam 官方页面](https://lastexam.ai/), [Artificial Analysis HLE 评分方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T08:39+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Index 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T08:39+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Artificial Analysis GDPval-AA V2.1](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa) | 2026-11-04T08:39+08:00 |
| vals-index-v2.2 | 不适用 | — | [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745), [Vals Index V2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T08:39+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [DeepSWE v1.1 方法说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DeepSWE 官方榜单](https://deepswe.datacurve.ai/)

研究备注：
- 不适用：DeepSWE v1.1 要求编码 agent 在软件仓库任务中提交代码改动并由隔离环境验证；Tencent 官方 API 将精确型号 hy-image-v3.5-preview 定义为文生图/参考生图/多轮编辑接口，成功结果是图像，不能按该代码补丁协议提交结果。未把其他 Hunyuan 语言模型或图像型号的成绩移用。

最近核验时间：2026-11-04T08:39+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Scale SWE-bench Pro V2 官方仓库](https://github.com/scaleapi/SWE-bench_Pro-os)
- [Scale SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 不适用：SWE-bench Pro V2 要求根据仓库和 issue 生成可测试的代码补丁；该型号的官方 API 输出图像，不提供该评测要求的代码补丁结果。

最近核验时间：2026-11-04T08:39+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Terminal-Bench 4.0 官方发布说明](https://www.tbench.ai/news/terminal-bench-4-0)
- [Terminal-Bench Harbor 官方仓库](https://github.com/harbor-framework/terminal-bench)

研究备注：
- 不适用：Terminal-Bench 4 在 Harbor 终端沙箱中评测 agent 任务完成情况；该图像生成 API 没有通用 shell/代码执行能力，返回图像，不能按终端任务协议评测。

最近核验时间：2026-11-04T08:39+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Terminal-Bench Science 官方发布说明](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Terminal-Bench Science 官方仓库](https://github.com/harbor-framework/terminal-bench-science)

研究备注：
- 不适用：Terminal-Bench Science 评测终端研究工作流，并检查分析、模拟、证明、代码或数据产物；该型号只能按官方接口生成/编辑图像，不具备执行终端工作流和提交所需研究产物的接口。

最近核验时间：2026-11-04T08:39+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Zapier AutomationBench 官方说明](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- 不适用：AutomationBench 要求 agent 调用应用工具完成跨应用工作流并满足最终状态断言；官方模型接口提供生图和图片编辑，没有可核实的通用应用工具调用或工作流操作输出。

最近核验时间：2026-11-04T08:39+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [OSWorld V2 官方仓库与版本说明](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)
- [OSWorld V2 官方项目](https://osworld-v2.xlang.ai/)

研究备注：
- 不适用：OSWorld V2.1 要求桌面操作 agent 观察 GUI 并发出操作动作；该型号接收文本/参考图并返回生成图像，不提供 GUI 动作或通用 tool-calling 接口。

最近核验时间：2026-11-04T08:39+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方任务与评分仓库](https://github.com/surge-ai/chartography)

研究备注：
- 不适用：Chartography 要求读取图表和问题后提交可评分的答案；尽管该模型可接收参考图，官方 API 的任务是图像生成/编辑且结果为图像，不能按图表问答协议返回答案。

最近核验时间：2026-11-04T08:39+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Humanity’s Last Exam 官方页面](https://lastexam.ai/)
- [Artificial Analysis HLE 评分方法](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 不适用：原始 Humanity’s Last Exam 是学术问答基准，需要提交可按答案评分的文本响应；该型号的官方 API 结果为图像，不能作为独立答题模型提交答案。未与 HLE-Diamond/HLE-Rolling 混用。

最近核验时间：2026-11-04T08:39+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Artificial Analysis Intelligence Index V5](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Index 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 不适用：Artificial Analysis Intelligence Index V5 是知识工作、编码、科学和一般知识等语言模型评测的复合指数；该图像生成 SKU 不提供这些子测任务所需的回答、代码或 agent 工作产物。未从 image leaderboard 推导语言模型指数。

最近核验时间：2026-11-04T08:39+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Artificial Analysis GDPval-AA V2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA 方法说明](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)

研究备注：
- 不适用：GDPval-AA v2.1 通过 agentic setting 评估职业工作成果，需完成文档、表格等工作产物；该型号的 API 只提供图像生成/编辑能力，不提供相关 agent 工作流和交付接口。

最近核验时间：2026-11-04T08:39+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Tencent Cloud Hy 生图调用指南](https://cloud.tencent.com/document/product/1823/135745)
- [Vals Index V2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 不适用：Vals Index v2.2 汇总 finance、coding、legal、tax 等领域的 agent 任务表现；该图像生成型号不能按其文本、代码及工具工作流协议交付可评分结果。

最近核验时间：2026-11-04T08:39+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Index 方法说明",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "不适用：Artificial Analysis Intelligence Index V5 是知识工作、编码、科学和一般知识等语言模型评测的复合指数；该图像生成 SKU 不提供这些子测任务所需的回答、代码或 agent 工作产物。未从 image leaderboard 推导语言模型指数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Zapier AutomationBench 官方说明",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "不适用：AutomationBench 要求 agent 调用应用工具完成跨应用工作流并满足最终状态断言；官方模型接口提供生图和图片编辑，没有可核实的通用应用工具调用或工作流操作输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方任务与评分仓库",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "不适用：Chartography 要求读取图表和问题后提交可评分的答案；尽管该模型可接收参考图，官方 API 的任务是图像生成/编辑且结果为图像，不能按图表问答协议返回答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "DeepSWE v1.1 方法说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DeepSWE 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "不适用：DeepSWE v1.1 要求编码 agent 在软件仓库任务中提交代码改动并由隔离环境验证；Tencent 官方 API 将精确型号 hy-image-v3.5-preview 定义为文生图/参考生图/多轮编辑接口，成功结果是图像，不能按该代码补丁协议提交结果。未把其他 Hunyuan 语言模型或图像型号的成绩移用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Artificial Analysis GDPval-AA V2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA 方法说明",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        }
      ],
      "notes": [
        "不适用：GDPval-AA v2.1 通过 agentic setting 评估职业工作成果，需完成文档、表格等工作产物；该型号的 API 只提供图像生成/编辑能力，不提供相关 agent 工作流和交付接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Humanity’s Last Exam 官方页面",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "Artificial Analysis HLE 评分方法",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "不适用：原始 Humanity’s Last Exam 是学术问答基准，需要提交可按答案评分的文本响应；该型号的官方 API 结果为图像，不能作为独立答题模型提交答案。未与 HLE-Diamond/HLE-Rolling 混用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "OSWorld V2 官方仓库与版本说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        },
        {
          "label": "OSWorld V2 官方项目",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "不适用：OSWorld V2.1 要求桌面操作 agent 观察 GUI 并发出操作动作；该型号接收文本/参考图并返回生成图像，不提供 GUI 动作或通用 tool-calling 接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Scale SWE-bench Pro V2 官方仓库",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os"
        },
        {
          "label": "Scale SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "不适用：SWE-bench Pro V2 要求根据仓库和 issue 生成可测试的代码补丁；该型号的官方 API 输出图像，不提供该评测要求的代码补丁结果。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Terminal-Bench Science 官方发布说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Terminal-Bench Science 官方仓库",
          "url": "https://github.com/harbor-framework/terminal-bench-science"
        }
      ],
      "notes": [
        "不适用：Terminal-Bench Science 评测终端研究工作流，并检查分析、模拟、证明、代码或数据产物；该型号只能按官方接口生成/编辑图像，不具备执行终端工作流和提交所需研究产物的接口。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Terminal-Bench 4.0 官方发布说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Terminal-Bench Harbor 官方仓库",
          "url": "https://github.com/harbor-framework/terminal-bench"
        }
      ],
      "notes": [
        "不适用：Terminal-Bench 4 在 Harbor 终端沙箱中评测 agent 任务完成情况；该图像生成 API 没有通用 shell/代码执行能力，返回图像，不能按终端任务协议评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T08:39+08:00",
      "checked_sources": [
        {
          "label": "Tencent Cloud Hy 生图调用指南",
          "url": "https://cloud.tencent.com/document/product/1823/135745"
        },
        {
          "label": "Vals Index V2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "不适用：Vals Index v2.2 汇总 finance、coding、legal、tax 等领域的 agent 任务表现；该图像生成型号不能按其文本、代码及工具工作流协议交付可评分结果。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T08:39+08:00",
  "model_id": "tencent/hy-image-v3.5-preview",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
