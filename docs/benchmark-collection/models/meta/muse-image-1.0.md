# Muse Image Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-image-1.0
- 模型名称：Muse Image
- 发布日期：2026-07-07
- 最近检查时间：2026-11-05T01:18+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Meta 官方将 Muse Image 描述为图像生成/编辑模型；本地 TOML 为 image 类型、图像输入/输出且 tools.supported=false。官方提到的内部搜索/代码工具用于生成流程，未显示为 benchmark 可调用的通用工具接口。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T01:18+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T01:18+08:00 |
| terminal-bench-v4 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T01:18+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T01:18+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Zapier AutomationBench](https://zapier.com/benchmarks), [AutomationBench repository](https://github.com/zapier/AutomationBench) | 2026-11-05T01:18+08:00 |
| osworld-v2.1 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [OSWorld V2.1 guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T01:18+08:00 |
| chartography | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Chartography paper](https://arxiv.org/html/2608.10677) | 2026-11-05T01:18+08:00 |
| humanitys-last-exam | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Humanity’s Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T01:18+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T01:18+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T01:18+08:00 |
| vals-index-v2.2 | 不适用 | — | [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/), [Vals Index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T01:18+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Zapier AutomationBench](https://zapier.com/benchmarks)
- [AutomationBench repository](https://github.com/zapier/AutomationBench)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [OSWorld V2.1 guide](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Chartography paper](https://arxiv.org/html/2608.10677)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Humanity’s Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Meta Muse Image announcement](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Vals Index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。

最近核验时间：2026-11-05T01:18+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Artificial Analysis Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Zapier AutomationBench",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "DeepSWE v1.1",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Humanity’s Last Exam",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "OSWorld V2.1 guide",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Terminal-Bench Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T01:18+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Image announcement",
          "url": "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/"
        },
        {
          "label": "Vals Index",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "该 Benchmark 要求文本回答、代码/终端操作、SaaS 工作流或桌面操作，而 Muse Image 的对外任务是生成/编辑图像；内部图像生成辅助工具不等同于可调用的通用 agent 工具。按不适用记录，未声称已穷尽所有榜单。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T01:18+08:00",
  "model_id": "meta/muse-image-1.0",
  "model_notes": [
    "Meta 官方将 Muse Image 描述为图像生成/编辑模型；本地 TOML 为 image 类型、图像输入/输出且 tools.supported=false。官方提到的内部搜索/代码工具用于生成流程，未显示为 benchmark 可调用的通用工具接口。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
