# Laguna XS 2.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：poolside/laguna-xs-2.1
- 模型名称：Laguna XS 2.1
- 发布日期：2026-07-02
- 最近检查时间：2026-11-05T01:50+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：4
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 模型身份及发布日期依据 Poolside 2026-07-02 的 Laguna XS 2.1 发布资料；发布资料将其与 7 月 21 日发布的 Laguna S 2.1 明确区分。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 0.3 (metric=pass@1; version=1.1; dataset=113 tasks; variant=pass@1 averaged over 3 attempts per task) | [Poolside DeepSWE v1.1 comparison](https://poolside.ai/blog/introducing-laguna-s-2-1), [DeepSWE v1.1 official leaderboard and methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T01:50+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-xs-2-1), [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T01:50+08:00 |
| terminal-bench-v4 | 待核实 | 37.5 (metric=success rate; version=2.0; harness=Harbor) | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-xs-2-1) | 2026-11-05T01:50+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1) | 2026-11-05T01:50+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [AutomationBench leaderboard](https://zapier.com/benchmarks), [Poolside Laguna XS 2.1 model card](https://huggingface.co/poolside/Laguna-XS-2.1) | 2026-11-05T01:50+08:00 |
| osworld-v2.1 | 不适用 | — | [Poolside Laguna XS 2.1 model card](https://huggingface.co/poolside/Laguna-XS-2.1), [OSWorld V2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T01:50+08:00 |
| chartography | 不适用 | — | [Poolside Laguna XS 2.1 model card](https://huggingface.co/poolside/Laguna-XS-2.1), [Chartography official benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T01:50+08:00 |
| humanitys-last-exam | 未找到 | — | [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1), [Humanity’s Last Exam leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T01:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1) | 2026-11-05T01:50+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1), [GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T01:50+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index 2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1) | 2026-11-05T01:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 0.3
- metric: pass@1
- version: 1.1
- dataset: 113 tasks
- variant: pass@1 averaged over 3 attempts per task
- source: [https://poolside.ai/blog/introducing-laguna-s-2-1](https://poolside.ai/blog/introducing-laguna-s-2-1)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Poolside DeepSWE v1.1 comparison](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [DeepSWE v1.1 official leaderboard and methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Poolside 的 DeepSWE v1.1 表列出 Laguna XS 2.1 为 0.3%，pass@1，平均每题 3 次尝试。页面声明对照表采用供应商、基准作者或第三方来源中的最高报告值；未指出该行所用来源或 harness。分数作为已公开的厂商报告记录，未推断 harness。

尚未解决的问题：
- 需要找到该 Laguna XS 2.1 结果的具体原始运行、来源和 harness，确认其测试条件。

最近核验时间：2026-11-05T01:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-xs-2-1)
- [SWE-bench Pro V2 official leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- TOML 中已有 47.6 的 SWE-Bench Pro 记录未标版本，来自 2026-07-02 的 XS 2.1 发布材料；官方 Pro V2 于 2026-09 发布且任务集更新，不能将旧行映射到 V2。检查的 Pro V2 榜单未找到 XS 2.1。

最近核验时间：2026-11-05T01:50+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 37.5
- metric: success rate
- version: 2.0
- harness: Harbor
- source: [https://poolside.ai/blog/introducing-laguna-xs-2-1](https://poolside.ai/blog/introducing-laguna-xs-2-1)
- date: 2026-07-02
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-xs-2-1)

研究备注：
- 官方 v4 榜单当前页面未显示可核验的 Laguna XS 2.1 行。TOML 中已有的 37.5 分明确属于 Terminal-Bench 2.0，不能映射到 v4。

尚未解决的问题：
- 需要取得可查询的完整 v4 榜单或该模型的原始 v4 评测记录。

最近核验时间：2026-11-05T01:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1)

研究备注：
- 已检查官方 0.1 结果页，未见 XS 2.1；该页没有显示完整参评模型集合，不能据此确认不存在成绩。

尚未解决的问题：
- 需要完整榜单或直接评测记录以确认是否有公开结果。

最近核验时间：2026-11-05T01:50+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Poolside Laguna XS 2.1 model card](https://huggingface.co/poolside/Laguna-XS-2.1)

研究备注：
- 模型支持工具且定位为 agentic coding，可适用工作流评测；Zapier 页面只展示前 10 条并说明还有 119 条折叠结果，无法确认隐藏结果中是否有该模型。

尚未解决的问题：
- 需要检查 Zapier 完整榜单的折叠项目或找到该模型 v1.0.6 原始运行。

最近核验时间：2026-11-05T01:50+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Poolside Laguna XS 2.1 model card](https://huggingface.co/poolside/Laguna-XS-2.1)
- [OSWorld V2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 模型规格为文本输入；OSWorld V2.1 需要根据桌面截图进行 GUI 操作，XS 2.1 没有视觉输入能力。

最近核验时间：2026-11-05T01:50+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Poolside Laguna XS 2.1 model card](https://huggingface.co/poolside/Laguna-XS-2.1)
- [Chartography official benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型规格为文本输入；Chartography 任务要求读取图表图像，XS 2.1 不具备图像输入能力。

最近核验时间：2026-11-05T01:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [Humanity’s Last Exam leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 已检查厂商发布资料和公开 HLE 页面，未找到 Laguna XS 2.1 的成绩。

最近核验时间：2026-11-05T01:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1)

研究备注：
- 未找到 Laguna XS 2.1 的 Artificial Analysis Intelligence Index v5.0 成绩；Poolside 的编码类报告不是该综合指数结果。

最近核验时间：2026-11-05T01:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1)
- [GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 已检查厂商发布资料及公开 GDPval-AA v2.1 页面，未找到 Laguna XS 2.1 成绩。

最近核验时间：2026-11-05T01:50+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index 2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Poolside Laguna XS 2.1 release page](https://poolside.ai/blog/introducing-laguna-s-2-1)

研究备注：
- 已检查当前公开 Vals Index 2.2 榜单，未找到 Laguna XS 2.1 的对应记录。

最近核验时间：2026-11-05T01:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        }
      ],
      "notes": [
        "未找到 Laguna XS 2.1 的 Artificial Analysis Intelligence Index v5.0 成绩；Poolside 的编码类报告不是该综合指数结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Poolside Laguna XS 2.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-XS-2.1"
        }
      ],
      "notes": [
        "模型支持工具且定位为 agentic coding，可适用工作流评测；Zapier 页面只展示前 10 条并说明还有 119 条折叠结果，无法确认隐藏结果中是否有该模型。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要检查 Zapier 完整榜单的折叠项目或找到该模型 v1.0.6 原始运行。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna XS 2.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-XS-2.1"
        },
        {
          "label": "Chartography official benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型规格为文本输入；Chartography 任务要求读取图表图像，XS 2.1 不具备图像输入能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Poolside DeepSWE v1.1 comparison",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard and methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Poolside 的 DeepSWE v1.1 表列出 Laguna XS 2.1 为 0.3%，pass@1，平均每题 3 次尝试。页面声明对照表采用供应商、基准作者或第三方来源中的最高报告值；未指出该行所用来源或 harness。分数作为已公开的厂商报告记录，未推断 harness。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要找到该 Laguna XS 2.1 结果的具体原始运行、来源和 harness，确认其测试条件。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "已检查厂商发布资料及公开 GDPval-AA v2.1 页面，未找到 Laguna XS 2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        },
        {
          "label": "Humanity’s Last Exam leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "已检查厂商发布资料和公开 HLE 页面，未找到 Laguna XS 2.1 的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna XS 2.1 model card",
          "url": "https://huggingface.co/poolside/Laguna-XS-2.1"
        },
        {
          "label": "OSWorld V2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "模型规格为文本输入；OSWorld V2.1 需要根据桌面截图进行 GUI 操作，XS 2.1 没有视觉输入能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-xs-2-1"
        },
        {
          "label": "SWE-bench Pro V2 official leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "TOML 中已有 47.6 的 SWE-Bench Pro 记录未标版本，来自 2026-07-02 的 XS 2.1 发布材料；官方 Pro V2 于 2026-09 发布且任务集更新，不能将旧行映射到 V2。检查的 Pro V2 榜单未找到 XS 2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        }
      ],
      "notes": [
        "已检查官方 0.1 结果页，未见 XS 2.1；该页没有显示完整参评模型集合，不能据此确认不存在成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要完整榜单或直接评测记录以确认是否有公开结果。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T01:50+08:00",
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
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-xs-2-1"
        }
      ],
      "notes": [
        "官方 v4 榜单当前页面未显示可核验的 Laguna XS 2.1 行。TOML 中已有的 37.5 分明确属于 Terminal-Bench 2.0，不能映射到 v4。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要取得可查询的完整 v4 榜单或该模型的原始 v4 评测记录。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T01:50+08:00",
      "checked_sources": [
        {
          "label": "Vals Index 2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Poolside Laguna XS 2.1 release page",
          "url": "https://poolside.ai/blog/introducing-laguna-s-2-1"
        }
      ],
      "notes": [
        "已检查当前公开 Vals Index 2.2 榜单，未找到 Laguna XS 2.1 的对应记录。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 4,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T01:50+08:00",
  "model_id": "poolside/laguna-xs-2.1",
  "model_notes": [
    "模型身份及发布日期依据 Poolside 2026-07-02 的 Laguna XS 2.1 发布资料；发布资料将其与 7 月 21 日发布的 Laguna S 2.1 明确区分。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
