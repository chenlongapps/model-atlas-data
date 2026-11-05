# GLM-5.3 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：zhipuai/glm-5.3
- 模型名称：GLM-5.3
- 发布日期：2026-08-14
- 最近检查时间：2026-11-04T17:25+08:00
- 整体处理状态：待复核
- 新增成绩数量：7
- 更新成绩数量：2
- 收集前已有成绩数量：17
- 当前已收录的对应成绩数量：2

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 冲突 | 66.9 (metric=resolved; version=1.1; effort=max; variant=temperature=0.95; top_p=1.0; 6h timeout; 400K context; harness=mini-swe-agent); 69.0 (metric=pass rate; version=1.1; dataset=113 tasks; effort=max; variant=uncertainty ±3 percentage points; leaderboard configuration details not stated) | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T17:25+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [Scale SWE-bench Pro leaderboard](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) | 2026-11-04T17:25+08:00 |
| terminal-bench-v4 | 冲突 | 88.2 (metric=pass@1; version=2.1; variant=max effort; harness=Claude Code 2.1.207); 28.3 (metric=avg@3; version=3.0; variant=max effort; harness=Claude Code 2.1.207); 41.9 (metric=pass@1; version=4.0.0; dataset=66 tasks; effort=max; variant=average over three repeats; harness=mini-swe-agent); 38.89 (metric=accuracy; version=4.0; harness=Mini-SWE-agent) | [Artificial Analysis Terminal-Bench 4.0 evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Hugging Face GLM-5.3 evaluation-result record](https://huggingface.co/zai-org/GLM-5.3/discussions/32), [Vals AI Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4) | 2026-11-04T17:25+08:00 |
| terminal-bench-science-v0.1 | 冲突 | 9.5 (metric=pass@1; version=0.1.0; dataset=70 tasks; effort=max; variant=average over three repeats; harness=mini-swe-agent); 5.71 (metric=accuracy; version=0.1.0; harness=Mini-SWE-agent) | [Artificial Analysis Terminal-Bench-Science 0.1 evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science), [Hugging Face GLM-5.3 evaluation-result record](https://huggingface.co/zai-org/GLM-5.3/discussions/32), [Vals AI Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T17:25+08:00 |
| automationbench-v1.0.6 | 待核实 | 48.2 (metric=pass@1; version=1.0.6; variant=max effort) | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [Zapier AutomationBench benchmark](https://zapier.com/benchmarks) | 2026-11-04T17:25+08:00 |
| osworld-v2.1 | 未找到 | — | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [OSWorld v2.1 official release JSON](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [OSWorld official repository](https://github.com/xlang-ai/OSWorld-V2) | 2026-11-04T17:25+08:00 |
| chartography | 未找到 | — | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography) | 2026-11-04T17:25+08:00 |
| humanitys-last-exam | 已存在 | 62.5 (metric=accuracy; effort=max; variant=with tools; temperature=1.0; top_p=0.95; max generation length=163840; max context length=300000; judge=GPT-5.6-Luna (medium)) | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [Humanity's Last Exam official site](https://lastexam.ai/) | 2026-11-04T17:25+08:00 |
| artificial-analysis-intelligence-index-v5 | 待核实 | 32 (metric=index score; version=5.0.1; effort=max) | [Artificial Analysis GLM-5.3 model profile](https://artificialanalysis.ai/models/glm-5-3) | 2026-11-04T17:25+08:00 |
| gdpval-aa-v2.1 | 未找到 | 1769 (metric=Elo; version=2; variant=max effort) | [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3), [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) | 2026-11-04T17:25+08:00 |
| vals-index-v2.2 | 已收录 | 59.73 (metric=performance score; version=2.2) | [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index) | 2026-11-04T17:25+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

#### 源 TOML 成绩记录 1

- name: DeepSWE
- score: 66.9
- metric: resolved
- version: 1.1
- effort: max
- variant: temperature=0.95; top_p=1.0; 6h timeout; 400K context
- harness: mini-swe-agent
- source: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: DeepSWE
- score: 69.0
- metric: pass rate
- version: 1.1
- dataset: 113 tasks
- effort: max
- variant: uncertainty ±3 percentage points; leaderboard configuration details not stated
- source: [https://deepswe.datacurve.ai/blog/deepswe-v1-1](https://deepswe.datacurve.ai/blog/deepswe-v1-1)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [DeepSWE v1.1 official leaderboard](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- GLM-5.3 model card records 66.9 for DeepSWE v1.1 and documents mini-swe-agent, temperature=0.95, top_p=1.0, six-hour timeout, and 400K context.
- The current DeepSWE leaderboard separately lists glm-5.3[max] at 69% ±3% across its 113-task v1.1 board; it does not expose that row’s harness or full execution settings.

尚未解决的问题：
- Both source results are retained. Their execution conditions are not sufficiently aligned to decide whether the score difference is a revision or a configuration conflict.
- The model-card result does not declare a scoring metric; its existing metric field is retained pending source clarification.

最近核验时间：2026-11-04T17:25+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [Scale SWE-bench Pro leaderboard](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)

研究备注：
- No exact GLM-5.3 result was found on the model card or current Scale SWE-bench Pro V2 leaderboard.

最近核验时间：2026-11-04T17:25+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 88.2
- metric: pass@1
- version: 2.1
- variant: max effort
- harness: Claude Code 2.1.207
- source: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench
- score: 28.3
- metric: avg@3
- version: 3.0
- variant: max effort
- harness: Claude Code 2.1.207
- source: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 3

- name: Terminal-Bench
- score: 41.9
- metric: pass@1
- version: 4.0.0
- dataset: 66 tasks
- effort: max
- variant: average over three repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 4

- name: Terminal-Bench
- score: 38.89
- metric: accuracy
- version: 4.0
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-4](https://www.vals.ai/benchmarks/terminal-bench-4)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Terminal-Bench 4.0 evaluation](https://artificialanalysis.ai/evaluations/terminalbench-4-0)
- [Hugging Face GLM-5.3 evaluation-result record](https://huggingface.co/zai-org/GLM-5.3/discussions/32)
- [Vals AI Terminal-Bench 4.0 leaderboard](https://www.vals.ai/benchmarks/terminal-bench-4)

研究备注：
- Artificial Analysis reports 41.9 for GLM-5.3 (Max), mini-swe-agent, pass@1 averaged over three repeats, on 66 tasks.
- Vals AI separately lists GLM 5.3 at 38.89% with Mini-SWE-agent. Its leaderboard labels the metric accuracy and does not provide repeat details for this row.

尚未解决的问题：
- The two public results differ (41.9 vs 38.89) and use differently described metrics/configuration. Both are retained without selecting a winner.
- The local definition uses task resolution rate, which is not the metric label stated by either source; mapping remains pending.

最近核验时间：2026-11-04T17:25+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench-Science
- score: 9.5
- metric: pass@1
- version: 0.1.0
- dataset: 70 tasks
- effort: max
- variant: average over three repeats
- harness: mini-swe-agent
- source: [https://artificialanalysis.ai/evaluations/terminal-bench-science](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

#### 源 TOML 成绩记录 2

- name: Terminal-Bench-Science
- score: 5.71
- metric: accuracy
- version: 0.1.0
- harness: Mini-SWE-agent
- source: [https://www.vals.ai/benchmarks/terminal-bench-science](https://www.vals.ai/benchmarks/terminal-bench-science)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis Terminal-Bench-Science 0.1 evaluation](https://artificialanalysis.ai/evaluations/terminal-bench-science)
- [Hugging Face GLM-5.3 evaluation-result record](https://huggingface.co/zai-org/GLM-5.3/discussions/32)
- [Vals AI Terminal-Bench-Science leaderboard](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Artificial Analysis reports 9.5 for GLM-5.3 (Max), mini-swe-agent, pass@1 averaged over three repeats, on the 70-task v0.1.0 set.
- Vals AI separately lists GLM 5.3 at 5.71% with Mini-SWE-agent and identifies the upstream v0.1.0 release.

尚未解决的问题：
- The two public results differ (9.5 vs 5.71) despite both naming Mini-SWE-agent; evaluation details are not aligned enough to reconcile them.
- Both sources use metrics not named by the local task resolution rate definition; mapping remains pending.

最近核验时间：2026-11-04T17:25+08:00

### AutomationBench (automationbench-v1.0.6)

#### 源 TOML 成绩记录 1

- name: AutomationBench
- score: 48.2
- metric: pass@1
- version: 1.0.6
- variant: max effort
- source: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [Zapier AutomationBench benchmark](https://zapier.com/benchmarks)

研究备注：
- The model card confirms 48.2 for exact version v1.0.6 and says the evaluation includes the null-type handling fix.
- The model card does not specify the dataset or metric; the existing pass@1 label and whether this is the public or private set remain unconfirmed.

尚未解决的问题：
- Do not treat the existing row as a verified public/private leaderboard result until its metric and dataset are documented.

最近核验时间：2026-11-04T17:25+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [OSWorld v2.1 official release JSON](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [OSWorld official repository](https://github.com/xlang-ai/OSWorld-V2)

研究备注：
- No exact GLM-5.3 result was found in the model card or official OSWorld v2.1 release materials.

最近核验时间：2026-11-04T17:25+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [Surge AI Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)

研究备注：
- No exact GLM-5.3 Chartography result was found. The similar GLM 5.3 Flash row is a different model and was not mapped.

最近核验时间：2026-11-04T17:25+08:00

### Humanity's Last Exam (humanitys-last-exam)

#### 源 TOML 成绩记录 1

- name: Humanity's Last Exam
- score: 62.5
- metric: accuracy
- effort: max
- variant: with tools; temperature=1.0; top_p=0.95; max generation length=163840; max context length=300000; judge=GPT-5.6-Luna (medium)
- source: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [Humanity's Last Exam official site](https://lastexam.ai/)

研究备注：
- The exact GLM-5.3 model-card row is HLE with tools, score 62.5. The official HLE definition uses accuracy.
- The model card documents temperature=1.0, top_p=0.95, max generation length=163840, max context=300000, and GPT-5.6-Luna (medium) judge; it gives no evaluation date.

最近核验时间：2026-11-04T17:25+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

#### 源 TOML 成绩记录 1

- name: Artificial Analysis Intelligence Index
- score: 32
- metric: index score
- version: 5.0.1
- effort: max
- source: [https://artificialanalysis.ai/models/glm-5-3](https://artificialanalysis.ai/models/glm-5-3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Artificial Analysis GLM-5.3 model profile](https://artificialanalysis.ai/models/glm-5-3)

研究备注：
- The GLM-5.3 (Max) profile reports index score 32, effort max, under Artificial Analysis Intelligence Index v5.0.1. The local benchmark definition is v5.0.

尚未解决的问题：
- The source uses method version 5.0.1 while the local definition is version 5.0; the raw row is preserved but not mapped.

最近核验时间：2026-11-04T17:25+08:00

### GDPval-AA (gdpval-aa-v2.1)

#### 源 TOML 成绩记录 1

- name: GDPval-AA
- score: 1769
- metric: Elo
- version: 2
- variant: max effort
- source: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Z.ai GLM-5.3 model card](https://huggingface.co/zai-org/GLM-5.3)
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)

研究备注：
- The model card reports GDPval-AA v2 at 1769 Elo, but no GLM-5.3 result was found for target version v2.1; the v2 score was not mapped.

最近核验时间：2026-11-04T17:25+08:00

### Vals Index (vals-index-v2.2)

#### 源 TOML 成绩记录 1

- name: Vals Index
- score: 59.73
- metric: performance score
- version: 2.2
- source: [https://www.vals.ai/benchmarks/vals_index](https://www.vals.ai/benchmarks/vals_index)
- 本地 Benchmark 定义映射：精确匹配

已检查的主要资料：
- [Vals AI Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)

研究备注：
- The exact GLM 5.3 row reports 59.73% on Vals Index version 2.2. No evaluation date or additional harness conditions are stated.

最近核验时间：2026-11-04T17:25+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GLM-5.3 model profile",
          "url": "https://artificialanalysis.ai/models/glm-5-3"
        }
      ],
      "notes": [
        "The GLM-5.3 (Max) profile reports index score 32, effort max, under Artificial Analysis Intelligence Index v5.0.1. The local benchmark definition is v5.0."
      ],
      "status": "待核实",
      "unresolved": [
        "The source uses method version 5.0.1 while the local definition is version 5.0; the raw row is preserved but not mapped."
      ]
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "Zapier AutomationBench benchmark",
          "url": "https://zapier.com/benchmarks"
        }
      ],
      "notes": [
        "The model card confirms 48.2 for exact version v1.0.6 and says the evaluation includes the null-type handling fix.",
        "The model card does not specify the dataset or metric; the existing pass@1 label and whether this is the public or private set remain unconfirmed."
      ],
      "status": "待核实",
      "unresolved": [
        "Do not treat the existing row as a verified public/private leaderboard result until its metric and dataset are documented."
      ]
    },
    "chartography": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "Surge AI Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        }
      ],
      "notes": [
        "No exact GLM-5.3 Chartography result was found. The similar GLM 5.3 Flash row is a different model and was not mapped."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "DeepSWE v1.1 official leaderboard",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "GLM-5.3 model card records 66.9 for DeepSWE v1.1 and documents mini-swe-agent, temperature=0.95, top_p=1.0, six-hour timeout, and 400K context.",
        "The current DeepSWE leaderboard separately lists glm-5.3[max] at 69% ±3% across its 113-task v1.1 board; it does not expose that row’s harness or full execution settings."
      ],
      "status": "冲突",
      "unresolved": [
        "Both source results are retained. Their execution conditions are not sufficiently aligned to decide whether the score difference is a revision or a configuration conflict.",
        "The model-card result does not declare a scoring metric; its existing metric field is retained pending source clarification."
      ]
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        }
      ],
      "notes": [
        "The model card reports GDPval-AA v2 at 1769 Elo, but no GLM-5.3 result was found for target version v2.1; the v2 score was not mapped."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "Humanity's Last Exam official site",
          "url": "https://lastexam.ai/"
        }
      ],
      "notes": [
        "The exact GLM-5.3 model-card row is HLE with tools, score 62.5. The official HLE definition uses accuracy.",
        "The model card documents temperature=1.0, top_p=0.95, max generation length=163840, max context=300000, and GPT-5.6-Luna (medium) judge; it gives no evaluation date."
      ],
      "status": "已存在",
      "unresolved": []
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "OSWorld v2.1 official release JSON",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "OSWorld official repository",
          "url": "https://github.com/xlang-ai/OSWorld-V2"
        }
      ],
      "notes": [
        "No exact GLM-5.3 result was found in the model card or official OSWorld v2.1 release materials."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Z.ai GLM-5.3 model card",
          "url": "https://huggingface.co/zai-org/GLM-5.3"
        },
        {
          "label": "Scale SWE-bench Pro leaderboard",
          "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
        }
      ],
      "notes": [
        "No exact GLM-5.3 result was found on the model card or current Scale SWE-bench Pro V2 leaderboard."
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Terminal-Bench-Science 0.1 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminal-bench-science"
        },
        {
          "label": "Hugging Face GLM-5.3 evaluation-result record",
          "url": "https://huggingface.co/zai-org/GLM-5.3/discussions/32"
        },
        {
          "label": "Vals AI Terminal-Bench-Science leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Artificial Analysis reports 9.5 for GLM-5.3 (Max), mini-swe-agent, pass@1 averaged over three repeats, on the 70-task v0.1.0 set.",
        "Vals AI separately lists GLM 5.3 at 5.71% with Mini-SWE-agent and identifies the upstream v0.1.0 release."
      ],
      "status": "冲突",
      "unresolved": [
        "The two public results differ (9.5 vs 5.71) despite both naming Mini-SWE-agent; evaluation details are not aligned enough to reconcile them.",
        "Both sources use metrics not named by the local task resolution rate definition; mapping remains pending."
      ]
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Terminal-Bench 4.0 evaluation",
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0"
        },
        {
          "label": "Hugging Face GLM-5.3 evaluation-result record",
          "url": "https://huggingface.co/zai-org/GLM-5.3/discussions/32"
        },
        {
          "label": "Vals AI Terminal-Bench 4.0 leaderboard",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-4"
        }
      ],
      "notes": [
        "Artificial Analysis reports 41.9 for GLM-5.3 (Max), mini-swe-agent, pass@1 averaged over three repeats, on 66 tasks.",
        "Vals AI separately lists GLM 5.3 at 38.89% with Mini-SWE-agent. Its leaderboard labels the metric accuracy and does not provide repeat details for this row."
      ],
      "status": "冲突",
      "unresolved": [
        "The two public results differ (41.9 vs 38.89) and use differently described metrics/configuration. Both are retained without selecting a winner.",
        "The local definition uses task resolution rate, which is not the metric label stated by either source; mapping remains pending."
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T17:25+08:00",
      "checked_sources": [
        {
          "label": "Vals AI Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        }
      ],
      "notes": [
        "The exact GLM 5.3 row reports 59.73% on Vals Index version 2.2. No evaluation date or additional harness conditions are stated."
      ],
      "status": "已收录",
      "unresolved": []
    }
  },
  "existing_records": 17,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T17:25+08:00",
  "model_id": "zhipuai/glm-5.3",
  "new_records": 7,
  "overall_status": "待复核",
  "updated_records": 2
}

-->
