# Qwen3.7 Plus Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.7-plus
- 模型名称：Qwen3.7 Plus
- 发布日期：2026-06-02
- 最近检查时间：2026-11-05T04:28+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- 精确型号文档对应快照 qwen3.7-plus-2026-05-26。模型 TOML 的 release_date 为 2026-06-02；Alibaba Cloud 官方生命周期页列出 Global 日期 2026-06-01，官方介绍文章日期为 2026-06-03。日期定义存在一天差异，本轮按当前仓库 release_date 维持队列顺序，并记录来源差异。
- 新增 Chartography 15.8%、AA 原始 HLE 36% 和 GDPval-AA v2.1 768 Elo 三条成绩；未将旧 AA Index v4.3.2 的综合分数映射为 V5。
- 后续核对 AA 精确型号页确认其比较数据对应 reasoning 版本，已将该版本条件补入 HLE 和 GDPval-AA 成绩的 variant 字段。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206) | 2026-11-05T04:21+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T04:21+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206) | 2026-11-05T04:21+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206) | 2026-11-05T04:21+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Alibaba Qwen3.7 Plus model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus) | 2026-11-05T04:21+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 official site](https://osworld-v2.xlang.ai/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [Alibaba Qwen3.7 Plus model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus) | 2026-11-05T04:21+08:00 |
| chartography | 已收录 | 15.8 (metric=accuracy (mean; Pass@1); dataset=100-task Chartography set; variant=Thinking on; 10 runs per task; harness=Inspect AI; Gemini 3.5 Flash judge) | [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official evaluation repository](https://github.com/surge-ai/chartography), [Alibaba Qwen3.7 Plus model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus) | 2026-11-05T04:21+08:00 |
| humanitys-last-exam | 已收录 | 36 (metric=accuracy; dataset=May 2025 revision; 2,158 text-only questions; variant=Reasoning version; pass@1; no tools) | [Artificial Analysis Qwen3.7 Plus comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:28+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.7 Plus model profile](https://artificialanalysis.ai/models/qwen3-7-plus), [Artificial Analysis v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Qwen3.7 Plus comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1) | 2026-11-05T04:21+08:00 |
| gdpval-aa-v2.1 | 已收录 | 768 (metric=Elo rating; version=2.1; dataset=220 tasks; 44 occupations; 9 industries; variant=Reasoning version; harness=Artificial Analysis Stirrup; shell access and web browsing) | [Artificial Analysis Qwen3.7 Plus comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1), [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:28+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T04:21+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206)

研究备注：
- 官方榜单当前只显示 21/28 个型号，未显示 Qwen3.7 Plus；不能据部分列表缺席断定没有成绩。

尚未解决的问题：
- 官方榜单显示 21/28 个型号，完整榜单中是否有该型号仍待核实。

最近核验时间：2026-11-05T04:21+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Alibaba 文章提到 SWE-bench Pro 系列，但未能从可读原文确认该型号的准确分数及 V2 版本；不将泛称 Pro 结果映射到 V2。

尚未解决的问题：
- 精确版本和分数仍需从原始结果表核实。

最近核验时间：2026-11-05T04:21+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206)

研究备注：
- Alibaba 文章只提及 Terminal-Bench 2.0，不能映射为 v4；官方 v4 动态榜单当前无法读取完整结果行。

尚未解决的问题：
- 未能确认 v4 完整榜单中是否存在该型号。

最近核验时间：2026-11-05T04:21+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Alibaba Qwen3.7 Plus official announcement](https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206)

研究备注：
- 官方 0.1 结果表列出的型号中没有 Qwen3.7 Plus；未从旧版或相近型号迁移成绩。

最近核验时间：2026-11-05T04:21+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Alibaba Qwen3.7 Plus model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus)

研究备注：
- 模型支持函数调用与工作流代理；Zapier 1.0.6 榜单显示前 10 项并折叠 119 项，当前无法确认完整名单。

尚未解决的问题：
- 完整榜单中是否含该型号待核实。

