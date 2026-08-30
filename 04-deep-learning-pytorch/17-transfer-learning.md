# Module 04.17 — Transfer Learning

## Capability
Adapt pretrained representations without treating them as magic.

## Mental model / core ideas
Pretraining provides useful features/weights; fine-tuning strategy depends on dataset size, domain shift, compute and overfitting risk.

## Practice
Freeze/unfreeze layers on a small vision/text task and compare outcomes.

## Debugging / transfer task
Diagnose poor transfer caused by preprocessing mismatch or too-aggressive fine-tuning.

## Build evidence
Build a transfer-learning experiment with a from-scratch baseline.

## Mastery check
Explain why the pretrained model helps or does not help on your data.

**Rule:** if you can execute the recipe but cannot explain the failure modes or adapt it to a different dataset/system, keep practicing.
