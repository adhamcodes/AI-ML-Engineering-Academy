# Module 1.5 — Matrix Multiplication and Linear Transformations

## Capability
Compute small matrix products and understand a matrix as a transformation that maps one vector space to another.

## Two complementary views
### Arithmetic view
Matrix multiplication combines rows of the first matrix with columns of the second.

If `A` is `m×n` and `B` is `n×p`, then `AB` is `m×p`.

The inner dimensions must match.

### Transformation view
A matrix can represent a function that transforms a vector:

`y = A x`

This may stretch, rotate, project, mix, or otherwise transform coordinates.

That interpretation is crucial for neural networks: learned weight matrices transform representations layer by layer.

## Composition
Applying transformation B and then A corresponds to `A(Bx) = (AB)x`.

Order matters. In general, `AB != BA`.

## Practice
For
`A=[[1,2],[0,1]]` and `x=[3,4]`, compute `Ax`.

State whether these products are defined:
- `(3×4)(4×2)`
- `(3×4)(3×2)`

Explain the resulting shape for the valid case.

## Mastery
You can predict product shape before multiplying and describe matrix multiplication as composition of transformations.
