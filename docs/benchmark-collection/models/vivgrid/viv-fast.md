# Viv Fast Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：vivgrid/viv-fast
- 模型名称：Viv Fast
- 发布日期：2026-09-21
- 最近检查时间：2026-11-04T09:22+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSWE 数据集与运行说明](https://huggingface.co/datasets/datacurve/deep-swe) | 2026-11-04T09:22+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-Bench Pro V2 官方完整榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T09:22+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 版本与评测说明](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T09:22+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench-Science 0.1 官方公告与结果](https://www.terminal-bench-science.ai/announcement), [Harbor 官方 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-04T09:22+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 榜单](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T09:22+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld 官方榜单页](https://osworld-v2.xlang.ai/), [OSWorld-V2 官方 README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md) | 2026-11-04T09:22+08:00 |
| chartography | 未找到 | — | [Surge Chartography 榜单](https://surgehq.ai/benchmarks/chartography), [Chartography 官方方法说明](https://github.com/surge-ai/chartography) | 2026-11-04T09:22+08:00 |
| humanitys-last-exam | 待核实 | — | [Humanity's Last Exam 官方基准页](https://lastexam.ai/), [HLE 官方提交 dashboard（跳转登录）](https://agi.safe.ai/dashboard) | 2026-11-04T09:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-04T09:22+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [GDPval-AA v2.1 官方基准与方法](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T09:22+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T09:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSWE 数据集与运行说明](https://huggingface.co/datasets/datacurve/deep-swe)

研究备注：
- 官方 v1.1 榜单当前显示的模型条目中未出现 viv-fast 或 Viv Fast；未发现可核实分数或对应 effort/harness。

最近核验时间：2026-11-04T09:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-Bench Pro V2 官方完整榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 检查了 Scale 官方 SWE-Bench Pro V2 完整榜单；当前公开排名中未出现 viv-fast 或 Viv Fast。没有可核实的 V2 成绩，未将其他 SWE-bench 版本映射过来。

最近核验时间：2026-11-04T09:22+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 官方榜单](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 版本与评测说明](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 官方榜单确认是 Terminal-Bench 4.0，指标为 resolution rate；榜单行在页面文本中为空，无法核对 Viv Fast 条目或测试配置。

尚未解决的问题：
- 官方 4.0 榜单当前动态结果没有被文本读取，不能据此确认完整模型名单。

最近核验时间：2026-11-04T09:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench-Science 0.1 官方公告与结果](https://www.terminal-bench-science.ai/announcement)
- [Harbor 官方 leaderboard](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- 官方公告说明 0.1 包含 70 项科学工作流任务并公布部分系统结果；Harbor leaderboard 页面只返回动态加载提示，未能核对完整条目。

尚未解决的问题：
- 未获得可读取的完整 leaderboard 行，不能确认是否存在 Viv Fast 的精确成绩。

最近核验时间：2026-11-04T09:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 榜单](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 榜单当前可读取部分未显示 Viv Fast，但页面注明还有 119 条折叠结果；公开文本不足以断定完整榜单没有该型号。

尚未解决的问题：
- 完整榜单的其余 119 条结果未从公开页面文本中展开核验；无可写入分数或测试配置。

最近核验时间：2026-11-04T09:22+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld 官方榜单页](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 官方 README](https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md)

研究备注：
- 官方 README 确认目标版本为 OSWorld 2.1；官方榜单当前页面标题显示 OSWorld 2.0。没有把 2.0 的记录转作 2.1 成绩。

尚未解决的问题：
- 未找到能核对 Viv Fast 与 OSWorld 2.1 精确版本绑定的公开榜单条目。

最近核验时间：2026-11-04T09:22+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography 榜单](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方方法说明](https://github.com/surge-ai/chartography)

研究备注：
- 检查了 Surge 的 Chartography 榜单和官方方法说明，未见 viv-fast 或 Viv Fast 的公开成绩。Vivgrid 文档确认模型支持图像输入，但没有披露该评测结果。

最近核验时间：2026-11-04T09:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Humanity's Last Exam 官方基准页](https://lastexam.ai/)
- [HLE 官方提交 dashboard（跳转登录）](https://agi.safe.ai/dashboard)

研究备注：
- HLE 公开基准主页未显示 Viv Fast 成绩；官方 submission dashboard 会跳转到登录页。按任务要求未尝试登录或绕过访问控制。

尚未解决的问题：
- 公开页面不足以核实 dashboard 中是否存在该型号提交；没有可核实的分数、数据集变体或测试条件。

最近核验时间：2026-11-04T09:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- Artificial Analysis 官方页面当前标注 Intelligence Index v5.0.1；页面当前公开模型结果中未见 Viv Fast。没有可映射的分数或推理档位。

尚未解决的问题：
- 当前官方页面标记为 v5.0.1；本地 benchmark ID 为 v5，若后续发现分数需确认其定义版本映射。

最近核验时间：2026-11-04T09:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [GDPval-AA v2.1 官方基准与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- Artificial Analysis 官方页面定义 GDPval-AA v2.1 为 220 项任务、44 个职业的 shell/web agent 评测；页面未出现 Viv Fast 的精确结果。

最近核验时间：2026-11-04T09:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 官方榜单与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals AI 官方 leaderboard 标注 v2.2；当前公开表格未见 Viv Fast 条目或成绩。

最近核验时间：2026-11-04T09:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "Artificial Analysis 官方页面当前标注 Intelligence Index v5.0.1；页面当前公开模型结果中未见 Viv Fast。没有可映射的分数或推理档位。"
      ],
      "status": "未找到",
      "unresolved": [
        "当前官方页面标记为 v5.0.1；本地 benchmark ID 为 v5，若后续发现分数需确认其定义版本映射。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Zapier 榜单当前可读取部分未显示 Viv Fast，但页面注明还有 119 条折叠结果；公开文本不足以断定完整榜单没有该型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "完整榜单的其余 119 条结果未从公开页面文本中展开核验；无可写入分数或测试配置。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方方法说明",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "检查了 Surge 的 Chartography 榜单和官方方法说明，未见 viv-fast 或 Viv Fast 的公开成绩。Vivgrid 文档确认模型支持图像输入，但没有披露该评测结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE 数据集与运行说明",
          "url": "https://huggingface.co/datasets/datacurve/deep-swe"
        }
      ],
      "notes": [
        "官方 v1.1 榜单当前显示的模型条目中未出现 viv-fast 或 Viv Fast；未发现可核实分数或对应 effort/harness。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 官方基准与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "Artificial Analysis 官方页面定义 GDPval-AA v2.1 为 220 项任务、44 个职业的 shell/web agent 评测；页面未出现 Viv Fast 的精确结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Humanity's Last Exam 官方基准页",
          "url": "https://lastexam.ai/"
        },
        {
          "label": "HLE 官方提交 dashboard（跳转登录）",
          "url": "https://agi.safe.ai/dashboard"
        }
      ],
      "notes": [
        "HLE 公开基准主页未显示 Viv Fast 成绩；官方 submission dashboard 会跳转到登录页。按任务要求未尝试登录或绕过访问控制。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开页面不足以核实 dashboard 中是否存在该型号提交；没有可核实的分数、数据集变体或测试条件。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "OSWorld 官方榜单页",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 官方 README",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/README.md"
        }
      ],
      "notes": [
        "官方 README 确认目标版本为 OSWorld 2.1；官方榜单当前页面标题显示 OSWorld 2.0。没有把 2.0 的记录转作 2.1 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到能核对 Viv Fast 与 OSWorld 2.1 精确版本绑定的公开榜单条目。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "SWE-Bench Pro V2 官方完整榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "检查了 Scale 官方 SWE-Bench Pro V2 完整榜单；当前公开排名中未出现 viv-fast 或 Viv Fast。没有可核实的 V2 成绩，未将其他 SWE-bench 版本映射过来。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench-Science 0.1 官方公告与结果",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor 官方 leaderboard",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "官方公告说明 0.1 包含 70 项科学工作流任务并公布部分系统结果；Harbor leaderboard 页面只返回动态加载提示，未能核对完整条目。"
      ],
      "status": "待核实",
      "unresolved": [
        "未获得可读取的完整 leaderboard 行，不能确认是否存在 Viv Fast 的精确成绩。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 官方榜单",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 版本与评测说明",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "官方榜单确认是 Terminal-Bench 4.0，指标为 resolution rate；榜单行在页面文本中为空，无法核对 Viv Fast 条目或测试配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方 4.0 榜单当前动态结果没有被文本读取，不能据此确认完整模型名单。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T09:22+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 官方榜单与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals AI 官方 leaderboard 标注 v2.2；当前公开表格未见 Viv Fast 条目或成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T09:22+08:00",
  "model_id": "vivgrid/viv-fast",
  "new_records": 0,
  "overall_status": "待复核"
}

-->
