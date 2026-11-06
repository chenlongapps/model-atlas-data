# DeepSWE / Vals Terminal-Bench 成绩同步（2026-11-06）

## 结果

修改 66 个已有模型文件，新增 80 条、更新 44 条成绩；另有 6 条精确记录已一致、保持不变。没有新增模型或 Benchmark 定义，没有修改模型基本信息、描述、本地化或其他 Benchmark 成绩。

| 来源 | 来源行数 | 新增 | 更新/补全 | 已一致 | 跳过 |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSWE v1.1，pass@1 | 70 | 50 | 13 | 6 | 1 |
| Vals Terminal-Bench 4.0，overall | 61 | 30 | 31 | 0 | 0 |

已对应的 130 条来源记录分别覆盖 DeepSWE 的 27 个模型、Vals 的 60 个模型；Muse Spark 1.3 的 max 和 xhigh 分别保存。成绩只在模型 TOML 中维护；本文不重复维护成绩清单。

## 来源与处理规则

- [DeepSWE 原始 JSON](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json)：`generated_at = 2026-09-22T06:27:15.860279+00:00`，全任务集 113 项。使用 `pass_at_1`，按现有定义的百分数单位精确乘以 100，不取整、不使用 pass@4，也不从通过数推算分数。
- [DeepSWE 方法及内嵌榜单](https://deepswe.datacurve.ai/blog/deepswe-v1-1)、[首页](https://deepswe.datacurve.ai/)：核对模型、档位、运行次数和成本。逐配置保留已尝试任务数、有效尝试数、四次运行及错误排除规则；Opus 4.8 max 只尝试了 111 项任务，不假设全部完成。置信区间原始比例值保存在注释中；上下文窗口失败、Agent 超时仍按来源计为失败。
- [Vals 原始 JSON](https://www.vals.ai/_astro/benchmark_view_terminal_bench_4.g-vQx4Dh.json)：`metadata.updated = 2026-11-05`。读取 `tasks.overall` 的原始 `accuracy`，保留三位小数或其实际精度；不导入七个分类分数。
- [Vals 方法](https://www.vals.ai/benchmarks/terminal-bench-4)：66 项任务，mini-swe-agent，三次完整 pass@1 的均值 avg@3；每任务 8 小时，不设步骤或费用上限。方法明确是任务验证器的二元通过率，因此这些行的 `accuracy` 与本地定义的 `task resolution rate` 表达同一评分，不做指标换算。旧记录的显示误差与当前标准误在注释中保留。
- 档位只读取当前行的 `reasoning_effort` / `compute_effort` 原字符串；空值省略，不从模型页默认设置、模型名称、`config` 的 default 后缀或旧 `variant` 解析。温度、top_p、输出上限和 Provider 等已知逐行设置保存在注释中，不当作模型固有属性。
- DeepSWE 无冲突成本使用 JSON 的 `mean_cost_usd`，即已评分尝试的平均任务费用，单位 `USD/task`；不使用中位数、不从 token 单价重算。Vals 使用同一行的 `cost_per_test`，单位 `USD/test`，不混用总评测成本。
- 更新时间、核验时间都不作为评测日期；不补 `date`。保留其他来源、不同 Harness 或不同条件的已有成绩，不自动选最高分，也不生成可比性未经确认的排名。
- 复用 `deepswe-v1.1`、`terminal-bench-v4` 定义；后者已声明兼容 `4.0` 和 `4.0.0`。原有记录的合法版本写法保持不变。

### 非直接路径映射

机构前缀及连字符/小数点差异按模型身份核对；Provider 不是模型研发机构。以下特殊 ID 另有明确依据：

| 来源 ID | 本地模型/条件 | 依据 |
| --- | --- | --- |
| `alibaba/qwen3.8-max-internal` | `alibaba/qwen3.8-max-0902` | Vals 公开榜单显示 Qwen 3.8 Max 0902，与旧 Max 分列；已有成本核对记录亦确认该内部键 |
| `meta/muse_spark_1_3_max` | `meta/muse-spark-1.3`，effort=`max` | [Vals 配置页](https://www.vals.ai/models/meta_muse_spark_1_3_max)及逐行 max 设置；xhigh 单列 |
| `mistralai/mistral-large-4-oss` | `mistral/mistral-large-4-1t-a52b` | [Vals 模型页](https://www.vals.ai/models/mistralai_mistral-large-4-oss)明确为 10 月 29 日开放权重版本，不合并 10 月 6 日 Preview |
| `reflection/Beam-1.0` | `reflection/beam-1.0-501b-a23b` | [Vals 模型页](https://www.vals.ai/models/reflection_Beam-1.0)及已有 Beam 1.0 档案 |
| `openai/gpt-5.4-mini-2026-03-17` | `openai/gpt-5.4-mini` | [Vals 模型页](https://www.vals.ai/models/openai_gpt-5.4-mini-2026-03-17)与本地发布版本均为 2026-03-17 |
| `meta/muse-wonder` | `meta/muse-wonder-1.0` | 已有来源、档位及成本对应，Wonder Full 继续单独保存 |
| `baseten/nemotron-3.5-super-vl-120b-a12b` | `nvidia/nemotron-3.5-super-vl-120b-a12b` | Baseten 是评测 Provider；本地原有同一来源记录已对应 NVIDIA 模型 |

## 跳过及待核实

1. **DeepSWE 一条检查点身份不明确**：JSON 的 `deepseek-v4-flash` 没有日期后缀，本地已有 Datacurve 成绩归在 `deepseek-v4-flash-0731`，另有早期 V4 Flash 档案。未核实精确检查点前，不修改旧成绩，也不向任一版本复制该行；在旧记录旁标注待复核。
2. **18 条已同步成绩的 DeepSWE 成本有冲突**：官网内嵌榜单和指定 JSON 的同配置 `mean_cost_usd` 不同，尚无可靠重定价依据。涉及 GPT-5.6 Sol、Luna、Terra 各五个档位，以及 GLM-5.3 Flash max、DeepSeek V4 Pro max、Gemini 3.6 Flash high。成绩照常保留，`cost` / `cost_unit` 均保持缺失；双方原始费用写入对应 TOML 注释，不自动选择较低或较高费用。跳过的 V4 Flash 行也有成本差异，但未导入该行。
3. **Vals 两条历史记录保留**：GPT-6 Sol 模型页旧值 34.34 与当前 overall 44.444 的实验/修订关系无法确认；旧 Qwen3.8 Max 模型页记录注明 single run，而当前 JSON 为 avg@3。旧记录不覆盖、不并入新记录，也不套用当前费用；对应模型文件已加注释。
4. **Beam 成本未提供**：Vals 的 `cost_per_test = null`，保持缺失，未填零。Vals 的明确零分可以保存，不代表零费用。
5. 不更新 `gemini-flash-latest` 等滚动别名的旧副本，不把指定模型结果自动传播到别名或其他版本。
6. **再分发许可需人工确认**：核对到 [Datacurve 代码仓库 LICENSE](https://raw.githubusercontent.com/datacurve-ai/deep-swe/main/LICENSE) 为 Apache-2.0，但不能据此断言网站榜单数据同样获得授权。Vals 页面标注 All rights reserved，JSON 未附单独数据许可；Models.dev 的 MIT 许可亦不自动覆盖第三方成绩。公开分发前仍应确认榜单数值和成本的适用授权，未复制任务内容或评测轨迹。

## 来源内容标识

2026-11-06 复取的 JSON 与本次读取的内容一致。以下是原始 HTTP 响应字节的 SHA-256；哈希仅识别内容，不证明真实性或许可。

| 来源 | SHA-256 |
| --- | --- |
| DeepSWE JSON | `a7c15d66288fd249c020b9931c017b92d1a3b90e480b3ff34974b752bd030019` |
| Vals Terminal-Bench JSON | `5ba784b71ce48173da02c365ac5c2f7bc09a99c5c489af560d08dd2639a63100` |

## 校验

- `python3 scripts/validate.py`：867 个 TOML，全部通过。
- `python3 -m unittest discover -s tests -v`：104 项通过。
- `node --test tests/web.test.mjs`：19 项通过。
- `python3 scripts/build.py`：生成 855 个模型、11 个定义、1 个语言文件的 JSON，构建成功；`dist/` 只由构建更新，不提交。
- 一次性只读审计：逐条对照 130 条已对应来源记录的分数、档位、成本值或缺失状态及定义唯一性；确认 66 个模型的基本字段、其他成绩及原有记录顺序未改变。18 条有冲突成本保持缺失，Beam 无成本；没有把成本元数据当作新的成绩身份。
- `git diff --check`：通过。
- 仓库原有定义未匹配警告从 1,204 条降至 1,184 条，歧义仍为 0；本次对应的 130 条来源记录均唯一匹配定义。其余未匹配项未扩大处理范围。原有 3 条中文模型描述翻译缺失仍保留；本次描述未变，无需改本地化。

以上检查不等同于完整上游 Schema、所有历史来源或数据再分发许可验证。`TODO.md` 中执行期间出现的独立改动未由本任务修改或回退。

## 修改的模型文件（66）

所有路径均位于 `models/`：

```text
alibaba/qwen3.8-max-0902.toml
alibaba/qwen3.8-max.toml
anthropic/claude-fable-5-1.toml
anthropic/claude-fable-5.toml
anthropic/claude-haiku-5-5.toml
anthropic/claude-opus-4-8.toml
anthropic/claude-opus-5-5.toml
anthropic/claude-opus-5.toml
anthropic/claude-sonnet-4-6.toml
anthropic/claude-sonnet-5-5.toml
anthropic/claude-sonnet-5.toml
deepseek/deepseek-v4-flash-0731.toml
deepseek/deepseek-v4-pro-0813.toml
deepseek/deepseek-v4-pro.toml
deepseek/deepseek-v4.1-flash-1017.toml
deepseek/deepseek-v4.1-flash.toml
fireworks/ember-1.toml
google/gemini-3.1-pro-preview.toml
google/gemini-3.5-flash.toml
google/gemini-3.6-flash.toml
google/gemini-3.7-flash.toml
google/gemini-3.8-flash.toml
google/gemini-4-argon.toml
google/gemini-4-carbon.toml
inception/mercury-2.5.toml
inception/mercury-3.toml
meta/muse-spark-1.1.toml
meta/muse-spark-1.2.toml
meta/muse-spark-1.3.toml
meta/muse-spark-open.toml
meta/muse-wonder-1.0.toml
meta/muse-wonder-full.toml
minimax/MiniMax-M3.1-Flash.toml
minimax/MiniMax-M3.toml
mistral/mistral-large-4-1t-a52b.toml
mistral/mistral-large-4.toml
moonshotai/kimi-k2.7-code.toml
moonshotai/kimi-k3.1-pro.toml
moonshotai/kimi-k3.toml
nvidia/nemotron-3.5-super-vl-120b-a12b.toml
openai/gpt-5.4-mini.toml
openai/gpt-5.5.toml
openai/gpt-5.6-luna.toml
openai/gpt-5.6-sol.toml
openai/gpt-5.6-terra.toml
openai/gpt-6-astra.toml
openai/gpt-6-luna.toml
openai/gpt-6-sol.toml
openai/gpt-6.1-sol.toml
openai/gpt-6.1-terra.toml
reflection/beam-1.0-501b-a23b.toml
stepfun/step-5-preview.toml
tencent/hy4-preview.toml
tencent/hy4.toml
thinkingmachines/inkling-2-small.toml
thinkingmachines/inkling-small.toml
thinkingmachines/inkling.toml
xai/grok-4.5.toml
xai/grok-4.6.toml
xai/grok-4.7.toml
xiaomi/mimo-v2.5-pro.toml
xiaomi/mimo-v2.6-flash.toml
xiaomi/mimo-v2.6-pro.toml
zhipuai/glm-5.2.toml
zhipuai/glm-5.3-flash.toml
zhipuai/glm-5.3.toml
```
