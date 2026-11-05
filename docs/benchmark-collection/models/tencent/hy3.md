# Hy3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：tencent/hy3
- 模型名称：Hy3
- 发布日期：2026-07-06
- 最近检查时间：2026-11-05T01:40+08:00
- 整体处理状态：待复核
- 新增成绩数量：4
- 更新成绩数量：0
- 收集前已有成绩数量：31
- 当前已收录的对应成绩数量：4

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | 28 (metric=score; variant=highest reasoning effort; 2h timeout; harness=mini-swe-agent) | [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3), [DeepSWE v1.1 release and leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-05T01:40+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T01:40+08:00 |
| terminal-bench-v4 | 已收录 | 71.7 (metric=score; version=2.1; variant=highest reasoning effort; 4h timeout; 500 episodes; harness=Terminus 2); 1 (metric=task resolution rate; version=4.0.0; dataset=66 tasks; variant=pass@1; average of 3 repeats per task; maximum 500 agent steps; upstream task timeouts; harness=mini-swe-agent) | [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3), [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3) | 2026-11-05T01:40+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3), [Artificial Analysis Terminal-Bench Science 0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Terminal-Bench Science 0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1) | 2026-11-05T01:40+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3), [AutomationBench leaderboard](https://zapier.com/benchmarks), [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3), [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T01:40+08:00 |
| osworld-v2.1 | 不适用 | — | [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3), [OSWorld V2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) | 2026-11-05T01:40+08:00 |
| chartography | 待核实 | 1.2 (metric=accuracy (mean; Pass@1); dataset=100 tasks; effort=High reasoning; variant=20 trials per task; no tools; harness=Inspect AI) | [Chartography live leaderboard](https://surgehq.ai/benchmarks/chartography), [Chartography evaluation paper](https://arxiv.org/html/2608.10677), [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3) | 2026-11-05T01:40+08:00 |
| humanitys-last-exam | 已收录 | 53.2 (metric=score; dataset=text-only; variant=highest reasoning effort; with tools); 37 (metric=score; dataset=text-only; variant=highest reasoning effort; without tools); 33 (metric=accuracy; dataset=May 2025 revision; 2,158 text-only questions from 2,500 total; variant=pass@1; judge=GPT-5.6 Luna (medium)) | [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3), [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3) | 2026-11-05T01:40+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3), [Artificial Analysis Intelligence Index v5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T01:40+08:00 |
| gdpval-aa-v2.1 | 已收录 | 1067 (metric=Elo rating; version=2.1; dataset=220 tasks across 44 occupations; variant=blind pairwise grading; Elo anchored to DeepSeek V4.1 Flash (max)=1600; harness=Stirrup) | [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3), [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T01:40+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index leaderboard](https://www.vals.ai/benchmarks/vals_index), [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3) | 2026-11-05T01:40+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 28
- metric: score
- variant: highest reasoning effort; 2h timeout
- harness: mini-swe-agent
- source: [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)
- [DeepSWE v1.1 release and leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 模型卡给出 DeepSWE 28，但现有 TOML 记录没有版本且 metric=score；本地目标定义要求版本 1.1、metric=pass@1，不能映射。

尚未解决的问题：
- 需找到明确标注 DeepSWE v1.1 与 pass@1 的 Hy3 原始评测记录。

最近核验时间：2026-11-05T01:40+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- 模型卡已有 57.9 分但未注明 V2；官方 Pro V2 榜单未找到 Hy3 的准确版本记录，未将旧行映射到 V2。

最近核验时间：2026-11-05T01:40+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 71.7
- metric: score
- version: 2.1
- variant: highest reasoning effort; 4h timeout; 500 episodes
- harness: Terminus 2
- source: [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 1
- metric: task resolution rate
- version: 4.0.0
- dataset: 66 tasks
- variant: pass@1; average of 3 repeats per task; maximum 500 agent steps; upstream task timeouts
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- [Artificial Analysis Terminal-Bench 4.0 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)

研究备注：
- 对比页列出 Hy3 的 Terminal-Bench 4.0 为 1%；方法页确认 66 项任务、mini-swe-agent、每项任务重复 3 次后按 pass@1 评分，并限制最多 500 步。旧 TOML 的 2.1/Terminus 2（71.7）结果作为另一版本保留。

最近核验时间：2026-11-05T01:40+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)
- [Artificial Analysis Terminal-Bench Science 0.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Terminal-Bench Science 0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1)

研究备注：
- 已检查模型卡及公开的 Science 0.1 资料，未找到 Hy3 的该版本结果。

最近核验时间：2026-11-05T01:40+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)
- [AutomationBench leaderboard](https://zapier.com/benchmarks)
- [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- [Artificial Analysis AutomationBench-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Zapier 榜单只显示前 10 条并提示另有 119 条折叠记录；AA 对比页的 AutomationBench-AA 18% 是 AA 自己的评测，不能视为目标 v1.0.6 指标 task_completed_correctly。

尚未解决的问题：
- 需要检查 Zapier 完整榜单或找到 Hy3 在官方 AutomationBench v1.0.6 下的原始结果。

最近核验时间：2026-11-05T01:40+08:00

### OSWorld (osworld-v2.1)

- 结论：不适用。

已检查的主要资料：
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)
- [OSWorld V2.1 evaluation guideline](https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)

研究备注：
- 模型文件及官方模型卡将 Hy3 标为文本输入；OSWorld V2.1 需要模型接收桌面截图并通过 GUI 操作，当前模型形态不满足评测输入要求。

最近核验时间：2026-11-05T01:40+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 1.2
- metric: accuracy (mean; Pass@1)
- dataset: 100 tasks
- effort: High reasoning
- variant: 20 trials per task; no tools
- harness: Inspect AI
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Chartography live leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Chartography evaluation paper](https://arxiv.org/html/2608.10677)
- [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)

研究备注：
- Surge 官方榜列出 Hy3 (High reasoning) 1.2%。论文说明基准把图表图片直接放入任务输入并禁用工具；Artificial Analysis 将 Tencent Hy3 列为仅文本输入。原始榜单成绩已保留，但尚不能解释该评测条目如何获得图像输入。

尚未解决的问题：
- 确认榜单条目使用的 Hy3 API/模型版本及视觉输入路径，解决与官方模型卡文本输入能力的冲突。

最近核验时间：2026-11-05T01:40+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 53.2
- metric: score
- dataset: text-only
- variant: highest reasoning effort; with tools
- source: [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 37
- metric: score
- dataset: text-only
- variant: highest reasoning effort; without tools
- source: [https://huggingface.co/tencent/Hy3](https://huggingface.co/tencent/Hy3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Humanity's Last Exam
- score: 33
- metric: accuracy
- dataset: May 2025 revision; 2,158 text-only questions from 2,500 total
- variant: pass@1; judge=GPT-5.6 Luna (medium)
- source: [https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- [Artificial Analysis HLE methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)

研究备注：
- Artificial Analysis 对比页列出 Hy3 33%；方法页说明此项使用 May 2025 HLE 的 2,158 道文本题（总集 2,500 题）、pass@1，由 GPT-5.6 Luna (medium) 判分。原有腾讯模型卡的 53.2 和 37 分记录 metric=score，原样保留且不映射到 accuracy。

最近核验时间：2026-11-05T01:40+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- [Artificial Analysis Intelligence Index v5 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- Hy3 对比页的 Intelligence Index 25 明确属于 v4.3.2；当前目标为 v5.0，未找到 Hy3 的 v5 指数成绩，未复用旧版分数。

最近核验时间：2026-11-05T01:40+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1067
- metric: Elo rating
- version: 2.1
- dataset: 220 tasks across 44 occupations
- variant: blind pairwise grading; Elo anchored to DeepSeek V4.1 Flash (max)=1600
- harness: Stirrup
- source: [https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Artificial Analysis Hy3 comparison](https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3)
- [GDPval-AA v2.1 methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 对比页列出 Hy3 的 GDPval-AA v2.1 为 1067 Elo。方法页说明共有 220 项任务、覆盖 44 个职业，使用 Stirrup agent harness 和盲测成对比较，Elo 锚定 DeepSeek V4.1 Flash (max)=1600；来源未给出 Hy3 的具体 reasoning effort 或评测日期，故省略。

最近核验时间：2026-11-05T01:40+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Tencent Hy3 model card](https://huggingface.co/tencent/Hy3)

研究备注：
- 检查当前 Vals Index 2.2 公开榜单，未找到 Hy3 的该版本成绩。

最近核验时间：2026-11-05T01:40+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Hy3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3"
        },
        {
          "label": "Artificial Analysis Intelligence Index v5 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Hy3 对比页的 Intelligence Index 25 明确属于 v4.3.2；当前目标为 v5.0，未找到 Hy3 的 v5 指数成绩，未复用旧版分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        },
        {
          "label": "AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "Artificial Analysis Hy3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3"
        },
        {
          "label": "Artificial Analysis AutomationBench-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "Zapier 榜单只显示前 10 条并提示另有 119 条折叠记录；AA 对比页的 AutomationBench-AA 18% 是 AA 自己的评测，不能视为目标 v1.0.6 指标 task_completed_correctly。"
      ],
      "status": "待核实",
      "unresolved": [
        "需要检查 Zapier 完整榜单或找到 Hy3 在官方 AutomationBench v1.0.6 下的原始结果。"
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Chartography live leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Chartography evaluation paper",
          "url": "https://arxiv.org/html/2608.10677"
        },
        {
          "label": "Artificial Analysis Hy3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3"
        }
      ],
      "notes": [
        "Surge 官方榜列出 Hy3 (High reasoning) 1.2%。论文说明基准把图表图片直接放入任务输入并禁用工具；Artificial Analysis 将 Tencent Hy3 列为仅文本输入。原始榜单成绩已保留，但尚不能解释该评测条目如何获得图像输入。"
      ],
      "status": "待核实",
      "unresolved": [
        "确认榜单条目使用的 Hy3 API/模型版本及视觉输入路径，解决与官方模型卡文本输入能力的冲突。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        },
        {
          "label": "DeepSWE v1.1 release and leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "模型卡给出 DeepSWE 28，但现有 TOML 记录没有版本且 metric=score；本地目标定义要求版本 1.1、metric=pass@1，不能映射。"
      ],
      "status": "待核实",
      "unresolved": [
        "需找到明确标注 DeepSWE v1.1 与 pass@1 的 Hy3 原始评测记录。"
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Hy3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3"
        },
        {
          "label": "GDPval-AA v2.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "对比页列出 Hy3 的 GDPval-AA v2.1 为 1067 Elo。方法页说明共有 220 项任务、覆盖 44 个职业，使用 Stirrup agent harness 和盲测成对比较，Elo 锚定 DeepSeek V4.1 Flash (max)=1600；来源未给出 Hy3 的具体 reasoning effort 或评测日期，故省略。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Hy3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3"
        },
        {
          "label": "Artificial Analysis HLE methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        }
      ],
      "notes": [
        "Artificial Analysis 对比页列出 Hy3 33%；方法页说明此项使用 May 2025 HLE 的 2,158 道文本题（总集 2,500 题）、pass@1，由 GPT-5.6 Luna (medium) 判分。原有腾讯模型卡的 53.2 和 37 分记录 metric=score，原样保留且不映射到 accuracy。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        },
        {
          "label": "OSWorld V2.1 evaluation guideline",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md"
        }
      ],
      "notes": [
        "模型文件及官方模型卡将 Hy3 标为文本输入；OSWorld V2.1 需要模型接收桌面截图并通过 GUI 操作，当前模型形态不满足评测输入要求。"
      ],
      "status": "不适用",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "模型卡已有 57.9 分但未注明 V2；官方 Pro V2 榜单未找到 Hy3 的准确版本记录，未将旧行映射到 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        },
        {
          "label": "Artificial Analysis Terminal-Bench Science 0.1 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Terminal-Bench Science 0.1 release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        }
      ],
      "notes": [
        "已检查模型卡及公开的 Science 0.1 资料，未找到 Hy3 的该版本结果。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Hy3 comparison",
          "url": "https://artificialanalysis.ai/models/comparisons/hy3-non-reasoning-vs-hy3"
        },
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        },
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        }
      ],
      "notes": [
        "对比页列出 Hy3 的 Terminal-Bench 4.0 为 1%；方法页确认 66 项任务、mini-swe-agent、每项任务重复 3 次后按 pass@1 评分，并限制最多 500 步。旧 TOML 的 2.1/Terminus 2（71.7）结果作为另一版本保留。"
      ],
      "status": "已收录",
      "unresolved": []
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T01:40+08:00",
      "checked_sources": [
        {
          "label": "Vals Index leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Tencent Hy3 model card",
          "url": "https://huggingface.co/tencent/Hy3"
        }
      ],
      "notes": [
        "检查当前 Vals Index 2.2 公开榜单，未找到 Hy3 的该版本成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 31,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T01:40+08:00",
  "model_id": "tencent/hy3",
  "new_records": 4,
  "overall_status": "待复核",
  "updated_records": 0
}

-->
