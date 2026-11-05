# Qwen3.8 Max Preview Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：alibaba/qwen3.8-max-preview
- 模型名称：Qwen3.8 Max Preview
- 发布日期：2026-07-19
- 最近检查时间：2026-11-04T23:31+08:00
- 整体处理状态：待复核
- 新增成绩数量：0
- 更新成绩数量：0
- 收集前已有成绩数量：15
- 当前已收录的对应成绩数量：0

## 模型身份与范围说明

- 官方资料确认 Qwen3.8 Max Preview 于 2026-07-19 开放；Qwen3.8-Max 正式版于 2026-08-03 发布。阿里 2026-08-04 通知称 Preview 于 8 月 5 日退役，8 月 6 日起 Preview 请求路由到正式版。
- 处理开始时 Preview TOML 含 15 条成绩，全部只引用 2026-08-03 的 GA 发布文章，未标出 Preview 检查点。为避免将正式版成绩归给 Preview，15 条已从本模型文件移除；正式版文件中已有的正式版记录未改动。
- 因 GA 与 Preview 的身份关系及多项源记录的版本/测试配置无法确认，相关目标项保留待核实；未找到直接属于 Preview 的可信成绩。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-04T23:31+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1), [SWE-bench Pro V2 leaderboard and version notes](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-04T23:31+08:00 |
| terminal-bench-v4 | 未找到 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Vals Qwen3.8 Max GA model page](https://www.vals.ai/models/alibaba_qwen3.8-max), [Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1), [Zapier AutomationBench v1.0.6 leaderboard and methodology](https://zapier.com/benchmarks) | 2026-11-04T23:31+08:00 |
| osworld-v2.1 | 未找到 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| chartography | 待核实 | — | [Preview official availability page](https://www.alibabacloud.com/help/en/lingma/qwen3-8-max-preview-limited-time-offer), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper](https://arxiv.org/abs/2608.10677), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| humanitys-last-exam | 待核实 | — | [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Alibaba models](https://artificialanalysis.ai/models/creators/alibaba), [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa), [Qwen3.8-Max GA model comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-o3), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1) | 2026-11-04T23:31+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- 此前 Preview 文件中的 DeepSWE 记录引自 2026-08-03 正式版资料；当前 DeepSWE 榜单显示的是 Qwen3.8-Max，未见 Preview。正式版材料不能证明结果来自 2026-07-19 Preview 检查点，因此相关行已从 Preview TOML 移除。

尚未解决的问题：
- 没有找到直接指向 Preview 端点或检查点的 DeepSWE v1.1 成绩；正式版结果不能据别名迁移反推为 Preview 结果。

最近核验时间：2026-11-04T23:31+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)
- [SWE-bench Pro V2 leaderboard and version notes](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 此前 Preview 文件中的 SWE-bench Pro 记录源自正式版资料，未证明属于 Preview，也未注明本地定义的 V2。Scale 在 2026-09-22 发布刷新后的 V2 split，不能把早期未注明版本的正式版行映射为 Preview 的 V2 成绩；对应行已从 Preview TOML 移除。

尚未解决的问题：
- 未找到 Preview 的 SWE-bench Pro V2 结果；GA 资料没有证明 Preview 身份或 V2 数据版本。

最近核验时间：2026-11-04T23:31+08:00

### Terminal-Bench (terminal-bench-v4)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- 此前 TOML 行对应 Terminal-Bench 2.1 且来源为正式版资料，并非 Preview 的 Terminal-Bench 4.0 成绩。未找到目标版本的 Preview 结果；该非 Preview 行已从 Preview TOML 移除。

最近核验时间：2026-11-04T23:31+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Vals Qwen3.8 Max GA model page](https://www.vals.ai/models/alibaba_qwen3.8-max)
- [Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- Vals 正式版 Qwen3.8 Max 页面存在 Terminal-Bench-Science 数据，但没有将该成绩标为 Preview；未找到 Preview 的 v0.1 成绩。

最近核验时间：2026-11-04T23:31+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)
- [Zapier AutomationBench v1.0.6 leaderboard and methodology](https://zapier.com/benchmarks)

研究备注：
- 此前 Preview TOML 中的候选记录来自 Qwen3.8-Max 正式版资料，使用公开 600 任务子集；Zapier 定义的官方榜单采用私有留出集，公开子集不等价。正式版来源及公开集结果均不能确认 Preview 的私有集成绩，对应行已移除。

尚未解决的问题：
- 没有找到明确属于 Preview 且与私有留出集定义对应的 AutomationBench v1.0.6 成绩。

最近核验时间：2026-11-04T23:31+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld v2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- 此前 Preview TOML 有 OSWorld-Verified 记录，但它来自正式版资料；GA 页面列出的 OSWorld 2.0 结果也不是本地定义的 v2.1。未找到 Preview 的 OSWorld v2.1 成绩。

最近核验时间：2026-11-04T23:31+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Preview official availability page](https://www.alibabacloud.com/help/en/lingma/qwen3-8-max-preview-limited-time-offer)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper](https://arxiv.org/abs/2608.10677)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- Surge 实时榜列出 Qwen 3.8 Max 的结果，但条目没有 Preview 后缀或可核实的运行日期，不能确认被测检查点；此前 Preview TOML 没有此项记录。

尚未解决的问题：
- 当前 Chartography 条目是否来自 Preview 或正式版检查点不明；未将该条目写入 Preview TOML。

最近核验时间：2026-11-04T23:31+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Qwen official GA model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Artificial Analysis Humanity's Last Exam evaluation](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- 此前 Preview TOML 的两条 HLE 记录与正式版官方资料相同，来源未指向 Preview 检查点；两行已从 Preview TOML 移除。未找到可归属 Preview 的 HLE 成绩。

尚未解决的问题：
- 正式版 HLE 成绩不能归属 Preview；没有 Preview 端点或检查点级来源。

最近核验时间：2026-11-04T23:31+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Alibaba models](https://artificialanalysis.ai/models/creators/alibaba)
- [Qwen3.8-Max GA release](https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- Artificial Analysis 当前 Alibaba 列表中可见的是正式版/后续快照，没有 Qwen3.8 Max Preview 的 Intelligence Index V5 条目；未找到 Preview 精确成绩。

最近核验时间：2026-11-04T23:31+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 evaluation](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Qwen3.8-Max GA model comparison](https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-o3)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- Artificial Analysis 页面列出的是 GA Qwen3.8-Max / 后续快照结果，未见 Preview 条目；未找到可归属 Preview 的 GDPval-AA v2.1 成绩。

最近核验时间：2026-11-04T23:31+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Preview to GA routing notice](https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1)

研究备注：
- Vals Index v2.2 页面显示的是 Qwen 3.8 Max 0902 后续快照，不是 Preview；未找到 Qwen3.8 Max Preview 的该版本成绩。

最近核验时间：2026-11-04T23:31+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Alibaba models",
          "url": "https://artificialanalysis.ai/models/creators/alibaba"
        },
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "Artificial Analysis 当前 Alibaba 列表中可见的是正式版/后续快照，没有 Qwen3.8 Max Preview 的 Intelligence Index V5 条目；未找到 Preview 精确成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Qwen official GA model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        },
        {
          "label": "Zapier AutomationBench v1.0.6 leaderboard and methodology",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "此前 Preview TOML 中的候选记录来自 Qwen3.8-Max 正式版资料，使用公开 600 任务子集；Zapier 定义的官方榜单采用私有留出集，公开子集不等价。正式版来源及公开集结果均不能确认 Preview 的私有集成绩，对应行已移除。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有找到明确属于 Preview 且与私有留出集定义对应的 AutomationBench v1.0.6 成绩。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Preview official availability page",
          "url": "https://www.alibabacloud.com/help/en/lingma/qwen3-8-max-preview-limited-time-offer"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/abs/2608.10677"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "Surge 实时榜列出 Qwen 3.8 Max 的结果，但条目没有 Preview 后缀或可核实的运行日期，不能确认被测检查点；此前 Preview TOML 没有此项记录。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前 Chartography 条目是否来自 Preview 或正式版检查点不明；未将该条目写入 Preview TOML。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Qwen official GA model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "此前 Preview 文件中的 DeepSWE 记录引自 2026-08-03 正式版资料；当前 DeepSWE 榜单显示的是 Qwen3.8-Max，未见 Preview。正式版材料不能证明结果来自 2026-07-19 Preview 检查点，因此相关行已从 Preview TOML 移除。"
      ],
      "status": "待核实",
      "unresolved": [
        "没有找到直接指向 Preview 端点或检查点的 DeepSWE v1.1 成绩；正式版结果不能据别名迁移反推为 Preview 结果。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Qwen3.8-Max GA model comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/qwen3-8-max-vs-o3"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "Artificial Analysis 页面列出的是 GA Qwen3.8-Max / 后续快照结果，未见 Preview 条目；未找到可归属 Preview 的 GDPval-AA v2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Qwen official GA model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Artificial Analysis Humanity's Last Exam evaluation",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "此前 Preview TOML 的两条 HLE 记录与正式版官方资料相同，来源未指向 Preview 检查点；两行已从 Preview TOML 移除。未找到可归属 Preview 的 HLE 成绩。"
      ],
      "status": "待核实",
      "unresolved": [
        "正式版 HLE 成绩不能归属 Preview；没有 Preview 端点或检查点级来源。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld v2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "此前 Preview TOML 有 OSWorld-Verified 记录，但它来自正式版资料；GA 页面列出的 OSWorld 2.0 结果也不是本地定义的 v2.1。未找到 Preview 的 OSWorld v2.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Qwen official GA model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard and version notes",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "此前 Preview 文件中的 SWE-bench Pro 记录源自正式版资料，未证明属于 Preview，也未注明本地定义的 V2。Scale 在 2026-09-22 发布刷新后的 V2 split，不能把早期未注明版本的正式版行映射为 Preview 的 V2 成绩；对应行已从 Preview TOML 移除。"
      ],
      "status": "待核实",
      "unresolved": [
        "未找到 Preview 的 SWE-bench Pro V2 结果；GA 资料没有证明 Preview 身份或 V2 数据版本。"
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Vals Qwen3.8 Max GA model page",
          "url": "https://www.vals.ai/models/alibaba_qwen3.8-max"
        },
        {
          "label": "Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "Vals 正式版 Qwen3.8 Max 页面存在 Terminal-Bench-Science 数据，但没有将该成绩标为 Preview；未找到 Preview 的 v0.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Qwen3.8-Max GA release",
          "url": "https://www.alibabacloud.com/blog/qwen3-8-max-a-new-bar-for-coding-and-cowork_603421"
        },
        {
          "label": "Qwen official GA model card",
          "url": "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "此前 TOML 行对应 Terminal-Bench 2.1 且来源为正式版资料，并非 Preview 的 Terminal-Bench 4.0 成绩。未找到目标版本的 Preview 结果；该非 Preview 行已从 Preview TOML 移除。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T23:31+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Preview to GA routing notice",
          "url": "https://www.alibabacloud.com/en/notice/alibaba_cloud_model_studio_model_upgrade_notice_81a?_p_lc=1"
        }
      ],
      "notes": [
        "Vals Index v2.2 页面显示的是 Qwen 3.8 Max 0902 后续快照，不是 Preview；未找到 Qwen3.8 Max Preview 的该版本成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 15,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T23:31+08:00",
  "model_id": "alibaba/qwen3.8-max-preview",
  "model_notes": [
    "官方资料确认 Qwen3.8 Max Preview 于 2026-07-19 开放；Qwen3.8-Max 正式版于 2026-08-03 发布。阿里 2026-08-04 通知称 Preview 于 8 月 5 日退役，8 月 6 日起 Preview 请求路由到正式版。",
    "处理开始时 Preview TOML 含 15 条成绩，全部只引用 2026-08-03 的 GA 发布文章，未标出 Preview 检查点。为避免将正式版成绩归给 Preview，15 条已从本模型文件移除；正式版文件中已有的正式版记录未改动。",
    "因 GA 与 Preview 的身份关系及多项源记录的版本/测试配置无法确认，相关目标项保留待核实；未找到直接属于 Preview 的可信成绩。"
  ],
  "new_records": 0,
  "overall_status": "待复核",
  "removed_records": 15,
  "updated_records": 0
}

-->
