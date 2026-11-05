# Nemotron 3.5 Super VL 120B A12B Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：nvidia/nemotron-3.5-super-vl-120b-a12b
- 模型名称：Nemotron 3.5 Super VL 120B A12B
- 发布日期：2026-10-15
- 最近检查时间：2026-11-04T02:37+08:00
- 整体处理状态：待复核
- 新增成绩数量：6
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：6

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard), [NVIDIA BF16 Hugging Face card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [NVIDIA Super 3.5 evaluation report](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html) | 2026-11-04T02:37+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard), [NVIDIA Super 3.5 evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html) | 2026-11-04T02:37+08:00 |
| terminal-bench-v4 | 冲突 | 0.0 (metric=task resolution rate; version=4.0.0; dataset=Terminal-Bench 4.0, 66 tasks; variant=Vals AI Baseten-hosted evaluation; reported ±0.00; harness=Mini-SWE-agent) | [Vals AI Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4), [Vals AI Super-VL model page](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b), [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard), [Artificial Analysis Terminal-Bench 4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 2026-11-04T02:37+08:00 |
| terminal-bench-science-v0.1 | 待核实 | 0 (metric=task resolution rate; version=0.1.0; dataset=70 tasks; variant=pass@1 averaged over 3 repeats; AA comparison displays rounded integer percent; harness=mini-swe-agent) | [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol), [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science) | 2026-11-04T02:37+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks), [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench), [Surge post-training results](https://surgehq.ai/post-training), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard), [Artificial Analysis AutomationBench-AA definition](https://artificialanalysis.ai/evaluations/automationbench-aa) | 2026-11-04T02:37+08:00 |
| osworld-v2.1 | 未找到 | — | [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2), [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:37+08:00 |
| chartography | 待核实 | — | [Surge post-training results](https://surgehq.ai/post-training), [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography paper](https://arxiv.org/html/2608.10677v1), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:37+08:00 |
| humanitys-last-exam | 已收录 | 29.2 (metric=accuracy; version=unspecified; dataset=HLE full set, 2,500 questions, 1 sample per question; variant=BF16); 29.0 (metric=accuracy; version=unspecified; dataset=HLE full set, 2,500 questions, 1 sample per question; variant=NVFP4) | [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard), [NVIDIA HLE evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html) | 2026-11-04T02:37+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 14 (metric=index score; version=5.0) | [Artificial Analysis Super-VL model page](https://artificialanalysis.ai/models/nemotron-3-5-super-vl), [NVIDIA BF16 Hugging Face card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16) | 2026-11-04T02:37+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [NVIDIA Nemotron Super 3.5 evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html), [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard) | 2026-11-04T02:37+08:00 |
| vals-index-v2.2 | 待核实 | 29.76 (metric=performance score; version=2.2; variant=Baseten-hosted model page; tested checkpoint precision not specified) | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals AI Super-VL model page](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b), [Baseten model page](https://www.baseten.co/library/nemotron-35-super-vl/) | 2026-11-04T02:37+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)
- [NVIDIA BF16 Hugging Face card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [NVIDIA Super 3.5 evaluation report](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html)

研究备注：
- NVIDIA model card 对此 Super-VL checkpoint 列出 DeepSWE [offline]：BF16 24.65、NVFP4 18.2；但没有说明 DeepSWE v1.1、metric、harness 或 effort。官方 v1.1 leaderboard 页面早于本模型发布且未列该模型；这些分数不满足版本/运行条件核验，不写入目标映射。
- NVIDIA Super 3.5 文本模型报告的 24.6 结果属于另一个 model variant，不能用来补齐该卡的配置。

尚未解决的问题：
- NVIDIA卡上的offline记录是否为DeepSWE v1.1及其测试配置，尚无公开证据。

最近核验时间：2026-11-04T02:37+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)
- [NVIDIA Super 3.5 evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html)

研究备注：
- Scale SWE-bench Pro V2 Full 页面未列该模型。NVIDIA Super-VL model card 的 51.78/51.30 没有标版本；对应官方 evaluation report 的 SWE-bench Pro 配置是 731 tasks，与目标 v2 默认 642-task/2.0.0 split 不同，故不移用。

最近核验时间：2026-11-04T02:37+08:00

### Terminal-Bench (terminal-bench-v4)

#### 已确认成绩 1

- name: Terminal-Bench
- score: 0.0
- metric: task resolution rate
- version: 4.0.0
- dataset: Terminal-Bench 4.0, 66 tasks
- variant: Vals AI Baseten-hosted evaluation; reported ±0.00
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)

已检查的主要资料：
- [Vals AI Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)
- [Vals AI Super-VL model page](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b)
- [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)
- [Artificial Analysis Terminal-Bench 4 methodology](https://artificialanalysis.ai/evaluations/terminalbench-4-0)

研究备注：
- Vals AI 的准确模型页/榜单列 Terminal-Bench 4.0 = 0.00% ± 0.00；其方法采用 Mini-SWE-agent、66 tasks、avg@3（每次 pass@1），本条记录采用 Vals/Baseten hosted结果。AA 的模型比较页亦显示 Super VL 0%，可作公开交叉核对。
- NVIDIA model card另列 Terminal Bench 4 [offline]：BF16=1、NVFP4=1.5，但没有说明 metric单位、任务集/版本或 harness。没有将这些数值映射或合并到 V4.0记录；独立来源数值有差异，配置可比性未确定。
- 各网页更新时间不是具体评测日期；未填写 date。

尚未解决的问题：
- NVIDIA offline结果与Vals/AA 0%结果数值不同，公开材料未给足测试条件以判定差异来源；保留Vals/AA目标配置记录，不取最高值。NVIDIA卡上的精度和score单位/协议需进一步核实。

最近核验时间：2026-11-04T02:37+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 已确认成绩 1

- name: Terminal-Bench-Science
- score: 0
- metric: task resolution rate
- version: 0.1.0
- dataset: 70 tasks
- variant: pass@1 averaged over 3 repeats; AA comparison displays rounded integer percent
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol)

已检查的主要资料：
- [Artificial Analysis comparison](https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol)
- [Artificial Analysis Terminal-Bench Science methodology](https://artificialanalysis.ai/evaluations/terminal-bench-science)

研究备注：
- AA 比较页对精确模型标签 Nemotron 3.5 Super VL 显示 0%。AA 方法页说明 v0.1.0、70 tasks、Mini-SWE-agent、pass@1三次平均；比较页只显示整数百分比。TOML保留0这一来源发布值。
- AA没有披露该项目使用BF16/NVFP4的哪种精度及服务配置，故条件仍待复核；不填effort或date。

尚未解决的问题：
- benchmark成绩对应的checkpoint精度/provider未披露。

最近核验时间：2026-11-04T02:37+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Zapier AutomationBench repository](https://github.com/zapier/AutomationBench)
- [Surge post-training results](https://surgehq.ai/post-training)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)
- [Artificial Analysis AutomationBench-AA definition](https://artificialanalysis.ai/evaluations/automationbench-aa)

研究备注：
- Zapier官方榜当前版本为1.0.6，但可读页面只展开top 10，另119项没有展开。
- Surge post-training页面列泛称 Nemotron 3.5 Super 的 AutomationBench pass@1 14.8%→27.5%，未说明精确BF16/NVFP4 checkpoint、版本或完整设置。NVIDIA卡的 AutomationBench-AA (BF16 32.44 / NVFP4 32.3) 是AA composite component，名称/定义不同，不作为AutomationBench 1.0.6。

尚未解决的问题：
- Zapier榜剩余119条不可见；Surge AutomationBench记录未说明精确checkpoint及协议。

最近核验时间：2026-11-04T02:37+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [OSWorld-V2 repository](https://github.com/xlang-ai/OSWorld-V2)
- [OSWorld-V2 leaderboard](https://osworld-v2.xlang.ai/)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- OSWorld-V2官方仓库与排行榜未找到Nemotron 3.5 Super VL的osworld-v2.1成绩。NVIDIA卡的OSWorld-Verified BF16 51.14、NVFP4 52.3是另一benchmark定义，不映射。

最近核验时间：2026-11-04T02:37+08:00

### Chartography (chartography)

- 当前状态：待核实。

已检查的主要资料：
- [Surge post-training results](https://surgehq.ai/post-training)
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography paper](https://arxiv.org/html/2608.10677v1)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- Surge post-training页面对泛称 Nemotron 3.5 Super 报告 Chartography with tools, pass@1 39.4%→50.6%；没有标明精确Super-VL BF16/NVFP4 checkpoint或完整工具配置。NVIDIA卡未列Chartography，Surge通用榜未见该模型。
- 原始Chartography标准协议是图表图像+问题、无工具；with-tools是不同条件，须与标准成绩分开记录。

尚未解决的问题：
- Surge图表理解结果的checkpoint精度和工具配置未知，无法确认属于本条Super-VL model id。

最近核验时间：2026-11-04T02:37+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 已确认成绩 1

- name: Humanity's Last Exam
- score: 29.2
- metric: accuracy
- version: unspecified
- dataset: HLE full set, 2,500 questions, 1 sample per question
- variant: BF16
- source: [https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

#### 已确认成绩 2

- name: Humanity's Last Exam
- score: 29.0
- metric: accuracy
- version: unspecified
- dataset: HLE full set, 2,500 questions, 1 sample per question
- variant: NVFP4
- source: [https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

已检查的主要资料：
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)
- [NVIDIA HLE evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html)

研究备注：
- NVIDIA model card及评测方法报告明确列 HLE full set：BF16 29.20、NVFP4 29.00。方法页注明完整集2,500题、每题1个样本；这是目标原始HLE完整集，不与2,158题text-only子集或with-tools text-only记录混淆。TOML分别保留两种精度。
- 来源没有报告具体benchmark执行日期、完整集harness或effort；未将release date或方法页日期填入date。

最近核验时间：2026-11-04T02:37+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 已确认成绩 1

- name: Artificial Analysis Intelligence Index
- score: 14
- metric: index score
- version: 5.0
- source: [https://artificialanalysis.ai/models/nemotron-3-5-super-vl](https://artificialanalysis.ai/models/nemotron-3-5-super-vl)

已检查的主要资料：
- [Artificial Analysis Super-VL model page](https://artificialanalysis.ai/models/nemotron-3-5-super-vl)
- [NVIDIA BF16 Hugging Face card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)

研究备注：
- AA官方模型页以准确标签 Nemotron 3.5 Super VL 列出 Intelligence Index 14；页面说明当前Index版本5.0。TOML收录公开分数14、version 5.0，不推断精度/effort/date。
- AA页面没有说明该Index使用BF16或NVFP4哪一精度；AA页链接到HF BF16 card不独立证明实际评测精度。

尚未解决的问题：
- AA Index结果所用checkpoint精度、provider及评测参数未披露。

最近核验时间：2026-11-04T02:37+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [NVIDIA Nemotron Super 3.5 evaluation methodology](https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html)
- [NVIDIA Super-VL model card](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard)

研究备注：
- AA GDPval-AA v2.1榜单未列目标模型。NVIDIA公开的 BF16 1211.20 / NVFP4 1206 是GDPval-AA v2，报告称实现loosely follows v2.1 methodology，但明确标为v2；不得改标或映射成v2.1。

最近核验时间：2026-11-04T02:37+08:00

### Vals Index (vals-index-v2.2)

#### 已确认成绩 1

- name: Vals Index
- score: 29.76
- metric: performance score
- version: 2.2
- variant: Baseten-hosted model page; tested checkpoint precision not specified
- source: [https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b)

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals AI Super-VL model page](https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b)
- [Baseten model page](https://www.baseten.co/library/nemotron-35-super-vl/)

研究备注：
- Vals AI模型页以Nemotron 3.5 Super VL列出Vals Index 29.76% ± 1.02；榜页确认Index版本2.2。TOML保留29.76，未把全局profile的effort/provider设置当成本次Index的确定条件。
- 模型页默认provider为Baseten，但提示不同benchmark可能使用不同provider/参数；该Index测试使用的BF16/NVFP4精度和具体参数未披露。页面10/30更新时间不是benchmark执行日期。

尚未解决的问题：
- Vals结果对应的checkpoint精度与benchmark-specific provider/参数未披露。

最近核验时间：2026-11-04T02:37+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Super-VL model page",
          "url": "https://artificialanalysis.ai/models/nemotron-3-5-super-vl"
        },
        {
          "label": "NVIDIA BF16 Hugging Face card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16"
        }
      ],
      "notes": [
        "AA官方模型页以准确标签 Nemotron 3.5 Super VL 列出 Intelligence Index 14；页面说明当前Index版本5.0。TOML收录公开分数14、version 5.0，不推断精度/effort/date。",
        "AA页面没有说明该Index使用BF16或NVFP4哪一精度；AA页链接到HF BF16 card不独立证明实际评测精度。"
      ],
      "status": "待核实",
      "unresolved": [
        "AA Index结果所用checkpoint精度、provider及评测参数未披露。"
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Zapier AutomationBench repository",
          "url": "https://github.com/zapier/AutomationBench"
        },
        {
          "label": "Surge post-training results",
          "url": "https://surgehq.ai/post-training"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA definition",
          "url": "https://artificialanalysis.ai/evaluations/automationbench-aa"
        }
      ],
      "notes": [
        "Zapier官方榜当前版本为1.0.6，但可读页面只展开top 10，另119项没有展开。",
        "Surge post-training页面列泛称 Nemotron 3.5 Super 的 AutomationBench pass@1 14.8%→27.5%，未说明精确BF16/NVFP4 checkpoint、版本或完整设置。NVIDIA卡的 AutomationBench-AA (BF16 32.44 / NVFP4 32.3) 是AA composite component，名称/定义不同，不作为AutomationBench 1.0.6。"
      ],
      "status": "待核实",
      "unresolved": [
        "Zapier榜剩余119条不可见；Surge AutomationBench记录未说明精确checkpoint及协议。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Surge post-training results",
          "url": "https://surgehq.ai/post-training"
        },
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography paper",
          "url": "https://arxiv.org/html/2608.10677v1"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "Surge post-training页面对泛称 Nemotron 3.5 Super 报告 Chartography with tools, pass@1 39.4%→50.6%；没有标明精确Super-VL BF16/NVFP4 checkpoint或完整工具配置。NVIDIA卡未列Chartography，Surge通用榜未见该模型。",
        "原始Chartography标准协议是图表图像+问题、无工具；with-tools是不同条件，须与标准成绩分开记录。"
      ],
      "status": "待核实",
      "unresolved": [
        "Surge图表理解结果的checkpoint精度和工具配置未知，无法确认属于本条Super-VL model id。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        },
        {
          "label": "NVIDIA BF16 Hugging Face card",
          "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "NVIDIA Super 3.5 evaluation report",
          "url": "https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html"
        }
      ],
      "notes": [
        "NVIDIA model card 对此 Super-VL checkpoint 列出 DeepSWE [offline]：BF16 24.65、NVFP4 18.2；但没有说明 DeepSWE v1.1、metric、harness 或 effort。官方 v1.1 leaderboard 页面早于本模型发布且未列该模型；这些分数不满足版本/运行条件核验，不写入目标映射。",
        "NVIDIA Super 3.5 文本模型报告的 24.6 结果属于另一个 model variant，不能用来补齐该卡的配置。"
      ],
      "status": "待核实",
      "unresolved": [
        "NVIDIA卡上的offline记录是否为DeepSWE v1.1及其测试配置，尚无公开证据。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "NVIDIA Nemotron Super 3.5 evaluation methodology",
          "url": "https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "AA GDPval-AA v2.1榜单未列目标模型。NVIDIA公开的 BF16 1211.20 / NVFP4 1206 是GDPval-AA v2，报告称实现loosely follows v2.1 methodology，但明确标为v2；不得改标或映射成v2.1。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        },
        {
          "label": "NVIDIA HLE evaluation methodology",
          "url": "https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html"
        }
      ],
      "notes": [
        "NVIDIA model card及评测方法报告明确列 HLE full set：BF16 29.20、NVFP4 29.00。方法页注明完整集2,500题、每题1个样本；这是目标原始HLE完整集，不与2,158题text-only子集或with-tools text-only记录混淆。TOML分别保留两种精度。",
        "来源没有报告具体benchmark执行日期、完整集harness或effort；未将release date或方法页日期填入date。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "OSWorld-V2 repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        },
        {
          "label": "OSWorld-V2 leaderboard",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        }
      ],
      "notes": [
        "OSWorld-V2官方仓库与排行榜未找到Nemotron 3.5 Super VL的osworld-v2.1成绩。NVIDIA卡的OSWorld-Verified BF16 51.14、NVFP4 52.3是另一benchmark定义，不映射。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        },
        {
          "label": "NVIDIA Super 3.5 evaluation methodology",
          "url": "https://docs.nvidia.com/nemotron/nightly/nemotron/super35/evaluate.html"
        }
      ],
      "notes": [
        "Scale SWE-bench Pro V2 Full 页面未列该模型。NVIDIA Super-VL model card 的 51.78/51.30 没有标版本；对应官方 evaluation report 的 SWE-bench Pro 配置是 731 tasks，与目标 v2 默认 642-task/2.0.0 split 不同，故不移用。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        }
      ],
      "notes": [
        "AA 比较页对精确模型标签 Nemotron 3.5 Super VL 显示 0%。AA 方法页说明 v0.1.0、70 tasks、Mini-SWE-agent、pass@1三次平均；比较页只显示整数百分比。TOML保留0这一来源发布值。",
        "AA没有披露该项目使用BF16/NVFP4的哪种精度及服务配置，故条件仍待复核；不填effort或date。"
      ],
      "status": "待核实",
      "unresolved": [
        "benchmark成绩对应的checkpoint精度/provider未披露。"
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        },
        {
          "label": "Vals AI Super-VL model page",
          "url": "https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b"
        },
        {
          "label": "Artificial Analysis comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/nemotron-3-5-super-vl-vs-gpt-6-1-sol"
        },
        {
          "label": "NVIDIA Super-VL model card",
          "url": "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b/modelcard"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4 methodology",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        }
      ],
      "notes": [
        "Vals AI 的准确模型页/榜单列 Terminal-Bench 4.0 = 0.00% ± 0.00；其方法采用 Mini-SWE-agent、66 tasks、avg@3（每次 pass@1），本条记录采用 Vals/Baseten hosted结果。AA 的模型比较页亦显示 Super VL 0%，可作公开交叉核对。",
        "NVIDIA model card另列 Terminal Bench 4 [offline]：BF16=1、NVFP4=1.5，但没有说明 metric单位、任务集/版本或 harness。没有将这些数值映射或合并到 V4.0记录；独立来源数值有差异，配置可比性未确定。",
        "各网页更新时间不是具体评测日期；未填写 date。"
      ],
      "status": "冲突",
      "unresolved": [
        "NVIDIA offline结果与Vals/AA 0%结果数值不同，公开材料未给足测试条件以判定差异来源；保留Vals/AA目标配置记录，不取最高值。NVIDIA卡上的精度和score单位/协议需进一步核实。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T02:37+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals AI Super-VL model page",
          "url": "https://www.vals.ai/models/baseten_nemotron-3.5-super-vl-120b-a12b"
        },
        {
          "label": "Baseten model page",
          "url": "https://www.baseten.co/library/nemotron-35-super-vl/"
        }
      ],
      "notes": [
        "Vals AI模型页以Nemotron 3.5 Super VL列出Vals Index 29.76% ± 1.02；榜页确认Index版本2.2。TOML保留29.76，未把全局profile的effort/provider设置当成本次Index的确定条件。",
        "模型页默认provider为Baseten，但提示不同benchmark可能使用不同provider/参数；该Index测试使用的BF16/NVFP4精度和具体参数未披露。页面10/30更新时间不是benchmark执行日期。"
      ],
      "status": "待核实",
      "unresolved": [
        "Vals结果对应的checkpoint精度与benchmark-specific provider/参数未披露。"
      ]
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T02:37+08:00",
  "model_id": "nvidia/nemotron-3.5-super-vl-120b-a12b",
  "new_records": 6,
  "overall_status": "待复核"
}

-->
