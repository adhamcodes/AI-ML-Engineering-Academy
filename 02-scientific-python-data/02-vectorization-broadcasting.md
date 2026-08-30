# Module 2.2 — Vectorization and Broadcasting

## Capability
Replace unnecessary Python loops with array operations and reason about broadcasting rather than guessing until shapes work.

Vectorization expresses an operation over arrays. NumPy often executes these operations in optimized compiled code.

Broadcasting lets compatible shapes interact without explicitly copying a smaller array across a larger one.

Example: subtract a feature-mean vector of shape `(features,)` from a data matrix `(rows, features)` to center every column.

## Broadcasting reasoning
Compare dimensions from the end. Dimensions are compatible when equal or one of them is 1 (under NumPy broadcasting rules).

## Practice
Given `X` shape `(100,5)` and `mean` shape `(5,)`, predict `X-mean` shape and meaning.

Given `(100,5)` and `(100,)`, do not guess—reason about alignment and test intentionally.

## Common mistake
Broadcasting can make wrong code run successfully. Shape compatibility does not prove semantic correctness.

## Mastery
You can explain both performance and correctness reasons for vectorization/broadcasting.
