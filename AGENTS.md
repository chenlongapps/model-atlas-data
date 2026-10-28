# 工作约定

- 本仓库只维护 Benchmark 定义和成绩，日常数据编辑限于 `data/benchmarks.json`、`data/scores.json`。
- 先读 `README.md`。来源 URL、表格定位、模型原名、评测条件及第三方许可必须保留；未知模型可用 `modelId: null`，不要模糊匹配或猜版本。
- `pending` 不进入快照。`approved` 也必须有核实的模型映射、可再分发许可、归属和可表达条件；状态本身不授予使用权。
- 不改写 `benchmarks/scores-vN.json`、已发布 manifest 或历史归属文件。Android 只接受更高版本，并全量替换成绩；构建必须保留所有仍有效的已发布 ID。
- 日常验证：`python3 scripts/validate.py`。改动校验或构建代码后运行：`python3 -m unittest discover -s tests -v`。
- 本地构建：`python3 scripts/build.py --version <新版本> --output build/site-v<新版本>`。删除旧成绩必须使用 `--allow-removals --reason` 并经人工核实。
- 不修改相邻 Android 仓库；不要推送、发布或部署，除非用户明确要求。
