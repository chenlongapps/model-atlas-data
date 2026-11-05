# Mistral OCR 4.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：mistral/mistral-ocr-4-1
- 模型名称：Mistral OCR 4.1
- 发布日期：2026-07-16
- 最近检查时间：2026-11-04T23:35+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- Mistral 官方模型页将 OCR 4.1（API ID mistral-ocr-4-1）定位为 2026-07-16 发布的 Document AI OCR 服务，提供文本/结构提取、段落级边界框和置信度。
- 本轮 11 项均要求软件工程/终端执行、应用或桌面智能体，或通用问答、推理和专业工作输出；与 OCR 4.1 当前官方接口能力不匹配，均标记为不适用。未找到可归属该模型的精确成绩，未借用其他 Mistral 模型成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T23:35+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Scale AI SWE-bench Pro V2 leaderboard and methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:35+08:00 |
| terminal-bench-v4 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Terminal-Bench 4.0 release and version notes](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T23:35+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Terminal-Bench-Science 0.1 official methodology and results](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T23:35+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Zapier AutomationBench leaderboard and methodology](https://zapier.com/benchmarks) | 2026-11-04T23:35+08:00 |
| osworld-v2.1 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [OSWorld-V2 repository and v2.1 release](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T23:35+08:00 |
| chartography | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T23:35+08:00 |
| humanitys-last-exam | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Humanity’s Last Exam paper and benchmark definition](https://arxiv.org/abs/2501.14249) | 2026-11-04T23:35+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Artificial Analysis Intelligence Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T23:35+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T23:35+08:00 |
| vals-index-v2.2 | 不适用 | — | [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1), [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr), [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T23:35+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE v1.1 evaluates long-horizon software engineering agents on repository tasks. OCR 4.1 is a document OCR service that extracts text and structure; it does not generate and submit software patches, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard.

最近核验时间：2026-11-04T23:35+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Scale AI SWE-bench Pro V2 leaderboard and methodology](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 requires an agent to modify a codebase and submit a patch that passes hidden tests. OCR 4.1 exposes document extraction, not code editing or patch submission, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard.

最近核验时间：2026-11-04T23:35+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Terminal-Bench 4.0 release and version notes](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4.0 evaluates agents that execute tasks in a sandboxed terminal. OCR 4.1 is a document OCR endpoint with no terminal or agent execution interface, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard.

最近核验时间：2026-11-04T23:35+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Terminal-Bench-Science 0.1 official methodology and results](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench-Science 0.1 evaluates agents executing scientific research workflows and producing tested artifacts such as analyses, simulations, proofs, and code. OCR 4.1 only extracts document content, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard.

最近核验时间：2026-11-04T23:35+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Zapier AutomationBench leaderboard and methodology](https://zapier.com/benchmarks)

研究备注：
- AutomationBench evaluates agents completing cross-application workflows in simulated business apps and checks final environment state. OCR 4.1 extracts document text and layout but cannot execute tools or workflows, so this benchmark is not applicable. No OCR 4.1 result was found on Zapier’s official page.

最近核验时间：2026-11-04T23:35+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [OSWorld-V2 repository and v2.1 release](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 evaluates long-horizon computer-use agents operating real desktop applications. OCR 4.1 does not expose GUI actions, planning, or task execution, so this benchmark is not applicable. No OCR 4.1 result was found in the official OSWorld materials.

最近核验时间：2026-11-04T23:35+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Surge Chartography benchmark](https://surgehq.ai/benchmarks/chartography)

研究备注：
- Chartography evaluates visual chart reading, domain interpretation, and multi-step reasoning. OCR 4.1 extracts document text and structure but does not answer chart questions or provide the required general visual reasoning, so this benchmark is not applicable. No OCR 4.1 result was found on Surge’s official benchmark page.

最近核验时间：2026-11-04T23:35+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Humanity’s Last Exam paper and benchmark definition](https://arxiv.org/abs/2501.14249)

研究备注：
- Humanity’s Last Exam requires closed-ended academic question answering and reasoning; its multimodal subset can include images. OCR 4.1 accepts images but is an OCR extraction service rather than a question-answering model, so this benchmark is not applicable. No exact OCR 4.1 result was found in the benchmark materials.

最近核验时间：2026-11-04T23:35+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Artificial Analysis Intelligence Index evaluation](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Artificial Analysis Intelligence Index V5 aggregates broad language-model capabilities across knowledge work, coding, science, and general knowledge. OCR 4.1 is a specialized document extraction service, not a general language model for the evaluated tasks, so this benchmark is not applicable. No exact OCR 4.1 entry was found.

最近核验时间：2026-11-04T23:35+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Artificial Analysis GDPval-AA evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA evaluates models producing professional work outputs in an agentic setting with an Elo-based comparison. OCR 4.1 only extracts document content and cannot complete the evaluated professional tasks, so this benchmark is not applicable. No exact OCR 4.1 result was found.

最近核验时间：2026-11-04T23:35+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Mistral OCR 4.1 official model page](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral OCR Processor documentation](https://docs.mistral.ai/studio/document-processing/basic_ocr)
- [Vals Index v2.2 leaderboard and methodology](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index v2.2 measures agent performance on finance, coding, legal, and tax tasks. OCR 4.1 is a document OCR processor without agent task execution or general reasoning, so this benchmark is not applicable. The official leaderboard lists evaluated agents/models but no Mistral OCR 4.1 result.

最近核验时间：2026-11-04T23:35+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Artificial Analysis Intelligence Index evaluation",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Artificial Analysis Intelligence Index V5 aggregates broad language-model capabilities across knowledge work, coding, science, and general knowledge. OCR 4.1 is a specialized document extraction service, not a general language model for the evaluated tasks, so this benchmark is not applicable. No exact OCR 4.1 entry was found."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Zapier AutomationBench leaderboard and methodology",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench evaluates agents completing cross-application workflows in simulated business apps and checks final environment state. OCR 4.1 extracts document text and layout but cannot execute tools or workflows, so this benchmark is not applicable. No OCR 4.1 result was found on Zapier’s official page."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Surge Chartography benchmark",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "Chartography evaluates visual chart reading, domain interpretation, and multi-step reasoning. OCR 4.1 extracts document text and structure but does not answer chart questions or provide the required general visual reasoning, so this benchmark is not applicable. No OCR 4.1 result was found on Surge’s official benchmark page."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE v1.1 evaluates long-horizon software engineering agents on repository tasks. OCR 4.1 is a document OCR service that extracts text and structure; it does not generate and submit software patches, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Artificial Analysis GDPval-AA evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA evaluates models producing professional work outputs in an agentic setting with an Elo-based comparison. OCR 4.1 only extracts document content and cannot complete the evaluated professional tasks, so this benchmark is not applicable. No exact OCR 4.1 result was found."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Humanity’s Last Exam paper and benchmark definition",
          "url": "https://arxiv.org/abs/2501.14249"
        }
      ],
      "notes": [
        "Humanity’s Last Exam requires closed-ended academic question answering and reasoning; its multimodal subset can include images. OCR 4.1 accepts images but is an OCR extraction service rather than a question-answering model, so this benchmark is not applicable. No exact OCR 4.1 result was found in the benchmark materials."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "OSWorld-V2 repository and v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 evaluates long-horizon computer-use agents operating real desktop applications. OCR 4.1 does not expose GUI actions, planning, or task execution, so this benchmark is not applicable. No OCR 4.1 result was found in the official OSWorld materials."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard and methodology",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires an agent to modify a codebase and submit a patch that passes hidden tests. OCR 4.1 exposes document extraction, not code editing or patch submission, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Terminal-Bench-Science 0.1 official methodology and results",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench-Science 0.1 evaluates agents executing scientific research workflows and producing tested artifacts such as analyses, simulations, proofs, and code. OCR 4.1 only extracts document content, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Terminal-Bench 4.0 release and version notes",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4.0 evaluates agents that execute tasks in a sandboxed terminal. OCR 4.1 is a document OCR endpoint with no terminal or agent execution interface, so this benchmark is not applicable. No OCR 4.1 result was found on the official leaderboard."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:35+08:00",
      "checked_sources": [
        {
          "label": "Mistral OCR 4.1 official model page",
          "url": "https://docs.mistral.ai/models/ocr-4-1"
        },
        {
          "label": "Mistral OCR Processor documentation",
          "url": "https://docs.mistral.ai/studio/document-processing/basic_ocr"
        },
        {
          "label": "Vals Index v2.2 leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index v2.2 measures agent performance on finance, coding, legal, and tax tasks. OCR 4.1 is a document OCR processor without agent task execution or general reasoning, so this benchmark is not applicable. The official leaderboard lists evaluated agents/models but no Mistral OCR 4.1 result."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:35+08:00",
  "model_id": "mistral/mistral-ocr-4-1",
  "model_notes": [
    "Mistral 官方模型页将 OCR 4.1（API ID mistral-ocr-4-1）定位为 2026-07-16 发布的 Document AI OCR 服务，提供文本/结构提取、段落级边界框和置信度。",
    "本轮 11 项均要求软件工程/终端执行、应用或桌面智能体，或通用问答、推理和专业工作输出；与 OCR 4.1 当前官方接口能力不匹配，均标记为不适用。未找到可归属该模型的精确成绩，未借用其他 Mistral 模型成绩。"
  ],
  "new_records": 0,
  "overall_status": "已完成",
  "updated_records": 0
}

-->
