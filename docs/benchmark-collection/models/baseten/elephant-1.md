# elephant-1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：baseten/elephant-1
- 模型名称：elephant-1
- 发布日期：2026-10-19
- 最近检查时间：2026-11-04T02:02+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE 官方运行说明](https://deepswe.datacurve.ai/run) | 2026-11-04T02:02+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Scale AI SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:02+08:00 |
| terminal-bench-v4 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T02:02+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Terminal-Bench-Science v0.1 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1), [Terminal-Bench-Science v0.1 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval) | 2026-11-04T02:02+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T02:02+08:00 |
| osworld-v2.1 | 待核实 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T02:02+08:00 |
| chartography | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测仓库](https://github.com/surge-ai/chartography), [Chartography 官方评测 task harness](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/task.py), [Chartography 官方 scorer](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/scorer.py) | 2026-11-04T02:02+08:00 |
| humanitys-last-exam | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T02:02+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Artificial Analysis Intelligence Index v5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models) | 2026-11-04T02:02+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models) | 2026-11-04T02:02+08:00 |
| vals-index-v2.2 | 不适用 | — | [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T02:02+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE 官方运行说明](https://deepswe.datacurve.ai/run)

研究备注：
- 官方模型卡确认 elephant-1 输入状态和类型化问题，输出选项概率，不生成自然语言或代码。DeepSWE 标准运行依赖 sandbox coding agent（官方运行文档列 Pier、mini-swe-agent 等）；当前没有把 decision-only checkpoint 接入 coding agent 的评测证据。当前榜单更新时间 2026-09-22，早于模型发布日期，未见模型条目；没有成绩可录入。

最近核验时间：2026-11-04T02:02+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Scale AI SWE-bench Pro V2 榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 官方 V2 公开评测要求 agent 生成代码 patch 并通过隐藏测试。Elephant-1 的公开接口只返回类型化决策概率，不生成 patch 或执行 agent 工作流；Scale V2 公共榜也未找到该模型的精确条目。没有可核实分数。

最近核验时间：2026-11-04T02:02+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 的标准测试是在 terminal 环境中由 agent 完成任务并验证结果。Elephant-1 只输出决策概率、无工具/命令执行接口；没有找到它经 agent wrapper 参与该版本的成绩。4.0 leaderboard 当前可读表格为空。

最近核验时间：2026-11-04T02:02+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Terminal-Bench-Science v0.1 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Terminal-Bench-Science v0.1 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval)

研究备注：
- Terminal-Bench Science 要求 terminal agent 产出并运行科学分析、模拟、证明或代码等 artifacts。Elephant-1 没有自然语言生成或终端工具接口；未找到经过额外 agent wrapper 的精确模型成绩。官方 leaderboard 页面为动态加载，无法读取其完整当前条目。

最近核验时间：2026-11-04T02:02+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 1.0.6 榜单可见前 10 项，另有 119 项折叠条目，当前网页无法确认完整榜单是否包含 elephant-1。标准测试需要 agent 调用业务应用工具并改变模拟环境状态；模型卡只列 typed decision 输出。定制 agent wrapper 理论上可能，未找到该 exact checkpoint 的公开分数或测试配置，故保留待核实。

尚未解决的问题：
- 需要完整展开 Zapier 官方榜单，或找到可验证的 elephant-1 agent wrapper 评测。

最近核验时间：2026-11-04T02:02+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 项目页](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld v2.1 的标准任务要求 computer-use agent 观察截图并执行 GUI actions。Elephant-1 支持图像输入，但官方输出 schema 仅包含 yes/no、choice、score 等 typed decisions，不含 GUI action 输出；标准接口并不直接匹配。官方仓库/项目页未找到 elephant-1 结果，若存在 adapter/system 评测仍需另行核实。

尚未解决的问题：
- 官方 leaderboard 为动态内容且当前未取得可完整检索的模型表；没有找到精确成绩。

最近核验时间：2026-11-04T02:02+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测仓库](https://github.com/surge-ai/chartography)
- [Chartography 官方评测 task harness](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/task.py)
- [Chartography 官方 scorer](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/scorer.py)

研究备注：
- Elephant-1 支持图像输入，但 Chartography 官方 harness 以图表图片配专家问题后，要求模型生成可由答案 scorer 评判的自然语言/数值答案。Elephant-1 当前模型卡公开的输出为结构化选项概率，不支持任意文本答案；把任务转为枚举 choice 会改变标准协议。官方榜单未找到该模型。

最近核验时间：2026-11-04T02:02+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- 原始 HLE 全集含选择题和需要短答/精确答案的题目，按最终生成答案评分。Elephant-1 虽可对给定选项作决策，但不能按标准协议生成完整 2,500 题所需的自由文本答案。技术报告中的 HLE-MultiChoice 是其他评测配置，不等于原始 HLE 全集成绩。

最近核验时间：2026-11-04T02:02+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Artificial Analysis Intelligence Index v5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)

研究备注：
- AA Intelligence Index v5.0 是九项知识、编程、科学与 agent/tool-use 评测的综合指数，含工具和文件型任务；decision-only 输出不能按完整标准协议完成。AA/官方模型材料未找到 elephant-1 的 v5.0 条目。Base Labs 报告中的 65/65.2 是其复刻的 Artificial Analysis Decision Index，不是 Intelligence Index v5.0，不能映射。

最近核验时间：2026-11-04T02:02+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)

研究备注：
- GDPval-AA v2.1 标准测试由 Stirrup agent 使用 shell/web 生成文档、幻灯片、图表和表格等工作产物，再由 blind pairwise judge 得出 Elo。Elephant-1 没有自由文本生成、工具调用或文件产出接口；没有找到 wrapper/system 版本成绩。

