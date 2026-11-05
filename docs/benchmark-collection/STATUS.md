<!-- benchmark-collection-run
{
  "current_model": null,
  "current_models": [],
  "last_completed_model": "google/gemini-3.1-flash-lite-preview",
  "last_execution": "2026-11-05T12:12+08:00",
  "priority_window_completed": {
    "candidate_count": 103,
    "first_pass_completed": 103,
    "from": "2026-09-05",
    "through": "2026-11-05"
  },
  "queue_metadata_corrections": {
    "google/gemini-3-pro-image": {
      "field": "release_date",
      "from": "2026-05-28",
      "source": "https://blog.google/innovation-and-ai/products/nano-banana-pro/",
      "to": "2025-11-20"
    },
    "google/gemini-3.1-flash-image": {
      "field": "release_date",
      "from": "2026-05-28",
      "source": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/",
      "to": "2026-02-26"
    },
    "google/gemma-4-26b-a4b-it": {
      "field": "release_date",
      "from": "2026-04-02",
      "note": "Google’s official Gemma release log says Gemma 4 launched in E2B, E4B, 31B, and 26B A4B sizes on March 31, 2026.",
      "source": "https://ai.google.dev/gemma/docs/releases",
      "to": "2026-03-31"
    },
    "google/gemma-4-31b-it": {
      "field": "release_date",
      "from": "2026-04-02",
      "note": "Google’s official Gemma release log says Gemma 4 launched in E2B, E4B, 31B, and 26B A4B sizes on March 31, 2026.",
      "source": "https://ai.google.dev/gemma/docs/releases",
      "to": "2026-03-31"
    },
    "google/gemma-4-E2B-it": {
      "field": "release_date",
      "from": "2026-04-02",
      "note": "Google’s official Gemma release log says Gemma 4 launched in E2B, E4B, 31B, and 26B A4B sizes on March 31, 2026.",
      "source": "https://ai.google.dev/gemma/docs/releases",
      "to": "2026-03-31"
    },
    "google/gemma-4-E4B-it": {
      "field": "release_date",
      "from": "2026-04-02",
      "note": "Google’s official Gemma release log says Gemma 4 launched in E2B, E4B, 31B, and 26B A4B sizes on March 31, 2026.",
      "source": "https://ai.google.dev/gemma/docs/releases",
      "to": "2026-03-31"
    },
    "meta/muse-spark-1.1": {
      "field": "release_date",
      "from": "2026-04-08",
      "note": "Meta announcement identifies Muse Spark 1.1 and is dated July 9, 2026; April 8 was the earlier unversioned Muse Spark announcement.",
      "source": "https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/",
      "to": "2026-07-09"
    },
    "mistral/mistral-medium-2604": {
      "field": "release_date",
      "from": "2026-04-29",
      "note": "Mistral model card and changelog list Apr 28; Mistral Legal Center lists Apr 29.",
      "source": "https://docs.mistral.ai/models/mistral-medium-3-5-26-04",
      "to": "2026-04-28"
    },
    "mistral/mistral-medium-3-5": {
      "field": "release_date",
      "from": "2026-04-30",
      "note": "The model card also lists April 28; Mistral Legal Center lists April 29.",
      "source": "https://docs.mistral.ai/resources/changelogs",
      "to": "2026-04-28"
    },
    "xai/grok-build-0.1": {
      "field": "release_date",
      "from": "2026-04-16",
      "note": "xAI release notes list the exact grok-build-0.1 model as early access on May 19, 2026; May 14 refers to the Grok Build product beta.",
      "source": "https://docs.x.ai/developers/release-notes",
      "to": "2026-05-19"
    }
  },
  "scope": {
    "from": "2026-09-05",
    "through": "2026-11-05"
  }
}

-->
# Benchmark 收集任务队列与断点

模型总数：849<br>
已完成首轮检查：352<br>
待处理（尚未开始）：497<br>
失败或中断：0<br>
最近执行时间：2026-11-05T12:12+08:00<br>
当前正在处理：无<br>
下一待处理模型：openai/gpt-5.3-chat-latest

本轮 release_date 范围：2026-09-05 至 2026-11-05<br>
范围候选模型：103（精确日期 101，日期精度不足而保守纳入 2）<br>
范围首轮完成：103<br>
范围待处理：0

队列按 release_date 从新到旧；同日按模型 ID 字典序；缺少发布日期的模型置末。首轮检查完成要求 11 项都已尝试且无检查失败；待核实或冲突项会使模型状态保持待复核。已完成表示 11 项核验全部结束，不要求每项都有成绩。队列表中的已检查项目表示已尝试核验，包含待核实、冲突和失败项。

