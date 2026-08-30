# Module 3.10 — Data Leakage

## Capability
Detect information that makes validation unrealistically easy because it would be unavailable or contaminated at deployment.

Leakage sources:
- future values;
- target proxies/post-outcome fields;
- preprocessing before splitting;
- duplicated entities across splits;
- aggregates computed using future/test data;
- model selection repeatedly against the test set.

## Debugging challenge
You receive a model with 99.8% validation accuracy. Audit the data pipeline before celebrating. Find at least five leakage checks.

## Mastery
Suspiciously excellent scores trigger investigation, not LinkedIn posting. 😭
