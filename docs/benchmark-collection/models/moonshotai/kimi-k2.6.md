# Kimi K2.6 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：moonshotai/kimi-k2.6
- 模型名称：Kimi K2.6
- 发布日期：2026-04-20
- 最近检查时间：2026-11-05T08:46+08:00
- 整体处理状态：待复核
- 新增成绩数量：3
- 更新成绩数量：1
- 收集前已有成绩数量：5
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 本地已有 5 条成绩记录，均不属于这 11 项目标版本；其中 SWE-Bench Pro hard-aa 与 Terminal-Bench 2.1 不作为 Pro V2 或 Terminal-Bench 4 成绩。
- 本轮新增两条 Moonshot 官方 HLE-Full 结果（无工具和启用工具），以及一条 Chartography 公开榜单原始分数；该分数的 reducer 未在榜单行标明，当前不计入 Benchmark 映射覆盖。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6), [DeepSWE leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T08:37+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Moonshot official Kimi K2.6 model card](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md), [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2) | 2026-11-05T08:37+08:00 |
| terminal-bench-v4 | 待核实 | 64.3 (metric=pass@1; version=2.1; harness=Claude Code) | [Moonshot official Kimi K2.6 model card](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md), [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:37+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6), [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:37+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Kimi K2.6 official API quickstart](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart), [AutomationBench leaderboard](https://zapier.com/benchmarks), [AutomationBench project](https://github.com/zapier/AutomationBench) | 2026-11-05T08:37+08:00 |
| osworld-v2.1 | 待核实 | — | [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6), [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/), [OSWorld V2.1 release notes](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1) | 2026-11-05T08:37+08:00 |
| chartography | 待核实 | 12.2 (dataset=Chartography full task set (100 tasks); variant=Thinking on; harness=Inspect AI Chartography harness; leaderboard configuration: 10 runs per task, Gemini 3.5 Flash judge) | [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Official Chartography benchmark harness and scoring protocol](https://github.com/surge-ai/chartography) | 2026-11-05T08:42+08:00 |
| humanitys-last-exam | 已收录 | 34.7 (metric=accuracy; dataset=HLE-Full; variant=Thinking mode enabled; no tools; maximum generation length 98,304 tokens); 54.0 (metric=accuracy; dataset=HLE-Full; variant=Thinking mode enabled; search, code-interpreter, and web-browsing tools; maximum generation length 262,144 tokens; per-step limit 49,152 tokens; retain only the most recent round of tool-related messages after context threshold) | [Moonshot official Kimi K2.6 model card](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md), [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:37+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact-model profile (current Intelligence Index V5.0.1 section)](https://artificialanalysis.ai/models/kimi-k2-6), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Kimi K2.6 Artificial Analysis article (older Index result)](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model) | 2026-11-05T08:46+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [GDPval-AA V2.1 definition](https://artificialanalysis.ai/evaluations/gdpval-aa), [Kimi K2.6 AA comparison page](https://artificialanalysis.ai/models/comparisons/kimi-k2-6-vs-kimi-k2-6-non-reasoning), [Kimi K2.6 Artificial Analysis article](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model) | 2026-11-05T08:37+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Kimi K2.6 Vals model page](https://www.vals.ai/models/kimi_kimi-k2.6), [Older Vals Index page](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T08:37+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6)
- [DeepSWE leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- DeepSWE leaderboard view is partial; no directly verifiable Kimi K2.6 v1.1 row was established.

尚未解决的问题：
- DeepSWE leaderboard view is partial; no directly verifiable Kimi K2.6 v1.1 row was established.

最近核验时间：2026-11-05T08:37+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Moonshot official Kimi K2.6 model card](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md)
- [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2)

研究备注：
- Kimi materials show an unversioned SWE-Bench Pro result of 58.6 under a SWE-agent-derived harness; the local 27.3 row is hard-aa/Claude Code. Neither is identified as Pro V2, which was released later.

尚未解决的问题：
- Kimi materials show an unversioned SWE-Bench Pro result of 58.6 under a SWE-agent-derived harness; the local 27.3 row is hard-aa/Claude Code. Neither is identified as Pro V2, which was released later.

最近核验时间：2026-11-05T08:37+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 64.3
- metric: pass@1
- version: 2.1
- harness: Claude Code
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Moonshot official Kimi K2.6 model card](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md)
- [Terminal-Bench 4.0 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Kimi materials show Terminal-Bench 2.0 at 66.7 with Terminus-2; the local 64.3 row is version 2.1/Claude Code. Neither maps to target version 4.0.

尚未解决的问题：
- Kimi materials show Terminal-Bench 2.0 at 66.7 with Terminus-2; the local 64.3 row is version 2.1/Claude Code. Neither maps to target version 4.0.

最近核验时间：2026-11-05T08:37+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6)
- [Terminal-Bench Science benchmark page](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- No exact Kimi K2.6 Terminal-Bench Science v0.1 result was verified; a dynamic leaderboard absence alone is insufficient to mark not found.

尚未解决的问题：
- No exact Kimi K2.6 Terminal-Bench Science v0.1 result was verified; a dynamic leaderboard absence alone is insufficient to mark not found.

最近核验时间：2026-11-05T08:37+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Kimi K2.6 official API quickstart](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart)
- [AutomationBench leaderboard](https://zapier.com/benchmarks)
- [AutomationBench project](https://github.com/zapier/AutomationBench)

研究备注：
- Official API supports tool calling and the task type is applicable, but no exact AutomationBench 1.0.6 result was verified. The leaderboard shows only partial entries.

尚未解决的问题：
- Official API supports tool calling and the task type is applicable, but no exact AutomationBench 1.0.6 result was verified. The leaderboard shows only partial entries.

最近核验时间：2026-11-05T08:37+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Kimi K2.6 official technical post](https://www.kimi.ai/blog/kimi-k2-6)
- [OSWorld V2.1 benchmark](https://osworld-v2.xlang.ai/)
- [OSWorld V2.1 release notes](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)

研究备注：
- Kimi materials report OSWorld-Verified, which is not OSWorld 2.1. No target-version score was verified.

尚未解决的问题：
- Kimi materials report OSWorld-Verified, which is not OSWorld 2.1. No target-version score was verified.

最近核验时间：2026-11-05T08:37+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 12.2
- dataset: Chartography full task set (100 tasks)
- variant: Thinking on
- harness: Inspect AI Chartography harness; leaderboard configuration: 10 runs per task, Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Official Chartography benchmark harness and scoring protocol](https://github.com/surge-ai/chartography)

研究备注：
- Surge 榜单直接列出 Kimi K2.6 (Thinking on) 的 12.2%。官方 README 说明完整 100 项任务、每项 10 次运行、Gemini 3.5 Flash judge，并支持 accuracy/mean 与 Pass@10 等 reducers；榜单行未标明所显示数值对应哪个 reducer，因此保留原始分数但暂不映射到本地 metric，覆盖率不计入。未公布评测日期或语义版本。

尚未解决的问题：
- 需确认 Surge 当前排行榜的 12.2% 对应 accuracy/mean (Pass@1) 还是其他 reducer。

最近核验时间：2026-11-05T08:42+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 34.7
- metric: accuracy
- dataset: HLE-Full
- variant: Thinking mode enabled; no tools; maximum generation length 98,304 tokens
- source: [https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 54.0
- metric: accuracy
- dataset: HLE-Full
- variant: Thinking mode enabled; search, code-interpreter, and web-browsing tools; maximum generation length 262,144 tokens; per-step limit 49,152 tokens; retain only the most recent round of tool-related messages after context threshold
- source: [https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Moonshot official Kimi K2.6 model card](https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md)
- [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Moonshot model card directly reports two HLE-Full accuracy results. They are separate no-tools and tool-enabled configurations; card footnotes specify thinking mode, generation limits and tools. No evaluation date is stated, so date is omitted.

最近核验时间：2026-11-05T08:37+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact-model profile (current Intelligence Index V5.0.1 section)](https://artificialanalysis.ai/models/kimi-k2-6)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Kimi K2.6 Artificial Analysis article (older Index result)](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)

研究备注：
- Kimi 当前 AA 精确型号页显示 Index N/A，并标明当前索引为 V5.0.1；2026-04 文章的 Index 54 未标 V5，不能映射。V5 使用 HLE-Diamond，亦不能由原始 HLE 分数推出。当前未找到公开 V5 分数。

最近核验时间：2026-11-05T08:46+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [GDPval-AA V2.1 definition](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Kimi K2.6 AA comparison page](https://artificialanalysis.ai/models/comparisons/kimi-k2-6-vs-kimi-k2-6-non-reasoning)
- [Kimi K2.6 Artificial Analysis article](https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model)

研究备注：
- The April article reports Elo 1520 without a V2.1 label. A search cache showed 1038 on a current comparison but the opened page did not show that row; neither value meets direct verification.

尚未解决的问题：
- The April article reports Elo 1520 without a V2.1 label. A search cache showed 1038 on a current comparison but the opened page did not show that row; neither value meets direct verification.

最近核验时间：2026-11-05T08:37+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Kimi K2.6 Vals model page](https://www.vals.ai/models/kimi_kimi-k2.6)
- [Older Vals Index page](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- Current V2.2 page only exposes latest/top/frontier models. Kimi aggregate 56.68% is not version-labeled; older V2 page 43.47% and release post 63.9% have unclear version or page scope. None is mapped to V2.2.

尚未解决的问题：
- Current V2.2 page only exposes latest/top/frontier models. Kimi aggregate 56.68% is not version-labeled; older V2 page 43.47% and release post 63.9% have unclear version or page scope. None is mapped to V2.2.

最近核验时间：2026-11-05T08:37+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:46+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model profile (current Intelligence Index V5.0.1 section)",
          "url": "https://artificialanalysis.ai/models/kimi-k2-6"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Kimi K2.6 Artificial Analysis article (older Index result)",
          "url": "https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model"
        }
      ],
      "notes": [
        "Kimi 当前 AA 精确型号页显示 Index N/A，并标明当前索引为 V5.0.1；2026-04 文章的 Index 54 未标 V5，不能映射。V5 使用 HLE-Diamond，亦不能由原始 HLE 分数推出。当前未找到公开 V5 分数。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Kimi K2.6 official API quickstart",
          "url": "https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart"
        },
        {
          "label": "AutomationBench leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench project",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Official API supports tool calling and the task type is applicable, but no exact AutomationBench 1.0.6 result was verified. The leaderboard shows only partial entries."
      ],
      "status": "待核实",
      "unresolved": [
        "Official API supports tool calling and the task type is applicable, but no exact AutomationBench 1.0.6 result was verified. The leaderboard shows only partial entries."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:42+08:00",
      "checked_sources": [
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Official Chartography benchmark harness and scoring protocol",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Surge 榜单直接列出 Kimi K2.6 (Thinking on) 的 12.2%。官方 README 说明完整 100 项任务、每项 10 次运行、Gemini 3.5 Flash judge，并支持 accuracy/mean 与 Pass@10 等 reducers；榜单行未标明所显示数值对应哪个 reducer，因此保留原始分数但暂不映射到本地 metric，覆盖率不计入。未公布评测日期或语义版本。"
      ],
      "status": "待核实",
      "unresolved": [
        "需确认 Surge 当前排行榜的 12.2% 对应 accuracy/mean (Pass@1) 还是其他 reducer。"
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Kimi K2.6 official technical post",
          "url": "https://www.kimi.ai/blog/kimi-k2-6"
        },
        {
          "label": "DeepSWE leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "DeepSWE leaderboard view is partial; no directly verifiable Kimi K2.6 v1.1 row was established."
      ],
      "status": "待核实",
      "unresolved": [
        "DeepSWE leaderboard view is partial; no directly verifiable Kimi K2.6 v1.1 row was established."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "GDPval-AA V2.1 definition",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Kimi K2.6 AA comparison page",
          "url": "https://artificialanalysis.ai/models/comparisons/kimi-k2-6-vs-kimi-k2-6-non-reasoning"
        },
        {
          "label": "Kimi K2.6 Artificial Analysis article",
          "url": "https://artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model"
        }
      ],
      "notes": [
        "The April article reports Elo 1520 without a V2.1 label. A search cache showed 1038 on a current comparison but the opened page did not show that row; neither value meets direct verification."
      ],
      "status": "待核实",
      "unresolved": [
        "The April article reports Elo 1520 without a V2.1 label. A search cache showed 1038 on a current comparison but the opened page did not show that row; neither value meets direct verification."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Moonshot official Kimi K2.6 model card",
          "url": "https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md"
        },
        {
          "label": "Humanity's Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Moonshot model card directly reports two HLE-Full accuracy results. They are separate no-tools and tool-enabled configurations; card footnotes specify thinking mode, generation limits and tools. No evaluation date is stated, so date is omitted."
      ],
      "status": "已收录",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Kimi K2.6 official technical post",
          "url": "https://www.kimi.ai/blog/kimi-k2-6"
        },
        {
          "label": "OSWorld V2.1 benchmark",
          "url": "https://osworld-v2.xlang.ai/"
        },
        {
          "label": "OSWorld V2.1 release notes",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        }
      ],
      "notes": [
        "Kimi materials report OSWorld-Verified, which is not OSWorld 2.1. No target-version score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "Kimi materials report OSWorld-Verified, which is not OSWorld 2.1. No target-version score was verified."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Moonshot official Kimi K2.6 model card",
          "url": "https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md"
        },
        {
          "label": "Kimi K2.6 official technical post",
          "url": "https://www.kimi.ai/blog/kimi-k2-6"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2"
        }
      ],
      "notes": [
        "Kimi materials show an unversioned SWE-Bench Pro result of 58.6 under a SWE-agent-derived harness; the local 27.3 row is hard-aa/Claude Code. Neither is identified as Pro V2, which was released later."
      ],
      "status": "待核实",
      "unresolved": [
        "Kimi materials show an unversioned SWE-Bench Pro result of 58.6 under a SWE-agent-derived harness; the local 27.3 row is hard-aa/Claude Code. Neither is identified as Pro V2, which was released later."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Kimi K2.6 official technical post",
          "url": "https://www.kimi.ai/blog/kimi-k2-6"
        },
        {
          "label": "Terminal-Bench Science benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "No exact Kimi K2.6 Terminal-Bench Science v0.1 result was verified; a dynamic leaderboard absence alone is insufficient to mark not found."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Kimi K2.6 Terminal-Bench Science v0.1 result was verified; a dynamic leaderboard absence alone is insufficient to mark not found."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Moonshot official Kimi K2.6 model card",
          "url": "https://huggingface.co/moonshotai/Kimi-K2.6/raw/main/README.md"
        },
        {
          "label": "Terminal-Bench 4.0 benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Kimi materials show Terminal-Bench 2.0 at 66.7 with Terminus-2; the local 64.3 row is version 2.1/Claude Code. Neither maps to target version 4.0."
      ],
      "status": "待核实",
      "unresolved": [
        "Kimi materials show Terminal-Bench 2.0 at 66.7 with Terminus-2; the local 64.3 row is version 2.1/Claude Code. Neither maps to target version 4.0."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:37+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Kimi K2.6 Vals model page",
          "url": "https://www.vals.ai/models/kimi_kimi-k2.6"
        },
        {
          "label": "Older Vals Index page",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "Current V2.2 page only exposes latest/top/frontier models. Kimi aggregate 56.68% is not version-labeled; older V2 page 43.47% and release post 63.9% have unclear version or page scope. None is mapped to V2.2."
      ],
      "status": "待核实",
      "unresolved": [
        "Current V2.2 page only exposes latest/top/frontier models. Kimi aggregate 56.68% is not version-labeled; older V2 page 43.47% and release post 63.9% have unclear version or page scope. None is mapped to V2.2."
      ]
    }
  },
  "existing_records": 5,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:46+08:00",
  "model_id": "moonshotai/kimi-k2.6",
  "model_notes": [
    "本地已有 5 条成绩记录，均不属于这 11 项目标版本；其中 SWE-Bench Pro hard-aa 与 Terminal-Bench 2.1 不作为 Pro V2 或 Terminal-Bench 4 成绩。",
    "本轮新增两条 Moonshot 官方 HLE-Full 结果（无工具和启用工具），以及一条 Chartography 公开榜单原始分数；该分数的 reducer 未在榜单行标明，当前不计入 Benchmark 映射覆盖。"
  ],
  "new_records": 3,
  "overall_status": "待复核",
  "updated_records": 1
}

-->
