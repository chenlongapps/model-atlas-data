# Benchmark 收集总览

统计由模型源 TOML、Benchmark 定义和单模型状态文档生成。覆盖率计入名称和指标匹配且版本精确一致或明确列入定义兼容版本的成绩；定义标为 unspecified 时，源记录可省略 version。

## 总体统计

| 指标 | 数值 |
|---|---:|
| 模型总数 | 849 |
| 已完成首轮检查 | 352 |
| 正在处理 | 0 |
| 尚未处理 | 497 |
| 存在待核实问题的模型 | 204 |
| 整体状态为待复核的模型 | 204 |
| 已有 Benchmark 成绩的模型 | 212 |
| 已收录的原始成绩条数 | 1738 |
| Benchmark 定义总数 | 11 |
| 最后更新时间 | 2026-11-05T12:13+08:00（Asia/Shanghai） |

首轮检查完成表示 11 项都已尝试并形成结果；其中待核实或冲突的模型仍显示待复核。模型处理进度、Benchmark 检查进度与成绩覆盖率分别按队列状态、单模型状态和源 TOML 统计。

## 11 项 Benchmark 覆盖统计

已检查模型计入已收录、已存在、未找到、不适用等完成核验状态。待核实、冲突和失败单独列出。待检查表示尚未尝试；覆盖率 = 已收录模型 / 模型总数。

| Benchmark | 已收录模型 | 已检查模型 | 待检查模型 | 检索中 | 待复核/失败 | 收录覆盖率 |
|---|---:|---:|---:|---:|---:|---:|
| DeepSWE (deepswe-v1.1) | 33 | 238 | 497 | 0 | 114 | 3.9% |
| SWE-bench Pro (swe-bench-pro-v2) | 15 | 271 | 497 | 0 | 81 | 1.8% |
| Terminal-Bench (terminal-bench-v4) | 46 | 225 | 497 | 0 | 127 | 5.4% |
| Terminal-Bench-Science (terminal-bench-science-v0.1) | 30 | 249 | 497 | 0 | 103 | 3.5% |
| AutomationBench (automationbench-v1.0.6) | 18 | 186 | 497 | 0 | 166 | 2.1% |
| OSWorld (osworld-v2.1) | 4 | 249 | 497 | 0 | 103 | 0.5% |
| Chartography (chartography) | 38 | 310 | 497 | 0 | 42 | 4.5% |
| Humanity's Last Exam (humanitys-last-exam) | 86 | 277 | 497 | 0 | 75 | 10.1% |
| Artificial Analysis Intelligence Index (artificial-analysis-intelligence-index-v5) | 39 | 305 | 497 | 0 | 47 | 4.6% |
| GDPval-AA (gdpval-aa-v2.1) | 46 | 257 | 497 | 0 | 95 | 5.4% |
| Vals Index (vals-index-v2.2) | 27 | 281 | 497 | 0 | 71 | 3.2% |

## 全模型 Benchmark 状态矩阵

图例：✅ 已收录或已核实存在；❌ 已检查未找到公开成绩；⏳ 正在检索或待核实；⚠️ 冲突或检查失败；➖ 不适用；— 尚未检查。状态来自单模型详细文档；表格不显示分数。

