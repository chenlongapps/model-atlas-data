# 网页与发布

[文档导航](README.md) · [开发与校验](development.md)

## 本地预览

```sh
python3 scripts/preview.py
```

打开 <http://127.0.0.1:8000/>，`Ctrl+C` 停止。可用 `--port 端口号` 或 `--port 0` 自动选择端口。

预览只监听本机，在临时目录构建网页与数据，退出后清理；不生成 manifest，因此页面标示发布信息不可用。无需第三方 Python 依赖。

## Web Explorer

默认地址：<https://chenlongapps.github.io/model-atlas-data/>（需成功部署）。Models 与 Benchmarks 提供搜索、筛选、排序、详情和双向导航；顶部搜索支持 `Ctrl+K` / `⌘K`。

界面支持中文与英文，首次按浏览器语言选择，不支持时回退英文；浏览器允许时记住选择。中文描述优先使用译文，缺失回退原文；英文显示原文，原始描述未必均为英文。

成绩按名称、版本和指标唯一关联，支持定义声明的兼容版本及 `unspecified` 例外，见[映射规则](data-format.md#benchmark-定义与展示)；未匹配记录仍在模型详情显示。表格按定义的 `higher_is_better` 排序，方向未知时保留原顺序；`effort` 单列，缺失显示 `—`。**显示顺序不证明不同实验条件可比，也不是排行榜。**

### 图表与交互

一个柱条或点对应一条成绩，不合并同模型配置、不只选最高分。图表筛选不修改下方原始成绩表。

| 视图 | 默认与刻度 | 缺失处理 |
| --- | --- | --- |
| 成绩柱状图 | 全部或部分成绩缺成本时默认；真实零点线性刻度，兼容负分和全零；按评分方向排序 | 无成本或发布日期也可显示 |
| 成本散点图 | 全部有效数值成绩都有成本时默认；成本默认对数，可切换线性 | 缺成本的记录不画，明确提示数量及柱状图入口 |
| 发布日期散点图 | 手动切换；线性时间轴 | 不推断发布日期，不画缺少坐标的记录 |

- 使用原始数值精度，不用表格舍入值。字符串成绩（如带置信区间的原文）不自动解析，仅在表格展示，并计入缺少有效坐标的数量。
- 成本单位必须精确一致；币种、每任务、加权每任务、每测试与整次评测费用不混用、不换算。真实零成本自动使对数轴回退线性并提示，不丢弃零或替换为极小值。
- 图表通栏展示，按机构固定配色。柱状图保留模型名、原始档位和机构 Logo，多记录时横向滚动，不挤压柱条。
- 图下机构图例可聚焦单一机构，再点当前机构或“显示所有机构”恢复；仍遵守成本、档位及条件筛选。档位与条件组收在“筛选”中，搜索只突出显示。
- 悬停/键盘聚焦显示详情，点击/Enter 固定，方向键切换，Escape/关闭清除选择；重合坐标可查看所有记录。前沿及机构聚焦分别标注不同模型与档位，不以“+N”代替；避让标签不移动数据坐标，必要时增加高度。
- 手动图表视图在语言切换时保留。样本量、被筛除和缺少坐标的记录数及来源均保留；时间只使用 manifest 的发布包生成时间，缺失时标明不可用。

### 象限与前沿的限制

成本模式默认开启象限和帕累托前沿，可手动关闭；条件不足时禁用。发布日期和柱状图模式不显示这两项。

- 象限按当前展示记录的成本、分数中位数划分，强弱方向遵循 `higher_is_better`，不是官方阈值。分界值按未舍入数据定位，简写可查看完整精度。
- 前沿是**当前可见点集的数学边界，不是经可比性验证的排名、官方前沿或统计显著优势**。它要求定义匹配、成本单位相同及评分方向已知，但不自动按 Harness、档位、来源或其他实验条件分组，也不限制评测白名单。
- 同一模型的不同配置逐条参与。同成本同分的记录全部保留；只有一个坐标时只画标记，不虚构线段。虚线连接观测点，不代表插值模型。
- 搜索只突出显示、不重算前沿；机构、档位、条件筛选会重算。字段相同仍不证明可比，缺少条件不能当默认值。数据与可比性说明可展开查看。

图表不改变原数据的来源或许可限制，公开分发前仍需处理[许可风险](review-notes.md#许可与分发)。

## GitHub Pages 部署

`.github/workflows/pages.yml` 运行测试、校验、构建，以官方 Pages Actions 同时发布网页、JSON、manifest 和 `LICENSE.models-dev`。使用全新输出目录，不提交 `dist/`。

首次启用：

1. **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
2. 确认 `github-pages` 环境允许默认分支；需要审批时先批准。
3. 在 **Actions → Deploy data to GitHub Pages → Run workflow** 选择默认分支运行，成功后查看环境链接。

### 数据端点

默认前缀为 `https://chenlongapps.github.io/model-atlas-data/`；自定义域名以部署地址为准：

```text
models.json
benchmarks.json
benchmark-results.json
i18n/zh-CN.json
manifest.json
LICENSE.models-dev
llms.txt
```

现有 Web Explorer 和 Android 端点继续使用原有 JSON 结构，成绩汇总作为独立端点发布。AI 导航源为 [`web/llms.txt`](../web/llms.txt)，使用英文手工维护；项目结构或数据约定变化时同步更新。网页资源（含 llms.txt）不进入 manifest，也不影响 `data_version`。

### manifest

| 字段 | 含义 |
| --- | --- |
| `schema_version` | manifest 格式版本，当前为整数 `1` |
| `git_commit` | 构建时实际检出的完整 Git 提交，不一定是触发提交 |
| `published_at` | UTC `YYYY-MM-DDTHH:MM:SSZ`；发布包生成时间，不是部署完成或评测日期 |
| `files` | JSON 与许可文件的相对路径 → 实际字节的 `sha256`（小写十六进制）、`size`（字节）；不含 manifest 自身 |
| `data_version` | `sha256:` 加规范化 `files` 对象的 SHA-256 |

`files` 包含 `models.json`、`benchmarks.json`、所有构建的 `i18n/*.json` 和 `LICENSE.models-dev`。Android 的 v1 清单校验仅接受这些路径，因此 `benchmark-results.json` 随发布包提供，独立于 `files` 和 `data_version`。规范化使用 UTF-8 JSON、按键排序、不转义非 ASCII、无多余空格、不添加末尾换行，参见 `json.dumps(files, ensure_ascii=False, sort_keys=True, separators=(",", ":"))`。同一清单及内容得到同一数据版本，不受 Git 提交或生成时间影响。哈希检测一致性，不提供签名或真实性保证。

### 本地生成完整发布包

先提交相关源码，输出目录应为全新目录：

```sh
python3 scripts/validate.py --check-results
python3 scripts/build.py --json-only --output /path/to/release
cp LICENSE.models-dev /path/to/release/LICENSE.models-dev
python3 scripts/manifest.py --output /path/to/release
cp -R web/. /path/to/release/
```

manifest 脚本支持 `--root`；`--output` 默认 `<root>/dist`，显式相对路径以当前目录为基准。它拒绝相关模型、定义、本地化、构建/manifest 脚本及许可文件存在未提交更改，校验输出清单后原子替换 manifest；不会自行重建或证明 JSON 来自当前提交，应紧接构建执行。

### 自动触发与排错

- `main` 分支的数据、网页、相关脚本、测试、许可及 Pages 工作流变更触发发布；改分支名需同步 `push.branches`。
- `Sync new Models.dev models` 成功完成也触发，即使没有新增模型。机器人 `GITHUB_TOKEN` 推送不会触发普通 push 工作流，因此使用 `workflow_run` 衔接；改同步工作流名称也须改此引用。
- 手动和同步事件只允许本仓库默认分支部署。各入口检出默认分支最新代码，不执行同步产物；实际版本以 checkout 和 manifest 为准。
- 发布串行执行，不取消进行中的发布。测试、校验、构建失败不部署，保留旧站点；构建只读，部署单独授予 `pages: write`、`id-token: write`，无需个人令牌。
- 失败先看 Actions 具体步骤：数据/测试失败修源文件；权限、Pages 设置或环境审批失败检查仓库配置。构建警告不阻止发布，也不表示来源、翻译或许可已获人工审核；此工作流不替代面向 PR 的通用 CI。
