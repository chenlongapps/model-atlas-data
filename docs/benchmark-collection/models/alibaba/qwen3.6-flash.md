# Qwen3.6 Flash Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.6-flash
- 模型名称：Qwen3.6 Flash
- 发布日期：2026-04-27
- 最近检查时间：2026-11-05T07:03+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Alibaba Model Studio 官方文档列出 API ID qwen3.6-flash 及快照 qwen3.6-flash-2026-04-16；快照日期不是评测日期。
- Alibaba 发布文将 Qwen3.6-35B-A3B 与 API ID qwen3.6-flash 联系起来，但其 SWE-Bench Pro/TBench 2.0 分数不属于 Pro V2/TBench 4，未迁移。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE official leaderboard](https://deepswe.datacurve.ai/), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash), [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | 2026-11-05T07:03+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash), [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | 2026-11-05T07:03+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 official page](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash), [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | 2026-11-05T07:03+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science 0.1 official page](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash), [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | 2026-11-05T07:03+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench official leaderboard](https://zapier.com/benchmarks), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash) | 2026-11-05T07:03+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2.1 official release materials](https://github.com/xlang-ai/OSWorld-V2/releases), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash) | 2026-11-05T07:03+08:00 |
| chartography | 待核实 | — | [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash) | 2026-11-05T07:03+08:00 |
| humanitys-last-exam | 待核实 | — | [Artificial Analysis HLE page](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash), [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | 2026-11-05T07:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Index V5 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash) | 2026-11-05T07:03+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [GDPval-AA v2.1 official leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash) | 2026-11-05T07:03+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index), [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash) | 2026-11-05T07:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)
- [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043)

研究备注：
- DeepSWE 只显示 21/28 models、57/70 configs；Alibaba 发布文未列该目标项。

尚未解决的问题：
- 需检查未展示配置和固定 API 快照。

最近核验时间：2026-11-05T07:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)
- [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043)

研究备注：
- Alibaba 文中报告 SWE-Bench Pro 49.5，但未标 V2；当前可见 Scale V2 榜无精确 API 型号，旧版分数不映射。

尚未解决的问题：
- 需核验完整 V2 榜及 API 快照。

最近核验时间：2026-11-05T07:03+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 official page](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)
- [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043)

研究备注：
- Alibaba 文中报告 Terminal-Bench 2.0 51.5，不是 v4；AA 当前只显示 28/240 models。

尚未解决的问题：
- 需核查完整 AA v4 榜及具体快照。

最近核验时间：2026-11-05T07:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official page](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)
- [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043)

研究备注：
- Alibaba 发布文未列 Science 0.1；AA 当前只显示 28/120 models。

尚未解决的问题：
- 需检查完整榜单。

最近核验时间：2026-11-05T07:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)

研究备注：
- Zapier v1.0.6 榜单另有 119 条折叠，当前无法确认该 API 型号或快照是否有成绩。

尚未解决的问题：
- 需核查完整榜单和快照。

最近核验时间：2026-11-05T07:03+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 official release materials](https://github.com/xlang-ai/OSWorld-V2/releases)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)

研究备注：
- OSWorld V2 官方榜单是动态页，当前无法确认 qwen3.6-flash 的精确成绩和固定快照。

尚未解决的问题：
- 需核实完整榜单与评测快照。

最近核验时间：2026-11-05T07:03+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)

研究备注：
- Qwen3.6 Flash 支持图像输入；Chartography 当前公开榜单可见部分无精确型号，但数据展示不完整。

尚未解决的问题：
- 需核查完整榜单和快照。

最近核验时间：2026-11-05T07:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis HLE page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)
- [Alibaba Qwen3.6-35B-A3B announcement](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043)

研究备注：
- 未找到精确 Flash API 型号的 HLE；AA HLE 页面只公开展示部分模型，未移用 Qwen3.6 27B/35B 权重成绩。

尚未解决的问题：
- 需核验完整榜单及 API checkpoint。

最近核验时间：2026-11-05T07:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Index V5 page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)

研究备注：
- 未找到精确 Flash API 型号的 Index V5 分数；可见 Qwen3.6 27B/35B 是不同型号，未映射。

