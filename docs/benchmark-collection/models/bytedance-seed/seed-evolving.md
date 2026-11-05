# Seed Evolving Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：bytedance-seed/seed-evolving
- 模型名称：Seed Evolving
- 发布日期：2026-06-23
- 最近检查时间：2026-11-05T02:34+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地 release_date 记为 2026-06-23；火山方舟公告仅确认 2026 年 6 月发布，未确认该具体日。按要求保留本地值，不推测修订。
- doubao-seed-evolving 是滚动更新 API，官方说明同一 ID 会持续指向新版本（周期性更新）；没有冻结模型快照时，无法将评测分数对应到特定版本。来源：https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement；https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh
- 本轮没有可核实到冻结版本的目标成绩；没有从 Seed 2.1 或其他相近模型转移分数。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310), [Volcano Ark release announcement](https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement) | 2026-11-05T02:34+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:34+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:34+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:34+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:34+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official site](https://osworld-v2.xlang.ai/), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:34+08:00 |
| chartography | 未找到 | — | [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:34+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Volcano Ark model release announcement](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh) | 2026-11-05T02:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis ByteDance model listing](https://artificialanalysis.ai/models/creators/bytedance_seed), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:34+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Volcano Ark model release announcement](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh) | 2026-11-05T02:34+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index), [Volcano Ark model release announcement](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh) | 2026-11-05T02:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)
- [Volcano Ark release announcement](https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement)

研究备注：
- The current official v1.1 leaderboard does not list doubao-seed-evolving. Ark identifies it as a rolling model alias; no score tied to a frozen revision was found.

最近核验时间：2026-11-05T02:34+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The current official V2 leaderboard does not list doubao-seed-evolving. No score tied to a frozen revision was found.

最近核验时间：2026-11-05T02:34+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The official TB4 page dynamically rendered no readable model rows during this check. Ark documents the model as a rolling alias without a frozen benchmark revision.

尚未解决的问题：
- Cannot confirm whether a v4.0 score exists for a specific Seed Evolving snapshot.

最近核验时间：2026-11-05T02:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The official Science 0.1 results page does not list doubao-seed-evolving.

最近核验时间：2026-11-05T02:34+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The visible v1.0.6 board shows 10 entries plus a collapsed “119 more”; the visible rows do not include doubao-seed-evolving.

尚未解决的问题：
- The full board could not be inspected, and Ark describes this model as a weekly-updated alias without a frozen revision.

最近核验时间：2026-11-05T02:34+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official site](https://osworld-v2.xlang.ai/)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- OSWorld v2.1 materials provide evaluation instructions but no result for doubao-seed-evolving. Ark lists GUI/task capabilities but no score.

尚未解决的问题：
- No exact score or frozen API revision is published in the checked sources. A Seed2.1 qualitative claim is for a different model and is not transferred.

最近核验时间：2026-11-05T02:34+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The current official Chartography listing does not show doubao-seed-evolving or a score for it.

最近核验时间：2026-11-05T02:34+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Volcano Ark model release announcement](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh)

研究备注：
- The current official HLE board does not list doubao-seed-evolving. No frozen-revision score was found.

最近核验时间：2026-11-05T02:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis ByteDance model listing](https://artificialanalysis.ai/models/creators/bytedance_seed)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The current Artificial Analysis ByteDance listing does not include Seed Evolving. V5 HLE-Diamond is a different benchmark from original HLE.

最近核验时间：2026-11-05T02:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Volcano Ark model release announcement](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh)

研究备注：
- The official AA evaluation page does not list Seed Evolving. No AA v2.1 score or frozen model revision was found.

最近核验时间：2026-11-05T02:34+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index)
- [Volcano Ark model release announcement](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh)

研究备注：
- The current official Vals Index page does not list Seed Evolving; no fixed-version result was found.

最近核验时间：2026-11-05T02:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis ByteDance model listing",
          "url": "https://artificialanalysis.ai/models/creators/bytedance_seed"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The current Artificial Analysis ByteDance listing does not include Seed Evolving. V5 HLE-Diamond is a different benchmark from original HLE."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The visible v1.0.6 board shows 10 entries plus a collapsed “119 more”; the visible rows do not include doubao-seed-evolving."
      ],
      "status": "待核实",
      "unresolved": [
        "The full board could not be inspected, and Ark describes this model as a weekly-updated alias without a frozen revision."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The current official Chartography listing does not show doubao-seed-evolving or a score for it."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        },
        {
          "label": "Volcano Ark release announcement",
          "url": "https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement"
        }
      ],
      "notes": [
        "The current official v1.1 leaderboard does not list doubao-seed-evolving. Ark identifies it as a rolling model alias; no score tied to a frozen revision was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Volcano Ark model release announcement",
          "url": "https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh"
        }
      ],
      "notes": [
        "The official AA evaluation page does not list Seed Evolving. No AA v2.1 score or frozen model revision was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Scale HLE leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Volcano Ark model release announcement",
          "url": "https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh"
        }
      ],
      "notes": [
        "The current official HLE board does not list doubao-seed-evolving. No frozen-revision score was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "OSWorld v2.1 materials provide evaluation instructions but no result for doubao-seed-evolving. Ark lists GUI/task capabilities but no score."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact score or frozen API revision is published in the checked sources. A Seed2.1 qualitative claim is for a different model and is not transferred."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The current official V2 leaderboard does not list doubao-seed-evolving. No score tied to a frozen revision was found."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The official Science 0.1 results page does not list doubao-seed-evolving."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Terminal-Bench 4.0 release notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The official TB4 page dynamically rendered no readable model rows during this check. Ark documents the model as a rolling alias without a frozen benchmark revision."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot confirm whether a v4.0 score exists for a specific Seed Evolving snapshot."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Volcano Ark model release announcement",
          "url": "https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh"
        }
      ],
      "notes": [
        "The current official Vals Index page does not list Seed Evolving; no fixed-version result was found."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:34+08:00",
  "model_id": "bytedance-seed/seed-evolving",
  "model_notes": [
    "本地 release_date 记为 2026-06-23；火山方舟公告仅确认 2026 年 6 月发布，未确认该具体日。按要求保留本地值，不推测修订。",
    "doubao-seed-evolving 是滚动更新 API，官方说明同一 ID 会持续指向新版本（周期性更新）；没有冻结模型快照时，无法将评测分数对应到特定版本。来源：https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement；https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh",
    "本轮没有可核实到冻结版本的目标成绩；没有从 Seed 2.1 或其他相近模型转移分数。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
