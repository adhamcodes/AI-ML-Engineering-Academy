# Module 04.15 — Checkpointing & Reproducibility

## Capability
Resume experiments and reproduce important results.

## Mental model / core ideas
A useful checkpoint includes model state plus enough optimizer/config/randomness/data-version context to continue or audit the run.

## Practice
Save/load model and optimizer; record seeds/config/commit/data fingerprint.

## Debugging / transfer task
Recover from a checkpoint whose architecture/config no longer matches.

## Build evidence
Create a minimal experiment manifest + resume command.

## Mastery check
Another person can reproduce the run without guessing hidden settings.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
