# ModelAtlas Data TODO

## 目标与边界

将 Benchmark 数据维护／发布与 Android 应用发版解耦。当前采用人工核实 + JSON + Python 校验／构建 + 静态 HTTPS 分发，不建设运行时后端或通用爬虫平台。

## P0：协议对齐

- [x] 对照 Android 当前 `BenchmarkManifest` / `BenchmarkSnapshot` / 更新逻辑，记录 v1 契约。
- [x] 修正初始清单和空骨架格式；明确版本 1 不是生产数据、首次远程真实数据需更高版本。
- [x] 明确全量替换、版本与摘要一致、客户端大小上限和高版本纠错规则。
- [x] 同步 Android 可选 `cost`：维护／发布 Schema、构建透传及费用语义文档；现有真实成绩不补造费用。
- [x] 使用 Android 实际解析器消费 Python 生成的原字节清单及快照，并完成隔离 Room 更新验收；不替代真实线上下载验收。

## P1：最小维护工具

- [x] 分离 Benchmark、来源、显式模型映射与成绩维护文件。
- [x] 建立严格 Schema、重复键／非有限数值检查、引用／范围／审核依赖校验。
- [x] 确定性全量构建、字节摘要、差异报告、不可变历史与空生产包门禁。
- [x] 增加校验 CI 配置，不包含部署权限或自动发布。
- [x] 完成本轮本地测试与命令验证，结果见下方验证记录。

## P2：真实数据试点

- [x] 选定 MMLU-Pro 为维护流程试点，核对官方固定修订 README 与仓库许可。
- [x] 录入三条官方表值，保留来源定位、采集日期、未知配置与待审核状态。
- [ ] 核实具体模型快照、Models.dev 规范 ID 及映射证据。
- [ ] 确认 Benchmark 数据修订、评测配置及 v1 可表达性。
- [ ] 完成结果再分发、归属、许可／NOTICE 与客户端展示复核。
- [x] 经维护者明确批准，改用 DeepSeek-R1 固定文档的五条成绩完成首批非空 v2 包；原三条试点未批准，以上三个待核实项仍针对旧试点。

## P3：发布与 Android 闭环

- [x] 准备版本化 GitHub Release 完整候选 archive／来源提交及恢复流程；候选先归档再部署，归档存在不代表上线成功。不依赖被忽略的本地 build 或有过期时间的 Actions artifact。
- [x] 准备人工触发 Pages Actions，串行发布，只上传生产站点并保留历史快照；尚未在线执行。
- [x] 验证实际 HTTPS 地址、200 无重定向及线上 SHA-256；本轮当前请求通过，不代表已覆盖完整缓存传播窗口或真实客户端验收。
- [x] 在 Android 配置 `benchmark_manifest_url`，从同一生产构建导出真实随包 v2、归属和 MIT 许可，设置页展示首批来源。
- [x] 更新 Android README / TODO / 数据源与架构中的旧状态。
- [ ] 完成真实客户端更新、失败保留旧数据、离线及纠错验收。
- [x] 完成本地跨仓库原字节契约、隔离 Room 更新／事务失败保留／离线重开及相关页面验收；真实 HTTPS 与真机验收不勾选。

## P4：覆盖扩展

- [ ] 按实际查询需求补充其他任务类别的 Benchmark，不把待核实名称直接作为已接入清单。
- [ ] 数据维护量上升后再添加具体来源导入脚本，仍需人工审核。
- [ ] 根据实际数据评估 Benchmark 名称／说明协议、关键配置扩展及可比性建模；不预先建设综合排名。

### 本轮：半年模型／十一项候选调查

- [x] 与维护者确认：2026-04-28～2026-10-28 按 Models.dev 发布日期收录，十一项全部调查；有证据就收录，保留不同实验。仅访问公开、无需登录或付费材料。
- [x] 固定 151 个规范模型 ID、目录原始响应摘要与抓取时间；旧八条结果、原定义／来源／映射以及 Android 随包五条保存保护基线。
- [x] 实现与 approved-only 构建分离的 candidate-only JSON／Markdown 预览：显式候选成员、双基线、覆盖矩阵、证据和发布阻塞；不生成 manifest、不改审核状态或 Android 协议。
- [x] 增加目录碰撞、原子替换／硬链接、附件 Schema、本批次版本／时间策略、CI 外部 Android 未检查提示和离线摘要一致性回归。
- [x] 359 条候选及相关映射完整导入维护文件，涉及 58／151 个模型；全部保持 pending，旧八条及 Android 随包不变。
- [x] 生成双基线**隔离暂存**报告，核验旧八条维护记录及 Android 随包五条和受保护文件；报告不是已导入或部署的快照。
- [ ] 继续核实并整理原指数 staging 未纳入的 259 条，逐条检查来源精度、模型身份及 fallback；不将其未经核实直接导入。
- [ ] 后续由维护者审核候选、许可／客户端归属及不可表达条件，再另行确认实际淘汰旧成绩、导出和部署；本轮不执行。
- [ ] 修改并测试批次审核生命周期：当前候选报告要求全部候选及依赖为 pending、保护旧基线，直接部分批准或淘汰会使校验失败；须保留审核证据并维持发布门禁。

