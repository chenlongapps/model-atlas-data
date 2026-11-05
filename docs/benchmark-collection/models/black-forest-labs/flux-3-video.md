# FLUX 3 Video Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：black-forest-labs/flux-3-video
- 模型名称：FLUX 3 Video
- 发布日期：2026-08-04
- 最近检查时间：2026-11-04T20:23+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Black Forest Labs 于 2026-08-04 发布 FLUX 3 Video；本地模型文件将其定义为文本、图像和视频输入，video/mp4 输出，且 tools/reasoning 均不支持。
- BFL 另提供 MCP Server 和 Agent Skills 用于外部代理调用视频生成服务；这些集成不改变本地模型定义的输出模态与工具能力。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/), [DeepSWE v1.1 官方方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T20:23+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [SWE-bench Pro 官方方法与实现](https://github.com/scaleapi/SWE-bench_Pro-os) | 2026-11-04T20:23+08:00 |
| terminal-bench-v4 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4), [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T20:23+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement), [Harbor Terminal-Bench-Science v0.1 官方排行榜](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard) | 2026-11-04T20:23+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Zapier AutomationBench 1.0.6 官方排行榜与方法](https://zapier.com/benchmarks), [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench) | 2026-11-04T20:23+08:00 |
| osworld-v2.1 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [OSWorld-V2 官方仓库与 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2), [OSWorld v2.1 官方发布清单](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json) | 2026-11-04T20:23+08:00 |
| chartography | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography), [Chartography 官方任务与评分实现](https://github.com/surge-ai/chartography) | 2026-11-04T20:23+08:00 |
| humanitys-last-exam | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Scale AI Humanity’s Last Exam 官方排行榜与方法](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T20:23+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Artificial Analysis Intelligence Index v5.0.1 官方评测](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T20:23+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Artificial Analysis GDPval-AA v2.1 官方评测与方法](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T20:23+08:00 |
| vals-index-v2.2 | 不适用 | — | [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes), [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview), [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3), [Vals Index v2.2 官方排行榜与方法](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T20:23+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [DeepSWE v1.1 官方排行榜](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 官方方法](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 评测长程软件工程任务，要求 Agent 提交可验证的代码补丁；FLUX 3 Video 输出 video/mp4，不提供代码文本或工具调用。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Scale AI SWE-bench Pro V2 官方排行榜](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [SWE-bench Pro 官方方法与实现](https://github.com/scaleapi/SWE-bench_Pro-os)

研究备注：
- SWE-bench Pro V2 要求 coding Agent 修改真实代码库并提交通过隐藏测试的补丁；视频生成接口无法产出可评分代码修改。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Terminal-Bench 4.0 官方排行榜](https://www.tbench.ai/?version=4)
- [Terminal-Bench 4.0 官方方法](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 要求 Agent 在沙箱终端执行任务并通过验证；FLUX 3 Video 不输出命令或代码，也不支持工具调用。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Terminal-Bench-Science 官方公告](https://www.terminal-bench-science.ai/announcement)
- [Harbor Terminal-Bench-Science v0.1 官方排行榜](https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard)

研究备注：
- Terminal-Bench-Science 要求 Agent 通过终端完成科学研究工作流，并提交代码、分析或模拟等可验证产物；MP4 输出不适配任务接口。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Zapier AutomationBench 1.0.6 官方排行榜与方法](https://zapier.com/benchmarks)
- [AutomationBench 官方仓库](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 1.0.6 要求 Agent 调用工具完成跨应用工作流，并按环境最终状态评分；FLUX 3 Video 是视频生成接口，不支持工具或环境操作。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [OSWorld-V2 官方仓库与 v2.1 说明](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld v2.1 官方发布清单](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)

研究备注：
- OSWorld v2.1 评测 Agent 在桌面环境中执行 GUI 工作流；FLUX 3 Video 不能执行电脑操作，且只输出视频。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Surge Chartography 官方排行榜](https://surgehq.ai/benchmarks/chartography)
- [Chartography 官方任务与评分实现](https://github.com/surge-ai/chartography)

研究备注：
- Chartography 虽以图像图表为输入，但要求返回可评分文字答案；FLUX 3 Video 输出 video/mp4，无法提交问答结果。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Scale AI Humanity’s Last Exam 官方排行榜与方法](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- Humanity’s Last Exam 要求模型返回可评分的最终文字答案与置信度；FLUX 3 Video 只生成视频，无法回答闭式问答。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Artificial Analysis Intelligence Index v5.0.1 官方评测](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Intelligence Index 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis Intelligence Index v5 汇总知识、编码、科学及 Agent 评测；模型输出的视频不能作为这些评测的文字答案或工作产物。未找到该精确型号 v5 成绩。

最近核验时间：2026-11-04T20:23+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Artificial Analysis GDPval-AA v2.1 官方评测与方法](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA 方法](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- GDPval-AA v2.1 使用 Stirrup、shell 与网页浏览工具完成职业工作任务，并要求文档、幻灯片、图表或表格等交付物；FLUX 3 Video 不支持工具，输出为视频。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Black Forest Labs FLUX 3 官方发布说明](https://docs.bfl.ml/release-notes)
- [Black Forest Labs FLUX 3 Video 概览](https://docs.bfl.ml/flux_3/flux3_overview)
- [Black Forest Labs FLUX 3 Video 官方 API 参考](https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3)
- [Vals Index v2.2 官方排行榜与方法](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 汇总金融、编码、法律和税务 Agent 任务，需要文字研究、代码、终端或业务工作流产物；视频生成输出不匹配这些任务。未找到该精确型号公开成绩。

最近核验时间：2026-11-04T20:23+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5.0.1 官方评测",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Intelligence Index 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index v5 汇总知识、编码、科学及 Agent 评测；模型输出的视频不能作为这些评测的文字答案或工作产物。未找到该精确型号 v5 成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Zapier AutomationBench 1.0.6 官方排行榜与方法",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench 官方仓库",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 1.0.6 要求 Agent 调用工具完成跨应用工作流，并按环境最终状态评分；FLUX 3 Video 是视频生成接口，不支持工具或环境操作。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Surge Chartography 官方排行榜",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography 官方任务与评分实现",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography 虽以图像图表为输入，但要求返回可评分文字答案；FLUX 3 Video 输出 video/mp4，无法提交问答结果。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "DeepSWE v1.1 官方排行榜",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 官方方法",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 评测长程软件工程任务，要求 Agent 提交可验证的代码补丁；FLUX 3 Video 输出 video/mp4，不提供代码文本或工具调用。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 官方评测与方法",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA 方法",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 使用 Stirrup、shell 与网页浏览工具完成职业工作任务，并要求文档、幻灯片、图表或表格等交付物；FLUX 3 Video 不支持工具，输出为视频。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Scale AI Humanity’s Last Exam 官方排行榜与方法",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "Humanity’s Last Exam 要求模型返回可评分的最终文字答案与置信度；FLUX 3 Video 只生成视频，无法回答闭式问答。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "OSWorld-V2 官方仓库与 v2.1 说明",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld v2.1 官方发布清单",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        }
      ],
      "notes": [
        "OSWorld v2.1 评测 Agent 在桌面环境中执行 GUI 工作流；FLUX 3 Video 不能执行电脑操作，且只输出视频。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 官方排行榜",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "SWE-bench Pro 官方方法与实现",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求 coding Agent 修改真实代码库并提交通过隐藏测试的补丁；视频生成接口无法产出可评分代码修改。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Terminal-Bench-Science 官方公告",
          "url": "https://www.terminal-bench-science.ai/announcement"
        },
        {
          "label": "Harbor Terminal-Bench-Science v0.1 官方排行榜",
          "url": "https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?leaderboard=v0-1-eval&tab=leaderboard"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 要求 Agent 通过终端完成科学研究工作流，并提交代码、分析或模拟等可验证产物；MP4 输出不适配任务接口。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Terminal-Bench 4.0 官方排行榜",
          "url": "https://www.tbench.ai/?version=4"
        },
        {
          "label": "Terminal-Bench 4.0 官方方法",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 要求 Agent 在沙箱终端执行任务并通过验证；FLUX 3 Video 不输出命令或代码，也不支持工具调用。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T20:23+08:00",
      "checked_sources": [
        {
          "label": "Black Forest Labs FLUX 3 官方发布说明",
          "url": "https://docs.bfl.ml/release-notes"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 概览",
          "url": "https://docs.bfl.ml/flux_3/flux3_overview"
        },
        {
          "label": "Black Forest Labs FLUX 3 Video 官方 API 参考",
          "url": "https://docs.bfl.ml/api-reference/utility/generate-a-video-with-flux-3"
        },
        {
          "label": "Vals Index v2.2 官方排行榜与方法",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 汇总金融、编码、法律和税务 Agent 任务，需要文字研究、代码、终端或业务工作流产物；视频生成输出不匹配这些任务。未找到该精确型号公开成绩。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T20:23+08:00",
  "model_id": "black-forest-labs/flux-3-video",
  "model_notes": [
    "Black Forest Labs 于 2026-08-04 发布 FLUX 3 Video；本地模型文件将其定义为文本、图像和视频输入，video/mp4 输出，且 tools/reasoning 均不支持。",
    "BFL 另提供 MCP Server 和 Agent Skills 用于外部代理调用视频生成服务；这些集成不改变本地模型定义的输出模态与工具能力。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
