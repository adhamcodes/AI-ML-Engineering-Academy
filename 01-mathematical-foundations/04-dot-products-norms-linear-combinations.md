# Module 1.4 — Dot Products, Norms, and Linear Combinations

## Capability
Compute and interpret dot products and vector magnitude, and understand a linear combination as weighted mixing.

## Dot product
For vectors of equal length:

`a·b = a1*b1 + a2*b2 + ...`

It turns two vectors into one scalar.

## ML meaning
A simple linear model often computes:

`score = w·x + b`

Each feature x is multiplied by a learned weight w, then combined.

Example:
`x=[2,3]`, `w=[0.5,-1]`

`w·x = 0.5*2 + (-1)*3 = -2`

The weights define how the model combines features.

## Norm
The Euclidean norm measures vector length:

`||x|| = sqrt(Σ x_i^2)`

Norms appear in distance, regularization, optimization, and similarity reasoning.

## Linear combination
`a*v1 + b*v2` is a weighted combination of vectors. Span/basis later build on this.

## Geometric intuition
The dot product also relates to alignment: vectors pointing similarly tend toward positive dot product; opposite directions tend negative; perpendicular vectors have dot product zero in Euclidean geometry.

## Practice
- Compute `[1,2,3]·[4,0,-1]`.
- Compute norm of `[3,4]`.
- Interpret `w·x+b` as a feature-scoring mechanism.
- Construct two different linear combinations of `[1,0]` and `[0,1]`.

## Mastery
You can explain why a dot product is useful in models, not just recite its formula.
