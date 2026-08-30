# Module 06.11 — Hugging Face Model Workflow

## Capability
Load, tokenize, run and evaluate open pretrained models while keeping abstraction transparent.

## Mental model / core ideas
Auto classes/config/tokenizers standardize model use but do not replace understanding of shapes, devices and objectives.

## Practice
Load a small model, inspect config/tokenizer, run inference and batch inputs.

## Debugging / transfer task
Repair device/padding/truncation/model-head mismatch.

## Build evidence
Create a reproducible open-model inference script.

## Mastery check
You can move below the pipeline abstraction when something breaks.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
