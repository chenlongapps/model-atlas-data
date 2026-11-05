# Qwen3.8 2.4T A95B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-2.4t-a95b
- 模型名称：Qwen3.8 2.4T A95B
- 发布日期：2026-08-12
- 最近检查时间：2026-11-04T18:19+08:00
- 整体处理状态：待复核
- 新增成绩数量：2
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 本文件对应开放权重 Qwen3.8 2.4T A95B（text-only）。Qwen3.8 Max 是基于该权重的独立云端版本，具备额外的视觉输入等能力；Max 的成绩不能归属于 A95B。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE 1.1 leaderboard](https://www.deepswe.dev/), [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-11-04T18:19+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-11-04T18:19+08:00 |
| terminal-bench-v4 | 已收录 | 11 (metric=task resolution rate; version=4.0.0; dataset=all 66 tasks; variant=pass@1 averaged over three repeats per task; harness=mini-swe-agent) | [Artificial Analysis exact-model comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash), [Artificial Analysis Terminal-Bench 4.0 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench 4.0 official release and resolution-rate definition](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T18:19+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Artificial Analysis Terminal-Bench-Science 0.1 evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-11-04T18:19+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks), [Artificial Analysis exact-model comparison (AutomationBench-AA)](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash), [AutomationBench public repository and dataset distinction](https://github.com/zapier/AutomationBench) | 2026-11-04T18:19+08:00 |
| osworld-v2.1 | 不适用 | — | [OSWorld V2 official benchmark page](https://osworld-v2.xlang.ai/), [OSWorld V2 official repository and v2.1 release](https://github.com/xlang-ai/OSWorld-V2), [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-11-04T18:19+08:00 |
| chartography | 不适用 | — | [Surge Chartography benchmark and leaderboard](https://surgehq.ai/benchmarks/chartography), [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-11-04T18:19+08:00 |
| humanitys-last-exam | 已收录 | 42 (metric=accuracy; version=unspecified; dataset=2,158 text-only questions from the original 2,500-question HLE set; variant=single answer; text-only subset) | [Artificial Analysis exact-model comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash), [Artificial Analysis HLE evaluation method](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T18:19+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Qwen3.8 2.4T A95B profile](https://artificialanalysis.ai/models/qwen3-8-2-4t-a95b), [Artificial Analysis Qwen3.8 A95B vs Max comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-qwen3-8-max-0803) | 2026-11-04T18:19+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis comparison showing 1597 Elo](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash), [Artificial Analysis comparison showing 1607 Elo](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-qwen3-5-122b-a10b), [Artificial Analysis comparison showing 1610 Elo](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-qwen3-8-2-4t-a95b), [Artificial Analysis GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T18:19+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard updated October 30, 2026](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T18:19+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE 1.1 leaderboard](https://www.deepswe.dev/)
- [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

研究备注：
- 已检查 DeepSWE 1.1 当前榜单及目标模型卡；榜单中出现的是 Qwen3.8 Max [xhigh]，不是开放权重 Qwen3.8 2.4T A95B。Max 的结果不移用。

最近核验时间：2026-11-04T18:19+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

研究备注：
- Scale 官方 V2 榜单未列出 Qwen3.8 2.4T A95B。模型卡中的 67.7 属于 Qwen3.8-Max，且没有证据证明对应仓库所定义的 V2 版本；不移用。

最近核验时间：2026-11-04T18:19+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 11
- metric: task resolution rate
- version: 4.0.0
- dataset: all 66 tasks
- variant: pass@1 averaged over three repeats per task
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis exact-model comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash)
- [Artificial Analysis Terminal-Bench 4.0 method](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Terminal-Bench 4.0 official release and resolution-rate definition](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Artificial Analysis 的精确模型比较页列出 A95B 11%。其 Terminal-Bench 4.0 方法页说明采用全部 66 项任务、mini-swe-agent、每项任务三次 pass@1 平均；测试 effort 与评测日期未公布。

最近核验时间：2026-11-04T18:19+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Terminal-Bench-Science 0.1 evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

研究备注：
- 已检查 Artificial Analysis 的 0.1 评测页；未找到 A95B 可读成绩。搜索到的 Qwen 相关旧条目为不同的 Qwen3.8 Max，未映射到 A95B。

最近核验时间：2026-11-04T18:19+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks)
- [Artificial Analysis exact-model comparison (AutomationBench-AA)](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash)
- [AutomationBench public repository and dataset distinction](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 当前榜单确认版本为 1.0.6，但榜单前十名后折叠了 119 条，无法从可读页面确认其中是否有 A95B，因此保留待核实。Artificial Analysis 的 57% 是 AutomationBench-AA，不能当作 Zapier 的 v1.0.6 私有榜单成绩。

尚未解决的问题：
- 需确认 Zapier 折叠的 119 条榜单记录中是否包含 Qwen3.8 2.4T A95B。

最近核验时间：2026-11-04T18:19+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [OSWorld V2 official benchmark page](https://osworld-v2.xlang.ai/)
- [OSWorld V2 official repository and v2.1 release](https://github.com/xlang-ai/OSWorld-V2)
- [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

研究备注：
- A95B 官方模型卡标为 text-only。OSWorld 是计算机使用任务，需要从桌面画面理解并操作界面，因此此纯文本模型不适用；没有记作 0。

最近核验时间：2026-11-04T18:19+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Surge Chartography benchmark and leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Qwen3.8-2.4T-A95B model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

研究备注：
- Chartography 官方定义为专业图表视觉理解评测；A95B 官方模型卡为 text-only，不支持图像输入，因此不适用。榜单上的 Qwen3.8 Max 是另一个支持视觉的云端版本。

最近核验时间：2026-11-04T18:19+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 42
- metric: accuracy
- version: unspecified
- dataset: 2,158 text-only questions from the original 2,500-question HLE set
- variant: single answer; text-only subset
- source: [https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis exact-model comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash)
- [Artificial Analysis HLE evaluation method](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis 精确模型对比页列出原始 Humanity's Last Exam 42%。其方法页说明采用原始 HLE 中 2,158 道文本题，pass@1，每题输出单个答案。评测日期、推理 effort 和 harness 未公布；不与 HLE-Diamond 混用。

最近核验时间：2026-11-04T18:19+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Qwen3.8 2.4T A95B profile](https://artificialanalysis.ai/models/qwen3-8-2-4t-a95b)
- [Artificial Analysis Qwen3.8 A95B vs Max comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-qwen3-8-max-0803)

研究备注：
- 当前 A95B 模型页的 Intelligence Index 显示 N/A，并将当前指数标为 v5.0.1。其他比较页的历史 Index 数值未证明属于当前 V5，不录入。

最近核验时间：2026-11-04T18:19+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis comparison showing 1597 Elo](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash)
- [Artificial Analysis comparison showing 1607 Elo](https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-qwen3-5-122b-a10b)
- [Artificial Analysis comparison showing 1610 Elo](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-qwen3-8-2-4t-a95b)
- [Artificial Analysis GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 三个精确 A95B 比较页分别显示 GDPval-AA v2.1 为 1597、1607、1610 Elo。未见可核对的评测时间戳或配置差异，存在冲突，暂不选择其一写入。官方方法说明评测使用 220 项任务、Stirrup shell 与网页浏览。

尚未解决的问题：
- 需取得能解释 1597、1607、1610 Elo 差异的评测时间戳或固定评测版本，再决定是否可收录。

最近核验时间：2026-11-04T18:19+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard updated October 30, 2026](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals 官方 2026-10-30 v2.2 榜单列出 Qwen 3.8 Max 0902（59.05%），没有列出准确的 Qwen3.8 2.4T A95B；不移用 Max 分数。

最近核验时间：2026-11-04T18:19+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Qwen3.8 2.4T A95B profile",
          "url": "https://artificialanalysis.ai/models/qwen3-8-2-4t-a95b"
        },
        {
          "label": "Artificial Analysis Qwen3.8 A95B vs Max comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-qwen3-8-max-0803"
        }
      ],
      "notes": [
        "当前 A95B 模型页的 Intelligence Index 显示 N/A，并将当前指数标为 v5.0.1。其他比较页的历史 Index 数值未证明属于当前 V5，不录入。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis exact-model comparison (AutomationBench-AA)",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash"
        },
        {
          "label": "AutomationBench public repository and dataset distinction",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Zapier 当前榜单确认版本为 1.0.6，但榜单前十名后折叠了 119 条，无法从可读页面确认其中是否有 A95B，因此保留待核实。Artificial Analysis 的 57% 是 AutomationBench-AA，不能当作 Zapier 的 v1.0.6 私有榜单成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 Zapier 折叠的 119 条榜单记录中是否包含 Qwen3.8 2.4T A95B。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography benchmark and leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Qwen3.8-2.4T-A95B model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        }
      ],
      "notes": [
        "Chartography 官方定义为专业图表视觉理解评测；A95B 官方模型卡为 text-only，不支持图像输入，因此不适用。榜单上的 Qwen3.8 Max 是另一个支持视觉的云端版本。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 1.1 leaderboard",
          "url": "https://www.deepswe.dev/"
        },
        {
          "label": "Qwen3.8-2.4T-A95B model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        }
      ],
      "notes": [
        "已检查 DeepSWE 1.1 当前榜单及目标模型卡；榜单中出现的是 Qwen3.8 Max [xhigh]，不是开放权重 Qwen3.8 2.4T A95B。Max 的结果不移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison showing 1597 Elo",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash"
        },
        {
          "label": "Artificial Analysis comparison showing 1607 Elo",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-qwen3-5-122b-a10b"
        },
        {
          "label": "Artificial Analysis comparison showing 1610 Elo",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-qwen3-8-2-4t-a95b"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "三个精确 A95B 比较页分别显示 GDPval-AA v2.1 为 1597、1607、1610 Elo。未见可核对的评测时间戳或配置差异，存在冲突，暂不选择其一写入。官方方法说明评测使用 220 项任务、Stirrup shell 与网页浏览。"
      ],
      "status": "冲突",
      "unresolved": [
        "需取得能解释 1597、1607、1610 Elo 差异的评测时间戳或固定评测版本，再决定是否可收录。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash"
        },
        {
          "label": "Artificial Analysis HLE evaluation method",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis 精确模型对比页列出原始 Humanity's Last Exam 42%。其方法页说明采用原始 HLE 中 2,158 道文本题，pass@1，每题输出单个答案。评测日期、推理 effort 和 harness 未公布；不与 HLE-Diamond 混用。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official benchmark page",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 official repository and v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Qwen3.8-2.4T-A95B model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        }
      ],
      "notes": [
        "A95B 官方模型卡标为 text-only。OSWorld 是计算机使用任务，需要从桌面画面理解并操作界面，因此此纯文本模型不适用；没有记作 0。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Qwen3.8-2.4T-A95B model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        }
      ],
      "notes": [
        "Scale 官方 V2 榜单未列出 Qwen3.8 2.4T A95B。模型卡中的 67.7 属于 Qwen3.8-Max，且没有证据证明对应仓库所定义的 V2 版本；不移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Terminal-Bench-Science 0.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Qwen3.8-2.4T-A95B model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        }
      ],
      "notes": [
        "已检查 Artificial Analysis 的 0.1 评测页；未找到 A95B 可读成绩。搜索到的 Qwen 相关旧条目为不同的 Qwen3.8 Max，未映射到 A95B。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-2-4t-a95b-vs-step-3-7-flash"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 method",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Terminal-Bench 4.0 official release and resolution-rate definition",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Artificial Analysis 的精确模型比较页列出 A95B 11%。其 Terminal-Bench 4.0 方法页说明采用全部 66 项任务、mini-swe-agent、每项任务三次 pass@1 平均；测试 effort 与评测日期未公布。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T18:19+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard updated October 30, 2026",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals 官方 2026-10-30 v2.2 榜单列出 Qwen 3.8 Max 0902（59.05%），没有列出准确的 Qwen3.8 2.4T A95B；不移用 Max 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T18:19+08:00",
  "model_id": "alibaba/qwen3.8-2.4t-a95b",
  "model_notes": [
    "本文件对应开放权重 Qwen3.8 2.4T A95B（text-only）。Qwen3.8 Max 是基于该权重的独立云端版本，具备额外的视觉输入等能力；Max 的成绩不能归属于 A95B。"
  ],
  "new_records": 2,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
