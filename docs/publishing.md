# 构建与发布

## 当前状态

已实现本地校验、预览／生产构建、Android assets 导出、发布基线归档、人工触发 Pages 工作流及线上只读检查。**本轮不提交、不推送、不部署。** 2026-10-28 本轮只读运行 `check_remote.py --expected-version 2`，确认线上 v2 直接 HTTPS 200、五条成绩及 SHA-256 通过；不代表真实 Android 客户端更新验收。首批维护者批准的数据为 v2／五条成绩，旧三条仍待审。十一项新候选保持 pending，其[假设替换预览](candidate-review.md)不是本节的发布包预览。

不要选择 Pages 的 `Deploy from a branch / (root)`：根目录是维护仓库，且当前只有空骨架，不是待部署站点。后续使用 Actions 只上传审核通过的生产构建目录。

## 安装与检查

Python 3.11+：

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

脚本完全离线，不请求来源或清单 URL；执行目录不影响仓库路径解析。`validate.py` 同时检查维护数据及根目录骨架的格式、版本和摘要。

## 预览

```sh
python3 scripts/build.py --version 2 --output build/preview-real-v2
python3 scripts/validate.py --artifacts build/preview-real-v2
```

输出所选目录（默认 `build/preview/`）：版本化完整快照、清单、归属／许可、`report.json`。快照按稳定 ID 排序、固定编码和换行，不加入自动时间戳；相同输入产生相同字节。报告包含新增、修改、删除 ID、待审核／拒绝成绩以及维护数据计数。

目前预览 v2 含五条已批准成绩，三条旧成绩被排除。预览仍**不得部署**，生产构建额外执行非空和删除确认门禁。旧的空 v2 预览如已存在，请使用新输出目录，不覆盖旧候选字节。

## 准备生产包（不自动部署）

首批数据已经维护者明确批准；本地准备命令为：

```sh
python3 scripts/prepare_release.py --output build/site-real-v2
python3 scripts/validate.py --artifacts build/site-real-v2
python3 scripts/export_android.py --artifacts build/site-real-v2 --output ../model-atlas-android/app/src/main/assets --check
```

`prepare_release.py` 读取 `data/release.json` 中的 `version`、`allowRemovals` 和 `reason`，再调用既有生产构建。默认输出为 `build/site/`，本轮使用独立目录保留既有产物。`--release` 是数据门禁，不是线上／真机验收结论。

导出时去掉 `--check` 才会更新 Android assets；默认只写本仓库 `build/android-assets/`。成绩按快照原字节复制，附清单、归属和所引用许可。清单仅供随包溯源／测试，运行时检查地址仍来自 Android 配置。导出不改变根目录骨架、不发布站点，不删除其他 assets。

- 默认基线是根目录版本 1 骨架。**首次发布后每轮都必须指定最近成功发布的完整站点作为 `--baseline`**，不能继续拿骨架比较。
- `--base-url` 可指定最终 HTTPS 站点前缀，不接受凭据、查询参数或片段。构建不检查线上是否可访问及是否重定向。
- 已知历史快照按原字节保留；同路径出现不同字节拒绝构建，不改写旧版本。同理保留历史归属／许可文件。
- 成绩删除需先查看预览报告，再加 `--allow-removals --reason '核实后的理由'`；空生产快照即使有确认也禁止。
- 修改分数、模型映射或条件会列入 `changed`；必须人工复核报告，不把 CI 通过当作数据审核。
- 默认输出只能在仓库 `build/` 下，也可以使用独立外部目录；禁止输出覆盖维护目录或基线。重跑同版本且内容一致是幂等的；变更候选快照内容时用一个新的空输出目录，不覆盖原候选。

例如已有 v2 生产站点时，先以它为基线预览 v3，审核后在另一目录生产构建：

```sh
python3 scripts/build.py --version 3 --baseline build/site --output build/preview-v3
python3 scripts/build.py --version 3 --baseline build/site --output build/site-v3 --release
```

`build/` 不入 Git，不能作为唯一历史存档。后续发布流程必须将成功产物与来源提交关联，保留可恢复的发布基线；若基线遗失，应先恢复并校验线上不可变历史，不从维护数据重新生成旧文件冒充原件。

## Pages 发布工作流

1. 在 GitHub 仓库 Settings → Pages 选择 **GitHub Actions**。建议给 `github-pages` 环境设置人工审核及仅 main 部署保护；不要部署维护分支根目录。
2. 修改 `data/`、审核来源／映射／许可，递增 `data/release.json.version`；成绩删除必须在预览报告核实后设置 `allowRemovals: true` 并说明 reason。PR／push 的 `validate.yml` 不部署。
3. 在 main 的 Actions 人工运行 **Publish reviewed benchmark data**。整个发布串行执行，不自动批准、采集或发布。首次无归档时只在预期线上清单返回 404 的情况下使用根目录骨架；如已有站点必须先恢复历史。
4. 后续从数值最大的 `benchmark-data-vN` GitHub Release 下载完整 `site.zip`，校验并作为基线。先保存新候选 archive，再部署 Pages；归档包含来源提交、报告、当前及全部历史成绩／许可，不只依赖有保留期的 Actions artifact。
5. 相同版本、相同来源提交可以恢复候选并重跑部署；同版本但不同提交拒绝重用，必须递增版本。归档早于部署，因此 **Release 存在不等于 Pages 已成功上线**；失败候选也可能成为下一次构建的历史基线，不会导致历史文件遗失。不要手工修改／删除归档或相应标签。
6. 仅上传 `manifest.json`、`benchmarks/`、`attributions/`、`third_party/`、`.nojekyll`，用 Pages 完整站点原子部署；内部报告、来源提交、维护 JSON、脚本和测试不上传。
7. 部署后 `check_remote.py` 核对真实 HTTPS 直接 200、无重定向、大小上限、预期版本、原始字节摘要及非空结构。失败标记工作流失败，不自动回退清单版本或改写旧快照。缓存传播未收敛时可重跑失败部署任务；仍需人工验证旧清单对应快照在缓存窗口可访问。

```sh
python3 scripts/check_remote.py --expected-version 2
```

首批完整站点 archive 的创建需要 GitHub `contents: write`，部署需要 `pages: write` 和 `id-token: write`；当前会话没有执行这些操作。恢复 zip 拒绝路径穿越、重复路径和符号链接，并校验清单／摘要；离线归档工具是 `release_archive.py`。

Android 已配 `https://chenlongapps.github.io/model-atlas-data/manifest.json`，新随包为 v2。旧测试 v1 客户端可更新到 v2；要在新随包客户端验证更新，须发布经审核的 v3 或在隔离测试库使用旧版本。不能只改同版本快照。

客户端设置页展示随包 DeepSeek 归属和 MIT 全文，但远程 v1 不同步许可旁车。未来新增来源须再次审核已安装客户端是否满足许可要求；不能仅凭站点附许可就宣称客户端已满足。全新安装完全离线时，成绩导入不等于同时具备离线模型目录；目录仍沿用独立的 Models.dev 首次加载。

## 纠错

已发布 v3 有错时，以更高版本 v4 发布修复后的完整数据；若需要恢复 v2 内容，也作为 v4 重新发布。仅把清单退回 v2 不会更新已经装有 v3 的客户端。恢复发布也必须审核删除报告与完整性，不能修改已发布 `scores-v3.json`。
