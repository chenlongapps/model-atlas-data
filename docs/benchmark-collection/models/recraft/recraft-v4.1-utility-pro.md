# Recraft V4.1 Utility Pro Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：recraft/recraft-v4.1-utility-pro
- 模型名称：Recraft V4.1 Utility Pro
- 发布日期：2026-05-14
- 最近检查时间：2026-11-05T06:05+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 模型身份核对为 recraft-v4.1-utility-pro，发布日期 2026-05-14；官方 API 精确变体为 recraftv4_1_utility_pro，返回 2K raster image；本地能力字段为 tools=false、reasoning=false。
- 未发现本批 11 项 Benchmark 的目标成绩。此处不适用判断基于官方端点输出形式和基准任务要求，不是将缺失成绩记为零。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T06:05+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T06:05+08:00 |
| terminal-bench-v4 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Terminal-Bench 4.0](https://www.tbench.ai/?efforts=all&version=4.0) | 2026-11-05T06:05+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T06:05+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft image-to-image endpoint](https://www.recraft.ai/docs/api-reference/tools/image-to-image), [Zapier AutomationBench 1.0.6](https://zapier.com/benchmarks) | 2026-11-05T06:05+08:00 |
| osworld-v2.1 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft image-to-image endpoint](https://www.recraft.ai/docs/api-reference/tools/image-to-image), [OSWorld V2.1](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T06:05+08:00 |
| chartography | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft image-to-image endpoint](https://www.recraft.ai/docs/api-reference/tools/image-to-image), [Surge Chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T06:05+08:00 |
| humanitys-last-exam | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T06:05+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [AA Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T06:05+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T06:05+08:00 |
| vals-index-v2.2 | 不适用 | — | [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1), [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1), [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T06:05+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [DeepSWE v1.1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- Benchmark 要求编码 agent 执行软件工程任务并提交代码补丁；Recraft endpoint 生成 SVG/栅格图像。

最近核验时间：2026-11-05T06:05+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Scale SWE-bench Pro V2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Benchmark 评测 agent 修改代码仓库并通过隐藏测试；Recraft endpoint 生成 SVG/栅格图像。

最近核验时间：2026-11-05T06:05+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Terminal-Bench 4.0](https://www.tbench.ai/?efforts=all&version=4.0)

研究备注：
- Benchmark 要求 agent 在终端执行任务；Recraft endpoint 不提供终端交互或代码文本输出。

最近核验时间：2026-11-05T06:05+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Terminal-Bench Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Benchmark 要求 agent 在终端完成科学工作流；Recraft endpoint 不提供终端交互或代码文本输出。

最近核验时间：2026-11-05T06:05+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft image-to-image endpoint](https://www.recraft.ai/docs/api-reference/tools/image-to-image)
- [Zapier AutomationBench 1.0.6](https://zapier.com/benchmarks)

研究备注：
- AutomationBench 衡量 agent 调用应用工具完成业务工作流；本地能力定义为不支持工具，端点仅输出图像。

最近核验时间：2026-11-05T06:05+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft image-to-image endpoint](https://www.recraft.ai/docs/api-reference/tools/image-to-image)
- [OSWorld V2.1](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld 要求 agent 观察并操作桌面；Recraft 的图像编辑接口接收图像/提示词后返回图像，没有桌面动作输出。

最近核验时间：2026-11-05T06:05+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft image-to-image endpoint](https://www.recraft.ai/docs/api-reference/tools/image-to-image)
- [Surge Chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography 需要依据图表和问题输出文本答案；Recraft 的图像输入用于图生图，输出仍是图像，任务格式不匹配。

最近核验时间：2026-11-05T06:05+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Artificial Analysis HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- HLE 要求对学术问题给出自动评分的答案文本；该型号只生成 SVG 或栅格图像。

最近核验时间：2026-11-05T06:05+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [AA Intelligence Index V5.0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA Intelligence Index V5.0.1 综合评估语言模型的知识工作、编码、科学和通用能力；该型号是图像生成 endpoint。

最近核验时间：2026-11-05T06:05+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA 要求通过 shell/网页工具完成职业任务并生成文档等文件；该型号仅生成图像。

最近核验时间：2026-11-05T06:05+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Recraft V4.1 API variants](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1)
- [Recraft V4.1 product documentation](https://www.recraft.ai/docs/recraft-models/recraft-v4-1)
- [Vals Index v2.2](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index 衡量金融、编码、法律及税务 agent 的工作表现；图像生成 endpoint 不具备这些文本/工具工作能力。

最近核验时间：2026-11-05T06:05+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft V4.1 product documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "AA Intelligence Index V5.0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA Intelligence Index V5.0.1 综合评估语言模型的知识工作、编码、科学和通用能力；该型号是图像生成 endpoint。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft image-to-image endpoint",
          "url": "https://www.recraft.ai/docs/api-reference/tools/image-to-image"
        },
        {
          "label": "Zapier AutomationBench 1.0.6",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench 衡量 agent 调用应用工具完成业务工作流；本地能力定义为不支持工具，端点仅输出图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft image-to-image endpoint",
          "url": "https://www.recraft.ai/docs/api-reference/tools/image-to-image"
        },
        {
          "label": "Surge Chartography",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography 需要依据图表和问题输出文本答案；Recraft 的图像输入用于图生图，输出仍是图像，任务格式不匹配。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "DeepSWE v1.1",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "Benchmark 要求编码 agent 执行软件工程任务并提交代码补丁；Recraft endpoint 生成 SVG/栅格图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft V4.1 product documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "GDPval-AA v2.1",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA 要求通过 shell/网页工具完成职业任务并生成文档等文件；该型号仅生成图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft V4.1 product documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Artificial Analysis HLE",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "HLE 要求对学术问题给出自动评分的答案文本；该型号只生成 SVG 或栅格图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft image-to-image endpoint",
          "url": "https://www.recraft.ai/docs/api-reference/tools/image-to-image"
        },
        {
          "label": "OSWorld V2.1",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld 要求 agent 观察并操作桌面；Recraft 的图像编辑接口接收图像/提示词后返回图像，没有桌面动作输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Scale SWE-bench Pro V2",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Benchmark 评测 agent 修改代码仓库并通过隐藏测试；Recraft endpoint 生成 SVG/栅格图像。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Terminal-Bench Science 0.1",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Benchmark 要求 agent 在终端完成科学工作流；Recraft endpoint 不提供终端交互或代码文本输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Terminal-Bench 4.0",
          "url": "https://www.tbench.ai/?efforts=all&version=4.0"
        }
      ],
      "notes": [
        "Benchmark 要求 agent 在终端执行任务；Recraft endpoint 不提供终端交互或代码文本输出。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T06:05+08:00",
      "checked_sources": [
        {
          "label": "Recraft V4.1 API variants",
          "url": "https://www.recraft.ai/docs/api-reference/models/recraft-v4-1"
        },
        {
          "label": "Recraft V4.1 product documentation",
          "url": "https://www.recraft.ai/docs/recraft-models/recraft-v4-1"
        },
        {
          "label": "Vals Index v2.2",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index 衡量金融、编码、法律及税务 agent 的工作表现；图像生成 endpoint 不具备这些文本/工具工作能力。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T06:05+08:00",
  "model_id": "recraft/recraft-v4.1-utility-pro",
  "model_notes": [
    "模型身份核对为 recraft-v4.1-utility-pro，发布日期 2026-05-14；官方 API 精确变体为 recraftv4_1_utility_pro，返回 2K raster image；本地能力字段为 tools=false、reasoning=false。",
    "未发现本批 11 项 Benchmark 的目标成绩。此处不适用判断基于官方端点输出形式和基准任务要求，不是将缺失成绩记为零。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
