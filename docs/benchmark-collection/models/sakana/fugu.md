# Fugu Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：sakana/fugu
- 模型名称：Fugu
- 发布日期：2026-06-15
- 最近检查时间：2026-11-05T02:56+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：1
- 收集前已有成绩数量：12
- 当前已收录的对应成绩数量：1

## 模型身份与范围说明

- 本轮只补充规范化了已有 HLE 记录：Sakana 技术报告 v2 的 Fugu 原始 HLE 为 47.2；完整 2,500 题含多模态、without tools。图中的 HLE(text) 48.5 属于不同数据集划分，不合并。报告没有公布评测日期，未填 date。来源：https://arxiv.org/html/2606.21228v2；https://labs.scale.com/leaderboard/humanitys_last_exam
- 本地 release_date 为 2026-06-15；Sakana 官方 Fugu 一般可用公告为 2026-06-22。两日期对应范围可能不同，保留仓库日期并记录差异，不自行重排或修改。来源：https://sakana.ai/fugu-release/

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 leaderboard and methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:56+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:56+08:00 |
| terminal-bench-v4 | 待核实 | — | [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all), [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:56+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2) | 2026-11-05T02:56+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md), [OSWorld official site](https://osworld-v2.xlang.ai/), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |
| chartography | 未找到 | — | [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |
| humanitys-last-exam | 已存在 | 47.2 (metric=accuracy; version=unspecified; dataset=Full 2,500-sample HLE, including multimodal samples; variant=without tools) | [Sakana Fugu technical report v2](https://arxiv.org/html/2606.21228v2), [Official HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index), [Sakana model catalog](https://console.sakana.ai/models) | 2026-11-05T02:56+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard and methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The current v1.1 public table does not list Fugu. Sakana reports no Fugu score for DeepSWE v1.1 in its technical report.

最近核验时间：2026-11-05T02:56+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The existing TOML row “SWE Bench Pro” 59.0 has no V2 version or V2 conditions. Sakana’s report names the earlier SWE Bench Pro evaluation; it does not report V2. The official V2 board does not list Fugu.

最近核验时间：2026-11-05T02:56+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0&efforts=all)
- [Terminal-Bench 4.0 release notes](https://www.tbench.ai/news/terminal-bench-4-0)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The existing Terminal Bench 2.1 result (80.2) is not v4.0. The current official v4 page did not expose readable dynamic rows.

尚未解决的问题：
- Cannot confirm whether an exact Fugu v4.0 result exists from the current dynamic board response.

最近核验时间：2026-11-05T02:56+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)

研究备注：
- The official Science 0.1 result table does not list Fugu; Sakana’s report does not include this benchmark.

最近核验时间：2026-11-05T02:56+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Sakana Fugu technical report](https://arxiv.org/html/2606.21228v2)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The v1.0.6 board shows the top 10 and a collapsed 116 additional entries. Sakana’s AutomationBench statement refers to Fugu Max, not Fugu.

尚未解决的问题：
- The complete leaderboard is not visible, so absence of a Fugu result cannot be confirmed.

最近核验时间：2026-11-05T02:56+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)
- [OSWorld official site](https://osworld-v2.xlang.ai/)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- Fugu accepts image inputs and supports tools, so the benchmark is not marked inapplicable. The official v2.1 materials checked do not list a Fugu result.

最近核验时间：2026-11-05T02:56+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Chartography official benchmark page](https://surgehq.ai/benchmarks/chartography)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- Fugu supports image input and text output; the current official Chartography board does not list Fugu. Sakana’s current Chartography claim is for Fugu Ultra, not Fugu.

最近核验时间：2026-11-05T02:56+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 47.2
- metric: accuracy
- version: unspecified
- dataset: Full 2,500-sample HLE, including multimodal samples
- variant: without tools
- source: [https://arxiv.org/html/2606.21228v2](https://arxiv.org/html/2606.21228v2)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Sakana Fugu technical report v2](https://arxiv.org/html/2606.21228v2)
- [Official HLE leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The existing 47.2 TOML score is explicitly listed for Fugu in report Table 1. Appendix A specifies the full 2,500-sample set including multimodal samples, without tools. HLE’s official methodology defines accuracy as its ranking metric; the record now uses the canonical benchmark name and matching metric/version. Figure 1 separately reports HLE(text) 48.5; that text-only split is not merged with this full-set result.

最近核验时间：2026-11-05T02:56+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- No Fugu result is listed for AA Intelligence Index V5. HLE-Diamond within AA V5 is distinct from the original HLE score above.

最近核验时间：2026-11-05T02:56+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The current official GDPval-AA v2.1 board does not list a Fugu Elo result. Sakana’s Fugu report does not contain this evaluation.

最近核验时间：2026-11-05T02:56+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 benchmark page](https://www.vals.ai/benchmarks/vals_index)
- [Sakana model catalog](https://console.sakana.ai/models)

研究备注：
- The current official Vals Index v2.2 listing does not show Fugu.

最近核验时间：2026-11-05T02:56+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "No Fugu result is listed for AA Intelligence Index V5. HLE-Diamond within AA V5 is distinct from the original HLE score above."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The v1.0.6 board shows the top 10 and a collapsed 116 additional entries. Sakana’s AutomationBench statement refers to Fugu Max, not Fugu."
      ],
      "status": "待核实",
      "unresolved": [
        "The complete leaderboard is not visible, so absence of a Fugu result cannot be confirmed."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Chartography official benchmark page",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "Fugu supports image input and text output; the current official Chartography board does not list Fugu. Sakana’s current Chartography claim is for Fugu Ultra, not Fugu."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard and methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The current v1.1 public table does not list Fugu. Sakana reports no Fugu score for DeepSWE v1.1 in its technical report."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The current official GDPval-AA v2.1 board does not list a Fugu Elo result. Sakana’s Fugu report does not contain this evaluation."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Sakana Fugu technical report v2",
          "url": "https://arxiv.org/html/2606.21228v2"
        },
        {
          "label": "Official HLE leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The existing 47.2 TOML score is explicitly listed for Fugu in report Table 1. Appendix A specifies the full 2,500-sample set including multimodal samples, without tools. HLE’s official methodology defines accuracy as its ranking metric; the record now uses the canonical benchmark name and matching metric/version. Figure 1 separately reports HLE(text) 48.5; that text-only split is not merged with this full-set result."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "OSWorld v2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        },
        {
          "label": "OSWorld official site",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "Fugu accepts image inputs and supports tools, so the benchmark is not marked inapplicable. The official v2.1 materials checked do not list a Fugu result."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The existing TOML row “SWE Bench Pro” 59.0 has no V2 version or V2 conditions. Sakana’s report names the earlier SWE Bench Pro evaluation; it does not report V2. The official V2 board does not list Fugu."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The official Science 0.1 result table does not list Fugu; Sakana’s report does not include this benchmark."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:56+08:00",
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
          "label": "Sakana Fugu technical report",
          "url": "https://arxiv.org/html/2606.21228v2"
        }
      ],
      "notes": [
        "The existing Terminal Bench 2.1 result (80.2) is not v4.0. The current official v4 page did not expose readable dynamic rows."
      ],
      "status": "待核实",
      "unresolved": [
        "Cannot confirm whether an exact Fugu v4.0 result exists from the current dynamic board response."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:56+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 benchmark page",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Sakana model catalog",
          "url": "https://console.sakana.ai/models"
        }
      ],
      "notes": [
        "The current official Vals Index v2.2 listing does not show Fugu."
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 12,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:56+08:00",
  "model_id": "sakana/fugu",
  "model_notes": [
    "本轮只补充规范化了已有 HLE 记录：Sakana 技术报告 v2 的 Fugu 原始 HLE 为 47.2；完整 2,500 题含多模态、without tools。图中的 HLE(text) 48.5 属于不同数据集划分，不合并。报告没有公布评测日期，未填 date。来源：https://arxiv.org/html/2606.21228v2；https://labs.scale.com/leaderboard/humanitys_last_exam",
    "本地 release_date 为 2026-06-15；Sakana 官方 Fugu 一般可用公告为 2026-06-22。两日期对应范围可能不同，保留仓库日期并记录差异，不自行重排或修改。来源：https://sakana.ai/fugu-release/"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
