# Module 07.9 — Hybrid Retrieval & Reranking

## Capability
Combine complementary retrieval signals and improve ordering.

## Mental model / core ideas
Lexical and semantic methods fail differently; candidate-generation plus reranking can improve precision at additional cost/latency.

## Practice
Compare BM25-like lexical, dense, hybrid and reranked results.

## Debugging / transfer task
Find a regression where reranker over-prioritizes semantically similar but wrong evidence.

## Build evidence
Build a pluggable retrieval pipeline.

## Mastery check
Justify added complexity with eval gains.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