### 本轮候选验证记录

- `python3 scripts/validate.py` 通过：当前维护层 12 条成绩，其中原 5 条 approved、原 3 条 pending 及新增 4 条 pending；未批准候选不参与发布构建。
- `python3 scripts/preview_candidates.py --staging --check-android` 通过：11 项、359 条候选，覆盖冻结的 151 个模型 ID 中的 58 个；18 组系统记录／调查线索。旧八条维护成绩、Android 随包 v2 五条及 15 个受保护文件已核对。报告写入 `build/candidate-review-2026-10-28/`，是隔离暂存的假设替换，不是完整导入或发布包。
- `python3 -m unittest discover -s tests -v`：78 项通过；`git diff --check` 通过。approved-only 预览 v3 仍为原五条，较随包 v2 基线 `+0 / ~0 / -0`，不代表发布或设备验收。
- 原 `staging-indices.json` 中另有 259 条未纳入候选，涉及未逐条核实精度／身份或 fallback；保留原暂存，后续取证。新增的其他 355 条候选仍待完整写入日常维护文件并经维护者审核、许可与 Android 归属复核。
- 没有修改 Android、设备、发布配置或历史，未提交、推送或部署。相邻 Android 工作树干净，不等同真实客户端在线更新验收。

### 2026-10-28：完成 pending 导入及首个来源初审

- 以 `merge_candidate_staging.py --check` 的输入摘要执行 `--apply`，写入 12 个文件；输入摘要一致，摘要不是并发锁。三份纳入范围的 staging 与维护层逐对象比较：13 项定义、18 个来源、206 条映射、359 条成绩均一致且 pending，批次 ID 集合一致；其中 355 条成绩为本次新增。原指数 staging 的其他 259 条未导入。
- `python3 -B scripts/validate.py` 通过：维护层 367 条成绩、5 条 approved，359 条批次候选均 pending；`python3 -B -m unittest discover -s tests -v` 通过 78 项。普通模式 `preview_candidates.py --check-android --output build/candidate-review-2026-10-28-imported` 通过，核对旧八条和 Android 保护文件；报告是候选假设差异，不是生产快照。
- 初审 Anthropic Haiku 5.5 system card 的五条候选：重新取得 PDF，SHA-256 与既存证据一致；官网确认模型名称和 API ID。原文确认 HLE 45.9／57.4、Chartography 46.4／86.2、OSWorld offline partial 72.4，以及各自工具／预算／判分配置；不同实验不可混合。Haiku 安全分类器无 fallback 的说明不能替代逐实验路由核实。数据修订／实际子集等未解决条件继续阻塞，成绩再分发许可及客户端归属也未确认；五条仍为 pending，不声称完成发布审核。Anthropic 商业服务条款不等于其公开 system card 结果的再分发授权。
- 另核查两个没有 `unrepresentedConditions` 的 AA 指数候选的权利阻塞：官网模型详情支持 GPT-6 Astra Max 的 v5.0 指数 57；xhigh 55 未在本次独立复核。网站条款 2.1 限个人非商业访问，2.2 对复制、分发和内容商业利用设限，3.3 限制自动搜索／采集；现无额外分发授权，两个候选均不得批准。空条件数组不等于已通过身份、配置、fallback 或权利审核。
- 未批准、删除、导出或发布；未修改 Android。线上状态及真实客户端未在本次操作中重新验收。

## 项目许可

- [ ] 由维护者确定本项目代码、原创文档及整理成果的许可；第三方材料仍遵守其各自条款，不自动套用项目许可。

## 验证记录

2026-10-28，macOS / Python 3.12.2 / jsonschema 4.26.0：

