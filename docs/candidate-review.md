# 候选采集与假设替换预览

本轮目标是调查 Android [Benchmark 清单](../../model-atlas-android/docs/benchmarks.md)的全部十一项，收集候选、出处和条件，**不是批准或发布，也不执行评测**。不删除旧八条维护成绩，不修改 Android 随包五条、设备数据、自动化 fixture 或发布配置。最终淘汰旧成绩须在维护者确认候选后另行执行。

## 固定范围

批次 `benchmark-refresh-2026-10-28` 的输入保存在 `data/reviews/2026-10-28/`：

- `models.json`：Models.dev 规范模型 ID、名称及原始发布日期，窗口 **2026-04-28～2026-10-28，含两端**。沿用 Android LLM 收录规则，以 `release_date` 而非 `last_updated` 筛选。本次 151 个 ID；完整响应的摘要和抓取时间随文件保存，不把浮动端点的将来响应当作本次目录。
- `baseline.json`：旧八条维护成绩及其定义／来源／映射的完整对象，Android 随包五条成绩与版本，以及受保护文件的摘要。这里只是不可变审核依据，不是另一套日常维护源。
- `batch.json`：明确列出本轮候选结果 ID、调查项目和附件，不把所有 pending 当成本轮候选。
- `evidence-*.json`：官方入口、实际查询记录、必要原文摘录与定位、可获得的响应摘要、仅系统级记录及阻塞原因。不是上游数据集或网页全文镜像。
- `staging-*.json`：本轮分组采集时保留的原始工作记录，其中部分文件已由维护者纳入版本控制；合并后不再作为日常维护或构建输入。正式候选仍以 `data/benchmarks.json`、`sources.json`、`model-mappings.json` 和 `results/` 为准，不能只编辑 staging 就认为已更新维护数据。

**本轮已完整合并：**359 条候选、206 条相关映射、13 项定义和 18 个来源与三份纳入范围的 staging 逐对象一致，全部保持 pending；维护层已写入 `batch.json`。未核实的 `staging-indices.json` 保留原状且不参与导入，只有 `staging-verified-indices.json` 中的四条指数成绩进入候选；另有 259 条原指数记录不在本批范围。旧八条及 Android 随包未替换。

只保存筛选必要的目录事实，不代理目录／价格。模型发布日期有争议、未知或精度跨边界时记录待核实，不补造日期。规范 ID 去重不等于 checkpoint 去重；`latest`、高速变体及同名记录不自动继承成绩。

## 目标版本

| 项目 | 本轮范围 |
| --- | --- |
| Artificial Analysis Intelligence Index | v5.0，仅摘录官方公布的指数，不自行计算 |
| Vals Index | v2.2，仅摘录官方公布的指数，不自行计算 |
| Terminal-Bench | 4.0／精确发布 4.0.0 |
| DeepSWE | v1.1 |
| SWE-bench Pro | V2 public，不含 v1、HARD-51 或 commercial private |
| OSWorld | 2.1，partial 与 binary 奖励不能混用 |
| AutomationBench | Zapier 1.0.6 strict pass rate，不用 AutomationBench-AA 替代 |
| Humanity's Last Exam | 原版；区分纯文本／完整集及工具配置，不扩入 Rolling／Diamond |
| GDPval-AA | v2.1，保留 Elo 语义及来源提供的区间，不当准确率 |
| Chartography | 核实数据修订／commit；没有正式数字版本就不编造 |
| Terminal-Bench-Science | 0.1／精确发布 0.1.0 |

旧版本只作调查线索，不填补目标版本缺项。指标、单位及方向按原文保留，不统一成百分制，不生成总榜；综合指数不是单项通过率。

## 采集与证据

1. 优先调查 **评测／数据集官网 → 模型公司发布页 → 第三方网站 → 网友测试**。优先级不是允许丢弃其他实验，也不是按最高分选择。
2. 只访问公开、无需登录或付费的材料；不使用 API Key，不下载 gated 资产，不绕过限制。收集已发表成绩，不运行评测。
3. 数值须能回到原文具体表行／列。映射必须有模型身份／版本证据和规范目录依据；不作模糊名称匹配。未知评测日期不以网页更新、模型发布日期或采集日代填。
4. 模型＋Agent 的成绩保留 Agent、工具、推理、预算和运行条件；多模型 fallback 只留 `systemOnly` 调查记录，不作为某个单模型的候选成绩。
5. 新定义、来源、映射和成绩全部 `pending`。来源条款不清则 `redistribution: pending`；代码许可不自动覆盖结果。不得为了通过校验将候选改成 approved。
6. `data/benchmarks.json`、`sources.json`、`model-mappings.json` 与 `results/*.json` 仍是维护来源。证据附件不再维护另一套结构化分数。
7. 现有 `harness` 可保留执行配置摘要；重要但发布 v1 不能完整表达的条件写入 `unrepresentedConditions` 并阻止批准，不藏在 notes 后发布。本轮不扩展 Android 协议。

