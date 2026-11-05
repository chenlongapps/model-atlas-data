# MiMo-V2-Omni Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：xiaomi/mimo-v2-omni
- 模型名称：MiMo-V2-Omni
- 发布日期：2026-03-18
- 最近检查时间：2026-11-05T11:05+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 官方发布资料确认 MiMo-V2-Omni 于 2026-03-18 发布，支持 text/image/audio/video 输入及工具调用、function execution 和 UI grounding。
- API 后续停用并路由至新型号；本次只记录明确归属于历史 MiMo-V2-Omni 的成绩，不映射后续型号结果。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| terminal-bench-v4 | 待核实 | — | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://snorkel.ai/leaderboard/terminal-bench-science/](https://snorkel.ai/leaderboard/terminal-bench-science/), [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| osworld-v2.1 | 待核实 | — | [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| chartography | 未找到 | — | [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography), [https://surgehq.ai/benchmarks](https://surgehq.ai/benchmarks), [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni) | 2026-11-05T11:05+08:00 |
| humanitys-last-exam | 已收录 | 22.0 (metric=accuracy) | [https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro](https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T11:04+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/mimo-v2-omni](https://artificialanalysis.ai/models/mimo-v2-omni) | 2026-11-05T11:04+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [https://artificialanalysis.ai/models/mimo-v2-omni](https://artificialanalysis.ai/models/mimo-v2-omni), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T11:04+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T11:04+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 未在当前 DeepSWE v1.1 可见榜单中确认 MiMo-V2-Omni；榜单只展示 21/28 个模型，不能据此断言未测。

尚未解决的问题：
- 需检查完整 v1.1 原始模型 ID。

最近核验时间：2026-11-05T11:04+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 官方页面提到的 SWE-Bench 是 SWE-Bench Verified，不是 2026-09 发布的 SWE-Bench Pro V2；动态榜单可见内容未确认精确型号。

尚未解决的问题：
- 需确认完整 Pro V2 leaderboard 的精确型号结果。

最近核验时间：2026-11-05T11:04+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 官方发布资料中的终端交互示例不构成 Terminal-Bench 4 成绩；未在当前 V4 公开资料中确认精确型号。

尚未解决的问题：
- 需复核 V4 的完整结果行及测试配置。

最近核验时间：2026-11-05T11:04+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://snorkel.ai/leaderboard/terminal-bench-science/](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 当前 Science v0.1 榜单可见结果中未确认 MiMo-V2-Omni；未用通用 Terminal-Bench 或其他版本成绩替代。

尚未解决的问题：
- 需复核完整榜单中的 exact model ID。

最近核验时间：2026-11-05T11:04+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 官方发布页确认结构化工具调用与 function execution，适用性成立；Zapier 1.0.6 页面折叠其余 119 条，无法由可见行确认精确型号。

尚未解决的问题：
- 需检查折叠的剩余模型结果。

最近核验时间：2026-11-05T11:04+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [https://osworld-v2.xlang.ai/](https://osworld-v2.xlang.ai/)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 模型支持图像输入、UI grounding 和操作能力；当前可读 OSWorld 网站仍标为 2.0，未确认该精确型号在目标 v2.1 的成绩。

尚未解决的问题：
- 需查明 v2.1 精确 leaderboard 及 MiMo-V2-Omni 条目。

最近核验时间：2026-11-05T11:04+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- [https://surgehq.ai/benchmarks](https://surgehq.ai/benchmarks)
- [https://mimo.xiaomi.com/mimo-v2-omni](https://mimo.xiaomi.com/mimo-v2-omni)

研究备注：
- 模型官方页面提及 CharXiv RQ 图表理解成绩，但该评测不是 Chartography；已直接检查 Surge 官方 Chartography 单项榜单和总榜，未发现 MiMo-V2-Omni / mimo-v2-omni 精确行。结论仅对应当前公开榜单快照。

最近核验时间：2026-11-05T11:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 22.0
- metric: accuracy
- source: [https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro](https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro](https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis 对比表明确列出 MiMo-V2-Omni 的 Humanity’s Last Exam = 22%；HLE 项不是标有星号的 estimated composite index 分数。源未披露该条结果的 effort、工具设置、数据子集或评测日期，故未补猜。

最近核验时间：2026-11-05T11:04+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/mimo-v2-omni](https://artificialanalysis.ai/models/mimo-v2-omni)

研究备注：
- AA 精确型号页的 Intelligence Index V5 显示 N/A / 无公开 API；对比页的 24* 是 v4.3.2 旧版复合指数且标为 estimated，不能写作 V5。

最近核验时间：2026-11-05T11:04+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://artificialanalysis.ai/models/mimo-v2-omni](https://artificialanalysis.ai/models/mimo-v2-omni)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 已查 AA 精确型号页与 v2.1 官方评测页，未找到该精确模型的 Elo 数字；当前页面未呈现完整历史榜单，因此不据缺席判未找到。

尚未解决的问题：
- 需要可核验的 MiMo-V2-Omni GDPval-AA v2.1 Elo 行。

最近核验时间：2026-11-05T11:04+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 Vals v2.2 页面只展示各实验室最佳模型，Xiaomi 行为后续 MiMo 型号；无法据此确认 MiMo-V2-Omni 没有历史分数。

尚未解决的问题：
- 需获取该历史型号在 v2.2 方法下的独立结果或完整记录。

最近核验时间：2026-11-05T11:04+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/mimo-v2-omni"
        }
      ],
      "notes": [
        "AA 精确型号页的 Intelligence Index V5 显示 N/A / 无公开 API；对比页的 24* 是 v4.3.2 旧版复合指数且标为 estimated，不能写作 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "官方发布页确认结构化工具调用与 function execution，适用性成立；Zapier 1.0.6 页面折叠其余 119 条，无法由可见行确认精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查折叠的剩余模型结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:05+08:00",
      "checked_sources": [
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "url": "https://surgehq.ai/benchmarks"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "模型官方页面提及 CharXiv RQ 图表理解成绩，但该评测不是 Chartography；已直接检查 Surge 官方 Chartography 单项榜单和总榜，未发现 MiMo-V2-Omni / mimo-v2-omni 精确行。结论仅对应当前公开榜单快照。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "未在当前 DeepSWE v1.1 可见榜单中确认 MiMo-V2-Omni；榜单只展示 21/28 个模型，不能据此断言未测。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整 v1.1 原始模型 ID。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/mimo-v2-omni"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "已查 AA 精确型号页与 v2.1 官方评测页，未找到该精确模型的 Elo 数字；当前页面未呈现完整历史榜单，因此不据缺席判未找到。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可核验的 MiMo-V2-Omni GDPval-AA v2.1 Elo 行。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/comparisons/mimo-v2-omni-vs-mimo-v2-pro"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis 对比表明确列出 MiMo-V2-Omni 的 Humanity’s Last Exam = 22%；HLE 项不是标有星号的 estimated composite index 分数。源未披露该条结果的 effort、工具设置、数据子集或评测日期，故未补猜。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "模型支持图像输入、UI grounding 和操作能力；当前可读 OSWorld 网站仍标为 2.0，未确认该精确型号在目标 v2.1 的成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需查明 v2.1 精确 leaderboard 及 MiMo-V2-Omni 条目。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "官方页面提到的 SWE-Bench 是 SWE-Bench Verified，不是 2026-09 发布的 SWE-Bench Pro V2；动态榜单可见内容未确认精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认完整 Pro V2 leaderboard 的精确型号结果。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "当前 Science v0.1 榜单可见结果中未确认 MiMo-V2-Omni；未用通用 Terminal-Bench 或其他版本成绩替代。"
      ],
      "status": "待核实",
      "unresolved": [
        "需复核完整榜单中的 exact model ID。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://mimo.xiaomi.com/mimo-v2-omni"
        }
      ],
      "notes": [
        "官方发布资料中的终端交互示例不构成 Terminal-Bench 4 成绩；未在当前 V4 公开资料中确认精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需复核 V4 的完整结果行及测试配置。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:04+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 Vals v2.2 页面只展示各实验室最佳模型，Xiaomi 行为后续 MiMo 型号；无法据此确认 MiMo-V2-Omni 没有历史分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "需获取该历史型号在 v2.2 方法下的独立结果或完整记录。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:05+08:00",
  "model_id": "xiaomi/mimo-v2-omni",
  "model_notes": [
    "官方发布资料确认 MiMo-V2-Omni 于 2026-03-18 发布，支持 text/image/audio/video 输入及工具调用、function execution 和 UI grounding。",
    "API 后续停用并路由至新型号；本次只记录明确归属于历史 MiMo-V2-Omni 的成绩，不映射后续型号结果。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