- `python3 scripts/validate.py` 通过：1 项 Benchmark、3 条待审核成绩、0 条已批准成绩；根目录 v1 骨架摘要匹配。
- `python3 -m unittest discover -s tests -v`：29 项通过。覆盖协议字段、严格 JSON、版本／摘要、未知值及 false／零值、审核依赖、许可／映射证据、范围、数量／字节限制、不可变历史、幂等构建和删除确认。
- `python3 scripts/build.py --version 2` 及产物校验通过：预览 v2 为空，明确列出三条被排除的成绩，没有更新根目录或线上清单。
- `python3 scripts/build.py --version 2 --release` 按预期返回 1：没有已批准成绩，拒绝空生产快照；未创建生产站点。
- Apache-2.0 副本与固定上游修订 LICENSE 逐字节一致。
- 本地相对文档链接与新增源码空白检查通过。
- 尚未执行 GitHub Actions、线上发布、Android Kotlin 解析／数据库或设备验收；没有改动 Android 仓库。

### 2026-10-28：同步可选 cost

- 维护与发布 Schema 接受可选数值／null，构建缺失输出 null，保留零及有限原值；不修改历史快照、清单或三条真实维护成绩，结构版本仍为 1。
- 全量单元测试 34 项通过，新增覆盖缺失／null／零／有限费用、非法类型与非有限 JSON 拒绝、费用单独变更的差异报告，以及旧快照省略 cost 的兼容性和原字节保留。
- 维护／骨架校验、预览构建及产物校验通过，`git diff --check` 通过。
- 未修改 Android、运行 Android 测试或执行发布；币种、单位及费用口径仍需另行确认。

### 2026-10-28：首批真实数据与两仓库本地闭环

- 维护者查看固定原文、五个分数、三个规范模型映射及许可后明确批准首批试用；维护数据共 3 项定义、8 条成绩，5 条 approved、3 条 pending。新增 MMLU-Pro EM 与 MATH-500；不合并旧 Overall Accuracy，不补费用、日期或未知工具状态。
- `prepare_release.py --output build/site-real-v2`、产物校验、Android assets 导出及 `--check` 通过。根目录初始骨架未变；没有发布新快照到线上。
- Python 全量 39 项通过，覆盖导出／只读核对、归档恢复与路径穿越拒绝、HTTPS 检查逻辑等；两份工作流 YAML 语法解析通过。未安装 actionlint、未运行 GitHub Actions。
- Android 相关单元测试实际 42 项全部通过（BenchmarkUpdate 5、SyncRunner 6、HttpSource 3、ModelDetailMapper 9、ModelRepository 19）；Debug APK、测试 APK 构建与 Debug Lint 通过。
- API 37 / `emulator-5554` 首轮 24 项 `OK`；补持久化后集成类 5 项 `OK`；再补真实构建 v3 经生产 HTTPS source 的完整替换测试，最终重建测试 APK、集成类 6 项 `OK`。共覆盖 26 个不同用例：Room 隔离库、断网保留、原字节清单更新、事务回滚、文件库重开、目录／收藏独立、评测详情、来源许可、阅读恢复与返回链路。未清数据或卸载现有应用，未操作连接的真机。
- `build/site-local-v3` 由真实维护数据和 v2 基线生成，仅作本地测试候选；通过导出脚本写入 Android instrumentation assets 的 `benchmark-contract-v3/`。验证随包 v2 → 注入 Python v3 原始 HTTP 响应 → 生产 HTTPS／大小／SHA 校验 → Room 全量替换并清除本地手改条目 → 详情 Flow 更新；不连接真实远程服务器，未发布 v3。主随包及待发布配置仍为 v2。
- MIT 正文核对一致；上游文件无末尾换行，本地副本仅增加末尾换行，未改许可条文。导出保留本地许可文件的完整字节。
- 只读运行 `check_remote.py --expected-version 2` 返回 HTTP 404，确认预期地址目前未上线；这是待部署状态，不记为线上验收通过。尚未提交、推送、创建 GitHub Release、部署 Pages 或完成真实 HTTPS 更新；远程 v1 不同步归属旁车，新来源的客户端许可兼容性仍须单独审核。

### 2026-10-28：修复首次 Actions 依赖缓存失败

- 用户提供的 Actions run `40667384443` / job `122745206444` 在 `setup-python` 失败：pip 缓存默认查找 `requirements.txt`／`pyproject.toml`，但仓库仅有 `requirements-dev.txt`。
- 在 `validate.yml` 与 `publish.yml` 的两个 pip 缓存步骤显式设置 `cache-dependency-path: requirements-dev.txt`；不改变数据或发布门禁。Node.js 20 弃用和 ubuntu-latest 迁移提示不是此次失败原因，未扩大范围升级 Actions。
- 本地 YAML 解析、两个缓存步骤的依赖路径及文件存在检查、`git diff --check` 通过；仅工作流配置修改，未重复执行数据／Android 测试。尚未提交、推送、重新触发 Actions 或部署；需在包含修复的新提交上运行工作流，重跑旧提交不会加载新配置。
