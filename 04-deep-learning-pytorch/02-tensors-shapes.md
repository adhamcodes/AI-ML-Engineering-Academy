# Module 04.2 — Tensors, Shapes & Broadcasting

## Capability
Reason about batches/features/channels and catch shape errors before running code.

## Mental model / core ideas
Tensor shape is part of the interface. Batch dimensions, feature/channel dimensions and broadcasting rules determine which operations are meaningful.

## Practice
Trace shapes through matrix multiplies, activations and batch operations; intentionally create and repair shape errors.

## Debugging / transfer task
Diagnose a loss computation silently broadcasting the wrong target shape.

## Build evidence
Create a shape-contract notebook/script with assertions for a mini-model.

## Mastery check
You can infer shapes on paper and explain why an operation is valid.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
