# 数据契约

## 契约依据

对齐相邻 `model-atlas-android` 工作区的：

- `app/src/main/java/io/github/chenlongapps/modelatlas/data/benchmark/BenchmarkData.kt`
- 同目录的 `BenchmarkUpdate.kt`、`BenchmarkSync.kt`
- `data/local/BenchmarkScoreDao.kt`

这不是共享 SDK：修改 Android 协议时仍需显式核对本仓库 Schema、脚本与测试。当前 Python 校验不是 Kotlin 解析或真机验收的替代。

## 发布层 v1

`manifest.json`：

```json
{
  "schemaVersion": 1,
  "version": 2,
  "url": "https://chenlongapps.github.io/model-atlas-data/benchmarks/scores-v2.json",
  "sha256": "<实际快照字节的64位十六进制摘要>"
}
```

快照顶层：`schemaVersion: 1`、相同的正整数 `version`、`scores` 数组。每条成绩字段：

| 字段 | 必需 | 含义 |
| --- | --- | --- |
| `id` | 是 | 结果稳定 ID，不随分数修正而变化；不同实验分别记录 |
| `modelId` | 是 | 经证据核实的 Models.dev 规范模型 ID，不是服务商模型服务 ID |
| `benchmarkId` | 是 | 稳定标识；已知的语义不同版本使用不同 ID |
| `score` | 是 | 原始有限数值，不默认换算、不取最高分 |
| `cost` | 否 | 原始有限数值或 null；缺失不视为零，币种、单位及总费用／平均费用口径尚未约定 |
| `metric` / `unit` | 否 | 原始指标及计量单位 |
| `higherIsBetter` | 否 | 高分是否更好；未知为 null |
| `subset` | 否 | 实际子集名称，不等同于数据集或 Benchmark 版本 |
| `harness` | 否 | 执行框架与来源明确的版本／执行配置摘要；客户端显示为“评测框架／执行配置” |
| `reasoningEffort` | 否 | 来源实际提供的推理等级 |
| `toolsEnabled` | 否 | 工具开关，未知不能填 false |
| `sourceUrl` / `sourceType` | 否 | 原始出处，以及 `benchmark_author` / `model_developer` / `independent` |
| `evaluatedAt` | 否 | 实际评测日期；当前维护规则仅接收完整 YYYY-MM-DD，未知为 null |

Android 可解析更宽松的字符串和来源类型；本仓库的发布 Schema **故意更严格**，拒绝拼写错误、额外字段和 `test` 来源。发布脚本会填写指标、单位、方向及来源，其他可选字段保持 null，不伪造缺失信息。

`cost` 对齐 Android 的 `Double? = null`：维护数据可省略或填 null，构建时统一输出 `cost: null`；明确的零与有限数值原样保留，不额外推定正负限制。不接受布尔值、数值字符串、NaN、Infinity 或超出 Double 范围的数值。它不是 Models.dev 的 API token 单价，`unit` 仍是成绩单位，不作为 cost 单位。当前 Android 不用此字段计算或详情展示；真实费用入库前须核实其含义、口径与来源，不依据 token 价格推算填入。

限制：清单 ≤ 64 KiB；快照 ≤ 16 MiB、≤ 100,000 条；版本必须能表示为 Kotlin Long。JSON 必须没有重复键、非有限数值或重复成绩 ID。

## 版本与更新语义

- `schemaVersion` 表示结构，`version` 表示内容，两者独立。文件名 `scores-v2.json` 的 2 是内容版本。
- `cost` 是兼容性可选字段，仍使用 `schemaVersion: 1`。旧快照允许省略，不能为补充字段重写历史；新增或修正费用需发布更高内容版本。
- 真实首批快照及 Android 新随包为版本 2。旧虚构随包 v1 可通过远程 v2 更新；新随包 v2 仅应用远程 v3 及以上。本仓库版本 1 空文件只是初始骨架，**不能视为生产数据**。
- 根目录原骨架曾使用 `dataVersion`、`results` 等不兼容字段；本轮在初始工作区修正，未执行发布。若另有历史已发布副本，先恢复其不可变字节并改用新版本，不将本轮骨架替换作为已发布版本的修改方式。
- 客户端仅更新更高版本。清单与快照版本、原始字节摘要必须一致。
- 更新是**全量替换**，不以模型或 Benchmark 增量追加。漏掉的成绩会从客户端删除。
- 下载、摘要、结构或数据库事务失败时客户端保留旧数据。空数组在客户端合法，但生产构建禁止空快照。
- SHA-256 只验证一致性，不是签名或独立来源认证；使用 HTTPS，客户端当前不跟随重定向。

## 维护层与发布层的映射

- `results.mappingId` → `model-mappings.modelId`。
- `results.benchmarkId` → 定义中的稳定 ID；定义提供 `metric`、`unit`、`higherIsBetter`。
- `results.sourceId` → 来源的 `url`、`sourceType`。
- `results` 的子集、Harness、推理、工具及评测日期同名展开。
- `results.cost` 同名透传，缺失转为 null，不从模型报价、成绩或其他记录补齐。
- 采集日期、来源发布日期、原文定位、模型映射证据、审核备注不冒充评测日期或工具配置。
- v1 没有独立的显示名称、Benchmark 说明、提示词、预算、采样等结构。重要且无法表达的已知条件放入 `unrepresentedConditions`，结果不得批准发布；先讨论客户端协议扩展。不能把条件藏到仅维护者可见的 `notes` 后照常发布。

客户端目前将 `benchmarkId` 直接当作标题。后续应独立接入显示名称和说明；暂不因此改用可变中文名称做主键。定义的 `version` 可为未知，不从论文年份或数据收集日期猜测；版本明确后由审核决定是否需要新的稳定 ID。

许可与归属输出为 `attributions/v<version>.json` 和 `third_party/`，与成绩快照一起保存。`export_android.py` 从 release 包导出原字节 `benchmarks.json`、用于溯源及契约测试的 `benchmark-manifest.json`、`benchmark-attributions.json` 与所引用许可。Android 设置页读取随包归属并展示 MIT 全文。**远程 v1 更新仍只同步成绩，不下载归属旁车**：新增来源前必须核查已安装客户端能否满足其条款，必要时先扩展协议和客户端；不能把静态随包归属说成任意远程来源的动态许可支持。

首批 DeepSeek 数据将原文的执行设置完整保留在 `harness` 摘要中，包括“对需要采样的 benchmark”这一限定；不将 Usage Recommendations 当成实际实验记录。未知的软件版本、逐任务采样适用性、日期和工具设置仍是未知，不能据此声称可比。
