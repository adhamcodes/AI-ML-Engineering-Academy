# Module 3.18 — PCA and Dimensionality Reduction

## Capability
Understand PCA as finding orthogonal directions of high variance and use it without leaking validation data.

PCA connects Phase 1 linear algebra to data: covariance/eigen/SVD intuition becomes practical.

Uses:
- visualization;
- compression;
- denoising/preprocessing in some pipelines.

Caveats:
- components can be hard to interpret;
- high variance is not always predictive relevance;
- scaling matters;
- PCA must be fit only on training data inside pipeline.

## Practice
Apply PCA to standardized data, inspect explained variance, reconstruct approximately, and compare downstream model performance.

## Mastery
You can explain what information PCA preserves and what it may discard.
