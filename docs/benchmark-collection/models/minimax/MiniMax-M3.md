# MiniMax-M3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：minimax/MiniMax-M3
- 模型名称：MiniMax-M3
- 发布日期：2026-06-01
- 最近检查时间：2026-11-05T04:50+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：6
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- 保留模型文件中已有 6 条成绩；本轮新增 Terminal-Bench 4.0、Terminal-Bench-Science 0.1、原始 HLE 与 Artificial Analysis Intelligence Index v5.0.1 各一条。两个 AA 终端成绩按其页面展示值记录，并注明整数舍入。
- 官方模型文章报告 Terminal-Bench 2.1=66.0 与泛称 SWE-Bench Pro=59.0；前者不映射至 4.0，后者发布早于 Pro V2，不映射至 V2。
- Artificial Analysis GDPval-AA v2.1 页面之间出现不同 Elo，未将任一数值写入 TOML；待获得明确的评测时间或统一结果后再复核。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DataCurve DeepSWE leaderboard archive (2026-06-15)](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/), [DeepSWE v1.1 release note](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3) | 2026-11-05T04:50+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale SWE-bench Pro V2 release note](https://labs.scale.com/blog/swe-bench-pro-v2), [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3) | 2026-11-05T04:50+08:00 |
| terminal-bench-v4 | 已收录 | 66.0 (metric=success rate; version=2.1); 2% (rounded display) (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=pass@1 averaged over three repeats; Artificial Analysis page displays a rounded integer; exact unrounded score not exposed; 500-step cap; harness=mini-swe-agent) | [Artificial Analysis MiniMax-M3 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3), [Artificial Analysis Terminal-Bench 4.0 evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Artificial Analysis Terminal-Bench methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| terminal-bench-science-v0.1 | 已收录 | 0% (rounded display) (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=pass@1 averaged over three repeats; Artificial Analysis page displays a rounded integer; exact unrounded score not exposed; 1,000-step cap; harness=mini-swe-agent) | [Artificial Analysis MiniMax-M3 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3), [Artificial Analysis Terminal-Bench-Science 0.1 evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Artificial Analysis Terminal-Bench-Science methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3) | 2026-11-05T04:50+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld V2 official website](https://osworld-v2.xlang.ai/), [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2), [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3) | 2026-11-05T04:50+08:00 |
| chartography | 未找到 | — | [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography evaluation repository](https://github.com/surge-ai/chartography), [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3) | 2026-11-05T04:50+08:00 |
| humanitys-last-exam | 已收录 | 39 (metric=accuracy; dataset=May 2025 revision; 2,158 text-only questions; variant=pass@1; no tools; GPT-5.6 Luna (medium) equality checker) | [Artificial Analysis MiniMax-M3 vs GLM-4.6 comparison](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6), [Artificial Analysis HLE evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| artificial-analysis-intelligence-index-v5 | 已收录 | 19 (metric=index score; version=5.0.1; dataset=Nine constituent evaluations in Artificial Analysis Intelligence Index v5.0.1; variant=Reasoning version) | [Artificial Analysis MiniMax-M3 model page](https://artificialanalysis.ai/models/minimax-m3), [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| gdpval-aa-v2.1 | 冲突 | — | [AA comparison: MiniMax-M3 vs GLM-4.6 (1242)](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6), [AA comparison: MiniMax-M3 vs o1 (1243)](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-o1), [AA comparison: MiniMax-M3 vs Qwen3.5 Omni Plus (1246)](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-qwen3-5-omni-plus), [AA GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [AA GDPval-AA methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T04:50+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2.1 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-05T04:50+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DataCurve DeepSWE leaderboard archive (2026-06-15)](https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 release note](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3)

研究备注：
- 2026-06-15 的官方榜单归档快照列出 minimax-m3 为 20% ± 4；该页注明榜单数据更新时间为 2026-06-11，且没有版本或 effort 选择项。DeepSWE v1.1 于 2026-06-14 发布，因此无法确认快照成绩对应 v1.1，未录入。

尚未解决的问题：
- 需找到明确标注 DeepSWE v1.1 的 MiniMax-M3 成绩，或可核实的对应评测配置。

最近核验时间：2026-11-05T04:50+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale SWE-bench Pro V2 release note](https://labs.scale.com/blog/swe-bench-pro-v2)
- [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3)

研究备注：
- MiniMax M3 官方文章中的 59.0% 是 2026-06-01 的泛称 SWE-Bench Pro 成绩，早于 2026-09 发布的 Pro V2；官方 V2 榜单未提供可确认的 M3 V2 成绩，不把历史泛称分数改标为 V2。

最近核验时间：2026-11-05T04:50+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 66.0
- metric: success rate
- version: 2.1
- source: [https://www.minimax.io/blog/minimax-m3](https://www.minimax.io/blog/minimax-m3)
- date: 2026-06-01
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 2% (rounded display)
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: pass@1 averaged over three repeats; Artificial Analysis page displays a rounded integer; exact unrounded score not exposed; 500-step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis MiniMax-M3 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3)
- [Artificial Analysis Terminal-Bench 4.0 evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Artificial Analysis Terminal-Bench methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 对比页将 2% 列在精确模型 MiniMax-M3 下；AA 独立评测全部 66 项，使用 mini-swe-agent，pass@1 每项三次重复平均，最多 500 步。对比页只显示整数百分比，因此 TOML 保留显示值并注明舍入，未声称底层值恰为 2.00%。

最近核验时间：2026-11-05T04:50+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 0% (rounded display)
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: pass@1 averaged over three repeats; Artificial Analysis page displays a rounded integer; exact unrounded score not exposed; 1,000-step cap
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis MiniMax-M3 comparison](https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3)
- [Artificial Analysis Terminal-Bench-Science 0.1 evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Artificial Analysis Terminal-Bench-Science methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 对比页显示 MiniMax-M3 为 0%；评测为官方 0.1.0 版本的 70 项任务，mini-swe-agent、pass@1 每项三次重复平均，最多 1,000 步。页面按整数百分比显示，精确底层分数不可读，故 TOML 记录为带舍入说明的字符串，不将缺失成绩写作 0。

最近核验时间：2026-11-05T04:50+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3)

研究备注：
- M3 支持工具调用和多模态代理工作流，benchmark 适用；当前榜单只呈现前 10 项，另有 119 项折叠，无法核定完整名单中是否有 M3。AA AutomationBench-AA 21% 是不同实现，不映射至 Zapier AutomationBench 1.0.6。

尚未解决的问题：
- 需要可读的完整 AutomationBench 1.0.6 榜单来确认是否存在 M3 条目。

最近核验时间：2026-11-05T04:50+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld V2 official website](https://osworld-v2.xlang.ai/)
- [OSWorld V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3)

研究备注：
- 模型文件已有 OSWorld-Verified 70.06%，MiniMax 官方方法明确其测试集与配置属于 OSWorld-Verified，不是 OSWorld 2.1。OSWorld V2 页面提到 M3 的诊断图，但没有可核实的 2.1 精确分数行。

尚未解决的问题：
- 需确认官方 2.1 评测中 M3 的准确版本、分数及配置。

最近核验时间：2026-11-05T04:50+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography official leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography evaluation repository](https://github.com/surge-ai/chartography)
- [MiniMax M3 official release and evaluations](https://www.minimax.io/blog/minimax-m3)

研究备注：
- M3 支持图像输入，benchmark 适用；当前公开排行榜未列出该精确型号，也未在 M3 官方评测文章找到 Chartography 成绩。

最近核验时间：2026-11-05T04:50+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 39
- metric: accuracy
- dataset: May 2025 revision; 2,158 text-only questions
- variant: pass@1; no tools; GPT-5.6 Luna (medium) equality checker
- source: [https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis MiniMax-M3 vs GLM-4.6 comparison](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6)
- [Artificial Analysis HLE evaluation methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 对比页给 MiniMax-M3 原始 Humanity’s Last Exam accuracy 39%，不是 v5 中的 HLE-Diamond 16%。AA 原始 HLE 使用 May 2025 全集中的 2,158 道纯文本题、pass@1，并由 GPT-5.6 Luna (medium) equality checker 判分；记录保留为独立原始 HLE 成绩。

最近核验时间：2026-11-05T04:50+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 19
- metric: index score
- version: 5.0.1
- dataset: Nine constituent evaluations in Artificial Analysis Intelligence Index v5.0.1
- variant: Reasoning version
- source: [https://artificialanalysis.ai/models/minimax-m3](https://artificialanalysis.ai/models/minimax-m3)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Artificial Analysis MiniMax-M3 model page](https://artificialanalysis.ai/models/minimax-m3)
- [Artificial Analysis Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA 当前模型页报告 reasoning 版本的 Intelligence Index 19，版本为 v5.0.1，含九项评测。TOML 保留源版本 5.0.1；Benchmark 定义显式声明 5.0.1 为 v5.0 系列兼容版本，以便覆盖率按 V5 项统计。

最近核验时间：2026-11-05T04:50+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：冲突。

已检查的主要资料：
- [AA comparison: MiniMax-M3 vs GLM-4.6 (1242)](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6)
- [AA comparison: MiniMax-M3 vs o1 (1243)](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-o1)
- [AA comparison: MiniMax-M3 vs Qwen3.5 Omni Plus (1246)](https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-qwen3-5-omni-plus)
- [AA GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [AA GDPval-AA methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 三个 AA 对比页对同一 MiniMax-M3 与 GDPval-AA v2.1 分别显示 1242、1243、1246 Elo，未标注不同 effort 或可辨别的模型变体，也没有给出分数评测日期；当前公开排行榜 HTML 无 M3 可核实行。保持冲突，不选取任一数值写入 TOML。
- 搜索摘要曾显示 1250，但直接页面现状未能复核，作为缓存线索而非可用分数。AA 2026-06 文章所述约 1670 未标 v2.1，且旧刻度与 v2.1 不同，不映射。此前 1109/1102 是 Nex-N2-Pro，不属于 M3。

尚未解决的问题：
- 需 AA 给出 GDPval-AA v2.1 MiniMax-M3 当前 Elo 或带日期的历史结果，以消解页面冲突。

最近核验时间：2026-11-05T04:50+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 official leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2.1 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- v2.2 榜单列出 MiniMax-M3.1-Flash，但未列 MiniMax-M3；搜索到的 M3 记录属于 v1.2、v2.0 或 v2.1，不能迁移到 v2.2。

最近核验时间：2026-11-05T04:50+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniMax-M3 model page",
          "url": "https://artificialanalysis.ai/models/minimax-m3"
        },
        {
          "label": "Artificial Analysis Intelligence Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 当前模型页报告 reasoning 版本的 Intelligence Index 19，版本为 v5.0.1，含九项评测。TOML 保留源版本 5.0.1；Benchmark 定义显式声明 5.0.1 为 v5.0 系列兼容版本，以便覆盖率按 V5 项统计。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "MiniMax M3 official release and evaluations",
          "url": "https://www.minimax.io/blog/minimax-m3"
        }
      ],
      "notes": [
        "M3 支持工具调用和多模态代理工作流，benchmark 适用；当前榜单只呈现前 10 项，另有 119 项折叠，无法核定完整名单中是否有 M3。AA AutomationBench-AA 21% 是不同实现，不映射至 Zapier AutomationBench 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要可读的完整 AutomationBench 1.0.6 榜单来确认是否存在 M3 条目。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography official leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography evaluation repository",
          "url": "https://github.com/surge-ai/chartography"
        },
        {
          "label": "MiniMax M3 official release and evaluations",
          "url": "https://www.minimax.io/blog/minimax-m3"
        }
      ],
      "notes": [
        "M3 支持图像输入，benchmark 适用；当前公开排行榜未列出该精确型号，也未在 M3 官方评测文章找到 Chartography 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "DataCurve DeepSWE leaderboard archive (2026-06-15)",
          "url": "https://web.archive.org/web/20260615111157/https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 release note",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "MiniMax M3 official release and evaluations",
          "url": "https://www.minimax.io/blog/minimax-m3"
        }
      ],
      "notes": [
        "2026-06-15 的官方榜单归档快照列出 minimax-m3 为 20% ± 4；该页注明榜单数据更新时间为 2026-06-11，且没有版本或 effort 选择项。DeepSWE v1.1 于 2026-06-14 发布，因此无法确认快照成绩对应 v1.1，未录入。"
      ],
      "status": "待核实",
      "unresolved": [
        "需找到明确标注 DeepSWE v1.1 的 MiniMax-M3 成绩，或可核实的对应评测配置。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "AA comparison: MiniMax-M3 vs GLM-4.6 (1242)",
          "url": "https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6"
        },
        {
          "label": "AA comparison: MiniMax-M3 vs o1 (1243)",
          "url": "https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-o1"
        },
        {
          "label": "AA comparison: MiniMax-M3 vs Qwen3.5 Omni Plus (1246)",
          "url": "https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-qwen3-5-omni-plus"
        },
        {
          "label": "AA GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "AA GDPval-AA methodology and version history",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "三个 AA 对比页对同一 MiniMax-M3 与 GDPval-AA v2.1 分别显示 1242、1243、1246 Elo，未标注不同 effort 或可辨别的模型变体，也没有给出分数评测日期；当前公开排行榜 HTML 无 M3 可核实行。保持冲突，不选取任一数值写入 TOML。",
        "搜索摘要曾显示 1250，但直接页面现状未能复核，作为缓存线索而非可用分数。AA 2026-06 文章所述约 1670 未标 v2.1，且旧刻度与 v2.1 不同，不映射。此前 1109/1102 是 Nex-N2-Pro，不属于 M3。"
      ],
      "status": "冲突",
      "unresolved": [
        "需 AA 给出 GDPval-AA v2.1 MiniMax-M3 当前 Elo 或带日期的历史结果，以消解页面冲突。"
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniMax-M3 vs GLM-4.6 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/minimax-m3-vs-glm-4-6"
        },
        {
          "label": "Artificial Analysis HLE evaluation methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 对比页给 MiniMax-M3 原始 Humanity’s Last Exam accuracy 39%，不是 v5 中的 HLE-Diamond 16%。AA 原始 HLE 使用 May 2025 全集中的 2,158 道纯文本题、pass@1，并由 GPT-5.6 Luna (medium) equality checker 判分；记录保留为独立原始 HLE 成绩。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "OSWorld V2 official website",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "MiniMax M3 official release and evaluations",
          "url": "https://www.minimax.io/blog/minimax-m3"
        }
      ],
      "notes": [
        "模型文件已有 OSWorld-Verified 70.06%，MiniMax 官方方法明确其测试集与配置属于 OSWorld-Verified，不是 OSWorld 2.1。OSWorld V2 页面提到 M3 的诊断图，但没有可核实的 2.1 精确分数行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认官方 2.1 评测中 M3 的准确版本、分数及配置。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale SWE-bench Pro V2 release note",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        },
        {
          "label": "MiniMax M3 official release and evaluations",
          "url": "https://www.minimax.io/blog/minimax-m3"
        }
      ],
      "notes": [
        "MiniMax M3 官方文章中的 59.0% 是 2026-06-01 的泛称 SWE-Bench Pro 成绩，早于 2026-09 发布的 Pro V2；官方 V2 榜单未提供可确认的 M3 V2 成绩，不把历史泛称分数改标为 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniMax-M3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science 0.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Artificial Analysis Terminal-Bench-Science methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 对比页显示 MiniMax-M3 为 0%；评测为官方 0.1.0 版本的 70 项任务，mini-swe-agent、pass@1 每项三次重复平均，最多 1,000 步。页面按整数百分比显示，精确底层分数不可读，故 TOML 记录为带舍入说明的字符串，不将缺失成绩写作 0。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis MiniMax-M3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-minimax-m3"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Artificial Analysis Terminal-Bench methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA 对比页将 2% 列在精确模型 MiniMax-M3 下；AA 独立评测全部 66 项，使用 mini-swe-agent，pass@1 每项三次重复平均，最多 500 步。对比页只显示整数百分比，因此 TOML 保留显示值并注明舍入，未声称底层值恰为 2.00%。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T04:50+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 official leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2.1 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        }
      ],
      "notes": [
        "v2.2 榜单列出 MiniMax-M3.1-Flash，但未列 MiniMax-M3；搜索到的 M3 记录属于 v1.2、v2.0 或 v2.1，不能迁移到 v2.2。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 6,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T04:50+08:00",
  "model_id": "minimax/MiniMax-M3",
  "model_notes": [
    "保留模型文件中已有 6 条成绩；本轮新增 Terminal-Bench 4.0、Terminal-Bench-Science 0.1、原始 HLE 与 Artificial Analysis Intelligence Index v5.0.1 各一条。两个 AA 终端成绩按其页面展示值记录，并注明整数舍入。",
    "官方模型文章报告 Terminal-Bench 2.1=66.0 与泛称 SWE-Bench Pro=59.0；前者不映射至 4.0，后者发布早于 Pro V2，不映射至 V2。",
    "Artificial Analysis GDPval-AA v2.1 页面之间出现不同 Elo，未将任一数值写入 TOML；待获得明确的评测时间或统一结果后再复核。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
