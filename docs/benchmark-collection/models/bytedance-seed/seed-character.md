# Seed Character Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：bytedance-seed/seed-character
- 模型名称：Seed Character
- 发布日期：2026-06-23
- 最近检查时间：2026-11-05T02:33+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 火山方舟公开列表出现两个不同版本：doubao-seed-character-260628 与 doubao-seed-character-251128，图像输入能力不同；本地模型记录没有 API ID 后缀。Character 是独立角色模型，不是 Seed2.1 Pro/Turbo 的变体。来源：https://www.volcengine.com/docs/82379/1330310；https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement
- 本地 release_date 为 2026-06-23；官方资料只确认 2026 年 6 月及 API ID 日期标记，无法确认该具体发布日期，故不改写模型 TOML 日期。
- 本轮没有可核实到该模型准确版本的目标成绩；没有转移 Seed2.1 的结果。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Volcano Ark release announcement](https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement) | 2026-11-05T02:33+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official site](https://osworld-v2.xlang.ai/), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| chartography | 待核实 | — | [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| humanitys-last-exam | 未找到 | — | [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis ByteDance model listing](https://artificialanalysis.ai/models/creators/bytedance_seed), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index), [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310) | 2026-11-05T02:33+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The current DeepSWE v1.1 leaderboard does not list either identified Seed Character API ID.

最近核验时间：2026-11-05T02:33+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Volcano Ark release announcement](https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement)

研究备注：
- The current V2 leaderboard does not list the generic Seed Character name or either identified API ID.

最近核验时间：2026-11-05T02:33+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The official dynamic v4 board response did not expose readable model rows. The matching Character API revision is also not identified in the repository model entry.

尚未解决的问题：
- Cannot verify whether a v4.0 score exists for either Seed Character API version; do not transfer Seed2.1 results.

最近核验时间：2026-11-05T02:33+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The official Science 0.1 results do not list Seed Character.

最近核验时间：2026-11-05T02:33+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The visible v1.0.6 board shows 10 entries and a collapsed “119 more” section; neither exact Character API ID is visible.

尚未解决的问题：
- The complete board could not be inspected, and the repository does not identify which Character API revision is intended.

最近核验时间：2026-11-05T02:33+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official site](https://osworld-v2.xlang.ai/)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- OSWorld materials checked provide evaluation instructions but no matching Seed Character result. Ark lists Character API IDs with different image-input capability.

尚未解决的问题：
- The local model entry does not identify doubao-seed-character-260628 versus doubao-seed-character-251128, so its tested computer-use capability/version cannot be pinned down.

最近核验时间：2026-11-05T02:33+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The current official Chartography listing does not show an exact Seed Character result. Ark lists 260628 and 251128 variants with different image support.

尚未解决的问题：
- The local model entry omits the API revision; the variants have different image-input capability, so exact eligibility and any result cannot be tied to this entry.

最近核验时间：2026-11-05T02:33+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The official HLE board does not list either identified Seed Character API ID.

最近核验时间：2026-11-05T02:33+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis ByteDance model listing](https://artificialanalysis.ai/models/creators/bytedance_seed)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The current Artificial Analysis ByteDance listing does not include Seed Character.

最近核验时间：2026-11-05T02:33+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The official AA v2.1 evaluation page does not list Seed Character.

最近核验时间：2026-11-05T02:33+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index)
- [Volcano Ark model list](https://www.volcengine.com/docs/82379/1330310)

研究备注：
- The current official Vals Index listing does not show Seed Character.

最近核验时间：2026-11-05T02:33+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:33+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis ByteDance model listing",
          "url": "https://artificialanalysis.ai/models/creators/bytedance_seed"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The current Artificial Analysis ByteDance listing does not include Seed Character."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:33+08:00",
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
        "The visible v1.0.6 board shows 10 entries and a collapsed “119 more” section; neither exact Character API ID is visible."
      ],
      "status": "待核实",
      "unresolved": [
        "The complete board could not be inspected, and the repository does not identify which Character API revision is intended."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:33+08:00",
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
        "The current official Chartography listing does not show an exact Seed Character result. Ark lists 260628 and 251128 variants with different image support."
      ],
      "status": "待核实",
      "unresolved": [
        "The local model entry omits the API revision; the variants have different image-input capability, so exact eligibility and any result cannot be tied to this entry."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:33+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The current DeepSWE v1.1 leaderboard does not list either identified Seed Character API ID."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:33+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The official AA v2.1 evaluation page does not list Seed Character."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:33+08:00",
      "checked_sources": [
        {
          "label": "Scale HLE leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The official HLE board does not list either identified Seed Character API ID."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:33+08:00",
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
        "OSWorld materials checked provide evaluation instructions but no matching Seed Character result. Ark lists Character API IDs with different image-input capability."
      ],
      "status": "待核实",
      "unresolved": [
        "The local model entry does not identify doubao-seed-character-260628 versus doubao-seed-character-251128, so its tested computer-use capability/version cannot be pinned down."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:33+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Volcano Ark release announcement",
          "url": "https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement"
        }
      ],
      "notes": [
        "The current V2 leaderboard does not list the generic Seed Character name or either identified API ID."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:33+08:00",
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
        "The official Science 0.1 results do not list Seed Character."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:33+08:00",
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
        "The official dynamic v4 board response did not expose readable model rows. The matching Character API revision is also not identified in the repository model entry."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot verify whether a v4.0 score exists for either Seed Character API version; do not transfer Seed2.1 results."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:33+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Volcano Ark model list",
          "url": "https://www.volcengine.com/docs/82379/1330310"
        }
      ],
      "notes": [
        "The current official Vals Index listing does not show Seed Character."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:33+08:00",
  "model_id": "bytedance-seed/seed-character",
  "model_notes": [
    "火山方舟公开列表出现两个不同版本：doubao-seed-character-260628 与 doubao-seed-character-251128，图像输入能力不同；本地模型记录没有 API ID 后缀。Character 是独立角色模型，不是 Seed2.1 Pro/Turbo 的变体。来源：https://www.volcengine.com/docs/82379/1330310；https://console.volcengine.com/ark/region:cn-beijing/docs/model-release-announcement",
    "本地 release_date 为 2026-06-23；官方资料只确认 2026 年 6 月及 API ID 日期标记，无法确认该具体发布日期，故不改写模型 TOML 日期。",
    "本轮没有可核实到该模型准确版本的目标成绩；没有转移 Seed2.1 的结果。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
