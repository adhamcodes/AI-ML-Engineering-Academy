# Module 1.7 — Eigenvalues, Eigenvectors, and Decomposition Intuition

## Capability
Understand the geometric idea of special directions preserved by a transformation and why decomposing matrices can reveal useful structure.

## Eigen idea
For a matrix A, an eigenvector v satisfies:

`A v = λ v`

After the transformation, v still points along the same line; it is scaled by eigenvalue λ (possibly reversing direction if negative).

Do not begin by memorizing determinant equations. Begin with the transformation picture.

## Why ML cares
Eigen concepts appear behind:
- PCA and dimensionality reduction;
- covariance structure;
- dynamical systems;
- optimization intuition.

## Decomposition idea
Matrix decompositions rewrite a complicated matrix as structured factors that expose geometry or make computation easier.

You only need intuition here for:
- eigendecomposition;
- singular value decomposition (SVD).

SVD is especially important because it applies broadly and underlies dimensionality reduction and low-rank approximation.

## Practice
Imagine a transformation that stretches the x-axis by 3 and y-axis by 0.5 without rotating. What are the obvious eigen-directions and scaling factors?

Explain why a low-rank approximation might be useful for compressing information.

## Depth boundary
You do not need a full proof of the spectral theorem or production numerical algorithms yet.

## Mastery
You can explain the equation `Av=λv` in geometry words and name one later ML use.
