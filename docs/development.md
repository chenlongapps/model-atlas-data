# 开发与校验

[文档导航](README.md) · [数据规范](data-format.md)

## 环境与常用命令

使用 Python 3.11+。语法检查、构建、网页预览只需标准库；同步和完整 Python 测试需要 `tomlkit`，版本与工作流保持一致。

在仓库根目录运行：

```sh
python3 scripts/validate.py
python3 scripts/build.py

# 完整测试
python3 -m pip install tomlkit==0.13.3
python3 -m unittest discover -s tests -v

# 网页测试需要 Node.js 20+
node --test tests/web.test.mjs

git diff --check
```

## 检查范围

| 检查 | 覆盖内容 | 不覆盖内容 |
| --- | --- | --- |
| `validate.py` | 递归解析 `models/`、`benchmarks/`、`i18n/` 的 TOML，报告位置与成功/失败数量 | Schema、字段语义、成绩真实性 |
| `build.py` | 路径、`schema = 2`、主要字段类型、成绩必填项与重复/冲突、URL 格式、定义必填项及唯一 ID、本地化结构和键引用 | 完整上游 Schema、联网核验来源、翻译语义、许可授权 |
| 单元测试 | 脚本及网页行为的回归检查 | 所有模型资料或评测条件的人工审核 |

`validate.py` 全部通过返回 `0`；语法、编码、读取错误或未找到 TOML 时返回 `1`。从其他目录运行可使用脚本绝对路径。

构建错误使 `build.py` 返回 `1`；以下情况只警告，不阻止构建：成绩未匹配定义、匹配歧义、来源缺失、现有语言缺少描述翻译。未知本地化 ID、无效字段类型等仍是错误。没有有效模型时失败，`benchmarks/` 和 `i18n/` 可以暂缺。

**构建成功不等于资料已核实。** 修改数据后还需对照来源、实验条件和模型版本；修改本地化后还需检查译文与原文一致。区分历史警告和本次新增问题，不为消除警告编造数据或新增定义。

## JSON 输出

默认输出到仓库的 `dist/`，不提交 Git：

```text
dist/
  models.json        # { "<lab>/<model-id>": { ...模型字段... } }
  benchmarks.json    # { "<benchmark-id>": { ...定义字段... } }
  i18n/
    zh-CN.json       # 保留原本地化表结构
```

- 模型保留 `schema`；Benchmark 的 `id` 用作对象键，不在定义内部重复。
- 不增加顶层 `version`、内嵌翻译、派生 `results` 或排行榜。
- 保留源字段（包括可转换为 JSON 的未知字段）、数组顺序、条件、来源和缺失状态；不补默认值、不合并成绩、不选择最高分。
- JSON 不保留 TOML 注释和数字书写形式，例如 `42.10` 可能输出为 `42.1`；不主动取整或重评分。NaN、Infinity 和不能直接转换为 JSON 的 TOML 日期/时间值被拒绝，日期应为源格式要求的字符串。
- 使用 UTF-8、稳定键排序及末尾换行，相同源数据得到相同内容。

可指定源仓库和输出目录；显式相对路径以当前工作目录为基准：

```sh
python3 /path/to/model-atlas-data/scripts/build.py \
  --root /path/to/model-atlas-data --output /path/to/output
```

全部校验、序列化和临时文件写入成功后，才逐文件原子替换产物；这不是整个目录的事务，替换阶段 I/O 故障可能留下部分更新，应修复后重跑。脚本不清空输出目录；已无对应源文件的旧 `i18n/*.json` 须手动移走。正式发布使用全新目录，见[发布说明](publishing.md)。

## 修改后报告

数据任务完成后简短列出修改路径、新增/修正成绩数、新建定义、主要来源、实际执行的检查，以及跳过项、冲突、来源与许可限制。不要声称未运行的检查已通过；无需另存一次性执行报告。
