# Module 04.12 — Normalization Layers

## Capability
Explain batch/layer normalization behavior and train/eval implications.

## Mental model / core ideas
Normalization transforms activations and may maintain statistics or normalize per example/features depending on method.

## Practice
Inspect BatchNorm statistics and compare train vs eval output; contrast with LayerNorm conceptually.

## Debugging / transfer task
Diagnose a validation bug caused by wrong mode or tiny-batch BatchNorm behavior.

## Build evidence
Add normalization to a model only after measuring a reason.

## Mastery check
Explain what is normalized, when statistics are learned, and failure cases.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