尚未解决的问题：
- 需核验完整指数数据并固定 API checkpoint。

最近核验时间：2026-11-05T07:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [GDPval-AA v2.1 official leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)

研究备注：
- GDPval 页当前仅展示 308 个模型中的 27 个；可见 Qwen3.6 开源型号不是 Flash API exact。

尚未解决的问题：
- 需核验完整榜单和 API checkpoint。

最近核验时间：2026-11-05T07:03+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)
- [Alibaba Model Studio Qwen3.6 Flash documentation](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash)

研究备注：
- Vals v2.2 当前只显示 latest/top/frontier 子集，无法判断完整数据是否有 Qwen3.6 Flash。

尚未解决的问题：
- 需检查完整榜单。

最近核验时间：2026-11-05T07:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Index V5 page",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        }
      ],
      "notes": [
        "未找到精确 Flash API 型号的 Index V5 分数；可见 Qwen3.6 27B/35B 是不同型号，未映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整指数数据并固定 API checkpoint。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        }
      ],
      "notes": [
        "Zapier v1.0.6 榜单另有 119 条折叠，当前无法确认该 API 型号或快照是否有成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查完整榜单和快照。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Chartography official benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        }
      ],
      "notes": [
        "Qwen3.6 Flash 支持图像输入；Chartography 当前公开榜单可见部分无精确型号，但数据展示不完整。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查完整榜单和快照。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        },
        {
          "label": "Alibaba Qwen3.6-35B-A3B announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043"
        }
      ],
      "notes": [
        "DeepSWE 只显示 21/28 models、57/70 configs；Alibaba 发布文未列该目标项。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查未展示配置和固定 API 快照。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 official leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        }
      ],
      "notes": [
        "GDPval 页当前仅展示 308 个模型中的 27 个；可见 Qwen3.6 开源型号不是 Flash API exact。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整榜单和 API checkpoint。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis HLE page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        },
        {
          "label": "Alibaba Qwen3.6-35B-A3B announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043"
        }
      ],
      "notes": [
        "未找到精确 Flash API 型号的 HLE；AA HLE 页面只公开展示部分模型，未移用 Qwen3.6 27B/35B 权重成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整榜单及 API checkpoint。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 official release materials",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        }
      ],
      "notes": [
        "OSWorld V2 官方榜单是动态页，当前无法确认 qwen3.6-flash 的精确成绩和固定快照。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实完整榜单与评测快照。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        },
        {
          "label": "Alibaba Qwen3.6-35B-A3B announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043"
        }
      ],
      "notes": [
        "Alibaba 文中报告 SWE-Bench Pro 49.5，但未标 V2；当前可见 Scale V2 榜无精确 API 型号，旧版分数不映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核验完整 V2 榜及 API 快照。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official page",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        },
        {
          "label": "Alibaba Qwen3.6-35B-A3B announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043"
        }
      ],
      "notes": [
        "Alibaba 发布文未列 Science 0.1；AA 当前只显示 28/120 models。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4.0 official page",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        },
        {
          "label": "Alibaba Qwen3.6-35B-A3B announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043"
        }
      ],
      "notes": [
        "Alibaba 文中报告 Terminal-Bench 2.0 51.5，不是 v4；AA 当前只显示 28/240 models。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核查完整 AA v4 榜及具体快照。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:03+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Alibaba Model Studio Qwen3.6 Flash documentation",
          "url": "https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-6-flash"
        }
      ],
      "notes": [
        "Vals v2.2 当前只显示 latest/top/frontier 子集，无法判断完整数据是否有 Qwen3.6 Flash。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查完整榜单。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:03+08:00",
  "model_id": "alibaba/qwen3.6-flash",
  "model_notes": [
    "Alibaba Model Studio 官方文档列出 API ID qwen3.6-flash 及快照 qwen3.6-flash-2026-04-16；快照日期不是评测日期。",
    "Alibaba 发布文将 Qwen3.6-35B-A3B 与 API ID qwen3.6-flash 联系起来，但其 SWE-Bench Pro/TBench 2.0 分数不属于 Pro V2/TBench 4，未迁移。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
