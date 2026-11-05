# Gemini Omni Flash Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：google/gemini-omni-flash-preview
- 模型名称：Gemini Omni Flash Preview
- 发布日期：2026-06-30
- 最近检查时间：2026-11-05T02:12+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：1
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 视频生成/编辑模型，API 输出仅 video/mp4，tools 不支持；与本轮 11 项文本作答、终端 agent、桌面操作或文件产出 Benchmark 协议不匹配。当前只有一条 LMArena Text-to-Video Arena 记录，和本轮目标无关。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| terminal-bench-v4 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| osworld-v2.1 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| chartography | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| humanitys-last-exam | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |
| vals-index-v2.2 | 不适用 | — | [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash), [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | 2026-11-05T02:12+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)
- [https://ai.google.dev/gemini-api/docs/deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

研究备注：
- 本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。

最近核验时间：2026-11-05T02:12+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T02:12+08:00",
      "checked_sources": [
        {
          "url": "https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash"
        },
        {
          "url": "https://ai.google.dev/gemini-api/docs/deprecations"
        }
      ],
      "notes": [
        "本地模型资料标注输入文本/图像/视频、输出 video/mp4，且不支持 tools；Google 当前 Omni 文档明确 gemini-omni-flash-preview 已 shut down，稳定版为 gemini-omni-1.1-flash。未将稳定版成绩迁移到 preview。"
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 1,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T02:12+08:00",
  "model_id": "google/gemini-omni-flash-preview",
  "model_notes": [
    "视频生成/编辑模型，API 输出仅 video/mp4，tools 不支持；与本轮 11 项文本作答、终端 agent、桌面操作或文件产出 Benchmark 协议不匹配。当前只有一条 LMArena Text-to-Video Arena 记录，和本轮目标无关。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