“有证据就收录”不等于“有公开网页就可发布”。候选、模型身份核实、结果分发授权、客户端归属兼容和维护者批准分别判断。

## 生成报告

首次将已核对的分组候选加入维护层时，确保无其他进程或会话正在编辑数据，先在仓库外隔离副本校验，再明确执行合并：

```sh
python3 -B scripts/merge_candidate_staging.py --check
# 核对上一步打印的 snapshot-sha256 后：
python3 -B scripts/merge_candidate_staging.py --apply --expected-sha256 <snapshot-sha256>
```

合并器只追加 pending，保留旧对象；相同 ID 内容不同则拒绝，不会删除 staging 或覆盖用户工作。它先验证证据、范围和完整候选集，并要求 apply 时的输入摘要与 check 一致，使用临时文件原子替换，并在失败时尽力回滚。摘要不是锁；**跨多个文件不是文件系统事务，也不保证意外崩溃后的恢复**，check 和 apply 期间都必须停止其他写入者。此命令不批准、发布或更新 Android。

导入前可使用隔离暂存预览；当前维护层已导入，日常核对使用下方普通模式：

```sh
python3 scripts/preview_candidates.py --staging --check-android
```

该命令在仓库外临时目录模拟完整候选合并及校验，并用实际相邻 Android 工作区核对受保护文件；不写维护数据。报告明确标注 `stagingOnly: true`，不能说成完整维护层已导入。**它不是发布包，也不会导出到 Android。** 临时模拟会同时纳入已追加的四条成绩，但不会重复计数。

完整合并后才使用普通模式：

```sh
python3 scripts/validate.py
python3 scripts/preview_candidates.py --check
python3 scripts/preview_candidates.py --check-android
```

默认输出 **`build/candidate-review-2026-10-28/report.md` 与 `report.json`**。只有这两份报告，不写 `manifest.json`、版本化 scores、发布配置或 Android assets。输入必须来自 `data/reviews/`，输出限仓库 `build/` 的独立目录；仅允许空目录或同批次、内容完全一致的 candidate-only 报告重跑，拒绝覆盖已修改的报告或混入已有生产／preview 产物。报告内容变化时指定新的空输出目录。通过独占临时文件和原子替换避免截断已有硬链接，也拒绝符号链接输出。

普通 `validate.py` 会离线检查所有 `data/reviews/*/batch.json`，不要求 CI 存在相邻 Android 仓库。加 `--check-android` 才核对相邻 checkout 的受保护摘要；未检查的外部文件在报告显示 `not-checked`，CLI／CI 日志也明确打印 NOTICE，不冒称已验证。基线内部摘要一致性、内仓库受保护文件和旧维护对象始终核验。每批只选择其明确列出的候选 ID，其他批次不会被自动纳入。本批次的十一项目标及日期／版本另有固定策略检查；证据附件有独立 Schema。

**审批流程阻塞：**当前批次校验要求所有候选和依赖保持 pending，并保护旧基线对象。正式批准部分候选或淘汰旧记录前，须先设计并测试保留原始审核证据、支持分批审核及基线演进的流程；不能直接改状态导致校验失败，也不能削弱发布许可与条件门禁。候选报告的移除列表只是全量替换假设，不是已批准的删除清单。

报告包含两套**假设**差异：

- **维护范围**：旧八条拟移出、新 pending 候选拟加入，但源文件和旧审核状态实际未改变。
- **Android 影响**：当前随包 v2 五条拟移出，列出新候选的考虑加入集合和映射／许可／协议阻塞。基线是随包字节，不冒称线上发布版本。该集合不是可直接导出的 Android 快照。

另输出十一项调查覆盖、151×11 模型覆盖矩阵、原始成绩／配置／证据、仅系统级记录及保护校验。`not-collected` 和矩阵中的零仅表示**本轮列明来源未收录**，不是分数为零，也不表示已经逐模型穷尽全网。

现有 `build.py` 无论 preview 还是 release 都只选择 approved；它的 preview **不包含本轮 pending 候选**。不得用现有 preview 冒充候选替换报告，也不得对候选报告调用 `export_android.py`。

`build/` 是可再生成且被忽略的产物；候选、范围、证据与基线不能只存在其中。报告确定性生成，不包含每次运行的时间戳。
