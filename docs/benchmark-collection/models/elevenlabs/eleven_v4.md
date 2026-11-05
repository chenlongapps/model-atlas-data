# Eleven v4 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：elevenlabs/eleven_v4
- 模型名称：Eleven v4
- 发布日期：2026-09-28
- 最近检查时间：2026-11-04T06:51+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [DeepSWE official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T06:51+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T06:51+08:00 |
| terminal-bench-v4 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Terminal-Bench run protocol](https://www.tbench.ai/run) | 2026-11-04T06:51+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Terminal-Bench Science benchmark page](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T06:51+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Zapier AutomationBench methodology](https://github.com/zapier/AutomationBench) | 2026-11-04T06:51+08:00 |
| osworld-v2.1 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T06:51+08:00 |
| chartography | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Chartography methodology](https://github.com/surge-ai/chartography) | 2026-11-04T06:51+08:00 |
| humanitys-last-exam | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Humanity’s Last Exam evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T06:51+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T06:51+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [GDPval-AA evaluation page](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T06:51+08:00 |
| vals-index-v2.2 | 不适用 | — | [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Vals Index methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T06:51+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [DeepSWE official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE evaluates long-horizon software-engineering agents that edit repositories and submit verifiable patches. Eleven v4 accepts text and returns audio, with no reasoning or tools.

最近核验时间：2026-11-04T06:51+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro requires a model to produce code patches for repository issues and pass tests; Eleven v4 is a speech synthesizer, not a code-producing agent.

最近核验时间：2026-11-04T06:51+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Terminal-Bench run protocol](https://www.tbench.ai/run)

研究备注：
- Terminal-Bench requires an agent to execute CLI tasks in a sandbox; Eleven v4 has no terminal tools and outputs audio.

最近核验时间：2026-11-04T06:51+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Terminal-Bench Science benchmark page](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science requires agent workflows and verifiable analyses, simulations, proofs, code, or data artifacts; this model only synthesizes speech.

最近核验时间：2026-11-04T06:51+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Zapier AutomationBench methodology](https://github.com/zapier/AutomationBench)

研究备注：
- AutomationBench requires cross-application agent workflows using simulated SaaS tools and final-state assertions; Eleven v4 cannot call tools or return workflow decisions.

最近核验时间：2026-11-04T06:51+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld requires an agent to observe desktop state and execute GUI actions; Eleven v4 has no image input or computer-use action interface.

最近核验时间：2026-11-04T06:51+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Chartography methodology](https://github.com/surge-ai/chartography)

研究备注：
- Chartography requires visual chart reading and text answers; Eleven v4 accepts no image input and returns audio rather than answers.

最近核验时间：2026-11-04T06:51+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Humanity’s Last Exam evaluation page](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Humanity’s Last Exam requires answering academic questions and scoring answer correctness; Eleven v4 synthesizes speech and does not provide text answers or reasoning.

最近核验时间：2026-11-04T06:51+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The Intelligence Index aggregates knowledge-work, coding, science, and reasoning results. A separate Artificial Analysis voice TTS score is not an Intelligence Index V5 score and is not recorded here.

最近核验时间：2026-11-04T06:51+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [GDPval-AA evaluation page](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA requires an agent to use shell/web tools and deliver professional work files; Eleven v4 outputs audio only.

最近核验时间：2026-11-04T06:51+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [ElevenLabs Eleven v4 model card](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)
- [Vals Index methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index aggregates finance, coding, legal, and tax agent-task performance; Eleven v4 is not an agent or reasoning model.

最近核验时间：2026-11-04T06:51+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The Intelligence Index aggregates knowledge-work, coding, science, and reasoning results. A separate Artificial Analysis voice TTS score is not an Intelligence Index V5 score and is not recorded here."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Zapier AutomationBench methodology",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "AutomationBench requires cross-application agent workflows using simulated SaaS tools and final-state assertions; Eleven v4 cannot call tools or return workflow decisions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Chartography methodology",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Chartography requires visual chart reading and text answers; Eleven v4 accepts no image input and returns audio rather than answers."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "DeepSWE official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE evaluates long-horizon software-engineering agents that edit repositories and submit verifiable patches. Eleven v4 accepts text and returns audio, with no reasoning or tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "GDPval-AA evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA requires an agent to use shell/web tools and deliver professional work files; Eleven v4 outputs audio only."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Humanity’s Last Exam evaluation page",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Humanity’s Last Exam requires answering academic questions and scoring answer correctness; Eleven v4 synthesizes speech and does not provide text answers or reasoning."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld requires an agent to observe desktop state and execute GUI actions; Eleven v4 has no image input or computer-use action interface."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro requires a model to produce code patches for repository issues and pass tests; Eleven v4 is a speech synthesizer, not a code-producing agent."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Terminal-Bench Science benchmark page",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science requires agent workflows and verifiable analyses, simulations, proofs, code, or data artifacts; this model only synthesizes speech."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Terminal-Bench run protocol",
          "url": "https://www.tbench.ai/run"
        }
      ],
      "notes": [
        "Terminal-Bench requires an agent to execute CLI tasks in a sandbox; Eleven v4 has no terminal tools and outputs audio."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T06:51+08:00",
      "checked_sources": [
        {
          "label": "ElevenLabs Eleven v4 model card",
          "url": "https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4"
        },
        {
          "label": "Vals Index methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index aggregates finance, coding, legal, and tax agent-task performance; Eleven v4 is not an agent or reasoning model."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T06:51+08:00",
  "model_id": "elevenlabs/eleven_v4",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
