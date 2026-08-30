# Module 1.6 — Systems of Equations, Span, Basis, and Rank Intuition

## Capability
Understand why multiple equations can be represented as `Ax=b` and reason qualitatively about redundancy, reachable outputs, and independent directions.

## Systems as matrices
A system such as:

`2x + y = 5`
`x - y = 1`

can be represented by a coefficient matrix A, unknown vector x, and result vector b.

This connects algebra to linear transformations.

## Span
The span of a set of vectors is every vector reachable by their linear combinations.

If two 2D vectors point in exactly the same direction, they do not span the whole plane. They give only one independent direction.

## Basis
A basis is a minimal set of independent vectors that can represent every vector in the space.

## Rank intuition
Rank tells you how many independent directions/information dimensions a matrix effectively carries.

In data, highly redundant features can reduce effective dimensionality even if many columns exist.

## Practice
- Do `[1,0]` and `[0,1]` span the 2D plane? Explain.
- Do `[1,1]` and `[2,2]` provide two independent directions? Explain.
- What does it mean intuitively if a 10-column matrix has rank much less than 10?

## Mastery
You can reason about independence/redundancy geometrically without needing formal proof language yet.