| 模型 | 发布日期 | DeepSWE | SWE-Pro | TBench 4 | TBench Science | AutomationBench | OSWorld 2.1 | Chartography | HLE | AA Index V5 | GDPval-AA | Vals Index |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [GPT-6.1 Terra (openai/gpt-6.1-terra)](models/openai/gpt-6.1-terra.md) | 2026-10-26 | ⏳ | ⏳ | ✅ | ✅ | ⏳ | ⏳ | ❌ | ⏳ | ✅ | ✅ | ⚠️ |
| [Kimi K3.1 Pro (moonshotai/kimi-k3.1-pro)](models/moonshotai/kimi-k3.1-pro.md) | 2026-10-23 | ⏳ | ❌ | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ⚠️ | ✅ |
| [Flint (recursive/flint)](models/recursive/flint.md) | 2026-10-21 | ❌ | ✅ | ❌ | ⏳ | ⏳ | ❌ | ➖ | ❌ | ❌ | ❌ | ❌ |
| [elephant-1 (baseten/elephant-1)](models/baseten/elephant-1.md) | 2026-10-19 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [mammoth-1 (baseten/mammoth-1)](models/baseten/mammoth-1.md) | 2026-10-19 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiniMax-M3.1-Flash (minimax/MiniMax-M3.1-Flash)](models/minimax/MiniMax-M3.1-Flash.md) | 2026-10-19 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ⏳ | ✅ |
| [DeepSeek V4.1 Flash 1017 (deepseek/deepseek-v4.1-flash-1017)](models/deepseek/deepseek-v4.1-flash-1017.md) | 2026-10-17 | ✅ | ❌ | ✅ | ✅ | ✅ | ⏳ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Mercury 3 (inception/mercury-3)](models/inception/mercury-3.md) | 2026-10-16 | ❌ | ❌ | ✅ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ✅ |
| [FLUX 3 Image Klein (black-forest-labs/flux-3-image-klein)](models/black-forest-labs/flux-3-image-klein.md) | 2026-10-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Krea 3 (krea/krea-3)](models/krea/krea-3.md) | 2026-10-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Muse Spark Open (meta/muse-spark-open)](models/meta/muse-spark-open.md) | 2026-10-15 | ✅ | ✅ | ⚠️ | ✅ | ⏳ | ❌ | ❌ | ⏳ | ✅ | ❌ | ✅ |
| [Nemotron 3.5 Super 120B A12B (nvidia/nemotron-3.5-super-120b-a12b)](models/nvidia/nemotron-3.5-super-120b-a12b.md) | 2026-10-15 | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ⏳ | ➖ | ❌ | ❌ | ❌ |
| [Nemotron 3.5 Super VL 120B A12B (nvidia/nemotron-3.5-super-vl-120b-a12b)](models/nvidia/nemotron-3.5-super-vl-120b-a12b.md) | 2026-10-15 | ⏳ | ❌ | ⚠️ | ⏳ | ⏳ | ❌ | ⏳ | ✅ | ⏳ | ❌ | ⏳ |
| [pplx-decider-flash-v1.2 (perplexity/pplx-decider-flash-v1.2)](models/perplexity/pplx-decider-flash-v1.2.md) | 2026-10-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [pplx-decider-v1.2 (perplexity/pplx-decider-v1.2)](models/perplexity/pplx-decider-v1.2.md) | 2026-10-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Jev 1.14 (typesafe/jev-1.14.0)](models/typesafe/jev-1.14.0.md) | 2026-10-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok Voice 3.0 (xai/grok-voice-3.0)](models/xai/grok-voice-3.0.md) | 2026-10-14 | ❌ | ❌ | ❌ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ❌ | ❌ |
| [Drama 3 (fish-audio/drama-3)](models/fish-audio/drama-3.md) | 2026-10-13 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini 4 Argon (google/gemini-4-argon)](models/google/gemini-4-argon.md) | 2026-10-13 | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ✅ | ❌ | ✅ | ⏳ | ✅ |
| [HeyGen Voice (heygen/heygen-voice-1)](models/heygen/heygen-voice-1.md) | 2026-10-13 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [HeyGen Voice Turbo (heygen/heygen-voice-1-turbo)](models/heygen/heygen-voice-1-turbo.md) | 2026-10-13 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Muse Wonder (meta/muse-wonder-1.0)](models/meta/muse-wonder-1.0.md) | 2026-10-12 | ✅ | ✅ | ✅ | ✅ | ⏳ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| [Muse Wonder Full (meta/muse-wonder-full)](models/meta/muse-wonder-full.md) | 2026-10-12 | ✅ | ❌ | ✅ | ✅ | ⏳ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| [d3 (vllm-sr/d3)](models/vllm-sr/d3.md) | 2026-10-10 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [d3-flash (vllm-sr/d3-flash)](models/vllm-sr/d3-flash.md) | 2026-10-10 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen-Image-2.1-Turbo (alibaba/qwen-image-2.1-turbo)](models/alibaba/qwen-image-2.1-turbo.md) | 2026-10-09 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [LightOnOCR-3 0.8B (lightonai/lightonocr-3-0.8b)](models/lightonai/lightonocr-3-0.8b.md) | 2026-10-08 | ❌ | ❌ | ⏳ | ❌ | ➖ | ➖ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Phocinae Largha 150M v1 (phocinae/phocinae-largha-150m-v1)](models/phocinae/phocinae-largha-150m-v1.md) | 2026-10-08 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Claude Haiku 5.5 (anthropic/claude-haiku-5-5)](models/anthropic/claude-haiku-5-5.md) | 2026-10-07 | ❌ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | ⏳ | ✅ | ✅ | ✅ |
| [MiniCPM-V 4.7 35B-A3B (openbmb/minicpm-v-4.7-35b-a3b)](models/openbmb/minicpm-v-4.7-35b-a3b.md) | 2026-10-07 | ❌ | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Nano Banana 2.1 (google/gemini-nano-banana-2.1)](models/google/gemini-nano-banana-2.1.md) | 2026-10-06 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ❌ | ❌ | ➖ | ➖ | ➖ |
| [Mistral Large 4 (mistral/mistral-large-4)](models/mistral/mistral-large-4.md) | 2026-10-06 | ⏳ | ⏳ | ✅ | ❌ | ⏳ | ⏳ | ❌ | ⏳ | ✅ | ⏳ | ⏳ |
| [Drex 2.0 (nace-ai/drex-v2.0)](models/nace-ai/drex-v2.0.md) | 2026-10-06 | ➖ | ➖ | ➖ | ➖ | ❌ | ⏳ | ➖ | ⏳ | ➖ | ➖ | ➖ |
| [MiniCPM-V 4.7 1B (openbmb/minicpm-v-4.7-1b)](models/openbmb/minicpm-v-4.7-1b.md) | 2026-10-06 | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Beam 1.0 501B A23B (reflection/beam-1.0-501b-a23b)](models/reflection/beam-1.0-501b-a23b.md) | 2026-10-05 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ | ➖ | ⏳ | ⚠️ | ✅ | ❌ | ✅ |
| [Sage 1.4 (levanto/levanto-sage-v1.4)](models/levanto/levanto-sage-v1.4.md) | 2026-10-04 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Kolibri 1 (aleph-alpha/kolibri-1)](models/aleph-alpha/kolibri-1.md) | 2026-10-03 | ❌ | ❌ | ❌ | ❌ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ❌ | ❌ |
| [Qwen-Image-2.1-Pro (alibaba/qwen-image-2.1-pro)](models/alibaba/qwen-image-2.1-pro.md) | 2026-10-02 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [FLUX 3 Image (black-forest-labs/flux-3-image)](models/black-forest-labs/flux-3-image.md) | 2026-10-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Clef (cloudflare/clef)](models/cloudflare/clef.md) | 2026-10-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Clef Flash (cloudflare/clef-flash)](models/cloudflare/clef-flash.md) | 2026-10-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MAI-Voice-2.1 (microsoft/mai-voice-2.1)](models/microsoft/mai-voice-2.1.md) | 2026-10-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MAI-Voice-2.1-Flash (microsoft/mai-voice-2.1-flash)](models/microsoft/mai-voice-2.1-flash.md) | 2026-10-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok Imagine Video 1.5 Lite (xai/grok-imagine-video-1.5-lite)](models/xai/grok-imagine-video-1.5-lite.md) | 2026-10-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Embed 5 Fast (cohere/embed-v5.0-fast)](models/cohere/embed-v5.0-fast.md) | 2026-09-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Embed 5 Pro (cohere/embed-v5.0-pro)](models/cohere/embed-v5.0-pro.md) | 2026-09-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [HeyGen Video (heygen/heygen-video-1)](models/heygen/heygen-video-1.md) | 2026-09-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Mercury Decide (inception/mercury-decide)](models/inception/mercury-decide.md) | 2026-09-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ⏳ | ➖ | ➖ | ➖ |
| [rerank-3 (voyageai/rerank-3)](models/voyageai/rerank-3.md) | 2026-09-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [rerank-3-lite (voyageai/rerank-3-lite)](models/voyageai/rerank-3-lite.md) | 2026-09-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Universal-3.6 Pro (assemblyai/universal-3-6-pro)](models/assemblyai/universal-3-6-pro.md) | 2026-09-29 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Ling 3.1 Flash (inclusionai/ling-3.1-flash)](models/inclusionai/ling-3.1-flash.md) | 2026-09-29 | ⏳ | ⏳ | ✅ | ❌ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ⚠️ | ❌ |
| [Liquid d1 (liquid/d1)](models/liquid/d1.md) | 2026-09-29 | ➖ | ➖ | ➖ | ➖ | ➖ | ❌ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-6.1 Sol (openai/gpt-6.1-sol)](models/openai/gpt-6.1-sol.md) | 2026-09-29 | ⏳ | ✅ | ✅ | ✅ | ⏳ | ❌ | ❌ | ❌ | ⚠️ | ⏳ | ✅ |
| [Claude Sonnet 5.5 (anthropic/claude-sonnet-5-5)](models/anthropic/claude-sonnet-5-5.md) | 2026-09-28 | ⏳ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| [Eleven v4 (elevenlabs/eleven_v4)](models/elevenlabs/eleven_v4.md) | 2026-09-28 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Eleven v4 Turbo (elevenlabs/eleven_v4_turbo)](models/elevenlabs/eleven_v4_turbo.md) | 2026-09-28 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Drex 1.5 (nace-ai/drex-v1.5)](models/nace-ai/drex-v1.5.md) | 2026-09-28 | ➖ | ➖ | ➖ | ➖ | ➖ | ⏳ | ➖ | ⏳ | ➖ | ➖ | ➖ |
| [MiniMax-M3.1-Flash-Preview (minimax/MiniMax-M3.1-Flash-Preview)](models/minimax/MiniMax-M3.1-Flash-Preview.md) | 2026-09-27 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [LongCat-2.5-Preview (meituan/longcat-2.5-preview)](models/meituan/longcat-2.5-preview.md) | 2026-09-25 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Perceptron Mk1.5 (perceptron/perceptron-mk1.5)](models/perceptron/perceptron-mk1.5.md) | 2026-09-25 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Qwen 3.8 Max Prime (alibaba/qwen3.8-max-prime)](models/alibaba/qwen3.8-max-prime.md) | 2026-09-23 | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Recraft V4.1 Flash (recraft/recraft-v4.1-flash)](models/recraft/recraft-v4.1-flash.md) | 2026-09-23 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Claude Opus 5.5 (anthropic/claude-opus-5-5)](models/anthropic/claude-opus-5-5.md) | 2026-09-22 | ✅ | ⏳ | ✅ | ✅ | ✅ | ⚠️ | ⏳ | ✅ | ✅ | ⚠️ | ✅ |
| [Ember-1 (fireworks/ember-1)](models/fireworks/ember-1.md) | 2026-09-22 | ⚠️ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Gemini 3.8 Flash Lite TTS (google/gemini-3.8-flash-lite-tts)](models/google/gemini-3.8-flash-lite-tts.md) | 2026-09-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini 3.8 Flash TTS (google/gemini-3.8-flash-tts)](models/google/gemini-3.8-flash-tts.md) | 2026-09-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-6 Luna (openai/gpt-6-luna)](models/openai/gpt-6-luna.md) | 2026-09-22 | ⏳ | ❌ | ⚠️ | ⚠️ | ✅ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ |
| [GPT-6 Sol (openai/gpt-6-sol)](models/openai/gpt-6-sol.md) | 2026-09-22 | ⏳ | ❌ | ⚠️ | ⚠️ | ✅ | ❌ | ✅ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Hy Image 3.5 Preview (tencent/hy-image-v3.5-preview)](models/tencent/hy-image-v3.5-preview.md) | 2026-09-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Solar Mini 4 (upstage/solar-mini4)](models/upstage/solar-mini4.md) | 2026-09-22 | ❌ | ❌ | ✅ | ❌ | ⏳ | ❌ | ➖ | ⚠️ | ⏳ | ✅ | ❌ |
| [MiMo-V2.6-Flash (xiaomi/mimo-v2.6-flash)](models/xiaomi/mimo-v2.6-flash.md) | 2026-09-22 | ⚠️ | ❌ | ✅ | ⏳ | ✅ | ❌ | ❌ | ✅ | ⏳ | ✅ | ⏳ |
| [MiMo-V2.6-Pro (xiaomi/mimo-v2.6-pro)](models/xiaomi/mimo-v2.6-pro.md) | 2026-09-22 | ⚠️ | ❌ | ✅ | ⏳ | ✅ | ❌ | ❌ | ✅ | ⏳ | ⚠️ | ⏳ |
| [Rune 26B-A4B (surogate/rune-26b-a4b)](models/surogate/rune-26b-a4b.md) | 2026-09-21 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Viv Fast (vivgrid/viv-fast)](models/vivgrid/viv-fast.md) | 2026-09-21 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [Grok 4.7 (xai/grok-4.7)](models/xai/grok-4.7.md) | 2026-09-21 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ⏳ | ⏳ | ✅ | ✅ |
| [MiMo-V2.6-Pro-UltraSpeed (xiaomi/mimo-v2.6-pro-ultraspeed)](models/xiaomi/mimo-v2.6-pro-ultraspeed.md) | 2026-09-21 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Transcribe 1 Pro (fish-audio/transcribe-1-pro)](models/fish-audio/transcribe-1-pro.md) | 2026-09-18 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.8 Omni Flash (alibaba/qwen3.8-omni-flash)](models/alibaba/qwen3.8-omni-flash.md) | 2026-09-17 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ⏳ | ❌ | ❌ |
| [Pareto (unbiased/pareto)](models/unbiased/pareto.md) | 2026-09-17 | ⏳ | ❌ | ✅ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ⏳ | ⏳ | ❌ |
| [Grok Voice Transcribe 2.0 (xai/grok-voice-transcribe-2.0)](models/xai/grok-voice-transcribe-2.0.md) | 2026-09-17 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Arrow 2 (quiverai/arrow-2)](models/quiverai/arrow-2.md) | 2026-09-16 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ➖ | ➖ |
| [Arrow 2 Telos (quiverai/arrow-2-telos)](models/quiverai/arrow-2-telos.md) | 2026-09-16 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ➖ | ➖ |
| [Step 5 Preview (stepfun/step-5-preview)](models/stepfun/step-5-preview.md) | 2026-09-16 | ✅ | ❌ | ⏳ | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ |
| [Gemini 3.8 Live (google/gemini-3.8-live)](models/google/gemini-3.8-live.md) | 2026-09-15 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Gemini 3.8 Live Extended Thinking (google/gemini-3.8-live-extended-thinking)](models/google/gemini-3.8-live-extended-thinking.md) | 2026-09-15 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Jev 1.13 (typesafe/jev-1.13.0)](models/typesafe/jev-1.13.0.md) | 2026-09-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ❌ | ➖ | ➖ | ➖ |
| [Jev (typesafe/jev-latest)](models/typesafe/jev-latest.md) | 2026-09-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen-Image-2.1 (alibaba/qwen-image-2.1)](models/alibaba/qwen-image-2.1.md) | 2026-09-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Scribe v2 Medical (elevenlabs/scribe_v2_medical)](models/elevenlabs/scribe_v2_medical.md) | 2026-09-11 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Kimi K2.8 Preview (moonshotai/kimi-k2.8-preview)](models/moonshotai/kimi-k2.8-preview.md) | 2026-09-11 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Fugu Max (sakana/fugu-max)](models/sakana/fugu-max.md) | 2026-09-11 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ |
| [Fugu Ultra v2 (sakana/fugu-ultra-v2)](models/sakana/fugu-ultra-v2.md) | 2026-09-11 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ |
| [DeepSeek V4.1 Flash (deepseek/deepseek-v4.1-flash)](models/deepseek/deepseek-v4.1-flash.md) | 2026-09-10 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ⏳ | ❌ | ✅ | ❌ |
| [Ling 3.0 Flash VL (inclusionai/ling-3.0-flash-vl)](models/inclusionai/ling-3.0-flash-vl.md) | 2026-09-10 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ❌ |
| [GPT-Live 1 (openai/gpt-live-1)](models/openai/gpt-live-1.md) | 2026-09-10 | ❌ | ❌ | ❌ | ⏳ | ⏳ | ➖ | ➖ | ❌ | ➖ | ➖ | ➖ |
| [North Small Translate (cohere/north-small-translate-1-0)](models/cohere/north-small-translate-1-0.md) | 2026-09-09 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Mercury 2.5 (inception/mercury-2.5)](models/inception/mercury-2.5.md) | 2026-09-08 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ⏳ | ⏳ |
| [GPT Image 2.5 Flare (openai/gpt-image-2.5-flare)](models/openai/gpt-image-2.5-flare.md) | 2026-09-08 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT Image 2.5 Sunburst (openai/gpt-image-2.5-sunburst)](models/openai/gpt-image-2.5-sunburst.md) | 2026-09-08 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiniCPM5-2B (openbmb/minicpm5-2b)](models/openbmb/minicpm5-2b.md) | 2026-09-06 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⏳ | ⏳ |
| [Ling 3.0 Flash Sante (inclusionai/ling-3.0-flash-sante)](models/inclusionai/ling-3.0-flash-sante.md) | 2026-09-04 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ⏳ | ⏳ |
| [MAI-Image-2.6-Flash (microsoft/mai-image-2.6-flash)](models/microsoft/mai-image-2.6-flash.md) | 2026-09-04 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-6 Astra (openai/gpt-6-astra)](models/openai/gpt-6-astra.md) | 2026-09-04 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | ⏳ | ✅ |
| [GPT-6 Astra (Fast) (openai/gpt-6-astra-fast)](models/openai/gpt-6-astra-fast.md) | 2026-09-04 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| [Lyria 3.5 (google/lyria-3.5)](models/google/lyria-3.5.md) | 2026-09-03 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MAI-Transcribe-2 (microsoft/mai-transcribe-2)](models/microsoft/mai-transcribe-2.md) | 2026-09-03 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.8 Max 0902 (alibaba/qwen3.8-max-0902)](models/alibaba/qwen3.8-max-0902.md) | 2026-09-02 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ✅ | ⏳ | ⏳ | ✅ |
| [Gemini 3.8 Flash (google/gemini-3.8-flash)](models/google/gemini-3.8-flash.md) | 2026-09-02 | ✅ | ⏳ | ⏳ | ⏳ | ✅ | ❌ | ✅ | ✅ | ⏳ | ✅ | ✅ |
| [Muse Spark 1.3 (meta/muse-spark-1.3)](models/meta/muse-spark-1.3.md) | 2026-09-02 | ✅ | ❌ | ⏳ | ⏳ | ✅ | ⏳ | ✅ | ✅ | ⏳ | ✅ | ❌ |
| [Claude Fable 5.1 (anthropic/claude-fable-5-1)](models/anthropic/claude-fable-5-1.md) | 2026-09-01 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⚠️ | ⏳ | ✅ | ✅ | ⏳ | ❌ |
| [Claude Mythos 5.1 (anthropic/claude-mythos-5-1)](models/anthropic/claude-mythos-5-1.md) | 2026-09-01 | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [Muse Voice Transcribe 1.0 (meta/muse-voice-transcribe-1.0)](models/meta/muse-voice-transcribe-1.0.md) | 2026-09-01 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [FLUX Video Edit [fast] (black-forest-labs/flux-video-edit)](models/black-forest-labs/flux-video-edit.md) | 2026-09 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Seedream 5.0 Flash (bytedance-seed/seedream-5.0-flash)](models/bytedance-seed/seedream-5.0-flash.md) | 2026-09 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Hy4 preview (tencent/hy4-preview)](models/tencent/hy4-preview.md) | 2026-08-28 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ❌ | ⏳ | ✅ |
| [Qwen3.8 Flash Next (alibaba/qwen3.8-flash-next)](models/alibaba/qwen3.8-flash-next.md) | 2026-08-27 | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ⏳ | ❌ |
| [Gemini Omni 1.1 Flash (google/gemini-omni-1.1-flash)](models/google/gemini-omni-1.1-flash.md) | 2026-08-27 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Ling 3.0 Flash Fin (inclusionai/ling-3.0-flash-fin)](models/inclusionai/ling-3.0-flash-fin.md) | 2026-08-27 | ❌ | ❌ | ⏳ | ❌ | ❌ | ➖ | ➖ | ⏳ | ❌ | ⏳ | ❌ |
| [Qwen3.8 Flash (alibaba/qwen3.8-flash)](models/alibaba/qwen3.8-flash.md) | 2026-08-26 | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ⏳ | ⏳ | ❌ | ⏳ | ❌ |
| [Gemini 3.5 Transcribe (google/gemini-3.5-transcribe)](models/google/gemini-3.5-transcribe.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini 3.5 Transcribe Live (google/gemini-3.5-transcribe-live)](models/google/gemini-3.5-transcribe-live.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiniMax H3 Max (minimax/MiniMax-H3-Max)](models/minimax/MiniMax-H3-Max.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4 Styles (recraft/recraft-v4-styles)](models/recraft/recraft-v4-styles.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4 Styles Pro (recraft/recraft-v4-styles-pro)](models/recraft/recraft-v4-styles-pro.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4 Styles Pro Vector (recraft/recraft-v4-styles-pro-vector)](models/recraft/recraft-v4-styles-pro-vector.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4 Styles Vector (recraft/recraft-v4-styles-vector)](models/recraft/recraft-v4-styles-vector.md) | 2026-08-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GLM-5.3-Flash (zhipuai/glm-5.3-flash)](models/zhipuai/glm-5.3-flash.md) | 2026-08-26 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| [Granite 4.2 8B (ibm/granite-4.2-8b)](models/ibm/granite-4.2-8b.md) | 2026-08-25 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ➖ | ❌ | ⏳ | ❌ | ❌ |
| [Apodex 1.1 Mini (apodex/apodex-1.1-mini)](models/apodex/apodex-1.1-mini.md) | 2026-08-24 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ |
| [FIBO Generate 1.5 (bria/fibo-generate-1.5)](models/bria/fibo-generate-1.5.md) | 2026-08-24 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [DeepSeek V4 Flash Vision Exp (deepseek/deepseek-v4-flash-vision-exp)](models/deepseek/deepseek-v4-flash-vision-exp.md) | 2026-08-21 | ⏳ | ❌ | ❌ | ❌ | ⏳ | ❌ | ⚠️ | ❌ | ❌ | ✅ | ❌ |
| [Wan3.0-Video-Prime (alibaba/wan3.0-video-prime)](models/alibaba/wan3.0-video-prime.md) | 2026-08-20 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [FLUX Video Upscale (black-forest-labs/flux-video-upscale)](models/black-forest-labs/flux-video-upscale.md) | 2026-08-20 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Ornith 1.5 35B A3B (deepreinforce/ornith-1.5-35b-a3b)](models/deepreinforce/ornith-1.5-35b-a3b.md) | 2026-08-18 | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| [Qwen3.8 27B (alibaba/qwen3.8-27b)](models/alibaba/qwen3.8-27b.md) | 2026-08-14 | ⏳ | ✅ | ❌ | ❌ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [MAI-Image-2.6 (microsoft/mai-image-2.6)](models/microsoft/mai-image-2.6.md) | 2026-08-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GLM-5.3 (zhipuai/glm-5.3)](models/zhipuai/glm-5.3.md) | 2026-08-14 | ⚠️ | ❌ | ⚠️ | ⚠️ | ⏳ | ❌ | ❌ | ✅ | ⏳ | ❌ | ✅ |
| [DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813)](models/deepseek/deepseek-v4-pro-0813.md) | 2026-08-13 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ✅ | ⏳ | ✅ | ✅ |
| [Gemini 3.7 Flash (google/gemini-3.7-flash)](models/google/gemini-3.7-flash.md) | 2026-08-13 | ✅ | ❌ | ⏳ | ⏳ | ✅ | ❌ | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| [Gemini Flash Latest (google/gemini-flash-latest)](models/google/gemini-flash-latest.md) | 2026-08-13 | ✅ | ❌ | ⏳ | ⏳ | ✅ | ❌ | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| [Toast 1 (mixedbread/toast-1)](models/mixedbread/toast-1.md) | 2026-08-13 | ➖ | ➖ | ➖ | ➖ | ❌ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [voyage-code-4 (voyageai/voyage-code-4)](models/voyageai/voyage-code-4.md) | 2026-08-13 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.8 2.4T A95B (alibaba/qwen3.8-2.4t-a95b)](models/alibaba/qwen3.8-2.4t-a95b.md) | 2026-08-12 | ❌ | ❌ | ✅ | ❌ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⚠️ | ❌ |
| [Flux TTS (deepgram/flux-tts)](models/deepgram/flux-tts.md) | 2026-08-12 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok 4.6 (xai/grok-4.6)](models/xai/grok-4.6.md) | 2026-08-12 | ✅ | ❌ | ✅ | ✅ | ⏳ | ❌ | ✅ | ✅ | ❌ | ⏳ | ❌ |
| [MAI-Code-1.1-Flash (microsoft/mai-code-1.1-flash)](models/microsoft/mai-code-1.1-flash.md) | 2026-08-11 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Nemotron 3.5 Lightning 30B A3B (nvidia/nemotron-3.5-lightning)](models/nvidia/nemotron-3.5-lightning.md) | 2026-08-11 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ➖ | ➖ | ✅ | ⏳ | ⏳ | ❌ |
| [Muse Glimmer 30B (meta/muse-glimmer-30b)](models/meta/muse-glimmer-30b.md) | 2026-08-10 | ❌ | ❌ | ✅ | ❌ | ⏳ | ⏳ | ✅ | ✅ | ⏳ | ✅ | ❌ |
| [Motif 3 (motif-technologies/motif-3)](models/motif-technologies/motif-3.md) | 2026-08-07 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ➖ | ➖ | ✅ | ❌ | ❌ | ❌ |
| [GPT-5.6 Cyber (openai/gpt-5.6-cyber)](models/openai/gpt-5.6-cyber.md) | 2026-08-07 | ❌ | ❌ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Grok Imagine Image 2.0 (xai/grok-imagine-image-2.0)](models/xai/grok-imagine-image-2.0.md) | 2026-08-07 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Wan3.0 (alibaba/wan3.0-video)](models/alibaba/wan3.0-video.md) | 2026-08-06 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Solar Pro 4 (upstage/solar-pro4)](models/upstage/solar-pro4.md) | 2026-08-06 | ❌ | ⏳ | ⚠️ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ❌ | ⏳ |
| [Qwen-Image-3.0 (alibaba/qwen-image-3.0)](models/alibaba/qwen-image-3.0.md) | 2026-08-05 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen-Image-3.0-Pro (alibaba/qwen-image-3.0-pro)](models/alibaba/qwen-image-3.0-pro.md) | 2026-08-05 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Muse Spark 1.2 (meta/muse-spark-1.2)](models/meta/muse-spark-1.2.md) | 2026-08-05 | ✅ | ❌ | ✅ | ⏳ | ⏳ | ❌ | ✅ | ⚠️ | ❌ | ⚠️ | ⏳ |
| [FLUX 3 Video (black-forest-labs/flux-3-video)](models/black-forest-labs/flux-3-video.md) | 2026-08-04 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.8 Max (alibaba/qwen3.8-max)](models/alibaba/qwen3.8-max.md) | 2026-08-03 | ✅ | ⏳ | ⚠️ | ✅ | ⏳ | ❌ | ✅ | ⏳ | ❌ | ✅ | ⏳ |
| [Sakana Namazu (sakana/sakana-namazu)](models/sakana/sakana-namazu.md) | 2026-08-03 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Seedance 2.5 (bytedance-seed/seedance-2.5)](models/bytedance-seed/seedance-2.5.md) | 2026-07-31 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [DeepSeek V4 Flash 0731 (deepseek/deepseek-v4-flash-0731)](models/deepseek/deepseek-v4-flash-0731.md) | 2026-07-31 | ✅ | ❌ | ✅ | ✅ | ⏳ | ❌ | ➖ | ⚠️ | ❌ | ⚠️ | ❌ |
| [MiniMax H3 (minimax/MiniMax-H3)](models/minimax/MiniMax-H3.md) | 2026-07-31 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini Robotics-ER 2 Preview (google/gemini-robotics-er-2-preview)](models/google/gemini-robotics-er-2-preview.md) | 2026-07-30 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Gemini Robotics-ER 2 Streaming Preview (google/gemini-robotics-er-2-streaming-preview)](models/google/gemini-robotics-er-2-streaming-preview.md) | 2026-07-30 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Inkling Small (thinkingmachines/inkling-small)](models/thinkingmachines/inkling-small.md) | 2026-07-30 | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ✅ | ✅ | ⏳ | ❌ | ✅ |
| [GPT-Live-Transcribe (openai/gpt-live-transcribe)](models/openai/gpt-live-transcribe.md) | 2026-07-28 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-Transcribe (openai/gpt-transcribe)](models/openai/gpt-transcribe.md) | 2026-07-28 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Claude Opus 5 (anthropic/claude-opus-5)](models/anthropic/claude-opus-5.md) | 2026-07-24 | ✅ | ⏳ | ⏳ | ⏳ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ✅ | ❌ |
| [Ling 3.0 Flash (inclusionai/ling-3.0-flash)](models/inclusionai/ling-3.0-flash.md) | 2026-07-23 | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ➖ | ⏳ | ❌ | ⏳ | ❌ |
| [MAI-Image-2.5-Pro (microsoft/mai-image-2.5-pro)](models/microsoft/mai-image-2.5-pro.md) | 2026-07-23 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MAI-Voice-2-Flash (microsoft/mai-voice-2-flash)](models/microsoft/mai-voice-2-flash.md) | 2026-07-23 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini 3.5 Flash Lite (google/gemini-3.5-flash-lite)](models/google/gemini-3.5-flash-lite.md) | 2026-07-21 | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ⏳ | ⏳ | ❌ | ❌ |
| [Gemini 3.6 Flash (google/gemini-3.6-flash)](models/google/gemini-3.6-flash.md) | 2026-07-21 | ⚠️ | ❌ | ❌ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ❌ | ⏳ | ⏳ |
| [Gemini Flash-Lite Latest (google/gemini-flash-lite-latest)](models/google/gemini-flash-lite-latest.md) | 2026-07-21 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Macaron V1 Tall (mindlab/macaron-v1-tall)](models/mindlab/macaron-v1-tall.md) | 2026-07-21 | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ⏳ |
| [Macaron V1 Venti (mindlab/macaron-v1-venti)](models/mindlab/macaron-v1-venti.md) | 2026-07-21 | ⏳ | ❌ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ⏳ |
| [Laguna S 2.1 (poolside/laguna-s-2.1)](models/poolside/laguna-s-2.1.md) | 2026-07-21 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ➖ | ❌ | ❌ | ❌ | ⏳ |
| [Seed Audio 1.0 (bytedance-seed/seed-audio-1.0)](models/bytedance-seed/seed-audio-1.0.md) | 2026-07-20 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.8 Max Preview (alibaba/qwen3.8-max-preview)](models/alibaba/qwen3.8-max-preview.md) | 2026-07-19 | ⏳ | ⏳ | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ |
| [Mistral OCR 4.1 (mistral/mistral-ocr-4-1)](models/mistral/mistral-ocr-4-1.md) | 2026-07-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Kimi K3 (moonshotai/kimi-k3)](models/moonshotai/kimi-k3.md) | 2026-07-16 | ⚠️ | ✅ | ✅ | ✅ | ⏳ | ❌ | ✅ | ✅ | ❌ | ⏳ | ✅ |
| [Nemotron 3 Embed 1B (nvidia/nemotron-3-embed-1b)](models/nvidia/nemotron-3-embed-1b.md) | 2026-07-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok 4.5 (xai/grok-4.5)](models/xai/grok-4.5.md) | 2026-07-16 | ⏳ | ❌ | ✅ | ❌ | ⏳ | ❌ | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| [Qwen3.7 Flash (alibaba/qwen3.7-flash)](models/alibaba/qwen3.7-flash.md) | 2026-07-15 | ❌ | ❌ | ❌ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Inkling (thinkingmachines/inkling)](models/thinkingmachines/inkling.md) | 2026-07-15 | ❌ | ✅ | ✅ | ✅ | ⏳ | ❌ | ⏳ | ✅ | ✅ | ⚠️ | ✅ |
| [Qwen-Audio-3.0-TTS Flash (alibaba/qwen-audio-3.0-tts-flash)](models/alibaba/qwen-audio-3.0-tts-flash.md) | 2026-07-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen-Audio-3.0-TTS Plus (alibaba/qwen-audio-3.0-tts-plus)](models/alibaba/qwen-audio-3.0-tts-plus.md) | 2026-07-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Muse Spark 1.1 (meta/muse-spark-1.1)](models/meta/muse-spark-1.1.md) | 2026-07-09 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ❌ | ✅ | ⏳ |
| [GPT-5.6 Luna (openai/gpt-5.6-luna)](models/openai/gpt-5.6-luna.md) | 2026-07-09 | ✅ | ❌ | ✅ | ✅ | ⏳ | ❌ | ✅ | ⏳ | ❌ | ⚠️ | ❌ |
| [GPT-5.6 Sol (openai/gpt-5.6-sol)](models/openai/gpt-5.6-sol.md) | 2026-07-09 | ✅ | ✅ | ✅ | ✅ | ⏳ | ❌ | ✅ | ⏳ | ❌ | ⏳ | ❌ |
| [GPT-5.6 Terra (openai/gpt-5.6-terra)](models/openai/gpt-5.6-terra.md) | 2026-07-09 | ✅ | ✅ | ✅ | ✅ | ⏳ | ❌ | ✅ | ⏳ | ❌ | ⚠️ | ❌ |
| [Seedream 5.0 Pro (bytedance-seed/seedream-5.0-pro)](models/bytedance-seed/seedream-5.0-pro.md) | 2026-07-08 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Cohere Transcribe Arabic (cohere/cohere-transcribe-arabic-07-2026)](models/cohere/cohere-transcribe-arabic-07-2026.md) | 2026-07-07 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Muse Image (meta/muse-image-1.0)](models/meta/muse-image-1.0.md) | 2026-07-07 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-Realtime-2.1 (openai/gpt-realtime-2.1)](models/openai/gpt-realtime-2.1.md) | 2026-07-06 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [GPT-Realtime-2.1 Mini (openai/gpt-realtime-2.1-mini)](models/openai/gpt-realtime-2.1-mini.md) | 2026-07-06 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Hy3 (tencent/hy3)](models/tencent/hy3.md) | 2026-07-06 | ⏳ | ❌ | ✅ | ❌ | ⏳ | ➖ | ⏳ | ✅ | ❌ | ✅ | ❌ |
| [Laguna XS 2.1 (poolside/laguna-xs-2.1)](models/poolside/laguna-xs-2.1.md) | 2026-07-02 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ❌ | ❌ | ❌ | ❌ |
| [Claude Sonnet 5 (anthropic/claude-sonnet-5)](models/anthropic/claude-sonnet-5.md) | 2026-06-30 | ✅ | ✅ | ⚠️ | ❌ | ⏳ | ❌ | ⚠️ | ✅ | ❌ | ⚠️ | ❌ |
| [Nano Banana 2 Lite (google/gemini-3.1-flash-lite-image)](models/google/gemini-3.1-flash-lite-image.md) | 2026-06-30 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ⏳ | ❌ |
| [Gemini Omni Flash Preview (google/gemini-omni-flash-preview)](models/google/gemini-omni-flash-preview.md) | 2026-06-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [LongCat-2.0 (meituan/longcat-2.0)](models/meituan/longcat-2.0.md) | 2026-06-30 | ❌ | ❌ | ✅ | ❌ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⚠️ | ❌ |
| [Ornith 1.0 31B (deepreinforce/ornith-1.0-31b)](models/deepreinforce/ornith-1.0-31b.md) | 2026-06-25 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Ornith 1.0 35B (deepreinforce/ornith-1.0-35b)](models/deepreinforce/ornith-1.0-35b.md) | 2026-06-25 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Ornith 1.0 397B (deepreinforce/ornith-1.0-397b)](models/deepreinforce/ornith-1.0-397b.md) | 2026-06-25 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Ornith 1.0 9B (deepreinforce/ornith-1.0-9b)](models/deepreinforce/ornith-1.0-9b.md) | 2026-06-25 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [Seed 2.1 Pro (bytedance-seed/seed-2.1-pro)](models/bytedance-seed/seed-2.1-pro.md) | 2026-06-23 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [Seed 2.1 Turbo (bytedance-seed/seed-2.1-turbo)](models/bytedance-seed/seed-2.1-turbo.md) | 2026-06-23 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [Seed Character (bytedance-seed/seed-character)](models/bytedance-seed/seed-character.md) | 2026-06-23 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ |
| [Seed Evolving (bytedance-seed/seed-evolving)](models/bytedance-seed/seed-evolving.md) | 2026-06-23 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [S2.1 Pro (fish-audio/s2.1-pro)](models/fish-audio/s2.1-pro.md) | 2026-06-23 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [LFM2.5-Embedding-350M (liquid/lfm2.5-embedding-350m)](models/liquid/lfm2.5-embedding-350m.md) | 2026-06-18 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [HappyHorse-1.1 (alibaba/happyhorse-1.1)](models/alibaba/happyhorse-1.1.md) | 2026-06-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Universal-3.5 Pro (assemblyai/universal-3-5-pro)](models/assemblyai/universal-3-5-pro.md) | 2026-06-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Seedance 2.0 Mini (bytedance-seed/seedance-2.0-mini)](models/bytedance-seed/seedance-2.0-mini.md) | 2026-06-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Fugu (sakana/fugu)](models/sakana/fugu.md) | 2026-06-15 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| [Fugu Ultra (sakana/fugu-ultra)](models/sakana/fugu-ultra.md) | 2026-06-15 | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ |
| [GLM-5.2 (zhipuai/glm-5.2)](models/zhipuai/glm-5.2.md) | 2026-06-13 | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ➖ | ➖ | ✅ | ❌ | ❌ | ❌ |
| [Kimi K2.7 Code (moonshotai/kimi-k2.7-code)](models/moonshotai/kimi-k2.7-code.md) | 2026-06-12 | ✅ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ✅ | ❌ | ❌ | ❌ | ⏳ |
| [Kimi K2.7 Code Highspeed (moonshotai/kimi-k2.7-code-highspeed)](models/moonshotai/kimi-k2.7-code-highspeed.md) | 2026-06-12 | ❌ | ❌ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [DiffusionGemma 26B A4B IT (google/diffusiongemma-26b-a4b-it)](models/google/diffusiongemma-26b-a4b-it.md) | 2026-06-10 | ❌ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ❌ | ❌ |
| [Claude Fable 5 (anthropic/claude-fable-5)](models/anthropic/claude-fable-5.md) | 2026-06-09 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ⚠️ | ❌ | ✅ | ❌ |
| [Claude Mythos 5 (anthropic/claude-mythos-5)](models/anthropic/claude-mythos-5.md) | 2026-06-09 | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [North Mini Code (cohere/north-mini-code-1-0)](models/cohere/north-mini-code-1-0.md) | 2026-06-09 | ❌ | ⏳ | ❌ | ❌ | ⏳ | ➖ | ➖ | ❌ | ⏳ | ⏳ | ❌ |
| [Gemini 3.5 Live Translate Preview (google/gemini-3.5-live-translate-preview)](models/google/gemini-3.5-live-translate-preview.md) | 2026-06-09 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiMo-V2.5-Pro-UltraSpeed (xiaomi/mimo-v2.5-pro-ultraspeed)](models/xiaomi/mimo-v2.5-pro-ultraspeed.md) | 2026-06-08 | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ❌ |
| [Riverflow 2.5 Fast (sourceful/riverflow-v2.5-fast)](models/sourceful/riverflow-v2.5-fast.md) | 2026-06-05 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Riverflow 2.5 Pro (sourceful/riverflow-v2.5-pro)](models/sourceful/riverflow-v2.5-pro.md) | 2026-06-05 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Nemotron 3 Ultra 550B A55B (nvidia/nemotron-3-ultra-550b-a55b)](models/nvidia/nemotron-3-ultra-550b-a55b.md) | 2026-06-04 | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ➖ | ➖ | ✅ | ⏳ | ✅ | ⏳ |
| [Nemotron 3.5 ASR Streaming Multilingual 0.6B (nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b)](models/nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b.md) | 2026-06-04 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemma 4 12B IT (google/gemma-4-12b-it)](models/google/gemma-4-12b-it.md) | 2026-06-03 | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [Krea 2 Turbo (krea/krea-2-medium-turbo)](models/krea/krea-2-medium-turbo.md) | 2026-06-03 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.7 Plus (alibaba/qwen3.7-plus)](models/alibaba/qwen3.7-plus.md) | 2026-06-02 | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ✅ | ✅ | ❌ | ✅ | ❌ |
| [MAI-Code-1-Flash (microsoft/mai-code-1-flash)](models/microsoft/mai-code-1-flash.md) | 2026-06-02 | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ➖ | ➖ | ✅ | ❌ | ❌ | ❌ |
| [MAI-Image-2.5 (microsoft/mai-image-2.5)](models/microsoft/mai-image-2.5.md) | 2026-06-02 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MAI-Transcribe-1.5 (microsoft/mai-transcribe-1.5)](models/microsoft/mai-transcribe-1.5.md) | 2026-06-02 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MAI-Voice-2 (microsoft/mai-voice-2)](models/microsoft/mai-voice-2.md) | 2026-06-02 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Nex-N2-Pro (nex-agi/nex-n2-pro)](models/nex-agi/nex-n2-pro.md) | 2026-06-02 | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⚠️ | ❌ |
| [Nemotron 3.5 Content Safety (nvidia/nemotron-3.5-content-safety)](models/nvidia/nemotron-3.5-content-safety.md) | 2026-06-02 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Aleph 2.0 (runwayml/aleph-2)](models/runwayml/aleph-2.md) | 2026-06-02 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiniMax-M3 (minimax/MiniMax-M3)](models/minimax/MiniMax-M3.md) | 2026-06-01 | ⏳ | ❌ | ✅ | ✅ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ⚠️ | ❌ |
| [Qwen-Audio-3.0-ASR Flash (alibaba/qwen-audio-3.0-asr-flash)](models/alibaba/qwen-audio-3.0-asr-flash.md) | 2026-06 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Aleph 2.0 (runway/aleph-2)](models/runway/aleph-2.md) | 2026-06 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok Imagine Video 1.5 (xai/grok-imagine-video-1.5)](models/xai/grok-imagine-video-1.5.md) | 2026-05-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Step 3.7 Flash (stepfun/step-3.7-flash)](models/stepfun/step-3.7-flash.md) | 2026-05-29 | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ✅ | ❌ |
| [Claude Opus 4.8 (anthropic/claude-opus-4-8)](models/anthropic/claude-opus-4-8.md) | 2026-05-28 | ⏳ | ❌ | ✅ | ✅ | ⏳ | ⏳ | ✅ | ✅ | ❌ | ⚠️ | ❌ |
| [Qwen3.7 Max (alibaba/qwen3.7-max)](models/alibaba/qwen3.7-max.md) | 2026-05-21 | ⏳ | ⏳ | ✅ | ❌ | ⏳ | ➖ | ➖ | ✅ | ❌ | ✅ | ❌ |
| [Hy-MT2-1.8B (tencent/hy-mt2-1.8b)](models/tencent/hy-mt2-1.8b.md) | 2026-05-21 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Hy-MT2-30B-A3B (tencent/hy-mt2-30b-a3b)](models/tencent/hy-mt2-30b-a3b.md) | 2026-05-21 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Hy-MT2-7B (tencent/hy-mt2-7b)](models/tencent/hy-mt2-7b.md) | 2026-05-21 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Command A Plus (cohere/command-a-plus-05-2026)](models/cohere/command-a-plus-05-2026.md) | 2026-05-20 | ⏳ | ⏳ | ✅ | ✅ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ⚠️ | ❌ |
| [Gemini 3.5 Flash (google/gemini-3.5-flash)](models/google/gemini-3.5-flash.md) | 2026-05-19 | ✅ | ⏳ | ❌ | ❌ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⏳ | ❌ |
| [MiniCPM5-1B (openbmb/minicpm5-1b)](models/openbmb/minicpm5-1b.md) | 2026-05-19 | ⏳ | ⏳ | ❌ | ❌ | ⏳ | ➖ | ➖ | ❌ | ❌ | ❌ | ❌ |
| [Grok Build 0.1 (xai/grok-build-0.1)](models/xai/grok-build-0.1.md) | 2026-05-19 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⚠️ | ⏳ |
| [Aion-3.0-Mini (aion-labs/aion-3.0-mini)](models/aion-labs/aion-3.0-mini.md) | 2026-05-14 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ❌ | ❌ | ❌ | ❌ |
| [Recraft V4.1 (recraft/recraft-v4.1)](models/recraft/recraft-v4.1.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Pro (recraft/recraft-v4.1-pro)](models/recraft/recraft-v4.1-pro.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Pro Vector (recraft/recraft-v4.1-pro-vector)](models/recraft/recraft-v4.1-pro-vector.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Utility (recraft/recraft-v4.1-utility)](models/recraft/recraft-v4.1-utility.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Utility Pro (recraft/recraft-v4.1-utility-pro)](models/recraft/recraft-v4.1-utility-pro.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Utility Pro Vector (recraft/recraft-v4.1-utility-pro-vector)](models/recraft/recraft-v4.1-utility-pro-vector.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Utility Vector (recraft/recraft-v4.1-utility-vector)](models/recraft/recraft-v4.1-utility-vector.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Recraft V4.1 Vector (recraft/recraft-v4.1-vector)](models/recraft/recraft-v4.1-vector.md) | 2026-05-14 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Krea 2 Large (krea/krea-2-large)](models/krea/krea-2-large.md) | 2026-05-12 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Krea 2 Medium (krea/krea-2-medium)](models/krea/krea-2-medium.md) | 2026-05-12 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Perceptron Mk1 (perceptron/perceptron-mk1)](models/perceptron/perceptron-mk1.md) | 2026-05-12 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ➖ | ➖ |
| [Gemini 3.1 Flash Lite (google/gemini-3.1-flash-lite)](models/google/gemini-3.1-flash-lite.md) | 2026-05-07 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ❌ |
| [GPT-Realtime-2 (openai/gpt-realtime-2)](models/openai/gpt-realtime-2.md) | 2026-05-07 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ❌ |
| [GPT-Realtime-Translate (openai/gpt-realtime-translate)](models/openai/gpt-realtime-translate.md) | 2026-05-07 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT Realtime Whisper (openai/gpt-realtime-whisper)](models/openai/gpt-realtime-whisper.md) | 2026-05-07 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [CoBuddy (baidu/cobuddy)](models/baidu/cobuddy.md) | 2026-05-06 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ❌ | ❌ | ❌ | ❌ |
| [Aion-3.0 (aion-labs/aion-3.0)](models/aion-labs/aion-3.0.md) | 2026-05-05 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ❌ | ❌ | ❌ | ❌ |
| [Realtime TTS-2 (inworld/inworld-tts-2)](models/inworld/inworld-tts-2.md) | 2026-05-05 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-5.5 Instant (openai/gpt-5.5-instant)](models/openai/gpt-5.5-instant.md) | 2026-05-05 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ❌ | ❌ |
| [Mistral Medium (latest) (mistral/mistral-medium-latest)](models/mistral/mistral-medium-latest.md) | 2026-04-29 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ❌ |
| [Mistral Medium 3.5 (mistral/mistral-medium-2604)](models/mistral/mistral-medium-2604.md) | 2026-04-28 | ⏳ | ❌ | ✅ | ✅ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ⚠️ | ❌ |
| [Mistral Medium 3.5 (mistral/mistral-medium-3-5)](models/mistral/mistral-medium-3-5.md) | 2026-04-28 | ⏳ | ❌ | ✅ | ✅ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ⚠️ | ❌ |
| [Nemotron 3 Nano Omni 30B A3B Reasoning (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning)](models/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning.md) | 2026-04-28 | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| [Laguna M.1 (poolside/laguna-m.1)](models/poolside/laguna-m.1.md) | 2026-04-28 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Laguna XS.2 (poolside/laguna-xs.2)](models/poolside/laguna-xs.2.md) | 2026-04-28 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Qwen3.6 Flash (alibaba/qwen3.6-flash)](models/alibaba/qwen3.6-flash.md) | 2026-04-27 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [DeepSeek V4 Flash (deepseek/deepseek-v4-flash)](models/deepseek/deepseek-v4-flash.md) | 2026-04-24 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ⏳ | ⚠️ | ⏳ |
| [DeepSeek V4 Pro (deepseek/deepseek-v4-pro)](models/deepseek/deepseek-v4-pro.md) | 2026-04-24 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ❌ | ⚠️ | ⏳ |
| [DeepSeek V4 Flash 0423 (deepseek/deepseek-v4-flash-0423)](models/deepseek/deepseek-v4-flash-0423.md) | 2026-04-23 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ |
| [DeepSeek V4 Pro 0423 (deepseek/deepseek-v4-pro-0423)](models/deepseek/deepseek-v4-pro-0423.md) | 2026-04-23 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ |
| [GPT-5.5 (openai/gpt-5.5)](models/openai/gpt-5.5.md) | 2026-04-23 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ✅ | ❌ | ⏳ | ⏳ |
| [GPT-5.5 Pro (openai/gpt-5.5-pro)](models/openai/gpt-5.5-pro.md) | 2026-04-23 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⏳ | ⏳ |
| [MiMo-V2.5-ASR (xiaomi/mimo-v2.5-asr)](models/xiaomi/mimo-v2.5-asr.md) | 2026-04-23 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [HappyHorse-1.0 (alibaba/happyhorse-1.0)](models/alibaba/happyhorse-1.0.md) | 2026-04-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.6 27B (alibaba/qwen3.6-27b)](models/alibaba/qwen3.6-27b.md) | 2026-04-22 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ❌ | ✅ | ⏳ |
| [Gemini Embedding 2 (google/gemini-embedding-2)](models/google/gemini-embedding-2.md) | 2026-04-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiMo-V2.5 (xiaomi/mimo-v2.5)](models/xiaomi/mimo-v2.5.md) | 2026-04-22 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ |
| [MiMo-V2.5-Pro (xiaomi/mimo-v2.5-pro)](models/xiaomi/mimo-v2.5-pro.md) | 2026-04-22 | ⏳ | ⏳ | ⚠️ | ⏳ | ⏳ | ⏳ | ➖ | ⏳ | ❌ | ⚠️ | ⏳ |
| [MiMo-V2.5-TTS (xiaomi/mimo-v2.5-tts)](models/xiaomi/mimo-v2.5-tts.md) | 2026-04-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiMo-V2.5-TTS-VoiceClone (xiaomi/mimo-v2.5-tts-voiceclone)](models/xiaomi/mimo-v2.5-tts-voiceclone.md) | 2026-04-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [MiMo-V2.5-TTS-VoiceDesign (xiaomi/mimo-v2.5-tts-voicedesign)](models/xiaomi/mimo-v2.5-tts-voicedesign.md) | 2026-04-22 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Deep Research Max Preview (google/deep-research-max-preview-04-2026)](models/google/deep-research-max-preview-04-2026.md) | 2026-04-21 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Gemini Deep Research Preview (google/deep-research-preview-04-2026)](models/google/deep-research-preview-04-2026.md) | 2026-04-21 | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [GPT-5.4 Image 2 (openai/gpt-5.4-image-2)](models/openai/gpt-5.4-image-2.md) | 2026-04-21 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [GPT-Image-2 (openai/gpt-image-2)](models/openai/gpt-image-2.md) | 2026-04-21 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.6 Max Preview (alibaba/qwen3.6-max-preview)](models/alibaba/qwen3.6-max-preview.md) | 2026-04-20 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ⏳ | ⏳ |
| [Kimi K2.6 (moonshotai/kimi-k2.6)](models/moonshotai/kimi-k2.6.md) | 2026-04-20 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ❌ | ⏳ | ⏳ |
| [Hy3 preview (tencent/hy3-preview)](models/tencent/hy3-preview.md) | 2026-04-20 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ⏳ | ⏳ |
| [Qwen3.6 35B-A3B (alibaba/qwen3.6-35b-a3b)](models/alibaba/qwen3.6-35b-a3b.md) | 2026-04-17 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ✅ | ⏳ |
| [Grok 4.3 (xai/grok-4.3)](models/xai/grok-4.3.md) | 2026-04-17 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ |
| [Claude Opus 4.7 (anthropic/claude-opus-4-7)](models/anthropic/claude-opus-4-7.md) | 2026-04-16 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ❌ | ⏳ | ⏳ |
| [Schematron V2 Small (inference-net/schematron-v2-small)](models/inference-net/schematron-v2-small.md) | 2026-04-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Schematron V2 Turbo (inference-net/schematron-v2-turbo)](models/inference-net/schematron-v2-turbo.md) | 2026-04-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini 3.1 Flash TTS Preview (google/gemini-3.1-flash-tts-preview)](models/google/gemini-3.1-flash-tts-preview.md) | 2026-04-15 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini Robotics-ER 1.6 Preview (google/gemini-robotics-er-1.6-preview)](models/google/gemini-robotics-er-1.6-preview.md) | 2026-04-14 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ |
| [GLM-5.1 (zhipuai/glm-5.1)](models/zhipuai/glm-5.1.md) | 2026-04-07 | ✅ | ⏳ | ✅ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ✅ | ⏳ |
| [Wan2.7 (alibaba/wan2.7)](models/alibaba/wan2.7.md) | 2026-04-03 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok Imagine Image Quality (xai/grok-imagine-image-quality)](models/xai/grok-imagine-image-quality.md) | 2026-04-03 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Qwen3.6 Plus (alibaba/qwen3.6-plus)](models/alibaba/qwen3.6-plus.md) | 2026-04-02 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⚠️ | ⏳ |
| [Step 3.5 Flash 2603 (stepfun/step-3.5-flash-2603)](models/stepfun/step-3.5-flash-2603.md) | 2026-04-02 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ❌ | ⏳ |
| [Trinity Large Thinking (arcee-ai/trinity-large-thinking)](models/arcee-ai/trinity-large-thinking.md) | 2026-04-01 | ⏳ | ⏳ | ✅ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ✅ | ⏳ |
| [GLM-5V-Turbo (zhipuai/glm-5v-turbo)](models/zhipuai/glm-5v-turbo.md) | 2026-04-01 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ❌ | ⏳ | ⏳ |
| [Gemma 4 26B A4B IT (google/gemma-4-26b-a4b-it)](models/google/gemma-4-26b-a4b-it.md) | 2026-03-31 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⏳ | ⏳ |
| [Gemma 4 31B IT (google/gemma-4-31b-it)](models/google/gemma-4-31b-it.md) | 2026-03-31 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⏳ | ⏳ |
| [Gemma 4 E2B IT (google/gemma-4-E2B-it)](models/google/gemma-4-E2B-it.md) | 2026-03-31 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ⏳ | ⏳ |
| [Gemma 4 E4B IT (google/gemma-4-E4B-it)](models/google/gemma-4-E4B-it.md) | 2026-03-31 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ❌ | ❌ | ⏳ | ⏳ |
| [Veo 3.1 Lite Preview (google/veo-3.1-lite-generate-preview)](models/google/veo-3.1-lite-generate-preview.md) | 2026-03-31 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Mercury Edit 2 (inception/mercury-edit-2)](models/inception/mercury-edit-2.md) | 2026-03-30 | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [OmniVoice (k2-fsa/omnivoice)](models/k2-fsa/omnivoice.md) | 2026-03-30 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Cohere Transcribe (cohere/cohere-transcribe-03-2026)](models/cohere/cohere-transcribe-03-2026.md) | 2026-03-26 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Gemini 3.1 Flash Live Preview (google/gemini-3.1-flash-live-preview)](models/google/gemini-3.1-flash-live-preview.md) | 2026-03-26 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Lyria 3 Clip Preview (google/lyria-3-clip-preview)](models/google/lyria-3-clip-preview.md) | 2026-03-25 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Lyria 3 Pro Preview (google/lyria-3-pro-preview)](models/google/lyria-3-pro-preview.md) | 2026-03-25 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Voxtral Mini TTS (mistral/voxtral-mini-tts-2603)](models/mistral/voxtral-mini-tts-2603.md) | 2026-03-23 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Nemotron Cascade 2 30B A3B (nvidia/nemotron-cascade-2-30b-a3b)](models/nvidia/nemotron-cascade-2-30b-a3b.md) | 2026-03-19 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⏳ | ⏳ |
| [MiniMax-M2.7 (minimax/MiniMax-M2.7)](models/minimax/MiniMax-M2.7.md) | 2026-03-18 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⚠️ | ⏳ |
| [MiniMax-M2.7-highspeed (minimax/MiniMax-M2.7-highspeed)](models/minimax/MiniMax-M2.7-highspeed.md) | 2026-03-18 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ⏳ | ❌ | ⏳ | ⏳ |
| [MiMo-V2-Omni (xiaomi/mimo-v2-omni)](models/xiaomi/mimo-v2-omni.md) | 2026-03-18 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ⏳ | ⏳ |
| [MiMo-V2-Pro (xiaomi/mimo-v2-pro)](models/xiaomi/mimo-v2-pro.md) | 2026-03-18 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⏳ | ⏳ |
| [MiMo-V2-TTS (xiaomi/mimo-v2-tts)](models/xiaomi/mimo-v2-tts.md) | 2026-03-18 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GPT-5.4 mini (openai/gpt-5.4-mini)](models/openai/gpt-5.4-mini.md) | 2026-03-17 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ✅ | ⏳ |
| [GPT-5.4 nano (openai/gpt-5.4-nano)](models/openai/gpt-5.4-nano.md) | 2026-03-17 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ❌ | ❌ | ⏳ |
| [Mistral Small 4 (mistral/mistral-small-2603)](models/mistral/mistral-small-2603.md) | 2026-03-16 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ✅ | ✅ | ⚠️ | ⏳ |
| [Mistral Small (latest) (mistral/mistral-small-latest)](models/mistral/mistral-small-latest.md) | 2026-03-16 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ❌ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Nemotron 3 Content Safety (nvidia/nemotron-3-content-safety)](models/nvidia/nemotron-3-content-safety.md) | 2026-03-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Nemotron VoiceChat (nvidia/nemotron-voicechat)](models/nvidia/nemotron-voicechat.md) | 2026-03-16 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok TTS (xai/grok-tts)](models/xai/grok-tts.md) | 2026-03-16 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [GLM-5-Turbo (zhipuai/glm-5-turbo)](models/zhipuai/glm-5-turbo.md) | 2026-03-16 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ❌ | ❌ | ❌ | ⏳ |
| [Nemotron 3 Super 120B A12B (nvidia/nemotron-3-super-120b-a12b)](models/nvidia/nemotron-3-super-120b-a12b.md) | 2026-03-11 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ➖ | ➖ | ✅ | ❌ | ⚠️ | ⏳ |
| [Reka Edge (rekaai/reka-edge)](models/rekaai/reka-edge.md) | 2026-03-11 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Gemini Embedding 2 Preview (google/gemini-embedding-2-preview)](models/google/gemini-embedding-2-preview.md) | 2026-03-10 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ |
| [Grok 4.20 (Non-Reasoning) (xai/grok-4.20-0309-non-reasoning)](models/xai/grok-4.20-0309-non-reasoning.md) | 2026-03-09 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |
| [Grok 4.20 (Reasoning) (xai/grok-4.20-0309-reasoning)](models/xai/grok-4.20-0309-reasoning.md) | 2026-03-09 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ⏳ | ⏳ | ⏳ |
| [GPT-5.4 (openai/gpt-5.4)](models/openai/gpt-5.4.md) | 2026-03-05 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ✅ | ⏳ | ✅ | ⏳ |
| [GPT-5.4 Pro (openai/gpt-5.4-pro)](models/openai/gpt-5.4-pro.md) | 2026-03-05 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ⏳ | ⏳ | ⏳ |
| [Gemini 3.1 Flash Lite Preview (google/gemini-3.1-flash-lite-preview)](models/google/gemini-3.1-flash-lite-preview.md) | 2026-03-03 | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ✅ | ⏳ | ⏳ |
| GPT-5.3 Chat (latest) (openai/gpt-5.3-chat-latest) | 2026-03-03 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 0.8B (alibaba/qwen3.5-0.8b) | 2026-03-02 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 2B (alibaba/qwen3.5-2b) | 2026-03-02 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 4B (alibaba/qwen3.5-4b) | 2026-03-02 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Moderation 26.03 (mistral/mistral-moderation-2603) | 2026-03-01 | — | — | — | — | — | — | — | — | — | — | — |
| S2 Pro (fish-audio/s2-pro) | 2026-03 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 9B Base (alibaba/qwen3.5-9b-base) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| Nano Banana 2 (google/gemini-3.1-flash-image) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| Nano Banana 2 Preview (google/gemini-3.1-flash-image-preview) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| pplx-embed-context-v1-0.6b (perplexity/pplx-embed-context-v1-0.6b) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| pplx-embed-context-v1-4b (perplexity/pplx-embed-context-v1-4b) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| pplx-embed-v1-0.6b (perplexity/pplx-embed-v1-0.6b) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| pplx-embed-v1-4b (perplexity/pplx-embed-v1-4b) | 2026-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 35B-A3B Base (alibaba/qwen3.5-35b-a3b-base) | 2026-02-24 | — | — | — | — | — | — | — | — | — | — | — |
| Mercury 2 (inception/mercury-2) | 2026-02-24 | — | — | — | — | — | — | — | — | — | — | — |
| LFM2 24B A2B (liquid/lfm2-24b-a2b) | 2026-02-24 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 122B-A10B (alibaba/qwen3.5-122b-a10b) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 27B (alibaba/qwen3.5-27b) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 35B-A3B (alibaba/qwen3.5-35b-a3b) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 9B (alibaba/qwen3.5-9b) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 Flash (alibaba/qwen3.5-flash) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Audio-1.5 (openai/gpt-audio-1.5) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Realtime-1.5 (openai/gpt-realtime-1.5) | 2026-02-23 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 3.1 Pro Preview (google/gemini-3.1-pro-preview) | 2026-02-19 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 3.1 Pro Preview Custom Tools (google/gemini-3.1-pro-preview-customtools) | 2026-02-19 | — | — | — | — | — | — | — | — | — | — | — |
| Trendyol Asure 12B (trendyol/asure-12b) | 2026-02-19 | — | — | — | — | — | — | — | — | — | — | — |
| Sarvam 105B (sarvam/sarvam-105b) | 2026-02-18 | — | — | — | — | — | — | — | — | — | — | — |
| Sarvam 30B (sarvam/sarvam-30b) | 2026-02-18 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 4.6 (anthropic/claude-sonnet-4-6) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Tiny Aya Earth (cohere/tiny-aya-earth) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Tiny Aya Fire (cohere/tiny-aya-fire) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Tiny Aya Global (cohere/tiny-aya-global) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Tiny Aya Water (cohere/tiny-aya-water) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Recraft V4 (recraft/recraft-v4) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Recraft V4 Pro (recraft/recraft-v4-pro) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Recraft V4 Pro Vector (recraft/recraft-v4-pro-vector) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Recraft V4 Vector (recraft/recraft-v4-vector) | 2026-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 Plus (alibaba/qwen3.5-plus) | 2026-02-16 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3.5 397B-A17B (alibaba/qwen3.5-397b-a17b) | 2026-02-15 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 2.0 Code (bytedance-seed/seed-2.0-code) | 2026-02-14 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 2.0 Lite (bytedance-seed/seed-2.0-lite) | 2026-02-14 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 2.0 Mini (bytedance-seed/seed-2.0-mini) | 2026-02-14 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 2.0 Pro (bytedance-seed/seed-2.0-pro) | 2026-02-14 | — | — | — | — | — | — | — | — | — | — | — |
| Seedream 5.0 Lite (bytedance-seed/seedream-5.0-lite) | 2026-02-13 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax-M2.5-highspeed (minimax/MiniMax-M2.5-highspeed) | 2026-02-13 | — | — | — | — | — | — | — | — | — | — | — |
| Seedance 2.0 (bytedance-seed/seedance-2.0) | 2026-02-12 | — | — | — | — | — | — | — | — | — | — | — |
| Seedance 2.0 Fast (bytedance-seed/seedance-2.0-fast) | 2026-02-12 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax-M2.5 (minimax/MiniMax-M2.5) | 2026-02-12 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-5 (zhipuai/glm-5) | 2026-02-12 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven v3 Conversational (elevenlabs/eleven_v3_conversational) | 2026-02-09 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4.6 (anthropic/claude-opus-4-6) | 2026-02-05 | — | — | — | — | — | — | — | — | — | — | — |
| Kling VIDEO 3.0 Pro (kuaishou/kling-v3.0-pro) | 2026-02-05 | — | — | — | — | — | — | — | — | — | — | — |
| Kling VIDEO 3.0 Standard (kuaishou/kling-v3.0-std) | 2026-02-05 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.3 Codex (openai/gpt-5.3-codex) | 2026-02-05 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.3 Codex Spark (openai/gpt-5.3-codex-spark) | 2026-02-05 | — | — | — | — | — | — | — | — | — | — | — |
| Voxtral Mini Transcribe 2 (mistral/voxtral-mini-2602) | 2026-02-04 | — | — | — | — | — | — | — | — | — | — | — |
| Voxtral Mini Transcribe Realtime (mistral/voxtral-mini-transcribe-realtime-2602) | 2026-02-04 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Coder Next (alibaba/qwen3-coder-next) | 2026-02-03 | — | — | — | — | — | — | — | — | — | — | — |
| Universal-3 Pro (assemblyai/universal-3-pro) | 2026-02-03 | — | — | — | — | — | — | — | — | — | — | — |
| Riverflow 2.0 Fast (sourceful/riverflow-v2-fast) | 2026-02-02 | — | — | — | — | — | — | — | — | — | — | — |
| Riverflow 2.0 Pro (sourceful/riverflow-v2-pro) | 2026-02-02 | — | — | — | — | — | — | — | — | — | — | — |
| Step 3.5 Flash (stepfun/step-3.5-flash) | 2026-01-29 | — | — | — | — | — | — | — | — | — | — | — |
| Grok Imagine Image (xai/grok-imagine-image) | 2026-01-28 | — | — | — | — | — | — | — | — | — | — | — |
| Grok Imagine Video (xai/grok-imagine-video) | 2026-01-28 | — | — | — | — | — | — | — | — | — | — | — |
| Trinity Large Preview (arcee-ai/trinity-large-preview) | 2026-01-27 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek OCR 2 (deepseek/deepseek-ocr-2) | 2026-01-27 | — | — | — | — | — | — | — | — | — | — | — |
| Kimi K2.5 (moonshotai/kimi-k2.5) | 2026-01-27 | — | — | — | — | — | — | — | — | — | — | — |
| Solar Pro 3 (upstage/solar-pro3) | 2026-01-26 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax-M2 Her (minimax/MiniMax-M2-Her) | 2026-01-23 | — | — | — | — | — | — | — | — | — | — | — |
| Speech 2.8 HD (minimax/speech-2.8-hd) | 2026-01-23 | — | — | — | — | — | — | — | — | — | — | — |
| Speech 2.8 Turbo (minimax/speech-2.8-turbo) | 2026-01-23 | — | — | — | — | — | — | — | — | — | — | — |
| Nemotron Content Safety Reasoning 4B (nvidia/nemotron-content-safety-reasoning-4b) | 2026-01-22 | — | — | — | — | — | — | — | — | — | — | — |
| TTS-1.5 Max (inworld/inworld-tts-1.5-max) | 2026-01-21 | — | — | — | — | — | — | — | — | — | — | — |
| TTS-1.5 Mini (inworld/inworld-tts-1.5-mini) | 2026-01-21 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.7-Flash (zhipuai/glm-4.7-flash) | 2026-01-19 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.7-FlashX (zhipuai/glm-4.7-flashx) | 2026-01-19 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.2 [klein] 4B (black-forest-labs/flux-2-klein-4b) | 2026-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.2 [klein] 9B (black-forest-labs/flux-2-klein-9b) | 2026-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| voyage-4 (voyageai/voyage-4) | 2026-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| voyage-4-large (voyageai/voyage-4-large) | 2026-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| voyage-4-lite (voyageai/voyage-4-lite) | 2026-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| voyage-multimodal-3.5 (voyageai/voyage-multimodal-3.5) | 2026-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-Image (zhipuai/glm-image) | 2026-01-14 | — | — | — | — | — | — | — | — | — | — | — |
| Scribe v2 (elevenlabs/scribe_v2) | 2026-01-12 | — | — | — | — | — | — | — | — | — | — | — |
| Jamba Mini (ai21/jamba-mini) | 2026-01-08 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 ASR 0.6B (alibaba/qwen3-asr-0.6b) | 2026-01 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 ASR 1.7B (alibaba/qwen3-asr-1.7b) | 2026-01 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 1.8 (bytedance-seed/seed-1-8) | 2025-12-28 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax-M2.1 (minimax/MiniMax-M2.1) | 2025-12-23 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.7 (zhipuai/glm-4.7) | 2025-12-22 | — | — | — | — | — | — | — | — | — | — | — |
| Aion-2.0 (aion-labs/aion-2.0) | 2025-12-21 | — | — | — | — | — | — | — | — | — | — | — |
| Orpheus V1 English (canopylabs/orpheus-v1-english) | 2025-12-19 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral OCR 3 (mistral/mistral-ocr-2512) | 2025-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| Llama Nemotron Embed VL 1B v2 (nvidia/llama-nemotron-embed-vl-1b-v2) | 2025-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| Llama Nemotron Rerank VL 1B v2 (nvidia/llama-nemotron-rerank-vl-1b-v2) | 2025-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| X-Ai/Grok-4-Fast-Non-Reasoning (xai/grok-4-fast-non-reasoning) | 2025-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| X-Ai/Grok-4-Fast-Reasoning (xai/grok-4-fast-reasoning) | 2025-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 3 Flash Preview (google/gemini-3-flash-preview) | 2025-12-17 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.2 [max] (black-forest-labs/flux-2-max) | 2025-12-16 | — | — | — | — | — | — | — | — | — | — | — |
| Seedance 1.5 Pro (bytedance-seed/seedance-1.5-pro) | 2025-12-16 | — | — | — | — | — | — | — | — | — | — | — |
| Orpheus Arabic Saudi (canopylabs/orpheus-arabic-saudi) | 2025-12-16 | — | — | — | — | — | — | — | — | — | — | — |
| MiMo-V2-Flash (xiaomi/mimo-v2-flash) | 2025-12-16 | — | — | — | — | — | — | — | — | — | — | — |
| Nemotron 3 Nano 30B A3B (nvidia/nemotron-3-nano-30b-a3b) | 2025-12-15 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash Native Audio Preview 12-2025 (google/gemini-2.5-flash-native-audio-preview-12-2025) | 2025-12-12 | — | — | — | — | — | — | — | — | — | — | — |
| Rerank 4 Fast (cohere/rerank-v4.0-fast) | 2025-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| Rerank 4 Pro (cohere/rerank-v4.0-pro) | 2025-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.2 (openai/gpt-5.2) | 2025-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.2 Chat (openai/gpt-5.2-chat-latest) | 2025-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.2 Codex (openai/gpt-5.2-codex) | 2025-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.2 Pro (openai/gpt-5.2-pro) | 2025-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| AutoGLM Phone 9B Multilingual (zhipuai/autoglm-phone-9b-multilingual) | 2025-12-10 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-ASR-2512 (zhipuai/glm-asr-2512) | 2025-12-10 | — | — | — | — | — | — | — | — | — | — | — |
| Devstral 2 (mistral/devstral-2512) | 2025-12-09 | — | — | — | — | — | — | — | — | — | — | — |
| Devstral Small 2 (mistral/devstral-small-2) | 2025-12-09 | — | — | — | — | — | — | — | — | — | — | — |
| Relace Search (relace/relace-search) | 2025-12-08 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.6V (zhipuai/glm-4.6v) | 2025-12-08 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.6V-Flash (zhipuai/glm-4.6v-flash) | 2025-12-08 | — | — | — | — | — | — | — | — | — | — | — |
| Rnj-1 Instruct (essentialai/rnj-1-instruct) | 2025-12-04 | — | — | — | — | — | — | — | — | — | — | — |
| Wan2.6 (alibaba/wan2.6) | 2025-12-03 | — | — | — | — | — | — | — | — | — | — | — |
| Seedream 4.5 (bytedance-seed/seedream-4.5) | 2025-12-03 | — | — | — | — | — | — | — | — | — | — | — |
| Nova 2 Lite (amazon/nova-2-lite) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Nova 2 Lite (amazon/nova-2-lite-v1) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Devstral 2 (latest) (mistral/devstral-medium-latest) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 14B (mistral/ministral-14b) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3 14B 2512 (mistral/ministral-14b-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3 14B (mistral/ministral-3-14b-instruct-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3 3B (mistral/ministral-3-3b-instruct-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3 8B (mistral/ministral-3-8b-instruct-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3 3B 2512 (mistral/ministral-3b-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3 8B 2512 (mistral/ministral-8b-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Large 3 (mistral/mistral-large-2512) | 2025-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Trinity Mini (arcee-ai/trinity-mini) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| Trinity Nano Preview (arcee-ai/trinity-nano-preview) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek Chat (deepseek/deepseek-chat) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek Reasoner (deepseek/deepseek-reasoner) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek V3.2 (deepseek/deepseek-v3.2) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| Kling VIDEO O1 (kuaishou/kling-video-o1) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| Gen-4.5 (runway/gen-4.5) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| Gen-4.5 (runwayml/gen-4.5) | 2025-12-01 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.2 [dev] (black-forest-labs/flux-2-dev) | 2025-11-25 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.2 [flex] (black-forest-labs/flux-2-flex) | 2025-11-25 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.2 [pro] (black-forest-labs/flux-2-pro) | 2025-11-25 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Image-1.5 (openai/gpt-image-1.5) | 2025-11-25 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4.5 (latest) (anthropic/claude-opus-4-5) | 2025-11-24 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4.5 (anthropic/claude-opus-4-5-20251101) | 2025-11-24 | — | — | — | — | — | — | — | — | — | — | — |
| Nano Banana Pro (google/gemini-3-pro-image) | 2025-11-20 | — | — | — | — | — | — | — | — | — | — | — |
| Nano Banana Pro Preview (google/gemini-3-pro-image-preview) | 2025-11-20 | — | — | — | — | — | — | — | — | — | — | — |
| Grok 4.1 Fast (xai/grok-4.1-fast) | 2025-11-19 | — | — | — | — | — | — | — | — | — | — | — |
| Grok 4.1 Fast (Reasoning) (xai/grok-4.1-fast-reasoning) | 2025-11-19 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 3 Pro Preview (google/gemini-3-pro-preview) | 2025-11-18 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.1 (openai/gpt-5.1) | 2025-11-13 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.1 Chat (openai/gpt-5.1-chat-latest) | 2025-11-13 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.1 Codex (openai/gpt-5.1-codex) | 2025-11-13 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.1 Codex Max (openai/gpt-5.1-codex-max) | 2025-11-13 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5.1 Codex mini (openai/gpt-5.1-codex-mini) | 2025-11-13 | — | — | — | — | — | — | — | — | — | — | — |
| Kimi K2 Thinking (moonshotai/kimi-k2-thinking) | 2025-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| Kimi K2 Thinking Turbo (moonshotai/kimi-k2-thinking-turbo) | 2025-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| GPT OSS Safeguard 120B (openai/gpt-oss-safeguard-120b) | 2025-10-29 | — | — | — | — | — | — | — | — | — | — | — |
| GPT OSS Safeguard 20B (openai/gpt-oss-safeguard-20b) | 2025-10-29 | — | — | — | — | — | — | — | — | — | — | — |
| Hailuo 2.3 (minimax/MiniMax-Hailuo-2.3) | 2025-10-28 | — | — | — | — | — | — | — | — | — | — | — |
| Hailuo 2.3 Fast (minimax/MiniMax-Hailuo-2.3-Fast) | 2025-10-28 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.1 Nemotron Safety Guard 8B v3 (nvidia/llama-3.1-nemotron-safety-guard-8b-v3) | 2025-10-28 | — | — | — | — | — | — | — | — | — | — | — |
| Nemotron Nano 12B v2 VL (nvidia/nemotron-nano-12b-v2-vl) | 2025-10-28 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax-M2 (minimax/MiniMax-M2) | 2025-10-27 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o Transcribe Diarize (openai/gpt-4o-transcribe-diarize) | 2025-10-17 | — | — | — | — | — | — | — | — | — | — | — |
| Llama Nemotron Embed 1B v2 (nvidia/llama-nemotron-embed-1b-v2) | 2025-10-16 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Image Mini (openai/gpt-5-image-mini) | 2025-10-16 | — | — | — | — | — | — | — | — | — | — | — |
| PaddleOCR VL (paddlepaddle/paddleocr-vl) | 2025-10-16 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 VL Flash (Alibaba Cloud) (alibaba/qwen3-vl-flash) | 2025-10-15 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Haiku 4.5 (latest) (anthropic/claude-haiku-4-5) | 2025-10-15 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Haiku 4.5 (anthropic/claude-haiku-4-5-20251001) | 2025-10-15 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 1.6 (bytedance-seed/seed-1-6) | 2025-10-15 | — | — | — | — | — | — | — | — | — | — | — |
| Veo 3.1 Fast Preview (google/veo-3.1-fast-generate-preview) | 2025-10-15 | — | — | — | — | — | — | — | — | — | — | — |
| Veo 3.1 Preview (google/veo-3.1-generate-preview) | 2025-10-15 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Image (openai/gpt-5-image) | 2025-10-14 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Search API (openai/gpt-5-search-api) | 2025-10-14 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Computer Use Preview (google/gemini-2.5-computer-use-preview-10-2025) | 2025-10-07 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Pro (openai/gpt-5-pro) | 2025-10-06 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Audio Mini (openai/gpt-audio-mini) | 2025-10-06 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Image-1 Mini (openai/gpt-image-1-mini) | 2025-10-06 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Realtime Mini (openai/gpt-realtime-mini) | 2025-10-06 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 VL 30B A3B Instruct (alibaba/qwen3-vl-30b-a3b-instruct) | 2025-10-04 | — | — | — | — | — | — | — | — | — | — | — |
| Granite-4.0-H-Micro (ibm/granite-4-h-micro) | 2025-10-02 | — | — | — | — | — | — | — | — | — | — | — |
| Granite-4.0-H-Small (ibm/granite-4-h-small) | 2025-10-02 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash TTS (google/gemini-2.5-flash-tts) | 2025-09-30 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Pro TTS (google/gemini-2.5-pro-tts) | 2025-09-30 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.6 (zhipuai/glm-4.6) | 2025-09-30 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 4.5 (latest) (anthropic/claude-sonnet-4-5) | 2025-09-29 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 4.5 (anthropic/claude-sonnet-4-5-20250929) | 2025-09-29 | — | — | — | — | — | — | — | — | — | — | — |
| Cydonia 24B V4.1 (thedrummer/cydonia-24b-v4.1) | 2025-09-27 | — | — | — | — | — | — | — | — | — | — | — |
| Relace Apply 3 (relace/relace-apply-3) | 2025-09-26 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash-Lite Preview 09-2025 (google/gemini-2.5-flash-lite-preview-09-2025) | 2025-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma-SEA-LION-v4-27B-IT (aisingapore/gemma-sea-lion-v4-27b-it) | 2025-09-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Max (alibaba/qwen3-max) | 2025-09-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 VL 235B A22B Instruct (alibaba/qwen3-vl-235b-a22b-instruct) | 2025-09-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 VL 235B A22B Thinking (alibaba/qwen3-vl-235b-a22b-thinking) | 2025-09-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3-VL Plus (alibaba/qwen3-vl-plus) | 2025-09-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Omni 30B A3B Thinking (alibaba/qwen3-omni-30b-a3b-thinking) | 2025-09-22 | — | — | — | — | — | — | — | — | — | — | — |
| Magistral Small 1.2 (mistral/magistral-small-2509) | 2025-09-18 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5-Codex (openai/gpt-5-codex) | 2025-09-15 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Max Preview (alibaba/qwen3-max-preview) | 2025-09-05 | — | — | — | — | — | — | — | — | — | — | — |
| Kimi K2 Instruct 0905 (moonshotai/kimi-k2-0905) | 2025-09-05 | — | — | — | — | — | — | — | — | — | — | — |
| Apertus 70B (swiss-ai/apertus-70b) | 2025-09-02 | — | — | — | — | — | — | — | — | — | — | — |
| Apertus 8B (swiss-ai/apertus-8b) | 2025-09-02 | — | — | — | — | — | — | — | — | — | — | — |
| x-AI/Grok-Code-Fast 1 (xai/grok-code-fast-1) | 2025-09-02 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3-Next 80B-A3B Instruct (alibaba/qwen3-next-80b-a3b-instruct) | 2025-09 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3-Next 80B-A3B (Thinking) (alibaba/qwen3-next-80b-a3b-thinking) | 2025-09 | — | — | — | — | — | — | — | — | — | — | — |
| Transcribe 1 (fish-audio/transcribe-1) | 2025-09 | — | — | — | — | — | — | — | — | — | — | — |
| Chirp 3 (google/chirp-3) | 2025-08-29 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 1.6 Flash (bytedance-seed/seed-1-6-flash) | 2025-08-28 | — | — | — | — | — | — | — | — | — | — | — |
| Command A Translate (cohere/command-a-translate-08-2025) | 2025-08-28 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Audio (openai/gpt-audio) | 2025-08-28 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Realtime (openai/gpt-realtime) | 2025-08-28 | — | — | — | — | — | — | — | — | — | — | — |
| Nano Banana (google/gemini-2.5-flash-image) | 2025-08-26 | — | — | — | — | — | — | — | — | — | — | — |
| Hermes 4 405B (nousresearch/hermes-4-405b) | 2025-08-26 | — | — | — | — | — | — | — | — | — | — | — |
| Command A Reasoning (cohere/command-a-reasoning-08-2025) | 2025-08-21 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek V3.1 (deepseek/deepseek-chat-v3.1) | 2025-08-21 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek-V3.1 (deepseek/deepseek-v3.1) | 2025-08-21 | — | — | — | — | — | — | — | — | — | — | — |
| Seed-OSS-36B-Instruct (bytedance-seed/seed-oss-36b-instruct) | 2025-08-20 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven v3 (elevenlabs/eleven_v3) | 2025-08-20 | — | — | — | — | — | — | — | — | — | — | — |
| Nemotron Nano 9B v2 (nvidia/nemotron-nano-9b-v2) | 2025-08-18 | — | — | — | — | — | — | — | — | — | — | — |
| Seed 1.6 Vision (bytedance-seed/seed-1-6-vision) | 2025-08-15 | — | — | — | — | — | — | — | — | — | — | — |
| Baichuan M2 32B (baichuan/baichuan-m2-32b) | 2025-08-13 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Medium 3.1 (mistral/mistral-medium-3.1) | 2025-08-12 | — | — | — | — | — | — | — | — | — | — | — |
| rerank-2.5 (voyageai/rerank-2.5) | 2025-08-11 | — | — | — | — | — | — | — | — | — | — | — |
| rerank-2.5-lite (voyageai/rerank-2.5-lite) | 2025-08-11 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.5V (zhipuai/glm-4.5v) | 2025-08-11 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 (openai/gpt-5) | 2025-08-07 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Chat (latest) (openai/gpt-5-chat-latest) | 2025-08-07 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Mini (openai/gpt-5-mini) | 2025-08-07 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-5 Nano (openai/gpt-5-nano) | 2025-08-07 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4.1 (latest) (anthropic/claude-opus-4-1) | 2025-08-05 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4.1 (anthropic/claude-opus-4-1-20250805) | 2025-08-05 | — | — | — | — | — | — | — | — | — | — | — |
| Lucid Origin (leonardo/lucid-origin) | 2025-08-05 | — | — | — | — | — | — | — | — | — | — | — |
| GPT OSS 120B (openai/gpt-oss-120b) | 2025-08-05 | — | — | — | — | — | — | — | — | — | — | — |
| GPT OSS 20B (openai/gpt-oss-20b) | 2025-08-05 | — | — | — | — | — | — | — | — | — | — | — |
| Parakeet TDT 0.6B v3 (nvidia/parakeet-tdt-0.6b-v3) | 2025-08 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3-Coder 30B-A3B Instruct (alibaba/qwen3-coder-30b-a3b-instruct) | 2025-07-31 | — | — | — | — | — | — | — | — | — | — | — |
| Command A Vision (cohere/command-a-vision-07-2025) | 2025-07-31 | — | — | — | — | — | — | — | — | — | — | — |
| Codestral 25.08 (mistral/codestral-2508) | 2025-07-30 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen Flash (alibaba/qwen-flash) | 2025-07-28 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 30B-A3B Instruct 2507 (alibaba/qwen3-30b-a3b-instruct-2507) | 2025-07-28 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Coder Flash (alibaba/qwen3-coder-flash) | 2025-07-28 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.5 (zhipuai/glm-4.5) | 2025-07-28 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.5-Air (zhipuai/glm-4.5-air) | 2025-07-28 | — | — | — | — | — | — | — | — | — | — | — |
| GLM-4.5-Flash (zhipuai/glm-4.5-flash) | 2025-07-28 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 235B-A22B Thinking 2507 (alibaba/qwen3-235b-a22b-thinking-2507) | 2025-07-25 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.3 Nemotron Super 49B v1.5 (nvidia/llama-3.3-nemotron-super-49b-v1.5) | 2025-07-25 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen MT Plus (alibaba/qwen-mt-plus) | 2025-07-24 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Coder Plus (alibaba/qwen3-coder-plus) | 2025-07-23 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3-Coder 480B-A35B Instruct (alibaba/qwen3-coder-480b-a35b-instruct) | 2025-07-22 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 235B-A22B Instruct 2507 (alibaba/qwen3-235b-a22b-instruct-2507) | 2025-07-21 | — | — | — | — | — | — | — | — | — | — | — |
| Voxtral Mini 3B 2507 (mistral/voxtral-mini-3b-2507) | 2025-07-15 | — | — | — | — | — | — | — | — | — | — | — |
| Voxtral Small 24B 2507 (mistral/voxtral-small-24b-2507) | 2025-07-15 | — | — | — | — | — | — | — | — | — | — | — |
| Voxtral Small (latest) (mistral/voxtral-small-latest) | 2025-07-15 | — | — | — | — | — | — | — | — | — | — | — |
| CogVideoX-3 (zhipuai/cogvideox-3) | 2025-07-15 | — | — | — | — | — | — | — | — | — | — | — |
| Kimi K2 0711 (moonshotai/kimi-k2) | 2025-07-11 | — | — | — | — | — | — | — | — | — | — | — |
| Kimi K2 Instruct (moonshotai/kimi-k2-instruct) | 2025-07-11 | — | — | — | — | — | — | — | — | — | — | — |
| Devstral Medium (mistral/devstral-medium-2507) | 2025-07-10 | — | — | — | — | — | — | — | — | — | — | — |
| Devstral Small (mistral/devstral-small-2507) | 2025-07-10 | — | — | — | — | — | — | — | — | — | — | — |
| Uncensored (cognitivecomputations/dolphin-mistral-24b-venice-edition) | 2025-07-09 | — | — | — | — | — | — | — | — | — | — | — |
| Morph V3 Fast (morph/morph-v3-fast) | 2025-07-07 | — | — | — | — | — | — | — | — | — | — | — |
| Morph V3 Large (morph/morph-v3-large) | 2025-07-07 | — | — | — | — | — | — | — | — | — | — | — |
| Jamba Large (ai21/jamba-large) | 2025-07-03 | — | — | — | — | — | — | — | — | — | — | — |
| ERNIE 4.5 21B A3B (baidu/ernie-4.5-21b-a3b) | 2025-06-30 | — | — | — | — | — | — | — | — | — | — | — |
| ERNIE 4.5 300B A47B (baidu/ernie-4.5-300b-a47b) | 2025-06-30 | — | — | — | — | — | — | — | — | — | — | — |
| ERNIE 4.5 VL 424B A47B  (baidu/ernie-4.5-vl-424b-a47b) | 2025-06-30 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 3n E2B IT (google/gemma-3n-e2b-it) | 2025-06-26 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 3n E4B IT (google/gemma-3n-e4b-it) | 2025-06-26 | — | — | — | — | — | — | — | — | — | — | — |
| o3-deep-research (openai/o3-deep-research) | 2025-06-26 | — | — | — | — | — | — | — | — | — | — | — |
| o4-mini-deep-research (openai/o4-mini-deep-research) | 2025-06-26 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Small 3.2 (mistral/mistral-small-2506) | 2025-06-20 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Small 3.2 24B (mistral/mistral-small-3.2-24b-instruct) | 2025-06-20 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash (google/gemini-2.5-flash) | 2025-06-17 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash-Lite (google/gemini-2.5-flash-lite) | 2025-06-17 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash-Lite Preview 06-17 (google/gemini-2.5-flash-lite-preview-06-17) | 2025-06-17 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Pro (google/gemini-2.5-pro) | 2025-06-17 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax M1 80K (minimax/minimax-m1-80k) | 2025-06-17 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Nemotron (nvidia/mistral-nemotron) | 2025-06-11 | — | — | — | — | — | — | — | — | — | — | — |
| Magistral Small (mistral/magistral-small-2506) | 2025-06-10 | — | — | — | — | — | — | — | — | — | — | — |
| o3-pro (openai/o3-pro) | 2025-06-10 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Embedding 0.6B (alibaba/qwen3-embedding-0.6b) | 2025-06-05 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Embedding 4B (alibaba/qwen3-embedding-4b) | 2025-06-05 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Embedding 8B (alibaba/qwen3-embedding-8b) | 2025-06-05 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Reranker 0.6B (alibaba/qwen3-reranker-0.6b) | 2025-06-05 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 Reranker 8B (alibaba/qwen3-reranker-8b) | 2025-06-05 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Pro Preview 06-05 (google/gemini-2.5-pro-preview) | 2025-06-05 | — | — | — | — | — | — | — | — | — | — | — |
| S1 (fish-audio/s1) | 2025-06 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.1 Kontext [dev] (black-forest-labs/flux-1-kontext-dev) | 2025-05-29 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.1 Kontext [max] (black-forest-labs/flux-kontext-max) | 2025-05-29 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.1 Kontext [pro] (black-forest-labs/flux-kontext-pro) | 2025-05-29 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek R1 0528 Qwen3 8B (deepseek/deepseek-r1-0528-qwen3-8b) | 2025-05-29 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek R1 0528 (deepseek/deepseek-r1-0528) | 2025-05-28 | — | — | — | — | — | — | — | — | — | — | — |
| Codestral Embed (mistral/codestral-embed-2505) | 2025-05-28 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4 (latest) (anthropic/claude-opus-4-0) | 2025-05-22 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Opus 4 (anthropic/claude-opus-4-20250514) | 2025-05-22 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 4 (latest) (anthropic/claude-sonnet-4-0) | 2025-05-22 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 4 (anthropic/claude-sonnet-4-20250514) | 2025-05-22 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.5 Flash Preview 05-20 (google/gemini-2.5-flash-preview-05-20) | 2025-05-20 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini Embedding 001 (google/gemini-embedding-001) | 2025-05-20 | — | — | — | — | — | — | — | — | — | — | — |
| Lyria RealTime (google/lyria-realtime-exp) | 2025-05-20 | — | — | — | — | — | — | — | — | — | — | — |
| Sarvam-M (sarvam/sarvam-m) | 2025-05-20 | — | — | — | — | — | — | — | — | — | — | — |
| Solar Pro 2 (upstage/solar-pro2) | 2025-05-20 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Medium 3 (mistral/mistral-medium-2505) | 2025-05-07 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Medium 3 (mistral/mistral-medium-3) | 2025-05-07 | — | — | — | — | — | — | — | — | — | — | — |
| Avatar IV (heygen/avatar-iv) | 2025-05 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Premier (amazon/nova-premier) | 2025-04-30 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 8B (alibaba/qwen3-8b) | 2025-04-29 | — | — | — | — | — | — | — | — | — | — | — |
| Llama Guard 4 12B (meta/llama-guard-4-12b) | 2025-04-29 | — | — | — | — | — | — | — | — | — | — | — |
| Llama Prompt Guard 2 22M (meta/llama-prompt-guard-2-22m) | 2025-04-29 | — | — | — | — | — | — | — | — | — | — | — |
| Llama Prompt Guard 2 86M (meta/llama-prompt-guard-2-86m) | 2025-04-29 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 235B-A22B (alibaba/qwen3-235b-a22b) | 2025-04-28 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 30B A3B (alibaba/qwen3-30b-a3b) | 2025-04-28 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen3 32B (alibaba/qwen3-32b) | 2025-04-28 | — | — | — | — | — | — | — | — | — | — | — |
| Palmyra X5 (writer/palmyra-x5) | 2025-04-28 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-Image-1 (openai/gpt-image-1) | 2025-04-24 | — | — | — | — | — | — | — | — | — | — | — |
| o3 (openai/o3) | 2025-04-16 | — | — | — | — | — | — | — | — | — | — | — |
| o4-mini (openai/o4-mini) | 2025-04-16 | — | — | — | — | — | — | — | — | — | — | — |
| Embed 4 (cohere/embed-v4.0) | 2025-04-15 | — | — | — | — | — | — | — | — | — | — | — |
| Aura-2 (deepgram/aura-2) | 2025-04-15 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.1 Nemotron 70B Instruct (nvidia/llama-3.1-nemotron-70b-instruct) | 2025-04-15 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4.1 (openai/gpt-4.1) | 2025-04-14 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4.1 mini (openai/gpt-4.1-mini) | 2025-04-14 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4.1 nano (openai/gpt-4.1-nano) | 2025-04-14 | — | — | — | — | — | — | — | — | — | — | — |
| Pixtral Large (25.02) (mistral/pixtral-large-2502) | 2025-04-08 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.1 Nemotron Ultra 253B (nvidia/llama-3.1-nemotron-ultra-253b) | 2025-04-07 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 4 Maverick 17B Instruct (meta/llama-4-maverick-17b-instruct) | 2025-04-05 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 4 Scout 17B Instruct (meta/llama-4-scout-17b-instruct) | 2025-04-05 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek V3 0324 (deepseek/deepseek-chat-v3-0324) | 2025-03-24 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek V3 0324 (deepseek/deepseek-v3-0324) | 2025-03-24 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o Mini Transcribe (openai/gpt-4o-mini-transcribe) | 2025-03-20 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o Mini TTS (openai/gpt-4o-mini-tts) | 2025-03-20 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o Transcribe (openai/gpt-4o-transcribe) | 2025-03-20 | — | — | — | — | — | — | — | — | — | — | — |
| o1-pro (openai/o1-pro) | 2025-03-19 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.3 Nemotron Super 49B v1 (nvidia/llama-3.3-nemotron-super-49b-v1) | 2025-03-18 | — | — | — | — | — | — | — | — | — | — | — |
| Magistral Medium (latest) (mistral/magistral-medium-latest) | 2025-03-17 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Small 3.1 24B (mistral/mistral-small-3-1-24b-instruct-2503) | 2025-03-17 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Small 3.1 24B (mistral/mistral-small-3.1-24b-instruct) | 2025-03-17 | — | — | — | — | — | — | — | — | — | — | — |
| Command A (cohere/command-a) | 2025-03-13 | — | — | — | — | — | — | — | — | — | — | — |
| Command A (cohere/command-a-03-2025) | 2025-03-13 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 3 12B IT (google/gemma-3-12b-it) | 2025-03-12 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 3 27B IT (google/gemma-3-27b-it) | 2025-03-12 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 3 4B IT (google/gemma-3-4b-it) | 2025-03-12 | — | — | — | — | — | — | — | — | — | — | — |
| Reka Flash 3 (rekaai/reka-flash-3) | 2025-03-10 | — | — | — | — | — | — | — | — | — | — | — |
| Skyfall 36B V2 (thedrummer/skyfall-36b-v2) | 2025-03-10 | — | — | — | — | — | — | — | — | — | — | — |
| QwQ 32B (alibaba/qwq-32b) | 2025-03-05 | — | — | — | — | — | — | — | — | — | — | — |
| QwQ Plus (alibaba/qwq-plus) | 2025-03-05 | — | — | — | — | — | — | — | — | — | — | — |
| Aya Vision 32B (cohere/c4ai-aya-vision-32b) | 2025-03-04 | — | — | — | — | — | — | — | — | — | — | — |
| Aya Vision 8B (cohere/c4ai-aya-vision-8b) | 2025-03-04 | — | — | — | — | — | — | — | — | — | — | — |
| Orpheus 3B (canopylabs/orpheus-3b-0.1-ft) | 2025-03 | — | — | — | — | — | — | — | — | — | — | — |
| CSM 1B (sesame/csm-1b) | 2025-03 | — | — | — | — | — | — | — | — | — | — | — |
| Command R7B Arabic (cohere/command-r7b-arabic-02-2025) | 2025-02-27 | — | — | — | — | — | — | — | — | — | — | — |
| Phi-4-mini (microsoft/phi-4-mini) | 2025-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| Phi-4-multimodal-instruct (microsoft/phi-4-multimodal-instruct) | 2025-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 3.7 (anthropic/claude-3-7-sonnet-20250219) | 2025-02-19 | — | — | — | — | — | — | — | — | — | — | — |
| Saba (mistral/mistral-saba) | 2025-02-17 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax image-01 (minimax/image-01) | 2025-02-15 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax image-01-live (minimax/image-01-live) | 2025-02-15 | — | — | — | — | — | — | — | — | — | — | — |
| Nova-3 (deepgram/nova-3) | 2025-02-12 | — | — | — | — | — | — | — | — | — | — | — |
| Aion-RP 1.0 (8B) (aion-labs/aion-rp-llama-3.1-8b) | 2025-02-04 | — | — | — | — | — | — | — | — | — | — | — |
| Sonar Deep Research (perplexity/sonar-deep-research) | 2025-02-01 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Small 3 (mistral/mistral-small-24b-instruct-2501) | 2025-01-30 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen2.5-VL 72B Instruct (alibaba/qwen2-5-vl-72b-instruct) | 2025-01-26 | — | — | — | — | — | — | — | — | — | — | — |
| ALLaM-2-7b (sdaia/allam-2-7b) | 2025-01-23 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek-R1 (deepseek/deepseek-r1) | 2025-01-20 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek-R1-Distill-Qwen-32B (deepseek/deepseek-r1-distill-qwen-32b) | 2025-01-20 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen-Omni Turbo (alibaba/qwen-omni-turbo) | 2025-01-19 | — | — | — | — | — | — | — | — | — | — | — |
| MiniMax Text 01 (MiniMax) (minimax/MiniMax-Text-01) | 2025-01-15 | — | — | — | — | — | — | — | — | — | — | — |
| DeepSeek-V3 (deepseek/deepseek-v3) | 2024-12-26 | — | — | — | — | — | — | — | — | — | — | — |
| o3-mini (openai/o3-mini) | 2024-12-20 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven Flash v2 (elevenlabs/eleven_flash_v2) | 2024-12-19 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven Flash v2.5 (elevenlabs/eleven_flash_v2_5) | 2024-12-19 | — | — | — | — | — | — | — | — | — | — | — |
| Phoenix 1.0 (leonardo/phoenix-1.0) | 2024-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.3 Euryale 70B (sao10k/l3.3-euryale-70b) | 2024-12-18 | — | — | — | — | — | — | — | — | — | — | — |
| Command R7B (cohere/command-r7b-12-2024) | 2024-12-13 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.0 Flash (google/gemini-2.0-flash) | 2024-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| Gemini 2.0 Flash-Lite (google/gemini-2.0-flash-lite) | 2024-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.3-70B-Instruct (meta/llama-3.3-70b-instruct) | 2024-12-06 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Lite 1.0 (amazon/nova-lite-v1) | 2024-12-05 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Micro 1.0 (amazon/nova-micro-v1) | 2024-12-05 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Pro 1.0 (amazon/nova-pro-v1) | 2024-12-05 | — | — | — | — | — | — | — | — | — | — | — |
| o1 (openai/o1) | 2024-12-05 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Lite (amazon/nova-lite) | 2024-12-03 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Micro (amazon/nova-micro) | 2024-12-03 | — | — | — | — | — | — | — | — | — | — | — |
| Nova Pro (amazon/nova-pro) | 2024-12-03 | — | — | — | — | — | — | — | — | — | — | — |
| Rerank 3.5 (cohere/rerank-v3.5) | 2024-12-02 | — | — | — | — | — | — | — | — | — | — | — |
| Kokoro 82M (hexgrad/kokoro-82m) | 2024-12 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o (2024-11-20) (openai/gpt-4o-2024-11-20) | 2024-11-20 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Large 2.1 (mistral/mistral-large-2411) | 2024-11-18 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen2.5-Coder-0.5B (alibaba/qwen2.5-coder-0.5b) | 2024-11-12 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen2.5-Coder-32B-Instruct (alibaba/qwen2.5-coder-32b-instruct) | 2024-11-12 | — | — | — | — | — | — | — | — | — | — | — |
| UnslopNemo 12B (thedrummer/unslopnemo-12b) | 2024-11-08 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen Turbo (alibaba/qwen-turbo) | 2024-11-01 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Large (latest) (mistral/mistral-large-latest) | 2024-11-01 | — | — | — | — | — | — | — | — | — | — | — |
| Pixtral Large (latest) (mistral/pixtral-large-latest) | 2024-11-01 | — | — | — | — | — | — | — | — | — | — | — |
| Recraft V3 (recraft/recraft-v3) | 2024-10-30 | — | — | — | — | — | — | — | — | — | — | — |
| Aya Expanse 32B (cohere/c4ai-aya-expanse-32b) | 2024-10-24 | — | — | — | — | — | — | — | — | — | — | — |
| Aya Expanse 8B (cohere/c4ai-aya-expanse-8b) | 2024-10-24 | — | — | — | — | — | — | — | — | — | — | — |
| Magnum v4 72B (anthracite-org/magnum-v4-72b) | 2024-10-22 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Haiku 3.5 (anthropic/claude-3-5-haiku-20241022) | 2024-10-22 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Sonnet 3.5 v2 (anthropic/claude-3-5-sonnet-20241022) | 2024-10-22 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 3B (mistral/ministral-3b) | 2024-10-16 | — | — | — | — | — | — | — | — | — | — | — |
| Ministral 8B Instruct (mistral/ministral-8b-instruct-2410) | 2024-10-16 | — | — | — | — | — | — | — | — | — | — | — |
| Palmyra X4 (writer/palmyra-x4) | 2024-10-09 | — | — | — | — | — | — | — | — | — | — | — |
| Whisper Large v3 Turbo (openai/whisper-large-v3-turbo) | 2024-10-01 | — | — | — | — | — | — | — | — | — | — | — |
| omni-moderation (openai/omni-moderation-latest) | 2024-09-26 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.2-11B-Vision-Instruct (meta/llama-3.2-11b-vision-instruct) | 2024-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.2-1B (meta/llama-3.2-1b) | 2024-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.2 1B Instruct (meta/llama-3.2-1b-instruct) | 2024-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.2-3B (meta/llama-3.2-3b) | 2024-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.2 3B Instruct (meta/llama-3.2-3b-instruct) | 2024-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.2-90B-Vision-Instruct (meta/llama-3.2-90b-vision-instruct) | 2024-09-25 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen2.5 7B Instruct (alibaba/qwen2.5-7b-instruct) | 2024-09-19 | — | — | — | — | — | — | — | — | — | — | — |
| Pixtral 12B (mistral/pixtral-12b) | 2024-09-11 | — | — | — | — | — | — | — | — | — | — | — |
| Command R (cohere/command-r-08-2024) | 2024-08-30 | — | — | — | — | — | — | — | — | — | — | — |
| Command R+ (cohere/command-r-plus-08-2024) | 2024-08-30 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3.1 Euryale 70B v2.2 (sao10k/l3.1-euryale-70b) | 2024-08-28 | — | — | — | — | — | — | — | — | — | — | — |
| Nemotron Mini 4B Instruct (nvidia/nemotron-mini-4b-instruct) | 2024-08-21 | — | — | — | — | — | — | — | — | — | — | — |
| Hermes 3 70B Instruct (nousresearch/hermes-3-llama-3.1-70b) | 2024-08-18 | — | — | — | — | — | — | — | — | — | — | — |
| Hermes 3 405B Instruct (nousresearch/hermes-3-llama-3.1-405b) | 2024-08-16 | — | — | — | — | — | — | — | — | — | — | — |
| Dracarys Llama 3.1 70B Instruct (abacusai/dracarys-llama-3.1-70b-instruct) | 2024-08-14 | — | — | — | — | — | — | — | — | — | — | — |
| Llama 3 8B Lunaris (sao10k/l3-lunaris-8b) | 2024-08-13 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o (2024-08-06) (openai/gpt-4o-2024-08-06) | 2024-08-06 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.1 [dev] (black-forest-labs/flux-1-dev) | 2024-08-01 | — | — | — | — | — | — | — | — | — | — | — |
| FLUX.1 [schnell] (black-forest-labs/flux-1-schnell) | 2024-08-01 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 2 2B IT (google/gemma-2-2b-it) | 2024-07-31 | — | — | — | — | — | — | — | — | — | — | — |
| BGE Multilingual Gemma2 (baai/bge-multilingual-gemma2) | 2024-07-25 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Large 2407 (mistral/mistral-large-2407) | 2024-07-24 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.1-70B-Instruct (meta/llama-3.1-70b-instruct) | 2024-07-23 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-3.1-8B-Instruct (meta/llama-3.1-8b-instruct) | 2024-07-23 | — | — | — | — | — | — | — | — | — | — | — |
| Llama-Guard-3-8B (meta/llama-guard-3-8b) | 2024-07-23 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven Turbo v2.5 (elevenlabs/eleven_turbo_v2_5) | 2024-07-19 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Nemo (mistral/mistral-nemo) | 2024-07-18 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o mini (openai/gpt-4o-mini) | 2024-07-18 | — | — | — | — | — | — | — | — | — | — | — |
| Gemma 2 27B (google/gemma-2-27b-it) | 2024-07-13 | — | — | — | — | — | — | — | — | — | — | — |
| Codestral-22B-v0.1 (mistral/codestral-22b-v0.1) | 2024-05-29 | — | — | — | — | — | — | — | — | — | — | — |
| Codestral (latest) (mistral/codestral-latest) | 2024-05-29 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral 7B Instruct v0.3 (mistral/mistral-7b-instruct-v0.3) | 2024-05-22 | — | — | — | — | — | — | — | — | — | — | — |
| Vision Large (vispark/vision-large) | 2024-05-15 | — | — | — | — | — | — | — | — | — | — | — |
| Vision Medium (vispark/vision-medium) | 2024-05-15 | — | — | — | — | — | — | — | — | — | — | — |
| Vision Small (vispark/vision-small) | 2024-05-15 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o (openai/gpt-4o) | 2024-05-13 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4o (2024-05-13) (openai/gpt-4o-2024-05-13) | 2024-05-13 | — | — | — | — | — | — | — | — | — | — | — |
| Hermes 2 Pro Llama 3 8B (nousresearch/hermes-2-pro-llama-3-8b) | 2024-04-30 | — | — | — | — | — | — | — | — | — | — | — |
| GTE Large EN v1.5 (alibaba/gte-large-en-v1.5) | 2024-04-20 | — | — | — | — | — | — | — | — | — | — | — |
| Mixtral 8x22B Instruct (mistral/mixtral-8x22b-instruct) | 2024-04-17 | — | — | — | — | — | — | — | — | — | — | — |
| WizardLM 2 8x22B (microsoft/wizardlm-2-8x22b) | 2024-04-15 | — | — | — | — | — | — | — | — | — | — | — |
| Rerank English 3 (cohere/rerank-english-v3.0) | 2024-04-11 | — | — | — | — | — | — | — | — | — | — | — |
| Rerank Multilingual 3 (cohere/rerank-multilingual-v3.0) | 2024-04-11 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen-VL Max (alibaba/qwen-vl-max) | 2024-04-08 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen Max (alibaba/qwen-max) | 2024-04-03 | — | — | — | — | — | — | — | — | — | — | — |
| BGE Reranker V2 M3 (baai/bge-reranker-v2-m3) | 2024-03-15 | — | — | — | — | — | — | — | — | — | — | — |
| Claude Haiku 3 (anthropic/claude-3-haiku-20240307) | 2024-03-13 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Large (mistral/mistral-large) | 2024-02-26 | — | — | — | — | — | — | — | — | — | — | — |
| SDXL-Lightning (bytedance-seed/stable-diffusion-xl-lightning) | 2024-02-21 | — | — | — | — | — | — | — | — | — | — | — |
| BGE M3 (baai/bge-m3) | 2024-01-30 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen Plus (alibaba/qwen-plus) | 2024-01-25 | — | — | — | — | — | — | — | — | — | — | — |
| Qwen-VL Plus (alibaba/qwen-vl-plus) | 2024-01-25 | — | — | — | — | — | — | — | — | — | — | — |
| text-embedding-3-large (openai/text-embedding-3-large) | 2024-01-25 | — | — | — | — | — | — | — | — | — | — | — |
| text-embedding-3-small (openai/text-embedding-3-small) | 2024-01-25 | — | — | — | — | — | — | — | — | — | — | — |
| Sonar (perplexity/sonar) | 2024-01-01 | — | — | — | — | — | — | — | — | — | — | — |
| Sonar Pro (perplexity/sonar-pro) | 2024-01-01 | — | — | — | — | — | — | — | — | — | — | — |
| Sonar Reasoning Pro (perplexity/sonar-reasoning-pro) | 2024-01-01 | — | — | — | — | — | — | — | — | — | — | — |
| SOLAR 10.7B Instruct v1.0 (upstage/solar-10.7b-instruct-v1.0) | 2023-12-12 | — | — | — | — | — | — | — | — | — | — | — |
| Mistral Embed (mistral/mistral-embed) | 2023-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| Mixtral 8x7B Instruct v0.1 (mistral/mixtral-8x7b-instruct-v0.1) | 2023-12-11 | — | — | — | — | — | — | — | — | — | — | — |
| DreamShaper 8 LCM (lykon/dreamshaper-8-lcm) | 2023-12-06 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven Turbo v2 (elevenlabs/eleven_turbo_v2) | 2023-11-09 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4 (openai/gpt-4) | 2023-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-4 Turbo (openai/gpt-4-turbo) | 2023-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| TTS-1 (openai/tts-1) | 2023-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| TTS-1 HD (openai/tts-1-hd) | 2023-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| Whisper 3 Large (openai/whisper-large-v3) | 2023-11-06 | — | — | — | — | — | — | — | — | — | — | — |
| Embed English Light 3 (cohere/embed-english-light-v3.0) | 2023-11-02 | — | — | — | — | — | — | — | — | — | — | — |
| Embed English 3 (cohere/embed-english-v3.0) | 2023-11-02 | — | — | — | — | — | — | — | — | — | — | — |
| Embed Multilingual Light 3 (cohere/embed-multilingual-light-v3.0) | 2023-11-02 | — | — | — | — | — | — | — | — | — | — | — |
| Embed Multilingual 3 (cohere/embed-multilingual-v3.0) | 2023-11-02 | — | — | — | — | — | — | — | — | — | — | — |
| BGE Base EN v1.5 (baai/bge-base-en-v1.5) | 2023-09-12 | — | — | — | — | — | — | — | — | — | — | — |
| BGE Large EN v1.5 (baai/bge-large-en-v1.5) | 2023-09-12 | — | — | — | — | — | — | — | — | — | — | — |
| Eleven Multilingual v2 (elevenlabs/eleven_multilingual_v2) | 2023-08-22 | — | — | — | — | — | — | — | — | — | — | — |
| MythoMax L2 13B (gryphe/mythomax-l2-13b) | 2023-08-10 | — | — | — | — | — | — | — | — | — | — | — |
| Weaver (alpha) (mancer/weaver) | 2023-08-02 | — | — | — | — | — | — | — | — | — | — | — |
| Stable Diffusion XL Base 1.0 (stabilityai/stable-diffusion-xl-base-1.0) | 2023-07-26 | — | — | — | — | — | — | — | — | — | — | — |
| ReMM SLERP 13B (undi95/remm-slerp-l2-13b) | 2023-07-22 | — | — | — | — | — | — | — | — | — | — | — |
| GTE Base (thenlper/gte-base) | 2023-07 | — | — | — | — | — | — | — | — | — | — | — |
| GTE Large (thenlper/gte-large) | 2023-07 | — | — | — | — | — | — | — | — | — | — | — |
| Multilingual E5 Large (intfloat/multilingual-e5-large) | 2023-06 | — | — | — | — | — | — | — | — | — | — | — |
| E5 Base v2 (intfloat/e5-base-v2) | 2023-05 | — | — | — | — | — | — | — | — | — | — | — |
| E5 Large v2 (intfloat/e5-large-v2) | 2023-05 | — | — | — | — | — | — | — | — | — | — | — |
| GPT-3.5-turbo (openai/gpt-3.5-turbo) | 2023-03-01 | — | — | — | — | — | — | — | — | — | — | — |
| Whisper (openai/whisper-1) | 2023-03-01 | — | — | — | — | — | — | — | — | — | — | — |
| text-embedding-ada-002 (openai/text-embedding-ada-002) | 2022-12-15 | — | — | — | — | — | — | — | — | — | — | — |
| all-MiniLM-L12-v2 (sentence-transformers/all-minilm-l12-v2) | 2021-08-30 | — | — | — | — | — | — | — | — | — | — | — |
| all-MiniLM-L6-v2 (sentence-transformers/all-minilm-l6-v2) | 2021-08-30 | — | — | — | — | — | — | — | — | — | — | — |
| all-mpnet-base-v2 (sentence-transformers/all-mpnet-base-v2) | 2021-08-30 | — | — | — | — | — | — | — | — | — | — | — |
| multi-qa-mpnet-base-dot-v1 (sentence-transformers/multi-qa-mpnet-base-dot-v1) | 2021-08-23 | — | — | — | — | — | — | — | — | — | — | — |
| paraphrase-MiniLM-L6-v2 (sentence-transformers/paraphrase-minilm-l6-v2) | 2021-05-19 | — | — | — | — | — | — | — | — | — | — | — |

## 需要关注的问题

- [GPT-6.1 Terra (openai/gpt-6.1-terra)](models/openai/gpt-6.1-terra.md) — DeepSWE: 待核实 — 需要在首轮模型覆盖完成后再次检查是否有发布后的官方结果。; SWE-bench Pro: 待核实 — 榜单快照早于模型发布；需在首轮覆盖完成后复查发布后结果。; AutomationBench: 待核实 — 需取得完整官方排行榜或官方模型行后再判断；没有写入 AA 的 AutomationBench-AA 分数。; OSWorld: 待核实 — 待确认分数及其与仓库 binary task completion rate 指标的对应关系；未从图表转写数值。; Humanity's Last Exam: 待核实 — 需要从 AA 原始榜单或可核对的原始评测报告确认准确分值及对应 effort。; Vals Index: 冲突 — 请 Vals AI 的后续修订说明或可追溯 run 记录解释 60.17% 与 60.54% 的差异。
- [Kimi K3.1 Pro (moonshotai/kimi-k3.1-pro)](models/moonshotai/kimi-k3.1-pro.md) — DeepSWE: 待核实 — Kimi 官方 DeepSWE 图表中的确切分数及其全部测试条件尚未从可读原始文本核实。; Terminal-Bench-Science: 待核实 — 待直接核实 Kimi 官方图表报告的 Claude-Code 配置数值；与已记录的独立评测属于不同 harness。; AutomationBench: 待核实 — 当前可读的 Zapier 榜单不足以确认折叠行中是否存在 Kimi K3.1 Pro 的 v1.0.6 成绩。; OSWorld: 待核实 — 待从原始报告确认分数、binary/partial 指标及测试集条件。; Chartography: 待核实 — 待从 Kimi 官方图表直接核实 with-Python 配置的确切分数和条件；该配置与 Surge 原生榜单分开。; Humanity's Last Exam: 待核实 — 待直接核实 Kimi 官方 HLE full-set with-tools 图表中的确切分数与条件。; GDPval-AA: 冲突 — 同一来源发布文章与当前排行榜的点估计相差 12 Elo，缺少修订说明或可区分的测试配置。
- [Flint (recursive/flint)](models/recursive/flint.md) — Terminal-Bench-Science: 待核实 — 官方 leaderboard 的动态结果未能从页面文本读取；后续可复查可交互榜单或源数据。; AutomationBench: 待核实 — 官方网页不能从当前可读表格确认折叠条目；没有找到可核实分数。
- [elephant-1 (baseten/elephant-1)](models/baseten/elephant-1.md) — AutomationBench: 待核实 — 需要完整展开 Zapier 官方榜单，或找到可验证的 elephant-1 agent wrapper 评测。; OSWorld: 待核实 — 官方 leaderboard 为动态内容且当前未取得可完整检索的模型表；没有找到精确成绩。
- [mammoth-1 (baseten/mammoth-1)](models/baseten/mammoth-1.md) — AutomationBench: 待核实 — 需要完整展开 Zapier 官方榜单，或找到可验证的 Mammoth-1 agent wrapper 结果。; OSWorld: 待核实 — 官方动态 leaderboard 未能完整检索；没有找到 Mammoth-1 精确分数。
- [MiniMax-M3.1-Flash (minimax/MiniMax-M3.1-Flash)](models/minimax/MiniMax-M3.1-Flash.md) — GDPval-AA: 待核实 — Recheck if the current official AA leaderboard exposes a MiniMax-M3.1-Flash row or a stable, directly viewable result; do not use the stale 1466 candidate without primary-source confirmation.
- [DeepSeek V4.1 Flash 1017 (deepseek/deepseek-v4.1-flash-1017)](models/deepseek/deepseek-v4.1-flash-1017.md) — OSWorld: 待核实 — Need a directly verifiable primary-source score and confirmation of the exact metric/configuration. Do not treat the secondary 69.3 Partial score as binary task completion rate.
- [Mercury 3 (inception/mercury-3)](models/inception/mercury-3.md) — AutomationBench: 待核实 — 需要核实 Zapier 官方榜单折叠项，或找到 Mercury 3 的原始 AutomationBench 评测结果及数据集条件。; OSWorld: 待核实 — 官方动态榜单内容未能读取；若存在 wrapper 结果，需确认精确版本、指标和运行配置。
- [Muse Spark Open (meta/muse-spark-open)](models/meta/muse-spark-open.md) — Terminal-Bench: 冲突 — 需要由维护者确认两条独立 evaluator 结果是否作为不同配置并列保留；AA 仅公布四舍五入整数值。; AutomationBench: 待核实 — 官方榜仍有 119 条未展开，当前可读内容不足以确认完整榜单是否包含该模型。; Humanity's Last Exam: 待核实 — Meta 方法没有明确该 with-tools 评测使用 benchmark 定义中的完整 2,500-question 原始集合，题集范围待核实。
- [Nemotron 3.5 Super 120B A12B (nvidia/nemotron-3.5-super-120b-a12b)](models/nvidia/nemotron-3.5-super-120b-a12b.md) — AutomationBench: 待核实 — Zapier 榜单仍有 119 条未展开；Surge 所列 Nemotron 3.5 Super 变体身份和配置不充分。; Chartography: 待核实 — 标准图像输入的 Chartography 与目标 text-only API 不兼容；Surge with-tools 的相关结果是否属于目标 API 及是否属于目标配置仍待核实。
- [Nemotron 3.5 Super VL 120B A12B (nvidia/nemotron-3.5-super-vl-120b-a12b)](models/nvidia/nemotron-3.5-super-vl-120b-a12b.md) — DeepSWE: 待核实 — NVIDIA卡上的offline记录是否为DeepSWE v1.1及其测试配置，尚无公开证据。; Terminal-Bench: 冲突 — NVIDIA offline结果与Vals/AA 0%结果数值不同，公开材料未给足测试条件以判定差异来源；保留Vals/AA目标配置记录，不取最高值。NVIDIA卡上的精度和score单位/协议需进一步核实。; Terminal-Bench-Science: 待核实 — benchmark成绩对应的checkpoint精度/provider未披露。; AutomationBench: 待核实 — Zapier榜剩余119条不可见；Surge AutomationBench记录未说明精确checkpoint及协议。; Chartography: 待核实 — Surge图表理解结果的checkpoint精度和工具配置未知，无法确认属于本条Super-VL model id。; Artificial Analysis Intelligence Index: 待核实 — AA Index结果所用checkpoint精度、provider及评测参数未披露。; Vals Index: 待核实 — Vals结果对应的checkpoint精度与benchmark-specific provider/参数未披露。
- [Grok Voice 3.0 (xai/grok-voice-3.0)](models/xai/grok-voice-3.0.md) — Terminal-Bench-Science: 待核实 — 需在公开可读的完整模型数据中复核 Grok Voice 3.0；没有写入分数。; AutomationBench: 待核实 — 完整公开榜单中是否包含 Grok Voice 3.0 尚未核实；通过适配器参评及其成绩均没有证据。; Humanity's Last Exam: 待核实 — 无法在不登录的官方提交看板中核实是否有该模型条目；未将 HLE-Diamond 或其他 Grok 版本结果代入。
- [Gemini 4 Argon (google/gemini-4-argon)](models/google/gemini-4-argon.md) — OSWorld: 待核实 — The repository definition tracks binary task completion rate; the reported partial score is a different metric and cannot be mapped without conflation.; GDPval-AA: 待核实 — Could not verify whether a result exists outside the currently visible public table; no score recorded.
- [Muse Wonder (meta/muse-wonder-1.0)](models/meta/muse-wonder-1.0.md) — AutomationBench: 待核实 — Cannot verify an exact Zapier 1.0.6 task_completed_correctly score or establish that the existing AA strict-pass metric is identical to the benchmark definition.
- [Muse Wonder Full (meta/muse-wonder-full)](models/meta/muse-wonder-full.md) — AutomationBench: 待核实 — An exact Zapier 1.0.6 task_completed_correctly score, or equivalence between the existing AA strict-pass metric and the canonical target metric, could not be verified.
- [LightOnOCR-3 0.8B (lightonai/lightonocr-3-0.8b)](models/lightonai/lightonocr-3-0.8b.md) — Terminal-Bench: 待核实 — Verify the exact checkpoint against the fully rendered Terminal-Bench 4.0 leaderboard; current page extraction did not expose model rows.
- [Claude Haiku 5.5 (anthropic/claude-haiku-5-5)](models/anthropic/claude-haiku-5-5.md) — OSWorld: 待核实 — Anthropic 页面仅称 Offline subset，未直接说明 partial reward；具体指标与 OSWorld 2.1 binary completion 定义的对应关系仍需核实。; Chartography: 待核实 — Anthropic 报告的 score 是否使用官方 Chartography mean Pass@1 协议和相同测试配置尚未确认。; Humanity's Last Exam: 待核实 — Anthropic 未说明两条分数所用题集是原始 HLE 还是 HLE-Rolling，且未给出 harness、effort 或测试日期；暂不能映射到本地 original HLE accuracy 定义。
- [MiniCPM-V 4.7 35B-A3B (openbmb/minicpm-v-4.7-35b-a3b)](models/openbmb/minicpm-v-4.7-35b-a3b.md) — OSWorld: 待核实 — 公开材料不足以确认该精确模型是否有 OSWorld v2.1 结果；需要可核对的 v2.1 排行榜/运行记录。
- [Mistral Large 4 (mistral/mistral-large-4)](models/mistral/mistral-large-4.md) — DeepSWE: 待核实 — 需要确认 Mistral 报告的 61.7% 对应本地定义的 pass@1 后，才可补 metric 并计入覆盖率。; SWE-bench Pro: 待核实 — 需复查模型发布后的官方 V2 Full 榜单或 Mistral 原始报告，确认是否存在对应版本成绩。; AutomationBench: 待核实 — 尚不能确认 59.9% 对应本地定义的 AutomationBench v1.0.6 及其 held-out private task set，故没有写入 TOML。; OSWorld: 待核实 — 需要可核实的 OSWorld V2.1 排行榜或精确模型结果。; Humanity's Last Exam: 待核实 — 需要可直接复核的官方结果页，确认 35% 是否确属原版 HLE 的该 Preview 版本。; GDPval-AA: 待核实 — 需要可直接复核的官方榜单或结果页，确认 1434 Elo 及准确模型版本。; Vals Index: 待核实 — 需要能把 V2.2 成绩明确关联到 10 月 6 日 Preview 的来源；当前网页结果不能区分目标检查点。
- [Drex 2.0 (nace-ai/drex-v2.0)](models/nace-ai/drex-v2.0.md) — OSWorld: 待核实 — 需确认 Nace 的 0.636 是否使用 OSWorld v2.1 及其准确指标/harness，当前不写入 TOML。; Humanity's Last Exam: 待核实 — 需要确认该 12.8 对应仓库定义的原版 HLE 2,500 题及 accuracy/pass@1 协议；当前不写入 TOML。
- [MiniCPM-V 4.7 1B (openbmb/minicpm-v-4.7-1b)](models/openbmb/minicpm-v-4.7-1b.md) — DeepSWE: 待核实 — 需要复查模型公开后的 DeepSWE v1.1 榜单或具体官方结果；当前无成绩可写入。; Terminal-Bench: 待核实 — 需在官方动态榜单中复查 MiniCPM-V 4.7 1B 的精确行及运行条件。; Terminal-Bench-Science: 待核实 — 需复查官方动态 Terminal-Bench Science 榜单是否有该精确模型及可核实条件。
- [Beam 1.0 501B A23B (reflection/beam-1.0-501b-a23b)](models/reflection/beam-1.0-501b-a23b.md) — DeepSWE: 冲突 — Reflection 后续文章报告 44.4%，而 HF 评测记录中的 BF16 成绩为 43.3%；文章没有提供足以核对两者测试配置的信息，保留现有 BF16 成绩，不择高覆盖。; AutomationBench: 冲突 — Reflection 后续文章报 public split 37.0，最终模型卡报 39.3，来源未解释差异。未找到 private split 成绩。; Chartography: 待核实 — 未确认榜单分数对应当前模型文件中的精确 checkpoint 和测试配置，暂不归入模型。; Humanity's Last Exam: 冲突 — Reflection 介绍文章另报 36.2%/51.2%，未披露足以核对的测试配置；另外需确认其与本地定义的原始 2,500 题使用完全一致。
- [Kolibri 1 (aleph-alpha/kolibri-1)](models/aleph-alpha/kolibri-1.md) — AutomationBench: 待核实 — 官方完整榜单模型行尚未核实，不能把其他 agent benchmark 的成绩移用。; Humanity's Last Exam: 待核实
- [Mercury Decide (inception/mercury-decide)](models/inception/mercury-decide.md) — Humanity's Last Exam: 待核实 — 需从 Artificial Analysis 官方 HLE-MultiChoice 页面取得 Mercury Decide 的精确 accuracy 与可核实测试条件；当前公开页面文本未显示该数值。
- [Ling 3.1 Flash (inclusionai/ling-3.1-flash)](models/inclusionai/ling-3.1-flash.md) — DeepSWE: 待核实 — HF 模型评测元数据缺少版本与 metric；59.7 是否对应本地 DeepSWE 1.1/pass@1 定义尚未被来源显式确认。; SWE-bench Pro: 待核实 — 来源元数据没有 config/subset；需要确认 68.74 对应本地定义的 V2 2.0.0 默认 642-task 配置，而非 hard 或其它配置。; AutomationBench: 待核实 — 官方模型卡评测图中的 AutomationBench 数值、版本和配置尚待直接复核；public set 结果不能代替官方 private task leaderboard。; Humanity's Last Exam: 待核实 — 需要从模型作者或一手评测记录确认 HLE 37.44 的有效 task、metric、数据子集及测试条件；不得将 HLE-Diamond 或旧 AA 指数结果当作原始 HLE。; GDPval-AA: 冲突 — 需确认 AA 的 1,617/1,618 是否不同运行、缓存版本或配置，并取得当前公开的一手榜单行后再写入。
- [GPT-6.1 Sol (openai/gpt-6.1-sol)](models/openai/gpt-6.1-sol.md) — DeepSWE: 待核实 — 需找到 GPT-6.1 Sol 准确版本的公开绝对成绩及测试条件。; AutomationBench: 待核实 — 需核实 GPT-6.1 Sol 是否有公开的 AutomationBench 1.0.6 绝对分数及精确 effort。; Artificial Analysis Intelligence Index: 冲突 — 需确认这五档分数对应 v5.0 还是 v5.0.1；当前 benchmark 定义为 v5.0。; GDPval-AA: 待核实 — 需找到准确模型版本的绝对 Elo、effort 和评测条件。
- [Claude Sonnet 5.5 (anthropic/claude-sonnet-5-5)](models/anthropic/claude-sonnet-5-5.md) — DeepSWE: 待核实 — 需要直接核对 Anthropic System Card 中 DeepSWE v1.1 的成绩及测试条件。; OSWorld: 冲突 — 本次未找到该模型 OSWorld v2.1 的 binary task completion rate。; Artificial Analysis Intelligence Index: 冲突 — 仓库目标定义为 v5.0；当前可核实的 Sonnet 5.5 行为 v5.0.1，需确认是否存在可映射的 v5.0 同版结果。
- [Drex 1.5 (nace-ai/drex-v1.5)](models/nace-ai/drex-v1.5.md) — OSWorld: 待核实 — Nace’s OSWorld-V2 0.640 row does not disclose release v2.1, metric, or harness; cannot map it to binary task completion rate.; Humanity's Last Exam: 待核实 — Nace’s HLE 11.4 row does not specify metric, dataset subset, or conditions; cannot confirm it is the original 2,500-question HLE target.
- [Qwen 3.8 Max Prime (alibaba/qwen3.8-max-prime)](models/alibaba/qwen3.8-max-prime.md) — Terminal-Bench: 待核实 — Third-party Terminal-Bench 2.1 claims conflict with the target v4 definition and the cited source is unavailable; verify the candidate against an original run before considering any score.
- [Claude Opus 5.5 (anthropic/claude-opus-5-5)](models/anthropic/claude-opus-5-5.md) — SWE-bench Pro: 待核实 — Cannot establish that the System Card 89.9% result used SWE-bench Pro V2 (642-task default configuration).; OSWorld: 冲突 — The verified 81.8% uses partial scoring, while the local Benchmark definition requires binary task completion rate.; Chartography: 待核实 — The Anthropic 89.0% result lacks enough published protocol details to compare with Surge standard-board 66.3%.; GDPval-AA: 冲突 — Anthropic launch report and current Artificial Analysis leaderboard report different Max scores for GDPval-AA v2.1 (1846 vs 1866); the reason is not published.
- [Ember-1 (fireworks/ember-1)](models/fireworks/ember-1.md) — DeepSWE: 冲突 — Fireworks launch report score 75.2% and SII avg@3 score 67.0% differ; the launch report does not publish enough evaluation details to reconcile them.; Terminal-Bench: 待核实 — Vals source metric is accuracy while the local v4 definition requires task resolution rate; source version label 4.0 also differs from the local canonical string 4.0.0.; Terminal-Bench-Science: 待核实 — Vals source metric is accuracy while the local v0.1.0 definition requires task resolution rate.
- [GPT-6 Luna (openai/gpt-6-luna)](models/openai/gpt-6-luna.md) — DeepSWE: 待核实 — 需核实 OpenAI 的 score 指标是否等同本地定义的 pass@1。; Terminal-Bench: 冲突 — 同一 Vals profile 的 9.60% 与当前排行榜 13.64% 不一致；旧结果缺少可比较的 harness/运行条件，尚不能判定是否为不同配置或结果修订。; Terminal-Bench-Science: 冲突 — 同一 Vals profile 的 10.00% 与当前排行榜 4.29% 不一致；旧结果的 harness/运行条件未说明，尚不能判定是否为不同配置或结果修订。; Chartography: 待核实 — 本地定义采用 accuracy (mean; Pass@1)，而排行榜值为 10 次运行的 accuracy/mean；需确认是否在本地定义下计为同一指标/版本。; Humanity's Last Exam: 待核实 — 需找到能直接核验 GPT-6 Luna 原始 HLE 分数、子集及条件的来源；历史 39% 目前仅有过期页面线索。; Artificial Analysis Intelligence Index: 待核实 — 本地定义版本为 5.0，AA 当前发布结果为 5.0.1；精确版本映射待复核。; GDPval-AA: 待核实 — 需进一步核实历史 Max 1445 Elo 是否为现行 v2.1 结果；当前可直接核验的 1052 是 Non-reasoning 配置。
- [GPT-6 Sol (openai/gpt-6-sol)](models/openai/gpt-6-sol.md) — DeepSWE: 待核实 — The source does not establish the run metric as pass@1, so this row remains outside exact local-definition coverage.; Terminal-Bench: 冲突 — The Vals profile's historical 34.34% and current 44.44% results have no disclosed run/configuration difference that explains the discrepancy.; The source metric is accuracy; local mapping uses task resolution rate.; Terminal-Bench-Science: 冲突 — The historical 31.43% and current 30.00% results have no disclosed run/configuration difference that explains the discrepancy.; The historical row's exact benchmark version and test configuration are not specified; the source metric is accuracy while local mapping uses task resolution rate.; Humanity's Last Exam: 待核实 — A directly accessible source row for GPT-6 Sol on the original Humanity's Last Exam set has not been verified.; Artificial Analysis Intelligence Index: 待核实 — Source version 5.0.1 does not exactly match the local definition version 5.0; do not silently rewrite either version.; GDPval-AA: 待核实 — A directly accessible official absolute Elo result for GPT-6 Sol on GDPval-AA v2.1 is still needed.; Vals Index: 待核实 — The profile's 52.71% score has no explicit version label and cannot be reconciled with the v2.2 leaderboard; no v2.2 result was added.
- [Solar Mini 4 (upstage/solar-mini4)](models/upstage/solar-mini4.md) — AutomationBench: 待核实 — Zapier 页面当前展示的数据不足以核实完整目标 v1.0.6 排行榜中是否存在 Solar Mini 4 行；需要之后检查官方完整榜单/原始导出。; Humanity's Last Exam: 冲突 — Upstage 英文 25.8% 与韩文 19.6 的差异无来源说明；需确认题集（全量 2,500 或 text-only 子集）、模型/API revision 及其他评测配置。; Artificial Analysis Intelligence Index: 待核实 — 本地定义为 v5.0，Artificial Analysis 当前方法页为 v5.0.1；当前 Solar Mini 4 profile 没有 V5 分数。需要确认本地目标定义是否应跟随 .1 修订版，并继续监看该型号是否重新上榜。
- [MiMo-V2.6-Flash (xiaomi/mimo-v2.6-flash)](models/xiaomi/mimo-v2.6-flash.md) — DeepSWE: 冲突 — Exact checkpoint leaderboard and model card report 67.9; Xiaomi release note reports approximately 65.7 for DeepSWE v1.1. Published evaluation conditions do not explain the difference, so preserve the existing 67.9 and flag for review.; Terminal-Bench-Science: 待核实 — No exact MiMo result was found in the model card or announcement. The official Harbor leaderboard is dynamically rendered and its full rows were not extractable during this check, so absence is not treated as fully confirmed.; Artificial Analysis Intelligence Index: 待核实 — The current AA profile reports 27 under v5.0.1, so the source row preserves version 5.0.1. The local benchmark definition is version 5.0; this record does not map to it and is excluded from mapped coverage pending definition/version review. The profile links to the published model weights but does not expose an evaluation checkpoint revision.; Vals Index: 待核实 — Vals reports 54.83% using the Xiaomi API, but does not identify the exact checkpoint revision. Xiaomi says MOPD checkpoints were released while the API names stayed mimo-v2.6-flash; this TOML entry points specifically to the Flash-RL weights, so the API result is not copied into the score table pending exact variant confirmation.
- [MiMo-V2.6-Pro (xiaomi/mimo-v2.6-pro)](models/xiaomi/mimo-v2.6-pro.md) — DeepSWE: 冲突 — The Pro-RL card and exact DataCurve row report 71.9 for DeepSWE v1.1; Xiaomi’s launch report separately says approximately 72.6. The reports do not explain whether this reflects a checkpoint or evaluation-condition change. Preserve 71.9 and flag the difference; do not substitute the higher value.; Terminal-Bench-Science: 待核实 — No exact Pro-RL result was found in the model card or announcement. The Harbor leaderboard is dynamically rendered and the current rows were not extractable, so absence cannot be fully confirmed.; Artificial Analysis Intelligence Index: 待核实 — The current profile reports 30 for the V5 Index and labels the live revision v5.0.1. The TOML preserves that version, while the local benchmark definition is 5.0, so the row does not map to coverage until the version definition is reconciled. The profile identifies Pro as an open-weight model but does not disclose the precise checkpoint revision used.; GDPval-AA: 冲突 — The Xiaomi Pro-RL card reports 1673 Elo, while Artificial Analysis comparison/search records include 1691 and an older page showed 1686. These are retained as separate source rows where available; no disclosed test-condition or checkpoint detail resolves the difference. Do not choose a maximum. AA methodology describes GDPval-AA v2.1 as 220 tasks across 44 occupations using Stirrup.; Vals Index: 待核实 — Vals reports 57.81% through the Xiaomi provider/API with temperature 1 and top_p 0.95, but does not disclose the exact checkpoint revision. Xiaomi states that the API alias was updated to MOPD while retaining its name; this TOML entry points to the Pro-RL weights, so no API score is copied pending exact variant confirmation.
- [Viv Fast (vivgrid/viv-fast)](models/vivgrid/viv-fast.md) — Terminal-Bench: 待核实 — 官方 4.0 榜单当前动态结果没有被文本读取，不能据此确认完整模型名单。; Terminal-Bench-Science: 待核实 — 未获得可读取的完整 leaderboard 行，不能确认是否存在 Viv Fast 的精确成绩。; AutomationBench: 待核实 — 完整榜单的其余 119 条结果未从公开页面文本中展开核验；无可写入分数或测试配置。; OSWorld: 待核实 — 未找到能核对 Viv Fast 与 OSWorld 2.1 精确版本绑定的公开榜单条目。; Humanity's Last Exam: 待核实 — 公开页面不足以核实 dashboard 中是否存在该型号提交；没有可核实的分数、数据集变体或测试条件。
- [Grok 4.7 (xai/grok-4.7)](models/xai/grok-4.7.md) — DeepSWE: 待核实 — 来源未给出可与本地 pass@1 定义精确核对的指标与测试配置。; Terminal-Bench: 待核实 — 当前两条记录的来源 metric 与本地定义不完全相同，且 xAI 未公布 harness；需保留原始条件并待定义映射复核。; Terminal-Bench-Science: 待核实 — 本地定义 metric 为 task resolution rate，而 AA 明确报告 pass@1；保留原始 metric，不改写为本地指标，等待精确映射确认。; AutomationBench: 待核实 — 公开榜单尚有未展开条目，不能据此确认不存在 Grok 4.7 成绩。; OSWorld: 待核实 — v2.1 的完整公开排行榜未能核实，当前公开榜与目标版本不一致。; Humanity's Last Exam: 待核实 — 原版 HLE 结果候选缺少可直接复核的公开行；不使用 HLE-Diamond 或未经确认的历史截图替代。; Artificial Analysis Intelligence Index: 待核实 — 本地定义版本 5.0 与来源页面版本 5.0.1 不一致，需要决定是否新增/更新定义后才能纳入覆盖率。
- [MiMo-V2.6-Pro-UltraSpeed (xiaomi/mimo-v2.6-pro-ultraspeed)](models/xiaomi/mimo-v2.6-pro-ultraspeed.md) — DeepSWE: 待核实 — UltraSpeed API SKU 是否有单独评测结果未公开；Pro-RL 不同报告的分数与条件也不完全一致。; Terminal-Bench: 待核实 — 尚无针对 UltraSpeed API SKU 的独立分数或评测配置。; Terminal-Bench-Science: 待核实 — 官方动态排行榜本次未完整载入，无法穷尽确认该项公开结果。; AutomationBench: 待核实 — 公开榜单未能完整展开；尚无该精确 SKU 的可核实结果。; OSWorld: 待核实 — 目标 v2.1 榜单结果未能完整读取，且已找到的 Pro sibling 结果版本/端点均不匹配。
- [Qwen3.8 Omni Flash (alibaba/qwen3.8-omni-flash)](models/alibaba/qwen3.8-omni-flash.md) — SWE-bench Pro: 待核实 — 报告只写 SWE-bench Pro，没有说明对应 V2 2.0.0 / 642-task 默认集；不能映射为本地 swe-bench-pro-v2 定义。; Terminal-Bench: 待核实 — 官方动态排行榜仍需人工/后续复核以确认是否有精确型号的 v4 成绩。; Terminal-Bench-Science: 待核实 — 排行榜未加载完整，尚不能确认该型号是否有公开结果。; AutomationBench: 待核实 — 排行榜其余 119 项未展开，不能将当前页面未显示该型号视为已确认无成绩。; OSWorld: 待核实 — 本地目标为 OSWorld 2.1；官方页面标题为 OSWorld 2.0，未找到该模型的 2.1 成绩。; Artificial Analysis Intelligence Index: 待核实 — 官方指数页和模型发布目录均为动态/部分列表，未找到精确型号不等于确认无成绩。
- [Pareto (unbiased/pareto)](models/unbiased/pareto.md) — DeepSWE: 待核实 — 本地定义要求 pass@1；官方分数表未明确该 metric，且 26.9 是 30-task slice、26.10 denominator 未确认。两条原始分数已保留，但定义映射待复核。; Terminal-Bench-Science: 待核实 — 动态 leaderboard 未加载，尚不能确认是否存在精确 Pareto 版本成绩。; AutomationBench: 待核实 — 榜单其余 119 条当前未展开，无法据此断言完整排行榜中没有 Pareto。; OSWorld: 待核实 — 本地目标定义是 OSWorld v2.1；没有可确认的 v2.1 成绩，不能将 v2.0 或 partial reward 结果映射到该定义。; Artificial Analysis Intelligence Index: 待核实 — AA 页面仅显示部分模型，当前未命中精确型号不足以确认公开榜单中完全没有结果。; GDPval-AA: 待核实 — AA leaderboard 为动态部分列表，需后续复核是否存在未显示的精确型号结果。
- [Arrow 2 (quiverai/arrow-2)](models/quiverai/arrow-2.md) — AutomationBench: 待核实 — 需进一步确认 AutomationBench v1.0.6 完整记录及 Arrow 2 是否曾以该准确模型版本参与测试；当前证据不足以判为未找到或不适用。; OSWorld: 待核实 — 需确认本地 v2.1 对应的官方评测版本以及 Arrow 2 是否符合该测试的 computer-use 接口要求。; Chartography: 待核实 — 现有资料不足以确定该模型能否在 Chartography 协议下返回可评分的图表推理答案，故保留待核实。
- [Arrow 2 Telos (quiverai/arrow-2-telos)](models/quiverai/arrow-2-telos.md) — AutomationBench: 待核实 — 需检查完整榜单记录，并确认该准确型号、版本与测试条件；页面中未显示不构成完整榜单没有成绩的证明。; OSWorld: 待核实 — 需确认 v2.1 对应的正式测试版本以及 Telos 是否曾在匹配的 computer-use harness 中测试。; Chartography: 待核实 — 需确认 Telos 是否能在 Chartography 协议下输出可评分的图表理解答案；当前资料没有精确测试记录。
- [Step 5 Preview (stepfun/step-5-preview)](models/stepfun/step-5-preview.md) — Terminal-Bench: 待核实 — 33.3 行未公布 harness/运行次数，无法判定它与 Vals 31.82 avg@3 结果的差异是否来自测试条件。; AutomationBench: 待核实 — 榜单其余折叠记录及模型卡图片中的成绩无法核验，不能据此判定为未找到。; OSWorld: 待核实 — 未核实到本地目标版本 v2.1 的准确型号成绩。; Chartography: 待核实 — StepFun 官方评测图表无法文本核验；没有可确认的 Chartography 分数或条件。; Humanity's Last Exam: 待核实 — 46.5 的数据集覆盖范围和完整测试条件无法核验，因此未写入 TOML。; Artificial Analysis Intelligence Index: 待核实 — 尚无与本地定义 v5.0 精确匹配且版本明确的成绩。; GDPval-AA: 待核实 — 未将研究中出现的 1566 候选值写入 TOML，因为无法从可读取的官方原始榜单或模型卡文本直接复核准确型号行。
- [Gemini 3.8 Live (google/gemini-3.8-live)](models/google/gemini-3.8-live.md) — Terminal-Bench: 待核实 — 需要从可完整读取的官方动态榜单或其他原始来源核验 Gemini 3.8 Live 是否有 V4 成绩。; Terminal-Bench-Science: 待核实 — 当前官方榜单结果行不可读取，无法判断公告之后是否新增 Gemini 3.8 Live。; AutomationBench: 待核实 — 折叠榜单其余记录不可见，不能断言全榜不存在 Gemini 3.8 Live。; OSWorld: 待核实 — 官方榜单数据行当前不可完整读取，目标型号与 v2.1 的成绩仍待核验。
- [Gemini 3.8 Live Extended Thinking (google/gemini-3.8-live-extended-thinking)](models/google/gemini-3.8-live-extended-thinking.md) — Terminal-Bench: 待核实 — 需从可完整读取的官方动态榜单或其他原始资料核验该型号是否有 V4 成绩。; Terminal-Bench-Science: 待核实 — 无法确认官方发布表之后的动态榜单是否新增该型号。; AutomationBench: 待核实 — 无法核对折叠的 119 项，不能据此断言全榜无此型号。; OSWorld: 待核实 — 榜单数据行不可读取，目标型号在 v2.1 的成绩尚未核验。
- [Kimi K2.8 Preview (moonshotai/kimi-k2.8-preview)](models/moonshotai/kimi-k2.8-preview.md) — Terminal-Bench: 待核实 — The live leaderboard's model rows could not be inspected; score and run conditions remain unverified.; Terminal-Bench-Science: 待核实 — The current live leaderboard's model rows could not be inspected, so absence of an exact Kimi K2.8 Preview result is not established.; AutomationBench: 待核实 — The full v1.0.6 leaderboard entries were not accessible for exact-model verification.; OSWorld: 待核实 — The interactive leaderboard rows could not be fully inspected for the exact Preview version.
- [Fugu Max (sakana/fugu-max)](models/sakana/fugu-max.md) — Terminal-Bench: 待核实 — The current v4 leaderboard's full model rows could not be read; an exact Fugu Max result and its run conditions remain unverified.; Terminal-Bench-Science: 待核实 — The live leaderboard's current result rows could not be inspected; no conclusion about a post-release Fugu Max result is possible.; AutomationBench: 待核实 — The Fugu Max value/configuration in Sakana's figure and the complete Zapier v1.0.6 leaderboard entry remain unverified; no score was recorded.; OSWorld: 待核实 — The interactive leaderboard's model rows remain unavailable for exact Fugu Max verification.; Chartography: 待核实 — The official Fugu Max figure value and evaluation configuration could not be verified; Fugu Ultra v2's 48.3 was not transferred.
- [Fugu Ultra v2 (sakana/fugu-ultra-v2)](models/sakana/fugu-ultra-v2.md) — DeepSWE: 待核实 — The reported 74.3 cannot be confirmed as DeepSWE v1.1 or mapped to its pass@1 metric and test conditions.; Terminal-Bench: 待核实 — The current v4 leaderboard's model rows and any exact Fugu Ultra v2 run conditions remain unverified.; Terminal-Bench-Science: 待核实 — The live leaderboard's current results could not be inspected for a post-release Fugu Ultra v2 score.; AutomationBench: 待核实 — The complete v1.0.6 leaderboard could not be inspected for an exact Fugu Ultra v2 entry.; OSWorld: 待核实 — The interactive leaderboard rows remain unavailable for exact Fugu Ultra v2 verification.; Chartography: 待核实 — It is unverified whether 48.3 uses the target Chartography definition and its accuracy (mean; Pass@1) configuration.; Humanity's Last Exam: 待核实 — The exact HLE(text) score, dataset scope, effort, harness, and relation to the target original dataset remain unverified.
- [DeepSeek V4.1 Flash (deepseek/deepseek-v4.1-flash)](models/deepseek/deepseek-v4.1-flash.md) — DeepSWE: 待核实 — The local definition's pass@1 metric and the official card's resolved metric need an explicit mapping decision; no source metric was rewritten.; Terminal-Bench: 待核实 — The source row's 4.0/pass@1 fields do not exactly match the local definition's 4.0.0/task resolution rate.; Terminal-Bench-Science: 待核实 — The current leaderboard's model rows remain unavailable for exact V4.1 Flash verification.; AutomationBench: 待核实 — The score's AutomationBench version, task set, and metric equivalence to the v1.0.6 held-out leaderboard are unverified.; OSWorld: 待核实 — An exact V4.1 Flash v2.1 result cannot be verified from the current interactive leaderboard.; Humanity's Last Exam: 待核实 — The source metric label and local accuracy metric do not exactly map; the with-tools row's dataset scope and harness are not stated.
- [Ling 3.0 Flash VL (inclusionai/ling-3.0-flash-vl)](models/inclusionai/ling-3.0-flash-vl.md) — DeepSWE: 待核实 — The official leaderboard and dataset lists are incomplete in the accessible page view, so an exact model result cannot be ruled out.; Terminal-Bench: 待核实 — The current v4 leaderboard rows remain unavailable for exact-model verification.; Terminal-Bench-Science: 待核实 — The live leaderboard's current rows could not be inspected for a post-release result.; AutomationBench: 待核实 — The full v1.0.6 leaderboard entries remain unavailable for exact-model verification.; OSWorld: 待核实 — The accessible leaderboard does not expose complete v2.1 rows for exact-model checking.; Humanity's Last Exam: 待核实 — The exact original HLE score, dataset scope, effort, harness, and evaluation date remain unverified.; GDPval-AA: 待核实 — The exact official v2.1 Elo score, effort/configuration, and evaluation date could not be verified.
- [GPT-Live 1 (openai/gpt-live-1)](models/openai/gpt-live-1.md) — Terminal-Bench-Science: 待核实 — 需在动态榜单或其他可访问的官方结果中核实发布后的 exact endpoint 结果。; AutomationBench: 待核实 — 需要访问完整的 1.0.6 榜单数据，确认 exact model/system 名称和测试配置。
- [Mercury 2.5 (inception/mercury-2.5)](models/inception/mercury-2.5.md) — DeepSWE: 待核实 — 官方榜单标注 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 Mercury 2.5；无法确定完整结果中是否存在精确条目。未找到可核实的成绩、指标及 harness。; Terminal-Bench: 待核实 — 官方榜单无法从页面文本读取模型行。Artificial Analysis 方法页说明该评测使用 66 项任务和 mini-swe-agent，但没有可核实的 Mercury 2.5 单项分数。; Terminal-Bench-Science: 待核实 — 官方榜单为动态页面，当前无法读取结果行；Artificial Analysis 页面未提供可确认的 Mercury 2.5 单项结果。; AutomationBench: 待核实 — Zapier 官方榜单确认目标版本 1.0.6，但页面只显示前 10 项并注明另有 119 项。第三方列出的 2.4% 对应 Artificial Analysis AutomationBench-AA（私有 657 项、无 guardrail 违规时目标完成率），与本地定义的 Zapier task_completed_correctly 指标不同，不写入目标 Benchmark。; Humanity's Last Exam: 待核实 — 第三方页面列出 11.8%，但标注 HLE Text-Only，与本地目标定义的原始 2,500 题多模态集不一致。Artificial Analysis 的 Mercury 2.5 页面及 HLE 评测页未显示完整集对应成绩，未写入候选分数。; GDPval-AA: 待核实 — Artificial Analysis 官方结果页未显示可核实的 Mercury 2.5 行；第三方提及的 474 未能核实其分数含义与评测条件，因此不写入。; Vals Index: 待核实 — 官方 v2.2 榜单未显示 Mercury 2.5。较早 Vals Index v2 榜单的 12.95% 不是目标 v2.2 版本，不能转录。
- [MiniCPM5-2B (openbmb/minicpm5-2b)](models/openbmb/minicpm5-2b.md) — DeepSWE: 待核实 — 官方榜单注明 113 个任务，但当前 Best 视图仅显示 21/28 个模型且未见 MiniCPM5-2B；不能据此确认完整榜单中没有发布后结果。; SWE-bench Pro: 待核实 — 模型卡列出 SWE-bench Pro 14.4，但没有注明 V2.0.0、指标或测试条件；Scale V2 榜单没有可核实的对应条目，故不补猜版本或 harness。; Terminal-Bench: 待核实 — 模型卡列出 Terminal-Bench v2.1 8.6，不属于目标 v4.0.0；V4 官方结果行当前无法读取，没有可确认的 V4 成绩。; Terminal-Bench-Science: 待核实 — 模型卡未列该项目；官方动态结果页面无法核验完整结果行，因此不能仅凭当前页面断言未参测。; AutomationBench: 待核实 — Zapier 官方榜单确认 1.0.6，但目前页面只呈现部分结果，未见 MiniCPM5-2B。Artificial Analysis AutomationBench-AA 是不同私有测试配置和指标，不符合本地定义的 task_completed_correctly，未转录。; GDPval-AA: 待核实 — AA 发布文章报告 831 Elo，但明确为旧版 GDPval-AA v2、人类锚点 1000；目标 v2.1 使用 DeepSeek V4.1 Flash (max)=1600 锚点及 Crowd-BT，无法换算。模型卡的 19.6 也没有足够指标/版本信息。; Vals Index: 待核实 — Vals 官方 v2.2 榜单显示的是 Best/Frontier 部分模型列表，未见 MiniCPM5-2B，但页面不是完整名单；当前没有可核实的目标版本成绩。
- [Ling 3.0 Flash Sante (inclusionai/ling-3.0-flash-sante)](models/inclusionai/ling-3.0-flash-sante.md) — DeepSWE: 待核实 — DeepSWE 官方榜单标注 113 项任务，但当前 Best 视图只显示 21/28 个模型且未见 Sante；官方模型卡中的评测图无法读取，不能据此确认完整结果列表没有 Sante。; SWE-bench Pro: 待核实 — Scale V2 榜单当前可读条目中未见 Sante；官方模型卡的评测图无法读取。基础版 Ling 3.0 Flash 的 Pro 成绩不是 Sante，也未证明符合目标 V2 条件，不转用。; Terminal-Bench: 待核实 — 官方 V4 榜单的结果表当前为空，Sante 模型卡中没有可读到的 V4 精确分数和条件。; Terminal-Bench-Science: 待核实 — 官方站点的动态榜单结果行无法读取；模型卡无可核验的对应分数，无法据此断定发布后没有条目。; AutomationBench: 待核实 — Zapier 官方页面确认版本 1.0.6，但当前只显示前 10 项且说明另有 119 项。模型支持 tools，因此不因医疗专业定位判为不适用；完整榜单中是否有 Sante 尚待确认。; Humanity's Last Exam: 待核实 — 官方模型卡列有 HLE with tools，但分数仅显示在无法读取的图片中。第三方复述的 53.2 不是可核验的原始来源数值，未写入。; GDPval-AA: 待核实 — Artificial Analysis 官方页面未能核实 Sante 条目，页面展示结果不完整。第三方百分比是估算值，且不是目标 Elo 指标，不能写入。; Vals Index: 待核实 — Vals 官方 v2.2 页面显示部分领先模型，未见 Sante，但不是完整模型名单，无法据此断言全榜不存在结果。
- [GPT-6 Astra (openai/gpt-6-astra)](models/openai/gpt-6-astra.md) — Artificial Analysis Intelligence Index: 待核实 — 已有五档 version 5.0 index score。当前 Artificial Analysis 方法页显示 v5.0.1，并记有 2026 年 11 月的重评；AA Data API 说明 patch 版本未必体现在 major.minor 字段。无法从公开精度确认本地小数对应的评测快照，暂保留全部记录并待复核版本/精度。; GDPval-AA: 待核实 — 已有五档 v2.1、220 public tasks、Stirrup Elo 记录。当前官方页面按整数显示的 high 档为 1537，而本地高精度记录为 1536.04；页面没有显示足以判断差异原因的精度。保留现有记录并待核实，其他四档显示值与记录四舍五入后吻合。
- [Qwen3.8 Max 0902 (alibaba/qwen3.8-max-0902)](models/alibaba/qwen3.8-max-0902.md) — Terminal-Bench: 待核实 — 来源指标与本地 Terminal-Bench 定义指标 task resolution rate 不同；保留来源原始指标，待核实映射。; Terminal-Bench-Science: 待核实 — 来源指标 share of tasks passed (pass@1) 与本地定义 task resolution rate 不同；保留来源原始指标，待核实映射。; AutomationBench: 待核实 — 候选 50.8% 只有二手转录支持；需取得 Qwen 原始发布表或 Zapier 对应结果及测试条件后再考虑录入。; Chartography: 待核实 — 候选 29.1% 的精确模型快照和评测时间未披露，待复核是否属于 0902。; Artificial Analysis Intelligence Index: 待核实 — 来源版本 v5.0.1 与本地定义版本 5.0 不完全相同；保留来源版本和分数，待确认是否调整 Benchmark 定义映射。; GDPval-AA: 待核实 — 当前 GDPval-AA v2.1 独立榜单未显示该模型；需确认 1668 是否仍是有效的历史成绩或已被修订/撤下。
- [Gemini 3.8 Flash (google/gemini-3.8-flash)](models/google/gemini-3.8-flash.md) — SWE-bench Pro: 待核实 — 源资料使用版本名 V2 和指标 resolve rate；仓库定义要求 2.0.0 与 task resolution rate。保留来源原写法，不强行改写以匹配定义，故映射待复核。; Terminal-Bench: 待核实 — 两个来源的版本写作 4.0，指标分别为 pass@1 与 accuracy；本地定义要求 4.0.0 / task resolution rate。原值保留，精确映射待复核。; Terminal-Bench-Science: 待核实 — 来源指标写作 share of tasks passed (pass@1) 和 accuracy；本地定义 metric 为 task resolution rate。精确映射待复核。; Artificial Analysis Intelligence Index: 待核实 — 来源版本 v5.0.1 与仓库定义 5.0 不一致，保留来源版本并待复核映射。
- [Muse Spark 1.3 (meta/muse-spark-1.3)](models/meta/muse-spark-1.3.md) — Terminal-Bench: 待核实 — 本地定义要求版本 4.0.0 与指标 task resolution rate；来源记录为 4.0 与 pass@1，保留来源字段，暂不计入精确映射覆盖率。; Terminal-Bench-Science: 待核实 — 本地定义指标为 task resolution rate；来源指标为 pass@1，未将其强行改写成定义值，因此不计入精确映射覆盖率。; OSWorld: 待核实 — 来源版本标签为 v2.1，本地定义字段为 osworld-v2.1；保留来源原标签，等待确认本地映射规范。69.6 partial score 也不是本地定义的 binary task completion rate。; Artificial Analysis Intelligence Index: 待核实 — 本地定义版本为 5.0，来源结果为 5.0.1；保留来源版本，不计入版本 5.0 的精确覆盖率。
- [Claude Fable 5.1 (anthropic/claude-fable-5-1)](models/anthropic/claude-fable-5-1.md) — SWE-bench Pro: 待核实 — 来源原文使用版本 V2 和指标 resolve rate；仓库定义是版本 2.0.0、task resolution rate。为保留源字段，TOML 未把版本或指标改写成定义值，因此该条仍待定义映射复核。; Terminal-Bench: 待核实 — 原始来源分别使用 accuracy / resolution rate 和版本 4.0；本地定义要求 task resolution rate、版本 4.0.0。保持来源标签后，相关行未精确映射，需复核定义兼容性。; Terminal-Bench-Science: 待核实 — Anthropic 与 Vals 来源使用 accuracy，版本分别显示 0.1 或 0.1.0；本地定义要求 task resolution rate、版本 0.1.0。未将源指标改写成本地标签，映射需复核。; AutomationBench: 待核实 — Zapier 官方页可核实 fallback 组合分数，但没有找到纯 Fable 5.1 的对应官方排行榜行；22.37% 目前仅有独立镜像交叉核对，待官方来源确认。; OSWorld: 冲突 — Anthropic 后续发布材料把 80.7 partial 标为 OSWorld 2.1；System Card 对同一 80.7 partial / 42.8 strict run 则标为 OSWorld 2.0，并称使用 2026-09-10 任务文件。官方 v2.1 于 2026-09-16 发布，AIB 当前 v2.1 榜单也未列 Fable。版本无法确认，且本地定义仅接受 binary task completion rate。; Chartography: 待核实 — Surge 行与本地 metric 精确匹配；Anthropic 系统卡四条原始指标标为 accuracy，而本地定义要求 accuracy (mean; Pass@1)。未把这些来源标签强行规范化，四条记录的定义映射待复核。; GDPval-AA: 待核实 — 曾见到的 Artificial Analysis 旧缓存快照中，Max、High、Medium、Low 比当前官方榜单各高 1 Elo（Xhigh 相同）。本次记录当前直接可见的官方值，但没有评测日期可用于判断这是榜单修订还是抓取版本差异。
- [Claude Mythos 5.1 (anthropic/claude-mythos-5-1)](models/anthropic/claude-mythos-5-1.md) — Terminal-Bench: 待核实 — 模型专属来源将指标称为 accuracy、版本写为 4.0；本地定义为 task resolution rate、4.0.0。原始值按来源保留，精确映射需复核。; Humanity's Last Exam: 待核实 — 摘要表的合并标签与详细测试对象描述不一致，无法确认是否存在单独的 Mythos 5.1 HLE 成绩；等待更明确的官方说明。
- [Hy4 preview (tencent/hy4-preview)](models/tencent/hy4-preview.md) — DeepSWE: 待核实 — 候选分数 64.3 来自模型卡提取记录，但无法确认它对应目标 v1.1；未录入 TOML。; SWE-bench Pro: 待核实 — 候选分数 65.7 的模型卡提取记录早于 V2 发布，且没有足够证据证明使用 V2 协议；未录入 TOML。; Terminal-Bench: 待核实 — 来源指标为 accuracy，仓库定义指标为 task resolution rate；保留来源原文指标，待核对映射。; Terminal-Bench-Science: 待核实 — 来源指标为 accuracy，仓库定义指标为 task resolution rate；保留来源原文指标，待核对映射。; AutomationBench: 待核实 — 候选 32.1% 仅可从二手转录核对；官方模型卡原图的具体行及评测条件未能独立确认。; GDPval-AA: 待核实 — 官方模型卡所列 GDPval-AA V2 1678 分不能证明属于 v2.1；未录入 TOML。
- [Qwen3.8 Flash Next (alibaba/qwen3.8-flash-next)](models/alibaba/qwen3.8-flash-next.md) — DeepSWE: 待核实 — Confirm whether the provider-reported 58.7 is the benchmark definition’s pass@1 metric; do not infer it from the value alone.; SWE-bench Pro: 待核实 — No source ties the 62.5 result to SWE-bench Pro V2 (2.0.0); no exact-model score was found on the current V2 board.; Terminal-Bench: 待核实 — Version and metric do not exactly match the local definition; keep the raw row and exclude it from exact-match coverage until reviewed.; Humanity's Last Exam: 待核实 — Confirm whether the score refers to the original 2,500-question HLE set used by the local definition, rather than a different subset; metric=score remains distinct from the definition’s accuracy.; GDPval-AA: 待核实 — Resolve the discrepancy between the dated third-party capture/older AA comparison and the current official leaderboard before recording an Elo result.
- [Ling 3.0 Flash Fin (inclusionai/ling-3.0-flash-fin)](models/inclusionai/ling-3.0-flash-fin.md) — Terminal-Bench: 待核实 — Verify mapping to the local version 4.0.0 / task resolution rate definition; retain the explicit source-reported zero in the meantime.; Humanity's Last Exam: 待核实 — Verify the historical 22.6% against the original 2,500-question HLE definition; do not assume it is the original set rather than HLE-Diamond.; GDPval-AA: 待核实 — Confirm whether any historical result belongs to GDPval-AA v2.1; do not transfer the v2 score.
- [Qwen3.8 Flash (alibaba/qwen3.8-flash)](models/alibaba/qwen3.8-flash.md) — DeepSWE: 待核实 — Confirm the provider-reported score metric before mapping to pass@1.; SWE-bench Pro: 待核实 — Confirm whether the 62.5 result used SWE-bench Pro V2 (2.0.0); no exact V2 attribution was found.; Chartography: 待核实 — Review metric-label mapping to the local accuracy (mean; Pass@1) definition.; Humanity's Last Exam: 待核实 — Confirm whether a score on the original 2,500-question HLE set exists; do not substitute the 2,158-question subset.; GDPval-AA: 待核实 — Find a source for the original GDPval-AA v2.1 Elo and exact tested configuration; do not record a normalized third-party score as Elo.
- [GLM-5.3-Flash (zhipuai/glm-5.3-flash)](models/zhipuai/glm-5.3-flash.md) — DeepSWE: 待核实 — 现有行 metric="resolved"，而仓库定义 metric="pass@1"；未找到来源明确说明 63.4 的原始指标，故保留行但不计入定义覆盖。; Terminal-Bench: 待核实 — Vals 页面将该结果列作 accuracy，版本写作 4.0；仓库定义要求 task resolution rate、4.0.0。原始成绩已保留，定义映射待核实。; Terminal-Bench-Science: 待核实 — 来源报告的指标为 pass@1；仓库定义使用 task resolution rate，定义映射待核实。; AutomationBench: 待核实 — Z.ai 对该行未明确标注 pass@1；仓库定义的指标为 task_completed_correctly。保留原始 metric="pass@1"，不擅自转换。
- [Granite 4.2 8B (ibm/granite-4.2-8b)](models/ibm/granite-4.2-8b.md) — Artificial Analysis Intelligence Index: 待核实 — 本地定义 version="5.0"，来源明确为 5.0.1；原始结果已保留，精确定义映射待复核，当前覆盖统计不计入。
- [Apodex 1.1 Mini (apodex/apodex-1.1-mini)](models/apodex/apodex-1.1-mini.md) — Chartography: 待核实 — 尚未确认开放权重 Apodex-1.1-mini 本体是否支持 Chartography 所需的图表图像输入；等待直接模型推理规格或明确评测记录。未新增分数。
- [DeepSeek V4 Flash Vision Exp (deepseek/deepseek-v4-flash-vision-exp)](models/deepseek/deepseek-v4-flash-vision-exp.md) — DeepSWE: 待核实 — 需要来源明确 DeepSWE 59.3 的版本与评分指标，才能映射到 v1.1。; AutomationBench: 待核实 — 需要确认 public 25.7 的评测版本和 metric 是否与本地 v1.0.6 定义相同。; Chartography: 冲突 — 官方模型卡 64.3 与 Surge 11.2 的测试配置差异未说明，不能判断是否是相同评测条件或同一结果的修订。
- [Ornith 1.5 35B A3B (deepreinforce/ornith-1.5-35b-a3b)](models/deepreinforce/ornith-1.5-35b-a3b.md) — DeepSWE: 待核实 — 需要确认 22 分对应 DeepSWE v1.1 及其 pass@1 指标。; SWE-bench Pro: 待核实 — 需确认 59.6 是否来自 SWE-bench Pro V2 默认 642 项配置，以及其 task resolution rate metric。
- [Qwen3.8 27B (alibaba/qwen3.8-27b)](models/alibaba/qwen3.8-27b.md) — DeepSWE: 待核实 — Qwen 卡片未明确该结果的评分 metric；需确认是否为 pass@1。; OSWorld: 待核实 — 需确认 OSWorld-Verified 84.3 使用的具体 release/version 和评测条件。; Humanity's Last Exam: 待核实 — 模型卡未确认 without-tools 条件，也未说明结果对应原始 HLE、HLE-Rolling 还是其它数据子集。
- [GLM-5.3 (zhipuai/glm-5.3)](models/zhipuai/glm-5.3.md) — DeepSWE: 冲突 — Both source results are retained. Their execution conditions are not sufficiently aligned to decide whether the score difference is a revision or a configuration conflict.; The model-card result does not declare a scoring metric; its existing metric field is retained pending source clarification.; Terminal-Bench: 冲突 — The two public results differ (41.9 vs 38.89) and use differently described metrics/configuration. Both are retained without selecting a winner.; The local definition uses task resolution rate, which is not the metric label stated by either source; mapping remains pending.; Terminal-Bench-Science: 冲突 — The two public results differ (9.5 vs 5.71) despite both naming Mini-SWE-agent; evaluation details are not aligned enough to reconcile them.; Both sources use metrics not named by the local task resolution rate definition; mapping remains pending.; AutomationBench: 待核实 — Do not treat the existing row as a verified public/private leaderboard result until its metric and dataset are documented.; Artificial Analysis Intelligence Index: 待核实 — The source uses method version 5.0.1 while the local definition is version 5.0; the raw row is preserved but not mapped.
- [DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813)](models/deepseek/deepseek-v4-pro-0813.md) — DeepSWE: 待核实 — Confirm the model-card score’s benchmark version and metric, and whether the leaderboard’s unqualified V4 Pro row is the 0813 checkpoint.; SWE-bench Pro: 待核实 — Verify whether the 55.4 result is SWE-bench Pro V2 and confirm its metric, harness, and test conditions before adding it.; Terminal-Bench: 待核实 — The local definition uses metric task resolution rate and version 4.0.0. The source labels are retained verbatim, so this raw row is not mapped pending definition reconciliation.; Terminal-Bench-Science: 待核实 — The local definition calls the metric task resolution rate, while the source calls it accuracy. The original source metric is retained and the row remains unmapped.; AutomationBench: 待核实 — Confirm whether this public result is target version 1.0.6 and what scoring metric produced 31.8; it is not treated as the private-set leaderboard result.; Chartography: 待核实 — Confirm whether the Surge DeepSeek V4 Pro (Max) result used the 0813 checkpoint and establish its evaluation conditions.; Artificial Analysis Intelligence Index: 待核实 — The two official pages disagree on the method-version suffix for the same displayed model/score. Confirm the applicable version before closing review.
- [Gemini 3.7 Flash (google/gemini-3.7-flash)](models/google/gemini-3.7-flash.md) — Terminal-Bench: 待核实 — 来源版本 4.0 与本地 4.0.0 的对应关系及 accuracy 到 task resolution rate 的映射尚未确认。; Terminal-Bench-Science: 待核实 — 来源 accuracy 与本地 task resolution rate 的映射尚未确认。; GDPval-AA: 冲突 — 官方对比页给出 1371 与 1392 Elo，且没有可确认的评测日期或最新快照标记；需要后续复核再决定是否记录。
- [Gemini Flash Latest (google/gemini-flash-latest)](models/google/gemini-flash-latest.md) — Terminal-Bench: 待核实 — 来源版本 4.0 与本地 4.0.0 的对应关系及 accuracy 到 task resolution rate 的映射尚未确认。; Terminal-Bench-Science: 待核实 — 来源 accuracy 与本地 task resolution rate 的映射尚未确认。; GDPval-AA: 冲突 — 1371 与 1392 Elo 分别来自官方不同页面；无可确认的评测日期或最新快照标记。
- [Qwen3.8 2.4T A95B (alibaba/qwen3.8-2.4t-a95b)](models/alibaba/qwen3.8-2.4t-a95b.md) — AutomationBench: 待核实 — 需确认 Zapier 折叠的 119 条榜单记录中是否包含 Qwen3.8 2.4T A95B。; GDPval-AA: 冲突 — 需取得能解释 1597、1607、1610 Elo 差异的评测时间戳或固定评测版本，再决定是否可收录。
- [Grok 4.6 (xai/grok-4.6)](models/xai/grok-4.6.md) — AutomationBench: 待核实 — Zapier 榜单折叠的 119 行中是否存在 Grok 4.6 尚无法确认。; GDPval-AA: 待核实 — 当前可访问的 v2.1 榜单无法交叉确认旧比较快照中的 1622 Elo；需找到当前可核验的 Grok 4.6 High 结果或确认旧快照仍适用。
- [MAI-Code-1.1-Flash (microsoft/mai-code-1.1-flash)](models/microsoft/mai-code-1.1-flash.md) — Terminal-Bench: 待核实 — 官方 Terminal-Bench 4.0 榜单通过浏览器读取时未呈现数据行；需在排行榜恢复可见后复查 MAI-Code-1.1-Flash。; AutomationBench: 待核实 — Zapier 榜单折叠的 119 行中是否存在 MAI-Code-1.1-Flash 尚无法确认。; OSWorld: 待核实 — OSWorld v2.1 官方交互榜单未能显示可核对模型行；需要可读的 v2.1 榜单数据继续核验。
- [Nemotron 3.5 Lightning 30B A3B (nvidia/nemotron-3.5-lightning)](models/nvidia/nemotron-3.5-lightning.md) — Terminal-Bench: 待核实 — Terminal-Bench 4.0 榜单当前未呈现可核验的数据行；需在榜单可读时复查是否列出该模型。; AutomationBench: 待核实 — 无法检查排行榜隐藏的 119 项，不能可靠判定该模型是否在榜单中。; Artificial Analysis Intelligence Index: 待核实 — 需确认 AA v5.0.1 与仓库 v5.0 定义的映射关系，以及该分数对应的 checkpoint 精度。; GDPval-AA: 待核实 — 需确认 638 Elo 对应的 checkpoint 精度是否为本模型 BF16。
- [Muse Glimmer 30B (meta/muse-glimmer-30b)](models/meta/muse-glimmer-30b.md) — AutomationBench: 待核实 — 当前无法检查 Zapier 榜单隐藏的 119 项，不能确定是否包含 Muse Glimmer。; OSWorld: 待核实 — 需查明 OSWorld-Verified 65.9 对应的评测版本，或在 v2.1 榜单数据可读时复查。; Artificial Analysis Intelligence Index: 待核实 — 需先确认本地 v5.0 与当前 v5.0.1 的映射规则，并明确应采用哪一版公开结果。
- [Motif 3 (motif-technologies/motif-3)](models/motif-technologies/motif-3.md) — Terminal-Bench: 待核实 — 官方 v4 榜单当前没有可读的成绩行，无法判定公开榜单是否列出 Motif 3。; AutomationBench: 待核实 — 无法检查榜单隐藏的 119 项，不能确定是否包含 Motif 3。
- [GPT-5.6 Cyber (openai/gpt-5.6-cyber)](models/openai/gpt-5.6-cyber.md) — Terminal-Bench: 待核实 — 官方结果页当前没有渲染可读榜单行；需后续重新核对完整 leaderboard。; Terminal-Bench-Science: 待核实 — 官方 Harbor leaderboard 仍显示加载中，公告 leaderboard 以图片展示；需后续核对完整可读结果。; AutomationBench: 待核实 — 官方网页折叠了其余 119 行；需后续核对隐藏榜单条目或官方原始结果。
- [Solar Pro 4 (upstage/solar-pro4)](models/upstage/solar-pro4.md) — SWE-bench Pro: 待核实 — 官方 V2 Full 榜单完整结果行在当前可读页面中不可见；需复查能完整呈现条目的官方结果页。; Terminal-Bench: 冲突 — 官方 AA 历史页为 1%，较新的官方比较页为 0%；缺少测试日期、模型快照或修订说明，需复核后才能确定是否为同条件冲突。; Terminal-Bench-Science: 待核实 — Harbor 官方 leaderboard 未加载出结果，当前无法核实完整榜单。; AutomationBench: 待核实 — Zapier 官方网页折叠 119 行，尚未核对完整榜单中的 Solar Pro 4 条目。; Vals Index: 待核实 — Vals 官方页面只呈现部分最新/头部模型；尚未找到能核对 Solar Pro 4 的完整 v2.2 结果集。
- [Muse Spark 1.2 (meta/muse-spark-1.2)](models/meta/muse-spark-1.2.md) — Terminal-Bench-Science: 待核实 — 需要继续核对 Harbor 官方 v0.1 排行榜是否有 Muse Spark 1.2 的精确成绩。; AutomationBench: 待核实 — Meta 的 public v3 与 Zapier v1.0.6 的版本对应关系及公开结果所用 harness 尚未确认；不得以现有 38.2 替代 v1.0.6 官方私有集成绩。; Humanity's Last Exam: 冲突 — 公开来源对同一 Muse Spark 1.2 HLE 结果报 44% 和 45%，无条件/修订说明；另需区分 AA 的 2,158 text-only 子集与完整 HLE 2,500 题。; GDPval-AA: 冲突 — GDPval-AA v2 的 1615（Meta 2026-09-02）与 1631（AA 2026-08-05）差异无已公布条件或修订解释；目标 v2.1 的 1474 已独立收录，不能由 v2 推导。; Vals Index: 待核实 — 当前公开 v2.2 页面没有 Muse Spark 1.2 精确成绩；需确认该版本是否曾完成评测。
- [Qwen3.8 Max (alibaba/qwen3.8-max)](models/alibaba/qwen3.8-max.md) — SWE-bench Pro: 待核实 — 已有的 67.7 未注明目标 V2.0.0 版本或对应 public/held-out 子集，无法确认与本 Benchmark 定义相同。; Terminal-Bench: 冲突 — AA 的 19% 与 Vals 的 34.34% 相差较大；来源给出的重试和重复次数不同，但不足以解释差值。保留为分开的已核实运行配置，待将来取得可比运行标识后复查。; AutomationBench: 待核实 — 已存在的 27.3 是 600-task public subset，但目标定义是 v1.0.6 held-out private leaderboard；来源未给版本及其与目标任务集的对应关系。; Humanity's Last Exam: 待核实 — 需确认两条 Qwen 卡成绩使用原始 2,500 题 HLE，而非其他 HLE 变体/子集；来源也未明确 metric accuracy。; Vals Index: 待核实 — 未找到带有 v2.2 版本标识且固定为首发 2026-08-03 Qwen3.8 Max 的成绩；模型页 55.30% 没有说明指数版本。
- [DeepSeek V4 Flash 0731 (deepseek/deepseek-v4-flash-0731)](models/deepseek/deepseek-v4-flash-0731.md) — AutomationBench: 待核实 — 需确认 25.1 结果的 AutomationBench 版本及其与 task_completed_correctly 的指标映射；也需确认现有 date 是否代表来源公布的评测日期。; Humanity's Last Exam: 冲突 — Artificial Analysis 来源对 HLE 结果的 37% 与 39% 不一致，尚未查明是否由评测修订或条件差异造成。; GDPval-AA: 冲突 — Artificial Analysis 官方来源的 Elo 数值 1441 与 1433 冲突，待确认有效记录。
- [Inkling Small (thinkingmachines/inkling-small)](models/thinkingmachines/inkling-small.md) — Terminal-Bench: 待核实 — 需核实官方榜单的 Accuracy 是否能按本地定义映射为 task resolution rate；在确认前保留原指标。; Artificial Analysis Intelligence Index: 待核实 — 本地定义版本为 5.0，当前官方型号页版本为 5.0.1；需确认是否更新本地定义或保持版本分开，当前不计入 V5.0 精确覆盖率。
- [Claude Opus 5 (anthropic/claude-opus-5)](models/anthropic/claude-opus-5.md) — SWE-bench Pro: 待核实 — 排行榜指标标签 Pass@1 与本仓库定义的 task resolution rate 不完全一致；覆盖率暂不计入，需核实二者语义映射。; Terminal-Bench: 待核实 — 原始来源指标为 accuracy，本仓库定义为 task resolution rate；保留源标签，暂不计入精确映射覆盖率。; Terminal-Bench-Science: 待核实 — 原始来源指标为 accuracy，本仓库定义为 task resolution rate；保留源标签，暂不计入精确映射覆盖率。; Humanity's Last Exam: 冲突 — Anthropic 两份官方资料对 Opus 5 相同 HLE 工具配置给出不同成绩，尚未说明评测轮次或设置差异；需要核实。
- [Ling 3.0 Flash (inclusionai/ling-3.0-flash)](models/inclusionai/ling-3.0-flash.md) — SWE-bench Pro: 待核实 — 缺少官方 metric 与 benchmark version；此原始记录不与本地 2.0.0 / task resolution rate 定义精确映射，也不能据此确认 V2 成绩。; Humanity's Last Exam: 待核实 — 需要确认 22.7 的原始评测配置和指标；Hugging Face 评测元数据当前存在 task ID mismatch。; GDPval-AA: 待核实 — 未取得可核实的精确 GDPval-AA v2.1 成绩；不采用社区转述的 1107，也不从不可读图表或搜索摘要推断。
- [Gemini 3.5 Flash Lite (google/gemini-3.5-flash-lite)](models/google/gemini-3.5-flash-lite.md) — Humanity's Last Exam: 待核实 — 官方动态排行榜未能直接核对 Gemini 3.5 Flash Lite 的分数行；应在原始排行榜可读时核实二手来源提及的约 18.8% 及其配置。; Artificial Analysis Intelligence Index: 待核实 — 本地定义版本为 5.0，原始资料版本为 5.0.1；确认两者能否按当前定义精确映射后，再将该成绩纳入覆盖率。
- [Gemini 3.6 Flash (google/gemini-3.6-flash)](models/google/gemini-3.6-flash.md) — DeepSWE: 冲突 — 需要确认 49.0 与 47% ±4% 是同一实验的官方修订还是不同轮次；同时核实本地 pass@1 与源记录 resolve rate 的映射。; Terminal-Bench-Science: 待核实 — 本地定义 metric 为 task resolution rate，Vals 原始标签为 accuracy；保持源标签并待核实精确映射。; AutomationBench: 待核实 — Google 模型卡未列 benchmark version/metric/harness，Zapier 完整榜的目标行仍待直接确认。; GDPval-AA: 待核实 — 公开 AA 页面未直接呈现该模型的 v2.1 Elo 行；需要原始提交或可读 leaderboard row。; Vals Index: 待核实 — 当前 v2.2 页面未覆盖该历史模型的行，尚不能确认无结果还是仅未展示。
- [Gemini Flash-Lite Latest (google/gemini-flash-lite-latest)](models/google/gemini-flash-lite-latest.md) — DeepSWE: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; SWE-bench Pro: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; Terminal-Bench: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; Terminal-Bench-Science: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; AutomationBench: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; OSWorld: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; Chartography: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; Humanity's Last Exam: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; Artificial Analysis Intelligence Index: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; GDPval-AA: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。; Vals Index: 待核实 — 需要原始来源明确记录本次评测所使用的不可变 Gemini 型号或证明评测当时该 latest alias 指向的具体版本。
- [Macaron V1 Tall (mindlab/macaron-v1-tall)](models/mindlab/macaron-v1-tall.md) — AutomationBench: 待核实 — 官方文档的 Macaron-V1 31.8 是否对应 Tall，以及它是否与本地私有留出集定义等价，均未明确。; Vals Index: 待核实 — 无法根据当前精选榜单确认 Macaron-V1-Tall 是否曾获得该版本成绩。
- [Macaron V1 Venti (mindlab/macaron-v1-venti)](models/mindlab/macaron-v1-venti.md) — DeepSWE: 待核实 — DeepSWE 58.4 的来源报告未标注数据版本；官方后续表格的 Macaron-V1 列未明确 Venti/Tall，且该分数使用 best-of-up-to-3，而本地定义为 pass@1。; AutomationBench: 待核实 — 31.8 是否属于 Macaron-V1-Venti 未被官方文档明确；公开 600 任务集成绩不能替代本地私有留出集定义。; Vals Index: 待核实 — 无法根据当前精选榜单确认 Macaron-V1-Venti 是否曾获 v2.2 成绩。
- [Laguna S 2.1 (poolside/laguna-s-2.1)](models/poolside/laguna-s-2.1.md) — Vals Index: 待核实 — 无法根据当前精选榜单确认 Laguna S 2.1 是否曾获得 Vals Index v2.2 成绩。
- [Qwen3.8 Max Preview (alibaba/qwen3.8-max-preview)](models/alibaba/qwen3.8-max-preview.md) — DeepSWE: 待核实 — 没有找到直接指向 Preview 端点或检查点的 DeepSWE v1.1 成绩；正式版结果不能据别名迁移反推为 Preview 结果。; SWE-bench Pro: 待核实 — 未找到 Preview 的 SWE-bench Pro V2 结果；GA 资料没有证明 Preview 身份或 V2 数据版本。; AutomationBench: 待核实 — 没有找到明确属于 Preview 且与私有留出集定义对应的 AutomationBench v1.0.6 成绩。; Chartography: 待核实 — 当前 Chartography 条目是否来自 Preview 或正式版检查点不明；未将该条目写入 Preview TOML。; Humanity's Last Exam: 待核实 — 正式版 HLE 成绩不能归属 Preview；没有 Preview 端点或检查点级来源。
- [Kimi K3 (moonshotai/kimi-k3)](models/moonshotai/kimi-k3.md) — DeepSWE: 冲突 — mini-SWE-agent 的 67.3 与当前榜 69% ± 5 的运行/检查点时间差尚无法核实；数据 Schema 也没有置信区间字段。; AutomationBench: 待核实 — 未找到 Kimi K3 在 AutomationBench 1.0.6 held-out/private task set 上的精确成绩。; GDPval-AA: 待核实 — 旧 v2 的 1668 与 1686 Elo 记录差异尚未解释；确认 v2.1 的 Kimi K3 成绩前需保留版本边界。
- [Grok 4.5 (xai/grok-4.5)](models/xai/grok-4.5.md) — DeepSWE: 待核实 — 现有 53% 记录的 metric 与本地定义不一致，且记录日期早于 xAI 官方发布公告；未擅自改写历史记录。; AutomationBench: 待核实 — 没有找到能够直接核实 Grok 4.5 在私有 held-out v1.0.6 任务集上的成绩、effort、harness 或评测日期。; GDPval-AA: 冲突 — 1381 与 1389 的来源快照及测试配置尚未对齐；不选择其一，不写入成绩。
- [Qwen3.7 Flash (alibaba/qwen3.7-flash)](models/alibaba/qwen3.7-flash.md) — AutomationBench: 待核实 — The Zapier page exposes only the first ten rows and collapses 119 more; the complete list was not verified. Artificial Analysis results found for Qwen3.7 Max/Plus are different models.; OSWorld: 待核实 — No exact model score for the V2.1 evaluation was found. The public project page still exposes V2.0 results; Qwen3.7 Plus V2.0 scores are not transferable.
- [Inkling (thinkingmachines/inkling)](models/thinkingmachines/inkling.md) — AutomationBench: 待核实 — The 5% AutomationBench-AA score is not comparable to the target definition’s task_completed_correctly metric; a precise Zapier primary-metric score for Inkling was not verified.; Chartography: 待核实 — The published trial protocol differs between the paper and current README, and the Inkling leaderboard row does not specify its run count.; GDPval-AA: 冲突 — Artificial Analysis’s dedicated V2.1 board reports 1080 while its comparison page reports 1081 for Inkling (Xhigh); no dated revision or condition difference resolves the discrepancy.
- [Muse Spark 1.1 (meta/muse-spark-1.1)](models/meta/muse-spark-1.1.md) — SWE-bench Pro: 待核实 — 本地 61.5 对应 731 项旧套件；尚未找到精确 V2 结果。; Terminal-Bench: 待核实 — 现有 80.0 是 version 2.1；尚未核实 v4.0 成绩。; Terminal-Bench-Science: 待核实 — 当前动态榜单信息不完整，尚不能确认公开成绩是否存在。; AutomationBench: 待核实 — 官方榜单折叠的其余模型无法逐项核对；AA 的 AutomationBench-AA 评分口径不同。; OSWorld: 待核实 — 现有 OSWorld-Verified 结果不是 v2.1；官方 2.1 页面未提供该模型的可读分数行。; Chartography: 待核实 — 榜单没有说明 24.4 对应 accuracy/mean、pass_at_10 还是其他 reducer；不能匹配本地 metric 定义。; Vals Index: 待核实 — 63.18% profile 分数没有显式版本标签；需确认它属于 Vals Index 2.2。
- [GPT-5.6 Luna (openai/gpt-5.6-luna)](models/openai/gpt-5.6-luna.md) — AutomationBench: 待核实 — 未能确认 14.9% 是否来自 AutomationBench v1.0.6 官方私有留出集及其完整测试条件；不写入模型 TOML。; Humanity's Last Exam: 待核实 — 此前研究发现 Max 39% 的候选，但现有比较页目前展示 HLE-Diamond 而非原始 HLE，无法在当前来源页面复核；暂不写入该候选分数。; GDPval-AA: 冲突 — 其他配置存在未解决的不一致：旧 AA 比较结果曾列 Max 1459/1460 及 High 1330/1331，而当前直接榜页仅列 Non-reasoning 928。未确认是否为评测修订或页面/快照差异，故不写入这些候选成绩。
- [GPT-5.6 Sol (openai/gpt-5.6-sol)](models/openai/gpt-5.6-sol.md) — AutomationBench: 待核实 — 未能确认 18.1% 是否来自 AutomationBench v1.0.6 官方私有留出集及其完整测试条件；不写入模型 TOML。; Humanity's Last Exam: 待核实 — 此前研究还发现 Xhigh 47%、High 46%、Medium 42% 与 Low 39% 候选，但当前比较页已改用 HLE-Diamond 或不再显示原始 HLE 行；这些候选暂不写入，需确认原始 HLE 条件。; GDPval-AA: 待核实 — 之前研究中 Xhigh 1569 与 High 1504 的候选分数未能在当前直接比较页或当前 leaderboard 复核；未写入 TOML，等待稳定的官方逐配置来源。
- [GPT-5.6 Terra (openai/gpt-5.6-terra)](models/openai/gpt-5.6-terra.md) — AutomationBench: 待核实 — 未能确认 15.2% 是否来自 AutomationBench v1.0.6 官方私有留出集及其完整测试条件；不写入模型 TOML。; Humanity's Last Exam: 待核实 — 此前研究还发现 High 39%、Low 29% 候选，但当前页面展示的相应分数属于 HLE-Diamond 或未显示原始 HLE；两者不混用，候选暂不写入。; GDPval-AA: 冲突 — Max 配置来源出现 1451 与 1462 两个 Elo 值，且当前 leaderboard 不列该 reasoning 配置；未确认是否为评测修订，故不写入 Max 候选成绩。
- [GPT-Realtime-2.1 (openai/gpt-realtime-2.1)](models/openai/gpt-realtime-2.1.md) — Terminal-Bench: 待核实 — 需要取得可查询的完整 Terminal-Bench 4.0 排行榜数据或原始评测记录后再定。; AutomationBench: 待核实 — 需要检查完整榜单中的其余结果或找到该模型的原始评测记录。; OSWorld: 待核实 — 公开页面未提供可确认其是否参评的完整结果记录。
- [GPT-Realtime-2.1 Mini (openai/gpt-realtime-2.1-mini)](models/openai/gpt-realtime-2.1-mini.md) — Terminal-Bench: 待核实 — 需要可查询的完整 Terminal-Bench 4.0 排行榜数据或该模型的原始评测记录。; AutomationBench: 待核实 — 需要检查完整榜单的折叠结果或找到原始评测记录。; OSWorld: 待核实 — 公开页面没有提供可确认是否参评的完整记录。
- [Hy3 (tencent/hy3)](models/tencent/hy3.md) — DeepSWE: 待核实 — 需找到明确标注 DeepSWE v1.1 与 pass@1 的 Hy3 原始评测记录。; AutomationBench: 待核实 — 需要检查 Zapier 完整榜单或找到 Hy3 在官方 AutomationBench v1.0.6 下的原始结果。; Chartography: 待核实 — 确认榜单条目使用的 Hy3 API/模型版本及视觉输入路径，解决与官方模型卡文本输入能力的冲突。
- [Laguna XS 2.1 (poolside/laguna-xs-2.1)](models/poolside/laguna-xs-2.1.md) — DeepSWE: 待核实 — 需要找到该 Laguna XS 2.1 结果的具体原始运行、来源和 harness，确认其测试条件。; Terminal-Bench: 待核实 — 需要取得可查询的完整 v4 榜单或该模型的原始 v4 评测记录。; Terminal-Bench-Science: 待核实 — 需要完整榜单或直接评测记录以确认是否有公开结果。; AutomationBench: 待核实 — 需要检查 Zapier 完整榜单的折叠项目或找到该模型 v1.0.6 原始运行。
- [Claude Sonnet 5 (anthropic/claude-sonnet-5)](models/anthropic/claude-sonnet-5.md) — Terminal-Bench: 冲突 — AA 14% 与 Anthropic 发布图表 10.3% 均指向 Terminal-Bench 4.0，现有公开资料未能对齐两次评测配置或解释差异。; AutomationBench: 待核实 — 已有 10.65% 的非版本化公开记录，无法可靠映射到 AutomationBench 1.0.6；不写入模型 TOML。; Chartography: 冲突 — 实时榜与论文快照对同名 Adaptive/Max 配置给出不同分数，缺少对应 run 日期/修订关系；不选取其中任一分数写入。; GDPval-AA: 冲突 — 相同 Max 档的官方比较页分数 1464/1449 冲突；需 AA 明确结果更新或评测批次后再录入。
- [Nano Banana 2 Lite (google/gemini-3.1-flash-lite-image)](models/google/gemini-3.1-flash-lite-image.md) — AutomationBench: 待核实 — 需要先核对 API tool capability 元数据，并进一步确认是否有 1.0.6 的准确模型结果。; OSWorld: 待核实 — 适用性依赖未解决的工具调用元数据和 action wrapper；未找到准确成绩。; GDPval-AA: 待核实 — 待解决工具能力元数据矛盾，并确认有无适用的官方 agent 配置或准确成绩。
- [LongCat-2.0 (meituan/longcat-2.0)](models/meituan/longcat-2.0.md) — AutomationBench: 待核实 — 公开榜单未能完整检查，且博客结果无法直接读取；不记录猜测分数。; GDPval-AA: 冲突 — 官方比较页面对相同模型与 GDPval-AA v2.1 给出 870/856 的未解释差异。
- [Ornith 1.0 31B (deepreinforce/ornith-1.0-31b)](models/deepreinforce/ornith-1.0-31b.md) — DeepSWE: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; SWE-bench Pro: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; Terminal-Bench: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; Terminal-Bench-Science: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; AutomationBench: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; OSWorld: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; Chartography: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; Humanity's Last Exam: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; Artificial Analysis Intelligence Index: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; GDPval-AA: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。; Vals Index: 待核实 — 该 31B 精确 checkpoint、可用模型接口及 benchmark 测试身份尚未由官方公开模型卡确认。
- [Ornith 1.0 35B (deepreinforce/ornith-1.0-35b)](models/deepreinforce/ornith-1.0-35b.md) — Terminal-Bench: 待核实 — 该目标版本或完整公开排行榜中的条目仍需后续复核。; AutomationBench: 待核实 — 该目标版本或完整公开排行榜中的条目仍需后续复核。
- [Ornith 1.0 397B (deepreinforce/ornith-1.0-397b)](models/deepreinforce/ornith-1.0-397b.md) — Terminal-Bench: 待核实 — 需要在榜单恢复完整可读取模型行后核实是否有目标版本成绩。; AutomationBench: 待核实 — 需要在榜单恢复完整可读取模型行后核实是否有目标版本成绩。
- [Ornith 1.0 9B (deepreinforce/ornith-1.0-9b)](models/deepreinforce/ornith-1.0-9b.md) — Terminal-Bench: 待核实 — 官方榜单结果行当前不可直接读取；后续可在页面恢复后复核。; AutomationBench: 待核实 — 官方榜单结果行当前不可直接读取；后续可在页面恢复后复核。
- [Seed 2.1 Pro (bytedance-seed/seed-2.1-pro)](models/bytedance-seed/seed-2.1-pro.md) — Terminal-Bench: 待核实 — The current official v4.0 leaderboard response exposes no readable model rows, so an exact v4 result cannot be confirmed.; AutomationBench: 待核实 — The full remaining leaderboard entries were not readable, so absence is not confirmed.; OSWorld: 待核实 — The statement does not identify OSWorld v2.1, the exact Pro API revision, or a reproducible score/configuration.; Humanity's Last Exam: 待核实 — The large official PDF could not be directly parsed in this research pass; HLE dataset/version, tool configuration, exact API revision, and score provenance remain unverified. No score written.
- [Seed 2.1 Turbo (bytedance-seed/seed-2.1-turbo)](models/bytedance-seed/seed-2.1-turbo.md) — Terminal-Bench: 待核实 — The current official v4.0 leaderboard response exposes no readable model rows, so an exact v4 result cannot be confirmed.; AutomationBench: 待核实 — The full remaining leaderboard entries were not readable, so absence is not confirmed.; OSWorld: 待核实 — The statement does not identify OSWorld v2.1, the exact Turbo API revision, or a reproducible score/configuration.; Humanity's Last Exam: 待核实 — The large official PDF could not be directly parsed in this research pass; HLE dataset/version, tool configuration, exact API revision, and score provenance remain unverified. No score written.
- [Seed Character (bytedance-seed/seed-character)](models/bytedance-seed/seed-character.md) — Terminal-Bench: 待核实 — Cannot verify whether a v4.0 score exists for either Seed Character API version; do not transfer Seed2.1 results.; AutomationBench: 待核实 — The complete board could not be inspected, and the repository does not identify which Character API revision is intended.; OSWorld: 待核实 — The local model entry does not identify doubao-seed-character-260628 versus doubao-seed-character-251128, so its tested computer-use capability/version cannot be pinned down.; Chartography: 待核实 — The local model entry omits the API revision; the variants have different image-input capability, so exact eligibility and any result cannot be tied to this entry.
- [Seed Evolving (bytedance-seed/seed-evolving)](models/bytedance-seed/seed-evolving.md) — Terminal-Bench: 待核实 — Cannot confirm whether a v4.0 score exists for a specific Seed Evolving snapshot.; AutomationBench: 待核实 — The full board could not be inspected, and Ark describes this model as a weekly-updated alias without a frozen revision.; OSWorld: 待核实 — No exact score or frozen API revision is published in the checked sources. A Seed2.1 qualitative claim is for a different model and is not transferred.
- [Fugu (sakana/fugu)](models/sakana/fugu.md) — Terminal-Bench: 待核实 — Cannot confirm whether an exact Fugu v4.0 result exists from the current dynamic board response.; AutomationBench: 待核实 — The complete leaderboard is not visible, so absence of a Fugu result cannot be confirmed.
- [Fugu Ultra (sakana/fugu-ultra)](models/sakana/fugu-ultra.md) — DeepSWE: 待核实 — Cannot verify that the 74.3 result is DeepSWE v1.1; no row added.; Terminal-Bench: 待核实 — Cannot confirm whether an exact Fugu Ultra v4.0 result exists from the current dynamic board response.; AutomationBench: 待核实 — The complete leaderboard is not visible, so absence of Fugu Ultra cannot be confirmed.; Chartography: 待核实 — No numeric score or exact effort/harness/test setup was recoverable, and the local model version is not pinned; no score added.; Humanity's Last Exam: 待核实 — Official API docs currently map fugu-ultra to v2.0 and also list v1.0/v1.1. The paper does not name a specific API ID, so the existing result cannot be assigned confidently to the current alias or a frozen release version.
- [GLM-5.2 (zhipuai/glm-5.2)](models/zhipuai/glm-5.2.md) — DeepSWE: 待核实 — Official static materials do not establish that this aggregate pass rate is pass@1 for GLM-5.2; confirm metric equivalence before mapping it to the local definition.; Terminal-Bench: 待核实 — Cannot confirm whether a v4.0 GLM-5.2 result exists from the current dynamic board response.; AutomationBench: 待核实 — Cannot attribute the 26.17% public-set result to AutomationBench v1.0.6 or its official held-out leaderboard. No score row added.
- [Kimi K2.7 Code (moonshotai/kimi-k2.7-code)](models/moonshotai/kimi-k2.7-code.md) — Terminal-Bench: 待核实 — 原始分数可核实；metric 和 version 与本地定义字段不完全相同，需复核映射。; AutomationBench: 待核实 — 官方榜单有折叠条目，当前可读页面不足以确认完整模型列表。; Vals Index: 待核实 — 49.99% 候选值缺少 Vals Index 版本标记，无法确认是否为 v2.2。
- [Kimi K2.7 Code Highspeed (moonshotai/kimi-k2.7-code-highspeed)](models/moonshotai/kimi-k2.7-code-highspeed.md) — AutomationBench: 待核实 — Zapier 官方榜单折叠条目，当前无法确认完整模型列表。
- [DiffusionGemma 26B A4B IT (google/diffusiongemma-26b-a4b-it)](models/google/diffusiongemma-26b-a4b-it.md) — Terminal-Bench: 待核实 — 官方动态榜单需复核，当前无法确认完整结果列表。; AutomationBench: 待核实 — Zapier 榜单的折叠条目无法从当前可读页面核验。; OSWorld: 待核实 — 尚未找到可直接确认的官方 v2.1 模型成绩行。
- [Claude Fable 5 (anthropic/claude-fable-5)](models/anthropic/claude-fable-5.md) — DeepSWE: 待核实 — 来源明确写 aggregate pass rate，但本地定义要求 pass@1；统计口径映射尚未核实。; Terminal-Bench: 待核实 — 不同来源的指标、测试配置和版本标记不完全相同，尚不能精确映射或比较。; Terminal-Bench-Science: 待核实 — Anthropic 自有运行缺少 harness、effort 和试验次数；其 accuracy 口径与本地 task resolution rate 定义尚未精确对应。; AutomationBench: 待核实 — 无法读取 Zapier 完整榜单；17.4% 与 17.1% 均缺少 AutomationBench 1.0.6 的明确版本标记，17.1% 亦未说明 metric。; Humanity's Last Exam: 冲突 — 同一已知工具条件有不同官方分数；缺少 effort、harness 和评测批次说明，需人工复核是否为结果更新或不同配置。
- [Claude Mythos 5 (anthropic/claude-mythos-5)](models/anthropic/claude-mythos-5.md) — DeepSWE: 待核实 — 公开页面显示的模型配置不完整，无法确认精确 Mythos 5 行。; Terminal-Bench: 待核实 — 官方动态榜单无法稳定读取完整行，不能确认 Mythos 5 是否有公开结果。; AutomationBench: 待核实 — 官方榜单剩余条目折叠，无法确认完整模型列表。; OSWorld: 待核实 — 未能从已检查的官方资料确认完整 v2.1 模型结果。
- [North Mini Code (cohere/north-mini-code-1-0)](models/cohere/north-mini-code-1-0.md) — SWE-bench Pro: 待核实 — 本地 40.2 行没有版本，无法确认它是否使用 SWE-bench Pro V2 数据。; AutomationBench: 待核实 — Zapier 官方榜单其余条目折叠，无法确认完整列表。; Artificial Analysis Intelligence Index: 待核实 — 本地 27.6 分数没有 Index 版本，无法与 V5 对齐。; GDPval-AA: 待核实 — 本地 win rate 行的版本和与 v2.1 的关系未说明，指标也不同于本地定义。
- [MiMo-V2.5-Pro-UltraSpeed (xiaomi/mimo-v2.5-pro-ultraspeed)](models/xiaomi/mimo-v2.5-pro-ultraspeed.md) — DeepSWE: 待核实 — 官方榜单未显示完整配置，且 Xiaomi 官方图表文本不可读取。; SWE-bench Pro: 待核实 — Xiaomi 官方性能对比图无法读取，尚不能确认是否含对应的 V2 评测结果。; Terminal-Bench: 待核实 — 官方动态榜单无法读取；可见的 MiMo-V2.5 Terminal-Bench 2.0 成绩不是 v4。; AutomationBench: 待核实 — 官方排行榜其余 119 行不可见；不把 Pro 母版成绩转给 UltraSpeed。; OSWorld: 待核实 — 需确认 UltraSpeed API 对该具体变体开放图像输入；不可仅凭系列能力判不适用。; Chartography: 待核实 — 需确认 UltraSpeed API 是否接受 Chartography 图表图像；不把 Pro 母版成绩转用。; Humanity's Last Exam: 待核实 — 官方性能对比图的内容未能读取，待复核是否包含可归属 UltraSpeed 的 HLE 分数。; GDPval-AA: 待核实 — 仅有母版/Reasoning variant 的公开 Elo；需找到 UltraSpeed 精确条目后才能收录。
- [Nemotron 3 Ultra 550B A55B (nvidia/nemotron-3-ultra-550b-a55b)](models/nvidia/nemotron-3-ultra-550b-a55b.md) — DeepSWE: 待核实 — 榜单可见配置不完整，不能据此确认完整列表无结果。; Terminal-Bench: 待核实 — 官方 Terminal-Bench 4 动态榜单无法读取完整结果。; AutomationBench: 待核实 — Zapier 官方排行榜其余 119 行不可见。; Artificial Analysis Intelligence Index: 待核实 — 需确认本地定义 5.0 是否应接受官方 V5.0.1；本次保留原版本，不修改 benchmark 定义。; Vals Index: 待核实 — 当前 Vals 页为所展示模型列表，未出现不能证明历史上不存在该型号结果。
- [Gemma 4 12B IT (google/gemma-4-12b-it)](models/google/gemma-4-12b-it.md) — DeepSWE: 待核实 — DeepSWE 动态榜单未展示全部配置。; Terminal-Bench: 待核实 — 官方 Terminal-Bench 4 动态榜单当前无法读取完整结果。; AutomationBench: 待核实 — Zapier 排行榜隐藏 119 个条目。; Humanity's Last Exam: 待核实 — 官方表未显式说明 HLE 分数的 metric；本地定义要求 accuracy，暂不做精确映射。
- [Qwen3.7 Plus (alibaba/qwen3.7-plus)](models/alibaba/qwen3.7-plus.md) — DeepSWE: 待核实 — 官方榜单显示 21/28 个型号，完整榜单中是否有该型号仍待核实。; SWE-bench Pro: 待核实 — 精确版本和分数仍需从原始结果表核实。; Terminal-Bench: 待核实 — 未能确认 v4 完整榜单中是否存在该型号。; AutomationBench: 待核实 — 完整榜单中是否含该型号待核实。; OSWorld: 待核实 — 动态结果表未能确认该型号在 v2.1 下的分数。
- [MAI-Code-1-Flash (microsoft/mai-code-1-flash)](models/microsoft/mai-code-1-flash.md) — DeepSWE: 待核实 — 官方榜单不完整，尚不能确认该型号是否有 DeepSWE v1.1 成绩。; SWE-bench Pro: 待核实 — 需要确认此泛称成绩对应的 Pro 数据集版本；不把它作为 SWE-bench Pro V2 结果。; Terminal-Bench: 待核实 — 未能确认 v4 完整榜单中是否有该型号。; AutomationBench: 待核实 — 榜单折叠结果中是否有该型号待核实。
- [Nex-N2-Pro (nex-agi/nex-n2-pro)](models/nex-agi/nex-n2-pro.md) — DeepSWE: 待核实 — 33.6 所属 DeepSWE 版本及其 metric 未注明；官方 v1.1 榜单不完整，不能映射为目标 v1.1。; Terminal-Bench: 待核实 — TB4 动态榜单不可读完整结果，尚不能确认 Nex-N2-Pro 是否有目标成绩。; AutomationBench: 待核实 — 折叠榜单中是否有精确型号待核实。; OSWorld: 待核实 — 缺少可核对的 v2.1 精确型号行及其动作配置。; GDPval-AA: 冲突 — 两个官方 AA 页面数值不一致，缺少可确认的评测修订/条件说明；待 AA 页面统一后再收录。
- [MiniMax-M3 (minimax/MiniMax-M3)](models/minimax/MiniMax-M3.md) — DeepSWE: 待核实 — 需找到明确标注 DeepSWE v1.1 的 MiniMax-M3 成绩，或可核实的对应评测配置。; AutomationBench: 待核实 — 需要可读的完整 AutomationBench 1.0.6 榜单来确认是否存在 M3 条目。; OSWorld: 待核实 — 需确认官方 2.1 评测中 M3 的准确版本、分数及配置。; GDPval-AA: 冲突 — 需 AA 给出 GDPval-AA v2.1 MiniMax-M3 当前 Elo 或带日期的历史结果，以消解页面冲突。
- [Step 3.7 Flash (stepfun/step-3.7-flash)](models/stepfun/step-3.7-flash.md) — DeepSWE: 待核实 — 公开榜单并非完整模型列表。; SWE-bench Pro: 待核实 — 需找到明确标注 Pro V2 的该型号成绩。; Terminal-Bench: 待核实 — 需有该型号 v4 的完整、可核验排行榜行。; AutomationBench: 待核实 — 完整排行榜内容当前不可见。; OSWorld: 待核实 — 动态榜单未能确认该型号 v2.1 结果。
- [Claude Opus 4.8 (anthropic/claude-opus-4-8)](models/anthropic/claude-opus-4-8.md) — DeepSWE: 待核实 — 来源评分术语与本地定义 pass@1 不完全一致，需确认聚合方式。; AutomationBench: 待核实 — Zapier 完整榜单当前不可见。; OSWorld: 待核实 — 现有版本及动态榜单不足以确认 v2.1。; GDPval-AA: 冲突 — 两处公开值相差 1 Elo，尚无法判定为显示/更新差异或评测冲突。
- [Qwen3.7 Max (alibaba/qwen3.7-max)](models/alibaba/qwen3.7-max.md) — DeepSWE: 待核实 — Metric and selected harness are unspecified; cannot map to the local pass@1 definition yet.; SWE-bench Pro: 待核实 — Need exact evidence that the existing generic Pro score used dataset version 2.0.0.; AutomationBench: 待核实 — No verified score for the exact v1.0.6 private leaderboard.
- [Command A Plus (cohere/command-a-plus-05-2026)](models/cohere/command-a-plus-05-2026.md) — DeepSWE: 待核实 — 公开可见列表不完整，无法确认未展示条目是否包含该型号。; SWE-bench Pro: 待核实 — 当前公开榜单展示的型号集合不完整，无法据缺少条目判定未评测。; AutomationBench: 待核实 — 无法查看完整官方榜单以确认目标型号是否已测。; OSWorld: 待核实 — 官方动态页面未能完整确认目标型号是否存在。; GDPval-AA: 冲突 — 公开页面数值不一致，无法判定评测日期或修订关系；未写入单一分数。
- [Gemini 3.5 Flash (google/gemini-3.5-flash)](models/google/gemini-3.5-flash.md) — SWE-bench Pro: 待核实 — 未找到 Gemini 3.5 Flash 精确 V2 结果；Scale 榜单未显示该型号。; AutomationBench: 待核实 — 无法确认该型号是否位于未展开的结果中。; OSWorld: 待核实 — 未找到精确 OSWorld 2.1 原始结果；动态榜单无法完整核对目标型号。; GDPval-AA: 待核实 — 无法确认 1656 的目标版本；AA High 的 1 Elo 差异与 effort 配置未解决。
- [MiniCPM5-1B (openbmb/minicpm5-1b)](models/openbmb/minicpm5-1b.md) — DeepSWE: 待核实 — 榜单可见列表不完整，无法确认未展示型号是否已评测。; SWE-bench Pro: 待核实 — 未能确认是否存在未公开或未展示结果。; AutomationBench: 待核实 — 无法确认该型号是否位于未展开结果中。
- [Grok Build 0.1 (xai/grok-build-0.1)](models/xai/grok-build-0.1.md) — DeepSWE: 待核实 — 当前榜单只显示部分模型，需查完整榜单或可归档的精确型号记录。; SWE-bench Pro: 待核实 — 未核实到目标模型的 V2 结果。; Terminal-Bench: 待核实 — 当前官方可读结果行为空/不可读，未核实精确成绩。; Terminal-Bench-Science: 待核实 — 需要精确模型 ID 的结果；Grok 4.x + Grok Build harness 不匹配。; AutomationBench: 待核实 — 排行榜其余折叠条目尚未逐项核验。; OSWorld: 待核实 — 需要 v2.1 精确型号结果。; Humanity's Last Exam: 待核实 — 38% 的 HLE 子集和模型快照与目标不一致。; Artificial Analysis Intelligence Index: 待核实 — AA 当前页面为 0616 快照，需确认与本地基础 ID 的版本关系。; GDPval-AA: 冲突 — 1065/1066 Elo 冲突及 0616 快照映射未解决。; Vals Index: 待核实 — 当前榜单不完整，缺席不等于未测。
- [Aion-3.0-Mini (aion-labs/aion-3.0-mini)](models/aion-labs/aion-3.0-mini.md) — DeepSWE: 待核实 — 榜单仅显示部分模型，无法确认未展示结果中是否含该型号。; SWE-bench Pro: 待核实 — 缺少完整候选清单，无法确认未展示的评测记录。; Terminal-Bench: 待核实 — 动态榜单数据未能读取，不能据此判断是否已有分数。; Terminal-Bench-Science: 待核实 — 动态结果表未能核实目标型号是否被评测。; AutomationBench: 待核实 — 无法查看完整榜单，目标型号是否出现在折叠部分仍待核实。; OSWorld: 待核实 — 尚未找到能确认 Aion-3.0-Mini 与 OSWorld 2.1 对应关系的公开结果。
- [Perceptron Mk1 (perceptron/perceptron-mk1)](models/perceptron/perceptron-mk1.md) — AutomationBench: 待核实 — 需要核实是否有公开、可复现的 Mk1 适配 harness，以及折叠榜单中是否有精确型号成绩。; OSWorld: 待核实 — 需要核实是否有公开 Mk1 桌面动作 harness及 OSWorld 2.1 精确结果。
- [Gemini 3.1 Flash Lite (google/gemini-3.1-flash-lite)](models/google/gemini-3.1-flash-lite.md) — DeepSWE: 待核实 — 需要核实榜单未展示的配置中是否有精确稳定版 gemini-3.1-flash-lite。; Terminal-Bench: 待核实 — 1% 候选成绩属于 gemini-3.1-flash-lite-preview 还是可映射稳定版尚未证实；来源未给具体评测日期或 effort。; Terminal-Bench-Science: 待核实 — 0% 候选成绩的模型 ID 与本地稳定版不一致；来源未给具体评测日期或 effort。; AutomationBench: 待核实 — 需核实折叠榜单中的精确型号和 AutomationBench 1.0.6 结果。; OSWorld: 待核实 — 需检查其他榜单视图或原始结果数据，确认是否有精确稳定版成绩。; Humanity's Last Exam: 待核实 — 须确认 Google 模型卡成绩对应的精确 API ID；Google 卡片与 AA 候选配置/数值不同，且未公布具体评测日期。; Artificial Analysis Intelligence Index: 待核实 — 需确认 score 6 对应 v5.0.1 且属于稳定版，而非 Preview 版本。; GDPval-AA: 待核实 — 需确认 431 Elo 是否适用于本地稳定模型 ID，并核实版本和测试条件。
- [GPT-Realtime-2 (openai/gpt-realtime-2)](models/openai/gpt-realtime-2.md) — DeepSWE: 待核实 — 需核实榜单未展示配置中是否有精确模型结果。; Terminal-Bench: 待核实 — 需核实完整榜单及其他 harness/effort 配置。; Terminal-Bench-Science: 待核实 — 需核实榜单其余结果中是否有 GPT-Realtime-2。; AutomationBench: 待核实 — 需核实官方榜单折叠行中的精确型号和成绩。; OSWorld: 待核实 — 需检查其他版本/数据集视图或原始结果数据。
- [CoBuddy (baidu/cobuddy)](models/baidu/cobuddy.md) — DeepSWE: 待核实 — 榜单未展示的配置中是否有本地 baidu/cobuddy 对应型号尚未确认；官方 API ID/具体版本也需补证。; Terminal-Bench: 待核实 — 需核实未展示榜单结果中是否存在精确 CoBuddy 型号及分数。; Terminal-Bench-Science: 待核实 — 需核实未展示榜单结果中是否存在精确 CoBuddy 型号及分数。; AutomationBench: 待核实 — 需要可访问完整榜单或原始评测记录确认成绩。; OSWorld: 待核实 — 需要核查其他榜单版本/数据集视图或维护者验证的原始记录。
- [Aion-3.0 (aion-labs/aion-3.0)](models/aion-labs/aion-3.0.md) — DeepSWE: 待核实 — 榜单未展示配置中是否有该精确模型和成绩尚未确认。; Terminal-Bench: 待核实 — 需检查完整榜单或原始结果，确认是否存在精确型号成绩。; Terminal-Bench-Science: 待核实 — 需检查完整榜单或原始结果，确认是否存在精确型号成绩。; AutomationBench: 待核实 — 需要访问完整榜单或公开原始评测记录。; OSWorld: 待核实 — 需要检查其他榜单版本/数据集视图或维护者验证的记录。
- [GPT-5.5 Instant (openai/gpt-5.5-instant)](models/openai/gpt-5.5-instant.md) — DeepSWE: 待核实 — 需核实 GPT-5.5 [xhigh] 是否来自 GPT-5.5 Instant 的特定 snapshot，而非其他 GPT-5.5 版本。; Terminal-Bench: 待核实 — 需检查榜单其余模型/配置，或确认是否有固定 Instant snapshot 成绩。; Terminal-Bench-Science: 待核实 — 需检查榜单其余模型/配置，或确认是否有固定 Instant snapshot 成绩。; AutomationBench: 待核实 — 需确认完整 1.0.6 榜单中是否存在与本地目标版本精确匹配的行。; OSWorld: 待核实 — 需核实是否有固定 GPT-5.5 Instant snapshot 的 OSWorld 2.1 记录及测试配置。; Humanity's Last Exam: 待核实 — 需确认 May 2026 snapshot 与本地模型目标的对应关系；来源未公布 effort 和评测日期。
- [Mistral Medium (latest) (mistral/mistral-medium-latest)](models/mistral/mistral-medium-latest.md) — DeepSWE: 待核实 — 需固定评测时间点所指向的模型版本，并检查未显示榜单配置。; Terminal-Bench: 待核实 — 需核实 AA 评测时 mistral-medium-latest 的目标 checkpoint。; Terminal-Bench-Science: 待核实 — 需核实评测时 alias 的目标 checkpoint。; AutomationBench: 待核实 — 需检查折叠榜单并核验评测时 alias 指向。; OSWorld: 待核实 — 需锁定评测时 alias 目标并检查完整 OSWorld V2.1 榜单。; Humanity's Last Exam: 待核实 — 需核实评测时 alias 的目标 checkpoint。; Artificial Analysis Intelligence Index: 待核实 — 需核实 AA 评测记录使用的模型 ID/checkpoint。; GDPval-AA: 待核实 — 需确认 alias 指向及 GDPval 官方读数差异。
- [Mistral Medium 3.5 (mistral/mistral-medium-2604)](models/mistral/mistral-medium-2604.md) — DeepSWE: 待核实 — 需核查榜单未显示的配置中是否有 Mistral Medium 3.5 精确结果。; AutomationBench: 待核实 — 需检查折叠条目中是否有固定 Mistral Medium 3.5 成绩。; OSWorld: 待核实 — 需确认动态榜单完整行和模型评测配置。; GDPval-AA: 冲突 — 需确认 761 与 769 的差异是否为官方修订或评测条件变化。
- [Mistral Medium 3.5 (mistral/mistral-medium-3-5)](models/mistral/mistral-medium-3-5.md) — DeepSWE: 待核实 — 需核实榜单未展示配置是否有精确型号成绩。; AutomationBench: 待核实 — 需核查完整 Zapier 1.0.6 榜单是否有该精确型号及成绩。; OSWorld: 待核实 — 需核查 OSWorld 2.1 官方其他数据集/版本视图或验证记录。; GDPval-AA: 冲突 — 需核实 AA 是否修订过该 GDPval-AA v2.1 Elo，以及哪个读数对应当前已发布结果。
- [Nemotron 3 Nano Omni 30B A3B Reasoning (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning)](models/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning.md) — DeepSWE: 待核实 — 需检查榜单折叠配置以确认是否有此模型。; Terminal-Bench: 待核实 — 需检查完整 AA 榜单是否有该模型行。; Terminal-Bench-Science: 待核实 — 需检查完整 AA 榜单是否有该模型行。; AutomationBench: 待核实 — 需检查折叠记录。
- [Laguna M.1 (poolside/laguna-m.1)](models/poolside/laguna-m.1.md) — DeepSWE: 待核实 — 需检查未显示的 DeepSWE 配置是否包括此精确模型。; SWE-bench Pro: 待核实 — 需核验完整 V2 榜及版本。; Terminal-Bench: 待核实 — 需核验完整 AA v4 榜单。; Terminal-Bench-Science: 待核实 — 需检查完整榜单。; AutomationBench: 待核实 — 需核查折叠榜单。; OSWorld: 待核实 — 需核实完整行和评测配置。; Humanity's Last Exam: 待核实 — 需查完整榜单或其他精确来源。; Artificial Analysis Intelligence Index: 待核实 — 需核验完整 v5.0.1 指数数据。; GDPval-AA: 待核实 — 需核验完整榜单。; Vals Index: 待核实 — 需检查完整 v2.2 榜单。
- [Laguna XS.2 (poolside/laguna-xs.2)](models/poolside/laguna-xs.2.md) — DeepSWE: 待核实 — 需检查未显示的 DeepSWE 配置是否包括此精确模型。; SWE-bench Pro: 待核实 — 需核验完整 V2 榜及版本。; Terminal-Bench: 待核实 — 需核验完整 AA v4 榜单。; Terminal-Bench-Science: 待核实 — 需检查完整榜单。; AutomationBench: 待核实 — 需核查折叠榜单。; OSWorld: 待核实 — 需核实完整行和评测配置。; Humanity's Last Exam: 待核实 — 需查完整榜单或其他精确来源。; Artificial Analysis Intelligence Index: 待核实 — 需核验完整 v5.0.1 指数数据。; GDPval-AA: 待核实 — 需核验完整榜单。; Vals Index: 待核实 — 需检查完整 v2.2 榜单。
- [Qwen3.6 Flash (alibaba/qwen3.6-flash)](models/alibaba/qwen3.6-flash.md) — DeepSWE: 待核实 — 需检查未展示配置和固定 API 快照。; SWE-bench Pro: 待核实 — 需核验完整 V2 榜及 API 快照。; Terminal-Bench: 待核实 — 需核查完整 AA v4 榜及具体快照。; Terminal-Bench-Science: 待核实 — 需检查完整榜单。; AutomationBench: 待核实 — 需核查完整榜单和快照。; OSWorld: 待核实 — 需核实完整榜单与评测快照。; Chartography: 待核实 — 需核查完整榜单和快照。; Humanity's Last Exam: 待核实 — 需核验完整榜单及 API checkpoint。; Artificial Analysis Intelligence Index: 待核实 — 需核验完整指数数据并固定 API checkpoint。; GDPval-AA: 待核实 — 需核验完整榜单和 API checkpoint。; Vals Index: 待核实 — 需检查完整榜单。
- [DeepSeek V4 Flash (deepseek/deepseek-v4-flash)](models/deepseek/deepseek-v4-flash.md) — DeepSWE: 待核实 — 无法确认榜单通用 API ID 对应本地 2026-04 Preview 的准确权重快照。; SWE-bench Pro: 待核实 — 公开动态榜单未能排除隐藏 Full/Hard 子榜中存在记录；模型对应版本和 Pro V2 结果仍需核实。; Terminal-Bench: 待核实 — 未找到可验证属于本地 Flash Preview 的 v4 结果；当前公开页覆盖不完整。; Terminal-Bench-Science: 待核实 — 未找到标明本地 2026-04 Preview 的 Terminal-Bench-Science 0.1.0 结果。; AutomationBench: 待核实 — 公开榜单折叠记录未能完整逐项核对，无法确认此精确版本是否有记录。; OSWorld: 待核实 — 动态榜单没有可稳定引用的该精确版本行。; Humanity's Last Exam: 待核实 — 成绩来源已确认，但原始题集范围及 Pass@1 与本地 accuracy 定义的映射尚待确认。; Artificial Analysis Intelligence Index: 待核实 — 旧发布分析没有 Index 版本，精确 Flash 页面未能确认 V5 分数。; GDPval-AA: 冲突 — Max 旧报告成绩与 AA v2.1 版本化结果不一致，暂不择值；旧无版本成绩保留。; Vals Index: 待核实 — 页面未能确认本地精确快照，也未完整列出全部候选模型。
- [DeepSeek V4 Pro (deepseek/deepseek-v4-pro)](models/deepseek/deepseek-v4-pro.md) — DeepSWE: 待核实 — 无法确认榜单通用 API ID 对应本地 2026-04 Preview 的准确权重快照。; SWE-bench Pro: 待核实 — 公开动态榜单未能排除隐藏 Full/Hard 子榜中存在记录；模型对应版本和 Pro V2 结果仍需核实。; Terminal-Bench: 待核实 — DeepSeek V4 Pro 11.11% Vals 候选的模型标题、发布日期与本地 Preview 记录存在身份歧义。; Terminal-Bench-Science: 待核实 — 未找到标明本地 2026-04 Preview 的 Terminal-Bench-Science 0.1.0 结果。; AutomationBench: 待核实 — 公开榜单折叠记录未能完整逐项核对，无法确认此精确版本是否有记录。; OSWorld: 待核实 — 动态榜单没有可稳定引用的该精确版本行。; Humanity's Last Exam: 待核实 — 成绩来源已确认，但原始题集范围及 Pass@1 与本地 accuracy 定义的映射尚待确认。; GDPval-AA: 冲突 — Max 旧报告成绩与 AA v2.1 版本化结果不一致，暂不择值；旧无版本成绩保留。; Vals Index: 待核实 — 页面未能确认本地精确快照，也未完整列出全部候选模型。
- [DeepSeek V4 Flash 0423 (deepseek/deepseek-v4-flash-0423)](models/deepseek/deepseek-v4-flash-0423.md) — DeepSWE: 待核实 — 无法确认榜单通用 API ID 对应本地 2026-04 Preview 的准确权重快照。; SWE-bench Pro: 待核实 — 公开动态榜单未能排除隐藏 Full/Hard 子榜中存在记录；模型对应版本和 Pro V2 结果仍需核实。; Terminal-Bench: 待核实 — 未找到可验证属于本地 Flash Preview 的 v4 结果；当前公开页覆盖不完整。; Terminal-Bench-Science: 待核实 — 未找到标明本地 2026-04 Preview 的 Terminal-Bench-Science 0.1.0 结果。; AutomationBench: 待核实 — 公开榜单折叠记录未能完整逐项核对，无法确认此精确版本是否有记录。; OSWorld: 待核实 — 动态榜单没有可稳定引用的该精确版本行。; Humanity's Last Exam: 待核实 — 独立 0423 checkpoint 未确认，无法将通用 Flash 的 HLE 结果归属于此模型 ID。; Artificial Analysis Intelligence Index: 待核实 — 无法确认 Index V5 分数或 0423 独立模型身份。; GDPval-AA: 待核实 — 无法确认本地 0423 是否为独立评测 checkpoint，不能迁移通用 Flash 或 0420 结果。; Vals Index: 待核实 — 页面未能确认本地精确快照，也未完整列出全部候选模型。
- [DeepSeek V4 Pro 0423 (deepseek/deepseek-v4-pro-0423)](models/deepseek/deepseek-v4-pro-0423.md) — DeepSWE: 待核实 — 不能确认当前榜单的通用 deepseek-v4-pro 行属于本地 0423 检查点。; SWE-bench Pro: 待核实 — 公开榜单的动态/筛选内容不完整，且 DeepSeek V4-Pro 官方评测版本未区分 0423。; Terminal-Bench: 待核实 — Vals 11.11% 行与本地 0423 的准确模型/权重快照无法确认。; Terminal-Bench-Science: 待核实 — 未找到独立标注 0423 的 Terminal-Bench-Science 结果。; AutomationBench: 待核实 — 折叠的榜单条目不能逐一确认，且 0423 独立模型身份未证实。; OSWorld: 待核实 — 公开动态页面没有可确认的 0423 行。; Humanity's Last Exam: 待核实 — 官方公告只确认 2026-04-24 的 V4 Pro Preview；本地记录日期为 2026-04-23，独立 checkpoint 与 HLE 归属未确认。; Artificial Analysis Intelligence Index: 待核实 — 本地 0423 与官方 0424 的日期/身份不一致，无法把后者页面状态或旧指数分数归给 0423。; GDPval-AA: 待核实 — 没有确认 0423 独立检查点；不把 0424 或通用 V4 Pro 结果迁移到本地 ID。; Vals Index: 待核实 — 未能从部分榜单确认本地 0423 型号。
- [GPT-5.5 (openai/gpt-5.5)](models/openai/gpt-5.5.md) — DeepSWE: 待核实 — 原始资料未明确该 aggregate pass rate 是否与本地定义的 pass@1 统计口径相同。; SWE-bench Pro: 待核实 — 无法把 OpenAI 未版本化的 SWE-Bench Pro 结果映射为 Pro V2。; Terminal-Bench: 待核实 — 当前公开榜单为动态/部分模型视图，不能据缺席判为无成绩。; Terminal-Bench-Science: 待核实 — 当前榜单为动态视图，无法据页面缺席判定无成绩。; AutomationBench: 待核实 — 后续公告分数与目标基准版本/测试条件未确认，折叠榜单无法完整检查。; OSWorld: 待核实 — v2.1 单独更新了任务快照/评估流程，不能将 Verified 或 v2.0 结果迁移。; GDPval-AA: 待核实 — High/Xhigh 候选值只在旧比较页缓存中出现，尚无可核验的当前原始结果。; Vals Index: 待核实 — 没有确认的 v2.2 成绩；旧版 v2 不能迁移。
- [GPT-5.5 Pro (openai/gpt-5.5-pro)](models/openai/gpt-5.5-pro.md) — DeepSWE: 待核实 — 未找到 GPT-5.5 Pro 的 v1.1 结果。; SWE-bench Pro: 待核实 — 原始发布页无旧版 SWE-Bench Pro 分数，V2 页面未显示该精确型号。; Terminal-Bench: 待核实 — 动态/部分榜单不支持据缺席断言无 v4 分数。; Terminal-Bench-Science: 待核实 — 当前页面为动态榜单，无法确认完整型号覆盖。; AutomationBench: 待核实 — 榜单折叠结果未能完整检查，不能据可见部分判未找到。; OSWorld: 待核实 — OSWorld-Verified 的缺失不等于 v2.1 已检查无成绩。; GDPval-AA: 待核实 — 没有可直接核实的 GPT-5.5 Pro v2.1 Elo。; Vals Index: 待核实 — 未找到能确认的 v2.2 Pro 结果；当前榜单展示不完整。
- [Qwen3.6 27B (alibaba/qwen3.6-27b)](models/alibaba/qwen3.6-27b.md) — DeepSWE: 待核实 — 未确认该精确模型是否在完整榜单的其他配置或折叠项中有结果。; SWE-bench Pro: 待核实 — 没有确认 Qwen 53.5 对应的任务集是否为 V2 默认 642 项，故不写入目标成绩。; Terminal-Bench: 待核实 — 未确认完整 Terminal-Bench 4 榜单中是否存在精确型号结果。; Terminal-Bench-Science: 待核实 — 未确认完整榜单中是否存在精确型号结果。; AutomationBench: 待核实 — 当前可见榜单不完整，未能确认精确型号的 1.0.6 成绩。; OSWorld: 待核实 — 未找到可确认的 OSWorld v2.1 精确结果；当前官方榜单标为 2.0。; Chartography: 待核实 — 未确认动态榜单中是否有未显示的精确型号结果。; Vals Index: 待核实 — 没有确认的 v2.2 精确结果；需完整榜单或原始评测报告核实。
- [MiMo-V2.5 (xiaomi/mimo-v2.5)](models/xiaomi/mimo-v2.5.md) — DeepSWE: 待核实 — 论文未将这一聚合 task success rate 明确写成 pass@1；harness 和评测日期未说明。; SWE-bench Pro: 待核实 — 未核实到精确 SWE-bench Pro V2 结果；动态榜单可见条目有限，不能据缺席断言未找到。; Terminal-Bench: 待核实 — 未核实到版本 4.0 的精确成绩；动态榜单未显示不能证明没有成绩。; Terminal-Bench-Science: 待核实 — 榜单是动态/有限显示，不能据缺席断言未找到。; AutomationBench: 待核实 — 未取得可读且能核实精确型号的官方结果行。; OSWorld: 待核实 — 动态结果页未列出精确型号；缺席不能作为未找到结论。; Chartography: 待核实 — 未获得可核实的精确成绩。; Humanity's Last Exam: 待核实 — 该记录 metric=pass@1，与本地完整 HLE 定义 metric=accuracy 不同，因此原始分数保留但不计 HLE 覆盖。; GDPval-AA: 待核实 — 缺少当前可见或可归档快照来独立复核 996 及其运行条件；未填写评测日期。; Vals Index: 待核实 — 没有可核验的精确 v2.2 数值；动态页面缺席不作为未找到。
- [MiMo-V2.5-Pro (xiaomi/mimo-v2.5-pro)](models/xiaomi/mimo-v2.5-pro.md) — DeepSWE: 待核实 — 原始分数可确认，但缺少足够证据把本地 score 标签更正成 pass@1，并且 Datacurve 区间无法由当前记录表达。; SWE-bench Pro: 待核实 — 未核实到精确 SWE-bench Pro V2 成绩；Scale 动态榜单缺少可确认条目，不据此断言未找到。; Terminal-Bench: 冲突 — 小米来源未公开 1.5 的 Harness、采样次数和完整配置；无法判定与 Vals 的 0.51 是配置差异还是记录冲突。; Terminal-Bench-Science: 待核实 — 动态榜单显示范围有限，不能据缺席断言未找到。; AutomationBench: 待核实 — 本地 metric=score，与本仓 task_completed_correctly 不一致；缺失评测条件不能补猜。; OSWorld: 待核实 — 未取得该版本可核实结果；动态榜单缺席不足以判未找到。; Humanity's Last Exam: 待核实 — AA 页面是旧版 HLE 评测上下文；小米卡没有提供完整 HLE 子集、工具及评测设置，不能作同配置冲突判断。; GDPval-AA: 冲突 — 三个来源未给出可对齐的运行快照/评测日期；需查找 1121 的历史页面快照，再判断 1107、1121 与 1129 是修订还是配置差异。; Vals Index: 待核实 — 没有核实到精确型号 v2.2 指数值；榜单缺席不作为未找到。
- [Deep Research Max Preview (google/deep-research-max-preview-04-2026)](models/google/deep-research-max-preview-04-2026.md) — AutomationBench: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; OSWorld: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Chartography: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Humanity's Last Exam: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Artificial Analysis Intelligence Index: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; GDPval-AA: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Vals Index: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。
- [Gemini Deep Research Preview (google/deep-research-preview-04-2026)](models/google/deep-research-preview-04-2026.md) — AutomationBench: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; OSWorld: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Chartography: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Humanity's Last Exam: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Artificial Analysis Intelligence Index: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; GDPval-AA: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。; Vals Index: 待核实 — 未找到足以确认目标成绩或匹配评测配置的来源。
- [GPT-5.4 Image 2 (openai/gpt-5.4-image-2)](models/openai/gpt-5.4-image-2.md) — Chartography: 待核实 — 精确 provider composite 的身份或目标版本成绩缺少可核验来源。; Humanity's Last Exam: 待核实 — 精确 provider composite 的身份或目标版本成绩缺少可核验来源。; Artificial Analysis Intelligence Index: 待核实 — 精确 provider composite 的身份或目标版本成绩缺少可核验来源。; GDPval-AA: 待核实 — 精确 provider composite 的身份或目标版本成绩缺少可核验来源。; Vals Index: 待核实 — 精确 provider composite 的身份或目标版本成绩缺少可核验来源。
- [Qwen3.6 Max Preview (alibaba/qwen3.6-max-preview)](models/alibaba/qwen3.6-max-preview.md) — DeepSWE: 待核实 — 检查了官方发布文和 DeepSWE 当前榜单，但未能从可见资料确认该型号的 DeepSWE v1.1 精确成绩。榜单公开视图只显示部分模型，不能将缺席视作未找到。; SWE-bench Pro: 待核实 — Qwen 发布文提及 SWE-bench Pro，但未标 V2；该发布文早于 2026-09-22 的 Pro V2 刷新版。目标版本与分数尚不能确认。; Terminal-Bench: 待核实 — Qwen 发布文提及 Terminal-Bench 2.0 与相对提升，没有目标绝对分数；版本 2.0 不能映射为 4.0。; Terminal-Bench-Science: 待核实 — 已检查官方发布资料和 Terminal-Bench Science 基准页，未核实该精确型号的 v0.1 成绩；动态页面未列出不构成未找到。; AutomationBench: 待核实 — 精确型号文档确认支持 function calling，任务类型适用；未确认该模型的 AutomationBench 1.0.6 成绩。榜单只展示部分条目，缺席不能判未找到。; Humanity's Last Exam: 待核实 — 官方发布页正文没有列出可读的 HLE 目标成绩；成绩图在文本视图中不可读取，未从不可读图像推定数值。; GDPval-AA: 待核实 — 旧 AA 比较页列的是 GDPval-AA v2，不是 v2.1；当前官方页面可见内容不足以确认该型号的 v2.1 分数。; Vals Index: 待核实 — Vals 当前 V2.2 榜单显示最新、top 和 frontier 模型；未显示该型号不能据此断言未找到。
- [Kimi K2.6 (moonshotai/kimi-k2.6)](models/moonshotai/kimi-k2.6.md) — DeepSWE: 待核实 — DeepSWE leaderboard view is partial; no directly verifiable Kimi K2.6 v1.1 row was established.; SWE-bench Pro: 待核实 — Kimi materials show an unversioned SWE-Bench Pro result of 58.6 under a SWE-agent-derived harness; the local 27.3 row is hard-aa/Claude Code. Neither is identified as Pro V2, which was released later.; Terminal-Bench: 待核实 — Kimi materials show Terminal-Bench 2.0 at 66.7 with Terminus-2; the local 64.3 row is version 2.1/Claude Code. Neither maps to target version 4.0.; Terminal-Bench-Science: 待核实 — No exact Kimi K2.6 Terminal-Bench Science v0.1 result was verified; a dynamic leaderboard absence alone is insufficient to mark not found.; AutomationBench: 待核实 — Official API supports tool calling and the task type is applicable, but no exact AutomationBench 1.0.6 result was verified. The leaderboard shows only partial entries.; OSWorld: 待核实 — Kimi materials report OSWorld-Verified, which is not OSWorld 2.1. No target-version score was verified.; Chartography: 待核实 — 需确认 Surge 当前排行榜的 12.2% 对应 accuracy/mean (Pass@1) 还是其他 reducer。; GDPval-AA: 待核实 — The April article reports Elo 1520 without a V2.1 label. A search cache showed 1038 on a current comparison but the opened page did not show that row; neither value meets direct verification.; Vals Index: 待核实 — Current V2.2 page only exposes latest/top/frontier models. Kimi aggregate 56.68% is not version-labeled; older V2 page 43.47% and release post 63.9% have unclear version or page scope. None is mapped to V2.2.
- [Hy3 preview (tencent/hy3-preview)](models/tencent/hy3-preview.md) — DeepSWE: 待核实 — Official preview materials do not list an exact DeepSWE v1.1 score; the public leaderboard view is partial.; SWE-bench Pro: 待核实 — The model card contains older or differently named coding results, not a directly confirmed SWE-bench Pro V2 score.; Terminal-Bench: 待核实 — The model card reports Terminal-Bench 2.0 = 54.4 without full metric/harness details; this is not version 4.0.; Terminal-Bench-Science: 待核实 — No exact Hy3-preview Terminal-Bench Science v0.1 result was verified.; AutomationBench: 待核实 — The text model supports agent workflows, but Zapier leaderboard shows only a partial set of entries; no exact score was verified.; Humanity's Last Exam: 待核实 — HF evaluation widget on the exact Hy3-preview model card shows `cais/hle` and `30*`. The card does not explain the metric, subset, conditions, or asterisk; the raw value is retained without metric and is not counted as a mapping.; GDPval-AA: 待核实 — No Hy3-preview row was verified on the current V2.1 page. The dynamic page may omit older models, so status remains pending.; Vals Index: 待核实 — Current V2.2 page displays selected latest/top/frontier models; absence of Hy3-preview is not conclusive.
- [Qwen3.6 35B-A3B (alibaba/qwen3.6-35b-a3b)](models/alibaba/qwen3.6-35b-a3b.md) — DeepSWE: 待核实 — No exact model score for DeepSWE v1.1 was verified; the public leaderboard view is partial.; SWE-bench Pro: 待核实 — Official model materials mention unversioned SWE-bench Pro, which predates/does not identify the V2 refresh; it is not mapped to Pro V2.; Terminal-Bench: 待核实 — Official model materials mention Terminal-Bench 2.0; it is not target version 4.0.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science v0.1 score was verified.; AutomationBench: 待核实 — Model supports tools and has a relevant task type; the visible official leaderboard subset does not establish this exact model’s score.; OSWorld: 待核实 — The model accepts images and supports agentic use, so the benchmark is applicable; the current OSWorld page did not provide a readable exact-model score.; Humanity's Last Exam: 待核实 — Qwen official model-card table lists the exact Qwen3.6-35B-A3B column and HLE score 21.4. The table does not specify metric, subset, test condition, or evaluation date; retain the raw row without filling those fields and keep mapping under review.; Vals Index: 待核实 — The current V2.2 leaderboard does not show this exact model; its selection of latest/top/frontier models is not exhaustive, so status remains pending.
- [Grok 4.3 (xai/grok-4.3)](models/xai/grok-4.3.md) — DeepSWE: 待核实 — No exact Grok 4.3 DeepSWE v1.1 score was verified; current public leaderboard displays only part of the model/configuration set.; SWE-bench Pro: 待核实 — No directly verifiable Grok 4.3 SWE-bench Pro V2 score was found. Do not map other Grok versions or unspecified Pro variants.; Terminal-Bench: 待核实 — No directly verifiable Grok 4.3 Terminal-Bench 4 score was found; nearby versions/configurations do not establish v4.0.; Terminal-Bench-Science: 待核实 — No exact Grok 4.3 Terminal-Bench Science v0.1 score was verified.; AutomationBench: 待核实 — Exact model supports function calling and the task is applicable. The visible leaderboard subset does not verify a Grok 4.3 score.; OSWorld: 待核实 — Exact model supports image input and tools, so the task is applicable; the current OSWorld page did not show a readable exact-model V2.1 row.; Chartography: 待核实 — Surge directly lists Grok 4.3 (High reasoning) at 12.9%. The leaderboard row does not specify which reducer is shown. The official harness reports accuracy/mean and Pass@10 (among other reducers), so the raw score is preserved without metric and is not counted toward mapped coverage. No evaluation date or semantic version is published.; Humanity's Last Exam: 待核实 — Reviewed the exact-model profile, release article and HLE page; no exact Grok 4.3 raw HLE result was verified. HLE-Diamond under AA Index V5 is a different dataset from original HLE.; GDPval-AA: 待核实 — Local TOML has a generic GDPval-AA Elo 1500 row from the April release article; it is not version-labeled V2.1. The current V2.1 page has no direct Grok 4.3 row. A search-index candidate was not visible in the opened primary page, so it is not added or treated as a verified conflict. Existing date equals article publication date; the source does not establish that it is the evaluation date, so this legacy field is flagged for later review and retained unchanged.; Vals Index: 待核实 — Current V2.2 board displays a selected latest/top/frontier set and does not verify Grok 4.3. Older Vals v2, v1.1, and v1 results are not mapped to V2.2.
- [Claude Opus 4.7 (anthropic/claude-opus-4-7)](models/anthropic/claude-opus-4-7.md) — DeepSWE: 待核实 — Current visible v1.1 board does not expose an exact Opus 4.7 row. A previous snapshot reports 54% ± 5% (max, mini-swe-agent) before v1.1 and cannot be mapped to the target revision.; SWE-bench Pro: 待核实 — Local records include 64.3 resolve rate without a V2 tag and 44.9 pass@1 on hard-aa; the system card’s SWE-Bench Pro result is also not labeled V2. The V2 refresh uses 642 tasks and cannot be inferred from these rows.; Terminal-Bench: 待核实 — Local rows are Terminal-Bench 2.1 under multiple harnesses. The system card reports Terminal-Bench 2.0 at 69.4; none is version 4.0.; Terminal-Bench-Science: 待核实 — No exact Opus 4.7 Terminal-Bench Science v0.1 result was verified. The current visible board does not establish that no result exists.; AutomationBench: 待核实 — Model is capable of multimodal tool/agent work, but the public leaderboard displays only 10 entries and folds another 119; no exact score was verified.; OSWorld: 待核实 — The system card/local record includes OSWorld-Verified 78.0 and an OSWorld 2.0 page reports 18.2; neither is OSWorld 2.1. No v2.1 score was verified.; Chartography: 待核实 — Leaderboard directly lists Claude Opus 4.7 (Adaptive/Max) at 16.5%. The page row does not identify the reducer; the harness allows accuracy/mean and Pass@10, so raw score is retained without metric and excluded from mapped coverage. The official README specifies 100 tasks, 10 runs/task, Gemini 3.5 Flash judge. No eval date/semantic version is published.; GDPval-AA: 待核实 — AA article reports 1,753 Elo for Opus 4.7 Adaptive Reasoning/Max Effort but does not label the benchmark version. V2.1 changed the Elo anchor and fitting, so this cannot be mapped to V2.1.; Vals Index: 待核实 — The V2.2 page shows a selected latest/top/frontier list and no visible Opus 4.7 row. Older V1 72.21%, V1.1 66.10%, and V2 56.11% are not mapped to V2.2.
- [Gemini Robotics-ER 1.6 Preview (google/gemini-robotics-er-1.6-preview)](models/google/gemini-robotics-er-1.6-preview.md) — DeepSWE: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; SWE-bench Pro: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; Terminal-Bench: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; Terminal-Bench-Science: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; AutomationBench: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; OSWorld: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; Humanity's Last Exam: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; Artificial Analysis Intelligence Index: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; GDPval-AA: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。; Vals Index: 待核实 — 未找到可直接核实的精确成绩；需要继续检查完整榜单、技术报告或后续公开资料。
- [GLM-5.1 (zhipuai/glm-5.1)](models/zhipuai/glm-5.1.md) — SWE-bench Pro: 待核实 — An exact GLM-5.1 score for the 642-task SWE-bench Pro V2 suite remains unverified.; Terminal-Bench-Science: 待核实 — No exact score confirmed; the public science leaderboard is dynamic and its visible material may be incomplete.; AutomationBench: 待核实 — The AA variant’s 20% is not mapped to AutomationBench v1.0.6; the exact official result remains unverified.; Humanity's Last Exam: 待核实 — The model card does not state scoring metric, exact HLE subset, evaluation conditions, or run date for its two HLE values.; Vals Index: 待核实 — Exact version mapping for the profile’s 56.33% remains unverified; no v2.2 score was added.
- [Qwen3.6 Plus (alibaba/qwen3.6-plus)](models/alibaba/qwen3.6-plus.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for this snapshot was verified.; SWE-bench Pro: 待核实 — No exact Qwen3.6 Plus score on SWE-bench Pro V2 was verified.; Terminal-Bench: 待核实 — Only a Terminal-Bench 2.0 result is reported in the release material; no v4 score was verified.; Terminal-Bench-Science: 待核实 — No exact score was verified; the public leaderboard is dynamic and incomplete.; AutomationBench: 待核实 — A folded leaderboard prevents confirming whether this exact model has a public result.; OSWorld: 待核实 — No exact OSWorld 2.1 score was verified.; GDPval-AA: 冲突 — The 989 vs 990 Elo difference remains unresolved; a direct, dated leaderboard entry is needed before writing a score.; Vals Index: 待核实 — Version mapping for the profile’s 52.13% remains unverified; no v2.2 score was added.
- [Step 3.5 Flash 2603 (stepfun/step-3.5-flash-2603)](models/stepfun/step-3.5-flash-2603.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for Step 3.5 Flash 2603 was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result for this snapshot was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench-Science 0.1.0 result was verified.; AutomationBench: 待核实 — No exact AutomationBench v1.0.6 score or configuration was verified.; Vals Index: 待核实 — No exact Vals Index v2.2 score for Step 3.5 Flash 2603 was verified.
- [Trinity Large Thinking (arcee-ai/trinity-large-thinking)](models/arcee-ai/trinity-large-thinking.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for Trinity Large Thinking was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench-Science 0.1.0 result was verified.; AutomationBench: 待核实 — Verify whether Trinity Large Thinking has a Zapier AutomationBench v1.0.6 task_completed_correctly score.; Vals Index: 待核实 — No exact Vals Index v2.2 score was verified.
- [GLM-5V-Turbo (zhipuai/glm-5v-turbo)](models/zhipuai/glm-5v-turbo.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 result was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench-Science 0.1.0 result was verified.; AutomationBench: 待核实 — No exact Zapier AutomationBench v1.0.6 result was verified.; OSWorld: 待核实 — The OSWorld release/configuration for the 62.3 result is unknown; no v2.1 score was verified.; Humanity's Last Exam: 待核实 — Verify whether the unconfirmed third-party 17.1% HLE candidate corresponds to this exact model and protocol.; GDPval-AA: 待核实 — No exact GDPval-AA v2.1 result was verified.; Vals Index: 待核实 — No exact Vals Index v2.2 result was verified.
- [Gemma 4 26B A4B IT (google/gemma-4-26b-a4b-it)](models/google/gemma-4-26b-a4b-it.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for Gemma 4 26B A4B IT was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science 0.1.0 result was verified.; AutomationBench: 待核实 — No exact Zapier AutomationBench v1.0.6 task_completed_correctly result was verified.; OSWorld: 待核实 — No exact OSWorld v2.1 result was verified.; GDPval-AA: 待核实 — No exact GDPval-AA v2.1 score was directly verified.; Vals Index: 待核实 — No exact Vals Index v2.2 result was verified.
- [Gemma 4 31B IT (google/gemma-4-31b-it)](models/google/gemma-4-31b-it.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for this model was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science 0.1.0 result was verified.; AutomationBench: 待核实 — No exact AutomationBench v1.0.6 task_completed_correctly result was verified.; OSWorld: 待核实 — No exact OSWorld v2.1 result was verified.; GDPval-AA: 待核实 — No exact GDPval-AA v2.1 score was directly verified.; Vals Index: 待核实 — No exact Vals Index v2.2 score for Gemma 4 31B IT was verified.
- [Gemma 4 E2B IT (google/gemma-4-E2B-it)](models/google/gemma-4-E2B-it.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for this model was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science 0.1.0 result was verified.; AutomationBench: 待核实 — No exact AutomationBench v1.0.6 task_completed_correctly result was verified.; OSWorld: 待核实 — No exact OSWorld v2.1 result was verified.; GDPval-AA: 待核实 — No exact GDPval-AA v2.1 score was directly verified.; Vals Index: 待核实 — No exact Vals Index v2.2 result was verified.
- [Gemma 4 E4B IT (google/gemma-4-E4B-it)](models/google/gemma-4-E4B-it.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for this model was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 result was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 result was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science 0.1.0 result was verified.; AutomationBench: 待核实 — No exact AutomationBench v1.0.6 task_completed_correctly result was verified.; OSWorld: 待核实 — No exact OSWorld v2.1 result was verified.; GDPval-AA: 待核实 — No exact GDPval-AA v2.1 score was directly verified.; Vals Index: 待核实 — No exact Vals Index v2.2 result was verified.
- [Mercury Edit 2 (inception/mercury-edit-2)](models/inception/mercury-edit-2.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 score was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 score was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science 0.1.0 score was verified.
- [Gemini 3.1 Flash Live Preview (google/gemini-3.1-flash-live-preview)](models/google/gemini-3.1-flash-live-preview.md) — DeepSWE: 待核实 — No exact DeepSWE v1.1 score for this model was verified.; SWE-bench Pro: 待核实 — No exact SWE-bench Pro V2 score was verified.; Terminal-Bench: 待核实 — No exact Terminal-Bench 4.0 score was verified.; Terminal-Bench-Science: 待核实 — No exact Terminal-Bench Science 0.1.0 score was verified.; AutomationBench: 待核实 — No exact AutomationBench v1.0.6 result was verified.; OSWorld: 待核实 — No exact OSWorld v2.1 result for this model was verified.; Humanity's Last Exam: 待核实 — No exact original HLE result was verified.; Artificial Analysis Intelligence Index: 待核实 — No exact Artificial Analysis Intelligence Index V5 score was verified.; GDPval-AA: 待核实 — No exact GDPval-AA v2.1 score was verified.; Vals Index: 待核实 — No exact Vals Index v2.2 score was verified.
- [Nemotron Cascade 2 30B A3B (nvidia/nemotron-cascade-2-30b-a3b)](models/nvidia/nemotron-cascade-2-30b-a3b.md) — DeepSWE: 待核实 — 已检查目标榜单，但未确认此精确模型的 v1.1 记录；其他 SWE 任务成绩不可替代。; SWE-bench Pro: 待核实 — 已检查目标数据集/排行榜资料，但现有可见成绩未能核实为该模型的 Pro V2 评测；不沿用 SWE-bench Verified 成绩。; Terminal-Bench: 待核实 — 模型资料中出现的 Terminal-Bench 2.0 成绩不属于 V4，未映射为目标成绩；仍需核实 V4 榜单。; Terminal-Bench-Science: 待核实 — 未确认准确型号的 Science v0.1 成绩；未从 Terminal-Bench 通用版推断。; AutomationBench: 待核实 — 未能确认该精确型号在 v1.0.6 榜单中的成绩；保留复核状态。; GDPval-AA: 待核实 — 当前榜单展示不完整，未在可读内容中核实该精确模型的 Elo；不能据未显示断言未参测。; Vals Index: 待核实 — 当前公开榜单仅展示各实验室最佳模型，不能据此确认或否定该精确型号成绩。
- [MiniMax-M2.7 (minimax/MiniMax-M2.7)](models/minimax/MiniMax-M2.7.md) — DeepSWE: 待核实 — 需在完整 v1.1 配置/原始数据中确认 exact model ID。; SWE-bench Pro: 待核实 — 需确认精确型号是否在 Pro V2 的完整结果中。; Terminal-Bench: 待核实 — 当前可见资料未确认 M2.7 的 Terminal-Bench 4.0 结果。; Terminal-Bench-Science: 待核实 — 需复核完整榜单中的 exact model ID。; AutomationBench: 待核实 — 需检查折叠的剩余模型结果。; GDPval-AA: 冲突 — 1494/1495 数值不一致；公开来源未说明其是否为 v2.1，未录入成绩。; Vals Index: 待核实 — 未确认 M2.7 在 v2.2 方法下的独立结果。
- [MiniMax-M2.7-highspeed (minimax/MiniMax-M2.7-highspeed)](models/minimax/MiniMax-M2.7-highspeed.md) — DeepSWE: 待核实 — 需检查完整 v1.1 配置中的 exact model ID。; SWE-bench Pro: 待核实 — 需确认该精确型号是否进入完整 Pro V2 结果。; Terminal-Bench: 待核实 — 需确认 V4 精确型号结果。; Terminal-Bench-Science: 待核实 — 需复核完整 Science 榜单。; AutomationBench: 待核实 — 需检查折叠的剩余模型结果。; Humanity's Last Exam: 待核实 — 需要 highspeed 精确型号的 HLE 评测记录或明确测试身份。; GDPval-AA: 待核实 — 需确认 highspeed 是否以目标 v2.1 配置单独测得分数；基座结果冲突未解。; Vals Index: 待核实 — 未确认 highspeed 在 Vals Index v2.2 下的精确结果。
- [MiMo-V2-Omni (xiaomi/mimo-v2-omni)](models/xiaomi/mimo-v2-omni.md) — DeepSWE: 待核实 — 需检查完整 v1.1 原始模型 ID。; SWE-bench Pro: 待核实 — 需确认完整 Pro V2 leaderboard 的精确型号结果。; Terminal-Bench: 待核实 — 需复核 V4 的完整结果行及测试配置。; Terminal-Bench-Science: 待核实 — 需复核完整榜单中的 exact model ID。; AutomationBench: 待核实 — 需检查折叠的剩余模型结果。; OSWorld: 待核实 — 需查明 v2.1 精确 leaderboard 及 MiMo-V2-Omni 条目。; GDPval-AA: 待核实 — 需要可核验的 MiMo-V2-Omni GDPval-AA v2.1 Elo 行。; Vals Index: 待核实 — 需获取该历史型号在 v2.2 方法下的独立结果或完整记录。
- [MiMo-V2-Pro (xiaomi/mimo-v2-pro)](models/xiaomi/mimo-v2-pro.md) — DeepSWE: 待核实 — 需要在完整、稳定的榜单数据中确认是否存在精确模型记录。; SWE-bench Pro: 待核实 — 当前榜单未能确认该型号是否评测，不能用其他 SWE-Bench Pro 版本替代。; Terminal-Bench: 待核实 — 需要直接核实 Terminal-Bench 4 结果榜单中的精确型号行。; Terminal-Bench-Science: 待核实 — 结果页不可读，保留待核实。; AutomationBench: 待核实 — 需检查折叠后的完整榜单或可下载数据。; GDPval-AA: 待核实 — 需取得明确标注 GDPval-AA v2.1 的 MiMo-V2-Pro 评测记录。; Vals Index: 待核实 — 需要完整历史模型结果或精确模型页确认 v2.2 记录。
- [GPT-5.4 mini (openai/gpt-5.4-mini)](models/openai/gpt-5.4-mini.md) — DeepSWE: 待核实 — 需核查完整实时榜单并确认 mini 型号是否有独立结果。; SWE-bench Pro: 待核实 — 现有 54.4% 不映射到 Pro V2，待完整榜单核实。; Terminal-Bench: 待核实 — 需要可读取的 Terminal-Bench 4 精确型号结果。; Terminal-Bench-Science: 待核实 — 结果页不可读，保留待核实。; AutomationBench: 待核实 — 需检查完整榜单数据。; OSWorld: 待核实 — 不能将 OSWorld-Verified 或 OSWorld 2.0 结果移植为 v2.1。; Vals Index: 待核实 — 需完整历史数据或精确模型页核实 v2.2。
- [GPT-5.4 nano (openai/gpt-5.4-nano)](models/openai/gpt-5.4-nano.md) — DeepSWE: 待核实 — 动态榜单数据不全，尚不能排除未展示的精确成绩。; SWE-bench Pro: 待核实 — 当前公开榜单未确认 nano 的 v2 成绩；本地旧版成绩不能替代。; Terminal-Bench: 待核实 — 需要官方 v4 结果页的精确模型行。; Terminal-Bench-Science: 待核实 — 动态榜单未加载。; AutomationBench: 待核实 — 需检查完整榜单数据。; OSWorld: 待核实 — 不能把 OSWorld-Verified 39.0% 当作 v2.1。; Vals Index: 待核实 — 版本和该动态型号页当前分数的对应关系不明。
- [Mistral Small 4 (mistral/mistral-small-2603)](models/mistral/mistral-small-2603.md) — DeepSWE: 待核实 — 动态榜单不完整，需确认 Mistral Small 4 精确结果。; SWE-bench Pro: 待核实 — 当前公开榜单未确认目标行。; Terminal-Bench: 待核实 — 需取得可读的 v4 精确结果。; Terminal-Bench-Science: 待核实 — 动态榜单未加载。; AutomationBench: 待核实 — 需检查完整榜单。; OSWorld: 待核实 — 尚无精确 v2.1 的公开记录核验。; GDPval-AA: 冲突 — 同一版本和变体存在 370 与 365 Elo 两个公开值，待 AA 说明是否为结果修订或不同运行。; Vals Index: 待核实 — 25.34% 对应的版本与评测日期未披露。
- [Mistral Small (latest) (mistral/mistral-small-latest)](models/mistral/mistral-small-latest.md) — DeepSWE: 待核实 — alias 的测试时解析版本及其独立榜单结果未确认。; SWE-bench Pro: 待核实 — alias 的评测快照和精确成绩未确认。; Terminal-Bench: 待核实 — 需要有明确测试快照的 latest alias 结果。; Terminal-Bench-Science: 待核实 — 动态榜单未加载，且 alias 测试时快照未知。; AutomationBench: 待核实 — 需完整榜单和精确测试时 alias 解析版本。; OSWorld: 待核实 — 需确认 v2.1 测试采用的 alias 快照。; Humanity's Last Exam: 待核实 — 缺少与 alias 精确绑定的 HLE 记录。; Artificial Analysis Intelligence Index: 待核实 — 缺少测试时 alias 解析版本的精确 V5 行。; GDPval-AA: 待核实 — 缺少 alias 精确行；底层 Small 4 结果还存在冲突。; Vals Index: 待核实 — 缺少精确 alias + v2.2 记录。
- [Nemotron VoiceChat (nvidia/nemotron-voicechat)](models/nvidia/nemotron-voicechat.md) — DeepSWE: 待核实 — 工具接口差异未解决，且未确认 DeepSWE v1.1 精确结果。; SWE-bench Pro: 待核实 — 本地工具能力与官方卡未能一致核实。; Terminal-Bench: 待核实 — 工具执行能力及精确 TB4 结果均待核实。; Terminal-Bench-Science: 待核实 — 工具执行能力及榜单结果待核实。; AutomationBench: 待核实 — 需核实 tools=true 对应的精确模型 API 能力及完整榜单行。
- [GLM-5-Turbo (zhipuai/glm-5-turbo)](models/zhipuai/glm-5-turbo.md) — DeepSWE: 待核实 — 需要进一步确认动态或部分加载榜单中的精确型号记录。; SWE-bench Pro: 待核实 — 需要进一步确认动态或部分加载榜单中的精确型号记录。; Terminal-Bench: 待核实 — 需要进一步确认动态或部分加载榜单中的精确型号记录。; Terminal-Bench-Science: 待核实 — 需要进一步确认动态或部分加载榜单中的精确型号记录。; AutomationBench: 待核实 — 无法确认 GLM-5-Turbo 是否存在官方 held-out 成绩。; Vals Index: 待核实 — 当前榜单无法判定 GLM-5-Turbo 是否曾有独立成绩。
- [Nemotron 3 Super 120B A12B (nvidia/nemotron-3-super-120b-a12b)](models/nvidia/nemotron-3-super-120b-a12b.md) — DeepSWE: 待核实 — 动态或部分加载榜单中尚不能确认精确型号行。; SWE-bench Pro: 待核实 — 动态或部分加载榜单中尚不能确认精确型号行。; Terminal-Bench: 待核实 — 动态或部分加载榜单中尚不能确认精确型号行。; Terminal-Bench-Science: 待核实 — 动态或部分加载榜单中尚不能确认精确型号行。; AutomationBench: 待核实 — 无法确认 Nemotron 3 Super 是否有官方 held-out 成绩。; GDPval-AA: 冲突 — 需核实 AA 页面间读数差异及更新时间/配置；暂不选取一个分数。; Vals Index: 待核实 — 无法从当前精简榜单判断 Nemotron 3 Super 是否存在独立成绩。
- [Reka Edge (rekaai/reka-edge)](models/rekaai/reka-edge.md) — DeepSWE: 待核实 — 榜单加载结果不足以判定没有成绩。; SWE-bench Pro: 待核实 — 榜单加载结果不足以判定没有成绩。; Terminal-Bench: 待核实 — 榜单加载结果不足以判定没有成绩。; Terminal-Bench-Science: 待核实 — 榜单加载结果不足以判定没有成绩。; AutomationBench: 待核实 — 需检查 AutomationBench 完整官方榜单中的 reka-edge-2603 记录。; OSWorld: 待核实 — 当前动态榜单未能确认 reka-edge-2603 的结果。; Chartography: 待核实 — 需要确认 Chartography 完整榜单中的精确型号成绩。; Humanity's Last Exam: 待核实 — 未取得 reka-edge-2603 的原始 HLE 成绩。; Artificial Analysis Intelligence Index: 待核实 — 需确认是否存在 AA 对应的精确型号档案或 V5 指数。; GDPval-AA: 待核实 — 尚无可核实的 reka-edge-2603 GDPval-AA 分数。; Vals Index: 待核实 — 精简榜单缺席不能证明没有旧成绩。
- [Grok 4.20 (Non-Reasoning) (xai/grok-4.20-0309-non-reasoning)](models/xai/grok-4.20-0309-non-reasoning.md) — DeepSWE: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; SWE-bench Pro: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; Terminal-Bench: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; Terminal-Bench-Science: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; AutomationBench: 待核实 — 需确认完整 held-out 官方榜单中的精确模型行。; OSWorld: 待核实 — 当前动态榜单未能确认精确模型行。; Chartography: 待核实 — 动态榜单未显示完整历史，缺席不足以判定未找到。; Humanity's Last Exam: 待核实 — 缺少该精确变体可核实的 HLE 结果行。; Artificial Analysis Intelligence Index: 待核实 — 需确认精确模型是否有 V5.0.1 结果；V5 采用 HLE-Diamond，和原始 HLE 不同。; GDPval-AA: 待核实 — 尚未取得该精确模型在 GDPval-AA v2.1 上可核实的分数。; Vals Index: 待核实 — 需取得与本地精确变体及 Vals Index v2.2 完全对应的结果。
- [Grok 4.20 (Reasoning) (xai/grok-4.20-0309-reasoning)](models/xai/grok-4.20-0309-reasoning.md) — DeepSWE: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; SWE-bench Pro: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; Terminal-Bench: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; Terminal-Bench-Science: 待核实 — 需在完整榜单中确认该精确 API ID 的目标 benchmark 结果。; AutomationBench: 待核实 — 需确认完整 held-out 官方榜单中的精确模型行。; OSWorld: 待核实 — 当前动态榜单未能确认精确模型行。; Chartography: 待核实 — 动态榜单未显示完整历史，缺席不足以判定未找到。; Artificial Analysis Intelligence Index: 待核实 — 需确认精确模型是否有 V5.0.1 结果；V5 采用 HLE-Diamond，和原始 HLE 不同。; GDPval-AA: 待核实 — 尚未取得该精确模型在 GDPval-AA v2.1 上可核实的分数。; Vals Index: 待核实 — 需取得与本地精确变体及 Vals Index v2.2 完全对应的结果。
- [GPT-5.4 (openai/gpt-5.4)](models/openai/gpt-5.4.md) — SWE-bench Pro: 待核实 — 需确认本地 public 记录是否属于 642-task V2，且与 57.7% 是否为相同评测条件；暂不把两者当成同一成绩。; Terminal-Bench: 待核实 — 需从完整官方 4.0 结果确认 GPT-5.4 的 exact score 与配置。; Terminal-Bench-Science: 待核实 — 需从可读取的完整 0.1 榜单或原始运行记录确认。; AutomationBench: 待核实 — 需核对官方榜单完整折叠结果及其私有 held-out 数据集配置。; OSWorld: 待核实 — 需确认 v2.1 精确运行结果；不将 OSWorld-Verified 作为 V2.1 成绩。; Artificial Analysis Intelligence Index: 待核实 — 需确认 GPT-5.4 是否已在 V5.0.1 完成评测；V5.0.1 与历史 v4 指数组成不同。; Vals Index: 待核实 — 需从 Vals 确认 65.91% 是否属于 v2.2。
- [GPT-5.4 Pro (openai/gpt-5.4-pro)](models/openai/gpt-5.4-pro.md) — DeepSWE: 待核实 — 需确认是否存在未列入当前公开榜单的 GPT-5.4 Pro 结果。; SWE-bench Pro: 待核实 — 需从完整 V2 榜单或原始评测资料确认。; Terminal-Bench: 待核实 — 需核对官方 V4 完整榜单是否含 GPT-5.4 Pro。; Terminal-Bench-Science: 待核实 — 需从完整 0.1 榜单或原始运行记录确认。; AutomationBench: 待核实 — 需核对官方榜单完整折叠结果及 Pro 变体。; OSWorld: 待核实 — 需确认公开 OSWorld V2.1 完整榜单中的 GPT-5.4 Pro 结果。; Chartography: 待核实 — 需确认动态榜单是否存在 GPT-5.4 Pro 历史评测。; Artificial Analysis Intelligence Index: 待核实 — 需确认 GPT-5.4 Pro 是否有 V5.0.1 结果。; GDPval-AA: 待核实 — 需取得精确 Pro 配置的 v2.1 Elo 和 source table。; Vals Index: 待核实 — 需确认是否有精确 GPT-5.4 Pro V2.2 结果。
- [Gemini 3.1 Flash Lite Preview (google/gemini-3.1-flash-lite-preview)](models/google/gemini-3.1-flash-lite-preview.md) — DeepSWE: 待核实 — 需确认该精确 preview endpoint 是否有未公开或未列出的成绩。; SWE-bench Pro: 待核实 — 需核对完整 V2 榜单中的精确 API ID。; Terminal-Bench: 待核实 — 需核对终端评测行绑定的模型 API ID。; Terminal-Bench-Science: 待核实 — 需从完整 0.1 榜单或 Harbor 原始运行资料确认。; AutomationBench: 待核实 — 需核对官方榜单完整折叠结果及模型 ID。; OSWorld: 待核实 — 需确认是否有外部 OSWorld v2.1 harness 的精确 Preview 评测。; Chartography: 待核实 — 动态榜单未显示完整历史，需进一步确认精确 Preview 行。; Humanity's Last Exam: 待核实 — 需取得精确 Preview 在原始 HLE（非 HLE-Diamond）上的公开结果。; GDPval-AA: 待核实 — 需取得精确 Preview 的 v2.1 Elo。; Vals Index: 待核实 — 需确认精确 Preview 的 44.02% 是否属于 V2.2。
