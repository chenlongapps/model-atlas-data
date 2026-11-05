# Recraft V4.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：recraft/recraft-v4.1
- 模型名称：Recraft V4.1
- 发布日期：2026-05-14
- 最近检查时间：2026-11-05T06:01+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 模型身份为 Recraft V4.1，发布日期 2026-05-14；官方资料称其为 text-to-image 服务，本地 TOML 显示 image output 且不支持 tools。
- 图像编辑端点接受 image + prompt 并返回 image，不代表视觉问答或桌面操作能力；本批 11 项均不适用于该图像生成型号。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints), [DeepSWE definition](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T06:01+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints), [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:01+08:00 |
| terminal-bench-v4 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints), [Terminal-Bench 4.0](https://www.tbench.ai/?efforts=all&version=4.0) | 2026-11-05T06:01+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints), [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T06:01+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints), [Zapier AutomationBench](https://zapier.com/benchmarks) | 2026-11-05T06:01+08:00 |
| osworld-v2.1 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Image-to-image API](https://www.recraft.ai/docs/api-reference/tools/image-to-image), [OSWorld V2](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:01+08:00 |
| chartography | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Image-to-image API](https://www.recraft.ai/docs/api-reference/tools/image-to-image), [Chartography benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:01+08:00 |
| humanitys-last-exam | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:01+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:01+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:01+08:00 |
| vals-index-v2.2 | 不适用 | — | [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:01+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints)
- [DeepSWE definition](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 软件工程任务要求可执行代码修改与文本/工具操作；Recraft V4.1 是图像生成 API。

最近核验时间：2026-11-05T06:01+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints)
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- SWE-bench Pro V2 需要软件工程 agent 产出代码补丁；Recraft V4.1 只提供图像生成/编辑端点。

最近核验时间：2026-11-05T06:01+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints)
- [Terminal-Bench 4.0](https://www.tbench.ai/?efforts=all&version=4.0)

研究备注：
- Terminal-Bench 要求 agent 在终端环境执行任务；Recraft 是图像生成服务，不提供终端交互或工具调用。

最近核验时间：2026-11-05T06:01+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints)
- [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 该评测要求在终端中完成科学工作流；Recraft 只生成或编辑图像。

最近核验时间：2026-11-05T06:01+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Recraft API endpoints](https://www.recraft.ai/docs/api-reference/endpoints)
- [Zapier AutomationBench](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 测量 agent 使用应用工具完成业务工作流；Recraft 图像 API 不提供模型工具调用或工作流动作。

最近核验时间：2026-11-05T06:01+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Image-to-image API](https://www.recraft.ai/docs/api-reference/tools/image-to-image)
- [OSWorld V2](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld 要求 agent 观察桌面并发出可执行操作；Recraft 图像编辑端点是 image + prompt → image，模型不提供桌面动作输出。

最近核验时间：2026-11-05T06:01+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Image-to-image API](https://www.recraft.ai/docs/api-reference/tools/image-to-image)
- [Chartography benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 要求根据图表和问题生成文本答案；Recraft 的图像输入用于 image-to-image 编辑，输出仍为图像，任务输入输出不匹配。

最近核验时间：2026-11-05T06:01+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 需要对学术问题生成答案文本；Recraft 的公开服务仅生成图像，无法输出评分所需答案。

最近核验时间：2026-11-05T06:01+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [AA Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA Intelligence Index V5.0.1 综合语言模型的知识工作、编码、科学与通用推理；Recraft 是图像生成服务。

最近核验时间：2026-11-05T06:01+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求通过 shell 和网页浏览完成职业任务并生成文件；Recraft 图像生成 API 不提供相应 agent 能力。

最近核验时间：2026-11-05T06:01+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 model documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 衡量金融、编码、法律、税务领域 agent 的工作输出；图像生成服务与目标任务不匹配。

最近核验时间：2026-11-05T06:01+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "AA Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA Intelligence Index V5.0.1 综合语言模型的知识工作、编码、科学与通用推理；Recraft 是图像生成服务。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Recraft API endpoints",
          "url": "https://www.recraft.ai/docs/api-reference/endpoints"
        },
        {
          "label": "Zapier AutomationBench",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 测量 agent 使用应用工具完成业务工作流；Recraft 图像 API 不提供模型工具调用或工作流动作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Image-to-image API",
          "url": "https://www.recraft.ai/docs/api-reference/tools/image-to-image"
        },
        {
          "label": "Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 要求根据图表和问题生成文本答案；Recraft 的图像输入用于 image-to-image 编辑，输出仍为图像，任务输入输出不匹配。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Recraft API endpoints",
          "url": "https://www.recraft.ai/docs/api-reference/endpoints"
        },
        {
          "label": "DeepSWE definition",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "软件工程任务要求可执行代码修改与文本/工具操作；Recraft V4.1 是图像生成 API。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求通过 shell 和网页浏览完成职业任务并生成文件；Recraft 图像生成 API 不提供相应 agent 能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Artificial Analysis HLE",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 需要对学术问题生成答案文本；Recraft 的公开服务仅生成图像，无法输出评分所需答案。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Image-to-image API",
          "url": "https://www.recraft.ai/docs/api-reference/tools/image-to-image"
        },
        {
          "label": "OSWorld V2",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld 要求 agent 观察桌面并发出可执行操作；Recraft 图像编辑端点是 image + prompt → image，模型不提供桌面动作输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Recraft API endpoints",
          "url": "https://www.recraft.ai/docs/api-reference/endpoints"
        },
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 需要软件工程 agent 产出代码补丁；Recraft V4.1 只提供图像生成/编辑端点。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Recraft API endpoints",
          "url": "https://www.recraft.ai/docs/api-reference/endpoints"
        },
        {
          "label": "Terminal-Bench Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "该评测要求在终端中完成科学工作流；Recraft 只生成或编辑图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Recraft API endpoints",
          "url": "https://www.recraft.ai/docs/api-reference/endpoints"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        }
      ],
      "notes": [
        "Terminal-Bench 要求 agent 在终端环境执行任务；Recraft 是图像生成服务，不提供终端交互或工具调用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:01+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 model documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Vals Index v2.2",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 衡量金融、编码、法律、税务领域 agent 的工作输出；图像生成服务与目标任务不匹配。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:01+08:00",
  "model_id": "recraft/recraft-v4.1",
  "model_notes": [
    "模型身份为 Recraft V4.1，发布日期 2026-05-14；官方资料称其为 text-to-image 服务，本地 TOML 显示 image output 且不支持 tools。",
    "图像编辑端点接受 image + prompt 并返回 image，不代表视觉问答或桌面操作能力；本批 11 项均不适用于该图像生成型号。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
