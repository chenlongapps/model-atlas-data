# mammoth-1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：baseten/mammoth-1
- 模型名称：mammoth-1
- 发布日期：2026-10-19
- 最近检查时间：2026-11-04T02:06+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE 官方运行说明](https://deepswe.datacurve.ai/run) | 2026-11-04T02:06+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Scale AI SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T02:06+08:00 |
| terminal-bench-v4 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T02:06+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Terminal-Bench Science v0.1 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1), [Terminal-Bench Science v0.1 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval) | 2026-11-04T02:06+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks), [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T02:06+08:00 |
| osworld-v2.1 | 待核实 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T02:06+08:00 |
| chartography | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方评测仓库](https://github.com/surge-ai/chartography), [Chartography 官方 task harness](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/task.py), [Chartography 官方 scorer](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/scorer.py) | 2026-11-04T02:06+08:00 |
| humanitys-last-exam | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T02:06+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Artificial Analysis Intelligence Index v5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models) | 2026-11-04T02:06+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models) | 2026-11-04T02:06+08:00 |
| vals-index-v2.2 | 不适用 | — | [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1), [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models), [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T02:06+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE 官方运行说明](https://deepswe.datacurve.ai/run)

研究备注：
- DeepSWE 标准运行要求 sandbox coding agents（官方运行文档列 Pier、mini-swe-agent 等），而 Mammoth-1 原生只返回 typed choice/score/yes-no 概率，不生成补丁或运行编码任务。官方榜单当前列 113 个任务、更新时间 2026-09-22，早于模型发布日期；未发现该模型成绩。

最近核验时间：2026-11-04T02:06+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Scale AI SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Scale V2 默认 public split 要求 agent 提交通过隐藏测试的代码补丁。Mammoth-1 原生没有自由文本/补丁生成、测试运行或工具交互输出；官方榜单也未找到模型条目。没有可核实分数。

最近核验时间：2026-11-04T02:06+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 标准协议要求 agent 操作终端环境并由 task resolution 评分。Mammoth-1 只有结构化决策概率输出，无 shell/terminal 工具；未找到其经 agent wrapper 参与的精确成绩。官方 4.0 页面当前可读榜格为空。

最近核验时间：2026-11-04T02:06+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Terminal-Bench Science v0.1 官方说明](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Terminal-Bench Science v0.1 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval)

研究备注：
- Science v0.1 包含 70 个科学研究 terminal workflows，要求 agent 产出并执行分析、模拟、证明、代码或数据 artifact；Mammoth-1 原生无自由文本与终端交互接口。未找到 wrapper/system 成绩，官方 leaderboard 当前返回动态加载内容。

