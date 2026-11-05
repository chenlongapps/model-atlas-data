# Claude Mythos 5.1 Benchmark 收集记录

文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。

## 基本信息

- 模型 ID：anthropic/claude-mythos-5-1
- 模型名称：Claude Mythos 5.1
- 发布日期：2026-09-01
- 最近检查时间：2026-11-04T15:03+08:00
- 整体处理状态：待复核
- 新增成绩数量：1
- 收集前已有成绩数量：0
- 当前已收录的对应成绩数量：0

## 11 项 Benchmark 状态

| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |
|---|---|---|---|---|
| deepswe-v1.1 | 未找到 | — | [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/), [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1) | 2026-11-04T15:03+08:00 |
| swe-bench-pro-v2 | 未找到 | — | [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full), [Scale V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2), [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf) | 2026-11-04T15:03+08:00 |
| terminal-bench-v4 | 待核实 | 60.9 (metric=accuracy; version=4.0; dataset=66 tasks; effort=max; variant=10 trials per task; harness=Claude Code --bare) | [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0) | 2026-11-04T15:03+08:00 |
| terminal-bench-science-v0.1 | 未找到 | — | [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [Terminal-Bench Science v0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1), [Vals AI Terminal-Bench Science results](https://www.vals.ai/benchmarks/terminal-bench-science) | 2026-11-04T15:03+08:00 |
| automationbench-v1.0.6 | 未找到 | — | [Anthropic Mythos 5.1 page](https://www.anthropic.com/claude/mythos), [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks), [AutomationBench scoring definition](https://github.com/zapier/AutomationBench) | 2026-11-04T15:03+08:00 |
| osworld-v2.1 | 未找到 | — | [AIB OSWorld 2.1 leaderboard](https://www.aib.vote/en/benchmarks/osworld-2-1), [OSWorld 2.1 XLANG release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json), [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Mythos 5.1 page](https://www.anthropic.com/claude/mythos) | 2026-11-04T15:03+08:00 |
| chartography | 未找到 | — | [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography), [Surge Chartography README and methodology](https://github.com/surge-ai/chartography/blob/main/README.md), [Anthropic Mythos 5.1 page](https://www.anthropic.com/claude/mythos), [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf) | 2026-11-04T15:03+08:00 |
| humanitys-last-exam | 待核实 | — | [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [System card readable transcript mirror](https://malob.github.io/ai-system-cards/anthropic/claude-fable-5-1/), [Artificial Analysis HLE leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 2026-11-04T15:03+08:00 |
| artificial-analysis-intelligence-index-v5 | 未找到 | — | [Artificial Analysis Intelligence Index leaderboard](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), [Artificial Analysis methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | 2026-11-04T15:03+08:00 |
| gdpval-aa-v2.1 | 未找到 | — | [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa), [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf), [Third-party GDPval-AA v2 claim reviewed](https://vectorwire.ai/benchmarks/gdpval-aa-v2) | 2026-11-04T15:03+08:00 |
| vals-index-v2.2 | 未找到 | — | [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index), [Vals Index v2.1 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1) | 2026-11-04T15:03+08:00 |

## 详细研究记录

### DeepSWE (deepswe-v1.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [DeepSWE v1.1 leaderboard](https://deepswe.datacurve.ai/)
- [DeepSWE v1.1 methodology](https://deepswe.datacurve.ai/blog/deepswe-v1-1)

研究备注：
- 系统卡明确给出 67.4% 的是 Fable 5.1；DeepSWE 榜单也未列 Mythos 5.1。两者同底层模型不构成独立评测归属依据。

最近核验时间：2026-11-04T15:03+08:00

### SWE-bench Pro (swe-bench-pro-v2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Scale SWE-bench Pro V2 Full leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)
- [Scale V2 release and protocol](https://labs.scale.com/blog/swe-bench-pro-v2)
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)

研究备注：
- Scale V2 Full 榜单列有 Fable 5.1（Claude Code, high）99.10 ± 0.50，没有 Mythos 5.1 行。系统卡中其他 SWE-bench Pro 结果也明确归属 Fable，且不能据此推成 V2。

最近核验时间：2026-11-04T15:03+08:00

### Terminal-Bench (terminal-bench-v4)

#### 源 TOML 成绩记录 1

- name: Terminal-Bench
- score: 60.9
- metric: accuracy
- version: 4.0
- dataset: 66 tasks
- effort: max
- variant: 10 trials per task
- harness: Claude Code --bare
- source: [https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）

已检查的主要资料：
- [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [Terminal-Bench 4.0 leaderboard](https://www.tbench.ai/?version=4.0)

研究备注：
- Anthropic 公开表明确标注 Claude Mythos 5.1 为 60.9%；系统卡配置为 66 项任务、每项 10 次试验、max thinking effort、Claude Code --bare。没有来源公布实际评测日期，因此未写 date。

尚未解决的问题：
- 模型专属来源将指标称为 accuracy、版本写为 4.0；本地定义为 task resolution rate、4.0.0。原始值按来源保留，精确映射需复核。

最近核验时间：2026-11-04T15:03+08:00

### Terminal-Bench-Science (terminal-bench-science-v0.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [Terminal-Bench Science v0.1 release](https://www.tbench.ai/news/terminal-bench-science-0-1)
- [Vals AI Terminal-Bench Science results](https://www.vals.ai/benchmarks/terminal-bench-science)

研究备注：
- Anthropic 系统卡给出的 52.6% 属于 Fable 5.1；公开官方榜单和 Vals AI 页面未找到 Mythos 5.1 行。未将 Fable 的 70 任务、10 次/任务等条件转给 Mythos。

最近核验时间：2026-11-04T15:03+08:00

### AutomationBench (automationbench-v1.0.6)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Anthropic Mythos 5.1 page](https://www.anthropic.com/claude/mythos)
- [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Zapier AutomationBench v1.0.6 leaderboard](https://zapier.com/benchmarks)
- [AutomationBench scoring definition](https://github.com/zapier/AutomationBench)

研究备注：
- Zapier 官方榜单的 31.4% 是 Fable 5.1 与 Opus 5 fallback 的系统分数；未发现 Mythos 5.1 独立成绩。

最近核验时间：2026-11-04T15:03+08:00

### OSWorld (osworld-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [AIB OSWorld 2.1 leaderboard](https://www.aib.vote/en/benchmarks/osworld-2-1)
- [OSWorld 2.1 XLANG release manifest](https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json)
- [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Mythos 5.1 page](https://www.anthropic.com/claude/mythos)

研究备注：
- AIB 当前 v2.1 榜单未列 Mythos 5.1。Anthropic 发布材料中的 77.9 partial / 41.7 strict 明确属于 Fable 5.1 的 OSWorld 2.0，不能用于 Mythos 或映射为 v2.1 binary completion rate。

最近核验时间：2026-11-04T15:03+08:00

### Chartography (chartography)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Surge Chartography leaderboard](https://surgehq.ai/benchmarks/chartography)
- [Surge Chartography README and methodology](https://github.com/surge-ai/chartography/blob/main/README.md)
- [Anthropic Mythos 5.1 page](https://www.anthropic.com/claude/mythos)
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)

研究备注：
- Surge 榜单没有 Mythos 5.1 行；Anthropic 系统卡列出的 42.6/86.2 与其他 Fable Chartography 数据均明确属于 Fable，配置和 judge 也彼此不同，未转录给 Mythos。

最近核验时间：2026-11-04T15:03+08:00

### Humanity's Last Exam (humanitys-last-exam)

- 当前状态：待核实。

已检查的主要资料：
- [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [System card readable transcript mirror](https://malob.github.io/ai-system-cards/anthropic/claude-fable-5-1/)
- [Artificial Analysis HLE leaderboard](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

研究备注：
- AA 榜单仅找到 Fable 5.1 行。Anthropic System Card 摘要表把 HLE 列为 “Fable 5.1 / Mythos 5.1”，但详细方法段明确说明评测对象是 Fable 5.1，未说明 Mythos API 单独运行；故未把 60.9%/65% 写入 Mythos TOML。

尚未解决的问题：
- 摘要表的合并标签与详细测试对象描述不一致，无法确认是否存在单独的 Mythos 5.1 HLE 成绩；等待更明确的官方说明。

最近核验时间：2026-11-04T15:03+08:00

### Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis Intelligence Index leaderboard](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis methodology and version history](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

研究备注：
- 当前 Artificial Analysis 页面显示 Intelligence Index v5.0.1；没有找到 Mythos 5.1 行。仓库目标为 v5.0，未将任何其他模型或版本结果映射到 Mythos。

最近核验时间：2026-11-04T15:03+08:00

### GDPval-AA (gdpval-aa-v2.1)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Artificial Analysis GDPval-AA v2.1 leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa)
- [Artificial Analysis GDPval-AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa)
- [Anthropic Fable and Mythos 5.1 release results](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Anthropic Fable/Mythos 5.1 system card](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)
- [Third-party GDPval-AA v2 claim reviewed](https://vectorwire.ai/benchmarks/gdpval-aa-v2)

研究备注：
- AA v2.1 榜单列出 Fable 5.1 多个 effort 行，没有 Mythos 行。Anthropic 的 1853 是 v2 且系统卡详细段落归于 Fable；一个第三方页面将 v2 的 1853 归给 Mythos，但未提供独立核实证据，不属于 v2.1，未写入。

最近核验时间：2026-11-04T15:03+08:00

### Vals Index (vals-index-v2.2)

- 结论：未找到公开成绩。

已检查的主要资料：
- [Vals Index v2.2 leaderboard](https://www.vals.ai/benchmarks/vals_index)
- [Vals Index v2.1 leaderboard](https://www.vals.ai/benchmarks/vals_index_v2_1)

研究备注：
- 当前 v2.2 榜单未找到 Mythos 5.1。旧 v2.1 页面存在 Fable 5.1 分数，模型和版本均不匹配，不转录。榜单更新时间不是评测日期。

最近核验时间：2026-11-04T15:03+08:00

<!-- benchmark-collection-state
{
  "benchmarks": {
    "artificial-analysis-intelligence-index-v5": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis Intelligence Index leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index"
        },
        {
          "label": "Artificial Analysis methodology and version history",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
        }
      ],
      "notes": [
        "当前 Artificial Analysis 页面显示 Intelligence Index v5.0.1；没有找到 Mythos 5.1 行。仓库目标为 v5.0，未将任何其他模型或版本结果映射到 Mythos。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "automationbench-v1.0.6": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Mythos 5.1 page",
          "url": "https://www.anthropic.com/claude/mythos"
        },
        {
          "label": "Anthropic Fable and Mythos 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Zapier AutomationBench v1.0.6 leaderboard",
          "url": "https://zapier.com/benchmarks"
        },
        {
          "label": "AutomationBench scoring definition",
          "url": "https://github.com/zapier/AutomationBench"
        }
      ],
      "notes": [
        "Zapier 官方榜单的 31.4% 是 Fable 5.1 与 Opus 5 fallback 的系统分数；未发现 Mythos 5.1 独立成绩。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "chartography": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Surge Chartography leaderboard",
          "url": "https://surgehq.ai/benchmarks/chartography"
        },
        {
          "label": "Surge Chartography README and methodology",
          "url": "https://github.com/surge-ai/chartography/blob/main/README.md"
        },
        {
          "label": "Anthropic Mythos 5.1 page",
          "url": "https://www.anthropic.com/claude/mythos"
        },
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        }
      ],
      "notes": [
        "Surge 榜单没有 Mythos 5.1 行；Anthropic 系统卡列出的 42.6/86.2 与其他 Fable Chartography 数据均明确属于 Fable，配置和 judge 也彼此不同，未转录给 Mythos。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "deepswe-v1.1": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "DeepSWE v1.1 leaderboard",
          "url": "https://deepswe.datacurve.ai/"
        },
        {
          "label": "DeepSWE v1.1 methodology",
          "url": "https://deepswe.datacurve.ai/blog/deepswe-v1-1"
        }
      ],
      "notes": [
        "系统卡明确给出 67.4% 的是 Fable 5.1；DeepSWE 榜单也未列 Mythos 5.1。两者同底层模型不构成独立评测归属依据。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "gdpval-aa-v2.1": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Artificial Analysis GDPval-AA v2.1 leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
        },
        {
          "label": "Artificial Analysis GDPval-AA methodology",
          "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#gdpval-aa"
        },
        {
          "label": "Anthropic Fable and Mythos 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "Third-party GDPval-AA v2 claim reviewed",
          "url": "https://vectorwire.ai/benchmarks/gdpval-aa-v2"
        }
      ],
      "notes": [
        "AA v2.1 榜单列出 Fable 5.1 多个 effort 行，没有 Mythos 行。Anthropic 的 1853 是 v2 且系统卡详细段落归于 Fable；一个第三方页面将 v2 的 1853 归给 Mythos，但未提供独立核实证据，不属于 v2.1，未写入。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "humanitys-last-exam": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable and Mythos 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "System card readable transcript mirror",
          "url": "https://malob.github.io/ai-system-cards/anthropic/claude-fable-5-1/"
        },
        {
          "label": "Artificial Analysis HLE leaderboard",
          "url": "https://artificialanalysis.ai/evaluations/humanitys-last-exam"
        }
      ],
      "notes": [
        "AA 榜单仅找到 Fable 5.1 行。Anthropic System Card 摘要表把 HLE 列为 “Fable 5.1 / Mythos 5.1”，但详细方法段明确说明评测对象是 Fable 5.1，未说明 Mythos API 单独运行；故未把 60.9%/65% 写入 Mythos TOML。"
      ],
      "status": "待核实",
      "unresolved": [
        "摘要表的合并标签与详细测试对象描述不一致，无法确认是否存在单独的 Mythos 5.1 HLE 成绩；等待更明确的官方说明。"
      ]
    },
    "osworld-v2.1": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "AIB OSWorld 2.1 leaderboard",
          "url": "https://www.aib.vote/en/benchmarks/osworld-2-1"
        },
        {
          "label": "OSWorld 2.1 XLANG release manifest",
          "url": "https://github.com/xlang-ai/OSWorld-V2/blob/main/benchmark_releases/osworld-v2.1.json"
        },
        {
          "label": "Anthropic Fable and Mythos 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Mythos 5.1 page",
          "url": "https://www.anthropic.com/claude/mythos"
        }
      ],
      "notes": [
        "AIB 当前 v2.1 榜单未列 Mythos 5.1。Anthropic 发布材料中的 77.9 partial / 41.7 strict 明确属于 Fable 5.1 的 OSWorld 2.0，不能用于 Mythos 或映射为 v2.1 binary completion rate。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "swe-bench-pro-v2": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Scale SWE-bench Pro V2 Full leaderboard",
          "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
        },
        {
          "label": "Scale V2 release and protocol",
          "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
        },
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        }
      ],
      "notes": [
        "Scale V2 Full 榜单列有 Fable 5.1（Claude Code, high）99.10 ± 0.50，没有 Mythos 5.1 行。系统卡中其他 SWE-bench Pro 结果也明确归属 Fable，且不能据此推成 V2。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-science-v0.1": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "Terminal-Bench Science v0.1 release",
          "url": "https://www.tbench.ai/news/terminal-bench-science-0-1"
        },
        {
          "label": "Vals AI Terminal-Bench Science results",
          "url": "https://www.vals.ai/benchmarks/terminal-bench-science"
        }
      ],
      "notes": [
        "Anthropic 系统卡给出的 52.6% 属于 Fable 5.1；公开官方榜单和 Vals AI 页面未找到 Mythos 5.1 行。未将 Fable 的 70 任务、10 次/任务等条件转给 Mythos。"
      ],
      "status": "未找到",
      "unresolved": []
    },
    "terminal-bench-v4": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Anthropic Fable and Mythos 5.1 release results",
          "url": "https://www.anthropic.com/claude-fable-and-mythos-5-1"
        },
        {
          "label": "Anthropic Fable/Mythos 5.1 system card",
          "url": "https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf"
        },
        {
          "label": "Terminal-Bench 4.0 leaderboard",
          "url": "https://www.tbench.ai/?version=4.0"
        }
      ],
      "notes": [
        "Anthropic 公开表明确标注 Claude Mythos 5.1 为 60.9%；系统卡配置为 66 项任务、每项 10 次试验、max thinking effort、Claude Code --bare。没有来源公布实际评测日期，因此未写 date。"
      ],
      "status": "待核实",
      "unresolved": [
        "模型专属来源将指标称为 accuracy、版本写为 4.0；本地定义为 task resolution rate、4.0.0。原始值按来源保留，精确映射需复核。"
      ]
    },
    "vals-index-v2.2": {
      "checked_at": "2026-11-04T15:03+08:00",
      "checked_sources": [
        {
          "label": "Vals Index v2.2 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index"
        },
        {
          "label": "Vals Index v2.1 leaderboard",
          "url": "https://www.vals.ai/benchmarks/vals_index_v2_1"
        }
      ],
      "notes": [
        "当前 v2.2 榜单未找到 Mythos 5.1。旧 v2.1 页面存在 Fable 5.1 分数，模型和版本均不匹配，不转录。榜单更新时间不是评测日期。"
      ],
      "status": "未找到",
      "unresolved": []
    }
  },
  "existing_records": 0,
  "first_pass_completed": true,
  "last_checked": "2026-11-04T15:03+08:00",
  "model_id": "anthropic/claude-mythos-5-1",
  "new_records": 1,
  "overall_status": "待复核"
}

-->
