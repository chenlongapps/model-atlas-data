# HappyHorse-1.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/happyhorse-1.1
- 模型名称：HappyHorse-1.1
- 发布日期：2026-06-16
- 最近检查时间：2026-11-05T02:41+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 阿里官方发布列表确认 happyhorse-1.1-t2v、-i2v、-r2v 于 2026-06-16 发布；官方接口为视频生成，输入文本/图像/参考素材并输出视频，不提供工具能力。来源：https://www.alibabacloud.com/help/en/model-studio/newly-released-models；https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/
- 已查看相应官方基准榜单或方法页；本模型类型与 11 项评测的答题/agent 输出不匹配，没有将可见榜单缺行视为“未找到”或将其他类型分数映射过来。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T02:41+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T02:41+08:00 |
| terminal-bench-v4 | 不适用 | — | [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/), [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?efforts=all&version=4.0) | 2026-11-05T02:41+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T02:41+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks) | 2026-11-05T02:41+08:00 |
| osworld-v2.1 | 不适用 | — | [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/), [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T02:41+08:00 |
| chartography | 不适用 | — | [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/), [Chartography benchmark listing](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T02:41+08:00 |
| humanitys-last-exam | 不适用 | — | [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-05T02:41+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/), [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T02:41+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/), [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T02:41+08:00 |
| vals-index-v2.2 | 不适用 | — | [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/), [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T02:41+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Official docs define HappyHorse-1.1 variants as text/image/reference-to-video generators; they do not produce code patches or coding-agent actions.

最近核验时间：2026-11-05T02:41+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- The official HappyHorse interface generates video and does not implement repository code fixes.

最近核验时间：2026-11-05T02:41+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/)
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?efforts=all&version=4.0)

研究备注：
- The official HappyHorse interface generates video and has no terminal/tool execution capability.

最近核验时间：2026-11-05T02:41+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Terminal-Bench Science 0.1 results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- The official HappyHorse interface generates video and has no scientific coding or terminal-agent capability.

最近核验时间：2026-11-05T02:41+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)

研究备注：
- AutomationBench evaluates tool-using agents executing application workflows; HappyHorse is a video-generation model with no tools.

最近核验时间：2026-11-05T02:41+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/)
- [OSWorld v2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- OSWorld requires screenshot observation and computer actions; the official HappyHorse interface outputs video and has no computer-use actions.

最近核验时间：2026-11-05T02:41+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/)
- [Chartography benchmark listing](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography evaluates chart understanding with textual answers; HappyHorse produces video output rather than chart-question answers.

最近核验时间：2026-11-05T02:41+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Scale HLE leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- The official HappyHorse model variants generate video, not textual answers to HLE questions.

最近核验时间：2026-11-05T02:41+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/)
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- HappyHorse is a video-generation model, not a general-purpose language model for this index.

最近核验时间：2026-11-05T02:41+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/)
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA evaluates agentic work products using tools; HappyHorse generates video and does not provide the required work-artifact workflow.

最近核验时间：2026-11-05T02:41+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Alibaba HappyHorse video model documentation](https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/)
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index evaluates agentic work output in business domains; HappyHorse is a video-generation model.

最近核验时间：2026-11-05T02:41+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse video model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/"
        },
        {
          "label": "Artificial Analysis methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "HappyHorse is a video-generation model, not a general-purpose language model for this index."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse release list",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench evaluates tool-using agents executing application workflows; HappyHorse is a video-generation model with no tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse video model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/"
        },
        {
          "label": "Chartography benchmark listing",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography evaluates chart understanding with textual answers; HappyHorse produces video output rather than chart-question answers."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse release list",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Official docs define HappyHorse-1.1 variants as text/image/reference-to-video generators; they do not produce code patches or coding-agent actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse video model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/"
        },
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA evaluates agentic work products using tools; HappyHorse generates video and does not provide the required work-artifact workflow."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse release list",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Scale HLE leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "The official HappyHorse model variants generate video, not textual answers to HLE questions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse video model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/"
        },
        {
          "label": "OSWorld v2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "OSWorld requires screenshot observation and computer actions; the official HappyHorse interface outputs video and has no computer-use actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse release list",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "The official HappyHorse interface generates video and does not implement repository code fixes."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse release list",
          "url": "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"
        },
        {
          "label": "Terminal-Bench Science 0.1 results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "The official HappyHorse interface generates video and has no scientific coding or terminal-agent capability."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse video model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        }
      ],
      "notes": [
        "The official HappyHorse interface generates video and has no terminal/tool execution capability."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:41+08:00",
      "checked_sources": [
        {
          "label": "Alibaba HappyHorse video model documentation",
          "url": "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/"
        },
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index evaluates agentic work output in business domains; HappyHorse is a video-generation model."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:41+08:00",
  "model_id": "alibaba/happyhorse-1.1",
  "model_notes": [
    "阿里官方发布列表确认 happyhorse-1.1-t2v、-i2v、-r2v 于 2026-06-16 发布；官方接口为视频生成，输入文本/图像/参考素材并输出视频，不提供工具能力。来源：https://www.alibabacloud.com/help/en/model-studio/newly-released-models；https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/",
    "已查看相应官方基准榜单或方法页；本模型类型与 11 项评测的答题/agent 输出不匹配，没有将可见榜单缺行视为“未找到”或将其他类型分数映射过来。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
