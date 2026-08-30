# Module 2.3 — Numerical Pitfalls and Reproducibility

## Capability
Recognize that computer numbers are finite approximations and make experiments reproducible enough to debug.

Important ideas:
- floating-point numbers are approximate;
- equality comparisons can be fragile;
- overflow/underflow can happen;
- dtypes affect range, precision, and memory;
- random-number generators should be seeded for reproducible experiments where appropriate;
- reproducible code also depends on data/version/environment, not seed alone.

## Exercise
Show why `0.1 + 0.2 == 0.3` can surprise you in binary floating point. Then use a tolerance-based comparison.

Generate random data twice with and without a fixed seed and describe what reproducibility you gained—and what you did not.

## ML transfer
Later, numerical stability matters in probabilities, losses, gradients, and mixed precision.

## Mastery
You do not interpret tiny floating-point differences as proof that the algorithm is broken.
