# Toast 1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mixedbread/toast-1
- 模型名称：Toast 1
- 发布日期：2026-08-13
- 最近检查时间：2026-11-04T18:05+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [DeepSWE v1.1 官方说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T18:05+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T18:05+08:00 |
| terminal-bench-v4 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Vals Terminal-Bench 4.0 官方说明](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T18:05+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Vals Terminal-Bench-Science 官方说明](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T18:05+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Mixedbread Toast 1 模型文档](https://www.mixedbread.com/docs/agent/models), [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks) | 2026-11-04T18:05+08:00 |
| osworld-v2.1 | 不适用 | — | [Mixedbread Toast 1 模型文档](https://www.mixedbread.com/docs/agent/models), [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T18:05+08:00 |
| chartography | 不适用 | — | [Mixedbread Toast 1 模型文档](https://www.mixedbread.com/docs/agent/models), [Surge Chartography 官方介绍及排行榜](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T18:05+08:00 |
| humanitys-last-exam | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Artificial Analysis HLE 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Mixedbread 官方评测目录](https://www.mixedbread.com/evals) | 2026-11-04T18:05+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Mixedbread 官方评测目录](https://www.mixedbread.com/evals), [Artificial Analysis Intelligence Index V5 官方评测页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T18:05+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa), [Mixedbread 官方评测目录](https://www.mixedbread.com/evals) | 2026-11-04T18:05+08:00 |
| vals-index-v2.2 | 不适用 | — | [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1), [Mixedbread 官方评测目录](https://www.mixedbread.com/evals), [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T18:05+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [DeepSWE v1.1 官方说明](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Toast 1 是检索子代理，官方说明由宿主模型负责推理、执行和最终输出；DeepSWE 评估完整的软件工程代理成果。未将作为子代理的模型或宿主系统成绩归给 Toast 1。

最近核验时间：2026-11-04T18:05+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Toast 1 官方定位是搜索与证据整理子代理，最终代码修改和回答由宿主模型完成；SWE-bench Pro V2 测量完整软件工程代理在真实代码仓库中的解决能力，不适合作为 Toast 1 独立成绩。

最近核验时间：2026-11-04T18:05+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Vals Terminal-Bench 4.0 官方说明](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Toast 1 提供检索证据，宿主模型负责执行；Terminal-Bench 4.0 要求 agent 在终端沙箱中完成任务并提交可验证产物。没有 Toast 1 独立成绩。

最近核验时间：2026-11-04T18:05+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Vals Terminal-Bench-Science 官方说明](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Toast 1 的职责是检索与证据整理，官方将科学工作流的推理、执行交给宿主模型；该 Benchmark 要求在终端环境完成科学工作流并通过任务 verifier。没有 Toast 1 独立成绩。

最近核验时间：2026-11-04T18:05+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Mixedbread Toast 1 模型文档](https://www.mixedbread.com/docs/agent/models)
- [Zapier AutomationBench 官方排行榜](https://zapier.com/benchmarks)

研究备注：
- Toast 1 支持 function calling，但在已查的官方榜单中未找到 Toast 1 的独立 AutomationBench v1.0.6 成绩；不把包含 Toast 1 子代理的宿主系统成绩归给它。

最近核验时间：2026-11-04T18:05+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 模型文档](https://www.mixedbread.com/docs/agent/models)
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- Toast 1 官方模型文档仅列文本输入和文本输出；OSWorld 2.1 是桌面计算机操作评测，需要处理 UI 状态和视觉观察。此项对 Toast 1 不适用。

最近核验时间：2026-11-04T18:05+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 模型文档](https://www.mixedbread.com/docs/agent/models)
- [Surge Chartography 官方介绍及排行榜](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Toast 1 官方模型文档仅列文本输入和文本输出；Chartography 测试对专业图表图像的视觉理解和推理。此项对 Toast 1 不适用。

最近核验时间：2026-11-04T18:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Artificial Analysis HLE 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Mixedbread 官方评测目录](https://www.mixedbread.com/evals)

研究备注：
- Toast 1 的官方定位是搜索和整理证据，宿主模型负责 reasoning 与最终作答；官方评测目录未列独立 HLE 成绩。HLE 是 closed-ended academic QA，不把 Toast 1 子代理配置视作 standalone 成绩。

最近核验时间：2026-11-04T18:05+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Mixedbread 官方评测目录](https://www.mixedbread.com/evals)
- [Artificial Analysis Intelligence Index V5 官方评测页](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- AA Index v5.0.1 汇总多项完整通用能力评测；Toast 1 官方定位为搜索子代理而非完整通用回答系统，官方榜页未列独立 Toast 1 成绩。

最近核验时间：2026-11-04T18:05+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Artificial Analysis GDPval-AA 官方评测页](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Mixedbread 官方评测目录](https://www.mixedbread.com/evals)

研究备注：
- GDPval-AA 测试职业任务并要求 agent 产出文档、幻灯片、图表和表格，再以 pairwise Elo 评价。Toast 1 只负责检索证据；发布文章中 GPT-5.6 Sol + Toast 1 的 OfficeQA 结果属于宿主系统，不属于 Toast 1 单体。

最近核验时间：2026-11-04T18:05+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Mixedbread Toast 1 官方介绍](https://www.mixedbread.com/blog/toast-1)
- [Mixedbread 官方评测目录](https://www.mixedbread.com/evals)
- [Vals Index v2.2 官方排行榜](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 汇总 finance、coding、legal 和 tax 等 agent 任务；Toast 1 的官方角色仅为检索代理，官方当前榜未列独立 Toast 1 成绩。

最近核验时间：2026-11-04T18:05+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Mixedbread 官方评测目录",
          "url": "https://www.mixedbread.com/evals"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "AA Index v5.0.1 汇总多项完整通用能力评测；Toast 1 官方定位为搜索子代理而非完整通用回答系统，官方榜页未列独立 Toast 1 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 模型文档",
          "url": "https://www.mixedbread.com/docs/agent/models"
        },
        {
          "label": "Zapier AutomationBench 官方排行榜",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Toast 1 支持 function calling，但在已查的官方榜单中未找到 Toast 1 的独立 AutomationBench v1.0.6 成绩；不把包含 Toast 1 子代理的宿主系统成绩归给它。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 模型文档",
          "url": "https://www.mixedbread.com/docs/agent/models"
        },
        {
          "label": "Surge Chartography 官方介绍及排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Toast 1 官方模型文档仅列文本输入和文本输出；Chartography 测试对专业图表图像的视觉理解和推理。此项对 Toast 1 不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "DeepSWE v1.1 官方说明",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Toast 1 是检索子代理，官方说明由宿主模型负责推理、执行和最终输出；DeepSWE 评估完整的软件工程代理成果。未将作为子代理的模型或宿主系统成绩归给 Toast 1。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Artificial Analysis GDPval-AA 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Mixedbread 官方评测目录",
          "url": "https://www.mixedbread.com/evals"
        }
      ],
      "notes": [
        "GDPval-AA 测试职业任务并要求 agent 产出文档、幻灯片、图表和表格，再以 pairwise Elo 评价。Toast 1 只负责检索证据；发布文章中 GPT-5.6 Sol + Toast 1 的 OfficeQA 结果属于宿主系统，不属于 Toast 1 单体。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Artificial Analysis HLE 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Mixedbread 官方评测目录",
          "url": "https://www.mixedbread.com/evals"
        }
      ],
      "notes": [
        "Toast 1 的官方定位是搜索和整理证据，宿主模型负责 reasoning 与最终作答；官方评测目录未列独立 HLE 成绩。HLE 是 closed-ended academic QA，不把 Toast 1 子代理配置视作 standalone 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 模型文档",
          "url": "https://www.mixedbread.com/docs/agent/models"
        },
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "Toast 1 官方模型文档仅列文本输入和文本输出；OSWorld 2.1 是桌面计算机操作评测，需要处理 UI 状态和视觉观察。此项对 Toast 1 不适用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Toast 1 官方定位是搜索与证据整理子代理，最终代码修改和回答由宿主模型完成；SWE-bench Pro V2 测量完整软件工程代理在真实代码仓库中的解决能力，不适合作为 Toast 1 独立成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Vals Terminal-Bench-Science 官方说明",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Toast 1 的职责是检索与证据整理，官方将科学工作流的推理、执行交给宿主模型；该 Benchmark 要求在终端环境完成科学工作流并通过任务 verifier。没有 Toast 1 独立成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Vals Terminal-Bench 4.0 官方说明",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Toast 1 提供检索证据，宿主模型负责执行；Terminal-Bench 4.0 要求 agent 在终端沙箱中完成任务并提交可验证产物。没有 Toast 1 独立成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T18:05+08:00",
      "checked_sources": [
        {
          "label": "Mixedbread Toast 1 官方介绍",
          "url": "https://www.mixedbread.com/blog/toast-1"
        },
        {
          "label": "Mixedbread 官方评测目录",
          "url": "https://www.mixedbread.com/evals"
        },
        {
          "label": "Vals Index v2.2 官方排行榜",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 汇总 finance、coding、legal 和 tax 等 agent 任务；Toast 1 的官方角色仅为检索代理，官方当前榜未列独立 Toast 1 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T18:05+08:00",
  "model_id": "mixedbread/toast-1",
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
