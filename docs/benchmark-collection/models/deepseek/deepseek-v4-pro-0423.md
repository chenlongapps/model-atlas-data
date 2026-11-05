# DeepSeek V4 Pro 0423 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4-pro-0423
- 模型名称：DeepSeek V4 Pro 0423
- 发布日期：2026-04-23
- 最近检查时间：2026-11-05T07:34+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地文件名称/发布日期为 DeepSeek V4 Pro 0423 / 2026-04-23；官方 V4 Preview 公告日期为 2026-04-24，且只确认 deepseek-v4-pro 通用模型。没有找到独立 0423 API 或权重标识，因此不从 0424/后续 Pro 版本迁移分数。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/), [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/), [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/) | 2026-11-05T07:34+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:34+08:00 |
| terminal-bench-v4 | 待核实 | — | [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4), [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Vals DeepSeek V4 Pro 型号页](https://www.vals.ai/models/deepseek_deepseek-v4-pro), [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/) | 2026-11-05T07:34+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:34+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks), [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:34+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/), [OSWorld-V2 v2.1 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:34+08:00 |
| chartography | 不适用 | — | [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:34+08:00 |
| humanitys-last-exam | 待核实 | — | [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348), [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/), [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 2026-11-05T07:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis GPT-5.5 Pro 型号页](https://artificialanalysis.ai/models/gpt-5-5-pro), [Artificial Analysis Intelligence Index V5 说明](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/) | 2026-11-05T07:34+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348), [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/) | 2026-11-05T07:34+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index), [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/) | 2026-11-05T07:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 官方榜单](https://deepswe.datacurve.ai/)
- [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/)
- [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/)

研究备注：
- DeepSWE v1.1 榜单显示 deepseek-v4-pro[max] 63%±6%，113 tasks、mini-swe-agent；没有 0423 标记，且 DeepSeek 后续版本沿用该 API 名称。榜单更新时间不是评测日期。

尚未解决的问题：
- 不能确认当前榜单的通用 deepseek-v4-pro 行属于本地 0423 检查点。

最近核验时间：2026-11-05T07:34+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [SWE-bench Pro V2 官方榜单](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Scale 页定义 V2 为更新后的 642-task split；当前公开结果列表未能确认 0423。DeepSeek V4-Pro 模型卡中的 SWE Pro 成绩未标 V2，不能移入。

尚未解决的问题：
- 公开榜单的动态/筛选内容不完整，且 DeepSeek V4-Pro 官方评测版本未区分 0423。

最近核验时间：2026-11-05T07:34+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Terminal-Bench 4.0 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Artificial Analysis Terminal-Bench 4.0 评测页](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Vals DeepSeek V4 Pro 型号页](https://www.vals.ai/models/deepseek_deepseek-v4-pro)
- [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/)

研究备注：
- Vals 有 DeepSeek V4 11.11% accuracy 候选，其型号页 slug 为 deepseek-v4-pro，但显示标题为 DeepSeek V4、发布日期 Apr 23，没有 0423 checkpoint 标记；未录入。
- 其他可见 DeepSeek 行明确属于 V4 Pro 0813、Flash 0731 等后续版本；当前公开榜单不支持将它们归给 0423。

尚未解决的问题：
- Vals 11.11% 行与本地 0423 的准确模型/权重快照无法确认。

最近核验时间：2026-11-05T07:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Terminal-Bench-Science 榜单与方法](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science 评测页](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Vals 当前可见 DeepSeek 行为 V4 Pro 0813 4.29%，不是 0423；榜单方法注明 v0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1。
- Artificial Analysis 当前页面仅公开部分模型，未能据缺席断言没有成绩。

尚未解决的问题：
- 未找到独立标注 0423 的 Terminal-Bench-Science 结果。

最近核验时间：2026-11-05T07:34+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 榜单](https://zapier.com/benchmarks)
- [DeepSeek API 更新记录](https://api-docs.deepseek.com/updates/)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- Zapier 当前页面标明 AutomationBench 1.0.6，但仅显示前 10 条并将其余 119 条折叠，不能据可见部分断言未评测。DeepSeek Pro GA 后续版本的 AutomationBench (Public) 分数不属于 0423，也没有确认该版本。

尚未解决的问题：
- 折叠的榜单条目不能逐一确认，且 0423 独立模型身份未证实。

最近核验时间：2026-11-05T07:34+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 官方榜单](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 v2.1 发布记录](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- OSWorld 榜单为动态页面，未能确认该精确模型版本的 v2.1 结果；不把其它版本或后续模型分数迁入。

尚未解决的问题：
- 公开动态页面没有可确认的 0423 行。

最近核验时间：2026-11-05T07:34+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- 本地文件和官方 V4 模型卡标注 DeepSeek V4 Pro 为文本输入/输出；Chartography 要求模型读取图表图像，因此不适用于文本版。
- 本地 0423 独立检查点身份未获官方确认；未将其他视觉模型的成绩迁移过来。

最近核验时间：2026-11-05T07:34+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348)
- [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/)
- [DeepSeek V4 Pro 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

研究备注：
- 官方技术报告列通用 V4 Pro Max 的 HLE 37.7 Pass@1 和带工具 48.2，但没有确认这些成绩对应本地 0423 检查点。

尚未解决的问题：
- 官方公告只确认 2026-04-24 的 V4 Pro Preview；本地记录日期为 2026-04-23，独立 checkpoint 与 HLE 归属未确认。

最近核验时间：2026-11-05T07:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis GPT-5.5 Pro 型号页](https://artificialanalysis.ai/models/gpt-5-5-pro)
- [Artificial Analysis Intelligence Index V5 说明](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/)

研究备注：
- Artificial Analysis 精确型号页对应 DeepSeek V4 Pro 0424，当前 V5.0.1 摘要为 N/A/Unknown；没有 0423 的精确型号页或 V5 分数。

尚未解决的问题：
- 本地 0423 与官方 0424 的日期/身份不一致，无法把后者页面状态或旧指数分数归给 0423。

最近核验时间：2026-11-05T07:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [GDPval-AA v2.1 榜单与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [DeepSeek V4 技术报告](https://arxiv.org/html/2606.19348)
- [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/)

研究备注：
- AA v2.1 榜单列 DeepSeek V4 Pro 0424 (Max) 1166 Elo（CI −17/+17）；官方 V4 报告的 Pro Max 1554 Elo 未注明 v2.1。两者都不能映射为本地 0423。

尚未解决的问题：
- 没有确认 0423 独立检查点；不把 0424 或通用 V4 Pro 结果迁移到本地 ID。

最近核验时间：2026-11-05T07:34+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index v2.2 榜单](https://www.vals.ai/benchmarks/vals_index)
- [DeepSeek V4 Preview 官方公告](https://deepseek.com/en/news/v4-preview/)

研究备注：
- 当前 Vals v2.2 页可见 DeepSeek V4 Pro 0813 等后续版本，未见 0423。榜单仅显示部分 latest/top/frontier 模型，缺席不足以证明未评测。

尚未解决的问题：
- 未能从部分榜单确认本地 0423 型号。

最近核验时间：2026-11-05T07:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GPT-5.5 Pro 型号页",
          "url": "https://artificialanalysis.ai/models/gpt-5-5-pro"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 说明",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "DeepSeek V4 Preview 官方公告",
          "url": "https://deepseek.com/en/news/v4-preview/"
        }
      ],
      "notes": [
        "Artificial Analysis 精确型号页对应 DeepSeek V4 Pro 0424，当前 V5.0.1 摘要为 N/A/Unknown；没有 0423 的精确型号页或 V5 分数。"
      ],
      "status": "待核实",
      "unresolved": [
        "本地 0423 与官方 0424 的日期/身份不一致，无法把后者页面状态或旧指数分数归给 0423。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 榜单",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "DeepSeek API 更新记录",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Zapier 当前页面标明 AutomationBench 1.0.6，但仅显示前 10 条并将其余 119 条折叠，不能据可见部分断言未评测。DeepSeek Pro GA 后续版本的 AutomationBench (Public) 分数不属于 0423，也没有确认该版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "折叠的榜单条目不能逐一确认，且 0423 独立模型身份未证实。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "本地文件和官方 V4 模型卡标注 DeepSeek V4 Pro 为文本输入/输出；Chartography 要求模型读取图表图像，因此不适用于文本版。",
        "本地 0423 独立检查点身份未获官方确认；未将其他视觉模型的成绩迁移过来。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 官方榜单",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSeek V4 Preview 官方公告",
          "url": "https://deepseek.com/en/news/v4-preview/"
        },
        {
          "label": "DeepSeek API 更新记录",
          "url": "https://api-docs.deepseek.com/updates/"
        }
      ],
      "notes": [
        "DeepSWE v1.1 榜单显示 deepseek-v4-pro[max] 63%±6%，113 tasks、mini-swe-agent；没有 0423 标记，且 DeepSeek 后续版本沿用该 API 名称。榜单更新时间不是评测日期。"
      ],
      "status": "待核实",
      "unresolved": [
        "不能确认当前榜单的通用 deepseek-v4-pro 行属于本地 0423 检查点。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA v2.1 榜单与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "DeepSeek V4 技术报告",
          "url": "https://arxiv.org/html/2606.19348"
        },
        {
          "label": "DeepSeek V4 Preview 官方公告",
          "url": "https://deepseek.com/en/news/v4-preview/"
        }
      ],
      "notes": [
        "AA v2.1 榜单列 DeepSeek V4 Pro 0424 (Max) 1166 Elo（CI −17/+17）；官方 V4 报告的 Pro Max 1554 Elo 未注明 v2.1。两者都不能映射为本地 0423。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有确认 0423 独立检查点；不把 0424 或通用 V4 Pro 结果迁移到本地 ID。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 技术报告",
          "url": "https://arxiv.org/html/2606.19348"
        },
        {
          "label": "DeepSeek V4 Preview 官方公告",
          "url": "https://deepseek.com/en/news/v4-preview/"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "官方技术报告列通用 V4 Pro Max 的 HLE 37.7 Pass@1 和带工具 48.2，但没有确认这些成绩对应本地 0423 检查点。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方公告只确认 2026-04-24 的 V4 Pro Preview；本地记录日期为 2026-04-23，独立 checkpoint 与 HLE 归属未确认。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方榜单",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 v2.1 发布记录",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "OSWorld 榜单为动态页面，未能确认该精确模型版本的 v2.1 结果；不把其它版本或后续模型分数迁入。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开动态页面没有可确认的 0423 行。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 官方榜单",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Scale 页定义 V2 为更新后的 642-task split；当前公开结果列表未能确认 0423。DeepSeek V4-Pro 模型卡中的 SWE Pro 成绩未标 V2，不能移入。"
      ],
      "status": "待核实",
      "unresolved": [
        "公开榜单的动态/筛选内容不完整，且 DeepSeek V4-Pro 官方评测版本未区分 0423。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench-Science 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "DeepSeek V4 Pro 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
        }
      ],
      "notes": [
        "Vals 当前可见 DeepSeek 行为 V4 Pro 0813 4.29%，不是 0423；榜单方法注明 v0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1。",
        "Artificial Analysis 当前页面仅公开部分模型，未能据缺席断言没有成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到独立标注 0423 的 Terminal-Bench-Science 结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Terminal-Bench 4.0 榜单与方法",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 评测页",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Vals DeepSeek V4 Pro 型号页",
          "url": "https://www.vals.ai/models/deepseek_deepseek-v4-pro"
        },
        {
          "label": "DeepSeek V4 Preview 官方公告",
          "url": "https://deepseek.com/en/news/v4-preview/"
        }
      ],
      "notes": [
        "Vals 有 DeepSeek V4 11.11% accuracy 候选，其型号页 slug 为 deepseek-v4-pro，但显示标题为 DeepSeek V4、发布日期 Apr 23，没有 0423 checkpoint 标记；未录入。",
        "其他可见 DeepSeek 行明确属于 V4 Pro 0813、Flash 0731 等后续版本；当前公开榜单不支持将它们归给 0423。"
      ],
      "status": "待核实",
      "unresolved": [
        "Vals 11.11% 行与本地 0423 的准确模型/权重快照无法确认。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T07:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 榜单",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "DeepSeek V4 Preview 官方公告",
          "url": "https://deepseek.com/en/news/v4-preview/"
        }
      ],
      "notes": [
        "当前 Vals v2.2 页可见 DeepSeek V4 Pro 0813 等后续版本，未见 0423。榜单仅显示部分 latest/top/frontier 模型，缺席不足以证明未评测。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能从部分榜单确认本地 0423 型号。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T07:34+08:00",
  "model_id": "deepseek/deepseek-v4-pro-0423",
  "model_notes": [
    "本地文件名称/发布日期为 DeepSeek V4 Pro 0423 / 2026-04-23；官方 V4 Preview 公告日期为 2026-04-24，且只确认 deepseek-v4-pro 通用模型。没有找到独立 0423 API 或权重标识，因此不从 0424/后续 Pro 版本迁移分数。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
