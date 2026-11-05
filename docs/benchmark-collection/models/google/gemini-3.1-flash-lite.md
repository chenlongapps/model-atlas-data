# Gemini 3.1 Flash Lite Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.1-flash-lite
- 模型名称：Gemini 3.1 Flash Lite
- 发布日期：2026-05-07
- 最近检查时间：2026-11-05T06:22+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 本地模型 ID 是稳定版 gemini-3.1-flash-lite。Google 官方版本表确认稳定 ID 发布于 2026-05-07，preview ID gemini-3.1-flash-lite-preview 发布于 2026-03-03；本地 release_date 与稳定版日期一致。
- 多项候选成绩来自 Preview 型号或 Preview 阶段评测。没有将其移入稳定版 TOML；分数仅作为待核实研究备注保留。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T06:22+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:22+08:00 |
| terminal-bench-v4 | 待核实 | — | [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview), [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview), [Terminal-Bench 4 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-05T06:22+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview), [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview), [Terminal-Bench Science evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-05T06:22+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite), [AutomationBench official leaderboard](https://zapier.com/benchmarks), [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview) | 2026-11-05T06:22+08:00 |
| osworld-v2.1 | 待核实 | — | [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite), [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/) | 2026-11-05T06:22+08:00 |
| chartography | 未找到 | — | [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:22+08:00 |
| humanitys-last-exam | 待核实 | — | [Google Gemini 3.1 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/), [Google Gemini 3.1 Flash-Lite evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-1-flash-lite), [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview), [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview), [Humanity's Last Exam official evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:22+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview), [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:22+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview), [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:22+08:00 |
| vals-index-v2.2 | 未找到 | — | [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite), [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index), [Vals Index V2 historical page](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T06:22+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 可读取的官方 DeepSWE 榜单仅显示部分项目（21/28 models、57/70 configs），未见精确稳定版型号；可见列表不完整，不能据此判定未参评。

尚未解决的问题：
- 需要核实榜单未展示的配置中是否有精确稳定版 gemini-3.1-flash-lite。

最近核验时间：2026-11-05T06:22+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- 检查可访问的 SWE-bench Pro V2 官方公开榜单，未见精确稳定版型号；未映射 Gemini 3.1 Pro、其他 Flash 型号或旧版 SWE-bench Pro 成绩。

最近核验时间：2026-11-05T06:22+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview)
- [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview)
- [Terminal-Bench 4 evaluation methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- AA 比较页报告 Gemini 3.1 Flash-Lite 1%（整数显示）；方法为 Terminal-Bench 4.0、66 tasks、pass@1、mini-swe-agent（每任务三次重复）。比较页对应 preview ID，而本地文件是稳定 ID；没有写入 TOML。

尚未解决的问题：
- 1% 候选成绩属于 gemini-3.1-flash-lite-preview 还是可映射稳定版尚未证实；来源未给具体评测日期或 effort。

最近核验时间：2026-11-05T06:22+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview)
- [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview)
- [Terminal-Bench Science evaluation methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 比较页报告 Terminal-Bench-Science 0.1 为 0%（来源明确显示的零分）；方法为 0.1.0、70 tasks、pass@1、mini-swe-agent（三次重复）。该页对应 preview ID，不能直接写入本地稳定版。

尚未解决的问题：
- 0% 候选成绩的模型 ID 与本地稳定版不一致；来源未给具体评测日期或 effort。

最近核验时间：2026-11-05T06:22+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview)

研究备注：
- Zapier 官方页显示前 10 项并折叠另外 119 项，无法从可见表确认稳定版是否有记录。AA 页面中的 AutomationBench-AA 7% 是不同配置/名称，不映射到 AutomationBench 1.0.6。

尚未解决的问题：
- 需核实折叠榜单中的精确型号和 AutomationBench 1.0.6 结果。

最近核验时间：2026-11-05T06:22+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [OSWorld V2 official leaderboard](https://osworld-v2.xlang.ai/)

研究备注：
- 稳定版支持图像输入、文本输出和工具；OSWorld 榜单带有动态版本/数据集筛选，当前可读取视图未见精确型号，无法据此断定没有结果。

尚未解决的问题：
- 需检查其他榜单视图或原始结果数据，确认是否有精确稳定版成绩。

最近核验时间：2026-11-05T06:22+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 检查 Surge 官方榜单未见精确稳定版型号。榜单上 Gemini 3.1 Pro 与 Gemini 3.5 Flash-Lite 是不同型号，其成绩不映射。

最近核验时间：2026-11-05T06:22+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite model card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/)
- [Google Gemini 3.1 Flash-Lite evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-1-flash-lite)
- [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview)
- [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview)
- [Humanity's Last Exam official evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Google 模型卡候选为 16.0%（High）；AA 比较页另列 17%，评测配置不同。相关资料发布于 preview 阶段且 AA 页面是 preview ID；未合并来源差异，也未写入稳定版 TOML。

尚未解决的问题：
- 须确认 Google 模型卡成绩对应的精确 API ID；Google 卡片与 AA 候选配置/数值不同，且未公布具体评测日期。

最近核验时间：2026-11-05T06:22+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview)
- [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前 Preview 型号页/比较页显示指数候选值 6，页面方法版本为 v5.0.1；结果对应 Preview 展示型号，未确认与本地稳定 ID 的映射。

尚未解决的问题：
- 需确认 score 6 对应 v5.0.1 且属于稳定版，而非 Preview 版本。

最近核验时间：2026-11-05T06:22+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite Preview API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview)
- [Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison](https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- AA 比较页给 Gemini 3.1 Flash-Lite Preview 候选 431 Elo；页面未提供 effort、harness 或评测日期。因模型 ID 为 Preview，未写入稳定版 TOML。

尚未解决的问题：
- 需确认 431 Elo 是否适用于本地稳定模型 ID，并核实版本和测试条件。

最近核验时间：2026-11-05T06:22+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Google Gemini 3.1 Flash-Lite stable API documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
- [Vals Index v2.2 official page](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index V2 historical page](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- 当前 V2.2 官方页面未列本地稳定型号。历史 V2 页面和 Preview 型号页面属于旧版本/不同模型 ID，不迁移成绩。

最近核验时间：2026-11-05T06:22+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite Preview API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前 Preview 型号页/比较页显示指数候选值 6，页面方法版本为 v5.0.1；结果对应 Preview 展示型号，未确认与本地稳定 ID 的映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 score 6 对应 v5.0.1 且属于稳定版，而非 Preview 版本。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite stable API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite"
        },
        {
          "label": "AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview"
        }
      ],
      "notes": [
        "Zapier 官方页显示前 10 项并折叠另外 119 项，无法从可见表确认稳定版是否有记录。AA 页面中的 AutomationBench-AA 7% 是不同配置/名称，不映射到 AutomationBench 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "需核实折叠榜单中的精确型号和 AutomationBench 1.0.6 结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite stable API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "检查 Surge 官方榜单未见精确稳定版型号。榜单上 Gemini 3.1 Pro 与 Gemini 3.5 Flash-Lite 是不同型号，其成绩不映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite stable API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "可读取的官方 DeepSWE 榜单仅显示部分项目（21/28 models、57/70 configs），未见精确稳定版型号；可见列表不完整，不能据此判定未参评。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要核实榜单未展示的配置中是否有精确稳定版 gemini-3.1-flash-lite。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite Preview API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "AA 比较页给 Gemini 3.1 Flash-Lite Preview 候选 431 Elo；页面未提供 effort、harness 或评测日期。因模型 ID 为 Preview，未写入稳定版 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 431 Elo 是否适用于本地稳定模型 ID，并核实版本和测试条件。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite model card",
          "url": "https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/"
        },
        {
          "label": "Google Gemini 3.1 Flash-Lite evaluation methodology",
          "url": "https://deepmind.google/models/evals-methodology/gemini-3-1-flash-lite"
        },
        {
          "label": "Google Gemini 3.1 Flash-Lite Preview API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview"
        },
        {
          "label": "Humanity's Last Exam official evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Google 模型卡候选为 16.0%（High）；AA 比较页另列 17%，评测配置不同。相关资料发布于 preview 阶段且 AA 页面是 preview ID；未合并来源差异，也未写入稳定版 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "须确认 Google 模型卡成绩对应的精确 API ID；Google 卡片与 AA 候选配置/数值不同，且未公布具体评测日期。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite stable API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite"
        },
        {
          "label": "OSWorld V2 official leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "稳定版支持图像输入、文本输出和工具；OSWorld 榜单带有动态版本/数据集筛选，当前可读取视图未见精确型号，无法据此断定没有结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "需检查其他榜单视图或原始结果数据，确认是否有精确稳定版成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite stable API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "检查可访问的 SWE-bench Pro V2 官方公开榜单，未见精确稳定版型号；未映射 Gemini 3.1 Pro、其他 Flash 型号或旧版 SWE-bench Pro 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite Preview API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview"
        },
        {
          "label": "Terminal-Bench Science evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 比较页报告 Terminal-Bench-Science 0.1 为 0%（来源明确显示的零分）；方法为 0.1.0、70 tasks、pass@1、mini-swe-agent（三次重复）。该页对应 preview ID，不能直接写入本地稳定版。"
      ],
      "status": "待核实",
      "unresolved": [
        "0% 候选成绩的模型 ID 与本地稳定版不一致；来源未给具体评测日期或 effort。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite Preview API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview"
        },
        {
          "label": "Artificial Analysis Gemini 3.1 Flash-Lite Preview comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/gemini-3-1-flash-lite-preview-vs-gemini-3-1-pro-preview"
        },
        {
          "label": "Terminal-Bench 4 evaluation methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "AA 比较页报告 Gemini 3.1 Flash-Lite 1%（整数显示）；方法为 Terminal-Bench 4.0、66 tasks、pass@1、mini-swe-agent（每任务三次重复）。比较页对应 preview ID，而本地文件是稳定 ID；没有写入 TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "1% 候选成绩属于 gemini-3.1-flash-lite-preview 还是可映射稳定版尚未证实；来源未给具体评测日期或 effort。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:22+08:00",
      "checked_sources": [
        {
          "label": "Google Gemini 3.1 Flash-Lite stable API documentation",
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite"
        },
        {
          "label": "Vals Index v2.2 official page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index V2 historical page",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "当前 V2.2 官方页面未列本地稳定型号。历史 V2 页面和 Preview 型号页面属于旧版本/不同模型 ID，不迁移成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:22+08:00",
  "model_id": "google/gemini-3.1-flash-lite",
  "model_notes": [
    "本地模型 ID 是稳定版 gemini-3.1-flash-lite。Google 官方版本表确认稳定 ID 发布于 2026-05-07，preview ID gemini-3.1-flash-lite-preview 发布于 2026-03-03；本地 release_date 与稳定版日期一致。",
    "多项候选成绩来自 Preview 型号或 Preview 阶段评测。没有将其移入稳定版 TOML；分数仅作为待核实研究备注保留。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
