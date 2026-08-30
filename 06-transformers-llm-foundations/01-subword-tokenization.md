# Module 06.1 — Subword Tokenization

## Capability
Explain why text is split into model-specific token units and how tokenization affects cost/behavior.

## Mental model / core ideas
Tokenizers map text to integer IDs from a finite vocabulary. Subword schemes balance vocabulary size, unknown words and sequence length.

## Practice
Inspect tokenization across words, code, numbers and multiple languages.

## Debugging / transfer task
Diagnose a context/cost estimate made from character count rather than tokens.

## Build evidence
Build a tokenizer-analysis notebook using an open tokenizer.

## Mastery check
Explain why token boundaries are model artifacts, not linguistic truth.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
