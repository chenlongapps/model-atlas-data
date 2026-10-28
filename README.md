# ModelAtlas Data

ModelAtlas Data 是 [ModelAtlas Android](https://github.com/chenlongapps/model-atlas-android) 的 Benchmark 成绩仓库。维护者核对可信来源后，将原始成绩记入 JSON；本仓库校验后生成 Android 可读取的完整静态快照。这里不采集成绩、不提供 API、不做排名，也不自动猜模型版本。

## 文件

```text
data/benchmarks.json       Benchmark 定义
data/scores.json           成绩、来源许可和模型映射证据；日常主要维护文件
scripts/validate.py        标准库校验
scripts/build.py           生成完整快照、manifest 和摘要
tests/test_data.py         数据、发布保护和 Android 契约测试
benchmarks/                不可变发布快照
manifest.json              仓库内固定的 Android v2 基线
attributions/v2.json       v2 Android 客户端已有的来源归属
third_party/               被引用的上游许可文本和来源声明
archive/pre-refactor-2026-10-28.zip 迁移前数据、候选证据及审核材料归档
.github/workflows/         PR 校验；人工触发的 Pages 发布
```

归档只用于追溯，不参与校验、构建或日常录入。迁移核对确认：16 项 Benchmark 定义不变；367 个成绩 ID 与状态完整保留（5 approved、362 pending）；20 条来源、212 条映射、审核决定、证据、staging 和 259 条未纳入候选的原始记录都保存在归档中。17 条被成绩引用的来源和全部映射证据已内嵌到成绩；另外 3 条未引用来源保留在归档。359 个本批候选 ID 全部仍为 pending，且不同于原 8 条维护基线成绩。

## JSON 记录

`data/benchmarks.json` 保存稳定 Benchmark ID、名称、已知版本、指标、单位、分数方向、有效范围、官方链接和状态。语义不同的明确版本使用不同 ID；未知版本保持 `null`。

`data/scores.json` 将成绩及其证据放在同一条记录中；来源和映射不再使用跨文件引用，也不需要手工造 `sourceId` 或 `mappingId`。`sourceType` 可留空，待确认后补充。来源许可和分发状态独立于成绩的 `status`：只有状态、模型映射、来源许可和客户端归属条件都通过，成绩才可以进入 Android 快照。

```json
{
  "scores": [
    {
      "id": "example-score-id",
      "modelId": null,
      "sourceModelName": "原始模型名称",
      "benchmarkId": "math-500",
      "score": 91.2,
      "sourceUrl": "https://example.org/results",
      "sourceType": "independent",
      "status": "pending",
      "source": {
        "publisher": "Benchmark publisher",
        "status": "pending",
        "license": {
          "redistribution": "pending"
        }
      },
      "modelMapping": {
        "status": "pending"
      }
    }
  ]
}
```

这是最小的待审记录示例；映射、许可或评测条件核实后，再补齐证据并更新状态。未知的权限明确写为 `pending`，不要省略它来暗示允许分发。`cost` 可以省略、为 `null` 或保留来源明确给出的有限数值；不会从 API 报价推算。未知模型使用 `modelId: null`，保留原始 `sourceModelName`，并保持待审。不同评测条件保留为独立结果，不按最高分合并。

## 添加和校验成绩

1. 确认 Benchmark 和成绩来源可信，记录原文链接及表格位置。
2. 在 `data/scores.json` 加一条记录；若 Benchmark 尚不存在，再在 `data/benchmarks.json` 添加定义。模型身份或许可尚未确认时用 `pending`，不要猜测或自动批准。
3. 运行：

```sh
python3 scripts/validate.py
```

只有明确核实映射、成绩条件和再分发权限后，才可将状态改为 `approved`。状态批准不授予许可：`source.license.redistribution` 必须为 `allowed`，许可文本、归属和证据必须完整；已知但 Android v1 无法表达的重要条件也会阻止发布。现有客户端只同步成绩，不会随远程快照更新其安装包中的来源归属，所以构建会按发布者、URL 和许可信息核对 Android 已有归属；新增记录无需创建 source ID。

## Android 快照与发布

当前已发布基线为 `manifest.json` 指向 `benchmarks/scores-v2.json`。manifest 与快照均使用 `schemaVersion: 1`、内容 `version: 2`；快照包含 `scores` 数组。发布快照的 SHA-256 是对原始 JSON 字节计算的。v2 快照 SHA-256：`9020d8b7cd82b510a3f1ba8256100972be30848d6bd4445683c9080b4dc2d63d`。此仓库保存的快照与 Android 随包字节一致；本次重构没有请求线上地址。

| 结果 ID | 模型 ID | Benchmark | 原始成绩 |
| --- | --- | --- | ---: |
| `deepseek-r1-readme-distill-qwen-32b-math-500` | `deepseek/deepseek-r1-distill-qwen-32b` | `math-500` | 94.3 |
| `deepseek-r1-readme-r1-math-500` | `deepseek/deepseek-r1` | `math-500` | 97.3 |
| `deepseek-r1-readme-r1-mmlu-pro-em` | `deepseek/deepseek-r1` | `mmlu-pro-em` | 84.0 |
| `deepseek-r1-readme-v3-math-500` | `deepseek/deepseek-v3` | `math-500` | 90.2 |
| `deepseek-r1-readme-v3-mmlu-pro-em` | `deepseek/deepseek-v3` | `mmlu-pro-em` | 75.9 |

Android 只接受比本地版本更高的正整数版本（Kotlin `Long`），先核对 manifest，再按快照原字节校验 SHA-256、解析全部成绩，并在 Room 事务中全量替换。相同或较低版本不会触发替换；下载、摘要、解析或事务失败时保留现有数据。因此每个新版本必须完整保留所有仍有效的已发布 ID。默认拒绝清空或移除旧成绩；确需移除时，必须显式说明理由。

只有加入或修正了 Android 可见的已批准成绩后才构建，例如：

```sh
python3 scripts/build.py --version 3 --output build/site-v3
```

版本必须大于最新基线。构建会排除待审成绩，检查 SHA-256、许可、客户端归属、非空、历史字节和删除保护；若 Android 可见成绩没有变化，会拒绝创建无意义的新版本。确认删除时额外使用 `--allow-removals --reason "核实后的理由"`。本命令只生成本地文件，不部署。

正式发布仅从 `main` 手动运行 GitHub Actions 的 **Publish benchmark snapshot**，填写高于线上版本的版本号。工作流读取线上完整历史、重新构建并验证，再部署 Pages 和核对实际 HTTPS 字节。本次任务没有运行发布工作流、推送或部署。

## 来源与第三方声明

本仓库是独立整理项目，不代表模型开发商或 Benchmark 作者。成绩保留来源原值、必要条件和归属，不代表 ModelAtlas 实测或不同实验可比。`third_party/deepseek-r1/README.md` 说明首批五条 DeepSeek 官方自报成绩的固定来源、归属、改动及许可边界；MIT 仅对应上游仓库文档，不能据此推定原 Benchmark 数据集或模型权重采用 MIT。MMLU-Pro 及其他候选来源仍按各自记录保留许可状态；公开可访问不等于获准再分发。

项目代码和原创文档的许可尚未确定。第三方材料遵守各自条款，不因本项目许可而改变。
