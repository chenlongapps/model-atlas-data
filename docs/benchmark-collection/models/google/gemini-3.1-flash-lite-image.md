# Nano Banana 2 Lite Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-3.1-flash-lite-image
- 模型名称：Nano Banana 2 Lite
- 发布日期：2026-06-30
- 最近检查时间：2026-11-05T02:11+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Google API 文档显示 Function calling 与 code execution 不支持，但当前模型 TOML 的 tools.supported=true；此项元数据冲突会影响 agent benchmark 适用性判断，本轮未改动模型能力字段。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/) | 2026-11-05T02:11+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T02:11+08:00 |
| terminal-bench-v4 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://www.tbench.ai/news/terminal-bench-4-0](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-05T02:11+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T02:11+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://zapier.com/benchmarks](https://zapier.com/benchmarks) | 2026-11-05T02:11+08:00 |
| osworld-v2.1 | 待核实 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T02:11+08:00 |
| chartography | 未找到 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T02:11+08:00 |
| humanitys-last-exam | 未找到 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T02:11+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 2026-11-05T02:11+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T02:11+08:00 |
| vals-index-v2.2 | 未找到 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image), [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T02:11+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)

研究备注：
- 目标 API 定位为图像生成/编辑，官方文档未列 coding-agent 或 patch 执行配置；未找到该准确 API ID 的成绩。

最近核验时间：2026-11-05T02:11+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 图像生成/编辑 API 未找到软件仓库修复 agent 配置或该精确 ID 成绩；V2 评测要求 agent 修改并提交代码。

最近核验时间：2026-11-05T02:11+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://www.tbench.ai/news/terminal-bench-4-0](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- 图像生成/编辑模型未找到终端 agent 配置或该精确 API ID 的 v4 成绩；官方文档称 API 不支持 code execution。

最近核验时间：2026-11-05T02:11+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 该模型定位为图像生成/编辑；Terminal-Bench Science 通过 terminal agent 执行科学工作流，未找到该精确 API ID 的测试配置。

最近核验时间：2026-11-05T02:11+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

研究备注：
- Google 文档定位其为图像生成/编辑模型，并注明 Function calling 不支持；仓库当前 tools.supported=true，与官方 API 文档冲突。Zapier 榜单余下 119 条折叠，无法通过榜单排除该模型。

尚未解决的问题：
- 需要先核对 API tool capability 元数据，并进一步确认是否有 1.0.6 的准确模型结果。

最近核验时间：2026-11-05T02:11+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 支持图像输入和文本输出，但 Google 文档称 Function calling 不支持，与本地 tools.supported=true 冲突；没有可靠证据确认该 API 在 v2.1 的桌面动作 wrapper 配置。

尚未解决的问题：
- 适用性依赖未解决的工具调用元数据和 action wrapper；未找到准确成绩。

最近核验时间：2026-11-05T02:11+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型支持图像输入、文本输出，适用于图表问答；当前 Surge 官方榜未检出 Nano Banana 2 Lite 或准确 API model code。未找到准确分数或测试配置。

最近核验时间：2026-11-05T02:11+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- 未找到该精确 API ID 的原始 HLE 公开成绩；不以其他 Gemini 型号或 HLE-Diamond 成绩替代。

最近核验时间：2026-11-05T02:11+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)

研究备注：
- 未找到该精确模型的 V5.0.1 指数总分；不从图像生成相关单项或其他 Gemini 版本推定。

最近核验时间：2026-11-05T02:11+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 未找到准确模型的 GDPval-AA v2.1 成绩。GDPval-AA 通过 Stirrup agent loop 使用 shell/web 产出专业文件；官方文档称 Function calling 不支持，而本地 tools.supported=true，能力信息有冲突。

尚未解决的问题：
- 待解决工具能力元数据矛盾，并确认有无适用的官方 agent 配置或准确成绩。

最近核验时间：2026-11-05T02:11+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image)
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 未找到 Nano Banana 2 Lite 的准确 Vals Index v2.2 成绩；不使用相近 Gemini 或图像模型单项评测替代。

最近核验时间：2026-11-05T02:11+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        }
      ],
      "notes": [
        "未找到该精确模型的 V5.0.1 指数总分；不从图像生成相关单项或其他 Gemini 版本推定。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "Google 文档定位其为图像生成/编辑模型，并注明 Function calling 不支持；仓库当前 tools.supported=true，与官方 API 文档冲突。Zapier 榜单余下 119 条折叠，无法通过榜单排除该模型。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要先核对 API tool capability 元数据，并进一步确认是否有 1.0.6 的准确模型结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型支持图像输入、文本输出，适用于图表问答；当前 Surge 官方榜未检出 Nano Banana 2 Lite 或准确 API model code。未找到准确分数或测试配置。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "目标 API 定位为图像生成/编辑，官方文档未列 coding-agent 或 patch 执行配置；未找到该准确 API ID 的成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "未找到准确模型的 GDPval-AA v2.1 成绩。GDPval-AA 通过 Stirrup agent loop 使用 shell/web 产出专业文件；官方文档称 Function calling 不支持，而本地 tools.supported=true，能力信息有冲突。"
      ],
      "status": "待核实",
      "unresolved": [
        "待解决工具能力元数据矛盾，并确认有无适用的官方 agent 配置或准确成绩。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "未找到该精确 API ID 的原始 HLE 公开成绩；不以其他 Gemini 型号或 HLE-Diamond 成绩替代。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "支持图像输入和文本输出，但 Google 文档称 Function calling 不支持，与本地 tools.supported=true 冲突；没有可靠证据确认该 API 在 v2.1 的桌面动作 wrapper 配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "适用性依赖未解决的工具调用元数据和 action wrapper；未找到准确成绩。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "图像生成/编辑 API 未找到软件仓库修复 agent 配置或该精确 ID 成绩；V2 评测要求 agent 修改并提交代码。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "该模型定位为图像生成/编辑；Terminal-Bench Science 通过 terminal agent 执行科学工作流，未找到该精确 API ID 的测试配置。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "图像生成/编辑模型未找到终端 agent 配置或该精确 API ID 的 v4 成绩；官方文档称 API 不支持 code execution。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:11+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image"
        },
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "未找到 Nano Banana 2 Lite 的准确 Vals Index v2.2 成绩；不使用相近 Gemini 或图像模型单项评测替代。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:11+08:00",
  "model_id": "google/gemini-3.1-flash-lite-image",
  "model_notes": [
    "Google API 文档显示 Function calling 与 code execution 不支持，但当前模型 TOML 的 tools.supported=true；此项元数据冲突会影响 agent benchmark 适用性判断，本轮未改动模型能力字段。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
