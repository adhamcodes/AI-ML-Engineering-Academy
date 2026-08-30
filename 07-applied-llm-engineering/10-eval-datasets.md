# Module 07.10 — Evaluation Datasets

## Capability
Create representative test cases before optimizing the system.

## Mental model / core ideas
An eval set encodes expected tasks, edge cases, failure costs and sometimes reference evidence/answers. It should evolve from real failures.

## Practice
Design easy/hard/adversarial/abstention cases.

## Debugging / transfer task
Find a dataset that only tests happy-path phrasing.

## Build evidence
Version an eval dataset with metadata and expected behavior.

## Mastery check
The set can detect regressions meaningful to users.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
