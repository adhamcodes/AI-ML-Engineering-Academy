# Module 04.9 — Datasets, DataLoaders & Input Pipelines

## Capability
Build correct PyTorch input pipelines without leaking preprocessing state.

## Mental model / core ideas
Dataset defines samples; DataLoader batches/shuffles/loads them. Training-only fitted preprocessing must not learn from validation/test data.

## Practice
Create a custom Dataset and train/validation DataLoaders with deterministic splits.

## Debugging / transfer task
Find leakage caused by fitting normalization or vocabulary before splitting.

## Build evidence
Build a reusable tabular/image dataset pipeline with assertions.

## Mastery check
Explain shuffling, batching, workers and split boundaries.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