| 模型 ID | 发布日期 | 处理状态 | 已检查项目 | 最近检查 |
|---|---|---|---:|---|
| [openai/gpt-6.1-terra](models/openai/gpt-6.1-terra.md) | 2026-10-26 | 待复核 | 11/11 | 2026-11-04T01:09+08:00 |
| [moonshotai/kimi-k3.1-pro](models/moonshotai/kimi-k3.1-pro.md) | 2026-10-23 | 待复核 | 11/11 | 2026-11-04T01:52+08:00 |
| [recursive/flint](models/recursive/flint.md) | 2026-10-21 | 待复核 | 11/11 | 2026-11-04T01:57+08:00 |
| [baseten/elephant-1](models/baseten/elephant-1.md) | 2026-10-19 | 待复核 | 11/11 | 2026-11-04T02:02+08:00 |
| [baseten/mammoth-1](models/baseten/mammoth-1.md) | 2026-10-19 | 待复核 | 11/11 | 2026-11-04T02:06+08:00 |
| [minimax/MiniMax-M3.1-Flash](models/minimax/MiniMax-M3.1-Flash.md) | 2026-10-19 | 待复核 | 11/11 | 2026-11-04T02:10+08:00 |
| [deepseek/deepseek-v4.1-flash-1017](models/deepseek/deepseek-v4.1-flash-1017.md) | 2026-10-17 | 待复核 | 11/11 | 2026-11-04T02:16+08:00 |
| [inception/mercury-3](models/inception/mercury-3.md) | 2026-10-16 | 待复核 | 11/11 | 2026-11-04T02:21+08:00 |
| [black-forest-labs/flux-3-image-klein](models/black-forest-labs/flux-3-image-klein.md) | 2026-10-15 | 已完成 | 11/11 | 2026-11-04T02:23+08:00 |
| [krea/krea-3](models/krea/krea-3.md) | 2026-10-15 | 已完成 | 11/11 | 2026-11-04T02:25+08:00 |
| [meta/muse-spark-open](models/meta/muse-spark-open.md) | 2026-10-15 | 待复核 | 11/11 | 2026-11-04T02:30+08:00 |
| [nvidia/nemotron-3.5-super-120b-a12b](models/nvidia/nemotron-3.5-super-120b-a12b.md) | 2026-10-15 | 待复核 | 11/11 | 2026-11-04T02:34+08:00 |
| [nvidia/nemotron-3.5-super-vl-120b-a12b](models/nvidia/nemotron-3.5-super-vl-120b-a12b.md) | 2026-10-15 | 待复核 | 11/11 | 2026-11-04T02:37+08:00 |
| [perplexity/pplx-decider-flash-v1.2](models/perplexity/pplx-decider-flash-v1.2.md) | 2026-10-15 | 已完成 | 11/11 | 2026-11-04T02:42+08:00 |
| [perplexity/pplx-decider-v1.2](models/perplexity/pplx-decider-v1.2.md) | 2026-10-15 | 已完成 | 11/11 | 2026-11-04T02:42+08:00 |
| [typesafe/jev-1.14.0](models/typesafe/jev-1.14.0.md) | 2026-10-14 | 已完成 | 11/11 | 2026-11-04T02:44+08:00 |
| [xai/grok-voice-3.0](models/xai/grok-voice-3.0.md) | 2026-10-14 | 待复核 | 11/11 | 2026-11-04T02:48+08:00 |
| [fish-audio/drama-3](models/fish-audio/drama-3.md) | 2026-10-13 | 已完成 | 11/11 | 2026-11-04T02:51+08:00 |
| [google/gemini-4-argon](models/google/gemini-4-argon.md) | 2026-10-13 | 待复核 | 11/11 | 2026-11-04T02:58+08:00 |
| [heygen/heygen-voice-1](models/heygen/heygen-voice-1.md) | 2026-10-13 | 已完成 | 11/11 | 2026-11-04T03:03+08:00 |
| [heygen/heygen-voice-1-turbo](models/heygen/heygen-voice-1-turbo.md) | 2026-10-13 | 已完成 | 11/11 | 2026-11-04T03:04+08:00 |
| [meta/muse-wonder-1.0](models/meta/muse-wonder-1.0.md) | 2026-10-12 | 待复核 | 11/11 | 2026-11-04T03:11+08:00 |
| [meta/muse-wonder-full](models/meta/muse-wonder-full.md) | 2026-10-12 | 待复核 | 11/11 | 2026-11-04T03:16+08:00 |
| [vllm-sr/d3](models/vllm-sr/d3.md) | 2026-10-10 | 已完成 | 11/11 | 2026-11-04T03:18+08:00 |
| [vllm-sr/d3-flash](models/vllm-sr/d3-flash.md) | 2026-10-10 | 已完成 | 11/11 | 2026-11-04T03:22+08:00 |
| [alibaba/qwen-image-2.1-turbo](models/alibaba/qwen-image-2.1-turbo.md) | 2026-10-09 | 已完成 | 11/11 | 2026-11-04T03:25+08:00 |
| [lightonai/lightonocr-3-0.8b](models/lightonai/lightonocr-3-0.8b.md) | 2026-10-08 | 待复核 | 11/11 | 2026-11-04T03:30+08:00 |
| [phocinae/phocinae-largha-150m-v1](models/phocinae/phocinae-largha-150m-v1.md) | 2026-10-08 | 已完成 | 11/11 | 2026-11-04T03:33+08:00 |
| [anthropic/claude-haiku-5-5](models/anthropic/claude-haiku-5-5.md) | 2026-10-07 | 待复核 | 11/11 | 2026-11-04T03:52+08:00 |
| [openbmb/minicpm-v-4.7-35b-a3b](models/openbmb/minicpm-v-4.7-35b-a3b.md) | 2026-10-07 | 待复核 | 11/11 | 2026-11-04T03:57+08:00 |
| [google/gemini-nano-banana-2.1](models/google/gemini-nano-banana-2.1.md) | 2026-10-06 | 已完成 | 11/11 | 2026-11-04T04:05+08:00 |
| [mistral/mistral-large-4](models/mistral/mistral-large-4.md) | 2026-10-06 | 待复核 | 11/11 | 2026-11-04T04:18+08:00 |
| [nace-ai/drex-v2.0](models/nace-ai/drex-v2.0.md) | 2026-10-06 | 待复核 | 11/11 | 2026-11-04T04:24+08:00 |
| [openbmb/minicpm-v-4.7-1b](models/openbmb/minicpm-v-4.7-1b.md) | 2026-10-06 | 待复核 | 11/11 | 2026-11-04T04:30+08:00 |
| [reflection/beam-1.0-501b-a23b](models/reflection/beam-1.0-501b-a23b.md) | 2026-10-05 | 待复核 | 11/11 | 2026-11-04T04:48+08:00 |
| [levanto/levanto-sage-v1.4](models/levanto/levanto-sage-v1.4.md) | 2026-10-04 | 已完成 | 11/11 | 2026-11-04T04:53+08:00 |
| [aleph-alpha/kolibri-1](models/aleph-alpha/kolibri-1.md) | 2026-10-03 | 待复核 | 11/11 | 2026-11-04T05:01+08:00 |
| [alibaba/qwen-image-2.1-pro](models/alibaba/qwen-image-2.1-pro.md) | 2026-10-02 | 已完成 | 11/11 | 2026-11-04T05:04+08:00 |
| [black-forest-labs/flux-3-image](models/black-forest-labs/flux-3-image.md) | 2026-10-01 | 已完成 | 11/11 | 2026-11-04T05:06+08:00 |
| [cloudflare/clef](models/cloudflare/clef.md) | 2026-10-01 | 已完成 | 11/11 | 2026-11-04T05:12+08:00 |
| [cloudflare/clef-flash](models/cloudflare/clef-flash.md) | 2026-10-01 | 已完成 | 11/11 | 2026-11-04T05:14+08:00 |
| [microsoft/mai-voice-2.1](models/microsoft/mai-voice-2.1.md) | 2026-10-01 | 已完成 | 11/11 | 2026-11-04T05:17+08:00 |
| [microsoft/mai-voice-2.1-flash](models/microsoft/mai-voice-2.1-flash.md) | 2026-10-01 | 已完成 | 11/11 | 2026-11-04T05:18+08:00 |
| [xai/grok-imagine-video-1.5-lite](models/xai/grok-imagine-video-1.5-lite.md) | 2026-10-01 | 已完成 | 11/11 | 2026-11-04T05:21+08:00 |
| [cohere/embed-v5.0-fast](models/cohere/embed-v5.0-fast.md) | 2026-09-30 | 已完成 | 11/11 | 2026-11-04T05:24+08:00 |
| [cohere/embed-v5.0-pro](models/cohere/embed-v5.0-pro.md) | 2026-09-30 | 已完成 | 11/11 | 2026-11-04T05:26+08:00 |
| [heygen/heygen-video-1](models/heygen/heygen-video-1.md) | 2026-09-30 | 已完成 | 11/11 | 2026-11-04T05:29+08:00 |
| [inception/mercury-decide](models/inception/mercury-decide.md) | 2026-09-30 | 待复核 | 11/11 | 2026-11-04T05:35+08:00 |
| [voyageai/rerank-3](models/voyageai/rerank-3.md) | 2026-09-30 | 已完成 | 11/11 | 2026-11-04T05:39+08:00 |
| [voyageai/rerank-3-lite](models/voyageai/rerank-3-lite.md) | 2026-09-30 | 已完成 | 11/11 | 2026-11-04T05:41+08:00 |
| [assemblyai/universal-3-6-pro](models/assemblyai/universal-3-6-pro.md) | 2026-09-29 | 已完成 | 11/11 | 2026-11-04T05:43+08:00 |
| [inclusionai/ling-3.1-flash](models/inclusionai/ling-3.1-flash.md) | 2026-09-29 | 待复核 | 11/11 | 2026-11-04T06:01+08:00 |
| [liquid/d1](models/liquid/d1.md) | 2026-09-29 | 已完成 | 11/11 | 2026-11-04T06:09+08:00 |
| [openai/gpt-6.1-sol](models/openai/gpt-6.1-sol.md) | 2026-09-29 | 待复核 | 11/11 | 2026-11-04T06:26+08:00 |
| [anthropic/claude-sonnet-5-5](models/anthropic/claude-sonnet-5-5.md) | 2026-09-28 | 待复核 | 11/11 | 2026-11-04T06:44+08:00 |
| [elevenlabs/eleven_v4](models/elevenlabs/eleven_v4.md) | 2026-09-28 | 已完成 | 11/11 | 2026-11-04T06:51+08:00 |
| [elevenlabs/eleven_v4_turbo](models/elevenlabs/eleven_v4_turbo.md) | 2026-09-28 | 已完成 | 11/11 | 2026-11-04T06:54+08:00 |
| [nace-ai/drex-v1.5](models/nace-ai/drex-v1.5.md) | 2026-09-28 | 待复核 | 11/11 | 2026-11-04T06:59+08:00 |
| [minimax/MiniMax-M3.1-Flash-Preview](models/minimax/MiniMax-M3.1-Flash-Preview.md) | 2026-09-27 | 已完成 | 11/11 | 2026-11-04T07:04+08:00 |
| [meituan/longcat-2.5-preview](models/meituan/longcat-2.5-preview.md) | 2026-09-25 | 已完成 | 11/11 | 2026-11-04T07:08+08:00 |
| [perceptron/perceptron-mk1.5](models/perceptron/perceptron-mk1.5.md) | 2026-09-25 | 已完成 | 11/11 | 2026-11-04T07:14+08:00 |
| [alibaba/qwen3.8-max-prime](models/alibaba/qwen3.8-max-prime.md) | 2026-09-23 | 待复核 | 11/11 | 2026-11-04T07:19+08:00 |
| [recraft/recraft-v4.1-flash](models/recraft/recraft-v4.1-flash.md) | 2026-09-23 | 已完成 | 11/11 | 2026-11-04T07:23+08:00 |
| [anthropic/claude-opus-5-5](models/anthropic/claude-opus-5-5.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T07:44+08:00 |
| [fireworks/ember-1](models/fireworks/ember-1.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T07:52+08:00 |
| [google/gemini-3.8-flash-lite-tts](models/google/gemini-3.8-flash-lite-tts.md) | 2026-09-22 | 已完成 | 11/11 | 2026-11-04T07:55+08:00 |
| [google/gemini-3.8-flash-tts](models/google/gemini-3.8-flash-tts.md) | 2026-09-22 | 已完成 | 11/11 | 2026-11-04T07:58+08:00 |
| [openai/gpt-6-luna](models/openai/gpt-6-luna.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T08:12+08:00 |
| [openai/gpt-6-sol](models/openai/gpt-6-sol.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T08:34+08:00 |
| [tencent/hy-image-v3.5-preview](models/tencent/hy-image-v3.5-preview.md) | 2026-09-22 | 已完成 | 11/11 | 2026-11-04T08:39+08:00 |
| [upstage/solar-mini4](models/upstage/solar-mini4.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T08:49+08:00 |
| [xiaomi/mimo-v2.6-flash](models/xiaomi/mimo-v2.6-flash.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T09:02+08:00 |
| [xiaomi/mimo-v2.6-pro](models/xiaomi/mimo-v2.6-pro.md) | 2026-09-22 | 待复核 | 11/11 | 2026-11-04T09:11+08:00 |
| [surogate/rune-26b-a4b](models/surogate/rune-26b-a4b.md) | 2026-09-21 | 已完成 | 11/11 | 2026-11-04T09:16+08:00 |
| [vivgrid/viv-fast](models/vivgrid/viv-fast.md) | 2026-09-21 | 待复核 | 11/11 | 2026-11-04T09:22+08:00 |
| [xai/grok-4.7](models/xai/grok-4.7.md) | 2026-09-21 | 待复核 | 11/11 | 2026-11-04T09:40+08:00 |
| [xiaomi/mimo-v2.6-pro-ultraspeed](models/xiaomi/mimo-v2.6-pro-ultraspeed.md) | 2026-09-21 | 待复核 | 11/11 | 2026-11-04T09:47+08:00 |
| [fish-audio/transcribe-1-pro](models/fish-audio/transcribe-1-pro.md) | 2026-09-18 | 已完成 | 11/11 | 2026-11-04T09:51+08:00 |
| [alibaba/qwen3.8-omni-flash](models/alibaba/qwen3.8-omni-flash.md) | 2026-09-17 | 待复核 | 11/11 | 2026-11-04T10:05+08:00 |
| [unbiased/pareto](models/unbiased/pareto.md) | 2026-09-17 | 待复核 | 11/11 | 2026-11-04T10:17+08:00 |
| [xai/grok-voice-transcribe-2.0](models/xai/grok-voice-transcribe-2.0.md) | 2026-09-17 | 已完成 | 11/11 | 2026-11-04T10:20+08:00 |
| [quiverai/arrow-2](models/quiverai/arrow-2.md) | 2026-09-16 | 待复核 | 11/11 | 2026-11-04T10:27+08:00 |
| [quiverai/arrow-2-telos](models/quiverai/arrow-2-telos.md) | 2026-09-16 | 待复核 | 11/11 | 2026-11-04T10:35+08:00 |
| [stepfun/step-5-preview](models/stepfun/step-5-preview.md) | 2026-09-16 | 待复核 | 11/11 | 2026-11-04T10:47+08:00 |
| [google/gemini-3.8-live](models/google/gemini-3.8-live.md) | 2026-09-15 | 待复核 | 11/11 | 2026-11-04T10:58+08:00 |
| [google/gemini-3.8-live-extended-thinking](models/google/gemini-3.8-live-extended-thinking.md) | 2026-09-15 | 待复核 | 11/11 | 2026-11-04T11:02+08:00 |
| [typesafe/jev-1.13.0](models/typesafe/jev-1.13.0.md) | 2026-09-15 | 已完成 | 11/11 | 2026-11-04T11:07+08:00 |
| [typesafe/jev-latest](models/typesafe/jev-latest.md) | 2026-09-15 | 已完成 | 11/11 | 2026-11-04T11:12+08:00 |
| [alibaba/qwen-image-2.1](models/alibaba/qwen-image-2.1.md) | 2026-09-14 | 已完成 | 11/11 | 2026-11-04T11:16+08:00 |
| [elevenlabs/scribe_v2_medical](models/elevenlabs/scribe_v2_medical.md) | 2026-09-11 | 已完成 | 11/11 | 2026-11-04T11:20+08:00 |
| [moonshotai/kimi-k2.8-preview](models/moonshotai/kimi-k2.8-preview.md) | 2026-09-11 | 待复核 | 11/11 | 2026-11-04T11:25+08:00 |
| [sakana/fugu-max](models/sakana/fugu-max.md) | 2026-09-11 | 待复核 | 11/11 | 2026-11-04T11:33+08:00 |
| [sakana/fugu-ultra-v2](models/sakana/fugu-ultra-v2.md) | 2026-09-11 | 待复核 | 11/11 | 2026-11-04T11:45+08:00 |
| [deepseek/deepseek-v4.1-flash](models/deepseek/deepseek-v4.1-flash.md) | 2026-09-10 | 待复核 | 11/11 | 2026-11-04T11:58+08:00 |
| [inclusionai/ling-3.0-flash-vl](models/inclusionai/ling-3.0-flash-vl.md) | 2026-09-10 | 待复核 | 11/11 | 2026-11-04T12:05+08:00 |
| [openai/gpt-live-1](models/openai/gpt-live-1.md) | 2026-09-10 | 待复核 | 11/11 | 2026-11-04T12:13+08:00 |
| [cohere/north-small-translate-1-0](models/cohere/north-small-translate-1-0.md) | 2026-09-09 | 已完成 | 11/11 | 2026-11-04T12:18+08:00 |
| [inception/mercury-2.5](models/inception/mercury-2.5.md) | 2026-09-08 | 待复核 | 11/11 | 2026-11-04T12:23+08:00 |
| [openai/gpt-image-2.5-flare](models/openai/gpt-image-2.5-flare.md) | 2026-09-08 | 已完成 | 11/11 | 2026-11-04T12:26+08:00 |
| [openai/gpt-image-2.5-sunburst](models/openai/gpt-image-2.5-sunburst.md) | 2026-09-08 | 已完成 | 11/11 | 2026-11-04T12:30+08:00 |
| [openbmb/minicpm5-2b](models/openbmb/minicpm5-2b.md) | 2026-09-06 | 待复核 | 11/11 | 2026-11-04T12:36+08:00 |
| [inclusionai/ling-3.0-flash-sante](models/inclusionai/ling-3.0-flash-sante.md) | 2026-09-04 | 待复核 | 11/11 | 2026-11-04T12:40+08:00 |
| [microsoft/mai-image-2.6-flash](models/microsoft/mai-image-2.6-flash.md) | 2026-09-04 | 已完成 | 11/11 | 2026-11-04T12:44+08:00 |
| [openai/gpt-6-astra](models/openai/gpt-6-astra.md) | 2026-09-04 | 待复核 | 11/11 | 2026-11-04T12:54+08:00 |
| [openai/gpt-6-astra-fast](models/openai/gpt-6-astra-fast.md) | 2026-09-04 | 已完成 | 11/11 | 2026-11-04T13:03+08:00 |
| [google/lyria-3.5](models/google/lyria-3.5.md) | 2026-09-03 | 已完成 | 11/11 | 2026-11-04T13:28+08:00 |
| [microsoft/mai-transcribe-2](models/microsoft/mai-transcribe-2.md) | 2026-09-03 | 已完成 | 11/11 | 2026-11-04T13:32+08:00 |
| [alibaba/qwen3.8-max-0902](models/alibaba/qwen3.8-max-0902.md) | 2026-09-02 | 待复核 | 11/11 | 2026-11-04T13:46+08:00 |
| [google/gemini-3.8-flash](models/google/gemini-3.8-flash.md) | 2026-09-02 | 待复核 | 11/11 | 2026-11-04T14:03+08:00 |
| [meta/muse-spark-1.3](models/meta/muse-spark-1.3.md) | 2026-09-02 | 待复核 | 11/11 | 2026-11-04T14:25+08:00 |
| [anthropic/claude-fable-5-1](models/anthropic/claude-fable-5-1.md) | 2026-09-01 | 待复核 | 11/11 | 2026-11-04T14:50+08:00 |
| [anthropic/claude-mythos-5-1](models/anthropic/claude-mythos-5-1.md) | 2026-09-01 | 待复核 | 11/11 | 2026-11-04T15:03+08:00 |
| [meta/muse-voice-transcribe-1.0](models/meta/muse-voice-transcribe-1.0.md) | 2026-09-01 | 已完成 | 11/11 | 2026-11-04T15:08+08:00 |
| [black-forest-labs/flux-video-edit](models/black-forest-labs/flux-video-edit.md) | 2026-09 | 已完成 | 11/11 | 2026-11-04T13:08+08:00 |
| [bytedance-seed/seedream-5.0-flash](models/bytedance-seed/seedream-5.0-flash.md) | 2026-09 | 已完成 | 11/11 | 2026-11-04T13:11+08:00 |
| [tencent/hy4-preview](models/tencent/hy4-preview.md) | 2026-08-28 | 待复核 | 11/11 | 2026-11-04T13:24+08:00 |
| [alibaba/qwen3.8-flash-next](models/alibaba/qwen3.8-flash-next.md) | 2026-08-27 | 待复核 | 11/11 | 2026-11-04T15:20+08:00 |
| [google/gemini-omni-1.1-flash](models/google/gemini-omni-1.1-flash.md) | 2026-08-27 | 已完成 | 11/11 | 2026-11-04T15:26+08:00 |
| [inclusionai/ling-3.0-flash-fin](models/inclusionai/ling-3.0-flash-fin.md) | 2026-08-27 | 待复核 | 11/11 | 2026-11-04T15:31+08:00 |
| [alibaba/qwen3.8-flash](models/alibaba/qwen3.8-flash.md) | 2026-08-26 | 待复核 | 11/11 | 2026-11-04T15:37+08:00 |
| [google/gemini-3.5-transcribe](models/google/gemini-3.5-transcribe.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T15:41+08:00 |
| [google/gemini-3.5-transcribe-live](models/google/gemini-3.5-transcribe-live.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T15:47+08:00 |
| [minimax/MiniMax-H3-Max](models/minimax/MiniMax-H3-Max.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T15:53+08:00 |
| [recraft/recraft-v4-styles](models/recraft/recraft-v4-styles.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T15:57+08:00 |
| [recraft/recraft-v4-styles-pro](models/recraft/recraft-v4-styles-pro.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T16:00+08:00 |
| [recraft/recraft-v4-styles-pro-vector](models/recraft/recraft-v4-styles-pro-vector.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T16:03+08:00 |
| [recraft/recraft-v4-styles-vector](models/recraft/recraft-v4-styles-vector.md) | 2026-08-26 | 已完成 | 11/11 | 2026-11-04T16:06+08:00 |
| [zhipuai/glm-5.3-flash](models/zhipuai/glm-5.3-flash.md) | 2026-08-26 | 待复核 | 11/11 | 2026-11-04T16:22+08:00 |
| [ibm/granite-4.2-8b](models/ibm/granite-4.2-8b.md) | 2026-08-25 | 待复核 | 11/11 | 2026-11-04T16:29+08:00 |
| [apodex/apodex-1.1-mini](models/apodex/apodex-1.1-mini.md) | 2026-08-24 | 待复核 | 11/11 | 2026-11-04T16:34+08:00 |
| [bria/fibo-generate-1.5](models/bria/fibo-generate-1.5.md) | 2026-08-24 | 已完成 | 11/11 | 2026-11-04T16:37+08:00 |
| [deepseek/deepseek-v4-flash-vision-exp](models/deepseek/deepseek-v4-flash-vision-exp.md) | 2026-08-21 | 待复核 | 11/11 | 2026-11-04T16:46+08:00 |
| [alibaba/wan3.0-video-prime](models/alibaba/wan3.0-video-prime.md) | 2026-08-20 | 已完成 | 11/11 | 2026-11-04T16:50+08:00 |
| [black-forest-labs/flux-video-upscale](models/black-forest-labs/flux-video-upscale.md) | 2026-08-20 | 已完成 | 11/11 | 2026-11-04T16:52+08:00 |
| [deepreinforce/ornith-1.5-35b-a3b](models/deepreinforce/ornith-1.5-35b-a3b.md) | 2026-08-18 | 待复核 | 11/11 | 2026-11-04T16:58+08:00 |
| [alibaba/qwen3.8-27b](models/alibaba/qwen3.8-27b.md) | 2026-08-14 | 待复核 | 11/11 | 2026-11-04T17:05+08:00 |
| [microsoft/mai-image-2.6](models/microsoft/mai-image-2.6.md) | 2026-08-14 | 已完成 | 11/11 | 2026-11-04T17:08+08:00 |
| [zhipuai/glm-5.3](models/zhipuai/glm-5.3.md) | 2026-08-14 | 待复核 | 11/11 | 2026-11-04T17:25+08:00 |
| [deepseek/deepseek-v4-pro-0813](models/deepseek/deepseek-v4-pro-0813.md) | 2026-08-13 | 待复核 | 11/11 | 2026-11-04T17:35+08:00 |
| [google/gemini-3.7-flash](models/google/gemini-3.7-flash.md) | 2026-08-13 | 待复核 | 11/11 | 2026-11-04T17:57+08:00 |
| [google/gemini-flash-latest](models/google/gemini-flash-latest.md) | 2026-08-13 | 待复核 | 11/11 | 2026-11-04T18:00+08:00 |
| [mixedbread/toast-1](models/mixedbread/toast-1.md) | 2026-08-13 | 已完成 | 11/11 | 2026-11-04T18:05+08:00 |
| [voyageai/voyage-code-4](models/voyageai/voyage-code-4.md) | 2026-08-13 | 已完成 | 11/11 | 2026-11-04T18:07+08:00 |
| [alibaba/qwen3.8-2.4t-a95b](models/alibaba/qwen3.8-2.4t-a95b.md) | 2026-08-12 | 待复核 | 11/11 | 2026-11-04T18:19+08:00 |
| [deepgram/flux-tts](models/deepgram/flux-tts.md) | 2026-08-12 | 已完成 | 11/11 | 2026-11-04T18:24+08:00 |
| [xai/grok-4.6](models/xai/grok-4.6.md) | 2026-08-12 | 待复核 | 11/11 | 2026-11-04T18:46+08:00 |
| [microsoft/mai-code-1.1-flash](models/microsoft/mai-code-1.1-flash.md) | 2026-08-11 | 待复核 | 11/11 | 2026-11-04T18:53+08:00 |
| [nvidia/nemotron-3.5-lightning](models/nvidia/nemotron-3.5-lightning.md) | 2026-08-11 | 待复核 | 11/11 | 2026-11-04T19:03+08:00 |
| [meta/muse-glimmer-30b](models/meta/muse-glimmer-30b.md) | 2026-08-10 | 待复核 | 11/11 | 2026-11-04T19:11+08:00 |
| [motif-technologies/motif-3](models/motif-technologies/motif-3.md) | 2026-08-07 | 待复核 | 11/11 | 2026-11-04T19:22+08:00 |
| [openai/gpt-5.6-cyber](models/openai/gpt-5.6-cyber.md) | 2026-08-07 | 待复核 | 11/11 | 2026-11-04T19:31+08:00 |
| [xai/grok-imagine-image-2.0](models/xai/grok-imagine-image-2.0.md) | 2026-08-07 | 已完成 | 11/11 | 2026-11-04T19:35+08:00 |
| [alibaba/wan3.0-video](models/alibaba/wan3.0-video.md) | 2026-08-06 | 已完成 | 11/11 | 2026-11-04T19:37+08:00 |
| [upstage/solar-pro4](models/upstage/solar-pro4.md) | 2026-08-06 | 待复核 | 11/11 | 2026-11-04T19:48+08:00 |
| [alibaba/qwen-image-3.0](models/alibaba/qwen-image-3.0.md) | 2026-08-05 | 已完成 | 11/11 | 2026-11-04T19:54+08:00 |
| [alibaba/qwen-image-3.0-pro](models/alibaba/qwen-image-3.0-pro.md) | 2026-08-05 | 已完成 | 11/11 | 2026-11-04T20:00+08:00 |
| [meta/muse-spark-1.2](models/meta/muse-spark-1.2.md) | 2026-08-05 | 待复核 | 11/11 | 2026-11-04T20:17+08:00 |
| [black-forest-labs/flux-3-video](models/black-forest-labs/flux-3-video.md) | 2026-08-04 | 已完成 | 11/11 | 2026-11-04T20:23+08:00 |
| [alibaba/qwen3.8-max](models/alibaba/qwen3.8-max.md) | 2026-08-03 | 待复核 | 11/11 | 2026-11-04T20:45+08:00 |
| [sakana/sakana-namazu](models/sakana/sakana-namazu.md) | 2026-08-03 | 已完成 | 11/11 | 2026-11-04T20:53+08:00 |
| [bytedance-seed/seedance-2.5](models/bytedance-seed/seedance-2.5.md) | 2026-07-31 | 已完成 | 11/11 | 2026-11-04T21:05+08:00 |
| [deepseek/deepseek-v4-flash-0731](models/deepseek/deepseek-v4-flash-0731.md) | 2026-07-31 | 待复核 | 11/11 | 2026-11-04T21:19+08:00 |
| [minimax/MiniMax-H3](models/minimax/MiniMax-H3.md) | 2026-07-31 | 已完成 | 11/11 | 2026-11-04T21:22+08:00 |
| [google/gemini-robotics-er-2-preview](models/google/gemini-robotics-er-2-preview.md) | 2026-07-30 | 已完成 | 11/11 | 2026-11-04T21:26+08:00 |
| [google/gemini-robotics-er-2-streaming-preview](models/google/gemini-robotics-er-2-streaming-preview.md) | 2026-07-30 | 已完成 | 11/11 | 2026-11-04T21:30+08:00 |
| [thinkingmachines/inkling-small](models/thinkingmachines/inkling-small.md) | 2026-07-30 | 待复核 | 11/11 | 2026-11-04T21:39+08:00 |
| [openai/gpt-live-transcribe](models/openai/gpt-live-transcribe.md) | 2026-07-28 | 已完成 | 11/11 | 2026-11-04T21:43+08:00 |
| [openai/gpt-transcribe](models/openai/gpt-transcribe.md) | 2026-07-28 | 已完成 | 11/11 | 2026-11-04T21:46+08:00 |
| [anthropic/claude-opus-5](models/anthropic/claude-opus-5.md) | 2026-07-24 | 待复核 | 11/11 | 2026-11-04T21:58+08:00 |
| [inclusionai/ling-3.0-flash](models/inclusionai/ling-3.0-flash.md) | 2026-07-23 | 待复核 | 11/11 | 2026-11-04T22:07+08:00 |
| [microsoft/mai-image-2.5-pro](models/microsoft/mai-image-2.5-pro.md) | 2026-07-23 | 已完成 | 11/11 | 2026-11-04T22:12+08:00 |
| [microsoft/mai-voice-2-flash](models/microsoft/mai-voice-2-flash.md) | 2026-07-23 | 已完成 | 11/11 | 2026-11-04T22:16+08:00 |
| [google/gemini-3.5-flash-lite](models/google/gemini-3.5-flash-lite.md) | 2026-07-21 | 待复核 | 11/11 | 2026-11-04T22:28+08:00 |
| [google/gemini-3.6-flash](models/google/gemini-3.6-flash.md) | 2026-07-21 | 待复核 | 11/11 | 2026-11-04T22:47+08:00 |
| [google/gemini-flash-lite-latest](models/google/gemini-flash-lite-latest.md) | 2026-07-21 | 待复核 | 11/11 | 2026-11-04T22:53+08:00 |
| [mindlab/macaron-v1-tall](models/mindlab/macaron-v1-tall.md) | 2026-07-21 | 待复核 | 11/11 | 2026-11-04T23:01+08:00 |
| [mindlab/macaron-v1-venti](models/mindlab/macaron-v1-venti.md) | 2026-07-21 | 待复核 | 11/11 | 2026-11-04T23:08+08:00 |
| [poolside/laguna-s-2.1](models/poolside/laguna-s-2.1.md) | 2026-07-21 | 待复核 | 11/11 | 2026-11-04T23:15+08:00 |
| [bytedance-seed/seed-audio-1.0](models/bytedance-seed/seed-audio-1.0.md) | 2026-07-20 | 已完成 | 11/11 | 2026-11-04T23:19+08:00 |
| [alibaba/qwen3.8-max-preview](models/alibaba/qwen3.8-max-preview.md) | 2026-07-19 | 待复核 | 11/11 | 2026-11-04T23:31+08:00 |
| [mistral/mistral-ocr-4-1](models/mistral/mistral-ocr-4-1.md) | 2026-07-16 | 已完成 | 11/11 | 2026-11-04T23:35+08:00 |
| [moonshotai/kimi-k3](models/moonshotai/kimi-k3.md) | 2026-07-16 | 待复核 | 11/11 | 2026-11-04T23:53+08:00 |
| [nvidia/nemotron-3-embed-1b](models/nvidia/nemotron-3-embed-1b.md) | 2026-07-16 | 已完成 | 11/11 | 2026-11-05T00:10+08:00 |
| [xai/grok-4.5](models/xai/grok-4.5.md) | 2026-07-16 | 待复核 | 11/11 | 2026-11-05T01:13+08:00 |
| [alibaba/qwen3.7-flash](models/alibaba/qwen3.7-flash.md) | 2026-07-15 | 待复核 | 11/11 | 2026-11-05T00:12+08:00 |
| [thinkingmachines/inkling](models/thinkingmachines/inkling.md) | 2026-07-15 | 待复核 | 11/11 | 2026-11-05T00:18+08:00 |
| [alibaba/qwen-audio-3.0-tts-flash](models/alibaba/qwen-audio-3.0-tts-flash.md) | 2026-07-14 | 已完成 | 11/11 | 2026-11-05T01:47+08:00 |
| [alibaba/qwen-audio-3.0-tts-plus](models/alibaba/qwen-audio-3.0-tts-plus.md) | 2026-07-14 | 已完成 | 11/11 | 2026-11-05T01:48+08:00 |
| [meta/muse-spark-1.1](models/meta/muse-spark-1.1.md) | 2026-07-09 | 待复核 | 11/11 | 2026-11-05T09:33+08:00 |
| [openai/gpt-5.6-luna](models/openai/gpt-5.6-luna.md) | 2026-07-09 | 待复核 | 11/11 | 2026-11-05T00:51+08:00 |
| [openai/gpt-5.6-sol](models/openai/gpt-5.6-sol.md) | 2026-07-09 | 待复核 | 11/11 | 2026-11-05T00:51+08:00 |
| [openai/gpt-5.6-terra](models/openai/gpt-5.6-terra.md) | 2026-07-09 | 待复核 | 11/11 | 2026-11-05T00:51+08:00 |
| [bytedance-seed/seedream-5.0-pro](models/bytedance-seed/seedream-5.0-pro.md) | 2026-07-08 | 已完成 | 11/11 | 2026-11-05T01:13+08:00 |
| [cohere/cohere-transcribe-arabic-07-2026](models/cohere/cohere-transcribe-arabic-07-2026.md) | 2026-07-07 | 已完成 | 11/11 | 2026-11-05T01:16+08:00 |
| [meta/muse-image-1.0](models/meta/muse-image-1.0.md) | 2026-07-07 | 已完成 | 11/11 | 2026-11-05T01:18+08:00 |
| [openai/gpt-realtime-2.1](models/openai/gpt-realtime-2.1.md) | 2026-07-06 | 待复核 | 11/11 | 2026-11-05T01:36+08:00 |
| [openai/gpt-realtime-2.1-mini](models/openai/gpt-realtime-2.1-mini.md) | 2026-07-06 | 待复核 | 11/11 | 2026-11-05T01:36+08:00 |
| [tencent/hy3](models/tencent/hy3.md) | 2026-07-06 | 待复核 | 11/11 | 2026-11-05T01:40+08:00 |
| [poolside/laguna-xs-2.1](models/poolside/laguna-xs-2.1.md) | 2026-07-02 | 待复核 | 11/11 | 2026-11-05T01:50+08:00 |
| [anthropic/claude-sonnet-5](models/anthropic/claude-sonnet-5.md) | 2026-06-30 | 待复核 | 11/11 | 2026-11-05T02:08+08:00 |
| [google/gemini-3.1-flash-lite-image](models/google/gemini-3.1-flash-lite-image.md) | 2026-06-30 | 待复核 | 11/11 | 2026-11-05T02:11+08:00 |
| [google/gemini-omni-flash-preview](models/google/gemini-omni-flash-preview.md) | 2026-06-30 | 已完成 | 11/11 | 2026-11-05T02:12+08:00 |
| [meituan/longcat-2.0](models/meituan/longcat-2.0.md) | 2026-06-30 | 待复核 | 11/11 | 2026-11-05T02:16+08:00 |
| [deepreinforce/ornith-1.0-31b](models/deepreinforce/ornith-1.0-31b.md) | 2026-06-25 | 待复核 | 11/11 | 2026-11-05T02:18+08:00 |
| [deepreinforce/ornith-1.0-35b](models/deepreinforce/ornith-1.0-35b.md) | 2026-06-25 | 待复核 | 11/11 | 2026-11-05T02:20+08:00 |
| [deepreinforce/ornith-1.0-397b](models/deepreinforce/ornith-1.0-397b.md) | 2026-06-25 | 待复核 | 11/11 | 2026-11-05T02:23+08:00 |
| [deepreinforce/ornith-1.0-9b](models/deepreinforce/ornith-1.0-9b.md) | 2026-06-25 | 待复核 | 11/11 | 2026-11-05T02:23+08:00 |
| [bytedance-seed/seed-2.1-pro](models/bytedance-seed/seed-2.1-pro.md) | 2026-06-23 | 待复核 | 11/11 | 2026-11-05T02:30+08:00 |
| [bytedance-seed/seed-2.1-turbo](models/bytedance-seed/seed-2.1-turbo.md) | 2026-06-23 | 待复核 | 11/11 | 2026-11-05T02:32+08:00 |
| [bytedance-seed/seed-character](models/bytedance-seed/seed-character.md) | 2026-06-23 | 待复核 | 11/11 | 2026-11-05T02:33+08:00 |
| [bytedance-seed/seed-evolving](models/bytedance-seed/seed-evolving.md) | 2026-06-23 | 待复核 | 11/11 | 2026-11-05T02:34+08:00 |
| [fish-audio/s2.1-pro](models/fish-audio/s2.1-pro.md) | 2026-06-23 | 已完成 | 11/11 | 2026-11-05T02:35+08:00 |
| [liquid/lfm2.5-embedding-350m](models/liquid/lfm2.5-embedding-350m.md) | 2026-06-18 | 已完成 | 11/11 | 2026-11-05T02:36+08:00 |
| [alibaba/happyhorse-1.1](models/alibaba/happyhorse-1.1.md) | 2026-06-16 | 已完成 | 11/11 | 2026-11-05T02:41+08:00 |
| [assemblyai/universal-3-5-pro](models/assemblyai/universal-3-5-pro.md) | 2026-06-15 | 已完成 | 11/11 | 2026-11-05T02:43+08:00 |
| [bytedance-seed/seedance-2.0-mini](models/bytedance-seed/seedance-2.0-mini.md) | 2026-06-15 | 已完成 | 11/11 | 2026-11-05T02:44+08:00 |
| [sakana/fugu](models/sakana/fugu.md) | 2026-06-15 | 待复核 | 11/11 | 2026-11-05T02:56+08:00 |
| [sakana/fugu-ultra](models/sakana/fugu-ultra.md) | 2026-06-15 | 待复核 | 11/11 | 2026-11-05T02:58+08:00 |
| [zhipuai/glm-5.2](models/zhipuai/glm-5.2.md) | 2026-06-13 | 待复核 | 11/11 | 2026-11-05T03:06+08:00 |
| [moonshotai/kimi-k2.7-code](models/moonshotai/kimi-k2.7-code.md) | 2026-06-12 | 待复核 | 11/11 | 2026-11-05T03:23+08:00 |
| [moonshotai/kimi-k2.7-code-highspeed](models/moonshotai/kimi-k2.7-code-highspeed.md) | 2026-06-12 | 待复核 | 11/11 | 2026-11-05T03:26+08:00 |
| [google/diffusiongemma-26b-a4b-it](models/google/diffusiongemma-26b-a4b-it.md) | 2026-06-10 | 待复核 | 11/11 | 2026-11-05T03:44+08:00 |
| [anthropic/claude-fable-5](models/anthropic/claude-fable-5.md) | 2026-06-09 | 待复核 | 11/11 | 2026-11-05T03:33+08:00 |
| [anthropic/claude-mythos-5](models/anthropic/claude-mythos-5.md) | 2026-06-09 | 待复核 | 11/11 | 2026-11-05T03:36+08:00 |
| [cohere/north-mini-code-1-0](models/cohere/north-mini-code-1-0.md) | 2026-06-09 | 待复核 | 11/11 | 2026-11-05T03:38+08:00 |
| [google/gemini-3.5-live-translate-preview](models/google/gemini-3.5-live-translate-preview.md) | 2026-06-09 | 已完成 | 11/11 | 2026-11-05T03:55+08:00 |
| [xiaomi/mimo-v2.5-pro-ultraspeed](models/xiaomi/mimo-v2.5-pro-ultraspeed.md) | 2026-06-08 | 待复核 | 11/11 | 2026-11-05T03:56+08:00 |
| [sourceful/riverflow-v2.5-fast](models/sourceful/riverflow-v2.5-fast.md) | 2026-06-05 | 已完成 | 11/11 | 2026-11-05T04:04+08:00 |
| [sourceful/riverflow-v2.5-pro](models/sourceful/riverflow-v2.5-pro.md) | 2026-06-05 | 已完成 | 11/11 | 2026-11-05T04:05+08:00 |
| [nvidia/nemotron-3-ultra-550b-a55b](models/nvidia/nemotron-3-ultra-550b-a55b.md) | 2026-06-04 | 待复核 | 11/11 | 2026-11-05T04:06+08:00 |
| [nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b](models/nvidia/nemotron-3.5-asr-streaming-multilingual-0.6b.md) | 2026-06-04 | 已完成 | 11/11 | 2026-11-04T21:01+08:00 |
| [google/gemma-4-12b-it](models/google/gemma-4-12b-it.md) | 2026-06-03 | 待复核 | 11/11 | 2026-11-05T04:08+08:00 |
| [krea/krea-2-medium-turbo](models/krea/krea-2-medium-turbo.md) | 2026-06-03 | 已完成 | 11/11 | 2026-11-05T04:19+08:00 |
| [alibaba/qwen3.7-plus](models/alibaba/qwen3.7-plus.md) | 2026-06-02 | 待复核 | 11/11 | 2026-11-05T04:28+08:00 |
| [microsoft/mai-code-1-flash](models/microsoft/mai-code-1-flash.md) | 2026-06-02 | 待复核 | 11/11 | 2026-11-05T04:22+08:00 |
| [microsoft/mai-image-2.5](models/microsoft/mai-image-2.5.md) | 2026-06-02 | 已完成 | 11/11 | 2026-11-05T04:23+08:00 |
| [microsoft/mai-transcribe-1.5](models/microsoft/mai-transcribe-1.5.md) | 2026-06-02 | 已完成 | 11/11 | 2026-11-05T04:24+08:00 |
| [microsoft/mai-voice-2](models/microsoft/mai-voice-2.md) | 2026-06-02 | 已完成 | 11/11 | 2026-11-05T04:25+08:00 |
| [nex-agi/nex-n2-pro](models/nex-agi/nex-n2-pro.md) | 2026-06-02 | 待复核 | 11/11 | 2026-11-05T04:34+08:00 |
| [nvidia/nemotron-3.5-content-safety](models/nvidia/nemotron-3.5-content-safety.md) | 2026-06-02 | 已完成 | 11/11 | 2026-11-05T04:35+08:00 |
| [runwayml/aleph-2](models/runwayml/aleph-2.md) | 2026-06-02 | 已完成 | 11/11 | 2026-11-05T04:36+08:00 |
| [minimax/MiniMax-M3](models/minimax/MiniMax-M3.md) | 2026-06-01 | 待复核 | 11/11 | 2026-11-05T04:50+08:00 |
| [alibaba/qwen-audio-3.0-asr-flash](models/alibaba/qwen-audio-3.0-asr-flash.md) | 2026-06 | 已完成 | 11/11 | 2026-11-05T04:50+08:00 |
| [runway/aleph-2](models/runway/aleph-2.md) | 2026-06 | 已完成 | 11/11 | 2026-11-05T04:50+08:00 |
| [xai/grok-imagine-video-1.5](models/xai/grok-imagine-video-1.5.md) | 2026-05-30 | 已完成 | 11/11 | 2026-11-05T05:14+08:00 |
| [stepfun/step-3.7-flash](models/stepfun/step-3.7-flash.md) | 2026-05-29 | 待复核 | 11/11 | 2026-11-05T05:14+08:00 |
| [anthropic/claude-opus-4-8](models/anthropic/claude-opus-4-8.md) | 2026-05-28 | 待复核 | 11/11 | 2026-11-05T05:14+08:00 |
| [alibaba/qwen3.7-max](models/alibaba/qwen3.7-max.md) | 2026-05-21 | 待复核 | 11/11 | 2026-11-05T05:30+08:00 |
| [tencent/hy-mt2-1.8b](models/tencent/hy-mt2-1.8b.md) | 2026-05-21 | 已完成 | 11/11 | 2026-11-05T05:37+08:00 |
| [tencent/hy-mt2-30b-a3b](models/tencent/hy-mt2-30b-a3b.md) | 2026-05-21 | 已完成 | 11/11 | 2026-11-05T05:37+08:00 |
| [tencent/hy-mt2-7b](models/tencent/hy-mt2-7b.md) | 2026-05-21 | 已完成 | 11/11 | 2026-11-05T05:37+08:00 |
| [cohere/command-a-plus-05-2026](models/cohere/command-a-plus-05-2026.md) | 2026-05-20 | 待复核 | 11/11 | 2026-11-05T05:58+08:00 |
| [google/gemini-3.5-flash](models/google/gemini-3.5-flash.md) | 2026-05-19 | 待复核 | 11/11 | 2026-11-05T05:58+08:00 |
| [openbmb/minicpm5-1b](models/openbmb/minicpm5-1b.md) | 2026-05-19 | 待复核 | 11/11 | 2026-11-05T05:58+08:00 |
| [xai/grok-build-0.1](models/xai/grok-build-0.1.md) | 2026-05-19 | 待复核 | 11/11 | 2026-11-05T09:36+08:00 |
| [aion-labs/aion-3.0-mini](models/aion-labs/aion-3.0-mini.md) | 2026-05-14 | 待复核 | 11/11 | 2026-11-05T06:01+08:00 |
| [recraft/recraft-v4.1](models/recraft/recraft-v4.1.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:01+08:00 |
| [recraft/recraft-v4.1-pro](models/recraft/recraft-v4.1-pro.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:01+08:00 |
| [recraft/recraft-v4.1-pro-vector](models/recraft/recraft-v4.1-pro-vector.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:05+08:00 |
| [recraft/recraft-v4.1-utility](models/recraft/recraft-v4.1-utility.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:05+08:00 |
| [recraft/recraft-v4.1-utility-pro](models/recraft/recraft-v4.1-utility-pro.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:05+08:00 |
| [recraft/recraft-v4.1-utility-pro-vector](models/recraft/recraft-v4.1-utility-pro-vector.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:06+08:00 |
| [recraft/recraft-v4.1-utility-vector](models/recraft/recraft-v4.1-utility-vector.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:06+08:00 |
| [recraft/recraft-v4.1-vector](models/recraft/recraft-v4.1-vector.md) | 2026-05-14 | 已完成 | 11/11 | 2026-11-05T06:06+08:00 |
| [krea/krea-2-large](models/krea/krea-2-large.md) | 2026-05-12 | 已完成 | 11/11 | 2026-11-05T06:15+08:00 |
| [krea/krea-2-medium](models/krea/krea-2-medium.md) | 2026-05-12 | 已完成 | 11/11 | 2026-11-05T06:15+08:00 |
| [perceptron/perceptron-mk1](models/perceptron/perceptron-mk1.md) | 2026-05-12 | 待复核 | 11/11 | 2026-11-05T06:15+08:00 |
| [google/gemini-3.1-flash-lite](models/google/gemini-3.1-flash-lite.md) | 2026-05-07 | 待复核 | 11/11 | 2026-11-05T06:22+08:00 |
| [openai/gpt-realtime-2](models/openai/gpt-realtime-2.md) | 2026-05-07 | 待复核 | 11/11 | 2026-11-05T06:22+08:00 |
| [openai/gpt-realtime-translate](models/openai/gpt-realtime-translate.md) | 2026-05-07 | 已完成 | 11/11 | 2026-11-05T06:22+08:00 |
| [openai/gpt-realtime-whisper](models/openai/gpt-realtime-whisper.md) | 2026-05-07 | 已完成 | 11/11 | 2026-11-05T06:28+08:00 |
| [baidu/cobuddy](models/baidu/cobuddy.md) | 2026-05-06 | 待复核 | 11/11 | 2026-11-05T06:28+08:00 |
| [aion-labs/aion-3.0](models/aion-labs/aion-3.0.md) | 2026-05-05 | 待复核 | 11/11 | 2026-11-05T06:28+08:00 |
| [inworld/inworld-tts-2](models/inworld/inworld-tts-2.md) | 2026-05-05 | 已完成 | 11/11 | 2026-11-05T06:41+08:00 |
| [openai/gpt-5.5-instant](models/openai/gpt-5.5-instant.md) | 2026-05-05 | 待复核 | 11/11 | 2026-11-05T06:41+08:00 |
| [mistral/mistral-medium-latest](models/mistral/mistral-medium-latest.md) | 2026-04-29 | 待复核 | 11/11 | 2026-11-05T06:53+08:00 |
| [mistral/mistral-medium-2604](models/mistral/mistral-medium-2604.md) | 2026-04-28 | 待复核 | 11/11 | 2026-11-05T06:53+08:00 |
| [mistral/mistral-medium-3-5](models/mistral/mistral-medium-3-5.md) | 2026-04-28 | 待复核 | 11/11 | 2026-11-05T06:41+08:00 |
| [nvidia/nemotron-3-nano-omni-30b-a3b-reasoning](models/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning.md) | 2026-04-28 | 待复核 | 11/11 | 2026-11-05T06:53+08:00 |
| [poolside/laguna-m.1](models/poolside/laguna-m.1.md) | 2026-04-28 | 待复核 | 11/11 | 2026-11-05T07:03+08:00 |
| [poolside/laguna-xs.2](models/poolside/laguna-xs.2.md) | 2026-04-28 | 待复核 | 11/11 | 2026-11-05T07:03+08:00 |
| [alibaba/qwen3.6-flash](models/alibaba/qwen3.6-flash.md) | 2026-04-27 | 待复核 | 11/11 | 2026-11-05T07:03+08:00 |
| [deepseek/deepseek-v4-flash](models/deepseek/deepseek-v4-flash.md) | 2026-04-24 | 待复核 | 11/11 | 2026-11-05T07:18+08:00 |
| [deepseek/deepseek-v4-pro](models/deepseek/deepseek-v4-pro.md) | 2026-04-24 | 待复核 | 11/11 | 2026-11-05T07:18+08:00 |
| [deepseek/deepseek-v4-flash-0423](models/deepseek/deepseek-v4-flash-0423.md) | 2026-04-23 | 待复核 | 11/11 | 2026-11-05T07:18+08:00 |
| [deepseek/deepseek-v4-pro-0423](models/deepseek/deepseek-v4-pro-0423.md) | 2026-04-23 | 待复核 | 11/11 | 2026-11-05T07:34+08:00 |
| [openai/gpt-5.5](models/openai/gpt-5.5.md) | 2026-04-23 | 待复核 | 11/11 | 2026-11-05T07:39+08:00 |
| [openai/gpt-5.5-pro](models/openai/gpt-5.5-pro.md) | 2026-04-23 | 待复核 | 11/11 | 2026-11-05T07:34+08:00 |
| [xiaomi/mimo-v2.5-asr](models/xiaomi/mimo-v2.5-asr.md) | 2026-04-23 | 已完成 | 11/11 | 2026-11-05T07:50+08:00 |
| [alibaba/happyhorse-1.0](models/alibaba/happyhorse-1.0.md) | 2026-04-22 | 已完成 | 11/11 | 2026-11-05T07:51+08:00 |
| [alibaba/qwen3.6-27b](models/alibaba/qwen3.6-27b.md) | 2026-04-22 | 待复核 | 11/11 | 2026-11-05T07:53+08:00 |
| [google/gemini-embedding-2](models/google/gemini-embedding-2.md) | 2026-04-22 | 已完成 | 11/11 | 2026-11-05T08:05+08:00 |
| [xiaomi/mimo-v2.5](models/xiaomi/mimo-v2.5.md) | 2026-04-22 | 待复核 | 11/11 | 2026-11-05T08:19+08:00 |
| [xiaomi/mimo-v2.5-pro](models/xiaomi/mimo-v2.5-pro.md) | 2026-04-22 | 待复核 | 11/11 | 2026-11-05T08:19+08:00 |
| [xiaomi/mimo-v2.5-tts](models/xiaomi/mimo-v2.5-tts.md) | 2026-04-22 | 已完成 | 11/11 | 2026-11-05T08:15+08:00 |
| [xiaomi/mimo-v2.5-tts-voiceclone](models/xiaomi/mimo-v2.5-tts-voiceclone.md) | 2026-04-22 | 已完成 | 11/11 | 2026-11-05T08:15+08:00 |
| [xiaomi/mimo-v2.5-tts-voicedesign](models/xiaomi/mimo-v2.5-tts-voicedesign.md) | 2026-04-22 | 已完成 | 11/11 | 2026-11-05T08:16+08:00 |
| [google/deep-research-max-preview-04-2026](models/google/deep-research-max-preview-04-2026.md) | 2026-04-21 | 待复核 | 11/11 | 2026-11-05T08:23+08:00 |
| [google/deep-research-preview-04-2026](models/google/deep-research-preview-04-2026.md) | 2026-04-21 | 待复核 | 11/11 | 2026-11-05T08:24+08:00 |
| [openai/gpt-5.4-image-2](models/openai/gpt-5.4-image-2.md) | 2026-04-21 | 待复核 | 11/11 | 2026-11-05T08:25+08:00 |
| [openai/gpt-image-2](models/openai/gpt-image-2.md) | 2026-04-21 | 已完成 | 11/11 | 2026-11-05T08:31+08:00 |
| [alibaba/qwen3.6-max-preview](models/alibaba/qwen3.6-max-preview.md) | 2026-04-20 | 待复核 | 11/11 | 2026-11-05T08:46+08:00 |
| [moonshotai/kimi-k2.6](models/moonshotai/kimi-k2.6.md) | 2026-04-20 | 待复核 | 11/11 | 2026-11-05T08:46+08:00 |
| [tencent/hy3-preview](models/tencent/hy3-preview.md) | 2026-04-20 | 待复核 | 11/11 | 2026-11-05T08:48+08:00 |
| [alibaba/qwen3.6-35b-a3b](models/alibaba/qwen3.6-35b-a3b.md) | 2026-04-17 | 待复核 | 11/11 | 2026-11-05T08:49+08:00 |
| [xai/grok-4.3](models/xai/grok-4.3.md) | 2026-04-17 | 待复核 | 11/11 | 2026-11-05T08:50+08:00 |
| [anthropic/claude-opus-4-7](models/anthropic/claude-opus-4-7.md) | 2026-04-16 | 待复核 | 11/11 | 2026-11-05T08:57+08:00 |
| [inference-net/schematron-v2-small](models/inference-net/schematron-v2-small.md) | 2026-04-16 | 已完成 | 11/11 | 2026-11-05T08:57+08:00 |
| [inference-net/schematron-v2-turbo](models/inference-net/schematron-v2-turbo.md) | 2026-04-16 | 已完成 | 11/11 | 2026-11-05T08:58+08:00 |
| [google/gemini-3.1-flash-tts-preview](models/google/gemini-3.1-flash-tts-preview.md) | 2026-04-15 | 已完成 | 11/11 | 2026-11-05T09:37+08:00 |
| [google/gemini-robotics-er-1.6-preview](models/google/gemini-robotics-er-1.6-preview.md) | 2026-04-14 | 待复核 | 11/11 | 2026-11-05T09:38+08:00 |
| [zhipuai/glm-5.1](models/zhipuai/glm-5.1.md) | 2026-04-07 | 待复核 | 11/11 | 2026-11-05T09:48+08:00 |
| [alibaba/wan2.7](models/alibaba/wan2.7.md) | 2026-04-03 | 已完成 | 11/11 | 2026-11-05T09:49+08:00 |
| [xai/grok-imagine-image-quality](models/xai/grok-imagine-image-quality.md) | 2026-04-03 | 已完成 | 11/11 | 2026-11-05T09:54+08:00 |
| [alibaba/qwen3.6-plus](models/alibaba/qwen3.6-plus.md) | 2026-04-02 | 待复核 | 11/11 | 2026-11-05T10:00+08:00 |
| [stepfun/step-3.5-flash-2603](models/stepfun/step-3.5-flash-2603.md) | 2026-04-02 | 待复核 | 11/11 | 2026-11-05T10:07+08:00 |
| [arcee-ai/trinity-large-thinking](models/arcee-ai/trinity-large-thinking.md) | 2026-04-01 | 待复核 | 11/11 | 2026-11-05T10:13+08:00 |
| [zhipuai/glm-5v-turbo](models/zhipuai/glm-5v-turbo.md) | 2026-04-01 | 待复核 | 11/11 | 2026-11-05T10:15+08:00 |
| [google/gemma-4-26b-a4b-it](models/google/gemma-4-26b-a4b-it.md) | 2026-03-31 | 待复核 | 11/11 | 2026-11-05T10:19+08:00 |
| [google/gemma-4-31b-it](models/google/gemma-4-31b-it.md) | 2026-03-31 | 待复核 | 11/11 | 2026-11-05T10:28+08:00 |
| [google/gemma-4-E2B-it](models/google/gemma-4-E2B-it.md) | 2026-03-31 | 待复核 | 11/11 | 2026-11-05T10:29+08:00 |
| [google/gemma-4-E4B-it](models/google/gemma-4-E4B-it.md) | 2026-03-31 | 待复核 | 11/11 | 2026-11-05T10:31+08:00 |
| [google/veo-3.1-lite-generate-preview](models/google/veo-3.1-lite-generate-preview.md) | 2026-03-31 | 已完成 | 11/11 | 2026-11-05T10:32+08:00 |
| [inception/mercury-edit-2](models/inception/mercury-edit-2.md) | 2026-03-30 | 待复核 | 11/11 | 2026-11-05T10:33+08:00 |
| [k2-fsa/omnivoice](models/k2-fsa/omnivoice.md) | 2026-03-30 | 已完成 | 11/11 | 2026-11-05T10:34+08:00 |
| [cohere/cohere-transcribe-03-2026](models/cohere/cohere-transcribe-03-2026.md) | 2026-03-26 | 已完成 | 11/11 | 2026-11-05T10:38+08:00 |
| [google/gemini-3.1-flash-live-preview](models/google/gemini-3.1-flash-live-preview.md) | 2026-03-26 | 待复核 | 11/11 | 2026-11-05T10:40+08:00 |
| [google/lyria-3-clip-preview](models/google/lyria-3-clip-preview.md) | 2026-03-25 | 已完成 | 11/11 | 2026-11-05T10:42+08:00 |
| [google/lyria-3-pro-preview](models/google/lyria-3-pro-preview.md) | 2026-03-25 | 已完成 | 11/11 | 2026-11-05T10:44+08:00 |
| [mistral/voxtral-mini-tts-2603](models/mistral/voxtral-mini-tts-2603.md) | 2026-03-23 | 已完成 | 11/11 | 2026-11-05T10:45+08:00 |
| [nvidia/nemotron-cascade-2-30b-a3b](models/nvidia/nemotron-cascade-2-30b-a3b.md) | 2026-03-19 | 待复核 | 11/11 | 2026-11-05T10:51+08:00 |
| [minimax/MiniMax-M2.7](models/minimax/MiniMax-M2.7.md) | 2026-03-18 | 待复核 | 11/11 | 2026-11-05T11:00+08:00 |
| [minimax/MiniMax-M2.7-highspeed](models/minimax/MiniMax-M2.7-highspeed.md) | 2026-03-18 | 待复核 | 11/11 | 2026-11-05T11:03+08:00 |
| [xiaomi/mimo-v2-omni](models/xiaomi/mimo-v2-omni.md) | 2026-03-18 | 待复核 | 11/11 | 2026-11-05T11:05+08:00 |
| [xiaomi/mimo-v2-pro](models/xiaomi/mimo-v2-pro.md) | 2026-03-18 | 待复核 | 11/11 | 2026-11-05T11:16+08:00 |
| [xiaomi/mimo-v2-tts](models/xiaomi/mimo-v2-tts.md) | 2026-03-18 | 已完成 | 11/11 | 2026-11-05T11:16+08:00 |
| [openai/gpt-5.4-mini](models/openai/gpt-5.4-mini.md) | 2026-03-17 | 待复核 | 11/11 | 2026-11-05T11:16+08:00 |
| [openai/gpt-5.4-nano](models/openai/gpt-5.4-nano.md) | 2026-03-17 | 待复核 | 11/11 | 2026-11-05T11:27+08:00 |
| [mistral/mistral-small-2603](models/mistral/mistral-small-2603.md) | 2026-03-16 | 待复核 | 11/11 | 2026-11-05T11:27+08:00 |
| [mistral/mistral-small-latest](models/mistral/mistral-small-latest.md) | 2026-03-16 | 待复核 | 11/11 | 2026-11-05T11:27+08:00 |
| [nvidia/nemotron-3-content-safety](models/nvidia/nemotron-3-content-safety.md) | 2026-03-16 | 已完成 | 11/11 | 2026-11-05T11:33+08:00 |
| [nvidia/nemotron-voicechat](models/nvidia/nemotron-voicechat.md) | 2026-03-16 | 待复核 | 11/11 | 2026-11-05T11:33+08:00 |
| [xai/grok-tts](models/xai/grok-tts.md) | 2026-03-16 | 已完成 | 11/11 | 2026-11-05T11:33+08:00 |
| [zhipuai/glm-5-turbo](models/zhipuai/glm-5-turbo.md) | 2026-03-16 | 待复核 | 11/11 | 2026-11-05T11:45+08:00 |
| [nvidia/nemotron-3-super-120b-a12b](models/nvidia/nemotron-3-super-120b-a12b.md) | 2026-03-11 | 待复核 | 11/11 | 2026-11-05T11:45+08:00 |
| [rekaai/reka-edge](models/rekaai/reka-edge.md) | 2026-03-11 | 待复核 | 11/11 | 2026-11-05T11:45+08:00 |
| [google/gemini-embedding-2-preview](models/google/gemini-embedding-2-preview.md) | 2026-03-10 | 已完成 | 11/11 | 2026-11-05T11:57+08:00 |
| [xai/grok-4.20-0309-non-reasoning](models/xai/grok-4.20-0309-non-reasoning.md) | 2026-03-09 | 待复核 | 11/11 | 2026-11-05T11:57+08:00 |
| [xai/grok-4.20-0309-reasoning](models/xai/grok-4.20-0309-reasoning.md) | 2026-03-09 | 待复核 | 11/11 | 2026-11-05T11:57+08:00 |
| [openai/gpt-5.4](models/openai/gpt-5.4.md) | 2026-03-05 | 待复核 | 11/11 | 2026-11-05T12:12+08:00 |
| [openai/gpt-5.4-pro](models/openai/gpt-5.4-pro.md) | 2026-03-05 | 待复核 | 11/11 | 2026-11-05T12:12+08:00 |
| [google/gemini-3.1-flash-lite-preview](models/google/gemini-3.1-flash-lite-preview.md) | 2026-03-03 | 待复核 | 11/11 | 2026-11-05T12:12+08:00 |
| openai/gpt-5.3-chat-latest | 2026-03-03 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-0.8b | 2026-03-02 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-2b | 2026-03-02 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-4b | 2026-03-02 | 未开始 | 0/11 | — |
| mistral/mistral-moderation-2603 | 2026-03-01 | 未开始 | 0/11 | — |
| fish-audio/s2-pro | 2026-03 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-9b-base | 2026-02-26 | 未开始 | 0/11 | — |
| google/gemini-3.1-flash-image | 2026-02-26 | 未开始 | 0/11 | — |
| google/gemini-3.1-flash-image-preview | 2026-02-26 | 未开始 | 0/11 | — |
| perplexity/pplx-embed-context-v1-0.6b | 2026-02-26 | 未开始 | 0/11 | — |
| perplexity/pplx-embed-context-v1-4b | 2026-02-26 | 未开始 | 0/11 | — |
| perplexity/pplx-embed-v1-0.6b | 2026-02-26 | 未开始 | 0/11 | — |
| perplexity/pplx-embed-v1-4b | 2026-02-26 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-35b-a3b-base | 2026-02-24 | 未开始 | 0/11 | — |
| inception/mercury-2 | 2026-02-24 | 未开始 | 0/11 | — |
| liquid/lfm2-24b-a2b | 2026-02-24 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-122b-a10b | 2026-02-23 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-27b | 2026-02-23 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-35b-a3b | 2026-02-23 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-9b | 2026-02-23 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-flash | 2026-02-23 | 未开始 | 0/11 | — |
| openai/gpt-audio-1.5 | 2026-02-23 | 未开始 | 0/11 | — |
| openai/gpt-realtime-1.5 | 2026-02-23 | 未开始 | 0/11 | — |
| google/gemini-3.1-pro-preview | 2026-02-19 | 未开始 | 0/11 | — |
| google/gemini-3.1-pro-preview-customtools | 2026-02-19 | 未开始 | 0/11 | — |
| trendyol/asure-12b | 2026-02-19 | 未开始 | 0/11 | — |
| sarvam/sarvam-105b | 2026-02-18 | 未开始 | 0/11 | — |
| sarvam/sarvam-30b | 2026-02-18 | 未开始 | 0/11 | — |
| anthropic/claude-sonnet-4-6 | 2026-02-17 | 未开始 | 0/11 | — |
| cohere/tiny-aya-earth | 2026-02-17 | 未开始 | 0/11 | — |
| cohere/tiny-aya-fire | 2026-02-17 | 未开始 | 0/11 | — |
| cohere/tiny-aya-global | 2026-02-17 | 未开始 | 0/11 | — |
| cohere/tiny-aya-water | 2026-02-17 | 未开始 | 0/11 | — |
| recraft/recraft-v4 | 2026-02-17 | 未开始 | 0/11 | — |
| recraft/recraft-v4-pro | 2026-02-17 | 未开始 | 0/11 | — |
| recraft/recraft-v4-pro-vector | 2026-02-17 | 未开始 | 0/11 | — |
| recraft/recraft-v4-vector | 2026-02-17 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-plus | 2026-02-16 | 未开始 | 0/11 | — |
| alibaba/qwen3.5-397b-a17b | 2026-02-15 | 未开始 | 0/11 | — |
| bytedance-seed/seed-2.0-code | 2026-02-14 | 未开始 | 0/11 | — |
| bytedance-seed/seed-2.0-lite | 2026-02-14 | 未开始 | 0/11 | — |
| bytedance-seed/seed-2.0-mini | 2026-02-14 | 未开始 | 0/11 | — |
| bytedance-seed/seed-2.0-pro | 2026-02-14 | 未开始 | 0/11 | — |
| bytedance-seed/seedream-5.0-lite | 2026-02-13 | 未开始 | 0/11 | — |
| minimax/MiniMax-M2.5-highspeed | 2026-02-13 | 未开始 | 0/11 | — |
| bytedance-seed/seedance-2.0 | 2026-02-12 | 未开始 | 0/11 | — |
| bytedance-seed/seedance-2.0-fast | 2026-02-12 | 未开始 | 0/11 | — |
| minimax/MiniMax-M2.5 | 2026-02-12 | 未开始 | 0/11 | — |
| zhipuai/glm-5 | 2026-02-12 | 未开始 | 0/11 | — |
| elevenlabs/eleven_v3_conversational | 2026-02-09 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-6 | 2026-02-05 | 未开始 | 0/11 | — |
| kuaishou/kling-v3.0-pro | 2026-02-05 | 未开始 | 0/11 | — |
| kuaishou/kling-v3.0-std | 2026-02-05 | 未开始 | 0/11 | — |
| openai/gpt-5.3-codex | 2026-02-05 | 未开始 | 0/11 | — |
| openai/gpt-5.3-codex-spark | 2026-02-05 | 未开始 | 0/11 | — |
| mistral/voxtral-mini-2602 | 2026-02-04 | 未开始 | 0/11 | — |
| mistral/voxtral-mini-transcribe-realtime-2602 | 2026-02-04 | 未开始 | 0/11 | — |
| alibaba/qwen3-coder-next | 2026-02-03 | 未开始 | 0/11 | — |
| assemblyai/universal-3-pro | 2026-02-03 | 未开始 | 0/11 | — |
| sourceful/riverflow-v2-fast | 2026-02-02 | 未开始 | 0/11 | — |
| sourceful/riverflow-v2-pro | 2026-02-02 | 未开始 | 0/11 | — |
| stepfun/step-3.5-flash | 2026-01-29 | 未开始 | 0/11 | — |
| xai/grok-imagine-image | 2026-01-28 | 未开始 | 0/11 | — |
| xai/grok-imagine-video | 2026-01-28 | 未开始 | 0/11 | — |
| arcee-ai/trinity-large-preview | 2026-01-27 | 未开始 | 0/11 | — |
| deepseek/deepseek-ocr-2 | 2026-01-27 | 未开始 | 0/11 | — |
| moonshotai/kimi-k2.5 | 2026-01-27 | 未开始 | 0/11 | — |
| upstage/solar-pro3 | 2026-01-26 | 未开始 | 0/11 | — |
| minimax/MiniMax-M2-Her | 2026-01-23 | 未开始 | 0/11 | — |
| minimax/speech-2.8-hd | 2026-01-23 | 未开始 | 0/11 | — |
| minimax/speech-2.8-turbo | 2026-01-23 | 未开始 | 0/11 | — |
| nvidia/nemotron-content-safety-reasoning-4b | 2026-01-22 | 未开始 | 0/11 | — |
| inworld/inworld-tts-1.5-max | 2026-01-21 | 未开始 | 0/11 | — |
| inworld/inworld-tts-1.5-mini | 2026-01-21 | 未开始 | 0/11 | — |
| zhipuai/glm-4.7-flash | 2026-01-19 | 未开始 | 0/11 | — |
| zhipuai/glm-4.7-flashx | 2026-01-19 | 未开始 | 0/11 | — |
| black-forest-labs/flux-2-klein-4b | 2026-01-15 | 未开始 | 0/11 | — |
| black-forest-labs/flux-2-klein-9b | 2026-01-15 | 未开始 | 0/11 | — |
| voyageai/voyage-4 | 2026-01-15 | 未开始 | 0/11 | — |
| voyageai/voyage-4-large | 2026-01-15 | 未开始 | 0/11 | — |
| voyageai/voyage-4-lite | 2026-01-15 | 未开始 | 0/11 | — |
| voyageai/voyage-multimodal-3.5 | 2026-01-15 | 未开始 | 0/11 | — |
| zhipuai/glm-image | 2026-01-14 | 未开始 | 0/11 | — |
| elevenlabs/scribe_v2 | 2026-01-12 | 未开始 | 0/11 | — |
| ai21/jamba-mini | 2026-01-08 | 未开始 | 0/11 | — |
| alibaba/qwen3-asr-0.6b | 2026-01 | 未开始 | 0/11 | — |
| alibaba/qwen3-asr-1.7b | 2026-01 | 未开始 | 0/11 | — |
| bytedance-seed/seed-1-8 | 2025-12-28 | 未开始 | 0/11 | — |
| minimax/MiniMax-M2.1 | 2025-12-23 | 未开始 | 0/11 | — |
| zhipuai/glm-4.7 | 2025-12-22 | 未开始 | 0/11 | — |
| aion-labs/aion-2.0 | 2025-12-21 | 未开始 | 0/11 | — |
| canopylabs/orpheus-v1-english | 2025-12-19 | 未开始 | 0/11 | — |
| mistral/mistral-ocr-2512 | 2025-12-18 | 未开始 | 0/11 | — |
| nvidia/llama-nemotron-embed-vl-1b-v2 | 2025-12-18 | 未开始 | 0/11 | — |
| nvidia/llama-nemotron-rerank-vl-1b-v2 | 2025-12-18 | 未开始 | 0/11 | — |
| xai/grok-4-fast-non-reasoning | 2025-12-18 | 未开始 | 0/11 | — |
| xai/grok-4-fast-reasoning | 2025-12-18 | 未开始 | 0/11 | — |
| google/gemini-3-flash-preview | 2025-12-17 | 未开始 | 0/11 | — |
| black-forest-labs/flux-2-max | 2025-12-16 | 未开始 | 0/11 | — |
| bytedance-seed/seedance-1.5-pro | 2025-12-16 | 未开始 | 0/11 | — |
| canopylabs/orpheus-arabic-saudi | 2025-12-16 | 未开始 | 0/11 | — |
| xiaomi/mimo-v2-flash | 2025-12-16 | 未开始 | 0/11 | — |
| nvidia/nemotron-3-nano-30b-a3b | 2025-12-15 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-native-audio-preview-12-2025 | 2025-12-12 | 未开始 | 0/11 | — |
| cohere/rerank-v4.0-fast | 2025-12-11 | 未开始 | 0/11 | — |
| cohere/rerank-v4.0-pro | 2025-12-11 | 未开始 | 0/11 | — |
| openai/gpt-5.2 | 2025-12-11 | 未开始 | 0/11 | — |
| openai/gpt-5.2-chat-latest | 2025-12-11 | 未开始 | 0/11 | — |
| openai/gpt-5.2-codex | 2025-12-11 | 未开始 | 0/11 | — |
| openai/gpt-5.2-pro | 2025-12-11 | 未开始 | 0/11 | — |
| zhipuai/autoglm-phone-9b-multilingual | 2025-12-10 | 未开始 | 0/11 | — |
| zhipuai/glm-asr-2512 | 2025-12-10 | 未开始 | 0/11 | — |
| mistral/devstral-2512 | 2025-12-09 | 未开始 | 0/11 | — |
| mistral/devstral-small-2 | 2025-12-09 | 未开始 | 0/11 | — |
| relace/relace-search | 2025-12-08 | 未开始 | 0/11 | — |
| zhipuai/glm-4.6v | 2025-12-08 | 未开始 | 0/11 | — |
| zhipuai/glm-4.6v-flash | 2025-12-08 | 未开始 | 0/11 | — |
| essentialai/rnj-1-instruct | 2025-12-04 | 未开始 | 0/11 | — |
| alibaba/wan2.6 | 2025-12-03 | 未开始 | 0/11 | — |
| bytedance-seed/seedream-4.5 | 2025-12-03 | 未开始 | 0/11 | — |
| amazon/nova-2-lite | 2025-12-02 | 未开始 | 0/11 | — |
| amazon/nova-2-lite-v1 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/devstral-medium-latest | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-14b | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-14b-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-3-14b-instruct-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-3-3b-instruct-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-3-8b-instruct-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-3b-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/ministral-8b-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| mistral/mistral-large-2512 | 2025-12-02 | 未开始 | 0/11 | — |
| arcee-ai/trinity-mini | 2025-12-01 | 未开始 | 0/11 | — |
| arcee-ai/trinity-nano-preview | 2025-12-01 | 未开始 | 0/11 | — |
| deepseek/deepseek-chat | 2025-12-01 | 未开始 | 0/11 | — |
| deepseek/deepseek-reasoner | 2025-12-01 | 未开始 | 0/11 | — |
| deepseek/deepseek-v3.2 | 2025-12-01 | 未开始 | 0/11 | — |
| kuaishou/kling-video-o1 | 2025-12-01 | 未开始 | 0/11 | — |
| runway/gen-4.5 | 2025-12-01 | 未开始 | 0/11 | — |
| runwayml/gen-4.5 | 2025-12-01 | 未开始 | 0/11 | — |
| black-forest-labs/flux-2-dev | 2025-11-25 | 未开始 | 0/11 | — |
| black-forest-labs/flux-2-flex | 2025-11-25 | 未开始 | 0/11 | — |
| black-forest-labs/flux-2-pro | 2025-11-25 | 未开始 | 0/11 | — |
| openai/gpt-image-1.5 | 2025-11-25 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-5 | 2025-11-24 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-5-20251101 | 2025-11-24 | 未开始 | 0/11 | — |
| google/gemini-3-pro-image | 2025-11-20 | 未开始 | 0/11 | — |
| google/gemini-3-pro-image-preview | 2025-11-20 | 未开始 | 0/11 | — |
| xai/grok-4.1-fast | 2025-11-19 | 未开始 | 0/11 | — |
| xai/grok-4.1-fast-reasoning | 2025-11-19 | 未开始 | 0/11 | — |
| google/gemini-3-pro-preview | 2025-11-18 | 未开始 | 0/11 | — |
| openai/gpt-5.1 | 2025-11-13 | 未开始 | 0/11 | — |
| openai/gpt-5.1-chat-latest | 2025-11-13 | 未开始 | 0/11 | — |
| openai/gpt-5.1-codex | 2025-11-13 | 未开始 | 0/11 | — |
| openai/gpt-5.1-codex-max | 2025-11-13 | 未开始 | 0/11 | — |
| openai/gpt-5.1-codex-mini | 2025-11-13 | 未开始 | 0/11 | — |
| moonshotai/kimi-k2-thinking | 2025-11-06 | 未开始 | 0/11 | — |
| moonshotai/kimi-k2-thinking-turbo | 2025-11-06 | 未开始 | 0/11 | — |
| openai/gpt-oss-safeguard-120b | 2025-10-29 | 未开始 | 0/11 | — |
| openai/gpt-oss-safeguard-20b | 2025-10-29 | 未开始 | 0/11 | — |
| minimax/MiniMax-Hailuo-2.3 | 2025-10-28 | 未开始 | 0/11 | — |
| minimax/MiniMax-Hailuo-2.3-Fast | 2025-10-28 | 未开始 | 0/11 | — |
| nvidia/llama-3.1-nemotron-safety-guard-8b-v3 | 2025-10-28 | 未开始 | 0/11 | — |
| nvidia/nemotron-nano-12b-v2-vl | 2025-10-28 | 未开始 | 0/11 | — |
| minimax/MiniMax-M2 | 2025-10-27 | 未开始 | 0/11 | — |
| openai/gpt-4o-transcribe-diarize | 2025-10-17 | 未开始 | 0/11 | — |
| nvidia/llama-nemotron-embed-1b-v2 | 2025-10-16 | 未开始 | 0/11 | — |
| openai/gpt-5-image-mini | 2025-10-16 | 未开始 | 0/11 | — |
| paddlepaddle/paddleocr-vl | 2025-10-16 | 未开始 | 0/11 | — |
| alibaba/qwen3-vl-flash | 2025-10-15 | 未开始 | 0/11 | — |
| anthropic/claude-haiku-4-5 | 2025-10-15 | 未开始 | 0/11 | — |
| anthropic/claude-haiku-4-5-20251001 | 2025-10-15 | 未开始 | 0/11 | — |
| bytedance-seed/seed-1-6 | 2025-10-15 | 未开始 | 0/11 | — |
| google/veo-3.1-fast-generate-preview | 2025-10-15 | 未开始 | 0/11 | — |
| google/veo-3.1-generate-preview | 2025-10-15 | 未开始 | 0/11 | — |
| openai/gpt-5-image | 2025-10-14 | 未开始 | 0/11 | — |
| openai/gpt-5-search-api | 2025-10-14 | 未开始 | 0/11 | — |
| google/gemini-2.5-computer-use-preview-10-2025 | 2025-10-07 | 未开始 | 0/11 | — |
| openai/gpt-5-pro | 2025-10-06 | 未开始 | 0/11 | — |
| openai/gpt-audio-mini | 2025-10-06 | 未开始 | 0/11 | — |
| openai/gpt-image-1-mini | 2025-10-06 | 未开始 | 0/11 | — |
| openai/gpt-realtime-mini | 2025-10-06 | 未开始 | 0/11 | — |
| alibaba/qwen3-vl-30b-a3b-instruct | 2025-10-04 | 未开始 | 0/11 | — |
| ibm/granite-4-h-micro | 2025-10-02 | 未开始 | 0/11 | — |
| ibm/granite-4-h-small | 2025-10-02 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-tts | 2025-09-30 | 未开始 | 0/11 | — |
| google/gemini-2.5-pro-tts | 2025-09-30 | 未开始 | 0/11 | — |
| zhipuai/glm-4.6 | 2025-09-30 | 未开始 | 0/11 | — |
| anthropic/claude-sonnet-4-5 | 2025-09-29 | 未开始 | 0/11 | — |
| anthropic/claude-sonnet-4-5-20250929 | 2025-09-29 | 未开始 | 0/11 | — |
| thedrummer/cydonia-24b-v4.1 | 2025-09-27 | 未开始 | 0/11 | — |
| relace/relace-apply-3 | 2025-09-26 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-lite-preview-09-2025 | 2025-09-25 | 未开始 | 0/11 | — |
| aisingapore/gemma-sea-lion-v4-27b-it | 2025-09-23 | 未开始 | 0/11 | — |
| alibaba/qwen3-max | 2025-09-23 | 未开始 | 0/11 | — |
| alibaba/qwen3-vl-235b-a22b-instruct | 2025-09-23 | 未开始 | 0/11 | — |
| alibaba/qwen3-vl-235b-a22b-thinking | 2025-09-23 | 未开始 | 0/11 | — |
| alibaba/qwen3-vl-plus | 2025-09-23 | 未开始 | 0/11 | — |
| alibaba/qwen3-omni-30b-a3b-thinking | 2025-09-22 | 未开始 | 0/11 | — |
| mistral/magistral-small-2509 | 2025-09-18 | 未开始 | 0/11 | — |
| openai/gpt-5-codex | 2025-09-15 | 未开始 | 0/11 | — |
| alibaba/qwen3-max-preview | 2025-09-05 | 未开始 | 0/11 | — |
| moonshotai/kimi-k2-0905 | 2025-09-05 | 未开始 | 0/11 | — |
| swiss-ai/apertus-70b | 2025-09-02 | 未开始 | 0/11 | — |
| swiss-ai/apertus-8b | 2025-09-02 | 未开始 | 0/11 | — |
| xai/grok-code-fast-1 | 2025-09-02 | 未开始 | 0/11 | — |
| alibaba/qwen3-next-80b-a3b-instruct | 2025-09 | 未开始 | 0/11 | — |
| alibaba/qwen3-next-80b-a3b-thinking | 2025-09 | 未开始 | 0/11 | — |
| fish-audio/transcribe-1 | 2025-09 | 未开始 | 0/11 | — |
| google/chirp-3 | 2025-08-29 | 未开始 | 0/11 | — |
| bytedance-seed/seed-1-6-flash | 2025-08-28 | 未开始 | 0/11 | — |
| cohere/command-a-translate-08-2025 | 2025-08-28 | 未开始 | 0/11 | — |
| openai/gpt-audio | 2025-08-28 | 未开始 | 0/11 | — |
| openai/gpt-realtime | 2025-08-28 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-image | 2025-08-26 | 未开始 | 0/11 | — |
| nousresearch/hermes-4-405b | 2025-08-26 | 未开始 | 0/11 | — |
| cohere/command-a-reasoning-08-2025 | 2025-08-21 | 未开始 | 0/11 | — |
| deepseek/deepseek-chat-v3.1 | 2025-08-21 | 未开始 | 0/11 | — |
| deepseek/deepseek-v3.1 | 2025-08-21 | 未开始 | 0/11 | — |
| bytedance-seed/seed-oss-36b-instruct | 2025-08-20 | 未开始 | 0/11 | — |
| elevenlabs/eleven_v3 | 2025-08-20 | 未开始 | 0/11 | — |
| nvidia/nemotron-nano-9b-v2 | 2025-08-18 | 未开始 | 0/11 | — |
| bytedance-seed/seed-1-6-vision | 2025-08-15 | 未开始 | 0/11 | — |
| baichuan/baichuan-m2-32b | 2025-08-13 | 未开始 | 0/11 | — |
| mistral/mistral-medium-3.1 | 2025-08-12 | 未开始 | 0/11 | — |
| voyageai/rerank-2.5 | 2025-08-11 | 未开始 | 0/11 | — |
| voyageai/rerank-2.5-lite | 2025-08-11 | 未开始 | 0/11 | — |
| zhipuai/glm-4.5v | 2025-08-11 | 未开始 | 0/11 | — |
| openai/gpt-5 | 2025-08-07 | 未开始 | 0/11 | — |
| openai/gpt-5-chat-latest | 2025-08-07 | 未开始 | 0/11 | — |
| openai/gpt-5-mini | 2025-08-07 | 未开始 | 0/11 | — |
| openai/gpt-5-nano | 2025-08-07 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-1 | 2025-08-05 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-1-20250805 | 2025-08-05 | 未开始 | 0/11 | — |
| leonardo/lucid-origin | 2025-08-05 | 未开始 | 0/11 | — |
| openai/gpt-oss-120b | 2025-08-05 | 未开始 | 0/11 | — |
| openai/gpt-oss-20b | 2025-08-05 | 未开始 | 0/11 | — |
| nvidia/parakeet-tdt-0.6b-v3 | 2025-08 | 未开始 | 0/11 | — |
| alibaba/qwen3-coder-30b-a3b-instruct | 2025-07-31 | 未开始 | 0/11 | — |
| cohere/command-a-vision-07-2025 | 2025-07-31 | 未开始 | 0/11 | — |
| mistral/codestral-2508 | 2025-07-30 | 未开始 | 0/11 | — |
| alibaba/qwen-flash | 2025-07-28 | 未开始 | 0/11 | — |
| alibaba/qwen3-30b-a3b-instruct-2507 | 2025-07-28 | 未开始 | 0/11 | — |
| alibaba/qwen3-coder-flash | 2025-07-28 | 未开始 | 0/11 | — |
| zhipuai/glm-4.5 | 2025-07-28 | 未开始 | 0/11 | — |
| zhipuai/glm-4.5-air | 2025-07-28 | 未开始 | 0/11 | — |
| zhipuai/glm-4.5-flash | 2025-07-28 | 未开始 | 0/11 | — |
| alibaba/qwen3-235b-a22b-thinking-2507 | 2025-07-25 | 未开始 | 0/11 | — |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | 2025-07-25 | 未开始 | 0/11 | — |
| alibaba/qwen-mt-plus | 2025-07-24 | 未开始 | 0/11 | — |
| alibaba/qwen3-coder-plus | 2025-07-23 | 未开始 | 0/11 | — |
| alibaba/qwen3-coder-480b-a35b-instruct | 2025-07-22 | 未开始 | 0/11 | — |
| alibaba/qwen3-235b-a22b-instruct-2507 | 2025-07-21 | 未开始 | 0/11 | — |
| mistral/voxtral-mini-3b-2507 | 2025-07-15 | 未开始 | 0/11 | — |
| mistral/voxtral-small-24b-2507 | 2025-07-15 | 未开始 | 0/11 | — |
| mistral/voxtral-small-latest | 2025-07-15 | 未开始 | 0/11 | — |
| zhipuai/cogvideox-3 | 2025-07-15 | 未开始 | 0/11 | — |
| moonshotai/kimi-k2 | 2025-07-11 | 未开始 | 0/11 | — |
| moonshotai/kimi-k2-instruct | 2025-07-11 | 未开始 | 0/11 | — |
| mistral/devstral-medium-2507 | 2025-07-10 | 未开始 | 0/11 | — |
| mistral/devstral-small-2507 | 2025-07-10 | 未开始 | 0/11 | — |
| cognitivecomputations/dolphin-mistral-24b-venice-edition | 2025-07-09 | 未开始 | 0/11 | — |
| morph/morph-v3-fast | 2025-07-07 | 未开始 | 0/11 | — |
| morph/morph-v3-large | 2025-07-07 | 未开始 | 0/11 | — |
| ai21/jamba-large | 2025-07-03 | 未开始 | 0/11 | — |
| baidu/ernie-4.5-21b-a3b | 2025-06-30 | 未开始 | 0/11 | — |
| baidu/ernie-4.5-300b-a47b | 2025-06-30 | 未开始 | 0/11 | — |
| baidu/ernie-4.5-vl-424b-a47b | 2025-06-30 | 未开始 | 0/11 | — |
| google/gemma-3n-e2b-it | 2025-06-26 | 未开始 | 0/11 | — |
| google/gemma-3n-e4b-it | 2025-06-26 | 未开始 | 0/11 | — |
| openai/o3-deep-research | 2025-06-26 | 未开始 | 0/11 | — |
| openai/o4-mini-deep-research | 2025-06-26 | 未开始 | 0/11 | — |
| mistral/mistral-small-2506 | 2025-06-20 | 未开始 | 0/11 | — |
| mistral/mistral-small-3.2-24b-instruct | 2025-06-20 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash | 2025-06-17 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-lite | 2025-06-17 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-lite-preview-06-17 | 2025-06-17 | 未开始 | 0/11 | — |
| google/gemini-2.5-pro | 2025-06-17 | 未开始 | 0/11 | — |
| minimax/minimax-m1-80k | 2025-06-17 | 未开始 | 0/11 | — |
| nvidia/mistral-nemotron | 2025-06-11 | 未开始 | 0/11 | — |
| mistral/magistral-small-2506 | 2025-06-10 | 未开始 | 0/11 | — |
| openai/o3-pro | 2025-06-10 | 未开始 | 0/11 | — |
| alibaba/qwen3-embedding-0.6b | 2025-06-05 | 未开始 | 0/11 | — |
| alibaba/qwen3-embedding-4b | 2025-06-05 | 未开始 | 0/11 | — |
| alibaba/qwen3-embedding-8b | 2025-06-05 | 未开始 | 0/11 | — |
| alibaba/qwen3-reranker-0.6b | 2025-06-05 | 未开始 | 0/11 | — |
| alibaba/qwen3-reranker-8b | 2025-06-05 | 未开始 | 0/11 | — |
| google/gemini-2.5-pro-preview | 2025-06-05 | 未开始 | 0/11 | — |
| fish-audio/s1 | 2025-06 | 未开始 | 0/11 | — |
| black-forest-labs/flux-1-kontext-dev | 2025-05-29 | 未开始 | 0/11 | — |
| black-forest-labs/flux-kontext-max | 2025-05-29 | 未开始 | 0/11 | — |
| black-forest-labs/flux-kontext-pro | 2025-05-29 | 未开始 | 0/11 | — |
| deepseek/deepseek-r1-0528-qwen3-8b | 2025-05-29 | 未开始 | 0/11 | — |
| deepseek/deepseek-r1-0528 | 2025-05-28 | 未开始 | 0/11 | — |
| mistral/codestral-embed-2505 | 2025-05-28 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-0 | 2025-05-22 | 未开始 | 0/11 | — |
| anthropic/claude-opus-4-20250514 | 2025-05-22 | 未开始 | 0/11 | — |
| anthropic/claude-sonnet-4-0 | 2025-05-22 | 未开始 | 0/11 | — |
| anthropic/claude-sonnet-4-20250514 | 2025-05-22 | 未开始 | 0/11 | — |
| google/gemini-2.5-flash-preview-05-20 | 2025-05-20 | 未开始 | 0/11 | — |
| google/gemini-embedding-001 | 2025-05-20 | 未开始 | 0/11 | — |
| google/lyria-realtime-exp | 2025-05-20 | 未开始 | 0/11 | — |
| sarvam/sarvam-m | 2025-05-20 | 未开始 | 0/11 | — |
| upstage/solar-pro2 | 2025-05-20 | 未开始 | 0/11 | — |
| mistral/mistral-medium-2505 | 2025-05-07 | 未开始 | 0/11 | — |
| mistral/mistral-medium-3 | 2025-05-07 | 未开始 | 0/11 | — |
| heygen/avatar-iv | 2025-05 | 未开始 | 0/11 | — |
| amazon/nova-premier | 2025-04-30 | 未开始 | 0/11 | — |
| alibaba/qwen3-8b | 2025-04-29 | 未开始 | 0/11 | — |
| meta/llama-guard-4-12b | 2025-04-29 | 未开始 | 0/11 | — |
| meta/llama-prompt-guard-2-22m | 2025-04-29 | 未开始 | 0/11 | — |
| meta/llama-prompt-guard-2-86m | 2025-04-29 | 未开始 | 0/11 | — |
| alibaba/qwen3-235b-a22b | 2025-04-28 | 未开始 | 0/11 | — |
| alibaba/qwen3-30b-a3b | 2025-04-28 | 未开始 | 0/11 | — |
| alibaba/qwen3-32b | 2025-04-28 | 未开始 | 0/11 | — |
| writer/palmyra-x5 | 2025-04-28 | 未开始 | 0/11 | — |
| openai/gpt-image-1 | 2025-04-24 | 未开始 | 0/11 | — |
| openai/o3 | 2025-04-16 | 未开始 | 0/11 | — |
| openai/o4-mini | 2025-04-16 | 未开始 | 0/11 | — |
| cohere/embed-v4.0 | 2025-04-15 | 未开始 | 0/11 | — |
| deepgram/aura-2 | 2025-04-15 | 未开始 | 0/11 | — |
| nvidia/llama-3.1-nemotron-70b-instruct | 2025-04-15 | 未开始 | 0/11 | — |
| openai/gpt-4.1 | 2025-04-14 | 未开始 | 0/11 | — |
| openai/gpt-4.1-mini | 2025-04-14 | 未开始 | 0/11 | — |
| openai/gpt-4.1-nano | 2025-04-14 | 未开始 | 0/11 | — |
| mistral/pixtral-large-2502 | 2025-04-08 | 未开始 | 0/11 | — |
| nvidia/llama-3.1-nemotron-ultra-253b | 2025-04-07 | 未开始 | 0/11 | — |
| meta/llama-4-maverick-17b-instruct | 2025-04-05 | 未开始 | 0/11 | — |
| meta/llama-4-scout-17b-instruct | 2025-04-05 | 未开始 | 0/11 | — |
| deepseek/deepseek-chat-v3-0324 | 2025-03-24 | 未开始 | 0/11 | — |
| deepseek/deepseek-v3-0324 | 2025-03-24 | 未开始 | 0/11 | — |
| openai/gpt-4o-mini-transcribe | 2025-03-20 | 未开始 | 0/11 | — |
| openai/gpt-4o-mini-tts | 2025-03-20 | 未开始 | 0/11 | — |
| openai/gpt-4o-transcribe | 2025-03-20 | 未开始 | 0/11 | — |
| openai/o1-pro | 2025-03-19 | 未开始 | 0/11 | — |
| nvidia/llama-3.3-nemotron-super-49b-v1 | 2025-03-18 | 未开始 | 0/11 | — |
| mistral/magistral-medium-latest | 2025-03-17 | 未开始 | 0/11 | — |
| mistral/mistral-small-3-1-24b-instruct-2503 | 2025-03-17 | 未开始 | 0/11 | — |
| mistral/mistral-small-3.1-24b-instruct | 2025-03-17 | 未开始 | 0/11 | — |
| cohere/command-a | 2025-03-13 | 未开始 | 0/11 | — |
| cohere/command-a-03-2025 | 2025-03-13 | 未开始 | 0/11 | — |
| google/gemma-3-12b-it | 2025-03-12 | 未开始 | 0/11 | — |
| google/gemma-3-27b-it | 2025-03-12 | 未开始 | 0/11 | — |
| google/gemma-3-4b-it | 2025-03-12 | 未开始 | 0/11 | — |
| rekaai/reka-flash-3 | 2025-03-10 | 未开始 | 0/11 | — |
| thedrummer/skyfall-36b-v2 | 2025-03-10 | 未开始 | 0/11 | — |
| alibaba/qwq-32b | 2025-03-05 | 未开始 | 0/11 | — |
| alibaba/qwq-plus | 2025-03-05 | 未开始 | 0/11 | — |
| cohere/c4ai-aya-vision-32b | 2025-03-04 | 未开始 | 0/11 | — |
| cohere/c4ai-aya-vision-8b | 2025-03-04 | 未开始 | 0/11 | — |
| canopylabs/orpheus-3b-0.1-ft | 2025-03 | 未开始 | 0/11 | — |
| sesame/csm-1b | 2025-03 | 未开始 | 0/11 | — |
| cohere/command-r7b-arabic-02-2025 | 2025-02-27 | 未开始 | 0/11 | — |
| microsoft/phi-4-mini | 2025-02-26 | 未开始 | 0/11 | — |
| microsoft/phi-4-multimodal-instruct | 2025-02-26 | 未开始 | 0/11 | — |
| anthropic/claude-3-7-sonnet-20250219 | 2025-02-19 | 未开始 | 0/11 | — |
| mistral/mistral-saba | 2025-02-17 | 未开始 | 0/11 | — |
| minimax/image-01 | 2025-02-15 | 未开始 | 0/11 | — |
| minimax/image-01-live | 2025-02-15 | 未开始 | 0/11 | — |
| deepgram/nova-3 | 2025-02-12 | 未开始 | 0/11 | — |
| aion-labs/aion-rp-llama-3.1-8b | 2025-02-04 | 未开始 | 0/11 | — |
| perplexity/sonar-deep-research | 2025-02-01 | 未开始 | 0/11 | — |
| mistral/mistral-small-24b-instruct-2501 | 2025-01-30 | 未开始 | 0/11 | — |
| alibaba/qwen2-5-vl-72b-instruct | 2025-01-26 | 未开始 | 0/11 | — |
| sdaia/allam-2-7b | 2025-01-23 | 未开始 | 0/11 | — |
| deepseek/deepseek-r1 | 2025-01-20 | 未开始 | 0/11 | — |
| deepseek/deepseek-r1-distill-qwen-32b | 2025-01-20 | 未开始 | 0/11 | — |
| alibaba/qwen-omni-turbo | 2025-01-19 | 未开始 | 0/11 | — |
| minimax/MiniMax-Text-01 | 2025-01-15 | 未开始 | 0/11 | — |
| deepseek/deepseek-v3 | 2024-12-26 | 未开始 | 0/11 | — |
| openai/o3-mini | 2024-12-20 | 未开始 | 0/11 | — |
| elevenlabs/eleven_flash_v2 | 2024-12-19 | 未开始 | 0/11 | — |
| elevenlabs/eleven_flash_v2_5 | 2024-12-19 | 未开始 | 0/11 | — |
| leonardo/phoenix-1.0 | 2024-12-18 | 未开始 | 0/11 | — |
| sao10k/l3.3-euryale-70b | 2024-12-18 | 未开始 | 0/11 | — |
| cohere/command-r7b-12-2024 | 2024-12-13 | 未开始 | 0/11 | — |
| google/gemini-2.0-flash | 2024-12-11 | 未开始 | 0/11 | — |
| google/gemini-2.0-flash-lite | 2024-12-11 | 未开始 | 0/11 | — |
| meta/llama-3.3-70b-instruct | 2024-12-06 | 未开始 | 0/11 | — |
| amazon/nova-lite-v1 | 2024-12-05 | 未开始 | 0/11 | — |
| amazon/nova-micro-v1 | 2024-12-05 | 未开始 | 0/11 | — |
| amazon/nova-pro-v1 | 2024-12-05 | 未开始 | 0/11 | — |
| openai/o1 | 2024-12-05 | 未开始 | 0/11 | — |
| amazon/nova-lite | 2024-12-03 | 未开始 | 0/11 | — |
| amazon/nova-micro | 2024-12-03 | 未开始 | 0/11 | — |
| amazon/nova-pro | 2024-12-03 | 未开始 | 0/11 | — |
| cohere/rerank-v3.5 | 2024-12-02 | 未开始 | 0/11 | — |
| hexgrad/kokoro-82m | 2024-12 | 未开始 | 0/11 | — |
| openai/gpt-4o-2024-11-20 | 2024-11-20 | 未开始 | 0/11 | — |
| mistral/mistral-large-2411 | 2024-11-18 | 未开始 | 0/11 | — |
| alibaba/qwen2.5-coder-0.5b | 2024-11-12 | 未开始 | 0/11 | — |
| alibaba/qwen2.5-coder-32b-instruct | 2024-11-12 | 未开始 | 0/11 | — |
| thedrummer/unslopnemo-12b | 2024-11-08 | 未开始 | 0/11 | — |
| alibaba/qwen-turbo | 2024-11-01 | 未开始 | 0/11 | — |
| mistral/mistral-large-latest | 2024-11-01 | 未开始 | 0/11 | — |
| mistral/pixtral-large-latest | 2024-11-01 | 未开始 | 0/11 | — |
| recraft/recraft-v3 | 2024-10-30 | 未开始 | 0/11 | — |
| cohere/c4ai-aya-expanse-32b | 2024-10-24 | 未开始 | 0/11 | — |
| cohere/c4ai-aya-expanse-8b | 2024-10-24 | 未开始 | 0/11 | — |
| anthracite-org/magnum-v4-72b | 2024-10-22 | 未开始 | 0/11 | — |
| anthropic/claude-3-5-haiku-20241022 | 2024-10-22 | 未开始 | 0/11 | — |
| anthropic/claude-3-5-sonnet-20241022 | 2024-10-22 | 未开始 | 0/11 | — |
| mistral/ministral-3b | 2024-10-16 | 未开始 | 0/11 | — |
| mistral/ministral-8b-instruct-2410 | 2024-10-16 | 未开始 | 0/11 | — |
| writer/palmyra-x4 | 2024-10-09 | 未开始 | 0/11 | — |
| openai/whisper-large-v3-turbo | 2024-10-01 | 未开始 | 0/11 | — |
| openai/omni-moderation-latest | 2024-09-26 | 未开始 | 0/11 | — |
| meta/llama-3.2-11b-vision-instruct | 2024-09-25 | 未开始 | 0/11 | — |
| meta/llama-3.2-1b | 2024-09-25 | 未开始 | 0/11 | — |
| meta/llama-3.2-1b-instruct | 2024-09-25 | 未开始 | 0/11 | — |
| meta/llama-3.2-3b | 2024-09-25 | 未开始 | 0/11 | — |
| meta/llama-3.2-3b-instruct | 2024-09-25 | 未开始 | 0/11 | — |
| meta/llama-3.2-90b-vision-instruct | 2024-09-25 | 未开始 | 0/11 | — |
| alibaba/qwen2.5-7b-instruct | 2024-09-19 | 未开始 | 0/11 | — |
| mistral/pixtral-12b | 2024-09-11 | 未开始 | 0/11 | — |
| cohere/command-r-08-2024 | 2024-08-30 | 未开始 | 0/11 | — |
| cohere/command-r-plus-08-2024 | 2024-08-30 | 未开始 | 0/11 | — |
| sao10k/l3.1-euryale-70b | 2024-08-28 | 未开始 | 0/11 | — |
| nvidia/nemotron-mini-4b-instruct | 2024-08-21 | 未开始 | 0/11 | — |
| nousresearch/hermes-3-llama-3.1-70b | 2024-08-18 | 未开始 | 0/11 | — |
| nousresearch/hermes-3-llama-3.1-405b | 2024-08-16 | 未开始 | 0/11 | — |
| abacusai/dracarys-llama-3.1-70b-instruct | 2024-08-14 | 未开始 | 0/11 | — |
| sao10k/l3-lunaris-8b | 2024-08-13 | 未开始 | 0/11 | — |
| openai/gpt-4o-2024-08-06 | 2024-08-06 | 未开始 | 0/11 | — |
| black-forest-labs/flux-1-dev | 2024-08-01 | 未开始 | 0/11 | — |
| black-forest-labs/flux-1-schnell | 2024-08-01 | 未开始 | 0/11 | — |
| google/gemma-2-2b-it | 2024-07-31 | 未开始 | 0/11 | — |
| baai/bge-multilingual-gemma2 | 2024-07-25 | 未开始 | 0/11 | — |
| mistral/mistral-large-2407 | 2024-07-24 | 未开始 | 0/11 | — |
| meta/llama-3.1-70b-instruct | 2024-07-23 | 未开始 | 0/11 | — |
| meta/llama-3.1-8b-instruct | 2024-07-23 | 未开始 | 0/11 | — |
| meta/llama-guard-3-8b | 2024-07-23 | 未开始 | 0/11 | — |
| elevenlabs/eleven_turbo_v2_5 | 2024-07-19 | 未开始 | 0/11 | — |
| mistral/mistral-nemo | 2024-07-18 | 未开始 | 0/11 | — |
| openai/gpt-4o-mini | 2024-07-18 | 未开始 | 0/11 | — |
| google/gemma-2-27b-it | 2024-07-13 | 未开始 | 0/11 | — |
| mistral/codestral-22b-v0.1 | 2024-05-29 | 未开始 | 0/11 | — |
| mistral/codestral-latest | 2024-05-29 | 未开始 | 0/11 | — |
| mistral/mistral-7b-instruct-v0.3 | 2024-05-22 | 未开始 | 0/11 | — |
| vispark/vision-large | 2024-05-15 | 未开始 | 0/11 | — |
| vispark/vision-medium | 2024-05-15 | 未开始 | 0/11 | — |
| vispark/vision-small | 2024-05-15 | 未开始 | 0/11 | — |
| openai/gpt-4o | 2024-05-13 | 未开始 | 0/11 | — |
| openai/gpt-4o-2024-05-13 | 2024-05-13 | 未开始 | 0/11 | — |
| nousresearch/hermes-2-pro-llama-3-8b | 2024-04-30 | 未开始 | 0/11 | — |
| alibaba/gte-large-en-v1.5 | 2024-04-20 | 未开始 | 0/11 | — |
| mistral/mixtral-8x22b-instruct | 2024-04-17 | 未开始 | 0/11 | — |
| microsoft/wizardlm-2-8x22b | 2024-04-15 | 未开始 | 0/11 | — |
| cohere/rerank-english-v3.0 | 2024-04-11 | 未开始 | 0/11 | — |
| cohere/rerank-multilingual-v3.0 | 2024-04-11 | 未开始 | 0/11 | — |
| alibaba/qwen-vl-max | 2024-04-08 | 未开始 | 0/11 | — |
| alibaba/qwen-max | 2024-04-03 | 未开始 | 0/11 | — |
| baai/bge-reranker-v2-m3 | 2024-03-15 | 未开始 | 0/11 | — |
| anthropic/claude-3-haiku-20240307 | 2024-03-13 | 未开始 | 0/11 | — |
| mistral/mistral-large | 2024-02-26 | 未开始 | 0/11 | — |
| bytedance-seed/stable-diffusion-xl-lightning | 2024-02-21 | 未开始 | 0/11 | — |
| baai/bge-m3 | 2024-01-30 | 未开始 | 0/11 | — |
| alibaba/qwen-plus | 2024-01-25 | 未开始 | 0/11 | — |
| alibaba/qwen-vl-plus | 2024-01-25 | 未开始 | 0/11 | — |
| openai/text-embedding-3-large | 2024-01-25 | 未开始 | 0/11 | — |
| openai/text-embedding-3-small | 2024-01-25 | 未开始 | 0/11 | — |
| perplexity/sonar | 2024-01-01 | 未开始 | 0/11 | — |
| perplexity/sonar-pro | 2024-01-01 | 未开始 | 0/11 | — |
| perplexity/sonar-reasoning-pro | 2024-01-01 | 未开始 | 0/11 | — |
| upstage/solar-10.7b-instruct-v1.0 | 2023-12-12 | 未开始 | 0/11 | — |
| mistral/mistral-embed | 2023-12-11 | 未开始 | 0/11 | — |
| mistral/mixtral-8x7b-instruct-v0.1 | 2023-12-11 | 未开始 | 0/11 | — |
| lykon/dreamshaper-8-lcm | 2023-12-06 | 未开始 | 0/11 | — |
| elevenlabs/eleven_turbo_v2 | 2023-11-09 | 未开始 | 0/11 | — |
| openai/gpt-4 | 2023-11-06 | 未开始 | 0/11 | — |
| openai/gpt-4-turbo | 2023-11-06 | 未开始 | 0/11 | — |
| openai/tts-1 | 2023-11-06 | 未开始 | 0/11 | — |
| openai/tts-1-hd | 2023-11-06 | 未开始 | 0/11 | — |
| openai/whisper-large-v3 | 2023-11-06 | 未开始 | 0/11 | — |
| cohere/embed-english-light-v3.0 | 2023-11-02 | 未开始 | 0/11 | — |
| cohere/embed-english-v3.0 | 2023-11-02 | 未开始 | 0/11 | — |
| cohere/embed-multilingual-light-v3.0 | 2023-11-02 | 未开始 | 0/11 | — |
| cohere/embed-multilingual-v3.0 | 2023-11-02 | 未开始 | 0/11 | — |
| baai/bge-base-en-v1.5 | 2023-09-12 | 未开始 | 0/11 | — |
| baai/bge-large-en-v1.5 | 2023-09-12 | 未开始 | 0/11 | — |
| elevenlabs/eleven_multilingual_v2 | 2023-08-22 | 未开始 | 0/11 | — |
| gryphe/mythomax-l2-13b | 2023-08-10 | 未开始 | 0/11 | — |
| mancer/weaver | 2023-08-02 | 未开始 | 0/11 | — |
| stabilityai/stable-diffusion-xl-base-1.0 | 2023-07-26 | 未开始 | 0/11 | — |
| undi95/remm-slerp-l2-13b | 2023-07-22 | 未开始 | 0/11 | — |
| thenlper/gte-base | 2023-07 | 未开始 | 0/11 | — |
| thenlper/gte-large | 2023-07 | 未开始 | 0/11 | — |
| intfloat/multilingual-e5-large | 2023-06 | 未开始 | 0/11 | — |
| intfloat/e5-base-v2 | 2023-05 | 未开始 | 0/11 | — |
| intfloat/e5-large-v2 | 2023-05 | 未开始 | 0/11 | — |
| openai/gpt-3.5-turbo | 2023-03-01 | 未开始 | 0/11 | — |
| openai/whisper-1 | 2023-03-01 | 未开始 | 0/11 | — |
| openai/text-embedding-ada-002 | 2022-12-15 | 未开始 | 0/11 | — |
| sentence-transformers/all-minilm-l12-v2 | 2021-08-30 | 未开始 | 0/11 | — |
| sentence-transformers/all-minilm-l6-v2 | 2021-08-30 | 未开始 | 0/11 | — |
| sentence-transformers/all-mpnet-base-v2 | 2021-08-30 | 未开始 | 0/11 | — |
| sentence-transformers/multi-qa-mpnet-base-dot-v1 | 2021-08-23 | 未开始 | 0/11 | — |
| sentence-transformers/paraphrase-minilm-l6-v2 | 2021-05-19 | 未开始 | 0/11 | — |
