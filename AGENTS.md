# 仓库工作约定

## 阅读顺序

先读 `README.md`、`docs/README.md`，按任务阅读协议、采集或发布说明；进度只维护在 `TODO.md`。

## 边界

- 本仓库仅维护、校验和分发 Benchmark 数据，不包含 Android UI、数据库或运行时 API 服务。
- Android 发布契约以 `docs/data-contract.md` 为准。修改结构前核对客户端 `data/benchmark/BenchmarkData.kt`，不要把维护层字段直接塞进发布层。
- `data/` 是维护数据的唯一来源；快照通过脚本生成。已发布版本不可修改，纠错也必须递增内容版本。
- 不自动抓取后发布，不做模糊模型匹配，不猜测版本、测试条件、单位或日期，不把未知值当作零或 false。
- AI 辅助收集不等于审核通过。只有证据和分发条件已核实的数据才能标记 `approved`；不能为了通过校验删除关键条件。
- 不改动相邻 Android 仓库，除非任务明确包含它；不要提交、推送或部署，除非用户要求。

## 验证

需要 Python 3.11+，依赖见 `requirements-dev.txt`。

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --version 2
```

`--release` 有意拒绝空成绩和未经审核的数据。不要通过放松校验使构建变绿。文档必须区分本地验证、线上发布和 Android 验收。
