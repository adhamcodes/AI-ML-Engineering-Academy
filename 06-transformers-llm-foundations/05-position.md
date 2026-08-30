# Module 06.5 — Positional Information & Causal Masking

## Capability
Explain how transformers represent order and enforce autoregressive visibility.

## Mental model / core ideas
Self-attention alone is permutation-insensitive; positional schemes inject order. Causal masks prevent future-token access during autoregressive prediction.

## Practice
Compare outputs with/without positional info in a toy setup; inspect a causal mask.

## Debugging / transfer task
Find future-token leakage from wrong mask.

## Build evidence
Create a mask visualization and shape test.

## Mastery check
Explain why training target shift and masking must align.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
