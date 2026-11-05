# DeepSeek V4 Flash 0731 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：deepseek/deepseek-v4-flash-0731
- 模型名称：DeepSeek V4 Flash 0731
- 发布日期：2026-07-31
- 最近检查时间：2026-11-04T21:19+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：3

## 模型身份与范围说明

- 身份依据：DeepSeek 官方更新与 0731 模型卡确认该版本；DeepSWE 榜单的 deepseek-v4-flash[max] 行未写 0731 后缀，按官方别名和 2026-08-06 收录时间对应到 2026-07-31 发布的 0731 版本。
- 仅新增版本和测试条件可核实且精确匹配的 DeepSWE v1.1、Terminal-Bench 4.0、Terminal-Bench-Science 0.1.0 三条记录；已有其他条件的分数保留。
- Artificial Analysis 的 HLE 和 GDPval-AA 来源存在数值冲突，均不写入分数；AutomationBench 结果版本和指标映射待核实。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 已收录 | 54.4 (metric=resolve rate; variant=max effort; harness=DeepSeek Harness minimal mode); 53% ±4% (metric=pass@1; version=1.1; dataset=113 tasks; effort=max; harness=Mini-SWE-agent) | [DeepSWE 官方排行榜](https://deepswe.datacurve.ai/), [DeepSeek 2026-07-31 官方发布记录](https://api-docs.deepseek.com/updates/) | 2026-11-04T21:19+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T21:19+08:00 |
| terminal-bench-v4 | 已收录 | 82.7 (metric=pass@1; version=2.1; variant=max); 18.69 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=average@3; per-run pass@1; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 排行榜](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T21:19+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 4.29 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=single run; pass@1; retry provider/infra errors; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench-Science 排行榜](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T21:19+08:00 |
| automationbench-v1.0.6 | 待核实 | 25.1 (metric=success rate; dataset=public; variant=max effort) | [DeepSeek 官方 2026-07-31 评测更新](https://api-docs.deepseek.com/updates/), [Zapier AutomationBench 官方页面](https://zapier.com/benchmarks), [AutomationBench v1.0.6 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md) | 2026-11-04T21:19+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2), [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/) | 2026-11-04T21:19+08:00 |
| chartography | 不适用 | — | [DeepSeek V4 Flash 0731 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731), [Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T21:19+08:00 |
| humanitys-last-exam | 冲突 | — | [Artificial Analysis 2026-07-31 评测文章](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash), [Artificial Analysis 模型对比页](https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-vs-deepseek-v4-flash), [Humanity’s Last Exam 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T21:19+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis DeepSeek V4 Flash 型号页](https://artificialanalysis.ai/models/deepseek-v4-flash/), [Artificial Analysis 2026-07-31 评测文章](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash) | 2026-11-04T21:19+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [Artificial Analysis GDPval-AA 官方排行榜](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis 模型对比页](https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-vs-deepseek-v4-flash) | 2026-11-04T21:19+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI Vals Index 2.2 官方页](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T21:19+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 54.4
- metric: resolve rate
- variant: max effort
- harness: DeepSeek Harness minimal mode
- source: [https://api-docs.deepseek.com/updates/](https://api-docs.deepseek.com/updates/)
- date: 2026-07-31
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 53% ±4%
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- effort: max
- harness: Mini-SWE-agent
- source: [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [DeepSWE 官方排行榜](https://deepswe.datacurve.ai/)
- [DeepSeek 2026-07-31 官方发布记录](https://api-docs.deepseek.com/updates/)

研究备注：
- 官方榜单记录 deepseek-v4-flash[max] 为 53% ±4%，v1.1、113 tasks、Mini-SWE-agent、pass@1；以原始字符串保留公布的误差范围。
- 榜单行未写 0731 后缀；DeepSeek 官方 2026-07-31 更新将 deepseek-v4-flash 标为该日发布型号，且榜单在 2026-08-06 加入该项，故按官方别名与时间线对应到 0731。
- TOML 中原有 54.4 resolve rate 是 DeepSeek Harness minimal mode，配置及版本不同，保留为单独原始成绩。

最近核验时间：2026-11-04T21:19+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 在 V2 官方榜单中未找到 DeepSeek V4 Flash 0731 的准确型号记录；未将其他版本或子集成绩移用。

最近核验时间：2026-11-04T21:19+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 82.7
- metric: pass@1
- version: 2.1
- variant: max
- source: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 18.69
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: average@3; per-run pass@1
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 排行榜](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- 精确型号行得分 18.69%；记录版本 4.0.0、66 tasks、Mini-SWE-agent、average@3（每次运行 pass@1）。TOML 中原有 82.7 属于 Terminal-Bench 2.1，单独保留。

最近核验时间：2026-11-04T21:19+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 4.29
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: single run; pass@1; retry provider/infra errors
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Terminal-Bench-Science 排行榜](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- 精确型号行得分 4.29%；记录上游版本 0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1，并保留来源说明的 provider/infra 错误重试条件。未公布的推理档位和评测日期省略。

最近核验时间：2026-11-04T21:19+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 25.1
- metric: success rate
- dataset: public
- variant: max effort
- source: [https://api-docs.deepseek.com/updates/](https://api-docs.deepseek.com/updates/)
- date: 2026-07-31
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [DeepSeek 官方 2026-07-31 评测更新](https://api-docs.deepseek.com/updates/)
- [Zapier AutomationBench 官方页面](https://zapier.com/benchmarks)
- [AutomationBench v1.0.6 官方变更记录](https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md)

研究备注：
- 模型 TOML 已有 25.1 public 结果，原文指标为 success rate；本地 v1.0.6 定义要求 task_completed_correctly，且官方材料未确认该模型结果使用 v1.0.6 测试集，因此保留原始行但不计入该定义覆盖率。
- 现有 date=2026-07-31 对应 DeepSeek 更新发布日期；尚无证据证明它是评测日期，未将其当作评测时间使用。

尚未解决的问题：
- 需确认 25.1 结果的 AutomationBench 版本及其与 task_completed_correctly 的指标映射；也需确认现有 date 是否代表来源公布的评测日期。

最近核验时间：2026-11-04T21:19+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld V2 官方仓库](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld V2 官方项目页](https://osworld-v2.xlang.ai/)

研究备注：
- 在所查官方资料中未找到 DeepSeek V4 Flash 0731 的 OSWorld V2.1 结果。该模型支持工具调用，不能仅凭文本输入模态判为不适用。

最近核验时间：2026-11-04T21:19+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [DeepSeek V4 Flash 0731 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)
- [Chartography 官方榜单](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 0731 官方模型卡将该模型标为 text-generation、text-only；Chartography 要求视觉图表理解。榜单中的 DeepSeek V4 Flash Vision (experimental) 是不同的视觉模型，不映射到本模型。

最近核验时间：2026-11-04T21:19+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis 2026-07-31 评测文章](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash)
- [Artificial Analysis 模型对比页](https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-vs-deepseek-v4-flash)
- [Humanity’s Last Exam 官方评测页](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Artificial Analysis 文章报告该模型 HLE 37%，其模型对比页对相同型号 Max 显示 39%；当前评测页未提供可解释该差异的记录。未选择其中一个分数写入 TOML。
- DeepSeek 的 Agents’ Last Exam 25.2 是另一项评测，不等同于 Humanity’s Last Exam。

尚未解决的问题：
- Artificial Analysis 来源对 HLE 结果的 37% 与 39% 不一致，尚未查明是否由评测修订或条件差异造成。

最近核验时间：2026-11-04T21:19+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis DeepSeek V4 Flash 型号页](https://artificialanalysis.ai/models/deepseek-v4-flash/)
- [Artificial Analysis 2026-07-31 评测文章](https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash)

研究备注：
- 当前型号页的 Intelligence Index V5.0 显示 N/A；发布文章中的 50 分属于 V4.1，不移作 V5.0 成绩。

最近核验时间：2026-11-04T21:19+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [Artificial Analysis GDPval-AA 官方排行榜](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis 模型对比页](https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-vs-deepseek-v4-flash)

研究备注：
- 同一准确型号在 GDPval-AA v2.1 的当前排行榜显示 1441 Elo，对比页显示 1433 Elo。未猜测是否为更新或配置差异，也未写入任一分数。

尚未解决的问题：
- Artificial Analysis 官方来源的 Elo 数值 1441 与 1433 冲突，待确认有效记录。

最近核验时间：2026-11-04T21:19+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Vals Index 2.2 官方页](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 官方 2.2 页面未找到 DeepSeek V4 Flash 0731 的准确型号结果；其他 DeepSeek 型号及旧版本 Vals Index 分数不适用。

最近核验时间：2026-11-04T21:19+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis DeepSeek V4 Flash 型号页",
          "url": "https://artificialanalysis.ai/models/deepseek-v4-flash/"
        },
        {
          "label": "Artificial Analysis 2026-07-31 评测文章",
          "url": "https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash"
        }
      ],
      "notes": [
        "当前型号页的 Intelligence Index V5.0 显示 N/A；发布文章中的 50 分属于 V4.1，不移作 V5.0 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek 官方 2026-07-31 评测更新",
          "url": "https://api-docs.deepseek.com/updates/"
        },
        {
          "label": "Zapier AutomationBench 官方页面",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench v1.0.6 官方变更记录",
          "url": "https://github.com/zapier/AutomationBench/blob/main/CHANGELOG.md"
        }
      ],
      "notes": [
        "模型 TOML 已有 25.1 public 结果，原文指标为 success rate；本地 v1.0.6 定义要求 task_completed_correctly，且官方材料未确认该模型结果使用 v1.0.6 测试集，因此保留原始行但不计入该定义覆盖率。",
        "现有 date=2026-07-31 对应 DeepSeek 更新发布日期；尚无证据证明它是评测日期，未将其当作评测时间使用。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 25.1 结果的 AutomationBench 版本及其与 task_completed_correctly 的指标映射；也需确认现有 date 是否代表来源公布的评测日期。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "DeepSeek V4 Flash 0731 官方模型卡",
          "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731"
        },
        {
          "label": "Chartography 官方榜单",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "0731 官方模型卡将该模型标为 text-generation、text-only；Chartography 要求视觉图表理解。榜单中的 DeepSeek V4 Flash Vision (experimental) 是不同的视觉模型，不映射到本模型。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSeek 2026-07-31 官方发布记录",
          "url": "https://api-docs.deepseek.com/updates/"
        }
      ],
      "notes": [
        "官方榜单记录 deepseek-v4-flash[max] 为 53% ±4%，v1.1、113 tasks、Mini-SWE-agent、pass@1；以原始字符串保留公布的误差范围。",
        "榜单行未写 0731 后缀；DeepSeek 官方 2026-07-31 更新将 deepseek-v4-flash 标为该日发布型号，且榜单在 2026-08-06 加入该项，故按官方别名与时间线对应到 0731。",
        "TOML 中原有 54.4 resolve rate 是 DeepSeek Harness minimal mode，配置及版本不同，保留为单独原始成绩。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA 官方排行榜",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis 模型对比页",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-vs-deepseek-v4-flash"
        }
      ],
      "notes": [
        "同一准确型号在 GDPval-AA v2.1 的当前排行榜显示 1441 Elo，对比页显示 1433 Elo。未猜测是否为更新或配置差异，也未写入任一分数。"
      ],
      "status": "冲突",
      "unresolved": [
        "Artificial Analysis 官方来源的 Elo 数值 1441 与 1433 冲突，待确认有效记录。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis 2026-07-31 评测文章",
          "url": "https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash"
        },
        {
          "label": "Artificial Analysis 模型对比页",
          "url": "https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-vs-deepseek-v4-flash"
        },
        {
          "label": "Humanity’s Last Exam 官方评测页",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Artificial Analysis 文章报告该模型 HLE 37%，其模型对比页对相同型号 Max 显示 39%；当前评测页未提供可解释该差异的记录。未选择其中一个分数写入 TOML。",
        "DeepSeek 的 Agents’ Last Exam 25.2 是另一项评测，不等同于 Humanity’s Last Exam。"
      ],
      "status": "冲突",
      "unresolved": [
        "Artificial Analysis 来源对 HLE 结果的 37% 与 39% 不一致，尚未查明是否由评测修订或条件差异造成。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 官方仓库",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld V2 官方项目页",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "在所查官方资料中未找到 DeepSeek V4 Flash 0731 的 OSWorld V2.1 结果。该模型支持工具调用，不能仅凭文本输入模态判为不适用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "在 V2 官方榜单中未找到 DeepSeek V4 Flash 0731 的准确型号记录；未将其他版本或子集成绩移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench-Science 排行榜",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "精确型号行得分 4.29%；记录上游版本 0.1.0、70 tasks、Mini-SWE-agent、单次 pass@1，并保留来源说明的 provider/infra 错误重试条件。未公布的推理档位和评测日期省略。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 排行榜",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "精确型号行得分 18.69%；记录版本 4.0.0、66 tasks、Mini-SWE-agent、average@3（每次运行 pass@1）。TOML 中原有 82.7 属于 Terminal-Bench 2.1，单独保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T21:19+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index 2.2 官方页",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "官方 2.2 页面未找到 DeepSeek V4 Flash 0731 的准确型号结果；其他 DeepSeek 型号及旧版本 Vals Index 分数不适用。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T21:19+08:00",
  "model_id": "deepseek/deepseek-v4-flash-0731",
  "model_notes": [
    "身份依据：DeepSeek 官方更新与 0731 模型卡确认该版本；DeepSWE 榜单的 deepseek-v4-flash[max] 行未写 0731 后缀，按官方别名和 2026-08-06 收录时间对应到 2026-07-31 发布的 0731 版本。",
    "仅新增版本和测试条件可核实且精确匹配的 DeepSWE v1.1、Terminal-Bench 4.0、Terminal-Bench-Science 0.1.0 三条记录；已有其他条件的分数保留。",
    "Artificial Analysis 的 HLE 和 GDPval-AA 来源存在数值冲突，均不写入分数；AutomationBench 结果版本和指标映射待核实。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