最近核验时间：2026-11-04T02:02+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Elephant-1 官方模型卡](https://huggingface.co/baselabs/elephant-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 2.2 聚合 finance、coding、legal 和 tax 的 agent 任务，含 Excel、命令行、应用构建及长期工作成果。Elephant-1 的 typed decision 输出不能完成标准完整套件；官方 v2.2 页面当前未见 elephant-1 成绩。

最近核验时间：2026-11-04T02:02+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Base Labs 技术报告",
          "url": "https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5.0",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis 模型榜单",
          "url": "https://artificialanalysis.ai/leaderboards/models"
        }
      ],
      "notes": [
        "AA Intelligence Index v5.0 是九项知识、编程、科学与 agent/tool-use 评测的综合指数，含工具和文件型任务；decision-only 输出不能按完整标准协议完成。AA/官方模型材料未找到 elephant-1 的 v5.0 条目。Base Labs 报告中的 65/65.2 是其复刻的 Artificial Analysis Decision Index，不是 Intelligence Index v5.0，不能映射。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Zapier AutomationBench 官方榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Zapier 1.0.6 榜单可见前 10 项，另有 119 项折叠条目，当前网页无法确认完整榜单是否包含 elephant-1。标准测试需要 agent 调用业务应用工具并改变模拟环境状态；模型卡只列 typed decision 输出。定制 agent wrapper 理论上可能，未找到该 exact checkpoint 的公开分数或测试配置，故保留待核实。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要完整展开 Zapier 官方榜单，或找到可验证的 elephant-1 agent wrapper 评测。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Surge AI Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方评测仓库",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Chartography 官方评测 task harness",
          "url": "https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/task.py"
        },
        {
          "label": "Chartography 官方 scorer",
          "url": "https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/scorer.py"
        }
      ],
      "notes": [
        "Elephant-1 支持图像输入，但 Chartography 官方 harness 以图表图片配专家问题后，要求模型生成可由答案 scorer 评判的自然语言/数值答案。Elephant-1 当前模型卡公开的输出为结构化选项概率，不支持任意文本答案；把任务转为枚举 choice 会改变标准协议。官方榜单未找到该模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE 官方运行说明",
          "url": "https://deepswe.datacurve.ai/run"
        }
      ],
      "notes": [
        "官方模型卡确认 elephant-1 输入状态和类型化问题，输出选项概率，不生成自然语言或代码。DeepSWE 标准运行依赖 sandbox coding agent（官方运行文档列 Pier、mini-swe-agent 等）；当前没有把 decision-only checkpoint 接入 coding agent 的评测证据。当前榜单更新时间 2026-09-22，早于模型发布日期，未见模型条目；没有成绩可录入。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Base Labs 技术报告",
          "url": "https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis 模型榜单",
          "url": "https://artificialanalysis.ai/leaderboards/models"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 标准测试由 Stirrup agent 使用 shell/web 生成文档、幻灯片、图表和表格等工作产物，再由 blind pairwise judge 得出 Elo。Elephant-1 没有自由文本生成、工具调用或文件产出接口；没有找到 wrapper/system 版本成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Base Labs 技术报告",
          "url": "https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models"
        },
        {
          "label": "Scale AI Humanity’s Last Exam 官方榜单",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "原始 HLE 全集含选择题和需要短答/精确答案的题目，按最终生成答案评分。Elephant-1 虽可对给定选项作决策，但不能按标准协议生成完整 2,500 题所需的自由文本答案。技术报告中的 HLE-MultiChoice 是其他评测配置，不等于原始 HLE 全集成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "OSWorld-V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "OSWorld v2.1 的标准任务要求 computer-use agent 观察截图并执行 GUI actions。Elephant-1 支持图像输入，但官方输出 schema 仅包含 yes/no、choice、score 等 typed decisions，不含 GUI action 输出；标准接口并不直接匹配。官方仓库/项目页未找到 elephant-1 结果，若存在 adapter/system 评测仍需另行核实。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 leaderboard 为动态内容且当前未取得可完整检索的模型表；没有找到精确成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "官方 V2 公开评测要求 agent 生成代码 patch 并通过隐藏测试。Elephant-1 的公开接口只返回类型化决策概率，不生成 patch 或执行 agent 工作流；Scale V2 公共榜也未找到该模型的精确条目。没有可核实分数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Terminal-Bench-Science v0.1 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Terminal-Bench-Science v0.1 leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要求 terminal agent 产出并运行科学分析、模拟、证明或代码等 artifacts。Elephant-1 没有自然语言生成或终端工具接口；未找到经过额外 agent wrapper 的精确模型成绩。官方 leaderboard 页面为动态加载，无法读取其完整当前条目。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Terminal-Bench 4.0 官方榜单",
          "url": "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
        },
        {
          "label": "Terminal-Bench 4.0 官方方法",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 的标准测试是在 terminal 环境中由 agent 完成任务并验证结果。Elephant-1 只输出决策概率、无工具/命令执行接口；没有找到它经 agent wrapper 参与该版本的成绩。4.0 leaderboard 当前可读表格为空。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:02+08:00",
      "checked_sources": [
        {
          "label": "Elephant-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/elephant-1"
        },
        {
          "label": "Base Labs 技术报告",
          "url": "https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models"
        },
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 2.2 聚合 finance、coding、legal 和 tax 的 agent 任务，含 Excel、命令行、应用构建及长期工作成果。Elephant-1 的 typed decision 输出不能完成标准完整套件；官方 v2.2 页面当前未见 elephant-1 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:02+08:00",
  "model_id": "baseten/elephant-1",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
