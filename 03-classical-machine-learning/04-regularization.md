# Module 3.4 — Regularization

## Capability
Explain why constraining coefficient magnitude can improve generalization and distinguish L1/L2 intuition.

Regularization adds a complexity penalty to the training objective.
- L2 discourages large squared weights and tends to shrink smoothly.
- L1 can drive some coefficients to zero under common formulations.

Scale matters: coefficients on differently scaled features interact with penalties, so preprocessing must live inside the validated pipeline.

## Practice
Compare unregularized/ridge/lasso-style models across validation curves. Observe train vs validation behavior as penalty strength changes.

## Mastery
You treat regularization strength as a model-selection choice evaluated without leakage.
