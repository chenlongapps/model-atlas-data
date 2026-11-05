# GPT-6 Astra (Fast) Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：openai/gpt-6-astra-fast
- 模型名称：GPT-6 Astra (Fast)
- 发布日期：2026-09-04
- 最近检查时间：2026-11-04T13:03+08:00
- 整体处理状态：已完成
- 新增成绩数量：1
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE official leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/) | 2026-11-04T13:03+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro dataset and V2 protocol](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro), [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/) | 2026-11-04T13:03+08:00 |
| terminal-bench-v4 | 未找到 | — | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T13:03+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [Terminal-Bench Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement) | 2026-11-04T13:03+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/) | 2026-11-04T13:03+08:00 |
| osworld-v2.1 | 未找到 | — | [Meta Muse Wonder model card and OSWorld V2.1 methodology](https://research.meta.ai/static/muse-wonder-model-card/), [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/) | 2026-11-04T13:03+08:00 |
| chartography | 未找到 | — | [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T13:03+08:00 |
| humanitys-last-exam | 未找到 | — | [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T13:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 57 (metric=index score; version=5.0; effort=max; variant=Fast mode) | [Artificial Analysis OpenAI model leaderboard](https://artificialanalysis.ai/providers/openai/), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Data API versioning documentation](https://artificialanalysis.ai/data-api/docs), [OpenAI GPT-6 Astra Fast mode release note](https://openai.com/index/gpt-6-astra/) | 2026-11-04T13:03+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis OpenAI model leaderboard](https://artificialanalysis.ai/providers/openai/) | 2026-11-04T13:03+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T13:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)

研究备注：
- DeepSWE 榜单列出的 GPT-6 Astra 为 xhigh 配置；未找到明确标注 Fast 的成绩，不能将该结果归到本模型。

最近核验时间：2026-11-04T13:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale AI SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro dataset and V2 protocol](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)

研究备注：
- Scale V2 榜单列出的 GPT-6 Astra (Codex) high 并未标注 Fast；不将该结果归到本模型。

最近核验时间：2026-11-04T13:03+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [Terminal-Bench 4.0 official release](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- OpenAI 发布资料报告标准 GPT-6 Astra 的 57.9%，没有说明为 Fast 模式；未找到 Fast 专属的公开成绩或测试条件。

最近核验时间：2026-11-04T13:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [Terminal-Bench Science 0.1 announcement](https://www.terminal-bench-science.ai/announcement)

研究备注：
- OpenAI 发布资料的 GPT-6 Astra 成绩（含较低成本设置）没有明确标注 Fast；不根据较低成本描述推断为 Fast。

最近核验时间：2026-11-04T13:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)

研究备注：
- Zapier 榜单列出 Astra Max、XHigh、High 等配置，但没有 Fast 专属成绩；OpenAI 发布的 Astra 总分也未标明 Fast。

最近核验时间：2026-11-04T13:03+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Meta Muse Wonder model card and OSWorld V2.1 methodology](https://research.meta.ai/static/muse-wonder-model-card/)
- [OSWorld V2.1 public evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)

研究备注：
- Meta 的 OSWorld v2.1 Astra 结果是 max reasoning；OpenAI 发布的 72.6 是 OSWorld v2.0 partial。均不等同于 Astra Fast 的 v2.1 结果。

最近核验时间：2026-11-04T13:03+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge AI Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Surge 榜单中的 GPT-6 Astra 成绩标为 Max reasoning；未找到 Fast 条件的成绩。

最近核验时间：2026-11-04T13:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OpenAI GPT-6 Astra release](https://openai.com/index/gpt-6-astra/)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- OpenAI 发布的 57.2 是标准 GPT-6 Astra with tools 成绩，没有标注 Fast；不转移到本模型。

最近核验时间：2026-11-04T13:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 57
- metric: index score
- version: 5.0
- effort: max
- variant: Fast mode
- source: [https://artificialanalysis.ai/providers/openai/](https://artificialanalysis.ai/providers/openai/)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis OpenAI model leaderboard](https://artificialanalysis.ai/providers/openai/)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Data API versioning documentation](https://artificialanalysis.ai/data-api/docs)
- [OpenAI GPT-6 Astra Fast mode release note](https://openai.com/index/gpt-6-astra/)

研究备注：
- Artificial Analysis 的 OpenAI 榜单明确列出 “GPT-6 Astra (max) (Fast)” 且 Index score 为 57，按公开整数精度记录。来源方法页当前标示 v5.0.1；Data API 文档说明 patch 版本不会反映在 major.minor 字段中，与本地定义 v5.0 对应。未公布具体评测日期，因此不填 date。

最近核验时间：2026-11-04T13:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis OpenAI model leaderboard](https://artificialanalysis.ai/providers/openai/)

研究备注：
- 已检查官方 v2.1 评测定义和 AA OpenAI 模型页，未找到可确认属于 Fast 的 Elo 成绩；不沿用标准 Astra 的结果。

最近核验时间：2026-11-04T13:03+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals v2.2 榜单有标准 GPT-6 Astra 结果，但未标注 Fast；无法确认该分数属于 Fast 模式。

最近核验时间：2026-11-04T13:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis OpenAI model leaderboard",
          "url": "https://artificialanalysis.ai/providers/openai/"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Data API versioning documentation",
          "url": "https://artificialanalysis.ai/data-api/docs"
        },
        {
          "label": "OpenAI GPT-6 Astra Fast mode release note",
          "url": "https://openai.com/index/gpt-6-astra/"
        }
      ],
      "notes": [
        "Artificial Analysis 的 OpenAI 榜单明确列出 “GPT-6 Astra (max) (Fast)” 且 Index score 为 57，按公开整数精度记录。来源方法页当前标示 v5.0.1；Data API 文档说明 patch 版本不会反映在 major.minor 字段中，与本地定义 v5.0 对应。未公布具体评测日期，因此不填 date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        }
      ],
      "notes": [
        "Zapier 榜单列出 Astra Max、XHigh、High 等配置，但没有 Fast 专属成绩；OpenAI 发布的 Astra 总分也未标明 Fast。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Surge 榜单中的 GPT-6 Astra 成绩标为 Max reasoning；未找到 Fast 条件的成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        }
      ],
      "notes": [
        "DeepSWE 榜单列出的 GPT-6 Astra 为 xhigh 配置；未找到明确标注 Fast 的成绩，不能将该结果归到本模型。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis OpenAI model leaderboard",
          "url": "https://artificialanalysis.ai/providers/openai/"
        }
      ],
      "notes": [
        "已检查官方 v2.1 评测定义和 AA OpenAI 模型页，未找到可确认属于 Fast 的 Elo 成绩；不沿用标准 Astra 的结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "OpenAI 发布的 57.2 是标准 GPT-6 Astra with tools 成绩，没有标注 Fast；不转移到本模型。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Wonder model card and OSWorld V2.1 methodology",
          "url": "https://research.meta.ai/static/muse-wonder-model-card/"
        },
        {
          "label": "OSWorld V2.1 public evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        }
      ],
      "notes": [
        "Meta 的 OSWorld v2.1 Astra 结果是 max reasoning；OpenAI 发布的 72.6 是 OSWorld v2.0 partial。均不等同于 Astra Fast 的 v2.1 结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro dataset and V2 protocol",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        },
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        }
      ],
      "notes": [
        "Scale V2 榜单列出的 GPT-6 Astra (Codex) high 并未标注 Fast；不将该结果归到本模型。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "Terminal-Bench Science 0.1 announcement",
          "url": "https://www.terminal-bench-science.ai/announcement"
        }
      ],
      "notes": [
        "OpenAI 发布资料的 GPT-6 Astra 成绩（含较低成本设置）没有明确标注 Fast；不根据较低成本描述推断为 Fast。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "OpenAI GPT-6 Astra release",
          "url": "https://openai.com/index/gpt-6-astra/"
        },
        {
          "label": "Terminal-Bench 4.0 official release",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "OpenAI 发布资料报告标准 GPT-6 Astra 的 57.9%，没有说明为 Fast 模式；未找到 Fast 专属的公开成绩或测试条件。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T13:03+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals v2.2 榜单有标准 GPT-6 Astra 结果，但未标注 Fast；无法确认该分数属于 Fast 模式。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T13:03+08:00",
  "model_id": "openai/gpt-6-astra-fast",
  "new_records": 1,
  "overall_status": "已完成"
}

-->
