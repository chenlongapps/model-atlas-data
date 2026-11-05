# HeyGen Video Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：heygen/heygen-video-1
- 模型名称：HeyGen Video
- 发布日期：2026-09-30
- 最近检查时间：2026-11-04T05:29+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T05:29+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md) | 2026-11-04T05:29+08:00 |
| terminal-bench-v4 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [Terminal-Bench run guide](https://www.tbench.ai/run) | 2026-11-04T05:29+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T05:29+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [AutomationBench official leaderboard/protocol](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-04T05:29+08:00 |
| osworld-v2.1 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T05:29+08:00 |
| chartography | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper and protocol](https://arxiv.org/html/2608.10677) | 2026-11-04T05:29+08:00 |
| humanitys-last-exam | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [Scale HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam) | 2026-11-04T05:29+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [AA Video Text-to-Video leaderboard](https://artificialanalysis.ai/video/leaderboard/text-to-video?audio-output=false) | 2026-11-04T05:29+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T05:29+08:00 |
| vals-index-v2.2 | 不适用 | — | [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video), [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T05:29+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE 要求提交并验证代码补丁；HeyGen Video 1 生成带音轨的视频，不执行代码任务。没有把底层 MiniMax H3 结果移用。

最近核验时间：2026-11-04T05:29+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [SWE-bench Pro V2 protocol](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)

研究备注：
- SWE-bench Pro V2 要求修改仓库、生成 git diff 并在独立环境验证；HeyGen Video 1 只生成视频，不提供代码 agent 能力。

最近核验时间：2026-11-04T05:29+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [Terminal-Bench run guide](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench 4 需要通过 Harbor 在沙箱终端运行 agent；HeyGen Video 1 是视频生成 API。

最近核验时间：2026-11-04T05:29+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [Terminal-Bench Science 0.1 protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science 要求执行科研终端流程并产出可测试工件；HeyGen Video 1 生成视频，不能执行工具或提交研究产物。

最近核验时间：2026-11-04T05:29+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [AutomationBench official leaderboard/protocol](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench 要求 agent 使用工具完成应用工作流并达到目标状态；HeyGen Video 1 不提供此类工作流操作。

最近核验时间：2026-11-04T05:29+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld 2.1 要求观察桌面界面并执行 GUI 操作；该型号输出视频而非操作，即使参考输入可含图像/视频也不符合操作协议。

最近核验时间：2026-11-04T05:29+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper and protocol](https://arxiv.org/html/2608.10677)

研究备注：
- Chartography 要求读取图表图像并用自由文本回答；HeyGen Video 1 生成视频，不能输出答案文本。

最近核验时间：2026-11-04T05:29+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [Scale HLE official leaderboard and methodology](https://labs.scale.com/leaderboard/humanitys_last_exam)

研究备注：
- 完整 HLE 在 2,500 道公开题上评估最终答案 accuracy；HeyGen Video 1 输出视频而非题目答案。没有将底层 MiniMax H3 成绩映射到 HeyGen Video 1。

最近核验时间：2026-11-04T05:29+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [AA Video Text-to-Video leaderboard](https://artificialanalysis.ai/video/leaderboard/text-to-video?audio-output=false)

研究备注：
- Intelligence Index V5 综合知识工作、编码、科学和通识任务；视频生成接口不适用。AA Video T2V 是另一项榜单（HeyGen Video 1 的视频偏好分），不是 Intelligence Index V5，且配置标签未完全明确，因此不写入本 Benchmark。

最近核验时间：2026-11-04T05:29+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [GDPval-AA methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA V2.1 要求 agent 使用 shell/web 并交付专业文档、幻灯片、图表等工作成果；视频生成 API 无法完成此协议。

最近核验时间：2026-11-04T05:29+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [HeyGen Video official model documentation](https://developers.heygen.com/docs/models/heygen-video)
- [Vals Index V2.2 official methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index V2.2 衡量 finance、coding、legal、tax 的 agentic 工作；HeyGen Video 1 没有工具执行接口且只输出视频。

最近核验时间：2026-11-04T05:29+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "AA Video Text-to-Video leaderboard",
          "url": "https://artificialanalysis.ai/video/leaderboard/text-to-video?audio-output=false"
        }
      ],
      "notes": [
        "Intelligence Index V5 综合知识工作、编码、科学和通识任务；视频生成接口不适用。AA Video T2V 是另一项榜单（HeyGen Video 1 的视频偏好分），不是 Intelligence Index V5，且配置标签未完全明确，因此不写入本 Benchmark。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "AutomationBench official leaderboard/protocol",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench 要求 agent 使用工具完成应用工作流并达到目标状态；HeyGen Video 1 不提供此类工作流操作。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper and protocol",
          "url": "https://arxiv.org/html/2608.10677"
        }
      ],
      "notes": [
        "Chartography 要求读取图表图像并用自由文本回答；HeyGen Video 1 生成视频，不能输出答案文本。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE 要求提交并验证代码补丁；HeyGen Video 1 生成带音轨的视频，不执行代码任务。没有把底层 MiniMax H3 结果移用。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA V2.1 要求 agent 使用 shell/web 并交付专业文档、幻灯片、图表等工作成果；视频生成 API 无法完成此协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "Scale HLE official leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        }
      ],
      "notes": [
        "完整 HLE 在 2,500 道公开题上评估最终答案 accuracy；HeyGen Video 1 输出视频而非题目答案。没有将底层 MiniMax H3 成绩映射到 HeyGen Video 1。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "OSWorld V2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld 2.1 要求观察桌面界面并执行 GUI 操作；该型号输出视频而非操作，即使参考输入可含图像/视频也不符合操作协议。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "SWE-bench Pro V2 protocol",
          "url": "https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 要求修改仓库、生成 git diff 并在独立环境验证；HeyGen Video 1 只生成视频，不提供代码 agent 能力。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "Terminal-Bench Science 0.1 protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science 要求执行科研终端流程并产出可测试工件；HeyGen Video 1 生成视频，不能执行工具或提交研究产物。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "Terminal-Bench run guide",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench 4 需要通过 Harbor 在沙箱终端运行 agent；HeyGen Video 1 是视频生成 API。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T05:29+08:00",
      "checked_sources": [
        {
          "label": "HeyGen Video official model documentation",
          "url": "https://developers.heygen.com/docs/models/heygen-video"
        },
        {
          "label": "Vals Index V2.2 official methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index V2.2 衡量 finance、coding、legal、tax 的 agentic 工作；HeyGen Video 1 没有工具执行接口且只输出视频。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T05:29+08:00",
  "model_id": "heygen/heygen-video-1",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
