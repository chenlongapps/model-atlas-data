# Claude Opus 4.7 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-opus-4-7
- 模型名称：Claude Opus 4.7
- 发布日期：2026-04-16
- 最近检查时间：2026-11-05T08:57+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 更新成绩数量：2
- 收集前已有成绩数量：19
- 当前已收录的对应成绩数量：2

## 模型身份与范围说明

- 原有两条 HLE 数值 46.9 与 54.7 保留；source 更新为 Anthropic 官方 System Card，补入完整 HLE 数据集与官方测试条件，并移除来源文章发布日期（不是已证实的评测日期）。
- 新增一条 Chartography 榜单原始分数 16.5（Adaptive/Max）；榜单未说明 reducer，故未填 metric、未计入覆盖。
- 其余历史编码和 OSWorld-Verified 结果的版本不匹配，不映射到目标版本。

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 待核实 | — | [DeepSWE v1.1 benchmark page](https://deepswe.datacurve.ai/blog/deepswe-v1-1), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/) | 2026-11-05T08:57+08:00 |
| swe-bench-pro-v2 | 待核实 | — | [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf), [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) | 2026-11-05T08:57+08:00 |
| terminal-bench-v4 | 待核实 | 66.1 (metric=success rate; version=2.1; harness=Terminus-2); 73.8 (metric=pass@1; version=2.1; variant=max; harness=Claude Code); 70.6 (metric=pass@1; version=2.1; variant=medium; harness=Cursor CLI); 71.4 (metric=pass@1; version=2.1; variant=medium; harness=Claude Code) | [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf), [Terminal-Bench 4 leaderboard](https://snorkel.ai/leaderboard/terminal-bench/), [Terminal-Bench 4 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-05T08:57+08:00 |
| terminal-bench-science-v0.1 | 待核实 | — | [Terminal-Bench Science v0.1 leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/), [Terminal-Bench Science benchmark](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-05T08:57+08:00 |
| automationbench-v1.0.6 | 待核实 | — | [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks), [AutomationBench official repository](https://github.com/zapier/AutomationBench) | 2026-11-05T08:57+08:00 |
| osworld-v2.1 | 待核实 | — | [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf), [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1), [OSWorld results page](https://osworld-v2.xlang.ai/) | 2026-11-05T08:57+08:00 |
| chartography | 待核实 | 16.5 (dataset=Chartography full task set (100 tasks); variant=Adaptive/Max; harness=Inspect AI Chartography harness; leaderboard configuration: 10 runs per task, Gemini 3.5 Flash judge) | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Official Chartography harness and scoring protocol](https://github.com/surge-ai/chartography) | 2026-11-05T08:57+08:00 |
| humanitys-last-exam | 已存在 | 46.9 (metric=accuracy; dataset=HLE full set (2,500 questions); effort=max; variant=no tools; thinking=auto; 1M total-token cap across contexts; no context compaction; harness=Reasoning-only; Claude Opus 4.6 grader); 54.7 (metric=accuracy; dataset=HLE full set (2,500 questions); effort=max; variant=with web search, web fetch, programmatic tool calling, and code execution; thinking=auto; 1M total-token cap across contexts; no context compaction; harness=Claude Opus 4.6 grader) | [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf), [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-05T08:57+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis exact-model profile (current Index V5.0.1 section)](https://artificialanalysis.ai/models/claude-opus-4-7), [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis Opus 4.7 analysis](https://artificialanalysis.ai/articles/opus-4-7-everything-you-need-to-know/) | 2026-11-05T08:57+08:00 |
| gdpval-aa-v2.1 | 待核实 | — | [Artificial Analysis Opus 4.7 analysis](https://artificialanalysis.ai/articles/opus-4-7-everything-you-need-to-know/), [GDPval-AA V2.1 leaderboard and definition](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis Intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-05T08:57+08:00 |
| vals-index-v2.2 | 待核实 | — | [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Older Vals Index V2 page](https://www.vals.ai/benchmarks/vals_index_v2) | 2026-11-05T08:57+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 当前状态：待核实。

已检查的主要资料：
- [DeepSWE v1.1 benchmark page](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)

研究备注：
- Current visible v1.1 board does not expose an exact Opus 4.7 row. A previous snapshot reports 54% ± 5% (max, mini-swe-agent) before v1.1 and cannot be mapped to the target revision.

尚未解决的问题：
- Current visible v1.1 board does not expose an exact Opus 4.7 row. A previous snapshot reports 54% ± 5% (max, mini-swe-agent) before v1.1 and cannot be mapped to the target revision.

最近核验时间：2026-11-05T08:57+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 当前状态：待核实。

已检查的主要资料：
- [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf)
- [SWE-bench Pro V2 leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)

研究备注：
- Local records include 64.3 resolve rate without a V2 tag and 44.9 pass@1 on hard-aa; the system card’s SWE-Bench Pro result is also not labeled V2. The V2 refresh uses 642 tasks and cannot be inferred from these rows.

尚未解决的问题：
- Local records include 64.3 resolve rate without a V2 tag and 44.9 pass@1 on hard-aa; the system card’s SWE-Bench Pro result is also not labeled V2. The V2 refresh uses 642 tasks and cannot be inferred from these rows.

最近核验时间：2026-11-05T08:57+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 66.1
- metric: success rate
- version: 2.1
- harness: Terminus-2
- source: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)
- date: 2026-05-28
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 73.8
- metric: pass@1
- version: 2.1
- variant: max
- harness: Claude Code
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 70.6
- metric: pass@1
- version: 2.1
- variant: medium
- harness: Cursor CLI
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 71.4
- metric: pass@1
- version: 2.1
- variant: medium
- harness: Claude Code
- source: [https://artificialanalysis.ai/agents/coding-agents](https://artificialanalysis.ai/agents/coding-agents)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf)
- [Terminal-Bench 4 leaderboard](https://snorkel.ai/leaderboard/terminal-bench/)
- [Terminal-Bench 4 benchmark page](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Local rows are Terminal-Bench 2.1 under multiple harnesses. The system card reports Terminal-Bench 2.0 at 69.4; none is version 4.0.

尚未解决的问题：
- Local rows are Terminal-Bench 2.1 under multiple harnesses. The system card reports Terminal-Bench 2.0 at 69.4; none is version 4.0.

最近核验时间：2026-11-05T08:57+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 当前状态：待核实。

已检查的主要资料：
- [Terminal-Bench Science v0.1 leaderboard](https://snorkel.ai/leaderboard/terminal-bench-science/)
- [Terminal-Bench Science benchmark](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- No exact Opus 4.7 Terminal-Bench Science v0.1 result was verified. The current visible board does not establish that no result exists.

尚未解决的问题：
- No exact Opus 4.7 Terminal-Bench Science v0.1 result was verified. The current visible board does not establish that no result exists.

最近核验时间：2026-11-05T08:57+08:00

### AutomationBench (automationbench-v1.0.6)

- 当前状态：待核实。

已检查的主要资料：
- [Zapier AutomationBench 1.0.6 leaderboard](https://zapier.com/benchmarks)
- [AutomationBench official repository](https://github.com/zapier/AutomationBench)

研究备注：
- Model is capable of multimodal tool/agent work, but the public leaderboard displays only 10 entries and folds another 119; no exact score was verified.

尚未解决的问题：
- Model is capable of multimodal tool/agent work, but the public leaderboard displays only 10 entries and folds another 119; no exact score was verified.

最近核验时间：2026-11-05T08:57+08:00

### OSWorld (osworld-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf)
- [OSWorld V2.1 release](https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1)
- [OSWorld results page](https://osworld-v2.xlang.ai/)

研究备注：
- The system card/local record includes OSWorld-Verified 78.0 and an OSWorld 2.0 page reports 18.2; neither is OSWorld 2.1. No v2.1 score was verified.

尚未解决的问题：
- The system card/local record includes OSWorld-Verified 78.0 and an OSWorld 2.0 page reports 18.2; neither is OSWorld 2.1. No v2.1 score was verified.

最近核验时间：2026-11-05T08:57+08:00

### Chartography (chartography)

#### 源 TOML 成绩记录 1

- name: Chartography
- score: 16.5
- dataset: Chartography full task set (100 tasks)
- variant: Adaptive/Max
- harness: Inspect AI Chartography harness; leaderboard configuration: 10 runs per task, Gemini 3.5 Flash judge
- source: [https://surgehq.ai/benchmarks/chartography](https://surgehq.ai/benchmarks/chartography)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Official Chartography harness and scoring protocol](https://github.com/surge-ai/chartography)

研究备注：
- Leaderboard directly lists Claude Opus 4.7 (Adaptive/Max) at 16.5%. The page row does not identify the reducer; the harness allows accuracy/mean and Pass@10, so raw score is retained without metric and excluded from mapped coverage. The official README specifies 100 tasks, 10 runs/task, Gemini 3.5 Flash judge. No eval date/semantic version is published.

尚未解决的问题：
- Leaderboard directly lists Claude Opus 4.7 (Adaptive/Max) at 16.5%. The page row does not identify the reducer; the harness allows accuracy/mean and Pass@10, so raw score is retained without metric and excluded from mapped coverage. The official README specifies 100 tasks, 10 runs/task, Gemini 3.5 Flash judge. No eval date/semantic version is published.

最近核验时间：2026-11-05T08:57+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 46.9
- metric: accuracy
- dataset: HLE full set (2,500 questions)
- effort: max
- variant: no tools; thinking=auto; 1M total-token cap across contexts; no context compaction
- harness: Reasoning-only; Claude Opus 4.6 grader
- source: [https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf)
- 本地 Benchmark 定义映射：已匹配

#### 源 TOML 成绩记录 2

- name: Humanity's Last Exam
- score: 54.7
- metric: accuracy
- dataset: HLE full set (2,500 questions)
- effort: max
- variant: with web search, web fetch, programmatic tool calling, and code execution; thinking=auto; 1M total-token cap across contexts; no context compaction
- harness: Claude Opus 4.6 grader
- source: [https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf)
- 本地 Benchmark 定义映射：已匹配

已检查的主要资料：
- [Anthropic Claude Opus 4.7 official system card](https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf)
- [Humanity's Last Exam definition](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- Anthropic system card directly supports both existing full-set accuracy scores: 46.9 no tools and 54.7 with web search, web fetch, programmatic tool calling and code execution. Both use max effort, thinking=auto, 1M total token cap, no compaction, with Opus 4.6 grader. Existing publication date was removed because it is not an evaluation date.

最近核验时间：2026-11-05T08:57+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis exact-model profile (current Index V5.0.1 section)](https://artificialanalysis.ai/models/claude-opus-4-7)
- [Artificial Analysis Index V5 definition](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis Opus 4.7 analysis](https://artificialanalysis.ai/articles/opus-4-7-everything-you-need-to-know/)

研究备注：
- Current exact-model profile shows Index N/A for V5.0.1. Older article score 57.3 (rounded 57) is a prior Index and not mapped to V5.

最近核验时间：2026-11-05T08:57+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 当前状态：待核实。

已检查的主要资料：
- [Artificial Analysis Opus 4.7 analysis](https://artificialanalysis.ai/articles/opus-4-7-everything-you-need-to-know/)
- [GDPval-AA V2.1 leaderboard and definition](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis Intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- AA article reports 1,753 Elo for Opus 4.7 Adaptive Reasoning/Max Effort but does not label the benchmark version. V2.1 changed the Elo anchor and fitting, so this cannot be mapped to V2.1.

尚未解决的问题：
- AA article reports 1,753 Elo for Opus 4.7 Adaptive Reasoning/Max Effort but does not label the benchmark version. V2.1 changed the Elo anchor and fitting, so this cannot be mapped to V2.1.

最近核验时间：2026-11-05T08:57+08:00

### Vals Index (vals-index-v2.2)

- 当前状态：待核实。

已检查的主要资料：
- [Vals Index V2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Older Vals Index V2 page](https://www.vals.ai/benchmarks/vals_index_v2)

研究备注：
- The V2.2 page shows a selected latest/top/frontier list and no visible Opus 4.7 row. Older V1 72.21%, V1.1 66.10%, and V2 56.11% are not mapped to V2.2.

尚未解决的问题：
- The V2.2 page shows a selected latest/top/frontier list and no visible Opus 4.7 row. Older V1 72.21%, V1.1 66.10%, and V2 56.11% are not mapped to V2.2.

最近核验时间：2026-11-05T08:57+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis exact-model profile (current Index V5.0.1 section)",
          "url": "https://artificialanalysis.ai/models/claude-opus-4-7"
        },
        {
          "label": "Artificial Analysis Index V5 definition",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis Opus 4.7 analysis",
          "url": "https://artificialanalysis.ai/articles/opus-4-7-everything-you-need-to-know/"
        }
      ],
      "notes": [
        "Current exact-model profile shows Index N/A for V5.0.1. Older article score 57.3 (rounded 57) is a prior Index and not mapped to V5."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Zapier AutomationBench 1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench official repository",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Model is capable of multimodal tool/agent work, but the public leaderboard displays only 10 entries and folds another 119; no exact score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "Model is capable of multimodal tool/agent work, but the public leaderboard displays only 10 entries and folds another 119; no exact score was verified."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Official Chartography harness and scoring protocol",
          "url": "https://github.com/surge-ai/chartography"
        }
      ],
      "notes": [
        "Leaderboard directly lists Claude Opus 4.7 (Adaptive/Max) at 16.5%. The page row does not identify the reducer; the harness allows accuracy/mean and Pass@10, so raw score is retained without metric and excluded from mapped coverage. The official README specifies 100 tasks, 10 runs/task, Gemini 3.5 Flash judge. No eval date/semantic version is published."
      ],
      "status": "待核实",
      "unresolved": [
        "Leaderboard directly lists Claude Opus 4.7 (Adaptive/Max) at 16.5%. The page row does not identify the reducer; the harness allows accuracy/mean and Pass@10, so raw score is retained without metric and excluded from mapped coverage. The official README specifies 100 tasks, 10 runs/task, Gemini 3.5 Flash judge. No eval date/semantic version is published."
      ]
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "DeepSWE v1.1 benchmark page",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        }
      ],
      "notes": [
        "Current visible v1.1 board does not expose an exact Opus 4.7 row. A previous snapshot reports 54% ± 5% (max, mini-swe-agent) before v1.1 and cannot be mapped to the target revision."
      ],
      "status": "待核实",
      "unresolved": [
        "Current visible v1.1 board does not expose an exact Opus 4.7 row. A previous snapshot reports 54% ± 5% (max, mini-swe-agent) before v1.1 and cannot be mapped to the target revision."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Opus 4.7 analysis",
          "url": "https://artificialanalysis.ai/articles/opus-4-7-everything-you-need-to-know/"
        },
        {
          "label": "GDPval-AA V2.1 leaderboard and definition",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis Intelligence benchmarking methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "AA article reports 1,753 Elo for Opus 4.7 Adaptive Reasoning/Max Effort but does not label the benchmark version. V2.1 changed the Elo anchor and fitting, so this cannot be mapped to V2.1."
      ],
      "status": "待核实",
      "unresolved": [
        "AA article reports 1,753 Elo for Opus 4.7 Adaptive Reasoning/Max Effort but does not label the benchmark version. V2.1 changed the Elo anchor and fitting, so this cannot be mapped to V2.1."
      ]
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Claude Opus 4.7 official system card",
          "url": "https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf"
        },
        {
          "label": "Humanity's Last Exam definition",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "Anthropic system card directly supports both existing full-set accuracy scores: 46.9 no tools and 54.7 with web search, web fetch, programmatic tool calling and code execution. Both use max effort, thinking=auto, 1M total token cap, no compaction, with Opus 4.6 grader. Existing publication date was removed because it is not an evaluation date."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Claude Opus 4.7 official system card",
          "url": "https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf"
        },
        {
          "label": "OSWorld V2.1 release",
          "url": "https://github.com/xlang-ai/OSWorld-V2/releases/tag/osworld-v2.1"
        },
        {
          "label": "OSWorld results page",
          "url": "https://osworld-v2.xlang.ai/"
        }
      ],
      "notes": [
        "The system card/local record includes OSWorld-Verified 78.0 and an OSWorld 2.0 page reports 18.2; neither is OSWorld 2.1. No v2.1 score was verified."
      ],
      "status": "待核实",
      "unresolved": [
        "The system card/local record includes OSWorld-Verified 78.0 and an OSWorld 2.0 page reports 18.2; neither is OSWorld 2.1. No v2.1 score was verified."
      ]
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Claude Opus 4.7 official system card",
          "url": "https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf"
        },
        {
          "label": "SWE-bench Pro V2 leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        }
      ],
      "notes": [
        "Local records include 64.3 resolve rate without a V2 tag and 44.9 pass@1 on hard-aa; the system card’s SWE-Bench Pro result is also not labeled V2. The V2 refresh uses 642 tasks and cannot be inferred from these rows."
      ],
      "status": "待核实",
      "unresolved": [
        "Local records include 64.3 resolve rate without a V2 tag and 44.9 pass@1 on hard-aa; the system card’s SWE-Bench Pro result is also not labeled V2. The V2 refresh uses 642 tasks and cannot be inferred from these rows."
      ]
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Terminal-Bench Science v0.1 leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench-science/"
        },
        {
          "label": "Terminal-Bench Science benchmark",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "No exact Opus 4.7 Terminal-Bench Science v0.1 result was verified. The current visible board does not establish that no result exists."
      ],
      "status": "待核实",
      "unresolved": [
        "No exact Opus 4.7 Terminal-Bench Science v0.1 result was verified. The current visible board does not establish that no result exists."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Claude Opus 4.7 official system card",
          "url": "https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf"
        },
        {
          "label": "Terminal-Bench 4 leaderboard",
          "url": "https://snorkel.ai/leaderboard/terminal-bench/"
        },
        {
          "label": "Terminal-Bench 4 benchmark page",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Local rows are Terminal-Bench 2.1 under multiple harnesses. The system card reports Terminal-Bench 2.0 at 69.4; none is version 4.0."
      ],
      "status": "待核实",
      "unresolved": [
        "Local rows are Terminal-Bench 2.1 under multiple harnesses. The system card reports Terminal-Bench 2.0 at 69.4; none is version 4.0."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-05T08:57+08:00",
      "checked_sources": [
        {
          "label": "Vals Index V2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Older Vals Index V2 page",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2"
        }
      ],
      "notes": [
        "The V2.2 page shows a selected latest/top/frontier list and no visible Opus 4.7 row. Older V1 72.21%, V1.1 66.10%, and V2 56.11% are not mapped to V2.2."
      ],
      "status": "待核实",
      "unresolved": [
        "The V2.2 page shows a selected latest/top/frontier list and no visible Opus 4.7 row. Older V1 72.21%, V1.1 66.10%, and V2 56.11% are not mapped to V2.2."
      ]
    }
  },
  "existing_records": 19,
  "first_pass_completed": true,
  "last_checked": "2026-11-05T08:57+08:00",
  "model_id": "anthropic/claude-opus-4-7",
  "model_notes": [
    "原有两条 HLE 数值 46.9 与 54.7 保留；source 更新为 Anthropic 官方 System Card，补入完整 HLE 数据集与官方测试条件，并移除来源文章发布日期（不是已证实的评测日期）。",
    "新增一条 Chartography 榜单原始分数 16.5（Adaptive/Max）；榜单未说明 reducer，故未填 metric、未计入覆盖。",
    "其余历史编码和 OSWorld-Verified 结果的版本不匹配，不映射到目标版本。"
  ],
  "new_records": 1,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
