# Phocinae Largha 150M v1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：phocinae/phocinae-largha-150m-v1
- 模型名称：Phocinae Largha 150M v1
- 发布日期：2026-10-08
- 最近检查时间：2026-11-04T03:33+08:00
- 整体处理状态：已完成
- 新增成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T03:33+08:00 |
| swe-bench-pro-v2 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Scale AI SWE-bench Pro V2 leaderboard and protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T03:33+08:00 |
| terminal-bench-v4 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Terminal-Bench 4.0 official protocol](https://www.tbench.ai/news/terminal-bench-4-0) | 2026-11-04T03:33+08:00 |
| terminal-bench-science-v0.1 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Terminal-Bench Science 0.1 official protocol](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-04T03:33+08:00 |
| automationbench-v1.0.6 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks) | 2026-11-04T03:33+08:00 |
| osworld-v2.1 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T03:33+08:00 |
| chartography | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Chartography official paper](https://arxiv.org/html/2608.10677v1) | 2026-11-04T03:33+08:00 |
| humanitys-last-exam | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Scale original Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam), [Humanity’s Last Exam official paper](https://arxiv.org/html/2501.14249v12) | 2026-11-04T03:33+08:00 |
| artificial-analysis-intelligence-index-v5 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T03:33+08:00 |
| gdpval-aa-v2.1 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Artificial Analysis GDPval-AA v2.1 protocol](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T03:33+08:00 |
| vals-index-v2.2 | 不适用 | — | [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1), [Vals Index V2.2 methodology and leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T03:33+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- DeepSWE requires an agent to generate and submit a code patch for isolated verification. This model emits zero output tokens and only returns typed boolean, choice-index, or integer-score decisions. The card history records a later v1.1 weight update on 2026-10-09; no score from its separate typed-decisions evaluation is used here.

最近核验时间：2026-11-04T03:33+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Scale AI SWE-bench Pro V2 leaderboard and protocol](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- SWE-bench Pro V2 requires a repository code diff that can be applied and tested. The decision-only API cannot produce arbitrary code output.

最近核验时间：2026-11-04T03:33+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Terminal-Bench 4.0 official protocol](https://www.tbench.ai/news/terminal-bench-4-0)

研究备注：
- Terminal-Bench 4 requires an agent to execute open-ended terminal tasks. The model returns typed decisions and cannot generate shell commands or terminal artifacts.

最近核验时间：2026-11-04T03:33+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Terminal-Bench Science 0.1 official protocol](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- Terminal-Bench Science requires terminal research workflows and testable analyses, simulations, proofs, code, or data artifacts. The model has no free-form text or artifact output.

最近核验时间：2026-11-04T03:33+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Zapier AutomationBench leaderboard and protocol](https://zapier.com/benchmarks)

研究备注：
- AutomationBench requires agents to execute end-to-end workflows through application tools and scores final environment state. This model is a typed-decision encoder with no tool interface or workflow output.

最近核验时间：2026-11-04T03:33+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- OSWorld v2.1 requires an agent to observe screenshots and return GUI actions. This model accepts text only and returns typed decisions, not image-conditioned GUI actions.

最近核验时间：2026-11-04T03:33+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Chartography official paper](https://arxiv.org/html/2608.10677v1)

研究备注：
- Chartography requires chart-image input and free-form text answers. The model has neither image input nor free-form text generation.

最近核验时间：2026-11-04T03:33+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Scale original Humanity’s Last Exam leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam)
- [Humanity’s Last Exam official paper](https://arxiv.org/html/2501.14249v12)

研究备注：
- The original HLE contains multiple-choice and exact-match answer questions; the official paper describes only 24% as multiple choice. This model can emit a closed-set choice but cannot generate the exact answer strings required by the full 2,500-question benchmark. Its typed-decisions and JevBench card scores are different evaluations.

最近核验时间：2026-11-04T03:33+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Artificial Analysis Intelligence Index V5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- The V5.0 composite spans knowledge work, coding, science, and general knowledge and includes open-answer and work-product tasks. A zero-token typed-decision encoder cannot satisfy the complete index protocol; HLE-Diamond within V5 is distinct from original HLE.

最近核验时间：2026-11-04T03:33+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Artificial Analysis GDPval-AA v2.1 protocol](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- GDPval-AA v2.1 requires a shell/web agent loop and professional deliverables such as documents, slides, diagrams, and spreadsheets. The model cannot generate these artifacts or execute tools.

最近核验时间：2026-11-04T03:33+08:00

### Vals Index (vals-index-v2.2)

- 结论：不适用。

已检查的主要资料：
- [Phocinae Largha 150M v1 official model card](https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1)
- [Vals Index V2.2 methodology and leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- Vals Index measures agentic finance, coding, legal, and tax work. A closed-set decision output cannot produce the required work products or use tools.

最近核验时间：2026-11-04T03:33+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Artificial Analysis Intelligence Index V5 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "The V5.0 composite spans knowledge work, coding, science, and general knowledge and includes open-answer and work-product tasks. A zero-token typed-decision encoder cannot satisfy the complete index protocol; HLE-Diamond within V5 is distinct from original HLE."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Zapier AutomationBench leaderboard and protocol",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "AutomationBench requires agents to execute end-to-end workflows through application tools and scores final environment state. This model is a typed-decision encoder with no tool interface or workflow output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Chartography official paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        }
      ],
      "notes": [
        "Chartography requires chart-image input and free-form text answers. The model has neither image input nor free-form text generation."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "DeepSWE requires an agent to generate and submit a code patch for isolated verification. This model emits zero output tokens and only returns typed boolean, choice-index, or integer-score decisions. The card history records a later v1.1 weight update on 2026-10-09; no score from its separate typed-decisions evaluation is used here."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 protocol",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "GDPval-AA v2.1 requires a shell/web agent loop and professional deliverables such as documents, slides, diagrams, and spreadsheets. The model cannot generate these artifacts or execute tools."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Scale original Humanity’s Last Exam leaderboard",
          "url": "https://labs.scale.com/leaderboard/humanitys_last_exam"
        },
        {
          "label": "Humanity’s Last Exam official paper",
          "url": "https://arxiv.org/html/2501.14249v12"
        }
      ],
      "notes": [
        "The original HLE contains multiple-choice and exact-match answer questions; the official paper describes only 24% as multiple choice. This model can emit a closed-set choice but cannot generate the exact answer strings required by the full 2,500-question benchmark. Its typed-decisions and JevBench card scores are different evaluations."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "OSWorld v2.1 requires an agent to observe screenshots and return GUI actions. This model accepts text only and returns typed decisions, not image-conditioned GUI actions."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Scale AI SWE-bench Pro V2 leaderboard and protocol",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "SWE-bench Pro V2 requires a repository code diff that can be applied and tested. The decision-only API cannot produce arbitrary code output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Terminal-Bench Science 0.1 official protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "Terminal-Bench Science requires terminal research workflows and testable analyses, simulations, proofs, code, or data artifacts. The model has no free-form text or artifact output."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Terminal-Bench 4.0 official protocol",
          "url": "https://www.tbench.ai/news/terminal-bench-4-0"
        }
      ],
      "notes": [
        "Terminal-Bench 4 requires an agent to execute open-ended terminal tasks. The model returns typed decisions and cannot generate shell commands or terminal artifacts."
      ],
      "status": "不适用",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T03:33+08:00",
      "checked_sources": [
        {
          "label": "Phocinae Largha 150M v1 official model card",
          "url": "https://huggingface.co/Phocinae/Phocinae-Largha-150M-v1"
        },
        {
          "label": "Vals Index V2.2 methodology and leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "Vals Index measures agentic finance, coding, legal, and tax work. A closed-set decision output cannot produce the required work products or use tools."
      ],
      "status": "不适用",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T03:33+08:00",
  "model_id": "phocinae/phocinae-largha-150m-v1",
  "new_records": 0,
  "overall_status": "已完成"
}

-->
