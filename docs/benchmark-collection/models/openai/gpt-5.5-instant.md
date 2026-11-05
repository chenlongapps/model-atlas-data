# GPT-5.5 Instant Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-5.5-instant
- 模型名称：GPT-5.5 Instant
- 发布日期：2026-05-05
- 最近检查时间：2026-11-05T06:41+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地记录将模型 API slug 关联到动态别名 chat-latest。OpenAI 文档说明该别名会更新底层 snapshot；候选排行榜中标为 GPT-5.5 Instant (May 2026) 或 GPT-5.5 [xhigh] 的分数不能在未确认 snapshot 时直接归入当前目标。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [OpenAI API changelog](https://developers.openai.com/api/docs/changelog), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:41+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:41+08:00 |
| terminal-bench-v4 | 待核实 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:41+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:41+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [OpenAI API changelog](https://developers.openai.com/api/docs/changelog), [AutomationBench official leaderboard](https://zapier.com/benchmarks) | 2026-11-05T06:41+08:00 |
| osworld-v2.1 | 待核实 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:41+08:00 |
| chartography | 未找到 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [OpenAI GPT-5.5 Instant system card](https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:41+08:00 |
| humanitys-last-exam | 待核实 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [OpenAI API changelog](https://developers.openai.com/api/docs/changelog), [OpenAI GPT-5.5 Instant system card](https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf), [AA GPT-5.5 Instant May 2026 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-5-instant-05-26-vs-gpt-5-5-non-reasoning), [Humanity's Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:41+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [AA GPT-5.5 Instant May 2026 model page](https://artificialanalysis.ai/models/gpt-5-5-instant-05-26), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:41+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [AA GPT-5.5 Instant May 2026 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-5-instant-05-26-vs-gpt-5-5-non-reasoning), [GDPval-AA v2.1 evaluation methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:41+08:00 |
| vals-index-v2.2 | 未找到 | — | [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:41+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE v1.1 榜单有 GPT-5.5 [xhigh] 候选 67%±6%，但没有固定 API snapshot 或 Instant 标记；本地文件指向会更新底层版本的 chat-latest，未写入候选。

尚未解决的问题：
- 需核实 GPT-5.5 [xhigh] 是否来自 GPT-5.5 Instant 的特定 snapshot，而非其他 GPT-5.5 版本。

最近核验时间：2026-11-05T06:41+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查 Scale 当前 SWE-bench Pro V2 公榜未发现精确 GPT-5.5 Instant 行；未映射 GPT-5.5、GPT-5.6 或其他快照。

最近核验时间：2026-11-05T06:41+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [Terminal-Bench 4.0 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- Artificial Analysis 当前可见 Terminal-Bench 4 榜单仅展示 28/240 个模型，未见可确认的精确 GPT-5.5 Instant snapshot。

尚未解决的问题：
- 需检查榜单其余模型/配置，或确认是否有固定 Instant snapshot 成绩。

最近核验时间：2026-11-05T06:41+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [Terminal-Bench Science 0.1 evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- Artificial Analysis 当前可见 Terminal-Bench Science 0.1 榜单仅展示 28/120 个模型，未见可确认的精确 GPT-5.5 Instant snapshot。

尚未解决的问题：
- 需检查榜单其余模型/配置，或确认是否有固定 Instant snapshot 成绩。

最近核验时间：2026-11-05T06:41+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)

研究备注：
- 模型支持工具，但 Zapier 榜单把额外 119 条折叠隐藏；动态 chat-latest 不能唯一锁定评测 snapshot。

尚未解决的问题：
- 需确认完整 1.0.6 榜单中是否存在与本地目标版本精确匹配的行。

最近核验时间：2026-11-05T06:41+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 支持图像输入和函数调用，但官方模型页未提供内置 Computer Use 工具；当前 OSWorld 榜单动态，尚未确认精确型号及兼容 harness。

尚未解决的问题：
- 需核实是否有固定 GPT-5.5 Instant snapshot 的 OSWorld 2.1 记录及测试配置。

最近核验时间：2026-11-05T06:41+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [OpenAI GPT-5.5 Instant system card](https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 当前 Surge 榜单未见精确 GPT-5.5 Instant 行；可见的 GPT 5.5 (xHigh reasoning) 31% 是不同标记/配置，未映射。

最近核验时间：2026-11-05T06:41+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- [OpenAI GPT-5.5 Instant system card](https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf)
- [AA GPT-5.5 Instant May 2026 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-5-instant-05-26-vs-gpt-5-5-non-reasoning)
- [Humanity's Last Exam evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA May 2026 比较页报告 GPT-5.5 Instant 22% 候选；AA 方法用 2,158 道 HLE 文本题、pass@1 和 GPT-5.6 Luna (medium) equality checker。候选未确认与本地动态 chat-latest snapshot 一致，且不是完整 2,500 题集，未写入。

尚未解决的问题：
- 需确认 May 2026 snapshot 与本地模型目标的对应关系；来源未公布 effort 和评测日期。

最近核验时间：2026-11-05T06:41+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [AA GPT-5.5 Instant May 2026 model page](https://artificialanalysis.ai/models/gpt-5-5-instant-05-26)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA May 2026 Instant 页面当前 V5 指数为 N/A；旧页面的 23* 是 v4.3.2 估算值，不作为 V5 成绩。

最近核验时间：2026-11-05T06:41+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [AA GPT-5.5 Instant May 2026 comparison](https://artificialanalysis.ai/models/comparisons/gpt-5-5-instant-05-26-vs-gpt-5-5-non-reasoning)
- [GDPval-AA v2.1 evaluation methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 检查的 May Instant 比较页未给出精确可匹配的 GDPval-AA v2.1 Elo；AA 页面提到 June Instant token usage，不是目标快照且无 Elo，未迁移。

最近核验时间：2026-11-05T06:41+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI chat-latest model documentation](https://developers.openai.com/api/docs/models/chat-latest)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前 Vals Index v2.2 页面未见精确 GPT-5.5 Instant 型号；没有从 GPT-5.5 xHigh 或其他快照转移成绩。

最近核验时间：2026-11-05T06:41+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "AA GPT-5.5 Instant May 2026 model page",
          "url": "https://artificialanalysis.ai/models/gpt-5-5-instant-05-26"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA May 2026 Instant 页面当前 V5 指数为 N/A；旧页面的 23* 是 v4.3.2 估算值，不作为 V5 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "OpenAI API changelog",
          "url": "https://developers.openai.com/api/docs/changelog"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "模型支持工具，但 Zapier 榜单把额外 119 条折叠隐藏；动态 chat-latest 不能唯一锁定评测 snapshot。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认完整 1.0.6 榜单中是否存在与本地目标版本精确匹配的行。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "OpenAI GPT-5.5 Instant system card",
          "url": "https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "当前 Surge 榜单未见精确 GPT-5.5 Instant 行；可见的 GPT 5.5 (xHigh reasoning) 31% 是不同标记/配置，未映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "OpenAI API changelog",
          "url": "https://developers.openai.com/api/docs/changelog"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE v1.1 榜单有 GPT-5.5 [xhigh] 候选 67%±6%，但没有固定 API snapshot 或 Instant 标记；本地文件指向会更新底层版本的 chat-latest，未写入候选。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实 GPT-5.5 [xhigh] 是否来自 GPT-5.5 Instant 的特定 snapshot，而非其他 GPT-5.5 版本。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "AA GPT-5.5 Instant May 2026 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-5-instant-05-26-vs-gpt-5-5-non-reasoning"
        },
        {
          "label": "GDPval-AA v2.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "检查的 May Instant 比较页未给出精确可匹配的 GDPval-AA v2.1 Elo；AA 页面提到 June Instant token usage，不是目标快照且无 Elo，未迁移。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "OpenAI API changelog",
          "url": "https://developers.openai.com/api/docs/changelog"
        },
        {
          "label": "OpenAI GPT-5.5 Instant system card",
          "url": "https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf"
        },
        {
          "label": "AA GPT-5.5 Instant May 2026 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-5-instant-05-26-vs-gpt-5-5-non-reasoning"
        },
        {
          "label": "Humanity's Last Exam evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA May 2026 比较页报告 GPT-5.5 Instant 22% 候选；AA 方法用 2,158 道 HLE 文本题、pass@1 和 GPT-5.6 Luna (medium) equality checker。候选未确认与本地动态 chat-latest snapshot 一致，且不是完整 2,500 题集，未写入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 May 2026 snapshot 与本地模型目标的对应关系；来源未公布 effort 和评测日期。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "支持图像输入和函数调用，但官方模型页未提供内置 Computer Use 工具；当前 OSWorld 榜单动态，尚未确认精确型号及兼容 harness。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实是否有固定 GPT-5.5 Instant snapshot 的 OSWorld 2.1 记录及测试配置。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查 Scale 当前 SWE-bench Pro V2 公榜未发现精确 GPT-5.5 Instant 行；未映射 GPT-5.5、GPT-5.6 或其他快照。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "Terminal-Bench Science 0.1 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "Artificial Analysis 当前可见 Terminal-Bench Science 0.1 榜单仅展示 28/120 个模型，未见可确认的精确 GPT-5.5 Instant snapshot。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查榜单其余模型/配置，或确认是否有固定 Instant snapshot 成绩。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "Terminal-Bench 4.0 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "Artificial Analysis 当前可见 Terminal-Bench 4 榜单仅展示 28/240 个模型，未见可确认的精确 GPT-5.5 Instant snapshot。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查榜单其余模型/配置，或确认是否有固定 Instant snapshot 成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:41+08:00",
      "checked_sources": [
        {
          "label": "OpenAI chat-latest model documentation",
          "url": "https://developers.openai.com/api/docs/models/chat-latest"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前 Vals Index v2.2 页面未见精确 GPT-5.5 Instant 型号；没有从 GPT-5.5 xHigh 或其他快照转移成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:41+08:00",
  "model_id": "openai/gpt-5.5-instant",
  "model_notes": [
    "本地记录将模型 API slug 关联到动态别名 chat-latest。OpenAI 文档说明该别名会更新底层 snapshot；候选排行榜中标为 GPT-5.5 Instant (May 2026) 或 GPT-5.5 [xhigh] 的分数不能在未确认 snapshot 时直接归入当前目标。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
