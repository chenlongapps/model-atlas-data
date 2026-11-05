# Nex-N2-Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nex-agi/nex-n2-pro
- 模型名称：Nex-N2-Pro
- 发布日期：2026-06-02
- 最近检查时间：2026-11-05T04:34+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 本地文件无既有 Benchmark 成绩。本轮新增 AA 原始 HLE 34%（reasoning 版本，text-only HLE）；相邻版本 DeepSWE / SWE-Bench Pro / Terminal-Bench 分数未误映射为目标版本。
- AA 当前 GDPval-AA v2.1 榜单与比较页分别列 1109 和 1102 Elo，条件或重算原因未明；记录冲突并暂不写入成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/), [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/), [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro), [DeepSWE v1.1 release notes](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T04:34+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale SWE-bench Pro V2 announcement](https://labs.scale.com/blog/swe-bench-pro-v2), [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/) | 2026-11-05T04:34+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/) | 2026-11-05T04:34+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/) | 2026-11-05T04:34+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks), [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro), [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/) | 2026-11-05T04:34+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 official site](https://osworld-v2.xlang.ai/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro) | 2026-11-05T04:34+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official evaluation repository](https://github.com/surge-ai/chartography), [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro) | 2026-11-05T04:34+08:00 |
| humanitys-last-exam | 已收录 | 34 (metric=accuracy; dataset=May 2025 revision; 2,158 text-only questions; variant=Reasoning version; pass@1; no tools) | [Artificial Analysis Nex-N2-Pro comparison](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5), [Artificial Analysis Nex-N2-Pro profile](https://artificialanalysis.ai/models/nex-n2-pro), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:34+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Nex-N2-Pro profile](https://artificialanalysis.ai/models/nex-n2-pro), [Artificial Analysis Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Nex-N2-Pro comparison](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5) | 2026-11-05T04:34+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis current GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Nex-N2-Pro comparison](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5), [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:34+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro) | 2026-11-05T04:34+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)
- [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/)
- [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro)
- [DeepSWE v1.1 release notes](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Nex 官方表列泛称 DeepSWE 33.6；模型卡最近更新 2026-06-11，早于 v1.1 于 2026-06-14 发布。官方 v1.1 榜单当前只显示 21/28 个型号，未能确认精确型号的 v1.1 结果。

尚未解决的问题：
- 33.6 所属 DeepSWE 版本及其 metric 未注明；官方 v1.1 榜单不完整，不能映射为目标 v1.1。

最近核验时间：2026-11-05T04:34+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale SWE-bench Pro V2 announcement](https://labs.scale.com/blog/swe-bench-pro-v2)
- [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/)

研究备注：
- Nex 官方表列 SWE-Bench Pro 58.8，但未注明 V2；V2 于 2026-09-22 才发布，当前 Scale V2 榜单未列 Nex-N2-Pro。旧泛称结果不映射到 642-task V2。

最近核验时间：2026-11-05T04:34+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4 official leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/)

研究备注：
- Nex 官方结果为 Terminal-Bench 2.1: 75.3，并非 4.0；官方 v4 页面当前未呈现可核验结果行。

尚未解决的问题：
- TB4 动态榜单不可读完整结果，尚不能确认 Nex-N2-Pro 是否有目标成绩。

最近核验时间：2026-11-05T04:34+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 official results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/)

研究备注：
- 官方 Science 0.1 结果页列出的 9 个型号中没有 Nex-N2-Pro；Nex 官方表未列该项目。

最近核验时间：2026-11-05T04:34+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench official leaderboard](https://zapier.com/benchmarks)
- [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro)
- [Nex-N2 official benchmark and methodology page](https://nex-agi.com/n2/)

研究备注：
- Nex-N2-Pro 支持图像输入、文本输出和函数调用，具备代理适用性；Zapier 1.0.6 榜单显示前 10 项并折叠另外 119 项，完整名单不可核验。

尚未解决的问题：
- 折叠榜单中是否有精确型号待核实。

最近核验时间：2026-11-05T04:34+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 official site](https://osworld-v2.xlang.ai/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro)

研究备注：
- 模型支持图像理解与函数调用；OSWorld 官方结果页为当前不可解析的动态表格，未能核实该型号成绩或 GUI 动作接入配置。

尚未解决的问题：
- 缺少可核对的 v2.1 精确型号行及其动作配置。

最近核验时间：2026-11-05T04:34+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official evaluation repository](https://github.com/surge-ai/chartography)
- [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro)

研究备注：
- 当前公开 Chartography 排行榜未列 Nex-N2-Pro；其图像输入与文本回答能力适用于该任务，但未找到精确型号公开分数。

最近核验时间：2026-11-05T04:34+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 34
- metric: accuracy
- dataset: May 2025 revision; 2,158 text-only questions
- variant: Reasoning version; pass@1; no tools
- source: [https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Nex-N2-Pro comparison](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5)
- [Artificial Analysis Nex-N2-Pro profile](https://artificialanalysis.ai/models/nex-n2-pro)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 比较页精确型号行列出 HLE 34%；该评测使用 2025 年 5 月修订版 2,158 道纯文本题，无工具、pass@1、GPT-5.6 Luna medium 判分。AA 型号页注明展示 reasoning 版本；该分数为原始 HLE，不是 HLE-Diamond。

最近核验时间：2026-11-05T04:34+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Nex-N2-Pro profile](https://artificialanalysis.ai/models/nex-n2-pro)
- [Artificial Analysis Index v5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Nex-N2-Pro comparison](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5)

研究备注：
- 当前精确型号页的 Index v5.0.1 显示 N/A；比较页的 28* 是旧版 v4.3.2 估算值，不能映射为 V5。

最近核验时间：2026-11-05T04:34+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis current GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Nex-N2-Pro comparison](https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5)
- [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前 GDPval-AA v2.1 榜单列 Nex-N2-Pro 1109 Elo（CI −19/+19）；AA 比较页仍列 1102 Elo。两页均为 AA v2.1，但未能确认差异是重算、更新还是其他条件；未在 TOML 写入任一分数。Nex 官方原始 GDPval 1585 不属于 GDPval-AA。

尚未解决的问题：
- 两个官方 AA 页面数值不一致，缺少可确认的评测修订/条件说明；待 AA 页面统一后再收录。

最近核验时间：2026-11-05T04:34+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Nex-N2-Pro official model card](https://huggingface.co/nex-agi/Nex-N2-Pro)

研究备注：
- 当前公开 v2.2 页展示 latest/top/frontier 子集，未列 Nex-N2-Pro；缺席不证明该型号从未被测试。

最近核验时间：2026-11-05T04:34+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Nex-N2-Pro profile",
          "url": "https://artificialanalysis.ai/models/nex-n2-pro"
        },
        {
          "label": "Artificial Analysis Index v5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Nex-N2-Pro comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5"
        }
      ],
      "notes": [
        "当前精确型号页的 Index v5.0.1 显示 N/A；比较页的 28* 是旧版 v4.3.2 估算值，不能映射为 V5。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench official leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Nex-N2-Pro official model card",
          "url": "https://huggingface.co/nex-agi/Nex-N2-Pro"
        },
        {
          "label": "Nex-N2 official benchmark and methodology page",
          "url": "https://nex-agi.com/n2/"
        }
      ],
      "notes": [
        "Nex-N2-Pro 支持图像输入、文本输出和函数调用，具备代理适用性；Zapier 1.0.6 榜单显示前 10 项并折叠另外 119 项，完整名单不可核验。"
      ],
      "status": "待核实",
      "unresolved": [
        "折叠榜单中是否有精确型号待核实。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T04:34+08:00",
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
          "label": "Nex-N2-Pro official model card",
          "url": "https://huggingface.co/nex-agi/Nex-N2-Pro"
        }
      ],
      "notes": [
        "当前公开 Chartography 排行榜未列 Nex-N2-Pro；其图像输入与文本回答能力适用于该任务，但未找到精确型号公开分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Nex-N2 official benchmark and methodology page",
          "url": "https://nex-agi.com/n2/"
        },
        {
          "label": "Nex-N2-Pro official model card",
          "url": "https://huggingface.co/nex-agi/Nex-N2-Pro"
        },
        {
          "label": "DeepSWE v1.1 release notes",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Nex 官方表列泛称 DeepSWE 33.6；模型卡最近更新 2026-06-11，早于 v1.1 于 2026-06-14 发布。官方 v1.1 榜单当前只显示 21/28 个型号，未能确认精确型号的 v1.1 结果。"
      ],
      "status": "待核实",
      "unresolved": [
        "33.6 所属 DeepSWE 版本及其 metric 未注明；官方 v1.1 榜单不完整，不能映射为目标 v1.1。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis current GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Nex-N2-Pro comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5"
        },
        {
          "label": "GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前 GDPval-AA v2.1 榜单列 Nex-N2-Pro 1109 Elo（CI −19/+19）；AA 比较页仍列 1102 Elo。两页均为 AA v2.1，但未能确认差异是重算、更新还是其他条件；未在 TOML 写入任一分数。Nex 官方原始 GDPval 1585 不属于 GDPval-AA。"
      ],
      "status": "冲突",
      "unresolved": [
        "两个官方 AA 页面数值不一致，缺少可确认的评测修订/条件说明；待 AA 页面统一后再收录。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Nex-N2-Pro comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/nex-n2-pro-vs-gpt-5-5"
        },
        {
          "label": "Artificial Analysis Nex-N2-Pro profile",
          "url": "https://artificialanalysis.ai/models/nex-n2-pro"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 比较页精确型号行列出 HLE 34%；该评测使用 2025 年 5 月修订版 2,158 道纯文本题，无工具、pass@1、GPT-5.6 Luna medium 判分。AA 型号页注明展示 reasoning 版本；该分数为原始 HLE，不是 HLE-Diamond。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:34+08:00",
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
          "label": "Nex-N2-Pro official model card",
          "url": "https://huggingface.co/nex-agi/Nex-N2-Pro"
        }
      ],
      "notes": [
        "模型支持图像理解与函数调用；OSWorld 官方结果页为当前不可解析的动态表格，未能核实该型号成绩或 GUI 动作接入配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "缺少可核对的 v2.1 精确型号行及其动作配置。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale SWE-bench Pro V2 announcement",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        },
        {
          "label": "Nex-N2 official benchmark and methodology page",
          "url": "https://nex-agi.com/n2/"
        }
      ],
      "notes": [
        "Nex 官方表列 SWE-Bench Pro 58.8，但未注明 V2；V2 于 2026-09-22 才发布，当前 Scale V2 榜单未列 Nex-N2-Pro。旧泛称结果不映射到 642-task V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 official results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Nex-N2 official benchmark and methodology page",
          "url": "https://nex-agi.com/n2/"
        }
      ],
      "notes": [
        "官方 Science 0.1 结果页列出的 9 个型号中没有 Nex-N2-Pro；Nex 官方表未列该项目。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench 4 official leaderboard",
          "url": "https://www.tbench.ai/?version=4.0&efforts=all"
        },
        {
          "label": "Nex-N2 official benchmark and methodology page",
          "url": "https://nex-agi.com/n2/"
        }
      ],
      "notes": [
        "Nex 官方结果为 Terminal-Bench 2.1: 75.3，并非 4.0；官方 v4 页面当前未呈现可核验结果行。"
      ],
      "status": "待核实",
      "unresolved": [
        "TB4 动态榜单不可读完整结果，尚不能确认 Nex-N2-Pro 是否有目标成绩。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:34+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Nex-N2-Pro official model card",
          "url": "https://huggingface.co/nex-agi/Nex-N2-Pro"
        }
      ],
      "notes": [
        "当前公开 v2.2 页展示 latest/top/frontier 子集，未列 Nex-N2-Pro；缺席不证明该型号从未被测试。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:34+08:00",
  "model_id": "nex-agi/nex-n2-pro",
  "model_notes": [
    "本地文件无既有 Benchmark 成绩。本轮新增 AA 原始 HLE 34%（reasoning 版本，text-only HLE）；相邻版本 DeepSWE / SWE-Bench Pro / Terminal-Bench 分数未误映射为目标版本。",
    "AA 当前 GDPval-AA v2.1 榜单与比较页分别列 1109 和 1102 Elo，条件或重算原因未明；记录冲突并暂不写入成绩。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
