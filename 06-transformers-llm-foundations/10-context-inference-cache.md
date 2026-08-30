# Module 06.10 — Context, Inference & KV Cache

## Capability
Understand inference cost drivers and why context length matters.

## Mental model / core ideas
Autoregressive decoding repeatedly attends to prior tokens; KV caching reuses earlier key/value states to avoid recomputation. Context length affects memory/latency and attention behavior.

## Practice
Estimate token/context costs and inspect cached generation conceptually.

## Debugging / transfer task
Diagnose latency caused by oversized prompts/repeated context.

## Build evidence
Profile generation under varying prompt/output lengths.

## Mastery check
Explain prefill vs decode qualitatively.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
