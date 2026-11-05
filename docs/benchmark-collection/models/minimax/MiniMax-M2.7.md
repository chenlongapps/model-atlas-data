# MiniMax-M2.7 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：minimax/MiniMax-M2.7
- 模型名称：MiniMax-M2.7
- 发布日期：2026-03-18
- 最近检查时间：2026-11-05T11:00+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：3
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 本地模型为文本输入/输出，支持工具与推理；发布日为 2026-03-18。
- 发布文章提到的 SWE-Pro 56.22% 和 Terminal Bench 2 57.0% 是旧版成绩；本地 SWE-Bench Pro 无版本字段，Terminal-Bench 是 2.1，均未映射为本任务的 Pro V2 或 Terminal-Bench 4。
- GDPval-AA 的公开分数在 1494 与 1495 间不一致，且未明确指向 v2.1，因此不写入目标成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/), [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) | 2026-11-05T11:00+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [https://www.minimax.io/blog/minimax-m27](https://www.minimax.io/blog/minimax-m27) | 2026-11-05T11:00+08:00 |
| terminal-bench-v4 | 待核实 | 51.1 (metric=success rate; version=2.1) | [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks), [https://www.minimax.io/blog/minimax-m27](https://www.minimax.io/blog/minimax-m27), [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494) | 2026-11-05T11:00+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://snorkel.ai/leaderboard/terminal-bench-science/](https://snorkel.ai/leaderboard/terminal-bench-science/), [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks) | 2026-11-05T11:00+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks), [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27) | 2026-11-05T11:00+08:00 |
| osworld-v2.1 | 不适用 | — | [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7), [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T11:00+08:00 |
| chartography | 不适用 | — | [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7), [https://surgehq.ai/benchmarks](https://surgehq.ai/benchmarks) | 2026-11-05T11:00+08:00 |
| humanitys-last-exam | 已收录 | 28.0 (metric=accuracy; dataset=HLE no-tool subset; variant=thinking enabled; no tools; single sample (pass@1); Artificial Analysis Index v4.0 protocol) | [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T11:00+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/minimax-m2-7](https://artificialanalysis.ai/models/minimax-m2-7) | 2026-11-05T11:00+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27), [https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know](https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa), [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494) | 2026-11-05T11:00+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index), [https://www.vals.ai/benchmarks/vals_index_v2](https://www.vals.ai/benchmarks/vals_index_v2), [https://www.vals.ai/models/minimax_MiniMax-M2.7](https://www.vals.ai/models/minimax_MiniMax-M2.7) | 2026-11-05T11:00+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- [https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)

研究备注：
- 精确型号未出现在当前公开可见的 21/28 个模型中；榜单未展示全部配置，不能据此断言没有评测。

尚未解决的问题：
- 需在完整 v1.1 配置/原始数据中确认 exact model ID。

最近核验时间：2026-11-05T11:00+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [https://www.minimax.io/blog/minimax-m27](https://www.minimax.io/blog/minimax-m27)

研究备注：
- Scale 于 2026-09-22 发布 SWE-Bench Pro V2 新版 split；M2.7 官方报告的旧 SWE-Pro 56.22% 早于该版，不能映射。当前动态榜单可见内容未确认精确型号。

尚未解决的问题：
- 需确认精确型号是否在 Pro V2 的完整结果中。

最近核验时间：2026-11-05T11:00+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 51.1
- metric: success rate
- version: 2.1
- source: [https://www.minimax.io/blog/minimax-m3](https://www.minimax.io/blog/minimax-m3)
- date: 2026-06-01
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)
- [https://www.minimax.io/blog/minimax-m27](https://www.minimax.io/blog/minimax-m27)
- [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494)

研究备注：
- 目标 Terminal-Bench 4.0 于 2026-08-28 发布；官方材料中的 57.0 是 Terminal-Bench 2.0，模型 TOML 另有 2.1 记录。均不是目标版本。

尚未解决的问题：
- 当前可见资料未确认 M2.7 的 Terminal-Bench 4.0 结果。

最近核验时间：2026-11-05T11:00+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://snorkel.ai/leaderboard/terminal-bench-science/](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [https://www.tbench.ai/benchmarks](https://www.tbench.ai/benchmarks)

研究备注：
- 未在当前公开结果表中确认 M2.7 的 Science v0.1 成绩；未将 Terminal-Bench 通用版成绩移用。

尚未解决的问题：
- 需复核完整榜单中的 exact model ID。

最近核验时间：2026-11-05T11:00+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)

研究备注：
- M2.7 支持工具调用，适用性成立；Zapier 1.0.6 页面折叠了其余 119 条结果，无法由可见行确认精确型号是否上榜。

尚未解决的问题：
- 需检查折叠的剩余模型结果。

最近核验时间：2026-11-05T11:00+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
- [https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- 模型只支持文本输入，不能接收 OSWorld 所需的桌面视觉截图。

最近核验时间：2026-11-05T11:00+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)
- [https://surgehq.ai/benchmarks](https://surgehq.ai/benchmarks)

研究备注：
- 模型只支持文本输入，不能接收 Chartography 所需的图表图像。

最近核验时间：2026-11-05T11:00+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 28.0
- metric: accuracy
- dataset: HLE no-tool subset
- variant: thinking enabled; no tools; single sample (pass@1); Artificial Analysis Index v4.0 protocol
- source: [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- MiniMax 技术报告表 4 给出 HLE 28.0；报告确认 HLE no-tool subset，M2.7 开启 thinking，HLE 按 Artificial Analysis Index v4.0 protocol、无工具、single sample (pass@1) 评测。未公布评测日期或更细的 HLE 子集版本。

最近核验时间：2026-11-05T11:00+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/minimax-m2-7](https://artificialanalysis.ai/models/minimax-m2-7)

研究备注：
- 精确型号页当前 Intelligence Index 显示 N/A / No publicly available API；旧文章提及的 Index 分数没有标为 V5，且 V5 使用 HLE-Diamond。

最近核验时间：2026-11-05T11:00+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [https://www.minimax.io/models/text/m27](https://www.minimax.io/models/text/m27)
- [https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know](https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [https://arxiv.org/html/2605.26494](https://arxiv.org/html/2605.26494)

研究备注：
- MiniMax 产品页报告 GDPval-AA Elo 1495；Artificial Analysis 文章正文为 1494、同文图注为 1495。MiniMax 技术报告另报 GDPval-AA 50.0，metric/测试协议不同。上述来源未把任一结果精确标为目标 v2.1，目标定义要求 Elo。

尚未解决的问题：
- 1494/1495 数值不一致；公开来源未说明其是否为 v2.1，未录入成绩。

最近核验时间：2026-11-05T11:00+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- [https://www.vals.ai/benchmarks/vals_index_v2](https://www.vals.ai/benchmarks/vals_index_v2)
- [https://www.vals.ai/models/minimax_MiniMax-M2.7](https://www.vals.ai/models/minimax_MiniMax-M2.7)

研究备注：
- 当前 v2.2 页面只展示每家实验室最佳模型且列出 M3.1-Flash；M2.7 页面旧的 60.14% 未标为 v2.2，旧 v2 页面 24.56% 也不适用于 v2.2。

尚未解决的问题：
- 未确认 M2.7 在 v2.2 方法下的独立结果。

最近核验时间：2026-11-05T11:00+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/minimax-m2-7"
        }
      ],
      "notes": [
        "精确型号页当前 Intelligence Index 显示 N/A / No publicly available API；旧文章提及的 Index 分数没有标为 V5，且 V5 使用 HLE-Diamond。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        },
        {
          "url": "https://www.minimax.io/models/text/m27"
        }
      ],
      "notes": [
        "M2.7 支持工具调用，适用性成立；Zapier 1.0.6 页面折叠了其余 119 条结果，无法由可见行确认精确型号是否上榜。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查折叠的剩余模型结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M2.7"
        },
        {
          "url": "https://surgehq.ai/benchmarks"
        }
      ],
      "notes": [
        "模型只支持文本输入，不能接收 Chartography 所需的图表图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "url": "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
        }
      ],
      "notes": [
        "精确型号未出现在当前公开可见的 21/28 个模型中；榜单未展示全部配置，不能据此断言没有评测。"
      ],
      "status": "待核实",
      "unresolved": [
        "需在完整 v1.1 配置/原始数据中确认 exact model ID。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://www.minimax.io/models/text/m27"
        },
        {
          "url": "https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "url": "https://arxiv.org/html/2605.26494"
        }
      ],
      "notes": [
        "MiniMax 产品页报告 GDPval-AA Elo 1495；Artificial Analysis 文章正文为 1494、同文图注为 1495。MiniMax 技术报告另报 GDPval-AA 50.0，metric/测试协议不同。上述来源未把任一结果精确标为目标 v2.1，目标定义要求 Elo。"
      ],
      "status": "冲突",
      "unresolved": [
        "1494/1495 数值不一致；公开来源未说明其是否为 v2.1，未录入成绩。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://arxiv.org/html/2605.26494"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "MiniMax 技术报告表 4 给出 HLE 28.0；报告确认 HLE no-tool subset，M2.7 开启 thinking，HLE 按 Artificial Analysis Index v4.0 protocol、无工具、single sample (pass@1) 评测。未公布评测日期或更细的 HLE 子集版本。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/MiniMaxAI/MiniMax-M2.7"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "模型只支持文本输入，不能接收 OSWorld 所需的桌面视觉截图。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "url": "https://www.minimax.io/blog/minimax-m27"
        }
      ],
      "notes": [
        "Scale 于 2026-09-22 发布 SWE-Bench Pro V2 新版 split；M2.7 官方报告的旧 SWE-Pro 56.22% 早于该版，不能映射。当前动态榜单可见内容未确认精确型号。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认精确型号是否在 Pro V2 的完整结果中。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "url": "https://www.tbench.ai/benchmarks"
        }
      ],
      "notes": [
        "未在当前公开结果表中确认 M2.7 的 Science v0.1 成绩；未将 Terminal-Bench 通用版成绩移用。"
      ],
      "status": "待核实",
      "unresolved": [
        "需复核完整榜单中的 exact model ID。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/benchmarks"
        },
        {
          "url": "https://www.minimax.io/blog/minimax-m27"
        },
        {
          "url": "https://arxiv.org/html/2605.26494"
        }
      ],
      "notes": [
        "目标 Terminal-Bench 4.0 于 2026-08-28 发布；官方材料中的 57.0 是 Terminal-Bench 2.0，模型 TOML 另有 2.1 记录。均不是目标版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前可见资料未确认 M2.7 的 Terminal-Bench 4.0 结果。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T11:00+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        },
        {
          "url": "https://www.vals.ai/models/minimax_MiniMax-M2.7"
        }
      ],
      "notes": [
        "当前 v2.2 页面只展示每家实验室最佳模型且列出 M3.1-Flash；M2.7 页面旧的 60.14% 未标为 v2.2，旧 v2 页面 24.56% 也不适用于 v2.2。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认 M2.7 在 v2.2 方法下的独立结果。"
      ]
    }
  },
  "existing_records": 3,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T11:00+08:00",
  "model_id": "minimax/MiniMax-M2.7",
  "model_notes": [
    "本地模型为文本输入/输出，支持工具与推理；发布日为 2026-03-18。",
    "发布文章提到的 SWE-Pro 56.22% 和 Terminal Bench 2 57.0% 是旧版成绩；本地 SWE-Bench Pro 无版本字段，Terminal-Bench 是 2.1，均未映射为本任务的 Pro V2 或 Terminal-Bench 4。",
    "GDPval-AA 的公开分数在 1494 与 1495 间不一致，且未明确指向 v2.1，因此不写入目标成绩。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
