# Module 04.7 — Optimizers & Update Dynamics

## Capability
Understand SGD, momentum and Adam well enough to diagnose optimization behavior.

## Mental model / core ideas
Optimizers transform gradients into parameter updates; learning rate and momentum/adaptive statistics change trajectory, not the objective itself.

## Practice
Implement SGD and momentum on a toy surface; compare with Adam qualitatively.

## Debugging / transfer task
Diagnose oscillation, divergence and slow progress from loss/gradient traces.

## Build evidence
Run controlled optimizer comparisons with fixed data/model/seed.

## Mastery check
Explain when changing optimizer hides a deeper problem and when it is justified.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
