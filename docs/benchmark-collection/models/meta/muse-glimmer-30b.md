# Muse Glimmer 30B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：meta/muse-glimmer-30b
- 模型名称：Muse Glimmer 30B
- 发布日期：2026-08-10
- 最近检查时间：2026-11-04T19:11+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：4

## 模型身份与范围说明

- Meta 官方公告与模型卡确认本条对应 Muse Glimmer 30B（文本+图像输入），发布日期为 2026-08-10。
- 模型卡中 SWE-Bench Pro 51.2 是原始 731-task 数据集，Terminal-Bench 51.7 是 v2.1，OSWorld-Verified 65.9 未注明 v2.1；均保留原始记录但不跨版本映射。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B), [Meta evaluation methodology](https://research.meta.ai/static/muse-glimmer-methodology) | 2026-11-04T19:11+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale SWE-bench Pro V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2), [Meta evaluation methodology](https://research.meta.ai/static/muse-glimmer-methodology), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |
| terminal-bench-v4 | 已收录 | 51.7 (metric=success rate; version=2.1; variant=with terminus2); 1.0 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0 (66 tasks); effort=high; variant=Artificial Analysis independent run; pass@1 averaged over 3 repeats; harness=mini-swe-agent) | [Artificial Analysis Muse Glimmer comparison](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3), [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Vals AI Terminal-Bench Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |
| osworld-v2.1 | 待核实 | — | [OSWorld-V2 project](https://osworld-v2.xlang.ai/), [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |
| chartography | 已收录 | 17.2 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=xHigh; variant=xHigh reasoning; mean of 10 runs per task; harness=Inspect AI; Gemini 3.5 Flash judge) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography official repository and leaderboard configuration](https://github.com/surge-ai/chartography) | 2026-11-04T19:11+08:00 |
| humanitys-last-exam | 已收录 | 22.0 (metric=accuracy; dataset=text-only; 2,158 questions; effort=high; variant=no tools; Artificial Analysis result) | [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B), [Meta evaluation methodology](https://research.meta.ai/static/muse-glimmer-methodology), [Artificial Analysis Muse Glimmer comparison](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3) | 2026-11-04T19:11+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | — | [Artificial Analysis Muse Glimmer model profile](https://artificialanalysis.ai/models/muse-glimmer), [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Artificial Analysis Muse Glimmer launch analysis](https://artificialanalysis.ai/articles/muse-glimmer) | 2026-11-04T19:11+08:00 |
| gdpval-aa-v2.1 | 已收录 | 793 (metric=Elo rating; version=2.1; dataset=220 tasks; 44 occupations; 9 industries; effort=high; harness=Artificial Analysis Stirrup; shell and web browsing) | [Artificial Analysis Muse Glimmer comparison](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3), [GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals AI Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-11-04T19:11+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-glimmer-methodology)

研究备注：
- 已检查官方 v1.1 榜单、Meta 模型卡和评测方法；未见 Muse Glimmer 的 DeepSWE v1.1 成绩。

最近核验时间：2026-11-04T19:11+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale SWE-bench Pro V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-glimmer-methodology)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Meta 模型卡列出的 SWE-Bench Pro 51.2 对应原始 731-task 数据集，Meta 方法报告说明对该数据集运行；它不是本地定义的 V2 默认 642-task 数据集。Scale V2 榜单也未见该模型。保留原始模型行，不映射到 v2.0.0。

最近核验时间：2026-11-04T19:11+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 51.7
- metric: success rate
- version: 2.1
- variant: with terminus2
- source: [https://huggingface.co/meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- date: 2026-08-10
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 1.0
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0 (66 tasks)
- effort: high
- variant: Artificial Analysis independent run; pass@1 averaged over 3 repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Muse Glimmer comparison](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3)
- [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Terminal-Bench 4.0 official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/4.0)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Artificial Analysis 当前比较页列出 Muse Glimmer (High) 的 Terminal-Bench 4.0 成绩 1%。其方法说明使用完整 66-task 数据集、mini-swe-agent、pass@1 并对每题 3 次重复取平均。Terminal-Bench 官方 v4 榜单当前未呈现可读成绩行；本记录明确标注为 Artificial Analysis 独立评测。模型卡中 51.7 是 Terminal-Bench 2.1，不与此行混淆。

最近核验时间：2026-11-04T19:11+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Terminal-Bench Science leaderboard and methodology](https://www.vals.ai/benchmarks/terminal-bench-science)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Vals AI 官方榜单未见 Muse Glimmer；Meta 模型卡及方法报告也未报告 Terminal-Bench Science v0.1 成绩。

最近核验时间：2026-11-04T19:11+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Zapier 官方榜单标注 v1.0.6，目前只显示前 10 项并折叠其余 119 项。Artificial Analysis 的 AutomationBench-AA 是另一评测，不能替代 Zapier v1.0.6。

尚未解决的问题：
- 当前无法检查 Zapier 榜单隐藏的 119 项，不能确定是否包含 Muse Glimmer。

最近核验时间：2026-11-04T19:11+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [OSWorld-V2 project](https://osworld-v2.xlang.ai/)
- [OSWorld-V2 official repository](https://github.com/xlang-ai/OSWorld-V2)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Meta 模型卡报告 OSWorld-Verified 65.9，但没有注明 OSWorld v2.1；该版本不能直接映射。已检查 OSWorld v2.1 项目和官方仓库，当前榜单读取时没有可确认的 Muse Glimmer 行。

尚未解决的问题：
- 需查明 OSWorld-Verified 65.9 对应的评测版本，或在 v2.1 榜单数据可读时复查。

最近核验时间：2026-11-04T19:11+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 17.2
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: xHigh
- variant: xHigh reasoning; mean of 10 runs per task
- harness: Inspect AI; Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography official repository and leaderboard configuration](https://github.com/surge-ai/chartography)

研究备注：
- Surge 官方榜单列出 Muse Glimmer 30B (xHigh reasoning) 17.2%。官方仓库说明是 100 tasks，指标 accuracy/mean (Pass@1)，榜单配置为每题 10 runs、Gemini 3.5 Flash judge，harness 为 Inspect AI；未公布语义版本或评测日期。

最近核验时间：2026-11-04T19:11+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 22.0
- metric: accuracy
- dataset: text-only; 2,158 questions
- effort: high
- variant: no tools; Artificial Analysis result
- source: [https://huggingface.co/meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [Meta evaluation methodology](https://research.meta.ai/static/muse-glimmer-methodology)
- [Artificial Analysis Muse Glimmer comparison](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3)

研究备注：
- Meta 模型卡列出 HLE Text (AA) 22.0。Meta 评测方法说明使用 HLE text-only 2,158 题、不允许工具，Muse Glimmer 采用 high reasoning strength；未给出评测日期或 HLE 语义版本。

最近核验时间：2026-11-04T19:11+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Muse Glimmer model profile](https://artificialanalysis.ai/models/muse-glimmer)
- [Artificial Analysis Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Artificial Analysis Muse Glimmer launch analysis](https://artificialanalysis.ai/articles/muse-glimmer)

研究备注：
- Artificial Analysis 当前模型页显示 Intelligence Index 6，当前方法版本为 v5.0.1；本地定义版本是 5.0。Artificial Analysis 发布分析还报告初始值 35，版本页面内容有更新。未将任一数值写入目标定义。

尚未解决的问题：
- 需先确认本地 v5.0 与当前 v5.0.1 的映射规则，并明确应采用哪一版公开结果。

最近核验时间：2026-11-04T19:11+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 793
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks; 44 occupations; 9 industries
- effort: high
- harness: Artificial Analysis Stirrup; shell and web browsing
- source: [https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Muse Glimmer comparison](https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3)
- [GDPval-AA v2.1 evaluation and methodology](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence Benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Artificial Analysis 官方比较页针对 Muse Glimmer (High) 列出 GDPval-AA v2.1 793 Elo。官方方法页确认 v2.1 包含 220 tasks、44 occupations、9 industries，并通过 Stirrup shell/web agent loop 使用盲测 pairwise comparisons 计算 Elo。Meta 卡上的 953 是 GDPval-AA v2，不映射至此版本。

最近核验时间：2026-11-04T19:11+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals AI Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Meta Muse Glimmer model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

研究备注：
- Vals AI 官方 v2.2 榜单当前未列出 Muse Glimmer；Meta 模型卡未报告 Vals Index 成绩。

最近核验时间：2026-11-04T19:11+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Glimmer model profile",
          "url": "https://artificialanalysis.ai/models/muse-glimmer"
        },
        {
          "label": "Artificial Analysis Index methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Artificial Analysis Muse Glimmer launch analysis",
          "url": "https://artificialanalysis.ai/articles/muse-glimmer"
        }
      ],
      "notes": [
        "Artificial Analysis 当前模型页显示 Intelligence Index 6，当前方法版本为 v5.0.1；本地定义版本是 5.0。Artificial Analysis 发布分析还报告初始值 35，版本页面内容有更新。未将任一数值写入目标定义。"
      ],
      "status": "待核实",
      "unresolved": [
        "需先确认本地 v5.0 与当前 v5.0.1 的映射规则，并明确应采用哪一版公开结果。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Zapier 官方榜单标注 v1.0.6，目前只显示前 10 项并折叠其余 119 项。Artificial Analysis 的 AutomationBench-AA 是另一评测，不能替代 Zapier v1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "当前无法检查 Zapier 榜单隐藏的 119 项，不能确定是否包含 Muse Glimmer。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography official repository and leaderboard configuration",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 官方榜单列出 Muse Glimmer 30B (xHigh reasoning) 17.2%。官方仓库说明是 100 tasks，指标 accuracy/mean (Pass@1)，榜单配置为每题 10 runs、Gemini 3.5 Flash judge，harness 为 Inspect AI；未公布语义版本或评测日期。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-glimmer-methodology"
        }
      ],
      "notes": [
        "已检查官方 v1.1 榜单、Meta 模型卡和评测方法；未见 Muse Glimmer 的 DeepSWE v1.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Glimmer comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3"
        },
        {
          "label": "GDPval-AA v2.1 evaluation and methodology",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Intelligence Benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Artificial Analysis 官方比较页针对 Muse Glimmer (High) 列出 GDPval-AA v2.1 793 Elo。官方方法页确认 v2.1 包含 220 tasks、44 occupations、9 industries，并通过 Stirrup shell/web agent loop 使用盲测 pairwise comparisons 计算 Elo。Meta 卡上的 953 是 GDPval-AA v2，不映射至此版本。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-glimmer-methodology"
        },
        {
          "label": "Artificial Analysis Muse Glimmer comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3"
        }
      ],
      "notes": [
        "Meta 模型卡列出 HLE Text (AA) 22.0。Meta 评测方法说明使用 HLE text-only 2,158 题、不允许工具，Muse Glimmer 采用 high reasoning strength；未给出评测日期或 HLE 语义版本。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 project",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld-V2 official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Meta 模型卡报告 OSWorld-Verified 65.9，但没有注明 OSWorld v2.1；该版本不能直接映射。已检查 OSWorld v2.1 项目和官方仓库，当前榜单读取时没有可确认的 Muse Glimmer 行。"
      ],
      "status": "待核实",
      "unresolved": [
        "需查明 OSWorld-Verified 65.9 对应的评测版本，或在 v2.1 榜单数据可读时复查。"
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale SWE-bench Pro V2 release and protocol",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        },
        {
          "label": "Meta evaluation methodology",
          "url": "https://research.meta.ai/static/muse-glimmer-methodology"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Meta 模型卡列出的 SWE-Bench Pro 51.2 对应原始 731-task 数据集，Meta 方法报告说明对该数据集运行；它不是本地定义的 V2 默认 642-task 数据集。Scale V2 榜单也未见该模型。保留原始模型行，不映射到 v2.0.0。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench Science leaderboard and methodology",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Vals AI 官方榜单未见 Muse Glimmer；Meta 模型卡及方法报告也未报告 Terminal-Bench Science v0.1 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Muse Glimmer comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/muse-glimmer-vs-hy3"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Terminal-Bench 4.0 official leaderboard",
          "url": "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Artificial Analysis 当前比较页列出 Muse Glimmer (High) 的 Terminal-Bench 4.0 成绩 1%。其方法说明使用完整 66-task 数据集、mini-swe-agent、pass@1 并对每题 3 次重复取平均。Terminal-Bench 官方 v4 榜单当前未呈现可读成绩行；本记录明确标注为 Artificial Analysis 独立评测。模型卡中 51.7 是 Terminal-Bench 2.1，不与此行混淆。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T19:11+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Meta Muse Glimmer model card",
          "url": "https://huggingface.co/meta-models/Muse-Glimmer-30B"
        }
      ],
      "notes": [
        "Vals AI 官方 v2.2 榜单当前未列出 Muse Glimmer；Meta 模型卡未报告 Vals Index 成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T19:11+08:00",
  "model_id": "meta/muse-glimmer-30b",
  "model_notes": [
    "Meta 官方公告与模型卡确认本条对应 Muse Glimmer 30B（文本+图像输入），发布日期为 2026-08-10。",
    "模型卡中 SWE-Bench Pro 51.2 是原始 731-task 数据集，Terminal-Bench 51.7 是 v2.1，OSWorld-Verified 65.9 未注明 v2.1；均保留原始记录但不跨版本映射。"
  ],
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
