# Module 07.14 — Cost, Latency, Caching & Routing

## Capability
Treat model calls as operational resources.

## Mental model / core ideas
Token volume, model size, round trips, retrieval, retries and concurrency affect latency/cost. Cache stable work and route tasks based on measured need.

## Practice
Profile per-stage latency/token/cost; test prompt caching or local cache where applicable.

## Debugging / transfer task
Find retry storms or expensive oversized context.

## Build evidence
Create a cost/latency budget.

## Mastery check
You can explain quality-cost tradeoffs quantitatively.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
