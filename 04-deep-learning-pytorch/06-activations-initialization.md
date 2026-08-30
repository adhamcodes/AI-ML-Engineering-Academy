# Module 04.6 — Activations & Initialization

## Capability
Choose activations/initialization with awareness of signal and gradient flow.

## Mental model / core ideas
Activation and initialization affect the distribution of forward signals and backward gradients. Poor choices can saturate or explode/vanish.

## Practice
Compare ReLU-like and sigmoid/tanh behavior; measure activation/gradient statistics at initialization.

## Debugging / transfer task
Repair a deep MLP whose activations collapse or gradients vanish.

## Build evidence
Create an experiment comparing two initialization/activation pairs on the same task.

## Mastery check
Defend your choice using observed training behavior, not folklore.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
