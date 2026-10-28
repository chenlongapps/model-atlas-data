# ModelAtlas Data

[ModelAtlas Android](https://github.com/chenlongapps/model-atlas-android) 的 Benchmark 数据维护与静态发布仓库，使数据更新不依赖应用发版。

**当前状态：已获维护者批准的首批真实数据为 2 项 Benchmark、3 个模型、5 条 DeepSeek 官方自报成绩；已导出 Android 随包 v2。** 2026-10-28 本轮只读确认线上 v2 直接 HTTPS 200、五条成绩及 SHA-256 一致；不代表真实 Android 客户端更新已验收。原有三条 MMLU-Pro Mini-Leaderboard 成绩继续待审核，不猜测映射。

新增的半年模型／十一项评测调查的 **359 条 pending 候选已完整导入维护数据**；证据及假设替换报告不代表批准、Android 接入或发布，旧八条维护成绩及 Android 随包仍保留。范围、命令和双基线差异见[候选采集与替换预览](docs/candidate-review.md)。

## 职责与边界

- 维护 Benchmark 定义、原始成绩、来源、许可和明确的规范模型映射。
- 校验后生成 Android 现有 v1 协议的完整 JSON 快照及 SHA-256 清单。
- Android 负责下载、验证、Room 事务替换及离线展示；本仓库不包含 UI、运行时 API 或模型目录／价格代理。
- 不自动批准 AI 收集的数据，不按最高分覆盖不同实验，不生成综合排名或声称未知配置可比。

## 项目结构

```text
data/                           # 人工维护的唯一数据源
  benchmarks.json               # Benchmark 定义、指标和范围
  sources.json                  # 出处、归属与使用条件
  model-mappings.json           # 来源名称到规范模型 ID 的显式证据
  release.json                  # 下一候选内容版本与删除审核说明
  results/<benchmark-id>.json    # 原始成绩、条件及审核状态
  reviews/2026-10-28/            # 固定范围、旧数据基线、候选 ID 及证据附件
schemas/                        # 维护文档与 Android 发布协议
scripts/                        # 离线校验、确定性构建
tests/                          # 合成测试数据，不进入生产快照
docs/                           # 协议、采集及发布说明
third_party/                    # 来源归属、修改声明和第三方许可
benchmarks/scores-v1.json        # 空的初始协议骨架，不是生产数据
manifest.json                   # 指向初始骨架的清单
build/                          # 本地产物，不入 Git
.github/workflows/validate.yml   # PR / push 校验 CI，不部署
.github/workflows/publish.yml    # 人工触发的 Pages 发布与不可变产物存档
AGENTS.md                       # 工程及数据维护约束
TODO.md                         # 阶段计划和验收状态
```

## 快速开始

Python 3.11+：

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --version 2 --output build/preview-real-v2
python3 scripts/validate.py --artifacts build/preview-real-v2
python3 scripts/prepare_release.py --output build/site-real-v2
python3 scripts/export_android.py --artifacts build/site-real-v2
```

默认构建仅生成 `build/preview/`，不修改维护数据、根目录骨架或线上站点。当前预览包含五条已批准成绩，排除 362 条待审记录（原三条及本批 359 条）。**不要部署预览或空骨架**：客户端采用全量替换，空快照会删除已有成绩。已有同版本预览字节不同时请换新的候选输出目录，不覆盖旧产物。

`prepare_release.py` 读取 `data/release.json` 并执行相同的非空／审核／删除门禁，不执行发布。`export_android.py` 默认仅写 `build/android-assets/`，带 `--output ../model-atlas-android/app/src/main/assets` 才显式更新相邻 Android 的随包文件；`--check` 只核对字节。正式发布与历史基线规则见[构建与发布](docs/publishing.md)。

## 数据更新链路

```text
官方来源 → 人工录入／审核 → Schema 与业务校验 → 完整快照 + 清单
                                                        ↓
                                      Pages 完整站点发布（线上已有 v2）
                                                        ↓
                                     Android 验证 → Room → 离线展示
```

清单字段为 `schemaVersion`、`version`、绝对 HTTPS `url` 和 `sha256`；快照字段为 `schemaVersion`、`version`、`scores`。结构版本与内容版本独立，**不得沿用旧骨架的 `dataVersion` / `results` 字段**。

成绩支持与 Android 对齐的可选 `cost`：有限数值或 null，保留零值，不推算缺失费用。币种及费用口径尚未约定，不等同于 API token 单价，详见[数据契约](docs/data-contract.md)。

首批真实包为 v2，Android 新随包同为 v2；旧测试 v1 客户端可更新到远程 v2，新随包客户端要到远程 v3 才下载更新。新发布包含全部保留成绩，旧快照不可改写；纠错同样发布更高版本。

入口已配置为 `https://chenlongapps.github.io/model-atlas-data/manifest.json`；2026-10-28 本轮 `check_remote.py --expected-version 2` 只读检查返回直接 HTTPS 200，线上 v2／五条成绩摘要通过，先前的 404 记录不再代表当前状态。本轮未执行发布，也未操作 Android 客户端。只部署审核后的构建产物，不发布维护仓库根目录。后续更新维护 JSON、递增 `data/release.json` 版本，审核后运行发布工作流；用户更新成绩不需要升级 APK。

## 文档与计划

- [文档索引](docs/README.md)
- [Android 数据契约](docs/data-contract.md)
- [采集、模型映射与人工审核](docs/collection-policy.md)
- [候选采集与假设替换预览](docs/candidate-review.md)
- [构建、发布及纠错](docs/publishing.md)
- [分阶段任务与验证结果](TODO.md)

近期优先级：十一项候选证据与替换预览 → 维护者审核／分发条件复核 → 另行确认替换与真实客户端验收；不先建设通用多源平台。

## 数据声明与许可

本项目为独立第三方整理项目，不代表模型开发商或评测机构。Benchmark 分数受版本、数据集、推理预算、工具和执行环境影响，不等同于所有真实任务表现。

项目自身代码、文档和整理成果的许可尚未确定。第三方材料保留各自归属与条款，不能将仓库代码许可自动用于数据集或其他材料。首批批准内容见 [third_party/deepseek-r1](third_party/deepseek-r1/README.md)，旧待审试点见 [third_party/mmlu-pro](third_party/mmlu-pro/README.md)。