最近核验时间：2026-11-04T02:06+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Zapier AutomationBench 官方榜单](https://zapier.com/benchmarks)
- [Zapier AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 1.0.6 官方榜单可见前 10 项，另有 119 项折叠记录，无法核验 Mammoth-1 是否在完整表中。标准测试要求 agent 调用业务应用工具并改变环境状态；模型卡公开的 typed decision 输出不含这些工具调用，但自定义 agent wrapper 仍可能，因此暂不判定不适用。没有找到精确模型分数或配置。

尚未解决的问题：
- 需要完整展开 Zapier 官方榜单，或找到可验证的 Mammoth-1 agent wrapper 结果。

最近核验时间：2026-11-04T02:06+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [OSWorld-V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 项目页](https://osworld-v2.xlang.ai/)

研究备注：
- OSWorld v2.1 要求 computer-use agent 观察截图并执行 GUI actions。Mammoth-1 支持图像输入，但原生输出是 typed decisions，不包含 GUI actions；官方项目页/仓库没有找到该模型结果。若存在 action adapter 或 agent system 成绩，仍需另行核实。

尚未解决的问题：
- 官方动态 leaderboard 未能完整检索；没有找到 Mammoth-1 精确分数。

最近核验时间：2026-11-04T02:06+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Surge AI Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方评测仓库](https://github.com/surge-ai/chartography)
- [Chartography 官方 task harness](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/task.py)
- [Chartography 官方 scorer](https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/scorer.py)

研究备注：
- Mammoth-1 支持图像输入，但 Chartography 标准 harness 让模型生成自由文本图表答案，再由 scorer 与 gold answer 判分。Mammoth-1 输出限于 yes/no、choice 或有序 score 概率；转成枚举选择会改变标准协议。Surge 官方榜单未找到模型条目。

最近核验时间：2026-11-04T02:06+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Scale AI Humanity’s Last Exam 官方榜单](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- 原始 HLE 全集包含自由短答/精确答案，并按生成的最终答案评分。Mammoth-1 可对给定选项输出决策概率，但不能通过原始 2,500 题全集的标准答案接口。Base Labs 报告中的 HLE-MultiChoice 属于作者复刻 AA Decision Index 的组件，不是原始 HLE 成绩。

最近核验时间：2026-11-04T02:06+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Artificial Analysis Intelligence Index v5.0](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)

研究备注：
- AA Intelligence Index v5.0 是包含知识、编码、科学、agent/tool/file tasks 的九项 composite；Mammoth-1 的 decision-only 原生输出不能执行完整标准协议。AA 官方页面/模型榜未找到 v5.0 条目。Base Labs 报告 65.9 是 Artificial Analysis Decision Index 自建复刻，不能映射成 v5.0。

最近核验时间：2026-11-04T02:06+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Artificial Analysis GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 模型榜单](https://artificialanalysis.ai/leaderboards/models)

研究备注：
- GDPval-AA v2.1 使用 Stirrup shell/web agent 流程生成文档、幻灯片、图表、电子表格等专业成果，再通过盲 pairwise 比较计算 Elo。Mammoth-1 没有自然语言生成、shell/web 工具或文件产出接口；未找到 wrapper/system 分数。

最近核验时间：2026-11-04T02:06+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Mammoth-1 官方模型卡](https://huggingface.co/baselabs/mammoth-1)
- [Base Labs 技术报告](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models)
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 聚合 finance、coding、legal、tax 八项 agent/work-product 任务，包括 spreadsheet、terminal、应用构建和长期工作成果。decision-only 输出不能完成完整标准套件；官方榜单和模型材料均未报告 Mammoth-1 该项分数。

最近核验时间：2026-11-04T02:06+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "AA Intelligence Index v5.0 是包含知识、编码、科学、agent/tool/file tasks 的九项 composite；Mammoth-1 的 decision-only 原生输出不能执行完整标准协议。AA 官方页面/模型榜未找到 v5.0 条目。Base Labs 报告 65.9 是 Artificial Analysis Decision Index 自建复刻，不能映射成 v5.0。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "Zapier 1.0.6 官方榜单可见前 10 项，另有 119 项折叠记录，无法核验 Mammoth-1 是否在完整表中。标准测试要求 agent 调用业务应用工具并改变环境状态；模型卡公开的 typed decision 输出不含这些工具调用，但自定义 agent wrapper 仍可能，因此暂不判定不适用。没有找到精确模型分数或配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要完整展开 Zapier 官方榜单，或找到可验证的 Mammoth-1 agent wrapper 结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
          "label": "Chartography 官方 task harness",
          "url": "https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/task.py"
        },
        {
          "label": "Chartography 官方 scorer",
          "url": "https://raw.githubusercontent.com/surge-ai/chartography/main/src/chartography/scorer.py"
        }
      ],
      "notes": [
        "Mammoth-1 支持图像输入，但 Chartography 标准 harness 让模型生成自由文本图表答案，再由 scorer 与 gold answer 判分。Mammoth-1 输出限于 yes/no、choice 或有序 score 概率；转成枚举选择会改变标准协议。Surge 官方榜单未找到模型条目。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "DeepSWE 标准运行要求 sandbox coding agents（官方运行文档列 Pier、mini-swe-agent 等），而 Mammoth-1 原生只返回 typed choice/score/yes-no 概率，不生成补丁或运行编码任务。官方榜单当前列 113 个任务、更新时间 2026-09-22，早于模型发布日期；未发现该模型成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "GDPval-AA v2.1 使用 Stirrup shell/web agent 流程生成文档、幻灯片、图表、电子表格等专业成果，再通过盲 pairwise 比较计算 Elo。Mammoth-1 没有自然语言生成、shell/web 工具或文件产出接口；未找到 wrapper/system 分数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "原始 HLE 全集包含自由短答/精确答案，并按生成的最终答案评分。Mammoth-1 可对给定选项输出决策概率，但不能通过原始 2,500 题全集的标准答案接口。Base Labs 报告中的 HLE-MultiChoice 属于作者复刻 AA Decision Index 的组件，不是原始 HLE 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "OSWorld v2.1 要求 computer-use agent 观察截图并执行 GUI actions。Mammoth-1 支持图像输入，但原生输出是 typed decisions，不包含 GUI actions；官方项目页/仓库没有找到该模型结果。若存在 action adapter 或 agent system 成绩，仍需另行核实。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方动态 leaderboard 未能完整检索；没有找到 Mammoth-1 精确分数。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Scale V2 默认 public split 要求 agent 提交通过隐藏测试的代码补丁。Mammoth-1 原生没有自由文本/补丁生成、测试运行或工具交互输出；官方榜单也未找到模型条目。没有可核实分数。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
        },
        {
          "label": "Terminal-Bench Science v0.1 官方说明",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Terminal-Bench Science v0.1 leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/10?tab=leaderboard&leaderboard=v0-1-eval"
        }
      ],
      "notes": [
        "Science v0.1 包含 70 个科学研究 terminal workflows，要求 agent 产出并执行分析、模拟、证明、代码或数据 artifact；Mammoth-1 原生无自由文本与终端交互接口。未找到 wrapper/system 成绩，官方 leaderboard 当前返回动态加载内容。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "Terminal-Bench 4.0 标准协议要求 agent 操作终端环境并由 task resolution 评分。Mammoth-1 只有结构化决策概率输出，无 shell/terminal 工具；未找到其经 agent wrapper 参与的精确成绩。官方 4.0 页面当前可读榜格为空。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:06+08:00",
      "checked_sources": [
        {
          "label": "Mammoth-1 官方模型卡",
          "url": "https://huggingface.co/baselabs/mammoth-1"
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
        "Vals Index v2.2 聚合 finance、coding、legal、tax 八项 agent/work-product 任务，包括 spreadsheet、terminal、应用构建和长期工作成果。decision-only 输出不能完成完整标准套件；官方榜单和模型材料均未报告 Mammoth-1 该项分数。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:06+08:00",
  "model_id": "baseten/mammoth-1",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