最近核验时间：2026-11-05T04:21+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 official site](https://osworld-v2.xlang.ai/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [Alibaba Qwen3.7 Plus model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus)

研究备注：
- 官方资料确认该型号支持图像输入、函数调用及 GUI 交互；OSWorld 官方结果表当前未提供可核对的完整型号行。

尚未解决的问题：
- 动态结果表未能确认该型号在 v2.1 下的分数。

最近核验时间：2026-11-05T04:21+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 15.8
- metric: accuracy (mean; Pass@1)
- dataset: 100-task Chartography set
- variant: Thinking on; 10 runs per task
- harness: Inspect AI; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official evaluation repository](https://github.com/surge-ai/chartography)
- [Alibaba Qwen3.7 Plus model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus)

研究备注：
- 榜单明确列出 Qwen 3.7 Plus (Thinking on) 15.8%。官方 README 将计分定义为 accuracy/mean (Pass@1)，并说明榜单配置为完整 100 项任务、每项 10 次运行、Gemini 3.5 Flash judge。榜单未注明语义版本或评测日期。

最近核验时间：2026-11-05T04:21+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 36
- metric: accuracy
- dataset: May 2025 revision; 2,158 text-only questions
- variant: Reasoning version; pass@1; no tools
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.7 Plus comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 比较页的精确模型行列出 HLE 36%；该旧评测使用 2025-05 修订版中 2,158 道文本题、无工具、pass@1 和 GPT-5.6 Luna medium 判分，属于原始 HLE 而非 HLE-Diamond。
- AA 型号页说明展示的是 Qwen3.7 Plus reasoning 版本；该条件已记入 variant。

最近核验时间：2026-11-05T04:28+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.7 Plus model profile](https://artificialanalysis.ai/models/qwen3-7-plus)
- [Artificial Analysis v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Qwen3.7 Plus comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1)

研究备注：
- 精确型号资料页的 Index v5.0.1 显示 N/A；旧比较页的 25 分属于 v4.3.2，不映射到本地 v5 定义。

最近核验时间：2026-11-05T04:21+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 768
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks; 44 occupations; 9 industries
- variant: Reasoning version
- harness: Artificial Analysis Stirrup; shell access and web browsing
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Qwen3.7 Plus comparison](https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1)
- [GDPval-AA v2.1 official evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 精确型号行列出 GDPval-AA v2.1 768 Elo；评测使用 220 项任务、44 种职业和 9 个行业，经 Stirrup 提供 shell 与网页浏览。来源未注明模型专属推理档位。
- AA 型号页说明展示的是 Qwen3.7 Plus reasoning 版本；该条件已记入 variant。

最近核验时间：2026-11-05T04:28+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前公开 v2.2 排行榜展示 19 个最新/前沿型号，其中没有 Qwen3.7 Plus；不从 Qwen 其他版本迁移成绩。

最近核验时间：2026-11-05T04:21+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.7 Plus model profile",
          "url": "https://artificialanalysis.ai/models/qwen3-7-plus"
        },
        {
          "label": "Artificial Analysis v5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Qwen3.7 Plus comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1"
        }
      ],
      "notes": [
        "精确型号资料页的 Index v5.0.1 显示 N/A；旧比较页的 25 分属于 v4.3.2，不映射到本地 v5 定义。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Alibaba Qwen3.7 Plus model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus"
        }
      ],
      "notes": [
        "模型支持函数调用与工作流代理；Zapier 1.0.6 榜单显示前 10 项并折叠 119 项，当前无法确认完整名单。"
      ],
      "status": "待核实",
      "unresolved": [
        "完整榜单中是否含该型号待核实。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "Alibaba Qwen3.7 Plus model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus"
        }
      ],
      "notes": [
        "榜单明确列出 Qwen 3.7 Plus (Thinking on) 15.8%。官方 README 将计分定义为 accuracy/mean (Pass@1)，并说明榜单配置为完整 100 项任务、每项 10 次运行、Gemini 3.5 Flash judge。榜单未注明语义版本或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Alibaba Qwen3.7 Plus official announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206"
        }
      ],
      "notes": [
        "官方榜单当前只显示 21/28 个型号，未显示 Qwen3.7 Plus；不能据部分列表缺席断定没有成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "官方榜单显示 21/28 个型号，完整榜单中是否有该型号仍待核实。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:28+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.7 Plus comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1"
        },
        {
          "label": "GDPval-AA v2.1 official evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 精确型号行列出 GDPval-AA v2.1 768 Elo；评测使用 220 项任务、44 种职业和 9 个行业，经 Stirrup 提供 shell 与网页浏览。来源未注明模型专属推理档位。",
        "AA 型号页说明展示的是 Qwen3.7 Plus reasoning 版本；该条件已记入 variant。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:28+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.7 Plus comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-7-plus-vs-glm-5-1"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 比较页的精确模型行列出 HLE 36%；该旧评测使用 2025-05 修订版中 2,158 道文本题、无工具、pass@1 和 GPT-5.6 Luna medium 判分，属于原始 HLE 而非 HLE-Diamond。",
        "AA 型号页说明展示的是 Qwen3.7 Plus reasoning 版本；该条件已记入 variant。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Alibaba Qwen3.7 Plus model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/qwen3-7-plus"
        }
      ],
      "notes": [
        "官方资料确认该型号支持图像输入、函数调用及 GUI 交互；OSWorld 官方结果表当前未提供可核对的完整型号行。"
      ],
      "status": "待核实",
      "unresolved": [
        "动态结果表未能确认该型号在 v2.1 下的分数。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Alibaba Qwen3.7 Plus official announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Alibaba 文章提到 SWE-bench Pro 系列，但未能从可读原文确认该型号的准确分数及 V2 版本；不将泛称 Pro 结果映射到 V2。"
      ],
      "status": "待核实",
      "unresolved": [
        "精确版本和分数仍需从原始结果表核实。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Alibaba Qwen3.7 Plus official announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206"
        }
      ],
      "notes": [
        "官方 0.1 结果表列出的型号中没有 Qwen3.7 Plus；未从旧版或相近型号迁移成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Alibaba Qwen3.7 Plus official announcement",
          "url": "https://www.alibabacloud.com/blog/qwen3-7-plus-multimodal-agent-intelligence_603206"
        }
      ],
      "notes": [
        "Alibaba 文章只提及 Terminal-Bench 2.0，不能映射为 v4；官方 v4 动态榜单当前无法读取完整结果行。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能确认 v4 完整榜单中是否存在该型号。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:21+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前公开 v2.2 排行榜展示 19 个最新/前沿型号，其中没有 Qwen3.7 Plus；不从 Qwen 其他版本迁移成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:28+08:00",
  "model_id": "alibaba/qwen3.7-plus",
  "model_notes": [
    "精确型号文档对应快照 qwen3.7-plus-2026-05-26。模型 TOML 的 release_date 为 2026-06-02；Alibaba Cloud 官方生命周期页列出 Global 日期 2026-06-01，官方介绍文章日期为 2026-06-03。日期定义存在一天差异，本轮按当前仓库 release_date 维持队列顺序，并记录来源差异。",
    "新增 Chartography 15.8%、AA 原始 HLE 36% 和 GDPval-AA v2.1 768 Elo 三条成绩；未将旧 AA Index v4.3.2 的综合分数映射为 V5。",
    "后续核对 AA 精确型号页确认其比较数据对应 reasoning 版本，已将该版本条件补入 HLE 和 GDPval-AA 成绩的 variant 字段。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
