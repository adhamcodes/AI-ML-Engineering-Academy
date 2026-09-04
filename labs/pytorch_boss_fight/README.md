# Broken PyTorch Training Boss Fight

This directory now contains the actual broken training project promised by Phase 4.

Install `torch`, then run `broken_train.py` and inspect the behavior before editing anything.

Symptoms are intentionally more useful than answers:

- validation behavior is suspicious,
- repeated runs are not trustworthy,
- the optimization loop has at least one state-management defect,
- the evaluation path does not fully behave like evaluation,
- the reported evidence is insufficient to prove generalization.

Copy `broken_train.py` to your own project and repair it. Your final report must identify root causes, not just present a lower loss.

Use `evaluator.py solution.py` for the minimum interface/determinism gate. Passing it is necessary, not sufficient; you still need split, training-loop, and evaluation reasoning.
