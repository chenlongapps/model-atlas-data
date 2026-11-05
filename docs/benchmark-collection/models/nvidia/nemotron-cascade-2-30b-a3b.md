# Nemotron Cascade 2 30B A3B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-cascade-2-30b-a3b
- 模型名称：Nemotron Cascade 2 30B A3B
- 发布日期：2026-03-19
- 最近检查时间：2026-11-05T10:51+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：1

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/) | 2026-11-05T10:51+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-05T10:51+08:00 |
| terminal-bench-v4 | 待核实 | — | [https://www.tbench.ai/](https://www.tbench.ai/) | 2026-11-05T10:51+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T10:51+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [https://zapier.com/benchmarks](https://zapier.com/benchmarks) | 2026-11-05T10:51+08:00 |
| osworld-v2.1 | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B), [https://github.com/xlang-ai/OSWorld-V2](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-05T10:51+08:00 |
| chartography | 不适用 | — | [https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B), [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography) | 2026-11-05T10:51+08:00 |
| humanitys-last-exam | 已收录 | 17.7 (metric=accuracy; dataset=HLE text-only split (2,158 examples); variant=no tool; thinking mode; 128K-token thinking budget; harness=default system prompt with boxed-answer instruction; GPT-OSS-120B for answer extraction and correctness verification) | [https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B), [https://arxiv.org/html/2603.19220](https://arxiv.org/html/2603.19220), [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T10:51+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [https://artificialanalysis.ai/models/nemotron-cascade-2-30b-a3b](https://artificialanalysis.ai/models/nemotron-cascade-2-30b-a3b) | 2026-11-05T10:51+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-05T10:51+08:00 |
| vals-index-v2.2 | 待核实 | — | [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index) | 2026-11-05T10:51+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://deepswe.datacurve.ai/](https://deepswe.datacurve.ai/)

研究备注：
- 已检查目标榜单，但未确认此精确模型的 v1.1 记录；其他 SWE 任务成绩不可替代。

尚未解决的问题：
- 已检查目标榜单，但未确认此精确模型的 v1.1 记录；其他 SWE 任务成绩不可替代。

最近核验时间：2026-11-05T10:51+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- 已检查目标数据集/排行榜资料，但现有可见成绩未能核实为该模型的 Pro V2 评测；不沿用 SWE-bench Verified 成绩。

尚未解决的问题：
- 已检查目标数据集/排行榜资料，但现有可见成绩未能核实为该模型的 Pro V2 评测；不沿用 SWE-bench Verified 成绩。

最近核验时间：2026-11-05T10:51+08:00

### Terminal-Bench (terminal-bench-v4)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.tbench.ai/](https://www.tbench.ai/)

研究备注：
- 模型资料中出现的 Terminal-Bench 2.0 成绩不属于 V4，未映射为目标成绩；仍需核实 V4 榜单。

尚未解决的问题：
- 模型资料中出现的 Terminal-Bench 2.0 成绩不属于 V4，未映射为目标成绩；仍需核实 V4 榜单。

最近核验时间：2026-11-05T10:51+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.tbench.ai/news/terminal-bench-science-0-1](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 未确认准确型号的 Science v0.1 成绩；未从 Terminal-Bench 通用版推断。

尚未解决的问题：
- 未确认准确型号的 Science v0.1 成绩；未从 Terminal-Bench 通用版推断。

最近核验时间：2026-11-05T10:51+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [https://zapier.com/benchmarks](https://zapier.com/benchmarks)

研究备注：
- 未能确认该精确型号在 v1.0.6 榜单中的成绩；保留复核状态。

尚未解决的问题：
- 未能确认该精确型号在 v1.0.6 榜单中的成绩；保留复核状态。

最近核验时间：2026-11-05T10:51+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)
- [https://github.com/xlang-ai/OSWorld-V2](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- 模型卡记录仅支持文本输入，无法接收桌面截图；不适用于视觉桌面操作评测。

最近核验时间：2026-11-05T10:51+08:00

### Chartography (chartography)

- 结论：不适用。

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)
- [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)

研究备注：
- 模型卡记录仅支持文本输入，无法接收图表图像；不适用于图表理解评测。

最近核验时间：2026-11-05T10:51+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 17.7
- metric: accuracy
- dataset: HLE text-only split (2,158 examples)
- variant: no tool; thinking mode; 128K-token thinking budget
- harness: default system prompt with boxed-answer instruction; GPT-OSS-120B for answer extraction and correctness verification
- source: [https://arxiv.org/html/2603.19220](https://arxiv.org/html/2603.19220)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)
- [https://arxiv.org/html/2603.19220](https://arxiv.org/html/2603.19220)
- [https://artificialanalysis.ai/evaluations/humanitys-last-exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- NVIDIA 官方模型卡报告 HLE no-tool 17.7。技术报告确认 text-only split（2,158 样本）、thinking 模式和 128K-token thinking budget；temperature 1.0、top-p 0.95，使用默认 system prompt 与 boxed-answer 指令，并由 GPT-OSS-120B 抽取和判分。没有公布评测日期。

最近核验时间：2026-11-05T10:51+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [https://artificialanalysis.ai/models/nemotron-cascade-2-30b-a3b](https://artificialanalysis.ai/models/nemotron-cascade-2-30b-a3b)

研究备注：
- 精确模型页的 Intelligence Index 为 N/A；该页面区分 HLE-Diamond 指数分项与 NVIDIA 报告中的原始 HLE text-only 成绩，不能将 17.7 作为 V5 指数成绩。

最近核验时间：2026-11-05T10:51+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [https://artificialanalysis.ai/evaluations/gdpval-aa](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- 当前榜单展示不完整，未在可读内容中核实该精确模型的 Elo；不能据未显示断言未参测。

尚未解决的问题：
- 当前榜单展示不完整，未在可读内容中核实该精确模型的 Elo；不能据未显示断言未参测。

最近核验时间：2026-11-05T10:51+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- 当前公开榜单仅展示各实验室最佳模型，不能据此确认或否定该精确型号成绩。

尚未解决的问题：
- 当前公开榜单仅展示各实验室最佳模型，不能据此确认或否定该精确型号成绩。

最近核验时间：2026-11-05T10:51+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/models/nemotron-cascade-2-30b-a3b"
        }
      ],
      "notes": [
        "精确模型页的 Intelligence Index 为 N/A；该页面区分 HLE-Diamond 指数分项与 NVIDIA 报告中的原始 HLE text-only 成绩，不能将 17.7 作为 V5 指数成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "未能确认该精确型号在 v1.0.6 榜单中的成绩；保留复核状态。"
      ],
      "status": "待核实",
      "unresolved": [
        "未能确认该精确型号在 v1.0.6 榜单中的成绩；保留复核状态。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B"
        },
        {
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "模型卡记录仅支持文本输入，无法接收图表图像；不适用于图表理解评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "已检查目标榜单，但未确认此精确模型的 v1.1 记录；其他 SWE 任务成绩不可替代。"
      ],
      "status": "待核实",
      "unresolved": [
        "已检查目标榜单，但未确认此精确模型的 v1.1 记录；其他 SWE 任务成绩不可替代。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "当前榜单展示不完整，未在可读内容中核实该精确模型的 Elo；不能据未显示断言未参测。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前榜单展示不完整，未在可读内容中核实该精确模型的 Elo；不能据未显示断言未参测。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B"
        },
        {
          "url": "https://arxiv.org/html/2603.19220"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "NVIDIA 官方模型卡报告 HLE no-tool 17.7。技术报告确认 text-only split（2,158 样本）、thinking 模式和 128K-token thinking budget；temperature 1.0、top-p 0.95，使用默认 system prompt 与 boxed-answer 指令，并由 GPT-OSS-120B 抽取和判分。没有公布评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B"
        },
        {
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "模型卡记录仅支持文本输入，无法接收桌面截图；不适用于视觉桌面操作评测。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "已检查目标数据集/排行榜资料，但现有可见成绩未能核实为该模型的 Pro V2 评测；不沿用 SWE-bench Verified 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "已检查目标数据集/排行榜资料，但现有可见成绩未能核实为该模型的 Pro V2 评测；不沿用 SWE-bench Verified 成绩。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "未确认准确型号的 Science v0.1 成绩；未从 Terminal-Bench 通用版推断。"
      ],
      "status": "待核实",
      "unresolved": [
        "未确认准确型号的 Science v0.1 成绩；未从 Terminal-Bench 通用版推断。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://www.tbench.ai/"
        }
      ],
      "notes": [
        "模型资料中出现的 Terminal-Bench 2.0 成绩不属于 V4，未映射为目标成绩；仍需核实 V4 榜单。"
      ],
      "status": "待核实",
      "unresolved": [
        "模型资料中出现的 Terminal-Bench 2.0 成绩不属于 V4，未映射为目标成绩；仍需核实 V4 榜单。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T10:51+08:00",
      "checked_sources": [
        {
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "当前公开榜单仅展示各实验室最佳模型，不能据此确认或否定该精确型号成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前公开榜单仅展示各实验室最佳模型，不能据此确认或否定该精确型号成绩。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T10:51+08:00",
  "model_id": "nvidia/nemotron-cascade-2-30b-a3b",
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
